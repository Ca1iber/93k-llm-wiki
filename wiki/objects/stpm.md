---
type: object
title: SmarTest Program Manager
layer: L3
stage: project
tags: [stpm, test-program-management, gui, mtp, stp, tpt]
related: [stpm-control-file, stpm-merge-rules-file, project, tpt-generate-device-dir, device-directory]
sources:
  - 02_System_reference/02.09_Test_Program_Management/02.09.02_SmarTest_Program_Manager.md
created: 2026-09-18
updated: 2026-09-20
verified: doc-only
---

# SmarTest Program Manager

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **136,660 字符逐字取自** `<02_System_reference/02.09_Test_Program_Management/02.09.02_SmarTest_Program_Manager.md>` 及其子主题 `<02_System_reference/02.09_Test_Program_Management/02.09.02.02.01_Creating_and_editing_an_STPM_control_file.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.01_Structure_of_an_STPM_control_file.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.02_File_and_parameter_settings.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.04_write_tp.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.05_add_test.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.06_add_burst.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.07_add_test_to_burst.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.08_add_empty_test_group.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.09_remove_test.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.10_replace_test.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.11_remove_label.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.12_add_pattern.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.13_replace_pattern.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.14_tpt_generate_template.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.15_tpt_import_from_device.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.16_tpt_generate_device_dir.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.17_tpt_merge.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.18_tpt_add_test.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.19_tpt_replace_test.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.20_tpt_generate_tp.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.21_tpt_compare_tp.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.22_tpt_generate_test_stages.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.23_extract_subflow.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.24_merge_subflow.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.25_remove_subflow.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.26_clear_duplicated.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.27_clear_unused.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.01_STPM_merge_rules_file_syntax.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.02_new_digital_pin.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.03_overwrite_digital_pin_no.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.04_merge_digital_pin_dir.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.05_new_dps_pin.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.06_overwrite_dps_pin_polarity.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.07_new_pin_group.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.08_overwrite_pin_group.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.09_merge_unused_pin_group.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.10_new_port.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.11_overwrite_port.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.12_new_site.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.13_overwrite_channel.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.14_new_timing_equation_set.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.15_new_waveform.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.16_modify_waveform_index.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.17_overwrite_statemap.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.18_new_level_resource.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.19_overwrite_level_resource.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.20_new_level_equation_set.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.21_new_level_set.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.22_new_ac_specset.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.23_new_dc_specset.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.24_overwrite_ac_spec_typ.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.25_overwrite_ac_spec_minmax.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.26_overwrite_dc_spec_typ.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.27_overwrite_dc_spec_minmax.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.28_overwrite_label_wvt.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.29_overwrite_flow_var_value.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.05.01_Test_suite_table_of_a_TPT.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.05.02_Bin_table_of_a_TPT.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.05.03_Test_table_of_a_TPT.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.05.04_Test_parameter_table_of_a_TPT.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.05.05_Test_flag_table_of_a_TPT.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.05.06_Test_stage_table_of_a_TPT.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.06_STPM_command_line_options.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Using SmarTest Program Manager › Creating and editing an STPM control file）

See the example file in `Structure of an STPM control file`（raw: `02.09.02.03.01_Structure_of_an_STPM_control_file.md`）.

### Example（取自子主题 STPM control file › Structure of an STPM control file）

Sample control file with support for test methods and binning:

```
##############################
# Input: Device Test Program Location
##

##############################
# Configuration
##

# Master Test Program (MTP) device path
mtp_device_testflow = '/home/user/93K_Device/project.tf'

# Merge Rules file.
merge_rules = '/home/user/setup/merge_rules.py'

##############################
# Integration Commands
##

add_test(
    test_flow_file = './home/user/new1_93k/testflow/test.tf', # Link to new test flow file
    test = 'test_n1' # test name
    )
add_test(
    test_flow_file = './home/user/new2_93k/testflow/test.tf', # Link to new test flow file
    test = 'test_n2', # target test name
    position = 'first',
    lev_reuse = 'auto'
    )

##############################
# Output: Device Test Program Location
##

# Write Master Test Program (MTP).
write_tp = '/home/user/93K_Device/project.tf'
```

### Syntax（取自子主题 STPM control file › File and parameter settings）

```
mtp_device_testflow = '<testflow_file>'
[mtp_template_dir = '<tpt_dir>']
[merge_rules = '<rules_file>']
[ate_target = '<platform>']
[ate_model = '<model>']
[ate_version = '<version>']
[temp_dir = '<temp_dir>']
[enable_backup = '<backup?>']
```

### Parameters（取自子主题 STPM control file › File and parameter settings）

The parameters of the commands in the order in which they are listed above:

| mtp_device_testflow | <testflow_file> (string) is the name and path of the testflow file of the MTP which STPM is to modify or otherwise work with.<br><br>It can be an absolute or a relative path. If it is a relative path, the base directory is the current working directory at the time STPM was called. |
|---|---|
| mtp_template_dir | <tpt_dir> (string) is the name and path of the directory containing the test program template (TPT).<br><br>It can be an absolute or a relative path. If it is a relative path, the base directory is the current working directory at the time STPM was called.<br><br>This is an optional parameter. Note, however, that some commands require a valid TPT to be specified. This is noted in these commands' descriptions. |
| merge_rules | <rules_file> (string) is the name and path of the merge rules file to use when adding or replacing tests.<br><br>It can be an absolute or a relative path. If it is a relative path, the base directory is the current working directory at the time STPM was called.<br><br>This is an optional parameter. If it is not specified, no merge rules file is used. |
| ate_target | <platform> (string) indicates the type of V93000 architecture on which the test program will run:<br><br>- '93000SS': Smart Scale system |
| ate_model | <model> (string) indicates the specific test system on which the test program will run.<br><br>The available settings depend on the specified ate_target.<br><br>For '93000SS', you can specify:<br><br>- 'PS1600'<br><br>This is an optional parameter. If it is omitted, the default used depends on the setting for ate_target: |
| ate_version | <version> (string) is the release number of the SmarTest version under which the test program will be running.<br><br>This is an optional parameter. If it is omitted, "7.1.4" is used. |
| temp_dir | <temp_dir> is the directory to which STPM writes temporary files.<br><br>It can be an absolute or a relative path. If it is a relative path, the base directory is the current working directory at the time STPM was called.<br><br>Make sure that the directory already exists and that STPM has write privileges in the specified directory.<br><br>This is an optional parameter. If it is omitted, /tmp is used (the tmp subdirectory of the root directory). |
| enable_backup | <backup?> (number) specifies whether STPM generates a backup copy of each modified file:<br><br>- 0: No backups are generated.<br>- 1: Backups are generated.<br><br>When backup files are generated, they are stored in a subdirectory of the directory in which the original file is located; the subdirectory is named back.<br><br>The name of the backup file is the same as the original file name, with a timestamp in the form "_YYMMDD_HHMMSS" appended.<br><br>For example, the backup copy of a pin configuration file mypins.cfg that is created on 2 November 2012 at 21:43:23 is stored as <device_directory>/configuration/back/mypins_121102_214323.cfg.<br><br>This is an optional parameter. If it is omitted, 1 is used (that is, backups are generated). |

### Example（取自子主题 STPM control file › File and parameter settings）

See the sample control file in `Structure of an STPM control file`（raw: `02.09.02.03.01_Structure_of_an_STPM_control_file.md`）.

### Syntax（取自子主题 STPM control file › Preprocessing and postprocessing scripts）

Both the pre_proc (shown below) and post_proc parameters have the same syntax.

```
pre_proc = '<script>[&mdir][&sdir][&mtp_tf][&mtp_pmf][&mtp_conf][&mtp_tim][&mtp_lev][&mtp_tt][&mtp_rout][&mtp_wf][&mtp_anctrl][&mtp_chatt][&mtp_prot][&mtp_att][&stp_tf][&stp_pmf][&stp_conf][&stp_tim][&stp_lev][&stp_tt][&stp_rout][&stp_wf][&stp_anctrl][&stp_chatt][&stp_prot][&stp_att][<user_parameters>]'
```

The available script parameters in the order in which they are listed above:

| <script> | The name and path of the script file to call.<br><br>The path can be absolute or relative. If it is a relative path, the base directory is the current working directory at the time STPM was called. |
|---|---|
| &mdir | Full path to the MTP directory. |
| &sdir | Full path to the STP directory. |
| &mtp_tf | Full path to the MTP testflow file. |
| &mtp_pmf | Full path to the MTP pattern master file. |
| &mtp_conf | Full path to the MTP configuration file. |
| &mtp_tim | Full path to the MTP timing file. |
| &mtp_lev | Full path to the MTP levels file. |
| &mtp_tt | Full path to the MTP test table file. |
| &mtp_rout | Full path to the MTP routing file. |
| &mtp_wf | Full path to the MTP waveform file. |
| &mtp_anctrl | Full path to the MTP analog control file. |
| &mtp_chatt | Full path to the MTP channel attributes file. |
| &mtp_prot | Full path to the MTP protocols file. |
| &mtp_att | Full path to the MTP pin attributes file. |
| &stp_tf | Full path to the STP testflow file. |
| &stp_pmf | Full path to the STP pattern master file. |
| &stp_conf | Full path to the STP configuration file. |
| &stp_tim | Full path to the STP timing file. |
| &stp_lev | Full path to the STP levels file. |
| &stp_tt | Full path to the STP test table file. |
| &stp_rout | Full path to the STP routing file. |
| &stp_wf | Full path to the STP waveform file. |
| &stp_anctrl | Full path to the STP analog control file. |
| &stp_chatt | Full path to the STP channel attributes file. |
| &stp_prot | Full path to the STP protocols file. |
| &stp_att | Full path to the STP pin attributes file. |
| <user_parameters> | Text that is passed unchanged to the script. This text must not contain any words that begin with &. |

Except for the name of the script file, all elements are optional.

### Example（取自子主题 STPM control file › Preprocessing and postprocessing scripts）

This example executes the write_tp command with two scripts:

- Before write_tp itself is executed, the preparation.py script from the current working directory is run. No parameters are passed to this script.
- After write_tp has finished executing, the cleanup.pl script is run. This script receives this parameter string (assuming that the MTP is located in /user/johndoe/mtp):

`--mdir '/user/johndoe/mtp' --cmd write --stage 3`

```
write_tp('user/johndoe/mtp/flow1.tf',
         pre_proc  = 'preparation.py',
         post_proc = '/usr/tools/scripts/cleanup.pl &mdir --cmd write --stage 3')
```

### Syntax（取自子主题 STPM control file › write tp）

```
write_tp(
    path = '<mtp_target_file>',
[pre_proc = <pre_proc>, ]
[post_proc = <post_proc>]
)
```

### Parameters（取自子主题 STPM control file › write tp）

The parameters in the order in which they are listed above:

| path | <mtp_target_file> (string) is the name and location under which STPM saves the MTP (master test program) testflow file after it has modified it.<br><br>It can be an absolute or a relative path. If it is a relative path, the base directory is the current working directory at the time STPM was called.<br><br>You can specify the same file here as for mtp_device_testflow. In that case, the original file is modified in place.<br><br>(You can still have STPM automatically create a backup of the MTP; see `enable_backup`（raw: `02.09.02.03.02_File_and_parameter_settings.md`） for details.) |
|---|---|
| pre_proc | <pre_proc> is a script that is executed before this command.<br><br>The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.<br><br>This is an optional parameter. |
| post_proc | <post_proc> is a script that is executed after this command.<br><br>The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.<br><br>This is an optional parameter. |

```

