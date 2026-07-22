# Science Research Writing Skill 设计规格

**日期：** 2026-07-22  
**状态：** 用户已批准，可进入实施  
**技术名称：** `science-research-writing`  
**对外名称：** *Science Research Writing: For Native and Non-Native Speakers of English*

## 1. 产品定位

`science-research-writing` 是一个面向实证研究论文的 Agent Skill。用户只需提供已有研究材料，并说明想写什么；Skill 负责识别用户当前所处的写作阶段，选择合适工作流，并在不改变作者学术原意的前提下交付下一份可用结果。

首版不按自然科学与社会科学划分用户，而是按论文类型划分：

- 支持采用常见实证研究结构的论文，包括理工科、医学、心理学、教育学、管理学、经济学等学科。
- 首版覆盖 Introduction、Methods、Results、Discussion、Conclusion、Abstract 和 Title。
- 首版不主打系统综述、纯理论论文和非标准结构的质性研究；这些类型将由后续独立工作流扩展。

## 2. 来源声明与知识产权边界

本 Skill 是一个独立、非官方项目，受 Hilary Glasman-Deal 著作 *Science Research Writing* 所呈现的论文逆向建模思路启发。

公开仓库必须明确区分两类内容：

1. **来源启发：** 根据目标期刊的优秀论文识别章节结构、信息功能和语言模式。
2. **项目原创机制：** 机器可读的目标期刊模型、章节功能地图、证据保护合约、内容来源追踪、标题—论文承诺检查、自动化不变量检查与公开评测方法。

仓库不得收录或重现原书 PDF、页面、练习题、答案、示例段落、词汇表或大量近似改写的文字。所有示例使用自建合成材料或可合法再利用的公开材料。

## 3. 核心用户体验

### 3.1 唯一入口

用户只需记住一个调用名称：

```text
使用 $science-research-writing 帮我写论文。
这是我目前已有的材料：[附件或文本]
```

用户不需要选择模式、记忆参数、掌握 Prompt 技巧，也不必先理解 IMRaD 等术语。

### 3.2 启动原则

Skill 先阅读用户提供的材料，再判断需要的工作流。

- 能从材料中可靠推断的信息不追问。
- 信息不完整时也要先给出可用的诊断或下一步，不将用户阻塞在问卷中。
- 必须追问时，一次只问一个对当前输出影响最大的问题。
- 如果用户没有提供目标期刊论文，使用保守的通用实证研究模型，不强制用户补充论文后才开始。

### 3.3 默认交付结构

默认输出只保留四个对新手有直接价值的部分：

1. **建议稿或诊断：** 当前即可使用的文字、结构或问题清单。
2. **组织逻辑：** 简要说明这份结果为何这样安排。
3. **需要作者确认：** 仅列出模型无法代替作者决定的学术问题。
4. **下一步：** 给出一个优先级最高的继续动作。

当存在学术风险时，才显示简洁的 Risk Flags；风险检查本身永远执行。

## 4. 内部工作流

### 4.1 用户阶段识别

Skill 将用户材料归入以下一种主状态：

- **想法阶段：** 只有研究主题、问题或初步假设。
- **材料阶段：** 已有研究设计、变量、结果、表格或笔记，但尚未成文。
- **局部初稿：** 已有一个或多个章节。
- **完整初稿：** 已有全文，主要需要修改、审计或适配期刊。

阶段识别结果决定默认工作流，但用户的显式要求始终优先。

### 4.2 内部能力模式

用户不直接选择下列模式；它们仅用于 Skill 内部路由：

- `lookup`：定位某个章节、写作问题或语言功能。
- `learn`：从目标期刊论文学习结构与功能模式。
- `model`：产生目标期刊写作模型。
- `plan`：规划论文或章节的功能顺序。
- `draft`：仅根据已有证据和作者意图起草。
- `revise`：修改已有文稿，并保留其学术内容。
- `audit`：检查结构、证据一致性、章节边界和结论强度。

一次任务可串联多个内部模式，例如完整初稿修改可按 `audit → plan → revise → audit` 执行。

### 4.3 七个章节模块

每个章节模块仅定义该章节的：

- 读者期待与核心任务；
- 常见信息功能及其逻辑顺序；
- 从目标论文建模时需观察的特征；
- 该章节与其他章节的边界；
- 高频失败模式与审计项。

模块不包含可直接套用的原书句库。所有语言生成必须由用户的内容和当前语境驱动。

## 5. 原创可引用机制

### 5.1 Target-Journal Model Builder

对用户提供的目标论文执行：

```text
Select → Segment → Label functions → Compare → Generalize → Validate → Version
```

产出带有来源记录的机器可读模型。模型记录文章和段落在执行什么信息功能，不保存用于模仿的原句。

### 5.2 Section Function Map

将每个章节表示为信息功能序列，用于规划、起草、审计和章节边界检查。

