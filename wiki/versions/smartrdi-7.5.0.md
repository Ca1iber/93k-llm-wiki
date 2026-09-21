---
type: version
title: SmartRDI 7.5.0 — 版本页
tags: [version, smartrdi]
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.04_RDI_Configure_file.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.09.01.01_Parameters_in_the_alarm_setup_file.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.09.01.02_Limit_setup_of_alarm_checking.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.09.01_Alarm_setup_file.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.09.02.01_rdi.alarm__.applySet.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.09.02.02_rdi.alarm__.check__.execute.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.09.02.03_rdi.alarm__.enable.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.09.02.05_rdi.alarm__.pin__.enable.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.09.02.07_rdi.id__.getAlarmPassFail.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.09.02_Alarm_handling_commands.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.09_SmartRDI__Alarm_handling_for_DCVI.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.08_forceDropMax.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.16_iForce.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.18_iMeas.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.32_preCharge.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.35_restoreRange.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.36_returnDropMax.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.41_vForce.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.43_vMeas.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.46_vMeasReturnDrop.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02_Setting_up_DC_Scale_pins_with_SmartRDI.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.15.05.03_rdi.route__.enableOnlyActiveSites.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.16.08_multiFFC.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.16.19_rdi.id__.getMultiFFC.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.21.09_rdi.tmu__.measMode.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.21.13_rdi.tmu__.samples.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.21_SmartRDI__TMU_test_setup.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.24.24_multiFFC.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.24.46_rdi.id__.getMultiFFC.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13_SmartRDI.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# SmartRDI 7.5.0

> **本页由 `extract/versions.py` 从 raw 的 `## Functional changes` 段落机械汇编**——分组、排序、出处都是脚本算的，**没有一句是模型写的**。
> 条目**原样转录**（含语料自己的措辞、大小写与错拼），本页不替它改。
>
> 因此本页只证明**「文档这么写」**，不证明**「机台这样」**（schema §11）。
> **本页没有被人在真实机台上核对过**（`verified: doc-only`）。

## 这一版改了什么（14 条）

格式：**出处文档 —— 语料原条目**。条目本身带 `SmartRDI 7.5.0:` 前缀，**那是原文的一部分，没有去掉**。

- [RDI_Configure file](<02_System_reference/02.07_Test_Method_Reference/02.07.13.04_RDI_Configure_file.md>) —— SmartRDI 7.5.0: New keywords UTIL_PADDING_RPTV_FLAT, PMUX_CTRL_MAX_SPEED, ALARM_HANDLING_DCVI_ENABLE, and ALARM_HANDLING_DCVI_SETUP_FILE.
- [RDI_Configure file](<02_System_reference/02.07_Test_Method_Reference/02.07.13.04_RDI_Configure_file.md>) —— SmartRDI 7.5.0: New testflow variable RDI_CONFIGURE_FILE.
- [iForce()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.16_iForce.md>) —— SmartRDI 7.5.0: Spec variables can be added to DC events.
- [iMeas()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.18_iMeas.md>) —— SmartRDI 7.5.0: New syntax for "LAST" measurements of FVI16.
- [preCharge()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.32_preCharge.md>) —— SmartRDI 7.5.0: DC Scale FVI16 card added.
- [restoreRange()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.35_restoreRange.md>) —— SmartRDI 7.5.0: DC Scale FVI16 card added.
- [vForce()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.41_vForce.md>) —— SmartRDI 7.5.0: Spec variables can be added to DC events.
- [vMeas()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.43_vMeas.md>) —— SmartRDI 7.5.0: New syntax for "LAST" measurements of FVI16.
- [Setting up DC Scale pins with SmartRDI](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02_Setting_up_DC_Scale_pins_with_SmartRDI.md>) —— SmartRDI 7.5.0: New functions forceSenseLink(), vCompliance(), forceDropMax(), returnDropMax().
- [Setting up DC Scale pins with SmartRDI](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02_Setting_up_DC_Scale_pins_with_SmartRDI.md>) —— SmartRDI 7.5.0: New functions vMeasBattery(), vMeasForceDrop(), vMeasReturnDrop().
- [rdi.tmu().measMode()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.21.09_rdi.tmu__.measMode.md>) —— SmartRDI 7.5.0: FVI16 added.
- [rdi.tmu().samples()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.21.13_rdi.tmu__.samples.md>) —— SmartRDI 7.5.0: FVI16 added.
- [SmartRDI: TMU test setup](<02_System_reference/02.07_Test_Method_Reference/02.07.13.21_SmartRDI__TMU_test_setup.md>) —— SmartRDI 7.5.0: DC Scale FVI16 card added
- [SmartRDI](<02_System_reference/02.07_Test_Method_Reference/02.07.13_SmartRDI.md>) —— SmartRDI 7.5.0: DC Scale FVI16 card added.


