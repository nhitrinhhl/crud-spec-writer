# Update (Edit) — Reference

Base: SRS CMUC 4 "Update Item", UC 5 "Edit Product".
Note: CMUC 4 in the template says "new mode" and "create a new item" — these are template
defects; use "edit mode" and "update the current item".

## Output
1. `UC <n>: Edit <Object>` — use-case-template.md
2. `Edit <Object> Screen` — form-screen-template.md in edit mode (when fields are known)

## Header
| Row | Pattern |
|---|---|
| Objective | This use case allows user to edit an existing <Object>. |
| Actor | <Roles> |
| Trigger | User clicks on "Edit" button on <<cross reference to <Object> Details screen>>. |
| Pre-condition | User logged in successfully as actor above.<br>[Status] of the <Object> is "<Status>". |
| Post-condition | <Object> is updated successfully. |

## Standard Activity Flows
| Step | User | System |
|---|---|---|
| (1) | User clicks on "Edit" button. | |
| (2) | | The system loads Edit <Object> screen at the edit mode with the current data. |
| (3) | User changes data and clicks on "Save" button. | |
| (4) | | The system validates the inputted data. |
| (4.1) | | If validation fails, the system displays inline error messages; go back to step (3). |
| (4.2) | | If validation passes, the system saves the changes, displays SCD n and loads <Object> Details screen. |
| (5) | User clicks on "Cancel" button (alternative at step (3)). | |
| (6) | | If there are unsaved changes, the system displays CFD 4; otherwise loads <Object> Details screen. |

## Standard Business Rules
| Step | Rule |
|---|---|
| (2) | **Screen Displaying Rules:** The system will load screen: <<cross reference to Edit <Object> screen>> at the edit mode.<br>- All fields are populated with the current data of the <Object>.<br>- Read-only fields: [<Code>], [<Field>] (<reason>).<br>- Editable fields: as stated in screen description. |
| (4)<br>(4.1) | **Validating Rules:** After user clicks on "Save" button, the system will validate all the mandatory fields as stated in screen description.<br>- If any mandatory field is left blank, under the corresponding field, display inline error message IEM 1 Please input in this field.<br>- <Format rules>.<br>- If [<Name>] already exists in another "<Object>" record (excluding the current one), display inline error message IEM 2 This name is already existed.<br>- Otherwise, go to step (4.2). |
| (4.2) | **Updating Rules:** After passing the validation rules, the system will update the current <Object> as below:<br>- Save all changes.<br>- Refer to CBR1 to log basic audit trail.<br>- The system will display success dialog SCD n The <Object> has been updated.<br>- The system will load screen: <<cross reference to <Object> Details screen>>. |
| (6) | **Confirmation Rules:** If user has changed any field, the system shows a confirmation message CFD 4 Are you sure you want to cancel?<br>- If User clicks on "Yes", discard the changes and load <<cross reference to <Object> Details screen>>.<br>- If User clicks on "No", close the dialog and stay on the current screen. |

## Checklist (cover each item or mark N/A)
- [ ] Trigger button + screen (detail screen and/or row action on list)
- [ ] Pre-condition on status (which statuses allow editing) and role
- [ ] Editable vs read-only fields (code, created fields, fields locked by status)
- [ ] Validating: mandatory (IEM 1), format, uniqueness excluding current record, conditional rules
- [ ] Updating: save changes, status change if any, impact on related records
- [ ] Updating: CBR1
- [ ] Redirect + SCD message
- [ ] Cancel with unsaved changes → CFD 4
- [ ] Concurrent edit (record changed by another user) → EMSG or N/A

## Questions to ask if missing
1. In which statuses can the object be edited, and by whom?
2. Which fields become read-only after creation?
3. After saving: go to details or list?
