---
type: object
title: UDUT - (UnDefine UTility line)
layer: L1
stage: pin
tags: [udut, l1, firmware-command, pin, utility-line, undefine, license-lock]
related: [dfut, udup, utility-lines, set-utility-lines, get-utility-lines, sequencer-controlled-utility-lines, udpr, udps, udpt, udvp, pin, command-reference, pin-config-locked-during-test]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.302_UDUT_-__UnDefine_UTility_line.md
created: 2026-09-24
updated: 2026-09-28
verified: doc-only
---

# UDUT - (UnDefine UTility line)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **394 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.302_UDUT_-__UnDefine_UTility_line.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
UDUT {(util_name)}
```

### Parameters

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98831.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：util_name | Specifies the utility line name or names to be undefined. The symbol @ removes all utility line definitions. If more than one name is to be removed,…

### Example

```
UDUT (@)
```

This command undefines all defined utility line names.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.302_UDUT_-__UnDefine_UTility_line.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if the referenced utility line has not been defined before.

<!-- 报错节 end -->

## 是什么

**`UDUT`（UnDefine UTility line）撤掉一条已经定义的 utility line 名，
并且顺手把那条 write utility line 的输出置成 0（低电平）。**
原文一句话说完：

> 「The UDUT (UnDefine UTility line) command removes a defined utility line name from the
> configuration, thereby setting the output state of write utility lines to 0 (low output).」

| 要素 | 值 |
|---|---|
| **动作** | `removes`——**撤，不是改** |
| **对象** | `a defined utility line name`——**只对「已经定义过」的名字有意义** |
| **作用域** | `the configuration`——**动的是配置** |
| **副作用** | **`thereby setting the output state of write utility lines to 0 (low output)`——输出态被置 0** |
| **产物** | **本篇未写有什么产物**——没有返回示例、没有状态查询 |

**⚠️ 那个副作用是本页最要紧的一句，也是它和同族的 [[udup]] 唯一的实质差别。**
`UDUP` 撤 utility purpose 时**没有这一句**；`UDUT` 撤 utility line 时**有**。
**原文用 `thereby`（从而）把两件事绑在一句里**——
**「撤定义」和「输出变 0」不是两件可选的事，是同一次操作的因果。**

**⚠️ 但原文只写到「输出态是 0」为止**：

| 想知道的事 | 本篇答得了吗 |
|---|---|
| 撤掉之后输出态是什么 | ✅ `0 (low output)` |
| 这个 0 是电压上的低电平、还是逻辑上的 0 | ❌ **语料未写** |
| 它作用在哪条线上（`write utility lines` **是复数**） | ❌ **语料未写**——撤的是一条线，为什么写的是复数，原文没说 |
| 对 DUT 上的信号有什么物理后果 | ❌ **语料未写** |
| 这条线以后还能不能再被驱动 | ❌ **语料未写** |

**「输出变 0」是文档事实；「这个 0 意味着什么」本篇一个字没有。**

### 参数只有 `util_name`，说明里 **三句话讲三件事**

参数表那一格逐字（三句是三段，原文就是三个 `<p>`）：

> 「Specifies the utility line name or names to be undefined.」

> 「The symbol @ removes all utility line definitions.」

> 「If more than one name is to be removed, the names must be separated by a comma.」

| 你写什么 | 效果 | 依据 |
|---|---|---|
| **一个名字** | 撤掉那一个 | 第 1 句 `name or names` |
| **多个名字**（**必须逗号分隔**） | 撤掉那几个 | 第 3 句 |
| **`@`** | **`removes all utility line definitions`——撤掉全部** | 第 2 句 |

**`@` 的范围要说准**：原文写的是 `all utility line definitions`（**全部 utility line 定义**）——
**不碰 utility purpose，也不碰 pin**。对照 [[udup]]：那一篇对应位置写的是
`removes all utility purpose definitions`——**两句句型完全一样、只有对象词不同。**
**⚠️ 一个要紧的推论：`UDUT (@)` 是全撤，它会把每一对写线都置 0。**
（**推断**，依据是 `thereby setting the output state of write utility lines to 0` 那句
讲的是**本命令**的因果，而 `@` 只是把对象扩到全部——**原文没有单独为 `@` 说一遍后果**。）

**语法的括号 `{}` 与 `()`**：语法行逐字是 `UDUT {(util_name)}`，例子逐字是 `UDUT (@)`——
**圆括号是要照写的字面字符，花括号是占位框**（读法与 [[udef]] 一致：
**本篇的例子、正文里花括号一次都没出现过**）。
**原文没有解释这两种括号的分工**，**所以这一步是推断，不是文档事实。**

### 例子只有一条，而且它用的是 `@`——**本篇没有「撤单个」的例子**

> 「This command undefines all defined utility line names.」

**唯一的例子是 `UDUT (@)`（全撤）。**
**「撤一条 / 撤几条」的写法要自己从参数说明推**（`name or names` + `separated by a comma`），
**本篇没有给那种命令行示例。**

### 报错条件：一句话，而且它是本篇唯一一条「前置条件」

（逐字见上面「报错条件」节，脚本取自本篇 `## Errors`。）

