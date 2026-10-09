---
type: object
title: GCTX? - (Get ConTeXt))
layer: L1
stage: pin
tags: [gctx, l1-command, firmware-command, query-command, mode-context, setup-component, equation-based, sprm]
related: [sprm, ctxt, constraint-level-mode-context-match, constraint-timing-mode-context-match, level, timing, pin]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.129_GCTX__-__Get_ConTeXt.md
created: 2026-09-24
updated: 2026-09-28
verified: doc-only
---

# GCTX? - (Get ConTeXt))

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **2,228 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.129_GCTX__-__Get_ConTeXt.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
GCTX? {setup_type},[setup_comp]
```

returns:

GCTX {setup_type}{,setup_nr|"name"},"[context_name]"

### Parameters

| setup_type | The type of the setup component for which the mode context is queried. Possible values are: | The type of the setup component for which the mode context is queried. Possible values are: |
|---|---|---|
| setup_type | TIM | Timing equation set |
| setup_type | LEV | Level equation set |
| setup_type | WAVE | Wavetable |
| setup_type | LBL | Sequencer label |
| setup_type | SPCF | Multi-port specification |
| setup_type | CURR | The mode context for the current primary sets (as defined with the SPRM command) and the current start label (as defined with the SQSL command). |
| setup_nr | The number of a setup component. This parameter is ignored for setup type CURR. | The number of a setup component. This parameter is ignored for setup type CURR. |
| name | The name of a wavetable, or the name of a multi-port specification. This parameter is ignored for setup type CURR. | The name of a wavetable, or the name of a multi-port specification. This parameter is ignored for setup type CURR. |
| context_name | The name of the mode context. If you specified CURR for the setup_type parameter, and the current mode context is not correct, GCTX? returns an empty string.<br><br>The context is only correct when all primary sets (defined by SPRM) and the current start label (defined by SQSL) are associated with the same mode context. Furthermore, if there exists a primary multi-port specification, the mode context must be the same for all ports of this specification. | The name of the mode context. If you specified CURR for the setup_type parameter, and the current mode context is not correct, GCTX? returns an empty string.<br><br>The context is only correct when all primary sets (defined by SPRM) and the current start label (defined by SQSL) are associated with the same mode context. Furthermore, if there exists a primary multi-port specification, the mode context must be the same for all ports of this specification. |

> ⚠️ 转录说明（非原文）：本表在上游 HTML 里含合并格（colspan / rowspan）；
> 跨格文字已按覆盖范围重复写出（**不是原表里有重复的格子**）。真结构见 `tdc-html/agent-html/98611.htm`。

### Example

```
> GCTX? TIM,101
< GCTX TIM,101,"High-Speed"
```

<!-- 语法节 end -->

## 是什么

**`GCTX?` 是「问 mode context」的那一条查询命令。** 原文第一句就是全部功能：

> 「The GCTX? (Get ConTeXt) query returns the mode context of the specified setup component or the context that is currently active.」

**一句话里其实有两个问题**：① **指定的** setup component 挂在哪个 mode context 下；
② **当前生效的** mode context 是哪一个（后者靠 `CURR` 这个取值问）。

> ⚠️ **命令名里多一个右括号**：标题写的是 `GCTX? - (Get ConTeXt))`——`ConTeXt` 后面是**两个** `)`。
> **原文如此**（上游 `98611.htm` 的 `<title>` 与正文 `<h1>` 两处都这样），**不是本页抄错**。

### 六种 `setup_type`：问的是「哪个 setup component」

`setup_type` 必填，取值是**封闭的六个**，原文的总起句是
`The type of the setup component for which the mode context is queried. Possible values are:`

| `setup_type` | 指的是什么（原文逐字） |
|---|---|
| `TIM` | `Timing equation set` |
| `LEV` | `Level equation set` |
| `WAVE` | `Wavetable` |
| `LBL` | `Sequencer label` |
| `SPCF` | `Multi-port specification` |
| `CURR` | **不是一种 component，是「现在」**：`The mode context for the current primary sets (as defined with the SPRM command) and the current start label (as defined with the SQSL command).` |

**`CURR` 与另外五个不是一类**：另外五个都要**指名一个 component**，只有它问的是**当下生效的那一套**。
而且它的定义把两样东西捆在一起——**`SPRM` 定的 primary sets** 与 **`SQSL` 定的 current start label**。

### 第二个位置：语法说「一个」，参数说「两个」

语法式里第二格是**一个**可选的 `[setup_comp]`；
而 Parameters 一节把它拆成**两格**，并且**两格都写了同一句「对 `CURR` 无效」**：

| 参数 | 原文 | 哪种 `setup_type` 用得上 |
|---|---|---|
| `setup_nr` | `The number of a setup component. This parameter is ignored for setup type CURR.` | 泛称「一个 setup component 的号」 |
| `name` | `The name of a wavetable, or the name of a multi-port specification. This parameter is ignored for setup type CURR.` | **原文只点了 `WAVE` 与 `SPCF` 两种** |

**`ignored for setup type CURR` 被抄了两遍**——所以 **`CURR` 那一格根本不带第二参数**，
写不写都一样（命令会忽略）。

> **（推断）**：`name` 这条路只对 `WAVE`/`SPCF` 明说，其余四种按号填。
> 依据是上面两格的原文——`name` 那一格只提 wavetable 与 multi-port specification；
> **但原文没有任何一句话把「六种取值 × 号 / 名」列成对照表**，
> **所以这一段是推断，不是文档事实**，本页不把它写成结论。

### 返回式：回的是 `GCTX`（不带 `?`），并且把 setup component 原样回声

```
GCTX {setup_type}{,setup_nr|"name"},"[context_name]"
```

三件事：① **返回的是 `GCTX`，没有问号**；② **第二格把你给的 `setup_nr` 或 `"name"` 原样回给你**
（示例里问 `TIM,101`、答就是 `TIM,101`）；③ **`context_name` 带双引号**。
语法式里那些方括号与花括号是**原文自己写的**（表示可选 / 必选），本页照抄。

### `CURR` 拿到空串：**不是报错，是「context 不 correct」**

> 「The name of the mode context. If you specified CURR for the setup_type parameter, and the current mode context is not correct, GCTX? returns an empty string.」

**这一句是本页最要紧的一句**：`GCTX? CURR` 回空串，**命令没坏**——
是「当前这一套不满足下面那三条条件」。

### 「correct」的判据，原文写全了：**三条**

> 「The context is only correct when all primary sets (defined by SPRM) and the current start label (defined by SQSL) are associated with the same mode context. Furthermore, if there exists a primary multi-port specification, the mode context must be the same for all ports of this specification.」

| # | 条件 | 依据（原文逐字） |
|---|---|---|
| 1 | **所有 primary set 同属一个 mode context** | `all primary sets (defined by SPRM) … are associated with the same mode context` |
| 2 | **current start label 也同属那个 context** | `and the current start label (defined by SQSL)` |
| 3 | **若存在 primary multi-port specification，它的所有 port 都必须同 context** | `the mode context must be the same for all ports of this specification` |

**注意第 3 条是 `Furthermore` 另起的一句**——它是**附加条件**，
**只在有 primary multi-port spec 时才存在**；没有 multi-port spec 的场合只看前两条。

## 典型用法

**先说范围**：本篇**没有 `## Procedure`、没有 `## Before you begin`、也没有 `## Application`**。
**所以「什么时候该用 `GCTX?`、它在哪个流程里排第几步」本篇一个字都没写（语料未写）。**
本篇能给读者的只有「怎么发、回复怎么读」。

