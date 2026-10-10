---
type: object
title: tpt_import_from_device
layer: L3
stage: project
tags: [project, stpm, tpt, test-program-template, device-directory, command, wildcard, copy-static-content, overwrite, smartest-7.0.4, smartest-7.2.1, smartest-7.2.2]
related: [stpm, stpm-control-file, tpt-generate-device-dir, stpm-merge-rules-file, device-directory, preprocessing-and-postprocessing-scripts, testflow-file, group-node, test-suite, testflow, mapping-project, project, smartest-7.0.4, smartest-7.2.1, smartest-7.2.2]
sources:
  - 02_System_reference/02.09_Test_Program_Management/02.09.02.03.15_tpt_import_from_device.md
created: 2026-09-21
updated: 2026-09-21
verified: doc-only
---

# tpt_import_from_device

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,478 字符逐字取自** `<02_System_reference/02.09_Test_Program_Management/02.09.02.03.15_tpt_import_from_device.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

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

### Parameters

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/132700.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 2 列。
> 首行（上游原文）：device_test_flow | <testflow_file> (string) is the path of the testflow file from which the test program template is to be generated. The path can be either abs…
> 表内引用（2 条，供检索）：`tpt_generate_device_dir`（raw: `02.09.02.03.16_tpt_generate_device_dir.md`） · `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）

### Example

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

<!-- 语法节 end -->

## 是什么

**`tpt_import_from_device` 是 STPM（SmarTest Program Manager）控制文件里的一条命令：
拿一个已经存在的 device directory，做出一个 test program template（下文简称 TPT）。**
原文头两句（逐字）：

> 「The tpt_import_from_device command for the SmarTest Program Manager (STPM) control file lets you create a test program template from an existing device directory.」
> 「When executing the command, STPM creates the files that make up a test program template, filling them with appropriate data from an existing testflow and device directory that you specify.」

**两句合起来是四件事**：

| # | 原文 | 要点 |
|---|---|---|
| 1 | `the … command for the SmarTest Program Manager (STPM) control file` | **它是写在 STPM 控制文件里的一条命令**，不是固件命令、也不是 C++ API |
| 2 | `lets you create a test program template from an existing device directory` | **输入是现成的 device directory，输出是 TPT** |
| 3 | `STPM creates the files that make up a test program template` | **建文件的是 STPM**（不是这条命令自己在机台上跑） |
| 4 | `filling them with appropriate data from an existing testflow and device directory that you specify` | **灌进去的数据来自两处：一个 testflow + 一个 device directory** |

**第 4 件是本命令的参数表的由来**：`device_test_flow` 指那个 testflow，
`copy_static_content` 从 device directory 里搬东西，`tpt_dir` 指产物落在哪。

**方向只有一个**：**device directory → TPT。** 原文没有任何一句说可以反过来
（**本页与 [[tpt-generate-device-dir]] 是一对反向操作**——那一页是 TPT → device directory；
**两条命令各自成篇，本页只讲 import 这一向**）。

### 八个参数：两个必填，六个可选

**语法节里有完整的语法与逐字定义**，这里只把「必填/可选/默认」摊平（**依据是语法行里的方括号与各格末尾那句话**）：

| 参数 | 必填 | 省略时（**原文**） |
|---|---|---|
| `device_test_flow` | ✅ **必填** | — |
| `tpt_dir` | ✅ **必填** | — |
| `include_groups` | 可选 | `If it is omitted, all groups are imported.` |
| `empty_groups` | 可选 | `If it is omitted, no groups are emptied.` |
| `copy_static_content` | 可选 | `If it is omitted, no additional content is copied.` |
| `allow_overwrite` | 可选 | `If it is omitted, no files or directories are overwritten.` |
| `pre_proc` | 可选 | —（原文只写 `This is an optional parameter.`） |
| `post_proc` | 可选 | 同上 |

**两个必填项的分工**（原文各一句）：

