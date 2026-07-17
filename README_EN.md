# SCI/SSCI Skills

> Polish the writing. Never rewrite the science.

`sci-ssci-skills` is an open-source collection of Agent Skills for research writing. Its first package, `sci-ssci-polishing`, translates Chinese academic prose into publication-oriented English and polishes English paragraphs or complete manuscript sections.

The Skill routes editing by rhetorical function and audits numbers, statistics, technical entities, citations, claim strength, limitations, and conclusions after every revision.

## Install

Node.js 18 or later is required.

```bash
npx skills add yilaai/sci-ssci-skills --global --agent codex --skill sci-ssci-polishing --yes --copy
```

List available packages:

```bash
npx skills add yilaai/sci-ssci-skills --list
```

## Use

```text
Use $sci-ssci-polishing to translate this Chinese Results paragraph into
academic English. Preserve every number, statistic, technical term, citation,
and causal qualification.
```

```text
Use $sci-ssci-polishing to polish this SSCI Discussion section. Improve
cross-paragraph coherence without changing claims, citations, limitations,
or conclusions.
```

## Corpus transparency

V2 started from a metadata candidate pool of 1,000 papers, screened a balanced shortlist of 200, and selected 60 papers across nine SCI/SSCI portfolio clusters: 40 for rule distillation, 10 for calibration, and 10 for sealed blind evaluation.

Distillation means abstracting recurring rhetorical functions, evidence boundaries, and failure modes. It does not mean model fine-tuning, copying journal sentences, or claiming universal disciplinary coverage.

Copyrighted full text and private extractions are excluded. The repository publishes only bibliographic metadata, selection labels, abstracted rules, synthetic examples, and aggregate evaluation results.

See the [Chinese README](README.md), [corpus method](skills/sci-ssci-polishing/references/corpus-method.md), and [blind retention report](benchmarks/blind-retention-results.md) for details.

## License and disclaimer

Original code, Skill instructions, and project documentation are licensed under the [Apache License 2.0](LICENSE). Third-party bibliographic facts and external resources remain subject to their source terms.

`SCI` and `SSCI` describe the corpus scope. This independent project is not affiliated with Clarivate, any journal, or any publisher. It is a public beta and does not guarantee acceptance or replace specialist review.
