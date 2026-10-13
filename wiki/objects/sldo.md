---
type: object
title: SLDO - (Switch Level and Dps Order)
layer: L1
stage: level
tags: [sldo, l1, firmware-command, level, dps, switching-order, test-suite-boundary, report-mode, query]
related: [level, dfps, dscp, dsus, pslv, drlv, rclv, dpspins-resources, command-reference, smartest-6.3.2, smartest-7.10.3, dfut, prlt]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.223_SLDO_-__Switch_Level_and_Dps_Order.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

> ⚠️ **本页若干处记的是 2026-10-10【之前】的语料形态。**
> 那一轮把语料里的表格一律换成了**指向上游 HTML 的指针**
> （见 `extract/PLAN-表格指针化.md`）。所以下文凡是说「表格被压平 / 被摊平 /
> 一格一行」的地方，指的是**更换之前**的样子 —— 现在语料里那个位置是**一句指针**，
> 真表仍在 `tdc-html/raw/` 的上游 HTML 里。**页码/引文都不受影响。**

# SLDO - (Switch Level and Dps Order)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **472 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.223_SLDO_-__Switch_Level_and_Dps_Order.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### SLDO

```
SLDO {order}, [report]
```

### Parameters

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98735.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：9 行 × 3 列。
> 首行（上游原文）：order | This parameter sets the switching order mode:

### Example

```
SLDO CVDL, AMBI
```

This example switches either the DPS voltage values or the level voltage values first when changing from one DPS or level set to the next depending on which of the three above mentioned cases occur and reports any ambiguous case.

<!-- 语法节 end -->

## 是什么

**`SLDO`（Switch Level and Dps Order）选的是「换 set 的那一刻，先动 DPS 电压还是先动 level 电压」。**
原文第一句把时刻、对象、可选项全写在一句里：

> 「The SLDO (Switch Level and Dps Order) command selects one of two switching order modes for switching voltage values of levels or DPS pins when changing from one DPS or level set to the next between two test suites.」

| 原文的措辞 | 说的是什么 |
|---|---|
| `voltage values of levels or DPS pins` | 管的是**两类电压**：level（驱动 / 比较电平）与 **DPS**（供电） |
| `when changing from one DPS or level set to the next` | **触发时刻是「换 set」**——不是测试执行当中 |
| `between two test suites` | 那一刻发生在**两个 test suite 之间** |
| `one of two switching order modes` | **两个模式**：`FDSL` / `CVDL` |

**「为什么要管顺序」这一层，本篇一个字没有。**
本页只给一条**（推断）**：换 set 时两类电压都要变，
**谁先谁后会决定中间那一瞬间 DUT 上看到的是什么**——
依据只有原文那两个措辞（`switching voltage values` 与 `between two test suites`），
**原文没有给任何理由，也没有举后果的例子**。

### `order`：两个模式

| 取值 | 原文逐字 | 行为 |
|---|---|---|
| `FDSL` | `First DPS, second levels. If this parameter is specified, the DPS voltage values are always switched before the voltage values of the levels.` | **永远 DPS 先**（`always`） |
| `CVDL` | `There are three possibilities:` | **看 DPS 电压往哪边走**，见下 |

**`CVDL` 的三条，逐字**：

> 「1. If DPS voltage values are increasing or stable, DPS voltages are switched before level voltages.」

> 「2. If DPS voltage values are decreasing or stable, level voltages are switched before DPS voltages.」

> 「3. If the voltages of some DPS pins are decreasing while the voltages of others are increasing (ambiguous case), DPS voltages are always switched first.」

| # | 条件 | 先动谁 |
|---|---|---|
| 1 | DPS 电压**上升或不变** | **DPS 先** |
| 2 | DPS 电压**下降或不变** | **level 先** |
| 3 | 一部分 DPS 降、另一部分升（`ambiguous case`） | **DPS 先**（`always`） |

