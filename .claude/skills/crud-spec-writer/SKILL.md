---
name: crud-spec-writer
description: Write CRUD use case specifications (View list, Create, View detail/Read, Update/Edit, Delete/Disable) for any module or object, in English, following the company SRS template section 3.3 "Common Use Cases" (UC header table, Activity Flows, Business Rules with BR codes, listing/form screen descriptions, IEM/CFD/SCD message codes, CBR1 audit trail). Input either by analysing source code from a GitHub link / local path, or by a guided interview (requires the superpowers plugin). Use when a BA asks to write, draft or review a use case or spec for viewing a list, creating, viewing details, editing, deleting or disabling an object, or a "Manage <Object>" section. Vietnamese triggers - "viết spec", "viết use case", "đặc tả", "xem danh sách", "danh sách", "thêm mới", "tạo mới", "xem chi tiết", "sửa", "chỉnh sửa", "cập nhật", "xóa", "vô hiệu hóa".
---

# CRUD Spec Writer

Writes CRUD use case specifications that drop straight into the company SRS
("<Customer Name>_<Project Name>_System Requirement Specification"), section 3 "Use Case
Specifications", in the format of section 3.3 "Common Use Cases" (CMUC 1–5).

**Language:** the user may write in Vietnamese or English. The spec output is ALWAYS English,
in the SRS's formal style ("The system will…", "User clicks on…"). Conversation (questions,
summaries) follows the user's language.

## Prerequisite — superpowers plugin (mandatory)
Before anything else, check that the skills `superpowers:brainstorming` and
`superpowers:verification-before-completion` are in your available skills list.
If either is missing, STOP and tell the user (in their language):

> This skill requires the superpowers plugin. Install it in Claude Code with
> `/plugin install superpowers@claude-plugins-official`, restart the session, then ask again.

Do not continue without it.

## Files

| File | Load when |
|---|---|
| `references/srs-conventions.md` | Always |
| `references/input-github.md` | Input Mode A (GitHub link / local source path) |
| `references/input-interview.md` | Input Mode B (interview), and for gaps after Mode A |
| `references/view-list.md` | View list of <Objects> |
| `references/create.md` | Create <Object> |
| `references/read.md` | View an existing <Object> (detail) |
| `references/update.md` | Edit / Update <Object> |
| `references/delete.md` | Delete or Disable <Object> |
| `templates/use-case-template.md` | Every UC |
| `templates/listing-screen-template.md` | View list (screen description) |
| `templates/form-screen-template.md` | Create / Read / Update screen description, if fields are known |
| `examples/product-view-list.md` | Reference level of detail; read before the first View list spec |

## The SRS is a format template, not a source of facts
This skill is used for many different apps. The SRS docx shows the FORMAT only; its content
(Case, Product, Solution, Customer Portal, Support Engineer, System Admin, its site map) is
sample data. Never take roles, menus, fields, statuses or rules from it. Use only what the
user or the user's source code gave. When something is unknown, use the **neutral default**
in `srs-conventions.md` §11 — never invent an app-specific rule.

## Workflow

### 1. Identify
From the request: object name (singular + plural), function(s), actor(s) if stated.
One request may cover several functions → one UC per function, in this order:
Create, Edit, View detail, View list, Delete/Disable.

### 2. Choose the input mode
- The request contains a GitHub URL or a local source path → **Mode A**.
- The request already gives everything required (see table below) → skip to step 4.
- Otherwise ask ONE question (user's language), e.g.
  "Do you have the source code on GitHub I can read, or shall I ask you a few questions?"
  - Link given → **Mode A** (`references/input-github.md`), then Mode B for the gaps only.
  - No code → **Mode B** (`references/input-interview.md`).

Required input to end up with:
- Object; actor(s) per function; entry point (menu, or button + screen).
- Fields/columns: name, type, mandatory, rules (max length, format, unique, value list).
- View list: which records are shown (incl. per-role visibility), default sorting, columns,
  buttons and who can use them.
- Delete: delete type (Recycle Bin / soft delete / permanent).

Never ask about numbering, pagination, search, column display or CBR1 — they are standard.

### 3. Approve the Input Summary
Play back the Input Summary (format in `input-interview.md`; with the Source Findings table
in Mode A). Write the spec only after the user approves it or says to proceed.
If the user opts out of questions ("cứ viết đi"), use the neutral defaults in
`srs-conventions.md` §11 and mark `[TBC]` only where no neutral default exists
(menu name, delete type, default status).

### 4. Load references
`references/srs-conventions.md` + the matching function reference(s).

### 5. Write
- Fill `templates/use-case-template.md` for each UC: header table → Activity Flows (step
  table + Mermaid) → Business Rules.
- View list: also fill `templates/listing-screen-template.md`.
- Create/Edit/View detail with known fields: also fill `templates/form-screen-template.md`.
- Number UCs, BRs and screens from 1, sequentially within the spec.
- A UC that is not written in this spec is referred to by name only: "Refer to UC: Create <Object>."
- Add a **New Messages** table if any new message code was introduced.
- Mode A: add the **Source Analysis** section (`input-github.md`).
- Save to `specs/<object>-<function>.md` (kebab-case) in the working directory unless the
  user names another location, and show the result in chat.

### 6. Verify, then close
Invoke `superpowers:verification-before-completion`. The "verification" for a spec is:
- the function checklist in each loaded reference — every item covered or explicitly `N/A`;
- the common checklist in `srs-conventions.md` §9;
- Mode A: every value taken from code has a file:line source.
Report what you checked and anything that failed; do not say "done" before this.
End the spec with **Open Questions**: every `[TBC]`, with the assumed value and the question.
If there are none, write "None."

## Short form: "Manage <Object>"
When the object needs only standard behaviour (typical for master data / lookup lists),
offer the short form instead of five full UCs. It refers to Common Use Cases (CMUC 1–5)
and lists only object-specific rules. Format: `references/srs-conventions.md` §8.

## Do not
- Do not translate the spec into Vietnamese or mix languages in the spec.
- Do not repeat the standard Pagination / Search Component / View Columns Display /
  Bulk Action text — write "Refer to <section name>." and spell out deviations only.
- Do not copy the known defects of the SRS template (`srs-conventions.md` §10).
- Do not invent field names, roles, statuses, value lists or per-role rules.
- Do not copy names or rules from the SRS sample content (Case, Product, Customer Portal…).
- Do not run, build or modify the user's source code (Mode A is read-only).
