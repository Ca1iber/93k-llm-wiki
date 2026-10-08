---
type: object
title: UDPR - (UnDefine Pin Role)
layer: L1
stage: pin
tags: [udpr, l1, firmware-command, pin, pin-alias, alias-set, undefine]
related: [dfpr, alias-set-editor, udef, udps, udpt, udup, udut, udvp, pin, command-reference, referenced-set-requires-prior-definition, smartest-6.5.2]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.297_UDPR_-__UnDefine_Pin_Role.md
created: 2026-09-24
updated: 2026-09-28
verified: doc-only
---

# UDPR - (UnDefine Pin Role)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **712 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.297_UDPR_-__UnDefine_Pin_Role.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
UDPR "alias_set_name"|@,"pin_alias",(package_pin_name|@)
```

### Parameters

| alias_set_name | The alias set name.<br><br>The alias of the pin (specified by the pin name parameter) defined in this alias set is deleted.<br><br>The symbol @ can be used to list all the required alias set names. |
|---|---|
| pin_alias | The pin alias. |
| package_pin_name | The package pin name.<br><br>The symbol @ can be used to list all the required package pin names. |

### Example

```
UDPR "@","",(@)
```

This example deletes all the alias sets.

```
UDPR "FUNC","",(@)
```

This example deletes the alias set FUNC.

```
UDPR "FUNC","CLK",(CP)
```

This example deletes the pair of package pin name CP and the pin alias CLK from the alias set FUNC.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.297_UDPR_-__UnDefine_Pin_Role.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if the package pin name has not been defined.

<!-- 报错节 end -->

## 是什么

**`UDPR`（UnDefine Pin Role）是 pin alias 那一族的撤销面**——删掉 `DFPR` 建起来的别名定义。
原文一句话就是全部机制：

> 「The UDPR command deletes the pin alias definitions.」

| 要素 | 值 |
|---|---|
| **动作** | `deletes`——**删，不是改** |
| **对象** | `the pin alias definitions`——**是「别名定义」，不是 pin 本身** |
| **作用域** | **本篇未写**（对照 [[udef]]，那一篇明写 `the current configuration`） |
| **产物** | **本篇未写有什么产物**——没有一个返回示例、没有一条状态查询 |

**本篇只有这一句散文 + 一张参数表 + 三个例子。**
所以「它到底动了什么、动了之后还剩什么」**只能从三个例子里读出来**——见下。

### 一条「别名定义」= 一个三元组，三个位置各自能全选

[[dfpr]] 那一页已经把 `DFPR` 建的映射表讲清了：一条定义是
**`alias_set_name` + `pin_alias` + `package_pin_name`** 的三元组，而集合本身有名字。
`UDPR` 的三个参数**就是这三个位置**，语法逐字（见上面「语法 / 参数」节）：

```
UDPR "alias_set_name"|@,"pin_alias",(package_pin_name|@)
```

| 位置 | 参数 | 语法里给的形态 | 参数表的说明（逐字） |
|---|---|---|---|
| 1 | `alias_set_name` | 名字 **或 `@`** | `The alias set name.` |
| 2 | `pin_alias` | **只有名字**（语法里**没有** `@` 这一段） | `The pin alias.` |
| 3 | `package_pin_name` | 名字 **或 `@`** | `The package pin name.` |

**光看参数表看不出「怎么删掉一整个集合」**——因为 `pin_alias` 那一格没有 `@` 可写。
答案在例子里：**写空串 `""`。**

### 三个例子 = 三种粒度，差别全在「哪个位置是空的」

**原文的 `## Example` 是按粒度递进给的**，这是本页最实用的一张表：

| # | 命令（逐字） | 删掉的是 | 原文说明（逐字） |
|---|---|---|---|
| 1 | `UDPR "@","",(@)` | **全部 alias set** | `This example deletes all the alias sets.` |
| 2 | `UDPR "FUNC","",(@)` | **一个 alias set**（`FUNC` 整个） | `This example deletes the alias set FUNC.` |
| 3 | `UDPR "FUNC","CLK",(CP)` | **一条三元组**（`FUNC` 里的 `CLK`→`CP`） | `This example deletes the pair of package pin name CP and the pin alias CLK from the alias set FUNC.` |

**读法（推断，依据就是这三个例子本身）**：

