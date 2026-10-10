---
type: object
title: PDIV? - (Period DIVider)
layer: L1
stage: timing
tags: [timing, period-divider, pdiv, l1-command, query-only, fast-pin, conf]
related: [conf, etds, clkr, timing-specification, timing]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.176_PDIV__-__Period_DIVider.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# PDIV? - (Period DIVider)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **564 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.176_PDIV__-__Period_DIVider.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
PDIV? {specset_id|"multi-port_spec"|"wavetbl"} [,spec_type][,(pinlist)]
```

returns:

```
PDIV {specset_id|"multi-port_spec"}, {period_div}
```

### Parameters

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98684.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 3 列。
> 首行（上游原文）：specset_id | Identifier of a timing specification, which is derived as follows: 100 * equation_set_no + specset_no

### Example

```
> PDIV? "fast",WFT,(I1)
< PDIV "fast",WFT,6,(I1)
```

This example queries the implicit period divider of the fast pin I1 in the wavetable `fast`. The factor is 6.

<!-- 语法节 end -->

## 是什么

**PDIV 只有查询这一半：它回一个数——某个东西的 `period_div`（period divider）。**
**页名本身就是证据**：标题是 `PDIV? - (Period DIVider)`，**没有 `PDIV`（不带 `?`）那一半**。
原文第一句是全部范围：

> 「The PDIV? query returns the period divider for fast pins (FAST option of CONF command) for the specified setup component.」

**一句话里三个限定**，缺一个就查不到：

| 限定 | 原文 |
|---|---|
| **只对 fast pin 有意义** | `for fast pins` |
| **fast pin 是哪来的** | `FAST option of CONF command` —— **由 [[conf]] 的 `FAST` 选项决定** |
| **查谁** | `for the specified setup component` —— **由第一个参数指定** |

**`setup component` 是哪个东西？本篇没给这个词下定义**（**语料未写**）——
后面的参数节把它落成了三个候选：`specset_id`、`multi-port_spec`、`wavetbl`。

**本篇是这一族里最薄的一篇**（1,696 字节），
**它没有 `## Application`、没有 `## Mode of operation`、没有 `## Errors`、没有 `## Procedure`**——
**所以「何时用、怎么用、错了怎么办」本篇都没交代**。
本页后面只能照着语法式与参数表写。

### `period_div` 的取值（**一个数，两种含义**）

> 「Possible values are -1 (for standard pins), 2, 3, 4, 6, 8 (only for fast pins).」

| 值 | 含义 |
|---|---|
| **`-1`** | **标准 pin**（`for standard pins`） |
| **`2, 3, 4, 6, 8`** | **fast pin 才有**（`only for fast pins`） |

**注意 `-1` 不是一个「分频比」，它是「这条不是 fast pin」的标记值。**
参数节的 `pinlist` 那一格把同一件事又说了一遍：

> 「This parameter is only applicable to fast pins. For standard pins,-1 is returned.」

（**`pins,-1` 之间少一个空格**——原文如此，见「出处」⚠️②。）
**所以查一个标准 pin，不会报错、也不会什么都没有，而是回 `-1`。**

**取值的集合里没有 `5`、没有 `7`**——**只有 2、3、4、6、8 这几个数**。
**为什么是这几个，本篇没说**（**语料未写**）。

### `spec_type` 决定「查的是哪一种」

`spec_type` 在语法式里是方括号 = 可选，但**参数节把它的取值和后果都写死了**：

| 取值 | 回什么（原文） |
|---|---|
| **`TIM`** | 「Returns the period divider of the timing sets (fast pins). If not all timing sets have the same period divider for the same fast pin, PDIV? returns an error.」 |
| **`WFT`** | 「Returns the implicit period divider of the wavetable specified as the first parameter.」 |

**两个取值的差别不只是「查谁」，措辞也不一样**：
`TIM` 说的是 **`the period divider of the timing sets`**，
`WFT` 说的是 **`the implicit period divider of the wavetable`**——
**后者多了 `implicit`（隐式的）这个词，前者没有。**
**「显式 / 隐式」在不在本篇里解释？没有**——**本篇只在这里出现 `implicit` 一次，没有给它的定义**（**语料未写**）。

**`TIM` 那个取值里藏着本篇唯一一条报错条件**，逐字：

> 「If not all timing sets have the same period divider for the same fast pin, PDIV? returns an error.」

**这是「同一条 fast pin 在各个 timing set 里的 period divider 必须一致」**——
**不一致就报错，不给一个「取第一个」之类的兜底。**
**注意它长在参数表的一格里，不在 `## Errors` 段里**——
**因为本篇根本没有 `## Errors` 段**（见「出处」）。

`wavetbl` 那一格与 `WFT` 是配套的：

> 「Name of a wavetable. This requires that spec_type is set to WFT.」

