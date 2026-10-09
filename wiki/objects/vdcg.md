---
type: object
title: VDCG? - (Verify Device Cycle for Group)
layer: L1
stage: timing
tags: [timing, device-cycle, vdcg, consistency-check, l1-command, firmware-command, pattern-tool, equation-based-timing]
related: [pattern-tool, wsus, wavetable, waveform-set, vclk, vtim, timing]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.321_VDCG__-__Verify_Device_Cycle_for_Group.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# VDCG? - (Verify Device Cycle for Group)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **2,972 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.321_VDCG__-__Verify_Device_Cycle_for_Group.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
VDCG? {waveform_set}, {dev_cyc_name}, {(pinlist)}
```

returns:

```
VDCG {waveform_set}, {dev_cyc_name}, {dev_cyc_len}
```

Or:

```
VDCG? {specset_id}, {dev_cyc_name}, {(pinlist)}
```

returns:

```
VDCG {specset_id}, {dev_cyc_name}, {dev_cyc_len}
```

Or:

```
VDCG? {wavetable_name}, {dev_cyc_name}, {(pinlist)}
```

returns:

```
VDCG {wavetable_name}, {dev_cyc_name}, {dev_cyc_len}
```

### Parameters

| waveform_set | Waveform set number. Enter PRM for the primary waveform set, or an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）. | Waveform set number. Enter PRM for the primary waveform set, or an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）. |
|---|---|---|
| specset_id | Derived as follows:<br><br>`100 * equation_set_no + specset_no` | Derived as follows:<br><br>`100 * equation_set_no + specset_no` |
| wavetable_name | The wavetable name. Enter a string of up to 40 alphanumeric characters (upper or lower case) enclosed in double quotes. | The wavetable name. Enter a string of up to 40 alphanumeric characters (upper or lower case) enclosed in double quotes. |
| dev_cyc_name | The device cycle name. Enter a string of up to 16 alphanumeric characters (upper or lower case) enclosed in double quotes.<br><br>Alternatively, you can enter: | The device cycle name. Enter a string of up to 16 alphanumeric characters (upper or lower case) enclosed in double quotes.<br><br>Alternatively, you can enter: |
|  | ALL | With this specifier the command checks that:<br><br>- The pins in pinlist have exactly the same device cycle names.<br>- For each device cycle, each pin defines the device cycle with the same length. |
|  | FDC | With this specifier the command checks that the first device cycle in the device cycle definition table for each pin in the pinlist has the same length. |
| pinlist | The pin name or names whose device cycles are to be checked. If more than one pin is required, the names must be separated with a comma. The @ character can be used to read all configured pins. | The pin name or names whose device cycles are to be checked. If more than one pin is required, the names must be separated with a comma. The @ character can be used to read all configured pins. |
| dev_cyc_len | Always 1 for SmarTest 7.10. | Always 1 for SmarTest 7.10. |

> ⚠️ 转录说明（非原文）：本表在上游 HTML 里含合并格（colspan / rowspan）；
> 跨格文字已按覆盖范围重复写出（**不是原表里有重复的格子**）。真结构见 `tdc-html/agent-html/98846.htm`。

### Example

```
VDCG? 1,ALL,(inputs)
```

returns:

```
VDCG 1,ALL,SLEN
```

This example checks the consistency of all device cycles for pins in the pin group "inputs" in waveform set 1. The test system replies that all device cycles for the specified group are consistently defined.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.321_VDCG__-__Verify_Device_Cycle_for_Group.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

- The waveform set is outside the valid range as set by `WSUS`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）.
- specset_id is invalid because equation_set_no, specset_no, or both are invalid.
- specset_id does not reference a defined wavetable.
- wavetable_name does not reference a defined wavetable.

<!-- 报错节 end -->

## 是什么

**VDCG? 做的是「一致性检查」：一组 pin 上的 device cycle，定义得一样不一样。** 原文第一句：

> 「The VDCG? (Verify Device Cycle for Group) query is a consistency check on device cycles for a
> group of pins. You can also use it within the context of the current label, given by
> TSTL, TSTL? - (TeST Label).」

**它也只有查询这一半**（全篇命令名都带 `?`：标题、三段语法、示例全是 `VDCG?`），
和 [[vclk]] / [[vtim]] 同属 Verify 一族，**不写任何东西**。
**而它多了一句别处没有的话**：**可以在「当前 label 的上下文里」用**——
`TSTL` 那一篇本页没读（见「出处」），**所以「label 上下文到底怎么影响它」本页答不了**。

### 两个判据，一句话说全

> 「The query checks that the device cycle referenced by dev_cyc_name is defined for every pin in
> the pinlist in the specified waveform set, and that the length of the device cycle for all pins
> in the pinlist is the same.」

| # | 判据 |
|---|---|
| ① | **这个 device cycle 在 pinlist 里每个 pin 上都有定义**（`is defined for every pin`） |
| ② | **它在每个 pin 上的长度相同**（`the length of the device cycle for all pins in the pinlist is the same`） |

### `dev_cyc_name` 位可以写两个特殊词

逐条取值见上面「语法 / 参数」节；这里只说它们**把检查换成了哪一种**：

| 写法 | 检查什么（原文逐字） |
|---|---|
| 一个具体的 device cycle 名 | 上面那两句：**每个 pin 都定义了它、且长度一致** |
| `ALL` | `The pins in pinlist have exactly the same device cycle names.` 与 `For each device cycle, each pin defines the device cycle with the same length.` |
| `FDC` | `With this specifier the command checks that the first device cycle in the device cycle definition table for each pin in the pinlist has the same length.` |

**`ALL` 与 `FDC` 查的不是一件事**：`ALL` 查**整张表**（名字集合 + 每个 cycle 的长度），
`FDC` 只查**第一行**（`the first device cycle`）的**长度**。
**`FDC` 是哪几个词的缩写，本篇没写**（**推断**：First Device Cycle，依据是那句里唯一的名词短语
`the first device cycle in the device cycle definition table`——**原文没有一句话点明缩写的展开**）。

### 「定义了还不够，还得有逻辑波形序列」

原文单独给了一句 `Note`：

> 「Note If one specific device cycle or FDC is queried, a response is only given if the logical
> waveform sequence is defined.」

**这是第三个前提，而且只在两种写法上生效**：**具体名**与 **`FDC`**——
**`ALL` 那句里没有这个条件**（原文只写了 `one specific device cycle or FDC`）。
**「logical waveform sequence 由谁定义、怎样才算已定义」，本篇一个字没写**（**语料未写**）；
**没定义过时是报错还是沉默，本篇也没说**——它只说了「不给答复」。

### 三个定位方式：fixed timing 一种、equation based 两种

三段语法（逐字见上面「语法 / 参数」节）对应三种第一位：
`waveform_set`、`specset_id`、`wavetable_name`。**equation based 那一侧本篇解释得比语法行细**：

> 「In equation-based testing, you must identify a wavetable instead of a waveform set. This is
> achieved either by supplying wavetable_name directly, or by supplying a specset_id, calculated
> from equation set number and spec set number as follows:」

> 「The appropriate wavetable is determined by looking at which wavetable is referenced by
> equation_set_no and specset_no in the timing specification file.」

**后一句的作用是「`specset_id` 怎么被解析」**：靠的是 **timing specification 文件里那个对应关系**。
**而 `## Errors` 里恰好有两条对着它**（`specset_id does not reference a defined wavetable.` /
`wavetable_name does not reference a defined wavetable.`）。

