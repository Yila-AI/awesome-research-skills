# 근거 보존 연구 Agent Skills

[English](README.md) · [中文](README_CN.md) · [日本語](README_ja.md)

> **과학적 내용을 조용히 바꾸지 않고 연구를 기획·작성·교정·발표하도록 돕는 3개의 공식 Agent Skill입니다.**

**문장은 다듬되, 과학은 다시 쓰지 않습니다.** 이 오픈소스 툴킷은 연구 글쓰기 전 과정에서 의미, 데이터, 인용, 한계, 주장의 강도를 보존합니다.

Codex, Claude Code 및 재사용 가능한 Skill 지시를 지원하는 다른 Agent에서 사용할 수 있습니다. 이 한국어 페이지는 핵심 요약본이며, 상세 문서는 영어와 중국어로 관리됩니다.

## Skill 선택

| Skill | 사용할 때 | 제공 결과 |
|---|---|---|
| [`science-research-writing`](skills/science-research-writing/SKILL.md) | 아이디어, 메모, 데이터, 문헌 또는 미완성 초고로 시작할 때 | 근거에 기반한 계획, 섹션 초고, 개정 또는 원고 감사 |
| [`sci-ssci-polishing`](skills/sci-ssci-polishing/SKILL.md) | 중국어 학술 문장을 영어로 번역하거나 영문 원고를 충실하게 교정할 때 | 투고용 학술 영어와 보존 감사 |
| [`research-presentation`](skills/research-presentation/SKILL.md) | 논문이나 연구 결과를 슬라이드로 만들 때 | 편집 가능하고 출처에 기반한 덱 계획, 발표자 노트, 출처 맵, 시각 QA |

## 30초 설치

설치 도구는 Node.js 18 이상이 필요합니다. 필요한 Skill 하나를 선택하세요.

```bash
# 논문 기획, 작성, 개정 또는 감사
npx skills add Yila-AI/awesome-research-skills --global --agent codex --skill science-research-writing --yes --copy

# 기존 원고 번역 또는 교정
npx skills add Yila-AI/awesome-research-skills --global --agent codex --skill sci-ssci-polishing --yes --copy

# 논문이나 연구 결과를 학술 발표로 변환
npx skills add Yila-AI/awesome-research-skills --global --agent codex --skill research-presentation --yes --copy
```

`npx skills add Yila-AI/awesome-research-skills --list`로 설치 가능한 모든 Skill을 확인할 수 있습니다.

## 바로 사용하기

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

## 왜 필요한가

AI를 활용한 학술 편집에서는 문장이 더 자연스러워지는 동안 다음과 같은 과학적 의미의 표류가 생길 수 있습니다.

- 신중한 결과가 인과적 주장으로 바뀌는 경우
- 연구의 한계가 사라지는 경우
- 숫자, 인용 또는 전문 용어가 변경되는 경우
- 문장이 근거가 지지하는 범위보다 강해지는 경우

이 Skill들은 문장의 명확성을 높이면서도 최종 학술적 판단을 저자에게 남겨 두도록 설계되었습니다.

## 재사용과 인용

```markdown
**Credit:** The evidence-preserving research-writing workflow is adapted from
[Yila-AI/awesome-research-skills](https://github.com/Yila-AI/awesome-research-skills),
including its Evidence-Preserving Draft Contract and Claim-Strength Contract.
```

평가, 코퍼스, 저작권 경계 및 상세한 사용 예시는 [영어 README](README.md)를 참고하세요.
