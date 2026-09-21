---
type: version
title: MTP 3.1.5 — 版本页
tags: [version, mtp]
related: []
sources:
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.09.03_Driver_Sharing_APIs.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.09.08_SharedContinuity_test_method.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.09.11_SharedLeakageParallel_test_method.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.09.12_SharedLeakageParallel_syntax.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.09.13_SharedIDD_test_method.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.02.05.01_apgc_command_syntax.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.02.01_APG_pattern_file_syntax.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.02_FOR_EACH_SHARED_SITE_BEGIN.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.03_FOR_EACH_SHARED_SITE_END.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.04_FOR_EACH_TEST_BEGIN.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.05_FOR_EACH_TEST_BEGIN_WITH_RESET.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.06_FOR_EACH_TEST_END.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.07_GET_CURRENT_UTILITY_CONTROL.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.08_GET_SITES_UNDER_TEST.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.10.01.01_MTP_CONTINUITY_PIN_TASK.iForce.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.10.01.02_MTP_CONTINUITY_PIN_TASK.vForce.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.10.01.03_MTP_CONTINUITY_PIN_TASK.limits.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.10.01.04_MTP_CONTINUITY_PIN_TASK.deviceSupply.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.10.01.05_MTP_CONTINUITY_PIN_TASK.forceSupply.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.10.01_MTP_CONTINUITY_PIN_TASK.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.10.02_MTP_CONTINUITY_TASK.pin.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.10.03_MTP_CONTINUITY_TASK.settlingTime.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.10.04_MTP_CONTINUITY_TASK.execute.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.10.05_MTP_CONTINUITY_TASK.postExecute.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.10.06_MTP_CONTINUITY_TASK.getPassFail.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.10.07_MTP_CONTINUITY_TASK.getValue.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.10_MTP_CONTINUITY_TASK.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.11.01_MTP_DPS_MEASURE.pin.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.11.02_MTP_DPS_MEASURE.execMode.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.11.03_MTP_DPS_MEASURE.samples.md
  # 本页共涉及 92 篇文档。上面只列了前 30 篇——**完整出处是正文每条后面的链接**，
  # 机器可读全量见 extract/version-facts.csv（按 doc 列筛）。**这是有意的截断，不是漏列。**
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# MTP 3.1.5

> **本页由 `extract/versions.py` 从 raw 的 `## Functional changes` 段落机械汇编**——分组、排序、出处都是脚本算的，**没有一句是模型写的**。
> 条目**原样转录**（含语料自己的措辞、大小写与错拼），本页不替它改。
>
> 因此本页只证明**「文档这么写」**，不证明**「机台这样」**（schema §11）。
> **本页没有被人在真实机台上核对过**（`verified: doc-only`）。

## 这一版改了什么（12 条）

格式：**出处文档 —— 语料原条目**。条目本身带 `MTP 3.1.5:` 前缀，**那是原文的一部分，没有去掉**。

