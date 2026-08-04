# Colour themes

Pin one theme for the whole deck and use its tokens everywhere: the same
accent for every kicker, the same surface for every card. A deck reads
designed because its colours repeat, not because it has many of them.

Each theme gives you: page background, card surface, three text levels, one
accent, and semantic colours for up/down/flat. Everything else is restraint —
if a colour is not in the theme, it does not go on the slide.

All six are distilled from real Chinese academic templates, and each carries a
page frame as well as a palette — the frame is most of what makes a deck read
as an academic report rather than a generic slide deck. **Choose by occasion
first, colour second**, and when nothing else decides it, `zju-navy` is the
safe default: its rail suits the most common request, a paper walked through
section by section.

There is deliberately no neutral corporate or editorial theme here. A deck
built for a lab meeting, a defense, or a grant panel should look like one; if
a request genuinely needs something else, say so rather than bending an
academic frame into a shape it was not distilled for.

## zju-navy — left-rail navigation, for a lab meeting or journal club

Distilled from a Chinese university group-meeting template. Its identity is
not the colour, it is the **standing left rail**: a deep navy column listing
every section of the talk, with the current one lit. The audience always knows
where they are, which is exactly what a long literature report needs.

| Token | Value | Use |
| --- | --- | --- |
| background | `#FFFFFF` | page |
| rail | `#003F88` | the left navigation column |
| rail-active-bg | `#FFFFFF` | current section's row inside the rail |
| rail-active-text | `#003F88` | current section's label |
| rail-text | `#E8F0FA` | the other sections' labels |
| surface | `#FFFFFF` | content cards (outlined, not filled) |
| surface-tint | `#CAE2FF` | the one pulled-out evidence panel |
| text-strong | `#003F88` | slide titles, card titles |
| text-body | `#1F2329` | body copy |
| text-muted | `#5A6B7F` | captions, sources |
| accent | `#003F88` | kickers, rules, the header square |
| accent-alt | `#CA865F` | second-level emphasis, terracotta |
| up / good | `#1A7A4A` | improvement |
| warn | `#B5541A` | caveats |

Fonts: `Inter` + `Noto Sans CJK SC`. Corners 0–2 pt, no shadows. Borders are
the signature: **1 pt dashed** in `accent` around content groups, and a
hairline rule under the slide title that runs to a small dot at the right
edge.

The rail, when you use it:

- About **19% of the page width**, full height, filled `rail`.
- One row per section, ~16% of page height each, so it comfortably holds
  **five or six sections**. With more than that, drop the rail rather than
  shrinking rows — a cramped rail is worse than none, and the density contract
  still governs the content area.
- The current row is a white block with `rail-active-text`; the rest sit in
  `rail-text` on the navy.
- Content then lives in the remaining ~81%: header band with a small `accent`
  square, the section number and title, then dashed-outlined columns. The
  header's hairline rule and everything under it hang off the **measured
  bottom of the wrapped title**, not a fixed offset — the content area is
  narrower than a full page, so titles wrap here more often than they would
  full-width, and a rule at a constant offset gets struck through the second
  line.
- The rail's top ~15% is where an institution mark goes **if the user supplied
  one**. With no mark, leave that space empty — do not draw a placeholder box.
  An empty outlined square reads as a rendering bug, not as a reserved slot.
  Never invent a university logo or name.

The rail is optional, not required. Skip it for the cover, section dividers,
and closing slide, and skip it entirely when the deck has no clean section
list — a full-width layout in these same tokens still reads as this theme.

**Laying out the content half.** The rail owns the left ~19%; you are arranging
the remaining ~81%. Header band across that area: a small accent square, the
section number and title, a hairline rule ending in a dot at the right edge.
Below it, two or three **dashed-outlined** columns — the dashed border, not a
fill, is what groups them. One column may be the tinted evidence panel
(`surface-tint`) carrying the takeaway bullets while the others hold figures.
Because the rail already eats a fifth of the width, keep to two or three
columns and let the figures shrink rather than the type.

## pku-crimson — the same left rail in university crimson

