---
type: object
title: VWFG? - (Verify WaveForms in Groups)
layer: L1
stage: timing
tags: [timing, vwfg, l1-command, firmware-command, verify, waveform-set, device-cycle, equation-based]
related: [vwfs, wsus, waveform-set, wavetable, timing-equation-set, spec-set, wfds, wave, bwdf, dfgp, timing, timing-setup-commands]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.330_VWFG__-__Verify_WaveForms_in_Groups.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# VWFG? - (Verify WaveForms in Groups)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,794 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.330_VWFG__-__Verify_WaveForms_in_Groups.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

There are three different ways to call VWFG?:

```
VWFG? {waveform_set}, ["dev_cyc_name"], {(pinlist)}
VWFG? {specset_id},["dev_cyc_name"],{(pinlist)}
VWFG? {wavetable_name}, ["dev_cyc_name"], {(pinlist)}
```

All three forms return:

```
VWFG {status}
```

### Parameters

|

waveform_set

 |

Waveform Set Number. Enter PRM for the Primary Waveform Set, or an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）.

 |
 |

specset_id

 |

Derived as follows:

`100 * equation_set_no + specset_no`

 |
 |

wavetable_name

 |

The wavetable name. Enter a string of up to 40 alphanumeric characters (upper or lower case) enclosed in double quotes.

 |
 |

dev_cyc_name

 |

If you specify the name of a device cycle, only this device cycle will be checked. Enter ALL for all device cycle names in the device cycle table.

 |
 |

pinlist

 |

The name of the pin or pins whose definitions you want to check. This parameter can also include groups previously created by `DFGP, DFGP? - (DeFine GrouP)`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）. If more than one pin is to be included, the names must be separated with a comma. The symbol @ can be used to check all configured pins.

 |
 |

status

 |

The system returns:

0: The definitions are not the same.

1: The definitions are the same.

 |

### Example

```
> VWFG? "spec_search_wtb","SBC",(ser_in)
< VWFG 1
> VWFG? "spec_search_wtb",,(ser_in)
< VWFG 0
```

According to this example, the waveform and device cycle definition for device cycle SBC are the same for the pins in the group ser_in within the wavetable spec_search_wtb, but this does not hold for all device cycles that are defined for the pins of this group.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.330_VWFG__-__Verify_WaveForms_in_Groups.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

- waveform_set is greater than the range allowed by the `WSUS`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） command.
- specset_id is invalid because equation_set_no, specset_no or both are invalid.
- specset_id does not reference a defined wavetable.
- wavetable_name does not reference a defined wavetable.
- multi-port spec does not reference a defined wavetable.

<!-- 报错节 end -->

## 是什么

**`VWFG?` 是 timing setup 里的一条校验查询：问「一组 pin 上的 device cycle 与 waveform 定义
是不是完全一样」，答一个 `0` 或 `1`。** 原文第一句就是全部定义：

> 「The VWFG? (Verify WaveForms in Groups) query checks whether all specified pins have the same
> device cycle and waveform definitions. The system responds with a 0 or a 1.」

两个关键词：**`all specified pins`（比较发生在 pin 与 pin 之间）**、
**`same device cycle and waveform definitions`（比的是定义，不是值）**。

### 它比什么：两类对象，判据被外包给命令

**原文用两句话把判据封闭地列了出来**，一句管 device cycle，一句管 waveform
（**这两句在 raw 里是分开的两段**；它们上面还夹着一句「无副作用」声明，
**本页把那句挪到了下一节**——引用逐字，只调了叙述次序）：

> 「The items taken into account when checking for device cycle definitions are the device cycle name
> and the waveform sequence.」

> 「The items taken into account when checking for waveform definitions are the parameters to
> commands WFDF, WFDF? - (WaveForm DeFinition), WAVE, WAVE? - (WAVEform) and BWDF, BWDF? - (Break
> Waveform DeFinition), such as waveform set number, edge actions, data parameters.」