- [Driver Sharing APIs](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.09.03_Driver_Sharing_APIs.md>) —— MTP 3.1.5: Added new APIs for testing any numbers of pins with any measurement conditions within one test method.
- [SharedContinuity test method](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.09.08_SharedContinuity_test_method.md>) —— MTP 3.1.5: New API MTP_CONTINUITY_TASK is added.
- [SharedLeakageParallel test method](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.09.11_SharedLeakageParallel_test_method.md>) —— MTP 3.1.5: The non-shared and cross-terminated pins can be precharged before measuring leakage current.
- [SharedLeakageParallel test method](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.09.11_SharedLeakageParallel_test_method.md>) —— MTP 3.1.5: Added new API: MTP_LEAKAGE_TASK.
- [SharedLeakageParallel syntax](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.09.12_SharedLeakageParallel_syntax.md>) —— MTP 3.1.5: Added new parameters: "PPMU Precharge", "Precharge Voltage", and "preFunction".
- [SharedIDD test method](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.09.13_SharedIDD_test_method.md>) —— MTP 3.1.5: Adeed new API: MTP_IDD_TASK.
- [apgc command syntax](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.02.05.01_apgc_command_syntax.md>) —— MTP 3.1.5: :Output generated with the -para option now supports the :testlabel: keyword
- [APG pattern file syntax](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.02.01_APG_pattern_file_syntax.md>) —— MTP 3.1.5: Parallel vectors can be called within the :testLabel: keyword.
- [SHARED_CONTINUITY_TEST](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.21_SHARED_CONTINUITY_TEST.md>) —— MTP 3.1.5: Added new API: MTP_CONTINUITY_TASK.
- [SHARED_IDD_TEST](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.22_SHARED_IDD_TEST.md>) —— MTP 3.1.5: Added new API: MTP_IDD_TASK.
- [SHARED_LEAKAGE_PARALLEL_TEST](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.23_SHARED_LEAKAGE_PARALLEL_TEST.md>) —— MTP 3.1.5: Added new member functions, precharge(), prechargeVoltage() preFunction(), for SHARED_LEAKAGE_PARALLEL_TEST.
- [SHARED_LEAKAGE_PARALLEL_TEST](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.23_SHARED_LEAKAGE_PARALLEL_TEST.md>) —— MTP 3.1.5: Added new API: MTP_LEAKAGE_TASK.


## 这一版新引入（82 条）

语料原句是 `Introduced in …`，说的是「**这篇文档描述的东西从这一版开始有**」。条目短，所以**文档放前面、原句放后面**：

