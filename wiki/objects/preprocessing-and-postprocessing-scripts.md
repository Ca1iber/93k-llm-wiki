---
type: object
title: Preprocessing and postprocessing scripts
layer: file
stage: project
tags: []
related: []
sources:
  - 02_System_reference/02.09_Test_Program_Management/02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# Preprocessing and postprocessing scripts

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,438 字符逐字取自** `<02_System_reference/02.09_Test_Program_Management/02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

Both the pre_proc (shown below) and post_proc parameters have the same syntax.

```
pre_proc = '<script>[&mdir][&sdir][&mtp_tf][&mtp_pmf][&mtp_conf][&mtp_tim][&mtp_lev][&mtp_tt][&mtp_rout][&mtp_wf][&mtp_anctrl][&mtp_chatt][&mtp_prot][&mtp_att][&stp_tf][&stp_pmf][&stp_conf][&stp_tim][&stp_lev][&stp_tt][&stp_rout][&stp_wf][&stp_anctrl][&stp_chatt][&stp_prot][&stp_att][<user_parameters>]'
```

The available script parameters in the order in which they are listed above:

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/143913.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：28 行 × 2 列。
> 首行（上游原文）：<script> | The name and path of the script file to call. The path can be absolute or relative. If it is a relative path, the base directory is the current worki…

Except for the name of the script file, all elements are optional.

### Example

This example executes the write_tp command with two scripts:

- Before write_tp itself is executed, the preparation.py script from the current working directory is run. No parameters are passed to this script.
- After write_tp has finished executing, the cleanup.pl script is run. This script receives this parameter string (assuming that the MTP is located in /user/johndoe/mtp):

`--mdir '/user/johndoe/mtp' --cmd write --stage 3`

```
write_tp('user/johndoe/mtp/flow1.tf',
         pre_proc  = 'preparation.py',
         post_proc = '/usr/tools/scripts/cleanup.pl &mdir --cmd write --stage 3')
```

<!-- 语法节 end -->

## 是什么

**这是 STPM 控制文件的一个参数机制**，不是一条独立命令。原文：

> 「The commands in the STPM control file allow preprocessing and postprocessing scripts to be
> specified that are **automatically run, respectively, before or after the command itself
> is executed**. This is done via the **`pre_proc`** and **`post_proc`** parameters.」

**两个参数：**

| 参数 | 什么时候跑 |
|---|---|
| **`pre_proc`** | **命令自己执行之前** |
| **`post_proc`** | **命令自己执行之后** |

**两者语法完全一样**（原文：`Both the pre_proc … and post_proc parameters have the same syntax.`），
所以下面的规则**同时适用于两个**。

### 参数是怎么变成命令行实参的：`&xxx` → `--xxx`

这是本页最该记住的一条**改写规则**：

> 「Each **system parameter starts with a `&`** and is replaced for the execution of the script
> with **a similar parameter prefixed with a double dash (`--`)** and the corresponding value.」

**原文举的例子**：在 `pre_proc` 的值里写 `&mdir`，
脚本被调用时会收到 **`--mdir '/user/johndoe/mtp'`**
（假设 `/user/johndoe/mtp` 就是当前 MTP 目录）。

**26 个系统参数**，每个就干一件事——**把一个路径原样递给你**：
`&mdir` / `&sdir`（MTP 目录 / STP 目录），
然后 **`&mtp_*` 十二个**（testflow / pattern master / configuration / timing / levels /
test table / routing / waveform / analog control / channel attributes / protocols / pin attributes），
再 **`&stp_*` 十二个**（**同名的一套**，只是换成 STP 那边）。
**完整清单和逐个说明在上面语法节的表里**（脚本逐字抽的），本节不重复。

### 自定义参数：加在最后，且不能以 `&` 开头

> 「You can also add **any number of custom parameters at the end** of the parameter list that are
> **passed unchanged** to the script. **These script parameter names must not begin with a `&`.**」

**这条限制的用意是明摆着的**：`&` 是系统参数的记号，你用了就会被当成系统参数去改写。
原文在语法节的 `<user_parameters>` 一行里又说了一遍：
`This text must not contain any words that begin with &.`

### 剩下的三条

1. **脚本是什么都行**：`Any script can be specified that is executable on the computer on which
   STPM is running.`
2. **出问题算你的**：原文说 **`The operator is responsible for`**
   ① 保证脚本要的支撑**在机器上装好了**（例如脚本语言的解释器），
   ② 保证**脚本能处理传给它的那些参数**。
3. **除了脚本名，其余全是可选的**
   （`Except for the name of the script file, all elements are optional.`）。

## 典型用法

**1. 怎么读那个 `pre_proc` / `post_proc` 的值**：把它当成**一个命令行**读——
**第一个词是脚本，后面全是实参**。`<script>` 的路径**可以是绝对也可以是相对**；
**相对路径的基准目录是「STPM 被调用那一刻的当前工作目录」**
（原文：`the current working directory at the time STPM was called`）——
**不是脚本所在目录，也不是 MTP 目录**。这一条最容易踩。

**2. 原文那个例子**：

```python
write_tp('user/johndoe/mtp/flow1.tf',
         pre_proc  = 'preparation.py',
         post_proc = '/usr/tools/scripts/cleanup.pl &mdir --cmd write --stage 3')
