#!/usr/bin/env python3
"""Verify installed Web Blueprint Engine mirrors against the canonical skill."""
from __future__ import annotations
import hashlib
import sys
from pathlib import Path

NAME="web-blueprint-engine"
ROOT=Path(__file__).resolve().parent.parent
SOURCE=ROOT/"skill"/"SKILL.md"
TARGETS=[
    ROOT/".agents/skills"/NAME/"SKILL.md",
    ROOT/".claude/skills"/NAME/"SKILL.md",
    ROOT/".opencode/skills"/NAME/"SKILL.md",
]

def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()

if not SOURCE.is_file():
    print("FAIL: canonical skill missing", file=sys.stderr); raise SystemExit(2)
expected=sha(SOURCE)
failed=False
for target in TARGETS:
    if not target.is_file():
        print(f"MISSING {target}"); failed=True
    elif sha(target) != expected:
        print(f"MISMATCH {target}"); failed=True
    else:
        print(f"OK {target}")
print("canonical sha256:", expected)
raise SystemExit(1 if failed else 0)
