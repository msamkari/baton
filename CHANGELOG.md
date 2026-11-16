# Changelog

## 1.1.0 (2026-11-15)
- Renamed to **baton** (was structured-handover): the skill is now `/baton:handover`; install with `/plugin install baton@samkari-plugins`. The repository was recreated under the new name. No behaviour change.

## 1.0.4 (2026-11-15)
Skill text only (both copies and the `.skill` bundle rebuilt from the root file; identical after line-ending normalisation), from the round-2 adversarial report:
- Resolved the contradiction between "no question in chat" and "ask one direct question if Subject/Domain is unclear": exactly one clarifying question in the chat is allowed, only before the document is created and only when the subject cannot be inferred; after creation the single document comment stays the only question.
- Added a fallback: when no document-creation tool or connector is available, the skill says so in one line and offers to write the handover as a Markdown file in the project, writing only after the user says yes.
- Added a data-minimisation rule: health details, financial account numbers, passwords/keys, government ID numbers and contact details are left out unless the user explicitly asks and they are needed; "contact details if available" for people was changed accordingly.
- Added tests (0 -> 6): copies and bundle identical, no contradiction, fallback, data-minimisation sentences, manifest and no personal data.
- Not verified: how a model follows these rules is predicted from the text, not tested with a live run, with or without a Docs connector. Known and unchanged: a document the user already shared still receives the mandatory comment.

## 1.0.3 (2026-11-15)
- License changed from PolyForm Noncommercial 1.0.0 to MIT, like the other plugins in the marketplace (the author holds all rights).

## 1.0.2 (2026-11-15)
- Added the plugin icon (square PNG, 1024 px), generated with Gemini and chosen by the author; clears the ICON_MISSING validator warning.
