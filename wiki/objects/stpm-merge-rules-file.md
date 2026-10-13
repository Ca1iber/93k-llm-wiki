---
type: object
title: STPM merge rules file
layer: file
stage: project
tags: [stpm, merge-rules, file-format, test-program-management, mtp, stp, tpt, project]
related: [stpm, stpm-control-file, preprocessing-and-postprocessing-scripts, project, testflow-file, device-directory, tpt-generate-device-dir, tpt-import-from-device]
sources:
  - 02_System_reference/02.09_Test_Program_Management/02.09.02.04_STPM_merge_rules_file.md
  # ⚠️ 2026-09-20 补：本页「语法 / 参数」节那 5,959 字符**逐字取自子主题**，
  # 原先只列了定义文档——**于是本页最重的那一节没有 `sources:`**
  # （正文的「出处」节早就写明了两篇，**frontmatter 和正文对不上**）。
  # **为什么不降级成转述**：§4 说语法/参数表由脚本抽、不许 LLM 重写；
  # §11 说改写参数表就是把文档事实降级成我的转述。**降级才是错的。**
  - 02_System_reference/02.09_Test_Program_Management/02.09.02.04.01_STPM_merge_rules_file_syntax.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

> ⚠️ **本页若干处记的是 2026-10-10【之前】的语料形态。**
> 那一轮把语料里的表格一律换成了**指向上游 HTML 的指针**
> （见 `extract/PLAN-表格指针化.md`）。所以下文凡是说「表格被压平 / 被摊平 /
> 一格一行」的地方，指的是**更换之前**的样子 —— 现在语料里那个位置是**一句指针**，
> 真表仍在 `tdc-html/raw/` 的上游 HTML 里。**页码/引文都不受影响。**

# STPM merge rules file

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **3,059 字符逐字取自** `<02_System_reference/02.09_Test_Program_Management/02.09.02.04_STPM_merge_rules_file.md>` 及其子主题 `<02_System_reference/02.09_Test_Program_Management/02.09.02.04.01_STPM_merge_rules_file_syntax.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### STPM merge rules file syntax（整篇，取自子主题）

# STPM merge rules file syntax

The STPM merge rules file contains a range of flags that specify the details of how SmarTest Program Manager (STPM) integrates source test programs (STPs) into the master test program (MTP).

Each flag instructs STPM what to do if a certain kind of action would be needed in the course of merging test programs. For example, the new_digital_pin flag lets you tell STPM to not add new pins at all or to add them while generating a warning message in the log.

The merge rules file to use is specified in the `STPM Setup File`（raw: `02.09.02.03_STPM_control_file.md`）. If no merge rules file is specified, default settings are assumed for all rules (as listed below).

The order of the rules is not important. No rule must appear more than once.

## Syntax

The merge rules file contains a range of flags, which can be set to allow, reject, or ignore. Not all options are available for all flags.

The three settings usually have the same general effect:

- allow: STPM performs the merger and automatically resolves any conflicts that may occur. This automatic resolution may have side effects, such as when pin numbers change.
- ignore: STPM performs the merger but does not resolve any conflicts that may occur. If the rule was triggered, you will usually need to manually resolve the issues in the target file (processed MTP).
- reject: STPM aborts the merger with an error without changing the MTP. You will have to manually resolve the issue in the source files (STP and/or original MTP).

This table lists the available flags and their supported settings. For details on the effect of each flag, see the pages describing the individual flags.

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/131150.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：34 行 × 5 列。
> 首行（上游原文）：Flag | Available settings | Default

## Example

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

<!-- 语法节 end -->

## 是什么

**一句话：merge rules file 是 STPM 的两份输入之一（另一份是 [[stpm-control-file]]），它逐条回答「合并时遇到这种情况该怎么办」。** 原文第一句（**⚠️ 原文如此，`test` 少一个 `s`，见「出处」①**）：

> 「The merge rules file of the SmarTest Program Manager (STPM) lets you fine-tune how test are integrated into existing master test programs (MTP).」

**三个名词在本篇里各有各的待遇**：`SmarTest Program Manager` 与 `master test programs` 都给了展开（STPM / MTP）；**第三个 `STP`（source test program）本篇一次都没有出现**——它只在本页「语法 / 参数」节的子主题文本里（见「出处」）。

**这份文件的定位是「可换的松紧度」**，原文给的场景是：

> 「For example, you may have more permissive rules early on the test program development process to allow for rapid changes and more restrictive ones later to protect well-debugged programs.」

### 谁决定用哪一份

> 「Which merge rules file is used in a merge process is specified in the STPM control file, enabling you to easily prepare and use different merge rule file, for example, for different stages of the development process.」

**（推断）一个 STPM control file 只点名一份 merge rules file**——依据是 `Which merge rules file` 这个单数句式；**要换规则就换文件**，而原文给的理由正是 `for example, for different stages of the development process`。

⚠️ **同一件事，另一篇文档里的叫法不一样**：本页「语法 / 参数」节里那段取自子主题的文字说的是 **`STPM Setup File`**（它链向的文件却是 `02.09.02.03_STPM_control_file.md`），而**定义文档这一句说的是 `STPM control file`**。**同一个文件两个名字，本页并列，不替它统一**（见「出处」⚠️ ⑦）。

### 它是可选的

> 「Merge rule files are optional; if you Do not specify a merge rules file, a default set of rules is used. (See the descriptions of the individual merge rule options for information on the defaults.)」

**「不写也有默认」有两个后果**（推断，依据就是这句话本身）：

- **不指定文件 ≠ 没有规则**——跑的是默认档。
- **默认值写在哪儿，本篇没有列**：原文只说 `See the descriptions of the individual merge rule options`，**把默认值散到了 28 个 flag 各自的页里**。

### 文件里有什么：28 个 flag + 1 篇 syntax

**定义文档自己没有语法段**（本页实测：**定义文档里 `## Syntax` 0 个**——本页「语法 / 参数」节里那个 `## Syntax` 是子主题的文本）。它给的是一张 29 条的 `#### Subtopics` 清单：