### 5.3 Evidence-Preserving Draft Contract

为每次起草或修改建立保护合约：

- 不新增用户材料中不存在的 claim、结果、机制、局限、引用或意义。
- 不改变数字、单位、统计符号、方向、显著性和引用归属。
- 不静默移动 claim-strength ladder 上的结论强度。
- 对无法从材料确定的内容使用明确占位符或请作者确认，不进行猜测。

### 5.4 Content Provenance Ledger

对关键陈述记录其来源类型：用户数据、用户明示判断、用户引用、结构性转述或待作者确认。该记录用于审计，默认不将技术细节全部展示给新手。

### 5.5 Title–Paper Promise Check

将标题视为向读者做出的内容承诺，检查标题中的对象、变量、关系、研究设计和适用范围是否被正文与证据支持。

## 6. 学术安全与错误处理

### 6.1 强制审计项

每次写作任务结束前必须检查：

- 新增的无依据内容；
- 数字、单位、统计符号与引用漂移；
- 结论强度升级或降级；
- 相关关系与因果关系混淆；
- 不显著结果、负向结果和条件限制被删除；
- 从特定样本静默扩大到更广人群；
- Results 中加入未授权解释，或 Discussion 中新增未支持结果；
- 目标论文原句的近似复制。

### 6.2 缺失材料

如果缺失信息不影响当前工作的安全性，Skill 继续工作并显式标记限制。如果缺失信息将导致学术内容被猜测，Skill 停止该部分起草，交付已能完成的部分，并询问一个关键问题。

### 6.3 冲突材料

当表格、正文、图注或用户口头说明相互冲突时，不自行选择一个版本。Skill 标明冲突位置和对文稿的影响，并请作者确认权威来源。

### 6.4 用户要求过度断言

如果用户要求超出当前证据的表达，Skill 不直接执行。它需要说明证据与表达之间的差距，给出一个与证据相符的版本，并由作者决定是否提供新证据。

## 7. Skill 包结构

```text
skills/science-research-writing/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── input-output-contract.md
│   ├── reverse-engineering-protocol.md
│   ├── introduction.md
│   ├── methods.md
│   ├── results.md
│   ├── discussion.md
│   ├── conclusion.md
│   ├── abstract.md
│   ├── title.md
│   └── certainty-and-claim-strength.md
├── scripts/
│   ├── validate_writing_model.py
│   └── check_draft_invariants.py
└── assets/
    ├── target-journal-model.json
    ├── section-function-map.md
    └── evidence-ledger.csv
```

`SKILL.md` 只保留路由规则、核心工作流与强制不变量，控制在 500 行以内。章节方法和详细规则通过 `references/` 按需加载。可重复执行、必须稳定判定的检查交给 `scripts/`。

Skill 目录内不创建 README、安装手册或发布日志。这些面向人类用户的内容位于仓库根目录和 `docs/science-research-writing/`。

## 8. 评测设计

### 8.1 对照组

每个固定测试案例使用相同模型、相同用户材料和相同生成条件，比较：

1. **Baseline A：** 不使用 Skill 或专门 Prompt。
2. **Baseline B：** 使用常见的“帮我写/润色论文”Prompt。
3. **Skill：** 使用 `science-research-writing`。

评测前冻结测试集、输入材料、评分规则和模型版本。仓库公开原始输出，不只展示最优案例。

### 8.2 最低测试场景

- 用户只说“帮我写论文”并附上材料；
- 研究材料完整与不完整；
- 有与没有目标期刊论文；
- 观察性研究被要求写成因果结论；
- 同时包含显著、不显著和负向结果；
- Results 和 Discussion 内容混合；
- 原文已经质量较高，检查是否过度修改；
- Introduction、Methods、Results、Discussion、Conclusion、Abstract 和 Title 的独立任务；
- 表格、正文和用户说明之间存在冲突。

### 8.3 质量指标

- 章节功能覆盖度；
- 组织、连贯性和读者可理解性；
- 作者意图保真度；
- 无依据内容数量；
- 数字、统计符号和引用漂移数量；
- claim-strength 漂移数量；
- 章节边界错误数量；
- 对目标期刊的结构适配度，同时检查近似复制；
- 已有优质内容的保留率。

### 8.4 新手体验指标

- 零配置启动成功率；
- 模糊请求路由准确率；
- 首份可用输出前的追问数和交互轮数；
- 用户需要理解的专业术语数量；
- 出错后能否给出明确、单一的恢复路径；
- 新手能否在不编写复杂 Prompt 的情况下完成一个章节。

### 8.5 发布门槛

不预先填写或宣称任何提升比例。首版使用以下可操作的发布门槛：

