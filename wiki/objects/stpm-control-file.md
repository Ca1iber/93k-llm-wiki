---
type: object
title: STPM control file
layer: file
stage: project
tags: [stpm, control-file, script, test-program-management, mtp, stp, tpt]
related: [stpm, stpm-merge-rules-file, preprocessing-and-postprocessing-scripts, testflow-file, test-suite, pattern-master-file]
sources:
  - 02_System_reference/02.09_Test_Program_Management/02.09.02.03_STPM_control_file.md
created: 2026-09-18
updated: 2026-09-20
verified: doc-only
---

# STPM control file

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **94,437 字符逐字取自** `<02_System_reference/02.09_Test_Program_Management/02.09.02.03_STPM_control_file.md>` 及其子主题 `<02_System_reference/02.09_Test_Program_Management/02.09.02.03.01_Structure_of_an_STPM_control_file.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.02_File_and_parameter_settings.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.04_write_tp.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.05_add_test.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.06_add_burst.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.07_add_test_to_burst.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.08_add_empty_test_group.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.09_remove_test.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.10_replace_test.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.11_remove_label.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.12_add_pattern.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.13_replace_pattern.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.14_tpt_generate_template.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.15_tpt_import_from_device.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.16_tpt_generate_device_dir.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.17_tpt_merge.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.18_tpt_add_test.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.19_tpt_replace_test.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.20_tpt_generate_tp.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.21_tpt_compare_tp.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.22_tpt_generate_test_stages.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.23_extract_subflow.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.24_merge_subflow.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.25_remove_subflow.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.26_clear_duplicated.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.27_clear_unused.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Structure of an STPM control file）

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

### Syntax（取自子主题 File and parameter settings）

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

### Parameters（取自子主题 File and parameter settings）

The parameters of the commands in the order in which they are listed above:

 |

mtp_device_testflow

 |

<testflow_file> (string) is the name and path of the testflow file of the MTP which STPM is to modify or otherwise work with.

It can be an absolute or a relative path. If it is a relative path, the base directory is the current working directory at the time STPM was called.

 |
 |

mtp_template_dir

 |

<tpt_dir> (string) is the name and path of the directory containing the test program template (TPT).

It can be an absolute or a relative path. If it is a relative path, the base directory is the current working directory at the time STPM was called.

This is an optional parameter. Note, however, that some commands require a valid TPT to be specified. This is noted in these commands' descriptions.

 |
 |

merge_rules

 |

<rules_file> (string) is the name and path of the merge rules file to use when adding or replacing tests.

It can be an absolute or a relative path. If it is a relative path, the base directory is the current working directory at the time STPM was called.

This is an optional parameter. If it is not specified, no merge rules file is used.

 |
 |

ate_target

 |

<platform> (string) indicates the type of V93000 architecture on which the test program will run:

- '93000SS': Smart Scale system
 |
 |

ate_model

 |

<model> (string) indicates the specific test system on which the test program will run.

The available settings depend on the specified ate_target.

For '93000SS', you can specify:

- 'PS1600'

This is an optional parameter. If it is omitted, the default used depends on the setting for ate_target:

 |
 |

ate_version

 |

<version> (string) is the release number of the SmarTest version under which the test program will be running.

This is an optional parameter. If it is omitted, "7.1.4" is used.

 |
 |

temp_dir

 |

<temp_dir> is the directory to which STPM writes temporary files.

It can be an absolute or a relative path. If it is a relative path, the base directory is the current working directory at the time STPM was called.

Make sure that the directory already exists and that STPM has write privileges in the specified directory.

This is an optional parameter. If it is omitted, /tmp is used (the tmp subdirectory of the root directory).

 |
 |

enable_backup

 |

<backup?> (number) specifies whether STPM generates a backup copy of each modified file:

- 0: No backups are generated.
- 1: Backups are generated.

When backup files are generated, they are stored in a subdirectory of the directory in which the original file is located; the subdirectory is named back.

The name of the backup file is the same as the original file name, with a timestamp in the form "_YYMMDD_HHMMSS" appended.

For example, the backup copy of a pin configuration file mypins.cfg that is created on 2 November 2012 at 21:43:23 is stored as <device_directory>/configuration/back/mypins_121102_214323.cfg.

This is an optional parameter. If it is omitted, 1 is used (that is, backups are generated).

 |

### Example（取自子主题 File and parameter settings）

See the sample control file in `Structure of an STPM control file`（raw: `02.09.02.03.01_Structure_of_an_STPM_control_file.md`）.

### Syntax（取自子主题 Preprocessing and postprocessing scripts）

Both the pre_proc (shown below) and post_proc parameters have the same syntax.

```
pre_proc = '<script>[&mdir][&sdir][&mtp_tf][&mtp_pmf][&mtp_conf][&mtp_tim][&mtp_lev][&mtp_tt][&mtp_rout][&mtp_wf][&mtp_anctrl][&mtp_chatt][&mtp_prot][&mtp_att][&stp_tf][&stp_pmf][&stp_conf][&stp_tim][&stp_lev][&stp_tt][&stp_rout][&stp_wf][&stp_anctrl][&stp_chatt][&stp_prot][&stp_att][<user_parameters>]'
```

The available script parameters in the order in which they are listed above:

 |

<script>

 |

The name and path of the script file to call.

The path can be absolute or relative. If it is a relative path, the base directory is the current working directory at the time STPM was called.

 |
 |

&mdir

 |

Full path to the MTP directory.

 |
 |

&sdir

 |

Full path to the STP directory.

 |
 |

&mtp_tf

 |

Full path to the MTP testflow file.

 |
 |

&mtp_pmf

 |

Full path to the MTP pattern master file.

 |
 |

&mtp_conf

 |

Full path to the MTP configuration file.

 |
 |

&mtp_tim

 |

Full path to the MTP timing file.

 |
 |

&mtp_lev

 |

Full path to the MTP levels file.

 |
 |

&mtp_tt

 |

Full path to the MTP test table file.

 |
 |

&mtp_rout

 |

Full path to the MTP routing file.

 |
 |

&mtp_wf

 |

Full path to the MTP waveform file.

 |
 |

&mtp_anctrl

 |

Full path to the MTP analog control file.

 |
 |

&mtp_chatt

 |

Full path to the MTP channel attributes file.

 |
 |

&mtp_prot

 |

Full path to the MTP protocols file.

 |
 |

&mtp_att

 |

Full path to the MTP pin attributes file.

 |
 |

&stp_tf

 |

Full path to the STP testflow file.

 |
 |

&stp_pmf

 |

Full path to the STP pattern master file.

 |
 |

&stp_conf

 |

Full path to the STP configuration file.

 |
 |

&stp_tim

 |

Full path to the STP timing file.

 |
 |

&stp_lev

 |

Full path to the STP levels file.

 |
 |

&stp_tt

 |

Full path to the STP test table file.

 |
 |

&stp_rout

 |

Full path to the STP routing file.

 |
 |

&stp_wf

 |

Full path to the STP waveform file.

 |
 |

&stp_anctrl

 |

Full path to the STP analog control file.

 |
 |

&stp_chatt

 |

Full path to the STP channel attributes file.

 |
 |

&stp_prot

 |

Full path to the STP protocols file.

 |
 |

&stp_att

 |

Full path to the STP pin attributes file.

 |
 |

<user_parameters>

 |

Text that is passed unchanged to the script. This text must not contain any words that begin with &.

 |

Except for the name of the script file, all elements are optional.

### Example（取自子主题 Preprocessing and postprocessing scripts）

This example executes the write_tp command with two scripts:

- Before write_tp itself is executed, the preparation.py script from the current working directory is run. No parameters are passed to this script.
- After write_tp has finished executing, the cleanup.pl script is run. This script receives this parameter string (assuming that the MTP is located in /user/johndoe/mtp):

`--mdir '/user/johndoe/mtp' --cmd write --stage 3`

```
write_tp('user/johndoe/mtp/flow1.tf',
         pre_proc  = 'preparation.py',
         post_proc = '/usr/tools/scripts/cleanup.pl &mdir --cmd write --stage 3')
```

### Syntax（取自子主题 write tp）

```
write_tp(
    path = '<mtp_target_file>',
[pre_proc = <pre_proc>, ]
[post_proc = <post_proc>]
)
```

### Parameters（取自子主题 write tp）

The parameters in the order in which they are listed above:

 |

path

 |

<mtp_target_file> (string) is the name and location under which STPM saves the MTP (master test program) testflow file after it has modified it.

It can be an absolute or a relative path. If it is a relative path, the base directory is the current working directory at the time STPM was called.

You can specify the same file here as for mtp_device_testflow. In that case, the original file is modified in place.

(You can still have STPM automatically create a backup of the MTP; see `enable_backup`（raw: `02.09.02.03.02_File_and_parameter_settings.md`） for details.)

 |
 |

pre_proc

 |

<pre_proc> is a script that is executed before this command.

The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.

This is an optional parameter.

 |
 |

post_proc

 |

<post_proc> is a script that is executed after this command.

The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.

This is an optional parameter.

 |

```