**1. 选 `setup_type`**（六个取值见上表）。

**2. 第二格怎么填**：

| 你要查的 | 第二格 |
|---|---|
| 某个具体 component | `{setup_nr}`（号）或 `"{name}"`（名；原文只对 `WAVE`/`SPCF` 明说） |
| **当前生效的** | **不填**——`CURR` 忽略第二参数（原文：`This parameter is ignored for setup type CURR.`） |

**3. 发查询**。原文的示例（`## Example`，逐字）：

```
> GCTX? TIM,101
< GCTX TIM,101,"High-Speed"
```

拆开读：

| 行 | 内容 | 说明 |
|---|---|---|
| `>` | **你发的** | `TIM`（timing equation set）+ `101`（`setup_nr`） |
| `<` | **回的** | `TIM,101` **原样回声**；`"High-Speed"` 是那个 mode context 的名字 |

> **`>` 与 `<` 这两个符号是什么意思，原文没写**（**语料未写**）。
> **（推断）**：看形状是「发出去的命令 / 回来的答复」，两行正好一一对应。
> **本页不把它写成结论**——原文没有一句话定义这两个符号。

**4. 读结果**：

- 回一个**带引号的名字** → 就是这个 component（或当前这一套）的 mode context。
- **回空串** → 只可能出现在 `CURR`；照上面三条判据逐条查是哪一条不满足。

**5. 报错**：**本篇没有 `## Errors` 段、也没有 `## Warnings` 段**——
所以「`GCTX?` 会不会报错、报什么」本篇没有。
**这不是本页漏写，是原文没有这两节。**

## 和谁有关

- [[sprm]] — **上游**。`CURR` 那格的定义与 `context_name` 的判据里，
  **`SPRM` 一共出现两次**，都是「primary sets 由它定义」。**那一篇本页没读。**
- `SQSL` — **另一条上游**（**本页不链**：`SQSL` 不在 allowlist 里，§9.1）。
  它定义 current start label，**与 `SPRM` 在同一个句子里并列出现**：
  `The mode context for the current primary sets (as defined with the SPRM command) and the current start label (as defined with the SQSL command).`
