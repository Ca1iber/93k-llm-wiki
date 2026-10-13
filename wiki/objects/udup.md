---
type: object
title: UDUP - (UnDefine Utility Purpose)
layer: L1
stage: pin
tags: [udup, l1, firmware-command, pin, utility-purpose, undefine, license-lock]
related: [dfup, upas, udut, utility-purpose-editor, udpr, udps, udpt, udvp, pin, command-reference, pin-config-locked-during-test, referenced-set-requires-prior-definition]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.301_UDUP_-__UnDefine_Utility_Purpose.md
created: 2026-09-24
updated: 2026-09-28
verified: doc-only
---

> ⚠️ **本页若干处记的是 2026-10-10【之前】的语料形态。**
> 那一轮把语料里的表格一律换成了**指向上游 HTML 的指针**
> （见 `extract/PLAN-表格指针化.md`）。所以下文凡是说「表格被压平 / 被摊平 /
> 一格一行」的地方，指的是**更换之前**的样子 —— 现在语料里那个位置是**一句指针**，
> 真表仍在 `tdc-html/raw/` 的上游 HTML 里。**页码/引文都不受影响。**

# UDUP - (UnDefine Utility Purpose)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **400 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.301_UDUP_-__UnDefine_Utility_Purpose.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
UDUP {(purpose_name)}
```

### Parameters

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98830.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：purpose_name | Specifies the utility purpose name or names to be undefined. The symbol @ removes all utility purpose definitions. If more than one name is to be…

### Example

```
UDUP (@)
```

This command undefines all defined utility purpose names.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.301_UDUP_-__UnDefine_Utility_Purpose.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if the referenced utility purpose has not been defined before.

<!-- 报错节 end -->

## 是什么

**`UDUP`（UnDefine Utility Purpose）把已经定义过的 utility purpose 名从配置里撤掉。**
原文一句话说完：

> 「The UDUP (UnDefine Utility Purpose) command removes one or more defined utility purpose
> names from the configuration.」

| 要素 | 值 |
|---|---|
| **动作** | `removes`——**撤，不是改** |
| **对象** | `one or more defined utility purpose names`——**是「名字」，而且明确可以一次撤多个** |
| **作用域** | `the configuration`——**动的是配置** |
| **产物** | **本篇未写有什么产物**——没有返回示例、没有状态查询 |

**⚠️ 「一个 utility purpose 到底是什么」本篇不定义。**
它的 `## Application` 只有一句（逐字）：

> 「For details about utility purposes, see Configuration Setup Commands.」

**即：本篇把「utility purpose 是什么」整个推给了另一篇文档，自己只讲「怎么撤」。**
（那一篇**本页读了**，见「出处」——**但它只给分组表，也不解释 utility purpose 是什么**。）

### 参数只有 `purpose_name`，说明里 **三句话讲三件事**

参数表那一格逐字（三句是三段，原文就是三个 `<p>`）：

> 「Specifies the utility purpose name or names to be undefined.」

> 「The symbol @ removes all utility purpose definitions.」

> 「If more than one name is to be removed, the names must be separated by a comma.」

| 你写什么 | 效果 | 依据 |
|---|---|---|
| **一个名字** | 撤掉那一个 | 第 1 句 `name or names` |
| **多个名字**（**必须逗号分隔**） | 撤掉那几个 | 第 3 句 |
| **`@`** | **`removes all utility purpose definitions`——撤掉全部** | 第 2 句 |

**`@` 的范围要说准**：原文写的是 `all utility purpose definitions`
（**全部 utility purpose 定义**）——**不碰 utility line，也不碰 pin**。
对照同族的 [[udut]]：那一篇对应位置写的是 `removes all utility line definitions`——
**两句句型完全一样、只有对象词不同**，这是这一族的标准写法。

