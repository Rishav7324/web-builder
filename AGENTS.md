# Web Builder Agent Instructions

This repository contains the Web Blueprint Engine universal website-building skill.

When the user asks you to build, redesign, or implement a website/web app, load and follow `skill/SKILL.md`.

Important behavior:
- Ask the skill's discovery questions only for information that is still missing.
- Do not create PRD/TRD/prompt documents unless explicitly requested.
- Implement the requested product directly in code.
- Inspect the existing repository before modifying it.
- Use real routes, data, validation, auth, and integrations where required.
- Do not leave fake production flows, dead buttons, TODO placeholders, or mock-only paths.
- Run lint/typecheck/tests/build and browser verification when available.
- Never claim completion when required functionality is knowingly broken.

`skill/SKILL.md` is the canonical skill source. Agent-specific copies under `.agents/`, `.claude/`, and `.opencode/` are discovery copies and should remain synchronized with it.
