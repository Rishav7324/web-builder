#!/usr/bin/env python3
"""Universal non-destructive installer for Web Blueprint Engine.

Canonical skill: skills/web-blueprint-engine/
Project-local installation is the safe default. Global installation is explicit.
"""
from __future__ import annotations
import argparse, hashlib, os, shutil, sys
from pathlib import Path

NAME = "web-blueprint-engine"
ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "skills" / NAME
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
    found=[]
    for name, signals in SIGNALS.items():
        if any((os.environ.get(s) if s.isidentifier() else Path(s).exists()) for s in signals):
            found.append(name)
    return list(dict.fromkeys(found or ["agents"]))

def copy_skill(target: Path, force: bool) -> str:
    source_hash = digest(SKILL)
    existing = target / "SKILL.md"
    if existing.exists():
        if digest(existing) == source_hash:
            return f"already-current: {target}"
        if not force:
            return f"skipped-existing: {target} (different skill; use --force to replace)"
    target.mkdir(parents=True, exist_ok=True)
    if target.exists() and force:
        for item in target.iterdir():
            shutil.rmtree(item) if item.is_dir() else item.unlink()
    for item in SOURCE.iterdir():
        dst = target / item.name
        shutil.copytree(item, dst, dirs_exist_ok=True) if item.is_dir() else shutil.copy2(item, dst)
    return f"installed: {target}"

def main() -> int:
    p=argparse.ArgumentParser(description="Install Web Blueprint Engine for coding agents")
    p.add_argument("--project", action="store_true")
    p.add_argument("--global", dest="global_install", action="store_true")
    p.add_argument("--targets", default="auto", help="auto, all, or comma list")
    p.add_argument("--force", action="store_true")
    p.add_argument("--detect", action="store_true")
    args=p.parse_args()
    if not SKILL.is_file():
        print(f"error: canonical skill missing: {SKILL}", file=sys.stderr); return 2
    if args.detect:
        print("\n".join(detect())); return 0
    project = args.project or not args.global_install
    if args.targets == "auto": selected=[x for x in detect() if x in PROJECT_TARGETS] or ["agents"]
    elif args.targets == "all": selected=["claude","opencode","agents","antigravity"]
    else: selected=[x.strip() for x in args.targets.split(",") if x.strip()]
    installed=errors=0
    for name in selected:
        if project and name in PROJECT_TARGETS:
            try: print(copy_skill(Path.cwd()/PROJECT_TARGETS[name], args.force)); installed+=1
            except OSError as e: print(f"[skip] project/{name}: {e}", file=sys.stderr); errors+=1
        if args.global_install and name in GLOBAL_TARGETS:
            try: print(copy_skill(GLOBAL_TARGETS[name], args.force)); installed+=1
            except OSError as e: print(f"[skip] global/{name}: {e}", file=sys.stderr); errors+=1
    if not installed:
        print("No writable installation target found. Copy skills/web-blueprint-engine manually.", file=sys.stderr); return 1
    print(f"Installed/verified {installed} target(s); {errors} error(s).")
    return 0 if not errors else 1

if __name__ == "__main__": raise SystemExit(main())
