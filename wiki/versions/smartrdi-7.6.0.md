---
type: version
title: SmartRDI 7.6.0 — 版本页
tags: [version, smartrdi]
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.04_RDI_Configure_file.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.03.01_runTimeVal.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.12.01.01_Register_structure.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.12.01_Setting_up_the_Register_Access_library.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.12.02.01_I2C_protocol_class_template.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.12.02.02_JTAG_protocol_class_template.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.12.02.03_SPI_protocol_class_template.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.12.02.04.01_I2C_predefined_transactions.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.12.02.04.02_JTAG_predefined_transactions.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.12.02.04.03_SPI_predefined_transactions.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.12.02.04_Creating_a_protocol_class.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.12.02_Protocol_management.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.12.03.01_Register_access_execution_mode.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.12.03.02_Static_configurations.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.12.03.03_Automatic_speed_adaptation.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.12.03.04_Register_read.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.12.03.05_Register_compare.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.12.03.06_Register_write.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.12.03.07_Write_array.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.12.03.08_RA_debugging.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.12.03_Usage_of_register_operations_in_test_method.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.12_Register_Access_library.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.09.02.02_rdi.alarm__.check__.execute.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.46_vMeasReturnDrop.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.14.02_runTimeVal.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.16.10_rdi.func__.startVec.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.16.11_rdi.func__.stopVec.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.17.01.11_rdi.func__.startVec.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.17.01.12_rdi.func__.stopVec.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.19.02_Sequencer-controlled_searching_with_cogo.md
  # 本页共涉及 33 篇文档。上面只列了前 30 篇——**完整出处是正文每条后面的链接**，
  # 机器可读全量见 extract/version-facts.csv（按 doc 列筛）。**这是有意的截断，不是漏列。**
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# SmartRDI 7.6.0

> **本页由 `extract/versions.py` 从 raw 的 `## Functional changes` 段落机械汇编**——分组、排序、出处都是脚本算的，**没有一句是模型写的**。
> 条目**原样转录**（含语料自己的措辞、大小写与错拼），本页不替它改。
>
> 因此本页只证明**「文档这么写」**，不证明**「机台这样」**（schema §11）。
> **本页没有被人在真实机台上核对过**（`verified: doc-only`）。

## 这一版改了什么（12 条）

格式：**出处文档 —— 语料原条目**。条目本身带 `SmartRDI 7.6.0:` 前缀，**那是原文的一部分，没有去掉**。

- [RDI_Configure file](<02_System_reference/02.07_Test_Method_Reference/02.07.13.04_RDI_Configure_file.md>) —— SmartRDI 7.6.0: New keyword SMV_IGNORE_COMMENT.
- [runTimeVal()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.03.01_runTimeVal.md>) —— SmartRDI 7.6.0: For the hwRelay() class, "NO" (no change) is supported.
- [rdi.alarm().check().execute()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.09.02.02_rdi.alarm__.check__.execute.md>) —— SmartRDI 7.6.0: Alarm check per result ID.
- [vMeasReturnDrop()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.46_vMeasReturnDrop.md>) —— SmartRDI 7.6.0: DPS128-HC channels are supported.
- [runTimeVal()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.14.02_runTimeVal.md>) —— SmartRDI 7.6.0: For the hwRelay() class, "NO" (no change) is supported.
- [rdi.func().startVec()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.16.10_rdi.func__.startVec.md>) —— SmartRDI 7.6.0: startVec() and stopVec() support the emap() class.
- [rdi.func().stopVec()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.16.11_rdi.func__.stopVec.md>) —— SmartRDI 7.6.0: startVec() and stopVec() support the emap() class.
- [rdi.func().startVec()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.17.01.11_rdi.func__.startVec.md>) —— SmartRDI 7.6.0: startVec() and stopVec() support the emap() class.
- [rdi.func().stopVec()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.17.01.12_rdi.func__.stopVec.md>) —— SmartRDI 7.6.0: startVec() and stopVec() support the emap() class.
- [Sequencer-controlled searching with cogo](<02_System_reference/02.07_Test_Method_Reference/02.07.13.19.02_Sequencer-controlled_searching_with_cogo.md>) —— SmartRDI 7.6.0: Linear search is supported with one subroutine for all search steps.
- [Sequencer Controlled Utility Mask with SmartRDI](<02_System_reference/02.07_Test_Method_Reference/02.07.13.23.04_Sequencer_Controlled_Utility_Mask_with_SmartRDI.md>) —— SmartRDI 7.6.0: Wait time can be added to pins in Pin Configuration for sequencer‑controlled utility pattern.
- [comment()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.05_comment.md>) —— SmartRDI 7.6.0: SMV_IGNORE_COMMENT in the RDI_Configure file can be used to globally allow comments output in pattern.


