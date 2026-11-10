# Input Mode B — Interview (superpowers:brainstorming)

Use when the user has no source code to share, or after Mode A for what the code cannot show.

## How to run it
1. Invoke the Skill `superpowers:brainstorming` and follow its conversation rules:
   - one question per message, a single plain sentence, in the user's language;
   - open questions first; offer a short menu only when the user is stuck or asks for options;
   - when the user says "just guess" / "cứ đoán", propose a concrete value and say it is your guess;
   - play back each part in a short chunk as soon as it is understood, marking guesses.
2. **Overrides — this skill wins over brainstorming on these points:**
   - Skip "Size the Work", "The Written Design", the builder check, the `docs/superpowers/specs/`
     location and the hand-off to `superpowers:writing-plans`.
   - The "full description" that needs approval is the **Input Summary** below, not a design document.
   - After approval, return to SKILL.md step 4 (write the spec). Nothing else is built.
   - If the user opts out of questions, use the neutral defaults in `srs-conventions.md` §11.
3. Skip anything already known (from the request, from Mode A, or from earlier answers).
4. Never ask about numbering, pagination, search, column display or CBR1 — those are standard.

## Ground to cover (territory, not a script — never read it out as a list)

| Topic | Needed for | What you must end up knowing |
|---|---|---|
| Object | all | Name (singular/plural), what it represents in the app |
| Functions | all | Which of View list / Create / View detail / Edit / Delete / Disable |
| Actors | all | Who does each function (may differ per function) |
| Entry point | all | Menu item, or button + screen that opens each function |
| Records shown | View list | Do all actors see the same records? Hidden statuses? |
| Default sorting | View list | Field + ascending/descending |
| Columns | View list | Order, which one links to the detail screen, any label different from the stored value |
| Buttons & filters | View list / detail | Which buttons, who can use them, in which status |
| Fields | Create / Edit / detail | Type, mandatory, max length, format, unique, value list, default |
| Auto code & default status | Create | Code format (e.g. SUPxx), status on creation |
| Editable after creation | Edit | Fields locked after creation or in some statuses |
| Delete type | Delete | Recycle Bin / hidden (soft delete) / permanent; effect on related records; blocked when referenced? |
| After saving | Create / Edit / Delete | Which screen opens next; success message wanted? |
| Special rules | any | Anything the app does differently from the standard |

Good question shapes (adapt to the object, never use sample-data names):
- "Walk me through how someone opens the <Objects> list today — which menu do they click?"
- "Does everyone who opens this list see the same <Objects>, or does someone see only part of them?"
- "When a <Object> is deleted, what should happen to it — gone for good, or recoverable?"

## Input Summary (play back before writing)

Send this in one message, in the user's language, then ask what is wrong or missing.
Write the spec only after the user approves it.

```
Object: <Object> (<Objects>)
Functions: <list>
Actors: <function → roles>
Entry point: <menu / button>
View list: records <rule> · sort <field asc/desc> · columns <list, link column> · buttons <list + who>
Fields: <name – type – mandatory – rules> …
Create: code <format> · default status <value> · after save <screen + message>
Edit: locked fields <list> · allowed statuses <list>
Delete: <type> · related records <effect>
Guesses (mine, not yours): <list> → will be marked [TBC]
```
