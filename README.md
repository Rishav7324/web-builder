# Web Blueprint Engine — Universal Direct Build Skill

A portable Agent Skills package for turning a website idea into a working, production-ready codebase.

This is the direct-build successor to the original Web Blueprint Engine V4. It keeps the original 28 discovery questions, but removes the document-first workflow:

**Old:** research → PRD → TRD → prompts → implementation plan

**New:** research when useful → same discovery → architecture decisions internally → **write real code → run tests/build → verify → fix**

## Portable agent support

The canonical skill is `skill/SKILL.md`. The repository also includes agent-discovery copies under:

- `.agents/skills/web-blueprint-engine/SKILL.md`
- `.claude/skills/web-blueprint-engine/SKILL.md`
- `.opencode/skills/web-blueprint-engine/SKILL.md`

A root `AGENTS.md` provides an additional instruction fallback for agents that read repository-level agent instructions.

## Install

### Project-local

```bash
python3 installer/install.py
```

### Global

```bash
python3 installer/install.py --global
```

The installer detects the common Claude Code, OpenCode, Agent Skills, and Antigravity discovery locations and copies the canonical skill into writable locations.

## Usage

Once discovered or installed, ask your coding agent to build a website normally.

Example:

> Build a modern Hindi writer website with a public article archive, author profile, categories, search, and an admin editor.

The skill asks the same structured discovery questions when required information is missing, then directly implements the application.

## Important limitation

No remote Git repository can force an arbitrary coding agent to install itself. Automatic discovery depends on the agent supporting a compatible skill/instruction convention and having the repository available. The repository therefore uses standard `SKILL.md` placement, an `AGENTS.md` fallback, and a cross-agent installer rather than pretending there is a universal auto-install API.

## Design principles

- Direct implementation over documentation
- Existing project compatibility over needless rewrites
- Secure-by-default
- Mobile-first
- Accessible
- SEO-aware
- Test and verify before claiming completion
- No fake buttons, mock production paths, or unresolved placeholders
- Minimal architecture that can grow with real requirements

## License

MIT
