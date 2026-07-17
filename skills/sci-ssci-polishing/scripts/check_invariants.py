#!/usr/bin/env python3
"""Check deterministic content invariants between source and revised prose."""

import argparse
import json
import re
from collections import Counter
from pathlib import Path


NUMBER_RE = re.compile(
    r"(?<![A-Za-z])(?:\d+(?:,\d{3})*(?:\.\d+)?|\.\d+)(?:%|\s*\u03bcM)?"
)
SQUARE_CITATION_RE = re.compile(r"\[(?:\d+[\u2013\u2014\-,;\s]*)+\]")
AUTHOR_YEAR_RE = re.compile(
    r"\([^()]*\b(?:19|20)\d{2}[a-z]?\b[^()]*\)", re.IGNORECASE
)


def normalize_token(token):
    return re.sub(r"\s+", " ", token.replace("\u2013", "-").replace("\u2014", "-")).strip()


def extract_numbers(text):
    return Counter(normalize_token(match.group(0)) for match in NUMBER_RE.finditer(text))


def extract_citations(text):
    matches = [match.group(0) for match in SQUARE_CITATION_RE.finditer(text)]
    matches.extend(match.group(0) for match in AUTHOR_YEAR_RE.finditer(text))
    return Counter(normalize_token(item) for item in matches)


def protected_term_counts(text, protected_terms):
    counts = {}
    for term in protected_terms:
        pattern = re.escape(term)
        if term and term[0].isalnum():
            pattern = r"(?<!\w)" + pattern
        if term and term[-1].isalnum():
            pattern = pattern + r"(?!\w)"
        counts[term] = len(re.findall(pattern, text, flags=re.IGNORECASE))
    return counts


def audit_texts(source, revision, protected_terms):
    source_numbers = extract_numbers(source)
    revision_numbers = extract_numbers(revision)
    source_citations = extract_citations(source)
    revision_citations = extract_citations(revision)
    source_terms = protected_term_counts(source, protected_terms)
    revision_terms = protected_term_counts(revision, protected_terms)

    result = {
        "numbers_preserved": source_numbers == revision_numbers,
        "citations_preserved": source_citations == revision_citations,
        "protected_terms_preserved": source_terms == revision_terms,
        "source_numbers": dict(source_numbers),
        "revision_numbers": dict(revision_numbers),
        "source_citations": dict(source_citations),
        "revision_citations": dict(revision_citations),
        "source_protected_terms": source_terms,
        "revision_protected_terms": revision_terms,
    }
    result["passed"] = all(
        result[key]
        for key in (
            "numbers_preserved",
            "citations_preserved",
            "protected_terms_preserved",
        )
    )
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("case", type=Path, help="JSON with source, revision, and protected_terms")
    args = parser.parse_args()
    case = json.loads(args.case.read_text(encoding="utf-8"))
    result = audit_texts(
        case["source"], case["revision"], case.get("protected_terms", [])
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(0 if result["passed"] else 1)


if __name__ == "__main__":
    main()
