# Preservation and evidence contract

The source text is authoritative for scientific content. A humanizing pass changes expression, not the underlying scholarship.

## Exact-token invariants

Preserve exactly unless the author explicitly asks for a correction:

- integers, decimals, signs, ranges, percentages, ratios, dates, and time points;
- units, doses, concentrations, temperatures, wavelengths, and thresholds;
- sample sizes, group labels, model names, dataset names, and instrument names;
- p values, confidence intervals, effect sizes, coefficients, test statistics, and significance markers;
- equations, variables, gene or protein names, chemical names, algorithms, and named metrics;
- in-text citations, cite keys, figure or table numbers, equation labels, and supplementary references.

Formatting may change only when the meaning and reference identity remain provably identical.

## Semantic invariants

Preserve:

- who or what performed an action;
- population, setting, intervention or exposure, comparator, and outcome;
- positive, negative, mixed, or null direction;
- temporal order and comparison basis;
- observed result versus interpretation versus prior literature;
- association, prediction, explanation, and causation distinctions;
- uncertainty, exceptions, limitations, boundary conditions, and conclusion scope.

## Claim-strength discipline

Do not silently move upward on this indicative ladder:

```text
may be consistent with / may suggest
< is associated with / relates to
< predicts
< contributes to
< affects / leads to
< causes / proves a general claim
```

Field conventions vary. The governing rule is that the revised verb must not be stronger than the supplied evidence.

For every empirical claim, privately record:

```text
claim -> evidence pointer -> evidence type -> supported scope -> verb strength
```

Acceptable evidence pointers include a number, statistical result, figure, table, supplied citation, qualitative excerpt, or explicitly identified author interpretation.

## Missing-evidence protocol

If a claim lacks visible support:

1. do not manufacture the support;
2. keep the original wording only when the user requested style-only editing and the claim is not being strengthened;
3. otherwise soften to the narrowest defensible form or leave the sentence unchanged;
4. add an author query requesting the relevant number, figure, table, citation, or qualification.

Never convert vague magnitude into a fabricated number. A request to “make this more convincing” does not authorize stronger claims.

## Citation protection

- Do not add, delete, renumber, or fabricate citations.
- Keep each citation attached to the proposition it supports.
- Do not merge sentences when the merge makes citation scope ambiguous.
- Do not turn cited background knowledge into a finding of the current study.
- Preserve citation style unless the user explicitly requests reformatting.

## Ambiguity protocol

When the source permits more than one meaning:

1. retain the narrowest supported reading;
2. avoid adding a missing logical or causal bridge;
3. identify the exact ambiguity under `Author queries`;
4. offer an optional alternative only when it is content-neutral.

## Verification limits

The deterministic checker compares number, citation, reference-label, and protected-term tokens. It cannot determine whether the rewrite changed negation, comparison direction, modality, causal meaning, evidence attachment, limitation scope, or conclusions. Audit those manually every time.