```

### Example（取自子主题 STPM control file › write tp）

See the sample control file in `Structure of an STPM control file`（raw: `02.09.02.03.01_Structure_of_an_STPM_control_file.md`）.

### Syntax（取自子主题 STPM control file › add test）

```
add_test(
test_flow_file = '<testflow_file>',
[test_source = '<test_source>', ]
[test_group = '<test_group>', ]
[test = '<test>', ]
[position  = '<position>', ]
[tim_reuse = '<timing_reuse>', ]
[lev_reuse = '<level_reuse>', ]
[pat_reuse = '<pattern_reuse>', ]
[reuse_scope = '<scope>', ]
[pat_dir = '<path>', ]
[test_flags  = [<test_flags>], ]
[test_method = '<method>', ]
[test_params = {<params>}, ]
[sbin_num = <sbin_num>,]
[sbin_label  = '<sbin_label>', ]
[hbin_num  = <hbin_num>,]
[hbin_label = '<hbin_label>', ]
[pre_proc = <pre_proc>, ]
[post_proc = <post_proc>]
)
```

### Parameters（取自子主题 STPM control file › add test）

The parameters in the order in which they are listed above:

| test_flow_file | <testflow_file> (string) is the path, including the name, of the testflow file of the source test program (STP) that contains the test that you want to add to the MTP.<br><br>The path can be either absolute or relative to the current working directory. |
|---|---|
| test_source | <test_source> (string) is the name of the test from the STP that will be added to the MTP.<br><br>If the STP contains only a single test, the test_source parameter can be omitted. If the STP contains multiple tests, test_source is required. |
| test_group | <test_group> (string) is the testflow group in which the test suite is generated.<br><br>If this parameter is not specified, the test suite is generated at the root of the MTP, at the end of the testflow. |
| test | <test> is the name for the added test in the MTP.<br><br>If this parameter is omitted, the name is added to the MTP with the same name that it has in the STP.<br><br>If there is already a test with the same name in the MTP, the test from the STP is not added and an error is generated. (This applies in both cases, whether you have specified a name using the test parameter or whether the default name is used.) |
| position | <position> (string) is the position within a test group where the new test is inserted.<br><br>The following values are available:<br><br>- optimal: STPM inserts the test in a position in the testflow group that requires the least amount of level and timing reloads during execution.<br>- first: The test suite is inserted as the first test in the testflow group.<br>- last: The test suite is inserted as the last in the testflow group.<br>- after:<test_name>: The test suite is inserted immediately after the test suite with the name <test_name> in the testflow group.<br>- before:<test_name>: The test suite is inserted immediately before the test suite with the name <test_name> in the testflow group.<br><br>If this parameter is omitted, optimal is used.<br><br>If the test_group parameter (see above) is omitted, the position parameter is ignored. |
| tim_reuse | <timing_reuse> (string) is the way in which timing settings in the MTP are to be reused for the added test:<br><br>- auto: STPM tries to reuse an existing timing, merging the timing from the new test with it. If this is not possible, a new timing is created.<br>- test:<test-name>: The timing from the existing test suite with the name <test-name> is used for the added test.<br>- <primary-keys>: You can explicitly specify the timing to use. How to do this differs for single-port and multiport tests:<br><br>- Single-port timing: Specify the timing as a combination of indexes, separated by periods: <eqnset-index>`.`<timset-index>`.`<specset-index><br>- Multiport timing: Specify the name of the multiport specification to use.<br><br>- none: STPM will not try to reuse any timing. Instead, it always creates new timing for the added test.<br><br>If this parameter is omitted, none is used. |
| lev_reuse | <level_reuse> (string) is the way in which level settings in the MTP are to be reused for the added test:<br><br>- auto: STPM tries to reuse existing levels, merging the levels from the new test with hem. If this is not possible, new levels are created.<br>- test:<test-name>: The levels from the existing test suite with the name <test-name> are used for the added test.<br>- <primary-keys>: You can explicitly specify the levels to use as a combination of indexes, separated by periods:<br><br><eqnset-index>`.`<levelset-index>`.`<specset-index><br><br>- none: STPM will not try to reuse any levels. Instead, it always creates new levels for the added test.<br><br>If this parameter is omitted, none is used. |
| pat_reuse | <pattern_reuse> (string) is the way in which patterns in the MTP are to be reused for the added test:<br><br>- test:<test-name>: The patterns from the existing test suite with the name <test-name> are used for the added test.<br>- <pattern-label>: You can explicitly specify the patterns to use by providing the name of the pattern label.<br>- none: STPM will not try to reuse any patterns. Instead, it always creates new patterns for the added test.<br><br>If this parameter is omitted, none is used. |
| reuse_scope | <scope> (string or list of strings) are the testflow groups that STPM is to analyze for purposes of merging or reusing primaries. STPM will ignore primaries from other testflow groups.<br><br>The scope can be:<br><br>- `"*all*"` to tell STPM to consider all groups<br>- A comma-separated list of testflow groups, enclosed in square brackets<br><br>If this parameter is not specified, the default is for STPM to consider the test suites in the testflow group specified in the test_group parameter (see above).<br><br>If test_group is not specified either, all groups are considered. |
| pat_dir | <path> (string) is the path of the directory where STPM is to store patterns that it copies from the STP to the device directory.<br><br>The path is relative to the vectors subdirectory of the device directory.<br><br>If this parameter is omitted, patterns is used. (That is, the patterns are copied to the vectors/patterns/ subdirectory of the device directory.) |
| test_flags | <test_flags> (list of strings) is a list of test suite flags that are enabled for the imported test. The list must be enclosed in square brackets.<br><br>Include in the list each test suite flag you want to be enabled for the test in the MTP, enclosed in quotes and separated by commas.<br><br>You can specify all flags supported in SmarTest. Use these spellings:<br><br>- bypass<br>- fail_per_label<br>- ffc_enable<br>- ffc_scan_enable<br>- ffv_enable<br>- frg_enable<br>- frg_single_shot<br>- hold<br>- hold_on_fail<br>- mx_waves_enable<br>- output_on_fail<br>- output_on_pass<br>- per_pin_on_fail<br>- per_pin_on_pass<br>- set_pass<br>- set_fail<br>- value_on_fail<br>- value_on_pass<br><br>For example: `test_flags = ['hold_on_fail','per_pin_on_fail']`<br><br>If this parameter is omitted, no flags are enabled for the test. |
| test_method | <method> (string) is the class of the test method of the test being added (for example, "ac_tml.AcTest.FunctionalTest").<br><br>If this parameter is omitted, the test is added to the MTP with the same type that it has in the STP. |
| test_params | <params> (list of name/value pairs) is a list of parameter values with which to call the test method.<br><br>This is a list of name/value pairs that are separated by commas; the entire list is wrapped in curly braces: {<name>':'<value>',...}<br><br>Each name and value is a string, both are separated by a colon:<br><br>- <name> is the name of a parameter that is known to the test method.<br>- <value> is the value that is passed into this parameter when the test method is called.<br><br>For example: `test_params = {'param1':'0','my_param':'CLK'}`<br><br>This is an optional parameter. If it is omitted, no parameters are passed to the test method. |
| sbin_num | <sbin_num> (string) is the software bin ID of the bin associated with the added test.<br><br>To be compatible with the SmarTest Data Formatter, the number must be between 0 and 32767.<br><br>This is an optional parameter; if hbin_num (see below) is specified, it is required. If it is omitted, a "Run" node without any associated bin is inserted in the test flow. |
| sbin_label | <description> (string) is a short text describing the purpose of the software bin. It is intended for human readers.<br><br>This is an optional parameter. If it is omitted, the bin remains unlabeled. |
| hbin_num | <hbin_num> (number) is the ID of the hardware bin connected to the software bin you are defining.<br><br>This is an optional parameter. If sbin_num (see above) is not specified, the hbin_num parameter cannot be specified. |
| hbin_label | <hbin_label> (string) is a short text describing the purpose of the hardware bin. It is intended for human readers.<br><br>This is an optional parameter. If it is omitted, the bin remains unlabeled. |
| pre_proc | <pre_proc> is a script that is executed before this command.<br><br>The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.<br><br>This is an optional parameter. |
| post_proc | <post_proc> is a script that is executed after this command.<br><br>The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.<br><br>This is an optional parameter. |

### Example（取自子主题 STPM control file › add test）

See the sample control file in `Structure of an STPM control file`（raw: `02.09.02.03.01_Structure_of_an_STPM_control_file.md`）.

### Syntax（取自子主题 STPM control file › add burst）

```
add_burst(
name       = '<burst_name>',
[ports      = ('<port>', ... ),]
[pre_proc   = <pre_proc>,          ]
[post_proc  = <post_proc>]
)
```

### Parameters（取自子主题 STPM control file › add burst）

The parameters in the order in which they are listed above:

| name | <testflow_file> (string) is the path, including the name, of the testflow file of the source test program (STP) that contains the test that you want to add to the MTP.<br><br>The path can be either absolute or relative to the current working directory. |
|---|---|
| ports | <ports> (list of strings) is a list of the ports for which the burst will be generated.<br><br>You can list any number of ports. Each port must be an individual string, the strings must be separated by commas, and the list must be enclosed in parentheses.<br><br>This parameter is optional. If it is not specified, STPM creates a single-port burst. |
| pre_proc | <pre_proc> is a script that is executed before this command.<br><br>The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.<br><br>This is an optional parameter. |
| post_proc | <post_proc> is a script that is executed after this command.<br><br>The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.<br><br>This is an optional parameter. |

### Syntax（取自子主题 STPM control file › add test to burst）

```
add_test_to_burst(
test_flow_file = '<testflow_file>',
[test_source    = '<test_source>',      ]
test           = '<test>',
[position       = '<position>',         ]
[pat_dir        = '<path>',             ]
[pat_reuse      = '<mode>',]
[pre_proc       = <pre_proc>,           ]
[post_proc      = <post_proc>]
)
```

### Parameters（取自子主题 STPM control file › add test to burst）

The parameters in the order in which they are listed above:

| test_flow_file | <testflow_file> (string) is the path (including the name) of the testflow file of the source test program (STP) that contains the test that you want to add to the test in the MTP.<br><br>The path can be either absolute or relative to the current working directory. |
|---|---|
| test_source | <test_source> (string) is the name of the test from the STP that will be added to the MTP.<br><br>If the STP contains only a single test, the test_source parameter can be omitted. If the STP contains multiple tests, test_source is required. |
| test | <test> (string) is the name of the existing test in the MTP. The test from the STP is added to this test. |
| position | <position> (string) is the position within the existing pattern burst where the new test is inserted.<br><br>The following values are available:<br><br>- first: STPM inserts the pattern from the STP at the beginning of the test (burst) in the MTP.<br>- last: The pattern from the STP is inserted at the end of the test (burst) in the MTP.<br>- after:<label_name>: The pattern from the STP is inserted immediately after the label with the name <label_name> in the test in the MTP.<br>- before:<label_name>: The pattern from the STP is inserted immediately before the label with the name <label_name> in the test in the MTP.<br><br>If this parameter is omitted, last is used. |
| pat_dir | <path> (string) is the path of the directory where STPM is to store patterns that it copies from the STP to the device directory.<br><br>The path is relative to the vectors subdirectory of the device directory.<br><br>If this parameter is omitted, patterns is used. (That is, the patterns are copied to the vectors/patterns/ subdirectory of the device directory.) |
| pat_reuse | <mode> (string) is the way in which patterns in the MTP are to be reused for the test that is added to the burst:<br><br>- test:<test-name>: The patterns from the existing test suite with the name <test-name> are used for the added test.<br>- <pattern-label>: You can explicitly specify the patterns to use by providing the name of the pattern label.<br>- none: STPM will not try to reuse any patterns. Instead, it always creates new patterns for the added test.<br><br>If this parameter is omitted, none is used. |
| pre_proc | <pre_proc> is a script that is executed before this command.<br><br>The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.<br><br>This is an optional parameter. |
| post_proc | <post_proc> is a script that is executed after this command.<br><br>The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.<br><br>This is an optional parameter. |

### Example（取自子主题 STPM control file › add test to burst）

See the sample control file in `Structure of an STPM control file`（raw: `02.09.02.03.01_Structure_of_an_STPM_control_file.md`）.

### Syntax（取自子主题 STPM control file › add empty test group）

```
add_empty_test_group(
test_group  = '<test_group>',
[description = '<description>',]
[parent = '<parent>', ]
[position = '<position>', ]
[pre_proc = <pre_proc>, ]
[post_proc = <post_proc>]
)
```

### Parameters（取自子主题 STPM control file › add empty test group）

The parameters in the order in which they are listed above:

| test_group | <test_group> (string) is the name of the new test group you want to create in the MTP. |
|---|---|
| description | <description> is a brief statement about the purpose of the new test group.<br><br>This parameter is intended just for humans; omitting it does not in any way affect the function of the test group.<br><br>This is an optional parameter. If it is omitted, no description is stored with the test group. |
| parent | <parent> (string) is the name of the test group in which the new test group will be created.<br><br>The test group you name as the parent must already exist in the MTP.<br><br>This is an optional parameter. If it is not specified, the test group is created at the top level of the MTP. |
| position | <position> (string) is the position within the parent where the new test group is created.<br><br>The following values are available:<br><br>- first: The test group is created at the beginning of the parent.<br>- last: The test group is created at the end of the parent.<br><br>If this parameter is omitted, last is used. |
| pre_proc | <pre_proc> is a script that is executed before this command.<br><br>The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.<br><br>This is an optional parameter. |
| post_proc | <post_proc> is a script that is executed after this command.<br><br>The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.<br><br>This is an optional parameter. |

### Syntax（取自子主题 STPM control file › remove test）

```
remove_test(
test = '<test>',
[tim_remove = '<timing_remove>', ]
[lev_remove = '<level_remove>', ]
[pat_remove = '<pattern_remove>', ]
[test_remove = <test_remove>, ]
[keep_pat_label = <keep_label>, ]
[pre_proc = <pre_proc>, ]
[post_proc = <post_proc>]
)
```

### Parameters（取自子主题 STPM control file › remove test）

The parameters in the order in which they are listed above:

| test | <test> (string) is the name of the test suite in the MTP that STPM should remove. |
|---|---|
| tim_remove | <timing_remove> is an instruction for STPM on how to remove the timing settings of the removed test:<br><br>- unused: STPM removes the settings if no other test uses them. (STPM may not be able to detect usage by tests that switch primaries in the C++ code.)<br>- none: The timing settings are not removed, even if no other test uses them.<br><br>If this parameter is omitted, unused is used. |
| lev_remove | <level_remove> (string) is an instruction for STPM on how to remove the levels of the removed test:<br><br>- unused: STPM removes the levels if no other test uses them. (STPM may not be able to detect usage by tests that switch primaries in the C++ code.)<br>- none: The levels are not removed, even if no other test uses them.<br><br>If this parameter is omitted, unused is used. |
| pat_remove | <pattern_remove> (string) is an instruction for STPM on how to remove the patterns of the removed test:<br><br>- unused: STPM removes the patterns if no other test uses them. (STPM may not be able to detect usage by tests that switch primaries in the C++ code.)<br>- none: The patterns are not removed, even if no other test uses them.<br><br>If this parameter is omitted, unused is used. |
| test_remove | <test_remove> (number) specifies whether the test suite is removed from the MTP:<br><br>- 0: The test suite is not removed.<br>- 1: The test suite is removed.<br><br>You can still remove timing, level, or patterns as described above. Indexes in the test suite that point to removed primaries are reset.<br><br>This parameter is optional. If it is not specified, the test suite is removed (as if you had specified `test_remove = 1`.) |
| keep_pat_label | <keep_label> (number) specifies whether the test suite labels in the MTP are kept when the test is removed:<br><br>- 0: The pattern labels are removed from the MTP.<br>- 1: The pattern labels are kept in the MTP.<br><br>This parameter is optional. If it is not specified, the labels are removed (as if you had specified `keep_pat_label = 0`.)<br><br>This parameter is ignored if `test_remove = 0` is specified |
| pre_proc | <pre_proc> is a script that is executed before this command.<br><br>The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.<br><br>This is an optional parameter. |
| post_proc | <post_proc> is a script that is executed after this command.<br><br>The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.<br><br>This is an optional parameter. |

### Syntax（取自子主题 STPM control file › replace test）

```
replace_test(
test_flow_file = '<testflow_file>',
[test_source = '<test_source>', ]
test = '<test>',
[tim_reuse = '<timing_reuse>', ]
[lev_reuse = '<level_reuse>', ]
[pat_reuse = '<pattern_reuse>', ]
[reuse_scope  = '<scope>', ]
[copy_test_method = '<copy_tm_att>', ]
[tim_remove = '<timing_remove>', ]
[lev_remove = '<level_remove>', ]
[pat_remove = '<pattern_remove>', ]
[pat_dir = '<path>', ]
[pre_proc = <pre_proc>, ]
[post_proc = <post_proc>]
)
```

### Parameters（取自子主题 STPM control file › replace test）

The parameters in the order in which they are listed above:

| test_flow_file | <testflow_file> (string) is the path (including the name) of the testflow file of the source test program (STP) that contains the test with which you want to replace an existing test in the MTP.<br><br>The path can be either absolute or relative to the current working directory. |
|---|---|
| test_source | <test_source> (string) is the name of the test from the STP that will be used to replace the existing test in the to the MTP.<br><br>If the MTP already contains a test by that name and the primaries are already set for that test, an error is generated and the test is not added to the MTP.<br><br>If the STP contains only a single test, the test_source parameter can be omitted. If the STP contains multiple tests, test_source is required. |
| test | <test> (string) is the name of the test in the MTP that is to be replaced. |
| tim_reuse | <timing_reuse> (string) is the way in which timing settings in the MTP are to be reused for the replacement test:<br><br>- auto: STPM tries to reuse an existing timing, merging the timing from the replacement test with it. If this is not possible, a new timing is created.<br>- test:<test-name>: The timing from the existing test suite with the name <test-name> is used for the replacement test.<br>- <primary-keys>: You can explicitly specify the timing to use. How to do this differs for single-port and multiport tests:<br><br>- Single-port timing: Specify the timing as a combination of indexes, separated by periods: <eqnset-index>`.`<timset-index>`.`<specset-index><br>- Multiport timing: Specify the name of the multiport timing set to use.<br><br>- none: STPM will not try to reuse any timing. Instead, it always creates new timing for the replacement test.<br><br>If this parameter is omitted, none is used. |
| lev_reuse | <level_reuse> (string) is the way in which level settings in the MTP are to be reused for the replacement test:<br><br>- auto: STPM tries to reuse existing levels, merging the levels from the replacement test with them. If this is not possible, new levels are created.<br>- test:<test-name>: The levels from the existing test suite with the name <test-name> are used for the replacement test.<br>- <primary-keys>: You can explicitly specify the levels to use as a combination of indexes, separated by periods:<br><br><eqnset-index>`.`<levelset-index>`.`<specset-index><br><br>- none: STPM will not try to reuse any levels. Instead, it always creates new levels for the replacement test.<br><br>If this parameter is omitted, none is used. |
| pat_reuse | <pattern_reuse> (string) is the way in which patterns in the MTP are to be reused for the replacement test:<br><br>- test:<test-name>: The patterns from the existing test suite with the name <test-name> are used for the replacement test.<br>- <pattern-label>: You can explicitly specify the patterns to use by providing the name of the pattern label.<br>- none: STPM will not try to reuse any patterns. Instead, it always creates new patterns for the replacement test.<br><br>If this parameter is omitted, none is used. |
| reuse_scope | <scope> (string or list of strings) are the testflow groups that STPM is to analyze for purposes of merging or reusing primaries. STPM will ignore primaries from other testflow groups.<br><br>The scope can be:<br><br>- `"*all*"` to tell STPM to consider all groups<br>- A comma-separated list of testflow groups<br><br>If this parameter is not specified, the test suites in the testflow group containing the replaced test are considered. |
| copy_test_method | <copy_tm_att> (0 or 1) specifies whether the attributes for the test method of the replaced test are copied from the STP or whether the attributes in the MTP are used:<br><br>- 0 (default): The attributes from the MTP are kept.<br>- 1: The attributes from the STP are copied to the MTP.<br><br>If this parameter is not specified, the attributes from the MTP are kept. |
| tim_remove | <timing_remove> (string) is an instruction for STPM on how to remove the timing settings of the replaced test:<br><br>- unused: STPM removes the settings if no other test uses them. (STPM may not be able to detect usage by tests that switch primaries in the C++ code.)<br>- none: The timing settings are not removed, even if no other test uses them.<br><br>If this parameter is omitted, unused is used. |
| lev_remove | <level_remove> (string) is an instruction for STPM on how to remove the levels of the replaced test:<br><br>- unused: STPM removes the levels if no other test uses them. (STPM may not be able to detect usage by tests that switch primaries in the C++ code.)<br>- none: The levels are not removed, even if no other test uses them.<br><br>If this parameter is omitted, unused is used. |
| pat_remove | <pattern_remove> (string) is an instruction for STPM on how to remove the patterns of the replaced test:<br><br>- unused: STPM removes the patterns if no other test uses them. (STPM may not be able to detect usage by tests that switch primaries in the C++ code.)<br>- none: The patterns are not removed, even if no other test uses them.<br>- If this parameter is omitted, unused is used. |
| pat_dir | <path> (string) is the path of the directory where STPM is to store patterns that it copies from the STP to the device directory.<br><br>The path is relative to the vectors subdirectory of the device directory.<br><br>If this parameter is omitted, patterns is used. (That is, the patterns are copied to the vectors/patterns/ subdirectory of the device directory.) |
| pre_proc | <pre_proc> is a script that is executed before this command.<br><br>The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.<br><br>This is an optional parameter. |
| post_proc | <post_proc> is a script that is executed after this command.<br><br>The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.<br><br>This is an optional parameter. |

### Example（取自子主题 STPM control file › replace test）

See the sample control file in `Structure of an STPM control file`（raw: `02.09.02.03.01_Structure_of_an_STPM_control_file.md`）.

### Syntax（取自子主题 STPM control file › remove label）

```
remove_label(
    label = '<label_name>',
[pmf_only = <pmf_flag>, ]
[pre_proc = <pre_proc>, ]
[post_proc = <post_proc>]
)
```

### Parameters（取自子主题 STPM control file › remove label）

The parameters in the order in which they are listed above:

| label | <label_name> (string) is the name of the label that you want to remove from the MTP. |
|---|---|
| pmf_only | <pmf_flag> (0 or 1) specifies whether the pattern is deleted from the MTP or only its entry from the pattern master:<br><br>- 0 (default): The pattern is deleted from the MPT.<br>- 1: The pattern is kept in the MTP, but its entry is removed from the pattern master file<br><br>If this parameter is not specified, the pattern is deleted from the MTP. |
| pre_proc | <pre_proc> is a script that is executed before this command.<br><br>The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.<br><br>This is an optional parameter. |
| post_proc | <post_proc> is a script that is executed after this command.<br><br>The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.<br><br>This is an optional parameter. |

### Syntax（取自子主题 STPM control file › add pattern）

```
add_pattern(
test_flow_file = '<testflow_file>',
context        = '<source>',
[pat_dir        = '<path>',           ]
[pre_proc       = <pre_proc>,         ]
[post_proc      = <post_proc>]
)
```

### Parameters（取自子主题 STPM control file › add pattern）

The parameters in the order in which they are listed above:

| test_flow_file | <testflow_file> (string) is the path (including the name) of the testflow file of the source test program (STP) that contains the pattern that you want to add to the MTP.<br><br>The path can be either absolute or relative to the current working directory. |
|---|---|
| context | <source> (string) describes the location of the desired pattern in the STP. There are two ways to specify the location:<br><br>- By providing the label name. For example: "pattern1".<br>- By providing the names of the test and the test suite, divided by a colon. For example: "mytest:ts3".<br><br>STPM will interpret any string without a colon as a label name and any string with a colon as the names of a test and a test suite. |
| pat_dir | <path> (string) is the path of the directory where STPM is to store patterns that it copies from the STP to the device directory.<br><br>The path is relative to the vectors subdirectory of the device directory.<br><br>If this parameter is omitted, patterns is used. (That is, the patterns are copied to the vectors/patterns/ subdirectory of the device directory.) |
| pre_proc | <pre_proc> is a script that is executed before this command.<br><br>The syntax of the parameter value is described in Preprocessing and postprocessing scripts.<br><br>This is an optional parameter. |
| post_proc | <post_proc> is a script that is executed after this command.<br><br>The syntax of the parameter value is described in Preprocessing and postprocessing scripts.<br><br>This is an optional parameter. |

### Example（取自子主题 STPM control file › add pattern）

This example adds the pattern from the test suite "func_ts_2" in the "func_test" test in the "tf1.tf" testflow to the /vectors/patterns directory of the MTP device directory.

```
add_pattern(test_flow_file='/user/johndoe/stp/tf1.tf', context='func_test:func_ts_2')
```

### Syntax（取自子主题 STPM control file › replace pattern）

```
replace_pattern(
test_flow_file         = '<testflow_file>',
context                = '<source>',
test                   = '<test_suite>',
[pat_dir                = '<path>',           ]
[pat_remove             = '<pat_remove>',     ]
[waveforms_compare_mode = '<compare_mode>',   ]
[pre_proc               = <pre_proc>,         ]
[post_proc              = <post_proc>]
)
```

### Parameters（取自子主题 STPM control file › replace pattern）

The parameters in the order in which they are listed above:

| test_flow_file | <testflow_file> (string) is the path (including the name) of the testflow file of the source test program (STP) that contains the pattern that you want to add to the MTP.<br><br>The path can be either absolute or relative to the current working directory. |
|---|---|
| context | <source> (string) describes the location of the desired pattern in the STP. There are two ways to specify the location:<br><br>- By providing the label name. For example: "pattern1".<br>- By providing the names of the test and the test suite, divided by a colon. For example: "mytest:ts3".<br><br>STPM will interpret any string without a colon as a label name and any string with a colon as the names of a test and a test suite. |
| test | <test_suite> (string) is the name of the MTP test suite in which you want to replace the pattern. |
| pat_dir | <path> (string) is the path of the directory where STPM is to store patterns that it copies from the STP to the device directory.<br><br>The path is relative to the vectors subdirectory of the device directory.<br><br>If this parameter is omitted, patterns is used. (That is, the patterns are copied to the vectors/patterns/ subdirectory of the device directory.) |
| pat_remove | <pat_remove> (string) specifies whether the old pattern from the MTP test suite is deleted from the MTP device directory:<br><br>- 'unused' (default): The pattern is deleted if no other test uses it.<br>- 'none': The pattern is not deleted.<br><br>If this parameter is not specified, the pattern is deleted if no other test uses it. |
| waveforms_compare_mode | <compare_mode> (string) specifies whether the waveforms in the new pattern are compared to the waveforms in the old pattern:<br><br>- 'none' (default): The waveforms of the two patterns are not compared.<br>- 'error': The waveforms are compared and an error is generated if any differences are found.<br>- 'warning': The waveforms are compared and a warning is generated if any differences are found.<br><br>If this parameter is not specified, the waveforms are not compared. |
| pre_proc | <pre_proc> is a script that is executed before this command.<br><br>The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.<br><br>This is an optional parameter. |
| post_proc | <post_proc> is a script that is executed after this command.<br><br>The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.<br><br>This is an optional parameter. |

### Example（取自子主题 STPM control file › replace pattern）

This example adds the pattern from the test suite "func_ts_2" in the "func_test" test in the "tf1.tf" testflow to the /vectors/patterns directory of the MTP device directory.

```
add_pattern(test_flow_file='/user/johndoe/stp/tf1.tf', context='func_test:func_ts_2')
```

### Syntax（取自子主题 STPM control file › tpt generate template）

```
tpt_generate_template(
tpt_dir    = <location>,
[pre_proc   = <pre_proc>,    ]
[post_proc  = <post_proc>]
)
```

### Parameters（取自子主题 STPM control file › tpt generate template）

The parameters in the order in which they are listed above:

| tpt_dir | <location> (string) is the path, including the name, where the new template files and directories are created.<br><br>The path can be either absolute or relative to the current working directory.<br><br>If the directory does not yet exist, STPM creates it. |
|---|---|
| pre_proc | <pre_proc> is a script that is executed before this command.<br><br>The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.<br><br>This is an optional parameter. |
| post_proc | <post_proc> is a script that is executed after this command.<br><br>The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.<br><br>This is an optional parameter. |

### Example（取自子主题 STPM control file › tpt generate template）

This example creates a test program template in the subdirectory "new_template" of the current working directory.

```
generate_new(
    tpt_dir  = 'new_template'
    )