- [[constraint-level-mode-context-match]] / [[constraint-timing-mode-context-match]] —
  **同一件事的约束侧**：那两页讲的正是「level / timing setup 的 mode context 必须一致」，
  而本篇六个 `setup_type` 里有 `LEV` 与 `TIM` 两个。
  **本篇没有链它们**（本篇连 `Related information` 一节都没有）。
  **两篇本页都没读**，所以它们怎么表述这条约束，本页不知道。
- [[ctxt]] — **名字成对的那一条**（`CTXT, CTXT? - (ConTeXT)`）。
  **本篇既没链它、正文也没提它**；两者是什么关系（谁是设置侧、谁是查询侧）
  **本篇一个字没有（语料未写）**。**那一篇本页没读。**
- [[level]] / [[timing]] — **`LEV` / `TIM` 两个 `setup_type` 各落在哪个 stage**。
  **两篇本页都没读。**
- [[pin]] — **`stage: pin` 的依据**（frontmatter 的字段，§6）。
  **但要注意**：本篇的六个 `setup_type` 覆盖 timing equation set / level equation set /
  wavetable / sequencer label / multi-port spec / 当前集合，**没有一个是 pin 配置**——
  **「为什么 `stage` 填 `pin`」在本篇里没有任何依据可查**，本页只照记 frontmatter。

**本页没有引用 `edges.jsonl` 的入边 / 出边数字**（没读边数据，故不报条数）。

## 版本

**本文档有 `## Functional changes` 段，段里只有一条**：

- `Introduced before SmarTest 6.3.2`

> **这一条是 §11.2 ② 说的哨兵值，不是「6.3.2 新增了 GCTX?」。**
> 措辞是 `before`，意思是「**在本套文档集覆盖范围开始之前就已经有了**」。
> **只可以说：7.10.3 上有它，而且它比 6.3.2 更老** → [[smartest-6.3.2]]。
> **不许把它读成「6.3.2 引入了 GCTX?」。**

**版本段里没有的东西（照实记，不替它补）**：没有第二条。
**所以「六个 `setup_type` 是哪个版本凑齐的」「`CURR` 是哪一版加的」在本篇里查不到。**

## 出处

`sources:` 一篇：

- `02_System_reference/02.06_Command_Reference/02.06.02.02.129_GCTX__-__Get_ConTeXt.md`
  （frontmatter 的 `source_topic` 是 `98611.htm`；**2,814 字节 / 124 行，整篇读完**——
  字节按 `st_size`、行数按 `wc -l`，§11.5 口径）
- 本页的「语法 / 参数」节是脚本从这一篇抽的（**本页一个字没动**）。

**本页没做的**：

- **原文点到的两样东西，一篇都没读**：`SPRM`（有页 [[sprm]]）、`SQSL`（无页）。
  所以**「primary sets 怎么设」「start label 怎么定」本页一个字都没有**。
- **`Related information` 一节本篇就没有**——不是本页没读，是**原文没有这一节**。
- **`## Application` / `## Errors` / `## Warnings` 三节本篇也都没有。**
  所以「什么时候用」「会产生什么错误」本页答不了。
- **图 0 张。** 实测 `![` / `<img` / `.png` / `.jpg` / `.gif` / `raw/` 六种写法在本篇
  **全部 0 命中**；上游 `98611.htm` 里也 **0 个 `<img>`、0 个图片路径**
  （`src=` 只有 1 处，是那个 `p.css` 样式表）。
  **所以本页没有任何来自图的结论**——**「没有图」是查过的事实，不是「够不着」（§11.4）。**
- **没在机台上发过 `GCTX?`**（`verified: doc-only`）。
  **所以「空串在真机上长什么样、会不会换成报错」本页答不了（§11）。**
- **§10 重复投放：本篇在语料里只有一份**（按文件名全树 glob，1 命中）——
  **不存在 ETIM 那种三份投放的情况。**

### 上游 `.htm` 核对（本页做的一步）

**下面两条去上游 `F:\master-dev\dorm-wsl-sytest\tdc-html\raw\98611.htm`（5,362 字节）核过。**

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> **① 标题末尾多一个右括号。** 原文逐字：`GCTX? - (Get ConTeXt))`
> ——`ConTeXt` 后面是**两个** `)`。
> **上游核对**：`98611.htm` 的 `<title>` 与正文标题两处都是 `GCTX? - (Get ConTeXt))`
> → **上游就坏的**（§11.2 ⑥），重做一次转换也救不回来。
> **本页的标题（含 frontmatter 的 `title`）照抄原样。**
>
> **② 坏字：本篇 0 个。** 照 §11.2 ① 那条判据（**英文文档里出现任何汉字，都是坏字**）
> 逐字查过：**本篇一个汉字都没有**——
> **但这是「本页读到的」，不是「本篇没有」**（§13.1：没找到 ≠ 没有）。

`verified: doc-only`
