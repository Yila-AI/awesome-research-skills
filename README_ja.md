# SCI/SSCI Research Writing Skills

[English](README.md) · [中文](README_CN.md) · [한국어](README_ko.md)

> Turn your research into a clear, well-structured paper, section by section.

**Polish the writing. Never rewrite the science.** This repository provides open-source Agent Skills for planning, drafting, revising, translating, and polishing SCI/SSCI papers while preserving meaning, data, citations, limitations, and claim strength.

This short Japanese guide is for researchers who want to quickly understand what the repository does. The main documentation is maintained in English and Chinese.

## What Problem Does It Solve?

Many researchers, especially non-native English writers, use AI to improve academic writing. The risk is that the text becomes more fluent while the science changes silently:

- a cautious result becomes a causal claim;
- a limitation disappears;
- a number, citation, or technical term changes;
- the prose sounds stronger than the evidence supports.

These Skills are designed to help AI improve the writing while keeping the author's scientific meaning intact.

## Which Skill Should I Use?

| If you are... | Use |
|---|---|
| Starting from ideas, notes, results, tables, or references | `science-research-writing` |
| Drafting Introduction, Methods, Results, Discussion, Abstract, or Title | `science-research-writing` |
| Translating Chinese academic prose into English | `sci-ssci-polishing` |
| Polishing English without changing the science | `sci-ssci-polishing` |
| Building your own research Agent | Reuse the evidence and claim-strength mechanisms |

## Install

Node.js 18 or later is required.

```bash
# Start from research materials
npx skills add Yila-AI/sci-ssci-skills --global --agent codex --skill science-research-writing --yes --copy

# Translate or polish an existing draft
npx skills add Yila-AI/sci-ssci-skills --global --agent codex --skill sci-ssci-polishing --yes --copy
```

## Copy-Paste Examples

```text
Use $science-research-writing.
I have research materials but do not know how to organize them into a paper.
Here are my research question, methods, main results, and target journal:
[paste materials]
```

```text
Use $sci-ssci-polishing.
Please polish this Discussion paragraph.
Do not change numbers, citations, terminology, limitations, or claim strength.
If anything sounds overclaimed, flag it instead of silently rewriting it.

Text:
[paste paragraph]
```

## Reuse and Credit

If this repository helps your research Agent, writing tool, or academic workflow, please cite or credit:

```markdown
**Credit:** The evidence-preserving research-writing workflow is adapted from
[Yila-AI/sci-ssci-skills](https://github.com/Yila-AI/sci-ssci-skills),
including its Evidence-Preserving Draft Contract and Claim-Strength Contract.
```

See the full [English README](README.md) for examples, evaluation notes, corpus boundaries, copyright boundaries, and project credits.
