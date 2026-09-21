---
type: version
title: SmartRDI 7.10.0 — 版本页
tags: [version, smartrdi]
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.04_RDI_Configure_file.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.06.01_rdi.getInfoLevel.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.06.02_rdi.setInfoLevel.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.20.01.03_rdi.startNextOreTemp.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.20.02.02_Template_file_based_on_user_code.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.20.02.03_Template_file_from_online_test_results.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.08.20.03.01.01_The__alarm__element.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.11.01.03_perSiteVal.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.11.07.03_Forcing_waveform_and_sampling_in_parallel_on_multiple_pins.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.11.08_Parallel_pulse_actions_with_measurement_and_sampling.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.46_vMeasReturnDrop.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.17.01.01_rdi.func__.burst.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.17.01.20_rdi.port_TA__MULTI_PORT_.func.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.19.02.02_pathPin.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.19.02_Sequencer-controlled_searching_with_cogo.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# SmartRDI 7.10.0

> **本页由 `extract/versions.py` 从 raw 的 `## Functional changes` 段落机械汇编**——分组、排序、出处都是脚本算的，**没有一句是模型写的**。
> 条目**原样转录**（含语料自己的措辞、大小写与错拼），本页不替它改。
>
> 因此本页只证明**「文档这么写」**，不证明**「机台这样」**（schema §11）。
> **本页没有被人在真实机台上核对过**（`verified: doc-only`）。

## 这一版改了什么（8 条）

格式：**出处文档 —— 语料原条目**。条目本身带 `SmartRDI 7.10.0:` 前缀，**那是原文的一部分，没有去掉**。

- [RDI_Configure file](<02_System_reference/02.07_Test_Method_Reference/02.07.13.04_RDI_Configure_file.md>) —— SmartRDI 7.10.0: New keyword ORE_TEMPLATE_DATA_FILE_SIZE_THRESHOLD; PPMU_PURE_VMEAS_2P2_COMPATIBLE_MODE is removed; and SMV_DIGCAP_AUTO_BURSTUPLOAD = TRUE by default.
- [Template file based on user code](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.20.02.02_Template_file_based_on_user_code.md>) —— SmartRDI 7.10.0: Results of each execution is added to a separate template file.
- [Template file from online test results](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.20.02.03_Template_file_from_online_test_results.md>) —— SmartRDI 7.10.0: Real test results of all sites can be added to the template file.
- [Forcing waveform and sampling in parallel on multiple pins](<02_System_reference/02.07_Test_Method_Reference/02.07.13.11.07.03_Forcing_waveform_and_sampling_in_parallel_on_multiple_pins.md>) —— SmartRDI 7.10.0: More parallel DC actions on multiple pins are supported.
- [vMeasReturnDrop()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.46_vMeasReturnDrop.md>) —— SmartRDI 7.10.0: UHC4T card is supported.
- [rdi.func().burst()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.17.01.01_rdi.func__.burst.md>) —— SmartRDI 7.10.0: Multi-port burst labels are supported in dynamic mode.
- [pathPin()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.19.02.02_pathPin.md>) —— SmartRDI 7.10.0: pathPin() is no longer required for retrieving cogo search results.
- [Sequencer-controlled searching with cogo](<02_System_reference/02.07_Test_Method_Reference/02.07.13.19.02_Sequencer-controlled_searching_with_cogo.md>) —— SmartRDI 7.10.0: Cogo result retrieval without .pathPin().


## 这一版新引入（7 条）

语料原句是 `Introduced in …`，说的是「**这篇文档描述的东西从这一版开始有**」。条目短，所以**文档放前面、原句放后面**：

- [rdi.getInfoLevel()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.06.01_rdi.getInfoLevel.md>) —— Introduced in SmartRDI 7.10.0
- [rdi.setInfoLevel()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.06.02_rdi.setInfoLevel.md>) —— Introduced in SmartRDI 7.10.0
- [rdi.startNextOreTemp()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.20.01.03_rdi.startNextOreTemp.md>) —— Introduced in SmartRDI 7.10.0
- [The <alarm> element](<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.20.03.01.01_The__alarm__element.md>) —— Introduced in SmartRDI 7.10.0
- [perSiteVal()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.11.01.03_perSiteVal.md>) —— Introduced in SmartRDI 7.10.0
- [Parallel pulse actions with measurement and sampling](<02_System_reference/02.07_Test_Method_Reference/02.07.13.11.08_Parallel_pulse_actions_with_measurement_and_sampling.md>) —— Introduced in SmartRDI 7.10.0
- [rdi.port(TA::MULTI_PORT).func()](<02_System_reference/02.07_Test_Method_Reference/02.07.13.17.01.20_rdi.port_TA__MULTI_PORT_.func.md>) —— Introduced in SmartRDI 7.10.0


## 出处

- 抽取自 raw 的 `## Functional changes` 段落；**本页正文列出 15 条**，涉及 **15 篇**文档。
- 抽取器：`extract/versions.py`（纯脚本）；机器可读全量：`extract/version-facts.csv`。
- **本页没有逐篇回读 raw 原文**——条目是段落级抽取的结果。若要据此下结论，请点开对应出处链接核对。
