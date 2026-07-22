#!/usr/bin/env python3
"""Audit exact tokens and semantic markers between research materials and a draft."""

import argparse
import json
import re
from collections import Counter
from pathlib import Path


NUMBER_RE = re.compile(
    r"(?<![A-Za-z])(?:\d+(?:,\d{3})*(?:\.\d+)?|\.\d+)(?:%|\s*(?:ms|μM|mg|kg|cm|mm))?"
)
SQUARE_CITATION_RE = re.compile(r"\[(?:\d+[–—\-,;\s]*)+\]")
AUTHOR_YEAR_RE = re.compile(
    r"\([^()]*\b(?:19|20)\d{2}[a-z]?\b[^()]*\)", re.IGNORECASE
)
MARKER_PATTERNS = {
    "uncertainty": re.compile(
        r"\b(?:may|might|could|suggests?|appears?|is consistent with)\b", re.IGNORECASE
    ),
    "association": re.compile(
        r"\b(?:is|was|were|are) associated with\b|\brelates? to\b|\brelated to\b",
        re.IGNORECASE,
    ),
    "prediction": re.compile(r"\bpredicts?|\bpredicted\b", re.IGNORECASE),
    "contribution": re.compile(r"\bcontributes?|\bcontributed\b", re.IGNORECASE),
    "effect": re.compile(r"\baffects?|\bleads? to\b|\bled to\b", re.IGNORECASE),
    "causation": re.compile(
        r"\bcauses?|\bcaused\b|\bdemonstrates? that\b|\bdemonstrated that\b|\bproves?\b",
        re.IGNORECASE,
    ),
    "null_result": re.compile(
        r"\bno difference\b|\bnot associated\b|\bdid not\b|\bnon[- ]significant\b",
        re.IGNORECASE,
    ),
    "negation": re.compile(r"\b(?:no|not|neither|without|never)\b", re.IGNORECASE),
}
STRENGTH_GROUPS = {"uncertainty", "association", "prediction", "contribution", "effect", "causation"}


def normalize_token(token):
    return re.sub(r"\s+", " ", token.replace("–", "-").replace("—", "-")).strip()


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
            pattern += r"(?!\w)"
        counts[term] = len(re.findall(pattern, text, flags=re.IGNORECASE))
    return counts


def extract_markers(text):
    return {name: len(pattern.findall(text)) for name, pattern in MARKER_PATTERNS.items()}


def audit_texts(source, draft, protected_terms):
    source_numbers = extract_numbers(source)
    draft_numbers = extract_numbers(draft)
    source_citations = extract_citations(source)
    draft_citations = extract_citations(draft)
    source_terms = protected_term_counts(source, protected_terms)
    draft_terms = protected_term_counts(draft, protected_terms)
    source_markers = extract_markers(source)
    draft_markers = extract_markers(draft)
    marker_differences = {
        name: {"source": source_markers[name], "draft": draft_markers[name]}
        for name in MARKER_PATTERNS
        if source_markers[name] != draft_markers[name]
    }

    result = {
        "numbers_preserved": source_numbers == draft_numbers,
        "citations_preserved": source_citations == draft_citations,
        "protected_terms_preserved": source_terms == draft_terms,
        "source_numbers": dict(source_numbers),
        "draft_numbers": dict(draft_numbers),
        "source_citations": dict(source_citations),
        "draft_citations": dict(draft_citations),
        "source_protected_terms": source_terms,
        "draft_protected_terms": draft_terms,
        "source_markers": source_markers,
        "draft_markers": draft_markers,
        "marker_differences": marker_differences,
        "claim_strength_changed": bool(STRENGTH_GROUPS.intersection(marker_differences)),
        "semantic_review_required": bool(marker_differences),
    }
    result["passed"] = all(
        result[key]
        for key in ("numbers_preserved", "citations_preserved", "protected_terms_preserved")
    )
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("case", type=Path, help="JSON with source, draft, and protected_terms")
    args = parser.parse_args()
    case = json.loads(args.case.read_text(encoding="utf-8"))
    result = audit_texts(case["source"], case["draft"], case.get("protected_terms", []))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(0 if result["passed"] else 1)


if __name__ == "__main__":
    main()
