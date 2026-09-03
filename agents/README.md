# Agent Adapters

This directory documents the host-specific integration strategy. The actual shared skill is `skills/web-builder/SKILL.md`.

Each adapter is intentionally thin: it explains how that host discovers the skill and points to the shared implementation instead of maintaining a divergent copy.

Supported adapter families are based on the portability pattern used by mature multi-agent skill distributions: plugin-tier hosts get native manifests where practical; instruction-tier hosts get their native rule file; skill-capable hosts get a standard `SKILL.md` copy.
