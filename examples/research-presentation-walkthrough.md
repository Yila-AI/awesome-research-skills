# Paper to Slides：最小工作流示例

下面的示例展示如何把一篇论文交给 `research-presentation`。它不是某一篇论文的固定模板，而是一个可复用的输入契约。

```text
Use $research-presentation.

Turn the attached paper into a 12-minute conference presentation.
Audience: researchers outside the paper's narrow subfield.
Language: English.
Output: editable PPTX, speaker notes, source map, evidence ledger, and a render-based QA report.

Requirements:
- Keep the main narrative to one research question and three takeaways.
- Trace every number and figure to a section, page, figure/table number, or DOI.
- Preserve uncertainty, limitations, and the authors' original claim strength.
- Ask one focused question if a missing detail would force a scientific guess.
```

## Expected intermediate artifacts

1. **Material inventory** — PDF text, figures, tables, captions, references, and missing items.
2. **Talk contract** — audience, duration, language, purpose, and template constraints.
3. **Ghost deck** — one sentence per slide before visual styling.
4. **Evidence ledger** — source anchor and claim-strength check for every consequential claim.
5. **Editable deck and notes** — slide content that can be revised by the author.
6. **Render QA** — PDF/PNG inspection plus a report of overflow, density, anchors, and notes.

The output is complete only when the author can answer “where did this claim come from?” for every consequential statement.