```

**拆开看，两个脚本的待遇完全不同：**

| | 脚本 | 收到的实参 |
|---|---|---|
| `pre_proc` | `preparation.py`（**相对路径**，从 cwd 起） | **没有**（原文：`No parameters are passed to this script.`） |
| `post_proc` | `/usr/tools/scripts/cleanup.pl`（**绝对路径**） | **`--mdir '/user/johndoe/mtp' --cmd write --stage 3`** |

**注意 `post_proc` 那一串是怎么拼出来的**：
`&mdir` 被**展开成** `--mdir '/user/johndoe/mtp'`（**带引号**），
而 `--cmd write --stage 3` 是**两个自定义参数**，
**原样传过去、一个字母都没动**（`--cmd` 和 `--stage` 不以 `&` 开头）。

**3. 什么时候用它**：STPM 命令执行前后要挂一段自己的处理
（准备输入、清理产物）时。**本页不知道 STPM 有哪些命令**——见「出处」。

## 和谁有关

- [[stpm-control-file ]] — `pre_proc` / `post_proc` 是**它的参数**；
  原文 `Related information` 里**只列了这一篇**
- [[mtpt]]、[[gpib-lan-communication-conventions]] — 同属
  `02.09_Test_Program_Management` 这一章，同批建页
- [[project]] — 本页 `stage: project` 的理由：STPM 是**测试程序管理**工具，
  不落在九个工艺阶段的任何一个上
- **`layer: file` 的理由**：这两个参数的落脚点是**控制文件里的字段**，
  写错的地方是文件，不是某段代码

## 版本

- **Introduced in SmarTest 7.2.2**

## 出处

`sources:` 一篇：
`02_System_reference/02.09_Test_Program_Management/02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`

**本页没做的**：

- **`write_tp` 这条命令本身，本页一个字都没有。** 它只是原文挑来举例的命令；
  **它有哪些参数、干什么，请看它的专页**。
- **`STPM control file` 这一篇本页没读**（原文 `Related information` 只列了它）。
  所以**「STPM 有哪些命令」「pre_proc / post_proc 能不能挂在这条命令上」本页不知道**。
- **26 个 `&` 参数里，本页正文只点名了 `&mdir` / `&sdir` / `&mtp_*` / `&stp_*` 四类**，
  逐个说明**只在上面语法节的表里**——**那一节是脚本逐字抽的，本页不重复**。
- **示例只抄了原文的那一个**；原文没有别的例子。
- **`02.09_Test_Program_Management` 底下其余篇本页没读。**

> ⚠️ **原文示例里的路径不一致，本页照抄没改**：
> 例子里写的是 `write_tp('user/johndoe/mtp/flow1.tf', …)`——
> **`user/johndoe/…` 没有开头的斜杠**（相对路径），
> 而同一段的说明文字和 `post_proc` 里写的都是 **`/user/johndoe/mtp`**（绝对路径）。
> **本页不知道这是有意还是笔误**，两个形态都照抄了。

`verified: doc-only`