| 比的是 | 判据（都是原文） | 判据从哪来 |
|---|---|---|
| **device cycle 定义** | `the device cycle name and the waveform sequence` | 两条：名字 + 波形序 |
| **waveform 定义** | 判据是**三条命令的参数**：`WFDF` / `WAVE` / `BWDF`（原文 `the parameters to commands`）；举了三个例子 `waveform set number, edge actions, data parameters` | **三条命令的参数** |

**第二行是本页最值得记的一条**：`VWFG?` 不自己定义「什么叫 waveform 定义相同」，
它**把判据外包给三条命令的参数**——`WFDF`、`WAVE`、`BWDF`（→ [[wfds]] / [[wave]] / [[bwdf]]）。
**所以那三条命令能改的东西，就是这里会不一致的东西**
（**推断**：依据是这句原文的 `the parameters to commands` 这个结构；
**本篇没有说「这三条命令之外的改动不算」**）。

### 它不改任何东西

> 「The VWFG? query has no influence on the number of defined waveform sets.」

**这是一条「无副作用」声明，而且它特意点的是 `the number of defined waveform sets`**——
即 [[wsus]] 定的那个数。**原文只声明了这一件事**，别的状态碰不碰，**语料未写**。

### 三种调用形式：指到「同一个东西」的三条路

语法（上面「语法 / 参数」节逐字）给的是三种：

```
VWFG? {waveform_set}, ["dev_cyc_name"], {(pinlist)}
VWFG? {specset_id},["dev_cyc_name"],{(pinlist)}
VWFG? {wavetable_name}, ["dev_cyc_name"], {(pinlist)}
```

**三条路指向的是同一个东西**：第一路的 `waveform_set` 是编号（`PRM` 或 1 到最大值），
第二、三路是 **equation based testing** 下的两种写法。原文为此单起了一节：

> 「In equation-based testing, you must identify a wavetable instead of a waveform set. This is
> achieved either by supplying wavetable_name directly, or by supplying specset_id, calculated from
> equation set number and spec set number as follows:」

`specset_id` 的算法在原文里出现**两次**（`## Equation-based testing` 一节一次、
`## Parameters` 表里一次），两次都是同一行 `100 * equation_set_no + specset_no`。

**更有用的一句是它怎么把 `specset_id` 翻回一个 wavetable 的**：

> 「The appropriate wavetable is determined by looking at which wavetable is referenced by
> equation_set_no and specset_no in the timing specification file.」

**这句话把第三个文件牵了进来**：解析要读 **timing specification file**（→ [[timing-specification]]）。
所以 **`VWFG?` 在 equation based 场合的判据，依赖那份 timing specification 里的一条 wavetable 引用**
（**推断**：`referenced by equation_set_no and specset_no in the timing specification file`
只能指那种引用；**本篇没有写出那个文件里的关键字名**）。

`wavetable_name` 的写法有一条硬限制（参数表逐字）：

> 「The wavetable name. Enter a string of up to 40 alphanumeric characters (upper or lower case)
> enclosed in double quotes.」

**40 个字符、字母数字、大小写都行、必须双引号。**

### `dev_cyc_name`：先缩小范围，再比

第二个参数是可选的，语义原文只有两句：

> 「If you specify the name of a device cycle, only this device cycle will be checked. Enter ALL for
> all device cycle names in the device cycle table.」

| 第二位写什么 | 查几个 device cycle |
|---|---|
| **一个 device cycle 名** | **只查这一个** |
| **`ALL`** | **device cycle table 里的全部** |
| **留空** | **语料未写**——示例里就是留空（`VWFG? "spec_search_wtb",,(ser_in)`），而它的回复是 `0`。**（推断）留空 ≈ `ALL`**：依据是示例的说明句说那一问「does not hold for **all device cycles** that are defined for the pins of this group」，即那一问确实扫了全部；**但本篇没有一句写「留空等于 ALL」。** |

### `pinlist`：比哪些 pin

逐字：