- [FOR_EACH_SHARED_SITE_BEGIN](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.02_FOR_EACH_SHARED_SITE_BEGIN.md>) —— Introduced in MTP 3.1.5
- [FOR_EACH_SHARED_SITE_END](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.03_FOR_EACH_SHARED_SITE_END.md>) —— Introduced in MTP 3.1.5
- [FOR_EACH_TEST_BEGIN](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.04_FOR_EACH_TEST_BEGIN.md>) —— Introduced in MTP 3.1.5
- [FOR_EACH_TEST_BEGIN_WITH_RESET](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.05_FOR_EACH_TEST_BEGIN_WITH_RESET.md>) —— Introduced in MTP 3.1.5
- [FOR_EACH_TEST_END](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.06_FOR_EACH_TEST_END.md>) —— Introduced in MTP 3.1.5
- [GET_CURRENT_UTILITY_CONTROL](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.07_GET_CURRENT_UTILITY_CONTROL.md>) —— Introduced in MTP 3.1.5
- [GET_SITES_UNDER_TEST](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.08_GET_SITES_UNDER_TEST.md>) —— Introduced in MTP 3.1.5
- [MTP_CONTINUITY_PIN_TASK.iForce()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.10.01.01_MTP_CONTINUITY_PIN_TASK.iForce.md>) —— Introduced in MTP 3.1.5
- [MTP_CONTINUITY_PIN_TASK.vForce()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.10.01.02_MTP_CONTINUITY_PIN_TASK.vForce.md>) —— Introduced in MTP 3.1.5
- [MTP_CONTINUITY_PIN_TASK.limits()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.10.01.03_MTP_CONTINUITY_PIN_TASK.limits.md>) —— Introduced in MTP 3.1.5
- [MTP_CONTINUITY_PIN_TASK.deviceSupply()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.10.01.04_MTP_CONTINUITY_PIN_TASK.deviceSupply.md>) —— Introduced in MTP 3.1.5
- [MTP_CONTINUITY_PIN_TASK.forceSupply()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.10.01.05_MTP_CONTINUITY_PIN_TASK.forceSupply.md>) —— Introduced in MTP 3.1.5
- [MTP_CONTINUITY_PIN_TASK](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.10.01_MTP_CONTINUITY_PIN_TASK.md>) —— Introduced in MTP 3.1.5
- [MTP_CONTINUITY_TASK.pin()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.10.02_MTP_CONTINUITY_TASK.pin.md>) —— Introduced in MTP 3.1.5
- [MTP_CONTINUITY_TASK.settlingTime()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.10.03_MTP_CONTINUITY_TASK.settlingTime.md>) —— Introduced in MTP 3.1.5
- [MTP_CONTINUITY_TASK.execute()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.10.04_MTP_CONTINUITY_TASK.execute.md>) —— Introduced in MTP 3.1.5
- [MTP_CONTINUITY_TASK.postExecute()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.10.05_MTP_CONTINUITY_TASK.postExecute.md>) —— Introduced in MTP 3.1.5
- [MTP_CONTINUITY_TASK.getPassFail()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.10.06_MTP_CONTINUITY_TASK.getPassFail.md>) —— Introduced in MTP 3.1.5
- [MTP_CONTINUITY_TASK.getValue()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.10.07_MTP_CONTINUITY_TASK.getValue.md>) —— Introduced in MTP 3.1.5
- [MTP_CONTINUITY_TASK](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.10_MTP_CONTINUITY_TASK.md>) —— Introduced in MTP 3.1.5
- [MTP_DPS_MEASURE.pin()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.11.01_MTP_DPS_MEASURE.pin.md>) —— Introduced in MTP 3.1.5
- [MTP_DPS_MEASURE.execMode()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.11.02_MTP_DPS_MEASURE.execMode.md>) —— Introduced in MTP 3.1.5
- [MTP_DPS_MEASURE.samples()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.11.03_MTP_DPS_MEASURE.samples.md>) —— Introduced in MTP 3.1.5
- [MTP_DPS_MEASURE.wait()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.11.04_MTP_DPS_MEASURE.wait.md>) —— Introduced in MTP 3.1.5
- [MTP_DPS_MEASURE.execute()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.11.05_MTP_DPS_MEASURE.execute.md>) —— Introduced in MTP 3.1.5
- [MTP_DPS_MEASURE.getPassFail()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.11.06_MTP_DPS_MEASURE.getPassFail.md>) —— Introduced in MTP 3.1.5
- [MTP_DPS_MEASURE.getValue()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.11.07_MTP_DPS_MEASURE.getValue.md>) —— Introduced in MTP 3.1.5
- [MTP_DPS_MEASURE](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.11_MTP_DPS_MEASURE.md>) —— Introduced in MTP 3.1.5
- [MTP_FUNC_TASK.pin()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.12.01_MTP_FUNC_TASK.pin.md>) —— Introduced in MTP 3.1.5
- [MTP_FUNC_TASK.execute()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.12.02_MTP_FUNC_TASK.execute.md>) —— Introduced in MTP 3.1.5
- [MTP_FUNC_TASK.getPassFail()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.12.03_MTP_FUNC_TASK.getPassFail.md>) —— Introduced in MTP 3.1.5
- [MTP_FUNC_TASK](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.12_MTP_FUNC_TASK.md>) —— Introduced in MTP 3.1.5
- [MTP_IDD_PIN_TASK.limits()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.13.01.01_MTP_IDD_PIN_TASK.limits.md>) —— Introduced in MTP 3.1.5
- [MTP_IDD_PIN_TASK](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.13.01_MTP_IDD_PIN_TASK.md>) —— Introduced in MTP 3.1.5
- [MTP_IDD_TASK.pin()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.13.02_MTP_IDD_TASK.pin.md>) —— Introduced in MTP 3.1.5
- [MTP_IDD_TASK.waitTime()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.13.03_MTP_IDD_TASK.waitTime.md>) —— Introduced in MTP 3.1.5
- [MTP_IDD_TASK.samples()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.13.04_MTP_IDD_TASK.samples.md>) —— Introduced in MTP 3.1.5
- [MTP_IDD_TASK.execute()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.13.05_MTP_IDD_TASK.execute.md>) —— Introduced in MTP 3.1.5
- [MTP_IDD_TASK.getPassFail()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.13.06_MTP_IDD_TASK.getPassFail.md>) —— Introduced in MTP 3.1.5
- [MTP_IDD_TASK.getValue()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.13.07_MTP_IDD_TASK.getValue.md>) —— Introduced in MTP 3.1.5
- [MTP_IDD_TASK](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.13_MTP_IDD_TASK.md>) —— Introduced in MTP 3.1.5
- [MTP_LEAKAGE_PIN_TASK.vForce()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.14.01.01_MTP_LEAKAGE_PIN_TASK.vForce.md>) —— Introduced in MTP 3.1.5
- [MTP_LEAKAGE_PIN_TASK.limits()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.14.01.02_MTP_LEAKAGE_PIN_TASK.limits.md>) —— Introduced in MTP 3.1.5
- [MTP_LEAKAGE_PIN_TASK.iRange()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.14.01.03_MTP_LEAKAGE_PIN_TASK.iRange.md>) —— Introduced in MTP 3.1.5
- [MTP_LEAKAGE_PIN_TASK.prechargeVoltage()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.14.01.04_MTP_LEAKAGE_PIN_TASK.prechargeVoltage.md>) —— Introduced in MTP 3.1.5
- [MTP_LEAKAGE_PIN_TASK.prechargeTime()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.14.01.05_MTP_LEAKAGE_PIN_TASK.prechargeTime.md>) —— Introduced in MTP 3.1.5
- [MTP_LEAKAGE_PIN_TASK](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.14.01_MTP_LEAKAGE_PIN_TASK.md>) —— Introduced in MTP 3.1.5
- [MTP_LEAKAGE_TASK.pin()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.14.02_MTP_LEAKAGE_TASK.pin.md>) —— Introduced in MTP 3.1.5
- [MTP_LEAKAGE_TASK.settlingTime()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.14.03_MTP_LEAKAGE_TASK.settlingTime.md>) —— Introduced in MTP 3.1.5
- [MTP_LEAKAGE_TASK.execute()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.14.04_MTP_LEAKAGE_TASK.execute.md>) —— Introduced in MTP 3.1.5
- [MTP_LEAKAGE_TASK.postExecute()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.14.05_MTP_LEAKAGE_TASK.postExecute.md>) —— Introduced in MTP 3.1.5
- [MTP_LEAKAGE_TASK.getPassFail()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.14.06_MTP_LEAKAGE_TASK.getPassFail.md>) —— Introduced in MTP 3.1.5
- [MTP_LEAKAGE_TASK.getValue()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.14.07_MTP_LEAKAGE_TASK.getValue.md>) —— Introduced in MTP 3.1.5
- [MTP_LEAKAGE_TASK](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.14_MTP_LEAKAGE_TASK.md>) —— Introduced in MTP 3.1.5
- [MTP_PPMU_MEASURE.pin()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.19.01_MTP_PPMU_MEASURE.pin.md>) —— Introduced in MTP 3.1.5
- [MTP_PPMU_MEASURE.execute()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.19.02_MTP_PPMU_MEASURE.execute.md>) —— Introduced in MTP 3.1.5
- [MTP_PPMU_MEASURE.getPassFail()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.19.03_MTP_PPMU_MEASURE.getPassFail.md>) —— Introduced in MTP 3.1.5
- [MTP_PPMU_MEASURE.getValue()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.19.04_MTP_PPMU_MEASURE.getValue.md>) —— Introduced in MTP 3.1.5
- [MTP_PPMU_MEASURE](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.19_MTP_PPMU_MEASURE.md>) —— Introduced in MTP 3.1.5
- [SHARED_LEAKAGE_PARALLEL_TEST.precharge()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.23.09_SHARED_LEAKAGE_PARALLEL_TEST.precharge.md>) —— Introduced in MTP 3.1.5
- [SHARED_LEAKAGE_PARALLEL_TEST.prechargeVoltage()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.23.10_SHARED_LEAKAGE_PARALLEL_TEST.prechargeVoltage.md>) —— Introduced in MTP 3.1.5
- [SHARED_LEAKAGE_PARALLEL_TEST.preFunction()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.23.11_SHARED_LEAKAGE_PARALLEL_TEST.preFunction.md>) —— Introduced in MTP 3.1.5
- [SHARING_CONFIGURATION.getInstance()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.01_SHARING_CONFIGURATION.getInstance.md>) —— Introduced in MTP 3.1.5
- [SHARING_CONFIGURATION.hasLoaded()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.02_SHARING_CONFIGURATION.hasLoaded.md>) —— Introduced in MTP 3.1.5
- [SHARING_CONFIGURATION.load()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.03_SHARING_CONFIGURATION.load.md>) —— Introduced in MTP 3.1.5
- [SHARING_CONFIGURATION.setRefPin()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.04_SHARING_CONFIGURATION.setRefPin.md>) —— Introduced in MTP 3.1.5
- [SHARING_CONFIGURATION.getModeContext()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.05_SHARING_CONFIGURATION.getModeContext.md>) —— Introduced in MTP 3.1.5
- [SHARING_CONFIGURATION.isFXDLIgnorePin()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.06_SHARING_CONFIGURATION.isFXDLIgnorePin.md>) —— Introduced in MTP 3.1.5
- [SHARING_CONFIGURATION.utilitySearchFirst()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.07_SHARING_CONFIGURATION.utilitySearchFirst.md>) —— Introduced in MTP 3.1.5
- [SHARING_CONFIGURATION.utilitySearchNext](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.08_SHARING_CONFIGURATION.utilitySearchNext.md>) —— Introduced in MTP 3.1.5
- [SHARING_CONFIGURATION.utilityActionExecute()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.09_SHARING_CONFIGURATION.utilityActionExecute.md>) —— Introduced in MTP 3.1.5
- [SHARING_CONFIGURATION.utilityGetApplicableSitesString()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.10_SHARING_CONFIGURATION.utilityGetApplicableSitesString.md>) —— Introduced in MTP 3.1.5
- [SHARING_CONFIGURATION.utilitySubstitutePins()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.11_SHARING_CONFIGURATION.utilitySubstitutePins.md>) —— Introduced in MTP 3.1.5
- [SHARING_CONFIGURATION.domainsGetXSize()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.12_SHARING_CONFIGURATION.domainsGetXSize.md>) —— Introduced in MTP 3.1.5
- [SHARING_CONFIGURATION.domainsGetYSize()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.13_SHARING_CONFIGURATION.domainsGetYSize.md>) —— Introduced in MTP 3.1.5
- [SHARING_CONFIGURATION.domainsGetZSize()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.14_SHARING_CONFIGURATION.domainsGetZSize.md>) —— Introduced in MTP 3.1.5
- [SHARING_CONFIGURATION.domainsGetApplicableSitesString()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.15_SHARING_CONFIGURATION.domainsGetApplicableSitesString.md>) —— Introduced in MTP 3.1.5
- [SHARING_CONFIGURATION.domainsGetSiteAtPos()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.16_SHARING_CONFIGURATION.domainsGetSiteAtPos.md>) —— Introduced in MTP 3.1.5
- [SHARING_CONFIGURATION.getTerminatedPinList()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.17_SHARING_CONFIGURATION.getTerminatedPinList.md>) —— Introduced in MTP 3.1.5
- [SHARING_CONFIGURATION.getBufferPinMap()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.18_SHARING_CONFIGURATION.getBufferPinMap.md>) —— Introduced in MTP 3.1.5
- [SHARING_CONFIGURATION.getDomain()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.19_SHARING_CONFIGURATION.getDomain.md>) —— Introduced in MTP 3.1.5
- [SHARING_CONFIGURATION](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25_SHARING_CONFIGURATION.md>) —— Introduced in MTP 3.1.5


## 出处

- 抽取自 raw 的 `## Functional changes` 段落；**本页正文列出 94 条**，涉及 **92 篇**文档。
- 抽取器：`extract/versions.py`（纯脚本）；机器可读全量：`extract/version-facts.csv`。
- **本页没有逐篇回读 raw 原文**——条目是段落级抽取的结果。若要据此下结论，请点开对应出处链接核对。