| 参数 | 原文定义 |
|---|---|
| `device_test_flow` | `<testflow_file> (string) is the path of the testflow file from which the test program template is to be generated.` |
| `tpt_dir` | `<location> (string) is the path, including the name, where the new template files and directories are created.` |

**两条路径规则完全一样**（原文两句，两个格子各有一份）：
`The path can be either absolute or relative to the current working directory.`
——**绝对路径或「相对当前工作目录」都行。注意基准是 current working directory，
不是 master file 那种「以文件自身所在目录为基准」**。

### `tpt_dir` 上有一条硬前提（**这是本命令唯一的「必须先满足」**）

原文（逐字，在 `tpt_dir` 那一格里）：

> 「If the directory does not yet exist, STPM creates it. If the directory already exists, it must either be empty or the allow_overwrite parameter (see below) must be set to 1.」

**条件 → 结果**：

| `tpt_dir` 的状态 | STPM 怎么做（**原文**） |
|---|---|
| **不存在** | **STPM 建它**（`STPM creates it`） |
| **存在、且为空** | **可以继续**（`must either be empty`） |
| **存在、非空** | **只有 `allow_overwrite = 1` 才能继续**（`or the allow_overwrite parameter … must be set to 1`） |

**⚠️ 这一格里那句 `or` 后面跟的是「必须设成 1」，但原文没有写「设成 1 之后会覆盖」——
覆盖的后果写在 `allow_overwrite` 那一格里**（见下）。**两格要合起来读。**

### `allow_overwrite`：0 与 1 是两个不同的结局

原文（逐字，含它自己的两个 bullet）：

> 「`<overwrite_flag>` specifies whether STPM may overwrite existing files in the test program template directory:
> - 0 (default): No existing files or directories in the test program template directory may be overwritten. If this prevents STPM from saving a created file, it displays an error and stops the conversion.
> - 1: STPM may overwrite existing files and directories.」

| 值 | 原文 | 后果 |
|---|---|---|
| `0`（**默认**） | `No existing files or directories in the test program template directory may be overwritten.` | **不许覆盖**；**一旦因此存不下一个已建好的文件 → 报一条错并停止这次转换**（`it displays an error and stops the conversion`） |
| `1` | `STPM may overwrite existing files and directories.` | **可以覆盖文件与目录** |

**两处要注意**：

1. **默认值 `0`，而语法行里它又是「可选」的**——**所以「不写」和「写 0」是同一件事**
   （原文：`If it is omitted, no files or directories are overwritten.`）。
2. **`0` 那一条是「可能报错」而不是「必然报错」**：原文写的是
   `If this prevents STPM from saving a created file` ——**先有冲突、才有错**。
   **原文没有说这条错误长什么样**（**本篇没有 `## Errors` 段**）。

### `copy_static_content`：三条限制 + 一条警告

原文（逐字）：

> 「`<copy_items>` (list of strings) is a list of names of files or directories that are to be copied from the existing device directory to the TPT directory.」

**清单本身就带三条限制**（同一格里，逐字）：

- `The list may contain only names (of files or directories), not paths.` ——**只写名字，不写路径**
- `The named items must be located in the top level of the device directory.` ——**必须在 device 目录的顶层**
- `Each name is enclosed in quotes and separated by commas.` ——**各自加引号、逗号分隔**

**原文给了一个例子**（逐字）：`copy_static_content = ['my_notes.txt','Change log']`
——**注意第二个名字里有空格（`Change log`），靠引号界定。**

**一条警告规则**（逐字）：

> 「If you include standard directories in this list (testflow, timing, levels, configuration, vectors, testtable), STPM generates a warning and does not copy the contents.」

**条件 → 结果**：**列了这六个标准目录中的任何一个** →
**STPM 发一条警告，并且不拷它的内容。**
**六个标准目录的名字照原文列出**：`testflow`、`timing`、`levels`、`configuration`、`vectors`、`testtable`。
**注意「不拷内容」与「不拷目录」的差别**：原文写的是 `does not copy the contents`
——**（推断）目录本身可能在，里面空着；依据只是 `contents` 这个词，原文没有再解释。**

