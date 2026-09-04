import tempfile
import unittest
from pathlib import Path

from scripts.check_markdown_links import find_broken_links
from scripts.validate_skills import validate_repository, validate_skill


REPO_ROOT = Path(__file__).resolve().parents[1]


class RepositoryValidationTests(unittest.TestCase):
    def test_repository_skills_are_valid(self):
        self.assertEqual(validate_repository(REPO_ROOT), [])

    def test_validator_rejects_missing_runtime_reference(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            skill_root = Path(temporary_directory) / "example-skill"
            (skill_root / "agents").mkdir(parents=True)
            (skill_root / "SKILL.md").write_text(
                "---\n"
                "name: example-skill\n"
                "description: Use when testing a repository Skill.\n"
                "---\n\n"
                "Read `references/missing.md` before continuing.\n",
                encoding="utf-8",
            )
            (skill_root / "agents" / "openai.yaml").write_text(
                "interface:\n"
                '  display_name: "Example Skill"\n'
                '  short_description: "Test Skill validation"\n'
                '  default_prompt: "Use $example-skill for this test."\n',
                encoding="utf-8",
            )
            errors = validate_skill(skill_root)
            self.assertTrue(any("missing referenced resource" in error for error in errors))

    def test_markdown_checker_reports_broken_relative_link(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            repo_root = Path(temporary_directory)
            (repo_root / "README.md").write_text(
                "[missing](docs/missing.md)\n",
                encoding="utf-8",
            )
            errors = find_broken_links(repo_root)
            self.assertEqual(len(errors), 1)
            self.assertIn("docs/missing.md", errors[0])

    def test_repository_markdown_links_are_valid(self):
        self.assertEqual(find_broken_links(REPO_ROOT), [])

    def test_public_entry_points_credit_yila_with_campaign_tracking(self):
        entry_points = [
            REPO_ROOT / "README.md",
            REPO_ROOT / "README_CN.md",
            REPO_ROOT / "README_ja.md",
            REPO_ROOT / "README_ko.md",
            REPO_ROOT / "distribution" / "science-research-writing" / "README.md",
            REPO_ROOT / "distribution" / "sci-ssci-polishing" / "README.md",
            REPO_ROOT / "distribution" / "academic-humanizer" / "README.md",
            REPO_ROOT / "distribution" / "research-presentation" / "README.md",
        ]
        for entry_point in entry_points:
            with self.subTest(entry_point=entry_point.relative_to(REPO_ROOT)):
                text = entry_point.read_text(encoding="utf-8")
                self.assertIn("https://yila.ai/?utm_source=github", text)
                self.assertIn("utm_campaign=awesome-research-skills", text)

        for readme_name in ("README.md", "README_CN.md", "README_ja.md", "README_ko.md"):
            text = (REPO_ROOT / readme_name).read_text(encoding="utf-8")
            self.assertIn("assets/research-workflow-hero-yila.webp", text)


if __name__ == "__main__":
    unittest.main()
