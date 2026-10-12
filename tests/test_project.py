from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_required_project_files_exist():
    for rel in [
        "gpt-project.yaml",
        "project-status.yaml",
        "README.md",
        "PROJECT.md",
        "STATUS.md",
        "docs/development-plan.md",
        "canonical/instructions.md",
    ]:
        assert (ROOT / rel).is_file(), rel


def test_canonical_instruction_contains_core_sections():
    text = (ROOT / "canonical/instructions.md").read_text(encoding="utf-8")
    for marker in [
        "## Identitet",
        "## Grundbeteende",
        "## Målgruppsanpassning",
        "## Originalitet och inspiration",
        "## Revision",
    ]:
        assert marker in text


def test_canonical_instruction_fits_custom_gpt_limit():
    text = (ROOT / "canonical/instructions.md").read_text(encoding="utf-8")
    assert len(text) <= 8000


def test_new_story_workflow_is_explicit():
    text = (ROOT / "canonical/instructions.md").read_text(encoding="utf-8")
    for marker in [
        "## Arbetsflöde för en ny novell",
        "**Skriv direkt**",
        "**Fyll i själv**",
        "**Fråga kort**",
        "överraska mig",
        "Exakt ordantal",
    ]:
        assert marker in text


def test_brief_acceptance_scenarios_exist():
    path = ROOT / "tests/brief-scenarios.md"
    assert path.is_file()
    text = path.read_text(encoding="utf-8")
    for marker in [
        "Scenario 1",
        "Scenario 2",
        "Scenario 3",
        "Scenario 4",
        "Scenario 5",
        "Scenario 6",
        "Scenario 7",
    ]:
        assert marker in text


def test_audience_adaptation_contract_is_explicit():
    text = (ROOT / "canonical/instructions.md").read_text(encoding="utf-8")
    for marker in [
        "Målgruppen ska påverka mer än ordval",
        "### Lågstadiet",
        "### Mellanstadiet",
        "### Tonåring",
        "### Vuxen",
        "undertext",
        "kalibreras efter läsarens ålder",
        "inte automatiskt bli moraliserande",
        "tonalitet konsekvent",
    ]:
        assert marker in text


def test_audience_acceptance_scenarios_exist():
    path = ROOT / "tests/audience-scenarios.md"
    assert path.is_file()
    text = path.read_text(encoding="utf-8")
    for marker in [
        "Scenario 1",
        "Scenario 2",
        "Scenario 3",
        "Scenario 4",
        "Scenario 5",
        "Scenario 6",
        "Scenario 7",
    ]:
        assert marker in text

def test_writing_partner_modes_are_explicit():
    text = (ROOT / "canonical/instructions.md").read_text(encoding="utf-8")
    for marker in [
        "## Skrivpartnerlägen",
        "**Idéutveckling:**",
        "**Synopsis och plan:**",
        "**Karaktärsarbete:**",
        "**Skrivande:**",
        "**Fortsättning/utbyggnad:**",
        "**Revision:**",
        "Växla naturligt",
    ]:
        assert marker in text


def test_writing_partner_acceptance_scenarios_exist():
    path = ROOT / "tests/writing-partner-scenarios.md"
    assert path.is_file()
    text = path.read_text(encoding="utf-8")
    for marker in [
        "Scenario 1", "Scenario 2", "Scenario 3", "Scenario 4", "Scenario 5",
        "Scenario 6", "Scenario 7", "Scenario 8", "Scenario 9",
    ]:
        assert marker in text



def test_literary_quality_contract_is_explicit():
    text = (ROOT / "canonical/instructions.md").read_text(encoding="utf-8")
    for marker in [
        "tydlig scenfunktion",
        "dialog avslöja vilja, relation eller konflikt",
        "Variera tempo, meningsrytm och scenlängd",
        "Gestalta viktiga ögonblick",
        "perspektiv och etablerade fakta konsekventa",
        "slutet kännas förberett och motiverat",
    ]:
        assert marker in text


def test_revision_contract_is_precise():
    text = (ROOT / "canonical/instructions.md").read_text(encoding="utf-8")
    for marker in [
        "Matcha ingreppets storlek mot uppgiften",
        "Vid kortning:",
        "Vid ökad spänning:",
        "Vid mer gestaltning:",
        "Vid svagt slut:",
    ]:
        assert marker in text


def test_literary_quality_acceptance_scenarios_exist():
    path = ROOT / "tests/literary-quality-scenarios.md"
    assert path.is_file()
    text = path.read_text(encoding="utf-8")
    for marker in [f"Scenario {i}" for i in range(1, 11)]:
        assert marker in text


def test_originality_and_inspiration_contract_is_explicit():
    text = (ROOT / "canonical/instructions.md").read_text(encoding="utf-8")
    for marker in [
        "självständigt verk",
        "dold mall",
        "breda egenskaper",
        "egen identitet",
        "text som användaren själv ger dig",
    ]:
        assert marker in text