Distilled from a crimson left-rail template. It shares `zju-navy`'s frame
exactly — measured rail width 19.5% against navy's 19.4%, the same dashed
content columns, the same dot-terminated rule under the title — so **build it
with the rail rules above**; only the palette differs.

Crimson reads more ceremonial and more institutional than navy, and it carries
further in a large room. Navy is calmer to sit in front of for an hour. Pick
crimson when the institution's own colour is red, when the occasion is formal
(a defense, an opening report), or when navy would fight the subject matter;
pick navy for a long reading-heavy session.

| Token | Value | Use |
| --- | --- | --- |
| background | `#FFFFFF` | page |
| rail | `#8B0012` | the left navigation column |
| rail-active-bg | `#FFFFFF` | current section's row inside the rail |
| rail-active-text | `#8B0012` | current section's label |
| rail-text | `#F6E7E9` | the other sections' labels |
| surface | `#FFFFFF` | content cards (outlined, not filled) |
| surface-tint | `#F7E4E6` | the one pulled-out evidence panel |
| text-strong | `#8B0012` | slide titles, card titles |
| text-body | `#1F2329` | body copy |
| text-muted | `#6B5A5C` | captions, sources |
| accent | `#8B0012` | kickers, rules, the header square |
| accent-alt | `#CA865F` | second-level emphasis, terracotta |
| up / good | `#1A7A4A` | improvement |
| warn | `#B5541A` | caveats |

Fonts, corners, and the dashed-border signature are `zju-navy`'s. Crimson on
white is a strong contrast, so keep filled crimson to the rail and the header
square — a crimson card behind crimson text is unreadable, and large crimson
areas beyond the rail read as a warning rather than a frame.

## deep-violet — top section band, for a defense or project review

Distilled from a Chinese project-completion defense template. Its identity is
the **full-width violet header band** carrying an oversized section number,
and violet knock-out tags that bite into card titles.

| Token | Value | Use |
| --- | --- | --- |
| background | `#FFFFFF` | page |
| band | `#660874` | the top header band |
| band-text | `#FFFFFF` | section number and title inside the band |
| surface | `#F7F2F7` | cards, violet-tinted |
| surface-alt | `#F3F5F9` | alternate/cool card, for contrast pairs |
| surface-foot | `#F2F2F2` | the bottom attribution strip |
| text-strong | `#2A0A30` | card titles, key numbers |
| text-body | `#333333` | body copy |
| text-muted | `#6B6B6B` | captions, sources |
| accent | `#660874` | tags, emphasis, arrows |
| accent-alt | `#4472C4` | secondary emphasis, chart series |
| attention | `#C00000` | the one number that matters |
| up / good | `#1A7A4A` | improvement |

Fonts: `Inter` + `Noto Sans CJK SC`, numbers in `JetBrains Mono`.
Corners 4 pt, no shadows, card borders 1 pt in `rgba(102,8,116,.18)`.

The band and the tags:

- Header band spans the full width and is **sized from its title, not fixed**.
  About 11% of page height is what a one-line title needs; a title that wraps
  to two lines needs a band that grows with it. Measured decks that pinned the
  band at 11% clipped the first line of a wrapped title at the top and spilled
  the second line out below — the band is a container, and containers are
  sized from their content like every other one. Compute the title's wrapped
  line count at its actual size, add the band's padding, and take the larger
  of that and the one-line height. Inside: the section number at 40–44 pt in
  `band-text` at ~55% opacity, then the section title at 28–32 pt solid. The
  right end of the band is where an institution mark goes **if the user gave
  you one**; with no mark, leave it empty rather than drawing an empty
  placeholder square.
- A **knock-out tag** is a small `accent` rectangle holding 2–4 characters in
  `band-text`, sitting at the left of a card's title row so the tag and the
  title read as one line. About 4% of page height suits a one-line title; when
  the title beside it wraps, the tag stays put and **everything below the
  title moves down** — a rule or divider placed at a fixed offset from the
  card's top will be struck through by the second line. Derive every following
  element's position from the title's measured bottom edge, never from a
  constant. Use tags to label parallel items (Topic 1 / Topic 2), never for
  decoration.
- Chains of steps use a `accent` chevron between compact cards rather than a
  drawn arrow with a shaft.
