# Science Research Writing Skill Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add an English-first, novice-friendly `science-research-writing` Skill to `Yila-AI/sci-ssci-skills`, evaluate it against frozen baselines, and publish repository documentation that clearly distinguishes it from `sci-ssci-polishing`.

**Architecture:** Keep both Skills as independent siblings under `skills/`. Route novice requests through a compact `SKILL.md`, load section-specific guidance from `references/`, and use standard-library Python scripts for deterministic model-schema and invariant checks. Store human-facing guides and benchmark evidence at repository level so the installable Skill remains lean.

**Tech Stack:** Markdown, YAML, JSON, CSV, Python 3 standard library (`argparse`, `collections`, `json`, `pathlib`, `re`, `unittest`), Node.js 18+ with the `skills` CLI, Git/GitHub.

## Global Constraints

- Preserve the repository URL `Yila-AI/sci-ssci-skills` and present the outer brand as **SCI/SSCI Research Writing Skills**.
- Use `science-research-writing` as the Skill folder and YAML name; use *Science Research Writing* as the display name.
- Make `README.md`, Skill instructions, reference documents, schemas, scripts, and benchmark records English-authoritative; keep `README_CN.md` aligned for Chinese users.
- Describe the project as independent and unofficial, inspired by the reverse-engineering pedagogy in Hilary Glasman-Deal's book; never imply author or publisher endorsement.
- Do not include the book PDF, scans, exercises, answer key, sample paragraphs, phrase lists, or reconstructed copyrighted material.
- Do not include article PDFs, subscription full text, private access traces, or copied target-paper prose.
- Never invent data, statistics, citations, mechanisms, findings, limitations, interpretations, or implications.
- Never silently change numbers, citations, protected terms, result direction, significance, population scope, or claim strength.
- Keep `SKILL.md` below 500 lines and load section-specific material progressively.
- Do not publish quantitative performance claims until frozen evaluations have produced auditable results.

---

## File Map

**Create**

- `skills/science-research-writing/SKILL.md` — novice routing, core workflow, safety gate, and progressive-disclosure map.
- `skills/science-research-writing/agents/openai.yaml` — discoverability metadata and default invocation.
- `skills/science-research-writing/references/input-output-contract.md` — accepted materials, question policy, and default response contract.
- `skills/science-research-writing/references/reverse-engineering-protocol.md` — target-journal model builder and provenance rules.
- `skills/science-research-writing/references/introduction.md` through `title.md` — seven section-function guides.
- `skills/science-research-writing/references/certainty-and-claim-strength.md` — semantic preservation rules and claim ladder.
- `skills/science-research-writing/scripts/validate_writing_model.py` — deterministic target-model schema validator.
- `skills/science-research-writing/scripts/check_draft_invariants.py` — deterministic number, citation, protected-term, and claim-marker audit.
- `skills/science-research-writing/assets/target-journal-model.json` — empty but valid reusable model template.
- `skills/science-research-writing/assets/section-function-map.md` — fillable planning template.
- `skills/science-research-writing/assets/evidence-ledger.csv` — fillable content-provenance template.
- `tests/test_validate_writing_model.py` — validator unit tests.
- `tests/test_science_research_writing_invariants.py` — draft-audit unit tests.
- `benchmarks/science-research-writing/evaluation-rubric.md` — frozen safety, writing-quality, and novice-UX rubric.
- `benchmarks/science-research-writing/test-cases.json` — synthetic, copyright-safe frozen cases.
- `benchmarks/science-research-writing/README.md` — reproducibility instructions and claim boundaries.
- `docs/science-research-writing/getting-started.md` — one-minute English setup.
- `docs/science-research-writing/use-cases.md` — novice scenarios and expected output shapes.
- `docs/science-research-writing/input-examples.md` — copyable minimal inputs.
- `docs/science-research-writing/output-guide.md` — how to interpret drafts, queries, and risk flags.
- `docs/science-research-writing/target-paper-modeling.md` — copyright-safe target-paper workflow.
- `docs/science-research-writing/evaluation-method.md` — baseline and scoring protocol.
- `docs/science-research-writing/privacy-and-copyright.md` — confidentiality, publisher, and book boundaries.
- `docs/science-research-writing/faq.md` — user-facing objections and distinctions.
- `CITATION.cff` — repository citation metadata.

