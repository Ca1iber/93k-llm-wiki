---
type: object
title: VPIN, VPIN? - (Virtual PIN)
layer: L1
stage: pin
tags: [vpin, l1, firmware-command, pin, virtual-pin, pin-configuration, result-logging, query-command]
related: [pin, command-reference, udvp, dfpn, smartest-7.10.0, smartest-7.10.3]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.03.02.35_VPIN__VPIN__-__Virtual_PIN.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# VPIN, VPIN? - (Virtual PIN)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **697 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.03.02.35_VPIN__VPIN__-__Virtual_PIN.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### VPIN

```
VPIN (pinlist)
```

### VPIN?

```
VPIN? ([(pinlist) | @]}
```

### Parameters

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/353731.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 4 列。
> 首行（上游原文）：pinlist | The name to be allocated to the pin. The query returns the name of the virtual pins that have been defined. The @ symbol can be used with the VPIN? qu…

### Example

- To define a virtual pin:

```
> VPIN (VPIN1)
```

- To define multiple virtual pins:

```
> VPIN (VPIN2,VPIN3)
```

- To list all defined virtual pins:

```
> VPIN? (@)
```

Returns:

```
< VPIN (VPIN1,VPIN2,VPIN3)
```

- To check for the existence of specific virtual pins:

```
> VPIN? (VPIN2,VPIN4,VPIN6)
```

Returns:

```
< VPIN (VPIN2)
```

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.03.02.35_VPIN__VPIN__-__Virtual_PIN.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error occurs if:

- The specified pin name has already been defined for another pin (virtual or not), port, or group.

<!-- 报错节 end -->

## 是什么

**`VPIN`（Virtual PIN）在软件里给一个「虚拟 pin」分配一个名字。** 原文第一段把机制讲完了，
**一句不多**——本页大半内容都是把这一段拆开：

> 「The VPIN (Virtual PIN) command allocates a name for a virtual pin in the software.
> The virtual pin is not connected to a pogo pin, but can be used to log certain test results.
> Virtual pins cannot be members of ports or groups. The VPIN? query returns a list of virtual pins
> that have been defined.」

| 原文 | 读出来是什么 |
|---|---|
| `allocates a name for a virtual pin in the software` | **产物是一个「名字」**，而且分配发生在 `in the software` |
| `The virtual pin is not connected to a pogo pin` | **它不对应任何物理 pogo pin** |
| `but can be used to log certain test results` | **但它可以拿来记录某些测试结果** |
| `Virtual pins cannot be members of ports or groups` | **它不能成为 port 或 group 的成员** |
| `The VPIN? query returns a list of virtual pins that have been defined.` | 查询侧：返回已定义的清单 |

**一句话机制：`VPIN` 买的是一个「可以出现在结果里的名字」，不是一个「可以接探针的通道」。**
——**它和实体 pin 的关键差别就在 `not connected to a pogo pin` 这一句**：
实体 pin 背后有通道、有 pogo、有 `CHIN?` 能查到的物理位置；
虚拟 pin **只有名字**。

**两处原文用词很紧，不能读宽：**

> **① `log certain test results`——`certain` 是个限定词，而原文没有列出是哪一些。**
> **「虚拟 pin 到底能记录哪些结果」——语料未写。**
> **照着这句话推「什么结果都能记」是读多了。**

> **② `in the software` 是原文对它的唯一定位。**
> **虚拟 pin 在 pattern / timing / level / testflow 里能不能用、怎么用——本篇一个字没写。**

### 两个方向：`VPIN` 定义，`VPIN?` 查询

| 命令 | 语法（逐字） |
|---|---|
| **`VPIN`**（定义） | `VPIN (pinlist)` |
| **`VPIN?`**（查询） | `VPIN? ([(pinlist) | @]}` |

> ⚠️ **`VPIN?` 那行括号不配对**：`(` 开头，`]}` 收尾。
> **上一行 `VPIN` 用的是 `(pinlist)`（成对），而这一行不是。**
> **核过上游 `raw/353731.htm`：htm 里就是 `VPIN? ( [( pinlist ) | @ ] }`**——
> **这是上游就有的**（§11.2 ⑥ 的判法），不是转换坏的。**本页照原样引，不替它补括号。**

**按本篇与同族语法行的写法读（推断）**：这一行想写的应该是 `{[(pinlist) | @]}`——
**花括号是「这里填东西」的占位框、方括号表示「可省」**。
依据有两条：① 括号要成对，而 `]}` 收尾就说明**外面那个应该是 `{`**；
② 定义那一行 `VPIN (pinlist)` 里的圆括号是**要照写的字面字符**。
**本篇没有符号说明表**，**所以这是本页的推断，不是文档事实**——**原文怎么写，本页就怎么引。**

