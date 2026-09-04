# Research Presentation: one-minute start

The public title of `research-presentation` is **Paper to Slides**. It turns a paper, manuscript, results, figures, or research notes into a source-grounded academic presentation instead of splitting an abstract across a series of text-heavy slides.

## Install

The installer requires Node.js 18 or later:

```bash
npx skills add Yila-AI/awesome-research-skills \
  --global \
  --agent codex \
  --skill research-presentation \
  --yes \
  --copy
```

## Use

```text
Use $research-presentation to turn this paper into a source-grounded research presentation.
Audience: [journal club / lab meeting / conference / seminar / thesis defense]
Time: [minutes]
Language: [English / Chinese / bilingual]
Output: editable PPTX, speaker notes, and a source map
```

Then attach a paper PDF, research materials, figures, tables, or supporting notes that you are allowed to process.

## What it delivers

- a one-sentence narrative purpose and outline for each slide;
- an evidence ledger that anchors important numbers, figures, and conclusions to their sources;
- editable slide content, speaker notes, and a coherent visual system;
- a rendered slide-by-slide review of overflow, density, sourcing, figure readability, and claim boundaries;
- an explicit list of missing evidence, conflicting inputs, and points that require author confirmation.

If you have only one paper, begin with:

```text
Use $research-presentation. Turn the attached paper into a 10-minute journal-club deck.
Keep every quantitative claim traceable to a figure, table, section, page, or DOI.
```

Next: [use cases](use-cases.md) · [paper-extraction contract](../../skills/research-presentation/references/paper-extraction.md) · [QA contract](../../skills/research-presentation/references/qa-contract.md) · [中文](getting-started_CN.md)
