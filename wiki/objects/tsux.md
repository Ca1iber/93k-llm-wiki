---
type: object
title: TSUX, TSUX? - (Timing Sets Used eXtended)
layer: L1
stage: timing
tags: [timing, timing-set, tsux, l1-command, firmware-command, system-only, test-flow-optimizer]
related: [tsus, wsus, waveform-set, timing]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.284_TSUX__TSUX__-__Timing_Sets_Used_eXtended.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# TSUX, TSUX? - (Timing Sets Used eXtended)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **423 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.284_TSUX__TSUX__-__Timing_Sets_Used_eXtended.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### TSUX

```

TSUX {waveform_set},{timing_set}
```

### TSUX?

```

TSUX? {waveform_set}
```

returns:

```
TSUX {waveform_set},{timing_set}
```

### Parameters

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98818.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 3 列。
> 首行（上游原文）：waveform_set | Waveform set number. Enter ALL for all waveform sets in the query command.
> 表内引用（1 条，供检索）：`TSUS`（raw: `02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`）

<!-- 语法节 end -->

## 是什么

**TSUX 是一条「你多半不该执行、但该看得懂」的命令**——它是给系统用的。
原文第一段就是整页最重要的一段：

> 「The TSUX (Timing Sets Used eXtended) command is only for use by the system, not the user. Do not attempt to execute it from the hpt utility! You may execute the query. The following information is provided to improve your understanding of any hpt output listings you may make.」

**四条信息，一条比一条硬**：

| 信息 | 原文 |
|---|---|
| **只给系统用** | `only for use by the system, not the user` |
| **别在 hpt 里执行它**（带感叹号） | `Do not attempt to execute it from the hpt utility!` |
| **但查询可以执行** | `You may execute the query.` |
| **写这一篇是为了让你看懂 hpt 的输出** | `The following information is provided to improve your understanding of any hpt output listings you may make.` |

**所以本篇的定位不是「教你怎么用」，是「教你怎么读你看到的东西」。**
**本页照这个定位写：`TSUX` 是「知道就好」，`TSUX?` 是「可以查」。**

### 它存在的理由：给「优化过的 timing set」留一份原始数

> 「During test flow optimization the TSUX command is used internally by the Test Flow Optimizer to generate additional (optimized) timing sets. The TSUS? query returns the number of all timing sets, including those that are optimized. Thus TSUX? is used to return the original number of timing sets, that is, those before optimization. The Test Flow Executor then calculates the number of optimized timing sets.」

**这一段把三个角色摆清楚了**，是理解 TSUX 的唯一入口：

| 角色 | 干什么 |
|---|---|
| **Test Flow Optimizer** | **内部**用它**生成额外的（优化过的）timing set** |
| **`TSUS?`（[[tsus]]）** | 回**全部** timing set 的个数，**包含优化出来的那些** |
| **`TSUX?`（本篇）** | 回**原始的**个数，**即优化之前的那些** |
| **Test Flow Executor** | **自己算出**优化后的 timing set 个数 |

**一句话记法：`TSUS?` 数是「现在一共有几个」，`TSUX?` 数是「优化之前有几个」。**
**两个数不一样，差别就是优化出来的那些。**
**而「多了几个」不是哪一个查询直接回的**——原文说的是
`The Test Flow Executor then calculates the number of optimized timing sets.`
**是 Executor 算的，不是命令回的。**

**还有一条总开关**：

> 「The command is not active unless optimized test flows are used.」

**没在用 optimized test flow 时，这条命令不生效。**

### 上下限关系：**TSUX 被 TSUS 夹住**

参数节 `timing_set` 那一格是本篇第二条硬规则，逐字：

> 「Timing set number. In the command, TSUX is set to this value for the specified waveform set, if the number is smaller than the current value of TSUS for this set. Otherwise, it is set to the current value of TSUS.」

**把它拆成两条分支**（这就是本页最该记住的一条）：

| 你给的值 | 结果 |
|---|---|
| **小于**该 waveform set 当前的 `TSUS` 值 | **就用你给的值** |
| **不小于**（等于或大于） | **被改成 `TSUS` 的当前值** |

**即 `TSUX ≤ TSUS` 恒成立**——**给大了不报错，是被夹到 `TSUS` 上。**
**注意条件写的是 `smaller than`（严格小于），不是 `less than or equal`**：
**给一个等于 `TSUS` 的值，走的是第二条分支**（结果一样，但读原文时别读成「可以相等」）。
**本篇没有 `## Errors` 段**，**所以「超出 `TSUS`」在本篇里不是一个错误情形，是一个被夹掉的输入。**

