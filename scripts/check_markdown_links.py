#!/usr/bin/env python3
"""Check repository Markdown files for broken relative links and images."""

from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote, urlsplit


FENCED_CODE_RE = re.compile(r"```.*?```", re.DOTALL)
MARKDOWN_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
HTML_LINK_RE = re.compile(r'(?:href|src)=["\']([^"\']+)["\']')
EXTERNAL_SCHEMES = {"http", "https", "mailto", "data"}


def extract_targets(text: str) -> list[str]:
    text_without_code = FENCED_CODE_RE.sub("", text)
    targets = [match.group(1).strip() for match in MARKDOWN_LINK_RE.finditer(text_without_code)]
    targets.extend(match.group(1).strip() for match in HTML_LINK_RE.finditer(text_without_code))
    return targets


def normalize_target(raw_target: str) -> str | None:
    target = raw_target
    if target.startswith("<") and ">" in target:
        target = target[1 : target.index(">")]
    else:
        target = target.split(maxsplit=1)[0]
    if not target or target.startswith("#") or target.startswith("//"):
        return None
    parsed = urlsplit(target)
    if parsed.scheme.lower() in EXTERNAL_SCHEMES:
        return None
    path = unquote(parsed.path)
    return path or None


def find_broken_links(repo_root: Path) -> list[str]:
    repo_root = repo_root.resolve()
    errors: list[str] = []
    for markdown_file in sorted(repo_root.rglob("*.md")):
        if ".git" in markdown_file.parts:
            continue
        text = markdown_file.read_text(encoding="utf-8")
        for raw_target in extract_targets(text):
            relative_target = normalize_target(raw_target)
            if relative_target is None:
                continue
            target_path = (markdown_file.parent / relative_target).resolve()
            try:
                target_path.relative_to(repo_root)
            except ValueError:
                errors.append(
                    f"{markdown_file.relative_to(repo_root)}: link escapes repository: {raw_target}"
                )
                continue
            if not target_path.exists():
                errors.append(
                    f"{markdown_file.relative_to(repo_root)}: missing target: {raw_target}"
                )
    return errors


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    errors = find_broken_links(repo_root)
    if errors:
        print("Broken local Markdown links:")
        for error in errors:
            print(f"- {error}")
        return 1
    markdown_count = sum(1 for path in repo_root.rglob("*.md") if ".git" not in path.parts)
    print(f"Checked relative links in {markdown_count} Markdown files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
