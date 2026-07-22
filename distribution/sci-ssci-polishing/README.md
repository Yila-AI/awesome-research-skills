# SCI/SSCI Academic Polishing — Lean Distribution

This is the use-only distribution of [`sci-ssci-polishing`](https://github.com/Yila-AI/sci-ssci-skills/tree/main/skills/sci-ssci-polishing). It contains the complete runtime Skill, its references and invariant checker, and the repository license. The corpus, benchmarks, provenance documents, and promotional assets remain in the full research repository.

## Install

Move the extracted `sci-ssci-polishing` directory into the Skills directory used by your Agent, then invoke:

```text
$sci-ssci-polishing
```

If your Agent supports the Skills CLI, installing the selected Skill directly from the repository remains the simplest option:

```bash
npx skills add Yila-AI/sci-ssci-skills --global --agent codex --skill sci-ssci-polishing --yes --copy
```

That command installs only the selected Skill; it does not place the complete research repository in the Agent's Skills directory.

## What is included

- `SKILL.md`: workflow and safety boundaries;
- `references/`: preservation, output, routing, and corpus-method guidance;
- `scripts/check_invariants.py`: deterministic checks for numbers, citations, and protected terms;
- `agents/openai.yaml`: Agent metadata;
- `LICENSE`: Apache License 2.0.

For corpus construction, benchmarks, public metadata, examples, and citation information, see the [full repository](https://github.com/Yila-AI/sci-ssci-skills).
