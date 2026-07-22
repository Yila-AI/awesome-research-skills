# README Positioning Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rewrite the English and Chinese repository READMEs so first-time visitors understand the two-Skill workflow, its book-inspired writing method, its corpus-informed polishing method, and its evidence-preserving boundaries.

**Architecture:** Keep the existing hero asset and repository files. Reorder and rewrite only `README.md` and `README_CN.md`, using parallel information architecture and exact cross-language parity for numbers, workflow choices, evaluation claims, and legal boundaries.

**Tech Stack:** GitHub-Flavored Markdown, Mermaid, relative repository links, Python test suite.

## Global Constraints

- Describe `science-research-writing` as independently inspired by the book's general pedagogy, without implying affiliation, endorsement, reproduction, or an official digital edition.
- Describe the corpus as a 1,000-paper metadata candidate pool screened to a 60-paper core portfolio, with aggregate observations from the 40-paper distillation split.
- Never claim that 1,000 full texts were downloaded, read, distilled, or used to train a model.
- Keep evaluation claims Skill-specific.
- Do not promise a good paper, publication, journal acceptance, or scientific correctness.
- Retain copyright, data, affiliation, license, and professional-review boundaries.

---

### Task 1: Rewrite the English README

**Files:**
- Modify: `README.md`

**Interfaces:**
- Consumes: existing hero image, Skill files, docs, benchmarks, corpus documentation, and `CITATION.cff`.
- Produces: the canonical English repository narrative mirrored by Task 2.

- [ ] **Step 1: Replace the first screen**

Keep the hero and add the approved headline, plain-language supporting copy, language/quick-start/install/reuse navigation, and the two-foundation repository story.

- [ ] **Step 2: Add the workflow chooser and one-sentence start**

Show current user materials, recommended Skill, and expected output. Keep both exact install commands.

- [ ] **Step 3: Explain the book-inspired method**

Add a section-function table, the independent/unofficial relationship, and the book/copyright boundaries.

- [ ] **Step 4: Add the claim-boundary example and corpus story**

Use the 120-student milk-tea example to distinguish scoped evidence from a universal claim. State the exact 1,000-to-200-to-60-to-40/10/10 corpus pipeline and aggregate paragraph/word counts.

- [ ] **Step 5: Promote reusable mechanisms and retain evaluations**

Feature the Evidence-Preserving Draft Contract, Claim-Strength Contract, and Target-Journal Model Builder first; retain secondary components, credit snippet, evaluations, boundaries, citation, and license.

- [ ] **Step 6: Validate the English README**

Run:

```bash
python3 - <<'PY'
from pathlib import Path
p = Path('README.md')
t = p.read_text()
required = [
    'science-research-writing', 'sci-ssci-polishing',
    '1,000-paper metadata candidate pool', '60-paper core portfolio',
    'Evidence-Preserving Draft Contract', 'Claim-Strength Contract',
    'Target-Journal Model Builder', 'CITATION.cff'
]
missing = [item for item in required if item not in t]
assert not missing, missing
print('English README required-content check: PASS')
PY
```

Expected: `English README required-content check: PASS`.

### Task 2: Rewrite the Chinese README with information parity

**Files:**
- Modify: `README_CN.md`

**Interfaces:**
- Consumes: the finalized section order and claims from Task 1.
- Produces: a natural Chinese README with the same facts, choices, links, and boundaries.

- [ ] **Step 1: Mirror the first screen and workflow**

Use the approved Chinese headline and shorthand: classic writing methods explain how to build the paper; the curated SCI/SSCI corpus informs how to express it.

- [ ] **Step 2: Mirror the method, example, corpus, and reuse sections**

Write idiomatic Chinese rather than sentence-by-sentence translation while preserving every number and qualification.

- [ ] **Step 3: Mirror evaluations and boundaries**

Keep Skill-specific evaluation wording and the same copyright, affiliation, and professional-review limitations.

- [ ] **Step 4: Validate parity markers**

Run:

```bash
python3 - <<'PY'
from pathlib import Path
for name in ('README.md', 'README_CN.md'):
    text = Path(name).read_text()
    for marker in ('science-research-writing', 'sci-ssci-polishing', '1,000', '60', '40', '10', 'CITATION.cff'):
        assert marker in text, (name, marker)
print('README parity-marker check: PASS')
PY
```

Expected: `README parity-marker check: PASS`.

### Task 3: Verify links, wording, and repository tests

**Files:**
- Verify: `README.md`
- Verify: `README_CN.md`
- Verify: repository test suite

**Interfaces:**
- Consumes: completed READMEs from Tasks 1 and 2.
- Produces: evidence that links resolve, prohibited claims are absent, Markdown is clean, and tests remain green.

- [ ] **Step 1: Check relative links**

Extract Markdown links with relative targets and assert that each target exists in the repository.

- [ ] **Step 2: Scan prohibited overclaims**

Search for wording that claims 1,000 full texts were distilled or that the project guarantees publication, journal acceptance, or scientific correctness. Manually review any matches in context.

- [ ] **Step 3: Check Markdown whitespace**

Run `git diff --check` and expect no output with exit code 0.

- [ ] **Step 4: Run the full test suite**

Run `python3 -m unittest discover -s tests -v` and expect all tests to pass.

- [ ] **Step 5: Review the final diff and commit**

Run `git diff -- README.md README_CN.md`, verify only approved README positioning changes are present, then commit the two README files and this plan with a concise documentation message.