> 「An error is generated if the referenced utility line has not been defined before.」

**这句话同时是本篇唯一一处讲「顺序」的地方**：**先定义、后撤**，
没定义过的名字拿来撤 **就报错**。**注意它用的词是 `referenced`（被引用的）**——
原文把 `UDUT` 的参数看成一个**引用**，而不是「一个待删的字符串」。

| 情况 | 会不会报错 |
|---|---|
| `util_name` 没定义过 | **报错**（这一条就是） |
| `@`（全撤）、而当时**一条都没定义** | **本篇未写**——`referenced` 指的是谁，原文没说清 |
| 撤掉一条正在被时序/pattern 使用的线 | **本篇未写** |

**后两行是「本篇没写」，不是「不报错」**（§2.1：没找到 ≠ 文档没有）。
**本篇也没有 `## Warnings` 段**（已核，0 命中）。

## 典型用法

**本篇没有 `## Procedure` / `## Before you begin` / `## What to do next`**——
用法只有 `## Example` 一条 + `## Parameters` 那一格。**按目的查**：

| 要做的 | 发什么 | 依据 |
|---|---|---|
| **撤掉全部 utility line** | `UDUT (@)` | `## Example` 逐字 |
| **撤掉一条** | `UDUT (util_name)`——**原文没有这个例子，是按参数说明写的** | `Specifies the utility line name or names to be undefined.` |
| **撤掉几条** | `UDUT (u1,u2)`——**逗号分隔**，同样**没有例子** | `the names must be separated by a comma` |
| 先看有哪些 utility line 可以撤 | **本篇没有查询语法**——见下 | — |
| 定义回来 | **本篇没有这个语法**——见「和谁有关」的 [[dfut]] | — |

**顺序上的前提**：**先定义、后撤**（见上面那一条报错句）。
**「谁定义的」本篇没指向任何命令**（见「和谁有关」）。

**操作上先想清楚的一件事：撤线会把它的输出打到 0。**
这是本篇第一个动作就带来的**物理侧变化**（`thereby setting the output state of write utility lines to 0`），
**不是「只是把名字从配置里划掉」。** **原文没有写这个 0 在 DUT 那侧意味着什么**——
**所以要不要先驱动到安全态，本页给不出依据，只能指出这一句的存在。**

**「怎么列出已有的 utility line」本篇答不了**：本篇**没有任何查询命令**
（已核：本篇 `?` **0 命中**）。**查到名字的那条路在本篇之外**（**本页没读那几篇**）。

**一条家族级的锁**：[[pin-config-locked-during-test]]。
`UDUT` 所属那一章（`Pin configuration setup commands`）的**章首**写着
`The firmware does not accept any configuration changes while a test is running.`
**这一句不在本篇正文里**（见「出处」）。
**注意别套错另一条**：[[pin-config-requires-sequencer-off]] 那条（「sequencer 非 OFF 不许改」）
点名的命令是 `DFPN` / `UDEF` / `CONF` / `PALS`，**里面没有 `UDUT`**——
**本篇的 `## Errors` 只有上面那一句，不含 sequencer 状态。**

## 和谁有关

### 这一族的结构：`UDxx` 是 `DFxx` 的撤销面

