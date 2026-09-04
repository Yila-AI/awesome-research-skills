# Research Presentation — Lean Distribution

This is the use-only distribution of [`research-presentation`](https://github.com/Yila-AI/awesome-research-skills/tree/main/skills/research-presentation), also presented publicly as **Paper to Slides**. It contains the complete runtime Skill, narrative and layout references, rendering and audit helpers, and the applicable license notices. Showcase images and source-case documentation remain in the full repository.

## Install

Move the extracted `research-presentation` directory into the Skills directory used by your Agent, then invoke:

```text
$research-presentation
```

If your Agent supports the Skills CLI, install only this Skill directly:

```bash
npx skills add Yila-AI/awesome-research-skills --global --agent codex --skill research-presentation --yes --copy
```

## Runtime notes

The core instructions work with a host that can create presentations. The bundled optional helpers require:

- Python 3.10 or later and `python-pptx` for `scripts/audit_pptx.py`;
- LibreOffice and Poppler for `scripts/render_slides.py`.

If these dependencies are unavailable, the Skill requires the host's native presentation and rendering tools and must report which QA steps could not be run.

## What is included

- `SKILL.md`: evidence-first paper-to-slides workflow and output contract;
- `references/`: extraction, narrative, layout, theme, rendering, and QA guidance;
- `scripts/`: rendering and structural-audit helpers;
- `agents/openai.yaml`: Agent interface metadata;
- `NOTICE` and `LICENSE`: third-party notices and Apache License 2.0.

For showcases, source-paper links, copyright boundaries, and citation information, see the [full repository](https://github.com/Yila-AI/awesome-research-skills).
