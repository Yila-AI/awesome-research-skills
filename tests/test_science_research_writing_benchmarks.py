import json
import unittest
from pathlib import Path


CASES = (
    Path(__file__).parents[1]
    / "benchmarks"
    / "science-research-writing"
    / "test-cases.json"
)


class BenchmarkFixtureTests(unittest.TestCase):
    def test_cases_cover_required_routes_and_safety_failures(self):
        cases = json.loads(CASES.read_text(encoding="utf-8"))
        self.assertGreaterEqual(len(cases), 12)

        routes = {case["expected_route"] for case in cases}
        self.assertTrue({"plan", "draft", "revise", "audit"}.issubset(routes))

        checks = {check for case in cases for check in case["safety_checks"]}
        self.assertTrue(
            {
                "causal_overreach",
                "number_drift",
                "citation_fabrication",
                "null_result_loss",
            }.issubset(checks)
        )

        expected_fields = {
            "id",
            "task",
            "materials",
            "protected_terms",
            "expected_route",
            "required_facts",
            "forbidden_claims",
            "safety_checks",
        }
        for case in cases:
            self.assertEqual(set(case), expected_fields)

    def test_case_ids_are_unique(self):
        cases = json.loads(CASES.read_text(encoding="utf-8"))
        case_ids = [case["id"] for case in cases]
        self.assertEqual(len(case_ids), len(set(case_ids)))


if __name__ == "__main__":
    unittest.main()
