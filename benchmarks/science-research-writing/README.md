# Science Research Writing Benchmarks

This directory evaluates whether `science-research-writing` improves evidence safety and novice usability without degrading academic writing quality.

## Frozen three-arm protocol

Use the same model, model version, settings, input materials, and run date for every arm.

```text
Baseline A: user task and materials only
Baseline B: user task plus a generic academic-writing prompt
Skill: user task plus the installed science-research-writing Skill
```

Save raw, unedited outputs as:

```text
raw-outputs/<case-id>/baseline-a.md
raw-outputs/<case-id>/baseline-b.md
raw-outputs/<case-id>/skill.md
```

Every output file must record the model identifier, model version, settings, date, prompt envelope, and arm. Score with `evaluation-rubric.md` without revealing arm labels to the reviewer.

## Claim boundaries

The fixtures are synthetic and test controlled failure modes. They do not demonstrate journal acceptance, disciplinary universality, superiority to domain experts, or independent human preference. Publish raw outputs, per-case scores, failures, and limitations before adding comparative claims to the repository landing page.
