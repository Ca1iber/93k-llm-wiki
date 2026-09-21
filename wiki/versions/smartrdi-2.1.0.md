---
type: version
title: SmartRDI 2.1.0 — 版本页
tags: [version, smartrdi]
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.02_Installing_and_using_SmartRDI.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.04_RDI_Configure_file.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.05.01_Basic_rules_for_SmartRDI.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.05.02_Multiport_programming_with_SmartRDI.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.05_Code_structure_with_SmartRDI.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.01.02_execute.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.01.04_RDI_BEGIN.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.01.05_RDI_END.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.01.06_RDI_INIT.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.01.07_RDI_UNIT_INIT.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.02.01_clearPinStatus.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.02.02_setPinStatus.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.02_Changing_the_default_pin_status_with_SmartRDI.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.03.01_runTimeVal.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.03_Changing_the_parameter_value_at_runtime_with_SmartRDI.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.08.01_port.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.08.02_portSync.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.08.03_RDI_PORT_BEGIN.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.08.04_RDI_PORT_END.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.14.02_getAnaSet.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.14.03_getPriAnaSet.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.14.04_setAnaSet.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.14.05_setPatBurst.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.14_Setting_and_retrieving_the_setup_name_with_SmartRDI.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.19.01_Using_hidden_upload_with_SmartRDI.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.19.02.03_rdi.hiddenUpload.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.21.01_wait.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.21.02_waitCycle.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08_SmartRDI__General_topics_and_functions.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.10.01_RDI_protocol_template.md
  # 本页共涉及 135 篇文档。上面只列了前 30 篇——**完整出处是正文每条后面的链接**，
  # 机器可读全量见 extract/version-facts.csv（按 doc 列筛）。**这是有意的截断，不是漏列。**
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# SmartRDI 2.1.0

> **本页由 `extract/versions.py` 从 raw 的 `## Functional changes` 段落机械汇编**——分组、排序、出处都是脚本算的，**没有一句是模型写的**。
> 条目**原样转录**（含语料自己的措辞、大小写与错拼），本页不替它改。
>
> 因此本页只证明**「文档这么写」**，不证明**「机台这样」**（schema §11）。
> **本页没有被人在真实机台上核对过**（`verified: doc-only`）。

## 这一版新引入（135 条）

语料原句是 `Introduced in …`，说的是「**这篇文档描述的东西从这一版开始有**」。条目短，所以**文档放前面、原句放后面**：