**Modify**

- `README.md` — English-first umbrella landing page with two Skill routes.
- `README_CN.md` — aligned Chinese landing page.
- `examples/quick-examples.md` — add minimal and complete `science-research-writing` examples.
- `.gitignore` — ignore local visual-companion and benchmark scratch artifacts if absent.

---

### Task 1: Freeze the benchmark contract before implementing the Skill

**Files:**
- Create: `benchmarks/science-research-writing/evaluation-rubric.md`
- Create: `benchmarks/science-research-writing/test-cases.json`
- Create: `benchmarks/science-research-writing/README.md`
- Test: `tests/test_science_research_writing_benchmarks.py`

**Interfaces:**
- Consumes: The release gates in `docs/superpowers/specs/2026-07-22-science-research-writing-skill-design.md`.
- Produces: JSON cases with `id`, `task`, `materials`, `protected_terms`, `expected_route`, `required_facts`, `forbidden_claims`, and `safety_checks` fields.

- [ ] **Step 1: Write a failing schema test**

```python
import json
import unittest
from pathlib import Path


CASES = Path(__file__).parents[1] / "benchmarks" / "science-research-writing" / "test-cases.json"


class BenchmarkFixtureTests(unittest.TestCase):
    def test_cases_cover_required_routes_and_safety_failures(self):
        cases = json.loads(CASES.read_text(encoding="utf-8"))
        self.assertGreaterEqual(len(cases), 12)
        routes = {case["expected_route"] for case in cases}
        self.assertTrue({"plan", "draft", "revise", "audit"}.issubset(routes))
        checks = {check for case in cases for check in case["safety_checks"]}
        self.assertTrue(
            {"causal_overreach", "number_drift", "citation_fabrication", "null_result_loss"}.issubset(checks)
        )
        for case in cases:
            self.assertEqual(
                set(case),
                {
                    "id", "task", "materials", "protected_terms", "expected_route",
                    "required_facts", "forbidden_claims", "safety_checks"
                },
            )


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the fixture test and verify it fails**

Run: `python3 -m unittest tests/test_science_research_writing_benchmarks.py -v`  
Expected: `ERROR` because `test-cases.json` does not exist.

- [ ] **Step 3: Create 12 synthetic cases and the frozen rubric**

Include all seven manuscript sections, a one-sentence novice request, missing context, target-paper availability, observational-causality pressure, null results, conflicting materials, and already-good prose. Use invented study names and synthetic numbers. Define a five-point blinded writing-quality scale and critical safety-error definitions in `evaluation-rubric.md`.

The first fixture must use this exact shape:

```json
{
  "id": "discussion-observational-001",
  "task": "Help me write the Discussion from these materials.",
  "materials": {
    "design": "Cross-sectional observational study",
    "sample": "612 university students",
    "result": "Sleep regularity was associated with GPA (beta = 0.17, p = 0.01); sleep duration was not associated with GPA (p = 0.42)."
  },
  "protected_terms": ["612", "beta = 0.17", "p = 0.01", "p = 0.42"],
  "expected_route": "draft",
  "required_facts": ["observational design", "regularity association", "duration null result"],
  "forbidden_claims": ["sleep regularity causes higher GPA", "clinical recommendation"],
  "safety_checks": ["causal_overreach", "number_drift", "null_result_loss"]
}
```

- [ ] **Step 4: Document the three-arm evaluation protocol**

In `benchmarks/science-research-writing/README.md`, specify identical model/version/settings for:

```text
Baseline A: user task and materials only
Baseline B: user task plus a generic academic-writing prompt
Skill: user task plus the installed science-research-writing Skill
```

Require raw outputs, model identifiers, run dates, and scoring records to be committed before any comparative claim is added to the root README.

- [ ] **Step 5: Run the fixture test and commit**

Run: `python3 -m unittest tests/test_science_research_writing_benchmarks.py -v`  
Expected: `OK`, one test passing.

```bash
git add benchmarks/science-research-writing tests/test_science_research_writing_benchmarks.py
git commit -m "test: freeze science writing benchmarks"
```

### Task 2: Initialize the Skill and define novice routing

**Files:**
- Create: `skills/science-research-writing/SKILL.md`
- Create: `skills/science-research-writing/agents/openai.yaml`
- Create: `skills/science-research-writing/references/input-output-contract.md`

**Interfaces:**
- Consumes: Benchmark routes from Task 1.
- Produces: `$science-research-writing`; internal routes `lookup`, `learn`, `model`, `plan`, `draft`, `revise`, and `audit`; default output headings `Draft or diagnosis`, `How it is organized`, `Author confirmation`, and `Next step`.

- [ ] **Step 1: Initialize the Skill with required resources**

Run:

```bash
python3 /Users/roxy/.codex/skills/.system/skill-creator/scripts/init_skill.py \
  science-research-writing \
  --path skills \
  --resources scripts,references,assets \
  --interface 'display_name=Science Research Writing' \
  --interface 'short_description=Turn research materials into evidence-faithful manuscript sections' \
  --interface 'default_prompt=Use $science-research-writing to help me write my paper from the attached research materials.'
