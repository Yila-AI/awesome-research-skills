# English-first Repository and Banner Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make the repository English-first for global users and add an original banner led by the message `1,000 HIGH-QUALITY PAPERS. ONE SCI/SSCI POLISHING SKILL.`

**Architecture:** Keep English as the canonical repository language while preserving the existing Chinese landing page as a peer translation. Store one project-local raster banner under `assets/` and reference the same asset from both language entry points. Preserve the full corpus funnel and limitations as searchable text below the marketing-led hero.

**Tech Stack:** GitHub Markdown, PNG/WebP raster asset generated with the built-in image generation tool, Python standard-library validation, existing Skill validation and unit tests.

## Global Constraints

- The banner shows `1,000` as the only corpus number.
- Use the exact headline `1,000 HIGH-QUALITY PAPERS. ONE SCI/SSCI POLISHING SKILL.`
- Use the exact supporting line `Polish the writing. Preserve the science.`
- Do not claim that 1,000 full texts were downloaded, read, used for model training, or directly distilled.
- Keep the complete `1,000 -> 200 -> 60` funnel in README text.
- Do not reproduce journal covers, publisher logos, Nature branding, or copyrighted paper text.

---

### Task 1: English-first documentation entry points

**Files:**
- Replace: `README.md`
- Create: `README_CN.md`
- Remove: `README_EN.md`

**Interfaces:**
- Consumes: the existing English and Chinese README content.
- Produces: one canonical English landing page and one complete Chinese translation with reciprocal links.

- [x] **Step 1: Preserve the current Chinese README as `README_CN.md`**

Move the complete current Chinese landing page without dropping installation, corpus, evaluation, copyright, or license sections.

- [x] **Step 2: Promote the English README to `README.md`**

Expand it to include the full content depth of the Chinese version, led by global positioning and precise corpus language.

- [x] **Step 3: Add reciprocal language links and banner reference**

Both files must link to the other language and reference `assets/sci-ssci-skills-banner.png` at the top.

- [x] **Step 4: Verify relative links**

Run a Python standard-library Markdown-link check from repository root.

Expected: every relative target in `README.md` and `README_CN.md` exists; no reference to `README_EN.md` remains.

### Task 2: Original global banner

**Files:**
- Create: `assets/sci-ssci-skills-banner.png`

**Interfaces:**
- Consumes: approved headline, support line, dark scientific editorial art direction, and factual constraints.
- Produces: a repository-local banner legible at standard GitHub README width.

- [x] **Step 1: Generate the banner with the built-in image tool**

Use a maximum 3:1 landscape composition, original navy/indigo scientific editorial design, clear left-to-right hierarchy, manuscript refinement and protected-token visual metaphors, and no third-party branding.

- [x] **Step 2: Inspect the generated asset**

Check exact text, spelling, crop safety, hierarchy, contrast, absence of watermarks, and readability at reduced width.

- [x] **Step 3: Save the selected asset in the repository**

Copy the final generated image to `assets/sci-ssci-skills-banner.png`; do not leave a README-referenced asset only in the generated-images directory.

### Task 3: Validate and publish

**Files:**
- Verify: all changed files

**Interfaces:**
- Consumes: completed English/Chinese documentation and banner.
- Produces: a tested GitHub commit available from `Yila-AI/sci-ssci-skills`.

- [x] **Step 1: Run repository checks**

Run:

```bash
python3 -m unittest discover -s tests -v
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/sci-ssci-polishing
git diff --check
```

Expected: five unit tests pass, Skill validation reports valid, and the Git diff has no whitespace errors.

- [x] **Step 2: Run corpus, privacy, and asset checks**

Verify the 1,000/200/60 row counts and split balance; scan for credentials and local paths; confirm no paper PDF/XML/JATS full text is tracked; confirm the banner exists and is a valid image.

- [x] **Step 3: Review, commit, and push**

Stage only the intended README, banner, design, and plan changes; review the staged diff; commit with a concise English-first branding message; push `main`.

- [x] **Step 4: Verify the remote landing page and installation discovery**

Run `npx skills add Yila-AI/sci-ssci-skills --list` from a clean temporary directory.

Expected: the remote repository exposes `sci-ssci-polishing` and the GitHub landing page uses the English README with the banner.
