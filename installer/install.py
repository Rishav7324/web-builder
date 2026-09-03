#!/usr/bin/env python3
"""Web Blueprint Engine v7 universal, non-destructive installer.

Project-local is the safe default. Global installation is opt-in.
The installer never downloads remote code and never overwrites a different
existing skill unless --force is explicitly supplied.
"""
from __future__ import annotations

import argparse
import hashlib
import os
import shutil
import sys
from pathlib import Path

NAME = "web-blueprint-engine"
VERSION = "7.0.0"
ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "skill"
SKILL = SOURCE / "SKILL.md"

PROJECT_TARGETS = {
    "claude": Path(".claude/skills") / NAME,
    "opencode": Path(".opencode/skills") / NAME,
    "agents": Path(".agents/skills") / NAME,
}

GLOBAL_TARGETS = {
    "claude": Path.home() / ".claude/skills" / NAME,
    "opencode": Path.home() / ".config/opencode/skills" / NAME,
    "agents": Path.home() / ".agents/skills" / NAME,
    "antigravity": Path.home() / ".gemini/config/skills" / NAME,
}

SIGNALS = {
    "claude": ("CLAUDE_CODE", ".claude", "CLAUDE.md"),
    "opencode": ("OPENCODE", ".opencode", "opencode.json"),
    "codex": ("CODEX", "CODEX_CLI", "AGENTS.md"),
    "antigravity": ("GEMINI_CLI", ".agents", ".gemini"),
}


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def detect() -> list[str]:
    found: list[str] = []
    for name, signals in SIGNALS.items():
        if any((os.environ.get(s) if s.isidentifier() else Path(s).exists()) for s in signals):
            found.append(name)
    if not found:
        found.append("agents")
    return list(dict.fromkeys(found))


def copy_skill(target: Path, force: bool) -> str:
    source_hash = digest(SKILL)
    existing = target / "SKILL.md"
    if existing.exists():
        if digest(existing) == source_hash:
            return f"already-current: {target}"
        if not force:
            return f"skipped-existing: {target} (different skill; use --force intentionally)"
    target.mkdir(parents=True, exist_ok=True)
    # Copy the complete skill directory, including future reference files.
    if target.exists() and force:
        for item in target.iterdir():
            if item.is_dir():
                shutil.rmtree(item)
            else:
                item.unlink()
    for item in SOURCE.iterdir():
        destination = target / item.name
        if item.is_dir():
            shutil.copytree(item, destination, dirs_exist_ok=True)
        else:
            shutil.copy2(item, destination)
    return f"installed: {target}"


def main() -> int:
    parser = argparse.ArgumentParser(description="Install Web Blueprint Engine for coding agents")
    parser.add_argument("--project", action="store_true", help="install into this repository")
    parser.add_argument("--global", dest="global_install", action="store_true", help="install for the current user")
    parser.add_argument("--targets", default="auto", help="auto, all, or comma-separated: claude,opencode,agents,antigravity")
    parser.add_argument("--force", action="store_true", help="replace a different existing skill")
    parser.add_argument("--detect", action="store_true", help="print detected agents and exit")
    args = parser.parse_args()

    if not SKILL.is_file():
        print(f"error: missing canonical skill: {SKILL}", file=sys.stderr)
        return 2

    if args.detect:
        for agent in detect():
            print(agent)
        return 0

    # Safe default: project-local. Never silently modify the user's home.
    project = args.project or not args.global_install
    global_install = args.global_install

    if args.targets == "auto":
        selected = [x for x in detect() if x in PROJECT_TARGETS]
        if not selected:
            selected = ["agents"]
    elif args.targets == "all":
        selected = ["claude", "opencode", "agents", "antigravity"]
    else:
        selected = [x.strip() for x in args.targets.split(",") if x.strip()]

    installed = 0
    errors = 0
    for name in selected:
        if project and name in PROJECT_TARGETS:
            try:
                print(copy_skill(Path.cwd() / PROJECT_TARGETS[name], args.force))
                installed += 1
            except OSError as exc:
                print(f"[skip] project/{name}: {exc}", file=sys.stderr)
                errors += 1
        if global_install and name in GLOBAL_TARGETS:
            try:
                print(copy_skill(GLOBAL_TARGETS[name], args.force))
                installed += 1
            except OSError as exc:
                print(f"[skip] global/{name}: {exc}", file=sys.stderr)
                errors += 1

    if installed == 0:
        print("No installation target was writable.", file=sys.stderr)
        print("Manual fallback: copy the 'skill' directory into an Agent Skills-compatible skills directory.", file=sys.stderr)
        return 1

    print(f"Web Blueprint Engine {VERSION}: complete ({installed} target(s), {errors} error(s)).")
    print("Restart the agent/session if it does not refresh skills automatically.")
    return 0 if errors == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