**即：第一格写 wavetable 名字时，`spec_type` 必须给 `WFT`。**
（`spec_type` 在语法式里写着可选——**但这条把「写 `wavetbl`」这一支的必填性补上了**。）

### `specset_id`：equation based 场合的那一串数字

> 「Identifier of a timing specification, which is derived as follows: 100 * equation_set_no + specset_no」

**与这一族其它命令同一个算法**（`ETDS` / `ETIM` / `TSUS` 都是这个式子）。
**本篇没有 `## Equation Based Testing` 那一节**，**所以「该用哪个 `specset_id`」本篇不教**——
`specset_id` 在这里只是「第一格能填什么」之一。相关页：[[timing-specification]]（**本页没读**）。

### multi-port：只说了「填名字」

> 「To query a multi-port specification, enter the name of the specification.」

**就这一句。** 多端口场合要不要 `portlist`、回读怎么区分 port，**本篇没说**（**语料未写**）。
**注意返回式里 `multi-port_spec` 这个位置没有引号**，而语法式里有：

| | 原文 |
|---|---|
| 语法式第一格 | `{specset_id\|"multi-port_spec"\|"wavetbl"}`（**带引号**） |
| 返回式第一格 | `{specset_id\|"multi-port_spec"}`（**不带引号**，而且**没有 `wavetbl` 这一支**） |

### 返回式与示例对不上（**本页发现的最实在一处矛盾**）

语法式的返回式是**两格**：

```
PDIV {specset_id|"multi-port_spec"}, {period_div}
```

**而 `## Example` 的回读行是四格**：

```
< PDIV "fast",WFT,6,(I1)
```

| 出现的字段 | 语法式里有吗 | 例子里有吗 |
|---|---|---|
| 第一格（规格 / wavetable 名） | 有 | 有（`"fast"`） |
| **`spec_type`** | **没有** | **有（`WFT`）** |
| `period_div` | 有 | 有（`6`） |
| **`pinlist`** | **没有** | **有（`(I1)`）** |

**语法式说「回两格」，例子回「四格」，多出来的正是 `spec_type` 与 `pinlist`。**
**两者能不能同时成立，本篇一个字没解释**——
**本页两处并列照记，不替它调和**（见「出处」⚠️①）。
**实用的一条读法（推断）**：照例子读，**回读带上你查的那个 `spec_type` 和 `pinlist`**；
**依据只有这一个例子，不是文档的声明。**

### 三个词指同一个数（**本篇不替它统一**）

**同一个量在本篇里有三种写法**，逐字并列：

| 写法 | 出现在哪 |
|---|---|
| **`period divider`** | 标题 `PDIV? - (Period DIVider)`、第一句 `returns the period divider`、`TIM` 那一格、`WFT` 那一格、`pinlist` 那一格 |
| **`period_div`** | 参数名那一格；返回式里也叫这个 |
| **`factor`** | `## Example` 的说明句：`The factor is 6.` |

**加上标题里的 `DIVider` 与命令名里的 `PDIV`，一共五种写法指同一个东西。**
**这不是错别字**（英文里 `period divider` 与 `period_div` 是同一个概念的长短写法），
**但 `factor` 是第三个词**——**本篇没有一句话说 `factor` 就是 `period_div`**
（**推断**：说明句讲的正是例子里那个回读值 `6`，**依据只有这一处上下文**）。
**本页照记，不替它统一。**
**命令大小写敏感（§11），所以引用取值时按原文照抄**：`TIM`、`WFT`、`-1`。

## 典型用法

**先说范围**：本篇**没有 `## Application`、没有 `## Procedure`、没有 `## Before you begin`、
没有 `## Errors`、没有 `## Mode of operation`**。
**所以「什么时候想起要查它」「查完拿来干什么」本页一个都答不了**——
本页只能照语法式与那一格参数写。

**1. 先确定你要查哪一种**（这是本篇唯一的选择点）：

| 你想知道 | 第一格写 | `spec_type` 写 | 依据 |
|---|---|---|---|
| **某个 timing set 的 period divider** | `specset_id` | `TIM` | `spec_type` 的 `TIM` 那一格 |
| **某个 wavetable 的（隐式）period divider** | `"wavetbl"` | **`WFT`（必填）** | `wavetbl` 那一格：`This requires that spec_type is set to WFT` |
| **某个多端口规格的** | `"multi-port_spec"` | 本篇没写 | `multi-port_spec` 那一格 |

**2. 填 `pinlist`**：**只对 fast pin 有效**；查标准 pin 会回 `-1`。

**3. 写法**：

```
PDIV? {specset_id|"multi-port_spec"|"wavetbl"} [,spec_type][,(pinlist)]
```

**4. 原文的示例（`## Example`，逐字）**：