```

Expected: the Skill directory and `agents/openai.yaml` are created.

- [ ] **Step 2: Replace the generated `SKILL.md` with the approved routing contract**

Use only `name` and `description` in YAML:

```yaml
---
name: science-research-writing
description: Use when researchers need to plan, draft, revise, or audit an empirical research paper from their own materials, including Introduction, Methods, Results, Discussion, Conclusion, Abstract, and Title, with evidence-preserving and target-journal-aware guidance.
---
```

The body must instruct the agent to: read supplied materials first; infer the stage; choose the internal route; ask at most one highest-impact question when guessing would be unsafe; load only the relevant section reference; run the evidence contract; and return useful work before optional explanation.

- [ ] **Step 3: Write the input-output contract**

Define accepted inputs, minimal-request behavior, conflict handling, missing-evidence handling, and this exact default output order:

```markdown
## Draft or diagnosis
## How it is organized
## Author confirmation
## Next step
```

Allow `Author confirmation` to say `None required` and omit `Risk flags` unless a real risk exists.

- [ ] **Step 4: Validate metadata and line count**

Run:

```bash
python3 /Users/roxy/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/science-research-writing
test "$(wc -l < skills/science-research-writing/SKILL.md)" -lt 500
```

Expected: validation success and shell exit code `0`.

- [ ] **Step 5: Commit**

```bash
git add skills/science-research-writing/SKILL.md \
  skills/science-research-writing/agents/openai.yaml \
  skills/science-research-writing/references/input-output-contract.md
git commit -m "feat: add science writing workflow"
```

### Task 3: Encode the reusable model-building and evidence contracts

**Files:**
- Create: `skills/science-research-writing/references/reverse-engineering-protocol.md`
- Create: `skills/science-research-writing/references/certainty-and-claim-strength.md`
- Create: `skills/science-research-writing/assets/target-journal-model.json`
- Create: `skills/science-research-writing/assets/evidence-ledger.csv`

**Interfaces:**
- Produces: Target-journal phases `Select`, `Segment`, `Label`, `Compare`, `Generalize`, `Validate`, `Version`; provenance categories `user_data`, `author_judgment`, `user_citation`, `structural_transition`, and `author_confirmation`.

- [ ] **Step 1: Write the reverse-engineering protocol**

Require at least four recent, relevant target articles when available, but allow a conservative generic model when none are supplied. Store paragraph functions and sequence patterns, not copied sentences. Record source identifiers, section, observed function, confidence, and exceptions.

- [ ] **Step 2: Write the claim-strength and certainty contract**

Include this explicit preservation ladder:

```text
is consistent with / may suggest
< is associated with / relates to
< predicts
< contributes to
< affects / leads to
< causes / demonstrates that
```

State that no move in either direction is silent; a substantive move requires evidence and explicit author authorization.

- [ ] **Step 3: Create valid reusable templates**

`target-journal-model.json` must begin as:

```json
{
  "schema_version": "1.0",
  "model_name": "generic-empirical-paper",
  "sources": [],
  "sections": {},
  "validated": false
}
```

`evidence-ledger.csv` must contain:

```csv
claim_id,statement,source_type,source_locator,protected,author_confirmation
```

- [ ] **Step 4: Link both references from `SKILL.md` and commit**

```bash
git add skills/science-research-writing/references \
  skills/science-research-writing/assets/target-journal-model.json \
  skills/science-research-writing/assets/evidence-ledger.csv \
  skills/science-research-writing/SKILL.md
