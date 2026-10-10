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

> 本节 **24,593 字符逐字取自** `<02_System_reference/02.09_Test_Program_Management/02.09.02.03_STPM_control_file.md>` 及其子主题 `<02_System_reference/02.09_Test_Program_Management/02.09.02.03.01_Structure_of_an_STPM_control_file.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.02_File_and_parameter_settings.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.04_write_tp.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.05_add_test.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.06_add_burst.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.07_add_test_to_burst.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.08_add_empty_test_group.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.09_remove_test.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.10_replace_test.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.11_remove_label.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.12_add_pattern.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.13_replace_pattern.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.14_tpt_generate_template.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.15_tpt_import_from_device.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.16_tpt_generate_device_dir.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.17_tpt_merge.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.18_tpt_add_test.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.19_tpt_replace_test.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.20_tpt_generate_tp.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.21_tpt_compare_tp.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.22_tpt_generate_test_stages.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.23_extract_subflow.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.24_merge_subflow.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.25_remove_subflow.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.26_clear_duplicated.md>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.27_clear_unused.md>`。**不是转述。**
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

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/131038.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 2 列。
> 首行（上游原文）：mtp_device_testflow | <testflow_file> (string) is the name and path of the testflow file of the MTP which STPM is to modify or otherwise work with. It can be an…

### Example（取自子主题 File and parameter settings）

See the sample control file in `Structure of an STPM control file`（raw: `02.09.02.03.01_Structure_of_an_STPM_control_file.md`）.

### Syntax（取自子主题 Preprocessing and postprocessing scripts）

Both the pre_proc (shown below) and post_proc parameters have the same syntax.

```
pre_proc = '<script>[&mdir][&sdir][&mtp_tf][&mtp_pmf][&mtp_conf][&mtp_tim][&mtp_lev][&mtp_tt][&mtp_rout][&mtp_wf][&mtp_anctrl][&mtp_chatt][&mtp_prot][&mtp_att][&stp_tf][&stp_pmf][&stp_conf][&stp_tim][&stp_lev][&stp_tt][&stp_rout][&stp_wf][&stp_anctrl][&stp_chatt][&stp_prot][&stp_att][<user_parameters>]'
```

