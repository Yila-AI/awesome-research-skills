# Output contract

Return the result in this order.

## 1. Polished text

Provide clean, publication-ready English. Do not insert annotations inside the prose unless the user requests tracked changes.

For Chinese input, output English only by default. Preserve established English technical terms supplied by the author.

## 2. Key changes

Use 2-5 bullets for a paragraph and up to 8 for a full section. Describe meaningful language or organization changes, such as:

- clarified the subject-action relation;
- moved the principal result before its interpretation;
- reduced redundant setup;
- standardized terminology;
- improved cross-paragraph progression.

Do not claim “improved scientific rigor” when only language was edited.

## 3. Preservation audit

Always include a compact audit:

```text
Preservation audit
- Numbers/statistics: Preserved
- Technical terms/entities: Preserved
- Citations: Preserved / Not present
- Claim and causal strength: Preserved
- Limitations/conclusions: Preserved / Not present
```

If exact preservation cannot be confirmed, replace `Preserved` with `Query` and explain why.

## 4. Author queries

Include only when a source ambiguity or apparent inconsistency affects meaning. Number each query and quote only the minimum source fragment needed to identify the issue.

Do not silently “correct” a scientific inconsistency.

## Optional tracked format

When requested, add a concise source-to-revision table after the clean text:

| Source segment | Revision | Reason |
|---|---|---|
| Short fragment | Revised fragment | Grammar / clarity / coherence |

Keep the clean revised text first.