**这六个页面（[[udut]] / [[udpr]] / [[udps]] / [[udpt]] / [[udup]] / [[udvp]]）是同一族命令的撤销侧。**
族的划分**不是本页猜的**：`02.06.03_Pin_configuration_setup_commands.md` 逐条给了分组，
逐字（已剥链接标记）：

| 分组（逐字） | 命令 |
|---|---|
| `Commands for utility lines:` | `DFUT`, **`UDUT`**, `DFUP`, `UPAS`, `UDUP` |
| `Commands for DPS pins:` | `DFPS`, `UDPS` |
| `Commands for pin alias:` | `DFPR`, `UDPR` |
| `Commands for pin groups and ports:` | `DFGP`, `UDGP`, `DFPT`, `UDPT` |
| — | `UDVP` **不在这个索引里**（实测 0 命中） |

**本页那一行是五条命令挤在一行**——逐字：

> 「Commands for utility lines: DFUT, UDUT, DFUP, UPAS, UDUP」

**它把 utility line 与 utility purpose 两条线合成了一个分组**：
`DFUT`/**`UDUT`** 是**线**那一对，`DFUP`/`UDUP` 是**用途**那一对（见 [[udup]]），
中间的 **`UPAS`（Utility Purpose ASsignment for multi-site）是第三个成员**。

**所以本页的正命令是 [[dfut]]**（同一行上的 `DeFine UTility line`）。

- [[dfut]] —— **正向命令：那页定义 utility line，本页撤掉。**
  **⚠️ 但这一条配对关系本页只能引索引**——
  **`UDUT` 自己的原文里 `DFUT` 0 命中**（实测），
  而且本篇的 `## Application` 也**没有**指向 `DFUT`。
  **「拿 `DFUT` 建、拿 `UDUT` 撤」是索引那条分组行的文档事实，
  不是本页原文的文档事实。** **本页没读 `DFUT` 的 raw。**
- [[udup]] —— **同族里最近的邻居，也是本页最该对照的一页**：
  两页的**语法形状、参数句型、例子的形式完全平行**（`UDUT {(util_name)}` 对
  `UDUP {(purpose_name)}`；`removes all utility line definitions` 对
  `removes all utility purpose definitions`；`UDUT (@)` 对 `UDUP (@)`）。
  **唯一的实质差别**：**本页第一句多了一个副作用**——
  `thereby setting the output state of write utility lines to 0 (low output)`，**`UDUP` 没有这句。**
  **本篇原文里 `UDUP` 0 命中、[[udup]] 原文里 `UDUT` 也 0 命中**（两边都实测过）。
- [[upas]] —— **同一行上的第三个成员**（`Utility Purpose ASsignment for multi-site`）。
  **本篇原文里 `UPAS` 0 命中**。**本页没读它。**
- [[utility-lines]] —— **本命令撤的那个对象**。
  **⚠️ 「utility line 是什么」本篇不定义**——它的 `## Application` 只有一句
  `For details about utility lines, see Configuration Setup Commands.`（**本页读了那一篇，
  它也不定义 utility line，只给分组表**）。**[[utility-lines]] 那一页本页没读**，
  所以它有没有补上这个定义，**本页不知道**。
- [[set-utility-lines]] / [[get-utility-lines]] / [[sequencer-controlled-utility-lines]] ——
  **同一对象域里的「驱动 / 读 / 控制」侧**。
  **本篇原文里这三个名字 0 命中，它们也都不在 `UDUT` 的入边里**（实测入边 6 条，
  见「出处」）——**这几条是按对象域列的，不是文档事实。本页没读它们。**
  **⚠️ 唯一一条把本页与它们连起来的依据是本篇那一句 `to 0 (low output)`：**
  **如果那些命令能把线驱动到 1，那么 `UDUT` 的副作用就是「把它打回 0」**——
  **但这是推断，本页没有读它们的原文来证实。**
- [[utility-line-view]] / [[utility-line-assignments]] —— **GUI / 分配侧的相邻页**。
  **同上：本篇 0 命中，本页没读，只是对象域相邻。**
- [[udpr]] / [[udps]] / [[udpt]] / [[udvp]] —— **同一族的另外四页**，见上表。
- [[pin]] / [[command-reference]] —— **归属**：本篇在 `02.06_Command_Reference` 下，
  而 `## Application` 指向 `Configuration Setup Commands.`。
  **⚠️ 但本篇在语料里被放进了三个不同的章**（见「出处」⚠️ ⑤）——
  它在 `02.06.12_Utility_Line_Commands` 那一系列里**也有一份**，
  **而那一份的 `## Application` 指的仍然是 pin configuration 那一章。**
  （§6：`stage` 填的是**最近的一段**，不是归属。）
- [[pin-config-locked-during-test]] —— **适用于本命令的那条锁**（见「典型用法」）。

### 一条入边把本命令概括得更短——值得对照

`02.06.03.01.05_Defining_a_utility_line.md`（**不在本篇 `sources:` 里，本页没读这篇的正文**）
第 14 行提到本命令，那一句逐字（剥掉链接标记后）：

> 「The UDUT command removes a utility line.」

**对照本篇第一句** `removes a defined utility line name from the configuration,
thereby setting the output state of write utility lines to 0 (low output)`——
**那一句把「名字」和「输出置 0」两样都省掉了，只剩「removes a utility line」。**
**⚠️ 本页只引 `edges.jsonl` 里那条带原句的边，没有回那一篇核上下文**——
**所以那一句前后还写了什么，本页不知道。**

### 一个本篇正文里完全没有、但别的文档明确点名的后果：DSL 授权锁

`02.04.05.08.02_Disabling_a_pin_configuration_license_lock.md`（**不在本篇 `sources:` 里，本页另读了它**）
把 `UDUT` 列进**能解除「pin configuration license lock」的命令**里，逐字（放在代码块里，
免得本页的引号把那个 `*` 吃成斜体）：

```
Several firmware commands can disable a device specific license lock, in other words, disable a pin configuration file. These firmware commands are *RST (ReSeT), UDAN (UnDefine ANalog pin), UDEF (UnDEFine pin), UDPS (Undefine DPS pin), UDUP (UnDefine Utility Purpose), and UDUT (UnDefine UTility line).
```

**即：跑一条 `UDUT`，会把 pin 配置文件的 device-specific license 签名作废。**
那一篇接着写（逐字）：

> 「The device-specific-license signature is no longer valid, the pin configuration file is
> unlocked, and the pin configuration related commands are enabled again.」

**⚠️ 本页的 `UDUT` 原文一个字都没提这件事。**
**这一条对本族里另外两页同样成立**：那份名单里还有 `UDPS` 与 `UDUP`
（见 [[udps]] / [[udup]]）。**`UDPR` / `UDPT` / `UDVP` 不在这份名单里**（本页核过）。

> **本页的 `（推断）` 有两处**：语法里 `{}` 与 `()` 的分工、`UDUT (@)` 会把每一对写线都置 0。
> 另外 [[set-utility-lines]] 那一条「把它打回 0」的读法也标了推断。
> 其余每条都能指到本篇原句，或上面那两篇被声明的文档的原行。

## 版本

`## Functional changes` 段有，**只有一条，逐字**：

```
- Introduced before SmarTest 6.3.2
```

**按 §11.2 ②，这不是「6.3.2 的变更记录」，是一个哨兵值。**
全语料那 2,677 条同款写法（`Introduced before …`）的意思是
「**在本文档集覆盖范围开始之前就已经有了**」——
**照字面读会生成一条「6.3.2 新增了 `UDUT`」的假信息，而且格式齐整。**

**所以：`UDUT` 究竟成立于哪个版本，这份语料里没有。**
本页只能记「**至少早于 6.3.2 的覆盖起点**」，**不能记成「6.3.2 引入」。**

**与同族的对照**：[[udpr]] 拿到的是**真版本号**（`Introduced in SmarTest 6.5.2`），
[[udvp]] 拿到的也是真版本号（`Introduced in SmarTest 7.10.0`），
而**本页与 [[udps]] / [[udpt]] / [[udup]] 拿到的都是哨兵值**。
**这不是本页的缺陷，是各篇文档各自的写法。**

**与 wiki 面向版本的关系**：本 wiki 面向 **SmarTest 7.10.3**，
**而本篇的版本段一条变更都没有**——**所以「6.3.2 之后 `UDUT` 有没有变过」语料里答不了。**

## 出处

`sources:` 一篇：
`02_System_reference/02.06_Command_Reference/02.06.02.02.302_UDUT_-__UnDefine_UTility_line.md`
（TDC `98831.htm`；**md 1,257 字节 / 46 行**，上游 htm 2,672 字节）。**整篇读完——本篇只有 46 行。**

**另外读了三篇 raw（本页 `sources:` 之外，逐条声明）：**

| 篇 | 为什么读 | 字节 / 行数 |
|---|---|---|
| `02.06.03_Pin_configuration_setup_commands.md`（TDC `10649.htm`） | **本篇 `## Application` 唯一指向的那一篇**；族的分组表与章首 Note 都在这里 | 3,305 B / 41 行 |
| `02.06.03.01.01_Introduction.md`（TDC `10650.htm`） | **同一张分组表在它里面也有一份**（用于判断那是「重复投放」还是「各写一遍」，§10 的判据） | 3,061 B / 37 行 |
| `02.04_Model_File_and_Licensing/02.04.05.08.02_Disabling_a_pin_configuration_license_lock.md`（TDC `114540.htm`） | **它是 `UDUT` 的一条入边**，而且给出一条本篇完全没写的后果（DSL 授权锁） | 3,831 B / 41 行 |

**还读了四篇 wiki 页（不是 raw）**：`wiki/objects/udef.md`、`wiki/objects/dfpr.md`
（对齐同族写法）、`wiki/constraints/pin-config-locked-during-test.md`、
`wiki/constraints/pin-config-requires-sequencer-off.md`（核对「哪条锁适用于本命令」）。

**本页的入边实测 6 条 / 6 篇**（`inline` + `toc` 口径，来源 `extract/edges.jsonl`）：
`02.06.12.02_List_of_utility_line_commands`、`02.06.02.02_List_of_commands`、
`02.06.03.01.01_Introduction`、`02.06.03.01.05_Defining_a_utility_line`、
`02.06.03_Pin_configuration_setup_commands`、`02_System_reference/index.md`。

**本页没做的**：

- **`DFUT` 的 raw 没读**——**本页连 `DFUT` 长什么样都不知道**，
  只知道索引那一行把 `DFUT` 与 `UDUT` 并列。**所以「utility line 怎么定义」本页一个字没有。**
- **`UPAS` 没读**——同一行上的第三个成员。
- **「utility line 到底是什么」本页答不了**：本篇把它推给
  `Configuration Setup Commands`，而**本页读了那一篇，它只给分组表**。
- **`set-utility-lines` / `get-utility-lines` / `sequencer-controlled-utility-lines` /
  `utility-lines` / `utility-line-view` / `utility-line-assignments` 一篇没读**——
  「输出态 0 怎么被读出来、怎么写回去」**本页答不了**。
- **`Defining_a_utility_line.md`（`02.06.03.01.05`）的正文没读**——
  本页只引了 `edges.jsonl` 里那条带原句的边（见「和谁有关」最后）。
- **`UTST - (UTility line STate)` / `UTOT - (UTility line OuTputs)` /
  `UTTI - (UTility line settling TIme)` 之类的兄弟命令没读**——
  它们存在于语料里（本页按文件名扫到过），**但本页没有读它们的正文**。
- **`Pin Configuration Example` 没读**——索引末尾指向它。
- **图：本篇没有内嵌图片。** 判据可核：本篇 md 里 `.png` / `.jpg` / `![` **0 命中**。
  **所以本页没有任何来自图的结论**（§11.4）。
- **没有实跑。** 没在机台上发过 `UDUT`、**没看过撤线之后那条线的实际电平**、
  没触发过那条 Error。`verified: doc-only` 说的就是这件事
  （§11：文档里有 ≠ 这台机器上能用；**这一页尤其如此——`0 (low output)` 是文档说的，不是量过的**）。
- **没有动 `wiki/index.md`**。

> ⚠️ **本篇的语料瑕疵与结构上要注意的地方，本页照实记下、一处都没替它改**（§11.2）。
> **本篇 md 的 CJK 字符数实测为 0**——**没有 §11.2 ① 那一族编码乱码。**
>
> **① `## Parameters` 那张表在 raw 里被压平，而且缺表头。** 逐字（本篇 `## Parameters`
> 起头那一段的完整原文）：
>
> ```
> ## Parameters
>
>  | util_name |
>
> Specifies the utility line name or names to be undefined.
>
> The symbol @ removes all utility line definitions.
>
> If more than one name is to be removed, the names must be separated by a comma.
>
>  |
> ```
>
> ——**参数名和说明各占一行、中间夹着孤立的 ` | `**。
> **⚠️ 注意它和同族的 [[udpr]] / [[udps]] / [[udpt]] 形态不同**：
> 那三篇的参数名是**单独一行**（`|` / 名字 / ` |`），
> 而本篇（和 [[udup]]）把 ` | util_name |` **挤在同一行**。
> **同一批文档、同一个版式，两种压平结果。**
> **说明文字一个字没丢**，但**本篇 raw 里没有 `Parameter` / `Description` 之类的表头行**——
> **所以「哪一列是什么」是从位置读出来的，不是原文写的。**
> **⚠️ 上游 `.htm` 里这张表是完整的**：`raw/98831.htm` 里写着
> `<table class="frame-topbot">`，里面是 `<colgroup><col><col></colgroup>`，
> `<tr>` 里两个 `<td>`。
> **所以「压平」是转换侧的产物，不是上游就坏的**（§11.2 ⑥ 的判法：回 `.htm` 核）。
>
> **② 第一句用单数，参数表用「单数或复数」。** 逐字：
> `removes a defined utility line name from the configuration`（**用的是单数名词短语**）
> 对 `Specifies the utility line name or names to be undefined.`（**`name or names`**）
> ——**两处不完全同构**。**⚠️ 对照同族的 [[udup]]：那一篇第一句是
> `removes one or more defined utility purpose names`（复数）**——
> **同一个句型，一篇用单数一篇用复数。本页并列，不替它统一。**
>
> **③ 同一个说法在本族里介词不一致。** 本篇逐字是
> `the names must be separated by a comma.`，
> 而 [[udps]] / [[udpt]] 逐字是 `the names must be separated with a comma.`
> ——**同一个句型，一个 `by` 一个 `with`**。本页照原样引，不替它统一。
>
> **④ 「撤一条线」却写成 `write utility lines`（复数）。** 逐字：
> `thereby setting the output state of write utility lines to 0 (low output)`
> ——**命令的对象是 `a defined utility line name`（单数），后果那一句却是 `lines`（复数）**。
> **原文没有解释这个数的不一致。本页照原样引，不替它改成单数。**
>
> **⑤ 本篇在语料里有**三份**投放，正文逐行完全相同。** 另两份是
> `02.06_Command_Reference/02.06.03.02.28_UDUT_-__UnDefine_UTility_line.md`
> （`source_topic: "98831_2.htm"`，1,260 字节）与
> `02.06_Command_Reference/02.06.12.02.04_UDUT_-__UnDefine_UTility_line.md`
> （`source_topic: "98831_3.htm"`，1,260 字节）。
> **实测 `diff`：三份的差别只有 frontmatter 的第 3、4 行**（`source_topic` / `source_html`），
> 那 1 字节的差就是 `98831` → `98831_2` / `98831_3`。
> **三份上游 `.htm` 也都在，而且 `cmp` 报三个文件完全一致**（都是 2,672 字节）——
> **所以这是上游 TDC 就有的重复投放，不是转换产生的**（§11.2 ⑥ 的判法）。
> **⚠️ 三份分属三个不同的章**：`02.06.02.02_List_of_commands`（本页 `sources:` 用的）、
> `02.06.03.02_List_of_configuration_commands`、`02.06.12.02_List_of_utility_line_commands`。
> **而三份的 `## Application` 都指向同一个 `Configuration Setup Commands`**——
> **这里有一个结构上的事实要记：本命令在 utility line 那一章里也有一份投放，
> 而那一份的 `## Application` 指的仍是 pin configuration 那一章。**
> 这是语料的结构，不是谁引错了。
> **本页的 `sources:` 用的是 `02.06.02.02.302` 那一份**；
> **另两份的内容本页没有另读一遍**（因为实测正文逐行相同）。

`verified: doc-only`
