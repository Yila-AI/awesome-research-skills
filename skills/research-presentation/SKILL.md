---
name: research-presentation
description: Create, revise, and quality-check source-grounded research presentations from papers, research notes, data, or manuscripts. Use for paper-to-slides, research presentation, scientific presentation, journal club, lab meeting, conference talk, seminar, thesis defense, dissertation defense, PPT/PPTX, 学术PPT, 科研汇报, 论文汇报, 组会汇报, 答辩PPT, and related slide-deck tasks.
license: Apache-2.0; see NOTICE for third-party attributions
---

# Research Presentation

Turn a paper or research corpus into a presentation that an audience can follow, verify, and discuss. The core promise is **paper to slides without losing the evidence**: preserve source meaning, choose a cumulative narrative, make figures legible, keep claims bounded, and deliver an editable deck with notes and a rendered QA trail.

This Skill owns the workflow from source inspection through final slide QA. It does not replace the author's scientific judgment, invent results, or silently strengthen a claim.

## Route the request

Choose the narrowest route that satisfies the request:

| Input / request | Route |
|---|---|
| One or more PDFs, papers, or manuscripts | Full paper-to-slides workflow below; read `references/paper-extraction.md` first |
| Research notes, tables, figures, or a protocol | Evidence-led presentation workflow; mark unsupported fields instead of filling them |
| Existing PPTX to revise | Inspect the source deck, preserve its visual contract when requested, then run the same render/QA loop |
| A presentation brief with no source document | Skip extraction, but still create a claim ledger, narrative outline, source/asset notes, and visual QA |
| “Make it prettier” or “change the style” | Diagnose the current deck before editing; preserve scientific content and citations |

Before building, infer one sentence:

> By the end, **[audience]** should **[understand/decide/discuss]** because **[central evidence-backed takeaway]**.

Ask at most one blocking question when a missing choice would change the deck materially (for example, defense versus journal club). Otherwise make a conservative assumption and state it in the run log.

## Non-negotiable contracts

1. **Evidence first.** Read the source before planning the slide sequence. Never use a figure, number, table cell, citation, mechanism, or limitation that is not traceable to the supplied source or an explicitly cited external source.
2. **Bounded claims.** Preserve population, setting, time frame, comparison, uncertainty, and claim strength. Distinguish author conclusions from presenter interpretation and label the latter.
3. **One narrative job per slide.** Use takeaway titles that answer the question raised by the previous slide; do not build an inventory of paper sections.
4. **One visual anchor per content slide.** Use a readable original figure/table, a meaningful metric, or a simple source-faithful diagram. Avoid decorative diagrams and generic stock imagery.
5. **Readable before complete.** Start body text at 12 pt (11 pt floor), titles at 28–32 pt, cover title at 40–56 pt, and keep sub-11-pt characters below 10% of the deck. Add a slide or cut copy instead of shrinking type.
6. **Source anchors everywhere.** Every content slide carries a visible anchor such as `Fig. 2`, `Table 1`, `§3.2`, or `p. 7`; speaker notes include a `[Sources]` block for claims and assets.
7. **No silent raster-only handoff.** Prefer native/editable text, tables, shapes, and charts. Use source figures as images when needed, but preserve their aspect ratio and provide the original asset or source map.
8. **Render before delivery.** Render every final slide, inspect the full-size pages, run overflow/coverage/font checks, and fix unintended overlap, clipping, wrapping, stretched figures, and empty placeholders.

## Paper-to-Slides workflow

### 1. Inventory and extract

Record the input files, target audience, language, venue, duration, expected slide count, output format, and available tools. Extract the entire paper text in one pass before section planning. Then work through the paper in order and write an evidence ledger containing:

- research question, gap, hypotheses, and contributions as the authors state them;
- study design, data, sample/population, baselines, parameters, and analysis steps;
- every meaningful quantity with unit, comparison, direction, and source pointer;
- every figure and table: what it shows, how to read it, and which panels matter;
- limitations, threats to validity, undefined terms, and out-of-scope claims;
- claims that are author judgments versus presenter synthesis.

For a PDF, use the host PDF tools or PyMuPDF/PDF extraction available in the environment. Use a lossless figure/table extraction tool when available; otherwise record the fallback and crop from rendered pages without changing the data. Read `references/paper-extraction.md` for the full ledger contract.

### 2. Choose the talk contract

Use the venue to set the arc:

