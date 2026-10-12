#!/usr/bin/env python3
"""Compile Novellskaparen's canonical instruction from its modular sources."""
import argparse
import json
from pathlib import Path

def compile_project(root: Path) -> str:
    manifest = json.loads((root / "canonical/assembly.json").read_text(encoding="utf-8"))
    parts = []
    for section in manifest["sections"]:
        path = (root / section["path"]).resolve()
        if not path.is_relative_to(root.resolve()) or not path.is_file():
            raise ValueError(f"Invalid or missing source: {section['path']}")
        contents = path.read_text(encoding="utf-8")
        if section["title"] != "header" and not contents.startswith("## " + section["title"] + "\n"):
            raise ValueError(f"Wrong section heading: {section['path']}")
        parts.append(contents)
    return "".join(parts)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", type=Path, default=Path("."))
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    root = args.project_root.resolve()
    output = root / "canonical/instructions.md"
    compiled = compile_project(root)
    if args.check:
        if not output.exists() or output.read_text(encoding="utf-8") != compiled:
            raise SystemExit("FAIL: compiled canonical instruction differs from generated file")
        print("Canonical modular compilation: PASS (byte-identical)")
    else:
        output.write_text(compiled, encoding="utf-8")
        print(f"Wrote {output}")

if __name__ == "__main__":
    main()