> **`pin_alias` 位置写空串 `""`，语义是「这个集合里所有 pin 的别名」。**
> 关键证据是例 2：它 `package_pin_name` 位置写的是 `(@)`（全部），
> 而原文说结果是 `deletes the alias set FUNC.`——**是整个集合没了，不是「集合里每一对被删了一遍」。**
> **本篇没有一句话解释 `""` 的语义**（参数表里 `pin_alias` 那格只有 `The pin alias.` 一句），
> **所以这是从例 1 / 例 2 一致的写法里读出来的**，标推断。

**⚠️ 三个位置里只有位置 2 没有 `@`**，这个不对称是本页最容易踩的地方：
**`UDPR "@",(@)` 这种写法语法里不存在**，要全删就照例 1 写。
**「`""` 能不能写成 `@`」——原文没说，本页不替它发明。**

### ⚠️ 参数表里那两句 `list`，是从 `DFPR` 的查询页搬过来的

位置 1 和位置 3 的说明各带一句 `@` 的用法，逐字两处：

> 「The symbol @ can be used to list all the required alias set names.」

> 「The symbol @ can be used to list all the required package pin names.」

**两句都用了 `list`（列举）。可 `UDPR` 是一条删除命令，它没有任何返回。**
对照 [[dfpr]] 那一页引的同一格原句（**本页回 `02.06.02.02.64` 那一份 raw 核过这一句**）：
`In the query, you can define multiple alias sets or use the symbol @ to list all the defined pin alias sets.`
——**`DFPR` 那句带 `In the query` 前缀，`list` 放在查询里是通的；
`UDPR` 这句把前缀去掉了，`list` 就悬空了。**
**本页照原样引，不替它把 `list` 改成 `delete`**（§11.2：raw 一个字节不动）。
**实际语义按三个例子读：`@` 在这里就是「全部」，不是「列出来」**（推断）。

### 三个例子共用一条前提，而那条前提本篇没写

例 2 和例 3 点名了 `FUNC` / `CLK` / `CP`，**读起来像 [[dfpr]] 那样先给过一张「现有 alias set」表**——
**但 `UDPR` 这篇没有那张表**：它的 `## Example` 第一个例子直接就是 `UDPR "@","",(@)`，
**前面没有任何「先交代有哪几个 pin」的句子**
（对照 [[dfpr]] 的 `## Examples`，那一页明写
`The pin configuration file includes three pins: CP, S0, and S1.`——
**本页也回 `02.06.02.02.64` 那一份 raw 核过这一句**，
raw 里三个 pin 名是带反引号的，本页按 §11.1 ③ 去掉）。

**所以本篇的 `FUNC` / `CLK` / `CP` 是从哪里来的，本篇没说。**
（**推断**：与 [[dfpr]] 的 Example 1/2/4/5 用的是同一组名字，那一篇里它们定义在
`FUNC` / `TRANS` 两个集合里。**但这是跨篇对照，不是本篇的文档事实**，本页只当推断用。）

## 典型用法

**本篇没有 `## Procedure` / `## Before you begin` / `## What to do next`**——
用法只有 `## Example` 那三条 + `## Parameters` 那张表。**按目的查**：

| 要做的 | 发什么 | 依据 |
|---|---|---|
| **删一个集合里的某一对别名** | `UDPR "FUNC","CLK",(CP)` | Example 3 逐字 |
| **删掉一整个集合** | `UDPR "FUNC","",(@)`——**中间写空串** | Example 2 逐字 + 它的说明句 |
| **删掉全部集合** | `UDPR "@","",(@)` | Example 1 逐字 |
| 删掉一个集合里所有别名、**但保留集合本身** | **本篇没有这个写法** | — |
| 先看有哪些集合 / 别名可以删 | **本篇没有查询语法** | — |

**顺序上的前提：本篇一个字没写。** 它没有 `## Predependencies` 段、没有 `## Before you begin`——
「删之前要先有什么」只有 `## Errors` 那一句沾到（**它说的是「pin 名得先定义过」**，见下）。

**一条家族级的锁**：[[pin-config-locked-during-test]]。
`UDPR` 所属的那一章（`Pin configuration setup commands`）**章首**写着
`The firmware does not accept any configuration changes while a test is running.`
**这一句不在本篇正文里**（见「出处」），但 `UDPR` 的定义位置就在那一章的分组表上，
**所以它适用于本命令**。**这一条说的是「测试在跑时不许改配置」，
不是「sequencer 非 OFF 不许改」**——后者是 [[pin-config-requires-sequencer-off]] 那条，
**它点名的四个命令（`DFPN` / `UDEF` / `CONF` / `PALS`）里没有 `UDPR`**（本页核过）。

