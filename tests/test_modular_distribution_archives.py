"""Validate actual runtime ZIP behavior sources, not just YAML metadata."""
from pathlib import Path
import zipfile
import yaml

ROOT = Path(__file__).resolve().parents[1]
VERSION = "0.0.0-ci"


def _member(z, suffix):
    matches = [name for name in z.namelist() if name.endswith(suffix)]
    assert len(matches) == 1, f"Expected one {suffix}, found {matches}"
    return z.read(matches[0]).decode("utf-8")


def test_all_distribution_archives_use_canonical_skill_bodies():
    cfg = yaml.safe_load((ROOT / "gpt-project.yaml").read_text(encoding="utf-8"))
    assert cfg["instructions"]["mode"] == "modular_skills"
    core = (ROOT / cfg["instructions"]["core"]).read_text(encoding="utf-8").strip()
    skills = cfg["skills"]["definitions"]
    assert len(skills) == 4
    bodies = {}
    for skill in skills:
        source = skill["source"]
        assert source.endswith("/source/instructions.md"), source
        bodies[skill["id"]] = (ROOT / source).read_text(encoding="utf-8").strip()
        assert bodies[skill["id"]]
    for target in ("plugin", "claude-skills"):
        archive = ROOT / "dist" / f"novellskaparen-{target}-{VERSION}.zip"
        assert archive.is_file(), archive
        with zipfile.ZipFile(archive) as z:
            for skill in skills:
                skill_id = skill["id"]
                rendered = _member(z, f"skills/{skill_id}/SKILL.md")
                assert core in rendered, f"{target}: missing shared core for {skill_id}"
                assert bodies[skill_id] in rendered, f"{target}: missing canonical body for {skill_id}"
                for other_id, other_body in bodies.items():
                    if other_id != skill_id:
                        assert other_body not in rendered, f"{target}: {skill_id} duplicates {other_id}"
    for target, suffix in (
        ("chat", "assistant/instructions.md"),
        ("claude-project", "project/instructions.md"),
        ("opencode", "AGENTS.md"),
    ):
        archive = ROOT / "dist" / f"novellskaparen-{target}-{VERSION}.zip"
        assert archive.is_file(), archive
        with zipfile.ZipFile(archive) as z:
            rendered = _member(z, suffix)
            assert core in rendered, f"{target}: missing shared core"
            for skill_id, body in bodies.items():
                assert body in rendered, f"{target}: missing behavior {skill_id}"
