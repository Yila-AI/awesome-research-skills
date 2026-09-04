import importlib.util
import json
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = REPO_ROOT / "skills" / "academic-humanizer"
CHECKER_PATH = SKILL_ROOT / "scripts" / "check_invariants.py"
CASES_PATH = REPO_ROOT / "benchmarks" / "academic-humanizer" / "reference-cases.json"


def load_checker_module():
    spec = importlib.util.spec_from_file_location(
        "academic_humanizer_invariant_checker", CHECKER_PATH
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


CHECKER = load_checker_module()


class AcademicHumanizerTests(unittest.TestCase):
    def test_reference_revisions_preserve_deterministic_invariants(self):
        cases = json.loads(CASES_PATH.read_text(encoding="utf-8"))
        for case in cases:
            with self.subTest(case=case["id"]):
                result = CHECKER.audit_texts(
                    case["source"], case["revision"], case["protected_terms"]
                )
                self.assertTrue(result["passed"], result)

    def test_reference_revisions_remove_targeted_template_patterns(self):
        cases = json.loads(CASES_PATH.read_text(encoding="utf-8"))
        for case in cases:
            with self.subTest(case=case["id"]):
                for pattern in case["removed_patterns"]:
                    self.assertIn(pattern, case["source"])
                    self.assertNotIn(pattern, case["revision"])

    def test_changed_number_fails_the_gate(self):
        source = "Model-A reached 87.08% accuracy among 612 participants [12]."
        revision = "Model-A reached 88.08% accuracy among 612 participants [12]."
        result = CHECKER.audit_texts(source, revision, ["Model-A"])
        self.assertFalse(result["passed"])
        self.assertFalse(result["numbers_preserved"])

    def test_changed_reference_type_fails_the_gate(self):
        source = "The gain is reported in Figure 3."
        revision = "The gain is reported in Table 3."
        result = CHECKER.audit_texts(source, revision, [])
        self.assertFalse(result["passed"])
        self.assertFalse(result["reference_labels_preserved"])

    def test_removed_tex_citation_fails_the_gate(self):
        source = r"The estimate follows prior work \\cite{lee2025}."
        revision = "The estimate follows prior work."
        result = CHECKER.audit_texts(source, revision, [])
        self.assertFalse(result["passed"])
        self.assertFalse(result["citations_preserved"])

    def test_voice_calibration_is_optional_and_disclosure_boundary_is_explicit(self):
        skill_text = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("voice-calibration.md", skill_text)
        self.assertIn("Without author samples", skill_text)
        self.assertIn("Do not claim or guarantee", skill_text)
        self.assertIn("detector", skill_text.lower())


if __name__ == "__main__":
    unittest.main()
