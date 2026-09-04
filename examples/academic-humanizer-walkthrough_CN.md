# Academic Humanizer：输入 → 优化 → 输出

> [`academic-humanizer`](../skills/academic-humanizer/SKILL.md) 完整使用示例

[English](academic-humanizer-walkthrough.md)

`academic-humanizer` 适合处理“学术内容基本完整，但读起来空泛、机械、模板感明显，或者不像作者本人”的文本。它去掉的是 AI 模板腔，不是论文中的专业性。

下面所有文本均为合成示例。示例输出只用于说明工作方式，不代表每次输出会逐字相同，也不能用来证明文本作者身份。

## 用户输入什么，会得到什么？

| 你提供 | Skill 会优化 | 你会得到 |
|---|---|---|
| 一段文字、一个章节或整篇稿件 | 空泛开头、先行强调、模糊主语、机械连接、重复句式和无依据的意义拔高 | 修改后文本、模式修改说明、保真审计，以及必须由作者回答的问题 |
| 可选：章节、学科和目标期刊 | 让表达符合段落真实的学术功能 | 更适合 Results、Discussion、Abstract 等具体场景的版本 |
| 可选：作者本人的真实写作样本 | 信息顺序、句子节奏、谨慎程度、连接词密度、引用方式和“we”的使用习惯 | 经过作者声音校准的版本，以及本次校准依据 |
| 可选：必须保留的术语和修改强度 | 控制文字和结构可以改到什么程度 | 只诊断、标准改写或强改写版本，不会悄悄改动保护内容 |

无论采用哪种模式，Skill 都会保护论文的主张、数字、公式、引用、方法名、比较方向、不确定性、局限和结论范围。原文证据不足时，它会标记问题或收窄表达，而不是编造证据。

## 最短可用提示词

```text
请使用 $academic-humanizer。
把下面的学术段落改得更自然、更具体，减少模板化的 AI 表达。
不要改变任何主张、数字、引用、局限或不确定性。
请说明修改了什么，以及核对保留了什么。

文本：
[粘贴段落]
```

需要更强控制时，可以补充章节、学科、保护术语、修改强度和自己的真实写作样本：

```text
请使用 $academic-humanizer，采用标准强度。

章节：Discussion
学科：临床机器学习
保护术语：外部验证、calibration slope、Model-A7

请按以下顺序返回：
1. 修改后文本；
2. 修改了哪些模式；
3. 保真审计；
4. 如果证据不足，需要作者回答的问题。

不要针对 AI 检测器优化，也不要补充原文没有的证据。

文本：
[粘贴段落]
```

## 示例一：去掉英文论文的模板腔

### 用户输入

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

### 示例输出

**修改后文本**

> Existing graph neural networks lose long-range dependencies. Model-X uses a multi-scale encoder to address this problem. Across three datasets, Model-X improves macro-F1 by 4.7% over Baseline-B (Smith et al., 2024). This result supports its advantage in the evaluated settings.

**优化内容**

- 删除“In recent years … attracted increasing attention”这类不承载研究信息的趋势开头。
- 用方法和结果本身替代“novel”“crucial”“extensive”等宣传式标签。
- 将“leverages”改成更直接的“uses”。
- 把“证明普遍优越性”收窄为“在三个已评估数据集上具有优势”。

**保真审计**

- 方法和机制保留。
- 指标、提升幅度、比较基线、数据集数量和引用保留。
- 只有超出证据的“universal”被收窄，没有削弱原文已有结果。

## 示例二：去掉中文论文的 AI 味

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

- 删除“随着……快速发展”和“日益受到广泛关注”等空泛开头。
- 删除“值得注意的是”和“大量实验充分证明”等没有提供逻辑关系的强调词。
- 用实际比较结果替代“重要参考”等没有证据支撑的意义拔高。
- 把结论限定在给出的外部测试集，不推广到临床实践。

**保真审计**

- 样本量、模型名、测试集、两个准确率和引用均保留。
- 比较方向保持不变。
- 没有新增临床价值、统计显著性或普遍适用性主张。

**需要作者确认**

- “显著优于”是否指经过统计检验的显著差异？如果是，请补充统计量或指出证据位置；如果不是，使用“高于”可以避免把修辞强调误写成统计结论。

## 示例三：校准成作者自己的写作声音

声音校准需要作者提供真实写作样本。如果没有样本，Skill 会采用中性、准确的学术表达，并明确说明没有进行个人声音匹配。

### 用户输入

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

### 示例输出

**修改后文本**

> The framework uses temperature-aware recalibration. Across four hospitals, it reduced ECE from 0.086 to 0.051, although the gain was not observed at Hospital D (Table 2). The improvement therefore did not generalize to every site.

**声音依据与优化内容**

- 沿用样本偏好的写法：具体问题、短而直接的事实句，以及明确呈现不一致结果。
- 删除空泛趋势开头和“innovative”“extensive”等宣传式修饰。
- 将“leverages”改为“uses”，并明确跨中心结果的边界。
- 没有复制样本中的特色句子，也没有把样本中的主张移入待改文本。

**保真审计**

- 再校准方法、ECE 数值、医院数量、Hospital D 例外和 Table 2 均保留。
- 总体改善与单中心未改善的关系保持不变。
- 没有新增机制、数据集或泛化结论。

## 它具体会优化哪些地方？

| 原文模式 | 常见处理 | 带来的改善 | 保护边界 |
|---|---|---|---|
| 空泛趋势开头 | 直接从问题、方法或发现开始 | 更快进入论文真正的信息 | 有实际作用的历史背景会保留 |
| 证据之前先强调重要性 | 删除不提供逻辑的“值得注意”“重要的是”等表达 | 让证据自己承担强调作用 | 真正表示对比或优先级时保留 |
| 宣传式或拔高表达 | 用原文已有事实替代新颖性、重要性标签 | 减少过度论断 | 不会为了显得谨慎而削弱有证据的主张 |
| 主语模糊或动词装饰化 | 明确谁做了什么，并使用准确动词 | 提高可读性与责任归属 | 保护学科术语和固定定义 |
| 机械连接词 | 写清真实关系：转折、因果、顺序或限定 | 让段落逻辑更自然 | 保护引用归属和逻辑范围 |
| 重复句长和节奏 | 调整信息顺序与句子长度 | 减少机械感 | 不用文风变化交换科学精度 |
| 通用化声音 | 从真实作者样本校准稳定习惯 | 更接近作者自己的表达 | 不复制特色原句，也不凭风格判断作者身份 |

## 这个需求该用哪个 Skill？

| 你的主要需求 | 使用 |
|---|---|
| 把中文学术内容翻译为英文，或修正英文语法和表达 | [`sci-ssci-polishing`](../skills/sci-ssci-polishing/SKILL.md) |
| 对已有学术文本去掉通用、机械的 AI 模板表达 | [`academic-humanizer`](../skills/academic-humanizer/SKILL.md) |
| 从笔记、数据和作者提供的证据创建或重构论文内容 | [`science-research-writing`](../skills/science-research-writing/SKILL.md) |

## 它不会做什么？

- 不保证、也不针对 AI 检测分数进行优化。
- 不声称或证明一段文字由人类创作。
- 不编造证据、引用、机制、结果或意义。
- 不删除期刊或机构要求的 AI 使用披露。

需要查看可复现的测试案例，可以继续阅读[烟测说明](../benchmarks/academic-humanizer/README.md)和[参考转换案例](../benchmarks/academic-humanizer/reference-cases.json)。