- 第 1 条是 `STPM merge rules file syntax`；
- 其余 28 条，**每一条是一个 flag 的名字**。

**这 28 个名字，原文一个字的解释都没有**——**每个 flag 干什么，得点进它自己那一页。**

**28 个 flag 分成四组**（分组与下面的取值 / 默认值都逐行读自本页「语法 / 参数」节里那张可用设置表——**那一节是子主题 `02.09.02.04.01` 的文本，本页没有打开那一篇**，见「出处」）：

| 组 | 条数 | flag |
|---|---|---|
| Pin, port, and site rules | 12 | `new_digital_pin` / `overwrite_digital_pin_no` / `merge_digital_pin_dir` / `new_dps_pin` / `overwrite_dps_pin_polarity` / `new_pin_group` / `overwrite_pin_group` / `merge_unused_pin_group` / `new_port` / `overwrite_port` / `new_site` / `overwrite_channel` |
| Timing and levels rules | 14 | `new_timing_equation_set` / `new_waveform` / `modify_waveform_index` / `overwrite_statemap` / `new_level_resource` / `overwrite_level_resource` / `new_level_equation_set` / `new_level_set` / `new_ac_specset` / `new_dc_specset` / `overwrite_ac_spec_typ` / `overwrite_ac_spec_minmax` / `overwrite_dc_spec_typ` / `overwrite_dc_spec_minmax` |
| Pattern rules | 1 | `overwrite_label_wvt` |
| Testflow rules | 1 | `overwrite_flow_var_value` |

**分组的名字本身就说明了它的粒度**：**pin / port / site、timing 与 levels、pattern、testflow**——四块正好是 STPM 合并时会碰到的四类对象。

### 一个 flag 能取三种值：`allow` / `ignore` / `reject`

原文先说了一句限制：

> 「The three settings usually have the same general effect:」

（**`usually` 是原文的用词**——**它自己承认有例外**，而例外是哪些，本篇没有列。）**三种设置的后果差别很大**：

| 设置 | STPM 做什么 | 出事了修哪儿 | 原文 |
|---|---|---|---|
| `allow` | 执行合并，**并自动解决冲突** | 不用修；**但自动解决有副作用**（原文举的例是 pin 号被改） | 「STPM performs the merger and automatically resolves any conflicts that may occur. This automatic resolution may have side effects, such as when pin numbers change.」 |
| `ignore` | 执行合并，**但不解决冲突** | **目标文件（processed MTP）** 里手动修 | 「STPM performs the merger but does not resolve any conflicts that may occur. If the rule was triggered, you will usually need to manually resolve the issues in the target file (processed MTP).」 |
| `reject` | **中止合并、报错、MTP 一个字节不改** | **源文件（STP 和/或原 MTP）** 里修 | 「STPM aborts the merger with an error without changing the MTP. You will have to manually resolve the issue in the source files (STP and/or original MTP).」 |

