#!/usr/bin/env python3
from __future__ import annotations

import json
import zipfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_RUNTIMES = {
    "chatgpt_chat",
    "chatgpt_custom",
    "claude_project",
    "opencode",
    "openai_plugin",
}
EXPECTED_CATEGORIES = {
    "behavior",
    "capability",
    "artifact",
    "workspace_state",
    "tool",
}
ACTIVE = ("chatgpt_chat", "chatgpt_custom", "claude_project")
INACTIVE = ("opencode", "openai_plugin")
errors: list[str] = []


def check(condition: bool, message: str) -> None:
    if not condition:
        errors.append(message)


cfg = yaml.safe_load((ROOT / "gpt-project.yaml").read_text(encoding="utf-8"))
model = yaml.safe_load((ROOT / "runtime-parity.yaml").read_text(encoding="utf-8"))

registered = set(model.get("registered_runtimes", []))
categories = set(model.get("compared_categories", []))
check(registered == EXPECTED_RUNTIMES, f"registered runtimes differ: {sorted(registered)}")
check(categories == EXPECTED_CATEGORIES, f"parity categories differ: {sorted(categories)}")
check(set(cfg.get("runtime_parity", {}).get("registered_runtimes", [])) == EXPECTED_RUNTIMES,
      "gpt-project runtime_parity registered runtimes differ")
check(set(cfg.get("runtime_parity", {}).get("compared_categories", [])) == EXPECTED_CATEGORIES,
      "gpt-project runtime_parity categories differ")

candidates = {
    item.get("runtime_id"): item
    for item in cfg.get("analysis", {}).get("runtime", {}).get("candidates", [])
    if isinstance(item, dict) and item.get("runtime_id")
}
check(set(candidates) == EXPECTED_RUNTIMES, "all five runtimes must have explicit assessment")

for runtime_id in ACTIVE:
    check(candidates.get(runtime_id, {}).get("activate_by_default") is True, f"{runtime_id} must be active")
    check(candidates.get(runtime_id, {}).get("suitability") == "ready", f"{runtime_id} must be ready")
    check(model.get("runtimes", {}).get(runtime_id, {}).get("active") is True, f"{runtime_id} parity model must be active")

for runtime_id in INACTIVE:
    check(candidates.get(runtime_id, {}).get("activate_by_default") is False, f"{runtime_id} must remain inactive")
    check(candidates.get(runtime_id, {}).get("suitability") == "reduced", f"{runtime_id} must be reduced")
    check(model.get("runtimes", {}).get(runtime_id, {}).get("active") is False, f"{runtime_id} parity model must be inactive")

zip_specs = {
    "chatgpt_chat": ("novellskaparen-chat-*.zip", "assistant/runtime-contract.json", "assistant/instructions.md"),
    "chatgpt_custom": ("novellskaparen-custom-gpt-*.zip", "builder/runtime-contract.json", "builder/instructions.md"),
    "claude_project": ("novellskaparen-claude-*.zip", "project/runtime-contract.json", "project/instructions.md"),
}

core_markers = list(cfg.get("instructions", {}).get("core_contract", {}).get("required_markers", []))
canonical = (ROOT / cfg["instructions"]["canonical"]).read_text(encoding="utf-8")

for runtime_id, (pattern, contract_name, instruction_name) in zip_specs.items():
    matches = sorted((ROOT / "dist").glob(pattern))
    if not matches:
        errors.append(f"missing built ZIP for {runtime_id}")
        continue
    with zipfile.ZipFile(matches[-1]) as zf:
        names = set(zf.namelist())
        if contract_name not in names:
            errors.append(f"{runtime_id} missing runtime contract")
            continue
        payload = json.loads(zf.read(contract_name).decode("utf-8"))
        check(payload.get("runtime_id") == runtime_id, f"{runtime_id} wrong runtime_id")
        for key in ("capabilities", "artifacts", "workspace_state", "tools"):
            check(payload.get(key) == cfg.get(key), f"{runtime_id} {key} contract drift")
        if instruction_name not in names:
            errors.append(f"{runtime_id} missing instruction file")
        else:
            instruction = zf.read(instruction_name).decode("utf-8")
            for marker in core_markers:
                check(marker in instruction, f"{runtime_id} missing core marker: {marker}")
            if runtime_id in {"chatgpt_chat", "claude_project"}:
                check(instruction == canonical, f"{runtime_id} instruction must equal canonical")

report = {
    "result": "PASS" if not errors else "FAIL",
    "registered_runtimes": sorted(registered),
    "compared_categories": sorted(categories),
    "active_runtimes": list(ACTIVE),
    "inactive_runtimes": list(INACTIVE),
    "errors": errors,
}
print(json.dumps(report, ensure_ascii=False, indent=2))
raise SystemExit(1 if errors else 0)
