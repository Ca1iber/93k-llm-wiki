---
type: object
title: PFND? - (Pin FiND)
layer: L1
stage: pin
tags: [pin, pfnd, port, differential-pair, pin-configuration, query, l1]
related: [pin, dfpt, port-editor, pin-configuration-tool, command-reference]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.178_PFND__-__Pin_FiND.md
created: 2026-09-24
updated: 2026-09-28
verified: doc-only
---

# PFND? - (Pin FiND)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **505 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.178_PFND__-__Pin_FiND.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
PFND? [group_type,] {(pin)}
```

returns:

```
PFND {group_type}, {(list)}, {(pin)}
```

### Parameters

| group_type | The group type can be PRT (for "port") or DIFF (for "differential pair"). PRT is the default. |
|---|---|
| pin | The name of the pin about which information is to be retrieved. |
| list | List of the ports that contain the pin, or the differential pair to which the specified pin belongs. |

### Example

```
> PFND? (I/O1_1)
< PFND PRT,(port_1,port_1.CP_1),(I/O1_1)
> PFND? DIFF,(P+)
< PFND DIFF,(P+,P-),(P+)
```

<!-- 语法节 end -->

## 是什么

**`PFND?`（Pin FiND）「反着查」：给它一个 pin，它告诉你这个 pin 属于哪个 port（或哪一对差分 pin）。**
全文一句话：

> 「The PFND? (Pin FiND) query returns the port or ports that contain the pin specified in the query,
> or the second pin in a pair of differential pins.」

**它只有查询形态，没有设置侧**（页标题就带 `?`）。
而**这一句里就埋着本篇的一处不一致**（见下「三处说法不一样」）。

### 两种模式，由一个**可选**参数切换

语法逐字是 `PFND? [group_type,] {(pin)}` —— `group_type` **带方括号 = 可省**，
而且**它后面跟着一个逗号**，所以省略时的写法是 `PFND? (pin)`（例子的第一条正是这样）。
可取的两种值逐字是：

> 「The group type can be PRT (for "port") or DIFF (for "differential pair"). PRT is the default.」

| `group_type` | 全称 | 查什么 | 返回的 `list` 是什么 |
|---|---|---|---|
| `PRT`（**默认**） | port | 包含该 pin 的**所有 port** | port 的列表 |
| `DIFF` | differential pair | 该 pin 所属的**差分对** | 差分对的那两个 pin |

**`PRT` 是默认值** —— 所以**不写 `group_type` 时按 port 查**，不是「两种都查」。

### 返回模板是三段，其中第三段是原样回显

```
PFND {group_type}, {(list)}, {(pin)}
```

| 段 | 是什么 | 例子 |
|---|---|---|
| 1 `group_type` | **你用的那个模式**（`PRT` / `DIFF`） | `PFND PRT,(port_1,port_1.CP_1),(I/O1_1)` |
| 2 `list` | 找到的组（**可多个**，模板里的括号 `{(list)}`） | `(port_1,port_1.CP_1)` |
| 3 `pin` | **你问的那个 pin，原样回来** | `(I/O1_1)` |

**第三段是回显**（**推断**，依据是例子里 `>` 发的是 `(I/O1_1)`、`<` 回的也是 `(I/O1_1)`；
**本篇没有一句说它是回显**）。

### 例子给的两个 `list`，都不是「一个名字」

原文 `## Example` 逐字两条：

```
> PFND? (I/O1_1)
< PFND PRT,(port_1,port_1.CP_1),(I/O1_1)
> PFND? DIFF,(P+)
< PFND DIFF,(P+,P-),(P+)
```

**`PRT` 那条的 `list` 是 `(port_1,port_1.CP_1)` —— 两个元素。**
按 `list` 那一格的定义（`List of the ports that contain the pin`），**两个都算 port**：

> 「List of the ports that contain the pin, or the differential pair to which the specified pin belongs.」

**`port_1` 和 `port_1.CP_1` 这种带点号的名字，本篇没有解释**——
**「点号是不是 port 名 + pin 名的拼接语法」= 语料未写**（**推断**：看形状像
`port_1` 里那个叫 `CP_1` 的 pin；**本篇没有一个字支持或否定它**）。

**`DIFF` 那条的 `list` 是 `(P+,P-)` —— 两个 pin，顺序里第一个就是你问的那个。**
（`>` 发的是 `(P+)`，`<` 回的是 `(P+,P-)`。）

### ⚠️ 同一个问题，本篇有三处说法不一样

「`DIFF` 模式到底返回什么」这一件事，本篇在三个地方各写了一遍，**三种措辞**：