**这一格的最后一句是把两条命令接起来的那条线**（逐字，语法节里带 raw 路径）：

> 「Any directories that are copied by means of this command will be included in the device directory generated with `tpt_generate_device_dir`」

**即：这里搬进 TPT 的目录，会在 [[tpt-generate-device-dir]] 那一步被带进新生成的 device directory。**
**交接点就是这句话**——**本页只管「搬进 TPT」，那一页管「从 TPT 再进 device directory」。**

### 通配符：`?` 与 `*`，但定义写在后面那一格里

**两个参数都能用通配符，而定义只在 `empty_groups` 那一格**——
**`include_groups` 那一格只给了一句指路**（逐字）：

> `include_groups` 格：`You can use the ? and * wildcard characters in the group name strings. (See empty_groups, below, for details.)`
> `empty_groups` 格：`You can use the ? and * wildcard characters in the group name strings; ? matches any single character and * matches zero or more characters.`

**完整的语义在 `empty_groups` 格里**（**因为它在参数表里排得靠后，所以是「向下看」**）：

| 通配符 | 原文 | 匹配 |
|---|---|---|
| `?` | `? matches any single character` | **任意一个字符** |
| `*` | `* matches zero or more characters` | **零个或多个字符** |

**原文给的两个例子（逐字）**：

- `For example, to empty all groups, you would specify empty_groups = '*'`
- `To empty the group temp1 and all groups with the name "test" followed by a single character, you would specify empty_groups = 'temp1', 'test?'`

**⚠️ 第二个例子里没有方括号**，而同一格上一段刚说过
`the list is enclosed in square brackets`（见 `## 出处`）。

### `empty_groups`：搬结构、不搬内容

原文（逐字）：

> 「An empty group is transferred to the test program template, but none of the test suites it contains are transferred. Empty groups are useful to preserve the structure of the testflow. They can be filled with new test suites later.」

| 这个 group | 会不会进 TPT（**原文**） |
|---|---|
| **group 本身** | ✅ `is transferred to the test program template` |
| **它里面的 test suites** | ❌ `none of the test suites it contains are transferred` |

**目的也是原文写的**：`useful to preserve the structure of the testflow` ——**保住结构**；
**后面可以再往里填新的 test suite**（`They can be filled with new test suites later.`）。

**`include_groups` 那一格给的是同一件事的另一半**（逐字）：
`<include_groups> (list of strings) is a list of groups in the specified testflow that are to be imported.`
——**一个决定「哪些进来」，一个决定「哪些进来但不带内容」**。
**⚠️ 两者的优先级：原文没有写。**（**如果同一个 group 同时出现在两个清单里会怎样，本篇一个字都没有**——
**本页不替它编。**）

### `pre_proc` / `post_proc`：包在这条命令外面

原文两句（逐字）：

> 「`<pre_proc>` is a script that is executed before this command.」
> 「`<post_proc>` is a script that is executed after this command.」

**两句的其余部分完全一样**（两个格子各重复一次）：
`The syntax of the parameter value is described in Preprocessing and postprocessing scripts.`
——**脚本语法不在本篇**，在 [[preprocessing-and-postprocessing-scripts]]
（raw：`02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）。
**本页没读那篇**，所以**脚本能干什么、返回值怎么用，本页不知道**。

## 典型用法

**原文没有 `## Procedure` 段，也没有 `## Before you begin` 段**——
**可依据的只有 `## Parameters` 里那一格硬前提、`## Example` 那一段说明加一段代码、
以及六条 `## Functional changes` 条目。** 下面这份顺序是**从原文还原**的。

**先满足前置**（**只有一条，且是逐字的**）：

| 前置 | 依据（**原文**） |
|---|---|
| **`tpt_dir` 不存在，或者存在且为空，或者你会写 `allow_overwrite = 1`** | `If the directory already exists, it must either be empty or the allow_overwrite parameter (see below) must be set to 1.` |
| **`copy_static_content` 里要搬的东西必须放在 device 目录顶层、且只写名字** | `The named items must be located in the top level of the device directory.` |