**语法的括号 `{}` 与 `()`**：语法行逐字是 `UDUP {(purpose_name)}`，例子逐字是 `UDUP (@)`——
**圆括号是要照写的字面字符，花括号是占位框**（读法与 [[udef]] 一致：
**本篇的例子、正文里花括号一次都没出现过**）。
**原文没有解释这两种括号的分工**，**所以这一步是推断，不是文档事实。**

### 例子只有一条，而且它用的是 `@`——**本篇没有「撤单个」的例子**

> 「This command undefines all defined utility purpose names.」

**唯一的例子是 `UDUP (@)`（全撤）。**
**「撤一个 / 撤几个」的写法要自己从参数说明推**（`name or names` + `separated by a comma`），
**本篇没有给那种命令行示例**。

| 想知道的事 | 本篇答得了吗 |
|---|---|
| 全撤 | ✅ `UDUP (@)` |
| 撤一个 / 撤几个 | ⚠️ 参数表说了怎么写，**但没有例子** |
| utility purpose 是什么、干什么用 | ❌ **推给了 `Configuration Setup Commands`**（本页读了，见「出处」） |
| 撤掉之后那些 utility purpose 名下的分配会怎样 | ❌ **语料未写** |
| 撤一个没定义过的名字会怎样 | ✅ **报错**——见下 |

### 报错条件：一句话，而且它是本篇唯一一条「前置条件」

（逐字见上面「报错条件」节，脚本取自本篇 `## Errors`。）

> 「An error is generated if the referenced utility purpose has not been defined before.」

**这句话同时是本篇唯一一处讲「顺序」的地方**：**先定义、后撤**，
没定义过的名字拿来撤 **就报错**。**注意它用的词是 `referenced`（被引用的）**——
原文把 `UDUP` 的参数看成一个**引用**，而不是「一个待删的字符串」。
**这和 [[referenced-set-requires-prior-definition]] 那一页收的那一族（spec/search/jitter set）
是同一个形状**，**但用词不同**：那一族写 `does not exist` / `exists`，
本篇写 `has not been defined before`。**本页不把两者合并**（本页也没读那一页的 raw）。

| 情况 | 会不会报错 |
|---|---|
| `purpose_name` 没定义过 | **报错**（这一条就是） |
| `@`（全撤）、而当时**一个都没定义** | **本篇未写**——`referenced` 指的是谁，原文没说清 |
| 撤掉一个正在被别处引用的 purpose | **本篇未写** |

**后两行是「本篇没写」，不是「不报错」**（§2.1：没找到 ≠ 文档没有）。
**本篇也没有 `## Warnings` 段**（已核，0 命中）。

## 典型用法

**本篇没有 `## Procedure` / `## Before you begin` / `## What to do next`**——
用法只有 `## Example` 一条 + `## Parameters` 那一格。**按目的查**：

| 要做的 | 发什么 | 依据 |
|---|---|---|
| **撤掉全部 utility purpose** | `UDUP (@)` | `## Example` 逐字 |
| **撤掉一个** | `UDUP (purpose_name)`——**原文没有这个例子，是按参数说明写的** | `Specifies the utility purpose name or names to be undefined.` |
| **撤掉几个** | `UDUP (p1,p2)`——**逗号分隔**，同样**没有例子** | `the names must be separated by a comma` |
| 先看有哪些 utility purpose 可以撤 | **本篇没有查询语法**——见下 | — |
| 定义回来 | **本篇没有这个语法**——见「和谁有关」的 [[dfup]] | — |

**顺序上的一条硬前提**：**先定义、后撤**。
`## Errors` 那一句 `has not been defined before` 说的就是它——
**所以 `UDUP` 的用法是被「已经定义过」卡住的**。
**「谁定义的」本篇没指向任何命令**（见「和谁有关」）。

**「怎么列出已有的 utility purpose」本篇答不了**：本篇**没有任何查询命令**
（已核：本篇 `?` **0 命中**，不像 [[udps]] 那样开头就提到 `DFPS?`）。
**查到名字的那条路在本篇之外**（`Utility Purpose State` 之类的命令页，**本页没读**）。