### 参数只有 `pinlist` 一格，而它把两个命令的说明写在了一起

> 「The name to be allocated to the pin. The query returns the name of the virtual pins that
> have been defined. The @ symbol can be used with the VPIN? query to list all pins previously
> defined by the VPIN command. If you query a non-existent pin name, the system returns nothing.」

**这一格里其实有两段话，属于两个不同的命令**（**本篇没有为它们各写一格**）：

| 句 | 属于哪一边 | 逐字 |
|---|---|---|
| 第 1 句 | **`VPIN`** | `The name to be allocated to the pin.` |
| 第 2 句 | **`VPIN?`** | `The query returns the name of the virtual pins that have been defined.` |
| 第 3 句 | **`VPIN?` 的 `@`** | `The @ symbol can be used with the VPIN? query to list all pins previously defined by the VPIN command.` |
| 第 4 句 | **`VPIN?` 的边界情况** | `If you query a non-existent pin name, the system returns nothing.` |

**`@` 只在查询侧有意义**——原文写的是 `The @ symbol can be used with the VPIN? query`，
**`VPIN (pinlist)` 那一行没有 `@` 这一说**。
**而且本篇的 `## Errors` 里没有「名字不许含 `@`」这一条**——
**所以这里不存在「`@` 一边当通配符、一边被禁用」的双身份问题**
（这一点是本页对**本篇**的核对结论，不是从别处推的）。

### ⚠️ 「returns nothing」与第四个例子对不上——**这是本页最要紧的一处**

| 处 | 逐字 |
|---|---|
| 参数格第 4 句 | `If you query a non-existent pin name, the system returns nothing.` |
| 例子的第 4 条 | `> VPIN? (VPIN2,VPIN4,VPIN6)` → `< VPIN (VPIN2)` |

**那三个名字里 `VPIN4` 与 `VPIN6` 并不存在，系统返回的是 `VPIN (VPIN2)`——
不是 `nothing`。** 两种读法**只有一种能让例子和这句共存**：

| 读法 | 后果 |
|---|---|
| **按「整条查询」读**（问不到东西就什么都不返回） | **与例子矛盾**——例子明明返回了一个名字 |
| **按「逐个名字」读**（不存在的那个名字不返回东西，其余的照返回） | **与例子一致**——`VPIN4` / `VPIN6` 各自「没有东西可返回」，`VPIN2` 有 |

**原文没有说该按哪种读，本页不替它裁。**
**但实操上的后果是确定的，而且比措辞重要**：
**`VPIN?` 一次问一串名字时，返回的清单会被自动筛短，只留存在的那些**——
**所以它可以用作「批量判存在」**（例子自己的小节标题就是
`To check for the existence of specific virtual pins:`）。
**反过来，「问一个不存在的名字」你拿到的是空、不是报错**——
**这跟「名字撞了会报错」（见下）是两回事，别混。**

### 名字不许撞：虚拟 pin 与实体 pin 共用一套命名空间

（全文见上面「报错条件」节，脚本逐字取自本篇 `## Errors`。）

> 「An error occurs if:
>
> - The specified pin name has already been defined for another pin (virtual or not), port, or group.」

| 这个名字已经被谁用了 | 会不会报错 |
|---|---|
| **另一个 pin**（**`virtual or not`——虚拟的也算**） | **报错** |
| **一个 port** | **报错** |
| **一个 group** | **报错** |

**`(virtual or not)` 这半句是本节的信息量所在**：**虚拟 pin 与实体 pin 共用一个命名空间**——
**你不能拿一个已经给数字通道用过的名字去建虚拟 pin，反过来也一样。**
（**推断**，依据就是这一句自己。**原文没有正面写「共用命名空间」这句话**。）

**注意这和正文那句不是一回事，两句话方向相反、说的是两件事**：

| 句子 | 说的是 | 出处 |
|---|---|---|
| `Virtual pins cannot be members of ports or groups` | **进去了之后不能当成员**（结构问题） | 正文第一段 |
| `has already been defined for another … port, or group` | **名字不能和 port / group 已有的名字撞**（命名问题） | `## Errors` |

**一条讲「能不能进去」，一条讲「名字会不会撞」。`VPIN` 建出来的 pin 进不了 port / group，
但它的名字依然会和一个已有的 port 名撞。**（**这是本页把两句话并列后的读法，原文没有把它们放在一起讲。**）