def test_continuity_contract_and_scenarios_exist():
    text = (ROOT / "canonical/instructions.md").read_text(encoding="utf-8")
    for marker in [
        "tidslinje",
        "användarens senaste uttryckliga instruktion",
        "hitta inte på att något tidigare har hänt",
        "motsäger varandra",
        "Återanvänd inte samma karaktärsbåge",
    ]:
        assert marker in text
    path = ROOT / "tests/originality-continuity-scenarios.md"
    assert path.is_file()
    scenarios = path.read_text(encoding="utf-8")
    for marker in [f"Scenario {i}" for i in range(1, 11)]:
        assert marker in scenarios


def test_distribution_metadata_is_explicit():
    cfg = __import__("yaml").safe_load((ROOT / "gpt-project.yaml").read_text(encoding="utf-8"))
    meta = cfg["runtime_metadata"]
    assert meta["name"] == "Novellskaparen"
    assert meta["conversation_starters_limit"] == 4
    assert meta["capabilities"]["image_generation"] == "recommended"
    assert meta["capabilities"]["web_search"] == "optional_for_fact_checking"


def test_custom_gpt_starters_are_builder_ready():
    text = (ROOT / "conversation-starters/starters.md").read_text(encoding="utf-8")
    starters = [line for line in text.splitlines() if line.startswith("- ")]
    assert len(starters) == 4
    assert any("Fortsätt" in line for line in starters)
    assert any("utveckla" in line.lower() for line in starters)


def test_step7_build_logic_contains_runtime_profiles_and_real_parity_report():
    cfg = __import__("yaml").safe_load((ROOT / "gpt-project.yaml").read_text(encoding="utf-8"))
    assert set(cfg["build_system"]["runtime_targets"]) == {"chat", "plugin", "claude_project", "claude_skills", "opencode"}
    assert cfg["runtime"]["custom_gpt"]["enabled"] is False


def test_build_is_clean_versioned_and_reproducible_by_contract():
    cfg = __import__("yaml").safe_load((ROOT / "gpt-project.yaml").read_text(encoding="utf-8"))
    assert cfg["build_system"]["deterministic_zip"] is True
    assert cfg["build_system"]["checksums"] == "sha256"
    assert set(cfg["build_system"]["targets"]) == {"project", "chat", "plugin", "claude_project", "claude_skills", "opencode"}


def test_release_workflow_uses_release_tag_and_explicit_artifacts():
    text = (ROOT / ".github/workflows/release.yml").read_text(encoding="utf-8")
    assert "github.event.release.tag_name" in text
    assert "gh release upload" in text
    for target in ("project", "chat", "plugin", "claude_project", "claude_skills", "opencode"):
        assert target in text
    assert "custom-gpt" not in text


def test_ci_verifies_reproducibility():
    text = (ROOT / ".github/workflows/ci.yml").read_text(encoding="utf-8")
    assert "Verify reproducible build" in text
    assert "diff -u /tmp/first-build.sha256 dist/SHA256SUMS.txt" in text


def test_gpt_builder_15_contracts_are_declared():
    cfg = __import__("yaml").safe_load((ROOT / "gpt-project.yaml").read_text(encoding="utf-8"))
    assert cfg["project"]["profile"] == "simple"
    assert cfg["model_robustness"]["level"] == "lightweight"
    assert cfg["model_robustness"]["instruction_adherence_evals"] is True
    assert cfg["instructions"]["core_contract"]["max_required_file_hops"] <= 1
    assert cfg["instructions"]["core_contract"]["knowledge_may_not_be_required_for_core_behavior"] is True
    assert cfg["workspace_state"]["state"]["authority"] == "none"
    assert cfg["tools"]["tools"] == []


def test_peer_runtime_assessment_is_explicit():
    cfg = __import__("yaml").safe_load((ROOT / "gpt-project.yaml").read_text(encoding="utf-8"))
    candidates = {item["runtime_id"]: item for item in cfg["analysis"]["runtime"]["candidates"]}
    assert set(candidates) == {
        "chatgpt_chat",
        "chatgpt_custom",
        "claude_project",
        "opencode",
        "openai_plugin",
    }
    assert candidates["chatgpt_chat"]["suitability"] == "ready"
    assert candidates["chatgpt_custom"]["suitability"] == "ready"
    assert candidates["claude_project"]["suitability"] == "ready"
    assert candidates["opencode"]["suitability"] == "reduced"
    assert candidates["openai_plugin"]["suitability"] == "reduced"
    assert cfg["runtime"]["claude"]["enabled"] is True


def test_platform_neutral_contract_schemas_exist():
    for rel in [
        "schemas/capability-contract.schema.json",
        "schemas/artifact-contract.schema.json",
        "schemas/workspace-state-contract.schema.json",
        "schemas/tool-contract.schema.json",
        "schemas/eval-case.schema.json",
        "schemas/test-manifest.schema.json",
    ]:
        assert (ROOT / rel).is_file(), rel