> ⚠️ **第 1 条与第 2 条都写了 `or stable`，而两条的结论相反。**
> **DPS 电压「不变」时，两条规则同时命中**——**原文没有说这时按哪条**。
> 这是原文自己的问题（**核过上游 `raw/98735.htm`，上游一字不差**），
> 见「出处」⚠️ ①。**本页并列，不替它调和。**

### `report`：四档，而且是「报什么」不是「做什么」

> 「This parameter sets the report mode, which can be one of the following:」

| 取值 | 原文逐字 | 报什么 |
|---|---|---|
| `ALL` | `Reports a change in the switching order from DPS voltages (first) to level voltages (first) and vice versa.` | **两个方向都报**（DPS 先 ↔ level 先） |
| `FLSD` | `First levels, second DPS. Reports a change in the switching order to switching level voltages first.` | **只报「改成 level 先」这个方向** |
| `AMBI` | `Ambiguous case. Reports an ambiguous case.` | **报 ambiguous case**（对应 `CVDL` 第 3 条） |
| `NONE` | `Nothing is reported. This is the default report mode.` | **什么都不报——这是默认** |

**`report` 不改切换行为**：它管的是**「顺序发生变化时要不要告诉你」**。
**默认是 `NONE`**——**也就是说，除非你显式设 `report`，中间换了顺序你不会有任何提示。**

### ⚠️ `FDSL` 与 `FLSD` 差一个字母顺序，含义相反

**这是本页最该记住的一处，因为两个取值分属两栏、长得极像：**

| 栏 | 取值 | 展开（原文逐字） |
|---|---|---|
| `order` | **`FDSL`** | `First DPS, second levels.` |
| `report` | **`FLSD`** | `First levels, second DPS.` |

**`FDSL` 是「DPS 先」，`FLSD` 是「level 先」——四个字母只是换了位置。**
**一个写在 `order` 里（决定行为），一个写在 `report` 里（决定报什么）**——
**填错栏位不会报错，只会静默地拿到另一件事**（本篇唯一的报错是拼写或语法错，
见「典型用法」最后一段）。

### `operation`：`SLDO?` 的位，只有一个取值

> 「This is the mode of operation. SAVE returns values for everything that can be set.」

**`SAVE` 是本篇唯一写出的取值**，意思是**「把所有可设的东西都回读出来」**
（即 `order` 与 `report` 一起给）。**原文没有解释 `SAVE` 这个名字，也没有列别的取值。**

**注意这一位的归属**：它出现在 `## SLDO?` 那一节底下的 `## Parameters` 里，
**是查询命令的位**，不是 `SLDO` 的位——**而 `## Parameters` 一节把两条命令的位混在一起排**
（见「出处」⚠️ ③）。

### `SLDO?`：查询形态，**不在本页的「语法 / 参数」节里**

原文有完整的查询形式（**逐字，从 `## SLDO?` 那节读出来的**）：

```
SLDO? [operation]
```

returns:

```
SLDO {order}, [report]
```

**这一节没有进本页的「语法 / 参数」节**——那是脚本按段名抽的，
`SLDO` 这一篇的标题里只写了 `SLDO`（没写 `SLDO?`），
所以 `## SLDO?` 那一节没被认出来。**机制写在「出处」⚠️ ④，本页只保证这里的转写逐字。**

**回读形状与写入形状相同**（`SLDO {order}, [report]`），**所以读回来的东西可以直接照着写回去。**

### 例子

```
SLDO CVDL, AMBI
```

> 「This example switches either the DPS voltage values or the level voltage values first when changing from one DPS or level set to the next depending on which of the three above mentioned cases occur and reports any ambiguous case.」

**照位置对回去**：`CVDL` = `order`（按三条规则择先）、`AMBI` = `report`（ambiguous 时报）。

## 典型用法

**本篇没有 `## Procedure` / `## Before you begin` / `## What to do next`**——
用法只有 `## Example` 一条、三段语法的约束、和一句报错。

