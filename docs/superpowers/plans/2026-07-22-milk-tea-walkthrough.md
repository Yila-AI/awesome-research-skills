# Bilingual Milk-Tea Walkthrough Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add separate English and Chinese end-to-end examples that show beginners how to use `science-research-writing` from an everyday question through a bounded paper plan.

**Architecture:** Create two standalone Markdown walkthroughs with parallel facts and stages. Add lightweight links from the English README, Chinese README, and quick examples without duplicating the walkthrough content.

**Tech Stack:** GitHub-Flavored Markdown, relative repository links, Python repository tests.

## Global Constraints

- Treat the milk-tea study as synthetic educational material, not a real study, benchmark, or measured Skill evaluation.
- Keep the fixed scenario facts identical across English and Chinese pages.
- Label response excerpts as illustrative outputs, not guaranteed or expected outputs.
- Do not invent missing method details, mechanisms, citations, or statistical results.
- Keep prompts copyable and explanations readable for beginners.

---

### Task 1: Create the English walkthrough

**Files:**
- Create: `examples/science-research-writing-walkthrough.md`

**Interfaces:**
- Consumes: `science-research-writing` input/output contract and the fixed synthetic scenario.
- Produces: the canonical international walkthrough linked by Task 3.

- [ ] **Step 1: Introduce the synthetic scenario and workflow map**

State the educational boundary and show curiosity -> question -> methods -> results -> discussion -> paper map.

- [ ] **Step 2: Add five progressive usage stages**

Include copyable prompts and concise illustrative outputs for research-question clarification, method-note organization, Results/Discussion separation, claim/title checks, and full-paper mapping.

- [ ] **Step 3: Add the reusable user template**

End with a generic prompt containing research question, available materials, requested section, intended meaning, protected facts, and missing-evidence handling.

- [ ] **Step 4: Validate required English facts**

Check for `120`, `30%`, `50%`, `70%`, `8.4`, `6.1`, all three tea bases, the synthetic disclaimer, and the seven manuscript sections.

### Task 2: Create the Chinese walkthrough

**Files:**
- Create: `examples/science-research-writing-walkthrough_CN.md`

**Interfaces:**
- Consumes: the facts, stage order, and safeguards from Task 1.
- Produces: a natural Chinese beginner walkthrough with cross-language parity.

- [ ] **Step 1: Write the Chinese scenario and five stages**

Use natural Chinese explanations and copyable Chinese prompts while preserving all fixed facts and boundaries.

- [ ] **Step 2: Add the Chinese reusable template**

Make the final template usable without requiring readers to understand internal Skill modes.

- [ ] **Step 3: Validate Chinese parity**

Check the same numeric markers, tea bases, seven sections, synthetic disclaimer, and five stages.

### Task 3: Integrate and verify

**Files:**
- Modify: `README.md`
- Modify: `README_CN.md`
- Modify: `examples/quick-examples.md`
- Verify: both walkthrough pages and repository tests

**Interfaces:**
- Consumes: both walkthrough paths from Tasks 1 and 2.
- Produces: discoverable links from the repository's three existing entry points.

- [ ] **Step 1: Add navigation links**

Link both walkthroughs after the README milk-tea example. Link the English walkthrough and Chinese companion near the top of quick examples.

- [ ] **Step 2: Verify relative links and parity markers**

Extract local Markdown links and assert that every target exists. Assert that both walkthroughs contain the fixed numeric markers and five stage headings.

- [ ] **Step 3: Scan example boundaries**

Confirm both pages explicitly say synthetic and illustrative, and do not present the scenario as a real study, benchmark result, or guarantee.

- [ ] **Step 4: Run repository checks**

Run `git diff --check` and `python3 -m unittest discover -s tests -v`. Expect no whitespace errors and all tests to pass.

- [ ] **Step 5: Review and commit**

Review the complete diff, stage only the two walkthroughs, three link integrations, and this plan, then commit with a concise documentation message.

