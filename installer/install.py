#!/usr/bin/env python3
"""Universal, non-destructive Web Builder skill installer."""
from __future__ import annotations

import argparse
import hashlib
import os
import shutil
import sys
from pathlib import Path

NAME = "web-blueprint-engine"
ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "skill"
SKILL = SOURCE / "SKILL.md"

PROJECT_TARGETS = {
    "claude": Path(".claude/skills") / NAME,
    "opencode": Path(".opencode/skills") / NAME,
    "agents": Path(".agents/skills") / NAME,
    "antigravity": Path(".agent/skills") / NAME,
    "gemini": Path(".gemini/skills") / NAME,
    "cursor": Path(".cursor/skills") / NAME,
}

GLOBAL_TARGETS = {
    "claude": Path.home() / ".claude/skills" / NAME,
    "opencode": Path.home() / ".config/opencode/skills" / NAME,
    "agents": Path.home() / ".agents/skills" / NAME,
    "antigravity": Path.home() / ".gemini/config/skills" / NAME,
    "antigravity-cli": Path.home() / ".gemini/antigravity-cli/skills" / NAME,
    "gemini": Path.home() / ".gemini/skills" / NAME,
    "cursor": Path.home() / ".cursor/skills" / NAME,
}

SIGNALS = {
    "claude": ("CLAUDE_CODE", ".claude", "CLAUDE.md"),
    "opencode": ("OPENCODE", ".opencode", "opencode.json"),
    "codex": ("CODEX", "CODEX_CLI", "AGENTS.md"),
    "antigravity": ("GEMINI_CLI", ".agent", ".agents", ".gemini"),
    "cursor": ("CURSOR", ".cursor"),
}


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def copy_skill(target: Path, force: bool) -> str:
    source_hash = digest(SKILL)
    existing = target / "SKILL.md"
    if existing.exists():
        if digest(existing) == source_hash and not force:
            # References may have been added after an older installation.
            if (SOURCE / "references").exists() and not (target / "references").exists():
                target.mkdir(parents=True, exist_ok=True)
                shutil.copytree(SOURCE / "references", target / "references", dirs_exist_ok=True)
                return f"updated-references: {target}"
            return f"already-current: {target}"
        if not force:
            return f"skipped-existing: {target} (different skill; use --force to replace)"

    target.mkdir(parents=True, exist_ok=True)
    if force:
        for item in target.iterdir():
            shutil.rmtree(item) if item.is_dir() else item.unlink()

    for item in SOURCE.iterdir():
        dst = target / item.name
        if item.is_dir():
            shutil.copytree(item, dst, dirs_exist_ok=True)
        else:
            shutil.copy2(item, dst)
    return f"installed: {target}"


def detect() -> list[str]:
    found: list[str] = []
    for name, signals in SIGNALS.items():
        for signal in signals:
            if signal.isidentifier():
                if os.environ.get(signal):
                    found.append(name)
                    break
            elif Path.cwd().joinpath(signal).exists():
                found.append(name)
                break
    return list(dict.fromkeys(found or ["agents"]))


def main() -> int:
    parser = argparse.ArgumentParser(description="Install Web Builder for coding agents")
    parser.add_argument("--project", action="store_true", help="Install into the current project")
    parser.add_argument("--global", dest="global_install", action="store_true", help="Install globally for the current user")
    parser.add_argument("--targets", default="auto", help="auto, all, or comma-separated targets")
    parser.add_argument("--force", action="store_true", help="Replace an existing different skill")
    parser.add_argument("--detect", action="store_true", help="Print detected hosts and exit")
    args = parser.parse_args()

    if not SKILL.is_file():
        print(f"error: canonical skill missing: {SKILL}", file=sys.stderr)
        return 2

    if args.detect:
        print("\n".join(detect()))
        return 0

    # Explicit scope wins. The bootstrap installer passes --global.
    if args.project and args.global_install:
        project = global_install = True
    elif args.project:
        project, global_install = True, False
    elif args.global_install:
        project, global_install = False, True
    else:
        project, global_install = True, False

    if args.targets == "auto":
        detected = detect()
        selected = detected if detected else ["agents"]
    elif args.targets == "all":
        selected = list(GLOBAL_TARGETS.keys())
    else:
        selected = [x.strip() for x in args.targets.split(",") if x.strip()]

    installed = errors = 0
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

    if not installed:
        print("No installation target selected or writable. Use --project or --global.", file=sys.stderr)
        return 1

    print(f"Installed/verified {installed} target(s); {errors} error(s).")
    return 0 if errors == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
