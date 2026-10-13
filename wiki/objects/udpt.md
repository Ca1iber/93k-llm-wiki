---
type: object
title: UDPT - (UnDefine PorT)
layer: L1
stage: pin
tags: [udpt, l1, firmware-command, pin, port, undefine]
related: [dfpt, dfgp, udgp, port-editor, udpr, udps, udup, udut, udvp, pin, command-reference, pin-config-locked-during-test]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.299_UDPT_-__UnDefine_PorT.md
created: 2026-09-24
updated: 2026-09-28
verified: doc-only
---

> ⚠️ **本页若干处记的是 2026-10-10【之前】的语料形态。**
> 那一轮把语料里的表格一律换成了**指向上游 HTML 的指针**
> （见 `extract/PLAN-表格指针化.md`）。所以下文凡是说「表格被压平 / 被摊平 /
> 一格一行」的地方，指的是**更换之前**的样子 —— 现在语料里那个位置是**一句指针**，
> 真表仍在 `tdc-html/raw/` 的上游 HTML 里。**页码/引文都不受影响。**

# UDPT - (UnDefine PorT)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **374 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.299_UDPT_-__UnDefine_PorT.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
UDPT {(portlist)}
```

### Parameters

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98824.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：portlist | List of port names or the symbol @@, which undefines all ports. If more than one port is to be removed, the names must be separated with a comma.

### Example

```
UDPT (port_1)
```

This command undefines port port_1.

<!-- 语法节 end -->

## 是什么

**`UDPT`（UnDefine PorT）把一个已经定义过的 port 从当前配置里撤掉。**
原文一句话说完：

> 「The UDPT (UnDefine PorT) command removes a previously defined port from the current
> configuration.」

| 要素 | 值 |
|---|---|
| **动作** | `removes`——**撤，不是改** |
| **对象** | `a previously defined port`——**只对「已经定义过」的 port 有意义** |
| **作用域** | `the current configuration`——**动的是配置** |
| **产物** | **本篇未写有什么产物**——没有返回示例、没有状态查询 |

**⚠️ 本篇只有这一句散文 + 一张参数表 + 一个例子。** 所以下面很多格子只能写「语料未写」。

### 参数只有 `portlist`，**而它的说明里有一个坏掉的符号**

逐字（见上面「语法 / 参数」节）：

> 「List of port names or the symbol @@, which undefines all ports.
> If more than one port is to be removed, the names must be separated with a comma.」

| 你写什么 | 效果 |
|---|---|
| **一个 port 名** | 撤掉那一个（例子里就是 `port_1`） |
| **多个 port 名**（**必须逗号分隔**） | 撤掉那几个 |
| **`@`（按本族的通例）** | `which undefines all ports`——撤掉全部 port |
| **`@@`（原文逐字如此）** | ——**「两个 `@` 更有效」吗？文档没说。** |

> **⚠️ 这里必须分开写清楚，因为原文的符号是坏的：**
> 本篇参数说明里逐字写的是 **`the symbol @@`（两个 `@`）**，
> 而**同族的 [[udps]] / [[udef]] 写的是 `the symbol @`（一个）**。
> **⚠️ 已回上游 `raw/98824.htm` 核过**：那里就是 `<strong>@@</strong>`——
> **是 TDC 上游就写坏的，不是 HTML→md 转换产生的**（§11.2 ⑥ 的判法）。
> **本页照原样引，不替它改成 `@`**（§11.2：raw 一个字节不动）。
> **实际该敲一个 `@` 还是两个，本篇答不了**——本页不推测。

**语法的括号 `{}` 与 `()`**：语法行逐字是 `UDPT {(portlist)}`，例子逐字是 `UDPT (port_1)`——
**圆括号是要照写的字面字符，花括号是占位框**（读法与 [[udef]] 一致：
**本篇的例子、正文里花括号一次都没出现过**）。
**原文没有解释这两种括号的分工**，**所以这一步是推断，不是文档事实。**

### 例子只有一条，只说「撤掉了」，没说「撤掉之后剩什么」

> 「This command undefines port port_1.」

**一句话，没有第二句。** 对照同族：[[udps]] 的例子担保 level 数据会留住、
[[udpr]] 的三个例子把三种粒度都示范了一遍，而**本页的例子什么额外信息都不给**。
**所以「port 撤掉之后，它原来的成员 pin 怎么算」——语料未写**（**这是本页最缺的一块**）。

| 想知道的事 | 本篇答得了吗 |
|---|---|
| 怎么撤掉一个 port | ✅ `UDPT (port_1)` |
| 撤掉之后 port 里的成员 pin 会怎样 | ❌ **语料未写** |
| port 与 pin group 的关系（`portlist` 里的名字从哪来） | ❌ **语料未写** |
| 撤一个没定义过的 port 会怎样 | ❌ **本篇没有 `## Errors` 段**（见下） |