**这张表就是这份文件的全部语义**：**`allow` 是「替你决定」，`ignore` 是「先合了再说」，`reject` 是「不许动」。**

**而且不是每个 flag 都三样齐**：

> 「The merge rules file contains a range of flags, which can be set to allow, reject, or ignore. Not all options are available for all flags.」

**按本页「语法 / 参数」节那张表逐行数**（28 行）：

| 设置 | 支持它的 flag 数 |
|---|---|
| `allow` | **28 / 28**（每个 flag 都支持） |
| `reject` | **26 / 28**（不支持的是 `merge_unused_pin_group` 与 `overwrite_label_wvt`） |
| `ignore` | **16 / 28** |

**`allow` 是唯一「哪个 flag 都能用」的设置**——这一条决定了下面的默认值那一节。

### 默认值偏松

**同一张表还有一列 `Default`，逐行数出来是**：

| 默认 | 条数 | 哪些 flag |
|---|---|---|
| `allow` | 16 | 其余 16 条 |
| `ignore` | 6 | `overwrite_digital_pin_no` / `overwrite_dps_pin_polarity` / `overwrite_pin_group` / `overwrite_channel` / `overwrite_statemap` / `overwrite_level_resource` |
| `reject` | 6 | `overwrite_port` / `overwrite_ac_spec_typ` / `overwrite_ac_spec_minmax` / `overwrite_dc_spec_typ` / `overwrite_dc_spec_minmax` / `overwrite_flow_var_value` |

**（推断）默认偏松是有道理的**——不指定文件时按默认跑，**如果默认是 `reject`，绝大多数合并第一次就会中止**；依据是上面三档的后果，加上 `Merge rule files are optional` 那一句。**这是本页的推断，不是原文的结论。**

**同一件事的另一面**：**默认是 `reject` 的那 6 条，不配文件就会中止合并**——**其中 5 条是 `overwrite_*` 的定时 / 电平 / 规格覆盖，1 条是 testflow 变量覆盖**（**（推断）这大概是「覆盖别人的值」这件事一律要人明确点头**，依据是这 6 条的名字都以 `overwrite_` 开头）。

### 两条写法上的硬规矩

> 「The order of the rules is not important. No rule must appear more than once.」

**规则顺序无所谓；但同一条不许出现两次。** **（推断）所以「先写默认、后面再覆盖」这种写法在本文件里没有依据**——依据就是这句 `No rule must appear more than once`；**要改就在那一行上改**。**原文没有说写重了会怎样**（报错？取后者？）——**语料未写**。

### 文件长什么样

本页「语法 / 参数」节的 `## Example` 给的是一份**把所有 28 个 flag 都写了一遍**的文件，形态是 `flag_name = 'setting'`、一 flag 一行：

```
new_digital_pin            = 'reject'
overwrite_digital_pin_no   = 'reject'
merge_digital_pin_dir      = 'reject'
```

（**完整的 28 行在本页「语法 / 参数」节，本页不重抄。**）原文对它的说明是：

> 「This example merge rules file sets all available options. Note that this is not necessary; if an option is missing, the default setting is used for it.」

**注意 `sets all available options` 里那个 `available`**——**这句话说的是「28 条都列出来了」，不是「每一条都能取它写的那个值」**（有一处对不上，见「出处」⚠️ ⑦）。

## 典型用法

**本篇没有 `## Procedure`、没有 `## Before you begin`、没有 `## What to do next`**，也没有 `## Related information`——**定义文档只有三段散文加两张清单**。**所以「怎么用」在本篇里只能排到「这份文件怎么被选中、里面怎么写」这两步**：