```

### Syntax（取自子主题 STPM control file › tpt import from device）

```
tpt_import_from_device(
device_test_flow = <testflow_file>,
    tpt_dir = <location>,
[include_groups  = <include_groups>, ]
[empty_groups = <empty_groups>, ]
[copy_static_content = <copy_items>], ]
[allow_overwrite = <overwrite_flag>, ]
[pre_proc = <pre_proc>, ]
[post_proc = <post_proc>]
)
```

### Parameters（取自子主题 STPM control file › tpt import from device）

| device_test_flow | <testflow_file> (string) is the path of the testflow file from which the test program template is to be generated.<br><br>The path can be either absolute or relative to the current working directory. |
|---|---|
| tpt_dir | <location> (string) is the path, including the name, where the new template files and directories are created.<br><br>The path can be either absolute or relative to the current working directory.<br><br>If the directory does not yet exist, STPM creates it. If the directory already exists, it must either be empty or the allow_overwrite parameter (see below) must be set to 1. |
| include_groups | <include_groups> (list of strings) is a list of groups in the specified testflow that are to be imported.<br><br>Each group name is a string enclosed in single or double quotes; groups are separated by commas, and the list is enclosed in square brackets.<br><br>You can use the ? and * wildcard characters in the group name strings. (See empty_groups, below, for details.)<br><br>This parameter is optional. If it is omitted, all groups are imported. |
| empty_groups | <empty_groups> (list of strings) is a list of groups that are to be emptied.<br><br>An empty group is transferred to the test program template, but none of the test suites it contains are transferred. Empty groups are useful to preserve the structure of the testflow. They can be filled with new test suites later.<br><br>Each group name is a string enclosed in single or double quotes; groups are separated by commas, and the list is enclosed in square brackets.<br><br>You can use the ? and * wildcard characters in the group name strings; ? matches any single character and * matches zero or more characters.<br><br>For example, to empty all groups, you would specify `empty_groups = '*'`. To empty the group temp1 and all groups with the name "test" followed by a single character, you would specify `empty_groups = 'temp1', 'test?'`.<br><br>This parameter is optional. If it is omitted, no groups are emptied. |
| copy_static_content | <copy_items> (list of strings) is a list of names of files or directories that are to be copied from the existing device directory to the TPT directory.<br><br>The list may contain only names (of files or directories), not paths. The named items must be located in the top level of the device directory. Each name is enclosed in quotes and separated by commas.<br><br>For example: `copy_static_content = ['my_notes.txt','Change log']`<br><br>If you include standard directories in this list (testflow, timing, levels, configuration, vectors, testtable), STPM generates a warning and does not copy the contents.<br><br>Any directories that are copied by means of this command will be included in the device directory generated with `tpt_generate_device_dir`（raw: `02.09.02.03.16_tpt_generate_device_dir.md`）.<br><br>This parameter is optional. If it is omitted, no additional content is copied. |
| allow_overwrite | <overwrite_flag> specifies whether STPM may overwrite existing files in the test program template directory:<br><br>- 0 (default): No existing files or directories in the test program template directory may be overwritten. If this prevents STPM from saving a created file, it displays an error and stops the conversion.<br>- 1: STPM may overwrite existing files and directories.<br><br>This parameter is optional. If it is omitted, no files or directories are overwritten. |
| pre_proc | <pre_proc> is a script that is executed before this command.<br><br>The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.<br><br>This is an optional parameter. |
| post_proc | <post_proc> is a script that is executed after this command.<br><br>The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.<br><br>This is an optional parameter. |

### Example（取自子主题 STPM control file › tpt import from device）

This example converts the testflow "my_testflow" (located in the "testflow" subdirectory of the current working directory) into a test program template in the directory "new_template", which is located at the same level as the current working directory. It copies all groups, empties the groups "init_group" and "final_group", copies the temp subdirectory to the TPT directory, and overwrites any existing files in the TPT directory.

```
tpt_import_from_device(
    device_test_flow    = 'testflow/my_testflow',
    tpt_dir             = '../new_template',
    empty_groups        = ['init_group', 'final_group'],
    copy_static_content = ['temp'],
    allow_overwrite     = 1
    )
```

### Syntax（取自子主题 STPM control file › tpt generate device dir）

```
tpt_generate_device_dir(
tpt_dir = <tpt_directory>,
    device_dir = <directory>,
[device_name = <device_name>, ]
[pre_proc = <pre_proc>, ]
post_proc = <post_proc>]
)
```

### Parameters（取自子主题 STPM control file › tpt generate device dir）

The parameters in the order in which they are listed above:

| tpt_dir | <tpt_directory> (string) is the name and path of the directory containing the TPT files from which the device directory is to be generated.<br><br>The path can be either absolute or relative to the current working directory. |
|---|---|
| device_dir | <directory> (string) is the path, including the name, where the new device directory is created. The directory must either not exist yet (in which case STPM creates it) or it must be empty.<br><br>The path can be either absolute or relative to the current working directory. |
| device_name | <device_name> (string) is the name for the newly created device.<br><br>This parameter is optional. If it is omitted, "device" is used. |
| pre_proc | <pre_proc> is a script that is executed before this command.<br><br>The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.<br><br>This is an optional parameter. |
| post_proc | <post_proc> is a script that is executed after this command.<br><br>The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.<br><br>This is an optional parameter. |

### Example（取自子主题 STPM control file › tpt generate device dir）

This example creates a device directory for the device "my_device" from the TPT master file "my_tpt.tpt" (located in the current working directory). The device directory is located at the same level as the current working directory.

```
tpt_generate_device_dir(
    tpt_dir     = 'my_tpt/'
    device_dir  = '../my_device/'
    device_name = 'my_device',
    )
```

### Syntax（取自子主题 STPM control file › tpt merge）

```
tpt_merge(
source_tpts = [<tpt_list>],
   target_tpt = <directory>,
[pre_proc = <pre_proc>, ]
[post_proc = <post_proc>]
)
```

### Parameters（取自子主题 STPM control file › tpt merge）

The parameters in the order in which they are listed above:

| source_tpts | <tpt_file> (list of strings) is a list of TPT directories that you want to merge into a single TPT.<br><br>Include in the list the path of each TPT you want to merge, enclosed in quotes and separated by commas.<br><br>Paths can be either absolute or relative to the current working directory.<br><br>In case of conflicts, objects from any source TPT overwrite those in the target TPT and objects from source TPTs at the end of the list overwrite those from TPTs at the beginning of the list. |
|---|---|
| target_tpt | <directory> (string) is the path, including the name, where the merged device directory is created. The TPT must already exist.<br><br>The path can be either absolute or relative to the current working directory. |
| pre_proc | <pre_proc> is a script that is executed before this command.<br><br>The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.<br><br>This is an optional parameter. |
| post_proc | <post_proc> is a script that is executed after this command.<br><br>The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.<br><br>This is an optional parameter. |

### Example（取自子主题 STPM control file › tpt merge）

This example copies the contents from three test program templates into one new template..

```
tpt_merge(
    source_tpts = ['my_tpt','my_other_tpt','../reference/best_tpt')
    target_tpt  = '../merged_tpt/'
    )
