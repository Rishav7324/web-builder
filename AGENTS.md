# Web Builder — Universal Agent Instructions

When this repository is used as an AI coding skill, load `skills/web-builder/SKILL.md` before handling website or web-app implementation work.

The skill asks the canonical discovery questions, skips answers already known, and then implements the product directly. Do not substitute PRD/TRD/coding-prompt documents for actual code unless the user explicitly asks for documentation.

Use the shared references under `references/` only when relevant. Preserve existing code, validate trust boundaries, test the implementation, and verify critical browser flows when tooling is available.

Host-specific adapters are under `.claude-plugin/`, `.codex-plugin/`, `.opencode/`, `gemini-extension.json`, `.cursor/`, `.windsurf/`, `.clinerules/`, `.kiro/`, `.qoder/`, `.openclaw/`, `.devin-plugin/`, `.grok-plugin/`, and `.github/` where supported.