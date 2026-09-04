# Awesome Research Skills

<p align="center">
  <img src="assets/research-workflow-hero.webp" alt="Awesome Research Skills — the research workflow every AI agent should have" width="100%">
</p>

> **The research workflow every AI agent should have.**

A growing open-source Skill stack for the full research lifecycle—from discovering and understanding papers to writing, reviewing, polishing, and presenting research.

Available today: research writing, faithful academic polishing, and paper-to-slides. More stages are being built. Across the workflow, Agents should show their sources, checks, uncertainty, and changes instead of silently rewriting the research.

Designed for Codex, Claude Code, WorkBuddy-style research agents, and other systems that support reusable Skill instructions.

<p align="center">
  <a href="https://github.com/Yila-AI/awesome-research-skills/actions/workflows/ci.yml"><img src="https://github.com/Yila-AI/awesome-research-skills/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/Yila-AI/awesome-research-skills" alt="Apache-2.0 license"></a>
  <a href="https://skills.sh/yila-ai/awesome-research-skills"><img src="https://skills.sh/b/yila-ai/awesome-research-skills" alt="Install count on skills.sh"></a>
</p>

<p align="center">
  <a href="README_CN.md">中文说明</a> ·
  <a href="README_ja.md">日本語</a> ·
  <a href="README_ko.md">한국어</a> ·
  <a href="#install-in-30-seconds">Install</a> ·
  <a href="#start-from-your-task">Start from a task</a> ·
  <a href="#the-full-research-lifecycle">Lifecycle</a> ·
  <a href="#use-only-one-skill">Lean download</a> ·
  <a href="#paper-to-slides-showcase">Showcase</a> ·
  <a href="#build-on-these-mechanisms">Reuse &amp; cite</a> ·
  <a href="#used-credited-or-adapted-by">Used by</a>
</p>

## Start from your task

| I want to… | Start with | What I get |
|---|---|---|
| Turn ideas, notes, data, or references into a paper | **Research Writer** · [`science-research-writing`](skills/science-research-writing/SKILL.md) | An evidence-grounded plan, section draft, revision, or manuscript audit |
| Improve academic English without changing the research | **Paper Polisher** · [`sci-ssci-polishing`](skills/sci-ssci-polishing/SKILL.md) | Publication-oriented English plus a preservation audit |
| Turn a paper or research results into a talk | **Paper to Slides** · [`research-presentation`](skills/research-presentation/SKILL.md) | An editable, source-grounded deck plan with notes, source map, and visual QA |

## Install in 30 seconds

Node.js 18 or later is required for the installer. Install the complete currently available stack:

```bash
npx skills add Yila-AI/awesome-research-skills --global --agent codex --skill '*' --yes --copy
```

Or install only the capability you need today:

```bash
# Plan, draft, revise, or audit a paper
npx skills add Yila-AI/awesome-research-skills --global --agent codex --skill science-research-writing --yes --copy

# Translate or polish an existing manuscript
npx skills add Yila-AI/awesome-research-skills --global --agent codex --skill sci-ssci-polishing --yes --copy

# Turn a paper or research results into an academic presentation
npx skills add Yila-AI/awesome-research-skills --global --agent codex --skill research-presentation --yes --copy
```

List all installable Skills with `npx skills add Yila-AI/awesome-research-skills --list`.

### Use only one Skill?

The commands above copy only the selected runtime Skill into your Agent's Skills directory. You do not need to clone the complete repository or point an Agent at the repository root. Versioned, use-only ZIP archives for production-ready Skills are published on the [Releases page](https://github.com/Yila-AI/awesome-research-skills/releases).

## The full research lifecycle

The project is growing toward one connected workflow rather than a folder of unrelated prompts:

```text
QUESTION → DISCOVER → READ → SYNTHESIZE → DESIGN → ANALYZE → WRITE → REVIEW → POLISH → COMMUNICATE
```

| Build status | Research stages |
|---|---|
| **Available now** | Write, Polish, Present |
| **Building next** | Discover, Read, Synthesize, Review |
| **Longer-term workflow** | Design, Analyze, Publish and broader research communication |

