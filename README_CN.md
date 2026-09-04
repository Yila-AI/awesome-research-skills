# Awesome Research Skills

<p align="center">
  <img src="assets/research-workflow-hero-yila.webp" alt="Awesome Research Skills by Yila.ai——每个 AI Agent 都应该具备的科研工作流" width="100%">
</p>

> **每个 AI Agent 都应该具备的科研工作流。**

这是一个面向科研全生命周期、持续扩展的开源 Skill Stack：从发现和理解论文，到研究写作、审查、润色与学术汇报。

当前已经提供科研写作、忠实学术润色和论文转汇报能力，更多科研环节正在建设。贯穿整个流程的共同要求是：Agent 必须交代来源、检查、不确定性和修改内容，而不是悄悄改写研究。

本项目由 **[Yila.ai](https://yila.ai/?utm_source=github&utm_medium=referral&utm_campaign=awesome-research-skills)** 构建并持续维护。Yila.ai 提供覆盖文献、证据、数据、写作和学术展示的科研工作空间。

适用于 Codex、Claude Code、WorkBuddy 风格科研 Agent，以及其他支持可复用 Skill 指令的 Agent 工作流。

<p align="center">
  <a href="https://github.com/Yila-AI/awesome-research-skills/actions/workflows/ci.yml"><img src="https://github.com/Yila-AI/awesome-research-skills/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/Yila-AI/awesome-research-skills" alt="Apache-2.0 许可证"></a>
  <a href="https://skills.sh/yila-ai/awesome-research-skills"><img src="https://skills.sh/b/yila-ai/awesome-research-skills" alt="skills.sh 安装量"></a>
  <a href="https://yila.ai/?utm_source=github&amp;utm_medium=referral&amp;utm_campaign=awesome-research-skills"><img src="https://img.shields.io/badge/Built%20by-Yila.ai-C9825A" alt="由 Yila.ai 构建"></a>
</p>

<p align="center">
  <a href="README.md">English</a> ·
  <a href="README_ja.md">日本語</a> ·
  <a href="README_ko.md">한국어</a> ·
  <a href="https://yila.ai/?utm_source=github&amp;utm_medium=referral&amp;utm_campaign=awesome-research-skills">体验 Yila.ai</a> ·
  <a href="#30-秒安装">安装</a> ·
  <a href="#从当前任务开始">从任务开始</a> ·
  <a href="#科研全流程">科研全流程</a> ·
  <a href="#只想使用一个-skill">轻量下载</a> ·
  <a href="#paper-to-slides-能力展示">Showcase</a> ·
  <a href="#在你的项目中复用这些机制">复用与引用</a> ·
  <a href="#使用致谢或改编本项目的项目">项目展示</a>
</p>

## 从当前任务开始

| 我现在想要…… | 从这里开始 | 我会得到什么 |
|---|---|---|
| 把研究想法、笔记、数据或文献组织成论文 | **Research Writer / 科研写作** · [`science-research-writing`](skills/science-research-writing/SKILL.md) | 有证据依据的论文计划、章节初稿、修订稿或完整性审计 |
| 在不改变研究内容的前提下提升学术英文 | **Paper Polisher / 论文润色** · [`sci-ssci-polishing`](skills/sci-ssci-polishing/SKILL.md) | 面向发表的学术英文和一份保真审计 |
| 把论文或研究结果做成学术汇报 | **Paper to Slides / 论文转汇报** · [`research-presentation`](skills/research-presentation/SKILL.md) | 可编辑、有来源的汇报方案，包含讲稿、来源映射和视觉质检 |

## 30 秒安装

安装器需要 Node.js 18 或更高版本。一条命令安装当前已经可用的全部能力：

```bash
npx skills add Yila-AI/awesome-research-skills --global --agent codex --skill '*' --yes --copy
```

也可以只安装你现在需要的能力：

```bash
# 规划、起草、修订或审计论文
npx skills add Yila-AI/awesome-research-skills --global --agent codex --skill science-research-writing --yes --copy

# 翻译或润色已有论文
npx skills add Yila-AI/awesome-research-skills --global --agent codex --skill sci-ssci-polishing --yes --copy

# 把论文或研究结果做成学术汇报
npx skills add Yila-AI/awesome-research-skills --global --agent codex --skill research-presentation --yes --copy
```

使用 `npx skills add Yila-AI/awesome-research-skills --list` 查看全部可安装 Skills。

### 只想使用一个 Skill？

上面的命令只会把选中的运行时 Skill 复制到 Agent 的 Skills 目录，不需要克隆整个仓库。已经达到可发布状态的 Skill 会在 [Releases 页面](https://github.com/Yila-AI/awesome-research-skills/releases)提供带版本的轻量 ZIP 包。

## 科研全流程

这个项目正在建设一条完整、连续的科研工作流，而不是把互不相关的 Prompt 放进同一个目录：

```text
问题 → 检索 → 阅读 → 综合 → 设计 → 分析 → 写作 → 审查 → 润色 → 传播
```

| 建设状态 | 科研环节 |
|---|---|
| **当前可用** | 写作、润色、学术汇报 |
| **接下来建设** | 文献检索、论文阅读、证据综合、研究审查 |
| **长期工作流** | 研究设计、数据分析、发表与更多科研传播场景 |

产品方向是提供一个统一的 `$research` 入口：它能够识别用户当前所处的科研阶段，并把任务路由给对应的专业模块。统一入口尚在建设中；当前版本仍然直接调用已经可用的各个 Skill。

各模块将共享研究问题、文献来源、证据、作者决策、论断、数据和修改记录，让检索阶段找到的依据能够一直延续到论文、审查和汇报，而不是在环节切换时丢失。

### 在 Yila.ai 使用完整科研工作流

这些开源 Skills 来自 [Yila.ai](https://yila.ai/?utm_source=github&utm_medium=referral&utm_campaign=awesome-research-skills) 正在构建的科研工作流。在更多环节被封装成可复用 Skill 的同时，Yila.ai 已经提供文献检索、论文阅读、证据综合、研究设计、数据分析、论文写作、科研配图、学术海报和 Slides 等一体化能力。

**[前往 Yila.ai 开始科研任务 →](https://yila.ai/?utm_source=github&utm_medium=referral&utm_campaign=awesome-research-skills)**

## 当前可用能力

当前版本已经提供三项相互衔接的能力：

| 方法来源 | 当前模块 | 它能帮你做什么 |
|---|---|---|
| Hilary Glasman-Deal 的《*Science Research Writing*》所代表的分章节教学和目标论文逆向拆解方法 | **Research Writer / 科研写作** · [`science-research-writing`](skills/science-research-writing/SKILL.md) | 判断论文每一部分应该完成什么任务，再把想法、笔记、数据、文献或初稿变成当前最有用的论文成果 |
| 从 1,000 篇 SCI/SSCI 论文元数据候选池出发的筛选和语料分析流程 | **Paper Polisher / 论文润色** · [`sci-ssci-polishing`](skills/sci-ssci-polishing/SKILL.md) | 翻译或润色已有论文，同时保护数据、引用、术语、局限和论断强度 |
| 以证据为中心的学术汇报设计 | **Paper to Slides / 论文转汇报** · [`research-presentation`](skills/research-presentation/SKILL.md) | 将论文和研究材料转化为可编辑、有来源锚点的学术汇报，并配套叙事规划、证据台账、讲稿备注和渲染质检 |

用大白话说：**写作 Skill 帮你把论文写清楚、改准确；`research-presentation` 再把证据搬进汇报，而不是把科学内容压扁成漂亮的页面。**最终的学术判断仍然属于作者。

### 正在开发科研 Agent？

你可以在自己的项目中复用本仓库的证据保护合约、论断强度控制和目标期刊建模方法。

[查看可复用机制](#在你的项目中复用这些机制) · [引用本仓库](CITATION.cff) · [添加你的项目](#使用致谢或改编本项目的项目)

## 一句话开始

```text
请使用 $science-research-writing 帮我写论文。
这是我现在已有的材料：[上传附件或粘贴文字]
```

Skill 会先读取你的材料，判断当前最有用的成果是计划、初稿、修改还是审计，不需要用户编写很长的 Prompt，也不需要选择内部模式。

[一分钟上手](docs/science-research-writing/getting-started.md) · [使用场景](docs/science-research-writing/use-cases.md) · [可复制的输入示例](docs/science-research-writing/input-examples.md) · [输出说明](docs/science-research-writing/output-guide.md)

如果你的目标是把论文做成 PPT，请先看 [Research Presentation 快速上手](docs/research-presentation/getting-started_CN.md) 和[使用场景](docs/research-presentation/use-cases_CN.md)。

## 可以直接复制的例子

### 从研究材料开始组织论文

```text
请使用 $science-research-writing。
我已经完成研究，但不知道怎么把它组织成一篇论文。

研究问题：
[粘贴你的研究问题]

方法：
[粘贴你做了什么]

主要结果：
[粘贴关键发现、表格或笔记]

目标期刊或领域：
[如果有就粘贴]
```

### 润色英文，但不改变科学内容

```text
请使用 $sci-ssci-polishing。
请帮我润色下面这段 Discussion，让它更清楚、更像论文表达。
不要改变数字、引用、专业术语、研究局限或论断强度。
如果有句子证据不足或表达过度，请标出来，不要悄悄替我改掉。

文本：
[粘贴段落]
```

## Paper to Slides 能力展示

`research-presentation` 可以把论文转化为有来源、有叙事、可编辑的科研汇报。[完整 Showcase](showcase/research-presentation/README_CN.md) 覆盖 6 个跨学科案例；其中网络流行病学案例包含两版完整的 12 页结果。

<p align="center">
  <a href="showcase/research-presentation/ecology-network/README.md">
    <img src="showcase/research-presentation/ecology-network/bright-azure-v2/01.webp" alt="Paper to Slides 封面示例" width="48%">
  </a>
  <a href="showcase/research-presentation/ecology-network/README.md">
    <img src="showcase/research-presentation/ecology-network/bright-azure-v2/05.webp" alt="Paper to Slides 结果页示例" width="48%">
  </a>
</p>

测试论文：[arXiv:2607.25475](https://arxiv.org/abs/2607.25475)。仓库只保留论文链接和引用信息，不复制原始 PDF。[浏览全部 6 个案例 →](showcase/research-presentation/README_CN.md)

## 为什么把《*Science Research Writing*》的方法变成 Agent 工作流？

Hilary Glasman-Deal 的《*Science Research Writing: For Native and Non-Native Speakers of English*》之所以受到研究者重视，是因为它教的不只是句型和语法。它先追问读者需要从实证论文的每个部分得到什么，再鼓励作者拆解自己领域的优秀论文，学习反复出现的信息功能，而不是复制原句。

一篇独立书评提到，该书第一版销量超过 35,000 册，并被翻译为中文、韩文和日文（[Anna Clemens, 2020](https://annaclemens.com/blog/book-review-science-research-writing-hilary-glasman-deal/)）。

它的核心思路可以归纳为七个读者问题：

| 论文部分 | 读者想知道什么 |
|---|---|
| 引言 | 为什么需要这项研究？ |
| 方法 | 研究具体是怎样做的？ |
| 结果 | 研究发现了什么？ |
| 讨论 | 这些发现意味着什么，又不能说明什么？ |
| 结论 | 现有证据真正支持什么结论？ |
| 摘要 | 如果只有一分钟，读者必须理解什么？ |
| 标题 | 这篇论文向读者承诺了什么？ |

`science-research-writing` 将这套通用方法转化为 Agent 可以执行的流程，并加入了自动任务路由、目标期刊建模、证据来源记录、作者确认边界和确定性草稿检查。

这是一个独立的非官方项目，与原书作者或 World Scientific 没有隶属或背书关系。仓库不复制原书、习题、答案、句库、示例段落或页面内容。详见[隐私与版权边界](docs/science-research-writing/privacy-and-copyright.md)。

## 英文更流畅，不代表学术上更忠实

假设 120 名大学生试喝了 9 种奶茶配方。结果发现，在这些参与者中，三分糖乌龙奶茶的平均评分最高。

**证据能够支持：**

> 在本研究的参与者中，三分糖乌龙奶茶的评分最高。

**证据不能支持：**

> 三分糖乌龙奶茶是世界上最好喝的奶茶配方。

第一句只报告了有边界的研究结果；第二句却偷偷把局部发现变成了普遍结论。两个写作 Skill 都会尽量发现这种漂移：证据可以被理清、组织、翻译和润色，但不能被悄悄加强。

[查看奶茶案例完整中文版](examples/science-research-writing-walkthrough_CN.md) · [Read the complete walkthrough in English](examples/science-research-writing-walkthrough.md)

## 当前 Skill 分别增加了什么？

### `science-research-writing`

- 根据想法、材料、局部初稿或完整初稿，自动进入当前最有用的任务；
- 按读者问题和信息功能组织引言、方法、结果、讨论、结论、摘要和标题；
- 学习目标期刊论文的功能与变化，不保存或复制原句；
- 记录关键陈述的来源，并标出缺失的证据；
- 检查数字、引用、保护术语和论断强度标记；
- 给出小白也能理解的输出，每次最多追问一个阻断性问题。

### `research-presentation`

- 从论文、初稿、图表或研究笔记开始规划有证据来源的汇报；
- 为关键论断保留证据台账和来源锚点；
- 根据文献汇报、组会、会议报告、研讨课或答辩选择叙事弧线；
- 输出可编辑的页面内容、讲稿备注和基于渲染结果的质检报告；
- 保留不确定性、局限和论断强度，而不是只追求视觉效果。

### `sci-ssci-polishing`

- 将中文学术内容翻译成适合发表场景的英文；
- 润色英文段落和完整论文章节；
- 改善信息顺序、清晰度、连贯性和学术语气；
- 保留数字、统计量、专业实体、引用、零结果、局限和结论；
- 不会为了让文字看起来更完整，自动编造机制、文献、结果或意义。

## 1,000 篇论文证据池——它意味着什么，又不意味着什么？

润色 Skill 从一个 **1,000 篇 SCI/SSCI 论文的元数据候选池**出发，通过分层筛选建立平衡的核心论文组合：

```text
1,000 篇元数据候选论文
               ↓
        200 篇平衡候选
               ↓
          60 篇核心组合
       ↙          ↓          ↘
40 篇提炼   10 篇校准   10 篇封闭盲测
```

60 篇核心组合包含 30 篇 SCI 和 30 篇 SSCI 论文，覆盖 9 个宽口径学科组合。40 篇提炼集包含 20 篇 SCI 和 20 篇 SSCI 论文，来自 28 本期刊，形成了基于 1,750 个可用段落和 220,158 个英文词的聚合观察。

这里的**“提炼”不是模型微调，也不是复制期刊原句**，而是将反复出现的章节功能、信息顺序、证据边界和失败模式转化为可复用的编辑规则。1,000 篇论文是筛选范围，并不代表项目下载、阅读或提炼了 1,000 篇全文，也不代表它们被用于训练模型。

[语料方法](skills/sci-ssci-polishing/references/corpus-method.md) · [筛选标准](corpus/selection-rubric.md) · [语料分布](corpus/corpus-summary.md) · [公开元数据](corpus/README.md)

## 在你的项目中复用这些机制

下面三个机制已被写成可单独阅读的组件，便于其他科研 Agent 和学术写作项目复用：

| 核心机制 | 它保护或实现什么 |
|---|---|
| [Evidence-Preserving Draft Contract](skills/science-research-writing/SKILL.md) | 防止在规划、起草和修改时新增没有依据的学术内容 |
| [Claim-Strength Contract](skills/science-research-writing/references/certainty-and-claim-strength.md) | 防止论断在提示、相关、预测、影响和因果之间悄悄漂移 |
| [Target-Journal Model Builder](skills/science-research-writing/references/reverse-engineering-protocol.md) | 学习目标论文的信息功能和变化，不复制原句 |

其他组件包括 [Section Function Map](skills/science-research-writing/assets/section-function-map.md)、[Content Provenance Ledger](skills/science-research-writing/assets/evidence-ledger.csv)、[Title-Paper Promise Check](skills/science-research-writing/references/title.md) 和 [Draft Invariant Checker](skills/science-research-writing/scripts/check_draft_invariants.py)。

简短致谢示例：

```markdown
**Credit:** The evidence-preserving research-writing workflow is adapted from
[Yila-AI/awesome-research-skills](https://github.com/Yila-AI/awesome-research-skills),
including its Evidence-Preserving Draft Contract and Claim-Strength Contract.
```

复用仍须遵守仓库许可证和适用的第三方权利。

## 使用、致谢或改编本项目的项目

这里收录公开使用、致谢、改编或讨论本仓库机制的项目。

| 项目 | 关系 |
|---|---|
| [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 已 credit 并改编本仓库的 claim-strength ladder 机制，用于防止多轮论文修改中的论断强度漂移。相关讨论见 [issue #569](https://github.com/Imbad0202/academic-research-skills/issues/569)、[issue #570](https://github.com/Imbad0202/academic-research-skills/issues/570) 和 [PR #573](https://github.com/Imbad0202/academic-research-skills/pull/573)。 |

如果你的科研 Agent、学术写作工具或开源项目正在使用或改编这套工作流，欢迎提交 [Issue](https://github.com/Yila-AI/awesome-research-skills/issues) 或 Pull Request，并附上一句简介和公开链接。

## 评测

已发布的评测结果必须按 Skill 分开理解。

### `sci-ssci-polishing`

| 评测 | 结果 |
|---|---:|
| 冻结的合成转换案例 | 6/6 通过 |
| 已验证可获取的盲测全文 | 9/10 |
| 发表级原文保留案例 | 18/18 通过 |
| 编造的科学内容 | 0/18 |
| 被改变的数字或引用标记 | 0/18 |
| 不必要的改写 | 0/18 |

[合成案例](benchmarks/synthetic-cases.md) · [合成输出](benchmarks/synthetic-case-outputs.md) · [盲测保留报告](benchmarks/blind-retention-results.md)

### `science-research-writing`

测试集和评分标准在实现前已经冻结。只有在原始输出、模型设置、逐案分数、失败和局限全部公开后，才会增加效果比较。

[评测协议](benchmarks/science-research-writing/README.md) · [冻结案例](benchmarks/science-research-writing/test-cases.json) · [评分标准](benchmarks/science-research-writing/evaluation-rubric.md) · [开发烟测](benchmarks/science-research-writing/smoke-test-results.md)

### `research-presentation`

公开 Showcase 展示了跨学科的输出设计，但目前还没有发布冻结的对照评测。Showcase 图片是示例，不是通用汇报质量的证据。

这些评测只支持狭义的安全性和一致性结论，不能证明期刊录用、全学科适用性、科学正确性，也不能证明它优于领域专家或专业编辑。

## 版权、数据与专业边界

- 仓库不包含书籍 PDF、论文 PDF、订阅全文、抽取的论文段落、句库或私有访问记录。
- 公开语料表只包含书目元数据、筛选标签和聚合结果。
- `SCI` 和 `SSCI` 用于描述语料和用户范围；本独立项目与 Clarivate、任何期刊、作者或出版社没有隶属关系。
- 本仓库已经达到可发布状态的 Skill 仍属于公开测试版，不替代作者、领域专家、统计学家、伦理审查或专业编辑的最终审核。

## 引用与许可证

正式引用信息见 [`CITATION.cff`](CITATION.cff)。原创代码、Skill 指令和项目文档使用 [Apache License 2.0](LICENSE)。第三方事实、名称和外部资源仍受各自来源条款约束。

Awesome Research Skills 由 **[Yila.ai](https://yila.ai/?utm_source=github&utm_medium=referral&utm_campaign=awesome-research-skills)** 构建并持续维护。
