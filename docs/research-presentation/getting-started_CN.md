# Research Presentation：一分钟上手

`research-presentation` 的对外标题是 **Paper to Slides**。它把论文、研究初稿、结果图表或研究笔记转化为有证据来源的学术汇报，而不是直接把摘要拆成一页页文字。

## 安装

需要 Node.js 18 或更高版本：

```bash
npx skills add Yila-AI/awesome-research-skills \
  --global \
  --agent codex \
  --skill research-presentation \
  --yes \
  --copy
```

## 使用

```text
Use $research-presentation to turn this paper into a source-grounded research presentation.
Audience: [journal club / lab meeting / conference / seminar / thesis defense]
Time: [minutes]
Language: [English / Chinese / bilingual]
Output: editable PPTX, speaker notes, and a source map
```

然后附上你有权处理的论文 PDF、研究材料、图表或补充说明。

## 它会交付什么

- 一页一句话的汇报叙事和页面大纲；
- 证据台账：每个关键数字、图表和结论的来源锚点；
- 可编辑的页面内容、讲稿备注和视觉系统建议；
- 渲染后的逐页检查：溢出、密度、来源标记、图表可读性和结论边界；
- 明确列出的缺失证据、冲突数据和需要作者确认的地方。

如果只有一篇论文，最稳妥的第一句是：

```text
Use $research-presentation. Turn the attached paper into a 10-minute journal-club deck.
Keep every quantitative claim traceable to a figure, table, section, page, or DOI.
```

下一步：[使用场景](use-cases_CN.md) · [论文抽取合约](../../skills/research-presentation/references/paper-extraction.md) · [质检合约](../../skills/research-presentation/references/qa-contract.md)