The product direction is a single `$research` entry point that can understand the current stage and route work to the right specialist module. The current release exposes each available Skill directly while that unified workflow is being built.

The modules will share research context—questions, sources, evidence, author decisions, claims, data, and revision history—so that evidence found during search can survive all the way into a manuscript, review, or presentation.

## Available today

The current release provides three connected capabilities:

| Foundation | Available module | What it helps you do |
|---|---|---|
| The section-by-section and reverse-engineering pedagogy associated with Hilary Glasman-Deal's *Science Research Writing* | **Research Writer** · [`science-research-writing`](skills/science-research-writing/SKILL.md) | Decide what each section needs to accomplish, then turn ideas, notes, data, references, or drafts into the next useful manuscript artifact |
| Writing observations derived through a corpus pipeline beginning with a 1,000-paper SCI/SSCI metadata candidate pool | **Paper Polisher** · [`sci-ssci-polishing`](skills/sci-ssci-polishing/SKILL.md) | Translate or polish an existing manuscript while preserving data, citations, terminology, limitations, and claim strength |
| Evidence-first academic presentation design | **Paper to Slides** · [`research-presentation`](skills/research-presentation/SKILL.md) | Turn papers and research materials into editable, source-grounded research presentations, with a narrative plan, evidence ledger, speaker notes, and render-based QA |

In plain language: **the writing Skills help build and refine the paper; `research-presentation` carries the evidence into a talk without flattening the science.** Scientific judgment remains with the author.

### Building a research Agent?

You can reuse the repository's Evidence-Preserving Draft Contract, Claim-Strength Contract, and Target-Journal Model Builder in your own project.

[Reuse the mechanisms](#build-on-these-mechanisms) · [Cite this repository](CITATION.cff) · [Add your project](#used-credited-or-adapted-by)

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

## Paper to Slides showcase

`research-presentation` turns a paper into a source-grounded, editable research presentation. The [full showcase](showcase/research-presentation/README.md) covers six cross-disciplinary cases; the network-epidemiology case also includes two complete 12-slide visual passes.

<p align="center">
  <a href="showcase/research-presentation/ecology-network/README.md">
    <img src="showcase/research-presentation/ecology-network/bright-azure-v2/01.webp" alt="Paper to Slides showcase cover" width="48%">
  </a>
  <a href="showcase/research-presentation/ecology-network/README.md">
    <img src="showcase/research-presentation/ecology-network/bright-azure-v2/05.webp" alt="Paper to Slides showcase result slide" width="48%">
  </a>
</p>

Source paper: [arXiv:2607.25475](https://arxiv.org/abs/2607.25475). The repository stores the canonical paper link, not the source PDF. [Browse all six cases →](showcase/research-presentation/README.md)

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

The first statement reports a bounded result. The second silently turns a local finding into a universal claim. The writing Skills are designed to detect this kind of drift: evidence can be clarified, organized, translated, and polished, but it must not be silently strengthened.

[Read the complete milk-tea walkthrough](examples/science-research-writing-walkthrough.md) · [查看中文完整案例](examples/science-research-writing-walkthrough_CN.md)

## What the available Skills add

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

### `research-presentation`

The public showcase demonstrates cross-disciplinary output design, but a frozen comparative benchmark has not yet been published. Showcase images are examples, not evidence of universal presentation quality.

These evaluations support narrow safety and consistency claims. They do not prove journal acceptance, universal disciplinary coverage, scientific correctness, or superiority to domain experts and professional editors.

## Copyright, data, and professional boundaries

- The repository contains no book PDF, article PDF, subscription full text, extracted paper paragraphs, phrase bank, or private access trace.
- Public corpus tables contain bibliographic metadata, screening annotations, and aggregate results only.
- `SCI` and `SSCI` describe corpus and user scope. This independent project is not affiliated with Clarivate, any journal, author, or publisher.
- Production-ready Skills in this repository are public beta software and do not replace author, domain-specialist, statistical, ethical, or professional editorial review.

## Citation and license

See [`CITATION.cff`](CITATION.cff) for formal citation metadata. Original code, Skill instructions, and project documentation are licensed under the [Apache License 2.0](LICENSE). Third-party facts, names, and external resources remain subject to their source terms.