```

### Example（取自子主题 write tp）

See the sample control file in `Structure of an STPM control file`（raw: `02.09.02.03.01_Structure_of_an_STPM_control_file.md`）.

### Syntax（取自子主题 add test）

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

### Parameters（取自子主题 add test）

The parameters in the order in which they are listed above:

 |

test_flow_file

 |

<testflow_file> (string) is the path, including the name, of the testflow file of the source test program (STP) that contains the test that you want to add to the MTP.

The path can be either absolute or relative to the current working directory.

 |
 |

test_source

 |

<test_source> (string) is the name of the test from the STP that will be added to the MTP.

If the STP contains only a single test, the test_source parameter can be omitted. If the STP contains multiple tests, test_source is required.

 |
 |

test_group

 |

<test_group> (string) is the testflow group in which the test suite is generated.

If this parameter is not specified, the test suite is generated at the root of the MTP, at the end of the testflow.

 |
 |

test

 |

<test> is the name for the added test in the MTP.

If this parameter is omitted, the name is added to the MTP with the same name that it has in the STP.

If there is already a test with the same name in the MTP, the test from the STP is not added and an error is generated. (This applies in both cases, whether you have specified a name using the test parameter or whether the default name is used.)

 |
 |

position

 |

<position> (string) is the position within a test group where the new test is inserted.

The following values are available:

- optimal: STPM inserts the test in a position in the testflow group that requires the least amount of level and timing reloads during execution.
- first: The test suite is inserted as the first test in the testflow group.
- last: The test suite is inserted as the last in the testflow group.
- after:<test_name>: The test suite is inserted immediately after the test suite with the name <test_name> in the testflow group.
- before:<test_name>: The test suite is inserted immediately before the test suite with the name <test_name> in the testflow group.

If this parameter is omitted, optimal is used.

If the test_group parameter (see above) is omitted, the position parameter is ignored.

 |
 |

tim_reuse

 |

<timing_reuse> (string) is the way in which timing settings in the MTP are to be reused for the added test:

- auto: STPM tries to reuse an existing timing, merging the timing from the new test with it. If this is not possible, a new timing is created.
- test:<test-name>: The timing from the existing test suite with the name <test-name> is used for the added test.
- <primary-keys>: You can explicitly specify the timing to use. How to do this differs for single-port and multiport tests:

  - Single-port timing: Specify the timing as a combination of indexes, separated by periods: <eqnset-index>`.`<timset-index>`.`<specset-index>
  - Multiport timing: Specify the name of the multiport specification to use.

- none: STPM will not try to reuse any timing. Instead, it always creates new timing for the added test.

If this parameter is omitted, none is used.

 |
 |

lev_reuse

 |

<level_reuse> (string) is the way in which level settings in the MTP are to be reused for the added test:

- auto: STPM tries to reuse existing levels, merging the levels from the new test with hem. If this is not possible, new levels are created.
- test:<test-name>: The levels from the existing test suite with the name <test-name> are used for the added test.
- <primary-keys>: You can explicitly specify the levels to use as a combination of indexes, separated by periods:

<eqnset-index>`.`<levelset-index>`.`<specset-index>

- none: STPM will not try to reuse any levels. Instead, it always creates new levels for the added test.

If this parameter is omitted, none is used.

 |
 |

pat_reuse

 |

<pattern_reuse> (string) is the way in which patterns in the MTP are to be reused for the added test:

- test:<test-name>: The patterns from the existing test suite with the name <test-name> are used for the added test.
- <pattern-label>: You can explicitly specify the patterns to use by providing the name of the pattern label.
- none: STPM will not try to reuse any patterns. Instead, it always creates new patterns for the added test.

If this parameter is omitted, none is used.

 |
 |

reuse_scope

 |

<scope> (string or list of strings) are the testflow groups that STPM is to analyze for purposes of merging or reusing primaries. STPM will ignore primaries from other testflow groups.

The scope can be:

- `"*all*"` to tell STPM to consider all groups
- A comma-separated list of testflow groups, enclosed in square brackets

If this parameter is not specified, the default is for STPM to consider the test suites in the testflow group specified in the test_group parameter (see above).

If test_group is not specified either, all groups are considered.

 |
 |

pat_dir

 |

<path> (string) is the path of the directory where STPM is to store patterns that it copies from the STP to the device directory.

The path is relative to the vectors subdirectory of the device directory.

If this parameter is omitted, patterns is used. (That is, the patterns are copied to the vectors/patterns/ subdirectory of the device directory.)

 |
 |

test_flags

 |

<test_flags> (list of strings) is a list of test suite flags that are enabled for the imported test. The list must be enclosed in square brackets.

Include in the list each test suite flag you want to be enabled for the test in the MTP, enclosed in quotes and separated by commas.

You can specify all flags supported in SmarTest. Use these spellings:

- bypass
- fail_per_label
- ffc_enable
- ffc_scan_enable
- ffv_enable
- frg_enable
- frg_single_shot
- hold
- hold_on_fail
- mx_waves_enable
- output_on_fail
- output_on_pass
- per_pin_on_fail
- per_pin_on_pass
- set_pass
- set_fail
- value_on_fail
- value_on_pass

For example: `test_flags = ['hold_on_fail','per_pin_on_fail']`

If this parameter is omitted, no flags are enabled for the test.

 |
 |

test_method

 |

<method> (string) is the class of the test method of the test being added (for example, "ac_tml.AcTest.FunctionalTest").

If this parameter is omitted, the test is added to the MTP with the same type that it has in the STP.

 |
 |

test_params

 |

<params> (list of name/value pairs) is a list of parameter values with which to call the test method.

This is a list of name/value pairs that are separated by commas; the entire list is wrapped in curly braces: {<name>':'<value>',...}

Each name and value is a string, both are separated by a colon:

- <name> is the name of a parameter that is known to the test method.
- <value> is the value that is passed into this parameter when the test method is called.

For example: `test_params = {'param1':'0','my_param':'CLK'}`

This is an optional parameter. If it is omitted, no parameters are passed to the test method.

 |
 |

sbin_num

 |

<sbin_num> (string) is the software bin ID of the bin associated with the added test.

To be compatible with the SmarTest Data Formatter, the number must be between 0 and 32767.

This is an optional parameter; if hbin_num (see below) is specified, it is required. If it is omitted, a "Run" node without any associated bin is inserted in the test flow.

 |
 |

sbin_label

 |

<description> (string) is a short text describing the purpose of the software bin. It is intended for human readers.

This is an optional parameter. If it is omitted, the bin remains unlabeled.

 |
 |

hbin_num

 |

<hbin_num> (number) is the ID of the hardware bin connected to the software bin you are defining.

This is an optional parameter. If sbin_num (see above) is not specified, the hbin_num parameter cannot be specified.

 |
 |

hbin_label

 |

<hbin_label> (string) is a short text describing the purpose of the hardware bin. It is intended for human readers.

This is an optional parameter. If it is omitted, the bin remains unlabeled.

 |
 |

pre_proc

 |

<pre_proc> is a script that is executed before this command.

The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.

This is an optional parameter.

 |
 |

post_proc

 |

<post_proc> is a script that is executed after this command.

The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.

This is an optional parameter.

 |

### Example（取自子主题 add test）

See the sample control file in `Structure of an STPM control file`（raw: `02.09.02.03.01_Structure_of_an_STPM_control_file.md`）.

### Syntax（取自子主题 add burst）

```
add_burst(
name       = '<burst_name>',
[ports      = ('<port>', ... ),]
[pre_proc   = <pre_proc>,          ]
[post_proc  = <post_proc>]
)
```

### Parameters（取自子主题 add burst）

The parameters in the order in which they are listed above:

 |

name

 |

<testflow_file> (string) is the path, including the name, of the testflow file of the source test program (STP) that contains the test that you want to add to the MTP.

The path can be either absolute or relative to the current working directory.

 |
 |

ports

 |

<ports> (list of strings) is a list of the ports for which the burst will be generated.

You can list any number of ports. Each port must be an individual string, the strings must be separated by commas, and the list must be enclosed in parentheses.

This parameter is optional. If it is not specified, STPM creates a single-port burst.

 |
 |

pre_proc

 |

<pre_proc> is a script that is executed before this command.

The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.

This is an optional parameter.

 |
 |

post_proc

 |

<post_proc> is a script that is executed after this command.

The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.

This is an optional parameter.

 |

### Syntax（取自子主题 add test to burst）

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

### Parameters（取自子主题 add test to burst）

The parameters in the order in which they are listed above:

 |

test_flow_file

 |

<testflow_file> (string) is the path (including the name) of the testflow file of the source test program (STP) that contains the test that you want to add to the test in the MTP.

The path can be either absolute or relative to the current working directory.

 |
 |

test_source

 |

<test_source> (string) is the name of the test from the STP that will be added to the MTP.

If the STP contains only a single test, the test_source parameter can be omitted. If the STP contains multiple tests, test_source is required.

 |
 |

test

 |

<test> (string) is the name of the existing test in the MTP. The test from the STP is added to this test.

 |
 |

position

 |

<position> (string) is the position within the existing pattern burst where the new test is inserted.

The following values are available:

- first: STPM inserts the pattern from the STP at the beginning of the test (burst) in the MTP.
- last: The pattern from the STP is inserted at the end of the test (burst) in the MTP.
- after:<label_name>: The pattern from the STP is inserted immediately after the label with the name <label_name> in the test in the MTP.
- before:<label_name>: The pattern from the STP is inserted immediately before the label with the name <label_name> in the test in the MTP.

If this parameter is omitted, last is used.

 |
 |

pat_dir

 |

<path> (string) is the path of the directory where STPM is to store patterns that it copies from the STP to the device directory.

The path is relative to the vectors subdirectory of the device directory.

If this parameter is omitted, patterns is used. (That is, the patterns are copied to the vectors/patterns/ subdirectory of the device directory.)

 |
 |

pat_reuse

 |

<mode> (string) is the way in which patterns in the MTP are to be reused for the test that is added to the burst:

- test:<test-name>: The patterns from the existing test suite with the name <test-name> are used for the added test.
- <pattern-label>: You can explicitly specify the patterns to use by providing the name of the pattern label.
- none: STPM will not try to reuse any patterns. Instead, it always creates new patterns for the added test.

If this parameter is omitted, none is used.

 |
 |

pre_proc

 |

<pre_proc> is a script that is executed before this command.

The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.

This is an optional parameter.

 |
 |

post_proc

 |

<post_proc> is a script that is executed after this command.

The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.

This is an optional parameter.

 |

### Example（取自子主题 add test to burst）

See the sample control file in `Structure of an STPM control file`（raw: `02.09.02.03.01_Structure_of_an_STPM_control_file.md`）.

### Syntax（取自子主题 add empty test group）

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

### Parameters（取自子主题 add empty test group）

The parameters in the order in which they are listed above:

 |

test_group

 |

<test_group> (string) is the name of the new test group you want to create in the MTP.

 |
 |

description

 |

<description> is a brief statement about the purpose of the new test group.

This parameter is intended just for humans; omitting it does not in any way affect the function of the test group.

This is an optional parameter. If it is omitted, no description is stored with the test group.

 |
 |

parent

 |

<parent> (string) is the name of the test group in which the new test group will be created.

The test group you name as the parent must already exist in the MTP.

This is an optional parameter. If it is not specified, the test group is created at the top level of the MTP.

 |
 |

position

 |

<position> (string) is the position within the parent where the new test group is created.

The following values are available:

- first: The test group is created at the beginning of the parent.
- last: The test group is created at the end of the parent.

If this parameter is omitted, last is used.

 |
 |

pre_proc

 |

<pre_proc> is a script that is executed before this command.

The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.

This is an optional parameter.

 |
 |

post_proc

 |

<post_proc> is a script that is executed after this command.

The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.

This is an optional parameter.

 |

### Syntax（取自子主题 remove test）

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

### Parameters（取自子主题 remove test）

The parameters in the order in which they are listed above:

 |

test

 |

<test> (string) is the name of the test suite in the MTP that STPM should remove.

 |
 |

tim_remove

 |

<timing_remove> is an instruction for STPM on how to remove the timing settings of the removed test:

- unused: STPM removes the settings if no other test uses them. (STPM may not be able to detect usage by tests that switch primaries in the C++ code.)
- none: The timing settings are not removed, even if no other test uses them.

If this parameter is omitted, unused is used.

 |
 |

lev_remove

 |

<level_remove> (string) is an instruction for STPM on how to remove the levels of the removed test:

- unused: STPM removes the levels if no other test uses them. (STPM may not be able to detect usage by tests that switch primaries in the C++ code.)
- none: The levels are not removed, even if no other test uses them.

If this parameter is omitted, unused is used.

 |
 |

pat_remove

 |

<pattern_remove> (string) is an instruction for STPM on how to remove the patterns of the removed test:

- unused: STPM removes the patterns if no other test uses them. (STPM may not be able to detect usage by tests that switch primaries in the C++ code.)
- none: The patterns are not removed, even if no other test uses them.

If this parameter is omitted, unused is used.

 |
 |

test_remove

 |

<test_remove> (number) specifies whether the test suite is removed from the MTP:

- 0: The test suite is not removed.
- 1: The test suite is removed.

You can still remove timing, level, or patterns as described above. Indexes in the test suite that point to removed primaries are reset.

This parameter is optional. If it is not specified, the test suite is removed (as if you had specified `test_remove = 1`.)

 |
 |

keep_pat_label

 |

<keep_label> (number) specifies whether the test suite labels in the MTP are kept when the test is removed:

- 0: The pattern labels are removed from the MTP.
- 1: The pattern labels are kept in the MTP.

This parameter is optional. If it is not specified, the labels are removed (as if you had specified `keep_pat_label = 0`.)

This parameter is ignored if `test_remove = 0` is specified

 |
 |

pre_proc

 |

<pre_proc> is a script that is executed before this command.

The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.

This is an optional parameter.

 |
 |

post_proc

 |

<post_proc> is a script that is executed after this command.

The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.

This is an optional parameter.

 |

### Syntax（取自子主题 replace test）

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

### Parameters（取自子主题 replace test）

The parameters in the order in which they are listed above:

 |

test_flow_file

 |

<testflow_file> (string) is the path (including the name) of the testflow file of the source test program (STP) that contains the test with which you want to replace an existing test in the MTP.

The path can be either absolute or relative to the current working directory.

 |
 |

test_source

 |

<test_source> (string) is the name of the test from the STP that will be used to replace the existing test in the to the MTP.

If the MTP already contains a test by that name and the primaries are already set for that test, an error is generated and the test is not added to the MTP.

If the STP contains only a single test, the test_source parameter can be omitted. If the STP contains multiple tests, test_source is required.

 |
 |

test

 |

<test> (string) is the name of the test in the MTP that is to be replaced.

 |
 |

tim_reuse

 |

<timing_reuse> (string) is the way in which timing settings in the MTP are to be reused for the replacement test:

- auto: STPM tries to reuse an existing timing, merging the timing from the replacement test with it. If this is not possible, a new timing is created.
- test:<test-name>: The timing from the existing test suite with the name <test-name> is used for the replacement test.
- <primary-keys>: You can explicitly specify the timing to use. How to do this differs for single-port and multiport tests:

  - Single-port timing: Specify the timing as a combination of indexes, separated by periods: <eqnset-index>`.`<timset-index>`.`<specset-index>
  - Multiport timing: Specify the name of the multiport timing set to use.

- none: STPM will not try to reuse any timing. Instead, it always creates new timing for the replacement test.

If this parameter is omitted, none is used.

 |
 |

lev_reuse

 |

<level_reuse> (string) is the way in which level settings in the MTP are to be reused for the replacement test:

- auto: STPM tries to reuse existing levels, merging the levels from the replacement test with them. If this is not possible, new levels are created.
- test:<test-name>: The levels from the existing test suite with the name <test-name> are used for the replacement test.
- <primary-keys>: You can explicitly specify the levels to use as a combination of indexes, separated by periods:

<eqnset-index>`.`<levelset-index>`.`<specset-index>

- none: STPM will not try to reuse any levels. Instead, it always creates new levels for the replacement test.

If this parameter is omitted, none is used.

 |
 |

pat_reuse

 |

<pattern_reuse> (string) is the way in which patterns in the MTP are to be reused for the replacement test:

- test:<test-name>: The patterns from the existing test suite with the name <test-name> are used for the replacement test.
- <pattern-label>: You can explicitly specify the patterns to use by providing the name of the pattern label.
- none: STPM will not try to reuse any patterns. Instead, it always creates new patterns for the replacement test.

If this parameter is omitted, none is used.

 |
 |

reuse_scope

 |

<scope> (string or list of strings) are the testflow groups that STPM is to analyze for purposes of merging or reusing primaries. STPM will ignore primaries from other testflow groups.

The scope can be:

- `"*all*"` to tell STPM to consider all groups
- A comma-separated list of testflow groups

If this parameter is not specified, the test suites in the testflow group containing the replaced test are considered.

 |
 |

copy_test_method

 |

<copy_tm_att> (0 or 1) specifies whether the attributes for the test method of the replaced test are copied from the STP or whether the attributes in the MTP are used:

- 0 (default): The attributes from the MTP are kept.
- 1: The attributes from the STP are copied to the MTP.

If this parameter is not specified, the attributes from the MTP are kept.

 |
 |

tim_remove

 |

<timing_remove> (string) is an instruction for STPM on how to remove the timing settings of the replaced test:

- unused: STPM removes the settings if no other test uses them. (STPM may not be able to detect usage by tests that switch primaries in the C++ code.)
- none: The timing settings are not removed, even if no other test uses them.

If this parameter is omitted, unused is used.

 |
 |

lev_remove

 |

<level_remove> (string) is an instruction for STPM on how to remove the levels of the replaced test:

- unused: STPM removes the levels if no other test uses them. (STPM may not be able to detect usage by tests that switch primaries in the C++ code.)
- none: The levels are not removed, even if no other test uses them.

If this parameter is omitted, unused is used.

 |
 |

pat_remove

 |

<pattern_remove> (string) is an instruction for STPM on how to remove the patterns of the replaced test:

- unused: STPM removes the patterns if no other test uses them. (STPM may not be able to detect usage by tests that switch primaries in the C++ code.)
- none: The patterns are not removed, even if no other test uses them.
- If this parameter is omitted, unused is used.
 |
 |

pat_dir

 |

<path> (string) is the path of the directory where STPM is to store patterns that it copies from the STP to the device directory.

The path is relative to the vectors subdirectory of the device directory.

If this parameter is omitted, patterns is used. (That is, the patterns are copied to the vectors/patterns/ subdirectory of the device directory.)

 |
 |

pre_proc

 |

<pre_proc> is a script that is executed before this command.

The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.

This is an optional parameter.

 |
 |

post_proc

 |

<post_proc> is a script that is executed after this command.

The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.

This is an optional parameter.

 |

### Example（取自子主题 replace test）

See the sample control file in `Structure of an STPM control file`（raw: `02.09.02.03.01_Structure_of_an_STPM_control_file.md`）.

### Syntax（取自子主题 remove label）

```
remove_label(
    label = '<label_name>',
[pmf_only = <pmf_flag>, ]
[pre_proc = <pre_proc>, ]
[post_proc = <post_proc>]
)
```

### Parameters（取自子主题 remove label）

The parameters in the order in which they are listed above:

 |

label

 |

<label_name> (string) is the name of the label that you want to remove from the MTP.

 |
 |

pmf_only

 |

<pmf_flag> (0 or 1) specifies whether the pattern is deleted from the MTP or only its entry from the pattern master:

- 0 (default): The pattern is deleted from the MPT.
- 1: The pattern is kept in the MTP, but its entry is removed from the pattern master file

If this parameter is not specified, the pattern is deleted from the MTP.

 |
 |

pre_proc

 |

<pre_proc> is a script that is executed before this command.

The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.

This is an optional parameter.

 |
 |

post_proc

 |

<post_proc> is a script that is executed after this command.

The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.

This is an optional parameter.

 |

### Syntax（取自子主题 add pattern）

```
add_pattern(
test_flow_file = '<testflow_file>',
context        = '<source>',
[pat_dir        = '<path>',           ]
[pre_proc       = <pre_proc>,         ]
[post_proc      = <post_proc>]
)
```

### Parameters（取自子主题 add pattern）

The parameters in the order in which they are listed above:

 |

test_flow_file

 |

<testflow_file> (string) is the path (including the name) of the testflow file of the source test program (STP) that contains the pattern that you want to add to the MTP.

The path can be either absolute or relative to the current working directory.

 |
 |

context

 |

<source> (string) describes the location of the desired pattern in the STP. There are two ways to specify the location:

- By providing the label name. For example: "pattern1".
- By providing the names of the test and the test suite, divided by a colon. For example: "mytest:ts3".

STPM will interpret any string without a colon as a label name and any string with a colon as the names of a test and a test suite.

 |
 |

pat_dir

 |

<path> (string) is the path of the directory where STPM is to store patterns that it copies from the STP to the device directory.

The path is relative to the vectors subdirectory of the device directory.

If this parameter is omitted, patterns is used. (That is, the patterns are copied to the vectors/patterns/ subdirectory of the device directory.)

 |
 |

pre_proc

 |

<pre_proc> is a script that is executed before this command.

The syntax of the parameter value is described in Preprocessing and postprocessing scripts.

This is an optional parameter.

 |
 |

post_proc

 |

<post_proc> is a script that is executed after this command.

The syntax of the parameter value is described in Preprocessing and postprocessing scripts.

This is an optional parameter.

 |

### Example（取自子主题 add pattern）

This example adds the pattern from the test suite "func_ts_2" in the "func_test" test in the "tf1.tf" testflow to the /vectors/patterns directory of the MTP device directory.

```
add_pattern(test_flow_file='/user/johndoe/stp/tf1.tf', context='func_test:func_ts_2')
```

### Syntax（取自子主题 replace pattern）

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

### Parameters（取自子主题 replace pattern）

The parameters in the order in which they are listed above:

 |

test_flow_file

 |

<testflow_file> (string) is the path (including the name) of the testflow file of the source test program (STP) that contains the pattern that you want to add to the MTP.

The path can be either absolute or relative to the current working directory.

 |
 |

context

 |

<source> (string) describes the location of the desired pattern in the STP. There are two ways to specify the location:

- By providing the label name. For example: "pattern1".
- By providing the names of the test and the test suite, divided by a colon. For example: "mytest:ts3".

STPM will interpret any string without a colon as a label name and any string with a colon as the names of a test and a test suite.

 |
 |

test

 |

<test_suite> (string) is the name of the MTP test suite in which you want to replace the pattern.

 |
 |

pat_dir

 |

<path> (string) is the path of the directory where STPM is to store patterns that it copies from the STP to the device directory.

The path is relative to the vectors subdirectory of the device directory.

If this parameter is omitted, patterns is used. (That is, the patterns are copied to the vectors/patterns/ subdirectory of the device directory.)

 |
 |

pat_remove

 |

<pat_remove> (string) specifies whether the old pattern from the MTP test suite is deleted from the MTP device directory:

- 'unused' (default): The pattern is deleted if no other test uses it.
- 'none': The pattern is not deleted.

If this parameter is not specified, the pattern is deleted if no other test uses it.

 |
 |

waveforms_compare_mode

 |

<compare_mode> (string) specifies whether the waveforms in the new pattern are compared to the waveforms in the old pattern:

- 'none' (default): The waveforms of the two patterns are not compared.
- 'error': The waveforms are compared and an error is generated if any differences are found.
- 'warning': The waveforms are compared and a warning is generated if any differences are found.

If this parameter is not specified, the waveforms are not compared.

 |
 |

pre_proc

 |

<pre_proc> is a script that is executed before this command.

The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.

This is an optional parameter.

 |
 |

post_proc

 |

<post_proc> is a script that is executed after this command.

The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.

This is an optional parameter.

 |

### Example（取自子主题 replace pattern）

This example adds the pattern from the test suite "func_ts_2" in the "func_test" test in the "tf1.tf" testflow to the /vectors/patterns directory of the MTP device directory.

```
add_pattern(test_flow_file='/user/johndoe/stp/tf1.tf', context='func_test:func_ts_2')
```

### Syntax（取自子主题 tpt generate template）

```
tpt_generate_template(
tpt_dir    = <location>,
[pre_proc   = <pre_proc>,    ]
[post_proc  = <post_proc>]
)
```

### Parameters（取自子主题 tpt generate template）

The parameters in the order in which they are listed above:

 |

tpt_dir

 |

<location> (string) is the path, including the name, where the new template files and directories are created.

The path can be either absolute or relative to the current working directory.

If the directory does not yet exist, STPM creates it.

 |
 |

pre_proc

 |

<pre_proc> is a script that is executed before this command.

The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.

This is an optional parameter.

 |
 |

post_proc

 |

<post_proc> is a script that is executed after this command.

The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.

This is an optional parameter.

 |

### Example（取自子主题 tpt generate template）

This example creates a test program template in the subdirectory "new_template" of the current working directory.

```
generate_new(
    tpt_dir  = 'new_template'
    )
