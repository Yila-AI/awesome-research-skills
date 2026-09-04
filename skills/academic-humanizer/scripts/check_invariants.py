#!/usr/bin/env python3
"""Check deterministic invariants between source and humanized academic prose."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path


NUMBER_RE = re.compile(
    r"(?<![A-Za-z])(?:[+−-]?±?\d+(?:,\d{3})*(?:\.\d+)?|\.\d+)"
    r"(?:\s*(?:%|‰|μM|mg|g|kg|mL|L|mm|cm|m|km|Hz|kHz|MHz|°C))?"
)
SQUARE_CITATION_RE = re.compile(r"\[(?:\d+[\u2013\u2014\-,;\s]*)+\]")
AUTHOR_YEAR_RE = re.compile(
    r"\([^()]*\b(?:19|20)\d{2}[a-z]?\b[^()]*\)", re.IGNORECASE
)
TEX_CITATION_RE = re.compile(r"\\cite[a-zA-Z*]*\{[^{}]+\}")
REFERENCE_LABEL_RE = re.compile(
    r"\b(?:Fig(?:ure)?\.?|Table|Eq(?:uation)?\.?|Section|Appendix)\s*"
    r"(?:S?\d+(?:\.\d+)*(?:[A-Za-z])?)"
    r"|(?:图|表|公式|附录)\s*[（(]?[A-Za-z]?\d+(?:\.\d+)*(?:[A-Za-z])?[）)]?",
    re.IGNORECASE,
)


def normalize_token(token: str) -> str:
    return re.sub(
        r"\s+",
        " ",
        token.replace("\u2013", "-")
        .replace("\u2014", "-")
        .replace("\u2212", "-"),
    ).strip()


def extract_numbers(text: str) -> Counter[str]:
    return Counter(normalize_token(match.group(0)) for match in NUMBER_RE.finditer(text))


def extract_citations(text: str) -> Counter[str]:
    matches = [match.group(0) for match in SQUARE_CITATION_RE.finditer(text)]
    matches.extend(match.group(0) for match in AUTHOR_YEAR_RE.finditer(text))
    matches.extend(match.group(0) for match in TEX_CITATION_RE.finditer(text))
    return Counter(normalize_token(item) for item in matches)


def extract_reference_labels(text: str) -> Counter[str]:
    return Counter(
        normalize_token(match.group(0)).lower()
        for match in REFERENCE_LABEL_RE.finditer(text)
    )


def protected_term_counts(text: str, protected_terms: list[str]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for term in protected_terms:
        pattern = re.escape(term)
        if term and term[0].isalnum():
            pattern = r"(?<!\w)" + pattern
        if term and term[-1].isalnum():
            pattern += r"(?!\w)"
        counts[term] = len(re.findall(pattern, text, flags=re.IGNORECASE))
    return counts


def audit_texts(
    source: str, revision: str, protected_terms: list[str]
) -> dict[str, object]:
    source_numbers = extract_numbers(source)
    revision_numbers = extract_numbers(revision)
    source_citations = extract_citations(source)
    revision_citations = extract_citations(revision)
    source_labels = extract_reference_labels(source)
    revision_labels = extract_reference_labels(revision)
    source_terms = protected_term_counts(source, protected_terms)
    revision_terms = protected_term_counts(revision, protected_terms)

    result: dict[str, object] = {
        "numbers_preserved": source_numbers == revision_numbers,
        "citations_preserved": source_citations == revision_citations,
        "reference_labels_preserved": source_labels == revision_labels,
        "protected_terms_preserved": source_terms == revision_terms,
        "source_numbers": dict(source_numbers),
        "revision_numbers": dict(revision_numbers),
        "source_citations": dict(source_citations),
        "revision_citations": dict(revision_citations),
        "source_reference_labels": dict(source_labels),
        "revision_reference_labels": dict(revision_labels),
        "source_protected_terms": source_terms,
        "revision_protected_terms": revision_terms,
    }
    result["passed"] = all(
        result[key]
        for key in (
            "numbers_preserved",
            "citations_preserved",
            "reference_labels_preserved",
            "protected_terms_preserved",
        )
    )
    return result


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Compare exact academic content tokens before and after revision."
    )
    parser.add_argument(
        "case", type=Path, help="JSON with source, revision, and optional protected_terms"
    )
    arguments = parser.parse_args()
    case = json.loads(arguments.case.read_text(encoding="utf-8"))
    result = audit_texts(
        case["source"], case["revision"], case.get("protected_terms", [])
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
