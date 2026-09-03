# Agent Adapters

This directory documents interoperability rather than pretending every agent exposes the same installation API.

## Resolution order

1. Explicit user request
2. Agent-native skill/plugin discovery
3. Project-local `.agents/skills/...`
4. Agent-specific project path (`.claude` / `.opencode`)
5. Repository-level `AGENTS.md` / `CLAUDE.md`
6. Included installer
7. Manual copy as final fallback

## Canonical source

`../skill/SKILL.md` is the only source of truth.

Agent-specific copies are mirrors for discovery compatibility. They should remain byte-identical to the canonical file.

## Multi-agent rule

Never let one agent silently change another agent's global configuration. Project-local installation is the reproducible default.
