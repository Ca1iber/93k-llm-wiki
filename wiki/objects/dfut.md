---
type: object
title: DFUT, DFUT? - (DeFine UTility line)
layer: L1
stage: pin
tags: [dfut, l1, firmware-command, pin, utility-line, utility-card, safety-line, exa-scale, xps256]
related: [pin, command-reference, utility-lines, utility-line-assignments, dut-interface-layout, utility-pogo-block-utility-card-v93000-exa-scale-systems, utility-card, xps256-status-flags, pals, dfup, upas, dfpr, pslv, smartest-7.10.3]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.70_DFUT__DFUT__-__DeFine_UTility_line.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

> ⚠️ **本页若干处记的是 2026-10-10【之前】的语料形态。**
> 那一轮把语料里的表格一律换成了**指向上游 HTML 的指针**
> （见 `extract/PLAN-表格指针化.md`）。所以下文凡是说「表格被压平 / 被摊平 /
> 一格一行」的地方，指的是**更换之前**的样子 —— 现在语料里那个位置是**一句指针**，
> 真表仍在 `tdc-html/raw/` 的上游 HTML 里。**页码/引文都不受影响。**

# DFUT, DFUT? - (DeFine UTility line)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **561 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.70_DFUT__DFUT__-__DeFine_UTility_line.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### DFUT

```
DFUT {ch_No}, {type}, {(util_name)}
```

### DFUT?

```
DFUT? {(util_name)}
```

returns

```
DFUT {ch_No}, {type}, {(util_name)}
```

### Parameters

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98560.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：ch_No | Channel number of the utility line specified with five or three digits. In the five‑digit format, the first three digits specify the utility pogo block.…

### Example

```
DFUT 16504,w,(filter)
```

This example assigns the name `filter` and operating mode w to utility line 4 of the first utility pogo block.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.70_DFUT__DFUT__-__DeFine_UTility_line.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

- The channel number is out of range.
- The channel number is already used.
- The utility line name is out of range.
- The utility line name is already assigned to an analog or digital pin.

<!-- 报错节 end -->

## 是什么

**`DFUT`（DeFine UTility line）只做两件事：给一条 utility line 起一个符号名、定它的方向。**
原文前三句把「本命令的产物 / utility line 是什么 / 下游是谁」一口气讲完：

> 「The DFUT command defines a symbolic name and an operation mode for a utility line.」

> 「Utility lines allow you to control external devices such as relays, solenoids or indicators, depending on the application. The utility lines are implemented as open drain output with a maximum current of 100 mA and a maximum voltage of about 5.0 V.」

> 「The definition made by command DFUT can be used by the UTST command to set or read the status of the utility line.」

| 句 | 说的是什么 |
|---|---|
| 第 1 句 | **产物是两样**：`util_name`（符号名）+ `type`（工作模式），都挂在同一条 utility line 上 |
| 第 2 句 | **utility line 是干什么的**：去控制外部器件（relay / solenoid / indicator）；电气上是 **open drain 输出**，上限 **100 mA**、约 **5.0 V** |
| 第 3 句 | **下游是 `UTST`**：这里定义出来的名字，由 `UTST` 拿去**设状态 / 读状态** |

**要紧的是第 3 句：本命令自己不动任何硬件。** 它只是「命名 + 定方向」，
**真正把线拉高拉低的是 `UTST`**——这条分工是原文给的，不是推断。
（反过来也成立：**没有 `DFUT` 定义过的线，`UTST` 就没有名字可用**——**这一半是本页的推断**，
依据是第 3 句的 `The definition made by command DFUT can be used by the UTST command to set or read the status of the utility line.`
与 `util_name` 那格「名字由本命令定义」。**本篇没有正面写「未定义的名字会怎样」**。）

### 三段语法：名字、方向、通道

| 段 | 参数 | 原文对它的说明 |
|---|---|---|
| 1 | `ch_No` | 通道号，**五位或三位**（两套写法，见下） |
| 2 | `type` | 工作模式：`W` / `R` / `RW`；Utility Card 上另有四个 `TRIGGER_*` 关键字 |
| 3 | `util_name` | 名字；查询里写 `@` 可列全部已定义的线 |

