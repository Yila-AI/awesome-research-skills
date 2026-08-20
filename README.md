<div align="center">
  <img src="assets/sci-ssci-research-writing-hero.png" alt="SCI/SSCI Research Writing Skills — Plan. Draft. Polish. Preserve the science." width="100%">
</div>

# SCI/SSCI Research Writing Skills

> **Turn your research into a clear, well-structured paper—section by section.**

**Polish the writing. Never rewrite the science.** This repository provides open-source Agent Skills for planning, drafting, revising, translating, and polishing SCI/SSCI papers while preserving meaning, data, citations, limitations, and claim strength.

Designed for Agent workflows such as Codex, Claude Code, WorkBuddy-style research agents, and other systems that support reusable Skill instructions.

<p align="center">
  <a href="README_CN.md">中文说明</a> ·
  <a href="README_ja.md">日本語</a> ·
  <a href="README_ko.md">한국어</a> ·
  <a href="docs/science-research-writing/getting-started.md">1-minute start</a> ·
  <a href="#install">Install</a> ·
  <a href="#which-skill-should-i-use">Which Skill?</a> ·
  <a href="#use-only-one-skill">Lean download</a> ·
  <a href="#build-on-these-mechanisms">Reuse &amp; cite</a> ·
  <a href="#used-credited-or-adapted-by">Used by</a>
</p>

## Paper to Slides showcase

`research-presentation` turns a paper into a source-grounded, editable research
presentation. The [full showcase](showcase/research-presentation/README.md)
now covers six cross-disciplinary cases; the network-epidemiology case also
includes two complete 12-slide visual passes.

<p align="center">
  <a href="showcase/research-presentation/ecology-network/README.md">
    <img src="showcase/research-presentation/ecology-network/bright-azure-v2/01.webp" alt="Paper to Slides showcase cover" width="48%">
  </a>
  <a href="showcase/research-presentation/ecology-network/README.md">
    <img src="showcase/research-presentation/ecology-network/bright-azure-v2/05.webp" alt="Paper to Slides showcase result slide" width="48%">
  </a>
</p>

