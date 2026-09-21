---
type: version
title: MTP 3.0.1 — 版本页
tags: [version, mtp]
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.255_TDEX__Test_Data_Extension.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.04.11_Compile_the_memory_test_program.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.01.01_Debugging.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.01.02_Failure_analysis.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.01.03_High-volume_manufacturing.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.01_Use_cases.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.02_Generate_vectors_and_reconstruction_information.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.04_Creating_a_testflow_in_SmarTest.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.01.01_Adding_the_ExecutionEngine_test_method_to_a_testflow.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.01.03.01_Parameters_for_the_ExecutionEngine_test_method.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.01.03_Setting_parameters_for_the_ExecutionEngine_test_method.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.01_Memory_testing_test_method.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.03.01_GDDR5_training_configuration_file.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.03.02_LoadConfig_test_method.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.03.03_Address_Training_test_method.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.03.04_Address_Bus_Inversion_Training_test_method.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.03.05_Clock_Training_test_method.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.03.06_Read_Training_test_method.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.03.07_Write_Training_test_method.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.03.08_GDDR5_Training_test_method.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.03.09_ChangeSpecification_test_method.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.03.10_Print_output.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.03_GDDR5_training_test_methods.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.04.01_EyeFinder_theory_of_operation.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.04.02_Using_EyeFinder.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.05_Parallel_Shmoo_test_method.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.06.02.05.01_SourceSync_fast_mode.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.06.02.05.02_SourceSync_standard_mode.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.06.02.05_Parameters_for_multistrobe_test_methods.md
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.06.03.03_DataTraining_parameters.md
  # 本页共涉及 104 篇文档。上面只列了前 30 篇——**完整出处是正文每条后面的链接**，
  # 机器可读全量见 extract/version-facts.csv（按 doc 列筛）。**这是有意的截断，不是漏列。**
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# MTP 3.0.1

> **本页由 `extract/versions.py` 从 raw 的 `## Functional changes` 段落机械汇编**——分组、排序、出处都是脚本算的，**没有一句是模型写的**。
> 条目**原样转录**（含语料自己的措辞、大小写与错拼），本页不替它改。
>
> 因此本页只证明**「文档这么写」**，不证明**「机台这样」**（schema §11）。
> **本页没有被人在真实机台上核对过**（`verified: doc-only`）。

## 这一版改了什么（106 条）

格式：**出处文档 —— 语料原条目**。条目本身带 `MTP 3.0.1:` 前缀，**那是原文的一部分，没有去掉**。