### 两个特殊参数值：`SWAP` 与 `NONE`

> 「This command parameter causes the values set by TSUSand TSUX to be switched, that is, TSUS is set to the current value of TSUX , and TSUX to that of TSUS for the specified waveform set.」

> 「This command parameter sets the value of TSUX back to 1 for the specified waveform set.」

| 值 | 做什么 |
|---|---|
| **`SWAP`** | **把 `TSUS` 与 `TSUX` 的值对调**（`TSUS` ← TSUX 的当前值；`TSUX` ← TSUS 的当前值），**按指定的 waveform set** |
| **`NONE`** | **把 `TSUX` 置回 `1`** |

**`SWAP` 的写法要连着读**：`TSUS is set to the current value of TSUX , and TSUX to that of TSUS`
——**后半句省略了动词**（`TSUX [is set] to that of TSUS`），**而且 `TSUX` 与逗号之间多一个空格**。
（原文如此，见「出处」⚠️②。）

**`NONE` 置回的是 `1`，不是 `0`**——**与 [[tsus]] 那一篇里
「上电时只有一个 timing set」那条一致**（**这一处对照说的是「读到的另一页」，
不是本篇的原文**）。

### ⚠️ `SWAP` 与 `NONE` **在语法式里没有位置**

这是本页发现的最实在一处缺口。两条语法式逐字是：

```
TSUX {waveform_set},{timing_set}
```

```
TSUX? {waveform_set}
```

**两格连着写、没有 `[,mode]` 之类的可选位**。
**而 `SWAP` / `NONE` 是参数表里两个有名字的条目**——
**它们该写在哪里，本篇一个字没说**（**语料未写**）。
**本页不替它补一个位置**（比如「第二格改写成 `SWAP`」这种）——
**那是编的，不是文档的。**
（**推断**：从语法式看，`{timing_set}` 那一格是唯一的可变位置，
所以 `SWAP` / `NONE` 最可能是**填在那一格**——**但这只是本页的猜测，
原文没有任何一句支持它，所以不能当用法写。**）

### 两格参数各自说什么

| 参数 | 原文 |
|---|---|
| `waveform_set` | 「Waveform set number. Enter ALL for all waveform sets in the query command.」 |
| `timing_set` | 见上；**它是唯一有夹取规则的** |

**`ALL` 只在查询里有**（`in the query command`）——
**命令那一半没有 `ALL`，这与 [[tsus]] / [[wsus]] 那一族的写法一致。**
**语法式的返回式与写入式逐字相同**（`TSUX {waveform_set},{timing_set}`）。

## 典型用法

**先说范围**：本篇**没有 `## Procedure`、没有 `## Before you begin`**。
`## Application` 一节全文只有两个词：

> 「Optimized testflows.」

**就这一句。** 没有 `## Examples`，**所以本篇一个示例都没有**——
**本页不复述任何「怎么用」的步骤，因为本篇没写。**

**1. 该不该执行它：**

| 你想干的事 | 能不能做 |
|---|---|
| **查**（`TSUX?`） | **可以**——原文：`You may execute the query.` |
| **改**（`TSUX`） | **不要**——原文：`Do not attempt to execute it from the hpt utility!` |

**2. 前置条件**：**只有在用 optimized test flow 时它才 active**
（`The command is not active unless optimized test flows are used.`）。
**不在用的时候去查会得到什么，本篇没写**（**语料未写**）——**既没说报错，也没说回 0。**

**3. 什么时候会想查它**：原文给了唯一一个场景——
**你手上有一份 hpt 的输出，想看懂它**
（`to improve your understanding of any hpt output listings you may make`）。
**这时 `TSUX?` 给你的是「优化之前有几个 timing set」**，
**而 [[tsus]] 的 `TSUS?` 给你的是「现在一共几个」**；
**两个数一比，差就是优化加进去的。**

**4. 查回来发现数不对时的排查顺序**（**顺序本身是建议**）：

1. **是不是根本没在用 optimized test flow**——那它不 active。
2. **你给的 `timing_set` 是不是 ≥ 当前的 `TSUS`**——是的话**它被夹到 `TSUS` 了**，不是你写的那个数。
3. **你要的是「优化后」的数还是「优化前」的**——**要优化后的那个，本篇不给你**，
   原文说那是 `The Test Flow Executor` 算的。

## 和谁有关

