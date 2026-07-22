# From a Milk-Tea Question to a Research Paper

> A complete beginner walkthrough for `science-research-writing`

[中文版](science-research-writing-walkthrough_CN.md)

## Before we begin

This is a **synthetic educational example**. The participants, methods, and results are fictional. The response excerpts are **illustrative outputs**, not benchmark results, guaranteed responses, or evidence that the proposed study is scientifically complete.

The purpose is to show how a user can start with an everyday question and gradually use the Skill to build a researchable question, organize methods, report findings, limit interpretation, and map a paper.

```text
curiosity
   ↓
researchable question
   ↓
methods inventory
   ↓
Results and Discussion
   ↓
claim and title checks
   ↓
complete paper map
```

You do not need to prepare everything before starting. Give the Skill what you have and tell it not to fill missing evidence with plausible details.

## Stage 1: Start with a curiosity

Imagine that your first idea is:

> Does adding more ice to milk tea make it taste sweeter?

The question sounds simple, but "more ice" could change temperature, dilution, drinking time, or all three. A safe writing workflow should clarify the question before drafting a paper.

### Copyable input

```text
Use $science-research-writing to help me plan a paper.

My initial question is: Does adding more ice to milk tea make it taste sweeter?
I have not designed the study yet.

Please explain in plain language:
1. which concepts are still ambiguous;
2. what decisions I need to make;
3. what materials or data I would need;
4. the single best next step.

Do not invent results or citations.
```

### Illustrative output

The Skill could identify questions such as:

- Are you studying the amount of ice, the serving temperature, or dilution over time?
- Will every drink begin with the same sugar concentration and volume?
- Does "sweeter" mean a rating on a scale, a forced choice, or something else?
- Who will taste the drinks, and will they know which condition they receive?
- At what time after serving will each rating be collected?

**One next step:** choose one independent variable and define how perceived sweetness will be measured before selecting participants or writing Methods.

The useful result is not a fabricated paper. It is a clearer question and a concrete next action.

For the rest of this walkthrough, suppose the researcher narrows the project to a simpler question:

> How do tea base and sugar level affect milk-tea ratings among university students?

## Stage 2: Organize method notes without filling the gaps

Suppose you now have these notes:

- 120 university students;
- three tea bases: black tea, oolong tea, and jasmine tea;
- three sugar levels: 30%, 50%, and 70%;
- nine recipes in total;
- anonymous recipe codes;
- ratings on a 10-point scale.

### Copyable input

```text
Use $science-research-writing to organize the Methods section of my paper.

Known information:
- 120 university students participated.
- We compared black tea, oolong tea, and jasmine tea.
- Each tea base was prepared with 30%, 50%, and 70% sugar.
- The nine recipes used anonymous codes.
- Participants rated the drinks on a 10-point scale.

Organize only the information I supplied under study design, participants,
conditions, procedure, measurement, and analysis.

List anything important that is still missing. Do not invent cup volume,
serving order, randomization, palate cleansing, exclusion criteria, study date,
ethics details, statistical tests, or software.
```

### Illustrative output

**Supported method skeleton**

> The study used an anonymous tasting design involving 120 university students. Nine milk-tea recipes combined three tea bases (black tea, oolong tea, and jasmine tea) with three sugar levels (30%, 50%, and 70%). The recipes were identified by anonymous codes, and participants rated the drinks on a 10-point scale.

**Information still required**

- participant recruitment and eligibility criteria;
- whether every participant tasted every recipe;
- recipe preparation, serving volume, and temperature;
- serving order and whether it was randomized;
- any palate-cleansing procedure;
- the wording and anchors of the 10-point scale;
- planned statistical analysis;
- study timing, ethics process, and consent procedure where applicable.

The Skill can organize supported facts immediately while leaving unsupported details visible for the author to resolve.

## Stage 3: Keep Results and Discussion separate

Suppose the descriptive results are:

- 30%-sugar oolong milk tea has the highest mean rating: 8.4/10;
- 70%-sugar oolong milk tea has a mean rating of 6.1/10;
- jasmine-tea ratings vary little across the three sugar levels.

No inferential statistics or external literature have been supplied.

### Copyable input