**然后是参数选择**（这张表是原文例子的逐参数对回去）：

| 你要的效果 | 参数 | 依据 |
|---|---|---|
| 指定从哪个 testflow 生成 | `device_test_flow = 'testflow/my_testflow'` | 必填格 |
| 指定 TPT 落在哪 | `tpt_dir = '../new_template'` | 必填格 |
| 只要一部分 group | `include_groups = [...]` | `a list of groups in the specified testflow that are to be imported` |
| 要 group 的壳、不要里面的 test suite | `empty_groups = ['init_group', 'final_group']` | `An empty group is transferred … none of the test suites it contains are transferred.` |
| 要从 device 目录搬几个静态文件/目录过去 | `copy_static_content = ['temp']` | `names of files or directories that are to be copied from the existing device directory to the TPT directory` |
| 目标目录非空、且你要覆盖 | `allow_overwrite = 1` | `STPM may overwrite existing files and directories.` |
| 命令前后各挂一段脚本 | `pre_proc` / `post_proc` | 那两格 |

**原文的完整例子（逐字，含它上面的说明句）**：

> 「This example converts the testflow "my_testflow" (located in the "testflow" subdirectory of the current working directory) into a test program template in the directory "new_template", which is located at the same level as the current working directory. It copies all groups, empties the groups "init_group" and "final_group", copies the temp subdirectory to the TPT directory, and overwrites any existing files in the TPT directory.」

```
tpt_import_from_device(
    device_test_flow    = 'testflow/my_testflow',
    tpt_dir             = '../new_template',
    empty_groups        = ['init_group', 'final_group'],
    copy_static_content = ['temp'],
    allow_overwrite     = 1
    )
```

**例子与说明句的三处对应**（**本页比对出来，原文没有逐条点**）：

| 说明句里的说法 | 代码里的落点 |
|---|---|
| `converts the testflow "my_testflow" (located in the "testflow" subdirectory of the current working directory)` | `device_test_flow = 'testflow/my_testflow'`（**相对路径，基准是 current working directory**） |
| `in the directory "new_template", which is located at the same level as the current working directory` | `tpt_dir = '../new_template'`（**`../` 正是「与当前工作目录同级」**） |
| `It copies all groups` | **`include_groups` 没写**——**正对上「省略即全部」** |
| `empties the groups "init_group" and "final_group"` | `empty_groups = ['init_group', 'final_group']` |
| `copies the temp subdirectory to the TPT directory` | `copy_static_content = ['temp']` |
| `overwrites any existing files in the TPT directory` | `allow_overwrite = 1` |

**照抄时注意三处**（**都在上面那段代码里**）：
① **参数名与 `=` 之间、`=` 与值之间都有空格**，而且**前两个参数的 `=` 是对齐过的**
（`device_test_flow    =` / `tpt_dir             =`），**后三个没有对齐**——**原文如此**；
② **值用单引号**（字符串与列表元素都是）；
③ **最后一个参数 `allow_overwrite = 1` 后面没有逗号，而前面的参数都有**——
**原文如此**（见 `## 出处`）。

**没有的东西**：本篇**没有 `## Errors` 段、没有 `## Warnings` 段、没有 `## Limits` 段、
没有 `## Application` 段**——**所以「哪一步会怎么报错」只有正文里那两处偶发的句子
（`it displays an error and stops the conversion`、`STPM generates a warning and does not copy the contents`），
**没有错误码、没有错误文本模板。**

## 和谁有关

- [[stpm-control-file]] — **上游，本命令的宿主**。原文第一句就说它是
  `the … command for the SmarTest Program Manager (STPM) control file`，
  **而那三个词是原文里的一个链接**（raw：`02.09.02.03_STPM_control_file.md`）。
  **本页没读那一篇**：**控制文件里这几条 tpt_* 命令怎么写、能不能混用、执行顺序谁定，本页不知道。**
