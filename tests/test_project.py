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
    text = (ROOT / "scripts/build_distributions.py").read_text(encoding="utf-8")
    for marker in ["runtime_profile_text", "PROFILE.md", "profile.md", "Full paritet", "Inga kända saknade kärnfunktioner"]:
        assert marker in text


def test_build_is_clean_versioned_and_reproducible_by_contract():
    text = (ROOT / "scripts/build_distributions.py").read_text(encoding="utf-8")
    for marker in [
        "validate_version(version)",
        "ensure_clean_dir(build_root)",
        "ensure_clean_dir(dist)",
        'f"{project_id}-project-{version}.zip"',
        "FIXED_ZIP_DATE",
    ]:
        assert marker in text


def test_release_workflow_uses_release_tag_and_explicit_artifacts():
    text = (ROOT / ".github/workflows/release.yml").read_text(encoding="utf-8")
    for marker in [
        "github.event.release.tag_name",
        "novellskaparen-project-${VERSION}.zip",
        "novellskaparen-chat-${VERSION}.zip",
        "novellskaparen-custom-gpt-${VERSION}.zip",
        "SHA256SUMS.txt",
        "DELIVERY-MANIFEST.json",
    ]:
        assert marker in text
    assert "dist/*.zip" not in text


def test_ci_verifies_reproducibility():
    text = (ROOT / ".github/workflows/ci.yml").read_text(encoding="utf-8")
    assert "Verify reproducible build" in text
    assert "diff -u /tmp/first-build.sha256 dist/SHA256SUMS.txt" in text