Source paper: [arXiv:2607.25475](https://arxiv.org/abs/2607.25475). The repository
stores the canonical paper link, not the source PDF.

| Education research | Epidemiology | Materials science |
|---|---|---|
| [![Education opportunity](showcase/research-presentation/education-opportunity/slate-orange/01-cover.webp)](showcase/research-presentation/README.md) | [![Epidemic mobility](showcase/research-presentation/epidemic-mobility/pku-red/01-cover.webp)](showcase/research-presentation/README.md) | [![Materials alloy](showcase/research-presentation/materials-alloy/forest-green/01-cover.webp)](showcase/research-presentation/README.md) |

| Sociology | Statistics | Full gallery |
|---|---|---|
| [![Sociology and democracy](showcase/research-presentation/sociology-democracy/zju-blue/01-cover.webp)](showcase/research-presentation/README.md) | [![Statistics ranking](showcase/research-presentation/statistics-ranking/deep-purple/01-cover.webp)](showcase/research-presentation/README.md) | [Browse all six cases →](showcase/research-presentation/README.md) |

## Which Skill should I use?

| If you are... | Use | Copy this starting point |
|---|---|---|
| Starting from an idea, notes, results, tables, or references | `science-research-writing` | `Use $science-research-writing. I have research materials but do not know how to organize them into a paper.` |
| Turning a paper, manuscript, or research results into an academic slide deck | `research-presentation` | `Use $research-presentation to turn this paper into a source-grounded research presentation.` |
| Trying to turn rough materials into Introduction, Methods, Results, Discussion, Abstract, or Title | `science-research-writing` | `Use $science-research-writing to help me draft the next useful manuscript section from the materials below.` |
| Translating Chinese academic prose into publication-oriented English | `sci-ssci-polishing` | `Use $sci-ssci-polishing. Translate this into academic English, but do not add claims or citations.` |
| Polishing an English manuscript without changing the science | `sci-ssci-polishing` | `Use $sci-ssci-polishing. Improve clarity and flow while preserving numbers, citations, limitations, and claim strength.` |
| Building your own research Agent | Reuse the mechanisms | Start from the [Evidence-Preserving Draft Contract](skills/science-research-writing/SKILL.md) and [Claim-Strength Contract](skills/science-research-writing/references/certainty-and-claim-strength.md). |

## Why star this repo?

Star this repository if you want a growing open-source toolkit for:

- writing research papers section by section;
- polishing SCI/SSCI manuscripts without changing the science;
- protecting numbers, citations, terminology, limitations, and claim strength during AI-assisted revision;
- building academic-writing Agents with reusable evidence-preserving rules;
- contributing examples, benchmarks, translations, and new research-writing Skills.

## Two foundations, one research-writing workflow

This repository does three connected jobs:

| Foundation | Skill | What it helps you do |
|---|---|---|
| The section-by-section and reverse-engineering pedagogy associated with Hilary Glasman-Deal's *Science Research Writing* | [`science-research-writing`](skills/science-research-writing/SKILL.md) | Decide what each section needs to accomplish, then turn ideas, notes, data, references, or drafts into the next useful manuscript artifact |
| Writing observations derived through a corpus pipeline beginning with a 1,000-paper SCI/SSCI metadata candidate pool | [`sci-ssci-polishing`](skills/sci-ssci-polishing/SKILL.md) | Translate or polish an existing manuscript while preserving data, citations, terminology, limitations, and claim strength |
| Evidence-first academic presentation design | [`research-presentation`](skills/research-presentation/SKILL.md) | Turn papers and research materials into editable, source-grounded research presentations, with a narrative plan, evidence ledger, speaker notes, and render-based QA |

In plain language: **the writing Skills help build and refine the paper; `research-presentation` carries the evidence into a talk without flattening the science.** Scientific judgment remains with the author.

<div align="center">
  <img src="assets/sci-ssci-research-writing-architecture.png" alt="Architecture of SCI/SSCI Research Writing Skills: a book-informed writing workflow and a curated SCI/SSCI corpus pipeline connected by evidence-preserving contracts" width="100%">
</div>

### Building a research Agent?

You can reuse the repository's Evidence-Preserving Draft Contract, Claim-Strength Contract, and Target-Journal Model Builder in your own project.

[Reuse the mechanisms](#build-on-these-mechanisms) · [Cite this repository](CITATION.cff) · [Add your project](#used-credited-or-adapted-by)

## Choose where you are

| What you have now | Use | What you get |
|---|---|---|
| An idea or research question | `science-research-writing` | Questions to resolve, a materials checklist, and a practical next step |
| Notes, data, references, or a protocol | `science-research-writing` | A paper plan or section draft grounded only in supplied materials |
| A partial or complete draft | `science-research-writing` | Revision, consistency checks, or an evidence audit |
| Chinese academic prose or an English manuscript | `sci-ssci-polishing` | Academic English plus a preservation audit |
| A paper or research results that need to become slides | `research-presentation` | A narrative outline, editable deck plan, source map, notes, and visual QA checklist |

## Start with one sentence

```text
Use $science-research-writing to help me write my paper.
Here are the materials I currently have: [attach files or paste text]
```

The Skill reads what you have, identifies whether the next useful result is a plan, draft, revision, or audit, and proceeds without requiring a long intake prompt or an internal mode selection.

[Getting started](docs/science-research-writing/getting-started.md) · [Use cases](docs/science-research-writing/use-cases.md) · [Copyable inputs](docs/science-research-writing/input-examples.md) · [Output guide](docs/science-research-writing/output-guide.md)

For paper-to-slides work, start with the [Research Presentation quick start](docs/research-presentation/getting-started.md) and [use cases](docs/research-presentation/use-cases.md).

## Copy-paste examples

### From materials to a paper structure

```text
Use $science-research-writing.
I have finished my study, but I do not know how to organize it into a paper.

Research question:
[paste your research question]

Methods:
[paste what you did]

Main results:
[paste key findings, tables, or notes]

Target journal or field:
[paste if available]
```

### Polish without changing the science

```text
Use $sci-ssci-polishing.
Please polish this Discussion paragraph for academic clarity.
Do not change numbers, citations, terminology, limitations, or claim strength.
If any sentence sounds unsupported or overclaimed, flag it instead of fixing it silently.

Text:
[paste paragraph]
```

## Install

Node.js 18 or later is required.

```bash
# Start from research materials
npx skills add Yila-AI/awesome-research-skills --global --agent codex --skill science-research-writing --yes --copy

# Translate or polish an existing draft
npx skills add Yila-AI/awesome-research-skills --global --agent codex --skill sci-ssci-polishing --yes --copy

# Turn a paper or research materials into an academic presentation
npx skills add Yila-AI/awesome-research-skills --global --agent codex --skill research-presentation --yes --copy
```

List all installable Skills:

```bash
npx skills add Yila-AI/awesome-research-skills --list
```

### Use only one Skill?

You do not need to clone the complete repository or point an Agent at the repository root merely to run one Skill. The `--skill ... --copy` commands above copy only the selected runtime Skill into your Agent's Skills directory.

For manual installation or downstream integration, download the packaged `sci-ssci-polishing` Skill from the [latest Lean Release](https://github.com/Yila-AI/awesome-research-skills/releases/latest). The full repository keeps the corpus, benchmarks, provenance, and examples available for researchers who want to inspect how the Skill was built and evaluated.

## Why turn *Science Research Writing* into an Agent workflow?

Hilary Glasman-Deal's *Science Research Writing: For Native and Non-Native Speakers of English* is valued because it teaches more than phrases and grammar. Its section-by-section approach asks what a reader needs from each part of an empirical paper, while its reverse-engineering pedagogy encourages researchers to examine successful papers in their own field and adapt recurring functions without copying sentences.

An independent review reports that the first edition sold more than 35,000 copies and was translated into Chinese, Korean, and Japanese ([Anna Clemens, 2020](https://annaclemens.com/blog/book-review-science-research-writing-hilary-glasman-deal/)).

The central idea can be summarized as seven reader questions:

| Manuscript section | The reader's question |
|---|---|
| Introduction | Why was this study needed? |
| Methods | What exactly was done? |
| Results | What was found? |
| Discussion | What do the findings mean—and what do they not mean? |
| Conclusion | What can the evidence actually support? |
| Abstract | What must a reader understand in one minute? |
| Title | What does the paper promise? |

`science-research-writing` operationalizes this general approach for Agent use and adds automatic task routing, target-journal modeling, evidence provenance, author-confirmation boundaries, and deterministic draft checks.

It is an independent, unofficial project. It is not affiliated with or endorsed by the author or World Scientific, and it does not reproduce the book, exercises, answer key, phrase lists, sample passages, or page content. See the [privacy and copyright boundaries](docs/science-research-writing/privacy-and-copyright.md).

## Fluent is not always faithful

Suppose 120 university students rate nine milk-tea recipes. The evidence shows that 30%-sugar oolong milk tea receives the highest average rating among these participants.

**Supported by the study:**

> Among the participants in this study, 30%-sugar oolong milk tea received the highest rating.

**Not supported by the study:**

> 30%-sugar oolong milk tea is the world's best milk-tea recipe.

The first statement reports a bounded result. The second silently turns a local finding into a universal claim. Both Skills are designed to detect this kind of drift: evidence can be clarified, organized, translated, and polished, but it must not be silently strengthened.

[Read the complete milk-tea walkthrough](examples/science-research-writing-walkthrough.md) · [查看中文完整案例](examples/science-research-writing-walkthrough_CN.md)

## What the two Skills add

### `science-research-writing`

- routes an idea, materials, partial draft, or full draft to the next useful task;
- maps Introduction, Methods, Results, Discussion, Conclusion, Abstract, and Title by reader question and rhetorical function;
- models target-journal functions and variation without storing copied prose;
- records the source of consequential statements and marks missing evidence;
- checks numbers, citations, protected terms, and claim-strength markers;
- gives novice-readable outputs and asks no more than one blocking question at a time.

### `research-presentation`

- turns a paper, manuscript, figures, tables, or research notes into a source-grounded talk plan;
- keeps an evidence ledger and source anchors for consequential claims;
- chooses a narrative arc for journal club, lab meeting, conference talk, seminar, or thesis defense;
- produces editable slide content, speaker notes, and a render-based QA report;
- preserves uncertainty, limitations, and claim strength instead of optimizing for visual polish alone.

### `sci-ssci-polishing`

- translates Chinese academic prose into publication-oriented English;
- polishes English paragraphs and complete manuscript sections;
- improves information order, clarity, cohesion, and academic tone;
- preserves numbers, statistics, technical entities, citations, null results, limitations, and conclusions;
- refuses to invent mechanisms, references, results, or implications merely to make prose sound more complete.

## The 1,000-paper evidence pool—what it does and does not mean

The polishing Skill began with a **1,000-paper SCI/SSCI metadata candidate pool** and used staged screening to build a balanced core portfolio:

```text
1,000-paper metadata candidate pool
                 ↓
        200-paper balanced shortlist
                 ↓
          60-paper core portfolio
        ↙           ↓           ↘
40 distillation  10 calibration  10 sealed blind evaluation
```

The 60-paper portfolio contains 30 SCI and 30 SSCI papers across nine broad discipline clusters. The 40-paper distillation split contains 20 SCI and 20 SSCI papers from 28 journals, yielding aggregate observations from 1,750 usable paragraphs and 220,158 words.

Here, **distillation does not mean model fine-tuning or copying journal sentences**. It means abstracting recurring rhetorical functions, information order, evidence boundaries, and failure modes into reusable editing rules. The 1,000-paper pool is a screening universe: it is not a claim that 1,000 full texts were downloaded, read, distilled, or used to train a model.

[Corpus method](skills/sci-ssci-polishing/references/corpus-method.md) · [Selection method](corpus/selection-rubric.md) · [Corpus summary](corpus/corpus-summary.md) · [Public metadata](corpus/README.md)

## Build on these mechanisms

The following mechanisms are documented as reusable components for other research Agents and academic-writing projects:

| Featured mechanism | What it protects or enables |
|---|---|
| [Evidence-Preserving Draft Contract](skills/science-research-writing/SKILL.md) | Prevents unsupported intellectual content during planning, drafting, and revision |
| [Claim-Strength Contract](skills/science-research-writing/references/certainty-and-claim-strength.md) | Prevents silent movement between suggestion, association, prediction, effect, and causation |
| [Target-Journal Model Builder](skills/science-research-writing/references/reverse-engineering-protocol.md) | Learns rhetorical functions and variation without copying target-paper wording |

Additional components include the [Section Function Map](skills/science-research-writing/assets/section-function-map.md), [Content Provenance Ledger](skills/science-research-writing/assets/evidence-ledger.csv), [Title-Paper Promise Check](skills/science-research-writing/references/title.md), and [Draft Invariant Checker](skills/science-research-writing/scripts/check_draft_invariants.py).

Suggested short credit:

```markdown
**Credit:** The evidence-preserving research-writing workflow is adapted from
[Yila-AI/awesome-research-skills](https://github.com/Yila-AI/awesome-research-skills),
including its Evidence-Preserving Draft Contract and Claim-Strength Contract.
```

Reuse remains subject to the repository license and any applicable third-party rights.

## Used, credited, or adapted by

This section lists public projects that use, credit, adapt, or discuss mechanisms from this repository.

| Project | Relationship |
|---|---|
| [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | Credited and adapted the claim-strength ladder mechanism for revision-round claim-drift guards. See related discussion in [issue #569](https://github.com/Imbad0202/academic-research-skills/issues/569), [issue #570](https://github.com/Imbad0202/academic-research-skills/issues/570), and [PR #573](https://github.com/Imbad0202/academic-research-skills/pull/573). |

Using or adapting this workflow in your own research Agent, academic-writing tool, or open-source project? Open an [issue](https://github.com/Yila-AI/awesome-research-skills/issues) or pull request to add your project here. Please include a short description and a public link.

## Evaluation

Evaluation claims remain Skill-specific.

### `sci-ssci-polishing`

| Evaluation | Result |
|---|---:|
| Frozen synthetic transformation cases | 6/6 passed |
| Verified blind full texts available | 9/10 |
| Publication-grade retention cases | 18/18 passed |
| Invented scientific content | 0/18 |
| Changed numbers or citation markers | 0/18 |
| Unnecessary rewrites | 0/18 |

[Synthetic cases](benchmarks/synthetic-cases.md) · [Synthetic outputs](benchmarks/synthetic-case-outputs.md) · [Blind retention report](benchmarks/blind-retention-results.md)

### `science-research-writing`

The test set and scoring rubric were frozen before implementation. Comparative results will be added only after raw outputs, model settings, case-level scores, failures, and limitations are available.

[Benchmark protocol](benchmarks/science-research-writing/README.md) · [Frozen cases](benchmarks/science-research-writing/test-cases.json) · [Evaluation rubric](benchmarks/science-research-writing/evaluation-rubric.md) · [Development smoke tests](benchmarks/science-research-writing/smoke-test-results.md)

These evaluations support narrow safety and consistency claims. They do not prove journal acceptance, universal disciplinary coverage, scientific correctness, or superiority to domain experts and professional editors.

## Copyright, data, and professional boundaries

- The repository contains no book PDF, article PDF, subscription full text, extracted paper paragraphs, phrase bank, or private access trace.
- Public corpus tables contain bibliographic metadata, screening annotations, and aggregate results only.
- `SCI` and `SSCI` describe corpus and user scope. This independent project is not affiliated with Clarivate, any journal, author, or publisher.
- Both Skills are public beta software and do not replace author, domain-specialist, statistical, ethical, or professional editorial review.

## Citation and license

See [`CITATION.cff`](CITATION.cff) for formal citation metadata. Original code, Skill instructions, and project documentation are licensed under the [Apache License 2.0](LICENSE). Third-party facts, names, and external resources remain subject to their source terms.