- [[tsus]] — **上游，也是本篇存在的理由（前置）**。
  本篇**三次**点名它：正文那句 `The TSUS? query returns the number of all timing sets`、
  参数节 `timing_set` 那一格的夹取规则、以及 `SWAP` 那一格。
  **两篇的分工是本页最值得记的一条**：
  [[tsus]] 的 `TSUS?` 数**全部**（含优化出来的），本篇的 `TSUX?` 数**优化之前的**。
  **[[tsus]] 那一页在本页建出来之前，给 `tsux` 这个链接只写了「只有名字」——
  因为写那一页时本篇的定义文档还没人读。本页把这一侧补上了**
  （**这一句说的是「读到的另一页的状态」，不是本篇的 raw。**）。
- [[wsus]] — **同族的另一条 `xxUSed` 命令（并列）**。
  **本篇没有点名 `WSUS`**——**「`WSUS` / `TSUS` / `TSUX` 是一族」这个说法来自
  这一族命令的名字形状与 [[tsus]] 那一页，不是本篇的原文。**
  `WSUS` 管的是**waveform set 的个数**，与 timing set 的个数是两笔账。
- [[waveform-set]] — **第一格指的东西（前置概念）**。
  本篇只说 `Waveform set number`，**不说它是什么、怎么建**。
  （**`waveform-set` 在清单里，所以本页链它；它还没有页**。）
- [[timing]] — **`stage: timing` 的依据**（frontmatter；§6：`stage` 填最近的一段，不是归属）。

**本篇点到名字、本页没读的还有三处**：

- **`Test Flow Optimizer`** —— 内部用 TSUX 生成优化过的 timing set。**没有专页，用反引号。**
- **`Test Flow Executor`** —— 自己算出优化后的 timing set 个数。**没有专页，用反引号。**
- **`hpt utility`** —— 原文两次提到它（`Do not attempt to execute it from the hpt utility!`
  与 `any hpt output listings`），**但它是哪一个工具、怎么用，本篇一个字没有**。

**本页没有引用 `edges.jsonl` 的入边/出边数字**（没读边数据，故不报条数）。

## 版本

**本文档有 `## Functional changes` 段，段里只有一条**：

- `Introduced before SmarTest 6.3.2`

> **这一条是 §11.2 ② 说的哨兵值，不是「6.3.2 新增了 TSUX」。**
> 措辞是 `before`，意思是「**在本套文档集覆盖范围开始之前就已经有了**」。
> **只可以说：7.10.3 上有它，而且它比 6.3.2 更老** → [[smartest-6.3.2]]。
> **不许把它读成「6.3.2 引入了 TSUX」。**

**版本段里没有的东西（照实记，不替它补）**：没有第二条。
**所以「optimized test flow 是哪一版引入的」「`SWAP` / `NONE` 是哪一版加的」
「`TSUX` 被标成 `only for use by the system` 是哪一版起的」在本篇里查不到。**

> **一条读法上的提醒**：本篇的版本比它的上游还「薄」——
> **它只说了 `Introduced before SmarTest 6.3.2`，没有一条与 optimized test flow 相关的变更记录**，
> **而正文里 `optimized test flow` 是它成立的前提。**
> **所以「这个前提是哪一版有的」在本篇里查不到**（**语料未写**）。

## 出处

`sources:` 一篇：

- `02_System_reference/02.06_Command_Reference/02.06.02.02.284_TSUX__TSUX__-__Timing_Sets_Used_eXtended.md`
  （frontmatter 的 `source_topic` 是 `98818.htm`；**1,786 字节 / 79 行，整篇读完**——
  字节按 `st_size`、行数按 `wc -l`，§11.5 口径）
- 本页的「语法 / 参数」节是脚本从这一篇抽的（**本页一个字没动**）。

**本页没做的**：

- **本篇没有 `## Errors` / `## Warnings` 段**，所以**本页没有「报错条件」节**
  ——**那是骨架按结构就不建这一节，不是漏写。**
  **顺带一条**：正因为没有报错段，**「`timing_set` 给大了会怎样」的答案只能从参数表里读**
  ——**它不是一个错误，是一个夹取**（见「是什么」）。
- **本篇没有 `## Examples` 段。** 所以**本页里没有一个来自示例的结论**——
  **「`SWAP` / `NONE` 怎么写」本页答不了**（见「是什么」那一节的 ⚠️）。
- **文档里点到的三处都没读**（也没有页）：`Test Flow Optimizer`、`Test Flow Executor`、
  `hpt utility`。所以：**optimized test flow 怎么开、优化出来的 timing set 从哪看、
  hpt 的输出长什么样——本页一个字都没有。**