1. **先确认要不要它。** 不要 → **什么都不用写**，默认档生效（`Merge rule files are optional`）。
2. **要它 → 写一份文件，在 STPM control file 里点名它。** 原文明说点名的动作在那一边（`Which merge rules file is used in a merge process is specified in the STPM control file`），**字段叫什么名字本篇没写**——要去 [[stpm-control-file]] 看（**本页核过那一页的「语法 / 参数」节里确有 `[merge_rules = '<rules_file>']` 这一行**，那是同族页对齐，不是本页的原始依据）。
3. **逐条决定松紧。** 每条 flag 从 `allow` / `ignore` / `reject` 里挑一个**它支持的值**——**哪些值支持见本页「语法 / 参数」节那张表**。**挑错了会怎样，本篇没有写**（**语料未写**）。
4. **一条一行、不重复、顺序随意。** 原文这两句就是全部格式要求。
5. **跑完看哪儿？** **本篇没有说结果落在哪里**——没有 `## Related information`，也没有一句提日志或报告。**那一节只在子主题文本里出现过一次 `warning message in the log`，本页没有回到那篇复核。**

**一条用法上的取舍（推断，依据是那三档的后果表）**：**最省事的写法是「只在默认不合意的那几条上写」**——因为**不写的按默认跑**，而默认已经是 `allow` 的占 16/28。**原文没有这么建议**；本页只是把那两句（`if an option is missing, the default setting is used for it.` 与默认值表）并排读出来的。

## 和谁有关

- [[stpm]] — **本页的父页**：STPM 那张 7 条子主题的清单里，**第 4 条就是本页**（`STPM merge rules file`）。**那一页列了本页的存在，但不知道本页里有什么**（它自己的「本页没做的」里写着）。
- [[stpm-control-file]] — **配套的另一份输入，也是「谁选中本文件」的唯一地方**。两页的关系是**「规则表 ↔ 点名它的配置文件」**：**控制文件里那个字段叫什么、还能配什么，本页一个字没有**；**反过来本页这 28 个 flag 与三档取值，控制文件那页也没有**（它那份语法节里只有 `[merge_rules = '<rules_file>']` 一行）。**本页没有读它的 raw。**
- [[preprocessing-and-postprocessing-scripts]] — **在 [[stpm-control-file]] 的下级里**（它是那份控制文件的子主题之一），与本页是**同一个控制文件下的两个子主题**。**本页没读它**，所以「合并前后跑脚本」与「合并规则」会不会互相影响，**本页不主张**。
- [[project]] — **本页 `stage: project` 的归属阶段页**：STPM 干的事属于测试程序管理这一段。
- [[testflow-file]] — **（推断）合并的落点**：原文说 STPM 处理的是 `master test programs (MTP)`，**而本篇没有一处说 MTP 由哪些文件组成**。**这一条是按名字接的（推断）**，本页不主张内容关系。
- [[device-directory]] — **（推断）同上**：STPM 围绕 test program 工作，而 device directory 是 93K 测试程序的容器。**本篇没有一处提 device directory**（0 命中）。
- [[tpt-generate-device-dir]] / [[tpt-import-from-device]] — **在 [[stpm]] 第 5 条子主题（`Test program template files`）的下级里**；本页与它们**没有链接关系**，只列为**同族的文件操作页**。
- [[mtp-maintenance-operations]] / [[mtp-shared-test-commands]] — **只在名字上并排**（本页反复出现 `MTP` 这个词），**本篇没有一处链到它们，也没有提过 MTP 的维护操作**（0 命中）——**本页不主张关系。**
- `STPM merge rules file syntax`（`02.09.02.04.01`）— **本页 29 条子主题里的第 1 条**，也是**本页「语法 / 参数」节里那 5,959 字符文本的来源**。**allowlist 里没有它的页名，本页不链它**；**本页也没有打开那一篇**（见「出处」）。
- 28 个 flag 各自的页（`02.09.02.04.02` 到 `02.09.02.04.29`）— **本篇一个链接都没给它们**（`#### Subtopics` 那张清单里是纯文本，没有锚点）。**本页一篇没读。**
- `Introduction and installation` / `Using SmarTest Program Manager` / `Test program template files` / `STPM command line options` / `STPM UI plug-in`（**均未建**）— [[stpm]] 那张清单里与本页并列的其余子主题。

## 版本

`## Functional changes` 段**有，只有一条**：

> 「Introduced in SmarTest 7.0.4」

**这一条不是哨兵值**：它写的是 `in`，不是 `Introduced before SmarTest 6.3.2` 那种「本文档集覆盖之前就已经有了」的说法（schema §11.2 ②）。**所以「merge rules file 从 SmarTest 7.0.4 起可用」可以照字面用。**

