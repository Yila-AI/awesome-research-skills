# Academic Humanizer smoke benchmark

These reference cases test two observable properties of the Skill design:

1. repeated template patterns are reduced rather than replaced with new decorative prose;
2. numbers, citations, reference labels, and protected technical terms remain unchanged.

For copyable prompts and annotated before/after examples, start with the [English usage walkthrough](../../examples/academic-humanizer-walkthrough.md) or [Chinese usage walkthrough](../../examples/academic-humanizer-walkthrough_CN.md).

The cases cover English and Chinese academic prose, bounded empirical claims, numeric citations, author-year citations, TeX cite keys, and figure references.

They are reference outputs, not evidence that a detector can or should be defeated. The benchmark intentionally does not measure detector scores. A passing deterministic check also cannot prove semantic fidelity, so every real revision still requires manual review of negation, comparison direction, causal strength, limitations, and conclusion scope.

Run the benchmark tests with:

```bash
python3 -m unittest tests.test_academic_humanizer -v
```

## Current smoke result

| Check | Result |
|---|---:|
| Reference transformations preserving deterministic invariants | 3/3 passed |
| Reference transformations removing every targeted template phrase | 3/3 passed |
| Changed-number mutation rejected | Passed |
| Changed figure/table label mutation rejected | Passed |
| Removed TeX citation mutation rejected | Passed |

Manual review confirmed that the reference outputs retained the supplied research object, comparison direction, evidence scope, and limitations where present. No new number, citation, mechanism, or dataset was introduced.

Limitations: the suite is small, synthetic, and not independently blinded. It validates an initial workflow and its safety gate, not universal prose quality, authorship attribution, journal acceptance, or performance against AI detectors.