**两个字符串参数有明文上限，而且数字不同**（参数表逐字）：
`wavetable_name` 是 `a string of up to 40 alphanumeric characters (upper or lower case) enclosed in double quotes`，
`dev_cyc_name` 是 `a string of up to 16 alphanumeric characters (upper or lower case) enclosed in double quotes`。

### 回什么：`dev_cyc_len`（**本页最对不上的一格**）

三段 `returns:` 都回三格：第一位（回显你给的那个）、`dev_cyc_name`、`dev_cyc_len`。
**而 `dev_cyc_len` 这一格，本篇自己给了两句方向不同的话**：

| 出处 | 原文逐字 |
|---|---|
| 参数表最后一行 | `Always 1 for SmarTest 7.10.` |
| `## Example` 的回复 | `VDCG 1,ALL,SLEN` |

**一栏说这个字段恒为 `1`，例子回的却是 `SLEN`。**
**本篇没有说 `SLEN` 是什么、也没有说它和 `1` 怎么并存**（**语料未写**）。
**本页两处并列照记，不替它裁定。**
—— **这一处本页核过上游的 `.htm`（`98846.htm`）：两处在上游就是这样的**（见「出处」⚠️ ①）。

### 一个 site 一次（这段与 [[vclk]] 逐字相同）

> 「With this command you can retrieve site specific information (only one site can be in focus at
> a time). For the site in focus, SmarTest displays results in the Testflow Editor and in the
> result tools. Also, any firmware queries report setup and results for the site currently in focus only.」

