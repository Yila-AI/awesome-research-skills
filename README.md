<div align="center">
  <img src="assets/sci-ssci-skills-banner.png" alt="1,000 high-quality papers. One SCI/SSCI polishing skill." width="100%">
</div>

<p align="center">
  <a href="README_CN.md">中文</a>
</p>

# SCI/SSCI Skills

> **1,000 high-quality papers. One SCI/SSCI polishing skill.**
>
> Polish the writing. Preserve the science.

`sci-ssci-skills` is an open-source collection of Agent Skills for research writing. Its first package, `sci-ssci-polishing`, translates Chinese academic prose into publication-oriented English and polishes English paragraphs or complete manuscript sections.

It is built for one constraint that generic polishing prompts often miss: a sentence can become more fluent while becoming less scientifically faithful.

## What it does

- Chinese academic paragraphs or sections -> academic English;
- English manuscript polishing at paragraph or complete-section level;
- rhetorical routing for Abstract, Introduction, Methods, Results, Discussion, and Conclusion;
- SCI, SSCI, and interdisciplinary manuscript support;
- post-edit audits of data, statistics, technical entities, citations, claim strength, limitations, and conclusions.

The core principle is simple:

> **Polish the writing. Never rewrite the science.**

## Why this is not another “Please polish” prompt

Generic language polishing often optimizes fluency alone. It may silently turn `was associated with` into `led to`, detach a citation from its proposition, remove a null result, or smooth away a limitation.

`sci-ssci-polishing` uses a preservation-first workflow:

```text
classify -> lock invariants -> route by section -> revise -> audit
```

It will not invent mechanisms, citations, data, limitations, or implications merely to make a passage sound more complete or more “top-journal-like.” If the scientific meaning is ambiguous, it preserves the narrower interpretation and asks the author.

## The 1,000-paper evidence pool

V2 began with a **1,000-paper SCI/SSCI metadata candidate pool** and used staged screening to build a balanced core corpus:

```text
1,000-paper metadata candidate pool
                 ↓
        200-paper balanced shortlist
                 ↓
          60-paper core portfolio
        ↙           ↓           ↘
40 distillation  10 calibration  10 sealed blind evaluation
```

The final portfolio contains 30 SCI and 30 SSCI papers across nine broad discipline clusters. The 40-paper distillation split contains 20 SCI and 20 SSCI papers from 28 journals, yielding aggregate observations from 1,750 usable paragraphs and 220,158 words.

Here, **distillation does not mean model fine-tuning or copying journal sentences**. It means abstracting recurring rhetorical functions, information order, evidence boundaries, and failure modes into reusable editing rules.

The 1,000-paper pool is a screening universe. It is not a claim that 1,000 full texts were downloaded, read, or used to train a model.

[Corpus method](skills/sci-ssci-polishing/references/corpus-method.md) · [Selection method](corpus/selection-rubric.md) · [Corpus summary](corpus/corpus-summary.md) · [Public metadata](corpus/README.md)

## Install

Node.js 18 or later is required.

```bash
npx skills add Yila-AI/sci-ssci-skills \
  --global \
  --agent codex \
  --skill sci-ssci-polishing \
  --yes \
  --copy
```

List the installable Skills first:

```bash
npx skills add Yila-AI/sci-ssci-skills --list
```

## Use

### Chinese to academic English

```text
Use $sci-ssci-polishing to translate this Chinese Results paragraph into
academic English. Preserve every number, statistic, technical term, citation,
and causal qualification.
```

### English manuscript polishing

```text
Use $sci-ssci-polishing to polish this SSCI Discussion section. Improve
cross-paragraph coherence without changing claims, citations, limitations,
or conclusions.
```

The default response contains:

1. polished English;
2. key language or organization changes;
3. a preservation audit;
4. author queries only when the source is ambiguous or incomplete.

[See synthetic input/output examples](examples/quick-examples.md)

## Section-aware editing

The Skill routes prose by rhetorical job rather than applying one generic “academic style.”

| Section | Primary editing objective |
|---|---|
| Abstract | Compact problem, approach, result, and calibrated implication |
| Introduction | Clear progression from established knowledge to gap and present study |
| Methods | Reproducibility, stable terminology, and procedural order |
| Results | Evidence order, quantitative precision, and null-result preservation |
| Discussion | Separation of finding, interpretation, implication, and limitation |
| Conclusion | Synthesis without scope inflation |

For a complete section, the Skill maps each paragraph's rhetorical job before repairing cross-paragraph progression.

## Preservation contract

Unless the author explicitly requests and verifies a substantive correction, the Skill preserves:

- numbers, statistics, ranges, units, sample sizes, and time points;
- genes, proteins, chemicals, datasets, instruments, scales, algorithms, and model names;
- in-text citations and the proposition each citation supports;
- positive, negative, and null directions;
- association, prediction, explanation, and causation boundaries;
- uncertainty markers, exceptions, limitations, and conclusions.

The included `check_invariants.py` helper provides a deterministic first pass over numbers, citations, and protected terms. Semantic checks—such as negation, causal strength, citation scope, and conclusion reach—remain mandatory and cannot be reduced to token matching.

## Current evaluation

| Evaluation | Result |
|---|---:|
| Frozen synthetic transformation cases | 6/6 passed |
| Verified blind full texts available | 9/10 |
| Publication-grade retention cases | 18/18 passed |
| Invented scientific content | 0/18 |
| Changed numbers or citation markers | 0/18 |
| Unnecessary rewrites | 0/18 |

The blind test asks a deliberately narrow question: when already strong, publication-grade prose does not clearly benefit from editing, can the Skill retain it instead of forcing cosmetic rewrites?

These results support safety and consistency claims only. They are not independent human ratings, evidence of journal acceptance, proof of universal disciplinary coverage, or proof of superiority to professional domain editors.

[Synthetic cases](benchmarks/synthetic-cases.md) · [Synthetic outputs](benchmarks/synthetic-case-outputs.md) · [Blind retention report](benchmarks/blind-retention-results.md)

## Copyright, data, and affiliation boundaries

- The repository contains no article PDFs, subscription full text, extracted paper paragraphs, or private access traces.
- Public corpus tables contain bibliographic metadata, screening annotations, and aggregate results only.
- Proprietary impact-factor, quartile, and ranking tables are excluded.
- `SCI` and `SSCI` describe the corpus scope. This independent project is not affiliated with Clarivate, any journal, or any publisher.
- The Skill is a public beta and does not replace author, specialist, or professional editorial review.

## License

Original code, Skill instructions, and project documentation are licensed under the [Apache License 2.0](LICENSE). Third-party bibliographic facts and external resources remain subject to their source terms; see the [data notes](corpus/README.md).
