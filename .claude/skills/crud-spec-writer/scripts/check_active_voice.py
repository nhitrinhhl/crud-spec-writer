#!/usr/bin/env python3
"""Flag passive-voice sentences in a spec (heuristic).

Usage:
    python3 check_active_voice.py <file.md> [<file.md> ...]

Prints "file:line: <match> | <line excerpt>" for every likely passive construction
(a form of "be"/"get" followed by a past participle, optionally with an adverb between).
Exit code 1 when anything is found, 0 when clean.

Not flagged: code spans, Mermaid blocks, guidance lines ("> ..."), text in double quotes and
message texts after a code (IEM/EMSG/CFD/SCD n ...) — UI copy is quoted verbatim from the app —
and the exceptions below, which are adjectives or fixed SRS labels rather than passive verbs.
Standard library only.
"""
import re
import sys

BE = r'(?:is|are|was|were|be|been|being|get|gets|got|gotten)'
IRREGULAR = (
    'shown|done|made|given|taken|seen|sent|kept|set|hidden|written|chosen|known|held|put|read|'
    'built|found|left|lost|run|begun|drawn|thrown|told|paid|meant|bound|brought|caught|cut|'
    'forbidden|forgotten|gone|hung|laid|led|shut|spent|split|struck|undone|won|broken'
)
PASSIVE = re.compile(
    rf'\b{BE}\s+(?:(?:not|also|only|still|then|always|never|already|automatically|successfully|'
    rf'immediately|\w+ly)\s+)*((?:\w+ed)|(?:{IRREGULAR}))\b(?!-)',
    re.IGNORECASE,
)
# Participles used as adjectives / states, and fixed SRS terms, that are not passive voice.
ALLOWED = {
    'required', 'logged', 'interested', 'supported', 'concerned', 'related', 'based', 'limited',
    'expected', 'allowed', 'needed', 'used', 'focused', 'involved', 'unsorted', 'red', 'need',
    'feed', 'speed', 'seed', 'bed', 'shed', 'hundred', 'kindred',
}
# "User logged in successfully as actor above." is the fixed SRS pre-condition.
SKIP_LINE = re.compile(r'logged in successfully as actor above', re.IGNORECASE)


def check(path):
    hits = 0
    in_code = False
    with open(path, encoding='utf8') as f:
        for n, line in enumerate(f, 1):
            s = line.strip()
            if s.startswith('```'):
                in_code = not in_code
                continue
            if in_code or s.startswith('>') or SKIP_LINE.search(s):
                continue
            text = re.sub(r'`[^`]*`', '', line)
            text = re.sub(r'"[^"]*"|“[^”]*”', '""', text)
            # message code followed by its text, inline or in the next table cell
            text = re.sub(r'\b(?:IEM|EMSG|CFD|SCD) (?:\d+|n|<n>)\s*\|[^|]*\|', '|', text)
            text = re.sub(r'\b(?:IEM|EMSG|CFD|SCD) (?:\d+|n|<n>) [^.?|]*[.?]', '', text)
            for m in PASSIVE.finditer(text):
                if m.group(1).lower() in ALLOWED:
                    continue
                hits += 1
                print(f'{path}:{n}: "{m.group(0)}" | {s[:140]}')
    return hits


def main(paths):
    total = sum(check(p) for p in paths)
    print(f'{total} possible passive sentence(s).' if total else 'No passive voice found.')
    return 1 if total else 0


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1:]))