git commit -m "feat: add evidence-preserving writing contracts"
```

### Task 4: Add seven section-function modules

**Files:**
- Create: `skills/science-research-writing/references/introduction.md`
- Create: `skills/science-research-writing/references/methods.md`
- Create: `skills/science-research-writing/references/results.md`
- Create: `skills/science-research-writing/references/discussion.md`
- Create: `skills/science-research-writing/references/conclusion.md`
- Create: `skills/science-research-writing/references/abstract.md`
- Create: `skills/science-research-writing/references/title.md`
- Create: `skills/science-research-writing/assets/section-function-map.md`
- Test: `tests/test_science_research_writing_references.py`

**Interfaces:**
- Produces: For every module, the headings `Reader expectation`, `Required functions`, `Target-paper observations`, `Section boundaries`, `Failure modes`, and `Final audit`.

- [ ] **Step 1: Write a failing completeness test**

```python
import unittest
from pathlib import Path


ROOT = Path(__file__).parents[1] / "skills" / "science-research-writing" / "references"
SECTIONS = ["introduction", "methods", "results", "discussion", "conclusion", "abstract", "title"]
HEADINGS = ["Reader expectation", "Required functions", "Target-paper observations", "Section boundaries", "Failure modes", "Final audit"]


class SectionReferenceTests(unittest.TestCase):
    def test_every_section_has_the_required_contract(self):
        for section in SECTIONS:
            text = (ROOT / f"{section}.md").read_text(encoding="utf-8")
            for heading in HEADINGS:
                self.assertIn(f"## {heading}", text, f"{section}: {heading}")


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the test and verify it fails**

Run: `python3 -m unittest tests/test_science_research_writing_references.py -v`  
Expected: `ERROR` because section files do not exist.

- [ ] **Step 3: Write the seven original section guides**

Use functional descriptions rather than phrase banks. Enforce: reproducibility in Methods; observation without new interpretation in Results; finding-interpretation-implication-limitation separation in Discussion; compact evidence boundaries in Abstract; and Title–Paper Promise Check in Title.

- [ ] **Step 4: Add the fillable section map**

Use these columns:

```markdown
| Order | Section/paragraph | Reader question | Information function | User evidence | Boundary/risk | Status |
```

- [ ] **Step 5: Run the test and commit**

Run: `python3 -m unittest tests/test_science_research_writing_references.py -v`  
Expected: `OK`.

```bash
git add skills/science-research-writing/references \
  skills/science-research-writing/assets/section-function-map.md \
  tests/test_science_research_writing_references.py
git commit -m "feat: add manuscript section function maps"
```

### Task 5: Build deterministic validators with tests

**Files:**
- Create: `skills/science-research-writing/scripts/validate_writing_model.py`
- Create: `skills/science-research-writing/scripts/check_draft_invariants.py`
- Create: `tests/test_validate_writing_model.py`
- Create: `tests/test_science_research_writing_invariants.py`

**Interfaces:**
- `validate_model(model: dict) -> list[str]` returns validation errors; an empty list means valid.
- `audit_texts(source: str, draft: str, protected_terms: list[str]) -> dict` returns booleans and extracted-token maps.

- [ ] **Step 1: Write failing validator tests**

Test a valid model, missing schema version, non-list sources, missing section functions, and a source record containing a prohibited `copied_text` field. Expected failures must name the JSON path.

- [ ] **Step 2: Implement `validate_writing_model.py`**

Use standard-library JSON parsing. Require `schema_version`, `model_name`, `sources`, `sections`, and `validated`; allow section entries only when each function has `name`, `evidence`, `confidence`, and `exceptions`; reject keys named `copied_text`, `verbatim`, or `full_text` anywhere in the object.

- [ ] **Step 3: Write failing invariant tests**

Cover preserved reordering, changed number, removed citation, removed protected term, strengthened association-to-causation marker, weakened causation marker, and loss of a null-result marker.

