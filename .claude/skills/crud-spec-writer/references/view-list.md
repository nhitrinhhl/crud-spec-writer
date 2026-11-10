# View List — Reference

Base: SRS CMUC 1 "View list of Items", UC 7 "View List of existing Products", Case List Screen.
This is the PRIMARY reference: all other functions should reach this level of detail.
Full worked example: `examples/product-view-list.md`.

## Output = UC + Listing Screen
1. `UC <n>: View List of existing <Objects>` — use-case-template.md
2. `<Object> List Screen` — listing-screen-template.md

## Header
| Row | Pattern |
|---|---|
| Objective | This use case allows user to view list of existing <Objects>. |
| Actor | <Roles as given by the user> |
| Trigger | User clicks on "<Menu Item>" in the left Navigation Pane. |
| Pre-condition | User logged in successfully as actor above. |
| Post-condition | The system displays the list of existing <Objects>. |

## Standard Activity Flows
| Step | User | System |
|---|---|---|
| (1) | User clicks on "<Menu Item>" in the left Navigation Pane. | |
| (2) | | The system loads <Object> List screen with the records that satisfy the Data Source conditions, sorted by Default Sorting. |
| (2.1) | | If no record satisfies the conditions, the system displays the empty state text. |
| (3) | User views the list. User may search, sort, change page, open an item (UC <n>: View an existing <Object>) or click on an action button (e.g. UC <n>: Create <Object>). | |

## Standard Business Rules
| Step | Rule |
|---|---|
| (2) | **Screen Displaying Rules:** The system will load screen: <<cross reference to <Object> List screen>>.<br>- The system retrieves data as described in Data Source of the screen.<br>- <Per-role visibility, one line per role>.<br>- The system sorts records as described in Default Sorting of the screen. |
| (2.1) | (you may merge this into the BR above) If there is no record to display, the table displays the text "<No <Object> found.>". |
| (3) | Optional **Screen Displaying Rules** for action visibility: The system displays "<Button>" button only when {Current Login User} has role "<Role>". |

## Checklist (cover each item or mark N/A)
- [ ] Objective / Actor / Trigger / Pre-condition / Post-condition
- [ ] Access steps: Step 1 log in, Step 2 menu path in Navigation Pane
- [ ] Data Source conditions — object, filters (e.g. exclude "Closed"), per-role visibility (e.g. own records only, Active-only for non-admins)
- [ ] Default Sorting — field + ascending/descending
- [ ] Every column: Component Type "Column Header", source field `Retrieve from [<Field>] of corresponding <Object>.`
- [ ] Display mapping for coded values (status, type, flags); date/number format
- [ ] Link to detail screen on the identifying column (`Link to item: <Object> details screen of this <Field>.`)
- [ ] Action buttons with visibility per role and `Refer to UC <n>: <name>.`
- [ ] Row-level actions (Edit / Delete icons) if any — visibility per status/role
- [ ] Search: "Refer to Search Component." + deviations (searched columns, min characters, exact match)
- [ ] Filters: value list, default value, logic, combination with search (AND)
- [ ] Pagination: "Refer to Pagination." or deviation (page size)
- [ ] View Columns Display: refer, or deviation (default sorted column icon)
- [ ] Bulk Action: refer (Export/Delete) or "N/A"
- [ ] Empty state text
- [ ] BR "Screen Displaying Rules: The system will load screen: <<cross reference to <Object> List screen>>."

## Questions to ask if missing (plain words, about the user's app)
1. Which menu item opens this list?
2. Do all actors see the same records, or does some role see only part of them? Are inactive / closed / deleted records shown?
3. Does any column show a different label than the stored value (e.g. a status shown as another word)?
4. Which buttons are on the screen (Create, Export, Delete, row actions), and who can use them?

If not answered, use the neutral defaults in `srs-conventions.md` §11.
