# README Positioning Design

## Goal

Reposition `sci-ssci-skills` as one evidence-preserving research-writing
workflow built from two complementary sources:

1. the section-by-section and reverse-engineering pedagogy associated with
   Hilary Glasman-Deal's *Science Research Writing*; and
2. writing observations distilled through the `sci-ssci-polishing` corpus
   pipeline, which starts from a 1,000-paper SCI/SSCI metadata candidate pool.

The README must make the repository understandable to a first-time visitor in
under 30 seconds without overstating the book relationship, corpus scope, or
evaluation results.

## Core Story

The repository does two connected jobs:

- `science-research-writing` helps researchers decide what each paper section
  needs to do and turns ideas, notes, data, references, or drafts into the next
  useful manuscript artifact.
- `sci-ssci-polishing` improves Chinese-to-English translation and existing
  English prose while preserving data, citations, terminology, limitations,
  and claim strength.

The public shorthand is:

> A research-writing classic informs how to build the paper. A curated
> SCI/SSCI corpus informs how to communicate it. Together, the Skills support
> the path from research materials to a polished manuscript.

The repository must not promise to produce a good or publishable paper on its
own. It helps users produce a better-structured, clearer, and more
evidence-faithful manuscript while leaving scientific judgment with the author.

## Accuracy Boundaries

- Say that `science-research-writing` is independently inspired by the book's
  general pedagogy. Do not imply affiliation, endorsement, reproduction, or an
  official digital edition.
- Say that the polishing project began with a 1,000-paper metadata candidate
  pool, screened to a 60-paper core portfolio, with aggregate observations
  reported from the 40-paper distillation split.
- Do not say that 1,000 full texts were downloaded, read, distilled, or used to
  train a model.
- Keep evaluation claims Skill-specific.
- Keep the copyright, data, affiliation, and professional-review limitations.

## README Information Architecture

Both `README.md` and `README_CN.md` will use the same structure:

1. Existing hero image.
2. Repository name and plain-language value proposition.
3. Short explanation of the two complementary foundations.
4. A three-column workflow chooser: current materials, Skill, and output.
5. One-sentence quick start and installation commands.
6. A short "why this exists" section explaining the book-inspired method.
7. A compact section-function table.
8. A memorable claim-boundary example using the milk-tea tasting scenario.
9. The corpus pipeline and its exact scope.
10. Three featured reusable mechanisms, followed by secondary components.
11. Skill-specific evaluation, boundaries, citation, and license.

The Mermaid flowchart moves below the workflow chooser. It supports the story
but does not lead it.

## First-Screen Copy

English headline:

> From research materials to a structured manuscript—without invented
> evidence, inflated claims, or rewritten science.

English supporting copy:

> Open-source Agent Skills for planning, drafting, revising, translating, and
> polishing research papers. Inspired by a widely used research-writing guide
> and informed by a curated SCI/SSCI corpus pipeline.

Chinese headline:

> 从研究材料到结构完整的论文：不编造证据，不夸大结论，不改写科学内容。

Chinese supporting copy:

> 经典写作方法帮助 Agent 理解论文应该怎么写；经过筛选的
> SCI/SSCI 论文语料帮助 Agent 理解论文应该怎么表达。

## Reuse and Citation

Promote three mechanisms first:

1. Evidence-Preserving Draft Contract;
2. Claim-Strength Contract;
3. Target-Journal Model Builder.

Keep the complete component list, but visually separate secondary utilities.
Provide a short repository-credit snippet and retain `CITATION.cff` for formal
citation. The wording must invite reuse under the repository license without
implying that attribution alone overrides third-party rights.

## Validation

Before publication:

- verify all relative links in both READMEs resolve;
- verify the two installation commands match installable Skill names;
- run the repository test suite;
- scan for prohibited overclaims about 1,000 papers, book affiliation, journal
  acceptance, and scientific correctness;
- compare English and Chinese headings, numbers, workflow choices, evaluation
  claims, and legal boundaries for parity.