### 四个例子：读法、符号、和他们之间的状态

| # | 命令（逐字） | 返回（逐字） | 这一条在演示什么 |
|---|---|---|---|
| 1 | `> VPIN (VPIN1)` | （无） | 定义一个虚拟 pin |
| 2 | `> VPIN (VPIN2,VPIN3)` | （无） | **一次定义多个，逗号分隔** |
| 3 | `> VPIN? (@)` | `< VPIN (VPIN1,VPIN2,VPIN3)` | **列全部**：一行、逗号分隔 |
| 4 | `> VPIN? (VPIN2,VPIN4,VPIN6)` | `< VPIN (VPIN2)` | **查特定的几个**（结果被筛短，见上） |

**两个符号的分工，本篇没有符号说明，是按例子读出来的（推断）**：
`>` 开头的是**你发出去的**，`< ` 开头的是**系统回来的**。
依据是**前两个例子只有 `>` 行、没有 `Returns:`，而后两个例子有 `Returns:` 且紧跟一行 `< ` 开头的**。

**另外，例 3 的返回清单正好是例 1 与例 2 定义过的那三个名字**（`VPIN1`、`VPIN2`、`VPIN3`）——
**也就是说这三条例子看起来是连着同一条会话跑的**（**推断**，
依据是返回的清单与前面定义过的名字**逐字对应、一个不多一个不少**；
**原文没有说例子之间是连续的**）。

## 典型用法

**本篇没有 `## Procedure` / `## Before you begin` / `## What to do next`**——
用法全部来自 `## Examples` 四条、`## Parameters` 那一格、以及正文第一段。
**四条例子已经是全部，本页只把它们排成顺序**：

```
① 想好一个没被占用的名字
② VPIN (名字)              或  VPIN (名字1,名字2)   ← 定义
③ 拿这个名字去记录它该记的那类结果                  ← 本篇只写「certain test results」
④ VPIN? (@)  或  VPIN? (…)                        ← 查已定义的有哪些
⑤ （要撤掉时）UDVP                                ← 本篇只在 Related information 点名
```

| 要做的事 | 怎么写 | 依据 |
|---|---|---|
| 定义一个虚拟 pin | `VPIN (VPIN1)` | `## Example` 第 1 条 |
| **一次定义多个** | `VPIN (VPIN2,VPIN3)`——**逗号分隔** | `## Example` 第 2 条 |
| **列出全部已定义的** | `VPIN? (@)` | `## Example` 第 3 条 |
| **批量查某几个是否存在** | `VPIN? (名字1,名字2,名字3)` | `## Example` 第 4 条 |
| 查一个不存在的名字 | 返回是**空**，**不是报错** | `If you query a non-existent pin name, the system returns nothing.` |
| **撤掉一个虚拟 pin** | **用 `UDVP`**——**本篇没有删除语法** | `## Related information` 唯一点名的命令，见 [[udvp]] |
| 用虚拟 pin 记具体哪一类结果 | **语料未写** | 正文只有 `certain test results`，没有清单 |

**三条容易踩的约束**：

1. **名字要先查重**（`VPIN? (@)` 或直接 `VPIN? (<你想用的名字>)`）——
   **撞了会报错**，而且**撞的对象可能是实体 pin、port 或 group**（见上）。
2. **虚拟 pin 进不了 port / group**——**这一条是正文写死的，不是建议**。
3. **`@` 只在查询侧用**——`VPIN` 那一行没有 `@` 写法。

**归属**：原文 `## Application` 一节全文只有一句——
`Creating virtual pins, see Virtual pins.`
**注意它的链接是往上跳层的**：目标在 `../02.08_Setup_and_Result_Tools/02.08.04.18.02.07.01_Virtual_pins.md`
——**即「怎么创建虚拟 pin」的做法不在命令参考章里，在 Setup and Result Tools 章**。
（那篇**本页没读**。）**这一句是 [[pin]] 与 [[command-reference]] 两个 `related` 的依据。**

**出错时**：**本篇 `## Errors` 只有一条**（就是名字撞了那条），而且**没有 `## Warnings` 段**
（已核：`## Warnings` 在本篇 0 命中）。
**特别提醒一句**：**「查一个不存在的名字」不在报错条件里**——
**本篇 `## Errors` 只有「名字已被占用」一条**，查询查不到是**返回空**。

## 和谁有关