- [[stpm]] — **执行者**。原文两处把动作派给它：`STPM creates the files that make up a test
  program template`、`STPM generates a warning`、`STPM may overwrite existing files`。
  **本页只有这个缩写的一个展开**（`SmarTest Program Manager`）**和它做的三件事**；
  **STPM 本身是什么、怎么起，在那一页。**
- [[tpt-generate-device-dir]] — **反向的那一条命令，也是本页的下游**。
  交接点逐字写在本页 `copy_static_content` 那一格里：
  `Any directories that are copied by means of this command will be included in the device
  directory generated with tpt_generate_device_dir`。
  **即：本命令搬进 TPT 的静态目录，会被那一条命令带进新 device directory。**
  **两句的范围要说清：本页负责「搬进 TPT」，那一页负责「从 TPT 进 device directory」。**
  **两页各自成篇、互为反向，没有把两条命令合成一页。**
- [[stpm-merge-rules-file]] — **同族的文件操作，但明确不构成依赖**。
  **本页的 `## 是什么` 里没有这个文件**，**这一条只是「都在 STPM 的文件操作这一族里」**。
  **判断依据转自 [[stpm-merge-rules-file]] 那页的自述（不是本页 sources 的内容）**：
  那页写它**与本页「没有链接关系，只列为同族的文件操作页」**。
  **本页没有读它，也不声称任何先后关系。**
- [[device-directory]] — **输入侧的那个目录**。原文两处点它：
  `from an existing device directory`、`copied from the existing device directory to the TPT directory`；
  而且 `copy_static_content` 的限制句说**只取顶层**（`must be located in the top level of the device directory`）。
  **device 目录本身的结构在那一页，本页只有「顶层」这个条件。**
- [[testflow-file]] — **`device_test_flow` 指的实体**。原文称它是
  `the path of the testflow file from which the test program template is to be generated`。
  **本页没有那页的任何事实**（testflow file 长什么样、里面有什么，都不在本页）。
- [[group-node]] — **（推断）group 的宿主页**。本命令有两个参数按 group 名选东西
  （`include_groups` / `empty_groups`），**而 group 在 testflow 里是什么结构，
  本页一个字都没有**；**依据只是那一页的名字（`group-node`）**。**本页没读它。**
- [[test-suite]] — **`empty_groups` 要丢掉的那一层**。原文说的是
  `none of the test suites it contains are transferred`——
  **test suite 是什么、怎么被 group 装起来，在那一页，本页没有。**
- [[testflow]] — **stage 页**。本命令作用于 testflow 的**结构**（group 的取舍与清空），
  **流程面的说明在 [[testflow]] 那一页，本页不写流程。**
- [[preprocessing-and-postprocessing-scripts]] — **`pre_proc` / `post_proc` 的语法出处**。
  原文两个格子各写了一次 `The syntax of the parameter value is described in …`。
  **本页没读那篇**，所以脚本怎么写、能不能拿到命令的输入输出，本页不知道。
- [[mapping-project]] / [[project]] — **本页的 `stage: project`（最近的一段）所指**。
  **§6：`stage` 填的是「读者该去哪一段找它的用法」，不是「归属」**——
  **本命令属于 L3 的外部控制（`layer: L3`），它建的是工程结构，所以最近的一段是 project。**
- [[smartest-7.0.4]] / [[smartest-7.2.1]] / [[smartest-7.2.2]] — **版本页**，
  本页 `## 版本` 里六条条目的落点。
- `02.09.02.03_STPM_control_file.md`（**raw 路径**）— 原文第一句那个链接的目标。
  **本页没读**（见上）。
- `testtable` / `vectors` / `configuration` / `levels` / `timing` / `testflow`（**六个标准目录名**）——
  **原文只在 `copy_static_content` 那一格把它们列出来**，**没有说它们各自装什么**。
  **本页照抄那六个名字，不做解释。**

## 版本

本文档**有** `## Functional changes` 段，**六条**（**逐字**，含语料自己的序号写法）：

