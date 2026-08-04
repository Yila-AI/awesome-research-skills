# Paper extraction and evidence ledger

## Purpose

Do extraction before slide planning. The deck can only preserve evidence that the ledger contains.

## Minimum pass

1. Extract the full PDF text in one pass; do not plan from headings alone.
2. Read the paper section by section in order.
3. Record every figure and table, including panel meaning and the source page.
4. Transcribe every table that may be needed in Q&A; a headline number is not a table extraction.
5. Record meaningful quantities with unit, comparison, direction, uncertainty, and source pointer.
6. Record limitations, undefined terms, and claims that the authors explicitly leave open.

## Ledger fields

Use a Markdown table or structured JSON with at least:

| Field | Meaning |
|---|---|
| `id` | Stable claim/figure/table identifier |
| `kind` | question, method, quantity, figure, table, limitation, author-claim, presenter-synthesis |
| `statement` | Faithful paraphrase or exact data label |
| `source_anchor` | section, figure/table, page, or URL |
| `entities` | Protected names, variables, groups, datasets, or instruments |
| `certainty` | reported, inferred, author-qualified, or unresolved |
| `used_on` | Slide IDs that use this item |

Do not convert `inferred`, `author-qualified`, or `unresolved` items into unqualified claims. Mark presenter synthesis visibly in the deck and notes.

## Figures and tables

Prefer lossless source crops or native charts. Preserve panel labels, axes, units, legends, and captions. Never stretch a figure to fill a frame. If a multi-panel figure is too small, split panels across slides and repeat the source anchor. If extraction fails, render the source page and crop only the stated region; record the fallback in `run-log.md`.

## Extraction quality gate

Before design, verify:

- the ledger contains the research question and author-stated contribution;
- all content slides can be assigned at least one source anchor;
- every displayed number can be traced to a ledger item;
- all main figures and tables have a reading note;
- limitations are represented, not silently omitted;
- the ledger is substantial enough to support selection rather than filler (target 10–20% of the paper body text for a normal empirical paper, with zero table rows treated as a failure regardless of ratio).