**一条家族级的锁**：[[pin-config-locked-during-test]]。
`UDUP` 所属那一章（`Pin configuration setup commands`）的**章首**写着
`The firmware does not accept any configuration changes while a test is running.`
**这一句不在本篇正文里**（见「出处」）。
**注意别套错另一条**：[[pin-config-requires-sequencer-off]] 那条（「sequencer 非 OFF 不许改」）
点名的命令是 `DFPN` / `UDEF` / `CONF` / `PALS`，**里面没有 `UDUP`**——
**本篇的 `## Errors` 只有上面那一句，不含 sequencer 状态。**

**出错时**：本篇 `## Errors` **只有一条**（上面那句），**没有 `## Warnings`**——
**所以「还有什么别的错法」本篇答不了。**

## 和谁有关

### 这一族的结构：`UDxx` 是 `DFxx` 的撤销面

**这六个页面（[[udup]] / [[udpr]] / [[udps]] / [[udpt]] / [[udut]] / [[udvp]]）是同一族命令的撤销侧。**
族的划分**不是本页猜的**：`02.06.03_Pin_configuration_setup_commands.md` 逐条给了分组，
逐字（已剥链接标记）：

| 分组（逐字） | 命令 |
|---|---|
| `Commands for utility lines:` | `DFUT`, `UDUT`, **`DFUP`**, `UPAS`, **`UDUP`** |
| `Commands for DPS pins:` | `DFPS`, `UDPS` |
| `Commands for pin alias:` | `DFPR`, `UDPR` |
| `Commands for pin groups and ports:` | `DFGP`, `UDGP`, `DFPT`, `UDPT` |
| — | `UDVP` **不在这个索引里**（实测 0 命中） |

**本页那一行是五条命令挤在一行**——逐字：

> 「Commands for utility lines: DFUT, UDUT, DFUP, UPAS, UDUP」

