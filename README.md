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
Viết spec xem danh sách và thêm mới Supplier. Actor: Admin, Purchasing Staff. Menu "Suppliers".
Cột: Supplier Code (link chi tiết), Supplier Name, Phone, Email, Status, Last Modified At.
Sort Supplier Code giảm dần. Thêm mới: Supplier Name (bắt buộc, max 100, không trùng), ...
```
```
/crud-spec-writer
Viết spec đầy đủ CRUD cho Supplier, code ở https://github.com/<org>/<repo>
```
```
viết spec xóa Supplier
```
Add "cứ viết đi" to skip the questions (neutral defaults + `[TBC]`).

Output: `specs/<object>-<function>.md` with UC header table, Activity Flows (table + Mermaid),
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
