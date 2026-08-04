# Layout recipes

Pick a layout from what the slide has to carry. Every recipe below is a
starting arrangement — adapt the column count, swap a card for a figure, drop
a row. What matters is that the arrangement matches the content's shape.

Most recipes share the same frame: a **kicker** (9–10 pt, uppercase, accent
colour) above a **title** (28–32 pt), content below, and an optional
**footnote** (9 pt, muted) for sources. That frame is what makes different
layouts read as one deck.

## Dense layouts — use these for content slides

Each clears the density floor when filled properly.

### metric-grid
Three to five headline numbers. Kicker + title, then an N-column grid of
cards; each card is label (9 pt uppercase muted) / value (36–44 pt Bold,
mono) / delta (10 pt, semantic colour). Add a one-line note under the grid
saying what the numbers are measured over.
*Typical: 18–24 shapes.*

### two-column
Claim on the left, evidence on the right — the workhorse for a result slide.
Left: a short lede (13 pt) plus three to five labelled points. Right: the
figure, table, or code block. Keep the columns top-aligned and give the
figure the wider share (roughly 40/60) when it carries detail.
*Variant — annotated figure:* when one source figure is the whole point, give
it the full width at its true aspect (never stretch) and replace the left
column with three to five numbered call-out chips pointing at the parts that
matter, plus a caption crediting the source. A bare, uncommented figure makes
the audience hunt.
*Typical: 14–20 shapes.*

### card-grid
Three or six parallel items — approaches, cohorts, failure modes. Each card:
title (16–18 pt Semibold), two-to-three-line description (11 pt), optional
tag. Three across reads best; six wants two rows of three.
*Variant — checklist:* for criteria with status (reproducibility checks,
inclusion criteria, submission readiness), drop to rows of icon + item +
status tag, grouped under two or three headings.
*Typical: 15–30 shapes.*

### comparison
Two options judged on the same axes. Either two columns with matched rows, or
a table with the criteria down the left. Mark the verdict explicitly — a tag,
a tick, a coloured cell — because a comparison without a conclusion makes the
reader do the work.
*Variant — pros and cons:* for limitations, threats to validity, and method
trade-offs, head each side with a one-line summary judgement in contrasting
semantic colours, then three to five specifics.
*Typical: 18–28 shapes.*

### table
Dense structured data. Header row in accent or `text-strong` on `surface`,
body rows 10–11 pt, zebra banding in `surface`, numbers right-aligned in
mono. Keep to seven columns; beyond that, split the slide or move detail to
the appendix.
*Typical: 25–45 shapes.*

### process-steps
A sequence of three to six stages. Numbered chips along a horizontal band,
each with a title (14–16 pt) and one line of detail (10–11 pt); connect them
with arrows or a rule. Say what moves between stages, not just their names.
*Variant — timeline:* when the stages are events against dates, run them along
a horizontal rule with dated markers, alternating labels above and below so
they do not collide. Good for study design, cohort enrolment, or the arc of a
literature.
*Typical: 15–24 shapes.*

### architecture-diagram
System or method structure. Boxes in `surface` with 1 pt borders, arrows in
`text-muted`, labels on the arrows saying what flows. Group related boxes in
a lightly tinted container with its own small caption.
*Typical: 25–50 shapes.*

### code-or-terminal
A snippet with commentary. Mono at 10–11 pt in a `surface` block with a
title bar; keep to about fifteen lines and put the explanation beside it, not
below. Highlight the two or three lines that matter.
*Typical: 12–20 shapes.*

## Sparse layouts — at most three per deck

### cover
Title (40–56 pt), one-line subtitle, author/venue/date, optional full-bleed
image. Nothing else.

### section-divider
A number, a section name, and one line saying what the section will settle.

### stat-highlight
One number at 72–96 pt with a single sentence of context. Reserve it for a
result the whole talk turns on.

### quote
One pulled quote at 24–32 pt with attribution. Use for a reviewer comment, a
definition, or a claim you are about to challenge.

### closing
Take-home points (three at most), contact, and — for a defense or a talk with
Q&A — the questions you expect and your one-line answers.

## Composition notes

- For a two- or three-slide section, use **progressive disclosure** rather than repeating one layout: begin with the system, figure, or claim at overview level; then devote the next slide to its contracts, diagnostic details, comparison axes, or numbered observations. Reuse the same visual vocabulary, but give the focused slide a distinct job.
- If a referenced figure is unavailable to the build script, make a clearly labelled structural reconstruction with native shapes. Carry over only relationships stated in the source brief (stages, flow, marked errors, comparisons, or alignments), and add numbered observations that tell the audience what to inspect; do not fabricate image-specific detail.

- Vary the layout every two to three slides. Six card-grids in a row reads as
  a template, not a design.
- Keep one consistent margin (0.5–0.6 in) and one gutter (0.2–0.25 in) across
  the deck; irregular gaps are the most common reason a deck looks amateur.
- Align to a grid. Twelve columns is plenty: full width, halves, thirds,
  quarters, and 40/60 cover nearly every recipe above.
- Let a slide breathe at its edges but not in its middle: a wide outer margin
  with tight, regular interior spacing reads dense-but-calm, which is the
  target.

**Treat 9–10 pt text as a scarce annotation budget, not a default styling tool.** Do not put sentences, repeated card subtitles, explanatory tags, figure labels, or footer prose at 9–10 pt. Make these 11 pt body text, remove them, or consolidate them into one short caption. Before adding a small label, ask whether its meaning is already conveyed by position, colour, or a larger heading. A few short kickers/page numbers are safe; many small labels across a grid are not, because the character-weighted audit counts every one.

In code, define explicit `BODY_PT = 11` (or larger) and `ANNOTATION_PT = 9 or 10` constants, and use the latter only for truly short metadata. Never use a font size below 9 pt: renderer-visible microtext is both unreadable and likely to fail the distribution check.
