import importlib.util
import unittest
from pathlib import Path


SCRIPT = (
    Path(__file__).parents[1]
    / "skills"
    / "sci-ssci-polishing"
    / "scripts"
    / "check_invariants.py"
)


def load_module():
    spec = importlib.util.spec_from_file_location("check_invariants", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class CheckInvariantsTests(unittest.TestCase):
    def test_decimal_percentage_is_one_number_token(self):
        module = load_module()

        numbers = module.extract_numbers("Accuracy was 87.08% in 612 participants.")

        self.assertEqual(dict(numbers), {"87.08%": 1, "612": 1})

    def test_accepts_reordering_with_identical_invariants(self):
        module = load_module()
        source = (
            "In 612 participants, Model-A7 improved accuracy from 84.79% to "
            "87.08% (Li & Chen, 2023)."
        )
        revision = (
            "Model-A7 improved accuracy from 84.79% to 87.08% among 612 "
            "participants (Li & Chen, 2023)."
        )

        audit = module.audit_texts(source, revision, ["Model-A7"])

        self.assertTrue(audit["passed"])

    def test_rejects_changed_percentage_and_dropped_citation(self):
        module = load_module()

        audit = module.audit_texts(
            "The score was 92.08% [17].",
            "The score was 93.08%.",
            [],
        )

        self.assertFalse(audit["passed"])
        self.assertFalse(audit["numbers_preserved"])
        self.assertFalse(audit["citations_preserved"])

    def test_rejects_dropped_protected_term(self):
        module = load_module()

        audit = module.audit_texts(
            "Values were normalized to GAPDH.",
            "Values were normalized.",
            ["GAPDH"],
        )

        self.assertFalse(audit["passed"])
        self.assertFalse(audit["protected_terms_preserved"])

    def test_short_term_uses_word_boundaries(self):
        module = load_module()

        counts = module.protected_term_counts(
            "AI evidence remains limited.",
            ["AI"],
        )

        self.assertEqual(counts["AI"], 1)


if __name__ == "__main__":
    unittest.main()