## 典型用法

**本篇没有 `## Procedure` / `## Before you begin` / `## What to do next`**——
用法只有 `## Example` 一条 + `## Parameters` 那张表。**按目的查**：

| 要做的 | 发什么 | 依据 |
|---|---|---|
| **撤掉一个 port** | `UDPT (port_1)` | `## Example` 逐字 |
| 撤掉多个 port | `UDPT (p1,p2)`——**逗号分隔** | `If more than one port is to be removed, the names must be separated with a comma.`——**原文没有给多 port 的完整例子** |
| **撤掉全部 port** | `UDPT (@)`——**按本族通例；原文这里印的是 `@@`**（见上） | `which undefines all ports`——**原文没有给命令行例子**（把两个事实合起来写是本页的整理，**不是原文的一条示例**） |
| 先看有哪些 port 可以撤 | **本篇没有查询语法** | — |
| 定义回来 | **本篇没有这个语法**——见「和谁有关」的 [[dfpt]] | — |

**顺序上的前提：本篇一个字没写。** 它没有 `## Predependencies` 段、没有 `## Before you begin`——
唯一沾到前提的是第一句里的 `a previously defined port`
（**即：撤的对象得先定义过**），**但「谁定义的」本篇没指向任何命令**。

**一条家族级的锁**：[[pin-config-locked-during-test]]。
`UDPT` 所属那一章（`Pin configuration setup commands`）的**章首**写着
`The firmware does not accept any configuration changes while a test is running.`
**这一句不在本篇正文里**（见「出处」）。
**注意别套错另一条**：[[pin-config-requires-sequencer-off]] 那条（「sequencer 非 OFF 不许改」）
**点名的命令是 `DFPN` / `UDEF` / `CONF` / `PALS`，里面没有 `UDPT`**——
**因为本篇根本没有 `## Errors` 段**（见下）。

### 出错时：**本篇没有 `## Errors`，也没有 `## Warnings`**

已核：本篇 md 里 `## Errors` / `## Warnings` **各 0 命中**，上游 `raw/98824.htm` 里也没有这两节。
**所以「撤一个没定义过的 port 会怎样」本篇答不了**（**语料未写**，本页不推测）。

> **⚠️ 本族的报错覆盖是不均匀的**：[[udpr]] / [[udup]] / [[udut]] / [[udvp]] **都有 `## Errors`**，
> 而 `UDPT` 和 [[udps]] **都没有**。
> **所以「这页找不到报错句」不等于「违反这条命令不报错」**——只等于「这一篇没写」。

## 和谁有关

### 这一族的结构：`UDxx` 是 `DFxx` 的撤销面

**这六个页面（[[udpt]] / [[udpr]] / [[udps]] / [[udup]] / [[udut]] / [[udvp]]）是同一族命令的撤销侧。**
族的划分**不是本页猜的**：`02.06.03_Pin_configuration_setup_commands.md` 逐条给了分组，
逐字（已剥链接标记）：

| 分组（逐字） | 命令 |
|---|---|
| `Commands for pin groups and ports:` | `DFGP`, `UDGP`, **`DFPT`**, **`UDPT`** |
| `Commands for DPS pins:` | `DFPS`, `UDPS` |
| `Commands for pin alias:` | `DFPR`, `UDPR` |
| `Commands for utility lines:` | `DFUT`, `UDUT`, `DFUP`, `UPAS`, `UDUP` |
| — | `UDVP` **不在这个索引里**（实测 0 命中） |

**本页那一行有四个命令，是这张表里最长的一行**——逐字：

> 「Commands for pin groups and ports: DFGP, UDGP, DFPT, UDPT」

**它把两对拆开写**：`DFGP`/`UDGP` 是**组**那一对，`DFPT`/`UDPT` 是**端口**那一对。
**所以本页的正命令是 [[dfpt]]**（同一行上的另一个「PorT」）。

