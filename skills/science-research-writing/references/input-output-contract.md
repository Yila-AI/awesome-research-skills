# Input and output contract

## Accepted inputs

Accept any combination of:

- a research question, hypothesis, or intended contribution;
- study design, participants, materials, procedures, measures, and analysis notes;
- results, tables, figures, statistical output, or structured findings;
- an outline, paragraph, section, abstract, title, or complete manuscript;
- author intent written in English or another language;
- target-journal instructions or relevant target papers;
- protected terminology, preferred English variety, and word limits.

Do not require a complete intake form. Begin with the material available.

## Minimal request behavior

For a request such as `Help me write my paper` with attached files:

1. inventory the files and extract the supported study facts;
2. identify the current manuscript stage;
3. state what can be produced safely now;
4. produce the first useful plan, draft, or diagnosis;
5. ask no more than one question if the next substantive step is blocked.

Do not expose internal mode names unless the user asks how the Skill works.

## Missing evidence

Use explicit neutral markers such as `[author to provide analysis method]` only when a visible gap is more useful than omission. Never turn a marker into invented prose. If the missing information does not block safe work, proceed and place it under `Author confirmation`.

## Conflicting evidence

When tables, figures, prose, notes, or user instructions disagree:

- quote or identify both conflicting values or statements;
- explain which output is blocked by the conflict;
- do not choose a source silently;
- ask which source is authoritative;
- continue with unaffected content.

When no content is unaffected, provide no provisional manuscript sentence. Do not insert alternatives such as `[A or B]` into prose, infer what an odds ratio means without variable definitions and reference coding, invent `Table X`, or create placeholders for unsupplied statistics.

## Target-paper inputs

Use target papers to observe section functions, information order, conventional boundaries, and variation across papers. Do not store, reproduce, or imitate sentences. Do not treat a target paper's methods, claims, citations, or findings as the author's content.

## Default response

```markdown
## Draft or diagnosis

[The manuscript-ready text, section plan, or prioritized diagnosis.]

## How it is organized

[A short explanation of the information-function sequence.]

## Author confirmation

[One decision or missing fact, or `None required`.]

## Next step

[One highest-priority action.]
```

Add this section only when necessary:

```markdown
## Risk flags

- [Specific evidence, claim, citation, privacy, or section-boundary risk.]
```

## Output rules

- Put useful work before process explanation.
- Preserve good existing prose instead of forcing cosmetic rewrites.
- When no change is necessary, reproduce the original text unchanged and do not append an optional revised version.
- Distinguish author-provided content from structural suggestions.
- Keep author questions specific and answerable.
- Do not claim journal acceptance, universal disciplinary fit, or factual verification that was not performed.
- Make `Next step` request the single missing evidence item or author decision with the greatest effect on the manuscript; do not offer generic expansion or cosmetic rewriting.
- Never begin `Next step` with `If you want, I can`. State one evidence action. For a Discussion with no supplied literature, mechanism, or documented limitations beyond design, use: `Provide the prior studies or author-supported interpretation you want compared with these results.`
- When no revision is necessary, make `Next step` an author verification action, not a new style suggestion.
