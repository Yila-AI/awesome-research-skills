# Milk-Tea Walkthrough Design

## Decision

Add one complete synthetic walkthrough in two separately authored versions:

- `examples/science-research-writing-walkthrough.md`
- `examples/science-research-writing-walkthrough_CN.md`

The English page serves international visitors. The Chinese page serves
Chinese-speaking beginners. They use the same facts, stages, safeguards, and
links, but each page is written naturally for its audience rather than as a
line-by-line bilingual layout.

Do not create a dataset folder, downloadable pseudo-data, screenshots, or
model-specific transcripts in this iteration. Those additions would increase
maintenance cost and could make an illustrative example look like a real study
or a benchmark result.

## Purpose

The existing examples are concise but academically abstract and fragmented.
The new walkthrough must let a novice see how one everyday question moves
through the complete `science-research-writing` workflow:

```text
curiosity -> research question -> methods inventory -> results draft
          -> discussion boundaries -> title and paper map -> reusable prompt
```

The walkthrough demonstrates how to use the Skill. It does not demonstrate
scientific validity, model superiority, journal readiness, or a measured Skill
effect.

## Synthetic Scenario

Use one stable fictional scenario throughout:

- question: how tea base and sugar level affect milk-tea ratings;
- participants: 120 university students;
- tea bases: black tea, oolong tea, and jasmine tea;
- sugar levels: 30%, 50%, and 70%;
- procedure: anonymous tasting and 10-point ratings;
- reported findings: 30%-sugar oolong receives the highest mean rating of
  8.4; 70%-sugar oolong receives 6.1; jasmine ratings vary little across the
  three sugar levels;
- scope boundary: a university-student sample from one setting does not
  represent all consumers.

All pages must identify these facts as synthetic and educational.

## Page Structure

Each language version follows the same seven-part structure.

### 1. What this example teaches

Explain that users may start with whatever they have. Show the complete
workflow map and state that outputs are illustrative, not benchmark results.

### 2. Stage 1: Start with a curiosity

Use the beginner question about whether ice amount changes perceived
sweetness. Provide a copyable prompt asking the Skill to identify ambiguous
concepts, needed materials, and the next step without inventing results or
citations.

Show an illustrative planning response that distinguishes ice amount from
temperature, asks whether sugar concentration is fixed, defines perceived
sweetness, and considers participants and blinding.

### 3. Stage 2: Organize method notes

Provide the 120-participant, three-tea-base, three-sugar-level notes and a
copyable prompt. Show the supported method skeleton and a missing-information
checklist. The example must not invent cup volume, serving order,
randomization, palate cleansing, exclusion criteria, study date, ethics
details, or statistical software.

### 4. Stage 3: Separate Results from Discussion

Provide the three fixed findings. Show a bounded Results paragraph and a
Discussion opening that repeats the main finding, preserves the weak/jasmine
result, avoids invented explanations, and states the sampling limitation.

### 5. Stage 4: Check claim strength and title promises

Contrast the supported scoped statement with the unsupported universal
"world's best" claim. Compare an overpromising title with a bounded title.

### 6. Stage 5: Map the complete paper

Use a compact section table covering Introduction, Methods, Results,
Discussion, Conclusion, Abstract, and Title. Each row names the reader question
and the milk-tea content that could answer it.

### 7. Try it with your own research

End with one copyable template covering research question, available
materials, requested section, intended meaning, protected facts, and a request
to flag missing evidence rather than fill it in.

## Output Presentation Rules

- Keep all prompts directly copyable.
- Put the useful output before explanation.
- Label every response excerpt as "illustrative output," not "the output" or
  "expected output."
- Keep outputs concise enough that readers can compare input and response on a
  phone or GitHub page.
- Explain what the Skill preserved or refused to invent after each stage.
- Use plain language before academic terminology.
- Do not imply the synthetic method is scientifically complete or ethically
  approved.

## Repository Integration

- Add English and Chinese walkthrough links immediately after the short
  milk-tea claim-boundary example in `README.md` and `README_CN.md`.
- Add a short "Complete walkthrough" link near the top of
  `examples/quick-examples.md`.
- Do not duplicate the complete walkthrough inside the READMEs or quick
  examples.
- Cross-link the English and Chinese walkthrough pages at the top of each.

## Validation

- Verify both walkthroughs contain all fixed synthetic facts and the synthetic
  disclaimer.
- Verify all relative links resolve.
- Verify the English and Chinese pages have parallel stages and claims.
- Scan for accidental claims that the example is a real study, benchmark, or
  measured evaluation.
- Run `git diff --check` and the full repository test suite.

