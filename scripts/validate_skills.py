#!/usr/bin/env python3
"""Validate installable Skill entrypoints and their local runtime references."""

from __future__ import annotations

import re
from pathlib import Path


NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FRONTMATTER_FIELD_RE = re.compile(r"^([a-z][a-z0-9-]*):\s*(.*?)\s*$")
RESOURCE_REFERENCE_RE = re.compile(
    r"`((?:references|scripts|assets)/[^`\s]+)`"
)
INTERFACE_FIELD_RE = re.compile(
    r'^\s{2}(display_name|short_description|default_prompt):\s*["\'](.+)["\']\s*$',
    re.MULTILINE,
)


def parse_frontmatter(skill_file: Path) -> tuple[dict[str, str], str, list[str]]:
    text = skill_file.read_text(encoding="utf-8")
    lines = text.splitlines()
    errors: list[str] = []
    if not lines or lines[0].strip() != "---":
        return {}, text, [f"{skill_file}: missing opening YAML delimiter"]

    try:
        closing_index = next(
            index for index, line in enumerate(lines[1:], start=1) if line.strip() == "---"
        )
    except StopIteration:
        return {}, text, [f"{skill_file}: missing closing YAML delimiter"]

    fields: dict[str, str] = {}
    for line in lines[1:closing_index]:
        match = FRONTMATTER_FIELD_RE.match(line)
        if match:
            fields[match.group(1)] = match.group(2).strip('"\'')
    body = "\n".join(lines[closing_index + 1 :]).strip()
    if not body:
        errors.append(f"{skill_file}: Markdown body is empty")
    return fields, body, errors


def validate_skill(skill_root: Path) -> list[str]:
    errors: list[str] = []
    skill_file = skill_root / "SKILL.md"
    if not skill_file.is_file():
        return [f"{skill_root}: missing SKILL.md"]

    fields, body, parse_errors = parse_frontmatter(skill_file)
    errors.extend(parse_errors)
    name = fields.get("name", "")
    description = fields.get("description", "")

    if not NAME_RE.fullmatch(name):
        errors.append(f"{skill_file}: invalid or missing name {name!r}")
    elif name != skill_root.name:
        errors.append(
            f"{skill_file}: name {name!r} does not match directory {skill_root.name!r}"
        )
    if not description:
        errors.append(f"{skill_file}: missing description")
    elif len(description) > 1024:
        errors.append(f"{skill_file}: description exceeds 1024 characters")

    for relative_reference in RESOURCE_REFERENCE_RE.findall(body):
        target = skill_root / relative_reference.rstrip(".,;:")
        if not target.exists():
            errors.append(f"{skill_file}: missing referenced resource {relative_reference}")

    interface_file = skill_root / "agents" / "openai.yaml"
    if not interface_file.is_file():
        errors.append(f"{skill_root}: missing agents/openai.yaml")
    else:
        interface_text = interface_file.read_text(encoding="utf-8")
        interface_fields = dict(INTERFACE_FIELD_RE.findall(interface_text))
        for field in ("display_name", "short_description", "default_prompt"):
            if not interface_fields.get(field):
                errors.append(f"{interface_file}: missing interface.{field}")
        default_prompt = interface_fields.get("default_prompt", "")
        if name and f"${name}" not in default_prompt:
            errors.append(
                f"{interface_file}: default_prompt must invoke ${name}"
            )

    return errors


def validate_repository(repo_root: Path) -> list[str]:
    skills_root = repo_root.resolve() / "skills"
    if not skills_root.is_dir():
        return [f"{skills_root}: missing skills directory"]
    skill_directories = [
        path
        for path in sorted(skills_root.iterdir())
        if path.is_dir() and (path / "SKILL.md").is_file()
    ]
    if not skill_directories:
        return [f"{skills_root}: no installable Skills found"]

    errors: list[str] = []
    for skill_root in skill_directories:
        errors.extend(validate_skill(skill_root))
    return errors


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    errors = validate_repository(repo_root)
    if errors:
        print("Skill validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    skill_count = len(tuple((repo_root / "skills").glob("*/SKILL.md")))
    print(f"Validated {skill_count} installable Skills.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
