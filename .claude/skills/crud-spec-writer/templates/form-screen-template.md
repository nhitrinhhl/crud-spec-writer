# Form / Detail Screen Template

Mirrors SRS section 4 "Create Case Screen" (Screen 2) and "Case Detail Screen" (Screen 3).
Used for Create (new mode), Update (edit mode) and Read (view mode) screens.
Replace every `<...>`. Delete guidance lines (starting with `>`) in the output.

---

### <Create / Edit / View> <Object> Screen

- This screen allows <Actor> to <create a new / edit an existing / view details of a> <Object>.
- <Actor> can access this screen by:
  - Step 1: Log in the system.
  - Step 2: <Click on "<Button>" on <<cross reference to <Screen> screen>>. | Click on one of <Objects> in <Object> List screen.>

*Screen <n>: <Object> <Form/Details> screen*

| # | Component | Comp. Type | Editable | Mandatory | Default Value | Description |
|---|---|---|---|---|---|---|
| 1 | <Code> | Label | N/A | N/A | N/A | Retrieve [<Code>] from the corresponding <Object>.<br>Auto-generated on creation, refer to BR <n>. |
| 2 | <Name> | Single Line of Text | Yes | Yes | N/A | User inputs <Name> of <Object>.<br>Max Length: <n> characters.<br>When user leaves this field blank and moves out of it, the system displays IEM 1 Please input in this field. |
| 3 | <Lookup> | Dropdown list | Yes | Yes | N/A | Value list: Retrieve all [<Name>] in "<Related Object>" that qualifies [Status] is "Active".<br>Sorting: Alphabetic order. |
| 4 | <Notes> | Multi lines of text | Yes | No | N/A | User inputs <Notes>.<br>Max Length: <n> characters. |
| 5 | <Status> | Label | N/A | N/A | "Active" | Retrieve [Status] from the corresponding <Object>. |
| 6 | Save | Button | N/A | N/A | N/A | This button allows user to save <Object>.<br>Refer to UC <n>: <name>. |
| 7 | Cancel | Button | N/A | N/A | N/A | This button allows user to cancel the action.<br><Refer to BR <n> (CFD 4) when user has changed any field.> |

> - Comp. Type values used in the SRS: Label, Single Line of Text, Multi lines of text,
>   Dropdown list, Button, Toolbar. Add Date Picker, Checkbox, Radio Button, Number, Email,
>   Phone when needed.
> - View mode: every field is Label, Editable = N/A, Mandatory = N/A; action buttons state
>   their enable/visibility conditions ("Enable when: [Status] of the corresponding <Object>
>   is "Active". [Role] of current user is "<Role>".").
> - Edit mode: fields that cannot change after creation are Label (read-only) — state why.