- [Compile the memory test program](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.04.11_Compile_the_memory_test_program.md>) —— MTP 3.0.1: A makefile is created and used during compilation
- [Compile the memory test program](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.04.11_Compile_the_memory_test_program.md>) —— MTP 3.0.1: Multiple instances of the compiler control dialog can be opened
- [Compile the memory test program](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.04.11_Compile_the_memory_test_program.md>) —— MTP 3.0.1: Compiler output is provided in a tab of the dialog
- [Compile the memory test program](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.04.11_Compile_the_memory_test_program.md>) —— MTP 3.0.1: Removed the -r0 option and support for non-binary reconstruction files (.apg.rec files)
- [Debugging](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.01.01_Debugging.md>) —— MTP 3.0.1: The ExecuteEngine test method replaces the Memtest test methods.
- [Failure analysis](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.01.02_Failure_analysis.md>) —— MTP 3.0.1: The ExecuteEngine test method replaces the Memtest test methods.
- [High-volume manufacturing](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.01.03_High-volume_manufacturing.md>) —— MTP 3.0.1: The ExecuteEngine test method replaces the Memtest test methods.
- [Use cases](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.01_Use_cases.md>) —— MTP 3.0.1: The Memtest test methods have been replaced by the ExecutionEngine testmethod
- [Generate vectors and reconstruction information](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.02_Generate_vectors_and_reconstruction_information.md>) —— MTP 3.0.1: Removed the -r0 option and support for non-binary reconstruction files (.apg.rec files)
- [Creating a testflow in SmarTest](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.04_Creating_a_testflow_in_SmarTest.md>) —— MTP 3.0.1: The ExecutionEngine test method replaces the Memtest test methods
- [Adding the ExecutionEngine test method to a testflow](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.01.01_Adding_the_ExecutionEngine_test_method_to_a_testflow.md>) —— MTP 3.0.1: The method for adding test methods to testflows has changed to that used for universal test methods
- [Parameters for the ExecutionEngine test method](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.01.03.01_Parameters_for_the_ExecutionEngine_test_method.md>) —— MTP 3.0.1: The ExecuteEngine test method replaces the Memtest test methods.
- [Setting parameters for the ExecutionEngine test method](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.01.03_Setting_parameters_for_the_ExecutionEngine_test_method.md>) —— MTP 3.0.1: Parameters are now set in the Test Suite window.
- [Memory testing test method](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.01_Memory_testing_test_method.md>) —— MTP 3.0.1: The Memtest test methods have been consolidated into the ExecutionEngine test method
- [EyeFinder theory of operation](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.04.01_EyeFinder_theory_of_operation.md>) —— MTP 3.0.1: Training can now run embedded on the test processor
- [Using EyeFinder](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.04.02_Using_EyeFinder.md>) —— MTP 3.0.1: Added parameters TrainingAlgorithm, out_pins, out_spec_names, in_pins, in_N_pins, in_spec_names; removed parameter period
- [Using EyeFinder](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.04.02_Using_EyeFinder.md>) —— MTP 3.0.1: The EyeFinder is now configured in a window instead of a dialog.
- [Parallel Shmoo test method](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.05_Parallel_Shmoo_test_method.md>) —— MTP 3.0.1: The parallell shmoo test methods have been consolidated into a sinlge test method with an updated interface.
- [SourceSync fast mode](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.06.02.05.01_SourceSync_fast_mode.md>) —— MTP 3.0.1: The test method is now a universal test method.
- [SourceSync fast mode](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.06.02.05.01_SourceSync_fast_mode.md>) —— MTP 3.0.1: The test method is now configured in a window instead of a dialog.
- [SourceSync standard mode](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.06.02.05.02_SourceSync_standard_mode.md>) —— MTP 3.0.1: The test method is now a universal test method.
- [SourceSync standard mode](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.06.02.05.02_SourceSync_standard_mode.md>) —— MTP 3.0.1: The test method is now configured in a window instead of a dialog.
- [Parameters for multistrobe test methods](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.06.02.05_Parameters_for_multistrobe_test_methods.md>) —— MTP 3.0.1: The test methods are now universal test methods.
- [Parameters for multistrobe test methods](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.06.02.05_Parameters_for_multistrobe_test_methods.md>) —— MTP 3.0.1: The test methods are now configured in a window instead of a dialog.
- [DataTraining parameters](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.06.03.03_DataTraining_parameters.md>) —— MTP 3.0.1: The test method is now configured in a window instead of a dialog.
- [Parameters for the DataTraining test method](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.06.03.04_Parameters_for_the_DataTraining_test_method.md>) —— MTP 3.0.1: New parameter TrainingAlgorithm
- [Parameters for the DataTrainingFlex test method](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.06.04.02_Parameters_for_the_DataTrainingFlex_test_method.md>) —— MTP 3.0.1: New parameter TrainingAlgorithm
- [Parameters for the DataTrainingFlex test method](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.06.04.02_Parameters_for_the_DataTrainingFlex_test_method.md>) —— MTP 3.0.1: The test method is now configured in a window instead of a dialog.
- [Driver sharing connections](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.02_Driver_sharing_connections.md>) —— MTP 3.0.1: Support for Y and hybrid sharing
- [Sharing configuration file](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.07.02_Sharing_configuration_file.md>) —— MTP 3.0.1: Introduced completely new syntax to support Y and hybrid sharing
- [Fd_merge tool](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.07.06_Fd_merge_tool.md>) —— MTP 3.0.1: New option -i to specify a comparison file
- [Fd_merge tool](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.07.06_Fd_merge_tool.md>) —— MTP 3.0.1: New option -e to choose a compensation algorithm
- [Fd_merge tool](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.07.06_Fd_merge_tool.md>) —— MTP 3.0.1: New option -H to generate a sample sharing configuration file
- [Fd_merge tool](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.07.06_Fd_merge_tool.md>) —— MTP 3.0.1: Removed option -V for specifying the verbosity level
- [OnlineCompensation syntax](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.09.06_OnlineCompensation_syntax.md>) —— MTP 3.0.1: Parameters are now edited in the Test Suite window
- [SharedContinuity syntax](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.09.09_SharedContinuity_syntax.md>) —— MTP 3.0.1: Parameters are now edited in the Test Suite window
- [SharedContinuity syntax](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.09.09_SharedContinuity_syntax.md>) —— MTP 3.0.1: There are no longer default values for the Shared_Pins and Non_shared_Pins parameters
- [SharedContinuity syntax](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.09.09_SharedContinuity_syntax.md>) —— MTP 3.0.1: New parameters Cross-Terminated Pins and Force Current Cross-Terminated
- [SharedContinuity syntax](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.09.09_SharedContinuity_syntax.md>) —— MTP 3.0.1: New result value Cross-Terminated Voltage(mV)
- [SharedContinuity syntax](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.09.09_SharedContinuity_syntax.md>) —— MTP 3.0.1: Added a shared continuity utility control
- [Setting parameters for the binning handler](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.09.18_Setting_parameters_for_the_binning_handler.md>) —— MTP 3.0.1: Parameters are now edited in the Test Suite window
- [Setting parameters for the binning executor](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.09.20_Setting_parameters_for_the_binning_executor.md>) —— MTP 3.0.1: Parameters are now edited in the Test Suite window
- [Test methods for driver sharing](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.09_Test_methods_for_driver_sharing.md>) —— MTP 3.0.1: Registering test methods is no longer necessary
- [Parameter dialog for mid-level X4 mode](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.08.02.03.01_Parameter_dialog_for_mid-level_X4_mode.md>) —— MTP 3.0.1: Parameters are now edited in the Test Suite window
- [Parameter dialog for mid-level X6 mode](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.08.02.03.02_Parameter_dialog_for_mid-level_X6_mode.md>) —— MTP 3.0.1: Parameters are now edited in the Test Suite window
- [Calibrate test system](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.08.02.03_Calibrate_test_system.md>) —— MTP 3.0.1: Registering test methods is no longer necessary
- [Time adjustment for mid-level termination](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.08_Time_adjustment_for_mid-level_termination.md>) —— MTP 3.0.1: Dynamic driver high level shift is also supported by HSM3G and HSM6800 boards
- [Test methods](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06_Test_methods.md>) —— MTP 3.0.1: Registering test methods is no longer necessary
- [System flags](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.10.01_System_flags.md>) —— MTP 3.0.1: Changed the recommended system flag settings
- [Testflow flags](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.10.02_Testflow_flags.md>) —— MTP 3.0.1: Changed the recommended testflow flag settings
- [Performing a Memory Test](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05_Performing_a_Memory_Test.md>) —— MTP 3.0.1: Registering test methods is no longer necessary
- [MTL Compiler Control dialog](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.02.04.01_MTL_Compiler_Control_dialog.md>) —— MTP 3.0.1: Dialog settings are ignored when the APG pattern file contains the :options: keyword
- [MTL Compiler Control dialog](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.02.04.01_MTL_Compiler_Control_dialog.md>) —— MTP 3.0.1: New options in the MTL Compiler Options section: Overwrite an Existing MTL Define, Define, Disable For-Loop Padding Only, Disable For-Loop Padding and Is/Nis Padding, Optimize Memory Usage
- [MTL Compiler Control dialog](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.02.04.01_MTL_Compiler_Control_dialog.md>) —— MTP 3.0.1: Multiple instances of the dialog can be opened from the MTM
- [MTL Compiler Control dialog](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.02.04.01_MTL_Compiler_Control_dialog.md>) —— MTP 3.0.1: Removed the -r0 option
- [Using the MTL compiler from the GUI](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.02.04_Using_the_MTL_compiler_from_the_GUI.md>) —— MTP 3.0.1: A makefile is created and used during compilation
- [Using the MTL compiler from the GUI](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.02.04_Using_the_MTL_compiler_from_the_GUI.md>) —— MTP 3.0.1: Multiple instances of the compiler control dialog can be opened
- [Using the MTL compiler from the GUI](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.02.04_Using_the_MTL_compiler_from_the_GUI.md>) —— MTP 3.0.1: Compiler output is provided in a tab of the dialog
- [Using the MTL compiler from the GUI](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.02.04_Using_the_MTL_compiler_from_the_GUI.md>) —— MTP 3.0.1: Removed the -r0 option and support for non-binary reconstruction files (.apg.rec files)
- [apgc command syntax](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.02.05.01_apgc_command_syntax.md>) —— MTP 3.0.1: New compiler switches to partially disable padding, to create create a makefile rule, to compress compiled patterns, and to overwrite program variables
- [apgc command syntax](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.02.05.01_apgc_command_syntax.md>) —— MTP 3.0.1: Command line options are ignored when the APG pattern file contains the :options: keyword
- [apgc command syntax](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.02.05.01_apgc_command_syntax.md>) —— MTP 3.0.1: Removed the -r0 option
- [Using the MTL compiler from the command line](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.02.05_Using_the_MTL_compiler_from_the_command_line.md>) —— MTP 3.0.1: Removed -r0 option and support for non-binary reconstruction files (.apg.rec files)
- [APG pattern file syntax](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.02.01_APG_pattern_file_syntax.md>) —— MTP 3.0.1: String macro values can be overwritten from the command line
- [APG pattern file syntax](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.02.01_APG_pattern_file_syntax.md>) —— MTP 3.0.1: Added :options: keyword
- [Preprocessor statements](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.02.02_Preprocessor_statements.md>) —— MTP 3.0.1: String macro values can be overwritten from the command line
- [Other control structures](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01.04_Other_control_structures.md>) —— MTP 3.0.1: nis{} instructions are incompatible with the sequencer mode and will be deprecated.
- [Subroutines](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01.07_Subroutines.md>) —— MTP 3.0.1: delay() is not compatible with PMU type DC events
- [Subroutines](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01.07_Subroutines.md>) —— MTP 3.0.1: Subroutines may not be named REFRESH_CTRL
- [Macros and functions in program files](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01.08_Macros_and_functions_in_program_files.md>) —— MTP 3.0.1: delay() is not compatible with PMU type DC events
- [Macros and functions in program files](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01.08_Macros_and_functions_in_program_files.md>) —— MTP 3.0.1: REFRESH_CTRL function added
- [Device access file syntax](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.04.01_Device_access_file_syntax.md>) —— MTP 3.0.1: Using groups and subgroups no longer recommended
- [Control instructions in device accesses](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.04.03_Control_instructions_in_device_accesses.md>) —— MTP 3.0.1: New instruction delay()
- [Pin mapping file syntax](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.06.01_Pin_mapping_file_syntax.md>) —— MTP 3.0.1: New pin attribute: interruptCtrl
- [Pin mapping file syntax](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.06.01_Pin_mapping_file_syntax.md>) —— MTP 3.0.1: New pin attribute: bitseq
- [Pin mapping file syntax](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.06.01_Pin_mapping_file_syntax.md>) —— MTP 3.0.1: New keyword: configure bus
- [Waveform mapping file syntax](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.07.01_Waveform_mapping_file_syntax.md>) —— MTP 3.0.1: Introduced native and native standard syntax
- [DC event file syntax](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.08.01_DC_event_file_syntax.md>) —— MTP 3.0.1: DC events now support also PMUs
- [Setting up padding](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.02.02_Setting_up_padding.md>) —— MTP 3.0.1: Padding is now supported before and at the end of for loops
- [Setting up padding](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.02.02_Setting_up_padding.md>) —— MTP 3.0.1: Padding is required before certain DC events
- [Setting up padding](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.02.02_Setting_up_padding.md>) —— MTP 3.0.1: Padding can be partly disabled using compiler switches
- [Wavetable syntax](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.03.01.01_Wavetable_syntax.md>) —— MTP 3.0.1: Introduced native and native standard syntax.
- [Automatic waveform generation](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.03.03_Automatic_waveform_generation.md>) —— MTP 3.0.1: When the sequencer mode is used, no replicated wavetables are generated
- [Setting up the generation of reconstruction information](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.11.01_Setting_up_the_generation_of_reconstruction_information.md>) —— MTP 3.0.1: Removed the -r0 option
- [Reconstruction information](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.11_Reconstruction_information.md>) —— MTP 3.0.1: Removed the -r0 option and support for serialized object tree output (.apg.rec files)
- [Setting up a maintenance operation](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.12.01_Setting_up_a_maintenance_operation.md>) —— MTP 3.0.1: New mode for dynamic refreshes: sequencer
- [Wavetables for maintenance operations](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.12.03_Wavetables_for_maintenance_operations.md>) —— MTP 3.0.1: Sequencer mode requires no special wavetables
- [Maintenance operations](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.12_Maintenance_operations.md>) —— MTP 3.0.1: New mode for dynamic refresh: sequencer
- [Maintenance operations](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.12_Maintenance_operations.md>) —— MTP 3.0.1: PMU type DC events may prevent timely refreshes
- [Maintenance operations](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.12_Maintenance_operations.md>) —— MTP 3.0.1: Maintenance operation can be enabled and disabled under program control
- [Specifying DC event details](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.13.01.01_Specifying_DC_event_details.md>) —— MTP 3.0.1: Two procedures added for specifying PMU type events
- [Setting up a DC event](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.13.01_Setting_up_a_DC_event.md>) —— MTP 3.0.1: DC events now support also PMUs
- [Setting up DC event sequences](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.13.02_Setting_up_DC_event_sequences.md>) —— MTP 3.0.1: Event sequences do not support PMU events
- [Controlling power supply and measurements](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.13_Controlling_power_supply_and_measurements.md>) —— MTP 3.0.1: DC events now support also PMUs
- [MTL compiler directories and file name extensions](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.05.01_MTL_compiler_directories_and_file_name_extensions.md>) —— MTP 3.0.1: Removed non-binary reconstruction files (.apg.rec files)
- [MTP tools overview](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.03.01_MTP_tools_overview.md>) —— MTP 3.0.1: The Memtest test methods have been consolidated into the ExecutionEngine test method
- [MTP tools overview](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.03.01_MTP_tools_overview.md>) —— MTP 3.0.1: The MTDC tool has been added
- [MTP tools overview](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.03.01_MTP_tools_overview.md>) —— MTP 3.0.1: The PDebug tool has been added
- [Operating principles of the BFM Viewer](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.04.01_Operating_principles_of_the_BFM_Viewer.md>) —— MTP 3.0.1: The ExecutionEngine test method replaces the Memtest test methods
- [Executing a memory test with the Memtest Execute test method](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.05.03.04_Executing_a_memory_test_with_the_Memtest_Execute_test_method.md>) —— MTP 3.0.1: The Memtest test methods have been replaced by the ExecutionEngine test method
- [Analyzing results using the Bit Fail Map Viewer](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.05.03.06_Analyzing_results_using_the_Bit_Fail_Map_Viewer.md>) —— MTP 3.0.1: The Memtest test methods have been replaced by the ExecutionEngine test method
- [DataTraining parameters](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.05.04.06.03.03_DataTraining_parameters.md>) —— MTP 3.0.1: The test method is now configured in a window instead of a dialog.
- [Parameters for the DataTraining test method](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.05.04.06.03.04_Parameters_for_the_DataTraining_test_method.md>) —— MTP 3.0.1: New parameter TrainingAlgorithm
- [Parameters for the DataTrainingFlex test method](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.05.04.06.04.02_Parameters_for_the_DataTrainingFlex_test_method.md>) —— MTP 3.0.1: New parameter TrainingAlgorithm
- [Parameters for the DataTrainingFlex test method](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.05.04.06.04.02_Parameters_for_the_DataTrainingFlex_test_method.md>) —— MTP 3.0.1: The test method is now configured in a window instead of a dialog.
- [Test solutions for devices with source-sync interface](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.05.04.06_Test_solutions_for_devices_with_source-sync_interface.md>) —— MTP 3.0.1: Registering test methods is no longer necessary


