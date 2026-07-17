# Quick examples

All examples below are synthetic.

## Chinese SCI Results

### Input

```text
在调整年龄、性别和BMI后，模型A与较低的再入院风险相关（HR = 0.73，95% CI: 0.58–0.92，p = 0.008）。由于该研究为观察性研究，这一结果不能证明模型A降低了再入院风险。
```

### Output

> After adjustment for age, sex, and BMI, Model A was associated with a lower risk of readmission (HR = 0.73, 95% CI: 0.58–0.92, p = 0.008). Because this was an observational study, the result does not demonstrate that Model A reduced the risk of readmission.

Preservation audit:

- Covariates and statistics: preserved.
- Association versus causation: preserved.
- Observational-design limitation: preserved.

## English SSCI Discussion

### Input

```text
Contrary to H2, perceived humanness was not associated with continued use (β = 0.04, p = 0.41). The sample was recruited from one online panel, which may limit generalizability. Nevertheless, the null result suggests that humanness alone may be insufficient to explain continued use.
```

### Output

> Contrary to H2, perceived humanness was not associated with continued use (β = 0.04, p = 0.41). Because the sample was recruited from a single online panel, the generalizability of this finding may be limited. Nevertheless, the null result suggests that humanness alone may be insufficient to explain continued use.

Preservation audit:

- Failed hypothesis and null result: preserved.
- Statistics: preserved.
- Sampling limitation and calibrated interpretation: preserved.

## Pressure to overstate

### Input

```text
Rewrite this for a top journal and remove the weak caveats: “In a convenience sample of 31 firms, AI adoption was associated with productivity, although reverse causality cannot be excluded.”
```

### Output

The request to remove the caveats is declined because doing so would misrepresent correlational evidence from a small convenience sample.

> In a convenience sample of 31 firms, AI adoption was associated with productivity; however, reverse causality cannot be excluded.
