# README Cover Visual Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produce one approved-direction README hero preview before modifying the repository homepage.

**Architecture:** Generate a single original raster hero using the built-in image-generation path, inspect it for composition and text accuracy, and present it for user approval. Repository integration is deliberately deferred until the user accepts the visual direction.

**Tech Stack:** Built-in image generation, local image inspection, PNG asset.

## Global Constraints

- Use the approved Research Writing Workbench direction.
- Do not copy the book cover or third-party visual identity.
- Do not modify README files during the preview task.
- Save any accepted project-bound asset under `assets/` only after approval.

---

### Task 1: Generate and review the banner preview

**Files:**
- Preview only: generated image under the built-in image-generation output directory
- Do not modify: `README.md`
- Do not modify: `README_CN.md`

**Interfaces:**
- Consumes: the approved visual design in `docs/superpowers/specs/2026-07-22-readme-cover-visual-design.md`
- Produces: one landscape PNG preview for user approval

- [ ] **Step 1: Generate one wide editorial banner**

Use the built-in image-generation tool with the exact project title, tagline, palette, composition, and avoid list in the design specification.

- [ ] **Step 2: Inspect the generated image**

Confirm that the title and tagline are spelled correctly, the image reads as scholarly writing rather than generic AI, and no prohibited third-party marks or copied artwork appear.

- [ ] **Step 3: Present the preview**

Render the PNG inline and ask the user whether to keep the direction, revise one visual element, or reject it before any README integration.
