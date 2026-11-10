# crud-spec-writer

A Claude Code skill that writes CRUD use case specifications (View list, Create, View detail,
Edit, Delete/Disable) in English, following the company SRS template section 3.3
"Common Use Cases".

## Requirements
- Claude Code
- The **superpowers** plugin (mandatory):
  ```
  /plugin install superpowers@claude-plugins-official
  ```
  Opening this folder in Claude Code also prompts you to enable it (`.claude/settings.json`).
- Optional, for reading private GitHub repos: GitHub CLI logged in (`gh auth login`).

## Install
Use it in this folder, or copy the skill to your user skills to use it everywhere:
```
cp -R .claude/skills/crud-spec-writer ~/.claude/skills/
```

## Use
Input options:
1. **Give everything in the prompt** – the skill writes right away after you approve a summary.
2. **Give a GitHub link** – the skill reads the code (read-only) and asks only about the gaps.
3. **Give just the object and function** – the skill interviews you one question at a time.

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
Add "just write it" to skip the questions (neutral defaults + `[TBC]`).

Writing rules: English only (spec, questions and replies) and active voice only
(`scripts/check_active_voice.py` checks it).

Output: a Word file in `~/Downloads` (`<Project>_<Object>_Use-Case-Specification.docx`), built on your
company SRS template (`*System*Requirement*Specification*.docx`, kept local, never committed), plus the
Markdown source `specs/<object>-<function>.md`. Both contain UC header table, Activity Flows (table; Mermaid in the .md only),
Business Rules, screen descriptions, New Messages and Open Questions.
Numbering always starts at UC 1 / BR 1 / Screen 1.

## Structure
```
.claude/
├── settings.json                    # enables superpowers plugin
└── skills/crud-spec-writer/
    ├── SKILL.md                     # workflow
    ├── templates/                   # use case, listing screen, form screen
    ├── references/                  # SRS conventions, input modes, one file per function
    └── examples/product-view-list.md
specs/customer-view-list.md          # sample output
```