def test_instruction_adherence_evals_are_registered():
    yaml = __import__("yaml")
    manifest = yaml.safe_load((ROOT / "tests/test-manifest.yaml").read_text(encoding="utf-8"))
    suite = manifest["suites"]["instruction_adherence"]
    assert suite["type"] == "behavioral"
    assert suite["blocking"] is True
    eval_dir = ROOT / suite["path"]
    eval_files = sorted(eval_dir.glob("*.yaml"))
    assert len(eval_files) >= 4
    for path in eval_files:
        case = yaml.safe_load(path.read_text(encoding="utf-8"))
        assert case["criticality"] in {"critical", "important", "optional"}
        assert case["input"]
        assert case["expected"]["required"]


def test_claude_projects_distribution_contract_is_configured():
    cfg = __import__("yaml").safe_load((ROOT / "gpt-project.yaml").read_text(encoding="utf-8"))
    claude = cfg["runtime"]["claude"]
    assert claude["enabled"] is True
    assert claude["mode"] == "claude_project"
    assert claude["project"]["instructions"] == "project/instructions.md"
    assert claude["project"]["knowledge"] == "project/knowledge"
    assert claude["project"]["runtime_contract"] == "project/runtime-contract.json"


def test_claude_build_and_validation_are_wired_into_ci():
    cfg = __import__("yaml").safe_load((ROOT / "gpt-project.yaml").read_text(encoding="utf-8"))
    ci = (ROOT / ".github/workflows/ci.yml").read_text(encoding="utf-8")
    assert {"claude_project", "claude_skills"}.issubset(cfg["build_system"]["runtime_targets"])
    assert "--targets project,chat,plugin,claude_project,claude_skills,opencode" in ci


def test_runtime_parity_model_covers_five_registered_runtimes():
    yaml = __import__("yaml")
    cfg = yaml.safe_load((ROOT / "gpt-project.yaml").read_text(encoding="utf-8"))
    parity = yaml.safe_load((ROOT / "runtime-parity.yaml").read_text(encoding="utf-8"))
    expected = {
        "chatgpt_chat",
        "chatgpt_custom",
        "claude_project",
        "opencode",
        "openai_plugin",
    }
    assert set(cfg["runtime_parity"]["registered_runtimes"]) == expected
    assert set(parity["registered_runtimes"]) == expected
    assert set(cfg["runtime_parity"]["compared_categories"]) == {
        "behavior", "capability", "artifact", "workspace_state", "tool"
    }
    assert parity["runtimes"]["chatgpt_chat"]["active"] is True
    assert parity["runtimes"]["chatgpt_custom"]["active"] is True
    assert parity["runtimes"]["claude_project"]["active"] is True
    assert parity["runtimes"]["opencode"]["active"] is False
    assert parity["runtimes"]["openai_plugin"]["active"] is False


def test_active_distributions_embed_runtime_contracts():
    cfg = __import__("yaml").safe_load((ROOT / "gpt-project.yaml").read_text(encoding="utf-8"))
    targets = cfg["build_system"]["runtime_targets"]
    for name in ("chat", "plugin", "claude_project", "claude_skills", "opencode"):
        assert all(targets[name].get(k) for k in ("builder", "runtime_id", "runtime_key", "artifact_type", "filename_pattern"))
    assert (ROOT / "canonical/instructions.md").is_file()


def test_ci_and_release_enforce_runtime_parity_and_readiness():
    ci = (ROOT / ".github/workflows/ci.yml").read_text(encoding="utf-8")
    release = (ROOT / ".github/workflows/release.yml").read_text(encoding="utf-8")
    for text in (ci, release):
        assert "validate_distributions.py" in text
        assert "--targets project,chat,plugin,claude_project,claude_skills,opencode" in text


def test_legacy_validator_scripts_are_not_used():
    ci = (ROOT / ".github/workflows/ci.yml").read_text(encoding="utf-8")
    release = (ROOT / ".github/workflows/release.yml").read_text(encoding="utf-8")
    for obsolete in ("validate_runtime_parity.py", "validate_release_readiness.py", "validate_workflow_parity.py"):
        assert not (ROOT / "scripts" / obsolete).exists()
        assert obsolete not in ci
        assert obsolete not in release



def test_final_hygiene_and_workflow_parity_are_enforced():
    ci = (ROOT / ".github/workflows/ci.yml").read_text(encoding="utf-8")
    release = (ROOT / ".github/workflows/release.yml").read_text(encoding="utf-8")
    for text in (ci, release):
        assert "lint_gpt_project.py" in text
        assert "validate_distributions.py" in text


def test_final_documentation_matches_active_runtime_model():
    project = (ROOT / "PROJECT.md").read_text(encoding="utf-8")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    status = (ROOT / "STATUS.md").read_text(encoding="utf-8")
    for text in (project, readme):
        for marker in ("Chat", "Plugin", "Claude Projects", "Claude Skills", "OpenCode", "v1.6.13"):
            assert marker in text
        assert "Custom GPT och Claude Projects byggs som aktiva" not in text
    assert "Migration till GPT Byggaren v1.6.13" in status
    assert "Projektet är i **förvaltningsläge**. PR:n kan mergeas." not in status