**出错时**：本篇 `## Errors` **只有一条**（逐字见上面「报错条件」节，脚本取自本篇），
**而且它和 [[dfpr]] 的 `## Errors` 逐字相同**：

> 「An error is generated if the package pin name has not been defined.」

**两份 raw 的 `## Errors` 段实测逐字节相等**（判据见「出处」⚠️ ③）——这不是本页的引用错误，
**是上游就写了同一句**。**注意它点的是 `the package pin name`，不是 `alias_set_name`、也不是 `pin_alias`**：

| 情况 | 会不会报错 |
|---|---|
| `package_pin_name` 没定义过 | **报错**（这一条就是） |
| `alias_set_name` 不存在 | **本篇未写** |
| `pin_alias` 不存在 | **本篇未写** |

**后两行是「本篇没写」，不是「不报错」**（§2.1：没找到 ≠ 文档没有）。
**本篇也没有 `## Warnings` 段**（已核，0 命中）——**所以「还有什么别的错法」本篇答不了。**

## 和谁有关

### 这一族的结构：`UDxx` 是 `DFxx` 的撤销面

**这六个页面（[[udpr]] / [[udps]] / [[udpt]] / [[udup]] / [[udut]] / [[udvp]]）是同一族命令的撤销侧。**
族的划分**不是本页猜的**：`02.06.03_Pin_configuration_setup_commands.md` 逐条给了分组，
逐字（已剥链接标记）：

| 分组（逐字） | 命令 |
|---|---|
| `Commands for pin alias:` | `DFPR`, **`UDPR`** |
| `Commands for DPS pins:` | `DFPS`, `UDPS` |
| `Commands for pin groups and ports:` | `DFGP`, `UDGP`, `DFPT`, `UDPT` |
| `Commands for utility lines:` | `DFUT`, `UDUT`, `DFUP`, `UPAS`, `UDUP` |
| `Commands for digital pins:` / `Commands for DC Scale pins:` | `DFPN`, `UDEF`, `DFPS`, `UDPS`, `PSSL`（还有 `UDEF`、`PSSL` 等） |
| — | `UDVP` **不在这个索引里**（实测 0 命中） |

**所以本页的正命令是 [[dfpr]]，两页在索引里同处一行**，逐字：

> 「Commands for pin alias: DFPR, UDPR」

- [[dfpr]] —— **反向命令：那页建、本页删。** `DFPR` 建集合与三元组、`UDPR` 删它们；
  **两页的 `## Errors` 逐字相同**（见「典型用法」）。
  **⚠️ 本页没读 `DFPR` 的 raw**——凡提到 `DFPR` 的地方，依据都是 [[dfpr]] 那一页本身。
- [[alias-set-editor]] —— **GUI 侧的同族对象页**。`UDPR` 有入边来自
  `02.08.04.18.01.04_Alias_set.md`，**本页没读它**。
- [[udef]] —— **同族另一支的撤销命令**（`UnDEFine pin`）。
  **`UDEF` 在本篇原文里 0 命中、`UDPR` 在那一篇里也 0 命中**（两边都实测过）——
  **两者的并列只出现在 `02.06.02.02_List_of_commands.md` 的字母序相邻行上**，逐字相邻（剥标记后）：
  `UDEF` → `UDGP` → **`UDPR`** → `UDPS` → `UDPT` → `UDRS` → `UDUP` → `UDUT`。
  **注意这份字母表里还有一个 `UDRS - (UnDefine Routing Set)`，它不在上面那张分组表里。**
- [[udps]] / [[udpt]] / [[udup]] / [[udut]] / [[udvp]] —— **同一族的另外五页**，见上表。
- [[pin]] / [[command-reference]] —— **归属**：本篇在 `02.06_Command_Reference` 下，
  而 `## Application` 指向 `Configuration setup. See Configuration Setup Commands.`（配置类命令章）。
  （§6：`stage` 填的是**最近的一段**，不是归属。）
- [[referenced-set-requires-prior-definition]] —— **同形但不同族的约束页**。
  那一页收的是 spec value set / search set / jitter set 等**「引用型集合」**的先定义后引用，
  **措辞是 `does not exist` / `exists`**；而本篇的报错句是 `has not been defined`。
  **形状像、用词不同，本页不把两者合并**（那一页自己也只声称覆盖 4 个集合族）。