| 出处 | 逐字 | 读起来是 |
|---|---|---|
| 开篇句 | `the second pin in a pair of differential pins` | **返回「那一对里的第二个 pin」**（一个） |
| `list` 那一格 | `the differential pair to which the specified pin belongs` | **返回「那一对」**（一对） |
| `## Example` 第二条 | `< PFND DIFF,(P+,P-),(P+)` | **返回两个 pin** |

**三处并列，本页不替它们调和**（§11.1 的「记录，不是修」）。
**能确定的只有一件事：例子的实际返回是两个** —— 而例子是唯一一处「能看见输出」的地方。
**「`P-` 是不是就是那个 `second pin`」本页不判**（本篇没有解释 `P+` / `P-` 谁先谁后）。

### 返回的那一段「名称」不能当标识符去用（一条边界）

原文只承诺这是**名字**：`The name of the pin about which information is to be retrieved.`
与 `List of the ports that contain the pin`。**这些名字能不能直接喂给别的命令、带不带引号、
空格的 pin 名怎么办 —— 语料未写**。
**而 `port_1.CP_1` 那个点号写法说明「名字里可能有结构」**（**推断**，依据是它出现在返回串里、
且本篇没有第二种解释）。**本条是提醒，不是文档要求。**

## 典型用法

**本篇没有 `## Procedure` / `## Before you begin` / `## What to do next`，
也没有 `## Errors` / `## Warnings`。** 用法只有 `## Application`、`## Parameters`、`## Example` 三处。

**1. 它是谁的一部分**（`## Application` 逐字）：

> 「Pin configuration, see Configuration Setup Commands.」

（原句里 `Configuration Setup Commands` 是语料内部链接，本页按 §11.1 ② 剥掉标记。）
**即：它属于 pin 配置那一族命令**——**这是本篇给的唯一一条「它归在哪」的说明。**

**2. 两种查法，对着目的选**：

| 你想知道 | 发什么 | 依据 |
|---|---|---|
| **这个 pin 在哪些 port 里** | `PFND? (pin)` 或 `PFND? PRT,(pin)` | `PRT is the default.` ＋ `## Example` 第一条 |
| **这个 pin 的差分对是那一对** | `PFND? DIFF,(pin)` | `## Example` 第二条 |

**3. 顺序与前提：本篇一条都没写。**
**没有 `## Predependencies` 段** —— 所以「pin 得先定义过」「port 得先建好」这类话，
**本篇一个字没有**（对照 [[dfpc]] 那一篇：它把 `The pin must have been defined with DFPN.`
写在专门的 `## Predependencies` 一节里）。**本页不替它补。**

**4. 什么时候用 —— 本篇没有写场景。**（**建议**，不是文档要求：既然它回答
「这个 pin 归在哪个 port / 哪一对差分 pin」，改 port 配置或查差分对之前拿它核一遍是自然的用法。
**本条是建议；文档没有给出任何使用场景。**）

**5. 出错怎么办：本页没有这一节。** 「pin 名写错了会怎样」「`group_type` 写了别的值会怎样」
**= 语料未写**（本篇既没有 `## Errors` 也没有 `## Warnings`）。

## 和谁有关

- [[pin]] — `stage: pin` 的落点：[[pin]] 那一页把它列进「**辅助查询命令（验证用）**」
  （与 `CHIN?` / `GCTX?` / `HWTY?` / `PRLT?` 并列），正合本篇「只查不设」的性质。
- [[dfpt]] — **推断**：`PFND? PRT` 查的那个「port」，是 `DFPT`（DeFine PorT）定义出来的东西。
  **本篇一个字没提过 `DFPT`**；这条并置的依据是 `group_type` 那一格写 `PRT (for "port")`
  与 `DFPT` 的页标题（**那一句在 [[pin]] 的 L1 命令表里**）。
  **本页没读 [[dfpt]] 的原文**，所以「port 里放了什么、能不能独立跑 timing」本页没有。
- [[port-editor]] — **推断**：port 的 GUI 侧编辑器。**本篇没提过任何 GUI**；
  依据只有「它和 `PRT` 同指 port」。**本页没读那一页。**
- [[pin-configuration-tool]] — **`## Application` 所指方向的落点**。
  原文写的是 `Pin configuration, see Configuration Setup Commands.` ——
  **它指的是那一章的命令**（`02.06.03_Pin_configuration_setup_commands`，
  **在 wiki 里没有同名的页**，所以本页用反引号写它）。
  wiki 里 pin 配置的 GUI 侧是 [[pin-configuration-tool]] 一族（**本页没读**）。
