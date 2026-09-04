---
name: sci-ssci-polishing
description: Use when researchers need Chinese academic prose translated into publication-oriented English or English manuscript paragraphs and complete sections polished for SCI, SSCI, or interdisciplinary submission.
license: Apache-2.0
---

# SCI/SSCI Academic Polishing

Polish the writing, not the science. Improve clarity, precision, coherence, concision, and disciplinary register while treating the author's evidence and claims as immutable unless the author explicitly authorizes a substantive change.

## Load only what is needed

- Always read `references/invariants.md` and `references/output-contract.md`.
- Read `references/rhetorical-routing.md` when polishing a complete section or when the section type is known.
- Read `references/corpus-method.md` only when explaining how this Skill was built or what its evidence base can and cannot support.

## Inputs

Accept either:

1. Chinese academic prose to translate into English.
2. English academic prose to polish.

The input may be one paragraph or a complete section. Useful context includes field, target journal, section type, preferred English variety, and terminology constraints. Do not require this context when the prose can be handled conservatively.

## Workflow

### 1. Classify the request

Identify:

- mode: `Chinese -> academic English` or `English polishing`;
- scope: `paragraph` or `full section`;
- domain family: `SCI`, `SSCI`, or `uncertain/interdisciplinary`;
- rhetorical function: Abstract, Introduction, Methods, Results, Discussion, Conclusion, literature review, or mixed;
- requested intensity: light, standard, or substantial language revision.

If the field or section is unclear, infer cautiously from the text. State the inference only when it materially affects the revision.

### 2. Build a preservation ledger before rewriting

Extract and lock every item listed in `references/invariants.md`, including all numbers, statistical expressions, units, citations, named entities, comparison directions, uncertainty markers, limitations, and claim strength.

Also record the paragraph's claim skeleton:

```text
context/problem -> method/evidence -> finding -> interpretation/qualification
```

Do not proceed as if two different skeletons were equivalent. If the intended relation is ambiguous, keep the weaker interpretation and add an author query.

### 3. Route by rhetorical function

Use `references/rhetorical-routing.md` rather than applying one generic “academic style.” A Methods paragraph should optimize reproducibility; a Results paragraph should optimize evidence order; an SSCI literature review should optimize synthesis and theoretical positioning.

For a full section:

1. revise each paragraph locally;
2. label its rhetorical job in a private working outline;
3. repair cross-paragraph progression and transitions;
4. remove redundant setup only when no claim, citation role, or limitation is lost;
5. re-audit the complete section.

### 4. Revise the prose

Prioritize in this order:

1. factual fidelity;
2. explicit logical relations;
3. correct disciplinary terminology;
4. sentence-level clarity;
5. paragraph coherence;
6. concision and rhythm.

Use the smallest revision that achieves the requested improvement. Published-looking prose is not permission to rewrite already clear sentences, inflate formality, or force every sentence toward one journal's rhythm.

Apply these default practices:

- put the main actor and action early;
- prefer precise verbs over inflated nominalizations;
- keep evidence adjacent to the claim it supports;
- use signposting only when it clarifies a real relation;
- vary sentence length without making sentences ornamental;
- preserve conventional technical phrases when they are already correct;
- translate meaning and rhetorical function, not Chinese word order;
- avoid thesaurus substitution, promotional language, and journal mimicry.

Never invent a citation, mechanism, limitation, rationale, transition, or implication merely to make the prose sound complete.

### 5. Run the preservation audit

Compare source and revision item by item. The audit must explicitly check:

- numbers, ranges, signs, decimal places, percentages, units, and statistical symbols;
- sample sizes, group labels, time points, model names, datasets, and instruments;
- citations and their attachment to claims;
- negation, comparison direction, modality, hedging, and causal strength;
- limitations, exceptions, boundary conditions, and conclusions.

If any substantive difference remains, revert it or surface it as an author query. Do not hide it in “key changes.”

When source and revision are available as local text, use `scripts/check_invariants.py` for a deterministic first pass over numbers, citations, and user-supplied protected terms. Treat a passing script result as necessary but not sufficient; manually audit claim direction, modality, causal strength, citation attachment, limitations, and conclusions.

## Editing intensity

### Light

Correct grammar, punctuation, word choice, and local flow. Preserve sentence and paragraph structure whenever possible.

### Standard (default)

Rewrite sentences and improve paragraph progression while preserving every scientific proposition and citation role.

### Substantial language revision

Reorder sentences or paragraphs for rhetorical clarity, but never add, remove, merge, or strengthen scientific claims without explicit author approval. List every meaningful reordering.

## Refusal boundary

If the user asks to make unsupported findings sound significant, hide limitations, convert association into causation, fabricate citations, or change results without evidence, refuse that part and offer a fidelity-preserving revision.

## Output

Follow `references/output-contract.md`. Return the polished English first, then a concise change summary, preservation audit, and author queries only when needed.
