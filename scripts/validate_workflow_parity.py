#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ci = (ROOT / ".github/workflows/ci.yml").read_text(encoding="utf-8")
release = (ROOT / ".github/workflows/release.yml").read_text(encoding="utf-8")
errors: list[str] = []

shared = [
    "lint_gpt_project.py",
    "python -m pytest -q -p no:cacheprovider",
    "build_distributions.py",
    "validate_distributions.py",
    "validate_runtime_parity.py",
    "validate_release_readiness.py",
    "project_hygiene.py --project-root . --mode final",
]
for marker in shared:
    if marker not in ci:
        errors.append(f"CI missing: {marker}")
    if marker not in release:
        errors.append(f"Release missing: {marker}")

target = "--targets project,chat,custom-gpt,claude"
if target not in ci or target not in release:
    errors.append("CI and release must build the same active targets")
if "github.event.release.tag_name" not in release:
    errors.append("Release must derive version from release tag")
if "validate_workflow_parity.py" not in ci:
    errors.append("CI must enforce workflow parity")
if "validate_workflow_parity.py" not in release:
    errors.append("Release must enforce workflow parity")

if errors:
    print("WORKFLOW PARITY: FAIL")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("WORKFLOW PARITY: PASS")
