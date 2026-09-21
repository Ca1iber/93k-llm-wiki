---
type: version
title: SmartRDI 2.4.1 — 版本页
tags: [version, smartrdi]
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.04_RDI_Configure_file.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.03_Changing_the_parameter_value_at_runtime_with_SmartRDI.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.17.01_addPort.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.17.02_syncGroup.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.17_Sync_group_support_with_SmartRDI.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.06_firstRunInLoop.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.10_insertSub.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.13_limit.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.02.05_firstRunInLoop.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.02.07_limit.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.20_insertSub.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.25_limit.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.13.10_format.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.13.17_vecVarOnly.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.19_SmartRDI__Pattern-based_conditional_jump_-_cogo.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.24.49.01.01_instruction.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.24.49.02.03_matchData.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# SmartRDI 2.4.1

> **本页由 `extract/versions.py` 从 raw 的 `## Functional changes` 段落机械汇编**——分组、排序、出处都是脚本算的，**没有一句是模型写的**。
> 条目**原样转录**（含语料自己的措辞、大小写与错拼），本页不替它改。
>
> 因此本页只证明**「文档这么写」**，不证明**「机台这样」**（schema §11）。
> **本页没有被人在真实机台上核对过**（`verified: doc-only`）。

## 这一版改了什么（8 条）

格式：**出处文档 —— 语料原条目**。条目本身带 `SmartRDI 2.4.1:` 前缀，**那是原文的一部分，没有去掉**。

- [RDI_Configure file](<02_System_reference/02.07_Test_Method_Reference/02.07.13.04_RDI_Configure_file.md>) —— SmartRDI 2.4.1: New keywords PER_LABEL_FUNC_RESULT_MODE and SMV_VEC_MEM_TYPE.
- [Changing the parameter value at runtime with SmartRDI](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.03_Changing_the_parameter_value_at_runtime_with_SmartRDI.md>) —— SmartRDI 2.4.1: Support iClamp() in DC tests.
- [limit()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.13_limit.md>) —— SmartRDI 2.4.1: One new option TA::NO_LIMIT only for DC Scale pins.
- [limit()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.02.07_limit.md>) —— SmartRDI 2.4.1: One new option TA::NO_LIMIT only for DC Scale pins.
- [limit()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.25_limit.md>) —— SmartRDI 2.4.1: One new option TA::NO_LIMIT only for DC Scale pins.
- [SmartRDI: Pattern-based conditional jump - cogo](<02_System_reference/02.07_Test_Method_Reference/02.07.13.19_SmartRDI__Pattern-based_conditional_jump_-_cogo.md>) —— SmartRDI 2.4.1: The cogo judgment supports DC Scale cards.
- [instruction()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.49.01.01_instruction.md>) —— SmartRDI 2.4.1: A new option for the MACT instruction: CONTINUE.
- [matchData()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.49.02.03_matchData.md>) —— SmartRDI 2.4.1: Support a CONTINUE option for the MACT instruction: MATCH_CONT.


## 这一版新引入（9 条）

语料原句是 `Introduced in …`，说的是「**这篇文档描述的东西从这一版开始有**」。条目短，所以**文档放前面、原句放后面**：

- [addPort()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.17.01_addPort.md>) —— Introduced in SmartRDI 2.4.1
- [syncGroup()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.17.02_syncGroup.md>) —— Introduced in SmartRDI 2.4.1
- [Sync group support with SmartRDI](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.17_Sync_group_support_with_SmartRDI.md>) —— Introduced in SmartRDI 2.4.1
- [firstRunInLoop()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.06_firstRunInLoop.md>) —— Introduced in SmartRDI 2.4.1
- [insertSub()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.10_insertSub.md>) —— Introduced in SmartRDI 2.4.1
- [firstRunInLoop()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.02.05_firstRunInLoop.md>) —— Introduced in SmartRDI 2.4.1
- [insertSub()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.20_insertSub.md>) —— Introduced in SmartRDI 2.4.1
- [format()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.10_format.md>) —— Introduced in SmartRDI 2.4.1
- [vecVarOnly()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.17_vecVarOnly.md>) —— Introduced in SmartRDI 2.4.1


## 出处

- 抽取自 raw 的 `## Functional changes` 段落；**本页正文列出 17 条**，涉及 **17 篇**文档。
- 抽取器：`extract/versions.py`（纯脚本）；机器可读全量：`extract/version-facts.csv`。
- **本页没有逐篇回读 raw 原文**——条目是段落级抽取的结果。若要据此下结论，请点开对应出处链接核对。
