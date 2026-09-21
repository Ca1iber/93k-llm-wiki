---
type: version
title: SmartRDI 7.10.3 — 版本页
tags: [version, smartrdi]
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.04_RDI_Configure_file.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.01.03_id.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.07.01_Automatic_masking_on_inactive_sites.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.07.02_Active_site_on_hold.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.07_Site_masking.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.09.02.04_rdi.alarm__.getEnabledPins.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.09.02.06_rdi.id__.getAlarmBurstValue.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.09.02.08_rdi.id__.getAlarmPassFailPerId.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.09.02.09_rdi.id__.getAlarmValue.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.09.02_Alarm_handling_commands.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.09_SmartRDI__Alarm_handling_for_DCVI.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.11.01.01_addWaveform.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.11.01.07_waveform.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.04_PS5000_MSET_timing.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.21.19_rdi.id__.getPropDelay.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# SmartRDI 7.10.3

> **本页由 `extract/versions.py` 从 raw 的 `## Functional changes` 段落机械汇编**——分组、排序、出处都是脚本算的，**没有一句是模型写的**。
> 条目**原样转录**（含语料自己的措辞、大小写与错拼），本页不替它改。
>
> 因此本页只证明**「文档这么写」**，不证明**「机台这样」**（schema §11）。
> **本页没有被人在真实机台上核对过**（`verified: doc-only`）。

## 这一版改了什么（4 条）

格式：**出处文档 —— 语料原条目**。条目本身带 `SmartRDI 7.10.3:` 前缀，**那是原文的一部分，没有去掉**。

- [RDI_Configure file](<02_System_reference/02.07_Test_Method_Reference/02.07.13.04_RDI_Configure_file.md>) —— SmartRDI 7.10.3: New keyword INACTIVE_SITE_AUTO_MASK; "-" character can be used in the UTIL_BLOCK definition.
- [id()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.01.03_id.md>) —— SmartRDI 7.10.3: 1000000 measurements result IDs are supported.
- [Alarm handling commands](<02_System_reference/02.07_Test_Method_Reference/02.07.13.09.02_Alarm_handling_commands.md>) —— SmartRDI 7.10.3: getAlarmBurstValue(), getAlarmPassFailPerID(), getAlarmValue(), and getEnabledPins()
- [waveform()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.11.01.07_waveform.md>) —— SmartRDI 7.10.3: RDI can automatically change the force mode for digital DC waveform.


## 这一版新引入（11 条）

语料原句是 `Introduced in …`，说的是「**这篇文档描述的东西从这一版开始有**」。条目短，所以**文档放前面、原句放后面**：

- [Automatic masking on inactive sites](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.07.01_Automatic_masking_on_inactive_sites.md>) —— Introduced in SmartRDI 7.10.3
- [Active site on hold](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.07.02_Active_site_on_hold.md>) —— Introduced in SmartRDI 7.10.3
- [Site masking](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.07_Site_masking.md>) —— Introduced in SmartRDI 7.10.3
- [rdi.alarm().getEnabledPins()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.09.02.04_rdi.alarm__.getEnabledPins.md>) —— Introduced in SmartRDI 7.10.3
- [rdi.id().getAlarmBurstValue()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.09.02.06_rdi.id__.getAlarmBurstValue.md>) —— Introduced in SmartRDI 7.10.3
- [rdi.id().getAlarmPassFailPerId()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.09.02.08_rdi.id__.getAlarmPassFailPerId.md>) —— Introduced in SmartRDI 7.10.3
- [rdi.id().getAlarmValue()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.09.02.09_rdi.id__.getAlarmValue.md>) —— Introduced in SmartRDI 7.10.3
- [SmartRDI: Alarm handling for DCVI](<02_System_reference/02.07_Test_Method_Reference/02.07.13.09_SmartRDI__Alarm_handling_for_DCVI.md>) —— Introduced in SmartRDI 7.10.3
- [addWaveform()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.11.01.01_addWaveform.md>) —— Introduced in SmartRDI 7.10.3
- [PS5000 MSET timing](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.04_PS5000_MSET_timing.md>) —— Introduced in SmartRDI 7.10.3
- [rdi.id().getPropDelay()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.21.19_rdi.id__.getPropDelay.md>) —— Introduced in SmartRDI 7.10.3


## 出处

- 抽取自 raw 的 `## Functional changes` 段落；**本页正文列出 15 条**，涉及 **15 篇**文档。
- 抽取器：`extract/versions.py`（纯脚本）；机器可读全量：`extract/version-facts.csv`。
- **本页没有逐篇回读 raw 原文**——条目是段落级抽取的结果。若要据此下结论，请点开对应出处链接核对。