**1. 写**：`SLDO {order}, [report]`。
`order` **必填**（`FDSL` 或 `CVDL`），`report` **可选**（方括号就是「可选」的意思），
**省略时是 `NONE`**（`Nothing is reported. This is the default report mode.`）。

> **下表右列的写法，除原文那一条例子外，都是本页按语法 `SLDO {order}, [report]` 拼出来的**
> ——**原文只给了 `SLDO CVDL, AMBI` 一条例子**，其余组合原文没有逐一示范。

| 想要什么 | 写什么 |
|---|---|
| **永远 DPS 先** | `SLDO FDSL`（要报的话再加 `,ALL` / `,FLSD` / `,AMBI`） |
| **看电压方向自动择先**（`CVDL`） | `SLDO CVDL` |
| **只想知道「改成 level 先」的时候** | `SLDO {order}, FLSD` |
| **想把 ambiguous case 也报出来** | `SLDO CVDL, AMBI`（**这就是原文的例子**） |
| **默认（不报）** | `SLDO {order}` |

**2. 读**：

| 想读什么 | 写什么 | 依据 |
|---|---|---|
| **当前设定**（`order` + `report`） | `SLDO? SAVE` | `SAVE returns values for everything that can be set.` |
| 只带 `order` 读 | `SLDO?`（`operation` 是可选的） | 语法 `SLDO? [operation]` |

> **`SLDO?` 这两行不在本页的「语法 / 参数」节里**（原因见「是什么」与「出处」⚠️ ④），
> **本页把它们逐字写在上面的「是什么」一节**，这里只给用法。

**3. 什么时候会用到它**：**两个 test suite 之间换了 DPS set 或 level set 的时候**
（原文：`when changing from one DPS or level set to the next between two test suites`）。
**其余时刻这条命令不参与。**

**4. 出错时**：**原文只有一句**，逐字：

`An error is generated if spelling or syntax is wrong.`

**即：本篇没有给任何「取值非法」「状态不允许」之类的条件**——
**拼写和语法之外，本篇没写别的失败情形。**
（**这一句没有出现在本页的「报错条件」节里**——不是本页漏了，原因见「出处」⚠️ ⑤。）

**归属**：原文 `## Application` 一节全文只有一句——
`Level setup, see Level Setup Commands.`

## 和谁有关

- [[level]] —— **`stage: level` 的依据**：原文 `## Application` 那唯一一句
  `Level setup, see Level Setup Commands.`，而 wiki 的 [[level]] 页 `sources:` 里
  **就有 `02.06.05_Level_Setup_Commands.md` 这一篇**（命令参考章的 level setup 章首页）。
  **所以这条归属是核过的，不是从篇名猜的**（§6：`stage` 是「**最近的一段**」，不是归属）。
- [[pslv]] —— **同一个时刻的另一个问题**：`SLDO` 管「**换 set 时两路电压谁先**」，
  [[pslv]] 的 `setup_time` 管「**各 DPS 的建立期结束在同一刻**」。
  —— **这个对照是本页的（推断）**：两篇各说各的一半，**没有任何一篇把两者写在一起**。
  两篇同属 level setup 章（`## Application` 都指向同一章）。
  **这条对照不是从 [[pslv]] 那一页读来的**——**依据是它 `sources:` 里那篇 raw**
  （原文与路径都写在「出处」，**那里标了它属于哪一篇**）。
- [[dfps]] / [[dscp]] / [[dsus]] —— **`DPS set` 这个东西的定义方 / 上限 / 数量**，
  同属 level setup 那一章。**本篇一个字没提它们**（实测 `DFPS` / `DSCP` / `DSUS` **0 命中**）——
  **列在这里是因为「换 set」的前提在它们那里**（**推断**：`SLDO` 只说 `DPS set`，
  而 set 是由那几条命令定义出来的）。**本页三篇都没读。**