```

### Syntax（取自子主题 tpt import from device）

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

### Parameters（取自子主题 tpt import from device）

|

device_test_flow

 |

<testflow_file> (string) is the path of the testflow file from which the test program template is to be generated.

The path can be either absolute or relative to the current working directory.

 |
 |

tpt_dir

 |

<location> (string) is the path, including the name, where the new template files and directories are created.

The path can be either absolute or relative to the current working directory.

If the directory does not yet exist, STPM creates it. If the directory already exists, it must either be empty or the allow_overwrite parameter (see below) must be set to 1.

 |
 |

include_groups

 |

<include_groups> (list of strings) is a list of groups in the specified testflow that are to be imported.

Each group name is a string enclosed in single or double quotes; groups are separated by commas, and the list is enclosed in square brackets.

You can use the ? and * wildcard characters in the group name strings. (See empty_groups, below, for details.)

This parameter is optional. If it is omitted, all groups are imported.

 |
 |

empty_groups

 |

<empty_groups> (list of strings) is a list of groups that are to be emptied.

An empty group is transferred to the test program template, but none of the test suites it contains are transferred. Empty groups are useful to preserve the structure of the testflow. They can be filled with new test suites later.

Each group name is a string enclosed in single or double quotes; groups are separated by commas, and the list is enclosed in square brackets.

You can use the ? and * wildcard characters in the group name strings; ? matches any single character and * matches zero or more characters.

For example, to empty all groups, you would specify `empty_groups = '*'`. To empty the group temp1 and all groups with the name "test" followed by a single character, you would specify `empty_groups = 'temp1', 'test?'`.

This parameter is optional. If it is omitted, no groups are emptied.

 |
 |

copy_static_content

 |

<copy_items> (list of strings) is a list of names of files or directories that are to be copied from the existing device directory to the TPT directory.

The list may contain only names (of files or directories), not paths. The named items must be located in the top level of the device directory. Each name is enclosed in quotes and separated by commas.

For example: `copy_static_content = ['my_notes.txt','Change log']`

If you include standard directories in this list (testflow, timing, levels, configuration, vectors, testtable), STPM generates a warning and does not copy the contents.

Any directories that are copied by means of this command will be included in the device directory generated with `tpt_generate_device_dir`（raw: `02.09.02.03.16_tpt_generate_device_dir.md`）.

This parameter is optional. If it is omitted, no additional content is copied.

 |
 |

allow_overwrite

 |

<overwrite_flag> specifies whether STPM may overwrite existing files in the test program template directory:

- 0 (default): No existing files or directories in the test program template directory may be overwritten. If this prevents STPM from saving a created file, it displays an error and stops the conversion.
- 1: STPM may overwrite existing files and directories.

This parameter is optional. If it is omitted, no files or directories are overwritten.

 |
 |

pre_proc

 |

<pre_proc> is a script that is executed before this command.

The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.

This is an optional parameter.

 |
 |

post_proc

 |

<post_proc> is a script that is executed after this command.

The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.

This is an optional parameter.

 |

### Example（取自子主题 tpt import from device）

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

### Syntax（取自子主题 tpt generate device dir）

```
tpt_generate_device_dir(
tpt_dir = <tpt_directory>,
    device_dir = <directory>,
[device_name = <device_name>, ]
[pre_proc = <pre_proc>, ]
post_proc = <post_proc>]
)
```

### Parameters（取自子主题 tpt generate device dir）

The parameters in the order in which they are listed above:

 |

tpt_dir

 |

<tpt_directory> (string) is the name and path of the directory containing the TPT files from which the device directory is to be generated.

The path can be either absolute or relative to the current working directory.

 |
 |

device_dir

 |

<directory> (string) is the path, including the name, where the new device directory is created. The directory must either not exist yet (in which case STPM creates it) or it must be empty.

The path can be either absolute or relative to the current working directory.

 |
 |

device_name

 |

<device_name> (string) is the name for the newly created device.

This parameter is optional. If it is omitted, "device" is used.

 |
 |

pre_proc

 |

<pre_proc> is a script that is executed before this command.

The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.

This is an optional parameter.

 |
 |

post_proc

 |

<post_proc> is a script that is executed after this command.

The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.

This is an optional parameter.

 |

### Example（取自子主题 tpt generate device dir）

This example creates a device directory for the device "my_device" from the TPT master file "my_tpt.tpt" (located in the current working directory). The device directory is located at the same level as the current working directory.

```
tpt_generate_device_dir(
    tpt_dir     = 'my_tpt/'
    device_dir  = '../my_device/'
    device_name = 'my_device',
    )