## 这一版新引入（18 条）

语料原句是 `Introduced in …`，说的是「**这篇文档描述的东西从这一版开始有**」。条目短，所以**文档放前面、原句放后面**：

- [Parameters in the alarm setup file](<02_System_reference/02.07_Test_Method_Reference/02.07.13.09.01.01_Parameters_in_the_alarm_setup_file.md>) —— Introduced in SmartRDI 7.5.0
- [Limit setup of alarm checking](<02_System_reference/02.07_Test_Method_Reference/02.07.13.09.01.02_Limit_setup_of_alarm_checking.md>) —— Introduced in SmartRDI 7.5.0
- [Alarm setup file](<02_System_reference/02.07_Test_Method_Reference/02.07.13.09.01_Alarm_setup_file.md>) —— Introduced in SmartRDI 7.5.0
- [rdi.alarm().applySet()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.09.02.01_rdi.alarm__.applySet.md>) —— Introduced in SmartRDI 7.5.0
- [rdi.alarm().check().execute()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.09.02.02_rdi.alarm__.check__.execute.md>) —— Introduced in SmartRDI 7.5.0
- [rdi.alarm().enable()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.09.02.03_rdi.alarm__.enable.md>) —— Introduced in SmartRDI 7.5.0
- [rdi.alarm().pin().enable()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.09.02.05_rdi.alarm__.pin__.enable.md>) —— Introduced in SmartRDI 7.5.0
- [rdi.id().getAlarmPassFail()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.09.02.07_rdi.id__.getAlarmPassFail.md>) —— Introduced in SmartRDI 7.5.0
- [Alarm handling commands](<02_System_reference/02.07_Test_Method_Reference/02.07.13.09.02_Alarm_handling_commands.md>) —— Introduced in SmartRDI 7.5.0
- [SmartRDI: Alarm handling for DCVI](<02_System_reference/02.07_Test_Method_Reference/02.07.13.09_SmartRDI__Alarm_handling_for_DCVI.md>) —— Introduced in SmartRDI 7.5.0
- [forceDropMax()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.08_forceDropMax.md>) —— Introduced in SmartRDI 7.5.0
- [returnDropMax()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.36_returnDropMax.md>) —— Introduced in SmartRDI 7.5.0
- [vMeasReturnDrop()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.46_vMeasReturnDrop.md>) —— Introduced in SmartRDI 7.5.0
- [rdi.route().enableOnlyActiveSites()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.15.05.03_rdi.route__.enableOnlyActiveSites.md>) —— Introduced in SmartRDI 7.5.0
- [multiFFC()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.16.08_multiFFC.md>) —— Introduced in SmartRDI 7.5.0
- [rdi.id().getMultiFFC()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.16.19_rdi.id__.getMultiFFC.md>) —— Introduced in SmartRDI 7.5.0
- [multiFFC()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.24_multiFFC.md>) —— Introduced in SmartRDI 7.5.0
- [rdi.id().getMultiFFC()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.46_rdi.id__.getMultiFFC.md>) —— Introduced in SmartRDI 7.5.0


## 出处

- 抽取自 raw 的 `## Functional changes` 段落；**本页正文列出 32 条**，涉及 **30 篇**文档。
- 抽取器：`extract/versions.py`（纯脚本）；机器可读全量：`extract/version-facts.csv`。
- **本页没有逐篇回读 raw 原文**——条目是段落级抽取的结果。若要据此下结论，请点开对应出处链接核对。