- [[pin]] / [[command-reference]] —— **归属**：`stage: pin` 的依据是 `## Application`
  指向 `Creating virtual pins, see Virtual pins.`；文档本身在 `02.06_Command_Reference` 下。
  （§6：`stage` 填的是**最近的一段**，不是归属。）
- [[udvp]] —— **本页 `## Related information` 唯一点名的命令**，
  也是**唯一能撤掉虚拟 pin 定义的路径**（本篇没有任何删除语法）。
  原文那一行逐字：
  `[UDVP - (UnDefine Virtual Pin)](<02.06.03.02.29_UDVP_-__UnDefine_Virtual_Pin.md>)`
  ——**关系是「本页建 / 那页撤」**。**那篇本页没读**，所以 `UDVP` 的语法本页一个字没有。
- [[smartest-7.10.0]] —— **引入版本页**：本篇 `## Functional changes` 只有一条
  `Introduced in SmarTest 7.10.0`，那页收的就是这条。
- [[smartest-7.10.3]] —— 本 wiki 面向的版本；**本篇的版本段停在 7.10.0**（见「版本」）。
- `Virtual pins`（**未建、且不在 allowlist 里**）—— **`## Application` 指定的那篇做法文档**，
  在 `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.02.07.01_Virtual_pins.md`。
  **「虚拟 pin 在 GUI 里怎么建、建成什么样」本页一个字没有。**
- [[dfpn]] —— **`（推断）`：实体 pin 的定义侧对家**。**本篇没有点名 `DFPN`**
  （已核：`DFPN` 在本篇 0 命中）。依据是 `## Errors` 里那句
  `has already been defined for another pin (virtual or not)`——
  **它承认存在「定义实体 pin」这条路径，而本篇不负责它**。
  **「实体 pin 拿什么定义」本篇一个字没写**——**这条是推断，不当文档事实用。**
- `port` / `group` / `pogo pin`（**均未建、且不在 allowlist 里**）——
  **本页三个关键否定句都挂在它们身上**（不对应 pogo pin、不能进 port / group、名字不能撞 port / group）。
  **它们各自是什么、怎么建，本页答不了**——本篇一个链接都没给。
- **`UDEF` / `CHIN` 这一族**——**本篇一个字没提**（已核：`UDEF` / `CHIN` 在本篇 0 命中）。
  **本页不写它们**，尽管它们同属 pin 配置类命令。

> **本页只有一条 `（推断）`（`DFPN` 那条），以及三处标了 `（推断）` 的读法**
> （`VPIN?` 的括号读法、例子里 `>` / `<` 的分工、例子之间是连续的）。
> **其余每条都能在本篇里指到原句。**

## 版本

本文档**有** `## Functional changes` 段，**只有一条，逐字**：

```
- Introduced in SmarTest 7.10.0
```

**这一条是明写的成立版本，不是 §11.2 ② 那个 `Introduced before …` 哨兵值**——
**所以 `VPIN` / `VPIN?` 确实是 SmarTest 7.10.0 引入的**，
这也和本篇正文对得上：**它是一套全新的东西**（虚拟 pin 这个概念、
`@` 查询、与实体 pin 共用命名空间，都是新机制的样子）。

**与 wiki 面向版本的关系**：本 wiki 面向 **SmarTest 7.10.3**（[[smartest-7.10.3]]），
**而本篇的版本段停在 7.10.0**——**所以 7.10.0 之后 `VPIN` 有没有变过，语料里没有。**
**本页写的全部是 7.10.0 时点的说法。**

> **一处本页特意不写的东西**：`## Functional changes` 里**没有**「`VPIN` 在 7.10.x 上被改过」
> 这类条目，**所以「7.10.0 引入时尚不完善、后面补了什么」本页一个字都不猜。**

## 出处

`sources:` 一篇：
`02_System_reference/02.06_Command_Reference/02.06.03.02.35_VPIN__VPIN__-__Virtual_PIN.md`
（TDC `353731.htm`；**md 1,866 字节 / 88 行**，上游 htm 4,587 字节）。**整篇读完——本篇只有 88 行。**

**本页没做的**：

- **图：本篇没有内嵌图片。** 判据可核：本篇 md 里 `.png` / `.jpg` / `![` **0 命中**。
  **所以本页没有任何来自图的结论**（§11.4）。
- **`Virtual pins`（`02.08.04.18.02.07.01`）没读**——**`## Application` 唯一的指向**。
  **所以「虚拟 pin 在 GUI / Setup Tool 里怎么建、建完长什么样、在哪儿能看到它」
  本页一个字没有**；本页只有命令行这一侧。
