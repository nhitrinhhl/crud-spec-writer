# SRS Conventions

Source: "<Customer Name>_<Project Name>_System Requirement Specification" v0.9 —
§1.4 Abbreviations, §3.3 Common Use Cases, §3.4 Common Business Rules, §6 Other Requirements,
§9 Appendices (Messages List).

## 1. Document placement

| Section | Content |
|---|---|
| 3.1 / 3.2 | Use cases per portal (e.g. Customer Portal, Internal Portal), grouped as Workflow Use Case / Manage Use Case / Other Use Case / Scheduled Job |
| 3.3 Common Use Cases | CMUC 1 View list of Items, CMUC 2 Create Item, CMUC 3 Read Item, CMUC 4 Update Item, CMUC 5 Delete Item |
| 3.4 Common Business Rules | CBR1 Logging Basic Audit Trail Rule |
| 4 Mockups Screen | Screen descriptions ("Screen n: <Name> screen") |
| 6 Other Requirements | Common field controls, Common Messages Configuration, View Columns Display, Pagination, Search Component, Bulk Action |
| 9.1 Messages List | Error Message (EMSG), Inline Error Message (IEM), Confirmation Dialog (CFD), Success Dialog (SCD) |

CRUD specs for a specific object go under "Manage Use Case" (UC n), and refer to CMUC
behaviour where the object does not change it.

## 2. Notation

| Notation | Meaning | Example |
|---|---|---|
| `[Field Name]` | Data field | [Product Code] |
| `"Text Value"` | A value, or a UI label (button, menu, status) | "Active", "Save" |
| `{Runtime Value}` | Value resolved at runtime (used in BRs) | {Current Login User}, {Current User Name}, {Current Date Time}, {Selected Product} |
| `<Value>` | Special value (Abbreviations table form) | <Today>, <Current User> |
| `<<cross reference to <Screen Name>>>` | Link to a screen description | <<cross reference to Product List screen>> |
| `<<Field>>` | Field value inside an Email Template only | <<Case ID>> |
| `(n)` / `(n.m)` | Activity step / sub-step | (4), (4.1) |
| `BR n` | Business rule — numbered across the whole SRS | BR 17 |
| `UC n: <Name>` | Use case reference | UC 4: Create Product |
| `CMUC n` | Common use case | CMUC 2: Create Item |
| `CBR n` | Common business rule | CBR1 |
| `ET n` | Email template | ET 1: Sending email to Customer after submitting Case |
| `[TBC]` | Assumed value awaiting confirmation (this skill) | |

Prefer `{Current Login User}` in BRs (as in CBR1).

## 3. Numbering

Every spec starts at 1 — do not ask for or continue from other numbers.
- **UC**: UC 1, UC 2, … in the order the UCs appear in the spec.
- **BR**: BR 1, BR 2, … continuing across all UCs of the same spec (not restarted per UC).
- **Screen**: "Screen 1: <Name> screen", "Screen 2: …", sequential within the spec.
- **Steps**: (1), (2), … restart per UC; branches as (4.1), (4.2). A BR row may cite several steps: `(4)<br>(4.1)`.
- **Reference to a UC outside the spec**: by name only — "Refer to UC: Create <Object>."
- **Message codes**: reuse the standard codes in §4; new codes continue after them.

## 4. Message codes

Always cite **code + text**, without quotes: `display inline error message IEM 1 Please input in this field.`

### Existing codes (SRS §9.1)

| Type | Display (SRS §6 / §9.1) | Code | Message |
|---|---|---|---|
| Inline Error Message | Red text under the field; field highlighted red | IEM 1 | Please input in this field. |
| | | IEM 2 | This name is already existed. |
| | | IEM 3 | You must specify a unique value for this field. |
| Error Message | Pop-up, title "Error Message", button "OK"/"Close"; clicking outside does not close it | EMSG 1 | You must specify a value for this required field. |
| | | EMSG 2 | The import file must be XLS file. |
| | | EMSG 3 | The data format of import file is not correct. |
| | | EMSG 4 | Are you sure, you want to send the item(s) to the site Recycle Bin? |
| | | EMSG 5 | You have approved leave request successfully. |
| Confirmation Dialog | Title "Confirmation", buttons Yes/OK – No/Cancel; clicking outside does not close it | CFD 1 | Are you sure you want to submit Case? |
| | | CFD 2 | Are you sure you want to submit Solution? |
| | | CFD 3 | Are you sure you want to accept Solution? |
| | | CFD 4 | Are you sure you want to cancel? |
| | | CFD 5 | Are you sure you want to delete this item? |
| Success Dialog | Title "Success Dialog", button "OK", closes automatically after 5s | SCD 1 | A new User Profile has been created. |
| | | SCD 2 | The User Profile has been updated. |
| | | SCD 3–5 | (project-specific samples) |