```

### Syntax（取自子主题 tpt merge）

```
tpt_merge(
source_tpts = [<tpt_list>],
   target_tpt = <directory>,
[pre_proc = <pre_proc>, ]
[post_proc = <post_proc>]
)
```

### Parameters（取自子主题 tpt merge）

The parameters in the order in which they are listed above:

 |

source_tpts

 |

<tpt_file> (list of strings) is a list of TPT directories that you want to merge into a single TPT.

Include in the list the path of each TPT you want to merge, enclosed in quotes and separated by commas.

Paths can be either absolute or relative to the current working directory.

In case of conflicts, objects from any source TPT overwrite those in the target TPT and objects from source TPTs at the end of the list overwrite those from TPTs at the beginning of the list.

 |
 |

target_tpt

 |

<directory> (string) is the path, including the name, where the merged device directory is created. The TPT must already exist.

The path can be either absolute or relative to the current working directory.

 |
 |

pre_proc

 |

<pre_proc> is a script that is executed before this command.

The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.

This is an optional parameter.

 |
 |

post_proc

 |

<post_proc> is a script that is executed after this command.

The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.

This is an optional parameter.

 |

### Example（取自子主题 tpt merge）

This example copies the contents from three test program templates into one new template..

```
tpt_merge(
    source_tpts = ['my_tpt','my_other_tpt','../reference/best_tpt')
    target_tpt  = '../merged_tpt/'
    )
