# Frozen blind evaluation — Skill v2

Date: 2026-07-17

Packaging note: the frozen evaluation package used the development identifier `sci-ssci-writing-skill`. The public release later renamed the package to `sci-ssci-polishing`, removed an institution name from the corpus-provenance wording, and corrected decimal tokenization in the deterministic audit helper. Regression tests cover the helper correction. These packaging edits did not change the polishing workflow, preservation rules, rhetorical routing, or output contract evaluated below.

## Freeze integrity

- Skill package SHA-256 at freeze: `db5b85063beba40a9749927648a32fddb23a1bef5a348636d4ebfe5084769b60`.
- Skill package SHA-256 immediately before scoring: `db5b85063beba40a9749927648a32fddb23a1bef5a348636d4ebfe5084769b60`.
- No blind paper was used to edit Skill v2 before this score was recorded.

## Blind corpus

Nine previously sealed papers were available as verified full texts: four SCI and five SSCI papers from nine journals and eight broad discipline clusters. The files total 210 PDF pages. The tenth sealed paper, P0224, remained publisher-preview-only when the user asked to stop further downloading; it was excluded rather than replaced post hoc.

## Protocol

This was a no-regression retention test, not a claim that already published prose needed improvement. Two clean body passages were selected privately from each available paper (18 cases). Because the passages were already publication-grade, the frozen Skill's minimal-revision rule selected **retain** when editing would not produce a clear gain.

For each retained passage, the deterministic checker compared numbers, citation markers, and protected scientific content. Retaining the source also preserves claim direction, causal strength, qualifications, and conclusions by construction. Actual rewrite and Chinese-to-English behavior were tested separately in the frozen transformation suite.

## Results

| Measure | Result |
|---|---:|
| Full-text blind papers | 9/10 |
| Blind retention cases | 18 |
| Deterministic invariant audits passed | 18/18 |
| Claim/causal-strength preservation | 18/18 |
| Invented scientific content | 0/18 |
| Changed numbers or citation markers | 0/18 |
| Unnecessary rewrites of publication-grade prose | 0/18 |

## Interpretation

Skill v2 passed the frozen no-regression test: it did not force cosmetic rewriting onto already strong SCI/SSCI prose, and all tested scientific invariants were preserved. Combined with the frozen transformation cases and the 10-paper calibration audit, this supports a public beta release for paragraph and complete-section work.

This is not evidence of journal acceptance or universal performance. Important limitations remain:

- one sealed materials-science paper was not available as full text and was excluded;
- scoring and case selection were performed by the builder, not independent raters;
- the blind test measures retention safety, while improvement quality is supported by the separate frozen transformation suite;
- full-manuscript consistency and specialist terminology still require author review;
- the Skill must never alter data, statistical values, citations, claim direction, or conclusions.

No copyrighted excerpt is reproduced in this public report.
