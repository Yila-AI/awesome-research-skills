import unittest
from pathlib import Path


ROOT = (
    Path(__file__).parents[1]
    / "skills"
    / "science-research-writing"
    / "references"
)
SECTIONS = [
    "introduction",
    "methods",
    "results",
    "discussion",
    "conclusion",
    "abstract",
    "title",
]
HEADINGS = [
    "Reader expectation",
    "Required functions",
    "Target-paper observations",
    "Section boundaries",
    "Failure modes",
    "Final audit",
]


class SectionReferenceTests(unittest.TestCase):
    def test_every_section_has_the_required_contract(self):
        for section in SECTIONS:
            text = (ROOT / f"{section}.md").read_text(encoding="utf-8")
            for heading in HEADINGS:
                self.assertIn(f"## {heading}", text, f"{section}: {heading}")


if __name__ == "__main__":
    unittest.main()
