# Academic Humanizer: Input → Optimizations → Output

> A practical walkthrough for [`academic-humanizer`](../skills/academic-humanizer/SKILL.md)

[中文版](academic-humanizer-walkthrough_CN.md)

`academic-humanizer` is for prose that is already academically usable but sounds generic, inflated, mechanically connected, or unlike the author. It removes the template voice while preserving the research.

All passages below are synthetic. The outputs are illustrative, not guaranteed responses or evidence that a detector can identify authorship.

## What do you provide, and what do you get?

| You provide | The Skill optimizes | You receive |
|---|---|---|
| A paragraph, section, or manuscript | Empty openings, generic emphasis, vague actors, mechanical transitions, repetitive cadence, and unsupported overclaiming | Revised text, a concise pattern-change report, a preservation audit, and any questions that require the author |
| Optional section, field, and venue context | Section-appropriate rhetoric and terminology | A revision suited to the passage's actual scholarly function |
| Optional genuine samples of your writing | Information order, sentence rhythm, hedging, connective density, citation integration, and use of “we” | A voice-calibrated revision plus a note explaining the voice evidence used |
| Optional protected terms and editing intensity | How far the wording and structure may change | An audit-only, standard, or strong revision without silently changing protected content |

The Skill always protects claims, numbers, equations, citations, named methods, comparison direction, uncertainty, limitations, and conclusion scope. When support is missing, it flags or narrows a claim rather than inventing evidence.

## The shortest useful prompt

```text
Use $academic-humanizer.
Make this academic passage less templated and more natural.
Do not change any claim, number, citation, limitation, or uncertainty.
Report what you changed and what you verified.

Text:
[paste your passage]
```

For more control, add the section, field, protected terms, editing intensity, and one or two genuine writing samples:

```text
Use $academic-humanizer in standard mode.

Section: Discussion
Field: clinical machine learning
Protected terms: external validation, calibration slope, Model-A7

Please return:
1. revised text;
2. patterns changed;
3. preservation audit;
4. author questions, if evidence is missing.

Do not optimize for an AI detector or add supporting evidence.

Text:
[paste your passage]
```

## Example 1: Remove an English template voice

### User input

```text
Use $academic-humanizer in standard mode.
This is a Results paragraph. Make it more direct and evidence-bounded.
Protect Model-X, Baseline-B, macro-F1, all numbers, and the citation.

In recent years, graph neural networks have attracted increasing attention.
However, existing models lose long-range dependencies. Importantly, our novel
Model-X leverages a multi-scale encoder to address this crucial challenge.
Extensive experiments demonstrate that Model-X improves macro-F1 by 4.7% over
Baseline-B on three datasets (Smith et al., 2024), thereby proving its universal
superiority.
```

### Illustrative output

**Revised text**

> Existing graph neural networks lose long-range dependencies. Model-X uses a multi-scale encoder to address this problem. Across three datasets, Model-X improves macro-F1 by 4.7% over Baseline-B (Smith et al., 2024). This result supports its advantage in the evaluated settings.

**Patterns changed**

- Removed the empty trend opening: “In recent years … attracted increasing attention.”
- Replaced promotional labels such as “novel”, “crucial”, and “extensive” with the method and result themselves.
- Replaced “leverages” with the more direct verb “uses”.
- Narrowed “proving its universal superiority” to the three evaluated datasets.

**Preservation audit**

- Method and mechanism: preserved.
- Metric, effect size, comparator, and dataset count: preserved.
- Citation: preserved.
- Claim strength: narrowed only where “universal” exceeded the supplied evidence.

## Example 2: Remove AI-like patterns from Chinese academic prose

### 用户输入

```text
请使用 $academic-humanizer，采用标准强度。
这是 Results 段落。请减少空泛开头、强调词和意义拔高。
保护 Model-A7、Baseline-C、外部测试集、所有数字和引用。

随着人工智能技术的快速发展，医学影像诊断日益受到广泛关注。
值得注意的是，本研究基于612例患者构建Model-A7。大量实验充分证明，
该模型在外部测试集上的准确率达到87.08%，显著优于Baseline-C的82.41%
[12]，从而为临床实践提供了重要参考。
```

### 示例输出

**修改后文本**

> 本研究基于612例患者构建Model-A7。在外部测试集中，Model-A7的准确率为87.08%，高于Baseline-C的82.41% [12]。这一比较表明Model-A7在该外部测试集上的准确率更高。

**优化内容**

