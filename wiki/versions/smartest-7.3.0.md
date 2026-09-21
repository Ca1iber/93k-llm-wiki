---
type: version
title: SmarTest 7.3.0 — 版本页
tags: [version, smartest]
related: []
sources:
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.06.03.07_PSSL_pogo_cable_assembly__pogo_pin_layout_and_model_file_configuration.md
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.06.03.10_HSM15_16G_pogo_cable_assembly_and_pogo_pin_layout.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.147_JSCF__JSCF__-__Jitter_Set_ConFiguration.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.148_JSDF__JSDF__-__Jitter_Set_DeFinition.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.162_MSCF__MSCF__-__Modulation_Set_ConFiguration.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.163_MSDF__MSDF__-__Modulation_Set_DeFinition.md
  - 02_System_reference/02.06_Command_Reference/02.06.03.01.03_Configuring_pin_type_and_operating_mode_for_a_context.md
  - 02_System_reference/02.06_Command_Reference/02.06.16.01.01_Two_ways_of_organizing_jitter_setup_data.md
  - 02_System_reference/02.06_Command_Reference/02.06.16.02.02_JSCF__JSCF__-__Jitter_Set_ConFiguration.md
  - 02_System_reference/02.06_Command_Reference/02.06.16.02.03_JSDF__JSDF__-__Jitter_Set_DeFinition.md
  - 02_System_reference/02.06_Command_Reference/02.06.16.02.07_MSCF__MSCF__-__Modulation_Set_ConFiguration.md
  - 02_System_reference/02.06_Command_Reference/02.06.16.02.08_MSDF__MSDF__-__Modulation_Set_DeFinition.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.122.01_JITTER_INJECTION_PINS.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.127_LOOPBACK_OPERATION_PINS.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.128_LOOPBACK_OPERATION_TASK.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.131_MODULATION_SET_TIMING.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# SmarTest 7.3.0

> **本页由 `extract/versions.py` 从 raw 的 `## Functional changes` 段落机械汇编**——分组、排序、出处都是脚本算的，**没有一句是模型写的**。
> 条目**原样转录**（含语料自己的措辞、大小写与错拼），本页不替它改。
>
> 因此本页只证明**「文档这么写」**，不证明**「机台这样」**（schema §11）。
> **本页没有被人在真实机台上核对过**（`verified: doc-only`）。

## 这一版改了什么（6 条）

格式：**出处文档 —— 语料原条目**。条目本身带 `SmarTest 7.3.0:` 前缀，**那是原文的一部分，没有去掉**。

- [JSCF, JSCF? - (Jitter Set ConFiguration)](<02_System_reference/02.06_Command_Reference/02.06.02.02.147_JSCF__JSCF__-__Jitter_Set_ConFiguration.md>) —— SmarTest 7.3.0: The MODULATION_SETS property was added.
- [JSDF, JSDF? - (Jitter Set DeFinition)](<02_System_reference/02.06_Command_Reference/02.06.02.02.148_JSDF__JSDF__-__Jitter_Set_DeFinition.md>) —— SmarTest 7.3.0: The jitter set can now be associated with a user defined mode context.
- [Configuring pin type and operating mode for a context](<02_System_reference/02.06_Command_Reference/02.06.03.01.03_Configuring_pin_type_and_operating_mode_for_a_context.md>) —— SmarTest 7.3.0: New operations modes were added for Pin Scale SL.
- [JSCF, JSCF? - (Jitter Set ConFiguration)](<02_System_reference/02.06_Command_Reference/02.06.16.02.02_JSCF__JSCF__-__Jitter_Set_ConFiguration.md>) —— SmarTest 7.3.0: The MODULATION_SETS property was added.
- [JSDF, JSDF? - (Jitter Set DeFinition)](<02_System_reference/02.06_Command_Reference/02.06.16.02.03_JSDF__JSDF__-__Jitter_Set_DeFinition.md>) —— SmarTest 7.3.0: The jitter set can now be associated with a user defined mode context.
- [JITTER_INJECTION_PINS](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.122.01_JITTER_INJECTION_PINS.md>) —— SmarTest 7.3.0: New member function linkModulationSet() for connecting a jitter set to a modulation set


## 这一版新引入（10 条）

语料原句是 `Introduced in …`，说的是「**这篇文档描述的东西从这一版开始有**」。条目短，所以**文档放前面、原句放后面**：

- [PSSL pogo cable assembly, pogo pin layout and model file configuration](<02_System_reference/02.03_DUT_board_design_reference/02.03.06.03.07_PSSL_pogo_cable_assembly__pogo_pin_layout_and_model_file_configuration.md>) —— Introduced in SmarTest 7.3.0
- [HSM15/16G pogo cable assembly and pogo pin layout](<02_System_reference/02.03_DUT_board_design_reference/02.03.06.03.10_HSM15_16G_pogo_cable_assembly_and_pogo_pin_layout.md>) —— Introduced in SmarTest 7.3.0
- [MSCF, MSCF? - (Modulation Set ConFiguration)](<02_System_reference/02.06_Command_Reference/02.06.02.02.162_MSCF__MSCF__-__Modulation_Set_ConFiguration.md>) —— Introduced in SmarTest 7.3.0
- [MSDF, MSDF? - (Modulation Set DeFinition)](<02_System_reference/02.06_Command_Reference/02.06.02.02.163_MSDF__MSDF__-__Modulation_Set_DeFinition.md>) —— Introduced in SmarTest 7.3.0
- [Two ways of organizing jitter setup data](<02_System_reference/02.06_Command_Reference/02.06.16.01.01_Two_ways_of_organizing_jitter_setup_data.md>) —— Introduced in SmarTest 7.3.0
- [MSCF, MSCF? - (Modulation Set ConFiguration)](<02_System_reference/02.06_Command_Reference/02.06.16.02.07_MSCF__MSCF__-__Modulation_Set_ConFiguration.md>) —— Introduced in SmarTest 7.3.0
- [MSDF, MSDF? - (Modulation Set DeFinition)](<02_System_reference/02.06_Command_Reference/02.06.16.02.08_MSDF__MSDF__-__Modulation_Set_DeFinition.md>) —— Introduced in SmarTest 7.3.0
- [LOOPBACK_OPERATION_PINS](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.127_LOOPBACK_OPERATION_PINS.md>) —— Introduced in SmarTest 7.3.0
- [LOOPBACK_OPERATION_TASK](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.128_LOOPBACK_OPERATION_TASK.md>) —— Introduced in SmarTest 7.3.0
- [MODULATION_SET_TIMING](<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.131_MODULATION_SET_TIMING.md>) —— Introduced in SmarTest 7.3.0


## 出处

- 抽取自 raw 的 `## Functional changes` 段落；**本页正文列出 16 条**，涉及 **16 篇**文档。
- 抽取器：`extract/versions.py`（纯脚本）；机器可读全量：`extract/version-facts.csv`。
- **本页没有逐篇回读 raw 原文**——条目是段落级抽取的结果。若要据此下结论，请点开对应出处链接核对。