- [Installing and using SmartRDI](<02_System_reference/02.07_Test_Method_Reference/02.07.13.02_Installing_and_using_SmartRDI.md>) —— Introduced in SmartRDI 2.1.0
- [RDI_Configure file](<02_System_reference/02.07_Test_Method_Reference/02.07.13.04_RDI_Configure_file.md>) —— Introduced in SmartRDI 2.1.0
- [Basic rules for SmartRDI](<02_System_reference/02.07_Test_Method_Reference/02.07.13.05.01_Basic_rules_for_SmartRDI.md>) —— Introduced in SmartRDI 2.1.0
- [Multiport programming with SmartRDI](<02_System_reference/02.07_Test_Method_Reference/02.07.13.05.02_Multiport_programming_with_SmartRDI.md>) —— Introduced in SmartRDI 2.1.0
- [Code structure with SmartRDI](<02_System_reference/02.07_Test_Method_Reference/02.07.13.05_Code_structure_with_SmartRDI.md>) —— Introduced in SmartRDI 2.1.0
- [execute()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.01.02_execute.md>) —— Introduced in SmartRDI 2.1.0
- [RDI_BEGIN()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.01.04_RDI_BEGIN.md>) —— Introduced in SmartRDI 2.1.0
- [RDI_END()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.01.05_RDI_END.md>) —— Introduced in SmartRDI 2.1.0
- [RDI_INIT()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.01.06_RDI_INIT.md>) —— Introduced in SmartRDI 2.1.0
- [RDI_UNIT_INIT()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.01.07_RDI_UNIT_INIT.md>) —— Introduced in SmartRDI 2.1.0
- [clearPinStatus()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.02.01_clearPinStatus.md>) —— Introduced in SmartRDI 2.1.0
- [setPinStatus()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.02.02_setPinStatus.md>) —— Introduced in SmartRDI 2.1.0
- [Changing the default pin status with SmartRDI](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.02_Changing_the_default_pin_status_with_SmartRDI.md>) —— Introduced in SmartRDI 2.1.0
- [runTimeVal()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.03.01_runTimeVal.md>) —— Introduced in SmartRDI 2.1.0
- [Changing the parameter value at runtime with SmartRDI](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.03_Changing_the_parameter_value_at_runtime_with_SmartRDI.md>) —— Introduced in SmartRDI 2.1.0
- [port()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.08.01_port.md>) —— Introduced in SmartRDI 2.1.0
- [portSync()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.08.02_portSync.md>) —— Introduced in SmartRDI 2.1.0
- [RDI_PORT_BEGIN()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.08.03_RDI_PORT_BEGIN.md>) —— Introduced in SmartRDI 2.1.0
- [RDI_PORT_END()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.08.04_RDI_PORT_END.md>) —— Introduced in SmartRDI 2.1.0
- [getAnaSet()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.14.02_getAnaSet.md>) —— Introduced in SmartRDI 2.1.0
- [getPriAnaSet()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.14.03_getPriAnaSet.md>) —— Introduced in SmartRDI 2.1.0
- [setAnaSet()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.14.04_setAnaSet.md>) —— Introduced in SmartRDI 2.1.0
- [setPatBurst()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.14.05_setPatBurst.md>) —— Introduced in SmartRDI 2.1.0
- [Setting and retrieving the setup name with SmartRDI](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.14_Setting_and_retrieving_the_setup_name_with_SmartRDI.md>) —— Introduced in SmartRDI 2.1.0
- [Using hidden upload with SmartRDI](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.19.01_Using_hidden_upload_with_SmartRDI.md>) —— Introduced in SmartRDI 2.1.0
- [rdi.hiddenUpload()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.19.02.03_rdi.hiddenUpload.md>) —— Introduced in SmartRDI 2.1.0
- [wait()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.21.01_wait.md>) —— Introduced in SmartRDI 2.1.0
- [waitCycle()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.21.02_waitCycle.md>) —— Introduced in SmartRDI 2.1.0
- [SmartRDI: General topics and functions](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08_SmartRDI__General_topics_and_functions.md>) —— Introduced in SmartRDI 2.1.0
- [RDI protocol template](<02_System_reference/02.07_Test_Method_Reference/02.07.13.10.01_RDI_protocol_template.md>) —— Introduced in SmartRDI 2.1.0
- [pname()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.10.02_pname.md>) —— Introduced in SmartRDI 2.1.0
- [read()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.10.03_read.md>) —— Introduced in SmartRDI 2.1.0
- [readExpect()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.10.04_readExpect.md>) —— Introduced in SmartRDI 2.1.0
- [regNum()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.10.05_regNum.md>) —— Introduced in SmartRDI 2.1.0
- [write()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.10.06_write.md>) —— Introduced in SmartRDI 2.1.0
- [getData()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.10.08_getData.md>) —— Introduced in SmartRDI 2.1.0
- [getDataStream()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.10.09_getDataStream.md>) —— Introduced in SmartRDI 2.1.0
- [getPassFail()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.10.10_getPassFail.md>) —— Introduced in SmartRDI 2.1.0
- [SmartRDI: d2s-like protocol test setup](<02_System_reference/02.07_Test_Method_Reference/02.07.13.10_SmartRDI__d2s-like_protocol_test_setup.md>) —— Introduced in SmartRDI 2.1.0
- [FS()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.11.01.02_FS.md>) —— Introduced in SmartRDI 2.1.0
- [waveform()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.11.01.07_waveform.md>) —— Introduced in SmartRDI 2.1.0
- [Using a DC resource as an AWG with SmartRDI](<02_System_reference/02.07_Test_Method_Reference/02.07.13.11.01_Using_a_DC_resource_as_an_AWG_with_SmartRDI.md>) —— Introduced in SmartRDI 2.1.0
- [average()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.11.04.01_average.md>) —— Introduced in SmartRDI 2.1.0
- [capMode()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.11.04.02_capMode.md>) —— Introduced in SmartRDI 2.1.0
- [FS()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.11.04.03_FS.md>) —— Introduced in SmartRDI 2.1.0
- [samples()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.11.04.06_samples.md>) —— Introduced in SmartRDI 2.1.0
- [getWaveform()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.11.04.09_getWaveform.md>) —— Introduced in SmartRDI 2.1.0
- [Using a DC resource as a digitizer with SmartRDI](<02_System_reference/02.07_Test_Method_Reference/02.07.13.11.04_Using_a_DC_resource_as_a_digitizer_with_SmartRDI.md>) —— Introduced in SmartRDI 2.1.0
- [SmartRDI: DC resource AWG/DGT usage](<02_System_reference/02.07_Test_Method_Reference/02.07.13.11_SmartRDI__DC_resource_AWG_DGT_usage.md>) —— Introduced in SmartRDI 2.1.0
- [average()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.01_average.md>) —— Introduced in SmartRDI 2.1.0
- [clamp()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.02_clamp.md>) —— Introduced in SmartRDI 2.1.0
- [iForce()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.08_iForce.md>) —— Introduced in SmartRDI 2.1.0
- [iMeas()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.09_iMeas.md>) —— Introduced in SmartRDI 2.1.0
- [iRange()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.11_iRange.md>) —— Introduced in SmartRDI 2.1.0
- [measWait()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.14_measWait.md>) —— Introduced in SmartRDI 2.1.0
- [pin()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.15_pin.md>) —— Introduced in SmartRDI 2.1.0
- [relay()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.17_relay.md>) —— Introduced in SmartRDI 2.1.0
- [valueMode()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.18_valueMode.md>) —— Introduced in SmartRDI 2.1.0
- [vForce()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.19_vForce.md>) —— Introduced in SmartRDI 2.1.0
- [vMeas()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.20_vMeas.md>) —— Introduced in SmartRDI 2.1.0
- [getValue()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.23_getValue.md>) —— Introduced in SmartRDI 2.1.0
- [Setting up PPMU with SmartRDI](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01_Setting_up_PPMU_with_SmartRDI.md>) —— Introduced in SmartRDI 2.1.0
- [average()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.02.02_average.md>) —— Introduced in SmartRDI 2.1.0
- [measWait()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.02.08_measWait.md>) —— Introduced in SmartRDI 2.1.0
- [pin()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.02.09_pin.md>) —— Introduced in SmartRDI 2.1.0
- [vMeas()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.02.12_vMeas.md>) —— Introduced in SmartRDI 2.1.0
- [getValue()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.02.13_getValue.md>) —— Introduced in SmartRDI 2.1.0
- [Setting up Board ADC with SmartRDI](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.02_Setting_up_Board_ADC_with_SmartRDI.md>) —— Introduced in SmartRDI 2.1.0
- [average()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.03.01_average.md>) —— Introduced in SmartRDI 2.1.0
- [clamp()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.03.02_clamp.md>) —— Introduced in SmartRDI 2.1.0
- [connect()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.03.03_connect.md>) —— Introduced in SmartRDI 2.1.0
- [disconnect()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.03.04_disconnect.md>) —— Introduced in SmartRDI 2.1.0
- [iMeas()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.03.06_iMeas.md>) —— Introduced in SmartRDI 2.1.0
- [iRange()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.03.08_iRange.md>) —— Introduced in SmartRDI 2.1.0
- [measWait()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.03.09_measWait.md>) —— Introduced in SmartRDI 2.1.0
- [pin()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.03.10_pin.md>) —— Introduced in SmartRDI 2.1.0
- [relay()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.03.11_relay.md>) —— Introduced in SmartRDI 2.1.0
- [vForce()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.03.12_vForce.md>) —— Introduced in SmartRDI 2.1.0
- [vMeas()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.03.13_vMeas.md>) —— Introduced in SmartRDI 2.1.0
- [getValue()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.03.14_getValue.md>) —— Introduced in SmartRDI 2.1.0
- [Setting up SPMU with SmartRDI](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.03_Setting_up_SPMU_with_SmartRDI.md>) —— Introduced in SmartRDI 2.1.0
- [DC test with digital channels](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01_DC_test_with_digital_channels.md>) —— Introduced in SmartRDI 2.1.0
- [average()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.01_average.md>) —— Introduced in SmartRDI 2.1.0
- [clamp()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.02_clamp.md>) —— Introduced in SmartRDI 2.1.0
- [connect()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.03_connect.md>) —— Introduced in SmartRDI 2.1.0
- [connectSense()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.04_connectSense.md>) —— Introduced in SmartRDI 2.1.0
- [disconnect()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.06_disconnect.md>) —— Introduced in SmartRDI 2.1.0
- [iForce()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.16_iForce.md>) —— Introduced in SmartRDI 2.1.0
- [iForceRange()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.17_iForceRange.md>) —— Introduced in SmartRDI 2.1.0
- [iMeas()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.18_iMeas.md>) —— Introduced in SmartRDI 2.1.0
- [iMeasRange()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.19_iMeasRange.md>) —— Introduced in SmartRDI 2.1.0
- [measWait()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.29_measWait.md>) —— Introduced in SmartRDI 2.1.0
- [pin()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.30_pin.md>) —— Introduced in SmartRDI 2.1.0
- [relay()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.34_relay.md>) —— Introduced in SmartRDI 2.1.0
- [restoreRange()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.35_restoreRange.md>) —— Introduced in SmartRDI 2.1.0
- [ungang()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.38_ungang.md>) —— Introduced in SmartRDI 2.1.0
- [vForce()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.41_vForce.md>) —— Introduced in SmartRDI 2.1.0
- [vForceRange()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.42_vForceRange.md>) —— Introduced in SmartRDI 2.1.0
- [vMeas()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.43_vMeas.md>) —— Introduced in SmartRDI 2.1.0
- [vMeasRange()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.45_vMeasRange.md>) —— Introduced in SmartRDI 2.1.0
- [getValue()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.51_getValue.md>) —— Introduced in SmartRDI 2.1.0
- [Setting up DC Scale pins with SmartRDI](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02_Setting_up_DC_Scale_pins_with_SmartRDI.md>) —— Introduced in SmartRDI 2.1.0
- [SmartRDI: DC test setup](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12_SmartRDI__DC_test_setup.md>) —— Introduced in SmartRDI 2.1.0
- [Generating a new digital capture pattern with SmartRDI](<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.01_Generating_a_new_digital_capture_pattern_with_SmartRDI.md>) —— Introduced in SmartRDI 2.1.0
- [Inserting digital capture actions in an existing pattern with SmartRDI](<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.02_Inserting_digital_capture_actions_in_an_existing_pattern_with_SmartRDI.md>) —— Introduced in SmartRDI 2.1.0
- [addVecRange()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.04_addVecRange.md>) —— Introduced in SmartRDI 2.1.0
- [bitPerWord()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.05_bitPerWord.md>) —— Introduced in SmartRDI 2.1.0
- [capMode()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.07_capMode.md>) —— Introduced in SmartRDI 2.1.0
- [initDiscard()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.11_initDiscard.md>) —— Introduced in SmartRDI 2.1.0
- [interSkip()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.12_interSkip.md>) —— Introduced in SmartRDI 2.1.0
- [label()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.13_label.md>) —— Introduced in SmartRDI 2.1.0
- [pin()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.14_pin.md>) —— Introduced in SmartRDI 2.1.0
- [samples()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.15_samples.md>) —— Introduced in SmartRDI 2.1.0
- [getVector()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.18_getVector.md>) —— Introduced in SmartRDI 2.1.0
- [getVectorBit()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.19_getVectorBit.md>) —— Introduced in SmartRDI 2.1.0
- [getVecVar()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.21_getVecVar.md>) —— Introduced in SmartRDI 2.1.0
- [SmartRDI: Digital capture test setup](<02_System_reference/02.07_Test_Method_Reference/02.07.13.13_SmartRDI__Digital_capture_test_setup.md>) —— Introduced in SmartRDI 2.1.0
- [pin()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.14.01_pin.md>) —— Introduced in SmartRDI 2.1.0
- [runTimeVal()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.14.02_runTimeVal.md>) —— Introduced in SmartRDI 2.1.0
- [setOff()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.14.03_setOff.md>) —— Introduced in SmartRDI 2.1.0
- [setOn()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.14.05_setOn.md>) —— Introduced in SmartRDI 2.1.0
- [SmartRDI: Digital channel relay control](<02_System_reference/02.07_Test_Method_Reference/02.07.13.14_SmartRDI__Digital_channel_relay_control.md>) —— Introduced in SmartRDI 2.1.0
- [rdi.func().burst()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.17.01.01_rdi.func__.burst.md>) —— Introduced in SmartRDI 2.1.0
- [rdi.func().label()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.17.01.05_rdi.func__.label.md>) —— Introduced in SmartRDI 2.1.0
- [rdi.getBurstPassFail()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.17.01.13_rdi.getBurstPassFail.md>) —— Introduced in SmartRDI 2.1.0
- [rdi.id().getPassFail()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.17.01.19_rdi.id__.getPassFail.md>) —— Introduced in SmartRDI 2.1.0
- [Functional test setup](<02_System_reference/02.07_Test_Method_Reference/02.07.13.17_Functional_test_setup.md>) —— Introduced in SmartRDI 2.1.0
- [set()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.18.01_set.md>) —— Introduced in SmartRDI 2.1.0
- [SmartRDI: Level and timing set changes](<02_System_reference/02.07_Test_Method_Reference/02.07.13.18_SmartRDI__Level_and_timing_set_changes.md>) —— Introduced in SmartRDI 2.1.0
- [rdi.id().getPassFail()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.21.18_rdi.id__.getPassFail.md>) —— Introduced in SmartRDI 2.1.0
- [pin()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.23.01_pin.md>) —— Introduced in SmartRDI 2.1.0
- [setOff()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.23.02_setOff.md>) —— Introduced in SmartRDI 2.1.0
- [setOn()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.23.03_setOn.md>) —— Introduced in SmartRDI 2.1.0
- [SmartRDI: Utility lines control](<02_System_reference/02.07_Test_Method_Reference/02.07.13.23_SmartRDI__Utility_lines_control.md>) —— Introduced in SmartRDI 2.1.0
- [SmartRDI](<02_System_reference/02.07_Test_Method_Reference/02.07.13_SmartRDI.md>) —— Introduced in SmartRDI 2.1.0


## 出处

- 抽取自 raw 的 `## Functional changes` 段落；**本页正文列出 135 条**，涉及 **135 篇**文档。
- 抽取器：`extract/versions.py`（纯脚本）；机器可读全量：`extract/version-facts.csv`。
- **本页没有逐篇回读 raw 原文**——条目是段落级抽取的结果。若要据此下结论，请点开对应出处链接核对。
