#!/usr/bin/env python3
"""Compile modular canonical sources preserving exact section order and whitespace."""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SECTION = re.compile(r"^## (.+)$", re.MULTILINE)

def split_sections(source: str):
    hits = list(SECTION.finditer(source))
    return {m.group(1): source[m.start():hits[i + 1].start() if i + 1 < len(hits) else None]
            for i, m in enumerate(hits)}

def compile_instruction():
    config = json.loads((ROOT / "canonical/assembly.json").read_text(encoding="utf-8"))
    raw = {owner: (ROOT / path).read_text(encoding="utf-8")
           for owner, path in config["sources"].items()}
    first = SECTION.search(raw["core"])
    if not first:
        raise ValueError("Core source has no sections")
    header = raw["core"][:first.start()]
    mapped = {owner: split_sections(value) for owner, value in raw.items()}
    used = set()
    parts = [header]
    for entry in config["sections"]:
        key = (entry["owner"], entry["title"])
        if key in used:
            raise ValueError(f"Duplicate section mapping: {key}")
        used.add(key)
        parts.append(mapped[entry["owner"]][entry["title"]])
    existing = {(owner, title) for owner, sections in mapped.items() for title in sections}
    if existing != used:
        raise ValueError(f"Unmapped or missing sections: {existing ^ used}")
    return "".join(parts), ROOT / config["output"]

def main():
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--write", action="store_true")
    args = parser.parse_args()
    content, path = compile_instruction()
    if args.check:
        if not path.exists() or path.read_text(encoding="utf-8") != content:
            raise SystemExit("FAIL: canonical instructions differ from modular source compilation")
        print("PASS: canonical instructions exactly match modular sources")
    elif args.write:
        path.write_text(content, encoding="utf-8")
        print(f"Updated {path}")

if __name__ == "__main__":
    main()