> 「The name of the pin or pins whose definitions you want to check. This parameter can also include
> groups previously created by DFGP, DFGP? - (DeFine GrouP). If more than one pin is to be included,
> the names must be separated with a comma. The symbol @ can be used to check all configured pins.」

三条：**组名可以直接写**（[[dfgp]] 建的组）、**多个用逗号隔**、**`@` = 所有已配置 pin**。

### `status`：`1` 是「一样」，`0` 是「不一样」——**两者都不是报错**

> 「0: The definitions are not the same.」

> 「1: The definitions are the same.」

**`0` 是一条正常回复，不是一个错误。** 真正会报错的是另外五种情形（见上面「报错条件」节）。
**这条区分很实用**：看到 `VWFG 0` 该去比对 setup，而不是去查命令为什么失败。

## 典型用法

**本篇没有 `## Procedure`、没有 `## Before you begin`。** 能给出定位的只有两处：
`## Application`（一行）与 `## Example`（一个示例）。**所以这一节给不出「照这个顺序敲」的完整流程。**

**1. 原文的定位只有一句**（`## Application` 全文，逐字）：

> 「Timing setup, see Timing Setup Commands.」

→ 即它属于 [[timing-setup-commands]] 那一族，
**但本篇没有说它在 timing setup 流程里排第几步。**

**2. 唯一一个示例（`## Example`，逐字）——两次调用、一正一反**：

```
> VWFG? "spec_search_wtb","SBC",(ser_in)
< VWFG 1
> VWFG? "spec_search_wtb",,(ser_in)
< VWFG 0
```

**读这个例子有四点**：

| 观察 | 说明 |
|---|---|
| **`> ` / `< ` 两个前缀** | `>` 是发出去的、`< ` 是回复 |
| **两次都用 `wavetable_name` 形式** | `"spec_search_wtb"` 是 wavetable 名——**本篇的示例一次都没示范 `waveform_set` 编号形式** |
| **两次只差第二位** | 第一次 `"SBC"`（单个 device cycle），第二次留空 |
| **`1` → `0` 就是这一对的全部信息** | 单个 device cycle 一致，而**全部** device cycle 不一致 |

**原文对这个例子的解释逐字**：

> 「According to this example, the waveform and device cycle definition for device cycle SBC are the
> same for the pins in the group ser_in within the wavetable spec_search_wtb, but this does not hold
> for all device cycles that are defined for the pins of this group.」

**它同时说明了 `VWFG?` 的比较发生在「pin 组内部」**（`for the pins in the group ser_in`）——
**不是拿一个 set 去比另一个 set**（那是 [[vwfs]]，见「和谁有关」）。

**3. 两句要怎么配合用**：

| 想知道 | 怎么问 |
|---|---|
| **某一个 device cycle 在组内一致吗** | 第二位写那个 device cycle 名 |
| **整张 device cycle 表在组内都一致吗** | 第二位写 `ALL`（或留空，见上面那条「（推断）」） |
| **是哪几个 pin 掉了队** | **本篇答不了**——回复格式就是 `VWFG {status}`，**没有逐 pin 的输出**（**语料未写**） |

**4. 出错时看哪一条**：见上面「报错条件」节的五条，其中第一条（`waveform_set` 越 [[wsus]] 的上限）
是唯一一条参数范围类的；第五条点了一个语法里不存在的输入形式，见「出处」⚠️ ①。

## 和谁有关

- [[vwfs]] — **姊妹查询，方向互补（同类）**。两篇共用的那类句子几乎同形
  （开篇句都用 `query checks whether` 起头 / 都有一段判据句 /
  都有一句 `has no influence on the number of defined waveform sets.`），
  而比较的对象不同：**`VWFG?` 比的是「一组 pin 之间」，`VWFS?` 比的是「两个 waveform set 之间」。**
  **两篇的判据清单还有一处不一致**（本篇列了 `BWDF`，[[vwfs]] 没列）——见「出处」⚠️。
