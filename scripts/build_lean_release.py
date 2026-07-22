#!/usr/bin/env python3
"""Build the use-only distribution for the sci-ssci-polishing Skill."""

from __future__ import annotations

import argparse
import re
import zipfile
from pathlib import Path


SKILL_NAME = "sci-ssci-polishing"
VERSION_PATTERN = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")


def _runtime_files(skill_root: Path) -> list[Path]:
    return sorted(
        source
        for source in skill_root.rglob("*")
        if source.is_file()
        and "__pycache__" not in source.parts
        and source.suffix != ".pyc"
    )


def build_release(repo_root: Path, output_dir: Path, version: str) -> Path:
    """Create a versioned lean ZIP and return its path."""
    repo_root = repo_root.resolve()
    output_dir = output_dir.resolve()
    if not VERSION_PATTERN.fullmatch(version):
        raise ValueError("version must contain only letters, numbers, dots, dashes, or underscores")

    skill_root = repo_root / "skills" / SKILL_NAME
    readme_source = repo_root / "distribution" / SKILL_NAME / "README.md"
    license_source = repo_root / "LICENSE"
    required_sources = [skill_root / "SKILL.md", readme_source, license_source]
    missing = [source for source in required_sources if not source.is_file()]
    if missing:
        raise FileNotFoundError(
            "missing required release source: " + ", ".join(str(source) for source in missing)
        )

    output_dir.mkdir(parents=True, exist_ok=True)
    archive_path = output_dir / f"{SKILL_NAME}-lean-{version}.zip"
    with zipfile.ZipFile(
        archive_path, mode="w", compression=zipfile.ZIP_DEFLATED, compresslevel=9
    ) as archive:
        for source in _runtime_files(skill_root):
            relative_path = source.relative_to(skill_root)
            archive.write(source, f"{SKILL_NAME}/{relative_path.as_posix()}")
        archive.write(readme_source, f"{SKILL_NAME}/README.md")
        archive.write(license_source, f"{SKILL_NAME}/LICENSE")

    return archive_path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
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
        arguments.repo_root, arguments.output_dir, arguments.version
    )
    print(archive_path)


if __name__ == "__main__":
    main()