```

### Syntax（取自子主题 STPM control file › tpt add test）

```
tpt_add_test(
test_flow_file = '<testflow_file>',
[test_source = '<test_source>', ]
[test = '<test>', ]
[position  = '<position>', ]
[tim_reuse = '<timing_reuse>', ]
[lev_reuse = '<level_reuse>', ]
[pat_reuse = '<pattern_reuse>', ]
[reuse_scope = '<scope>', ]
[pat_dir = '<path>', ]
[pre_proc = <pre_proc>, ]
[post_proc = <post_proc>]
)
```

### Parameters（取自子主题 STPM control file › tpt add test）

The parameters in the order in which they are listed above:

| test_flow_file | <testflow_file> (string) is the path, including the name, of the testflow file of the source test program (STP) that contains the test that you want to add to the MTP.<br><br>The path can be either absolute or relative to the current working directory. |
|---|---|
| test_source | <test_source> (string) is the name of the test from the STP that will be added to the MTP. The test must be included in the `test suite table`（raw: `02.09.02.05.01_Test_suite_table_of_a_TPT.md`）.<br><br>If the STP contains only a single test, the test_source parameter can be omitted. If the STP contains multiple tests, test_source is required. |
| test | <test> is the name for the added test in the MTP.<br><br>If this parameter is omitted, the name is added to the MTP with the name specified for it in the `test suite table`（raw: `02.09.02.05.01_Test_suite_table_of_a_TPT.md`）.<br><br>If there is already a test with the same name in the MTP, the test from the STP is not added and an error is generated. (This applies in both cases, whether you have specified a name using the test parameter or whether the default name is used.) |
| position | <position> (string) is the position within a test group where the new test is inserted.<br><br>The following values are available:<br><br>- optimal: STPM inserts the test in a position in the testflow group that requires the least amount of level and timing reloads during execution.<br>- first: The test suite is inserted as the first test in the testflow group.<br>- last: The test suite is inserted as the last in the testflow group.<br>- after:<test_name>: The test suite is inserted immediately after the test suite with the name <test_name> in the testflow group.<br>- before:<test_name>: The test suite is inserted immediately before the test suite with the name <test_name> in the testflow group.<br><br>If this parameter is omitted, optimal is used. |
| tim_reuse | <timing_reuse> (string) is the way in which timing settings in the MTP are to be reused for the added test:<br><br>- auto: STPM tries to reuse an existing timing, merging the timing from the new test with it. If this is not possible, a new timing is created.<br>- test:<test-name>: The timing from the existing test suite with the name <test-name> is used for the added test.<br>- <primary-keys>: You can explicitly specify the timing to use. How to do this differs for single-port and multiport tests:<br><br>- Single-port timing: Specify the timing as a combination of indexes, separated by periods:<br><br><eqnset-index>`.`<timset-index>`.`<specset-index><br><br>- Multiport timing: Specify the name of the multiport specification to use.<br><br>- none: STPM will not try to reuse any timing. Instead, it always creates new timing for the added test.<br><br>If this parameter is omitted, none is used. |
| lev_reuse | <level_reuse> (string) is the way in which level settings in the MTP are to be reused for the added test:<br><br>- auto: STPM tries to reuse existing levels, merging the levels from the new test with hem. If this is not possible, new levels are created.<br>- test:<test-name>: The levels from the existing test suite with the name <test-name> are used for the added test.<br>- <primary-keys>: You can explicitly specify the levels to use as a combination of indexes, separated by periods:<br><br><eqnset-index>`.`<levelset-index>`.`<specset-index><br><br>- none: STPM will not try to reuse any levels. Instead, it always creates new levels for the added test.<br><br>If this parameter is omitted, none is used. |
| pat_reuse | <pattern_reuse> (string) is the way in which patterns in the MTP are to be reused for the added test:<br><br>- test:<test-name>: The patterns from the existing test suite with the name <test-name> are used for the added test.<br>- <pattern-label>: You can explicitly specify the patterns to use by providing the name of the pattern label.<br>- none: STPM will not try to reuse any patterns. Instead, it always creates new patterns for the added test.<br><br>If this parameter is omitted, none is used. |
| reuse_scope | <scope> (string or list of strings) are the testflow groups that STPM is to analyze for purposes of merging or reusing primaries. STPM will ignore primaries from other testflow groups.<br><br>The scope can be:<br><br>- `"*all*"` to tell STPM to consider all groups<br>- A comma-separated list of testflow groups, enclosed in square brackets<br><br>If this parameter is not specified, the default is for STPM to consider the test suites in the testflow group specified in the test_group parameter (see above).<br><br>If test_group is not specified either, all groups are considered. |
| pat_dir | <path> (string) is the path of the directory where STPM is to store patterns that it copies from the STP to the device directory.<br><br>The path is relative to the vectors subdirectory of the device directory.<br><br>If this parameter is omitted, patterns is used. (That is, the patterns are copied to the vectors/patterns/ subdirectory of the device directory.) |
| pre_proc | <pre_proc> is a script that is executed before this command.<br><br>The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.<br><br>This is an optional parameter. |
| post_proc | <post_proc> is a script that is executed after this command.<br><br>The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.<br><br>This is an optional parameter. |

### Example（取自子主题 STPM control file › tpt add test）

See the sample control file in `Structure of an STPM control file`（raw: `02.09.02.03.01_Structure_of_an_STPM_control_file.md`）.

### Syntax（取自子主题 STPM control file › tpt replace test）

```
tpt_replace_test(
test_flow_file = '<testflow_file>',
[test_source = '<test_source>', ]
test = '<test>',
[tim_reuse = '<timing_reuse>', ]
[lev_reuse = '<level_reuse>', ]
[pat_reuse = '<pattern_reuse>', ]
[reuse_scope  = '<scope>', ]
[tim_remove = '<timing_remove>', ]
[lev_remove = '<level_remove>', ]
[pat_remove = '<pattern_remove>', ]
[pat_dir = '<path>', ]
[pre_proc = <pre_proc>, ]
[post_proc = <post_proc>]
)
```

### Parameters（取自子主题 STPM control file › tpt replace test）

The parameters in the order in which they are listed above:

| test_flow_file | <testflow_file> (string) is the path (including the name) of the testflow file of the source test program (STP) that contains the test with which you want to replace an existing test in the MTP.<br><br>The path can be either absolute or relative to the current working directory. |
|---|---|
| test_source | <test_source> (string) is the name of the test from the STP that will be used to replace the existing test in the to the MTP. The test must be included in the `test suite table`（raw: `02.09.02.05.01_Test_suite_table_of_a_TPT.md`）.<br><br>If the MTP already contains a test by that name and the primaries are already set for that test, an error is generated and the test is not added to the MTP.<br><br>If the STP contains only a single test, the test_source parameter can be omitted. If the STP contains multiple tests, test_source is required. |
| test | <test> (string) is the name of the test in the MTP that is to be replaced. |
| tim_reuse | <timing_reuse> (string) is the way in which timing settings in the MTP are to be reused for the replacement test:<br><br>- auto: STPM tries to reuse an existing timing, merging the timing from the replacement test with it. If this is not possible, a new timing is created.<br>- test:<test-name>: The timing from the existing test suite with the name <test-name> is used for the replacement test.<br>- <primary-keys>: You can explicitly specify the timing to use. How to do this differs for single-port and multiport tests:<br><br>- Single-port timing: Specify the timing as a combination of indexes, separated by periods:<br><br><eqnset-index>`.`<timset-index>`.`<specset-index><br><br>- Multiport timing: Specify the name of the multiport timing set to use.<br><br>- none: STPM will not try to reuse any timing. Instead, it always creates new timing for the replacement test.<br><br>If this parameter is omitted, none is used. |
| lev_reuse | <level_reuse> (string) is the way in which level settings in the MTP are to be reused for the replacement test:<br><br>- auto: STPM tries to reuse existing levels, merging the levels from the replacement test with them. If this is not possible, new levels are created.<br>- test:<test-name>: The levels from the existing test suite with the name <test-name> are used for the replacement test.<br>- <primary-keys>: You can explicitly specify the levels to use as a combination of indexes, separated by periods:<br><br><eqnset-index>`.`<levelset-index>`.`<specset-index><br><br>- none: STPM will not try to reuse any levels. Instead, it always creates new levels for the replacement test.<br><br>If this parameter is omitted, none is used. |
| pat_reuse | <pattern_reuse> (string) is the way in which patterns in the MTP are to be reused for the replacement test:<br><br>- test:<test-name>: The patterns from the existing test suite with the name <test-name> are used for the replacement test.<br>- <pattern-label>: You can explicitly specify the patterns to use by providing the name of the pattern label.<br>- none: STPM will not try to reuse any patterns. Instead, it always creates new patterns for the replacement test.<br><br>If this parameter is omitted, none is used. |
| reuse_scope | <scope> (string or list of strings) are the testflow groups that STPM is to analyze for purposes of merging or reusing primaries. STPM will ignore primaries from other testflow groups.<br><br>The scope can be:<br><br>- `"*all*"` to tell STPM to consider all groups<br>- A comma-separated list of testflow groups<br><br>If this parameter is not specified, the test suites in the testflow group containing the replaced test are considered. |
| tim_remove | <timing_remove> (string) is an instruction for STPM on how to remove the timing settings of the replaced test:<br><br>- unused: STPM removes the settings if no other test uses them. (STPM may not be able to detect usage by tests that switch primaries in the C++ code.)<br>- none: The timing settings are not removed, even if no other test uses them.<br><br>If this parameter is omitted, unused is used. |
| lev_remove | <level_remove> (string) is an instruction for STPM on how to remove the levels of the replaced test:<br><br>- unused: STPM removes the levels if no other test uses them. (STPM may not be able to detect usage by tests that switch primaries in the C++ code.)<br>- none: The levels are not removed, even if no other test uses them.<br><br>If this parameter is omitted, unused is used. |
| pat_remove | <pattern_remove> (string) is an instruction for STPM on how to remove the patterns of the replaced test:<br><br>- unused: STPM removes the patterns if no other test uses them. (STPM may not be able to detect usage by tests that switch primaries in the C++ code.)<br>- none: The patterns are not removed, even if no other test uses them.<br>- If this parameter is omitted, unused is used. |
| pat_dir | <path> (string) is the path of the directory where STPM is to store patterns that it copies from the STP to the device directory.<br><br>The path is relative to the vectors subdirectory of the device directory.<br><br>If this parameter is omitted, patterns is used. (That is, the patterns are copied to the vectors/patterns/ subdirectory of the device directory.) |
| pre_proc | <pre_proc> is a script that is executed before this command.<br><br>The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.<br><br>This is an optional parameter. |
| post_proc | <post_proc> is a script that is executed after this command.<br><br>The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.<br><br>This is an optional parameter. |

### Syntax（取自子主题 STPM control file › tpt generate tp）

```
tpt_generate_tp(
[generate_complete_device_directory = <complete_device_flag>,     ]
[error_on_non_existing_primaries    = <missing_primaries_flag>,   ]
[ignore_empty_groups                = <ignore_empty_groups_flag>, ]
[pre_proc                           = <pre_proc>,                 ]
[post_proc                          = <post_proc>]
)
```

### Parameters（取自子主题 STPM control file › tpt generate tp）

| generate_complete_device_directory | <complete_device_flag> specify whether a complete device directory or only a skeleton is generated:<br><br>- 0: The generated device directory contains only a testflow file. If the use of a test table is specified in the TPT, a test table is also generated.<br>- 1 (default): A complete device directory is generated.<br><br>If this parameter is omitted, 1 is used (a complete directory is generated). |
|---|---|
| error_on_non_existing_primaries | <missing_primaries_flag> specifies whether warnings are generated for missing primaries:<br><br>- 0: STPM generates no warning if a test suite refers to primaries that do not exist in the TPT.<br>- 1 (default): STPM generates warnings when non-existent primaries are referenced.<br><br>If this parameter is omitted, 1 is used (warnings are generated). |
| ignore_empty_groups | <ignore_empty_groups_flag> specifies what happens with empty groups in the testflow of the TPT:<br><br>- 0: Empty groups are copied to the testflow of the output test program.<br>- 1 (default): Empty groups are not copied to the testflow of the output test program.<br><br>If this parameter is omitted, 1 is used (empty groups are not copied). |
| pre_proc | <pre_proc> is a script that is executed before this command.<br><br>The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.<br><br>This is an optional parameter. |
| post_proc | <post_proc> is a script that is executed after this command.<br><br>The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.<br><br>This is an optional parameter. |

### Syntax（取自子主题 STPM control file › tpt compare tp）

```
tpt_compare_tp(
[report_file_path = '<report_file>',       ]
[include_groups   = <include_groups>,      ]
[pre_proc         = <pre_proc>,            ]
[post_proc        = <post_proc>]
)
```

### Parameters（取自子主题 STPM control file › tpt compare tp）

| report_file_path | <report_file> (string) is the path (including the name) where the command is to store the report file.<br><br>If this parameter is omitted, the file is named compare_log.html and is stored in the current working directory. |
|---|---|
| include_groups | <include_groups> (list of strings) is a list of groups in the specified testflow that are to be compared.<br><br>Each group name is a string enclosed in single or double quotes; groups are separated by commas, and the list is enclosed in square brackets.<br><br>This parameter is optional. If it is omitted, the entire testflow is compared. |
| pre_proc | <pre_proc> is a script that is executed before this command.<br><br>The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.<br><br>This is an optional parameter. |
| post_proc | <post_proc> is a script that is executed after this command.<br><br>The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.<br><br>This is an optional parameter. |

### Syntax（取自子主题 STPM control file › tpt generate test stages）

```
tpt_generate_test_stages(
[include_undefined_objects = <flag>,      ]
[pre_proc                  = <pre_proc>,  ]
[post_proc                 = <post_proc>]
)
```

### Parameters（取自子主题 STPM control file › tpt generate test stages）

The parameters in the order in which they are listed above:

| include_undefined_objects | <flag> (0 or 1) specifies how STPM treats undefined objects in the `test stage table`（raw: `02.09.02.05.06_Test_stage_table_of_a_TPT.md`）:<br><br>- 0: Undefined objects are not included in the data log profile.<br>- 1 (default): Undefined objects are treated as enabled.<br><br>An object is considered undefined for a test stage when the object's row contains neither Y nor N in the column for that test stage.<br><br>If this parameter is omitted, 1 is used. That is, undefined objects are considered to be enabled. |
|---|---|
| pre_proc | <pre_proc> is a script that is executed before this command.<br><br>The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.<br><br>This is an optional parameter. |
| post_proc | <post_proc> is a script that is executed after this command.<br><br>The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.<br><br>This is an optional parameter. |

### Syntax（取自子主题 STPM control file › extract subflow）

```
extract_subflow(
test_flow_file = '<file_path>',
test_groups = [<group_list>],
[levels_mode = <levels_mode>, ]
[timing_mode = <timing_mode>,
[pattern_mode = <pattern_mode>, ]
[config_mode = <config_mode>, ]
[keep_tim_eqnsets = [<tim_eqnsets>], ]
[keep_lev_eqnsets = [<lev_eqnsets>], ]
[keep_wavetables = [<wavetables>], ]
[keep_specifications = [<specs>], ]
[keep_pattern_files = [<pattern_files>], ]
[keep_setup_file_names = <keep_file_names_flag>, ]
[copy_static_content = [<copy_items>], ]
[copy_patterns = <copy_pattern_flag>, ]
[allow_overwrite = <overwrite_flag>, ]
[pre_proc = <pre_proc>, ]
[post_proc = <post_proc>]
)
```

### Parameters（取自子主题 STPM control file › extract subflow）

The parameters in the order in which they are listed above:

| test_flow_file | <file_path> (string) is the name and path of the testflow file for the STP you want to generate.<br><br>It can be an absolute or a relative path. If it is a relative path, the base directory is the current working directory at the time STPM was called.<br><br>If folders specified in the path do not yet exist, STPM creates them. |
|---|---|
| test_groups | <group_list> (list of strings) is a list of test groups that are exported. The list must be enclosed in square brackets..<br><br>Include in the list each testflow group you want to export to the STP, enclosed in quotes and separated by commas.<br><br>For example: `test_groups = ['tg3','fail_tg']` |
| levels_mode | <levels_mode> specifies the way in which level settings are extracted from the MTP:<br><br>- 'used' (default): Only level settings that are used by the extracted test groups are copied from the MTP to the STP.<br>- 'all': All level settings from the MTP are copied to the STP, even if none of the extracted test groups is using them.<br>- 'keep_file': No level settings are copied to the STP. Instead, the STP uses the level file of the MTP. This requires that the STP is located in the same directory as the MTP.<br><br>This parameter is optional. If it is omitted, only the level settings used in the subflow are copied. |
| timing_mode | <timing_mode> specifies the way in which timing settings are extracted from the MTP:<br><br>- 'used' (default): Only timing settings that are used by the extracted test groups are copied from the MTP to the STP.<br>- 'all': All timing settings from the MTP are copied to the STP, even if none of the extracted test groups is using them.<br>- 'keep_file': No timing settings are copied to the STP. Instead, the STP uses the timing file of the MTP. This requires that the STP is located in the same directory as the MTP.<br><br>This parameter is optional. If it is omitted, only the timing settings used in the subflow are copied. |
| pattern_mode | <pattern_mode> specifies the way in which patterns are extracted from the MTP:<br><br>- 'used' (default): Only patterns that are used by the extracted test groups are copied from the MTP to the STP.<br>- 'all': All patterns from the MTP are copied to the STP, even if none of the extracted test groups is using them.<br><br>This parameter is optional. If it is omitted, only the patterns used in the subflow are copied. |
| config_mode | <config_mode> specifies the way in which configuration settings are extracted from the MTP:<br><br>- 'used': Only configuration settings that are used by the extracted test groups are copied from the MTP to the STP.<br>- 'all' (default): All configuration settings from the MTP are copied to the STP, even if none of the extracted test groups is using them.<br><br>This parameter is optional. If it is omitted, all config settings from the MTP are copied. |
| keep_tim_eqnsets | <tim_eqnsets> is a list of timing equation sets that are extracted from the MTP even if they are not used by the extracted test groups.<br><br>The value is a list of equation set numbers separated by commas. For example: [1, 5, 9, 13]<br><br>This parameter is optional. |
| keep_lev_eqnsets | <lev_eqnsets> is a list of level equation sets that are extracted from the MTP even if they are not used by the extracted test groups.<br><br>The value is a list of equation set numbers separated by commas. For example: [7,8]<br><br>This parameter is optional. |
| keep_wavetables | <wavetables> is a list of wavetables that are extracted from the MTP even if they are not used by the extracted test groups.<br><br>The value is a list of wavetable names, enclosed in quotes and separated by commas. For example: ['mytable', 'wavetable2']<br><br>This parameter is optional. |
| keep_specifications | <specifications> is a list of specifications that are extracted from the MTP even if they are not used by the extracted test groups.<br><br>The value is a list of specification names, enclosed in quotes and separated by commas. For example: ['spec5', 'spec5b']<br><br>This parameter is optional. |
| keep_pattern_files | <pattern_files> is a list of level pattern files that are extracted from the MTP even if they are not used by the extracted test groups.<br><br>The value is a list of pattern file paths, enclosed in quotes and separated by commas. Paths can be absolute or relative to the directory of the MTP. For example: ['/home/johndoe/tps/init_pattern.bin l', 'device/vectors/pat3.binl'']<br><br>This parameter is optional. |
| keep_setup_file_names | <keep_file_names_flag> specifies whether the names of setups are changed in the exported testflow:<br><br>- 0 (default): The names are changed to match the name of the extracted testflow.<br>- 1: The names remain the same as in the MTP.<br><br>This parameter is optional. If it is omitted, the names are changed. |
| copy_static_content | <copy_items> (list of strings) specifies is a list of names of files or directories that are to be copied from the device directory of the MTP to the device directory of the extracted subflow.<br><br>The list may contain only names (of files or directories), not paths. The named items must be located in the top level of the device directory. Each name is enclosed in quotes and separated by commas.<br><br>These values are supported:<br><br>- A list of names of files or directories (but not paths). The named items must be located in the top level of the device directory. Each name is enclosed in quotes and separated by commas.<br><br>For example: `copy_static_content = ['my_notes.txt','Change log']`<br><br>If you include standard directories in this list (see below), STPM generates a warning and does not copy the contents.<br><br>- ['*all*'] (default): Every file and directory in the device directory is copied, except the standard directories testflow, timing, levels, configuration, vectors, and testtable.<br>- []: No additional files or directories are copied.<br><br>This parameter is optional. If it is omitted, all objects from the top level of the device directory are copied (as if ['*all*'] had been specified). |
| copy_patterns | <copy_pattern_flag> specifies whether the patterns from the MTP are copied to the STP:<br><br>- 0: The patterns are not copied to the STP. The pattern master file of the STP refers to the patterns in the MTP.<br>- 1 (default): The patterns are copied to the STP. There are no references to the MTP patterns in the pattern master file of the STP.<br><br>This parameter is optional. If it is omitted, the patterns are copied. |
| allow_overwrite | <overwrite_flag> specifies whether STPM may overwrite existing files in the STP directory:<br><br>- 0 (default): No existing files or directories in the device directory may be overwritten. If this prevents STPM from saving a created file, it displays an error and stops the conversion.<br>- 1: STPM may overwrite existing files and directories.<br><br>This parameter is optional. If it is omitted, no files or directories are overwritten. |
| pre_proc | <pre_proc> is a script that is executed before this command.<br><br>The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.<br><br>This is an optional parameter. |
| post_proc | <post_proc> is a script that is executed after this command.<br><br>The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.<br><br>This is an optional parameter. |

### Syntax（取自子主题 STPM control file › merge subflow）

```
merge_subflow(
test_flow_file = '<file_path>',
[include_groups = [<include_group_list>], ]
[exclude_groups = [<exclude_group_list>], ]
[parent = '<parent_group>', ]
[position = '<position>', ]
[tim_eqnset_index = '<tim_index>', ]
[lev_eqnset_index = '<lev_index>', ]
[levels_mode = <levels_mode>, ]
[timing_mode = <timing_mode>, ]
[pattern_mode = <pattern_mode>, ]
[keep_tim_eqnsets = [<tim_eqnsets>], ]
[keep_lev_eqnsets = [<lev_eqnsets>], ]
[keep_wavetables = [<wavetables>], ]
[keep_specifications = [<specs>], ]
[keep_pattern_files = [<pattern_files>], ]
[copy_static_content = [<copy_items>], ]
[pre_proc = <pre_proc>, ]
[post_proc = <post_proc>]
)
```

### Parameters（取自子主题 STPM control file › merge subflow）

The parameters in the order in which they are listed above:

| test_flow_file | <file_path> (string) is the name and path of the testflow file for the STP you want to merge into the MTP.<br><br>It can be an absolute or a relative path. If it is a relative path, the base directory is the current working directory at the time STPM was called. |
|---|---|
| include_groups | <include_group_list> (list of strings) is a list of testflow groups that STPM is to import. If you use this parameter, only those groups specified in the list are imported.<br><br>The list must be enclosed in square brackets. Each testflow group in the list must be enclosed in quotes and separated by commas.<br><br>For example: `test_groups = ['tg3','fail_tg']`<br><br>This parameter is optional. It cannot be used when you also specify exclude_groups (see below). |
| exclude_groups | <exclude_group_list> (list of strings) is a list of testflow groups that STPM is to exclude from the merge process. If you use this parameter, all groups from the STP are merged, except those groups specified in the list.<br><br>The list must be enclosed in square brackets. Each testflow group in the list must be enclosed in quotes and separated by commas.<br><br>For example: `test_groups = ['tg3','fail_tg']`<br><br>This parameter is optional. It cannot be used when you also specify include_groups (see above). |
| parent | <parent_group> (string) is the name of the test group into which the tests from the subflow will be inserted.<br><br>The test group you name as the parent must already exist in the MTP.<br><br>This is an optional parameter. If it is not specified, the subflow in imported into the top level of the MTP. |
| position | <position> (string) is the position within the parent where the imported tests are inserted.<br><br>The following values are available:<br><br>- first: The tests are inserted at the beginning of the parent.<br>- last: The tests are inserted at the end of the parent.<br>- after:<test_name>: The test suite is inserted immediately after the test suite with the name <test_name> in the testflow group.<br>- before:<test_name>: The test suite is inserted immediately before the test suite with the name <test_name> in the testflow group.<br><br>If this parameter is omitted, last is used. |
| tim_eqnset_index | <tim_index> (string) specifies how the timing equation set indexes are imported from the STP to the MTP:<br><br>- 'keep': The indexes are transferred unchanged.<br>- 'keep+<number>': <number> is added to each index that is imported.<br><br>This is an optional parameter. If it is not specified, 'keep' is used. |
| lev_eqnset_index | <lev_index> (string) specifies how the level equation set indexes are imported from the STP to the MTP:<br><br>- 'keep': The indexes are transferred unchanged.<br>- 'keep+<number>': <number> is added to each index that is imported.<br><br>This is an optional parameter. If it is not specified, 'keep' is used. |
| levels_mode | <levels_mode> specifies the way in which level settings are merged into the MTP:<br><br>- 'used' (default): Only level settings that are used by the merged subflow are copied from the STP to the MTP.<br>- 'all': All level settings from the STP are copied to the MTP, even if none of the merged test groups is using them.<br><br>This parameter is optional. If it is omitted, only the level settings used in the subflow are copied. |
| timing_mode | <timing_mode> specifies the way in which timing settings are merged into the MTP:<br><br>- 'used' (default): Only timing settings that are used by the merged subflow are copied from the STP to the MTP.<br>- 'all': All timing settings from the STP are copied to the MTP, even if none of the merged test groups is using them.<br><br>This parameter is optional. If it is omitted, only the timing settings used in the subflow are copied. |
| pattern_mode | <pattern_mode> specifies the way in which timing settings are merged into the MTP:<br><br>- 'used' (default): Only patterns that are used by the merged subflow are copied from the STP to the MTP.<br>- 'all': All patterns from the STP are copied to the MTP, even if none of the merged test groups is using them.<br><br>This parameter is optional. If it is omitted, only the patterns used in the subflow are copied. |
| keep_tim_eqnsets | <tim_eqnsets> is a list of timing equation sets from the STP that are merged into the MTP even if they are not used by the merged test groups.<br><br>The value is a list of equation set numbers separated by commas. For example: [1, 5, 9, 13]<br><br>This parameter is optional. |
| keep_lev_eqnsets | <lev_eqnsets> is a list of level equation sets from the STP that are merged into the MTP even if they are not used by the merged test groups.<br><br>The value is a list of equation set numbers separated by commas. For example: [7,8]<br><br>This parameter is optional. |
| keep_wavetables | <wavetables> is a list of wavetables from the STP that are merged into the MTP even if they are not used by the merged test groups.<br><br>The value is a list of wavetable names, enclosed in quotes and separated by commas. For example: ['mytable', 'wavetable2']<br><br>This parameter is optional. |
| keep_specifications | <specifications> is a list of specifications from the STP that are merged into the MTP even if they are not used by the merged test groups.<br><br>The value is a list of specification names, enclosed in quotes and separated by commas. For example: ['spec5', 'spec5b']<br><br>This parameter is optional. |
| keep_pattern_files | <pattern_files> is a list of level pattern files from the STP that are merged into the MTP even if they are not used by the merged test groups.<br><br>The value is a list of pattern file paths, enclosed in quotes and separated by commas. Paths can be absolute or relative to the directory of the MTP. For example: ['/home/johndoe/tps/init_pattern.bin l', 'device/vectors/pat3.binl'']<br><br>This parameter is optional. |
| copy_static_content | <copy_items> (list of strings) specifies is a list of names of files or directories that are to be copied from the device directory of the merged STP to the device directory of the MTP.<br><br>The list may contain only names (of files or directories), not paths. The named items must be located in the top level of the device directory. Each name is enclosed in quotes and separated by commas.<br><br>These values are supported:<br><br>- A list of names of files or directories (but not paths). The named items must be located in the top level of the device directory. Each name is enclosed in quotes and separated by commas.<br><br>For example: `copy_static_content = ['my_notes.txt','Change log']`<br><br>If you include standard directories in this list (see below), STPM generates a warning and does not copy the contents.<br><br>- ['*all*']: Every file and directory in the device directory is copied, except the standard directories testflow, timing, levels, configuration, vectors, and testtable.<br>- [] (default): No additional files or directories are copied.<br><br>This parameter is optional. If it is omitted, no additional content is copied (as if [] had been specified). |
| pre_proc | <pre_proc> is a script that is executed before this command.<br><br>The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.<br><br>This is an optional parameter. |
| post_proc | <post_proc> is a script that is executed after this command.<br><br>The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.<br><br>This is an optional parameter. |

### Syntax（取自子主题 STPM control file › remove subflow）

```
extract_subflow(
test_flow_file  = '<file_path>',
[include_groups  = [<include_group_list>],    ]
[exclude_groups  = [<exclude_group_list>],    ]
[pre_proc        = <pre_proc>,                ]
[post_proc       = <post_proc>]
)
```

### Parameters（取自子主题 STPM control file › remove subflow）

The parameters in the order in which they are listed above:

| test_flow_file | <file_path> (string) is the name and path of the testflow file for the STP. The tests that were imported from this STP will be removed from the MTP.<br><br>It can be an absolute or a relative path. If it is a relative path, the base directory is the current working directory at the time STPM was called. |
|---|---|
| include_groups | <include_group_list> (list of strings) is a list of testflow groups that STPM is to remove. If you use this parameter, only those groups specified in the list are removed from the MTP.<br><br>The list must be enclosed in square brackets. Each testflow group in the list must be enclosed in quotes and separated by commas.<br><br>For example: `test_groups = ['tg3','fail_tg']`<br><br>This parameter is optional. It cannot be used when you also specify exclude_groups (see below). |
| exclude_groups | <exclude_group_list> (list of strings) is a list of testflow groups that STPM is to leave in the MTP. If you use this parameter, all groups in the STP are deleted from the MTP, except those groups specified in the list.<br><br>The list must be enclosed in square brackets. Each testflow group in the list must be enclosed in quotes and separated by commas.<br><br>For example: `test_groups = ['tg3','fail_tg']`<br><br>This parameter is optional. It cannot be used when you also specify include_groups (see above). |
| pre_proc | <pre_proc> is a script that is executed before this command.<br><br>The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.<br><br>This is an optional parameter. |
| post_proc | <post_proc> is a script that is executed after this command.<br><br>The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.<br><br>This is an optional parameter. |

### Syntax（取自子主题 STPM control file › clear duplicated）

```
clear_duplicated(
[proc_wavetables  = <0_or_1>, ]
[proc_tim_eqnsets = <0_or_1>, ]
[proc_tim_sets = <0_or_1>, ]
[proc_tim_specsets = <0_or_1>, ]
[proc_lev_eqnsets  = <0_or_1>, ]
[proc_lev_sets  = <0_or_1>, ]
[proc_lev_specsets = <0_or_1>, ]
[proc_specifications = <0_or_1>, ]
[proc_merge_pins = <0_or_1>, ]
[skip_wavetables = [<wavetables>], ]
[skip_tim_eqnsets = [<tim_eqnsets>], ]
[skip_lev_eqnsets = [<lev_eqnsets>], ]
[skip_specifications = [<specs>], ]
[analyze_only = <analyze_flag>, ]
[analyzer_path = <path>, ]
[pre_proc = <pre_proc>, ]
[post_proc = <post_proc>]
)
```

### Parameters（取自子主题 STPM control file › clear duplicated）

The parameters in the order in which they are listed above:

| proc_wavetables | Whether duplicate wavetables are removed:<br><br>- 0: They are not removed.<br>- 1: They are removed.<br><br>This parameter is optional, the default is 1. |
|---|---|
| proc_tim_eqnsets | Whether duplicate timing equation sets are removed:<br><br>- 0: They are not removed.<br>- 1: They are removed.<br><br>This parameter is optional, the default is 1. |
| proc_tim_sets | Whether duplicate timing sets are removed:<br><br>- 0: They are not removed.<br>- 1: They are removed.<br><br>This parameter is optional, the default is 1. |
| proc_tim_specsets | Whether duplicate timing specifications are removed:<br><br>- 0: They are not removed.<br>- 1: They are removed.<br><br>This parameter is optional, the default is 1. |
| proc_lev_eqnsets | Whether duplicate level equation sets are removed:<br><br>- 0: They are not removed.<br>- 1: They are removed.<br><br>This parameter is optional, the default is 1. |
| proc_lev_sets | Whether duplicate level sets are removed:<br><br>- 0: They are not removed.<br>- 1: They are removed.<br><br>This parameter is optional, the default is 1. |
| proc_lev_specsets | Whether duplicate level spec sets are removed:<br><br>- 0: They are not removed.<br>- 1: They are removed.<br><br>This parameter is optional, the default is 1. |
| proc_specifications | Whether duplicate specifications are removed:<br><br>- 0: They are not removed.<br>- 1: They are removed.<br><br>This parameter is optional, the default is 1. |
| proc_merge_pins | Whether definitions for similar pins are merged in the wavetable, timing set, level set, and DPS pins definitions:<br><br>- 0: They are not merged.<br>- 1: They are merged.<br><br>This parameter is optional, the default is 0. |
| skip_wavetables | <wavetables> is a list of wavetables that are not removed from the MTP even if they are duplicates.<br><br>The value is a list of wavetable names, enclosed in quotes and separated by commas. For example: ['wt1', 'wt2', 'wt3']<br><br>This parameter is optional. |
| skip_tim_eqnsets | <tim_eqnsets> is a list of timing equation sets that are not removed from the MTP even if they are duplicates.<br><br>The value is a list of equation set numbers separated by commas. For example: [1, 5, 9, 13]<br><br>This parameter is optional. |
| skip_lev_eqnsets | <lev_eqnsets> is a list of level equation sets that are not removed from the MTP even if they are duplicates.<br><br>The value is a list of equation set numbers separated by commas. For example: [7,8]<br><br>This parameter is optional. |
| skip_specifications | <specifications> is a list of specifications that are not removed from the MTP even if they are duplicates.<br><br>The value is a list of specification names, enclosed in quotes and separated by commas. For example: ['spec1', 'spec2', 'spec3']<br><br>This parameter is optional. |
| analyze_only | <analyze_flag> specifies whether duplicate primaries are actually removed:<br><br>- 0: Any found duplicates are removed.<br>- 1: No primaries are removed but STPM generates a report of found duplicates.<br><br>This parameter is optional, the default is 0. |
| analyzer_path | <path> is the name and location of the report file containing the result of the analysis.<br><br>If analyze_only (see above) is 0, this parameter is ignored. If analyze_only is 1, this parameter is observed.<br><br>This parameter is optional. If it is not specified, the default is <device directory>/reports/duplicated_report.csv. |
| pre_proc | <pre_proc> is a script that is executed before this command.<br><br>The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.<br><br>This is an optional parameter. |
| post_proc | <post_proc> is a script that is executed after this command.<br><br>The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.<br><br>This is an optional parameter. |

### Syntax（取自子主题 STPM control file › clear unused）

```
clear_unused(
[proc_timing = <0_or_1>, ]
[proc_levels = <0_or_1>, ]
[proc_patterns = <0_or_1>, ]
[proc_ports = <0_or_1>, ]
[proc_groups = <0_or_1>, ]
[proc_nonexistent_pins = <0_or_1>, ]
[skip_wavetables = [<wavetables>], ]
[skip_tim_eqnsets = [<tim_eqnsets>], ]
[skip_lev_eqnsets = [<lev_eqnsets>], ]
[skip_specifications = [<specifications>], ]
[skip_patterns = [<patterns>], ]
[analyze_only = <analyze_flag>, ]
[analyzer_path = <path>, ]
[pre_proc = <pre_proc>, ]
[post_proc =<post_proc>]
)
```

### Parameters（取自子主题 STPM control file › clear unused）

The parameters in the order in which they are listed above:

| proc_timing | Whether unused wavetables, timing equation sets, timing sets, and timing spec sets are deleted from the MTP:<br><br>- 0: They are not removed.<br>- 1: They are removed.<br><br>This parameter is optional, the default is 1. |
|---|---|
| proc_levels | Whether unused level equation sets, level sets, and level spec sets are deleted from the MTP:<br><br>- 0: They are not removed.<br>- 1: They are removed.<br><br>This parameter is optional, the default is 1. |
| proc_patterns | Whether unused pattern labels are removed:<br><br>- 0: They are not removed.<br>- 1: They are removed.<br><br>This parameter is optional, the default is 1. |
| proc_ports | Whether unused ports are removed:<br><br>- 0: They are not removed.<br>- 1: They are removed.<br><br>This parameter is optional, the default is 1. |
| proc_groups | Whether unused pin groups are removed:<br><br>- 0: They are not removed.<br>- 1: They are removed.<br><br>This parameter is optional, the default is 1. |
| proc_nonexistent_pins | Whether timing and level specifications for unused pins are removed:<br><br>- 0: They are not removed.<br>- 1: They are removed.<br><br>This parameter is optional, the default is 0. |
| skip_wavetables | <wavetables> is a list of wavetables that are not removed from the MTP even if they are unused.<br><br>The value is a list of wavetable names, enclosed in quotes and separated by commas. For example: ['wt1', 'wt2', 'wt3']<br><br>This parameter is optional. |
| skip_tim_eqnsets | <tim_eqnsets> is a list of timing equation sets that are not removed from the MTP even if they are unused.<br><br>The value is a list of equation set numbers separated by commas. For example: [1, 5, 9, 13]<br><br>This parameter is optional. |
| skip_lev_eqnsets | <lev_eqnsets> is a list of level equation sets that are not removed from the MTP even if they are unused.<br><br>The value is a list of equation set numbers separated by commas. For example: [7,8]<br><br>This parameter is optional. |
| skip_specifications | <specifications> is a list of specifications that are not removed from the MTP even if they are unused.<br><br>The value is a list of specification names, enclosed in quotes and separated by commas. For example: ['spec1', 'spec2', 'spec3']<br><br>This parameter is optional. |
| skip_patterns | <patterns> is a list of pattern files that are not removed from the MTP even if they are unused.<br><br>The value is a list of paths of pattern files, enclosed in quotes and separated by commas. The paths can be either absolute or relative to current device directory (in which case they must include the name of the directory).<br><br>For example (assuming a device directory named mtp): ['/usr/engineer/pat.binl', 'mtp/vectors/DAC/pat.binl']<br><br>This parameter is optional. |
| analyze_only | <analyze_flag> specifies whether duplicate primaries are actually removed:<br><br>- 0: Any found duplicates are removed.<br>- 1: No primaries are removed but STPM generates a report of found duplicates.<br><br>This parameter is optional, the default is 0. |
| analyzer_path | <path> is the name and location of the report file containing the result of the analysis.<br><br>If analyze_only (see above) is 0, this parameter is ignored. If analyze_only is 1, this parameter is observed.<br><br>This parameter is optional. If it is not specified, the default is <device directory>/reports/unused_report.csv. |
| pre_proc | <pre_proc> is a script that is executed before this command.<br><br>The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.<br><br>This is an optional parameter. |
| post_proc | <post_proc> is a script that is executed after this command.<br><br>The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.<br><br>This is an optional parameter. |

### Syntax（取自子主题 STPM merge rules file › STPM merge rules file syntax）

The merge rules file contains a range of flags, which can be set to allow, reject, or ignore. Not all options are available for all flags.

The three settings usually have the same general effect:

- allow: STPM performs the merger and automatically resolves any conflicts that may occur. This automatic resolution may have side effects, such as when pin numbers change.
- ignore: STPM performs the merger but does not resolve any conflicts that may occur. If the rule was triggered, you will usually need to manually resolve the issues in the target file (processed MTP).
- reject: STPM aborts the merger with an error without changing the MTP. You will have to manually resolve the issue in the source files (STP and/or original MTP).

This table lists the available flags and their supported settings. For details on the effect of each flag, see the pages describing the individual flags.

 |

Flag

 |

Available settings

 |

Default

 |
 |

Allow

 |

Ignore

 |

Reject

 |
 |

Pin, port, and site rules

 |

 |

 |

 |

 |
 |

`new_digital_pin`（raw: `02.09.02.04.02_new_digital_pin.md`）

 |

+

 |

 |

+

 |

allow

 |
 |

`overwrite_digital_pin_no`（raw: `02.09.02.04.03_overwrite_digital_pin_no.md`）

 |

+

 |

+

 |

+

 |

ignore

 |
 |

`merge_digital_pin_dir`（raw: `02.09.02.04.04_merge_digital_pin_dir.md`）

 |

+

 |

 |

+

 |

allow

 |
 |

`new_dps_pin`（raw: `02.09.02.04.05_new_dps_pin.md`）

 |

+

 |

 |

+

 |

allow

 |
 |

`overwrite_dps_pin_polarity`（raw: `02.09.02.04.06_overwrite_dps_pin_polarity.md`）

 |

+

 |

+

 |

+

 |

ignore

 |
 |

`new_pin_group`（raw: `02.09.02.04.07_new_pin_group.md`）

 |

+

 |

+

 |

+

 |

allow

 |
 |

`overwrite_pin_group`（raw: `02.09.02.04.08_overwrite_pin_group.md`）

 |

+

 |

+

 |

+

 |

ignore

 |
 |

`merge_unused_pin_group`（raw: `02.09.02.04.09_merge_unused_pin_group.md`）

 |

+

 |

+

 |

 |

allow

 |
 |

`new_port`（raw: `02.09.02.04.10_new_port.md`）

 |

+

 |

 |

+

 |

allow

 |
 |

`overwrite_port`（raw: `02.09.02.04.11_overwrite_port.md`）

 |

+

 |

+

 |

+

 |

reject

 |
 |

`new_site`（raw: `02.09.02.04.12_new_site.md`）

 |

+

 |

 |

+

 |

allow

 |
 |

`overwrite_channel`（raw: `02.09.02.04.13_overwrite_channel.md`）

 |

+

 |

+

 |

+

 |

ignore

 |
 |

Timing and levels rules

 |

 |

 |

 |

 |
 |

`new_timing_equation_set`（raw: `02.09.02.04.14_new_timing_equation_set.md`）

 |

+

 |

 |

+

 |

allow

 |
 |

`new_waveform`（raw: `02.09.02.04.15_new_waveform.md`）

 |

+

 |

 |

+

 |

allow

 |
 |

`modify_waveform_index`（raw: `02.09.02.04.16_modify_waveform_index.md`）

 |

+

 |

 |

+

 |

allow

 |
 |

`overwrite_statemap`（raw: `02.09.02.04.17_overwrite_statemap.md`）

 |

+

 |

+

 |

+

 |

ignore

 |
 |

`new_level_resource`（raw: `02.09.02.04.18_new_level_resource.md`）

 |

+

 |

+

 |

+

 |

allow

 |
 |

`overwrite_level_resource`（raw: `02.09.02.04.19_overwrite_level_resource.md`）

 |

+

 |

+

 |

+

 |

ignore

 |
 |

`new_level_equation_set`（raw: `02.09.02.04.20_new_level_equation_set.md`）

 |

+

 |

 |

+

 |

allow

 |
 |

`new_level_set`（raw: `02.09.02.04.21_new_level_set.md`）

 |

+

 |

 |

+

 |

allow

 |
 |

`new_ac_specset`（raw: `02.09.02.04.22_new_ac_specset.md`）

 |

+

 |

 |

+

 |

allow

 |
 |

`new_dc_specset`（raw: `02.09.02.04.23_new_dc_specset.md`）

 |

+

 |

 |

+

 |

allow

 |
 |

`overwrite_ac_spec_typ`（raw: `02.09.02.04.24_overwrite_ac_spec_typ.md`）

 |

+

 |

+

 |

+

 |

reject

 |
 |

`overwrite_ac_spec_minmax`（raw: `02.09.02.04.25_overwrite_ac_spec_minmax.md`）

 |

+

 |

+

 |

+

 |

reject

 |
 |

`overwrite_dc_spec_typ`（raw: `02.09.02.04.26_overwrite_dc_spec_typ.md`）

 |

+

 |

+

 |

+

 |

reject

 |
 |

`overwrite_dc_spec_minmax`（raw: `02.09.02.04.27_overwrite_dc_spec_minmax.md`）

 |

+

 |

+

 |

+

 |

reject

 |
 |

Pattern rules

 |

 |

 |

 |

 |
 |

`overwrite_label_wvt`（raw: `02.09.02.04.28_overwrite_label_wvt.md`）

 |

+

 |

+

 |

 |

allow

 |
 |

Testflow rules

 |

 |

 |

 |

 |
 |

`overwrite_flow_var_value`（raw: `02.09.02.04.29_overwrite_flow_var_value.md`）

 |

+

 |

+

 |

+

 |

reject

 |

### Example（取自子主题 STPM merge rules file › STPM merge rules file syntax）

This example merge rules file sets all available options. Note that this is not necessary; if an option is missing, the default setting is used for it.

```
new_digital_pin            = 'reject'
overwrite_digital_pin_no   = 'reject'
merge_digital_pin_dir      = 'reject'
new_dps_pin                = 'reject'
overwrite_dps_pin_polarity = 'reject'
new_pin_group              = 'allow'
overwrite_pin_group        = 'ignore'
merge_unused_pin_group     = 'ignore'
new_port                   = 'allow'
overwrite_port             = 'reject'
new_site                   = 'reject'
overwrite_channel          = 'ignore'

new_timing_equation_set  = 'allow'
new_waveform             = 'reject'
modify_waveform_index    = 'reject'
overwrite_statemap       = 'reject'
new_level_resource       = 'reject'
overwrite_level_resource = 'reject'
new_level_equation_set   = 'allow'
new_level_set            = 'allow'
new_ac_specset           = 'allow'
new_dc_specset           = 'allow'
overwrite_ac_spec_minmax = 'reject'
overwrite_dc_spec_minmax = 'reject'
overwrite_ac_spec_typ    = 'reject'
overwrite_dc_spec_typ    = 'reject'
```

```

overwrite_label_wvt      = 'reject'

overwrite_flow_var_value = 'reject'
```

### Syntax（取自子主题 STPM merge rules file › new digital pin）

The new_digital_pin flag can be set to allow (default) or reject:

- allow

STPM adds the pin to the MTP and notes it in the log:

```
Warning: New digital pin 'sig1' was added to MTP.
```

- reject

STPM does not add the pin or the test to the MTP and the merge process fails. The error is noted in the log:

```
Error: Digital pin 'sig1' is not defined in MTP.
```

### Example（取自子主题 STPM merge rules file › new digital pin）

This setting makes sure that no digital pins are added to the MTP and merge processes fail that would require pins to be added:

```
new_digital_pin = 'reject'
```

### Syntax（取自子主题 STPM merge rules file › overwrite digital pin no）

The overwrite_digital_pin_no flag can be set to allow, ignore (default), or reject:

- allow

STPM changes the pin number in the MTP and notes it in the log:

```
Warning: Pin number conflict detected: digital pin 'sig1', '1'(STP)->'2'(MTP)
(overwriting MTP pin number by '1')
```

- ignore

STPM does not change the pin number in the MTP but still adds the test from the STP (source test program) and notes it in the log:

```
Warning: Pin number conflict detected: digital pin 'sig1', '1'(STP)->'2'(MTP)
(keeping MTP pin number '2')
```

- reject

STPM does not add the test to the MTP and the merge process fails. The error is noted in the log:

```
Error: Pin number conflict detected: digital pin 'sig1', '1'(STP)->'2'(MTP)
```

### Example（取自子主题 STPM merge rules file › overwrite digital pin no）

This setting makes sure that no digital pins are renumbered in the MTP and merge processes fail that would require pins to be renumbered:

```
overwrite_digital_pin_no = 'reject'
```

### Syntax（取自子主题 STPM merge rules file › merge digital pin dir）

The merge_digital_pin_dir flag can be set to allow (default) or reject:

- allow

STPM changes all pins in the MTP with incompatible directions to IO pins and notes it in the log:

```
Warning: Pin type conflict detected: digital pin 'clk',
'IO'->'I' (merging pin types, IO + I -> IO)
Warning: Pin type conflict detected: digital pin 'sigA',
'IO'->'I' (merging pin types, IO + I -> IO)
```

- reject

STPM does not add the test to the MTP and the merge process fails. The error is noted in the log:

```
Error: Pin type conflict detected: digital pin 'clk', 'O'->'I'
Error: Pin type conflict detected: digital pin 'sigA', 'IO'->'O'
```

### Example（取自子主题 STPM merge rules file › merge digital pin dir）

This setting makes sure that all digital pins in the MTP keep their directions and merge processes fail that would require pins to change their direction:

```
merge_digital_pin_dir = 'reject'
```

### Syntax（取自子主题 STPM merge rules file › new dps pin）

The new_dps_pin flag can be set to allow (default) or reject:

- allow

STPM adds the pin to the MTP and notes it in the log:

```
Warning: New power supply pin 'vcc1' was added to MTP.
```

- reject

STPM does not add the pin or the test to the MTP and the merge process fails. The error is noted in the log:

```
Error: Power supply pin 'vcc1' is not defined in MTP
```

### Example（取自子主题 STPM merge rules file › new dps pin）

This setting makes sure that no DPS pins are added to the MTP and merge processes fail that would require pins to be added:

```
new_dps_pin = 'reject'
```

### Syntax（取自子主题 STPM merge rules file › overwrite dps pin polarity）

The overwrite_dps_pin_polarity flag can be set to allow, ignore (default), or reject:

- allow

STPM changes the pin polarity in the MTP and notes it in the log:

```
Warning: Polarity conflict detected: power supply pin 'vcc', 'NEG'(STP)->'POS'(MTP)
(overwriting MTP pin polarity by 'NEG')
```

- ignore

STPM does not change the pin polarity in the MTP but still adds the test from the STP (source test program) and notes it in the log:

```
Warning: Polarity conflict detected: power supply pin 'vcc', 'NEG'(STP)->'POS'(MTP)
(keeping MTP pin polarity 'POS')
```

- reject

STPM does not add the test to the MTP and the merge process fails. The error is noted in the log:

```
Error: Polarity conflict detected: power supply pin 'vcc', 'NEG'(STP)->'POS'(MTP)
```

### Example（取自子主题 STPM merge rules file › overwrite dps pin polarity）

This setting makes sure that no DPS pin polarities are changed in the MTP and merge processes fail that would require pin polarities to be changed:

```
overwrite_dps_pin_polarity = 'reject'
```

### Syntax（取自子主题 STPM merge rules file › new pin group）

The new_pin_group flag can be set to allow (default), ignore, or reject:

- allow

STPM adds the pin group to the MTP and notes it in the log:

```
Warning: New pin group 'MY_GROUP' was added to MTP
```

- ignore

STPM adds the test to the MTP but does not create the pin group in the MTP. Instead, it uses the individual member pins of the ignored group in the MTP.

This is noted in the log:

```
Warning: Pin group 'MY_GROUP' is not defined in MTP (ignored)
```

- reject

STPM does not add the pin group or the test to the MTP and the merge process fails. The error is noted in the log:

```
Error: Pin group 'MY_GROUP' is not defined in MTP
```

### Example（取自子主题 STPM merge rules file › new pin group）

This setting causes STPM to always automatically create new pin groups when they are needed to merge tests:

```
new_pin_group = 'allow'
```

### Syntax（取自子主题 STPM merge rules file › overwrite pin group）

The overwrite_pin_group flag can be set to allow, ignore (default), or reject:

- allow

STPM changes the pin group definition in the MTP. Any pins that were part of the group before its definition was overwritten and now are no longer part of it are added individually in all locations where the group is used.

This is noted in the log:

```
Warning: Pin group conflict detected: group 'all_inputs',
'I:clk,data,sigA,sigB'(STP)->'I:clk,data,sigA'(MTP)
(overwriting MTP group by I:clk,data,sigA,sigB)
```

- ignore

STPM does not change the pin group definition in the MTP but still adds the test from the STP (source test program) and notes it in the log:

```
Warning: Pin group conflict detected: group 'all_inputs',
'I:clk,data,sigA,sigB'(STP)->'I:clk,data,sigA'(MTP)
(keeping MTP group definition I:clk,data,sigA)
```

- reject

STPM does not add the test to the MTP and the merge process fails. The error is noted in the log:

```
Error: Pin group conflict detected: group 'all_inputs',
'I:clk,data,sigA,sigB'(STP)->'I:clk,data,sigA'(MTP)
```

### Example（取自子主题 STPM merge rules file › overwrite pin group）

This setting makes sure that no pin group definitions in the MTP are changed but that merge processes requiring such changes still succeed. (This usually requires you to fix the resulting MTP before it can be used.)

```
overwrite_pin_group = 'ignore'
```

### Syntax（取自子主题 STPM merge rules file › merge unused pin group）

The merge_unused_pin_group flag can be set to allow (default) or ignore:

- allow

STPM imports the pin group definition into the MTP.

- ignore

STPM does not import the pin group definition into the MTP.

In both cases, the test is imported into the MTP. Note that this rule affects only unused pin groups; it has no effect on used pin groups.

### Example（取自子主题 STPM merge rules file › merge unused pin group）

This setting makes sure that only pin group definitions are imported into the MTP that are actually used.

```
merge_unused_pin_group = 'ignore'
```

### Syntax（取自子主题 STPM merge rules file › new port）

The new_port flag can be set to allow (default) or reject:

- allow

STPM adds the port definition to the MTP and notes it in the log:

```
Warning: New port 'port1' was added to MTP
```

- reject

STPM does not add the port definition or the test to the MTP and the merge process fails. The error is noted in the log:

```
Error: Port 'port1' is not defined in MTP
```

### Example（取自子主题 STPM merge rules file › new port）

This setting causes STPM to add any new port definitions to the MTP when they are needed to merge a test:

```
new_port = 'allow'
```

### Syntax（取自子主题 STPM merge rules file › overwrite port）

The overwrite_port flag can be set to allow, ignore, or reject (default):

- allow

STPM changes the port definition in the MTP and notes it in the log:

```
Warning: Port conflict detected: port 'port1', 'sigA,clk'(STP)->'sigA'(MTP) (overwriting MTP port by sigA,clk)
```

- ignore

STPM does not change the port definition in the MTP but still adds the test from the STP (source test program) and notes it in the log:

```
Warning: Port conflict detected: port 'port1', 'sigA,clk'(STP)->'sigA'(MTP) (keeping MTP port definition sigA)
```

- reject

STPM does not add the port definition or the test to the MTP and the merge process fails. The error is noted in the log:

```
Error: Port conflict detected: port 'port1', 'sigA,clk'(STP)->'sigA'(MTP)
```

### Example（取自子主题 STPM merge rules file › overwrite port）

This setting makes sure that no port definitions are changed in the MTP and merge processes fail that would require ports to be redefined:

```
overwrite_port = 'reject'
```

### Syntax（取自子主题 STPM merge rules file › new site）

The new_site flag can be set to allow (default) or reject:

- allow

STPM adds the site definition to the MTP and notes it in the log:

```
Warning: Sites 2..5 are not defined in MTP (added)
```

- reject

STPM does not add the site definition or the test to the MTP and the merge process fails. The error is noted in the log:

```
Error: Sites 2..5 are not defined in MTP
```

### Example（取自子主题 STPM merge rules file › new site）

This setting makes sure that no site definitions are added to the MTP and merge processes fail that would require site definitions to be added:

```
new_site = 'reject'
```

### Syntax（取自子主题 STPM merge rules file › overwrite channel）

The overwrite_channel flag can be set to allow, ignore (default), or reject:

- allow

STPM changes the channel definition in the MTP and notes it in the log:

```
Warning: Pin channel conflict detected: pin 'sigB', site 1, '10406'(STP)->'10405'(MTP)
(overwriting MTP channel by '10406')
```

- ignore

STPM does not change the channel definition in the MTP but still adds the test from the STP (source test program) and notes it in the log:

```
Warning: Pin channel conflict detected: pin 'sigB', site 1, '10406'(STP)->'10405'(MTP)
(keeping MTP channel '10405')
```

- reject

STPM does not add the channel definition or the test to the MTP and the merge process fails. The error is noted in the log:

```
Error: Pin channel conflict detected: pin 'sigB', site 1, '10406'(STP)->'10405'(MTP)
```

### Example（取自子主题 STPM merge rules file › overwrite channel）

This setting makes sure that no channel definitions in the MTP are changed but that merge processes requiring such changes still succeed. (This usually requires you to fix the resulting MTP before it can be used.)

```
overwrite_channel = 'ignore'
```

### Syntax（取自子主题 STPM merge rules file › new timing equation set）

The new_timing_equation_set flag can be set to allow (default) or reject:

- allow

STPM adds a new wavetable, equation set, and spec set to the MTP and notes it in the log. Note that it first adds an error message to the log caused by the inability to reuse existing primaries, but this error is non-fatal and does not prevent the test from being added:

```
Trying to reuse the following tests primaries:
 [Stil_1]
  Error: Equation 'eq_shared = 2.51' differs from master equation in MTP EQNSET 1
Reuse failed - see errors above.
Adding WAVETBL 'wt1'
Adding EQNSET 2
Adding SPECSET 1
```

- reject

STPM does not add the primaries or the test to the MTP and the merge process fails. The error is noted in the log:

```
Trying to reuse the following tests primaries:
 [Stil_1]
  Error: Equation 'eq_shared = 2.51' differs from master equation in MTP EQNSET 1
Reuse failed - see errors above.
Adding WAVETBL 'wt1'
Adding EQNSET 2
Error: Failed: adding new equation set was rejected by merge rule 'new_timing_equation_set'
```

### Example（取自子主题 STPM merge rules file › new timing equation set）

This setting causes STPM to add any new timing equations to the MTP when they are needed to merge a test:

```
new_timing_equation_set = 'allow'
```

### Syntax（取自子主题 STPM merge rules file › new waveform）

The new_waveform flag can be set to allow (default) or reject:

- allow

STPM adds a new waveform to the MTP and notes it in the log. Note that it first adds an error message to the log caused by the inability to reuse existing waveforms, but this error is non-fatal and does not prevent the test from being added:

```
Trying to reuse the following tests primaries:
 [Stil_1]
  Error: Waveform [1 "0.0:1 25.0:F1N 75.0:F0N" M]
  is not covered by any MTP waveform in pin 'clk', wavetable 'wt1'
Reuse failed - see errors above.
Adding WAVETBL 'wt1'
Adding EQNSET 2
Adding SPECSET 1
```

- reject

STPM does not add the waveform to the MTP. Instead, it tries to add a new timing equation set. If that succeeds, the test is added to the MTP. If adding the equation set fails, the merge process fails and the MTP is not changed.

The error is noted in the log:

```
Trying to reuse the following tests primaries:
 [Stil_1]
  Error: Waveform [1 "0.0:1 25.0:F1N 75.0:F0N" M]
  is not covered by any MTP waveform in pin 'clk', wavetable 'wt1'
Reuse failed - see errors above.
```

### Example（取自子主题 STPM merge rules file › new waveform）

This setting makes sure that no waveforms are added to the MTP and merge processes fail that would require waveforms to be added:

```
new_waveform = 'reject'
```

### Syntax（取自子主题 STPM merge rules file › modify waveform index）

The modify_waveform_index flag can be set to allow (default) or reject:

- allow

STPM changes the waveform index in the added test and notes it in the log. It also modifies the patterns using these waveforms, which may greatly increase the processing time for adding large tests (patterns with hundreds of megabytes).

Note that it first adds an error message to the log caused by the inability to reuse an existing waveform index, but this error is non-fatal and does not prevent the test from being added:

```
Trying to reuse the following tests primaries:
 [Stil_11]
  Warning: Waveform [0 "0.0:1 25.0:F1N 75.0:F0N" P]
  is not covered by any MTP waveform in pin 'clk', wavetable 'wt1'
  Error: Waveform [0 "0.0:1 25.0:F1N 75.0:F0N" P]
  index was changed (0->1) in pin 'clk', wavetable 'wt1'
```

- reject

STPM does not change the waveform index. Instead, it tries to add a new timing equation set. If that succeeds, the test is added to the MTP. If adding the equation set fails, the merge process fails and the MTP is not changed.

```
The error is noted in the log:Trying to reuse the following tests primaries:
 [Stil_1]
  Warning: Waveform [0 "0.0:1 25.0:F1N 75.0:F0N" P]
  is not covered by any MTP waveform in pin 'clk', wavetable 'wt1'
  Error: Waveform [0 "0.0:1 25.0:F1N 75.0:F0N" P]
  index was changed (0->1) in pin 'clk', wavetable 'wt1'
Reuse failed - see errors above.
```

### Example（取自子主题 STPM merge rules file › modify waveform index）

This setting makes sure that no waveforms in the MTP are reused with a different index, and merge processes fail that would require waveforms to be reused with a different index:

```
modify_waveform_index = 'reject'
```

### Syntax（取自子主题 STPM merge rules file › overwrite statemap）

The overwrite_statemap flag can be set to allow, ignore (default), or reject:

- allow

STPM overwrites the state map in the MTP and notes it in the log:

```
Warning: Statemap info of waveform [2 "{ 80.0:L }" L] differs from MTP
waveform statemap in pin 'data', wavetable 'wt1':
 [H x1 wt1] != [L x1 wt1] (overwriting master statemap by 'H x1 wt1')
```

- ignore

STPM does not change the state map in the MTP but still adds the test from the STP (source test program) and notes it in the log:

```
Warning: Statemap info of waveform [2 "{ 80.0:L }" L] differs from MTP
waveform statemap in pin 'data', wavetable 'wt1':
 [H x1 wt1] != [L x1 wt1] (keeping master statemap 'L x1 wt1')
```

- reject

STPM does not change the state map. Instead, it tries to add a new timing equation set. If that succeeds, the test is added to the MTP. If adding the equation set fails, the merge process fails and the MTP is not changed.

The error is noted in the log:

```
Error: Statemap info of waveform [2 "{ 80.0:L }" L] differs from MTP
waveform statemap in pin 'data', wavetable 'wt1':
 [H x1 wt1] != [L x1 wt1]
```

### Example（取自子主题 STPM merge rules file › overwrite statemap）

This setting makes sure that the state map of the MTP is not overwritten and merge processes fail that would require it to be overwritten:

```
overwrite_statemap = 'reject'
```

### Syntax（取自子主题 STPM merge rules file › new level resource）

The new_level_resource flag can be set to allow (default) or reject:

- allow

STPM adds the level resource to the MTP and notes it in the log:

```
Warning: Resource 'ioh' is not defined for master pin 'out' in
levelset 1 (set to the new value: '5.0').
```

- reject

STPM does not add the level resource or the test to the MTP and the merge process fails. The error is noted in the log:

```
Error: Resource 'ioh' is not defined for master pin 'out' in levelset 1
```

### Example（取自子主题 STPM merge rules file › new level resource）

This setting makes sure that no level resources are added to the MTP and merge processes fail that would require level resources to be added:

```
new_level_resource = 'reject'
```

### Syntax（取自子主题 STPM merge rules file › overwrite level resource）

The overwrite_level_resource flag can be set to allow, ignore (default), or reject:

- allow

STPM overwrites the level resource in the MTP and notes it in the log:

```
Warning: Resource 'vih' conflict detected for master pin 'clk'
in levelset 1 (vil != vih) (keeping master resource value 'vih')
```

- ignore

STPM does not change the level resource in the MTP but still adds the test from the STP (source test program) and notes it in the log:

```
Warning: Resource 'vih' conflict detected for master pin 'clk'
in levelset 1 (vil != vih) (overwriting master resource value by 'vil')
```

- reject

STPM does not change the level resource. Instead, it tries to add a new level equation set. If that succeeds, the test is added to the MTP. If adding the equation set fails, the merge process fails and the MTP is not changed.

The error is noted in the log:

```
Error: Resource 'vih' conflict detected for master pin 'clk' in levelset 1 (vil != vih)
```

### Example（取自子主题 STPM merge rules file › overwrite level resource）

This setting makes sure that the level resources in the MTP are not overwritten and merge processes fail that would require level resources to be overwritten:

```
overwrite_level_resource = 'reject'
```

### Syntax（取自子主题 STPM merge rules file › new level equation set）

The new_level_equation_set flag can be set to allow (default) or reject:

- allow

STPM adds the level equation set to the MTP and notes it in the log. Note that it first adds an error message to the log, but this error is non-fatal and does not prevent the test from being added:

```
Error: Resource 'vih' conflict detected for master pin 'clk' in
levelset 1 (vil != vih)
Warning: Resource 'ioh' is not defined for master pin 'out' in
levelset 1 (set to the new value: '5.0' ).
Adding new levels equation set [EQNSET 3 'DCL2']
Adding new levels specset [SPECSET 1 'Cat1_Sel1']
```

- reject

STPM does not add the level equation set or the test to the MTP and the merge process fails. The error is noted in the log:

```
Error: Resource 'vih' conflict detected for master pin 'clk' in
levelset 1 (vil != vih)
Warning: Resource 'ioh' is not defined for master pin 'out' in
levelset 1 (set to the new value: '5.0' ).
```

### Example（取自子主题 STPM merge rules file › new level equation set）

This setting causes STPM to add any new level equation sets to the MTP when they are needed to merge a test:

```
new_level_equation_set = 'allow'
```

### Syntax（取自子主题 STPM merge rules file › new level set）

The new_level_set flag can be set to allow (default) or reject:

- allow

STPM adds the level set to the MTP and notes it in the log. Note that it first adds an error message to the log, but this error is non-fatal and does not prevent the test from being added:

```
Error: Resource 'ioh' is not defined for master pin 'out' in levelset 1
Warning: Adding new levelset [LEVELSET 1 'DCL2'] due to the conflict(s) above
```

- reject

STPM does not add the level set to the MTP. Instead, it tries to add a new level equation set. If that succeeds, the test is added to the MTP. If adding the equation set fails, the merge process fails and the MTP is not changed.

The error is noted in the log:

```
Error: Resource 'vih' conflict detected for master pin 'clk' in
levelset 1 (vil != vih)
```

### Example（取自子主题 STPM merge rules file › new level set）

This setting causes STPM to add any new level sets to the MTP when they are needed to merge a test:

```
new_level_set = 'allow'
```

### Syntax（取自子主题 STPM merge rules file › new ac specset）

The new_ac_specset flag can be set to allow (default) or reject:

- allow

STPM adds the AC spec set to the MTP and notes it in the log:

```
Warning: Spec 'my_values.max' value differs from master spec value
in specset 1 (61 != 6)
Warning: New specset required due to the conflict(s) above.
Adding SPECSET 12
```

- reject

STPM does not add the spec set to the MTP. Instead, it tries to add new level and timing equation sets. If that succeeds, the test is added to the MTP. If adding the equation sets fails, the merge process fails and the MTP is not changed.

The error is noted in the log:

```
Error: Spec 'my_values.max' value differs from master spec value
in specset 1 (61 != 6)
```

### Example（取自子主题 STPM merge rules file › new ac specset）

This setting causes STPM to add any new AC spec sets to the MTP when they are needed to merge a test:

```
new_ac_specset = 'allow'
```

### Syntax（取自子主题 STPM merge rules file › new dc specset）

The new_dc_specset flag can be set to allow (default) or reject:

- allow

STPM adds the DC spec set to the MTP and notes it in the log:

```
Warning: Spec 'vih.max' value differs from master spec value
in specset 1 (4.31 != 4.3)
Warning: New specset required due to the conflict(s) above.
Adding SPECSET 12
```

- reject

STPM does not add the spec set to the MTP. Instead, it tries to add new level and timing equation sets. If that succeeds, the test is added to the MTP. If adding the equation sets fails, the merge process fails and the MTP is not changed.

The error is noted in the log:

```
Error: Spec 'vih.max' value differs from master spec value
in specset 1 (4.31 != 4.3)
```

### Example（取自子主题 STPM merge rules file › new dc specset）

This setting causes STPM to add any new DC spec sets to the MTP when they are needed to merge a test:

```
new_dc_specset = 'allow'
```

### Syntax（取自子主题 STPM merge rules file › overwrite ac spec typ）

The overwrite_ac_spec_typ flag can be set to allow, ignore, or reject (default):

- allow

STPM overwrites the AC spec value in the MTP and notes it in the log:

```
Warning: Spec 'my_values.typ' value differs from
master spec value in specset 1 (5.1 != 5)
(overwriting master spec value by '5.1')
```

- ignore

STPM does not change the AC spec value in the MTP but still adds the test from the STP (source test program) and notes it in the log:

```
Warning: Spec 'my_values.typ' value differs from
master spec value in specset 1 (5.1 != 5)
(keeping master spec value '5')
```

- reject

STPM does not change the AC spec value. Instead, it tries to add new level and timing equation sets. If that succeeds, the test is added to the MTP. If adding the equation sets fails, the merge process fails and the MTP is not changed.

The error is noted in the log:

```
Error: Spec 'my_values.typ' value differs from master spec value in specset 1 (5.1 != 5)

```

### Example（取自子主题 STPM merge rules file › overwrite ac spec typ）

This setting makes sure that the typical AC spec values in the MTP are not overwritten and merge processes fail that would require these values to be overwritten:

```
overwrite_ac_spec_typ = 'reject'
```

### Syntax（取自子主题 STPM merge rules file › overwrite ac spec minmax）

The overwrite_ac_spec_minmax flag can be set to allow, ignore, or reject (default):

- allow

STPM overwrites the AC spec values in the MTP and notes it in the log:

```
Warning: Spec 'my_values.min' value differs from master spec value
in specset 1 (42 != 4) (overwriting master spec value by '42')
Warning: Spec 'my_values.max' value differs from master spec value
in specset 1 (61 != 6) (overwriting master spec value by '61')
```

- ignore

STPM does not change the AC spec values in the MTP but still adds the test from the STP (source test program) and notes it in the log:

```
Warning: Spec 'my_values.min' value differs from master spec value
in specset 1 (42 != 4) (keeping master spec value '4')
Warning: Spec 'my_values.max' value differs from master spec value
in specset 1 (61 != 6) (keeping master spec value '6')
```

- reject

STPM does not change the AC spec value. Instead, it tries to add new level and timing equation sets. If that succeeds, the test is added to the MTP. If adding the equation sets fails, the merge process fails and the MTP is not changed.

The error is noted in the log:

```
Error: Spec 'my_values.min' value differs from master spec value
in specset 1 (42 != 4) (keeping master spec value '4')
Error: Spec 'my_values.max' value differs from master spec value
in specset 1 (61 != 6) (keeping master spec value '6')
```

### Example（取自子主题 STPM merge rules file › overwrite ac spec minmax）

This setting makes sure that the minimum and maximum AC spec values in the MTP are not overwritten and merge processes fail that would require these values to be overwritten:

```
overwrite_ac_spec_minmax = 'reject'
```

### Syntax（取自子主题 STPM merge rules file › overwrite dc spec typ）

The overwrite_dc_spec_typ flag can be set to allow, ignore, or reject (default):

- allow

STPM overwrites the DC spec value in the MTP and notes it in the log:

```
Warning: Spec 'vih.typ' value differs from master spec value
in specset 1 (4.1 != 4) (overwriting master spec value by '4.1')
```

- ignore

STPM does not change the DC spec value in the MTP but still adds the test from the STP (source test program) and notes it in the log:

```
Warning: Spec 'vih.typ' value differs from master spec value
in specset 1 (4.1 != 4) (keeping master spec value '4')
```

- reject

STPM does not change the DC spec value. Instead, it tries to add new level and timing equation sets. If that succeeds, the test is added to the MTP. If adding the equation sets fails, the merge process fails and the MTP is not changed.

The error is noted in the log:

```
Error: Spec 'vih.typ' value differs
from master spec value in specset 1 (4.1 != 4)
```

### Example（取自子主题 STPM merge rules file › overwrite dc spec typ）

This setting makes sure that the typical DC spec values in the MTP are not overwritten and merge processes fail that would require these values to be overwritten:

```
overwrite_dc_spec_typ = 'reject'
```

### Syntax（取自子主题 STPM merge rules file › overwrite dc spec minmax）

The overwrite_dc_spec_minmax flag can be set to allow, ignore, or reject (default):

- allow

STPM overwrites the DC spec values in the MTP and notes it in the log:

```
Warning: Spec 'vih.min' value differs from master spec value
in specset 1 (3.51 != 3.5) (overwriting master spec value by '3.51')
Warning: Spec 'vih.max' value differs from master spec value
in specset 1 (4.31 != 4.3) (overwriting master spec value by '4.31')
```

- ignore

STPM does not change the DC spec values in the MTP but still adds the test from the STP (source test program) and notes it in the log:

```
Warning: Spec 'vih.min' value differs from master spec value
3 in specset 1 (3.51 != 3.5) (keeping master spec value '3.5')
4 Warning: Spec 'vih.max' value differs from master spec value
5 in specset 1 (4.31 != 4.3) (keeping master spec value '4.3')
```

- reject

STPM does not change the DC spec values or add the test to the MTP, and the merge process fails. The error is noted in the log:

```
Error: Spec 'vih.min' value differs from master spec value
in specset 1 (3.51 != 3.5)
```

### Example（取自子主题 STPM merge rules file › overwrite dc spec minmax）

This setting makes sure that the minimum and maximum DC spec values in the MTP are not overwritten and merge processes fail that would require these values to be overwritten:

```
overwrite_dc_spec_minmax = 'reject'
```

### Syntax（取自子主题 STPM merge rules file › overwrite label wvt）

The overwrite_label_wvt flag can be set to allow (default) or ignore:

- allow

STPM replaces the wavetable name in the pattern it imports from the STP with the name of a suitable wavetable that already present in the MTP (if such a wavetable exists). A wavetable is considered suitable if the pattern does not need to be modified (except for the replacement of the wavetable name attribute).

- ignore

STPM always leaves the name of the wavetable in the imported pattern as is and imports the wavetable.

There is no warning irrespective of the setting of this option. This setting has no effect when additional modifications to the pattern are needed during the import.

### Example（取自子主题 STPM merge rules file › overwrite label wvt）

This setting makes sure that the wavetable information in imported patterns is not modified:

```
overwrite_statemap = 'ignore'
```

### Syntax（取自子主题 STPM merge rules file › overwrite flow var value）

The overwrite_flow_var_value flag can be set to allow, ignore, or reject (default):

- allow

STPM overwrites the value of the user testflow variable in the MTP with the value from the STP and generates a warning.

- ignore

STPM keeps the value of the user testflow variable in the MTP (ignoring the value from the STP) and generates a warning.

- reject

STPM stops merging the subflow and generates an error.

### Example（取自子主题 STPM merge rules file › overwrite flow var value）

This setting lets changed values from the STP overwrite the values in the MTP:

```
overwrite_flow_var_value = allow
```

### Syntax（取自子主题 Test program template files › Test suite table of a TPT）

Each row in the test suite table describes one test suite. The table contains these columns:

- TestSuite Name: The name for the test suite in the test program.
- Test Group: The test group in the test program to which the test suite belongs.

If this column is left empty, the test suite is placed in the top level of the testflow.

- Timing: The timing to be used by this test, specified as the indexes of the equation set, spec set, and timing set to use (for example, 1|2|1).

This column can be left empty, in which case any generated test program will not include timing information for this test suite.

- Levels: The levels to be used by this test, specified as the indexes of the equation set, spec set, and level set to use (for example, |speci|1,1,3).

This column can be left empty, in which case any generated test program will not include level information for this test suite.

- Pattern: The name of the pattern to be used by this test.

This column can be left empty, in which case any generated test program will not include pattern information for this test suite.

- Test Flags: The name of a set of test suite flags that is defined in the `test flag table`（raw: `02.09.02.05.05_Test_flag_table_of_a_TPT.md`）. The name you specify here must come from the Flag Set ID column.
- Notes: Any notes you want to make about the test suite. Comments are strictly for human use and are not processed in any way by STPM.

### Syntax（取自子主题 Test program template files › Bin table of a TPT）

Each row in the bin table describes one bin. The table contains these columns:

- SBin: The ID of the software bin. It is used to refer to this bin from the `test suite table`（raw: `02.09.02.05.01_Test_suite_table_of_a_TPT.md`）. To be compatible with the SmarTest Data Formatter, the number must be between 0 and 32767.
- SBin Label: The name of the software bin.
- HBin: The ID of the hardware bin connected to the software bin.
- HBin Label: The name of the hardware bin.

Note that this information will be ignored by STPM when it converts the CSV file into a testflow.

- Type: The type of the bin. It can be "good", "bad", or "other".
- Color: The color for the bin. The color can be any string.

If this column is left empty, STPM uses "" (empty string) for the color.

- Reprobe: The reprobe flag for the bin. It can be 1 (on) or 0 (off).

If this column is left empty, STPM uses 0 (reprobe off).

- Overon: The overon flag for the bin. It can be 1 (on) or 0 (off).

If this column is left empty, STPM uses 0 (overon off).

- Notes: Any notes you want to make about the bin. Comments are strictly for human use and are not processed in any way by STPM.

### Syntax（取自子主题 Test program template files › Test table of a TPT）

Each row in the test suite table describes one test. The table contains these columns:

- Test Suite Name: The name of the test suite in the test program that contains the test. The test suite must be defined with this name in the `test suite table`（raw: `02.09.02.05.01_Test_suite_table_of_a_TPT.md`）.
- Test Name: The name of the test.
- Test Stage: The name of the test stage for which these limits apply.

If this column is left empty, the limits in this row apply to all test stages.

- SBin: The number of the software bin to which this test is connected. You can specify any bin number that is defined in the SBin column of the `bin table`（raw: `02.09.02.05.02_Bin_table_of_a_TPT.md`）.

If this column is left empty, no binning occurs as a result of this test.

- Test Number: The test number for this test.

If this column is left empty, the test number will be generated automatically by SmarTest.

- Lower Limit: The lower limit for this test.

If this column is left empty, there is no lower limit for the test.

- Lower Op: The operator for comparing the lower limit for this test with the measured value.

This column is required when a lower limit has been specified (see above) and ignored otherwise.

- Upper Op: The operator for comparing the measured value with the upper limit for this test with the measured value.

This column is required when an upper limit has been specified (see above) and ignored otherwise.

- Upper Limit: The upper limit for this test.

If this column is left empty, there is no upper limit for the test.

- Unit: The unit for the lower and upper limit values for this test.

Whether a value is required in this column when a limit is specified depends on the test method. The permitted values likewise depend on the test method.

- Source: Whether this limit will be stored in the testflow or in the test table.
- Notes: Any notes you want to make about the test. Comments are strictly for human use and are not processed in any way by STPM.

### Syntax（取自子主题 Test program template files › Test parameter table of a TPT）

Each row in the test suite table describes one set of test parameters. The table contains these columns:

- Test Suite Name: The name of the test suite in the test program to which the parameters apply. The test suite must be defined with this name in the `test suite table`（raw: `02.09.02.05.01_Test_suite_table_of_a_TPT.md`）.
- Test Method: The name of the test method being executed in the test suite.
- Param: Each of these named Param contains the name and value for one parameter that is passed to the test method.

You can create as many parameter columns as desired. Each column must have the title Param.

Parameters must be specified in the column the form <name>`=`<value>, for example, `output=None`.

### Syntax（取自子主题 Test program template files › Test flag table of a TPT）

Each row in the test flag table describes one set of settings of test suite flags. The table contains these columns:

- Flag Set ID: The name for the set of test flags. It is used to refer to this set from the `test suite table`（raw: `02.09.02.05.01_Test_suite_table_of_a_TPT.md`）.
- (individual flags): Each column corresponds to one flag. It can contain 1 to indicate that the flag is on, or 0 to indicate that it is off.
- Notes: Any notes you want to make about the test flag set. Comments are strictly for human use and are not processed in any way by STPM.

### Syntax（取自子主题 Test program template files › Test stage table of a TPT）

Each row in the test flags table describes a test object. The table contains these columns:

- Test Object: The object to which different values are assigned in different test stages. You can specify the name of a test group, test suite, or user testflow variable here.
- Type: The type of the object. Supported types include:

  - GROUP: test group
  - TEST_SUITE: test suite
  - USER_FLAG: user testflow variable

- Stage: <stage>: Each test stage has its own column with the name "Stage" foollowe dby the name of the stage, for example, Stage: QA. You can freely choose the names of the stages.

Each column specifies how the test object is to be handled in this stage:

  - For test groups and test suites, the columns contain Y or N:

Y: The object is included in the test in this stage.

N: The object is not included in the test in this stage.

  - For testflow variables, the columns contain an integer that is assigned to the variable in this test stage.

- Notes: Any notes you want to make about the test object. Comments are strictly for human use and are not processed in any way by STPM.

### Syntax（取自子主题 STPM command line options）

```
stpm[-help][-version][-timestamp][-licwait][-progress][-debug][-template][-setup <control_file>]
```

The parameters have these effects:

- -help: Displays online help. No merging is performed and no file needs to be specified.
- -version: The version of STPM is output to STDOUT.
- -timestamp: A time stamp is added to each line that is output to STDOUT.
- -licwait: If no license is currently available, STPM waits until one becomes available.

If this option is not used, STPM exits with an error message when no license is available.

- -debug: Intermediate file are generated to make debugging easier. What specific files are generated depends on the operations specified in the control file.
- -template: Templates for a `control file`（raw: `02.09.02.03_STPM_control_file.md`） and a `merge rules file`（raw: `02.09.02.04_STPM_merge_rules_file.md`） are created. No conversion is performed and no control file needs to be specified.

The template files are located in the templates subdirectory of the current directory.

- -setup: The control file to use. You can specify the file using a relative or absolute path; relative paths are based on the current directory.

See `STPM Control Fil`（raw: `02.09.02.03_STPM_control_file.md`）`e`（raw: `../02.11_Data_Conversion_and_Bridges/02.11.01.05.03_STIL_Reader_setup_file.md`） for a description of control files.

All of the parameters are optional. Specifying no parameter at all is the same as specifying `stpm -help`.

### Example（取自子主题 STPM command line options）

This example launches STPM with the control file setup/MyControl.setup. If no license is available, STPM will wait until the next license becomes available. Each line it outputs to STDOUT will have a timestamp:

```
stpm -timestamp -licwait -setup setup/MySetup.setup
```

<!-- 语法节 end -->

## 是什么

**先说要紧的：本页的定义文档是一张目录页，不是一篇文章。**
它总共 16 行，**除了 `#### Subtopics` 那张 7 条的清单，一个字都没有**——
没有正文、没有 `## Syntax`、没有 `## Procedure`、没有 `## Related information`。

**所以本页能据文档说的只有一件事：SmarTest Program Manager 是由哪 7 块组成的。**

| # | 子主题（原文清单逐字） | 名字本身说明了什么 |
|---|---|---|
| 1 | `Introduction and installation` | **有安装环节**——它不是即装即用的 |
| 2 | `Using SmarTest Program Manager` | 有使用说明；**它的下级才是操作细节** |
| 3 | `STPM control file` | **一份脚本形态的输入**，见 [[stpm-control-file]] |
| 4 | `STPM merge rules file` | **第二份输入**：合并规则，见 [[stpm-merge-rules-file]] |
| 5 | `Test program template files` | **TPT 这一族文件**——它围绕模板工作 |
| 6 | `STPM command line options` | **能命令行驱动**，不是纯 GUI |
| 7 | `STPM UI plug-in` | **有 GUI 插件**——和本页 `layer: gui` 相符 |

> **「名字本身说明了什么」那一列是按名字读的，原文没有对这些名字做任何解释。**
> **这一列是（推断），不是文档事实。** 唯一能算文档事实的是那 7 个名字本身。

### 缩写 STPM / 本页的标题对不上，但这是原文的写法

页面标题是 **`SmarTest Program Manager`**（原文 `# SmarTest Program Manager`），
而 7 条子主题里有 **5 条用缩写 `STPM`**（第 3、4、6、7 条）、
**1 条用全称**（第 2 条 `Using SmarTest Program Manager`）。
**（推断）`STPM` = `SmarTest Program Manager`**——依据是两处混用同一组词、
且第 4 条 `STPM merge rules file` 与本页的兄弟页 [[stpm-merge-rules-file]] 同名。
**原文没有给出这个缩写的定义**（本页通篇没有一句 `STPM stands for …`）。

### 本页的「语法 / 参数」节不是定义文档写的

本页「语法 / 参数」节**开头自己写明了这件事**，逐字引：

> 「⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。」

**同一段还说这一节有 134,986 字符。**
**也就是说：这一页 5,800 行里，实质内容几乎全部来自那 7 条子主题的下级，
而本页 `sources:` 只有定义文档那一篇——那些下级本页一篇都没读。**

**这正是本页必须读明白的地方：语法节很长，但它长不等于本页有依据。**
**要给某一条命令下判断，得去读它自己那一页。**

## 典型用法

> **原文没有 `## Procedure` / `## Before you begin` / `## What to do next` 段，
> 也没有任何散文。** 定义文档只给了一张目录。
> **所以「怎么用 SmarTest Program Manager」在本页的语料里就是「语料未写」。**

**能说的只有流程骨架，而且它是从名字推出来的（推断）：**

| 阶段 | 对应子主题 | 依据 |
|---|---|---|
| **装** | `Introduction and installation` | 名字里的 `installation` |
| **学怎么用** | `Using SmarTest Program Manager` | 名字 |
| **写输入** | `STPM control file` + `STPM merge rules file` | 两份都被叫 `file` |
| **喂模板** | `Test program template files` | 名字 |
| **跑** | `STPM command line options` / `STPM UI plug-in` | **两条并列 ⇒ 两种驱动方式** |

**「两种驱动方式并列」这一条是有原文支撑的**：第 6 条与第 7 条同时存在，
**一个叫 command line、一个叫 UI plug-in**——
**（推断）同一个工具既能命令行跑、也能在 GUI 里跑**；原文没有说它们是不是等价。

**下一步**：定义文档没有 `## Related information` 段，**所以没有官方的下一步指向**。
**唯一的路是顺着上面那张 7 条清单点下去。**

## 和谁有关

- [[stpm-control-file]] — **本页的第 3 条子主题**，也是 STPM 的主要输入。
  **两页的关系是「工具 ↔ 输入」**；**本页不知道那份文件里有什么**，那要读那一页
- [[stpm-merge-rules-file]] — **本页的第 4 条子主题**，第二份输入
- [[preprocessing-and-postprocessing-scripts]] — **在第 3 条子主题的下级里**
  （它是 `STPM control file` 的子主题之一）；本页没读它
- [[tpt-generate-device-dir]] / [[tpt-import-from-device]] — **在第 5 条子主题
  `Test program template files` 的下级里**；本页没读它们
- [[project]] — 本页 `stage: project` 的归属阶段页：**STPM 干的事属于测试程序管理这一段**
- [[device-directory]] — **（推断）它的产物落点**；依据是它围绕 test program 工作，
  而 device directory 是 93K 测试程序的容器。**原文在本页一个字没说**
- [[testflow-file]] — **（推断）被它改写的对象之一**；**本页无依据**，只作为同族文件对照
- `Introduction and installation` / `Using SmarTest Program Manager` /
  `Test program template files` / `STPM command line options` / `STPM UI plug-in`（**均未建**）—
  **本页 7 条子主题里剩下的 5 条**；**本页的正文除了名字，对它们一无所知**
- [[setup-management-tool]] / [[test-program-explorer]] / [[testflow-tool]] —
  同属 `02.08` / `02.09` 一带的工具页；**本页不主张它们和 STPM 有任何具体关系**

## 版本

**本文档没有 `## Functional changes` 段。**

**这不是缺陷，是这份文档的性质**——它是一张 16 行的目录页，
**连正文都没有，自然也没有版本记录。**

**后果要说清楚**：
- **本页没有任何版本条目**——不知道 STPM 是哪个 SmarTest 版本引入的，也不知道它改过什么。
- **本页也无法给出「本页面向 SmarTest 7.10.3」之外的信息**（那是全库的基准版本，见 schema §11）。
- **要版本只能去子主题里找**：`Introduction and installation` 是名字上最可能带版本条目的一条，
  **本页没读它**。

## 出处

`sources:` 一篇：

`02_System_reference/02.09_Test_Program_Management/02.09.02_SmarTest_Program_Manager.md`
（TDC `132829.htm`）

**这一篇只有 16 行、约 400 字节**，全部内容是一段 `#### Subtopics` 清单（7 条）。
**没有正文、没有 `## Syntax`、没有 `## Procedure`、没有 `## Before you begin`、
没有 `## What to do next`、没有 `## Related information`、没有 `## Functional changes`、一张图都没有。**

**本页没做的**：

- **7 条子主题一篇都没读**，**它们的下级（约几十篇）一篇都没读**。
  **这是本页最重的声明**：本页「语法 / 参数」节有 134,986 字符，
  **全部来自那些未读的子主题**——
  **它们逐字在本页上（脚本抽的），但本页对它们的正文一无所知。**
  **本页的正文因此只写到「这个工具有哪 7 块」为止。**
- **本页没有引任何英文原句逐字**——**因为定义文档里没有可供引用的散文**。
  唯一逐字引的是本页「语法 / 参数」节脚本自己写的那三行警告（它是页面构件，不是 raw 语料）。
- **没有实测**：本页没有装过、没有跑过 SmarTest Program Manager，
  **连它长什么界面都不知道**。
- **`layer: gui` 这个归属本页无法用原文佐证**——
  定义文档没有一句话说它有图形界面；**唯一的线索是第 7 条子主题叫 `STPM UI plug-in`**。

> ⚠️ **本页没有可报告的语料瑕疵**（错别字、自相矛盾、链接指错）。
> **原因不是语料干净，是这份文档太短**——16 行里除了 7 个标题就没有可出错的句子。
> **本页能报告的只有「它没有内容」这件事本身，而那已经写在上面了。**
>
> **补一条形状上的观察（不是瑕疵）**：同一组概念在原文里**缩写与全称混用**——
> `STPM`（第 3、4、6、7 条）与 `SmarTest Program Manager`（第 2 条）并存，
> **而 `#` 标题用的是全称**。**原文没有定义过 `STPM` 这个缩写。**

`verified: doc-only`