```

### Syntax（取自子主题 tpt add test）

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

### Parameters（取自子主题 tpt add test）

The parameters in the order in which they are listed above:

 |

test_flow_file

 |

<testflow_file> (string) is the path, including the name, of the testflow file of the source test program (STP) that contains the test that you want to add to the MTP.

The path can be either absolute or relative to the current working directory.

 |
 |

test_source

 |

<test_source> (string) is the name of the test from the STP that will be added to the MTP. The test must be included in the `test suite table`（raw: `02.09.02.05.01_Test_suite_table_of_a_TPT.md`）.

If the STP contains only a single test, the test_source parameter can be omitted. If the STP contains multiple tests, test_source is required.

 |
 |

test

 |

<test> is the name for the added test in the MTP.

If this parameter is omitted, the name is added to the MTP with the name specified for it in the `test suite table`（raw: `02.09.02.05.01_Test_suite_table_of_a_TPT.md`）.

If there is already a test with the same name in the MTP, the test from the STP is not added and an error is generated. (This applies in both cases, whether you have specified a name using the test parameter or whether the default name is used.)

 |
 |

position

 |

<position> (string) is the position within a test group where the new test is inserted.

The following values are available:

- optimal: STPM inserts the test in a position in the testflow group that requires the least amount of level and timing reloads during execution.
- first: The test suite is inserted as the first test in the testflow group.
- last: The test suite is inserted as the last in the testflow group.
- after:<test_name>: The test suite is inserted immediately after the test suite with the name <test_name> in the testflow group.
- before:<test_name>: The test suite is inserted immediately before the test suite with the name <test_name> in the testflow group.

If this parameter is omitted, optimal is used.

 |
 |

tim_reuse

 |

<timing_reuse> (string) is the way in which timing settings in the MTP are to be reused for the added test:

- auto: STPM tries to reuse an existing timing, merging the timing from the new test with it. If this is not possible, a new timing is created.
- test:<test-name>: The timing from the existing test suite with the name <test-name> is used for the added test.
- <primary-keys>: You can explicitly specify the timing to use. How to do this differs for single-port and multiport tests:

  - Single-port timing: Specify the timing as a combination of indexes, separated by periods:

<eqnset-index>`.`<timset-index>`.`<specset-index>

  - Multiport timing: Specify the name of the multiport specification to use.

- none: STPM will not try to reuse any timing. Instead, it always creates new timing for the added test.

If this parameter is omitted, none is used.

 |
 |

lev_reuse

 |

<level_reuse> (string) is the way in which level settings in the MTP are to be reused for the added test:

- auto: STPM tries to reuse existing levels, merging the levels from the new test with hem. If this is not possible, new levels are created.
- test:<test-name>: The levels from the existing test suite with the name <test-name> are used for the added test.
- <primary-keys>: You can explicitly specify the levels to use as a combination of indexes, separated by periods:

<eqnset-index>`.`<levelset-index>`.`<specset-index>

- none: STPM will not try to reuse any levels. Instead, it always creates new levels for the added test.

If this parameter is omitted, none is used.

 |
 |

pat_reuse

 |

<pattern_reuse> (string) is the way in which patterns in the MTP are to be reused for the added test:

- test:<test-name>: The patterns from the existing test suite with the name <test-name> are used for the added test.
- <pattern-label>: You can explicitly specify the patterns to use by providing the name of the pattern label.
- none: STPM will not try to reuse any patterns. Instead, it always creates new patterns for the added test.

If this parameter is omitted, none is used.

 |
 |

reuse_scope

 |

<scope> (string or list of strings) are the testflow groups that STPM is to analyze for purposes of merging or reusing primaries. STPM will ignore primaries from other testflow groups.

The scope can be:

- `"*all*"` to tell STPM to consider all groups
- A comma-separated list of testflow groups, enclosed in square brackets

If this parameter is not specified, the default is for STPM to consider the test suites in the testflow group specified in the test_group parameter (see above).

If test_group is not specified either, all groups are considered.

 |
 |

pat_dir

 |

<path> (string) is the path of the directory where STPM is to store patterns that it copies from the STP to the device directory.

The path is relative to the vectors subdirectory of the device directory.

If this parameter is omitted, patterns is used. (That is, the patterns are copied to the vectors/patterns/ subdirectory of the device directory.)

 |
 |

pre_proc

 |

<pre_proc> is a script that is executed before this command.

The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.

This is an optional parameter.

 |
 |

post_proc

 |

<post_proc> is a script that is executed after this command.

The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.

This is an optional parameter.

 |

### Example（取自子主题 tpt add test）

See the sample control file in `Structure of an STPM control file`（raw: `02.09.02.03.01_Structure_of_an_STPM_control_file.md`）.

### Syntax（取自子主题 tpt replace test）

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

### Parameters（取自子主题 tpt replace test）

The parameters in the order in which they are listed above:

 |

test_flow_file

 |

<testflow_file> (string) is the path (including the name) of the testflow file of the source test program (STP) that contains the test with which you want to replace an existing test in the MTP.

The path can be either absolute or relative to the current working directory.

 |
 |

test_source

 |

<test_source> (string) is the name of the test from the STP that will be used to replace the existing test in the to the MTP. The test must be included in the `test suite table`（raw: `02.09.02.05.01_Test_suite_table_of_a_TPT.md`）.

If the MTP already contains a test by that name and the primaries are already set for that test, an error is generated and the test is not added to the MTP.

If the STP contains only a single test, the test_source parameter can be omitted. If the STP contains multiple tests, test_source is required.

 |
 |

test

 |

<test> (string) is the name of the test in the MTP that is to be replaced.

 |
 |

tim_reuse

 |

<timing_reuse> (string) is the way in which timing settings in the MTP are to be reused for the replacement test:

- auto: STPM tries to reuse an existing timing, merging the timing from the replacement test with it. If this is not possible, a new timing is created.
- test:<test-name>: The timing from the existing test suite with the name <test-name> is used for the replacement test.
- <primary-keys>: You can explicitly specify the timing to use. How to do this differs for single-port and multiport tests:

  - Single-port timing: Specify the timing as a combination of indexes, separated by periods:

<eqnset-index>`.`<timset-index>`.`<specset-index>

  - Multiport timing: Specify the name of the multiport timing set to use.

- none: STPM will not try to reuse any timing. Instead, it always creates new timing for the replacement test.

If this parameter is omitted, none is used.

 |
 |

lev_reuse

 |

<level_reuse> (string) is the way in which level settings in the MTP are to be reused for the replacement test:

- auto: STPM tries to reuse existing levels, merging the levels from the replacement test with them. If this is not possible, new levels are created.
- test:<test-name>: The levels from the existing test suite with the name <test-name> are used for the replacement test.
- <primary-keys>: You can explicitly specify the levels to use as a combination of indexes, separated by periods:

<eqnset-index>`.`<levelset-index>`.`<specset-index>

- none: STPM will not try to reuse any levels. Instead, it always creates new levels for the replacement test.

If this parameter is omitted, none is used.

 |
 |

pat_reuse

 |

<pattern_reuse> (string) is the way in which patterns in the MTP are to be reused for the replacement test:

- test:<test-name>: The patterns from the existing test suite with the name <test-name> are used for the replacement test.
- <pattern-label>: You can explicitly specify the patterns to use by providing the name of the pattern label.
- none: STPM will not try to reuse any patterns. Instead, it always creates new patterns for the replacement test.

If this parameter is omitted, none is used.

 |
 |

reuse_scope

 |

<scope> (string or list of strings) are the testflow groups that STPM is to analyze for purposes of merging or reusing primaries. STPM will ignore primaries from other testflow groups.

The scope can be:

- `"*all*"` to tell STPM to consider all groups
- A comma-separated list of testflow groups

If this parameter is not specified, the test suites in the testflow group containing the replaced test are considered.

 |
 |

tim_remove

 |

<timing_remove> (string) is an instruction for STPM on how to remove the timing settings of the replaced test:

- unused: STPM removes the settings if no other test uses them. (STPM may not be able to detect usage by tests that switch primaries in the C++ code.)
- none: The timing settings are not removed, even if no other test uses them.

If this parameter is omitted, unused is used.

 |
 |

lev_remove

 |

<level_remove> (string) is an instruction for STPM on how to remove the levels of the replaced test:

- unused: STPM removes the levels if no other test uses them. (STPM may not be able to detect usage by tests that switch primaries in the C++ code.)
- none: The levels are not removed, even if no other test uses them.

If this parameter is omitted, unused is used.

 |
 |

pat_remove

 |

<pattern_remove> (string) is an instruction for STPM on how to remove the patterns of the replaced test:

- unused: STPM removes the patterns if no other test uses them. (STPM may not be able to detect usage by tests that switch primaries in the C++ code.)
- none: The patterns are not removed, even if no other test uses them.
- If this parameter is omitted, unused is used.
 |
 |

pat_dir

 |

<path> (string) is the path of the directory where STPM is to store patterns that it copies from the STP to the device directory.

The path is relative to the vectors subdirectory of the device directory.

If this parameter is omitted, patterns is used. (That is, the patterns are copied to the vectors/patterns/ subdirectory of the device directory.)

 |
 |

pre_proc

 |

<pre_proc> is a script that is executed before this command.

The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.

This is an optional parameter.

 |
 |

post_proc

 |

<post_proc> is a script that is executed after this command.

The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.

This is an optional parameter.

 |

### Syntax（取自子主题 tpt generate tp）

```
tpt_generate_tp(
[generate_complete_device_directory = <complete_device_flag>,     ]
[error_on_non_existing_primaries    = <missing_primaries_flag>,   ]
[ignore_empty_groups                = <ignore_empty_groups_flag>, ]
[pre_proc                           = <pre_proc>,                 ]
[post_proc                          = <post_proc>]
)
```

### Parameters（取自子主题 tpt generate tp）

|

generate_complete_device_directory

 |

<complete_device_flag> specify whether a complete device directory or only a skeleton is generated:

- 0: The generated device directory contains only a testflow file. If the use of a test table is specified in the TPT, a test table is also generated.
- 1 (default): A complete device directory is generated.

If this parameter is omitted, 1 is used (a complete directory is generated).

 |
 |

error_on_non_existing_primaries

 |

<missing_primaries_flag> specifies whether warnings are generated for missing primaries:

- 0: STPM generates no warning if a test suite refers to primaries that do not exist in the TPT.
- 1 (default): STPM generates warnings when non-existent primaries are referenced.

If this parameter is omitted, 1 is used (warnings are generated).

 |
 |

ignore_empty_groups

 |

<ignore_empty_groups_flag> specifies what happens with empty groups in the testflow of the TPT:

- 0: Empty groups are copied to the testflow of the output test program.
- 1 (default): Empty groups are not copied to the testflow of the output test program.

If this parameter is omitted, 1 is used (empty groups are not copied).

 |
 |

pre_proc

 |

<pre_proc> is a script that is executed before this command.

The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.

This is an optional parameter.

 |
 |

post_proc

 |

<post_proc> is a script that is executed after this command.

The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.

This is an optional parameter.

 |

### Syntax（取自子主题 tpt compare tp）

```
tpt_compare_tp(
[report_file_path = '<report_file>',       ]
[include_groups   = <include_groups>,      ]
[pre_proc         = <pre_proc>,            ]
[post_proc        = <post_proc>]
)
```

### Parameters（取自子主题 tpt compare tp）

|

report_file_path

 |

<report_file> (string) is the path (including the name) where the command is to store the report file.

If this parameter is omitted, the file is named compare_log.html and is stored in the current working directory.

 |
 |

include_groups

 |

<include_groups> (list of strings) is a list of groups in the specified testflow that are to be compared.

Each group name is a string enclosed in single or double quotes; groups are separated by commas, and the list is enclosed in square brackets.

This parameter is optional. If it is omitted, the entire testflow is compared.

 |
 |

pre_proc

 |

<pre_proc> is a script that is executed before this command.

The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.

This is an optional parameter.

 |
 |

post_proc

 |

<post_proc> is a script that is executed after this command.

The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.

This is an optional parameter.

 |

### Syntax（取自子主题 tpt generate test stages）

```
tpt_generate_test_stages(
[include_undefined_objects = <flag>,      ]
[pre_proc                  = <pre_proc>,  ]
[post_proc                 = <post_proc>]
)
```

### Parameters（取自子主题 tpt generate test stages）

The parameters in the order in which they are listed above:

 |

include_undefined_objects

 |

<flag> (0 or 1) specifies how STPM treats undefined objects in the `test stage table`（raw: `02.09.02.05.06_Test_stage_table_of_a_TPT.md`）:

- 0: Undefined objects are not included in the data log profile.
- 1 (default): Undefined objects are treated as enabled.

An object is considered undefined for a test stage when the object's row contains neither Y nor N in the column for that test stage.

If this parameter is omitted, 1 is used. That is, undefined objects are considered to be enabled.

 |
 |

pre_proc

 |

<pre_proc> is a script that is executed before this command.

The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.

This is an optional parameter.

 |
 |

post_proc

 |

<post_proc> is a script that is executed after this command.

The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.

This is an optional parameter.

 |

### Syntax（取自子主题 extract subflow）

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

### Parameters（取自子主题 extract subflow）

The parameters in the order in which they are listed above:

 |

test_flow_file

 |

<file_path> (string) is the name and path of the testflow file for the STP you want to generate.

It can be an absolute or a relative path. If it is a relative path, the base directory is the current working directory at the time STPM was called.

If folders specified in the path do not yet exist, STPM creates them.

 |
 |

test_groups

 |

<group_list> (list of strings) is a list of test groups that are exported. The list must be enclosed in square brackets..

Include in the list each testflow group you want to export to the STP, enclosed in quotes and separated by commas.

For example: `test_groups = ['tg3','fail_tg']`

 |
 |

levels_mode

 |

<levels_mode> specifies the way in which level settings are extracted from the MTP:

- 'used' (default): Only level settings that are used by the extracted test groups are copied from the MTP to the STP.
- 'all': All level settings from the MTP are copied to the STP, even if none of the extracted test groups is using them.
- 'keep_file': No level settings are copied to the STP. Instead, the STP uses the level file of the MTP. This requires that the STP is located in the same directory as the MTP.

This parameter is optional. If it is omitted, only the level settings used in the subflow are copied.

 |
 |

timing_mode

 |

<timing_mode> specifies the way in which timing settings are extracted from the MTP:

- 'used' (default): Only timing settings that are used by the extracted test groups are copied from the MTP to the STP.
- 'all': All timing settings from the MTP are copied to the STP, even if none of the extracted test groups is using them.
- 'keep_file': No timing settings are copied to the STP. Instead, the STP uses the timing file of the MTP. This requires that the STP is located in the same directory as the MTP.

This parameter is optional. If it is omitted, only the timing settings used in the subflow are copied.

 |
 |

pattern_mode

 |

<pattern_mode> specifies the way in which patterns are extracted from the MTP:

- 'used' (default): Only patterns that are used by the extracted test groups are copied from the MTP to the STP.
- 'all': All patterns from the MTP are copied to the STP, even if none of the extracted test groups is using them.

This parameter is optional. If it is omitted, only the patterns used in the subflow are copied.

 |
 |

config_mode

 |

<config_mode> specifies the way in which configuration settings are extracted from the MTP:

- 'used': Only configuration settings that are used by the extracted test groups are copied from the MTP to the STP.
- 'all' (default): All configuration settings from the MTP are copied to the STP, even if none of the extracted test groups is using them.

This parameter is optional. If it is omitted, all config settings from the MTP are copied.

 |
 |

keep_tim_eqnsets

 |

<tim_eqnsets> is a list of timing equation sets that are extracted from the MTP even if they are not used by the extracted test groups.

The value is a list of equation set numbers separated by commas. For example: [1, 5, 9, 13]

This parameter is optional.

 |
 |

keep_lev_eqnsets

 |

<lev_eqnsets> is a list of level equation sets that are extracted from the MTP even if they are not used by the extracted test groups.

The value is a list of equation set numbers separated by commas. For example: [7,8]

This parameter is optional.

 |
 |

keep_wavetables

 |

<wavetables> is a list of wavetables that are extracted from the MTP even if they are not used by the extracted test groups.

The value is a list of wavetable names, enclosed in quotes and separated by commas. For example: ['mytable', 'wavetable2']

This parameter is optional.

 |
 |

keep_specifications

 |

<specifications> is a list of specifications that are extracted from the MTP even if they are not used by the extracted test groups.

The value is a list of specification names, enclosed in quotes and separated by commas. For example: ['spec5', 'spec5b']

This parameter is optional.

 |
 |

keep_pattern_files

 |

<pattern_files> is a list of level pattern files that are extracted from the MTP even if they are not used by the extracted test groups.

The value is a list of pattern file paths, enclosed in quotes and separated by commas. Paths can be absolute or relative to the directory of the MTP. For example: ['/home/johndoe/tps/init_pattern.bin l', 'device/vectors/pat3.binl'']

This parameter is optional.

 |
 |

keep_setup_file_names

 |

<keep_file_names_flag> specifies whether the names of setups are changed in the exported testflow:

- 0 (default): The names are changed to match the name of the extracted testflow.
- 1: The names remain the same as in the MTP.

This parameter is optional. If it is omitted, the names are changed.

 |
 |

copy_static_content

 |

<copy_items> (list of strings) specifies is a list of names of files or directories that are to be copied from the device directory of the MTP to the device directory of the extracted subflow.

The list may contain only names (of files or directories), not paths. The named items must be located in the top level of the device directory. Each name is enclosed in quotes and separated by commas.

These values are supported:

- A list of names of files or directories (but not paths). The named items must be located in the top level of the device directory. Each name is enclosed in quotes and separated by commas.

For example: `copy_static_content = ['my_notes.txt','Change log']`

If you include standard directories in this list (see below), STPM generates a warning and does not copy the contents.

- ['*all*'] (default): Every file and directory in the device directory is copied, except the standard directories testflow, timing, levels, configuration, vectors, and testtable.
- []: No additional files or directories are copied.

This parameter is optional. If it is omitted, all objects from the top level of the device directory are copied (as if ['*all*'] had been specified).

 |
 |

copy_patterns

 |

<copy_pattern_flag> specifies whether the patterns from the MTP are copied to the STP:

- 0: The patterns are not copied to the STP. The pattern master file of the STP refers to the patterns in the MTP.
- 1 (default): The patterns are copied to the STP. There are no references to the MTP patterns in the pattern master file of the STP.

This parameter is optional. If it is omitted, the patterns are copied.

 |
 |

allow_overwrite

 |

<overwrite_flag> specifies whether STPM may overwrite existing files in the STP directory:

- 0 (default): No existing files or directories in the device directory may be overwritten. If this prevents STPM from saving a created file, it displays an error and stops the conversion.
- 1: STPM may overwrite existing files and directories.

This parameter is optional. If it is omitted, no files or directories are overwritten.

 |
 |

pre_proc

 |

<pre_proc> is a script that is executed before this command.

The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.

This is an optional parameter.

 |
 |

post_proc

 |

<post_proc> is a script that is executed after this command.

The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.

This is an optional parameter.

 |

### Syntax（取自子主题 merge subflow）

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

### Parameters（取自子主题 merge subflow）

The parameters in the order in which they are listed above:

 |

test_flow_file

 |

<file_path> (string) is the name and path of the testflow file for the STP you want to merge into the MTP.

It can be an absolute or a relative path. If it is a relative path, the base directory is the current working directory at the time STPM was called.

 |
 |

include_groups

 |

<include_group_list> (list of strings) is a list of testflow groups that STPM is to import. If you use this parameter, only those groups specified in the list are imported.

The list must be enclosed in square brackets. Each testflow group in the list must be enclosed in quotes and separated by commas.

For example: `test_groups = ['tg3','fail_tg']`

This parameter is optional. It cannot be used when you also specify exclude_groups (see below).

 |
 |

exclude_groups

 |

<exclude_group_list> (list of strings) is a list of testflow groups that STPM is to exclude from the merge process. If you use this parameter, all groups from the STP are merged, except those groups specified in the list.

The list must be enclosed in square brackets. Each testflow group in the list must be enclosed in quotes and separated by commas.

For example: `test_groups = ['tg3','fail_tg']`

This parameter is optional. It cannot be used when you also specify include_groups (see above).

 |
 |

parent

 |

<parent_group> (string) is the name of the test group into which the tests from the subflow will be inserted.

The test group you name as the parent must already exist in the MTP.

This is an optional parameter. If it is not specified, the subflow in imported into the top level of the MTP.

 |
 |

position

 |

<position> (string) is the position within the parent where the imported tests are inserted.

The following values are available:

- first: The tests are inserted at the beginning of the parent.
- last: The tests are inserted at the end of the parent.
- after:<test_name>: The test suite is inserted immediately after the test suite with the name <test_name> in the testflow group.
- before:<test_name>: The test suite is inserted immediately before the test suite with the name <test_name> in the testflow group.

If this parameter is omitted, last is used.

 |
 |

tim_eqnset_index

 |

<tim_index> (string) specifies how the timing equation set indexes are imported from the STP to the MTP:

- 'keep': The indexes are transferred unchanged.
- 'keep+<number>': <number> is added to each index that is imported.

This is an optional parameter. If it is not specified, 'keep' is used.

 |
 |

lev_eqnset_index

 |

<lev_index> (string) specifies how the level equation set indexes are imported from the STP to the MTP:

- 'keep': The indexes are transferred unchanged.
- 'keep+<number>': <number> is added to each index that is imported.

This is an optional parameter. If it is not specified, 'keep' is used.

 |
 |

levels_mode

 |

<levels_mode> specifies the way in which level settings are merged into the MTP:

- 'used' (default): Only level settings that are used by the merged subflow are copied from the STP to the MTP.
- 'all': All level settings from the STP are copied to the MTP, even if none of the merged test groups is using them.

This parameter is optional. If it is omitted, only the level settings used in the subflow are copied.

 |
 |

timing_mode

 |

<timing_mode> specifies the way in which timing settings are merged into the MTP:

- 'used' (default): Only timing settings that are used by the merged subflow are copied from the STP to the MTP.
- 'all': All timing settings from the STP are copied to the MTP, even if none of the merged test groups is using them.

This parameter is optional. If it is omitted, only the timing settings used in the subflow are copied.

 |
 |

pattern_mode

 |

<pattern_mode> specifies the way in which timing settings are merged into the MTP:

- 'used' (default): Only patterns that are used by the merged subflow are copied from the STP to the MTP.
- 'all': All patterns from the STP are copied to the MTP, even if none of the merged test groups is using them.

This parameter is optional. If it is omitted, only the patterns used in the subflow are copied.

 |
 |

keep_tim_eqnsets

 |

<tim_eqnsets> is a list of timing equation sets from the STP that are merged into the MTP even if they are not used by the merged test groups.

The value is a list of equation set numbers separated by commas. For example: [1, 5, 9, 13]

This parameter is optional.

 |
 |

keep_lev_eqnsets

 |

<lev_eqnsets> is a list of level equation sets from the STP that are merged into the MTP even if they are not used by the merged test groups.

The value is a list of equation set numbers separated by commas. For example: [7,8]

This parameter is optional.

 |
 |

keep_wavetables

 |

<wavetables> is a list of wavetables from the STP that are merged into the MTP even if they are not used by the merged test groups.

The value is a list of wavetable names, enclosed in quotes and separated by commas. For example: ['mytable', 'wavetable2']

This parameter is optional.

 |
 |

keep_specifications

 |

<specifications> is a list of specifications from the STP that are merged into the MTP even if they are not used by the merged test groups.

The value is a list of specification names, enclosed in quotes and separated by commas. For example: ['spec5', 'spec5b']

This parameter is optional.

 |
 |

keep_pattern_files

 |

<pattern_files> is a list of level pattern files from the STP that are merged into the MTP even if they are not used by the merged test groups.

The value is a list of pattern file paths, enclosed in quotes and separated by commas. Paths can be absolute or relative to the directory of the MTP. For example: ['/home/johndoe/tps/init_pattern.bin l', 'device/vectors/pat3.binl'']

This parameter is optional.

 |
 |

copy_static_content

 |

<copy_items> (list of strings) specifies is a list of names of files or directories that are to be copied from the device directory of the merged STP to the device directory of the MTP.

The list may contain only names (of files or directories), not paths. The named items must be located in the top level of the device directory. Each name is enclosed in quotes and separated by commas.

These values are supported:

- A list of names of files or directories (but not paths). The named items must be located in the top level of the device directory. Each name is enclosed in quotes and separated by commas.

For example: `copy_static_content = ['my_notes.txt','Change log']`

If you include standard directories in this list (see below), STPM generates a warning and does not copy the contents.

- ['*all*']: Every file and directory in the device directory is copied, except the standard directories testflow, timing, levels, configuration, vectors, and testtable.
- [] (default): No additional files or directories are copied.

This parameter is optional. If it is omitted, no additional content is copied (as if [] had been specified).

 |
 |

pre_proc

 |

<pre_proc> is a script that is executed before this command.

The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.

This is an optional parameter.

 |
 |

post_proc

 |

<post_proc> is a script that is executed after this command.

The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.

This is an optional parameter.

 |

### Syntax（取自子主题 remove subflow）

```
extract_subflow(
test_flow_file  = '<file_path>',
[include_groups  = [<include_group_list>],    ]
[exclude_groups  = [<exclude_group_list>],    ]
[pre_proc        = <pre_proc>,                ]
[post_proc       = <post_proc>]
)
```

### Parameters（取自子主题 remove subflow）

The parameters in the order in which they are listed above:

 |

test_flow_file

 |

<file_path> (string) is the name and path of the testflow file for the STP. The tests that were imported from this STP will be removed from the MTP.

It can be an absolute or a relative path. If it is a relative path, the base directory is the current working directory at the time STPM was called.

 |
 |

include_groups

 |

<include_group_list> (list of strings) is a list of testflow groups that STPM is to remove. If you use this parameter, only those groups specified in the list are removed from the MTP.

The list must be enclosed in square brackets. Each testflow group in the list must be enclosed in quotes and separated by commas.

For example: `test_groups = ['tg3','fail_tg']`

This parameter is optional. It cannot be used when you also specify exclude_groups (see below).

 |
 |

exclude_groups

 |

<exclude_group_list> (list of strings) is a list of testflow groups that STPM is to leave in the MTP. If you use this parameter, all groups in the STP are deleted from the MTP, except those groups specified in the list.

The list must be enclosed in square brackets. Each testflow group in the list must be enclosed in quotes and separated by commas.

For example: `test_groups = ['tg3','fail_tg']`

This parameter is optional. It cannot be used when you also specify include_groups (see above).

 |
 |

pre_proc

 |

<pre_proc> is a script that is executed before this command.

The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.

This is an optional parameter.

 |
 |

post_proc

 |

<post_proc> is a script that is executed after this command.

The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.

This is an optional parameter.

 |

### Syntax（取自子主题 clear duplicated）

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

### Parameters（取自子主题 clear duplicated）

The parameters in the order in which they are listed above:

 |

proc_wavetables

 |

Whether duplicate wavetables are removed:

- 0: They are not removed.
- 1: They are removed.

This parameter is optional, the default is 1.

 |
 |

proc_tim_eqnsets

 |

Whether duplicate timing equation sets are removed:

- 0: They are not removed.
- 1: They are removed.

This parameter is optional, the default is 1.

 |
 |

proc_tim_sets

 |

Whether duplicate timing sets are removed:

- 0: They are not removed.
- 1: They are removed.

This parameter is optional, the default is 1.

 |
 |

proc_tim_specsets

 |

Whether duplicate timing specifications are removed:

- 0: They are not removed.
- 1: They are removed.

This parameter is optional, the default is 1.

 |
 |

proc_lev_eqnsets

 |

Whether duplicate level equation sets are removed:

- 0: They are not removed.
- 1: They are removed.

This parameter is optional, the default is 1.

 |
 |

proc_lev_sets

 |

Whether duplicate level sets are removed:

- 0: They are not removed.
- 1: They are removed.

This parameter is optional, the default is 1.

 |
 |

proc_lev_specsets

 |

Whether duplicate level spec sets are removed:

- 0: They are not removed.
- 1: They are removed.

This parameter is optional, the default is 1.

 |
 |

proc_specifications

 |

 Whether duplicate specifications are removed:

- 0: They are not removed.
- 1: They are removed.

This parameter is optional, the default is 1.

 |
 |

proc_merge_pins

 |

Whether definitions for similar pins are merged in the wavetable, timing set, level set, and DPS pins definitions:

- 0: They are not merged.
- 1: They are merged.

This parameter is optional, the default is 0.

 |
 |

skip_wavetables

 |

<wavetables> is a list of wavetables that are not removed from the MTP even if they are duplicates.

The value is a list of wavetable names, enclosed in quotes and separated by commas. For example: ['wt1', 'wt2', 'wt3']

This parameter is optional.

 |
 |

skip_tim_eqnsets

 |

<tim_eqnsets> is a list of timing equation sets that are not removed from the MTP even if they are duplicates.

The value is a list of equation set numbers separated by commas. For example: [1, 5, 9, 13]

This parameter is optional.

 |
 |

skip_lev_eqnsets

 |

<lev_eqnsets> is a list of level equation sets that are not removed from the MTP even if they are duplicates.

The value is a list of equation set numbers separated by commas. For example: [7,8]

This parameter is optional.

 |
 |

skip_specifications

 |

<specifications> is a list of specifications that are not removed from the MTP even if they are duplicates.

The value is a list of specification names, enclosed in quotes and separated by commas. For example: ['spec1', 'spec2', 'spec3']

This parameter is optional.

 |
 |

analyze_only

 |

<analyze_flag> specifies whether duplicate primaries are actually removed:

- 0: Any found duplicates are removed.
- 1: No primaries are removed but STPM generates a report of found duplicates.

This parameter is optional, the default is 0.

 |
 |

analyzer_path

 |

<path> is the name and location of the report file containing the result of the analysis.

If analyze_only (see above) is 0, this parameter is ignored. If analyze_only is 1, this parameter is observed.

This parameter is optional. If it is not specified, the default is <device directory>/reports/duplicated_report.csv.

 |
 |

pre_proc

 |

<pre_proc> is a script that is executed before this command.

The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.

This is an optional parameter.

 |
 |

post_proc

 |

<post_proc> is a script that is executed after this command.

The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.

This is an optional parameter.

 |

### Syntax（取自子主题 clear unused）

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

### Parameters（取自子主题 clear unused）

The parameters in the order in which they are listed above:

 |

proc_timing

 |

Whether unused wavetables, timing equation sets, timing sets, and timing spec sets are deleted from the MTP:

- 0: They are not removed.
- 1: They are removed.

This parameter is optional, the default is 1.

 |
 |

proc_levels

 |

Whether unused level equation sets, level sets, and level spec sets are deleted from the MTP:

- 0: They are not removed.
- 1: They are removed.

This parameter is optional, the default is 1.

 |
 |

proc_patterns

 |

Whether unused pattern labels are removed:

- 0: They are not removed.
- 1: They are removed.

This parameter is optional, the default is 1.

 |
 |

proc_ports

 |

Whether unused ports are removed:

- 0: They are not removed.
- 1: They are removed.

This parameter is optional, the default is 1.

 |
 |

proc_groups

 |

Whether unused pin groups are removed:

- 0: They are not removed.
- 1: They are removed.

This parameter is optional, the default is 1.

 |
 |

proc_nonexistent_pins

 |

Whether timing and level specifications for unused pins are removed:

- 0: They are not removed.
- 1: They are removed.

This parameter is optional, the default is 0.

 |
 |

skip_wavetables

 |

<wavetables> is a list of wavetables that are not removed from the MTP even if they are unused.

The value is a list of wavetable names, enclosed in quotes and separated by commas. For example: ['wt1', 'wt2', 'wt3']

This parameter is optional.

 |
 |

skip_tim_eqnsets

 |

<tim_eqnsets> is a list of timing equation sets that are not removed from the MTP even if they are unused.

The value is a list of equation set numbers separated by commas. For example: [1, 5, 9, 13]

This parameter is optional.

 |
 |

skip_lev_eqnsets

 |

<lev_eqnsets> is a list of level equation sets that are not removed from the MTP even if they are unused.

The value is a list of equation set numbers separated by commas. For example: [7,8]

This parameter is optional.

 |
 |

skip_specifications

 |

<specifications> is a list of specifications that are not removed from the MTP even if they are unused.

The value is a list of specification names, enclosed in quotes and separated by commas. For example: ['spec1', 'spec2', 'spec3']

This parameter is optional.

 |
 |

skip_patterns

 |

<patterns> is a list of pattern files that are not removed from the MTP even if they are unused.

The value is a list of paths of pattern files, enclosed in quotes and separated by commas. The paths can be either absolute or relative to current device directory (in which case they must include the name of the directory).

For example (assuming a device directory named mtp): ['/usr/engineer/pat.binl', 'mtp/vectors/DAC/pat.binl']

This parameter is optional.

 |
 |

analyze_only

 |

<analyze_flag> specifies whether duplicate primaries are actually removed:

- 0: Any found duplicates are removed.
- 1: No primaries are removed but STPM generates a report of found duplicates.

This parameter is optional, the default is 0.

 |
 |

analyzer_path

 |

<path> is the name and location of the report file containing the result of the analysis.

If analyze_only (see above) is 0, this parameter is ignored. If analyze_only is 1, this parameter is observed.

This parameter is optional. If it is not specified, the default is <device directory>/reports/unused_report.csv.

 |
 |

pre_proc

 |

<pre_proc> is a script that is executed before this command.

The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.

This is an optional parameter.

 |
 |

post_proc

 |

<post_proc> is a script that is executed after this command.

The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.

This is an optional parameter.

 |

<!-- 语法节 end -->

## 是什么

**一句话：STPM control file 是一段脚本，不是一张配置表。** 原文就一句定义：

> 「An STPM control file contains a script that tells SmarTest Program Manager how to perform an conversion process. There are commands for adding, replacing, and removing tests as well as parameters and setup commands.」

**拆开来看，这一句给了三件事**：

| 原文片段 | 意味着 |
|---|---|
| `contains a script` | 它是**可执行的一串命令**，不是被读进来的键值表 |
| `tells SmarTest Program Manager how to perform an conversion process` | **读它的人是 [[stpm]]**；它描述的是**一次「转换过程」** |
| `commands for adding, replacing, and removing tests as well as parameters and setup commands` | 内容分两类：**命令**（增/替/删测试）+ **参数与 setup 命令** |

**本页真正有用的东西是它的目录。** 定义文档自己没有正文，只给了一张 **27 条的 `Subtopics` 清单**——
**那 27 条就是这份脚本能做的事的全集**（原文的措辞是 `There are commands for …`）。
按名字归类，结构如下：

| 组 | 条数 | 子主题 |
|---|---|---|
| **定义 / 配置** | 3 | `Structure of an STPM control file` / `File and parameter settings` / `Preprocessing and postprocessing scripts` |
| **测试增删改** | 7 | `write_tp` / `add_test` / `add_burst` / `add_test_to_burst` / `add_empty_test_group` / `remove_test` / `replace_test` |
| **pattern 与 label** | 3 | `remove_label` / `add_pattern` / `replace_pattern` |
| **TPT 操作** | 9 | `tpt_generate_template` / `tpt_import_from_device` / `tpt_generate_device_dir` / `tpt_merge` / `tpt_add_test` / `tpt_replace_test` / `tpt_generate_tp` / `tpt_compare_tp` / `tpt_generate_test_stages` |
| **subflow** | 3 | `extract_subflow` / `merge_subflow` / `remove_subflow` |
| **清理** | 2 | `clear_duplicated` / `clear_unused` |

**分组是「按名字」分的，不是原文分的**（原文只给平铺的 27 条清单）。**能据原文说的是：这 27 条全都挂着 `commands` 这个词**——
`tpt_*` 那 9 条是**测试程序模板（TPT）侧**的操作，`*_subflow` 那 3 条是**子流程**的抽取 / 合并 / 删除，
最后 2 条是**清理冗余与未用项**。

> **注意 `Subtopics` 这张清单本身就是「会存在的页」**（schema §9.1 第四类：
> 定义文档自己声明的父子关系），所以上面这些**名字可以链**——
> 其中 `preprocessing-and-postprocessing-scripts`、`tpt-generate-device-dir`、
> `tpt-import-from-device`、`stpm-merge-rules-file` 已经在本 wiki 里建好了。

### 这份文件长什么样：四个区

**（以下来自本页「语法 / 参数」节里脚本逐字抽的那个 `Example`——
脚本自己标了它取自子主题 `Structure of an STPM control file`，而那个子主题本页没读。）**

示例把整份文件分成四个用 `#` 注释块标出的区，顺序与角色是：