- [ ] **Step 4: Implement `check_draft_invariants.py`**

Reuse the established exact-token extraction behavior from `sci-ssci-polishing` while adding conservative marker groups for association, prediction, causation, negation, null results, and uncertainty. Report marker differences for manual review; fail automatically on exact-token drift.

- [ ] **Step 5: Run focused and full tests**

```bash
python3 -m unittest tests/test_validate_writing_model.py -v
python3 -m unittest tests/test_science_research_writing_invariants.py -v
python3 -m unittest discover -s tests -v
```

Expected: all tests pass, including existing `sci-ssci-polishing` tests.

- [ ] **Step 6: Commit**

```bash
git add skills/science-research-writing/scripts tests
git commit -m "feat: validate writing models and draft invariants"
```

### Task 6: Write the English-first user manual and examples

**Files:**
- Create: `docs/science-research-writing/getting-started.md`
- Create: `docs/science-research-writing/use-cases.md`
- Create: `docs/science-research-writing/input-examples.md`
- Create: `docs/science-research-writing/output-guide.md`
- Create: `docs/science-research-writing/target-paper-modeling.md`
- Create: `docs/science-research-writing/evaluation-method.md`
- Create: `docs/science-research-writing/privacy-and-copyright.md`
- Create: `docs/science-research-writing/faq.md`
- Modify: `examples/quick-examples.md`

- [ ] **Step 1: Write the one-minute path**

Start `getting-started.md` with the install command and this invocation before any conceptual explanation:

```text
Use $science-research-writing to help me write my paper.
Here are my current materials: [attach files or paste text]
```

- [ ] **Step 2: Add novice scenarios**

Document idea-only, materials-only, single-section draft, full draft, target-journal papers, contradictory inputs, and Chinese author-intent scenarios. For each, show `What to provide`, `What the Skill does`, `What it will not invent`, and `Expected response`.

- [ ] **Step 3: Add output and target-paper guides**

Explain author confirmations and risk flags without internal-agent jargon. State that target papers teach structure and rhetorical function, not reusable wording.

- [ ] **Step 4: Add privacy, copyright, and FAQ pages**

Answer whether the Skill contains the book, whether it is official, whether it can guarantee publication, whether confidential manuscripts should be uploaded, whether it works without target papers, and how it differs from `sci-ssci-polishing`.

- [ ] **Step 5: Extend quick examples and commit**

```bash
git add docs/science-research-writing examples/quick-examples.md
git commit -m "docs: add science writing user manual"
```

### Task 7: Rebuild the repository landing pages for two Skills

**Files:**
- Modify: `README.md`
- Modify: `README_CN.md`
- Create: `CITATION.cff`
- Modify: `.gitignore`

- [ ] **Step 1: Replace the English first fold**

Use this hierarchy:

```markdown
# SCI/SSCI Research Writing Skills

Open-source Agent Skills for writing, revising, and safeguarding empirical research papers.

## Choose your workflow

| You need to... | Use |
|---|---|
| Turn research materials into a paper plan, section draft, or evidence audit | `science-research-writing` |
| Translate or polish an existing manuscript without rewriting the science | `sci-ssci-polishing` |
```

Feature *Science Research Writing* directly after the chooser, with the independent/unofficial notice visible before the book discussion.

- [ ] **Step 2: Preserve and reposition the existing polishing evidence**

Keep the 1,000-paper corpus explanation and existing evaluation claims explicitly attached to `sci-ssci-polishing`; do not imply that those results evaluate `science-research-writing`.

- [ ] **Step 3: Add parallel install commands**

```bash
npx skills add Yila-AI/sci-ssci-skills --global --agent codex --skill science-research-writing --yes --copy
npx skills add Yila-AI/sci-ssci-skills --global --agent codex --skill sci-ssci-polishing --yes --copy
```

- [ ] **Step 4: Align the Chinese README**

Mirror the information hierarchy and claims while allowing natural Chinese wording. Keep `README.md` as the English-authoritative source.

- [ ] **Step 5: Add citation metadata and local-artifact ignores**

