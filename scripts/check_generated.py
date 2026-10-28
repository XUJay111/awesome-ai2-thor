#!/usr/bin/env python3
"""Fail when tracked outputs differ from a fresh, deterministic generation."""
import argparse
from datetime import date
import subprocess
import sys
from catalog import ROOT, ROOMS

OUTPUTS = [
    "README.md", "README.zh-CN.md", "assets/floorplan-light.svg",
    "assets/floorplan-dark.svg", "assets/timeline-light.svg", "assets/timeline-dark.svg", "assets/social-preview.svg",
    *(f"assets/rooms/{room[1]}.svg" for room in ROOMS),
    "assets/fonts/Archivo.woff2", "docs/index.html", "docs/.nojekyll",
]

def snapshot():
    return {path: (ROOT / path).read_bytes() if (ROOT / path).exists() else None for path in OUTPUTS}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--as-of", type=date.fromisoformat,
                        help="Reference date forwarded to the generator (YYYY-MM-DD).")
    args = parser.parse_args()
    command = [sys.executable, str(ROOT / "scripts/generate_readme.py")]
    if args.as_of:
        command += ["--as-of", args.as_of.isoformat()]
    before = snapshot()
    subprocess.run(command, cwd=ROOT, check=True)
    after = snapshot()
    changed = [path for path in OUTPUTS if before[path] != after[path]]
    if changed:
        print("Generated files were stale (now regenerated): " + ", ".join(changed), file=sys.stderr)
        print("Review and commit the generated files, then run make check again.", file=sys.stderr)
        return 1
    print("All generated files are current; regeneration is byte-for-byte stable.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
