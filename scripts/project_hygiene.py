#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import shutil
from pathlib import Path

CACHE_DIRS = {"__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache"}
SAFE_FILE_NAMES = {".DS_Store"}
SAFE_SUFFIXES = {".tmp", ".temp"}
HISTORICAL_RE = re.compile(
    r"(^|[-_.])(old|backup|bak|previous|copy|final-final|v[2-9][0-9]*)([-_.]|$)",
    re.IGNORECASE,
)


def run_hygiene(root: Path, mode: str, fix: bool) -> dict:
    removed = []
    findings = []

    for name in ["build", "dist"]:
        p = root / name
        if p.exists():
            if fix:
                shutil.rmtree(p)
                removed.append(name + "/")
            else:
                findings.append({
                    "severity": "warning",
                    "code": "HY100",
                    "message": "Generated directory exists in source tree",
                    "path": name + "/",
                })

    for p in sorted(root.rglob("*"), key=lambda x: len(x.parts), reverse=True):
        if not p.exists():
            continue
        rel = p.relative_to(root).as_posix()
        if p.is_dir() and p.name in CACHE_DIRS:
            if fix:
                shutil.rmtree(p)
                removed.append(rel + "/")
            else:
                findings.append({
                    "severity": "warning",
                    "code": "HY110",
                    "message": "Cache directory found",
                    "path": rel,
                })
            continue
        if p.is_file() and (p.name in SAFE_FILE_NAMES or p.suffix.lower() in SAFE_SUFFIXES):
            if fix:
                p.unlink()
                removed.append(rel)
            else:
                findings.append({
                    "severity": "warning",
                    "code": "HY111",
                    "message": "Temporary file found",
                    "path": rel,
                })

    for p in root.rglob("*"):
        if not p.is_file():
            continue
        rel = p.relative_to(root).as_posix()
        if HISTORICAL_RE.search(p.stem):
            findings.append({
                "severity": "warning",
                "code": "HY200",
                "message": "Filename suggests historical/superseded copy; manual assessment required",
                "path": rel,
            })

    if mode == "final":
        for rel in [
            "gpt-project.yaml",
            "project-status.yaml",
            "docs/development-plan.md",
            "runtime-parity.yaml",
        ]:
            if not (root / rel).exists():
                findings.append({
                    "severity": "blocked",
                    "code": "HY300",
                    "message": "Required canonical project file missing",
                    "path": rel,
                })

    if any(f["severity"] == "blocked" for f in findings):
        result = "blocked"
    elif findings:
        result = "warning"
    else:
        result = "pass"

    return {"result": result, "mode": mode, "removed": sorted(set(removed)), "findings": findings}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--project-root", default=".")
    ap.add_argument("--mode", choices=["checkpoint", "final"], default="checkpoint")
    ap.add_argument("--fix", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    report = run_hygiene(Path(args.project_root).resolve(), args.mode, args.fix)
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        for item in report["removed"]:
            print(f"REMOVED {item}")
        for f in report["findings"]:
            print(f"{f['severity'].upper():7} {f['code']} {f['message']} [{f.get('path','')}]")
        print(f"Hygiene result: {report['result'].upper()}")

    return 1 if report["result"] == "blocked" else 0


if __name__ == "__main__":
    raise SystemExit(main())
