---
type: version
title: MTP 3.1.3 — 版本页
tags: [version, mtp]
related: []
sources:
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.01.04_Setting_up_the_MTP_MEMORY_TEST_API.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.01_Memory_testing_test_method.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.06.02.05.01_SourceSync_fast_mode.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.06.02.05.02_SourceSync_standard_mode.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.09.03_Driver_Sharing_APIs.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.09.04_Setting_up_for_using_driver_sharing_APIs.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.09.08_SharedContinuity_test_method.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.09.11_SharedLeakageParallel_test_method.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.09.13_SharedIDD_test_method.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.09.15_SharedVBump_test_method.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.09_Test_methods_for_driver_sharing.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.12.02.01.01_MTL_compiler_options.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.02.05.01_apgc_command_syntax.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.02.05_Using_the_MTL_compiler_from_the_command_line.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.02.03.02.01.01_MTL_compiler_options.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.02_MTP-EWC.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.03.01_MTP_tools_overview.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.05.01_Automatic_Map_Converter_operating_principles.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.05.02_Creating_a_map_converter_library_with_the_Automatic_Map_Converter.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.05.03_Device_property_file.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.05_Automatic_Map_Converter.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.15.01_MTP_MEMORY_PATTERN.setBitMapFileName.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.15.02_MTP_MEMORY_PATTERN.setBitMapFilePath.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.15.03_MTP_MEMORY_PATTERN.addBitMapFileUserComments.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.15.04_MTP_MEMORY_PATTERN.generateBitmapFile.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.15.05_MTP_MEMORY_PATTERN.getBitMapFileName.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.15.07_MTP_MEMORY_PATTERN.getFailBitCount.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.15.08_MTP_MEMORY_PATTERN.getFailingAddressList.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.15_MTP_MEMORY_PATTERN.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.02_MTP_MEMORY_TEST.addBitMapFileUserComments.md
  # 本页共涉及 103 篇文档。上面只列了前 30 篇——**完整出处是正文每条后面的链接**，
  # 机器可读全量见 extract/version-facts.csv（按 doc 列筛）。**这是有意的截断，不是漏列。**
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# MTP 3.1.3

> **本页由 `extract/versions.py` 从 raw 的 `## Functional changes` 段落机械汇编**——分组、排序、出处都是脚本算的，**没有一句是模型写的**。
> 条目**原样转录**（含语料自己的措辞、大小写与错拼），本页不替它改。
>
> 因此本页只证明**「文档这么写」**，不证明**「机台这样」**（schema §11）。
> **本页没有被人在真实机台上核对过**（`verified: doc-only`）。

## 这一版改了什么（18 条）

格式：**出处文档 —— 语料原条目**。条目本身带 `MTP 3.1.3:` 前缀，**那是原文的一部分，没有去掉**。

- [Memory testing test method](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.01_Memory_testing_test_method.md>) —— MTP 3.1.3: MTP_MEMORY_TEST and MTP_MEMORY_PATTERN APIs are introduced to develop a customized test method.
- [SourceSync fast mode](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.06.02.05.01_SourceSync_fast_mode.md>) —— MTP 3.1.3: Added the Shmoo parameter section.
- [SourceSync fast mode](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.06.02.05.01_SourceSync_fast_mode.md>) —— MTP 3.1.3: Added the DQ Offset Min and DQ Offset Max limits.
- [SourceSync standard mode](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.06.02.05.02_SourceSync_standard_mode.md>) —— MTP 3.1.3: Added the Shmoo parameter section.
- [SourceSync standard mode](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.06.02.05.02_SourceSync_standard_mode.md>) —— MTP 3.1.3: Added the DQ Offset Min and DQ Offset Max limits
- [SharedContinuity test method](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.09.08_SharedContinuity_test_method.md>) —— MTP 3.1.3: New API SHARED_CONTINUITY_TEST is introduced for developing a customized test method.
- [SharedLeakageParallel test method](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.09.11_SharedLeakageParallel_test_method.md>) —— MTP 3.1.3: The SHARED_LEAKAGE_PARALLEL_TEST API is introduced to develop a customized test method.
- [SharedIDD test method](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.09.13_SharedIDD_test_method.md>) —— MTP 3.1.3: Adeed new API: SHARED_IDD_TEST.
- [SharedVBump test method](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.09.15_SharedVBump_test_method.md>) —— MTP 3.1.3: The SHARED_VBUMP_TEST API is introduced to develop a customized test method.
- [Test methods for driver sharing](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.09_Test_methods_for_driver_sharing.md>) —— MTP 3.1.3: Four APIs are introduced to create custom test methods for driver sharing in continuity test, IDD test, VBump test, and parallel leakage test.
- [MTL compiler options](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.12.02.01.01_MTL_compiler_options.md>) —— MTP 3.1.3: The Optimize Memory Usage option is now set through a pop-up menu.
- [MTL compiler options](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.12.02.01.01_MTL_compiler_options.md>) —— MTP 3.1.3: The padding options have been consolidated.
- [apgc command syntax](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.02.05.01_apgc_command_syntax.md>) —— MTP 3.1.3: Added -pps and -para options
- [Using the MTL compiler from the command line](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.02.05_Using_the_MTL_compiler_from_the_command_line.md>) —— MTP 3.1.3: Added support for generating parallel vectors
- [MTL compiler options](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.02.03.02.01.01_MTL_compiler_options.md>) —— MTP 3.1.3: The Optimize Memory Usage option is now set through a pop-up menu.
- [MTL compiler options](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.02.03.02.01.01_MTL_compiler_options.md>) —— MTP 3.1.3: The padding options have been consolidated.
- [MTP-EWC](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.02_MTP-EWC.md>) —— MTP 3.1.3: The MTP Build console view is added.
- [MTP tools overview](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.03.01_MTP_tools_overview.md>) —— MTP 3.1.3: The Automatic Map Converter has been added


