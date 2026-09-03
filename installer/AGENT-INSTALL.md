# Universal Agent Installation

## Project-local (recommended)

Run from the repository root:

```bash
python3 installer/install.py --project --targets all
```

Windows PowerShell:

```powershell
./installer/install.ps1 --project --targets all
```

This installs the canonical skill into the common project-local discovery paths:

- `.agents/skills/web-blueprint-engine/SKILL.md`
- `.claude/skills/web-blueprint-engine/SKILL.md`
- `.opencode/skills/web-blueprint-engine/SKILL.md`

## Global

```bash
python3 installer/install.py --global --targets all
```

Use global installation only when you intentionally want the skill available across projects.

## One target only

```bash
python3 installer/install.py --project --targets claude
python3 installer/install.py --project --targets opencode
python3 installer/install.py --project --targets agents
python3 installer/install.py --project --targets antigravity
```

## Detection

```bash
python3 installer/detect.py
```

Detection is advisory and non-destructive. It never modifies the machine.

## Update

Re-run the installer after pulling a newer version. Existing different skills are skipped by default. Use `--force` only when you explicitly want replacement.

## Multi-agent repositories

For repositories worked on by multiple coding agents, prefer project-local installation and commit the standard discovery files. Each agent can then discover the same canonical skill without changing another agent's global configuration.

## Important limitation

No installer can guarantee automatic installation inside an arbitrary closed agent. The host must allow file access and skill/instruction discovery. This package maximizes interoperability without pretending that an unsupported agent has an installation API.