**`DFUT` 与 `DFUT?` 的语法行是同一形状**（`DFUT?` 只是少了 `ch_No` 与 `type` 两段）：

> 「For the query, it specifies the utility line name to be retrieved. @ can be used to list all defined utility lines.」

**即：查询里 `util_name` 的位置可以写 `@`。** 但**原文没给 `@` 的命令行例子**，
所以本页只写「那一位写 `@`」，**不替它编一条完整命令**。

### `ch_No`：五位数与三位数两套写法

> 「Channel number of the utility line specified with five or three digits.」

| 格式 | 前几位说什么 | 后两位说什么 | 原文 |
|---|---|---|---|
| **五位数（现行）** | **前三位 = utility pogo block** | 通道号 | `In the five鈥慸igit format, the first three digits specify the utility pogo block.` |
| **三位数（legacy）** | **首位 = utility pogo block，取值 `1 ... 8`**（对应 `UTIL鈥? ... UTIL鈥?`） | 通道号 | `In the legacy three鈥慸igit format, the first digit (1 ... 8) specifies the utility pogo block UTIL鈥? ... UTIL鈥?.` |

**两种格式的后两位都是通道号，取值一样**：

> 「The last two digits specify the channel number 01 ... 32 of the utility line.」

**读回来一律是五位**——这条对 `PALS?` 同样成立：

> 「When reading the defined utility lines with the DFUT? command, the data returned always have the five鈥慸igit format. The same applies to the PALS? command.」

**还有一套编号：命令里的通道号与 pogo block 上印的号差 1。**

> 「On the utility pogo blocks, an offset of -1 is to be considered and the channel number is URW00 ... URW31.」

| 同一个通道 | 命令里（`ch_No` 后两位） | pogo block 上 |
|---|---|---|
| 第 1 条 | `01` | `URW00` |
| 第 32 条 | `32` | `URW31` |

（上表两端是**由 `an offset of -1` 直接算出来的**，不是原文另写的对应表。）

> ⚠️ **上面两条引文里的 `鈥慸` 与 `鈥?` 是语料坏字，本页照原样引**（见「出处」⚠️）。
> `five鈥慸igit` 的正字是 **`five-digit`**、`three鈥慸igit` 是 **`three-digit`**；
> `UTIL鈥? ... UTIL鈥?` 的正字是 **`UTIL‑1 ... UTIL‑8`**（那根短横是 U+2011）。
> **拿正字去 raw 里搜是搜不到的**——`digit` 也搜不到（`d` 被坏字吃掉了）。

### `type`：三个方向，外加四个 `TRIGGER_*` 关键字

**三个方向是本命令的常规取值**，逐字：

> 「Specifies the operating mode of the utility line with the following specifiers:」

> 「- W: Write-Only」

> 「- R: Read-Only」

> 「- RW: Read-Write」

**另外四个关键字只在装了 Utility Card 时才有意义**，逐字：

> 「Utility lines of the optional Utility Card can also be configured as safety lines or as global shutdown line for hardware鈥慶ontrolled shutdown of XPS256 pins:」

| 取值 | 原文的定性 |
|---|---|
| `TRIGGER_IF_HIGH` | `Safety line` |
| `TRIGGER_IF_LOW` | `Safety line` |
| `TRIGGER_SITE_IF_HIGH` | `Global shutdown line` |
| `TRIGGER_SITE_IF_LOW` | `Global shutdown line` |

**即：utility line 在 Utility Card 上可以被配成一条「安全线 / 全局关断线」**，
作用是 `hardware鈥慶ontrolled shutdown of XPS256 pins`。
细节原文推给了另一篇：`For more information, refer to XPS256 safety line and DUT board disconnect.`
（那篇**本页没读**，见「出处」。）

### `util_name`：16 个字符，而且不许撞 pin 名

> 「Name of the utility line.」

