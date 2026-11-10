# crud-spec-writer

A Claude Code skill for Business Analysts. It writes CRUD use case specifications (View list,
Create, View detail, Edit, Delete/Disable) for any object of any app, in the format of the
company SRS template, section 3.3 "Common Use Cases", and delivers them as a Word file.

- **Two input modes:** it reads the app's source code from a GitHub link (read-only), or it
  interviews you one question at a time.
- **SRS format:** UC header table, Activity Flows, Business Rules with BR codes, screen
  descriptions, IEM/EMSG/CFD/SCD message codes and the CBR1 audit trail rule.
- **Word output:** a `.docx` in `~/Downloads`, built on your SRS template.
- **Writing rules:** English only, active voice only, numbering from UC 1 / BR 1 / Screen 1.

## Requirements
- Claude Code.
- The **superpowers** plugin (mandatory). The skill stops if you have not installed it.
  ```
  /plugin install superpowers@claude-plugins-official
  ```
  When you open this folder in Claude Code, `.claude/settings.json` also prompts you to enable it.
- Python 3 (standard library only) for the two scripts.
- Your company SRS template, a `*System*Requirement*Specification*.docx`, in the working folder
  or in `~/Downloads`. This repo does not contain it, because it is company-internal. Keep it local.
- Optional: the GitHub CLI, logged in (`gh auth login`), to read private repositories.

## Install
Use the skill inside this folder, or copy it to your user skills to use it in every project:
```
cp -R .claude/skills/crud-spec-writer ~/.claude/skills/
```

## How it works
1. **Identify:** the skill reads the object, the functions and the actors from your request.
2. **Collect input** in one of two modes:
   - **Mode A, source code:** you give a GitHub link or a local path. The skill clones it
     read-only, reads the models, migrations, validation, enums, permissions and UI code, and
     builds a Source Findings table with a `file:line` source for every fact. It asks you only
     about what the code does not show.
   - **Mode B, interview:** the skill uses `superpowers:brainstorming` and asks one plain
     question per message about your app.
3. **Approve the Input Summary:** the skill plays back what it found or heard and writes
   nothing until you approve it. If you say "just write it", it uses neutral defaults and
   marks each assumption `[TBC]`.
4. **Write:** the skill fills the templates and follows the function references, in the SRS
   heading structure, and saves the Markdown source to `specs/<object>-<function>.md`.
5. **Export to Word:** `scripts/md_to_srs_docx.py` keeps the template's styles, heading
   numbering, header and footer, and replaces only the body.
6. **Verify:** the skill runs `superpowers:verification-before-completion` with the function
   checklists, the common SRS checklist, `scripts/check_active_voice.py` and, in Mode A, a
   check that every fact has a `file:line` source.

## Use
Examples:
```
/crud-spec-writer
Write the View list and Create spec for Supplier. Actors: Admin, Purchasing Staff. Menu "Suppliers".
Columns: Supplier Code (link to details), Supplier Name, Phone, Email, Status, Last Modified At.
Sort by Supplier Code descending. Create: Supplier Name (mandatory, max 100, unique), ...
```
```
/crud-spec-writer
Write the full CRUD spec for Supplier, code at https://github.com/<org>/<repo>
```
```
write the delete spec for Supplier
```
Add "just write it" to skip the questions. For simple lookup data, ask for the short
**"Manage <Object>"** form: it refers to the Common Use Cases instead of repeating them.

You may write to the skill in another language (e.g. Vietnamese). It always answers and
writes in English.

## Output
- **Word file:** `~/Downloads/<Project>_<Object>_Use-Case-Specification.docx`
- **Markdown source:** `specs/<object>-<function>.md`

Both files contain:
- **Use Case Specifications:** for each UC, the header table (Objective, Actor, Trigger,
  Pre-condition, Post-condition), Activity Flows and Business Rules.
- **Mockups Screen:** the list, form and detail screen descriptions.
- **Appendices:** New Messages, Source Analysis (Mode A only) and Open Questions (every `[TBC]`).

Both files show the Activity Flows as a step table. The Markdown file also has a Mermaid
diagram; the Word file does not, so draw the swimlane from the table if you need one.

## Writing rules
- **English only** for the spec, the questions and the replies.
- **Active voice only:** "The system creates a new Task.", never "A new Task is created."
  UI and message texts copied from the app keep their exact wording.
- **The SRS template gives the format, not the facts.** The skill never takes roles, menus,
  fields or rules from its sample content (Case, Product, Customer Portal). Where you give no
  answer, it uses a neutral default.
- **The spec refers to standard behaviour instead of repeating it:** Pagination, Search
  Component, View Columns Display and Bulk Action.

## Scripts
Both scripts use only the Python 3 standard library.

| Script | Purpose |
|---|---|
| `scripts/md_to_srs_docx.py <spec.md> <srs-template.docx> <output.docx>` | Converts a spec to Word on the SRS template |
| `scripts/check_active_voice.py <file.md> …` | Flags passive sentences and exits with code 1 when it finds any. A heuristic: it skips quoted UI text and message texts |

## Structure
```
.claude/
├── settings.json                        # enables the superpowers plugin
└── skills/crud-spec-writer/
    ├── SKILL.md                         # workflow and rules
    ├── templates/
    │   ├── use-case-template.md         # UC header, Activity Flows, Business Rules
    │   ├── listing-screen-template.md   # list screen description
    │   └── form-screen-template.md      # create / edit / detail screen description
    ├── references/
    │   ├── srs-conventions.md           # notation, message codes, CBR1, defaults, checklist
    │   ├── input-github.md              # Mode A: source code analysis
    │   ├── input-interview.md           # Mode B: interview and Input Summary
    │   └── view-list.md, create.md, read.md, update.md, delete.md
    ├── examples/product-view-list.md    # reference level of detail
    └── scripts/
        ├── md_to_srs_docx.py            # Markdown to .docx on the SRS template
        └── check_active_voice.py        # passive voice check
specs/customer-view-list.md              # sample output
```