- [[drlv]] / [[rclv]] —— **level 那一侧的写值命令**（同批同族）：
  `SLDO` 只管**顺序**，**具体电平值由它们写**。**本篇没有提过它们**（实测 0 命中）。
  **本页没读。**
- [[dpspins-resources]] —— **方程路线的 DPS 模块**，同样属于「DPS set 从哪来」那一层。
  **本篇没提。**
- [[command-reference]] —— **归属**：本篇在 `02.06_Command_Reference` 下。
- `Level Setup Commands`（**未建页、且不在 allowlist 里**）—— 原文指定的应用章首页。
- `ambiguous case`（**不是一个对象**，这里单独说明）—— `CVDL` 第 3 条与 `report AMBI`
  都用这个词，**本篇没有定义它的判据**（多少根针、差多少伏才算「有升有降」，本篇没写）。

## 版本

本文档**有** `## Functional changes` 段，**只有一条**：

```
- Introduced before SmarTest 6.3.2
```

**这一条是 §11.2 ② 的哨兵值**（措辞是 `before`，不是 `Introduced in`）——
**意思是「早于本文档集覆盖范围」**，**所以 `SLDO` 究竟成立于哪个版本，这份语料里没有。**
**7.10.3 上它有没有变，本篇版本段也没写**（本 wiki 面向 [[smartest-7.10.3]]）。

## 出处

`sources:` 一篇：
`02_System_reference/02.06_Command_Reference/02.06.02.02.223_SLDO_-__Switch_Level_and_Dps_Order.md`
（TDC `98735.htm`；**md 1,408 字节 / 136 行**，上游 htm 5,763 字节）。**整篇读完。**

**本页没做的**：

- **`Level Setup Commands`（`02.06.05` 章首页）没读**——原文 `## Application` 指着它，
  **所以「level setup 那一章里 `SLDO` 排在什么位置」本页不知道**；
  本页只知道它在 wiki 里对应 [[level]]（判据见「和谁有关」）。
- **[[pslv]] / [[drlv]] / [[rclv]] / [[dfps]] / [[dscp]] / [[dsus]] / [[dpspins-resources]] 一篇没读**——
  「level set / DPS set 是什么、谁定的、上限多少」**本页一个字没有**。
- **`ambiguous case` 的判据本页没有**——`CVDL` 第 3 条与 `report AMBI` 都用它，
  **但本篇没写「怎么算 ambiguous」**。
- **图：本篇没有内嵌图片**——判据可核：本篇 md 里 `.png` / `.jpg` / `![` **0 命中**。
  **所以本页没有任何来自图的结论。**
- **编码坏字：本篇 0 处**——`[一-鿿]` 扫过整篇 md，**一个汉字都没有**。**实测，不是没查。**
- **没有实跑。** 没有在机台上发过 `SLDO` / `SLDO?`、没有在两个 test suite 之间换过 set、
  没有触发过那句报错。`verified: doc-only` 说的就是这件事（§11：文档里有 ≠ 这台机器上能用）。