```
> PDIV? "fast",WFT,(I1)
< PDIV "fast",WFT,6,(I1)
```

> 「This example queries the implicit period divider of the fast pin I1 in the wavetable `fast`. The factor is 6.」

**逐格读**：`"fast"` 是**wavetable 名**（第一格）→ `WFT` 是 **`spec_type`** →
`6` 是**回来的 `period_div`** → `(I1)` 是**查的那条 fast pin**。
**说明句把 `6` 叫 `factor`**——**原文自己的用词，和参数名 `period_div` 不是同一个词**
（**三个词指同一个数，见「是什么」末节**）。

**5. 一个**本篇没给、本页只能标成「未写」的操作问题**：
**`TIM` 与 `WFT` 哪个该用、什么时候用**——**本篇一个字没说**。
（**推断**：`WFT` 那一支要你给 wavetable 名、`TIM` 那一支要你给 `specset_id`，
所以**手上有什么名字**可能才是选择依据；**但这是本页猜的，原文没有依据。**）

## 和谁有关

- [[conf]] — **fast pin 的定义来源（前置）**。本篇第一句唯一的依赖就是它：
  `for fast pins (FAST option of CONF command)`。
  **`CONF` 那一篇本页没读**，所以 **`FAST` 选项怎么设、设了之后哪些 pin 变成 fast pin
  ——本页一个字都没有。**
- [[etds]] — **用掉这个数的下游（下游）**。
  **这条对照来自本批另一页 [[etds]] 的 raw，不是本篇**——
  [[etds]] 的 `pdiv:n` 规则写的是
  `n must be the same value as the period_div value of the pins in pinlist within the timing set specified by the timing_set parameter`，
  **`period_div` 这个 token 与本篇回的那个数是同一个词**。
  **本篇从头到尾没出现 `ETDS` 这个命令名**，所以**「ETDS 的 `pdiv:n` 该怎么填」请去 [[etds]] 看，
  别拿本页的数去反推它。**
- [[clkr]] — **一个必须分清的名字（并列）**。
  **本篇的 `period_div` 与 `period resolution` 不是同一个词**，
  而 **`period resolution` 在 [[pclk]] 那一篇里与 `CLKR` 一起出现**。
  **这一条对照同样来自本批另一页的 raw（[[pclk]] 那一篇），不是本篇**——
  **本篇从未出现 `CLKR`，也没出现 `period resolution`。**
  **所以两者是不是一回事，本页不判**；**要那一侧请去 [[clkr]] / [[pclk]]。**
- [[timing-specification]] — **`specset_id` 指的那个东西（前置概念）**。
  本篇把 `specset_id` 定义成 `Identifier of a timing specification`，
  **但「一个 timing specification 长什么样」本篇没有**。**那一篇本页没读。**
- [[timing]] — **`stage: timing` 的依据**（frontmatter；§6：`stage` 填最近的一段，不是归属）。
  本页是 [[timing]] 的 L1 表里 timing setup 一族的一条**只读**命令。

**本篇点到名字、本页没读的还有一处**：

- **`FAST option of CONF command`** —— 见上，它是本篇唯一的前置机制。
- **`wavetable`（`wavetbl`）** —— 本篇两次用到这个名字（第一格的取值、`WFT` 的说明），
  **但「wavetable 是什么、怎么建」本篇没有**。[[wavetable]] 那一页本页没读。

**本页没有引用 `edges.jsonl` 的入边/出边数字**（没读边数据，故不报条数）。

## 版本

**本文档有 `## Functional changes` 段，段里只有一条**：

- `Introduced before SmarTest 6.3.2`

> **这一条是 §11.2 ② 说的哨兵值，不是「6.3.2 新增了 PDIV」。**
> 措辞是 `before`，意思是「**在本套文档集覆盖范围开始之前就已经有了**」。
> **只可以说：7.10.3 上有它，而且它比 6.3.2 更老** → [[smartest-6.3.2]]。
> **不许把它读成「6.3.2 引入了 PDIV」。**

**版本段里没有的东西（照实记，不替它补）**：没有第二条。
**所以「`2, 3, 4, 6, 8` 这组取值哪一版定的」「`TIM` / `WFT` 两个 `spec_type`
哪一版加的」「fast pin 是哪一版引入的」在本篇里查不到。**

## 出处

`sources:` 一篇：

- `02_System_reference/02.06_Command_Reference/02.06.02.02.176_PDIV__-__Period_DIVider.md`
  （frontmatter 的 `source_topic` 是 `98684.htm`；**1,124 字节 / 110 行，整篇读完**——
  字节按 `st_size`、行数按 `wc -l`，§11.5 口径）
- 本页的「语法 / 参数」节是脚本从这一篇抽的（**本页一个字没动**）。

**本页没做的**：