```text
Use $science-research-writing to draft a Results paragraph and the opening of
the Discussion.

Synthetic study: anonymous tasting by 120 university students.
Finding 1: 30%-sugar oolong milk tea had the highest mean rating, 8.4/10.
Finding 2: 70%-sugar oolong milk tea had a mean rating of 6.1/10.
Finding 3: jasmine-tea ratings varied little across 30%, 50%, and 70% sugar.

Preserve every number and the weak jasmine result. Do not claim statistical
significance, causality, a psychological mechanism, or universal consumer
preference. Do not add citations.
```

### Illustrative Results output

> Among the nine recipes, oolong milk tea with 30% sugar received the highest mean rating (8.4/10). The corresponding rating for oolong milk tea with 70% sugar was 6.1/10. Ratings for the jasmine-tea base varied little across the three sugar levels.

This paragraph reports what was observed. It does not explain why the ratings differed or claim that the descriptive differences are statistically significant.

### Illustrative Discussion output

> In this sample, oolong milk tea with 30% sugar received the highest mean rating, whereas a higher sugar level did not correspond to a higher rating for the same tea base. Ratings for the jasmine-tea base changed little across sugar levels. Because inferential results were not provided, these patterns should be treated as descriptive. In addition, the participants were university students from one setting, so the findings should not be generalized to consumers of all ages and regions.

The Discussion can interpret the pattern and state its boundaries. It cannot invent a preference mechanism, import unsupported health explanations, or turn one student sample into all consumers.

## Stage 4: Check claim strength and title promises

The same observation can be written at very different strengths.

**Supported by the supplied evidence:**

> Among participants in this study, 30%-sugar oolong milk tea received the highest mean rating.

**Not supported by the supplied evidence:**

> 30%-sugar oolong milk tea is the world's best milk-tea recipe.

The first statement is limited to the observed sample. The second silently turns a local descriptive result into a universal conclusion.

The title creates the same risk:

| Title | Assessment |
|---|---|
| *The World's Best Milk-Tea Recipe* | Overpromises a universal result |
| *Milk-Tea Ratings across Tea Bases and Sugar Levels among University Students* | Names the comparison and the studied population without adding a causal promise |

A title is a promise. Every major promise in it should be supported by the paper.

## Stage 5: Map the complete paper

The Skill can now map the available evidence to the job of each manuscript section.

| Section | Reader question | Milk-tea content | What is still needed |
|---|---|---|---|
| Introduction | Why was the study needed? | Tea base and sugar may shape product ratings | Verified literature and a supported research gap |
| Methods | What exactly was done? | 120 students, three tea bases, three sugar levels, anonymous codes, 10-point ratings | Recruitment, preparation, order, measurement anchors, analysis, and ethics details |
| Results | What was found? | 8.4 for 30%-sugar oolong, 6.1 for 70%-sugar oolong, little jasmine variation | Complete table and inferential results, if conducted |
| Discussion | What might the findings mean? | Preferences did not rise uniformly with sugar in this sample | Verified comparisons, author-supported explanations, and fuller limitations |
| Conclusion | What can the evidence support? | A bounded summary of ratings in this sample | Final analysis and confirmed scope |
| Abstract | What matters in one minute? | Question, design, main ratings, and cautious conclusion | Completed sections and verified final numbers |
| Title | What does the paper promise? | Tea base, sugar level, ratings, and university-student scope | Alignment with the final design and analysis |

The map does not make incomplete evidence complete. It shows what can be written now and what must be supplied before the manuscript can safely say more.

## Try it with your own research

Copy this template and replace the brackets:

```text
Use $science-research-writing to help me with my paper.

Research question:
[What are you trying to find out?]

Materials I currently have:
[Notes, protocol, tables, figures, references, or draft]

What I want to work on now:
[Plan, Introduction, Methods, Results, Discussion, Conclusion, Abstract,
Title, revision, or audit]

My intended meaning:
[What should the reader understand?]

Facts that must not change:
[Numbers, statistics, technical terms, citations, null results, limitations,
and claim boundaries]

If evidence is missing or conflicting, flag it instead of filling the gap.
Do not invent data, citations, methods, mechanisms, or conclusions.
```

Use [`science-research-writing`](../skills/science-research-writing/SKILL.md) when you need to plan, draft, restructure, or audit scientific content from author-supplied evidence. Use [`sci-ssci-polishing`](../skills/sci-ssci-polishing/SKILL.md) when the scientific content already exists and the main task is translation or language polishing.
