---
type: version
title: MTP 3.3.1 — 版本页
tags: [version, mtp]
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.255_TDEX__Test_Data_Extension.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.01_Memory_testing_test_method.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.02.05.01_apgc_command_syntax.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01.01.01_Data_types_relevant_to_operators.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01.01_Operators.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01.05_Variables.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01.06_Values.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01.09.01.01_Defining_MTL_arrays.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01.09_Array_in_MTL.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.06.01_Pin_mapping_file_syntax.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.02.02_Creating_MTL_files_with_the_MTP_wizard.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.02.05.01_Syntax_highlight_in_the_MTP_editor.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.02.05.02_Content_assistant_in_the_MTP_editor.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.02.05.03_Error_annotations_in_the_MTP_editor.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.02.05.04.01_Keyboard_shortcuts_with_the_MTP_editor.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.02.05_Features_for_the_editor_of_MTP-EWC.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# MTP 3.3.1

> **本页由 `extract/versions.py` 从 raw 的 `## Functional changes` 段落机械汇编**——分组、排序、出处都是脚本算的，**没有一句是模型写的**。
> 条目**原样转录**（含语料自己的措辞、大小写与错拼），本页不替它改。
>
> 因此本页只证明**「文档这么写」**，不证明**「机台这样」**（schema §11）。
> **本页没有被人在真实机台上核对过**（`verified: doc-only`）。

## 这一版改了什么（24 条）

格式：**出处文档 —— 语料原条目**。条目本身带 `MTP 3.3.1:` 前缀，**那是原文的一部分，没有去掉**。

- [TDEX (Test Data Extension)](<02_System_reference/02.06_Command_Reference/02.06.02.02.255_TDEX__Test_Data_Extension.md>) —— MTP 3.3.1: Adds new attributes for pin: system, optional
- [Memory testing test method](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.01_Memory_testing_test_method.md>) —— MTP 3.3.1: The ExecutionEngine test method starts to support the Pin Scale SL digital card.
- [apgc command syntax](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.02.05.01_apgc_command_syntax.md>) —— MTP 3.3.1: Adds a new option --genidFilter.
- [Operators](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01.01_Operators.md>) —— MTP 3.3.1: Adds new operators: &&, ||, !, and ? :
- [Variables](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01.05_Variables.md>) —— MTP 3.3.1: Variables in the .prog files get new data types: strings, Boolean, and T_KEY.
- [Values](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01.06_Values.md>) —— MTP 3.3.1: Values in the APG program can be strings, Boolean values, and the T_KEY data type besides integers.
- [Defining MTL arrays](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01.09.01.01_Defining_MTL_arrays.md>) —— MTP 3.3.1: MTL array data type can be strings, Boolean, or the T_KEY data type besides integers.
- [Array in MTL](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01.09_Array_in_MTL.md>) —— MTP 3.3.1: The data type of MTL array can be strings, Boolean, and T_KEY besides integers.
- [Pin mapping file syntax](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.06.01_Pin_mapping_file_syntax.md>) —— MTP 3.3.1: New keyword: using protocol
- [Pin mapping file syntax](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.06.01_Pin_mapping_file_syntax.md>) —— MTP 3.3.1: New pin attributes: system, optional
- [Creating MTL files with the MTP wizard](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.02.02_Creating_MTL_files_with_the_MTP_wizard.md>) —— MTP 3.3.1: Adds a new menu command MTP Wizard for opening an MTP wizard.
- [Syntax highlight in the MTP editor](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.02.05.01_Syntax_highlight_in_the_MTP_editor.md>) —— MTP 3.3.1: Adds the color for device parameter.
- [Content assistant in the MTP editor](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.02.05.02_Content_assistant_in_the_MTP_editor.md>) —— MTP 3.3.1: Adds subroutine and device parameter content assistants.
- [Content assistant in the MTP editor](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.02.05.02_Content_assistant_in_the_MTP_editor.md>) —— MTP 3.3.1: "Ctrl + space" can list all kinds of content assistants.
- [Error annotations in the MTP editor](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.02.05.03_Error_annotations_in_the_MTP_editor.md>) —— MTP 3.3.1: Adds error annotations for subroutine and device parameter check.
- [Keyboard shortcuts with the MTP editor](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.02.05.04.01_Keyboard_shortcuts_with_the_MTP_editor.md>) —— MTP 3.3.1: Adds keyboard shortcuts for subroutine and device parameter content assistants.
- [Features for the editor of MTP-EWC](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.02.05_Features_for_the_editor_of_MTP-EWC.md>) —— MTP 3.3.1: The hyperlink solution starts to support subroutine and device parameter.
- [Features for the editor of MTP-EWC](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.02.05_Features_for_the_editor_of_MTP-EWC.md>) —— MTP 3.3.1: The text help solution starts to support subroutine and device parameter.
- [Features for the editor of MTP-EWC](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.02.05_Features_for_the_editor_of_MTP-EWC.md>) —— MTP 3.3.1: The content assistant solution starts to support subroutine and device parameter.
- [Features for the editor of MTP-EWC](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.02.05_Features_for_the_editor_of_MTP-EWC.md>) —— MTP 3.3.1: The syntax highlight solution starts to support subroutine and device parameter.
- [Features for the editor of MTP-EWC](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.02.05_Features_for_the_editor_of_MTP-EWC.md>) —— MTP 3.3.1: The error annotations solution starts to support subroutine and device parameter.
- [Features for the editor of MTP-EWC](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.02.05_Features_for_the_editor_of_MTP-EWC.md>) —— MTP 3.3.1: File paths can include variables.
- [Features for the editor of MTP-EWC](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.02.05_Features_for_the_editor_of_MTP-EWC.md>) —— MTP 3.3.1: Provides warnings on the pin mapping file.
- [Features for the editor of MTP-EWC](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.02.05_Features_for_the_editor_of_MTP-EWC.md>) —— MTP 3.3.1: Supports using F3 to open and jump to the definition file for a cursor pointed setup.


## 这一版新引入（1 条）

语料原句是 `Introduced in …`，说的是「**这篇文档描述的东西从这一版开始有**」。条目短，所以**文档放前面、原句放后面**：

- [Data types relevant to operators](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01.01.01_Data_types_relevant_to_operators.md>) —— Introduced in MTP 3.3.1


## 出处

- 抽取自 raw 的 `## Functional changes` 段落；**本页正文列出 25 条**，涉及 **16 篇**文档。
- 抽取器：`extract/versions.py`（纯脚本）；机器可读全量：`extract/version-facts.csv`。
- **本页没有逐篇回读 raw 原文**——条目是段落级抽取的结果。若要据此下结论，请点开对应出处链接核对。