### New codes
- Next free codes in the template: **IEM 4, EMSG 6, CFD 6, SCD 6** — or continue from the numbers the user gives.
- Patterns: `SCD n You have created the <Object>.` / `SCD n You have updated the <Object>.` /
  `SCD n You have deleted the <Object>.` (active voice) / `CFD n Are you sure you want to disable this <Object>?`
- Reuse an existing code when the text fits (IEM 1 for blank mandatory, CFD 4 for cancel, CFD 5 for delete).
- List every new code in a **New Messages** table at the end of the spec (Type | Code | Message).
- Note: §6 "Common Messages Configuration" says the Informing Message closes after 10s, §9.1 says the Success Dialog closes after 5s. Use **SCD, 5s**.

## 5. Business Rule wording

Description cell = underlined bold rule type + line break + rule lines.

| Rule type | Opening line (use verbatim) |
|---|---|
| **Screen Displaying Rules:** | The system will load screen: <<cross reference to <Screen> screen>>. (add "at the new mode" / "at the view mode" / "at the edit mode" for form screens) |
| **Validating Rules:** | After user clicks on "Save" button, the system will validate all the mandatory fields as stated in screen description. |
| **Creating Rules:** | After passing the validation rules, the system will create a new <Object> as below: |
| **Updating Rules:** | After passing the validation rules, the system will update the current <Object> as below: |
| **Confirmation Rules:** | The system shows a confirmation message CFD n <text> with two buttons "OK" and "Cancel". |
| **Deleting Rules:** | If user clicks on the "OK" button from the confirmation dialog, the system will … |
| **Disabling Rules:** | If user clicks on the "OK" button from the confirmation dialog, the system will update [Status] of the current <Object> to "Inactive". |

Phrasing rules:
- "The system will …", "User clicks on "<Button>"…", "If …, display … Otherwise, go to step (n)."
- Branches name their target: `If User clicks on "No", go to BR n.` / `go to step (3).`
- End data-changing rules with: `Save all changes.` → `Refer to CBR1 to log basic audit trail.` → navigation line → message line.
- Auto-generated code: `[<Code>] is generated as this format: <Prefix>XX where XX is auto increasing number.` (e.g. PXX), or the long form `[Case ID] = "CA" + xxxxx` with a legend for each part.
- Status-dependent display: one condition per line.

## 6. Common rules

**CBR1 Logging Basic Audit Trail Rule** (SRS §3.4)
- When the system creates the record: update [Created by] to [User ID] of {Current Login User}; update [Created at] to current date time.
- When the system creates or updates the record: update [Last modified by] to [User ID] of {Current Login User}; update [Last modified at] to current date time.

Every Create / Update / Delete / Disable BR must contain: `Refer to CBR1 to log basic audit trail.`
Optional workflow audit line (when the object keeps an [Audit Trail]): `Append to [Audit Trail] as: <Action> by {Current User Name} at {Current Date Time}.`

## 7. Standard behaviour (SRS §6 "Other Requirements") — refer, don't repeat

Unless the user states otherwise, listing screens follow these sections. Write
"Refer to <section name>." and spell out **deviations only**.

| Section | Summary (for your understanding — do not paste into the spec) |
|---|---|
| View Columns Display | The system cuts text longer than the cell with "…" and shows a tooltip with full content; headers unsorted by default; unsorted/ascending/descending icons |
| Pagination | New search or page-size change → refresh, back to page 1; "<<" "<" disabled on page 1, ">>" ">" disabled on last page; 1 page still shows pagination; total records shown on the left; user can type the page number |
| Search Component | Free text; "contain" logic across all presented columns; refresh table + pagination; blank keyword → reset to default view |
| Bulk Action | First column is a checkbox; header checkbox selects current page only; selection kept across pages; Dropdown (Bulk Action / Export / Delete) or buttons (Delete / Export) enabled when ≥1 row selected |
| Common field controls | Refer to dev team's component library |

Date/time display: write the format only if the user gave one. Otherwise write
"Date time format: Refer to Common field controls." (the format differs per project).

## 8. "Manage <Object>" short form (SRS: Manage Line of Business)

Use when the object only needs standard CMUC behaviour.