**本页读到的 [[vclk]] 那一篇里有逐字相同的一段，而 [[vtim]] 那一篇没有**（**三篇都是本页的取材**）。
**读法**：结果只对当前 in focus 的那个 site 有效 → [[site-focus-required-before-command]]。

## 典型用法

**1. 最小的一次调用**（原文 `## Example`，逐字）：

```
VDCG? 1,ALL,(inputs)
```

returns:

```
VDCG 1,ALL,SLEN
```

逐位对一遍：

| 位 | 例中的值 | 是什么 |
|---|---|---|
| 1 | `1` | `waveform_set`——waveform set 1 |
| 2 | `ALL` | `dev_cyc_name` 位的特殊词——查**整张 device cycle 表** |
| 3 | `(inputs)` | `pinlist`——叫 `inputs` 的那个 pin group |

原文的说明逐字：

> 「This example checks the consistency of all device cycles for pins in the pin group "inputs" in
> waveform set 1. The test system replies that all device cycles for the specified group are consistently defined.」

**注意 `SLEN` 在这里被当成「一致」的答复**（`consistently defined`），
**而参数表说这一格「恒为 1」**（见「是什么」那一节）。**两处对不上，本页不裁定。**

**2. 怎么挑 `dev_cyc_name` 的写法**（本页按上面那张表归纳，**顺序本身是建议**）：

| 你想问的 | 写法 |
|---|---|
| **某一个 cycle 在这组 pin 上是不是都有、长度是不是一样** | 写那个 cycle 的名字（**前提：logical waveform sequence 已定义**） |
| **这组 pin 的 cycle 名字集合是不是完全一样** | `ALL` |
| **这组 pin 的第一行是不是一样长** | `FDC`（**前提同上**） |

**3. 四条报错全是「指错了地方」**（见「报错条件」节）：waveform set 越 [[wsus]] 的范围、
`specset_id` 本身算错（`equation_set_no` / `specset_no` 有一处无效）、
`specset_id` 指不到已定义的 wavetable、`wavetable_name` 指不到已定义的 wavetable
——**四条里三条在 equation based 那条路上**。
**「长度不一致 / 名字不一致」本身不在这四条里**——**它不是报错，它是这个查询要给你的答案**
（**推断**，依据是 `## Errors` 四条没有一条讲不一致，而本篇第一句说这个查询就是查一致性；
**原文没有一句话替这条分工背书**）。

**4. 它是 Pattern Tool 的编辑命令。** 本篇 `## Application` 全文就一句：

> 「Edit command in Pattern Tool.」

**这一句把它和同族另外两条分开了**：本页读到的 [[vclk]] / [[vtim]] 两篇，`## Application` 都写
`Timing setup, see Timing Setup Commands.`，**只有本篇写 Pattern Tool**（**三篇都是本页的取材**）→ [[pattern-tool]]。
**「在 Pattern Tool 里排第几步」本篇没说。**

## 和谁有关

- [[pattern-tool]] — **上游入口**。本篇 `## Application` 全文是 `Edit command in Pattern Tool.`
  ——**本篇没有说它是哪个界面动作的背面、也没有说它在编辑流程里排第几步。**
- [[wsus]] — **`waveform_set` 上限的来源（前置）**。本篇两处点名：
  参数表的 `The maximum number is determined by WSUS, WSUS? - (Waveform Sets USed).` 与 `## Errors` 第一条。
- [[wavetable]] — **equation based 下第一位指的实体（同类）**。
  `specset_id` 与 `wavetable_name` 两条指法最后都要落到「一个已定义的 wavetable」上
  （`## Errors` 那两条就是对着它）。**wavetable 本身的正文在那一页里**，本页只保证本篇这么用了这个词。
