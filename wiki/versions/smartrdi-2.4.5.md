---
type: version
title: SmartRDI 2.4.5 — 版本页
tags: [version, smartrdi]
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.04_RDI_Configure_file.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.06_RDI_INFO_LEVEL.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.01.05_RDI_END.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.01.08_RDI_WAIT_TEST_DONE.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.01_General_SmartRDI_functions.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.06.03_rdi.getActiveRdiRev.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.06.04_rdi.getCompileRdiRev.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.06_Getting_the_SmartRDI_revision_information.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.08.02_portSync.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.08_Multiport_handling.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.16_SmartRDI_warning_handling.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.19.02.01_rdi.disableSmcExec.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.19.02.02_rdi.enableSmcExec.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.19.02.03_rdi.hiddenUpload.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.19.02.04_rdi.site.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.19.02_SmartRDI_functions_controlling_SmartCalc__SMC.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.21_Wait_time_in_SmartRDI.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.26_loadCap.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.16.02_emapLocation.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.16.12_xMode.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.23.04_Sequencer_Controlled_Utility_Mask_with_SmartRDI.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.24.03_burstLabel.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.24.23_labelName.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# SmartRDI 2.4.5

> **本页由 `extract/versions.py` 从 raw 的 `## Functional changes` 段落机械汇编**——分组、排序、出处都是脚本算的，**没有一句是模型写的**。
> 条目**原样转录**（含语料自己的措辞、大小写与错拼），本页不替它改。
>
> 因此本页只证明**「文档这么写」**，不证明**「机台这样」**（schema §11）。
> **本页没有被人在真实机台上核对过**（`verified: doc-only`）。

## 这一版改了什么（11 条）

格式：**出处文档 —— 语料原条目**。条目本身带 `SmartRDI 2.4.5:` 前缀，**那是原文的一部分，没有去掉**。

- [RDI_Configure file](<02_System_reference/02.07_Test_Method_Reference/02.07.13.04_RDI_Configure_file.md>) —— SmartRDI 2.4.5: During the 1st run, SmartRDI is able to judge whether the burst pattern needs to be regenerated when BURST_NAME_MD5 is set to FALSE.
- [RDI_Configure file](<02_System_reference/02.07_Test_Method_Reference/02.07.13.04_RDI_Configure_file.md>) —— SmartRDI 2.4.5: New keywords USER_NAMED_LABEL_CONTENT_CHECK, DEFAULT_EMAP_LOCATION, ENABLE_RDI_INFO_LOG_FILE, DISABLE_SMC_EXEC_GLOBAL, DISABLE_SMC_EXEC_SHORT_BURST, SMV_DIGCAP_AUTO_BURSTUPLOAD, UTIL_DYN_MASK_UNSPECIFIED_PIN, UTIL_DYN_MASK_INACTIVE_SITE, DIGCAP_ADAPTIVE_RESULT_SIZE, and TMU_TIMEOUT_50ms.
- [RDI_INFO_LEVEL](<02_System_reference/02.07_Test_Method_Reference/02.07.13.06_RDI_INFO_LEVEL.md>) —— SmartRDI 2.4.5: Support RDI_INFO_LEVEL 3.
- [RDI_END()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.01.05_RDI_END.md>) —— SmartRDI 2.4.5: New execution mode TA::NON_BLOCKING is added to supported non-blocking pattern execution.
- [portSync()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.08.02_portSync.md>) —— SmartRDI 2.4.5: New parameter TA::CTIM for exact port synchronization.
- [rdi.hiddenUpload()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.19.02.03_rdi.hiddenUpload.md>) —— SmartRDI 2.4.5: Combined use of SMC_DISABLE(true) with rdi.hiddenUpload(TA::ALL) no more reports an error.
- [rdi.site()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.19.02.04_rdi.site.md>) —— SmartRDI 2.4.5: rdi.site().id().getXXX() can be called anywhere inside a test method's run() function; the error map result supports common thread SMC.
- [loadCap()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.26_loadCap.md>) —— SmartRDI 2.4.5: Minimum load capacity allowed changes from 1 uF to 1 nF, for better support of pattern‑based mode for AVI64.
- [emapLocation()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.16.02_emapLocation.md>) —— SmartRDI 2.4.5: Default error map location changes from TA::TP (test processor) to TA::RAM (unused vector memory on the tester).
- [burstLabel()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.03_burstLabel.md>) —— SmartRDI 2.4.5: burstLabel() supports multiple ports, and can be used in combination with portSync().
- [labelName()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.23_labelName.md>) —— SmartRDI 2.4.5: A label name with or without an MD5 postfix option.


## 这一版新引入（13 条）

语料原句是 `Introduced in …`，说的是「**这篇文档描述的东西从这一版开始有**」。条目短，所以**文档放前面、原句放后面**：

- [RDI_WAIT_TEST_DONE()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.01.08_RDI_WAIT_TEST_DONE.md>) —— Introduced in SmartRDI 2.4.5
- [General SmartRDI functions](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.01_General_SmartRDI_functions.md>) —— Introduced in SmartRDI 2.4.5
- [rdi.getActiveRdiRev()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.06.03_rdi.getActiveRdiRev.md>) —— Introduced in SmartRDI 2.4.5
- [rdi.getCompileRdiRev()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.06.04_rdi.getCompileRdiRev.md>) —— Introduced in SmartRDI 2.4.5
- [Getting the SmartRDI revision information](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.06_Getting_the_SmartRDI_revision_information.md>) —— Introduced in SmartRDI 2.4.5
- [Multiport handling](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.08_Multiport_handling.md>) —— Introduced in SmartRDI 2.4.5
- [SmartRDI warning handling](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.16_SmartRDI_warning_handling.md>) —— Introduced in SmartRDI 2.4.5
- [rdi.disableSmcExec()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.19.02.01_rdi.disableSmcExec.md>) —— Introduced in SmartRDI 2.4.5
- [rdi.enableSmcExec()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.19.02.02_rdi.enableSmcExec.md>) —— Introduced in SmartRDI 2.4.5
- [SmartRDI functions controlling SmartCalc (SMC)](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.19.02_SmartRDI_functions_controlling_SmartCalc__SMC.md>) —— Introduced in SmartRDI 2.4.5
- [Wait time in SmartRDI](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.21_Wait_time_in_SmartRDI.md>) —— Introduced in SmartRDI 2.4.5
- [xMode()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.16.12_xMode.md>) —— Introduced in SmartRDI 2.4.5
- [Sequencer Controlled Utility Mask with SmartRDI](<02_System_reference/02.07_Test_Method_Reference/02.07.13.23.04_Sequencer_Controlled_Utility_Mask_with_SmartRDI.md>) —— Introduced in SmartRDI 2.4.5


## 出处

- 抽取自 raw 的 `## Functional changes` 段落；**本页正文列出 24 条**，涉及 **23 篇**文档。
- 抽取器：`extract/versions.py`（纯脚本）；机器可读全量：`extract/version-facts.csv`。
- **本页没有逐篇回读 raw 原文**——条目是段落级抽取的结果。若要据此下结论，请点开对应出处链接核对。