> **本页只有上面标出的两处 `（推断）`**（`""` 的语义、`@` 的实际语义）。
> 其余每条都能指到本篇的原句、原表，或上面那两篇索引的原行。

## 版本

`## Functional changes` 段有，**只有一条，逐字**：

```
- Introduced in SmarTest 6.5.2
```

**这一条不是哨兵值**：措辞是 `Introduced in`（**不是 `before`**），
所以按字面读就是「**6.5.2 引入**」——与 §11.2 ② 那种 `Introduced before SmarTest 6.3.2` 的写法**不是一回事**
（对照同族的 [[udps]] / [[udpt]] / [[udup]] / [[udut]]：**那四页拿到的都是哨兵值**）。

**另有一条独立印证**：`02.06.03_Pin_configuration_setup_commands.md` 的 `## Functional changes` 里逐字写着

```
- SmarTest 6.5.2: New command: UDPR
```

**两份文档各自说 6.5.2，方向一致**（一处是本命令的引入版本，一处是索引的变更记录）。
**同一个索引里紧邻的一行是 `- SmarTest 6.5.2: New command: DFPR`**——
**即 `DFPR` 与 `UDPR` 是同一次发布成对进来的**。
（**这是那篇索引的文档事实**，**不是本页对 `DFPR` raw 的引用**。）

**与 wiki 面向版本的关系**：本 wiki 面向 **SmarTest 7.10.3**（[[smartest-7.10.3]]），
**而本篇的版本段只有 6.5.2 这一条**——**所以「6.5.2 之后 `UDPR` 有没有变过」语料里答不了。**

## 出处

`sources:` 一篇：
`02_System_reference/02.06_Command_Reference/02.06.02.02.297_UDPR_-__UnDefine_Pin_Role.md`
（TDC `112438.htm`；**md 1,324 字节 / 82 行**，上游 htm 3,423 字节）。**整篇读完——本篇只有 82 行。**

**另读了两篇 raw 全文 + 一篇 raw 的三处片段（本页 `sources:` 之外，逐条声明）：**

| 篇 | 为什么读 | 字节 / 行数 |
|---|---|---|
| `02_System_reference/02.06_Command_Reference/02.06.03_Pin_configuration_setup_commands.md`（TDC `10649.htm`） | **本篇 `## Application` 唯一指向的那一篇**；族的分组表就在这里 | 3,305 B / 41 行 |
| `02_System_reference/02.06_Command_Reference/02.06.03.01.01_Introduction.md`（TDC `10650.htm`） | **同一张分组表在它里面也有一份**——用于判断那是「重复投放」还是「各写一遍」（§10 的判据） | 3,061 B / 37 行 |
| `02.06_Command_Reference/02.06.02.02.64_DFPR__DFPR__-__DeFine_Pin_Role.md`（TDC `112436.htm`）**——只核了三处，没有整篇读** | 本页引它的三处：`## Errors` 段逐字节比对、`In the query,` 开头那句、`The pin configuration file includes three pins:` 开头那句 | **3,517 B / 251 行（本页未通读）** |

**还读了四篇 wiki 页（不是 raw）**：`wiki/objects/dfpr.md`、`wiki/objects/udef.md`
（对齐同族写法）、`wiki/constraints/pin-config-locked-during-test.md`、
`wiki/constraints/pin-config-requires-sequencer-off.md`（核对「哪条锁适用于本命令」）。

**本页没做的**：

- **`DFPR` 的 raw 没有通读。** 整篇只有上面表里那三处核过：
  `## Errors` 段的逐字节比对、`In the query,` 开头那一句、`The pin configuration file includes three pins:` 开头那一句；
  **其余 `DFPR` 细节（Example 1/2/4/5 的输出行、`DEF`/`ALL` 的说明）依据都是 [[dfpr]] 那一页，未经本页原文复核。**
- **`Alias_set.md`（`02.08.04.18.01.04`）没读**——那条入边里 `DFPR` 与 `UDPR` 两个链接首尾相接。
  **所以「GUI 上 alias set 长什么样、界面里怎么删」本页没有。**
- **`Configuration Setup Commands` 那一章的其余命令页没读**——
  本页只知道分组表上 `UDPR` 和 `DFPR` 同一行，以及章首那句 Note。