The available script parameters in the order in which they are listed above:

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/143913.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：28 行 × 2 列。
> 首行（上游原文）：<script> | The name and path of the script file to call. The path can be absolute or relative. If it is a relative path, the base directory is the current worki…

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

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/132794.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：path | <mtp_target_file> (string) is the name and location under which STPM saves the MTP (master test program) testflow file after it has modified it. It can b…
> 表内引用（2 条，供检索）：`enable_backup`（raw: `02.09.02.03.02_File_and_parameter_settings.md`） · `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）

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

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/130881.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：19 行 × 2 列。
> 首行（上游原文）：test_flow_file | <testflow_file> (string) is the path, including the name, of the testflow file of the source test program (STP) that contains the test that you…
> 表内引用（1 条，供检索）：`Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）

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

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/138220.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 2 列。
> 首行（上游原文）：name | <testflow_file> (string) is the path, including the name, of the testflow file of the source test program (STP) that contains the test that you want to a…
> 表内引用（1 条，供检索）：`Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）

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

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/131020.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 2 列。
> 首行（上游原文）：test_flow_file | <testflow_file> (string) is the path (including the name) of the testflow file of the source test program (STP) that contains the test that you…
> 表内引用（1 条，供检索）：`Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）

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

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/140643.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 2 列。
> 首行（上游原文）：test_group | <test_group> (string) is the name of the new test group you want to create in the MTP.
> 表内引用（1 条，供检索）：`Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）

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

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/130900.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 2 列。
> 首行（上游原文）：test | <test> (string) is the name of the test suite in the MTP that STPM should remove.
> 表内引用（1 条，供检索）：`Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）

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

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/130985.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：14 行 × 2 列。
> 首行（上游原文）：test_flow_file | <testflow_file> (string) is the path (including the name) of the testflow file of the source test program (STP) that contains the test with whi…
> 表内引用（1 条，供检索）：`Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）

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

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/140646.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 2 列。
> 首行（上游原文）：label | <label_name> (string) is the name of the label that you want to remove from the MTP.
> 表内引用（1 条，供检索）：`Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）

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

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/143922.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 2 列。
> 首行（上游原文）：test_flow_file | <testflow_file> (string) is the path (including the name) of the testflow file of the source test program (STP) that contains the pattern that …

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

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/143923.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 2 列。
> 首行（上游原文）：test_flow_file | <testflow_file> (string) is the path (including the name) of the testflow file of the source test program (STP) that contains the pattern that …
> 表内引用（1 条，供检索）：`Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）

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

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/132698.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：tpt_dir | <location> (string) is the path, including the name, where the new template files and directories are created. The path can be either absolute or rela…
> 表内引用（1 条，供检索）：`Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）

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

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/132700.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 2 列。
> 首行（上游原文）：device_test_flow | <testflow_file> (string) is the path of the testflow file from which the test program template is to be generated. The path can be either abs…
> 表内引用（2 条，供检索）：`tpt_generate_device_dir`（raw: `02.09.02.03.16_tpt_generate_device_dir.md`） · `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）

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

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/132751.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 2 列。
> 首行（上游原文）：tpt_dir | <tpt_directory> (string) is the name and path of the directory containing the TPT files from which the device directory is to be generated. The path c…
> 表内引用（1 条，供检索）：`Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）

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

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/140674.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 2 列。
> 首行（上游原文）：source_tpts | <tpt_file> (list of strings) is a list of TPT directories that you want to merge into a single TPT. Include in the list the path of each TPT you w…
> 表内引用（1 条，供检索）：`Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）

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

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/140657.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：11 行 × 2 列。
> 首行（上游原文）：test_flow_file | <testflow_file> (string) is the path, including the name, of the testflow file of the source test program (STP) that contains the test that you…
> 表内引用（2 条，供检索）：`test suite table`（raw: `02.09.02.05.01_Test_suite_table_of_a_TPT.md`） · `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）

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

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/140661.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：13 行 × 2 列。
> 首行（上游原文）：test_flow_file | <testflow_file> (string) is the path (including the name) of the testflow file of the source test program (STP) that contains the test with whi…
> 表内引用（2 条，供检索）：`test suite table`（raw: `02.09.02.05.01_Test_suite_table_of_a_TPT.md`） · `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）

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

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/140664.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 2 列。
> 首行（上游原文）：generate_complete_device_directory | <complete_device_flag> specify whether a complete device directory or only a skeleton is generated: 0: The generated device…
> 表内引用（1 条，供检索）：`Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）

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

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/140668.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 2 列。
> 首行（上游原文）：report_file_path | <report_file> (string) is the path (including the name) where the command is to store the report file. If this parameter is omitted, the file…
> 表内引用（1 条，供检索）：`Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）

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

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/140669.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：include_undefined_objects | <flag> (0 or 1) specifies how STPM treats undefined objects in the test stage table: 0: Undefined objects are not included in the da…
> 表内引用（2 条，供检索）：`test stage table`（raw: `02.09.02.05.06_Test_stage_table_of_a_TPT.md`） · `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）

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

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/140648.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：17 行 × 2 列。
> 首行（上游原文）：test_flow_file | <file_path> (string) is the name and path of the testflow file for the STP you want to generate. It can be an absolute or a relative path. If i…
> 表内引用（1 条，供检索）：`Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）

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

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/140650.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：18 行 × 2 列。
> 首行（上游原文）：test_flow_file | <file_path> (string) is the name and path of the testflow file for the STP you want to merge into the MTP. It can be an absolute or a relative …
> 表内引用（1 条，供检索）：`Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）

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

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/140653.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 2 列。
> 首行（上游原文）：test_flow_file | <file_path> (string) is the name and path of the testflow file for the STP. The tests that were imported from this STP will be removed from the…
> 表内引用（1 条，供检索）：`Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）

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

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/135018.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：17 行 × 2 列。
> 首行（上游原文）：proc_wavetables | Whether duplicate wavetables are removed: 0: They are not removed. 1: They are removed. This parameter is optional, the default is 1.
> 表内引用（1 条，供检索）：`Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）

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

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/135019.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：15 行 × 2 列。
> 首行（上游原文）：proc_timing | Whether unused wavetables, timing equation sets, timing sets, and timing spec sets are deleted from the MTP: 0: They are not removed. 1: They are …
> 表内引用（1 条，供检索）：`Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）

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
