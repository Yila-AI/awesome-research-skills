#!/usr/bin/env python3
"""Build a versioned, use-only distribution for one repository Skill."""

from __future__ import annotations

import argparse
import re
import zipfile
from pathlib import Path


DEFAULT_SKILL_NAME = "sci-ssci-polishing"
VERSION_PATTERN = re.compile(
    r"^v?(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)"
    r"(?:-[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?"
    r"(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?$"
)
SKILL_NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def _runtime_files(skill_root: Path) -> list[Path]:
    return sorted(
        source
        for source in skill_root.rglob("*")
        if source.is_file()
        and "__pycache__" not in source.parts
        and source.suffix != ".pyc"
    )


def discover_skill_names(repo_root: Path) -> tuple[str, ...]:
    """Return every installable Skill directory in stable order."""
    skills_root = repo_root.resolve() / "skills"
    if not skills_root.is_dir():
        return ()
    return tuple(
        path.name
        for path in sorted(skills_root.iterdir())
        if path.is_dir() and (path / "SKILL.md").is_file()
    )


def build_release(
    repo_root: Path,
    output_dir: Path,
    version: str,
    skill_name: str = DEFAULT_SKILL_NAME,
) -> Path:
    """Create a versioned lean ZIP and return its path."""
    repo_root = repo_root.resolve()
    output_dir = output_dir.resolve()
    if not VERSION_PATTERN.fullmatch(version):
        raise ValueError("version must be semantic, for example v1.2.0 or v1.2.0-rc.1")
    if not SKILL_NAME_PATTERN.fullmatch(skill_name):
        raise ValueError("skill name must contain lowercase letters, numbers, and single hyphens")
    available_skills = discover_skill_names(repo_root)
    if skill_name not in available_skills:
        available = ", ".join(available_skills) or "none"
        raise ValueError(f"unknown Skill {skill_name!r}; available Skills: {available}")

    skill_root = repo_root / "skills" / skill_name
    readme_source = repo_root / "distribution" / skill_name / "README.md"
    license_source = repo_root / "LICENSE"
    required_sources = [skill_root / "SKILL.md", readme_source, license_source]
    missing = [source for source in required_sources if not source.is_file()]
    if missing:
        raise FileNotFoundError(
            "missing required release source: " + ", ".join(str(source) for source in missing)
        )

    output_dir.mkdir(parents=True, exist_ok=True)
    archive_path = output_dir / f"{skill_name}-lean-{version}.zip"
    with zipfile.ZipFile(
        archive_path, mode="w", compression=zipfile.ZIP_DEFLATED, compresslevel=9
    ) as archive:
        for source in _runtime_files(skill_root):
            relative_path = source.relative_to(skill_root)
            archive.write(source, f"{skill_name}/{relative_path.as_posix()}")
        archive.write(readme_source, f"{skill_name}/README.md")
        archive.write(license_source, f"{skill_name}/LICENSE")

    return archive_path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--skill",
        default=DEFAULT_SKILL_NAME,
        help="Skill directory name (defaults to sci-ssci-polishing)",
    )
    parser.add_argument("--version", required=True, help="Release version, for example v1.0.0")
    parser.add_argument(
        "--output-dir", type=Path, default=Path("dist"), help="Archive output directory"
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Repository root",
    )
    arguments = parser.parse_args()
    archive_path = build_release(
        arguments.repo_root,
        arguments.output_dir,
        arguments.version,
        arguments.skill,
    )
    print(archive_path)


if __name__ == "__main__":
    main()
