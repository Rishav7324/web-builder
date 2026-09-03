#!/usr/bin/env python3
"""Universal, non-destructive Web Builder skill installer."""
from __future__ import annotations

import argparse
import hashlib
import os
import shutil
import subprocess
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
    "codex": Path(".agents/skills") / NAME,
    "antigravity": Path(".agent/skills") / NAME,
    "gemini": Path(".gemini/skills") / NAME,
    "cursor": Path(".cursor/skills") / NAME,
}

GLOBAL_TARGETS = {
    "claude": Path.home() / ".claude/skills" / NAME,
    "opencode": Path.home() / ".config/opencode/skills" / NAME,
    "agents": Path.home() / ".agents/skills" / NAME,
    "codex": Path.home() / ".agents/skills" / NAME,
    "antigravity": Path.home() / ".gemini/config/skills" / NAME,
    "antigravity-cli": Path.home() / ".gemini/antigravity-cli/skills" / NAME,
    "gemini": Path.home() / ".gemini/skills" / NAME,
    "cursor": Path.home() / ".cursor/skills" / NAME,
}

# Project-local signals. These are intentionally conservative: a marker must
# exist in the current project (or its matching environment variable be set).
PROJECT_SIGNALS = {
    "claude": ("CLAUDE_CODE", ".claude", "CLAUDE.md"),
    "opencode": ("OPENCODE", ".opencode", "opencode.json"),
    "codex": ("CODEX", "CODEX_CLI", "AGENTS.md", ".codex"),
    "antigravity": ("GEMINI_CLI", ".agent"),
    "gemini": ("GEMINI_CLI", ".gemini"),
    "cursor": ("CURSOR", ".cursor"),
}

# Global signals. Prefer an actual executable or a host-specific config path
# over generic directories such as ~/.agents or ~/.gemini, which can belong to
# multiple tools.
GLOBAL_SIGNALS = {
    "claude": ("CLAUDE_CODE", "claude", Path.home() / ".claude"),
    "opencode": ("OPENCODE", "opencode", Path.home() / ".config/opencode"),
    "codex": ("CODEX", "CODEX_CLI", "codex", Path.home() / ".codex"),
    "antigravity": ("ANTIGRAVITY", "antigravity", Path.home() / ".agent"),
    "antigravity-cli": ("ANTIGRAVITY_CLI", "agy", Path.home() / ".gemini/antigravity-cli"),
    "gemini": ("GEMINI_CLI", "gemini"),
    "cursor": ("CURSOR", "cursor", Path.home() / ".cursor"),
}


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def command_exists(name: str) -> bool:
    return shutil.which(name) is not None


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


def detect_project() -> list[str]:
    found: list[str] = []
    for name, signals in PROJECT_SIGNALS.items():
        for signal in signals:
            if signal.isidentifier() and os.environ.get(signal):
                found.append(name)
                break
            if not signal.isidentifier() and Path.cwd().joinpath(signal).exists():
                found.append(name)
                break
    return list(dict.fromkeys(found))


def detect_global() -> list[str]:
    found: list[str] = []
    for name, signals in GLOBAL_SIGNALS.items():
        for signal in signals:
            if isinstance(signal, Path):
                if signal.exists():
                    found.append(name)
                    break
            elif signal.isidentifier() and os.environ.get(signal):
                found.append(name)
                break
            elif command_exists(signal):
                found.append(name)
                break
    return list(dict.fromkeys(found))


def detect(scope: str = "both") -> list[str]:
    if scope == "project":
        return detect_project()
    if scope == "global":
        return detect_global()
    return list(dict.fromkeys(detect_project() + detect_global()))


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
        scope = "global" if args.global_install else "project" if args.project else "both"
        print("\n".join(detect(scope)))
        return 0

    # Explicit scope wins. The bootstrap installer uses --global.
    if args.project and args.global_install:
        project = global_install = True
    elif args.project:
        project, global_install = True, False
    elif args.global_install:
        project, global_install = False, True
    else:
        project, global_install = True, False

    if args.targets == "auto":
        if global_install:
            selected = detect_global()
        elif project:
            selected = detect_project()
        else:
            selected = []
    elif args.targets == "all":
        selected = list(GLOBAL_TARGETS.keys()) if global_install else list(PROJECT_TARGETS.keys())
    else:
        selected = [x.strip() for x in args.targets.split(",") if x.strip()]

    # Do not silently install a generic/unknown agent. Explicit --targets can
    # always be used when the user wants a non-detectable host.
    if not selected:
        scope = "global" if global_install else "project"
        print(f"No supported {scope} agent detected. Nothing was installed.")
        print("Use --targets all to install for every supported target, or pass a comma-separated target list.")
        return 0

    installed = errors = 0
    seen_destinations: set[Path] = set()
    for name in selected:
        targets = []
        if project and name in PROJECT_TARGETS:
            targets.append(("project", Path.cwd() / PROJECT_TARGETS[name]))
        if global_install and name in GLOBAL_TARGETS:
            targets.append(("global", GLOBAL_TARGETS[name]))

        for scope, target in targets:
            # Codex and generic Agent Skills intentionally share ~/.agents/skills.
            # Avoid installing the same physical directory twice.
            if target in seen_destinations:
                continue
            seen_destinations.add(target)
            try:
                print(copy_skill(target, args.force))
                installed += 1
            except OSError as exc:
                print(f"[skip] {scope}/{name}: {exc}", file=sys.stderr)
                errors += 1

    print(f"Installed/verified {installed} target(s); {errors} error(s).")
    return 0 if errors == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