- **Journal club / lab meeting:** question → gap → model/method → strongest evidence → limitations → discussion questions.
- **Conference talk:** problem → contribution → method → result → implication, with fewer side details.
- **Thesis defense:** problem → research program → methods → contribution-by-contribution evidence → limitations → future work.
- **Seminar / teaching:** motivating example → concept → worked evidence → application → recap.

Default to 12 content-bearing slides unless the user specifies another length. A 12-minute talk usually needs 10–14 slides; add pages when the evidence cannot remain readable.

### 3. Build the ghost deck

Write one line per slide before designing:

```text
S01 Cover — what is the paper and why should this audience care?
S02 Question — what existing assumption is being challenged?
S03 Mechanism — what system or design tests the question?
S04–S08 Evidence — what does each result establish, and what does it not establish?
S09 Validation — which checks support the interpretation?
S10 Boundary — where does the evidence stop?
S11 Synthesis — what are the three defensible takeaways?
S12 Discussion — which next question is worth asking?
```

For each slide specify: narrative title, one-sentence takeaway, evidence anchor, visual anchor, speaker-note purpose, and what the audience should do next. Delete repeated summaries and generic “Methods / Results” titles unless they are paired with a claim.

### 4. Select the visual system and layouts

Read `references/themes.md` before choosing colours and `references/layouts.md` before arranging the first content slide. Choose one theme for the entire deck; choose layouts from the content's shape, not from a fixed template sequence.

Use the theme's page frame and tokens consistently. Prefer two-column claim/evidence, annotated figure, comparison, metric-grid, process-steps, architecture, table, and closing layouts. Use sparse cover, divider, stat-highlight, quote, and closing slides sparingly. Vary the silhouette every two or three slides, but keep margins, title placement, footer anchors, and typography stable.

Do not invent an institutional logo, affiliation, dataset, chart, or missing figure. If an image is unavailable, build only a clearly labelled structural reconstruction from relationships stated in the source.

### 5. Build the editable deck

Use the host presentation workflow and keep the implementation reproducible. In Codex environments follow the active presentation toolchain; in other Agent hosts use their native slide writer. Keep generated source code, extracted evidence, figure manifest, and build log beside the deck. Use source figures at their native aspect ratio. Put short citations in visible footers and full `[Sources]` blocks in notes.

Speaker notes should contain, in order:

1. the spoken transition into the slide;
2. the one result or idea to emphasize;
3. caveats or interpretation boundaries;
4. a `[Sources]` block with paper/figure/table/page or URL references.

### 6. Render and audit

Render the final PPTX to PDF and one PNG per slide. Run the bundled scripts when their dependencies are available:

```bash
python scripts/render_slides.py deck.pptx --outdir rendered
python scripts/audit_pptx.py deck.pptx --rendered rendered --report qa-report.json
```

Inspect every slide at full size, not only a contact sheet. Repair:

- overflow, clipping, accidental overlap, and title wrapping;
- body text below the floor or excessive annotation text;
- figures stretched, blurred, or too small to read;
- missing source anchors, notes, page numbers, or unresolved placeholders;
- slides below the visual-coverage floor or with large unexplained dead bands;
- repeated card grids that make the talk feel mechanically templated.

Re-render after every substantive repair. Do not claim a deck is clean from an audit that did not inspect the latest rendered files.

## Output contract

Return a primary editable `.pptx` whenever the host supports it, plus:

```text
deck.pptx
deck.pdf
rendered/slide-01.png ...
evidence-ledger.md or extraction.md
deck-outline.md
speaker-notes.md (when notes cannot be embedded)
source-map.md
qa-report.json or qa-report.md
run-log.md
```

If a required capability is unavailable, deliver the safe artifacts that are possible and state exactly what was not produced. Never present a screenshot-only fallback as an editable PPTX.

## Bundled resources

- `references/themes.md` — six academic themes, tokens, frames, and signature compositions.
- `references/layouts.md` — theme-neutral layout recipes and density guidance.
- `references/paper-extraction.md` — extraction, figure, table, quantity, and source-anchor contract.
- `references/narrative-planning.md` — audience, arc, ghost-deck, and speaker-note guidance.
- `references/qa-contract.md` — render, overflow, readability, coverage, and provenance checks.
- `references/rendering.md` — cross-platform fonts, PDF/PNG rendering, and editable-output boundaries.
- `scripts/render_slides.py` — thin wrapper around LibreOffice/Poppler when installed.
- `scripts/audit_pptx.py` — deterministic structural and rendered-file checks.