- **[[udvp]] 的原文没读**——**「怎么撤掉一个虚拟 pin」的语法本页没有**；
  本页只有 `## Related information` 点名它的那一行。
- **没有 `## Warnings` 段**（已核，0 命中），只有 `## Errors` 一条。
  **脚本那条报错节的抬头写的是 `## Errors` / `## Warnings` 两个段名——
  对本篇来说 `## Warnings` 是空的。**
- **`certain test results` 到底是哪一些结果，本篇没有列**——
  **所以「虚拟 pin 能记什么」这一条本页只能写「语料未写」。**
- **虚拟 pin 在 pattern / timing / level / testflow 里的可用性，本篇没有写**——
  **本页不拿别处的文档补这一块。**
- **没有实跑。** 没有在机台上发过 `VPIN` / `VPIN?`、没建过虚拟 pin、
  没触发过「名字已被占用」那条报错、**也没验证过 `VPIN? (名字,不存在的名字)` 到底返回什么**。
  `verified: doc-only` 说的就是这件事（§11：文档里有 ≠ 这台机器上能用）。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**（§11.2）。
> **本篇 md 的 CJK 字符数实测为 0**——**没有 §11.2 ① 那一族编码乱码。**
>
> **① `VPIN?` 的语法行括号不配对。** 逐字：
> `VPIN? ([(pinlist) | @]}`
> ——**`(` 开头、`]}` 收尾**。**核过上游 `raw/353731.htm`：htm 里就是
> `VPIN? ( [( pinlist ) | @ ] }`，一模一样**——**所以是上游就有的**（§11.2 ⑥），
> **不是 md 转换坏的，重做转换也救不回来。**
> **本页照原样引**（「语法 / 参数」节里就是这一行），**正文里那条正确写法标了 `（推断）`。**
>
> **② 参数格那句 `returns nothing` 与例子 4 的返回对不上。** 逐字两处：
> `If you query a non-existent pin name, the system returns nothing.`（参数格）
> 对 `< VPIN (VPIN2)`（例 4 在 `VPIN? (VPIN2,VPIN4,VPIN6)` 之后的返回）。
> **核过上游 `raw/353731.htm`：两处都一模一样**（§11.2 ⑥）——
> **这是文档自己内部的措辞不严，不是转换问题。**
> **本页不替它裁**（两种读法都列在「是什么」里），
> **只把「例子演示了什么」照实记下来。**
>
> **③ 同一个概念在一段里大小写摇摆：`virtual pin` / `Virtual pins`。**
> 逐字：`allocates a name for a virtual pin in the software`（小写 `v`）
> → `The virtual pin is not connected to a pogo pin`（小写）
> → `Virtual pins cannot be members of ports or groups`（**大写 `V`**）
> → `returns a list of virtual pins that have been defined`（小写）。
> **四处在同一段里，全篇其余地方也两种混用。**
> **`virtual pin` 不是命令、不涉大小写敏感（§11 那条只管命令名）**——
> **本页照原样引，不替它统一；也不把它当成某个专有名词的定名。**
>
> **④ `## Parameters` 那张表在 raw 里被压平，而且只有一个 `pinlist` 格。**
> 逐字（本篇 `## Parameters` 起头的**完整原文**）：
> ```
> ## Parameters
>
>  |
>
> pinlist
>
>  |
>
> The name to be allocated to the pin. The query returns the name of the virtual pins that have been defined. The @ symbol can be used with the VPIN? query to list all pins previously defined by the VPIN command. If you query a non-existent pin name, the system returns nothing.
>
>  |
> ```
> ——**每一格独占一行，中间夹着孤立的 ` | `**。**「语法 / 参数」节里那个孤零零的 ` | ` 就是它**
> （同批的 [[dfut]] / [[dfpr]] / [[pslv]] 同一形态）。
> **说明文字一个字没丢**，但**本篇 raw 里没有表头行**。
> **而且两个命令（`VPIN` 与 `VPIN?`）共用这一格**——上面「是什么」里那张
> 「哪一句属于哪一边」的表是本页的整理，**不是原文分好的**。
>
> **⑤ `## Related information` 一节只有一行、一个链接，没有任何说明文字。**
> 逐字：
> ```
> ## Related information
>
> [UDVP - (UnDefine Virtual Pin)](<02.06.03.02.29_UDVP_-__UnDefine_Virtual_Pin.md>)
> ```
> ——**原文没有说「为什么要看它」**。上面「和谁有关」里那句「本页建 / 那页撤」
> **是本页从两个命令名读出来的，原文那一节一个字都没解释。**

`verified: doc-only`