- **`Pin Configuration Example` 没读**——索引末尾指向它
  （索引原句：`An example of a pin configuration file is given in Pin Configuration Example.`，
  其中 `Pin Configuration Example` 在 raw 里是链接，本页按 §11.1 ② 剥掉标记）。
  **所以「alias set 在配置文件里长什么样」本页没有。**
- **图：本篇没有内嵌图片。** 判据可核：本篇 md 里 `.png` / `.jpg` / `![` **0 命中**。
  **所以本页没有任何来自图的结论**（§11.4）。
- **没有实跑。** 没在机台上发过 `UDPR`、没删过 alias set、没触发过那条 Error。
  `verified: doc-only` 说的就是这件事（§11：文档里有 ≠ 这台机器上能用）。
- **没有动 `wiki/index.md`**。

> ⚠️ **本篇的语料瑕疵与结构上要注意的地方，本页照实记下、一处都没替它改**（§11.2）。
> **本篇 md 的 CJK 字符数实测为 0**——**没有 §11.2 ① 那一族编码乱码。**
>
> **① `## Parameters` 那张表在 raw 里被压平，而且缺表头。** 三格（`alias_set_name` /
> `pin_alias` / `package_pin_name`）的说明都散成「一格一行 + 游离 ` | `」，
> **每两格之间还夹着两个 ` | `**。逐字（本篇 `## Parameters` 起头那一段的原文）：
>
> ```
> ## Parameters
>
> |
>
> alias_set_name
>
>  |
> ```
>
> ——**第一行那个 `|` 后面没有空格，后面的都是 ` | `**（同一张表里两种写法，本页照原样记）。
> **说明文字一个字没丢**，但**本篇 raw 里没有 `Parameter` / `Description` 之类的表头行**——
> **所以「哪一列是什么」是从位置读出来的，不是原文写的**。
>
> **⚠️ 上游 `.htm` 里这张表是完整的**：`raw/112438.htm` 里写着
> `<table class="frame-topbot">`，里面是 `<colgroup><col><col></colgroup>`，
> **三个 `<tr>`、每行两个 `<td>`**。
> **所以「压平」是转换侧的产物，不是上游就坏的**（§11.2 ⑥ 的判法：回 `.htm` 核）——
> **这条结论与下一条不同，别混。**
>
> **② 参数表里那两句 `list` 与命令的动作不符。** 逐字两处：
> `The symbol @ can be used to list all the required alias set names.` /
> `The symbol @ can be used to list all the required package pin names.`
> ——**删除命令却写 `list`**（上面已对照过 [[dfpr]] 的同一格，那一篇带 `In the query` 前缀）。
> **本页照原样引，不替它改词。**
>
> **③ `## Errors` 段与 `DFPR` 的 `## Errors` 逐字相同。** 两边都是
> `An error is generated if the package pin name has not been defined.`
> ——**实测两份 raw 从 `## Errors` 到下一个 `## ` 之间的文本逐字节相等**。
> **这是上游就有的重复，不是本页引错，也不是转换产生的。**
>
> **④ 参数表里有一处指代不明。** 逐字：
> `The alias of the pin (specified by the pin name parameter) defined in this alias set is deleted.`
> ——**`the pin name parameter`** 指哪一格？本篇的参数表里**没有叫 `pin name` 的参数**，
> 只有 `pin_alias` 和 `package_pin_name`。**本页不替它指定**（§11.2：不许替语料改，
> 也不许假装没看见）。**另注意这句说的是「做什么」（删），不是「`alias_set_name` 是什么」**，
> 而它和 `The alias set name.` 挤在同一格里（上游那个 `<td>` 里本来就是两个 `<p>`）。
>
> **⑤ `## Example` 的三个例子前面没有交代前提。** 例 2 / 例 3 用了 `FUNC` / `CLK` / `CP`
> 三个名字，**本篇却没有像 [[dfpr]] 那样先写一句「配置文件里有哪几个 pin」**。
> **这三个名字的来处本篇未写。**
>
> **⑥ 本篇在语料里只有一份投放。** 实测：`by-category` 下文件名含 `_UDPR_` 的 `.md`
> **只有 `02.06.02.02.297` 这一份**（对照：`UDPS` / `UDUP` / `UDUT` 各两份以上）。
> 判据是**文件名扫描**，不是全文比对。**所以本页没有「两份投放在哪几行不一致」的问题。**

`verified: doc-only`