> 「This parameter can have up to 16 alphanumeric characters and must not contain blank spaces, or any of the following characters: # ; ( ' ' ) ? @ ,」

| 规则 | 值 |
|---|---|
| 长度 | 最多 **16 个字母数字字符**（`alphanumeric`） |
| 不许有 | **空格** |
| 不许有 | `#` `;` `(` `'` `'` `)` `?` `@` `,`（**原文逐字如此**，见「出处」⚠️ ②） |

**`@` 被列进了禁用字符，却在查询里当通配符用**——两处说的是不同位置
（不许出现在**名字里**；出现在**查询的那一位**上才是「列全部」）。**原文没有解释这一点**，
本页只把两处并列。

**名字还和 pin 名共用一套命名空间**（**推断**，依据是报错条件里那条
`The utility line name is already assigned to an analog or digital pin.`——
「已经分给了 analog/digital pin」意味着一个名字不能同时是 pin 名和 utility line 名）。

### 例子：`DFUT 16504,w,(filter)`

```
DFUT 16504,w,(filter)
```

> 「This example assigns the name filter and operating mode w to utility line 4 of the first utility pogo block.」

**把例子的号拆开对回去**（按上面五位数那条规则）：

| 段 | 值 | 说明 |
|---|---|---|
| pogo block | `165` | 五位数的**前三位** |
| 通道 | `04` | 五位数的**后两位**，即「utility line 4」 |
| `type` | `w` | 原文小写（见下） |
| `util_name` | `filter` | — |

**原文说 `165` 这个块是「the first utility pogo block」**——这与三位数那条规则对得上
（legacy 首位 `1` = `UTIL‑1` = 第一个块），**但「`165` 的首位 `1` 就是那个 1」这一步是本页的推断**，
**本篇没有写这句话**。

> **⚠️ 例子里的 `w` 是小写，而取值表里写的是大写 `W`。** 原文两处**逐字如此**：
> 取值表 `- W: Write-Only`，例子 `DFUT 16504,w,(filter)` 与其说明 `operating mode w`。
> §11 说**命令大小写敏感、原样保留**——**本页两处各照各的引，不替它统一，也不判哪个对。**

## 典型用法

**本篇没有 `## Procedure` / `## Before you begin` / `## What to do next`**——
用法全部来自 `## Example` 一条、`## Parameters` 那张表、以及正文前两句。
**顺序是死的：先 `DFUT` 定义，之后才谈得上拿 `UTST` 去动这条线。**

| 要做的事 | 怎么写 | 依据 |
|---|---|---|
| **定义一条 utility line** | `DFUT {ch_No}, {type}, {(util_name)}` | 语法（逐字在「语法 / 参数」节） |
| 按名字读一条的定义 | `DFUT? {(util_name)}` | 同上 |
| **列出全部已定义的线** | 查询里 `util_name` 那一位写 `@` | `@ can be used to list all defined utility lines.`——**原文没有给命令行例子** |
| 定义完去动这条线 | 用 `UTST`（**未建页**，见「和谁有关」） | 「The definition made by command DFUT can be used by the UTST command to set or read the status of the utility line.」 |
| 一次定义多条 / 一次定义多个名字 | **语料未写** | — |
| **撤掉一条定义（un-define）** | **语料未写** | 本篇**没有任何删除语法**，也没有「重复定义同名会怎样」的写法 |

**三条容易踩的约束，都来自「语法 / 参数」节**（本页只把后果说清）：

1. **号要对**：`ch_No` 是五位或三位，**不是随便一个整数**；
   五位的前三位是 pogo block、后两位才是通道号。
2. **名字要合规**：≤ 16 个字母数字字符、无空格、不含那九个禁用字符。
3. **名字不许撞**：不能和已分配的 analog / digital pin 名相同（那是报错条件之一）。

**归属**：原文 `## Application` 一节全文只有一句——
`For details about utility lines, see Configuration Setup Commands.`
（`Configuration Setup Commands` 那篇**本页没读**。）

