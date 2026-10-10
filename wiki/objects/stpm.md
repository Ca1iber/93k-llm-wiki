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

> 本节 **65,142 字符逐字取自** `<02_System_reference/02.09_Test_Program_Management/02.09.02_SmarTest_Program_Manager.md>` 及其子主题 `<02_System_reference/02.09_Test_Program_Management/02.09.02.02.01_Creating_and_editing_an_STPM_control_file.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.01_Structure_of_an_STPM_control_file.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.02_File_and_parameter_settings.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.04_write_tp.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.05_add_test.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.06_add_burst.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.07_add_test_to_burst.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.08_add_empty_test_group.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.09_remove_test.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.10_replace_test.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.11_remove_label.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.12_add_pattern.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.13_replace_pattern.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.14_tpt_generate_template.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.15_tpt_import_from_device.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.16_tpt_generate_device_dir.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.17_tpt_merge.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.18_tpt_add_test.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.19_tpt_replace_test.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.20_tpt_generate_tp.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.21_tpt_compare_tp.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.22_tpt_generate_test_stages.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.23_extract_subflow.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.24_merge_subflow.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.25_remove_subflow.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.26_clear_duplicated.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.27_clear_unused.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.01_STPM_merge_rules_file_syntax.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.02_new_digital_pin.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.03_overwrite_digital_pin_no.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.04_merge_digital_pin_dir.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.05_new_dps_pin.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.06_overwrite_dps_pin_polarity.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.07_new_pin_group.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.08_overwrite_pin_group.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.09_merge_unused_pin_group.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.10_new_port.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.11_overwrite_port.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.12_new_site.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.13_overwrite_channel.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.14_new_timing_equation_set.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.15_new_waveform.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.16_modify_waveform_index.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.17_overwrite_statemap.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.18_new_level_resource.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.19_overwrite_level_resource.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.20_new_level_equation_set.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.21_new_level_set.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.22_new_ac_specset.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.23_new_dc_specset.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.24_overwrite_ac_spec_typ.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.25_overwrite_ac_spec_minmax.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.26_overwrite_dc_spec_typ.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.27_overwrite_dc_spec_minmax.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.28_overwrite_label_wvt.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.29_overwrite_flow_var_value.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.05.01_Test_suite_table_of_a_TPT.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.05.02_Bin_table_of_a_TPT.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.05.03_Test_table_of_a_TPT.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.05.04_Test_parameter_table_of_a_TPT.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.05.05_Test_flag_table_of_a_TPT.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.05.06_Test_stage_table_of_a_TPT.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.06_STPM_command_line_options.md>`。**不是转述。**
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

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/131038.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 2 列。
> 首行（上游原文）：mtp_device_testflow | <testflow_file> (string) is the name and path of the testflow file of the MTP which STPM is to modify or otherwise work with. It can be an…

### Example（取自子主题 STPM control file › File and parameter settings）

See the sample control file in `Structure of an STPM control file`（raw: `02.09.02.03.01_Structure_of_an_STPM_control_file.md`）.

### Syntax（取自子主题 STPM control file › Preprocessing and postprocessing scripts）

Both the pre_proc (shown below) and post_proc parameters have the same syntax.

```
pre_proc = '<script>[&mdir][&sdir][&mtp_tf][&mtp_pmf][&mtp_conf][&mtp_tim][&mtp_lev][&mtp_tt][&mtp_rout][&mtp_wf][&mtp_anctrl][&mtp_chatt][&mtp_prot][&mtp_att][&stp_tf][&stp_pmf][&stp_conf][&stp_tim][&stp_lev][&stp_tt][&stp_rout][&stp_wf][&stp_anctrl][&stp_chatt][&stp_prot][&stp_att][<user_parameters>]'
```