- [[waveform-set]] — **fixed timing 下第一位指的实体（同类）**。同上，本页只保证本篇这么用了这个词。
- [[vclk]] / [[vtim]] — **同族的三条 Verify 查询（并列）**。
  **本篇一次没点名它们**；「同族」的依据是**三篇同在一章（`02.06.02.02.*`）**，
  且 [[vclk]] 那一篇带一段与本篇逐字相同的 site focus 说明（**三篇都是本页的取材**）。
  **一条能看出分工的差别**：本篇的 `## Application` 写 Pattern Tool，另外两篇写 Timing setup（**同上，三篇都是本页的取材**）。
- [[timing]] — **stage 页**。本页 `stage: timing` 的依据是 frontmatter，以及三段语法都在讲
  waveform set / timing set / wavetable（`specset_id` 由 `100 * equation_set_no + specset_no` 算得）——
  **注意本篇的 `## Application` 本身没有出现 `timing` 这个词**（它写的是 Pattern Tool），**这一点照实说**。
- `TSTL, TSTL? - (TeST Label)`（**未建，故用反引号，§9.1**）— **本篇唯一点名的「上下文」**：
  `You can also use it within the context of the current label, given by TSTL, TSTL? - (TeST Label).`
  **本页没读它**，**所以「label 上下文怎么用」本页一个字没有。**

## 版本

**本文档有 `## Functional changes` 段，段里只有一条**：

- `Introduced before SmarTest 6.3.2`

> **这一条是 §11.2 ② 说的哨兵值，不是「6.3.2 新增了 VDCG」。**
> 措辞是 `before`，意思是「**在本套文档集覆盖范围开始之前就已经有了**」。
> **只可以说：7.10.3 上有它，而且它比 6.3.2 更老** → [[smartest-6.3.2]]。
> **不许把它读成「6.3.2 引入了 VDCG」。**

**版本段里没有的东西（照实记，不替它补）**：没有第二条。
**所以「`dev_cyc_len` 那一格是从哪一版变成 `SLEN` 的」「`Always 1` 那句是哪一版写的」在本篇里查不到**
——**而这两句正是本篇自相矛盾的那两句，版本段里一条都没有。**

## 出处

`sources:` 一篇：

- `02_System_reference/02.06_Command_Reference/02.06.02.02.321_VDCG__-__Verify_Device_Cycle_for_Group.md`
  （frontmatter 的 `source_topic` 是 `98846.htm`；**5,300 字节 / 168 行，整篇读完**——
  字节按 `st_size`、行数按 `wc -l`，§11.5 口径）
- 本页的「语法 / 参数」节与「报错条件」节是脚本从这一篇抽的（**本页一个字没动**）。

**本页没做的**：

- **`TSTL` 那一篇没读。** 本篇只在第一句里点名它（`given by TSTL, TSTL? - (TeST Label)`），
  **「label 上下文怎么设、怎么用」本页一个字没有。**
- **`WSUS` / `Pattern Tool` / `Timing specification` 三篇都没读。**
  **上限怎么定（WSUS）、Pattern Tool 里的路径怎么写、timing specification 文件里的
  `equation_set_no` / `specset_no` 对应关系长什么样，本页全无。**
- **`logical waveform sequence` 的正文没读。** 它是那句 `Note` 的前提，
  **但本篇没有链给它任何一篇**——所以本页连「该去哪读」都指不出来。
- **图 0 张。** 实测 `![` / `<img` / `.png` / `.jpg` / `.gif` / `raw/` 六种写法在本篇
  **全部 0 命中**。**所以本页没有任何来自图的结论**——
  **这张「没有图」是查过的事实，不是「够不着」（§11.4）。**
  （**device cycle 表长什么样**这个问题，本页只有那三句文字，没有图可看。）
- **没在机台上跑过 `VDCG?`**（`verified: doc-only`）。
  **所以「`SLEN` 到底是不是真的会出现」本页只能保证「文档这么写」（§11）。**
- **本篇没有 `## Warnings` 段**，所以「报错条件」节里只有 `## Errors` 的四条——不是漏写。

### §10 重复投放：本篇在语料里有**四份**（本页查过）

