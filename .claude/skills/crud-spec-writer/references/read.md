# Read (View detail) — Reference

Base: SRS CMUC 3 "Read Item", UC 6 "View an existing Product", Case Detail Screen.

## Output
1. `UC <n>: View an existing <Object>` — use-case-template.md
2. `<Object> Details Screen` — form-screen-template.md in view mode (all Label)

## Header
| Row | Pattern |
|---|---|
| Objective | This use case allows user to view the details of a <Object>. |
| Actor | <Roles> (or "All authenticated users.") |
| Trigger | User selects to open an existing <Object> on <<cross reference to <Object> List screen>>. |
| Pre-condition | User logged in successfully as actor above.<br>(+ visibility condition, e.g. "The <Object> is visible to the user as described in Data Source of <Object> List screen.") |
| Post-condition | The system displays the details of the selected <Object>. |

## Standard Activity Flows
| Step | User | System |
|---|---|---|
| (1) | User clicks on [<Code>] of a <Object> on <Object> List screen. | |
| (2) | | The system loads <Object> Details screen of {Selected <Object>} at the view mode. |
| (3) | User views the details. User may click on an available action button (Edit / Delete / Disable). | |

## Standard Business Rules
| Step | Rule |
|---|---|
| (2) | **Screen Displaying Rules:** The system will load screen: <<cross reference to <Object> Details screen>> of {Selected <Object>} at the view mode.<br>- The system shows all fields as read-only.<br>- The system displays "<Edit>" button only when {Current Login User} has role "<Role>" and [Status] of the <Object> is "<Status>".<br>- The system displays "<Delete/Disable>" button only when … |

## Checklist (cover each item or mark N/A)
- [ ] Trigger: open item from list (which column/link), and any other entry point (deep link, related screen)
- [ ] Screen Displaying (view mode) with {Selected <Object>}
- [ ] Field list with source and format (date, currency, mapping)
- [ ] Related lists/tabs on the detail screen (e.g. Solutions of a Case) or N/A
- [ ] Action buttons and their visibility/enable conditions per role AND per status
- [ ] Access to an item the user is not allowed to see (e.g. direct URL) → EMSG or N/A
- [ ] Navigation back (breadcrumb / Back button)

## Questions to ask if missing
1. Which actions appear on the detail screen, for which roles and statuses?
2. Any related lists or tabs?
3. Fields shown that are not on the create form (audit fields, computed values)?
