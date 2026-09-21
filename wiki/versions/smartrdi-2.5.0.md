---
type: version
title: SmartRDI 2.5.0 — 版本页
tags: [version, smartrdi]
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.04_RDI_Configure_file.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.04.01_digCapBurstSiteUpload.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.04_Controlling_burst_site_upload.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.09.02_Pass_Fail_per_label_without_break_vectors.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.20.01.01_rdi.enableOre.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.20.01.02_rdi.oreFile.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.20.01_Applying_Offline_Result_Emulation_in_SmartRDI.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.20.02.01_Template_file_from_the_first_run.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.20.03.01.02_The__cogo__element.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.20.03.01.03_The__dc__element.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.20.03.01.04_The__digCap__element.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.20.03.01.05_The__dgt__element.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.20.03.01.06_The__emap__element.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.20.03.01.07_The__func__element.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.20.03.01.08_The__protocol__element.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.20.03.01.09_The__rfm__element.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.20.03.01.10_The__smartVec__element.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.20.03.01.11_The__tmu__element.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.20.03.01_Test_name_elements.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.20.03_ORE_file_format.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.20_Using_Offline_Result_Emulation_in_SmartRDI.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.18_valueMode.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.13.03.01_rdi.digCapImmediateUpload.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.13.03.02_rdi.id__.getImmediateVector.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.13.03_Using_Immediate_Upload_in_SmartRDI.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.14.04_setOffRunTime.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.14.06_setOnRunTime.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.15.03_Routing_Tools_hardware.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.15.04_Routing_Tools_configuration.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.15.05.01_rdi.route__.applyState.md
  # 本页共涉及 44 篇文档。上面只列了前 30 篇——**完整出处是正文每条后面的链接**，
  # 机器可读全量见 extract/version-facts.csv（按 doc 列筛）。**这是有意的截断，不是漏列。**
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# SmartRDI 2.5.0

> **本页由 `extract/versions.py` 从 raw 的 `## Functional changes` 段落机械汇编**——分组、排序、出处都是脚本算的，**没有一句是模型写的**。
> 条目**原样转录**（含语料自己的措辞、大小写与错拼），本页不替它改。
>
> 因此本页只证明**「文档这么写」**，不证明**「机台这样」**（schema §11）。
> **本页没有被人在真实机台上核对过**（`verified: doc-only`）。

## 这一版改了什么（4 条）

格式：**出处文档 —— 语料原条目**。条目本身带 `SmartRDI 2.5.0:` 前缀，**那是原文的一部分，没有去掉**。

- [RDI_Configure file](<02_System_reference/02.07_Test_Method_Reference/02.07.13.04_RDI_Configure_file.md>) —— SmartRDI 2.5.0: New keywords DC_BURST_SITE_UPLOAD, DIGCAP_BURST_SITE_UPLOAD, PURE_GENERATION_MODE, PER_LABEL_FUNC_RESULT_NO_BREAK_VEC, ENABLE_ORE, ORE_FILE, and ROUTING_SETUP_FILE.
- [RDI_Configure file](<02_System_reference/02.07_Test_Method_Reference/02.07.13.04_RDI_Configure_file.md>) —— SmartRDI 2.5.0: Four keywords have their default values changed: PPMU_DEFAULT_VALUE_MODE (from "SA" to "BADC"), PER_LABEL_FUNC_RESULT_MODE (from "FLBL" to "ERMP"), DEFAULT_SMV_READ_MODE (from "EMAP" to "DIGCAP"), VEC_MODE_SAMPLING_WAIT (from "MSET" to "PATTERN").
- [valueMode()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.18_valueMode.md>) —— SmartRDI 2.5.0: The default value is changed from TA::SA to TA::BADC.
- [writeData()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.36_writeData.md>) —— SmartRDI 2.5.0: writeData() supports to generate patterns with per-site data.


## 这一版新引入（41 条）

语料原句是 `Introduced in …`，说的是「**这篇文档描述的东西从这一版开始有**」。条目短，所以**文档放前面、原句放后面**：