- 确定性不变量脚本通过全部单元测试；
- 专门设置的因果越界、数字漂移、引用伪造和不显著结果删除案例中，Skill 不出现任何一项重大学术安全错误；
- 在可与两组 baseline 直接配对的测试案例中，至少 80% 的案例显示 Skill 的学术安全错误数更少；
- 在预先公开的五分写作质量量表上，Skill 的总体中位数不得比表现最好的 baseline 低 0.25 分以上；
- 模糊的一句话请求在至少 90% 的路由测试中进入正确主工作流，并在至多一次追问后给出首份可用结果。

如果任一条件未达成，就不做正式效果宣称，而是根据失败案例迭代并重跑完整评测。

## 9. 仓库级文档与可引用性

本 Skill 不新建独立仓库，而是作为第二个平级 Skill 加入 `Yila-AI/sci-ssci-skills`：

```text
skills/
├── sci-ssci-polishing/       # 已有：翻译、润色与学术保真
└── science-research-writing/ # 新增：从材料到规划、起草与审计
```

仓库外层品牌使用 **SCI/SSCI Research Writing Skills**，`Science Research Writing` 作为当前主推的旗舰 Skill。保留现有仓库 URL，以继承已有 Star、Fork、外部链接与引用关系。

仓库采用英文优先的国际化结构：

- `README.md` 为英文主入口；
- `README_CN.md` 为内容对齐的中文入口；
- Skill 指令、参考文档、脚本字段、评测规则与原始结果以英文为权威版本；
- 中文文档负责降低本土新手的安装和使用门槛，不建立与英文版分离的功能承诺。

仓库级内容包含：

```text
docs/science-research-writing/
├── getting-started.md
├── use-cases.md
├── input-examples.md
├── output-guide.md
├── target-paper-modeling.md
├── evaluation-method.md
├── privacy-and-copyright.md
└── faq.md

benchmarks/science-research-writing/
├── evaluation-rubric.md
├── test-cases.json
├── baseline-outputs/
├── skill-outputs/
├── blind-review-results.md
└── limitations.md
```

仓库使用明确的开源许可证，并提供 `CITATION.cff`、版本标签、稳定链接、BibTeX 和 Markdown 引用模板。每个原创机制使用独立、稳定、可直接链接的文件，说明它解决的问题、算法步骤、输入输出和复用时的归属方式。

## 10. README 第一屏

README 第一屏必须在不需要用户理解内部机制的情况下回答四个问题：这是什么、能做什么、怎么安装、怎么第一次使用。

建议结构：

```text
Science Research Writing
For Native and Non-Native Speakers of English

An independent, unofficial Agent Skill inspired by the
reverse-engineering approach in Hilary Glasman-Deal’s book.

Give it your research materials. Tell it what you want to write.
The Skill will guide the next step.

[Install command]

Use $science-research-writing to help me write my paper.
Here are my current materials: [attach files]
```

第一屏不使用“证据性科研”、“STEMM”或其他需要解释的品牌术语。

## 11. 公众号发布设计

主标题方向：

> 很多博士生想全文背下来的科研写作神书，我把它的方法做成了一个 Skill

文章结构：

1. 为什么这本书会让读者产生“想背下来”的感受；
2. 阅读、收藏与写作时真正调用方法之间的差距；
3. 为什么要做成 Skill，而不是读书笔记或一条 Prompt；
4. 新手的一句话调用与完整输出示例；
5. Skill 内部如何判断阶段、建模并保护学术原意；
6. 裸模型、普通 Prompt 与 Skill 的公开评测结果；
7. Skill 不会做的事情与作者责任；
8. 安装、使用与 GitHub 地址。

文章可以引用 Bilibili、豆瓣、Goodreads 与书评中的公开热度信号来证明用户需求，但不将传播热度宣称为效果证据。Skill 的效果只使用本项目预先冻结的测试集和公开结果支持。

## 12. 实施顺序

为了避免先写大量文案、最后才发现 Skill 没有带来稳定增益，实施按以下顺序执行：

1. 创建冻结测试集和评分标准；
2. 保存裸模型与普通 Prompt 的 baseline 输出；
3. 实现核心路由、章节模块和证据保护合约；
4. 实现确定性检查脚本与模板；
5. 运行完整评测并根据失败案例迭代；
6. 达到发布门槛后完成仓库文档、README 和引用基础设施；
7. 根据真实评测结果完成公众号文章。

## 13. 验收条件

本 Skill 在满足以下条件后才视为可发布：

- 新手仅使用一句话和已有材料即可启动；
- 七个章节模块均有独立工作流和审计项；
- 目标期刊建模可在不保存或复制原句的前提下产生可用结构模型；
- 不变量检查脚本能够检出预设的数字、引用、保护术语和结论强度漂移案例；
- 固定测试集、评分方法、原始输出和限制全部可审查；
- Skill 达到第 8.5 节规定的学术安全、写作质量和新手路由门槛；
- 仓库对原书的启发、项目原创贡献和版权边界作出明确声明；
- README 第一屏可让新访客在一分钟内理解、安装并开始使用。

