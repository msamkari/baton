structured-handover-doc

A fully independent Claude Skill — builds a structured handover/coordination document (Structured Handover Document) for any situation, project, or trip, from context scattered across a single conversation (messages, documents, images), into one unified format ready to share with a third party.

*Open the repo and read exactly what this Skill tells Claude to do — no black box.*

## Structure

The output is a Claude Doc titled "[Subject] – [Domain] Handover", with five sections in a fixed order (renamed to fit the domain):

1. Situation & History
2. Current Plan
3. People Involved
4. Schedule & Key Dates
5. Outstanding Items

Always ends with one specific comment on the document. The only question allowed in the chat is one clarifying question before the document is created, and only when the subject cannot be inferred; once the document exists there is no chat question.

**If no document tool is available** (for example in plain Claude Code), the skill says so in one line and offers to write the handover as a Markdown file in the project; it writes the file only after you say yes.

**Data minimisation.** The skill leaves out health details, financial account numbers, passwords and keys, government ID numbers and contact details unless you explicitly ask for them to be included and they are needed for the handover. This is an instruction to the model: it is predicted to be followed, not verified with a live run, and you should still read the document before sharing it.

## Independence

Does not depend on any other Skill, or on any persistent-memory structure. Builds the document from the current conversation's context only.

## Files

- `SKILL.md` — the Skill's definition.
- `.claude-plugin/plugin.json` and `skills/structured-handover-doc/SKILL.md` — the Claude Code plugin packaging (the skill file is a copy of the root `SKILL.md`; keep them in sync).
- `LICENSE` — MIT License.
- `releases/v1/structured-handover-doc.skill` — the packaged bundle, ready to upload and activate.

## Install as a plugin

```
/plugin marketplace add msamkari/samkari-plugins
/plugin install structured-handover@samkari-plugins
```

## License

MIT. See `LICENSE`. (Versions up to 1.0.2 were released under PolyForm Noncommercial 1.0.0; from 1.0.3 the project is MIT.)

## Privacy and support

This plugin is a single instruction file: it has no scripts or hooks, collects nothing, stores nothing and sends nothing anywhere itself. It only shapes how Claude writes the handover document from what you give it in the conversation. Support: GitHub Issues (link below).

## Report an Issue / Feedback

Found a bug or have a suggestion? Please open a GitHub Issue in this repository: https://github.com/msamkari/structured-handover-doc-skill/issues
