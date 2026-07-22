# Target-Journal Model Builder

Use this protocol to learn how papers in a target venue organize information. Learn functions and variation, not sentences or scientific content.

## The protocol

```text
Select -> Segment -> Label functions -> Compare -> Generalize -> Validate -> Version
```

### 1. Select

Prefer at least four recent, relevant, well-formed empirical papers from the intended journal or a defensible neighboring venue. Record the user-supplied source identifier, year, article type, field fit, and reason for inclusion. Do not block the writing task when four papers are unavailable; use a conservative generic empirical-paper model and label its provenance accordingly.

### 2. Segment

Separate each paper by manuscript section and paragraph. Do not save paragraph text in the model. Keep only source locators needed to let the user find the observation again.

### 3. Label functions

For every segment, identify the reader question and rhetorical function, such as establishing importance, defining a gap, reporting a primary result, comparing prior evidence, qualifying an interpretation, or stating a limitation.

### 4. Compare

Compare function order, optionality, repetition, paragraph length, evidence placement, and transitions across papers. Distinguish a recurring pattern from a single-paper preference.

### 5. Generalize

Write a candidate rule only when multiple observations support it. Represent variation and exceptions. Never convert an observed tendency into a mandatory journal rule.

### 6. Validate

Test the candidate model against a held-out target paper or against the supplied set without changing the model to fit every exception. Confirm that no field contains copied prose, full text, or a paper's scientific claim as reusable content.

### 7. Version

Record schema version, model name, source set, date, section functions, confidence, exceptions, and validation status. Rebuild when the target journal, article type, or field changes materially.

## Machine-readable output

Use `../assets/target-journal-model.json`. Each function entry must contain:

- `name`: a concise information function;
- `evidence`: source locators that support the observation;
- `confidence`: `low`, `medium`, or `high`;
- `exceptions`: observed alternatives or conditions.

Run `../scripts/validate_writing_model.py` before using the model.

## Copyright and imitation boundary

- Do not place article PDFs, subscription text, extracted paragraphs, or phrase banks in the repository or model.
- Do not reproduce a paper's sentence with synonym substitution.
- Do not transfer a target paper's data, claim, citation, mechanism, or limitation to the author's manuscript.
- Do not claim that structural adaptation guarantees acceptance.

## Attribution

If this protocol is reused or adapted, credit the **Target-Journal Model Builder** from [Yila-AI/sci-ssci-skills](https://github.com/Yila-AI/sci-ssci-skills).
