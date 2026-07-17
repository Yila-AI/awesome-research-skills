# Preservation invariants

The source text is the authority for scientific content. Language revision does not authorize substantive revision.

## Tier 1: exact-token invariants

Preserve exactly unless the author explicitly requests correction:

- integers, decimals, ranges, signs, percentages, ratios, dates, and time points;
- units, doses, concentrations, temperatures, wavelengths, and thresholds;
- sample sizes and group labels;
- p values, confidence intervals, effect sizes, model coefficients, test statistics, and significance markers;
- equations, variable names, gene/protein names, chemical names, datasets, instruments, scales, algorithms, and model names;
- in-text citations, citation groups, figure/table numbers, and supplementary-item references.

Formatting may change only when meaning is provably identical and the requested style requires it. Otherwise preserve the token.

## Tier 2: semantic invariants

Preserve:

- who or what performed an action;
- population, setting, intervention/exposure, comparator, and outcome;
- positive/negative/null direction;
- temporal order and comparison basis;
- association versus prediction versus explanation versus causation;
- observed result versus author interpretation versus prior literature;
- scope, exceptions, limitations, uncertainty, and boundary conditions;
- the conclusion's strength and reach.

## Claim-strength ladder

Do not move upward without explicit evidence and authorization:

```text
is consistent with / may suggest
< is associated with / relates to
< predicts
< contributes to
< affects / leads to
< causes / demonstrates that
```

The exact ordering can vary by field, but a revision must never silently convert a weaker epistemic claim into a stronger one.

## Citation invariants

- Do not add, delete, renumber, or fabricate citations.
- Keep each citation attached to the proposition it supports.
- Do not turn a cited background claim into the current study's finding.
- Do not combine sentences if doing so makes citation scope ambiguous.

## Ambiguity protocol

When the source is ambiguous:

1. preserve the narrowest defensible meaning;
2. avoid supplying a missing mechanism or causal link;
3. place the ambiguity under `Author queries`;
4. offer an optional alternative only if clearly labeled and content-neutral.

## Audit representation

Use a compact ledger when the input contains sensitive scientific detail:

| Category | Source | Revision | Status |
|---|---|---|---|
| Numbers/statistics | exact tokens | exact tokens | Preserved / Query |
| Entities/terms | exact terms | exact terms | Preserved / Query |
| Citations | source mapping | revised mapping | Preserved / Query |
| Claim strength | source level | revised level | Preserved / Query |
| Limitations | source scope | revised scope | Preserved / Query |

## Deterministic audit helper

For local files, create a JSON case and run:

```bash
python3 scripts/check_invariants.py case.json
```

```json
{
  "source": "Among 612 participants, Model-A7 yielded 87.08% accuracy (Li, 2023).",
  "revision": "Model-A7 yielded 87.08% accuracy among 612 participants (Li, 2023).",
  "protected_terms": ["Model-A7"]
}
```

The helper checks exact counts of numbers, bracketed or author-year citations, and protected terms. It cannot verify logic, negation, comparison direction, causal strength, citation attachment, limitations, or conclusions; audit those manually every time.
