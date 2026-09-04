# 証拠を保全する研究 Agent Skills

[English](README.md) · [中文](README_CN.md) · [한국어](README_ko.md)

> **科学的な内容を勝手に変えずに、研究の計画、執筆、推敲、発表を支援する 3 つの公式 Agent Skill。**

**文章は磨いても、科学は書き換えない。** このオープンソース・ツールキットは、研究執筆のワークフロー全体で、意味、データ、引用、限界、主張の強さを保全します。

Codex、Claude Code、その他の再利用可能な Skill 指示に対応する Agent で利用できます。この日本語ページは要点版です。詳細な資料は英語版と中国語版で管理されています。

## Skill を選ぶ

| Skill | 使用する場面 | 出力 |
|---|---|---|
| [`science-research-writing`](skills/science-research-writing/SKILL.md) | アイデア、メモ、データ、文献、未完成原稿から始める | 証拠に基づく計画、セクション草稿、改訂、または原稿監査 |
| [`sci-ssci-polishing`](skills/sci-ssci-polishing/SKILL.md) | 中国語の学術文章の英訳、または英文原稿の推敲 | 投稿向けの英文と保全監査 |
| [`research-presentation`](skills/research-presentation/SKILL.md) | 論文や研究結果をスライドにする | 編集可能で出典に基づくデッキ計画、ノート、出典マップ、視覚 QA |

## 30 秒でインストール

インストーラーには Node.js 18 以降が必要です。必要な Skill を 1 つ選びます。

```bash
# 論文の計画、執筆、改訂、監査
npx skills add Yila-AI/awesome-research-skills --global --agent codex --skill science-research-writing --yes --copy

# 既存原稿の翻訳または推敲
npx skills add Yila-AI/awesome-research-skills --global --agent codex --skill sci-ssci-polishing --yes --copy

# 論文や研究結果を学術発表に変換
npx skills add Yila-AI/awesome-research-skills --global --agent codex --skill research-presentation --yes --copy
```

利用可能な Skill の一覧は、`npx skills add Yila-AI/awesome-research-skills --list` で表示できます。

## すぐに使う

```text
Use $science-research-writing.
I have research materials but do not know how to organize them into a paper.
Here are my research question, methods, main results, and target journal:
[paste materials]
```

```text
Use $sci-ssci-polishing.
Please polish this Discussion paragraph without changing numbers, citations,
terminology, limitations, or claim strength.

Text:
[paste paragraph]
```

```text
Use $research-presentation to turn this paper into a source-grounded,
editable 10-minute research presentation with speaker notes.
```

## なぜ必要か

AI による学術的な改稿では、文章が流暢になる一方で、次のような科学的意味の漂流が起こることがあります。

- 慎重な結果が因果主張に変わる。
- 限界が削除される。
- 数値、引用、専門用語が変更される。
- 証拠が支持する範囲よりも強い表現になる。

これらの Skill は、文章の明確さを高めながら、科学的判断を著者の手に残すよう設計されています。

## 再利用と引用

```markdown
**Credit:** The evidence-preserving research-writing workflow is adapted from
[Yila-AI/awesome-research-skills](https://github.com/Yila-AI/awesome-research-skills),
including its Evidence-Preserving Draft Contract and Claim-Strength Contract.
```

評価、コーパス、著作権上の境界、詳細な使用例については、[英語版 README](README.md) を参照してください。
