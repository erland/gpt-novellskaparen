#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
import zipfile
from pathlib import Path

try:
    import yaml
except Exception as exc:
    raise SystemExit("PyYAML is required") from exc


FORBIDDEN_PARTS = {
    ".git",
    "__pycache__",
    ".pytest_cache",
    "research",
    "evals",
    "tests",
}


def load_cfg(root: Path) -> dict:
    return yaml.safe_load((root / "gpt-project.yaml").read_text(encoding="utf-8"))


def validate_custom(root: Path, cfg: dict) -> list[str]:
    errors = []
    build = root / "build" / "custom-gpt"
    if not build.exists():
        return ["Custom GPT build directory missing"]

    instr = build / "builder" / "instructions.md"
    if not instr.exists():
        errors.append("Missing builder/instructions.md")
    else:
        actual = len(instr.read_text(encoding="utf-8"))
        limit = int(cfg["runtime"]["custom_gpt"]["instruction"]["max_characters"])
        if actual > limit:
            errors.append(f"Instruction too long: {actual} > {limit}")

    kp = build / "builder" / "knowledge-package"
    files = [p for p in kp.rglob("*") if p.is_file()] if kp.exists() else []
    limit = int(cfg["runtime"]["custom_gpt"]["knowledge"]["max_files"])
    if len(files) > limit:
        errors.append(f"Too many Knowledge files: {len(files)} > {limit}")

    required = [
        build / "builder" / "instructions.md",
        build / "builder" / "conversation-starters.md",
        build / "builder" / "capabilities.md",
        build / "builder" / "profile.md",
        build / "README.md",
        build / "COMPATIBILITY.md",
        build / "VERSION",
        build / "MANIFEST.json",
    ]
    for p in required:
        if not p.exists():
            errors.append(f"Missing required file: {p.relative_to(build)}")
    compat = build / "COMPATIBILITY.md"
    if compat.exists() and "senare buildsteg" in compat.read_text(encoding="utf-8"):
        errors.append("Compatibility report still contains provisional parity text")
    return errors


def validate_chat(root: Path, cfg: dict) -> list[str]:
    errors = []
    build = root / "build" / "chat"
    if not build.exists():
        return ["Chat build directory missing"]

    required = [
        build / "START-HERE.md",
        build / "VERSION",
        build / "MANIFEST.json",
        build / "assistant" / "instructions.md",
        build / "assistant" / "PROFILE.md",
        build / "assistant" / "conversation-starters.md",
    ]
    for p in required:
        if not p.exists():
            errors.append(f"Missing required file: {p.relative_to(build)}")

    for p in build.rglob("*"):
        if not p.is_file():
            continue
        rel = p.relative_to(build)
        if any(part in FORBIDDEN_PARTS for part in rel.parts):
            errors.append(f"Forbidden runtime path: {rel}")
    return errors


def validate_claude(root: Path, cfg: dict) -> list[str]:
    errors = []
    build = root / "build" / "claude"
    if not build.exists():
        return ["Claude Projects build directory missing"]

    required = [
        build / "README.md",
        build / "VERSION",
        build / "MANIFEST.json",
        build / "project" / "instructions.md",
        build / "project" / "runtime-contract.json",
        build / "project" / "knowledge",
    ]
    for p in required:
        if not p.exists():
            errors.append(f"Missing required Claude file: {p.relative_to(build)}")

    instr = build / "project" / "instructions.md"
    canonical = root / cfg["instructions"]["canonical"]
    if instr.exists() and instr.read_bytes() != canonical.read_bytes():
        errors.append("Claude Project Instructions are not identical with canonical instruction")

    contract = build / "project" / "runtime-contract.json"
    if contract.exists():
        payload = json.loads(contract.read_text(encoding="utf-8"))
        if payload.get("runtime_id") != "claude_project":
            errors.append("Claude runtime contract has wrong runtime_id")
        adapter = payload.get("adapter", {})
        if adapter.get("claude_code_conventions") is not False:
            errors.append("Claude Projects must not require Claude Code conventions")
        if adapter.get("persistent_state_required") is not False:
            errors.append("Claude Projects must preserve non-stateful core contract")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", default=".")
    args = parser.parse_args()

    root = Path(args.project_root).resolve()
    cfg = load_cfg(root)

    errors = []
    errors.extend(validate_chat(root, cfg))
    if cfg["runtime"]["custom_gpt"]["enabled"]:
        errors.extend(validate_custom(root, cfg))
    if cfg.get("runtime", {}).get("claude", {}).get("enabled"):
        errors.extend(validate_claude(root, cfg))

    if errors:
        print("VALIDATION: FAIL")
        for e in errors:
            print(f"- {e}")
        return 1

    print("VALIDATION: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
