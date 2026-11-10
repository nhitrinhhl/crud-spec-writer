# Listing Screen Template

Mirrors SRS section 4 "Mockups Screen" → "Case List Screen" (Screen 1).
Replace every `<...>`. Delete guidance lines (starting with `>`) in the output.

---

### <Object> List Screen

- This screen allows <Actor(s)> to view list of existing <Objects>.
- <Actor(s)> can access this screen by:
  - Step 1: Log in the system.
  - Step 2: Click on module "<Menu Item>" in Navigation Pane in the left.

*Screen <n>: <Object> List screen*
> Mockup/image goes here in Word. If no mockup was provided, write: `Mockup: [TBC]`.

| **Data Source** | Retrieve all "<Object>" records satisfying:<br>- <Condition 1, e.g. [Status] is not "Closed".><br>- <Per-role condition, e.g. If {Current Login User} has role "<Role>": [Owner] is [User ID] of {Current Login User}.> |
|---|---|
| **Default Sorting** | The system sorts records by [<Field>] in <ascending/descending> order. |

> - Data Source must state per-role visibility when roles see different records.
> - If the user gave no conditions, write `Retrieve all "<Object>" records.` (neutral default, srs-conventions.md §11).

| # | Component | Component Type | Description |
|---|---|---|---|
| 1 | <Create> | Button | This button allows <Actor> to create a new <Object>.<br>Display only when {Current Login User} has role "<Role>".<br>Refer to UC <n>: Create <Object>. (or "Refer to UC: Create <Object>." if that UC is not in this spec) |
| 2 | Search Bar | Search Bar | Refer to Search Component. |
| 3 | <Filter> | Dropdown | Value list: <values / source>.<br>Default value: "<All>".<br><Filtering logic>. |
| 4 | Checkbox | Checkbox | Refer to Bulk Action. |
| 5 | <Code Field> | Column Header | Retrieve from [<Code Field>] of corresponding <Object>.<br>Link to item: <Object> details screen of this <Code Field>. |
| 6 | <Field> | Column Header | Retrieve from [<Field>] of corresponding <Object>. |
| 7 | <Status> | Column Header | Retrieve from [Status] of corresponding <Object>, display as:<br>- "<X>" if [Status] is "<A>" or "<B>".<br>- "<Y>" if [Status] is "<C>".<br>- Otherwise, display as "<Z>". |
| 8 | <Date Field> | Column Header | Retrieve from [<Date Field>] of corresponding <Object>.<br>Date time format: <format given by the user, or "Refer to Common field controls."> |
| 9 | Pagination | Pagination | Refer to Pagination. |

> Component Type values: Button, Search Bar, Column Header, Link, Checkbox, Dropdown, Pagination.
> Patterns (use verbatim):
> - Column:  `Retrieve from [<Field>] of corresponding <Object>.`
> - Mapping: `display as: - "X" if [Status] is "A" or "B". Otherwise, display as "Y".`
> - Link:    `Link to item: <Object> details screen of this <Field>.`
> - Button:  `This button allows <actor> to <action>. Refer to UC <n>: <name>.`
> - Lookup:  `Retrieve from [<Name Field>] of "<Related Object>" that has [<ID>] is [<FK>] of corresponding <Object>.`
> Remove rows that do not apply (no filter → no Dropdown row; no bulk action → no Checkbox row).

**Other display rules**
- View columns display: Refer to View Columns Display.
- Pagination: Refer to Pagination.
- Search: Refer to Search Component. <Deviation, e.g. "Search applies to columns <A>, <B> only.">
- Bulk Action: <Refer to Bulk Action. | N/A – this screen has no bulk action.>
- Empty state: If no record satisfies the Data Source conditions (or the search keyword), the table displays the text "<No data found.>".
