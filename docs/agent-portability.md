# Agent Portability

Web Builder is distributed like a portable multi-agent skill package. The canonical implementation lives in `skills/web-builder/SKILL.md`. Host-specific adapters are intentionally thin and exist only where an agent needs a native manifest, rule file, plugin entrypoint, or command convention.

## Architecture

- `skills/web-builder/` — canonical skill and shared references.
- `agents/<agent>/` — human-readable adapter notes and installation metadata.
- `.claude-plugin/` — Claude Code plugin metadata.
- `.codex-plugin/` — Codex plugin metadata.
- `.opencode/` — OpenCode plugin/command adapter.
- `gemini-extension.json` — Gemini CLI / Antigravity extension metadata.
- `.cursor/`, `.windsurf/`, `.clinerules/`, `.kiro/`, `.qoder/`, `.github/` — instruction-tier adapters.
- `.openclaw/` — OpenClaw skill mirror.
- `references/` — shared implementation guidance loaded only when needed.

The adapters point back to the same behavior. They do not fork the product logic.
