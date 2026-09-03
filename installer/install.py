#!/usr/bin/env python3
"""Universal Web Blueprint Engine installer."""
from __future__ import annotations
import os, shutil, sys
from pathlib import Path

SKILL_NAME = "web-blueprint-engine"
HERE = Path(__file__).resolve().parent.parent
SOURCE = HERE / "skill"

def home_candidates() -> list[tuple[str, Path]]:
    home = Path.home()
    return [
        ("Claude Code", home / ".claude" / "skills"),
        ("OpenCode", home / ".config" / "opencode" / "skills"),
        ("Agent Skills", home / ".agents" / "skills"),
        ("Antigravity", home / ".gemini" / "config" / "skills"),
    ]

def project_candidates(cwd: Path) -> list[tuple[str, Path]]:
    return [
        ("Claude Code", cwd / ".claude" / "skills"),
        ("OpenCode", cwd / ".opencode" / "skills"),
        ("Agent Skills / Antigravity", cwd / ".agents" / "skills"),
    ]

def install_to(base: Path) -> Path:
    target = base / SKILL_NAME
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        shutil.rmtree(target)
    shutil.copytree(SOURCE, target)
    return target

def main() -> int:
    cwd = Path.cwd()
    if not SOURCE.is_dir() or not (SOURCE / "SKILL.md").is_file():
        print(f"Invalid package: missing {SOURCE / 'SKILL.md'}")
        return 1

    installed: list[tuple[str, Path]] = []
    for name, base in project_candidates(cwd):
        try:
            installed.append((name, install_to(base)))
        except OSError as exc:
            print(f"[skip] {name}: {exc}")

    if "--global" in sys.argv:
        for name, base in home_candidates():
            try:
                installed.append((f"{name} (global)", install_to(base)))
            except OSError as exc:
                print(f"[skip] {name} (global): {exc}")

    if not installed:
        print("No writable discovery directory was found.")
        print("Copy the 'skill' directory manually into an Agent Skills-compatible skills directory.")
        return 1

    for name, path in installed:
        print(f"[installed] {name}: {path}")
    print("Done. Restart the coding agent/session if skills are not refreshed automatically.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
