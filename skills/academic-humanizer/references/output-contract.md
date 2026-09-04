# Output contract

Return only the sections useful for the requested mode.

## Rewrite modes

### 1. Revised text

Provide clean text without inline annotations unless the user requests tracked changes. Preserve the original language unless translation was explicitly requested.

### 2. Pattern changes

Use two to six concise bullets. Name meaningful categories rather than claiming that the text is now “human-written”. Examples:

- replaced a generic opening with the study's concrete problem;
- removed repeated significance claims that added no evidence;
- shortened clause-stacked sentences while keeping citation scope;
- replaced vague magnitude with supplied quantitative evidence;
- reduced mechanical connective repetition.

### 3. Fidelity audit

Always report:

```text
Fidelity audit
- Numbers and statistics: Preserved / Query / Not present
- Citations and reference labels: Preserved / Query / Not present
- Technical terms and named entities: Preserved / Query
- Claim and causal strength: Preserved / Query
- Limitations and uncertainty: Preserved / Query / Not present
- Voice calibration: Strong basis / Moderate basis / Limited basis / Not performed
```

### 4. Author queries

Include only when ambiguity, unsupported language, missing evidence, or an apparent inconsistency affects meaning. Quote the minimum fragment needed to identify the issue. Never hide a scientific question inside the change summary.

## Audit-only mode

Return a compact table:

| Location | Pattern | Why it weakens the passage | Smallest useful fix |
|---|---|---|---|

Then provide the fidelity risks and author queries. Do not rewrite unless requested.

## Optional source-to-revision view

When the user requests tracked or explanatory output, add a concise table after the clean revision:

| Source segment | Revision | Reason |
|---|---|---|

Keep fragments short. Do not expose private chain-of-thought or label text as AI-generated based on stylistic cues.
