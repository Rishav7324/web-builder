#!/usr/bin/env python3
"""Sync discovery mirrors from the canonical Agent Skill."""
from __future__ import annotations
import shutil
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
SOURCE=ROOT/"skills"/"web-blueprint-engine"
NAME="web-blueprint-engine"
TARGETS=[ROOT/".agents/skills"/NAME,ROOT/".claude/skills"/NAME,ROOT/".opencode/skills"/NAME]
if not (SOURCE/"SKILL.md").is_file(): raise SystemExit("Missing skills/web-blueprint-engine/SKILL.md")
for target in TARGETS:
    target.mkdir(parents=True,exist_ok=True)
    shutil.copy2(SOURCE/"SKILL.md",target/"SKILL.md")
    print("synced",target)
print("Done. Canonical source: skills/web-blueprint-engine/")