**出错时**：四条报错条件在下面「报错条件」节（脚本从原文 `## Errors` 逐字取）。
本页不重复那四条，只提醒一句：**它们按「通道」和「名字」分成两组**
（通道号越界 / 通道已占用；名字越界 / 名字已被 pin 占用）——**两组各查各的**。

## 和谁有关

- [[pin]] / [[command-reference]] —— **归属**：`stage: pin` 依据是 `## Application` 指向
  `Configuration Setup Commands`（配置类命令章）；doc 本身在 `02.06_Command_Reference` 下。
  （§6：`stage` 填的是「**最近的一段**」，不是归属。）
- [[utility-lines]] / [[utility-line-assignments]] / [[dut-interface-layout]] ——
  **上游的号从哪来**：原文在 `ch_No` 那格里**两次**指向它们
  （`For valid pogo blocks, refer to DUT interface layout and to Utility pogo block mapping in Utility pogo block - Utility Card (V93000 EXA Scale systems).`
  与 `For more information, see Utility line assignments and DUT interface layout`）。
  **本页没读这三篇。**
- [[utility-pogo-block-utility-card-v93000-exa-scale-systems]] ——
  **五位格式里「合法的 pogo block」的清单在这篇里**（原文点名的 `Utility pogo block mapping`
  是它的一节）。**本页没读。**
- [[utility-card]] —— **那四个 `TRIGGER_*` 关键字只对它上面的线有效**
  （原文：`Utility lines of the optional Utility Card`）。**本页没读。**
- [[xps256-status-flags]] —— **同一条「安全线」的两端**：`DFUT` 这一侧把线**配成**
  safety line / global shutdown line，XPS256 那一侧把它**报成状态标志**
  （那页的 `Safety line` / `DUT board disconnect` 两个标志写的是「从正确配置的 trigger source
  收到 shutdown 信号」）。**（推断）**，依据是两篇各自的措辞 + 本篇那句
  `For more information, refer to XPS256 safety line and DUT board disconnect.`；
  **本篇没有直说这两件事是一条链**。
- [[pals]] —— **同类命令**：原文在讲「读回来一律五位」时**点名它**
  （`The same applies to the PALS? command.`）。**本页没读它。**
- [[dfup]] / [[upas]] —— **同族，但本篇一个字没提**（实测 `DFUP` / `UPAS` 0 命中）：
  `DFUT` 定义**单条** utility line，`DFUP` 定义 utility purpose（**一组**线），
  `UPAS` 再给多 site 赋不同状态。**这一句的依据不是本篇**，是本批另一页的原文
  `02.06.02.02.304_UPAS__UPAS__-__Utility_Purpose_ASsignment_for_multi-site.md`
  （它开头写 `The utility purpose must have been defined with the DFUP command.`）——
  **所以这是一条跨篇的（推断），不是 `DFUT` 自己说的**。`DFUP` 的原文**本页没读**。
- `UTST`（**未建页、且不在 allowlist 里**）—— **下游**：原文第 3 句点名的命令，
  「设状态 / 读状态」都在它那里。**本页没读它，所以 `UTST` 的语法本页一个字没有。**
- `Configuration Setup Commands` / `XPS256 safety line and DUT board disconnect`
  （**均未建、且不在 allowlist 里**）—— 原文指定的两处「详情在这」。

## 版本

本文档**有** `## Functional changes` 段，三条，**逐字**：

| 条目 | 和正文对得上吗 |
|---|---|
| `Introduced before SmarTest 6.3.2` | **是 §11.2 ② 的哨兵值**，见下① |
| `SmarTest 7.10.1: Three-digit utility pogo block designator on V93000 EXA Scale systems.` | **与正文的措辞相撞**，见下② |
| `SmarTest 7.10.2: New keywords for the type parameter to configure shutdown of XPS256 pins using utility lines.` | **对得上**：正文里那四个 `TRIGGER_*` 关键字就是它 |