- **本篇没有 `## Errors` / `## Warnings` 段**，所以**本页没有「报错条件」节**
  ——**那是骨架按结构就不建这一节，不是漏写。**
  本篇唯一提到报错的地方是参数表 `TIM` 那一格里的
  `If not all timing sets have the same period divider for the same fast pin, PDIV? returns an error.`
  ——**本页把它写在正文里了（见「是什么」），因为脚本抽不出它。**
- **文档里点到的名字一篇都没读**：`CONF`（`FAST` 选项）、`wavetable`。
  所以：**`FAST` 怎么设、wavetable 是什么，本页一个字都没有。**
- **本篇没有 `## Application` 节**——**所以「PDIV 属于哪一章、在流程里排第几步」本页没有**。
  **本页不替它编一个 `Timing Setup` 的归属**：归属要靠 `## Application` 那一句原文，
  **本篇没有那一句。**
- **`## 是什么` 里那条「照例子读回读带 `spec_type` 与 `pinlist`」标了「推断」**——
  **依据只有那一个示例，本篇没有一句话说返回式与例子哪个对。**
- **图 0 张。** 实测 `![` / `<img` / `.png` / `.jpg` / `.gif` / `raw/` 六种写法在本篇
  **全部 0 命中**。**所以本页没有任何来自图的结论**——
  **这张「没有图」是查过的事实，不是「够不着」（§11.4）。**
- **没在机台上跑过 `PDIV?`**（`verified: doc-only`）。
  **所以「查一条标准 pin 真的回 `-1` 吗」本页只能保证「文档这么写」（§11）。**

### §10 重复投放：本篇在语料里有**三份**（本页查过）

| 路径 | `source_topic` | 字节 | 与**本页这一份**的正文 |
|---|---|---|---|
| `02.06_Command_Reference/02.06.02.02.176_PDIV__-__Period_DIVider.md`（**本页的出处**） | `98684.htm` | 1,696 | — |
| `02.06_Command_Reference/02.06.06.02.21_PDIV__-__Period_DIVider.md` | `98684_2.htm` | 1,697 | **把篇内相对链接的前缀归一化后，`diff` 报 0 行差异** |
| `02.08_Setup_and_Result_Tools/02.08.04.34.02.02.21_PDIV__-__Period_DIVider.md` | `98684_3.htm` | 1,708 | **同上——0 行差异** |

**三份的差别只有两处**：① frontmatter 的 `source_topic` / `source_html`；
② **篇内相对链接的前缀**（第三份多一层 `../02.06_Command_Reference/`，字节数差的就是它）。
**本页的结论全部只来自第一份**；另两份只核了 frontmatter、字节数与 `diff` 行数，
**没有读它们的正文**（§12 不越取材边界）。

### 上游 `.htm` 核对（2026-09-24 做，这是本页**多出来的**一步）

**下面两条本页全去上游 `F:\master-dev\dorm-wsl-sytest\tdc-html\raw\98684.htm`（4,971 字节）核过。
结论：都是「上游就坏的」（§11.2 ⑥）——重做一次转换也救不回来。**

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> **① 语法式的返回式和 `## Example` 对不上。** 两处逐字并列：
> ```
> returns:
> PDIV {specset_id|"multi-port_spec"}, {period_div}
> ```
> ```
> > PDIV? "fast",WFT,(I1)
> < PDIV "fast",WFT,6,(I1)
> ```
> **返回式两格、例子四格**，多出来的是 `spec_type`（`WFT`）与 `pinlist`（`(I1)`）。
> **上游核对**：`98684.htm` 里这两处就是这样——`Syntax` 块里是
> `PDIV? {specset_id|"multi-port_spec"|"wavetbl"} [,spec_type][,(pinlist)]` 后接
> `returns:PDIV {specset_id|"multi-port_spec"}, {period_div}`；
> 而例子的 `prettyprint` 块里是 `&gt; PDIV? "fast",WFT,(I1)` /
> `&lt; PDIV "fast",WFT,6,(I1)` → **上游就坏的。本页两处并列照记，不判定哪个对。**
>
> **② `For standard pins,-1 is returned.`——少一个空格。** 原文逐字：
> `This parameter is only applicable to fast pins. For standard pins,-1 is returned.`
> **`pins,` 与 `-1` 之间没有空格。**
> **上游核对**：`98684.htm` 里是
> `For standard pins,<code>-1</code> is returned.`——**逗号后直接跟 `<code>`，
> 上游本来就没有空格字符**，靠 `<code>` 的样式分界 → **上游就坏的。**
>
> **③ 坏字：本篇 0 个。** 照 §11.2 ① 那条判据（**英文文档里出现任何汉字，都是坏字**）逐字查过：
> **本篇一个汉字都没有**——**但这是「本页读到的」，不是「本篇没有」**（§13.1：没找到 ≠ 没有）。

`verified: doc-only`