- [[dfpt]] —— **正向命令：那页定义 port，本页撤掉。**
  **⚠️ 但这一条配对关系本页只能引索引**——
  **`UDPT` 自己的原文里 `DFPT` 0 命中**（实测），**第一句也只说 `a previously defined port`，
  没有说是谁定义的**。所以「拿 `DFPT` 建、拿 `UDPT` 撤」**是索引那条分组行的文档事实，
  不是本页原文的文档事实**。**本页没读 `DFPT` 的 raw。**
- [[dfgp]] / [[udgp]] —— **同一行上的另一对（组）**。
  `DFGP` 建 pin group、`UDGP` 撤 pin group。**本页原文一个字没提它们**（0 命中）——
  这一条同样只来自索引那一行。**本页没读这两篇。**
- [[udpr]] / [[udps]] / [[udup]] / [[udut]] / [[udvp]] —— **同一族的另外五页**，见上表。
  **本页原文里这五个命令名全部 0 命中**（实测）——族的并列只出现在索引与
  `02.06.02.02_List_of_commands.md` 的字母序里。
- [[port-editor]] —— **GUI 侧的同族对象页**。**`UDPT` 在本篇里 0 命中**，
  而且 `UDPT` 在 `edges.jsonl` 里**没有任何一条入边来自 `port-editor`**
  （实测：入边只有 4 条，来自 `List_of_commands` / `Introduction` /
  `Pin_configuration_setup_commands` / `index`）。**所以这条关系是按对象域列的，不是文档事实。**
- [[pin]] / [[command-reference]] —— **归属**：本篇在 `02.06_Command_Reference` 下，
  而 `## Application` 指向 `Pin configuration, see Configuration Setup Commands.`。
  （§6：`stage` 填的是**最近的一段**，不是归属。）
- [[pin-config-locked-during-test]] —— **适用于本命令的那条锁**（见「典型用法」）。

### 它不在那份 DSL 授权锁的名单里

`02.04.05.08.02_Disabling_a_pin_configuration_license_lock.md` 列出了能作废
pin configuration license 签名的命令（`*RST` / `UDAN` / `UDEF` / `UDPS` / `UDUP` / `UDUT`），
**`UDPT` 不在这份名单里**（本页核过）。**即：撤 port 不会作废那个签名。**
（**这是「那一篇没列它」这个事实**，**不是「撤 port 一定不影响签名」这个结论**——
那一篇没有正面说过后者。）

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
**照字面读会生成一条「6.3.2 新增了 `UDPT`」的假信息，而且格式齐整。**

**所以：`UDPT` 究竟成立于哪个版本，这份语料里没有。**
本页只能记「**至少早于 6.3.2 的覆盖起点**」，**不能记成「6.3.2 引入」。**

**与同族的对照**：[[udpr]] 拿到的是**真版本号**（`Introduced in SmarTest 6.5.2`），
[[udvp]] 拿到的也是真版本号（`Introduced in SmarTest 7.10.0`），
而**本页与 [[udps]] / [[udup]] / [[udut]] 拿到的都是哨兵值**。
**这不是本页的缺陷，是各篇文档各自的写法。**

**与 wiki 面向版本的关系**：本 wiki 面向 **SmarTest 7.10.3**，
**而本篇的版本段一条变更都没有**——**所以「6.3.2 之后 `UDPT` 有没有变过」语料里答不了。**

## 出处

`sources:` 一篇：
`02_System_reference/02.06_Command_Reference/02.06.02.02.299_UDPT_-__UnDefine_PorT.md`
（TDC `98824.htm`；**md 1022 字节 / 42 行**，上游 htm 2,347 字节）。
**整篇读完——本篇只有 42 行，是本族六页里最短的一篇。**

**另外读了两篇 raw 全文 + 三篇 raw 的若干句（本页 `sources:` 之外，逐条声明）：**

| 篇 | 为什么读 | 字节 / 行数 |
|---|---|---|
| `02.06.03_Pin_configuration_setup_commands.md`（TDC `10649.htm`） | **本篇 `## Application` 唯一指向的那一篇**；族的分组表与章首 Note 都在这里 | 3,305 B / 41 行 |
| `02.06.03.01.01_Introduction.md`（TDC `10650.htm`） | **同一张分组表在它里面也有一份**（用于判断那是「重复投放」还是「各写一遍」，§10 的判据） | 3,061 B / 37 行 |

**还读了三篇 wiki 页（不是 raw）**：`wiki/objects/udef.md`（对照同族写法）、
`wiki/constraints/pin-config-locked-during-test.md`、
`wiki/constraints/pin-config-requires-sequencer-off.md`（核对「哪条锁适用于本命令」）。