- **`TSUS` 那一篇的 raw 不在本页的 `sources:` 里**——
  本页关于 [[tsus]] 的说法**全部只引用本篇自己的句子**；
  「两篇的分工」那一条是**本页对本篇那一段的归纳**。
  **`[[tsus]]` 那一页里写了什么，见那一页，本页不为它背书。**
- **图 0 张。** 实测 `![` / `<img` / `.png` / `.jpg` / `.gif` / `raw/` 六种写法在本篇
  **全部 0 命中**。**所以本页没有任何来自图的结论**——
  **这张「没有图」是查过的事实，不是「够不着」（§11.4）。**
- **没在机台上跑过 `TSUX` / `TSUX?`**（`verified: doc-only`）。
  **所以「`TSUX?` 在没开优化时到底回什么」本页答不了（§11）**——
  **文档只说它 `not active`，没说 `not active` 是什么表现。**

### §10 重复投放：本篇在语料里有**三份**（本页查过）

| 路径 | `source_topic` | 字节 | 与**本页这一份**的正文 |
|---|---|---|---|
| `02.06_Command_Reference/02.06.02.02.284_TSUX__TSUX__-__Timing_Sets_Used_eXtended.md`（**本页的出处**） | `98818.htm` | 2,156 | — |
| `02.06_Command_Reference/02.06.06.02.33_TSUX__TSUX__-__Timing_Sets_Used_eXtended.md` | `98818_2.htm` | 2,157 | **把篇内相对链接的前缀归一化后，`diff` 报 0 行差异** |
| `02.08_Setup_and_Result_Tools/02.08.04.34.02.02.33_TSUX__TSUX__-__Timing_Sets_Used_eXtended.md` | `98818_3.htm` | 2,249 | **同上——0 行差异** |

**三份的差别只有两处**：① frontmatter 的 `source_topic` / `source_html`；
② **篇内相对链接的前缀**（第三份多一层 `../02.06_Command_Reference/`，字节数差的就是它）。
**本页的结论全部只来自第一份**；另两份只核了 frontmatter、字节数与 `diff` 行数，
**没有读它们的正文**（§12 不越取材边界）。

### 上游 `.htm` 核对（2026-09-24 做，这是本页**多出来的**一步）

**下面两条本页全去上游 `F:\master-dev\dorm-wsl-sytest\tdc-html\raw\98818.htm`（6,031 字节）核过。
结论：都是「上游就坏的」（§11.2 ⑥）——重做一次转换也救不回来。**

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> **① `SWAP` 与 `NONE` 在语法式里没有位置**（**这不是错字，是一处缺口**）。
> 参数表里逐字有这两条——**`SWAP` 那一格**写的是：
>
> > 「This command parameter causes the values set by TSUSand TSUX to be switched, that is, TSUS is set to the current value of TSUX , and TSUX to that of TSUS for the specified waveform set.」
>
> **`NONE` 那一格**写的是：
>
> > 「This command parameter sets the value of TSUX back to 1 for the specified waveform set.」
>
> **而两条语法式是 `TSUX {waveform_set},{timing_set}` 与 `TSUX? {waveform_set}`，
> 都没有第三个位置。**
> **上游核对**：`98818.htm` 里语法块与参数表就是这样，**参数表有两个具名条目、
> 语法式只有两格** → **上游就缺。本页照记，不替它补位置。**
>
> **② 两处少空格 / 多空格。** 原文逐字（`SWAP` 那一格）：
> `This command parameter causes the values set by TSUSand TSUX to be switched, that is, TSUS is set to the current value of TSUX , and TSUX to that of TSUS for the specified waveform set.`
> **两处**：① `TSUSand`——**`TSUS` 与 `and` 之间少一个空格**；
> ② `TSUX , and`——**逗号前多一个空格**。
> **上游核对**：`98818.htm` 里就是
> `<a href="98817.htm"` 之后接 `>TSUS</a>and TSUX to be switched, that is, TSUS is set to the current value of TSUX , and`
> ——**标签边界与逗号位置都是上游的写法** → **上游就坏的。本页照抄，没加空格、也没删空格。**
>
> **③ 坏字：本篇 0 个。** 照 §11.2 ① 那条判据（**英文文档里出现任何汉字，都是坏字**）逐字查过：
> **本篇一个汉字都没有**——**但这是「本页读到的」，不是「本篇没有」**（§13.1：没找到 ≠ 没有）。

`verified: doc-only`