**① `Introduced before SmarTest 6.3.2` 不是「6.3.2 的变更」。** 按 §11.2 ②，
它是「**早于本文档集覆盖范围**」的哨兵——**所以 `DFUT` 究竟成立于哪个版本，这份语料里没有。**

**② 两个 `three-digit` 说的不是同一件事，本页并列，不替它们调和。**
版本段写的是 **`Three-digit utility pogo block designator`**（**块的号用三位写**），
而正文把**整串 `ch_No` 只有三位的那种写法**叫 `legacy`（**那个 `three-digit` 在正文里带坏字，
见「出处」⚠️ ①，本行不引它**）：

> 「In the legacy three鈥慸igit format, the first digit (1 ... 8) specifies the utility pogo block UTIL鈥? ... UTIL鈥?.」

**两处都用 `three-digit` 这个词，指的东西可能不同**——
按正文那句 `In the five鈥慸igit format, the first three digits specify the utility pogo block` 读，
版本段那条更像是在说「**块号从此要写三位**」（也就是五位总数里的前三位的来源，见下），
而正文那个 `legacy` 说的是「**整串只有三位**」。**原文没说这两句是同一件事，本页不判。**

**③ 一个（推断）的旁证**：版本段把 `Three-digit utility pogo block designator`
挂在 **V93000 EXA Scale systems** 上，而正文 `ch_No` 那格引用的是
`Utility pogo block - Utility Card (V93000 EXA Scale systems)`。
**即「三位块号」是 EXA Scale 的行为**——**依据只是这两处的产品名相同**，
**原文没有把这两句话连起来写。**

**④ 与 wiki 面向版本的关系**：本 wiki 面向 **SmarTest 7.10.3**（[[smartest-7.10.3]]），
而这一篇的版本段**停在 7.10.2**——**7.10.2 之后 `DFUT` 有没有变，语料里没有。**

## 出处

`sources:` 一篇：
`02_System_reference/02.06_Command_Reference/02.06.02.02.70_DFUT__DFUT__-__DeFine_UTility_line.md`
（TDC `98560.htm`；**md 2,446 字节 / 106 行**，上游 htm 9,925 字节）。**整篇读完。**

**本页没做的**：

- **五张相关的文档一张没读**：`DUT interface layout`、`Utility line assignments`、
  `Utility Card`、`XPS256 safety line and DUT board disconnect`、
  `Configuration Setup Commands`。
  **所以：合法的 pogo block 是哪些、utility line 在 DUT 板上怎么走、安全线怎么配、
  那四个 `TRIGGER_*` 具体触发什么——本页一个字都没有。**
- **`Utility pogo block - Utility Card (V93000 EXA Scale systems)` 没读**——
  **五位格式里 pogo block 的合法取值清单在那篇里**（原文点名的 `Utility pogo block mapping`）。
- **`UTST` 没读**——**「定义完之后怎么动这条线」本页没有**；
  本页只有「下游是 `UTST`」这一句原文。
- **`PALS?` 没读**——原文拿它做类比（回读同为五位），本页只引那一句。
- **`DFUP` / `UPAS` 的原文没读**——「和谁有关」里那条同族关系是**跨篇推断**，
  依据写在那一节里。
- **图：本篇没有内嵌图片**——判据可核：本篇 md 里 `.png` / `.jpg` / `![` **0 命中**。
  **所以本页没有任何来自图的结论。**
- **没有实跑。** 没有在机台上发过 `DFUT` / `DFUT?`、没建过 utility line、
  没触发过那四条报错。`verified: doc-only` 说的就是这件事（§11：文档里有 ≠ 这台机器上能用）。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**（§11.2）：
