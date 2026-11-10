# Create — Reference

Base: SRS CMUC 2 "Create Item", UC 4 "Create Product", Create Case Screen.

## Output
1. `UC <n>: Create <Object>` — use-case-template.md
2. `Create <Object> Screen` — form-screen-template.md (when fields are known)

## Header
| Row | Pattern |
|---|---|
| Objective | This use case allows user to create a new <Object>. |
| Actor | <Roles> |
| Trigger | User clicks on "Create" button on <<cross reference to <Object> List screen>>. |
| Pre-condition | User logged in successfully as actor above. |
| Post-condition | A new <Object> is successfully created. |

## Standard Activity Flows
| Step | User | System |
|---|---|---|
| (1) | User clicks on "Create" button. | |
| (2) | | The system loads Create <Object> screen at the new mode. |
| (3) | User inputs data and clicks on "Save" button. | |
| (4) | | The system validates the inputted data. |
| (4.1) | | If validation fails, the system displays inline error messages; go back to step (3). |
| (4.2) | | If validation passes, the system creates the <Object>, displays SCD n and loads <Object> List screen. |
| (5) | User clicks on "Cancel" button (alternative at step (3)). | |
| (6) | | The system displays CFD 4 if there are unsaved changes; otherwise loads the previous screen. |

Steps (5)–(6) are optional — include them if Cancel behaviour must be specified.

## Standard Business Rules
| Step | Rule |
|---|---|
| (2) | **Screen Displaying Rules:** The system will load screen: <<cross reference to Create <Object> screen>> at the new mode.<br>- Default values: <field = value>. |
| (4)<br>(4.1) | **Validating Rules:** After user clicks on "Save" button, the system will validate all the mandatory fields as stated in screen description.<br>- If any mandatory field is left blank, under the corresponding field, display inline error message IEM 1 Please input in this field.<br>- If [<Field>] is not in the format <format>, display inline error message IEM n Invalid <Field> format.<br>- If [<Name>] already exists in "<Object>", display inline error message IEM 2 This name is already existed. (or IEM 3 You must specify a unique value for this field.)<br>- If [<Field A>] is "<Value>", [<Field B>] is mandatory.<br>- Otherwise, go to step (4.2). |
| (4.2) | **Creating Rules:** After passing the validation rules, the system will create a new <Object> as below:<br>- Save all inputted data.<br>- [<Code>] is generated as this format: <Prefix>XX where XX is auto increasing number.<br>- Update [Status] as "<Default Status>".<br>- Save all changes.<br>- Refer to CBR1 to log basic audit trail.<br>- The system will display success dialog SCD n A new <Object> has been created.<br>- The system will load screen: <<cross reference to <Object> List screen>>. |
| (6) | **Confirmation Rules:** If user has changed any field, the system shows a confirmation message CFD 4 Are you sure you want to cancel?<br>- If User clicks on "Yes", discard the inputted data and load the previous screen.<br>- If User clicks on "No", close the dialog and stay on the current screen. |

## Checklist (cover each item or mark N/A)
- [ ] Trigger button + screen
- [ ] Screen Displaying (new mode), default values
- [ ] Validating: mandatory → IEM 1
- [ ] Validating: format (email, phone, number, date, max length)
- [ ] Validating: uniqueness → IEM 2 / IEM 3 (state which field(s), case-sensitive or not)
- [ ] Validating: conditional mandatory / cross-field rules
- [ ] Creating: save inputted data
- [ ] Creating: auto-generated code format (e.g. PXX) or N/A
- [ ] Creating: default status
- [ ] Creating: CBR1
- [ ] Creating: redirect screen + SCD message (new code → New Messages)
- [ ] Side effects: emails (ET n), related records, or N/A
- [ ] Cancel behaviour (CFD 4) or N/A

## Questions to ask if missing
1. Fields: type, mandatory, max length, format, unique?
2. Is there an auto-generated code? Format?
3. Default status on creation?
4. After saving: go to list or to the new item's details? Success message?