## 这一版新引入（89 条）

语料原句是 `Introduced in …`，说的是「**这篇文档描述的东西从这一版开始有**」。条目短，所以**文档放前面、原句放后面**：

- [Setting up the MTP_MEMORY_TEST API](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.01.04_Setting_up_the_MTP_MEMORY_TEST_API.md>) —— Introduced in MTP 3.1.3
- [Driver Sharing APIs](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.09.03_Driver_Sharing_APIs.md>) —— Introduced in MTP 3.1.3
- [Setting up for using driver sharing APIs](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.09.04_Setting_up_for_using_driver_sharing_APIs.md>) —— Introduced in MTP 3.1.3
- [Automatic Map Converter operating principles](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.05.01_Automatic_Map_Converter_operating_principles.md>) —— Introduced in MTP 3.1.3
- [Creating a map converter library with the Automatic Map Converter](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.05.02_Creating_a_map_converter_library_with_the_Automatic_Map_Converter.md>) —— Introduced in MTP 3.1.3
- [Device property file](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.05.03_Device_property_file.md>) —— Introduced in MTP 3.1.3
- [Automatic Map Converter](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.05_Automatic_Map_Converter.md>) —— Introduced in MTP 3.1.3
- [MTP_MEMORY_PATTERN.setBitMapFileName()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.15.01_MTP_MEMORY_PATTERN.setBitMapFileName.md>) —— Introduced in MTP 3.1.3
- [MTP_MEMORY_PATTERN.setBitMapFilePath()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.15.02_MTP_MEMORY_PATTERN.setBitMapFilePath.md>) —— Introduced in MTP 3.1.3
- [MTP_MEMORY_PATTERN.addBitMapFileUserComments()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.15.03_MTP_MEMORY_PATTERN.addBitMapFileUserComments.md>) —— Introduced in MTP 3.1.3
- [MTP_MEMORY_PATTERN.generateBitmapFile()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.15.04_MTP_MEMORY_PATTERN.generateBitmapFile.md>) —— Introduced in MTP 3.1.3
- [MTP_MEMORY_PATTERN.getBitMapFileName()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.15.05_MTP_MEMORY_PATTERN.getBitMapFileName.md>) —— Introduced in MTP 3.1.3
- [MTP_MEMORY_PATTERN.getFailBitCount()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.15.07_MTP_MEMORY_PATTERN.getFailBitCount.md>) —— Introduced in MTP 3.1.3
- [MTP_MEMORY_PATTERN.getFailingAddressList()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.15.08_MTP_MEMORY_PATTERN.getFailingAddressList.md>) —— Introduced in MTP 3.1.3
- [MTP_MEMORY_PATTERN](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.15_MTP_MEMORY_PATTERN.md>) —— Introduced in MTP 3.1.3
- [MTP_MEMORY_TEST.addBitMapFileUserComments()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.02_MTP_MEMORY_TEST.addBitMapFileUserComments.md>) —— Introduced in MTP 3.1.3
- [MTP_MEMORY_TEST.enableAddressBasedResults()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.03_MTP_MEMORY_TEST.enableAddressBasedResults.md>) —— Introduced in MTP 3.1.3
- [MTP_MEMORY_TEST.enableFailBitCount()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.04_MTP_MEMORY_TEST.enableFailBitCount.md>) —— Introduced in MTP 3.1.3
- [MTP_MEMORY_TEST.execute()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.05_MTP_MEMORY_TEST.execute.md>) —— Introduced in MTP 3.1.3
- [MTP_MEMORY_TEST.getPassFailResult()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.10_MTP_MEMORY_TEST.getPassFailResult.md>) —— Introduced in MTP 3.1.3
- [MTP_MEMORY_TEST.restrictToChannelCaptureMemorySize()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.14_MTP_MEMORY_TEST.restrictToChannelCaptureMemorySize.md>) —— Introduced in MTP 3.1.3
- [MTP_MEMORY_TEST.setBitMapFilePath()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.16_MTP_MEMORY_TEST.setBitMapFilePath.md>) —— Introduced in MTP 3.1.3
- [MTP_MEMORY_TEST.setBitmapMode()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.17_MTP_MEMORY_TEST.setBitmapMode.md>) —— Introduced in MTP 3.1.3
- [MTP_MEMORY_TEST.setFailAddressListOrdering()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.18_MTP_MEMORY_TEST.setFailAddressListOrdering.md>) —— Introduced in MTP 3.1.3
- [MTP_MEMORY_TEST.setFailListStyle()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.19_MTP_MEMORY_TEST.setFailListStyle.md>) —— Introduced in MTP 3.1.3
- [MTP_MEMORY_TEST.setFBCLimit()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.20_MTP_MEMORY_TEST.setFBCLimit.md>) —— Introduced in MTP 3.1.3
- [MTP_MEMORY_TEST.setImmediateBitmapToFile()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.21_MTP_MEMORY_TEST.setImmediateBitmapToFile.md>) —— Introduced in MTP 3.1.3
- [MTP_MEMORY_TEST.setMaxFailingAddressesToLogPerPin()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.22_MTP_MEMORY_TEST.setMaxFailingAddressesToLogPerPin.md>) —— Introduced in MTP 3.1.3
- [MTP_MEMORY_TEST.setMaxFailingAddressesToReconstructPerPin()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.23_MTP_MEMORY_TEST.setMaxFailingAddressesToReconstructPerPin.md>) —— Introduced in MTP 3.1.3
- [MTP_MEMORY_TEST.setNumberOfFailCyclesToAcquirePerPin()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.25_MTP_MEMORY_TEST.setNumberOfFailCyclesToAcquirePerPin.md>) —— Introduced in MTP 3.1.3
- [MTP_MEMORY_TEST.setResultPins()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.37_MTP_MEMORY_TEST.setResultPins.md>) —— Introduced in MTP 3.1.3
- [MTP_MEMORY_TEST.setStartCaptureCycle()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.38_MTP_MEMORY_TEST.setStartCaptureCycle.md>) —— Introduced in MTP 3.1.3
- [MTP_MEMORY_TEST.setStopCaptureCycle()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.39_MTP_MEMORY_TEST.setStopCaptureCycle.md>) —— Introduced in MTP 3.1.3
- [MTP_MEMORY_TEST](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17_MTP_MEMORY_TEST.md>) —— Introduced in MTP 3.1.3
- [SHARED_CONTINUITY_TEST.init()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.21.01_SHARED_CONTINUITY_TEST.init.md>) —— Introduced in MTP 3.1.3
- [SHARED_CONTINUITY_TEST.sharingConfigFile()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.21.02_SHARED_CONTINUITY_TEST.sharingConfigFile.md>) —— Introduced in MTP 3.1.3
- [SHARED_CONTINUITY_TEST.pinShared()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.21.03_SHARED_CONTINUITY_TEST.pinShared.md>) —— Introduced in MTP 3.1.3
- [SHARED_CONTINUITY_TEST.forceVoltage()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.21.04_SHARED_CONTINUITY_TEST.forceVoltage.md>) —— Introduced in MTP 3.1.3
- [SHARED_CONTINUITY_TEST.pinNonShared()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.21.05_SHARED_CONTINUITY_TEST.pinNonShared.md>) —— Introduced in MTP 3.1.3
- [SHARED_CONTINUITY_TEST.forceCurrentNonShared()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.21.06_SHARED_CONTINUITY_TEST.forceCurrentNonShared.md>) —— Introduced in MTP 3.1.3
- [SHARED_CONTINUITY_TEST.pinCross()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.21.07_SHARED_CONTINUITY_TEST.pinCross.md>) —— Introduced in MTP 3.1.3
- [SHARED_CONTINUITY_TEST.forceCurrentCross()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.21.08_SHARED_CONTINUITY_TEST.forceCurrentCross.md>) —— Introduced in MTP 3.1.3
- [SHARED_CONTINUITY_TEST.terminationDPS()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.21.09_SHARED_CONTINUITY_TEST.terminationDPS.md>) —— Introduced in MTP 3.1.3
- [SHARED_CONTINUITY_TEST.supplyDPS()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.21.10_SHARED_CONTINUITY_TEST.supplyDPS.md>) —— Introduced in MTP 3.1.3
- [SHARED_CONTINUITY_TEST.settlingTime()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.21.11_SHARED_CONTINUITY_TEST.settlingTime.md>) —— Introduced in MTP 3.1.3
- [SHARED_CONTINUITY_TEST.output()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.21.12_SHARED_CONTINUITY_TEST.output.md>) —— Introduced in MTP 3.1.3
- [SHARED_CONTINUITY_TEST.execute()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.21.13_SHARED_CONTINUITY_TEST.execute.md>) —— Introduced in MTP 3.1.3
- [SHARED_CONTINUITY_TEST.judgeAndLog()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.21.14_SHARED_CONTINUITY_TEST.judgeAndLog.md>) —— Introduced in MTP 3.1.3
- [SHARED_CONTINUITY_TEST().print()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.21.15_SHARED_CONTINUITY_TEST__.print.md>) —— Introduced in MTP 3.1.3
- [SHARED_CONTINUITY_TEST.getPassFail()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.21.16_SHARED_CONTINUITY_TEST.getPassFail.md>) —— Introduced in MTP 3.1.3
- [SHARED_CONTINUITY_TEST.getValue()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.21.17_SHARED_CONTINUITY_TEST.getValue.md>) —— Introduced in MTP 3.1.3
- [SHARED_CONTINUITY_TEST](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.21_SHARED_CONTINUITY_TEST.md>) —— Introduced in MTP 3.1.3
- [SHARED_IDD_TEST.init()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.22.01_SHARED_IDD_TEST.init.md>) —— Introduced in MTP 3.1.3
- [SHARED_IDD_TEST.sharingConfigFile()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.22.02_SHARED_IDD_TEST.sharingConfigFile.md>) —— Introduced in MTP 3.1.3
- [SHARED_IDD_TEST.vdd()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.22.03_SHARED_IDD_TEST.vdd.md>) —— Introduced in MTP 3.1.3
- [SHARED_IDD_TEST.vddq()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.22.04_SHARED_IDD_TEST.vddq.md>) —— Introduced in MTP 3.1.3
- [SHARED_IDD_TEST.resetPin()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.22.05_SHARED_IDD_TEST.resetPin.md>) —— Introduced in MTP 3.1.3
- [SHARED_IDD_TEST.waitTime()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.22.06_SHARED_IDD_TEST.waitTime.md>) —— Introduced in MTP 3.1.3
- [SHARED_IDD_TEST.samples()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.22.07_SHARED_IDD_TEST.samples.md>) —— Introduced in MTP 3.1.3
- [SHARED_IDD_TEST.execute()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.22.08_SHARED_IDD_TEST.execute.md>) —— Introduced in MTP 3.1.3
- [SHARED_IDD_TEST.judgeAndLog()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.22.09_SHARED_IDD_TEST.judgeAndLog.md>) —— Introduced in MTP 3.1.3
- [SHARED_IDD_TEST.print()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.22.10_SHARED_IDD_TEST.print.md>) —— Introduced in MTP 3.1.3
- [SHARED_IDD_TEST.getPassFail()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.22.11_SHARED_IDD_TEST.getPassFail.md>) —— Introduced in MTP 3.1.3
- [SHARED_IDD_TEST.getValue()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.22.12_SHARED_IDD_TEST.getValue.md>) —— Introduced in MTP 3.1.3
- [SHARED_IDD_TEST](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.22_SHARED_IDD_TEST.md>) —— Introduced in MTP 3.1.3
- [SHARED_LEAKAGE_PARALLEL_TEST.init()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.23.01_SHARED_LEAKAGE_PARALLEL_TEST.init.md>) —— Introduced in MTP 3.1.3
- [SHARED_LEAKAGE_PARALLEL_TEST.sharingConfigFile()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.23.02_SHARED_LEAKAGE_PARALLEL_TEST.sharingConfigFile.md>) —— Introduced in MTP 3.1.3
- [SHARED_LEAKAGE_PARALLEL_TEST.pinShared()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.23.03_SHARED_LEAKAGE_PARALLEL_TEST.pinShared.md>) —— Introduced in MTP 3.1.3
- [SHARED_LEAKAGE_PARALLEL_TEST.pinNonShared()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.23.04_SHARED_LEAKAGE_PARALLEL_TEST.pinNonShared.md>) —— Introduced in MTP 3.1.3
- [SHARED_LEAKAGE_PARALLEL_TEST.pinCross()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.23.05_SHARED_LEAKAGE_PARALLEL_TEST.pinCross.md>) —— Introduced in MTP 3.1.3
- [SHARED_LEAKAGE_PARALLEL_TEST.forceVoltage()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.23.06_SHARED_LEAKAGE_PARALLEL_TEST.forceVoltage.md>) —— Introduced in MTP 3.1.3
- [SHARED_LEAKAGE_PARALLEL_TEST.settlingTime()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.23.07_SHARED_LEAKAGE_PARALLEL_TEST.settlingTime.md>) —— Introduced in MTP 3.1.3
- [SHARED_LEAKAGE_PARALLEL_TEST.prechargeTime()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.23.08_SHARED_LEAKAGE_PARALLEL_TEST.prechargeTime.md>) —— Introduced in MTP 3.1.3
- [SHARED_LEAKAGE_PARELLEL_TEST.execute()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.23.12_SHARED_LEAKAGE_PARELLEL_TEST.execute.md>) —— Introduced in MTP 3.1.3
- [SHARED_LEAKAGE_PARALLEL_TEST.judegeAndLog()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.23.13_SHARED_LEAKAGE_PARALLEL_TEST.judegeAndLog.md>) —— Introduced in MTP 3.1.3
- [SHARED_LEAKAGE_PARALLEL_TEST.print()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.23.14_SHARED_LEAKAGE_PARALLEL_TEST.print.md>) —— Introduced in MTP 3.1.3
- [SHARED_LEAKAGE_PARALLEL_TEST.getPassFail()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.23.15_SHARED_LEAKAGE_PARALLEL_TEST.getPassFail.md>) —— Introduced in MTP 3.1.3
- [SHARED_LEAKAGE_PARALLEL_TEST.getValue()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.23.16_SHARED_LEAKAGE_PARALLEL_TEST.getValue.md>) —— Introduced in MTP 3.1.3
- [SHARED_LEAKAGE_PARALLEL_TEST](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.23_SHARED_LEAKAGE_PARALLEL_TEST.md>) —— Introduced in MTP 3.1.3
- [SHARED_VBUMP_TEST.init()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.24.01_SHARED_VBUMP_TEST.init.md>) —— Introduced in MTP 3.1.3
- [SHARED_VBUMP_TEST.sharingConfigFile()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.24.02_SHARED_VBUMP_TEST.sharingConfigFile.md>) —— Introduced in MTP 3.1.3
- [SHARED_VBUMP_TEST.bumpSource()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.24.03_SHARED_VBUMP_TEST.bumpSource.md>) —— Introduced in MTP 3.1.3
- [SHARED_VBUMP_TEST.highPower()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.24.04_SHARED_VBUMP_TEST.highPower.md>) —— Introduced in MTP 3.1.3
- [SHARED_VBUMP_TEST.resultPin()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.24.05_SHARED_VBUMP_TEST.resultPin.md>) —— Introduced in MTP 3.1.3
- [SHARED_VBUMP_TEST.resetPin()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.24.06_SHARED_VBUMP_TEST.resetPin.md>) —— Introduced in MTP 3.1.3
- [SHARED_VBUMP_TEST.execute()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.24.07_SHARED_VBUMP_TEST.execute.md>) —— Introduced in MTP 3.1.3
- [SHARED_VBUMP_TEST.judegeAndLog()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.24.08_SHARED_VBUMP_TEST.judegeAndLog.md>) —— Introduced in MTP 3.1.3
- [SHARED_VBUMP_TEST.getPassFail()](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.24.10_SHARED_VBUMP_TEST.getPassFail.md>) —— Introduced in MTP 3.1.3
- [SHARED_VBUMP_TEST](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.24_SHARED_VBUMP_TEST.md>) —— Introduced in MTP 3.1.3


## 出处

- 抽取自 raw 的 `## Functional changes` 段落；**本页正文列出 107 条**，涉及 **103 篇**文档。
- 抽取器：`extract/versions.py`（纯脚本）；机器可读全量：`extract/version-facts.csv`。
- **本页没有逐篇回读 raw 原文**——条目是段落级抽取的结果。若要据此下结论，请点开对应出处链接核对。