The available script parameters in the order in which they are listed above:

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/143913.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：28 行 × 2 列。
> 首行（上游原文）：<script> | The name and path of the script file to call. The path can be absolute or relative. If it is a relative path, the base directory is the current worki…

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

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/132794.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：path | <mtp_target_file> (string) is the name and location under which STPM saves the MTP (master test program) testflow file after it has modified it. It can b…
> 表内引用（2 条，供检索）：`enable_backup`（raw: `02.09.02.03.02_File_and_parameter_settings.md`） · `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）

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

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/130881.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：19 行 × 2 列。
> 首行（上游原文）：test_flow_file | <testflow_file> (string) is the path, including the name, of the testflow file of the source test program (STP) that contains the test that you…
> 表内引用（1 条，供检索）：`Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）

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

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/138220.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 2 列。
> 首行（上游原文）：name | <testflow_file> (string) is the path, including the name, of the testflow file of the source test program (STP) that contains the test that you want to a…
> 表内引用（1 条，供检索）：`Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）

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

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/131020.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 2 列。
> 首行（上游原文）：test_flow_file | <testflow_file> (string) is the path (including the name) of the testflow file of the source test program (STP) that contains the test that you…
> 表内引用（1 条，供检索）：`Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）

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

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/140643.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 2 列。
> 首行（上游原文）：test_group | <test_group> (string) is the name of the new test group you want to create in the MTP.
> 表内引用（1 条，供检索）：`Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）

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

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/130900.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 2 列。
> 首行（上游原文）：test | <test> (string) is the name of the test suite in the MTP that STPM should remove.
> 表内引用（1 条，供检索）：`Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）

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

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/130985.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：14 行 × 2 列。
> 首行（上游原文）：test_flow_file | <testflow_file> (string) is the path (including the name) of the testflow file of the source test program (STP) that contains the test with whi…
> 表内引用（1 条，供检索）：`Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）

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

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/140646.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 2 列。
> 首行（上游原文）：label | <label_name> (string) is the name of the label that you want to remove from the MTP.
> 表内引用（1 条，供检索）：`Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）

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

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/143922.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 2 列。
> 首行（上游原文）：test_flow_file | <testflow_file> (string) is the path (including the name) of the testflow file of the source test program (STP) that contains the pattern that …

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

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/143923.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 2 列。
> 首行（上游原文）：test_flow_file | <testflow_file> (string) is the path (including the name) of the testflow file of the source test program (STP) that contains the pattern that …
> 表内引用（1 条，供检索）：`Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）

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

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/132698.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：tpt_dir | <location> (string) is the path, including the name, where the new template files and directories are created. The path can be either absolute or rela…
> 表内引用（1 条，供检索）：`Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）

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

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/132700.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 2 列。
> 首行（上游原文）：device_test_flow | <testflow_file> (string) is the path of the testflow file from which the test program template is to be generated. The path can be either abs…
> 表内引用（2 条，供检索）：`tpt_generate_device_dir`（raw: `02.09.02.03.16_tpt_generate_device_dir.md`） · `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）

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

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/132751.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 2 列。
> 首行（上游原文）：tpt_dir | <tpt_directory> (string) is the name and path of the directory containing the TPT files from which the device directory is to be generated. The path c…
> 表内引用（1 条，供检索）：`Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）

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

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/140674.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 2 列。
> 首行（上游原文）：source_tpts | <tpt_file> (list of strings) is a list of TPT directories that you want to merge into a single TPT. Include in the list the path of each TPT you w…
> 表内引用（1 条，供检索）：`Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）

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

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/140657.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：11 行 × 2 列。
> 首行（上游原文）：test_flow_file | <testflow_file> (string) is the path, including the name, of the testflow file of the source test program (STP) that contains the test that you…
> 表内引用（2 条，供检索）：`test suite table`（raw: `02.09.02.05.01_Test_suite_table_of_a_TPT.md`） · `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）

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

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/140661.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：13 行 × 2 列。
> 首行（上游原文）：test_flow_file | <testflow_file> (string) is the path (including the name) of the testflow file of the source test program (STP) that contains the test with whi…
> 表内引用（2 条，供检索）：`test suite table`（raw: `02.09.02.05.01_Test_suite_table_of_a_TPT.md`） · `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）

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

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/140664.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 2 列。
> 首行（上游原文）：generate_complete_device_directory | <complete_device_flag> specify whether a complete device directory or only a skeleton is generated: 0: The generated device…
> 表内引用（1 条，供检索）：`Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）

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

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/140668.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 2 列。
> 首行（上游原文）：report_file_path | <report_file> (string) is the path (including the name) where the command is to store the report file. If this parameter is omitted, the file…
> 表内引用（1 条，供检索）：`Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）

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

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/140669.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：include_undefined_objects | <flag> (0 or 1) specifies how STPM treats undefined objects in the test stage table: 0: Undefined objects are not included in the da…
> 表内引用（2 条，供检索）：`test stage table`（raw: `02.09.02.05.06_Test_stage_table_of_a_TPT.md`） · `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）

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

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/140648.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：17 行 × 2 列。
> 首行（上游原文）：test_flow_file | <file_path> (string) is the name and path of the testflow file for the STP you want to generate. It can be an absolute or a relative path. If i…
> 表内引用（1 条，供检索）：`Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）

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

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/140650.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：18 行 × 2 列。
> 首行（上游原文）：test_flow_file | <file_path> (string) is the name and path of the testflow file for the STP you want to merge into the MTP. It can be an absolute or a relative …
> 表内引用（1 条，供检索）：`Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）

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

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/140653.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 2 列。
> 首行（上游原文）：test_flow_file | <file_path> (string) is the name and path of the testflow file for the STP. The tests that were imported from this STP will be removed from the…
> 表内引用（1 条，供检索）：`Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）

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

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/135018.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：17 行 × 2 列。
> 首行（上游原文）：proc_wavetables | Whether duplicate wavetables are removed: 0: They are not removed. 1: They are removed. This parameter is optional, the default is 1.
> 表内引用（1 条，供检索）：`Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）

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

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/135019.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：15 行 × 2 列。
> 首行（上游原文）：proc_timing | Whether unused wavetables, timing equation sets, timing sets, and timing spec sets are deleted from the MTP: 0: They are not removed. 1: They are …
> 表内引用（1 条，供检索）：`Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）

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