- Close a slide with the attribution strip: full-width `surface-foot`, one
  line of `text-muted`, for who did the work or where the data came from.

**Two signature compositions.** For parallel items, run a `card-grid` under the
band where each card title opens with a knock-out tag and the title continues
on the same line; body underneath as labelled fragments, optionally a row of
small figures inside the card, closing with the attribution strip. For steps
that hand off to each other, run `process-steps` with the chevron instead of an
arrow — four or five compact two-line cards across one row, each naming what
happens and what comes out; beyond five, wrap to a second row rather than
shrinking the type.

## nsfc-slate — slate and orange, for a grant application or funded-project defense

Distilled from an NSFC application-defense template. Slate navy carries the
structure, orange carries the counterpoint — the two-column comparison
(需求 vs 现状, 目标 vs 基础) is this theme's native gesture, one column headed
slate and the other orange.

| Token | Value | Use |
| --- | --- | --- |
| background | `#FFFFFF` | page |
| band | `#44546A` | cover band, section number block, footer strip |
| band-text | `#FFFFFF` | text on slate |
| surface | `#FFFFFF` | cards — outlined `rgba(68,84,106,.25)`, faint shadow |
| surface-tint | `#F2F4F7` | secondary panels, table bands |
| text-strong | `#333B47` | titles, key numbers |
| text-body | `#3F454F` | body copy |
| text-muted | `#767171` | captions, sources |
| accent | `#44546A` | pills, numbered discs, rules |
| accent-alt | `#ED7D31` | the contrast column, arrows, progress marks |
| attention | `#C00000` | the one number or clause that must be seen |
| up / good | `#1A7A4A` | improvement |

Fonts: `Inter` + `Noto Sans CJK SC`, numbers in `JetBrains Mono`.
Corners: pills for column headers (full-height radius), 4 pt on cards.

The chrome:

- Content-page header is light: a small slate corner tab at the top-left
  (sized to its section label, roughly 10% of page height for one line), the
  slide title beside it in `text-strong`, a hairline under both. No full-width
  band — the slate mass lives on the cover and section pages instead.
- **Paired columns are the signature** — this theme's form of `comparison`,
  and it fits any two-sided argument: need versus current state, goal versus
  foundation, before versus after. Each column opens with a pill-shaped header
  (one slate, one orange), then numbered discs (①②③) in the column's colour
  with a bold lead-in and a 12 pt explanation. A dashed vertical rule separates
  the columns. Keep the two columns to the same number of points; an unequal
  pair reads as an unfinished thought rather than a contrast.
- Section pages: an oversized number in a filled slate square, the section
  title at 32–40 pt beside or below it, a short rule, and a slate strip along
  the page bottom. These pages are sparse by design and count against the
  sparse-layout budget.
- `attention` red is for the standout clause or number an NSFC reviewer must
  not miss — one per slide at most, never decoration.

## forest-green — deep green with a standing title panel, for ecology and field sciences

Distilled from a joint-fund (subtropical forest) template. A deep evergreen
panel anchors the cover and contents pages; content pages stay light with a
green title line and a tinted evidence panel. The original dresses its panel
with landscape photography — abstract that to solid `panel` fill unless the
user supplies imagery; never source your own.

| Token | Value | Use |
| --- | --- | --- |
| background | `#FFFFFF` | page |
| panel | `#0E5849` | the standing left panel on cover/contents |
| panel-text | `#FFFFFF` | vertical display type on the panel |
| surface | `#FFFFFF` | content cards, outlined `rgba(14,88,73,.28)` |
| surface-tint | `#EDF3F2` | the evidence/summary panel, table bands |
| text-strong | `#0E5849` | slide titles, card titles |
| text-body | `#1F2329` | body copy |
| text-muted | `#5F6B67` | captions, sources |
| accent | `#0E5849` | title underline, number chips, footer strip |
| accent-alt | `#FFC000` | sparing warm emphasis |
| attention | `#C00000` | annotation frames on figures, the flagged value |
| up / good | `#1A7A4A` | improvement |