**「只有一条」的后果要说清**：

- **28 个 flag 里，没有一个的引入 / 变更记录在本篇**——**要版本得进各自那一页**（本页没读）。
- **本页不知道三档取值的语义变过没有**（`allow` / `ignore` / `reject` 从头就在这里，**但这是本页的观察，原文没有一句这样说**）。
- **它没有说 7.0.4 之前 STPM 是怎么合并的**——**语料未写。**

## 出处

`sources:` 一篇：
`02_System_reference/02.09_Test_Program_Management/02.09.02.04_STPM_merge_rules_file.md`
（TDC `130563.htm`，2,961 字节，48 行）。**整篇读完。**
**实测：全语料里标题为 `STPM merge rules file` 的文档只有这一篇**（按 `title:` 扫 `by-category/` 下全部 md）——**没有第二处投放。**

**定义文档实际有什么**（这是本页可信度的要点）：

| 本篇有的 | 本篇没有的 |
|---|---|
| `#### Subtopics` 一张 29 条清单 | **`## Syntax`（定义文档里 0 个）** |
| 三段散文（用途 / 谁选中它 / 可选） | `## Procedure` / `## Before you begin` / `## What to do next` |
| `## Functional changes` 一条 | `## Related information` / `## Errors` / `## Warnings` |

**本页没做的**：

- **⚠️ 本页「语法 / 参数」节里那 5,959 字符的文本，绝大部分不属于本篇。** 脚本的段头自己写着它「逐字取自 `<02_System_reference/02.09_Test_Program_Management/02.09.02.04_STPM_merge_rules_file.md>` **及其子主题** `<02_System_reference/02.09_Test_Program_Management/02.09.02.04.01_STPM_merge_rules_file_syntax.md>`」，**并且那一节的段名带着「（整篇，取自子主题）」这个后缀**。
- **子主题 `02.09.02.04.01`（syntax）本页没有打开。** 本页正文里凡是用到「三档取值的语义」「28 个 flag 的分组 / 取值 / 默认值」「`## Example` 那份完整规则文件」的地方，**依据都是本页「语法 / 参数」节里已经逐字在的那段文本**；本页逐处标了来源，**但没有回到 `02.09.02.04.01` 的原文复核过**——**这是本页最重的一条限制**（⚠️ ⑦ 那处对不上就是它直接造成的）。
- **28 个 flag 各自的页（`02.09.02.04.02` 到 `02.09.02.04.29`）一篇没读。** 所以「每个 flag 到底在什么情况下触发」**本页一个字没有**——**本页只有名字、分组、可取的值、默认值。**
- **`STPM control file`（`02.09.02.03`）的 raw 没读。** 本页只核了 [[stpm-control-file]] 那一页 wiki 页的「语法 / 参数」节（用来确认它确实收 `merge_rules` 这个字段），**没有回原文**。
- **`STPM merge rules file syntax` 那篇 raw 没读**，见上。
- **图：本篇文档没有内嵌图片**，所以**本页没有 ④ 图证**。
  判据可核：本篇 md 里 `png` / `jpg` / `![` **0 命中**，
  其上游 `F:\master-dev\dorm-wsl-sytest\tdc-html\raw\130563.htm`（10,418 字节）里 `<img` 与 `.png` **也 0 命中**。
  **不是「图够不着」，是这篇文档不带图。**
- **没有实跑。** 没有写过一份 merge rules file、没有跑过 STPM 合并、没有触发过 `reject` 的中止。`verified: doc-only` 说的就是这件事。
- **没有动 `wiki/index.md`**（实测 `index.md` 里 `stpm-merge-rules-file` 0 命中），也没有把本页挂进 [[stpm]] 的正文。