> **「和谁有关」里那条 [[pslv]] 对照，依据在这里**（**不是本篇的引文，所以没有写进正文**）：
> 同批的 `02_System_reference/02.06_Command_Reference/02.06.02.02.195_PSLV__PSLV__-__Power_Supply_LeVeL.md`
> 里，`setup_time` 那格逐字写着
> `All DPS's are synchronized so that they finish their settling periods at the same point in time.`
> ——**这一句属于那一篇，不属于本篇**；本页只在「和谁有关」里用中文说两者的分工。
> **它不是从 [[pslv]] 那一页读来的**，而是从那一篇 raw 读来的（同一批任务里读的）。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**（§11.2）：
>
> **① `CVDL` 的第 1 条与第 2 条都含 `or stable`，而两条结论相反。** 逐字两条：
> ```
> 1. If DPS voltage values are increasing or stable, DPS voltages are switched before level voltages.
> ```
> ```
> 2. If DPS voltage values are decreasing or stable, level voltages are switched before DPS voltages.
> ```
> ——**「DPS 电压不变」同时满足两条**，而一条说 DPS 先、一条说 level 先。
> **核过上游 `raw/98735.htm`：上游一字不差**（§11.2 ⑥ 那一类：上游就坏的，救不回来）。
> **本页并列两句，不替它调和，也不判哪个对**——**这一条会直接影响实际行为，读到别绕开它。**
>
> **② 标题写 `Dps`，正文写 `DPS`。** 逐字：
> 标题（`title:` 与 H1）是 `SLDO - (Switch Level and Dps Order)`，
> 正文第一句是 `The SLDO (Switch Level and Dps Order) command selects one of two switching order modes for switching voltage values of levels or DPS pins when changing from one DPS or level set to the next between two test suites.`
> ——**`Dps` 只出现在四个地方**：`title:` 那一行、`source_html:` 那一行的文件名、
> H1、以及第一句的括号里；**正文其余各处一律是 `DPS`**（实测）。
> **所以展开式的写法在同一篇里就两种。**
> **本页两处各照各的引，没有替它统一**（同 [[pslv]] 的 `LeVeL` / `LeVel` 那一处，
> 那一处被本工程的第七类检查抓出来过）。
>
> **③ `## Parameters` 一节把两条命令的位混排在一起。** `order` 与 `report` 是 `SLDO` 的位，
> **`operation` 是 `SLDO?` 的位**，而三者在同一节里连续出现，
> **原文没有把「哪一位属于哪条命令」标出来**——本页在「是什么」里按所在的命令分栏说明，
> **但那是本页的整理，不是原文的结构。**
>
> **④ 骨架的「语法 / 参数」节没有收进原文的 `## SLDO?` 一节。**
> 缺的是两块，逐字（这里只能用行内代码写，免得围栏嵌套）：
> **标题行** `## SLDO?`；
> **它的语法行** `SLDO? [operation]`；
> **它的 `returns:` 行** `SLDO {order}, [report]`。
> **这三样在「语法 / 参数」节里一个都没有**（那一节只有 `### SLDO` 一节）。
> **原因已核**（不是「raw 里没有」，也不是本页漏了）：
> `extract/objpack.py` 的 `title_aliases()` 只从**标题**里取命令名，
> 本篇标题是 `SLDO - (Switch Level and Dps Order)`，**逗号前只有 `SLDO` 一个名字**
> （对照 `DFUT, DFUT? - (DeFine UTility line)` 那种写法会取到两个），
> 于是 `## SLDO?` 这个标题既不在 `SEC_HEADS` 里、也不在别名集里，**被跳过**。
> 实测 `collect_syntax()` 对本篇返回的三段是 `['SLDO', 'Parameters', 'Example']`。
> **本页没有改「语法 / 参数」节（那是脚本的，§4）**——**缺的那两行逐字补写在「是什么」里。**
>
> **⑤ 本页没有「报错条件」节，因为脚本的门槛没过——不是本篇没有 `## Errors`。**
> 本篇 raw **有** `## Errors` 段，全文一句（逐字）：
> ```
> An error is generated if spelling or syntax is wrong.
> ```
> ——**这句只有 53 个字符，而脚本的门槛是 `ERR_MIN = 60`**
> （`extract/objscaffold.py`：「比这短的段不算材料（实测 <60 字符的多是空壳）」），
> **所以它没被收进页面**。实测 `error_block()` 对本篇返回**空串**。
> **本页按骨架的规矩不加那一节**（「有这节的页才有」），**只把这一句记在这里**，
> 免得读者以为「这条命令不会失败」。
>
> **⑥ `Parameters` 那张表在 raw 里被压平。** 与同批的 [[dfut]] / [[prlt]] 同一形态：
> 每格说明散成「一格一行 + 游离 `|`」，**表头（`Parameter` / `Description` 之类）本篇 raw 里没有**。
> 「语法 / 参数」节开头那个孤立的 ` | ` 就是它。

`verified: doc-only`