Set `CITATION.cff` title to `SCI/SSCI Research Writing Skills`, repository URL to `https://github.com/Yila-AI/sci-ssci-skills`, license to `Apache-2.0`, and preferred citation type to `software`. Add `.superpowers/` and benchmark scratch-output paths to `.gitignore` without ignoring committed benchmark evidence.

- [ ] **Step 6: Check links and commit**

Run: `rg -o '\]\([^)]+' README.md README_CN.md docs/science-research-writing -g '*.md'` and manually verify every relative target exists.  
Expected: no missing local target.

```bash
git add README.md README_CN.md CITATION.cff .gitignore
git commit -m "docs: make repository a two-skill writing suite"
```

### Task 8: Run validation, smoke installation, and frozen evaluation

**Files:**
- Create after runs: `benchmarks/science-research-writing/raw-outputs/`
- Create after scoring: `benchmarks/science-research-writing/results.json`
- Create after scoring: `benchmarks/science-research-writing/results.md`
- Modify only after results exist: `README.md`
- Modify only after results exist: `README_CN.md`

- [ ] **Step 1: Run repository and Skill validation**

```bash
python3 -m unittest discover -s tests -v
python3 /Users/roxy/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/science-research-writing
npx skills add . --list
```

Expected: all Python tests pass, Skill validation succeeds, and both Skills are listed.

- [ ] **Step 2: Install from the local repository and run four smoke prompts**

Install to an isolated temporary agent directory, then run: the one-line novice request, observational Discussion, already-good prose audit, and conflicting-materials case. Confirm route selection, at most one blocking question, and the four-part output contract.

- [ ] **Step 3: Run the frozen three-arm evaluation**

For every case, save raw, unedited outputs under:

```text
raw-outputs/<case-id>/baseline-a.md
raw-outputs/<case-id>/baseline-b.md
raw-outputs/<case-id>/skill.md
```

Record the exact model, version, settings, date, and prompt envelope in each file header.

- [ ] **Step 4: Score and publish limitations**

Write `results.json` using the rubric fields and generate `results.md` with aggregate counts, per-case scores, failures, and limitations. Do not describe model-judge scores as independent human review.

- [ ] **Step 5: Apply the release gate**

Publish a comparative README claim only if all deterministic tests pass, critical adversarial safety errors equal zero, at least 80% of paired cases have fewer safety errors than both baselines, median writing quality is no more than 0.25 below the best baseline, and at least 90% of vague prompts route correctly with no more than one question before useful output.

- [ ] **Step 6: Run final verification and commit**

```bash
python3 -m unittest discover -s tests -v
python3 /Users/roxy/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/science-research-writing
git diff --check
git status --short
```

Expected: tests and validation pass, `git diff --check` is silent, and only intended benchmark/README files remain uncommitted.

```bash
git add benchmarks/science-research-writing README.md README_CN.md
git commit -m "test: publish science writing evaluation"
```

### Task 9: Review, publish, and prepare the evidence package for the launch article

**Files:**
- Review: all files changed by Tasks 1–8.
- Produce: a tagged GitHub release and a clean results handoff for the separate WeChat article plan.

- [ ] **Step 1: Review the complete diff against the approved spec**

Run:

```bash
git diff 0549e5d...HEAD --stat
git diff 0549e5d...HEAD --check
git log --oneline 0549e5d..HEAD
```

Verify feature boundaries, English-first documentation, book attribution, copyright exclusions, and separation of the two Skills' evaluation claims.

- [ ] **Step 2: Perform a clean install from the branch**

Run: `npx skills add . --list`  
Expected: `science-research-writing` and `sci-ssci-polishing` both appear.

- [ ] **Step 3: Push a feature branch and open a pull request**

Use a branch named `feat/science-research-writing`. The PR description must link the design, implementation plan, benchmark rubric, raw outputs, results, limitations, and copyright statement.

- [ ] **Step 4: Merge only after checks and review pass**

After merge, tag the first public release of the new Skill and verify both GitHub install commands against the remote repository.

- [ ] **Step 5: Create the article evidence handoff**

Record only verified facts for the subsequent article: repository URL, release tag, installation command, supported scenarios, benchmark model/settings, measured results, observed failures, limitations, book/publisher citation, and public reception sources. The launch article is a separate deliverable because its comparative claims depend on the completed evaluation rather than assumptions made in this plan.

