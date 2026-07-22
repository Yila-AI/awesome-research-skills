# Evaluation Method

The evaluation is frozen before Skill implementation and compares three arms under identical model conditions:

```text
Baseline A: task and materials only
Baseline B: task plus a generic academic-writing prompt
Skill: task plus science-research-writing
```

## What is measured

- critical safety errors: invented content, token drift, claim-strength movement, null-result loss, scope inflation, source conflict, and copying;
- writing quality: organization, clarity, section fitness, and evidence integration;
- novice experience: route accuracy, questions before useful work, jargon burden, and next-step clarity;
- retention: whether already-good prose remains unchanged when revision adds no value.

## Publication rules

Raw outputs, model/version/settings, run dates, per-case scores, failures, and limitations must be published before comparative claims appear in the root README. Model-judge results are labeled as such and are not described as independent human review.

See the frozen [benchmark protocol](../../benchmarks/science-research-writing/README.md) and [rubric](../../benchmarks/science-research-writing/evaluation-rubric.md).
