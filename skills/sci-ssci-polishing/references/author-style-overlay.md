# Author style overlay

An optional surface-style layer supplied by the user: a house style, a group
or supervisor convention, a personal voice, or a journal's language
preferences. It governs **wording only**, never scientific content.

The overlay is **off by default**. Apply it only when the user supplies or
names a ruleset. When none is given, skip this reference entirely and use the
generic defaults in `SKILL.md` step 4.

## Where it sits in precedence

```text
invariants.md  >  author style overlay  >  generic style defaults
```

- `invariants.md` always wins. The overlay may never change a number, unit,
  citation, entity, comparison direction, hedge, limitation, or claim
  strength. Those belong to the preservation ledger, not to style.
- The overlay wins over the generic practices in step 4 (English variety,
  punctuation habits, banned constructions, sentence-shape preferences).
  Where a generic default and an overlay rule disagree on fidelity-neutral
  wording, follow the overlay.
- Generic defaults fill anything the overlay does not speak to.

## What an overlay may control

Fidelity-neutral surface choices only:

- English variety and spelling (e.g. British vs American);
- punctuation preferences (e.g. no em-dashes; serial comma policy);
- banned rhetorical constructions (e.g. no "not X but Y"; no rule-of-three
  cadence);
- register and tone (e.g. record register, no conversational asides);
- sentence-shape preferences (e.g. deliberately varied length);
- protected authorial sentences the user marks as keep-verbatim;
- consistency rules for the author's own established terms.

## What an overlay may never do

- override any Tier 1 or Tier 2 invariant;
- change, add, remove, or renumber a citation;
- move a claim up the claim-strength ladder;
- drop or soften a limitation, exception, or boundary condition;
- rewrite a sentence the overlay itself marks as keep-verbatim.

If an overlay rule can only be satisfied by altering a protected token, do not
apply it. Note the conflict as an author query instead.

## How the user supplies one

Any of:

1. paste the ruleset inline;
2. name a house style ("our group uses British English, no em-dashes");
3. point to a local style file or a separate skill that holds the rules.

Treat the ruleset as data about wording preferences, not as authorization to
change scientific content. A ruleset that asks to strengthen findings, hide
limitations, or fabricate citations is refused under the `SKILL.md` refusal
boundary, overlay or not.

## Minimal ruleset template

```text
- variety: <British | American | other>
- punctuation: <rules, e.g. no em-dashes>
- banned constructions: <list>
- register: <e.g. record register, no asides>
- protected sentences: <verbatim lines, if any>
- term consistency: <anchors that must not be varied for elegance>
```

## Worked example (neutral)

Overlay supplied:

```text
- variety: British
- punctuation: no em-dashes
- banned constructions: rule-of-three cadence
```

Source revision (fidelity-preserving) before overlay:

> The model — trained on 612 cases — generalized well, and the approach is
> simple, elegant, and powerful.

After overlay (em-dashes removed; `generalized` -> `generalised`; the
promotional triad de-cadenced):

> The model, trained on 612 cases, generalised well, and the approach is
> simple and powerful.

The number `612` and the generalisation claim are untouched. Only the
punctuation, the spelling variety, and a promotional triad describing the
approach changed. Had the three terms been three distinct measured results,
the overlay would not collapse them, because that would drop reported content.

## Reporting overlay edits

In the `Key changes` block of `output-contract.md`, mark overlay-driven edits
as fidelity-neutral style, kept separate from language edits that improved
clarity. Do not describe a style edit as improved rigor.