**它把 utility line 与 utility purpose 两条线合成了一个分组**：
`DFUT`/`UDUT` 是**线**那一对（见 [[udut]]），`DFUP`/**`UDUP`** 是**用途**那一对，
中间的 **`UPAS`（Utility Purpose ASsignment for multi-site）是第三个成员**——
**它不做定义也不做撤销，做的是「把 purpose 分配到多 site」**（这是从命令名读的，本页没读它）。

**所以本页的正命令是 [[dfup]]**（同一行上的 `DeFine Utility Purpose`）。

- [[dfup]] —— **正向命令：那页定义 utility purpose，本页撤掉。**
  **⚠️ 但这一条配对关系本页只能引索引**——
  **`UDUP` 自己的原文里 `DFUP` 0 命中**（实测），
  而且本篇的 `## Application` 也**没有**指向 `DFUP`。
  **「拿 `DFUP` 建、拿 `UDUP` 撤」是索引那条分组行的文档事实，
  不是本页原文的文档事实。** **本页没读 `DFUP` 的 raw。**
- [[upas]] —— **同一行上的第三个成员**（`Utility Purpose ASsignment for multi-site`）。
  **本篇原文里 `UPAS` 0 命中**。**本页没读它。**
  **⚠️ 它与本页的顺序关系本页不知道**——`upas` 那一页**在 allowlist 里**，
  而 [[referenced-set-requires-prior-definition]] 那一页提到过 `UPAS` 出现在
  `must have been defined with` 的扫描结果里。**那是那一页的观察，不是本页的结论。**
- [[udut]] —— **同族里最近的邻居，也是本页最该对照的一页**：
  两页的**语法形状、参数句型、例子的形式完全平行**（`UDUP {(purpose_name)}` 对
  `UDUT {(util_name)}`；`removes all utility purpose definitions` 对
  `removes all utility line definitions`；`UDUP (@)` 对 `UDUT (@)`）。
  **唯一的实质差别**：`UDUT` 的第一句多了一个副作用——
  `thereby setting the output state of write utility lines to 0 (low output)`，**本页没有这句。**
  **本篇原文里 `UDUT` 0 命中、[[udut]] 原文里 `UDUP` 也 0 命中**（两边都实测过）。
- [[utility-purpose-editor]] —— **GUI 侧的同族对象页**（allowlist 里有）。
  **`UDUP` 在本篇里 0 命中**；**本页没读它**。
  **注意**：`UDUP` 的入边里**没有来自 `utility-purpose-editor` 的**
  （实测入边 5 条：`Disabling_a_pin_configuration_license_lock` / `List_of_commands` /
  `Introduction` / `Pin_configuration_setup_commands` / `index`）。
  **所以这条关系是按对象域列的，不是文档事实。**
- [[udpr]] / [[udps]] / [[udpt]] / [[udvp]] —— **同一族的另外四页**，见上表。
- [[pin]] / [[command-reference]] —— **归属**：本篇在 `02.06_Command_Reference` 下，
  而 `## Application` 指向 `Configuration Setup Commands.`。
  **⚠️ 但注意本篇在语料里被放进了三个不同的章**（见「出处」⚠️ ⑤）——
  它在 `02.06.12_Utility_Line_Commands` 那一系列里**也有一份**，
  **而那一份的 `## Application` 指的仍然是 pin configuration 那一章**。
  （§6：`stage` 填的是**最近的一段**，不是归属。）
- [[pin-config-locked-during-test]] —— **适用于本命令的那条锁**（见「典型用法」）。
- [[referenced-set-requires-prior-definition]] —— **同形但不同族的约束页**（措辞不同，见「是什么」）。

### 一个本篇正文里完全没有、但别的文档明确点名的后果：DSL 授权锁

`02.04.05.08.02_Disabling_a_pin_configuration_license_lock.md`（**不在本篇 `sources:` 里，本页另读了它**）
把 `UDUP` 列进**能解除「pin configuration license lock」的命令**里，逐字（放在代码块里，
免得本页的引号把那个 `*` 吃成斜体）：

```
Several firmware commands can disable a device specific license lock, in other words, disable a pin configuration file. These firmware commands are *RST (ReSeT), UDAN (UnDefine ANalog pin), UDEF (UnDEFine pin), UDPS (Undefine DPS pin), UDUP (UnDefine Utility Purpose), and UDUT (UnDefine UTility line).
```

**即：跑一条 `UDUP`，会把 pin 配置文件的 device-specific license 签名作废。**
那一篇接着写（逐字）：

> 「The device-specific-license signature is no longer valid, the pin configuration file is
> unlocked, and the pin configuration related commands are enabled again.」

**⚠️ 本页的 `UDUP` 原文一个字都没提这件事。**
**这一条对本族里另外两页同样成立**：那份名单里还有 `UDPS` 与 `UDUT`
（见 [[udps]] / [[udut]]）。**`UDPR` / `UDPT` / `UDVP` 不在这份名单里**（本页核过）。

> **本页的 `（推断）` 只有一处**：语法里 `{}` 与 `()` 的分工。
> 其余每条都能指到本篇原句，或上面那两篇被声明的文档的原行。

## 版本

`## Functional changes` 段有，**只有一条，逐字**：

```
- Introduced before SmarTest 6.3.2
```

**按 §11.2 ②，这不是「6.3.2 的变更记录」，是一个哨兵值。**
全语料那 2,677 条同款写法（`Introduced before …`）的意思是
「**在本文档集覆盖范围开始之前就已经有了**」——
**照字面读会生成一条「6.3.2 新增了 `UDUP`」的假信息，而且格式齐整。**

**所以：`UDUP` 究竟成立于哪个版本，这份语料里没有。**
本页只能记「**至少早于 6.3.2 的覆盖起点**」，**不能记成「6.3.2 引入」。**

**与同族的对照**：[[udpr]] 拿到的是**真版本号**（`Introduced in SmarTest 6.5.2`），
[[udvp]] 拿到的也是真版本号（`Introduced in SmarTest 7.10.0`），
而**本页与 [[udps]] / [[udpt]] / [[udut]] 拿到的都是哨兵值**。
**这不是本页的缺陷，是各篇文档各自的写法。**

**与 wiki 面向版本的关系**：本 wiki 面向 **SmarTest 7.10.3**，
**而本篇的版本段一条变更都没有**——**所以「6.3.2 之后 `UDUP` 有没有变过」语料里答不了。**

## 出处

`sources:` 一篇：
`02_System_reference/02.06_Command_Reference/02.06.02.02.301_UDUP_-__UnDefine_Utility_Purpose.md`
（TDC `98830.htm`；**md 1,220 字节 / 46 行**，上游 htm 2,589 字节）。**整篇读完——本篇只有 46 行。**

**另外读了三篇 raw（本页 `sources:` 之外，逐条声明）：**

| 篇 | 为什么读 | 字节 / 行数 |
|---|---|---|
| `02.06.03_Pin_configuration_setup_commands.md`（TDC `10649.htm`） | **本篇 `## Application` 唯一指向的那一篇**；族的分组表与章首 Note 都在这里 | 3,305 B / 41 行 |
| `02.06.03.01.01_Introduction.md`（TDC `10650.htm`） | **同一张分组表在它里面也有一份**（用于判断那是「重复投放」还是「各写一遍」，§10 的判据） | 3,061 B / 37 行 |
| `02.04_Model_File_and_Licensing/02.04.05.08.02_Disabling_a_pin_configuration_license_lock.md`（TDC `114540.htm`） | **它是 `UDUP` 的一条入边**，而且给出一条本篇完全没写的后果（DSL 授权锁） | 3,831 B / 41 行 |

**还读了四篇 wiki 页（不是 raw）**：`wiki/objects/udef.md`、`wiki/objects/dfpr.md`
（对齐同族写法）、`wiki/constraints/pin-config-locked-during-test.md`、
`wiki/constraints/pin-config-requires-sequencer-off.md`（核对「哪条锁适用于本命令」）。

**本页没做的**：

- **`DFUP` 的 raw 没读**——**本页连 `DFUP` 长什么样都不知道**，
  只知道索引那一行把 `DFUP` 与 `UDUP` 并列。**所以「utility purpose 怎么定义」本页一个字没有。**
- **`UPAS` 没读**——同一行上的第三个成员，**它与本页的顺序关系本页不知道**。
- **「utility purpose 到底是什么」本页答不了**：本篇把它推给
  `Configuration Setup Commands`，而**本页读了那一篇，它只给分组表**——
  **它也不定义 utility purpose**。**所以这一问在本页读过的文档里没有答案。**
- **`UPST - (Utility Purpose STate)` / `UPTI - (Utility Purpose settling TIme)` 之类的兄弟命令没读**——
  它们存在于语料里（本页按文件名扫到过），**但本页没有读它们的正文**，
  **所以「怎么查一个 utility purpose 的状态」本页答案为空。**
- **`utility-purpose-editor` 没读**——见「和谁有关」里那条（它对本页没有入边）。
- **`Pin Configuration Example` 没读**——索引末尾指向它。
- **图：本篇没有内嵌图片。** 判据可核：本篇 md 里 `.png` / `.jpg` / `![` **0 命中**。
  **所以本页没有任何来自图的结论**（§11.4）。
- **没有实跑。** 没在机台上发过 `UDUP`、没撤过 utility purpose、没触发过那条 Error。
  `verified: doc-only` 说的就是这件事（§11：文档里有 ≠ 这台机器上能用）。
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
>  | purpose_name |
>
> Specifies the utility purpose name or names to be undefined.
>
> The symbol @ removes all utility purpose definitions.
>
> If more than one name is to be removed, the names must be separated by a comma.
>
>  |
> ```
>
> ——**参数名和说明各占一行、中间夹着孤立的 ` | `**。
> **⚠️ 注意它和同族的 [[udpr]] / [[udps]] / [[udpt]] 形态不同**：
> 那三篇的参数名是**单独一行**（`|` / 名字 / ` |`），
> 而本篇（和 [[udut]]）把 ` | purpose_name |` **挤在同一行**。
> **同一批文档、同一个版式，两种压平结果。**
> **说明文字一个字没丢**，但**本篇 raw 里没有 `Parameter` / `Description` 之类的表头行**——
> **所以「哪一列是什么」是从位置读出来的，不是原文写的。**
> **⚠️ 上游 `.htm` 里这张表是完整的**：`raw/98830.htm` 里写着
> `<table class="frame-topbot">`，里面是 `<colgroup><col><col></colgroup>`，
> `<tr>` 里两个 `<td>`。
> **所以「压平」是转换侧的产物，不是上游就坏的**（§11.2 ⑥ 的判法：回 `.htm` 核）。
>
> **② 本篇的 `## Errors` 只有一句，而它用了 `referenced` 这个词。** 逐字：
> `An error is generated if the referenced utility purpose has not been defined before.`
> ——**`referenced` 指的是「参数里写的那个名字」还是「别处引用了它」，
> 原文没说清**。**本页照原样引，不替它选一个解释。**
> **注意它与 [[udpr]] 的报错句不是一回事**：那一篇是
> `An error is generated if the package pin name has not been defined.`
> （无 `before`、主语是 `the package pin name`）；**本篇是 `has not been defined before`。
> 两篇句型相似、用词不同。**
>
> **③ 第一句说「一个或多个」，而参数表说「名字或名字们」。** 逐字：
> `removes one or more defined utility purpose names from the configuration`（**复数 `names`**）
> 对 `Specifies the utility purpose name or names to be undefined.`（**`name or names`**）
> ——**两处不完全同构**。**本页并列，不替它统一。**
>
> **④ 同一个说法在本族里介词不一致。** 本篇逐字是
> `the names must be separated by a comma.`，
> 而 [[udps]] / [[udpt]] 逐字是 `the names must be separated with a comma.`
> ——**同一个句型，一个 `by` 一个 `with`**。本页照原样引，不替它统一。
>
> **⑤ 本篇在语料里有**三份**投放，正文逐行完全相同。** 另两份是
> `02.06_Command_Reference/02.06.03.02.27_UDUP_-__UnDefine_Utility_Purpose.md`
> （`source_topic: "98830_2.htm"`，1,223 字节）与
> `02.06_Command_Reference/02.06.12.02.03_UDUP_-__UnDefine_Utility_Purpose.md`
> （`source_topic: "98830_3.htm"`，1,223 字节）。
> **实测 `diff`：三份的差别只有 frontmatter 的第 3、4 行**（`source_topic` / `source_html`），
> 那 1 字节的差就是 `98830` → `98830_2` / `98830_3`。
> **三份上游 `.htm` 也都在，而且 `cmp` 报三个文件完全一致**（都是 2,589 字节）——
> **所以这是上游 TDC 就有的重复投放，不是转换产生的**（§11.2 ⑥ 的判法）。
> **⚠️ 三份分属三个不同的章**：`02.06.02.02_List_of_commands`（本页 `sources:` 用的）、
> `02.06.03.02_List_of_configuration_commands`、`02.06.12.02_List_of_utility_line_commands`。
> **而三份的 `## Application` 都指向同一个 `Configuration Setup Commands`**——
> **这里有一个结构上的事实要记：本命令在 utility line 那一章里也有一份投放，
> 而那一份的 `## Application` 指的仍是 pin configuration 那一章。**
> 这是语料的结构，不是谁引错了。
> **本页的 `sources:` 用的是 `02.06.02.02.301` 那一份**；
> **另两份的内容本页没有另读一遍**（因为实测正文逐行相同）。

`verified: doc-only`