## 这一版新引入（21 条）

语料原句是 `Introduced in …`，说的是「**这篇文档描述的东西从这一版开始有**」。条目短，所以**文档放前面、原句放后面**：

- [Register structure](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.12.01.01_Register_structure.md>) —— Introduced in SmartRDI 7.6.0
- [Setting up the Register Access library](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.12.01_Setting_up_the_Register_Access_library.md>) —— Introduced in SmartRDI 7.6.0
- [I2C protocol class template](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.12.02.01_I2C_protocol_class_template.md>) —— Introduced in SmartRDI 7.6.0
- [JTAG protocol class template](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.12.02.02_JTAG_protocol_class_template.md>) —— Introduced in SmartRDI 7.6.0
- [SPI protocol class template](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.12.02.03_SPI_protocol_class_template.md>) —— Introduced in SmartRDI 7.6.0
- [I2C predefined transactions](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.12.02.04.01_I2C_predefined_transactions.md>) —— Introduced in SmartRDI 7.6.0
- [JTAG predefined transactions](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.12.02.04.02_JTAG_predefined_transactions.md>) —— Introduced in SmartRDI 7.6.0
- [SPI predefined transactions](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.12.02.04.03_SPI_predefined_transactions.md>) —— Introduced in SmartRDI 7.6.0
- [Creating a protocol class](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.12.02.04_Creating_a_protocol_class.md>) —— Introduced in SmartRDI 7.6.0
- [Protocol management](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.12.02_Protocol_management.md>) —— Introduced in SmartRDI 7.6.0
- [Register access execution mode](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.12.03.01_Register_access_execution_mode.md>) —— Introduced in SmartRDI 7.6.0
- [Static configurations](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.12.03.02_Static_configurations.md>) —— Introduced in SmartRDI 7.6.0
- [Automatic speed adaptation](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.12.03.03_Automatic_speed_adaptation.md>) —— Introduced in SmartRDI 7.6.0
- [Register read](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.12.03.04_Register_read.md>) —— Introduced in SmartRDI 7.6.0
- [Register compare](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.12.03.05_Register_compare.md>) —— Introduced in SmartRDI 7.6.0
- [Register write](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.12.03.06_Register_write.md>) —— Introduced in SmartRDI 7.6.0
- [Write array](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.12.03.07_Write_array.md>) —— Introduced in SmartRDI 7.6.0
- [RA debugging](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.12.03.08_RA_debugging.md>) —— Introduced in SmartRDI 7.6.0
- [Usage of register operations in test method](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.12.03_Usage_of_register_operations_in_test_method.md>) —— Introduced in SmartRDI 7.6.0
- [Register Access library](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.12_Register_Access_library.md>) —— Introduced in SmartRDI 7.6.0
- [rdi.id().getTmuErrorState()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.21.21_rdi.id__.getTmuErrorState.md>) —— Introduced in SmartRDI 7.6.0


## 出处

- 抽取自 raw 的 `## Functional changes` 段落；**本页正文列出 33 条**，涉及 **33 篇**文档。
- 抽取器：`extract/versions.py`（纯脚本）；机器可读全量：`extract/version-facts.csv`。
- **本页没有逐篇回读 raw 原文**——条目是段落级抽取的结果。若要据此下结论，请点开对应出处链接核对。
