import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = REPO_ROOT / "skills" / "research-presentation"


class ResearchPresentationSkillTests(unittest.TestCase):
    def test_runtime_skill_has_required_contract_files(self):
        required = {
            "SKILL.md",
            "NOTICE",
            "agents/openai.yaml",
            "references/paper-extraction.md",
            "references/narrative-planning.md",
            "references/qa-contract.md",
            "references/rendering.md",
            "references/themes.md",
            "references/layouts.md",
            "scripts/render_slides.py",
            "scripts/audit_pptx.py",
        }
        present = {
            path.relative_to(SKILL_ROOT).as_posix()
            for path in SKILL_ROOT.rglob("*")
            if path.is_file() and "__pycache__" not in path.parts
        }
        self.assertTrue(required.issubset(present))

    def test_skill_frontmatter_and_public_title_are_stable(self):
        skill = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
        interface = (SKILL_ROOT / "agents" / "openai.yaml").read_text(encoding="utf-8")
        self.assertIn("name: research-presentation", skill)
        self.assertIn("paper-to-slides", skill)
        self.assertIn("Research Presentation — Paper to Slides", interface)

    def test_readmes_expose_selective_install(self):
        for readme_name in ("README.md", "README_CN.md"):
            readme = (REPO_ROOT / readme_name).read_text(encoding="utf-8")
            self.assertIn("--skill research-presentation", readme)


if __name__ == "__main__":
    unittest.main()