```
#### Manage <Object>
- **Objective**: This use case is used the common functions (Create, View, Update, Delete) to manage data.
- **Actor**: <Role 1>, <Role 2>.
- **Common behavior and business rules**: Refer to Common Use Cases for more details of common behavior and business rules, when creating, viewing, updating, deleting in this object.
- **Business Rules**:
  - Besides of business rules described in Common Use Cases, following rules are required for this object.
  - Creating new item Rules:
    - Validation rules:
      - <e.g. [Name] must be unique. If duplicated, display IEM 2 This name is already existed.>
  - Updating Rules:
    - Validation rules: <list, or "Same as Creating new item Rules.">
  - Deleting rules:
    - <e.g. Cannot delete if referenced by any active <Related Object>; display EMSG n …>
    - <Delete type: Recycle Bin / soft-delete flag / permanent>
- **Screens**:
  - For listing screen: Refer to <<cross reference to <Object> List screen>>.
  - For creation screen: Refer to <<cross reference to Create <Object> screen>>.
  - For viewing screen: Refer to <<cross reference to <Object> Details screen>>.
  - For updating screen: Refer to <<cross reference to Edit <Object> screen>>.
```

## 9. Common self-check (run on every spec)

- [ ] Output is English only; formal SRS phrasing.
- [ ] Every sentence is in active voice (`scripts/check_active_voice.py` reports nothing).
- [ ] Header table has all 5 rows: Objective, Actor, Trigger, Pre-condition, Post-condition.
- [ ] Trigger names a quoted UI label and a screen cross reference (or menu path).
- [ ] Pre-condition starts with "User logged in successfully as actor above."
- [ ] A BR cites every Activity step that has system behaviour; every BR cites an existing step.
- [ ] Step table and Mermaid flowchart match (same steps, same branches).
- [ ] Each BR Description starts with an underlined bold rule type.
- [ ] The spec cites every message as code + text; the New Messages table lists every new code.
- [ ] Every data-changing BR says "Refer to CBR1 to log basic audit trail."
- [ ] Every BR that ends the flow says which screen loads next.
- [ ] The spec refers to standard behaviour by section name and does not repeat it.
- [ ] UC / BR / Screen numbers start at 1 and are sequential within the spec.
- [ ] The spec takes no role, field, status, value list or rule from the SRS sample content and invents none.
- [ ] The spec marks every assumption `[TBC]` and lists it in Open Questions.

## 10. Known defects in the SRS template — do NOT copy

| Location | Defect | Correct form |
|---|---|---|
| UC 1 Pre-condition | "Use logged in successfully…" | "User logged in successfully…" |
| UC 3 BR 8 | Cites CFD 2 (submit Solution) for Accept | Use the matching message (CFD 3) |
| UC 5 BR 15 | Step (4) repeated for Updating | Updating is step (5) / (4.2) |
| UC 8 BR 18 | Cites CFD 3 (accept Solution) for Disable; broken "Error! Reference source not found." | New CFD "Are you sure you want to disable this <Object>?" and a valid BR reference |
| CMUC 4 BR 27 | "load the corresponding screen at the new mode" | "…at the edit mode" |
| CMUC 4 BR 29 | Updating rule says "create a new item" | "update the current item" |
| Case List Screen | Search Bar's Component Type holds a column description; Case ID row has no Component Type; "New Case" refers to UC 2 | Component Type "Search Bar" / "Column Header"; refer to the correct UC |
| Section labels | Mix of "Activities Flow" and "Activity Flows"; "Pre-condition:" and "Pre-conditions" | Use **Activity Flows** and **Pre-condition:** (as in §3.3) |

## 11. Neutral defaults (when the user gave no answer)

Use these instead of inventing app-specific rules. They are valid spec text, not `[TBC]`.

| Missing input | Neutral default |
|---|---|
| Per-role visibility | All actors of the UC see the same records: `Retrieve all "<Object>" records.` |
| Data Source conditions | No condition (all records). If the object has a [Status] the user mentioned, still show all statuses. |
| Status / type display mapping | Show the stored value: `Retrieve from [<Field>] of corresponding <Object>.` (no "display as" mapping) |
| Value lists (Dropdown) | `Value list: Retrieve all [<Name>] in "<Related Object>".` — no listed values |
| Action button visibility | `Display only for the actors of UC: <Verb> <Object>.` + `Refer to UC: <Verb> <Object>.` |
| Bulk Action | `N/A – this screen has no bulk action.` |
| Empty state | `If there is no record to display, the table displays the text "No data found."` |
| Date / number format | `Refer to Common field controls.` |
| Mockup | `Mockup: The BA will attach the mockup.` |
| Delete type | Ask the user — no neutral default (`[TBC]`). |
| Entry point (menu name) | Ask the user — use `"<Objects>"` in the left Navigation Pane + `[TBC]`. |
| Default status on create | Ask the user if the object has a status; otherwise N/A. |