## 这一版新引入（33 条）

语料原句是 `Introduced in …`，说的是「**这篇文档描述的东西从这一版开始有**」。条目短，所以**文档放前面、原句放后面**：

- [TDEX (Test Data Extension)](<02_System_reference/02.06_Command_Reference/02.06.02.02.255_TDEX__Test_Data_Extension.md>) —— Introduced in MTP 3.0.1
- [GDDR5 training configuration file](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.03.01_GDDR5_training_configuration_file.md>) —— Introduced in MTP 3.0.1
- [LoadConfig test method](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.03.02_LoadConfig_test_method.md>) —— Introduced in MTP 3.0.1
- [Address Training test method](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.03.03_Address_Training_test_method.md>) —— Introduced in MTP 3.0.1
- [Address Bus Inversion Training test method](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.03.04_Address_Bus_Inversion_Training_test_method.md>) —— Introduced in MTP 3.0.1
- [Clock Training test method](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.03.05_Clock_Training_test_method.md>) —— Introduced in MTP 3.0.1
- [Read Training test method](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.03.06_Read_Training_test_method.md>) —— Introduced in MTP 3.0.1
- [Write Training test method](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.03.07_Write_Training_test_method.md>) —— Introduced in MTP 3.0.1
- [GDDR5 Training test method](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.03.08_GDDR5_Training_test_method.md>) —— Introduced in MTP 3.0.1
- [ChangeSpecification test method](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.03.09_ChangeSpecification_test_method.md>) —— Introduced in MTP 3.0.1
- [Print output](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.03.10_Print_output.md>) —— Introduced in MTP 3.0.1
- [GDDR5 training test methods](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.03_GDDR5_training_test_methods.md>) —— Introduced in MTP 3.0.1
- [Identifying sites](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.07.04_Identifying_sites.md>) —— Introduced in MTP 3.0.1
- [Overview of the ready-made test methods](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.09.02_Overview_of_the_ready-made_test_methods.md>) —— Introduced in MTP 3.0.1
- [ResetOverCurrentProtection test method](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.09.07_ResetOverCurrentProtection_test_method.md>) —— Introduced in MTP 3.0.1
- [SharedContinuity test method](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.09.08_SharedContinuity_test_method.md>) —— Introduced in MTP 3.0.1
- [SharedLeakageParallel test method](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.09.11_SharedLeakageParallel_test_method.md>) —— Introduced in MTP 3.0.1
- [SharedLeakageParallel syntax](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.09.12_SharedLeakageParallel_syntax.md>) —— Introduced in MTP 3.0.1
- [SharedIDD test method](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.09.13_SharedIDD_test_method.md>) —— Introduced in MTP 3.0.1
- [SharedIDD syntax](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.09.14_SharedIDD_syntax.md>) —— Introduced in MTP 3.0.1
- [SharedVBump test method](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.09.15_SharedVBump_test_method.md>) —— Introduced in MTP 3.0.1
- [SharedVBump syntax](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.09.16_SharedVBump_syntax.md>) —— Introduced in MTP 3.0.1
- [Verifying the DUT board](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.08.02_Verifying_the_DUT_board.md>) —— Introduced in MTP 3.0.1
- [MTL Defines](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.02.04.01.01_MTL_Defines.md>) —— Introduced in MTP 3.0.1
- [Buses](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.06.02_Buses.md>) —— Introduced in MTP 3.0.1
- [Copying vectors](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.06.04_Copying_vectors.md>) —— Introduced in MTP 3.0.1
- [Device access delays](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.05_Device_access_delays.md>) —— Introduced in MTP 3.0.1
- [Enabling and disabling maintenance operations in APG program file](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.12.02_Enabling_and_disabling_maintenance_operations_in_APG_program_file.md>) —— Introduced in MTP 3.0.1
- [Differences between DCScale type and PMU type events](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.13.01.02_Differences_between_DCScale_type_and_PMU_type_events.md>) —— Introduced in MTP 3.0.1
- [Limitations of PMU type DC events](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.13.01.03_Limitations_of_PMU_type_DC_events.md>) —— Introduced in MTP 3.0.1
- [Converting MTP testflows to UTM](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.06.01_Converting_MTP_testflows_to_UTM.md>) —— Introduced in MTP 3.0.1
- [convertTestflow](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.06_convertTestflow.md>) —— Introduced in MTP 3.0.1
- [Diagnostic output](<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.31.06_Diagnostic_output.md>) —— Introduced in MTP 3.0.1


## 出处

- 抽取自 raw 的 `## Functional changes` 段落；**本页正文列出 139 条**，涉及 **104 篇**文档。
- 抽取器：`extract/versions.py`（纯脚本）；机器可读全量：`extract/version-facts.csv`。
- **本页没有逐篇回读 raw 原文**——条目是段落级抽取的结果。若要据此下结论，请点开对应出处链接核对。
