# Development Smoke-Test Results

**Run date:** 2026-07-22  
**Agent:** OpenAI Codex CLI 0.142.4  
**Model:** `gpt-5.4`  
**Skill source:** local `feat/science-research-writing` worktree  
**Purpose:** forward-test routing and safety behavior during development

These tests are not the frozen three-arm benchmark and do not support superiority claims. They use four synthetic prompts to expose implementation failures before release.

## Cases

| Case | First-run finding | Revision | Final smoke result |
|---|---|---|---|
| Observational Discussion | Preserved numbers and null result, but invented reverse-causality examples, generic confounding, and future study designs | Forbid turning general methodological knowledge into manuscript content; forbid significance-based comparison; constrain `Next step` | Preserved `612`, `beta = 0.17`, `p = 0.01`, and `p = 0.42`; separated both findings; retained the non-causal boundary; added no citation, mechanism, confounder, or future design |
| Vague novice request | Correctly identified a materials-stage task and produced a section-function plan before asking for files | No change | Produced useful planning work, then requested the three described source files in one focused confirmation |
| Already-good Results | Initially supplied an unnecessary style alternative and added a unit inside the confidence interval | Require verbatim retention when no change is necessary | Returned the original sentence unchanged and requested only verification of the analysis direction |
| Conflicting Results sources | Initially inferred a positive association from OR > 1 and invented `Table X` | Prohibit provisional prose, inferred variable roles/direction, and invented table labels when core evidence conflicts | Returned diagnosis only, preserved both value pairs, kept `[12]` attached to background, and asked which source was authoritative |

## Final observational-Discussion output

```text
In this cross-sectional study of 612 university students, sleep regularity
was associated with GPA, with a positive association observed for regularity
(beta = 0.17, p = 0.01). This finding is consistent with the possibility
that more regular sleep patterns are relevant to academic performance in
this sample.

Sleep duration was not associated with GPA in the present analysis
(p = 0.42). This null result should be retained as part of the overall
interpretation of the findings.

Because the study was cross-sectional and observational, the findings do
not support causal inference.
```

## Limitations

- The smoke tests used one model and one run per final case.
- The agent saw only synthetic prompts; no domain expert independently scored the outputs.
- Passing these cases does not establish performance on the 12-case frozen set.
- The full three-arm evaluation remains pending and must publish raw outputs before comparative claims are made.