**本页没做的**：

- **`DFPT` 的 raw 没读**——**本页连 `DFPT` 长什么样都不知道**，
  只知道索引那一行把 `DFPT` 与 `UDPT` 并列。
  **所以「port 怎么定义、`DFPT` 有哪些参数」本页一个字没有。**
- **`DFGP` / `UDGP` 没读**——同一行上另一对。
- **`port-editor` 没读**——见「和谁有关」里那条（它对本页没有入边，本页也不该声称关系）。
- **`Pin Configuration Example` 没读**——索引末尾指向它。
  **所以「port 在配置文件里长什么样」本页没有。**
- **图：本篇没有内嵌图片。** 判据可核：本篇 md 里 `.png` / `.jpg` / `![` **0 命中**。
  **所以本页没有任何来自图的结论**（§11.4）。
- **没有实跑。** 没在机台上发过 `UDPT`、没撤过 port、**也没试过 `@@` 到底是不是能用的写法**。
  `verified: doc-only` 说的就是这件事（§11：文档里有 ≠ 这台机器上能用）。
- **没有动 `wiki/index.md`**。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**（§11.2）。
> **本篇 md 的 CJK 字符数实测为 0**——**没有 §11.2 ① 那一族编码乱码。**
>
> **① ⚠️ `@@` —— 上游 `raw/98824.htm` 里就写着两个 `@`。** 逐字：
> `List of port names or the symbol @@, which undefines all ports.`
> ——**上游是 `<strong>@@</strong>`，转换一个字节没动它**。
> **所以这是「上游就坏的」（§11.2 ⑥），救不回来，只能照实记。**
> 对照同族的 [[udps]]（`the symbol @ which undefines all DPS pins`）与
> [[udef]]（`the symbol @ which removes all pins`）**都写一个 `@`**。
> **本页不判哪个对、也不替它改**，只在正文「是什么」里把这件事讲到。
>
> **② `## Parameters` 那张表在 raw 里被压平。** 逐字（本篇 `## Parameters` 起头那一段的原文）：
>
> ```
> ## Parameters
>
>  |
>
> portlist
>
>  |
> ```
>
> ——**一格一行、中间夹着孤立的 ` | `**（同族各页同一形态）。
> **说明文字一个字没丢**，但**本篇 raw 里没有 `Parameter` / `Description` 之类的表头行**——
> **所以「哪一列是什么」是从位置读出来的，不是原文写的。**
> **⚠️ 上游 `.htm` 里这张表是完整的**：`raw/98824.htm` 里写着
> `<table class="frame-topbot">`，里面是 `<colgroup><col><col></colgroup>`，
> `<tr>` 里两个 `<td>`。
> **所以「压平」是转换侧的产物，不是上游就坏的**（§11.2 ⑥ 的判法：回 `.htm` 核）——
> **这条与 ① 不是一回事，别混。**
>
> **③ 本篇原文没有 `## Errors`，也没有 `## Warnings`**（已核，本篇 md 与上游 htm 里各 0 命中）。
> **注意上面「报错条件」那一节在本页是不存在的**——**这不是脚本漏抽，是 raw 里没有这一节**
> （对照 [[udpr]] / [[udup]] / [[udut]] / [[udvp]]：那四页有）。
>
> **④ 例子的措辞与本族其它页不一致。** 本篇是 `This command undefines port port_1.`，
> 而 [[udps]] 用的是 `This example removes pin Vee from the setup.`、
> [[udpr]] 用的是 `This example deletes all the alias sets.`——
> **`This command` / `This example` 两种开头在同一族里混用。本页照原样引，不替它统一。**
>
> **⑤ `separated with a comma`（本篇）与 `separated by a comma`（[[udup]] / [[udut]]）
> 是同一个句型的两种介词。** 本页照原样引。
>
> **⑥ 本篇在语料里只有一份投放。** 实测：`by-category` 下文件名含 `_UDPT_` 的 `.md`
> **只有 `02.06.02.02.299` 这一份**。判据是**文件名扫描**，不是全文比对。
> **注意 `UDPR` 也只有一份，而 `UDPS` / `UDUP` / `UDUT` 各有多份**——
> **「`02.06.03.02.*` 那一系列配置命令页里没有 `UDPT`」**，
> 所以本页没有「两份投放在哪几行不一致」的问题。

`verified: doc-only`
