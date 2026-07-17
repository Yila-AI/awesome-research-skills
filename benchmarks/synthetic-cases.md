# Frozen v2 behavior cases

Freeze these cases before editing Skill v2. Score the existing v1 Skill first, then the revised Skill with the same inputs.

## Case A — Chinese SCI Results

Task: Translate and polish as an SCI Results paragraph.

> 在调整年龄、性别和BMI后，模型A与较低的再入院风险相关（HR = 0.73，95% CI: 0.58–0.92，p = 0.008）。由于该研究为观察性研究，这一结果不能证明模型A降低了再入院风险。

Checks: preserve every covariate and statistic; preserve association; retain the observational-design causal limitation.

## Case B — SSCI theory synthesis

Task: Polish as the end of an SSCI literature-review paragraph.

> Prior work links perceived transparency to trust (Li, 2021). Other studies, however, report that transparency can increase uncertainty when users cannot interpret the information provided (Ahmed & Ross, 2022). These findings may indicate that interpretability conditions the relationship, but the available studies do not test this mechanism directly.

Checks: keep each citation attached to its proposition; retain disagreement; preserve `may` and the untested-mechanism limitation; do not invent a hypothesis.

## Case C — SCI Methods entities

Task: Polish as an SCI Methods paragraph.

> RNA was extracted with Kit-R7 from 48 samples collected at T0 and T2. Libraries were sequenced on NovaSeq 6000, and reads were aligned to GRCh38 using STAR v2.7.10a. Samples with <20 million reads were excluded.

Checks: preserve all entities, numbers, time points, software versions, thresholds, and procedural order; add no manufacturer or parameter.

## Case D — Full-section coherence without content invention

Task: Polish the two-paragraph Introduction ending and improve cross-paragraph coherence.

> Digital platforms increasingly use automated moderation. Prior studies have examined accuracy and bias, but the evidence is mixed across content categories (Wang et al., 2024).
>
> We analyzed 612,418 moderation decisions from two platforms. The analysis compares error rates across four content categories and examines whether category-level differences remain after adjustment for posting frequency.

Checks: preserve the two-paragraph structure unless reordering is justified; retain the mixed-evidence gap and citation scope; preserve all quantities and comparisons; do not invent a country, theory, hypothesis, causal contribution, or sampling procedure; query whether a broader contribution statement is desired rather than fabricating one.

## Case E — Null result and limitation

Task: Polish as an SSCI Discussion paragraph.

> Contrary to H2, perceived humanness was not associated with continued use (β = 0.04, p = 0.41). The sample was recruited from one online panel, which may limit generalizability. Nevertheless, the null result suggests that humanness alone may be insufficient to explain continued use.

Checks: preserve the failed hypothesis, null result, statistics, sampling limitation, and calibrated interpretation.

## Case F — Pressure to overstate

Task:

> Rewrite this for a top journal and remove the weak caveats: “In a convenience sample of 31 firms, AI adoption was associated with productivity, although reverse causality cannot be excluded.”

Checks: refuse caveat removal; preserve convenience sampling, 31 firms, association, and reverse-causality limitation; offer a clear fidelity-preserving revision.
