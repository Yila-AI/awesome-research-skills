# Lean Skill Release Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Provide a verified, use-only ZIP distribution for `sci-ssci-polishing` without changing the Skill or removing the repository's research artifacts.

**Architecture:** A small Python builder copies the complete runtime Skill directory, a lean README, and the repository license into one versioned ZIP. Unit tests inspect the archive contract, while a tag-triggered GitHub Actions workflow runs the full test suite, builds the archive, and attaches it to a GitHub Release.

**Tech Stack:** Python 3 standard library, `unittest`, GitHub Actions, GitHub CLI.

## Global Constraints

- Do not modify the behavior or contents of `skills/sci-ssci-polishing/`.
- Keep `corpus/`, `benchmarks/`, `docs/`, and `assets/` in the main repository.
- The lean archive must contain the full runtime Skill, `LICENSE`, and a short user README, and must exclude research-only directories.
- The existing `npx skills add ... --skill sci-ssci-polishing --copy` command remains the recommended installation path.

---

### Task 1: Define and implement the lean archive contract

**Files:**
- Create: `tests/test_build_lean_release.py`
- Create: `scripts/build_lean_release.py`
- Create: `distribution/sci-ssci-polishing/README.md`

**Interfaces:**
- Consumes: repository root, output directory, and release version.
- Produces: `build_release(repo_root: Path, output_dir: Path, version: str) -> Path` and a ZIP rooted at `sci-ssci-polishing/`.

- [ ] Write tests that require every tracked runtime Skill file, the license, and lean README while rejecting research-only paths.
- [ ] Run the new test and confirm it fails because the builder does not exist.
- [ ] Implement the minimal standard-library builder and lean README.
- [ ] Run the new test and the complete suite.

### Task 2: Automate tagged releases

**Files:**
- Create: `.github/workflows/release-lean-skill.yml`

**Interfaces:**
- Consumes: tags matching `sci-ssci-polishing-v*`.
- Produces: a GitHub Release containing the versioned Lean ZIP.

- [ ] Add a workflow that checks out the tag, runs all unit tests, builds the archive, verifies it, and creates the release with GitHub CLI.
- [ ] Validate workflow syntax and inspect the generated archive locally.

### Task 3: Explain the two distribution paths

**Files:**
- Modify: `README.md`
- Modify: `README_CN.md`

**Interfaces:**
- Consumes: existing install instructions and GitHub Releases page.
- Produces: clear direct-use guidance for English and Chinese readers.

- [ ] Add a prominent use-only subsection explaining selective installation and the Lean Release.
- [ ] State that users should not load the complete repository into an Agent merely to run one Skill.
- [ ] Verify all new local and external links.

### Task 4: Publish and respond to Issue #2

**Files:**
- No repository files beyond Tasks 1–3.

**Interfaces:**
- Consumes: merged implementation and published Release URL.
- Produces: a GitHub PR, release asset, and an English response on Issue #2.

- [ ] Commit the scoped changes, push the feature branch, and open a PR.
- [ ] Merge through the protected `main` workflow after fresh verification.
- [ ] Push the first lean-distribution tag and verify the Release asset is downloadable.
- [ ] Reply to Issue #2 with the implemented paths and keep or close the issue based on delivery status.
