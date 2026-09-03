#!/usr/bin/env bash
# Web Builder — universal one-command installer
set -euo pipefail
REPO="https://github.com/Rishav7324/web-builder.git"
TMP="${TMPDIR:-/tmp}/web-builder-install-$$"
cleanup(){ rm -rf "$TMP"; }
trap cleanup EXIT INT TERM

if ! command -v git >/dev/null 2>&1; then
  echo "Error: git is required." >&2
  exit 1
fi
if ! command -v python3 >/dev/null 2>&1; then
  echo "Error: Python 3 is required." >&2
  exit 1
fi

echo "Installing Web Builder..."
git clone --depth 1 --quiet "$REPO" "$TMP"
# Auto mode installs only agents actually detected on this machine.
# Use installer/install.py --global --targets all for an explicit all-host install.
python3 "$TMP/installer/install.py" --global --targets auto "$@"
echo "Web Builder installed successfully."