| 区（示例里的注释原文） | 里面放什么 |
|---|---|
| `# Input: Device Test Program Location` | 区的标题行本身是注释；真正的输入写在下一个区 |
| `# Configuration` | `mtp_device_testflow`（MTP 测试流程路径）+ `merge_rules`（合并规则文件） |
| `# Integration Commands` | 命令，示例里是两个 `add_test(...)` |
| `# Output: Device Test Program Location` | 输出，示例里是 `write_tp` |

**两个区名（Input / Output）在示例里都是空标题**——真正的内容一个在 `# Configuration` 下、
一个在 `# Integration Commands` 下。**这是示例的写法，不是原文的要求**（原文那一句只说了有命令、有参数、有 setup 命令）。

### 一处值得注意的形状差异：`write_tp` 在示例里是赋值，在语法节里是调用

**（同样来自本页「语法 / 参数」节，来源是子主题，本页未读那些子主题。）**

| 出现在哪 | 写法 |
|---|---|
| `Example`（取自 `Structure of an STPM control file`） | `write_tp = '/home/user/93K_Device/project.tf'` |
| `Syntax`（取自子主题 `write_tp`） | `write_tp(path = '<mtp_target_file>', [pre_proc = …], [post_proc = …])` |

**同一个东西，一处写成赋值、一处写成函数调用。** 而同一个示例里的 `add_test` 两处都是**调用**
（`add_test(test_flow_file = …, test = …)`）。
**原文没有解释这种差异，本页不替它调和**——按 §10 并列记下。
**（推断）示例那两行是「配置项」语义上的简写**，依据是它紧跟在 `mtp_device_testflow = …`
和 `merge_rules = …` 两个赋值后面；**但这只是推断，原文一个字没说。**