| 路径 | `source_topic` | 字节 | 与**本页这一份**的正文 |
|---|---|---|---|
| `02.06_Command_Reference/02.06.02.02.321_VDCG__-__Verify_Device_Cycle_for_Group.md`（**本页的出处**） | `98846.htm` | 4,292 | — |
| `02.06_Command_Reference/02.06.06.02.36_VDCG__-__Verify_Device_Cycle_for_Group.md` | `98846_2.htm` | 4,293 | **`diff` 报 4 行差异——全部是 frontmatter 的 `source_topic` / `source_html` 两行** |
| `02.06_Command_Reference/02.06.07.02.35_VDCG__-__Verify_Device_Cycle_for_Group.md` | `98846_3.htm` | 4,293 | **同上——4 行差异，只有 frontmatter** |
| `02.08_Setup_and_Result_Tools/02.08.04.34.02.02.36_VDCG__-__Verify_Device_Cycle_for_Group.md` | `98846_4.htm` | 4,385 | **差异只有 frontmatter 与篇内相对链接的前缀**（第四份多一层 `../02.06_Command_Reference/`，字节数差的就是它） |

**四份的正文逐行相同**（按 §10 重复投放：**四份落在三个不同章里**，
`02.06.06` 与 `02.06.07` 各有一份，说明这篇文档被三处目录同时收录）。
**本页的结论全部只来自第一份**；另三份只核了 frontmatter、字节数与 `diff` 行数，
**没有逐字读它们的正文**（§12 不越取材边界）。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
> **① `dev_cyc_len` 一格两说。** 逐字并列：
> `Always 1 for SmarTest 7.10.`（参数表）与 `VDCG 1,ALL,SLEN`（`## Example` 的回复）。
> **`SLEN` 这一串在本篇里只出现这一次，全文没有一处解释它。**
> **本页核过上游的 `.htm`（`raw/98846.htm`）**：那句
> `Always 1 for SmarTest 7.10.` 与那行
> `VDCG 1,ALL,SLEN` **在 `.htm` 里就是这样**——
> **所以这不是转换坏的，是上游文档自己的两处对不上（§11.2 ⑥）**，
> **拿哪一处都核不出「哪一处才算数」。**
> **② `Note` 后面缺一个冒号。** 逐字：
> ```
> Note If one specific device cycle or FDC is queried, a response is only given if the logical waveform sequence is defined.
> ```
> **同族的 [[wfds]] 那一篇写 `Note` 时用的是另一种句式**
> （`Note that the index must be specified decimally here, whereas in the wavetable, it is coded hexadecimally.`
> 与 `Note also the following:`——**前者带 `that`、后者带冒号**，**两处都是本页的取材**），
> **只有本篇直接接了一个 `If` 分句**。**本页照原样引，不替它补标点。**
> **③ `@` 的动词与同族不一致。** 本篇写的是
> `The @ character can be used to read all configured pins.`——
> **用的是 `read`**；而本页读到的 [[vclk]] 那一篇写的是
> `The @ symbol can be used to check all configured pins.`（**用 `check`**），
> **连 `character` / `symbol` 两个词都不同**。**本页照各自的原样引，不替它们统一。**
> **④ 回复字段混在输入参数表里。** `dev_cyc_len` 是回复里的值，却和 `waveform_set` / `wavetable_name`
> 这些输入参数排在同一张 `Parameters` 表里。**同族三篇都是这个写法**
> （[[vclk]] 的 `autocorrect`、[[vtim]] 的 `status` 同理，**三篇都是本页的取材**）——**本页照原样记。**
> **⑤ 同一篇里两种记号。** 三段语法里的第二格都写作 `{dev_cyc_name}`（花括号包住），
> 而参数表里那两个特殊词写作裸字 **`ALL`** 与 **`FDC`**（参数表的原文是
> `Alternatively, you can enter:` 之后直接列出这两个词）——
> **同一篇没有说明「特殊词」与「名字」在语法行里怎么区分**（**语料未写**）。**本页照原样引。**
> **⑥ 坏字：本篇 0 个。** 照 §11.2 ① 那条判据（**英文文档里出现任何汉字，都是坏字**）逐字查过：
> **本篇一个汉字都没有**——**但这是「本页读到的」，不是「本篇没有」**（§13.1：没找到 ≠ 没有）。

`verified: doc-only`
