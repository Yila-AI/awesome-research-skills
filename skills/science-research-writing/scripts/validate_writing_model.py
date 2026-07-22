#!/usr/bin/env python3
"""Validate a copyright-safe target-journal writing model."""

import argparse
import json
from pathlib import Path


REQUIRED_TOP_LEVEL = {
    "schema_version": str,
    "model_name": str,
    "sources": list,
    "sections": dict,
    "validated": bool,
}
REQUIRED_FUNCTION_FIELDS = {
    "name": str,
    "evidence": list,
    "confidence": str,
    "exceptions": list,
}
PROHIBITED_FIELDS = {"copied_text", "verbatim", "full_text"}
CONFIDENCE_VALUES = {"low", "medium", "high"}


def find_prohibited_fields(value, path="$", errors=None):
    if errors is None:
        errors = []
    if isinstance(value, dict):
        for key, child in value.items():
            child_path = f"{path}.{key}"
            if key.lower() in PROHIBITED_FIELDS:
                errors.append(f"{child_path}: prohibited field")
            find_prohibited_fields(child, child_path, errors)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            find_prohibited_fields(child, f"{path}[{index}]", errors)
    return errors


def validate_model(model):
    errors = []
    if not isinstance(model, dict):
        return ["$: expected object"]

    for field, expected_type in REQUIRED_TOP_LEVEL.items():
        path = f"$.{field}"
        if field not in model:
            errors.append(f"{path}: missing required field")
        elif not isinstance(model[field], expected_type):
            errors.append(f"{path}: expected {expected_type.__name__}")

    sections = model.get("sections")
    if isinstance(sections, dict):
        for section_name, section in sections.items():
            section_path = f"$.sections.{section_name}"
            if not isinstance(section, dict):
                errors.append(f"{section_path}: expected object")
                continue
            functions = section.get("functions")
            if functions is None:
                errors.append(f"{section_path}.functions: missing required field")
                continue
            if not isinstance(functions, list):
                errors.append(f"{section_path}.functions: expected list")
                continue
            for index, function in enumerate(functions):
                function_path = f"{section_path}.functions[{index}]"
                if not isinstance(function, dict):
                    errors.append(f"{function_path}: expected object")
                    continue
                for field, expected_type in REQUIRED_FUNCTION_FIELDS.items():
                    path = f"{function_path}.{field}"
                    if field not in function:
                        errors.append(f"{path}: missing required field")
                    elif not isinstance(function[field], expected_type):
                        errors.append(f"{path}: expected {expected_type.__name__}")
                confidence = function.get("confidence")
                if isinstance(confidence, str) and confidence not in CONFIDENCE_VALUES:
                    errors.append(f"{function_path}.confidence: expected low, medium, or high")

    errors.extend(find_prohibited_fields(model))
    return errors


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("model", type=Path, help="Target-journal model JSON")
    args = parser.parse_args()
    model = json.loads(args.model.read_text(encoding="utf-8"))
    errors = validate_model(model)
    print(json.dumps({"valid": not errors, "errors": errors}, indent=2))
    raise SystemExit(1 if errors else 0)


if __name__ == "__main__":
    main()
