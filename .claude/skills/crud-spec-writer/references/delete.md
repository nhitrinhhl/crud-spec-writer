# Delete / Disable — Reference

Base: SRS CMUC 5 "Delete Item", UC 8 "Disable an existing Product".
Note: UC 8 BR 18 cites the wrong message (CFD 3) and a broken reference — do not copy.

## Delete vs Disable — decide first
| | Delete | Disable |
|---|---|---|
| Effect | Record removed (Recycle Bin / soft-delete flag / permanent) | [Status] → "Inactive"; record kept and still viewable |
| Typical for | Drafts, records never referenced | Master data referenced by other records (Product, Customer) |
| Title | UC <n>: Delete an existing <Object> | UC <n>: Disable an existing <Object> |
| Rule type | **Deleting Rules:** | **Disabling Rules:** |

The delete type MUST be stated explicitly — CMUC 5 leaves three options open
("move to the Recycle Bin / flag the document as deleted / delete the item permanently").
If the user has not said, ask; if they say proceed, use "flag as deleted (soft delete) [TBC]".

## Header
| Row | Pattern |
|---|---|
| Objective | This use case allows user to <delete/disable> an existing <Object>. |
| Actor | <Roles> |
| Trigger | User clicks on "<Delete/Disable>" button on <<cross reference to <Object> Details screen>>. |
| Pre-condition | User logged in successfully as actor above.<br>[Status] of the <Object> is "<Status>". |
| Post-condition | The selected <Object> is <deleted/disabled> successfully. |

## Standard Activity Flows
| Step | User | System |
|---|---|---|
| (1) | User clicks on "<Delete/Disable>" button. | |
| (2) | | The system shows confirmation dialog CFD n. |
| (3) | User clicks on "OK" or "Cancel". | |
| (4) | | If "OK": the system <deletes/disables> the <Object>, updates related records, displays SCD n and loads <Object> List screen. |
| (4.1) | | If "Cancel": the system closes the dialog and does nothing. |

## Standard Business Rules
| Step | Rule |
|---|---|
| (2) | **Confirmation Rules:** The system shows a confirmation message CFD 5 Are you sure you want to delete this item? with two buttons "OK" and "Cancel". (Disable: new code, e.g. CFD n Are you sure you want to disable this <Object>?)<br>- If User clicks on "OK", go to BR <n+1>.<br>- If User clicks on "Cancel", the system closes the confirmation dialog and does nothing. |
| (4) | **Deleting Rules:** If user clicks on the "OK" button from the confirmation dialog, the system will:<br>- <Move the selected <Object> to the Recycle Bin. \| Update [Is Deleted] of the selected <Object> to "Yes"; the record is no longer displayed in any screen. \| Delete the selected <Object> permanently.><br>- <Impact on related records, e.g. update [Status] of all open <Related Object> related to this <Object> to "Closed" (open = [Status] is not "Closed").><br>- Save all changes.<br>- Refer to CBR1 to log basic audit trail.<br>- The system will display success dialog SCD n The <Object> has been deleted.<br>- The system will load screen: <<cross reference to <Object> List screen>>. |
| (4) | **Disabling Rules:** (Disable variant) If user clicks on the "OK" button from the confirmation dialog, the system will:<br>- Update [Status] of the current <Object> to "Inactive".<br>- <Impact on related records>.<br>- Save all changes.<br>- Refer to CBR1 to log basic audit trail.<br>- The system will load screen: <<cross reference to <Object> List screen>>. |
| (2) | Optional **Validating Rules:** before confirmation — if the <Object> is referenced by <Related Object> with <condition>, display error message EMSG n <text> and stop. |

## Checklist (cover each item or mark N/A)
- [ ] Delete or Disable decided (and why)
- [ ] Trigger: detail screen button, list row action, and/or Bulk Action
- [ ] Pre-condition: status / role
- [ ] Blocking validation: referenced by other records → EMSG, or N/A
- [ ] Confirmation: CFD 5 (delete) or new CFD (disable), "OK"/"Cancel", both branches
- [ ] Delete type stated: Recycle Bin / soft-delete flag / permanent
- [ ] Impact on related records (close/disable/detach) or N/A
- [ ] CBR1
- [ ] Redirect + success message
- [ ] Pagination after delete on the last page (Refer to Pagination) or N/A
- [ ] Re-enable / restore path (Enable UC, restore from Recycle Bin) or N/A

## Questions to ask if missing
1. Delete or disable? If delete: Recycle Bin, soft-delete flag, or permanent?
2. What happens to related records?
3. Can it be deleted when referenced? If not, which error message?