- **Introduced in SmarTest 7.0.4**
- **SmarTest 7.2.1: Added support for wildcard characters to empty_groups.**
- **SmarTest 7.2.1: Added the copy_static_content, allow_overwrite, and include_groups parameters.**
- **SmarTest 7.2.1: Removed the tpt_name parameter.**
- **SmarTest 7.2.1: Renamed command to tpt_import_from_device.**
- **SmarTest 7.2.2: Added the pre_proc and post_proc parameters.**

**这六条能读出四件事**（**每一条都直接写在条目里，不是本页猜的**）：

| 读出的 | 依据（**逐字**） |
|---|---|
| **本命令 7.0.4 就有，7.2.1 大改，7.2.2 又加两个参数** | 三条不同版本的条目 |
| **7.2.1 之前它叫别的名字** | `Renamed command to tpt_import_from_device.` ——**旧名是什么，原文没有写** |
| **`tpt_name` 这个参数 7.2.1 被删了** | `Removed the tpt_name parameter.` ——**本篇正文里没有 `tpt_name` 的任何说明，它长什么样、替代它的是什么，语料里没有** |
| **通配符与三个参数是同一版加的** | 两条 `SmarTest 7.2.1:` 条目 |

**⚠️ 第一条不是 §11.2 ② 那个哨兵**（哨兵写 `Introduced before SmarTest 6.3.2`）——
**`Introduced in SmarTest 7.0.4` 是常规引入条目。**

**与 wiki 面向版本的关系**：本 wiki 面向 **SmarTest 7.10.3**，
**7.0.4 / 7.2.1 / 7.2.2 都早于 7.10.3**——**按文档的说法，本页写的这套参数（八个）在 7.10.3 上
是齐全的**（**依据是「7.2.2 加了最后两个」这一条，而 7.2.2 < 7.10.3**）。
**注意 §11**：这只说明**文档这么写**，**不说明某台机台上装的是这个版本、也不说明它在机台上验过**
（本页 `verified: doc-only`）。

## 出处

`sources:` 一篇：
`02_System_reference/02.09_Test_Program_Management/02.09.02.03.15_tpt_import_from_device.md`

**本页没做的：**

- **只读了这一篇。** 原文里的三个链接目标**一个都没读**：
  `02.09.02.03_STPM_control_file.md`（[[stpm-control-file]]）、
  `02.09.02.03.16_tpt_generate_device_dir.md`（[[tpt-generate-device-dir]]）、
  `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`
  （[[preprocessing-and-postprocessing-scripts]]）。
  **所以：控制文件怎么写、反向那条命令的十个参数是什么、脚本怎么挂，本页一个字都没有。**
- **产出物没有看过一眼**：**TPT 里到底有哪些文件、目录层级什么样，本篇只说
  `the files that make up a test program template`，没有列清单**——
  **本页给不出 TPT 的目录树。**
- **`tpt_name` 没查**：它是 7.2.1 被删掉的参数，**本篇正文里没有它的任何说明**
  （**删除条目本身是逐字的，但那个参数是什么，语料里没有**）。
- **两个清单冲突时的行为没查**：**同一个 group 既在 `include_groups` 又在 `empty_groups` 里
  会怎样，原文没有写**，本页也没有别的地方可查。
- **错误与警告的文本没查**：本篇**没有 `## Errors` / `## Warnings` 段**；
  正文里只偶发地提到 `it displays an error and stops the conversion`
  与 `STPM generates a warning and does not copy the contents`。
  **所以错误码、错误文本、警告显示在哪，本页和原文一样没有。**
