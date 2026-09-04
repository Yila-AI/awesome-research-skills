# Academic Humanizer — Lean Distribution

This is the use-only distribution of [`academic-humanizer`](https://github.com/Yila-AI/awesome-research-skills/tree/main/skills/academic-humanizer). It removes generic, templated, and AI-like patterns from Chinese or English academic prose while preserving the science.

It is an editing aid, not an AI-detector bypass. It does not certify that text is human-written, and researchers remain responsible for following the disclosure policy of their journal, institution, or funder.

## Install

Move the extracted `academic-humanizer` directory into the Skills directory used by your Agent, then invoke:

```text
$academic-humanizer
```

If your Agent supports the Skills CLI, install only this Skill directly from the repository:

```bash
npx skills add Yila-AI/awesome-research-skills --global --agent codex --skill academic-humanizer --yes --copy
```

## Try it

```text
Use $academic-humanizer in standard mode.
Make this academic passage less templated and more natural.
Do not change any claim, number, citation, limitation, or uncertainty.
Return the revised text, patterns changed, preservation audit, and author questions.

Text:
[paste your passage]
```

See three complete examples—from user input through each optimization to the final output—in the [English walkthrough](https://github.com/Yila-AI/awesome-research-skills/blob/main/examples/academic-humanizer-walkthrough.md) or [Chinese walkthrough](https://github.com/Yila-AI/awesome-research-skills/blob/main/examples/academic-humanizer-walkthrough_CN.md).

## What it does

- audits repeated academic AI-writing patterns in Chinese and English;
- removes empty framing, inflated significance, mechanical transitions, and synthetic cadence;
- calibrates the revision to genuine author writing samples when supplied;
- checks that numbers, citations, reference labels, and protected terms survive the edit;
- reports claim-evidence gaps instead of inventing support.

The archive includes the complete runtime Skill, references, deterministic invariant checker, Agent metadata, third-party notice, and repository license.

The Skill is built and maintained by [Yila.ai](https://yila.ai/?utm_source=github&utm_medium=release&utm_campaign=awesome-research-skills), where literature, evidence, data, writing, and presentation can remain connected across the research workflow.
