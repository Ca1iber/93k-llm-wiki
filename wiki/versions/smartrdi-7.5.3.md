---
type: version
title: SmartRDI 7.5.3 — 版本页
tags: [version, smartrdi]
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.04_RDI_Configure_file.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.03_Changing_the_parameter_value_at_runtime_with_SmartRDI.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.11.01_rdi.pureGenerationMode.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.14.01_getAnaResultHandle.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.09.01.01_Parameters_in_the_alarm_setup_file.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.09.02_Alarm_handling_commands.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.09_SmartRDI__Alarm_handling_for_DCVI.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.11.04.01_average.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.01_average.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.18_valueMode.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.01_average.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.16.06_FFV.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.16.18_rdi.id__.getFFV.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.19.02.02_pathPin.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.21.22_rdi.id__.getTmuFinished.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# SmartRDI 7.5.3

> **本页由 `extract/versions.py` 从 raw 的 `## Functional changes` 段落机械汇编**——分组、排序、出处都是脚本算的，**没有一句是模型写的**。
> 条目**原样转录**（含语料自己的措辞、大小写与错拼），本页不替它改。
>
> 因此本页只证明**「文档这么写」**，不证明**「机台这样」**（schema §11）。
> **本页没有被人在真实机台上核对过**（`verified: doc-only`）。

## 这一版改了什么（10 条）

格式：**出处文档 —— 语料原条目**。条目本身带 `SmartRDI 7.5.3:` 前缀，**那是原文的一部分，没有去掉**。

- [RDI_Configure file](<02_System_reference/02.07_Test_Method_Reference/02.07.13.04_RDI_Configure_file.md>) —— SmartRDI 7.5.3: New keywords FAST_PPMU_LEVEL_TRANSFER and ROUTING_ACK_CHECK.
- [Changing the parameter value at runtime with SmartRDI](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.03_Changing_the_parameter_value_at_runtime_with_SmartRDI.md>) —— SmartRDI 7.5.3: Support of the fast transfer mode for PPMU voltage levels.
- [Parameters in the alarm setup file](<02_System_reference/02.07_Test_Method_Reference/02.07.13.09.01.01_Parameters_in_the_alarm_setup_file.md>) —— SmartRDI 7.5.3: GlobalDisableAlarmIth and DisableAlarmIth to define a current threshold value for disabling alarm checks globally or per pin.
- [Alarm handling commands](<02_System_reference/02.07_Test_Method_Reference/02.07.13.09.02_Alarm_handling_commands.md>) —— SmartRDI 7.5.3: rdi.alarm().globalDisableAlarmIth(double) and rdi.alarm().pin(pinA).disableAlarmIth(double) to define a current threshold value for disabling alarm checks globally or per pin.
- [SmartRDI: Alarm handling for DCVI](<02_System_reference/02.07_Test_Method_Reference/02.07.13.09_SmartRDI__Alarm_handling_for_DCVI.md>) —— SmartRDI 7.5.3: Alarm checking can be disabled by current limits.
- [average()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.11.04.01_average.md>) —— SmartRDI 7.5.3: The default average values for PPMU and BADC are changed.
- [average()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.01_average.md>) —— SmartRDI 7.5.3: The default average values for PPMU and BADC are changed.
- [valueMode()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.18_valueMode.md>) —— SmartRDI 7.5.3: New value TA::PF_ONLY.
- [average()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.01_average.md>) —— SmartRDI 7.5.3: The default average values for PPMU and BADC are changed.
- [pathPin()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.19.02.02_pathPin.md>) —— SmartRDI 7.5.3: pathPin() is no longer required for retrieving binary and linear search results.


## 这一版新引入（5 条）

语料原句是 `Introduced in …`，说的是「**这篇文档描述的东西从这一版开始有**」。条目短，所以**文档放前面、原句放后面**：

- [rdi.pureGenerationMode()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.11.01_rdi.pureGenerationMode.md>) —— Introduced in SmartRDI 7.5.3
- [getAnaResultHandle()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.14.01_getAnaResultHandle.md>) —— Introduced in SmartRDI 7.5.3
- [FFV()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.16.06_FFV.md>) —— Introduced in SmartRDI 7.5.3
- [rdi.id().getFFV()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.16.18_rdi.id__.getFFV.md>) —— Introduced in SmartRDI 7.5.3
- [rdi.id().getTmuFinished()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.21.22_rdi.id__.getTmuFinished.md>) —— Introduced in SmartRDI 7.5.3


## 出处

- 抽取自 raw 的 `## Functional changes` 段落；**本页正文列出 15 条**，涉及 **15 篇**文档。
- 抽取器：`extract/versions.py`（纯脚本）；机器可读全量：`extract/version-facts.csv`。
- **本页没有逐篇回读 raw 原文**——条目是段落级抽取的结果。若要据此下结论，请点开对应出处链接核对。
