<div align="center">
  <img src="assets/sci-ssci-research-writing-hero.png" alt="SCI/SSCI 科研写作 Skills——规划、起草、润色，保护科学内容" width="100%">
</div>

# SCI/SSCI 科研写作 Skills

> **从研究材料到结构完整的论文：不编造证据，不夸大结论，不改写科学内容。**

这是一组用于规划、起草、修改、翻译和润色科研论文的开源 Agent Skills。仓库将一套经典的分章节论文写作方法，与通过筛选后 SCI/SSCI 论文语料流程提炼的写作观察结合起来。

<p align="center">
  <a href="README.md">English</a> ·
  <a href="docs/science-research-writing/getting-started.md">1 分钟上手</a> ·
  <a href="#安装"> 安装</a> ·
  <a href="#只想使用一个-skill">轻量下载</a> ·
  <a href="#在你的项目中复用这些机制">复用与引用</a> ·
  <a href="#使用这些-skills-的项目">项目展示</a>
</p>

## 两个来源，一条科研写作流程

这个仓库主要做两件相互衔接的事：

| 方法来源 | Skill | 它能帮你做什么 |
|---|---|---|
| Hilary Glasman-Deal 的《*Science Research Writing*》所代表的分章节教学和目标论文逆向拆解方法 | [`science-research-writing`](skills/science-research-writing/SKILL.md) | 判断论文每一部分应该完成什么任务，再把想法、笔记、数据、文献或初稿变成当前最有用的论文成果 |
| 从 1,000 篇 SCI/SSCI 论文元数据候选池出发的筛选和语料分析流程 | [`sci-ssci-polishing`](skills/sci-ssci-polishing/SKILL.md) | 翻译或润色已有论文，同时保护数据、引用、术语、局限和论断强度 |

用大白话说：**经典写作方法帮助 Agent 理解论文应该怎么写；经过筛选的 SCI/SSCI 论文语料帮助 Agent 理解论文应该怎么表达。**两个 Skill 共同帮助研究者获得结构更清楚、表达更准确、证据更忠实的论文，最终的学术判断仍然属于作者。

<div align="center">
  <img src="assets/sci-ssci-research-writing-architecture.png" alt="SCI/SSCI 科研写作 Skills 架构：由经典著作启发的写作工作流、SCI/SSCI 论文语料筛选流程与证据保护合约" width="100%">
</div>

### 正在开发科研 Agent？

你可以在自己的项目中复用本仓库的证据保护合约、论断强度控制和目标期刊建模方法。

[查看可复用机制](#在你的项目中复用这些机制) · [引用本仓库](CITATION.cff) · [添加你的项目](#使用这些-skills-的项目)

## 看看你现在适合哪个 Skill

| 你现在有什么 | 使用 | 通常会得到什么 |
|---|---|---|
| 一个想法或研究问题 | `science-research-writing` | 需要明确的问题、材料清单和实际可执行的下一步 |
| 笔记、数据、文献或研究方案 | `science-research-writing` | 只基于现有材料的论文计划或章节初稿 |
| 局部初稿或完整论文 | `science-research-writing` | 修改建议、前后一致性检查或证据审计 |
| 中文学术文字或英文论文 | `sci-ssci-polishing` | 学术英文和一份保真审计 |

## 一句话开始

```text
请使用 $science-research-writing 帮我写论文。
这是我现在已有的材料：[上传附件或粘贴文字]
```

Skill 会先读取你的材料，判断当前最有用的成果是计划、初稿、修改还是审计，不需要用户编写很长的 Prompt，也不需要选择内部模式。

[一分钟上手](docs/science-research-writing/getting-started.md) · [使用场景](docs/science-research-writing/use-cases.md) · [可复制的输入示例](docs/science-research-writing/input-examples.md) · [输出说明](docs/science-research-writing/output-guide.md)

## 安装

需要 Node.js 18 或更高版本。

```bash
# 从研究材料开始写论文
npx skills add Yila-AI/sci-ssci-skills --global --agent codex --skill science-research-writing --yes --copy

# 翻译或润色已有初稿
npx skills add Yila-AI/sci-ssci-skills --global --agent codex --skill sci-ssci-polishing --yes --copy
```

查看仓库中所有可安装的 Skills：

```bash
npx skills add Yila-AI/sci-ssci-skills --list
```

### 只想使用一个 Skill？

如果只是为了运行某个 Skill，你不需要克隆完整仓库，也不需要让 Agent 读取仓库根目录。上面带有 `--skill ... --copy` 的命令只会把选中的运行时 Skill 复制到 Agent 的 Skills 目录。

如需手动安装或集成到其他项目，可以从[最新 Lean Release](https://github.com/Yila-AI/sci-ssci-skills/releases/latest)下载已打包的 `sci-ssci-polishing` Skill。完整仓库继续保留语料、评测、来源记录和案例，供需要审查 Skill 构建与评估方法的研究者使用。

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

第一句只报告了有边界的研究结果；第二句却偷偷把局部发现变成了普遍结论。两个 Skill 都会尽量发现这种漂移：证据可以被理清、组织、翻译和润色，但不能被悄悄加强。

[查看奶茶案例完整中文版](examples/science-research-writing-walkthrough_CN.md) · [Read the complete walkthrough in English](examples/science-research-writing-walkthrough.md)

## 两个 Skill 分别增加了什么？

### `science-research-writing`

- 根据想法、材料、局部初稿或完整初稿，自动进入当前最有用的任务；
- 按读者问题和信息功能组织引言、方法、结果、讨论、结论、摘要和标题；
- 学习目标期刊论文的功能与变化，不保存或复制原句；
- 记录关键陈述的来源，并标出缺失的证据；
- 检查数字、引用、保护术语和论断强度标记；
- 给出小白也能理解的输出，每次最多追问一个阻断性问题。

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
[Yila-AI/sci-ssci-skills](https://github.com/Yila-AI/sci-ssci-skills),
including its Evidence-Preserving Draft Contract and Claim-Strength Contract.
```

复用仍须遵守仓库许可证和适用的第三方权利。

## 使用这些 Skills 的项目

如果你的科研 Agent、学术写作工具或开源项目正在使用或改编这套工作流，欢迎提交 [Issue](https://github.com/Yila-AI/sci-ssci-skills/issues) 或 Pull Request，并附上一句简介和公开链接。

_暂时还没有收录项目。_

## 评测

两个 Skill 的评测结果必须分开理解。

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

这些评测只支持狭义的安全性和一致性结论，不能证明期刊录用、全学科适用性、科学正确性，也不能证明它优于领域专家或专业编辑。

## 版权、数据与专业边界

- 仓库不包含书籍 PDF、论文 PDF、订阅全文、抽取的论文段落、句库或私有访问记录。
- 公开语料表只包含书目元数据、筛选标签和聚合结果。
- `SCI` 和 `SSCI` 用于描述语料和用户范围；本独立项目与 Clarivate、任何期刊、作者或出版社没有隶属关系。
- 两个 Skill 均为公开测试版，不替代作者、领域专家、统计学家、伦理审查或专业编辑的最终审核。

## 引用与许可证

正式引用信息见 [`CITATION.cff`](CITATION.cff)。原创代码、Skill 指令和项目文档使用 [Apache License 2.0](LICENSE)。第三方事实、名称和外部资源仍受各自来源条款约束。