- [digCapBurstSiteUpload()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.04.01_digCapBurstSiteUpload.md>) —— Introduced in SmartRDI 2.5.0
- [Controlling burst site upload](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.04_Controlling_burst_site_upload.md>) —— Introduced in SmartRDI 2.5.0
- [Pass/Fail per label without break vectors](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.09.02_Pass_Fail_per_label_without_break_vectors.md>) —— Introduced in SmartRDI 2.5.0
- [rdi.enableOre()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.20.01.01_rdi.enableOre.md>) —— Introduced in SmartRDI 2.5.0
- [rdi.oreFile()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.20.01.02_rdi.oreFile.md>) —— Introduced in SmartRDI 2.5.0
- [Applying Offline Result Emulation in SmartRDI](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.20.01_Applying_Offline_Result_Emulation_in_SmartRDI.md>) —— Introduced in SmartRDI 2.5.0
- [Template file from the first run](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.20.02.01_Template_file_from_the_first_run.md>) —— Introduced in SmartRDI 2.5.0
- [The <cogo> element](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.20.03.01.02_The__cogo__element.md>) —— Introduced in SmartRDI 2.5.0
- [The <dc> element](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.20.03.01.03_The__dc__element.md>) —— Introduced in SmartRDI 2.5.0
- [The <digCap> element](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.20.03.01.04_The__digCap__element.md>) —— Introduced in SmartRDI 2.5.0
- [The <dgt> element](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.20.03.01.05_The__dgt__element.md>) —— Introduced in SmartRDI 2.5.0
- [The <emap> element](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.20.03.01.06_The__emap__element.md>) —— Introduced in SmartRDI 2.5.0
- [The <func> element](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.20.03.01.07_The__func__element.md>) —— Introduced in SmartRDI 2.5.0
- [The <protocol> element](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.20.03.01.08_The__protocol__element.md>) —— Introduced in SmartRDI 2.5.0
- [The <rfm> element](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.20.03.01.09_The__rfm__element.md>) —— Introduced in SmartRDI 2.5.0
- [The <smartVec> element](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.20.03.01.10_The__smartVec__element.md>) —— Introduced in SmartRDI 2.5.0
- [The <tmu> element](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.20.03.01.11_The__tmu__element.md>) —— Introduced in SmartRDI 2.5.0
- [Test name elements](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.20.03.01_Test_name_elements.md>) —— Introduced in SmartRDI 2.5.0
- [ORE file format](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.20.03_ORE_file_format.md>) —— Introduced in SmartRDI 2.5.0
- [Using Offline Result Emulation in SmartRDI](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.20_Using_Offline_Result_Emulation_in_SmartRDI.md>) —— Introduced in SmartRDI 2.5.0
- [rdi.digCapImmediateUpload()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.03.01_rdi.digCapImmediateUpload.md>) —— Introduced in SmartRDI 2.5.0
- [rdi.id().getImmediateVector()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.03.02_rdi.id__.getImmediateVector.md>) —— Introduced in SmartRDI 2.5.0
- [Using Immediate Upload in SmartRDI](<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.03_Using_Immediate_Upload_in_SmartRDI.md>) —— Introduced in SmartRDI 2.5.0
- [setOffRunTime()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.14.04_setOffRunTime.md>) —— Introduced in SmartRDI 2.5.0
- [setOnRunTime()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.14.06_setOnRunTime.md>) —— Introduced in SmartRDI 2.5.0
- [Routing Tools hardware](<02_System_reference/02.07_Test_Method_Reference/02.07.13.15.03_Routing_Tools_hardware.md>) —— Introduced in SmartRDI 2.5.0
- [Routing Tools configuration](<02_System_reference/02.07_Test_Method_Reference/02.07.13.15.04_Routing_Tools_configuration.md>) —— Introduced in SmartRDI 2.5.0
- [rdi.route().applyState()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.15.05.01_rdi.route__.applyState.md>) —— Introduced in SmartRDI 2.5.0
- [rdi.route().downloadPmuxMemSet()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.15.05.02_rdi.route__.downloadPmuxMemSet.md>) —— Introduced in SmartRDI 2.5.0
- [rdi.route().execute()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.15.05.04_rdi.route__.execute.md>) —— Introduced in SmartRDI 2.5.0
- [rdi.route().pin().setOff()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.15.05.05.01_rdi.route__.pin__.setOff.md>) —— Introduced in SmartRDI 2.5.0
- [rdi.route().pin().setOn()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.15.05.05.02_rdi.route__.pin__.setOn.md>) —— Introduced in SmartRDI 2.5.0
- [rdi.route().pin().execute()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.15.05.05.03_rdi.route__.pin__.execute.md>) —— Introduced in SmartRDI 2.5.0
- [rdi.route().pin()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.15.05.05_rdi.route__.pin.md>) —— Introduced in SmartRDI 2.5.0
- [rdi.route().reset()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.15.05.06_rdi.route__.reset.md>) —— Introduced in SmartRDI 2.5.0
- [rdi.route().showPmuxSensorStatus()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.15.05.07_rdi.route__.showPmuxSensorStatus.md>) —— Introduced in SmartRDI 2.5.0
- [rdi.route().showPmuxStatus()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.15.05.08_rdi.route__.showPmuxStatus.md>) —— Introduced in SmartRDI 2.5.0
- [rdi.route()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.15.05_rdi.route.md>) —— Introduced in SmartRDI 2.5.0
- [SmartRDI: DUT board connections control by Routing Tools](<02_System_reference/02.07_Test_Method_Reference/02.07.13.15_SmartRDI__DUT_board_connections_control_by_Routing_Tools.md>) —— Introduced in SmartRDI 2.5.0
- [getCommentCycleNum()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.22.07_getCommentCycleNum.md>) —— Introduced in SmartRDI 2.5.0
- [getCommentVectorNum()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.22.08_getCommentVectorNum.md>) —— Introduced in SmartRDI 2.5.0


## 出处

- 抽取自 raw 的 `## Functional changes` 段落；**本页正文列出 45 条**，涉及 **44 篇**文档。
- 抽取器：`extract/versions.py`（纯脚本）；机器可读全量：`extract/version-facts.csv`。
- **本页没有逐篇回读 raw 原文**——条目是段落级抽取的结果。若要据此下结论，请点开对应出处链接核对。
