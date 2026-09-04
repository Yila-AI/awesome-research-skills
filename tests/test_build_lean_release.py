import tempfile
import unittest
import zipfile
from pathlib import Path

from scripts.build_lean_release import build_release, discover_skill_names


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = REPO_ROOT / "skills" / "sci-ssci-polishing"


class LeanReleaseTests(unittest.TestCase):
    def test_archive_contains_complete_runtime_skill_and_distribution_files(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            archive_path = build_release(
                REPO_ROOT, Path(temporary_directory), "v1.0.0"
            )

            self.assertEqual(
                archive_path.name, "sci-ssci-polishing-lean-v1.0.0.zip"
            )
            with zipfile.ZipFile(archive_path) as archive:
                archived_files = {
                    name for name in archive.namelist() if not name.endswith("/")
                }

            expected_skill_files = {
                f"sci-ssci-polishing/{source.relative_to(SKILL_ROOT).as_posix()}"
                for source in SKILL_ROOT.rglob("*")
                if source.is_file() and "__pycache__" not in source.parts
            }
            self.assertTrue(expected_skill_files.issubset(archived_files))
            self.assertIn("sci-ssci-polishing/README.md", archived_files)
            self.assertIn("sci-ssci-polishing/LICENSE", archived_files)

    def test_archive_excludes_research_only_and_generated_files(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            archive_path = build_release(
                REPO_ROOT, Path(temporary_directory), "v1.0.0"
            )

            with zipfile.ZipFile(archive_path) as archive:
                archived_files = archive.namelist()

            excluded_components = {
                "assets",
                "benchmarks",
                "corpus",
                "docs",
                "examples",
                "__pycache__",
            }
            for archived_file in archived_files:
                self.assertTrue(archived_file.startswith("sci-ssci-polishing/"))
                self.assertTrue(excluded_components.isdisjoint(Path(archived_file).parts))
                self.assertFalse(archived_file.endswith(".pyc"))

    def test_rejects_unsafe_version_text(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            with self.assertRaisesRegex(ValueError, "version"):
                build_release(REPO_ROOT, Path(temporary_directory), "../latest")

    def test_rejects_non_semantic_version(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            with self.assertRaisesRegex(ValueError, "semantic"):
                build_release(REPO_ROOT, Path(temporary_directory), "latest")

    def test_builds_every_installable_skill(self):
        expected_skills = {
            "academic-humanizer",
            "research-presentation",
            "sci-ssci-polishing",
            "science-research-writing",
        }
        self.assertEqual(set(discover_skill_names(REPO_ROOT)), expected_skills)
        with tempfile.TemporaryDirectory() as temporary_directory:
            for skill_name in expected_skills:
                with self.subTest(skill=skill_name):
                    archive_path = build_release(
                        REPO_ROOT,
                        Path(temporary_directory),
                        "v1.0.0",
                        skill_name,
                    )
                    self.assertEqual(
                        archive_path.name,
                        f"{skill_name}-lean-v1.0.0.zip",
                    )
                    with zipfile.ZipFile(archive_path) as archive:
                        archived_files = archive.namelist()
                    self.assertIn(f"{skill_name}/SKILL.md", archived_files)
                    self.assertIn(f"{skill_name}/README.md", archived_files)
                    self.assertIn(f"{skill_name}/LICENSE", archived_files)

    def test_rejects_unknown_skill(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            with self.assertRaisesRegex(ValueError, "unknown Skill"):
                build_release(
                    REPO_ROOT,
                    Path(temporary_directory),
                    "v1.0.0",
                    "not-a-skill",
                )

    def test_release_workflow_runs_tests_and_publishes_the_archive(self):
        workflow_path = REPO_ROOT / ".github" / "workflows" / "release-lean-skill.yml"
        workflow = workflow_path.read_text(encoding="utf-8")

        for skill_name in discover_skill_names(REPO_ROOT):
            self.assertIn(f'"{skill_name}-v*"', workflow)
        self.assertIn("contents: write", workflow)
        self.assertIn("python3 -m unittest discover -s tests -v", workflow)
        self.assertIn("scripts/build_lean_release.py", workflow)
        self.assertIn('--skill "$skill_name"', workflow)
        self.assertIn("sha256sum", workflow)
        self.assertIn("gh release create", workflow)
        self.assertIn("https://yila.ai/?utm_source=github", workflow)
        self.assertIn("utm_medium=release", workflow)

    def test_both_readmes_explain_selective_install_and_lean_download(self):
        for readme_name in ("README.md", "README_CN.md"):
            with self.subTest(readme=readme_name):
                readme = (REPO_ROOT / readme_name).read_text(encoding="utf-8")
                self.assertIn("--skill sci-ssci-polishing", readme)
                self.assertIn("--skill academic-humanizer", readme)
                self.assertIn("--skill research-presentation", readme)
                self.assertIn("--skill science-research-writing", readme)
                self.assertIn(
                    "https://github.com/Yila-AI/awesome-research-skills/releases",
                    readme,
                )


if __name__ == "__main__":
    unittest.main()