### 参数区的一句原文（本页读了的那篇里唯一讲参数的话）

定义文档的正文里**除了开头那句定义，就只剩 `## Functional changes` 一节**。
**「`mtp_device_testflow` 到底是什么、有哪些参数、默认值是什么」这些本页一个字都没有**——
它们在未读的子主题 `File and parameter settings` 里。

## 典型用法

> **原文没有 `## Procedure` / `## Before you begin` / `## What to do next` 段。**
> 定义文档只有 43 行：一张 `Subtopics` 清单 + 一句定义 + 一条版本记录。**没有步骤可抄。**

**能说的只有「这份脚本在流程里的位置」**：

**1. 它是一次转换过程的输入。** 原文：`tells SmarTest Program Manager how to perform an conversion process`。
**转换的两端都是外部的东西**：输入是别人的测试程序（示例里叫 STP —— source test program），
输出是 MTP（master test program）。**（推断）依据是示例的区名 `Input:` / `Output:` 和
`mtp_device_testflow` 这个键名里的 `mtp`**；**原文没有在小节里解释 STP / MTP 这对缩写。**

**2. 写它的顺序（照示例的区序）**：
**先定输入与配置**（`mtp_device_testflow`、`merge_rules`）→
**再写命令**（`add_test` 之类）→ **最后写输出**（`write_tp`）。
**如果输出路径与输入路径相同，就是原地改**——（推断）依据是示例里两个值逐字相同
（都是 `/home/user/93K_Device/project.tf`）；**原文没在这篇里说这件事。**

