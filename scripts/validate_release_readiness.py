#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errors: list[str] = []


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


proc = subprocess.run([sys.executable, str(ROOT / "scripts" / "validate_runtime_parity.py")], cwd=ROOT)
if proc.returncode != 0:
    errors.append("runtime parity gate failed")

manifest_path = ROOT / "dist" / "DELIVERY-MANIFEST.json"
if not manifest_path.is_file():
    errors.append("DELIVERY-MANIFEST.json missing")
else:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    artifact_types = {item.get("type") for item in manifest.get("artifacts", [])}
    for required in {"project_zip", "chat_zip", "custom_gpt_zip", "claude_zip", "checksums"}:
        if required not in artifact_types:
            errors.append(f"delivery manifest missing artifact type: {required}")

sums_path = ROOT / "dist" / "SHA256SUMS.txt"
if not sums_path.is_file():
    errors.append("SHA256SUMS.txt missing")
else:
    sums: dict[str, str] = {}
    for line in sums_path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        digest, name = line.split(None, 1)
        sums[name.strip()] = digest
    for pattern in (
        "novellskaparen-project-*.zip",
        "novellskaparen-chat-*.zip",
        "novellskaparen-custom-gpt-*.zip",
        "novellskaparen-claude-*.zip",
    ):
        matches = sorted((ROOT / "dist").glob(pattern))
        if not matches:
            errors.append(f"missing release artifact for pattern: {pattern}")
            continue
        path = matches[-1]
        if sums.get(path.name) != sha256(path):
            errors.append(f"checksum mismatch or missing: {path.name}")
        try:
            with zipfile.ZipFile(path) as zf:
                bad = zf.testzip()
                if bad:
                    errors.append(f"ZIP CRC error in {path.name}: {bad}")
        except zipfile.BadZipFile:
            errors.append(f"invalid ZIP: {path.name}")

report = {
    "result": "PASS" if not errors else "FAIL",
    "runtime_parity_exit_code": proc.returncode,
    "errors": errors,
}
print(json.dumps(report, ensure_ascii=False, indent=2))
raise SystemExit(1 if errors else 0)
