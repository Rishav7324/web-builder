# Web Blueprint Engine — Universal Direct Build v7

A portable, production-oriented Agent Skill for turning website and web-app requirements into **real, verified code**.

## What v7 adds

- One canonical `skill/SKILL.md`
- Agent Skills-compatible layout
- Claude Code fallback via `CLAUDE.md` + `.claude/skills/...`
- OpenCode discovery via `.opencode/skills/...` and `.agents/skills/...`
- Codex-compatible repository guidance via `AGENTS.md` + `.agents/skills/...`
- Google Antigravity / Agent Skills-oriented `.agents/skills/...`
- Claude-compatible plugin metadata in `.claude-plugin/plugin.json`
- Cross-platform Python, shell and PowerShell installers
- Non-destructive agent detection
- Project-local installation by default
- Explicit global installation
- Safe `--force` overwrite only when intentionally requested
- Mirror verification and synchronization utilities
- Multi-agent repository safety rules
- Original reference material retained under `references/`
- Direct implementation instead of mandatory PRD/TRD/prompt generation

## Repository layout

```text
skill/SKILL.md                         # canonical skill
references/                            # original V4-derived detailed references
.agents/skills/web-blueprint-engine/   # Agent Skills / Codex / Antigravity mirror
.claude/skills/web-blueprint-engine/   # Claude Code mirror
.opencode/skills/web-blueprint-engine/ # OpenCode mirror
.claude-plugin/plugin.json             # Claude-compatible plugin metadata
AGENTS.md                              # generic/Codex repository fallback
CLAUDE.md                              # Claude Code repository fallback
installer/                             # detection, install, sync, verify
agent-adapters/                        # machine-readable interoperability policy
skill-manifest.json                    # package metadata
```

## Install for one or many agents

### Automatic project-local detection

```bash
python3 installer/install.py --project --targets auto
```

### Install all project-local adapters

```bash
python3 installer/install.py --project --targets all
```

### Global installation (explicit)

```bash
python3 installer/install.py --global --targets all
```

### Detect the host

```bash
python3 installer/install.py --detect
```

### Windows PowerShell

```powershell
./installer/install.ps1 --project --targets all
```

### Verify mirrors

```bash
python3 installer/verify.py
```

### Sync mirrors from canonical source

```bash
python3 installer/sync-mirrors.py
```

## Supported targets

The package is designed for:

- Claude Code
- OpenCode
- OpenAI Codex and Codex-compatible Agent Skills environments
- Google Antigravity / Gemini Agent Skills-compatible environments
- other agents that discover standard `SKILL.md` skills
- custom agents that can read repository instructions

The installer is deliberately conservative. It never silently modifies global configuration, never downloads arbitrary remote code, and does not replace a different existing skill unless `--force` is explicitly supplied.

## Direct-build behavior

The skill keeps the original structured discovery questions but skips questions already answered by the user. It then:

1. inspects the repository
2. selects the smallest suitable architecture
3. implements real frontend/backend/data/auth/integrations
4. wires real states and user journeys
5. runs lint/typecheck/tests/build
6. performs browser verification when available
7. fixes deterministic failures
8. reports actual implementation status

PRD/TRD/AI-prompt documents are **not** the default deliverable. The codebase is.

## Multi-agent safety

When multiple coding agents work on the same repository:

- treat `skill/SKILL.md` as the source of truth
- prefer project-local skill installation
- keep agent mirrors identical
- do not edit another agent's global configuration without explicit intent
- do not commit secrets or machine-specific paths
- avoid destructive git operations
- do not run competing package-manager operations concurrently

## Important limitation

There is no universal API that lets a GitHub repository force every arbitrary AI agent to execute an installer. Automatic installation is possible only where the host exposes compatible skill/plugin discovery or filesystem execution.

This project therefore maximizes interoperability rather than making an impossible guarantee: standard skill layout + common agent discovery paths + repository instruction fallbacks + an explicit cross-platform installer.

## Original package preservation

The original package was a V4 document/blueprint generator. Its detailed reference material is retained in `references/` so no useful domain knowledge is lost. The active canonical skill intentionally supersedes its document-first workflow and turns those requirements into implementation and verification rules.

## License

MIT
