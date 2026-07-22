import importlib.util
import unittest
from pathlib import Path


SCRIPT = (
    Path(__file__).parents[1]
    / "skills"
    / "science-research-writing"
    / "scripts"
    / "check_draft_invariants.py"
)


def load_module():
    spec = importlib.util.spec_from_file_location("check_draft_invariants", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class DraftInvariantTests(unittest.TestCase):
    def test_accepts_reordering_with_preserved_tokens_and_markers(self):
        module = load_module()
        source = "Among 612 students, Model-B was associated with GPA (Li, 2024)."
        draft = "Model-B was associated with GPA among 612 students (Li, 2024)."
        audit = module.audit_texts(source, draft, ["Model-B"])
        self.assertTrue(audit["passed"])
        self.assertFalse(audit["semantic_review_required"])

    def test_fails_changed_number(self):
        module = load_module()
        audit = module.audit_texts("The estimate was 1.31.", "The estimate was 1.13.", [])
        self.assertFalse(audit["passed"])
        self.assertFalse(audit["numbers_preserved"])

    def test_fails_removed_citation(self):
        module = load_module()
        audit = module.audit_texts("The pattern persisted [12].", "The pattern persisted.", [])
        self.assertFalse(audit["passed"])
        self.assertFalse(audit["citations_preserved"])

    def test_fails_removed_protected_term(self):
        module = load_module()
        audit = module.audit_texts("Model-B predicted relapse.", "The model predicted relapse.", ["Model-B"])
        self.assertFalse(audit["passed"])
        self.assertFalse(audit["protected_terms_preserved"])

    def test_flags_association_strengthened_to_causation(self):
        module = load_module()
        audit = module.audit_texts(
            "Treatment was associated with recovery.",
            "Treatment caused recovery.",
            [],
        )
        self.assertTrue(audit["passed"])
        self.assertTrue(audit["semantic_review_required"])
        self.assertTrue(audit["claim_strength_changed"])

    def test_flags_causation_weakened_to_association(self):
        module = load_module()
        audit = module.audit_texts(
            "Randomization demonstrated that treatment caused recovery.",
            "Treatment was associated with recovery.",
            [],
        )
        self.assertTrue(audit["semantic_review_required"])
        self.assertTrue(audit["claim_strength_changed"])

    def test_flags_removed_null_result_marker(self):
        module = load_module()
        audit = module.audit_texts(
            "There was no difference in retention (p = 0.61).",
            "Retention was evaluated (p = 0.61).",
            [],
        )
        self.assertTrue(audit["passed"])
        self.assertTrue(audit["semantic_review_required"])
        self.assertIn("null_result", audit["marker_differences"])


if __name__ == "__main__":
    unittest.main()