Fonts: `Inter` + `Noto Sans CJK SC`; the panel's display type may use
`Noto Serif CJK SC` for the traditional 竖排 flavour, body never does.
Corners 2–4 pt, shadows faint.

The chrome:

- Cover and contents: the `panel` fills the left ~30% of the page, carrying a
  short vertical title in `panel-text`; the right side holds the TOC as rows
  of number chips (01 02 03…) — the current section's chip solid `accent`
  with dark text, the rest greyed. Reuse the same page as a section divider
  by advancing the highlighted chip.
- Content pages: no panel. Title in `text-strong` with a short `accent`
  underline hung from the title's measured bottom, a full-width one-line
  summary strip in `surface-tint` or outlined white beneath it, then the
  content grid. A 1%-height `accent` strip closes the page bottom.
- Figures may carry `attention`-red annotation frames to point at the region
  under discussion — the frame is evidence markup, not decoration, and wants
  a caption explaining what it flags.

## bright-azure — figure-forward, for a project defense that argues with pictures

Distilled from an NSFC application/completion template. Where `nsfc-slate`
argues in paired text columns, this one argues in **rows of figures**: a
strip of four images across the page, chained by an arrow, framed above and
below by a claim and a conclusion. Choose it when the evidence is visual —
microscopy, device stacks, model architectures — and the talk is a walk
through pictures rather than through numbers.

| Token | Value | Use |
| --- | --- | --- |
| background | `#FFFFFF` | page |
| band | `#0066CC` | header band, gradient-capable toward `#2E80D4` |
| band-text | `#FFFFFF` | section number and title inside the band |
| surface | `#FFFFFF` | figure frames and claim boxes, outlined `#2E80D4` |
| surface-tint | `#DDF2FF` | the mid-page emphasis strip |
| surface-alt | `#EBEFF4` | secondary panels, table bands |
| text-strong | `#0066CC` | slide titles, card titles, figure labels |
| text-body | `#1F2329` | body copy |
| text-muted | `#5A6B7F` | captions, sources |
| accent | `#2E80D4` | chips, arrows, frames |
| attention | `#C00000` | the claim sentence and the flagged region |

Fonts: `Inter` + `Noto Sans CJK SC`, numbers in `JetBrains Mono`.
Corners: pill-shaped figure captions, 4 pt on frames.

The chrome:

- Header band across the top, about **14.5% of page height** for a one-line
  title — and like every other band, it grows with a title that wraps. Inside:
  section number then title in `band-text`, left-aligned.
- **The figure strip is the signature.** Three or four framed images in a row,
  each with a pill caption beneath it in `accent`, and a solid arrow between
  the last two showing the direction of the argument. Frames share one height;
  images letterbox inside them rather than stretch.
- Above the strip sits the claim — a white outlined box whose lead-in phrase
  is `attention` red and whose body is `text-body`. Below it sits the
  conclusion in the same shape. Claim, evidence, conclusion, top to bottom.
- A `surface-tint` full-width strip carries the one-line thesis between the
  claim and the figures when the argument needs a beat.
- Because this theme leans on images, the extraction contract's figure crops
  matter more here than anywhere: a figure strip built from redrawn
  approximations is worse than a text layout. Every frame carries a real crop
  from the source, letterboxed — a stretched micrograph is a delivery-blocking
  defect, not a styling choice.

## Applying a theme

- Set the slide background explicitly; the PPTX default white is not any of
  these themes' background.
- Cards are a filled rectangle in `surface` plus a 1 pt border — that pair is
  what makes a grid read as cards rather than floating text. Fills are also
  the cheapest way to raise ink coverage: text alone covers a few percent of
  a page, while the same text inside filled cards covers the block it sits
  in. A deck that reads empty is usually a deck of unfilled text boxes.
- Give a card real padding (0.15–0.2 in) and let it span its full grid cell.
  Cards sized to their text leave ragged gaps; cards sized to the grid form
  the even bands that make a page look composed.
- Use accent sparingly: kickers, one rule under the title, one highlighted
  number. An accent used on everything stops being an accent.
- Semantic colours (up/warn/down) carry meaning; never use them decoratively.
- Check contrast: body text against its own surface, not against the page.
