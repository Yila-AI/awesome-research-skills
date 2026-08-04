# Research presentation QA contract

## Structural checks

- PPTX opens and contains the expected number of slides.
- Every content slide has a title, a visual anchor, and a source anchor.
- Notes exist for every slide or a separate speaker-notes file exists.
- Text boxes, figures, tables, and connectors do not overlap unintentionally.
- No placeholder text, empty image frames, or invented logos remain.

## Typography and density

- Cover title: 40–56 pt; slide titles: 28–32 pt; body: 12 pt target, 11 pt floor.
- Sub-11-pt characters stay below 10% of all visible text characters.
- Titles do not wrap unexpectedly; shorten copy or grow the title container.
- Each non-exempt content slide has a clear visual anchor and meaningful rendered coverage; large blank panels are defects.

## Scientific fidelity

- Every number, table cell, figure, claim, limitation, and citation is traceable.
- Original figures preserve aspect ratio and source labels.
- Presenter interpretation is labelled separately from author conclusions.
- No confidence interval, effect size, mechanism, or implication is fabricated.

## Render gate

Render the exact final PPTX after the last edit. Inspect every page at full size and use a contact sheet only for deck-level rhythm. Record tool versions, commands, fallbacks, and unresolved limitations in `run-log.md`. A clean structural audit is not a substitute for visual inspection.