- **没有查过 `testtable` 等六个标准目录各自装什么**（见 `## 和谁有关` 最后一条）。
- **一张图都没看。** 本篇**没有图片引用**（`![` 0 处，本页核过）。
- **没有交叉验证任何别处的文档**（§11：本页只写这一篇里有的）。
  **尤其：本命令与 [[tpt-generate-device-dir]] 是「互为反向」这个说法，
  本页只依据 `copy_static_content` 那格里的一句交接句 + 两条命令名——
  原文没有一句话说它们是一对。**

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> **① 语法行里有三处多余/错位的方括号。** 语法节逐字：
> ```
> tpt_import_from_device(
> device_test_flow = <testflow_file>,
>     tpt_dir = <location>,
> [include_groups  = <include_groups>, ]
> [empty_groups = <empty_groups>, ]
> [copy_static_content = <copy_items>], ]
> [allow_overwrite = <overwrite_flag>, ]
> ```
> ——**可选参数都用 `[ … ]` 括起来，可 `copy_static_content` 那一行结尾多出一个 `], ]`**
> （方括号闭合了两次）；**而 `include_groups` / `empty_groups` / `allow_overwrite`
> 三行是 `, ]`（逗号在方括号里面）**，**与 `copy_static_content` 那行的写法不一致**。
> **同一段语法里两种写法并存。本页照原样引，不替它统一。**
>
> **② 首行参数没有缩进，其余参数都缩进四格。** 逐字：
> `tpt_import_from_device(` 的下一行是 `device_test_flow = <testflow_file>,`（**顶格**），
> 而 `tpt_dir` 起都是**四格缩进**；**例子的收尾 `)` 也是四格缩进**（`    )`）。
> **本页照原样引。**
>
> **③ 两个格式不一致的写法：`include_groups  = ` 有两个空格。** 逐字：
> `[include_groups  = <include_groups>, ]`（**参数名与 `=` 之间两个空格**），
> 而同一段里其它行都是一个空格。**例子里 `device_test_flow    = ` / `tpt_dir             = `
> 又是对齐用的多空格**——**三处空格数各不相同，原文如此。**
>
> **④ `## Parameters` 那张表没有表头行。** 语法节里逐字可见：表的第一行是孤立的 `|`，
> 紧接着就是 `device_test_flow`——**没有 `Parameter` / `Description/Range` 之类的表头**
> （**对比：同一章的其它篇有表头，只是写重复了**）。
> **本页照实说，不替它补表头。**
>
> **⑤ `empty_groups` 那两个例子里没有方括号，而同一格上一段刚说「列表要用方括号括起来」。**
> 逐字并列：
> `Each group name is a string enclosed in single or double quotes; groups are separated by commas, and the list is enclosed in square brackets.`
> 与 `to empty all groups, you would specify empty_groups = '*'`、
> `you would specify empty_groups = 'temp1', 'test?'`
> ——**两个例子的右边都不是方括号列表**（第二个甚至连外层引号都没有，两个单引号串直接并列）。
> **原文没有说明这是简写还是另一种合法写法。本页照原样引，不替它补方括号。**
>
> **⑥ 例子里最后一个参数后面没有逗号。** 逐字：
> ```
>     copy_static_content = ['temp'],
>     allow_overwrite     = 1
>     )
> ```
> ——**`allow_overwrite = 1` 与 `)` 之间没有逗号**，而它前面的每一个参数都有。
> **原文如此，本页不替它补。**
>
> **⑦ `## Parameters` 的前两格没有「optional」那句话，而后面六格都有。**
> 前两格（`device_test_flow` / `tpt_dir`）**结尾是路径规则句**；
> 后六格结尾分别是 `This parameter is optional.…` / `This is an optional parameter.`。
> **「哪个必填」这件事原文没有用一句话说，只能从这两处的缺席读出来**——
> **本页在 `## 是什么` 那张表里就是这么读的，标明了读法。**
>
> **⑧ 命令名全篇小写带下划线，而本篇 `title` 也是这个形态**（`tpt_import_from_device`）——
> **不是大写命令（如 `DFPN`）那种写法**。**本页照原样。**
>
> **⑨ 本篇没有 §11.2 ① 那种编码损坏。** 本页查过：**全文没有汉字，也没有 `鈥`**
> （`[一-鿿]` 与 `鈥` 均 0 命中）。

`verified: doc-only`
