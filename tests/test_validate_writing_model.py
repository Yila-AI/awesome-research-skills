import importlib.util
import unittest
from pathlib import Path


SCRIPT = (
    Path(__file__).parents[1]
    / "skills"
    / "science-research-writing"
    / "scripts"
    / "validate_writing_model.py"
)


def load_module():
    spec = importlib.util.spec_from_file_location("validate_writing_model", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def valid_model():
    return {
        "schema_version": "1.0",
        "model_name": "journal-discussion",
        "sources": [{"id": "paper-1", "year": 2025, "article_type": "Article"}],
        "sections": {
            "discussion": {
                "functions": [
                    {
                        "name": "state principal finding",
                        "evidence": ["paper-1:discussion:p1"],
                        "confidence": "medium",
                        "exceptions": [],
                    }
                ]
            }
        },
        "validated": True,
    }


class WritingModelValidatorTests(unittest.TestCase):
    def test_accepts_valid_model(self):
        module = load_module()
        self.assertEqual(module.validate_model(valid_model()), [])

    def test_reports_missing_schema_version(self):
        module = load_module()
        model = valid_model()
        del model["schema_version"]
        self.assertIn("$.schema_version: missing required field", module.validate_model(model))

    def test_rejects_non_list_sources(self):
        module = load_module()
        model = valid_model()
        model["sources"] = "paper-1"
        self.assertIn("$.sources: expected list", module.validate_model(model))

    def test_reports_missing_function_field(self):
        module = load_module()
        model = valid_model()
        del model["sections"]["discussion"]["functions"][0]["exceptions"]
        self.assertIn(
            "$.sections.discussion.functions[0].exceptions: missing required field",
            module.validate_model(model),
        )

    def test_rejects_copied_text_anywhere(self):
        module = load_module()
        model = valid_model()
        model["sources"][0]["copied_text"] = "A copied sentence."
        self.assertIn("$.sources[0].copied_text: prohibited field", module.validate_model(model))


if __name__ == "__main__":
    unittest.main()