- [[command-reference]] — **归属**：本篇在 `02.06_Command_Reference` 下。
- **出边只有一条**（就是 `## Application` 里的 `Configuration Setup Commands`），
  **它指向的是「章」而不是某条命令** —— 所以本篇**没有点名任何兄弟命令**（见「出处」）。

## 版本

`## Functional changes` 段有，**只有一条**，逐字：

```
- Introduced before SmarTest 6.3.2
```

**这是哨兵值**（§11.2 ②）：`before` 说明它在**本文档集覆盖范围开始之前**就已经有了，
**具体哪个版本引入，语料里没有**。
**本篇只有这一条，所以「7.10.3 上它有没有变」也是无记录**。

## 出处

`sources:` 一篇：
`02_System_reference/02.06_Command_Reference/02.06.02.02.178_PFND__-__Pin_FiND.md`
（TDC `98686.htm`，**1,101 字节 / 67 行**）。**整篇读完**——本页引文全部来自这一篇；
另**核对过上游 `raw/98686.htm`**（下面 ⚠️ 两条注明了核对结论）。

**入边 2 条 / 2 篇、出边 1 条**（`edges.jsonl` 原始行数）：

| 方向 | 边 |
|---|---|
| 入 | `02.06.02.02_List_of_commands`（line 187，`inline`） |
| 入 | `02_System_reference/index.md`（line 2189，`toc`） |
| 出 | `02.06.03_Pin_configuration_setup_commands`（line 54，`inline`）—— 就是 `## Application` 那一句 |

**两条入边的 `anchor` 字段都是 `null`**（整篇引用，没有锚点）。

**本页没做的**：

- **`DFPT` 没读** —— 所以「port 是什么、怎么建、port 里放什么」本页一个字没有；
  「`PFND` 的 port 就是 `DFPT` 定义的 port」是**推断**（依据写在「和谁有关」里）。
- **`Configuration Setup Commands`（`02.06.03`）那一章没读** ——
  所以「它在 pin 配置命令族里排第几、和谁配对」本页没有。
- **差分对（differential pair）的定义文档没读** —— 所以「差分对在哪儿配、`P+`/`P-` 的命名规矩」
  本页没有；**本篇只出现 `DIFF` 这个值和例子里的 `P+`/`P-`**。
- **`port_1.CP_1` 那种点号名字的含义：语料未写**（本页只给了形状上的推断）。
- **`group_type` 写别的值会怎样、pin 名不存在会怎样：语料未写**（本篇没有 Errors / Warnings 段）。
- **图：本篇没有内嵌图片** —— 判据可核：本篇 md 里 `.png` / `![` **0 命中**。
- **编码坏字：本篇 0 处**（`[一-鿿]` 扫过整篇，**一个汉字都没有**）；
  **整词替换（`DC/DC power units`）0 命中**；**省略号（U+2026 与三个 ASCII 点）0 命中**。三条都是实测结果，不是没查。
- **没有实跑。** 没有在机台上发过 `PFND?`，没有拿它查过任何真实的 port 或差分对。
  `verified: doc-only`。
- **没有动 `wiki/index.md`**，也没有把本页挂进 [[pin]]。

> ⚠️ **本篇的语料瑕疵，照实记、一处都没替它改**（§11.2）：
>
> **① `DIFF` 模式返回什么，本篇三处说法不一致。** 逐字三处：
> `or the second pin in a pair of differential pins`（开篇句，**说返回一个**）／
> `or the differential pair to which the specified pin belongs`（`list` 那格，**说返回一对**）／
> `< PFND DIFF,(P+,P-),(P+)`（例子，**实际回了两个**）。
> **已核上游 `raw/98686.htm`：三处在 htm 里就是这么写的**（开篇句、
> `List of the ports that contain the pin, or the differential pair to which the specified pin belongs.`、
> 例子两行）——**上游如此，不是转换丢字**。**本页不替它们调和。**
>
> **② `## Parameters` 表在 raw 里被压平，而且没有表头。** 三格（`group_type` / `pin` / `list`）
> 各散成「一格一行 + 游离 `|`」，说明文字一个字没丢；
> **表头本篇 raw 里没有**（已核上游：那张表的 `<caption></caption>` 是空的）。
>
> **③ `## Application` 在骨架的「语法 / 参数」节之外。** 脚本按段标记抽（§4），
> 那一节收的是 `Syntax` + `Parameters` + `Example`。
> `## Application` 那一句（含它那条链接）**不在语法节里** —— 它是本页正文的引用，
> 也是本页**唯一一条出边**的来源。**这不是抽取漏了，是它本来就不该进语法节。**

`verified: doc-only`
