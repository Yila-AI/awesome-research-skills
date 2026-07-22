# Model Target Papers Without Copying Them

Target papers are useful because research writing conventions vary by field, journal, article type, and section. They should teach the Agent what a paragraph does, not give it sentences to imitate.

## Workflow

```text
Select -> Segment -> Label functions -> Compare -> Generalize -> Validate -> Version
```

1. Select preferably four or more recent, relevant empirical papers.
2. Segment by section and paragraph without storing paragraph text in the model.
3. Label each segment's reader question and information function.
4. Compare order, optionality, evidence placement, and exceptions.
5. Generalize only recurring patterns; keep alternatives visible.
6. Validate against a held-out paper or the supplied set.
7. Version the model with sources, date, confidence, and scope.

## Safe observation

Safe observations include: `Discussion paragraphs commonly begin with the study finding before comparing prior work` or `Methods usually identify the setting before eligibility criteria`.

Unsafe transfer includes: copied sentences, paraphrased target claims, target citations, target mechanisms, target data, or a journal tendency presented as a mandatory rule.

The machine-readable implementation is the [Target-Journal Model Builder](../../skills/science-research-writing/references/reverse-engineering-protocol.md).
