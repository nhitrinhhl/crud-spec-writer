#!/usr/bin/env python3
"""Convert a crud-spec-writer Markdown spec into a .docx that uses the company SRS template.

Usage:
    python3 md_to_srs_docx.py <spec.md> <srs-template.docx> <output.docx>

The template supplies styles, numbering, page setup, header and footer. Its body is replaced by
the spec. Styles used (all present in the SRS template): Heading1-4, SRSBullet, Caption, Strong.

Markdown handled (the subset the skill writes):
  # .. ####            -> Heading1 .. Heading4 (auto-numbered by the template)
  | table |            -> SRS table (grey header row; key/value tables get a grey first column)
  **Label** (alone)    -> dark-blue bold label ("Activity Flows", "Business Rules", ...)
  *Caption* (alone)    -> Caption style ("Screen 1: ...")
  - item / "  - item"  -> SRSBullet level 1 / 2
  in cells: <br> = new paragraph, "- " = bullet, "&nbsp;&nbsp;- " = level-2 bullet,
            <u>**X:**</u> = rule type (Strong + underline), **x** = bold, `x` = plain
  ```mermaid blocks, "---" rules and "> " guidance lines are skipped.
Standard library only.
"""
import re
import shutil
import sys
import tempfile
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape

TEXT_WIDTH = None  # set from the template's sectPr
GREY = '<w:shd w:val="clear" w:color="auto" w:fill="D9D9D9"/>'
BORDERS = ''.join(
    f'<w:{side} w:val="single" w:sz="{sz}" w:space="0" w:color="BFBFBF"/>'
    for side, sz in (('top', 12), ('left', 12), ('bottom', 12), ('right', 12), ('insideH', 8), ('insideV', 8))
)
LABEL_RPR = '<w:b/><w:color w:val="1F3864"/><w:szCs w:val="22"/>'

# Column weights by header text (first match wins); otherwise weighted by text length.
KNOWN_WIDTHS = {
    ('step', 'br code', 'description'): [8, 9, 83],
    ('step', 'user', 'system'): [8, 46, 46],
    ('#', 'component', 'component type', 'description'): [4, 18, 14, 64],
    ('#', 'component', 'comp. type', 'editable', 'mandatory', 'default value', 'description'): [4, 14, 12, 8, 10, 12, 40],
    ('type', 'code', 'message'): [20, 10, 70],
    ('item', 'value', 'source (file:line)', 'confidence'): [34, 22, 34, 10],
}


def esc(t):
    return escape(t, {'"': '&quot;'})


def runs(text, base_rpr=''):
    """Inline markdown -> w:r elements."""
    out = []
    pos = 0
    pattern = re.compile(r'<u>\*\*(.+?)\*\*</u>|\*\*(.+?)\*\*|`([^`]+)`')
    for m in pattern.finditer(text):
        if m.start() > pos:
            out.append(run(text[pos:m.start()], base_rpr))
        if m.group(1) is not None:
            out.append(run(m.group(1), '<w:rStyle w:val="Strong"/>' + base_rpr + '<w:u w:val="single"/>'))
        elif m.group(2) is not None:
            out.append(run(m.group(2), base_rpr + '<w:b/>'))
        else:
            out.append(run(m.group(3), base_rpr))
        pos = m.end()
    if pos < len(text):
        out.append(run(text[pos:], base_rpr))
    return ''.join(out)


def run(t, rpr=''):
    t = t.replace('&nbsp;', ' ').replace('&lt;', '<').replace('&gt;', '>')
    rp = f'<w:rPr>{rpr}</w:rPr>' if rpr else ''
    return f'<w:r>{rp}<w:t xml:space="preserve">{esc(t)}</w:t></w:r>'


def para(text, style=None, level=None, rpr='', jc=None):
    ppr = ''
    if style:
        ppr += f'<w:pStyle w:val="{style}"/>'
    if level:
        ppr += f'<w:numPr><w:ilvl w:val="{level}"/><w:numId w:val="27"/></w:numPr>'
    if jc:
        ppr += f'<w:jc w:val="{jc}"/>'
    return f'<w:p><w:pPr>{ppr}</w:pPr>{runs(text, rpr)}</w:p>'


def cell_paras(text, rpr=''):
    parts = [p for p in re.split(r'<br\s*/?>', text)]
    out = []
    for p in parts:
        raw = p
        nested = raw.startswith('&nbsp;')
        stripped = raw.replace('&nbsp;', '').strip()
        if stripped.startswith('- '):
            out.append(para(stripped[2:], 'SRSBullet', level=1 if nested else None, rpr=rpr))
        else:
            out.append(para(stripped, rpr=rpr))
    return ''.join(out) or '<w:p/>'


def split_row(line):
    line = line.strip()
    if line.startswith('|'):
        line = line[1:]
    if line.endswith('|'):
        line = line[:-1]
    cells, cur, in_code = [], '', False
    for ch in line:
        if ch == '`':
            in_code = not in_code
        if ch == '|' and not in_code:
            cells.append(cur.strip())
            cur = ''
        else:
            cur += ch
    cells.append(cur.strip())
    return cells


