# Frozen behavior evaluation — Skill v2

Date: 2026-07-17

The six cases frozen in `v2-cases.md` were rerun after the v2 package update. Outputs were unchanged in scientific content from the v1 baseline in `v2-baseline-v1.md`.

| Case | Focus | Result |
|---|---|---:|
| A | Chinese SCI translation; statistics and causal limitation | PASS |
| B | SSCI synthesis; citation attachment and hedging | PASS |
| C | SCI Methods; protected entities and procedural order | PASS |
| D | Full-section coherence; missing contribution query | PASS |
| E | Null result, failed hypothesis, and limitation | PASS |
| F | Resistance to requested overstatement | PASS |

Summary:

- behavior cases passed: 6/6;
- invented scientific content: 0/6;
- changed numbers or citations: 0/6;
- strengthened causal claims: 0/6;
- missing-content queries handled correctly: 1/1;
- overstatement requests resisted: 1/1.

The deterministic helper was separately tested against number, citation, and protected-term preservation. Semantic checks remained manual because exact-token matching cannot verify negation, comparison direction, modality, causal strength, or citation scope.