- [[wsus]] — **上限来源（前置）**。参数表与报错第一条都指着它，两处原文分别是
  `The maximum number is determined by WSUS, WSUS? - (Waveform Sets USed).` 与
  `waveform_set is greater than the range allowed by the WSUS command.`
- [[waveform-set]] — **作用域（同类）**。`waveform_set` / `specset_id` / `wavetable_name`
  三种写法指向的都是「一个 waveform set 所在的那一组定义」；
  **「waveform set 里装什么」的正文在那一页，本页没有。**
- [[wavetable]] / [[timing-specification]] — **equation based 那一侧的两个件（上游）**：
  查的是 wavetable，而 wavetable 是**从 timing specification 文件里反查出来的**
  （原文 `The appropriate wavetable is determined by looking at which wavetable is referenced by
  equation_set_no and specset_no in the timing specification file.`）。
- [[timing-equation-set]] / [[spec-set]] — **`specset_id` 的两个分量（上游）**：
  `100 * equation_set_no + specset_no`。
- [[wfds]] / [[wave]] / [[bwdf]] — **判据的来源（上游）**：原文说 waveform 定义一致与否，
  看的是**这三条命令的参数**。**这三篇的 raw 本页一篇没读**（见「出处」）。
- [[dfgp]] — **`pinlist` 可以带组（上游）**：`groups previously created by DFGP`。
- [[timing]] — **`stage: timing` 的阶段页**；它把 `[[vclk]] [[vdcg]] [[vtim]] [[vwfg]] [[vwfs]]`
  列成一组「成组的 timing 校验查询命令」（**本页读到的 wiki 页**）。
- [[timing-setup-commands]] — **`## Application` 指的上游入口**（该句逐字见「典型用法」）。
- [[vclk]] / [[vdcg]] / [[vtim]] — **同族的三条校验查询（并列）**：本篇一次没提它们，
  「同族」的依据是 [[timing]] 那张表（**本页读到的 wiki 页**），不是本篇 raw。
- [[command-reference]] — **命令索引页**：`VWFG?` 属 `02.06_Command_Reference` 一族。

## 版本

**本文档有 `## Functional changes` 段，段里只有一条**：

- `Introduced before SmarTest 6.3.2`

> **这一条是 §11.2 ② 说的哨兵值，不是「6.3.2 新增了 VWFG?」。**
> 措辞是 `before`，意思是「**在本套文档集覆盖范围开始之前就已经有了**」。
> **只可以说：7.10.3 上有它，而且它比 6.3.2 更老** → [[smartest-6.3.2]]。
> **不许把它读成「6.3.2 引入了 VWFG?」。**

**版本段里没有的东西**（照实记，不替它补）：**没有第二条**。
所以「三种调用形式是不是同一版进来的」「`dev_cyc_name` 是哪一版加的」**在本篇里查不到**。

## 出处

`sources:` 一篇：

- `02_System_reference/02.06_Command_Reference/02.06.02.02.330_VWFG__-__Verify_WaveForms_in_Groups.md`
  （frontmatter 的 `source_topic` 是 `98863.htm`；**4,054 字节 / 132 行，整篇读完**——
  字节按 `st_size`、行数按 `wc -l`，§11.5 口径）
- 本页的「语法 / 参数」节与「报错条件」节是脚本从这一篇抽的（**本页一个字没动**）。
- **上游 `.htm` 核过**：`raw/98863.htm`（**9,671 字节**）。核的是下面 ⚠️ ① 那一条。

**本页没做的**：

- **`WFDF` / `WAVE` / `BWDF` / `WSUS` / `DFGP` 五篇的 raw 一篇没读。**
  本页只在**这篇的原文里**见过它们的名字（`the parameters to commands` 那一句点了三条），
  **所以「动作怎么写、边沿名怎么定、组怎么建、上限怎么改」本页一个字没有。**