def widths(header, rows, n):
    key = tuple(re.sub(r'<[^>]+>|\*', '', h).strip().lower() for h in header)
    weights = KNOWN_WIDTHS.get(key)
    if not weights:
        if n == 2:
            weights = [22, 78]
        else:
            lens = [max(len(re.sub(r'<[^>]+>|\*', '', r[i])) if i < len(r) else 0 for r in [header] + rows) for i in range(n)]
            weights = [min(max(l, 6), 60) for l in lens]
    total = sum(weights)
    w = [int(TEXT_WIDTH * x / total) for x in weights]
    w[-1] += TEXT_WIDTH - sum(w)
    return w


def table(lines):
    rows = [split_row(l) for l in lines if not re.match(r'^\|\s*:?-{3,}', l.strip())]
    n = max(len(r) for r in rows)
    rows = [r + [''] * (n - len(r)) for r in rows]
    first = re.sub(r'\*', '', rows[0][0]).strip()
    key_value = n == 2 and first.endswith(':') or first in ('Data Source', 'Default Sorting')
    header = rows[0]
    w = widths(header, rows[1:], n)
    grid = ''.join(f'<w:gridCol w:w="{x}"/>' for x in w)
    xml = [f'<w:tbl><w:tblPr><w:tblW w:w="{TEXT_WIDTH}" w:type="dxa"/><w:tblBorders>{BORDERS}</w:tblBorders>'
           f'<w:tblLayout w:type="fixed"/><w:tblLook w:val="04A0" w:firstRow="1" w:lastRow="0" w:firstColumn="1" '
           f'w:lastColumn="0" w:noHBand="0" w:noVBand="1"/></w:tblPr><w:tblGrid>{grid}</w:tblGrid>']
    for ri, r in enumerate(rows):
        is_header = ri == 0 and not key_value
        trpr = '<w:trPr><w:tblHeader/></w:trPr>' if is_header else ''
        xml.append(f'<w:tr>{trpr}')
        for ci, c in enumerate(r):
            shade = GREY if is_header or (key_value and ci == 0) else ''
            rpr = '<w:b/>' if is_header else ''
            text = re.sub(r'^\*\*(.*)\*\*$', r'\1', c) if (is_header or (key_value and ci == 0)) else c
            if key_value and ci == 0:
                rpr = '<w:b/>'
            xml.append(f'<w:tc><w:tcPr><w:tcW w:w="{w[ci]}" w:type="dxa"/>{shade}</w:tcPr>{cell_paras(text, rpr)}</w:tc>')
        xml.append('</w:tr>')
    xml.append('</w:tbl>')
    return ''.join(xml) + '<w:p/>'


def convert(md):
    out = []
    lines = md.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        s = line.strip()
        if s.startswith('```'):
            i += 1
            while i < len(lines) and not lines[i].strip().startswith('```'):
                i += 1
            i += 1
            continue
        if s.startswith('|'):
            block = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                block.append(lines[i])
                i += 1
            out.append(table(block))
            continue
        i += 1
        if not s or s == '---' or s.startswith('>'):
            continue
        m = re.match(r'^(#{1,4})\s+(.*)$', s)
        if m:
            out.append(para(m.group(2), f'Heading{len(m.group(1))}'))
            continue
        if re.fullmatch(r'\*\*[^*]+\*\*', s):
            out.append(para(s[2:-2], rpr=LABEL_RPR))
            continue
        if re.fullmatch(r'\*[^*]+\*', s):
            out.append(para(s[1:-1], 'Caption'))
            continue
        lm = re.match(r'^(\s*)- (.*)$', line)
        if lm:
            out.append(para(lm.group(2), 'SRSBullet', level=1 if len(lm.group(1)) >= 2 else None))
            continue
        out.append(para(s))
    return ''.join(out)


def main(md_path, template, output):
    global TEXT_WIDTH
    md = Path(md_path).read_text(encoding='utf8')
    tmp = Path(tempfile.mkdtemp())
    try:
        with zipfile.ZipFile(template) as z:
            z.extractall(tmp)
        for p in tmp.rglob('*'):
            if p.is_symlink():
                p.unlink()
        doc_path = tmp / 'word' / 'document.xml'
        doc = doc_path.read_text(encoding='utf8')
        sect = doc[doc.rindex('<w:sectPr'):doc.rindex('</w:body>')]
        pw = int(re.search(r'<w:pgSz w:w="(\d+)"', sect).group(1))
        ml = int(re.search(r'w:left="(\d+)"', sect).group(1))
        mr = int(re.search(r'w:right="(\d+)"', sect).group(1))
        TEXT_WIDTH = pw - ml - mr
        sect = sect.replace('<w:titlePg/>', '')  # no cover page: use the normal header on page 1
        head = doc[:doc.index('<w:body>') + len('<w:body>')]
        doc_path.write_text(head + convert(md) + sect + '</w:body></w:document>', encoding='utf8')
        out = Path(output)
        out.parent.mkdir(parents=True, exist_ok=True)
        if out.exists():
            out.unlink()
        with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as z:
            names = sorted(p for p in tmp.rglob('*') if p.is_file())
            ct = tmp / '[Content_Types].xml'
            z.write(ct, '[Content_Types].xml')
            for p in names:
                if p != ct:
                    z.write(p, p.relative_to(tmp).as_posix())
        print(out)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == '__main__':
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    main(*sys.argv[1:])