> ⚠️ **本篇的语料瑕疵，照实记下、一处都没替它改**（§11.2）。**下面引文里的内部链接标记按 §11.1 ② 剥成纯文本。**
>
> **① `how test are integrated`（`test` 少了复数 `s`）。** 逐字是
> `The merge rules file of the SmarTest Program Manager (STPM) lets you fine-tune how test are integrated into existing master test programs (MTP).`
> ——**本页照抄这个单数。**
>
> **② `different merge rule file`（应为 `files`）。** 逐字是
> `enabling you to easily prepare and use different merge rule file, for example, for different stages of the development process.`
> ——**`different` 后面接的是单数。**
>
> **③ 句中大写 `Do`。** 逐字是
> `Merge rule files are optional; if you Do not specify a merge rules file, a default set of rules is used.`
> ——**`Do` 在句中大写**（同一篇别处的 `do` 都小写）。
>
> **④ `No rule must appear more than once.`** ——**常见写法是 `may`**。**本页按字面读成「不许重复」，但这一句的措辞本身值得记一笔。**
>
> **⑤ `#### Subtopics` 是 H4，比版本段还低两级。** 本篇的标题是 H1、`## Functional changes` 是 H2，**而子主题清单的级别是 H4**——**中间没有 H3**。
>
> **⑥ `## Example` 里那份规则文件被拆成两个代码块。** 前 26 行一块，**块结束之后另起一块**装 `overwrite_label_wvt` 与 `overwrite_flow_var_value` 两行（两块之间还夹着空行）。**同一份文件被截成两段**——**本页没有打开子主题，所以不判这是转换造成的还是原文本来就分了两块。**
>
> **⑦ 同一件事在两篇里有两种叫法，而且「可用设置」与「Example」有一处对不上。** 这一条是跨两篇 + 跨两节的，分开说：
>
> - **同一个文件两个名字**：定义文档说 `the STPM control file`，而本页「语法 / 参数」节的子主题文本说 `The merge rules file to use is specified in the STPM Setup File.`——**那一句后面跟着的链接目标正是 `02.09.02.03_STPM_control_file.md`**。**本页并列，不替它统一。**
> - **`overwrite_label_wvt` 那一行对不上**：按本页「语法 / 参数」节的可用设置表逐格读，它是 **`Allow` = `+` / `Ignore` = `+` / `Reject` 空 / `Default` = `allow`**；而同一节的 `## Example` 里写着 `overwrite_label_wvt      = 'reject'`。**两处都在本页同一节里**（都来自子主题），**本页并列，不替它调和**——**本页没有打开 `02.09.02.04.01`，所以判不了那一格是原文就空着，还是被压平时丢了一格**（见上面「本页没做的」）。
>
> **这一格 2026-09-20 判了，办法是 §11.2 ⑥ 那一条：去看上游的 `.htm`。**
> 上游是 `F:\master-dev\dorm-wsl-sytest\tdc-html\raw\131150.htm`（`02.09.02.04.01` 的那一份）。
> **那一格在上游 HTML 里就是空的**——`overwrite_label_wvt` 那一行的五个 `<td>` 依次是
> 第一格（`<td>` 里包着一个指向 `135571.htm` 的锚，锚文字就是 `overwrite_label_wvt`）、
> 第二格 `<td><p>+</p></td>`、第三格 `<td><p>+</p></td>`、
> **第四格 `<td><p>&nbsp;</p></td>`（只有不换行空格）**、
> 第五格 `<td><p><span class="keyword">allow</span></p></td>`。
> **所以「`Reject` 不支持」是上游就写着的，不是压平丢格**——按 §11.2 ⑥ 那张判据表，
> 这属于「**上游就坏的**」那一栏：**将来重做一次转换也救不回来。**
> **代价照实说**：**这个结论是看 `.htm` 得来的，不是读 `02.09.02.04.01` 得来的**——
> **本页仍然没有打开那一篇**（见上面「本页没做的」）。
>
> **顺带把另外 27 行也核了**（同一张上游表逐行解析，再与本页「语法 / 参数」节的 `## Example` 逐条对照）：
> **28 条里只有 `overwrite_label_wvt` 这一条取了表里没有的值**，其余 27 条全部落在自己那一行的 `+` 格里。
> **同一遍还把上面「一个 flag 能取三种值」那一节的三个数对上了**：`allow` 支持 **28 / 28**、
> `reject` **26 / 28**（缺 `merge_unused_pin_group` 与 `overwrite_label_wvt`）、
> `ignore` **16 / 28**；默认值 **`allow` 16 条 / `ignore` 6 条 / `reject` 6 条**——
> **与上游表逐格一致，那三张表没有错。**
>
> **⑧ 编码坏字：本篇 0 处**（按 §11.2 ① 的判据用 `[\u4e00-\u9fff]` 扫过整篇，**一个汉字都没有**）；
> **整词替换（`DC/DC power units`）本篇 0 命中**——**两条都是实测结果，不是没查。**

`verified: doc-only`
