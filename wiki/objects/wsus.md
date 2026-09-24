---
type: object
title: WSUS, WSUS? - (Waveform Sets USed)
layer: L1
stage: timing
tags: [timing, waveform-set, wsus, l1-command, firmware-command, resource-limits]
related: [dscp, tsus, waveform-set, timing-setup-commands, timing, conf]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# WSUS, WSUS? - (Waveform Sets USed)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **676 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### WSUS

```
WSUS {waveform_set}
```

### WSUS?

```
WSUS?
```

returns:

```
WSUS {waveform_set}
```

### Parameters

|

waveform_set

 |

Waveform set number. This is the highest number currently allocated to a waveform set or the highest number of a set you want to load. The number you enter must not exceed the maximum number of waveform sets allowed (defined by the `DSCP`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md`） command).

This number is automatically updated to include any new waveform set as it is created. At power-on, only one waveform set (containing one timing set and default values) is available.

 |

### Example

```
WSUS 3
```

This example sets the number of used waveform sets to 3.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

- waveform_set is greater than the range allowed by the DSCP command.
- waveform_set is smaller than one.

<!-- 报错节 end -->

## 是什么

**WSUS 管的是一个数：这套设置「用到第几号」waveform set。**
它不管波形长什么样、也不管波形怎么定义——**它只管这个数字**。原文第一句：

> 「The WSUS (Waveform Sets USed) command sets the number of defined waveform sets to the given value.」

### 这个数是「用到第几号」，不是「定义了几个」

参数释义比第一句讲得更死，逐字：

> 「Waveform set number. This is the highest number currently allocated to a waveform set
> or the highest number of a set you want to load. The number you enter must not exceed
> the maximum number of waveform sets allowed (defined by the DSCP command).」

**两个口径并排在一句里**：`currently allocated`（**已经分配出去的**）与
`a set you want to load`（**你准备装入的**）。
**这说明 WSUS 既能报现状、也能「先把位子开好再装」**——
后半句正是它作为**装载前准备动作**的那一面。

**上电时的初值是 1，不是 0**，原文紧接着：

> 「This number is automatically updated to include any new waveform set as it is created.
> At power-on, only one waveform set (containing one timing set and default values) is available.」

**一句话里三件事**：① 数字**会自己长**（新建一个 waveform set 就往上加一）；
② 上电只有 **1 个** waveform set；③ **那唯一的一个里也已经含有一个 timing set**。

### 写与读：`WSUS` / `WSUS?` 是同一格式的进出两半

| 方向 | 写法 | 回什么 |
|---|---|---|
| 写 | `WSUS {waveform_set}` | — |
| 读 | `WSUS?` | `WSUS {waveform_set}`（**与写入格式逐字相同**） |

原文对 `?` 这一半只有一句：

> 「The WSUS? query returns the number of waveform sets currently defined.」

### 上下限与两条报错（**同一条边界的两侧**）

| 边界 | 原文来源 | 越界后果 |
|---|---|---|
| **上限** | `Maximum allowed waveform sets as set by DSCP` | `waveform_set is greater than the range allowed by the DSCP command.` |
| **下限** | 最小是 1 | `waveform_set is smaller than one.` |

上限的**具体值写在第一句里，而且是「默认 = 最大」**：

> 「The new value has to be an integer in the range of 1 to Maximum allowed waveform sets
> as set by DSCP, DSCP? - (Define System Control Parameter) (the default is 16, the maximum is 16).」

**注意上限的来源 `DSCP` 那一篇本页没读**——`16` 是默认值还是硬上限、
**能不能改、在哪改，本篇一个字没写**（见「出处」）。

### 「删除」这一半才是它常被喊出来的理由

原文用一整段讲删除，**这是 `## Application` 之外唯一交代「什么时候用」的地方**：

> 「You can use the WSUS command to delete sets.」

> 「If the timing setup file that you want to load to hardware contains more waveform sets
> than you require, you can use the WSUS command to delete all the sets above the number you specify.」

**场景很具体**：手里那个 timing setup 文件里的 waveform set **比你需要的多** →
**把数字设到你要用的那一号** → **号比它大的那些 set 全被删掉**。
「上面」= **号大于给定值的那些**（**推断**，依据就是 `above the number you specify`
与 `delete all the sets` 这两处措辞；**原文没有举一个号数例子，
也没有说删掉的东西还能不能回来——那一条语料未写**）。

## 典型用法

**1. 只想知道现状**：`WSUS?` → 拿到「现在用到几号」。**一行，没有参数。**

**2. 装载前先把位子开好**：按参数释义那半句 `or the highest number of a set you want to load`，
**先把数字设到你要装的最高号，再装那个 timing setup file**。
（**推断**，依据是参数释义里那半句与 `The number you enter must not exceed`；
**原文没有排出「先 WSUS 再装文件」这个顺序，本页不替它编一条。**）

**3. 裁掉多余的**（就是原文那一段的四个动作）：
**数清那个 timing setup file 里有多少 waveform set** → **定下你实际要用到第几号** →
`WSUS <那个号>` → **号更大的那些 set 被删掉**。
**这一步原文没写可逆**——**本页不敢替它说可逆**（见「是什么」末段）。

**4. 原文的示例（`## Example`，逐字）**：

```
WSUS 3
```

> 「This example sets the number of used waveform sets to 3.」

**例子里没有 `?`、也没有回读**——**原文没有示范「设完再读一次确认」这一步**。
**3 落在 1..16 里，不越界。**

**5. 边界上的两个数别踩**：`WSUS 0` 与 `WSUS 17` 都会报（下限 `smaller than one`，
上限 `greater than the range allowed by the DSCP command`）。
**那个 17 是本页按 `the maximum is 16` 推的（推断）**——
**若 DSCP 那边被改过，越界的那个数就不一定是 17。**

## 和谁有关

- [[dscp]] — **上限的来源（前置）**。本篇**三次**把上限指给它：`as set by DSCP`、
  `(defined by the DSCP command)`、以及 `## Errors` 的第一条。
  **这是本页唯一一条有原文逐字支撑的依赖关系。**
- [[waveform-set]] — **本页数的那个东西（同类）**。
  本篇那句 `only one waveform set (containing one timing set and default values)`
  是**本篇唯一一次描述 waveform set 的内容**；「它到底装什么」的正文在
  [[waveform-set]] 那一页——**那一页的 raw 不在本页的 `sources:` 里**。
- [[tsus]] — **同族的另一条 `xxUSed` 命令（并列）**。
  **本篇没有点名 `TSUS`**；「`WSUS` / `TSUS` / `LSUS` / `DSUS` 是四条 `xxUSed` 查询」
  这个说法来自 [[sprm]] 的一行（**本页读到的另一页的一行，不是本页的 raw**）。
- [[timing-setup-commands]] — **上游入口**。本篇 `## Application` 一节逐字全文是：
  > 「Timing setup, see Timing Setup Commands.」
  **只有这几个词加一个链接。** 本篇没有给出 WSUS 在 timing setup 里的位置。
- [[timing]] — **stage 页**。本页 `stage: timing` 的依据是那句 `Timing setup` 与 frontmatter
  （§6：`stage` 填最近的一段，不是归属）。[[timing]] 的 L1 表里也已有本页一行——
  `定义/删除 waveform set 的个数`（**本页读到的 wiki 页**）。
- [[conf]] — **一处本页不判的写法差异**：[[sprm]] 那一行把 `waveform_set_no` 的上限写成
  「由 [[wsus]] 定，且须 ≤ [[conf]] 允许的上限」，而本篇逐字写的是 `as set by DSCP`。
  **两个说法本页照原样并列，不替它们调和**——**本页的取材只有 WSUS 这一篇**
  （`CONF` 那一篇与 [[sprm]] 的 raw 都不在其中）。

**以 waveform set 为对象、但本篇没点名的邻居**：`WSDM`（Waveform Set Display Mode）、
`VWFS`（Verify WaveForm Sets）——**名字来自 [[timing-setup-commands]] 语法节里那一串子主题**
（**本页读到的 wiki 页**），**本页没有读它们的 raw**——
**所以本页不为它们写任何关系。没读到，就不写。**

## 版本

**本文档有 `## Functional changes` 段，段里只有一条**：

- `Introduced before SmarTest 6.3.2`

> **这一条是 §11.2 ② 说的哨兵值，不是「6.3.2 新增了 WSUS」。**
> 措辞是 `before`，意思是「**在本套文档集覆盖范围开始之前就已经有了**」。
> **只可以说：7.10.3 上有它，而且它比 6.3.2 更老** → [[smartest-6.3.2]]。
> **不许把它读成「6.3.2 引入了 WSUS」。**

**版本段里没有的东西（照实记，不替它补）**：没有第二条。
所以「上限 16 是哪一版定的」「删除语义哪一版改过」**在本篇里查不到**。

## 出处

`sources:` 一篇：

- `02_System_reference/02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`
  （frontmatter 的 `source_topic` 是 `98878.htm`；**1,986 字节 / 67 行，整篇读完**——
  字节按 `st_size`、行数按 `wc -l`，§11.5 口径）
- 本页的「语法 / 参数」节与「报错条件」节是脚本从这一篇抽的（**本页一个字没动**）。

**本页没做的**：

- **`DSCP` 那一篇没读。** 所以：`16` 是默认值还是硬上限、**能不能改、在哪改**、
  改了以后 `WSUS` 的上界跟着怎么走——**本页一个字都没有**。
  本页只保证「本篇写了 `as set by DSCP` 与 `the default is 16, the maximum is 16`」。
- **`Timing Setup Commands` 那一篇没读。** 本篇只在 `## Application` 里给了它的标题。
  **所以「WSUS 在 timing setup 流程里排第几步」本页没有。**
- **图 0 张。** 实测 `![` / `<img` / `.png` / `.jpg` / `.gif` / `raw/` 六种写法在本篇
  **全部 0 命中**。**所以本页没有任何来自图的结论**——
  **这张「没有图」是查过的事实，不是「够不着」。**
- **没有在机台上跑过** `WSUS` / `WSUS?`（`verified: doc-only`）。
  **「设完 3 之后是不是真的只剩 3 个 set」本页只能保证「文档这么写」（§11）。**
- **本篇没有 `## Warnings` 段**，所以「报错条件」节里只有 `## Errors` 的两条——不是漏写。

### §10 重复投放：本篇在语料里有**三份**（本页查过）

| 路径 | `source_topic` | 字节 | 与**本页这一份**的正文 |
|---|---|---|---|
| `02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`（**本页的出处**） | `98878.htm` | 1,986 | — |
| `02.06_Command_Reference/02.06.06.02.46_WSUS__WSUS__-__Waveform_Sets_USed.md` | `98878_2.htm` | 1,987 | **`diff` 报 0 行差异（正文逐行相同）** |
| `02.08_Setup_and_Result_Tools/02.08.04.34.02.02.46_WSUS__WSUS__-__Waveform_Sets_USed.md` | `98878_3.htm` | 2,079 | **`diff` 报 12 行差异——两份正文不一样** |

**本页的结论全部只来自第一份**（`98878.htm`）。
**第三份多了什么、少什么，本页没看**——按 §12 不越取材边界
（本页只比了字节数与 `diff` 行数，**没有读它的正文**）。
**记这一条的用处**：按 §10，遇到「两篇说法不同」时先做这一步；
**本篇恰好有一份正文不同的孪生，所以「WSUS 到底说什么」这个问题，语料里有两个答案。**

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
> **① 同一个数字被三种口径指称。** 逐字并列：
>
> - 标题与正文：`WSUS (Waveform Sets USed)`、`the number of defined waveform sets`
> - `WSUS?` 那一句：`the number of waveform sets currently defined`
> - `## Example` 的说明：`This example sets the number of used waveform sets to 3.`
> - 参数释义：`the highest number currently allocated to a waveform set`
>
> **`defined`（定义了几个）与 `used`（用了几个）在英文里不是一回事**，
> 而这条命令的缩写写的正好是 `USed`。**本篇没有说这两者是同一件事**——
> **本页把它们并列照记，不替它统一。**
> **② `the default is 16, the maximum is 16`**——**默认值等于最大值**，本篇就是这么写的，
> **本页照抄，不替它解释**（它到底是「默认就开到顶」还是别的意思，**语料未写**）。
> **③ 坏字：本篇 0 个。** 照 §11.2 ① 那条判据（**英文文档里出现任何汉字，都是坏字**）
> 逐字查过：**本篇一个汉字都没有**——
> **但这是「本页读到的」，不是「本篇没有」**（§13.1：没找到 ≠ 没有）。

`verified: doc-only`