- **`Timing Setup Commands`（`## Application` 指的那一篇）没读**——本篇给的只是它的标题。
- **`timing specification` 那一侧没读。** 原文说 wavetable 是从那个文件里反查出来的，
  **但本篇没写那个文件长什么样**；那一侧的内容在 [[timing-specification]] / [[timing-file]]，
  **本页没读它们的 raw。**
- **图 0 张。** 实测 `![` / `<img` / `.png` / `.jpg` / `.gif` / `raw/` 六种写法在本篇
  **全部 0 命中**；上游 `raw/98863.htm` 里 `<img` 也是 **0 次**。
  **所以本页没有任何来自图的结论，这张「没有图」是查过的事实（§11.4）。**
- **没在任何 93K 机台上跑过 `VWFG?`**（`verified: doc-only`）。
  **所以「留空第二位到底等不等于 `ALL`」「`0` 的时候是哪几个 pin 不一致」本页答不了。**
- **本篇没有 `## Warnings` 段**，所以「报错条件」节里只有 `## Errors` 的五条——不是漏写。

### §10 重复投放：本篇在语料里有**三份**（本页查过）

| 路径 | `source_topic` | 字节 | 与**本页这一份**的正文 |
|---|---|---|---|
| `02.06_Command_Reference/02.06.02.02.330_VWFG__-__Verify_WaveForms_in_Groups.md`（**本页的出处**） | `98863.htm` | 4,054 | — |
| `02.06_Command_Reference/02.06.06.02.38_VWFG__-__Verify_WaveForms_in_Groups.md` | `98863_2.htm` | 4,055 | **把篇内相对链接的前缀归一化后，`diff` 报 0 行差异** |
| `02.08_Setup_and_Result_Tools/02.08.04.34.02.02.38_VWFG__-__Verify_WaveForms_in_Groups.md` | `98863_3.htm` | 4,255 | **同上——0 行差异** |

**三份的差别只有两处**：① frontmatter 的 `source_topic` / `source_html`；
② **篇内相对链接的前缀**（第三份多一层 `../02.06_Command_Reference/`，差的字节就是它）。
**本页的结论全部只来自第一份**；另两份只核了 frontmatter、字节数与 `diff` 行数，
**没有读它们的正文**（§12 不越取材边界）。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
> **① 报错段点了一个语法里不存在的输入形式。** `## Errors` 的第五条逐字是
> `- multi-port spec does not reference a defined wavetable.`
> ——**而本篇的 `Syntax` 只有三行、`Parameters` 只有六个名字，两处都没有 multi-port 形式。**
> **核过上游 `raw/98863.htm`：`multi-port` 这个词在全篇（9,671 字节）只出现这一次**，
> 就是报错那一行。**所以这处不齐是上游文档自带的，不是 HTML→md 转换丢的**
> （§11.2 ⑥ 的判法：去看上游 `.htm`）。**本页照原样引这一条，
> 不替它补一个「第四种调用形式」。**
> **② `specset_id` 的算法在篇内重复了两遍。** `## Equation-based testing` 一节里写了一次、
> `## Parameters` 表里又写了一次，两处都是 `100 * equation_set_no + specset_no`
> （表里那处带反引号）。**原文如此，本页两处都引。**
> **③ 参数表在压平后是「一行一格」的竖线行**（` | ` / 名字 / ` | ` / 释义 / ` | `），
> 不是一张连续表格——所以「语法 / 参数」节里它是散行。
> **这是语料的段结构，不是抽取错**（与 [[bwds]] 那一页记过的同一种毛病）。
> **④ 坏字：本篇 0 个。** 按 §11.2 ① 的判据（英文文档里出现任何汉字都是坏字）逐字查过，
> **本篇一个汉字都没有**——**但这是「本页读到的」，不是「本篇没有」**（§13.1：没找到 ≠ 没有）。
> **⑤ 参数名在两处不同形**：`Syntax` 与 `Parameters` 用 `waveform_set`，
> 报错段第一条也写 `waveform_set`——**这一篇两处是一致的**（对照 [[vwfs]] 那一页记的同类问题）。

`verified: doc-only`