**3. 有备份机制。** 示例的配置区里没有它，但本页「语法 / 参数」节的 `Parameters` 表里有
`enable_backup`（`0` 不备份 / `1` 备份），**原文用一整段讲了备份文件落在哪、叫什么名字**：
子目录名叫 `back`，文件名追加 `"_YYMMDD_HHMMSS"`，例子是
`<device_directory>/configuration/back/mypins_121102_214323.cfg`。
**（这一条来自未读的子主题 `File and parameter settings`，只是逐字出现在本页语法节里。）**

**4. 有前处理 / 后处理脚本。** 本页「语法 / 参数」节有 `pre_proc` / `post_proc` 的完整语法，
**几乎每个命令都带这两个可选参数**。**它们怎么用、`&mdir` 这类占位符是什么，在本页语法节里，
而那是子主题 `Preprocessing and postprocessing scripts` 的内容——本页没读那一篇。**

**5. 下一步**：定义文档没有 `## Related information` 段。**要走下去只能顺着上面那张 27 条的清单点。**

## 和谁有关

- [[stpm]] — **读这份文件的那个工具**。原文：`tells SmarTest Program Manager how to perform an conversion process`。
  **两页的关系是「输入 ↔ 执行者」，不是同类**
- [[stpm-merge-rules-file]] — **配置区里 `merge_rules` 这个键指向的文件**；
  **（推断）依据只是键名与文件名的字面对应**，原文在本页没把两者连起来说
- [[preprocessing-and-postprocessing-scripts]] — **本页 27 条子主题里的第 3 条**，
  已被本 wiki 建页；它是 `pre_proc` / `post_proc` 的语法出处
- [[testflow-file]] — **被转换的那个东西**：`mtp_device_testflow` 的值就是一个 testflow 文件路径
- [[test-suite ]] — 命令的宾语：`add_test` / `remove_test` / `replace_test` 操作的
  都是 test suite；**原文在本页没有说这件事，只说「commands for adding, replacing, and removing tests」**
- [[pattern-master-file]] — `remove_label` 的参数 `pmf_only` 讲的是「pattern 从 pattern master 里删不删」，
  **（推断）`pmf` 就是 pattern master file 的缩写**；原文没展开这个缩写
- [[device-directory]] — 备份的例子、`pat_dir` 的相对基准都指向它
- [[tpt-generate-device-dir]] / [[tpt-import-from-device]] — **本页 27 条子主题里已经建好页的两条**
- `tpt_generate_template` / `tpt_merge` / `tpt_add_test` / `tpt_replace_test` / `tpt_generate_tp` /
  `tpt_compare_tp` / `tpt_generate_test_stages` / `extract_subflow` / `merge_subflow` / `remove_subflow` /
  `clear_duplicated` / `clear_unused` / `write_tp` / `add_test` / `add_burst` / `add_test_to_burst` /
  `add_empty_test_group` / `remove_test` / `replace_test` / `remove_label` / `add_pattern` /
  `replace_pattern` / `Structure of an STPM control file` / `File and parameter settings`（**均未建**）—
  **本页 27 条子主题里剩下的那些**；**它们的语法在本页「语法 / 参数」节里逐字存在，
  但每一篇的正文（什么时候用、有什么坑）本页都没有**
- [[command-reference]] / [[project]] — 同层对照：`project` 是本页 `stage: project` 的归属阶段页

## 版本

原文有 `## Functional changes` 段，**只有一条**：

- **Introduced in SmarTest 7.0.4**

> **注意这一条和 `testflow-file` 那页的写法不同。**
> 那边第一条写的是 `Introduced before SmarTest 6.3.2`（**哨兵值**，意思是「在覆盖范围开始前就有了」，
> schema §11.2 ②）；**这里写的是 `Introduced in SmarTest 7.0.4`——是确切的引入版本**。
> **两份文档用的是两种措辞，本页照原文记，不替它们统一。**

**定义文档只记了引入版本，没有任何后续变更条目**——
所以「7.0.4 之后这个文件的语法改过什么」本页没有。**（那要看 27 个子主题各自的 `Functional changes`，本页没读。）**

## 出处

`sources:` 一篇：

`02_System_reference/02.09_Test_Program_Management/02.09.02.03_STPM_control_file.md`
（TDC `130562.htm`）

**这一篇只有 42 行**：一段 `#### Subtopics` 清单（27 条）+ 一句定义 + 一条 `## Functional changes`。
**它没有正文、没有 `## Syntax`、没有 `## Procedure`、没有 `## Related information`。**

**本页没做的**：

- **27 个子主题一篇都没读。** 它们是本页内容的正主——**每个命令的参数表、默认值、
  前置条件、报错，本页全部没有**。
  `sources:` 只列了定义文档一篇，**所以本页的正文只写到「有哪些命令」为止**。
- **本页「是什么」和「典型用法」里有几段标了「来自本页『语法 / 参数』节」**——
  **那几段的依据是脚本逐字抽进本页的子主题内容，不是我读过的文档**，
  每一处我都标了它取自哪个子主题。**把它们写进来是因为它们逐字在本页上；
  「那一篇到底还说了什么」本页仍然不知道。**
- **`## Functional changes` 里只有引入版本**，无变更历史（见上）。
- **一篇文档一张图都没有**，本页没有任何来自图的结论。
- **没有实测**：本页没有跑过 STPM，也没有拿一份真实 control file 验证过。

> ⚠️ **本篇的语料瑕疵，照实记，一处都没替它改**：
>
> ① **定义句里有 `an conversion`**（应为 `a conversion`）：
> `tells SmarTest Program Manager how to perform an conversion process`。
> ② **`## Functional changes` 之外没有任何小节**——**这一条不是瑕疵，是事实**，写在这里是为了
> 让读者明白「本页为什么这么薄」：**薄的原因是定义文档本身是张目录页，不是本页偷懒。**
>
> **另外有几处瑕疵出现在本页「语法 / 参数」节里（脚本逐字抽的，来自本页未读的子主题），
> 本页一并记下但不改语法节**：
> ③ `merging the levels from the new test with hem` —— **`hem` 应为 `them`**。
> ④ `The pattern is deleted from the MPT.` —— **`MPT` 应为 `MTP`**（同一句上下文里其余地方都写 MTP）。
> ⑤ `replace the existing test in the to the MTP` —— **多了一个 `the`**。
> ⑥ `The list must be enclosed in square brackets..` —— **两个句号**。
> ⑦ `This parameter is ignored if \`test_remove = 0\` is specified` —— **句末缺句号**。
> ⑧ `['/home/johndoe/tps/init_pattern.bin l', 'device/vectors/pat3.binl'']` ——
> **第一个路径里混进了一个空格（`.bin l`），且整个列表的两个单引号对不齐**。

`verified: doc-only`