>
> **① 四行里有编码坏字（§11.2 ① 那一族），三种形态。** 逐字（左列的「出处」都是**完整原文片段**，不是截断）：
>
> | 坏字 | 出处（逐字） | 正字 | 吃掉了什么 |
> |---|---|---|---|
> | `鈥慸` | `In the five鈥慸igit format` / `the five鈥慸igit format.` | `five-digit` / `five-digit` | **吃掉了 `d`**（`digit` → `igit`） |
> | `鈥慸` | `In the legacy three鈥慸igit format` | `three-digit` | 同上 |
> | `鈥慶` | `hardware鈥慶ontrolled shutdown of XPS256 pins:` | `hardware-controlled` | **吃掉了 `c`**（`controlled` → `ontrolled`） |
> | `鈥?` | `specifies the utility pogo block UTIL鈥? ... UTIL鈥?.` | `UTIL‑1 ... UTIL‑8` | **一个数字都没剩下**，两处还长成同一个样子 |
>
> **「正字」那一列不是本页猜的**：`five‑digit` / `three‑digit` / `UTIL‑1 ... UTIL‑8`
> 三处**核过上游 `raw/98560.htm`**，那里写的是 U+2011 短横，**完好**——
> **所以这一族是 md 转换时坏的（§11.2 ①），不是上游就坏的。**
> **但正字拿去搜是搜不到的**：`digit` / `controlled` / `UTIL-1` **在本篇里 0 命中**，
> 要搜得搜坏掉的那个形态。`鈥` 是「三字节字符的头两个字节」，**只能定到区间**
> （U+2000–U+203F），**不许当映射用**；`鈥慸` / `鈥慶` 里那个尾巴是被并进去的 ASCII 字母。
>
> **② 禁用字符表里有两个 `'`，而且 `@` 同时在「名里禁用」和「查询里当通配符」两处。** 逐字：
> `must not contain blank spaces, or any of the following characters: # ; ( ' ' ) ? @ ,`
> ——**这一处核过上游 `raw/98560.htm`：htm 里就是 `# ; ( ' ' ) ? @ ,`**
> （§11.2 ⑥ 的判法：上游就坏的，救不回来）。**看着像少了引号和斜杠之类的字符，本页照原样记。**
>
> **③ 例子用小写 `w`，取值表用大写 `W`。** 逐字两处：
> `- W: Write-Only`（取值表）对 `DFUT 16504,w,(filter)`（例子）与
> `This example assigns the name filter and operating mode w to utility line 4 of the first utility pogo block.`
> **§11 说命令大小写敏感——本页两处各照各的引，不替它统一。**
>
> **④ `Related information` 的三个链接粘在一起，中间一个分隔符都没有**（同批的
> [[dfpr]] / [[pslv]] 都记了同一形态）。逐字：
> ```
> [DUT interface layout](<../02.03_DUT_board_design_reference/02.03.03.01_DUT_interface_layout.md>)[Utility line assignments](<../02.03_DUT_board_design_reference/02.03.04.01_Utility_line_assignments.md>)[Utility Card](<../02.05_Test_Head_Cards/02.05.08.04_Utility_Card.md>)
> ```
> ——**三个链接名首尾相接**，不带分隔读起来是一条长名字。
> **核过上游 `raw/98560.htm`：htm 里它们是三个各自独立的 `<div>`，而且各带一个
> `title=` 提示语**（`DUT interface layout` 那条的提示语讲 test head 的卡组合与
> utility line / utility power supplies 的路由）——**所以这是 md 转换时丢了分隔与
> `title=` 属性**（§11.2 ① 那一族：上游是好的）。**本页没有把 `title=` 的文字写进正文**，
> 因为它不在本页的 `sources:` 里，**也不是本页的引文**。
>
> **⑤ `Parameters` 那张表在 raw 里被压平。** 三格说明都散成「一格一行 + 游离 `|`」，
> 逐字起头是：
> ```
>  | ch_No |
> ```
> ——**「语法 / 参数」节里那个孤立的 ` | ` 就是它**（同批 [[dfpr]] / [[pslv]] 同一形态）。
> **说明文字一个字没丢**，但**表头（`Parameter` / `Description` 之类）本篇 raw 里没有**。
>
> **⑥ 本篇没有 `## Warnings` 段**（只有 `## Errors`）。脚本的报错节抬头写的是
> `## Errors` / `## Warnings` 两个段名，**对本篇来说 `## Warnings` 是空的**。

`verified: doc-only`