- 删除“随着……快速发展”和“日益受到广泛关注”等不承载研究信息的开头。
- 删除“值得注意的是”和“大量实验充分证明”等先行强调。
- 用实际比较结果代替“重要参考”等没有证据支撑的意义拔高。
- 把结论范围限定在给出的外部测试集，不将单次比较推广到临床实践。

**保真审计**

- 样本量、模型名、测试集、两个准确率和引用均保留。
- 比较方向保持不变。
- 没有新增临床价值、统计显著性或普遍适用性主张。

**Author question**

- Does “显著优于” refer to a statistically significant difference? If so, supply the statistic or point to its location; otherwise, “高于” avoids turning rhetorical emphasis into a statistical claim.

## Example 3: Calibrate the revision to the author's voice

Voice matching requires genuine author samples. Without them, the Skill uses a neutral academic voice and says that personal calibration was not performed.

### User input

```text
Use $academic-humanizer in voice-matching mode.
Match stable features of my sample, but do not copy its phrases or import its claims.
Protect all numbers, Hospital D, Table 2, and the direction of every result.

My writing sample:
We focus on one practical question: whether calibration survives deployment
shift. Across four hospitals, the answer is mixed.

Draft to revise:
In recent years, reliable deployment has become increasingly important. Our
innovative framework leverages temperature-aware recalibration. Extensive
experiments demonstrate that it reduced ECE from 0.086 to 0.051 across four
hospitals. However, the gain was not observed at Hospital D (Table 2),
highlighting the complex nature of real-world generalization.
```

### Illustrative output

**Revised text**

> The framework uses temperature-aware recalibration. Across four hospitals, it reduced ECE from 0.086 to 0.051, although the gain was not observed at Hospital D (Table 2). The improvement therefore did not generalize to every site.

**Voice basis and pattern changes**

- Followed the sample's preference for a concrete question, short factual sentences, and an explicit mixed result.
- Removed the generic trend opening and promotional “innovative” and “extensive”.
- Replaced “leverages” with “uses” and made the cross-site limitation explicit.
- Did not copy a distinctive sentence or transfer a claim from the sample.

**Preservation audit**

- Recalibration method, ECE values, number of hospitals, Hospital D exception, and Table 2 reference: preserved.
- The overall improvement and site-specific failure remain in the same relationship.
- No new mechanism, dataset, or generalization claim was introduced.

## What kinds of optimization does it perform?

| Pattern in the draft | Typical action | Benefit | Guardrail |
|---|---|---|---|
| Empty trend opening | Start with the actual problem, method, or finding | Faster access to the scholarly point | Keep genuine historical context when it matters |
| Importance labels before evidence | Remove “importantly”, “notably”, “值得注意的是”, and similar cues when they add no logic | Lets the evidence carry emphasis | Keep a cue when it marks a real contrast or priority |
| Promotional or inflated language | Replace novelty and significance claims with supplied facts | Reduces overclaiming | Do not weaken a supported claim merely to sound modest |
| Vague or ornamental verbs | Name the actor and use a precise action | Improves clarity and accountability | Preserve field-specific terminology |
| Mechanical transitions | Express the actual relation: contrast, cause, sequence, or qualification | Improves coherence | Preserve citation attachment and logical scope |
| Repetitive sentence cadence | Vary sentence length and information order | Produces more natural scholarly rhythm | Do not trade precision for stylistic variety |
| Generic voice | Calibrate stable habits from genuine author samples | Makes the revision more recognizably the author's | Never copy distinctive phrases or infer identity from style |

## Choose the right Skill

| Your primary need | Use |
|---|---|
| Translate Chinese academic prose into English or correct grammar and expression | [`sci-ssci-polishing`](../skills/sci-ssci-polishing/SKILL.md) |
| Remove generic AI-like patterns from otherwise usable academic prose | [`academic-humanizer`](../skills/academic-humanizer/SKILL.md) |
| Create or restructure manuscript content from notes, data, and author-supplied evidence | [`science-research-writing`](../skills/science-research-writing/SKILL.md) |

## What it does not do

- It does not guarantee or optimize an AI-detector score.
- It does not certify that a passage was written by a human.
- It does not invent evidence, citations, mechanisms, results, or implications.
- It does not remove required AI-use disclosure language.

For reproducible test cases, see the [smoke benchmark](../benchmarks/academic-humanizer/README.md) and [reference transformations](../benchmarks/academic-humanizer/reference-cases.json).
