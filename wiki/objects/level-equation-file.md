---
type: object
title: Level equation file
layer: file
stage: level
tags: [level, protocol-level, use-protocol, prot-lev, level-segment, equation-set, device-level-file, smartest-7.1.0]
related: [level-file, equation-based-level-setup, level-setup-tool, spec-set, eqsp, protocol-editor, device-directory, level, smartest-7.1.0]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.11.01.05.01_Level_equation_file.md
created: 2026-09-21
updated: 2026-09-21
verified: doc-only
---

# Level equation file

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **942 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.11.01.05.01_Level_equation_file.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

USE_PROTOCOL "<protocolName:<levelSegmentName>" [<portList>]

Parameter
 |

Parameter

 |

Description/Range

 |
 |

protocolName

 |

The name of the protocol to use.

 |
 |

levelSegmentName

 |

Name of the level segment to be used.

Must be defined for the protocol specified by protocolName.

 |
 |

portList

 |

(optional) List of protocol ports.

If omitted, all ports assigned to the protocol specified by protocolName. will be used.

 |

### Example

The following except shows how to use the USE_PROTOCOL statement within a device level setup file.

```
hp93000,level,0.1
 ...
EQSP LEV,EQN,#9000005436
EQNSET 1 "levels equation set"

SPECS    # starts the declaration of the specs
v_il_ctl [V]
 ...
EQUATIONS
# put here depend specs, resources in [V] and [mA]
 ...

LEVELSET 1 "normal"
#USE_PROTOCOL "<protocolName>:<levelSegmentName>" <portList>
USE_PROTOCOL "MDIO:DefaultPowerLevels" PoMDIO

PINS std_ins reset_b wse_gen
vil= v_il_ctl

 ...
```

<!-- 语法节 end -->

## 是什么

**这一页讲两样东西，只有两样：`USE_PROTOCOL` 语句，和它引进来的那个 `.prot_lev` 文件。**
**它不讲 equation set 文件的一般格式**——那是 [[level-file]] 的题目，本页在
`## 和谁有关` 里显式指过去。

**它为什么存在**，原文第一句（逐字）：

> 「The device level file handling has been enhanced to handle protocol level segments using the USE_PROTOCOL statement.」

**两件事：① device level file 的处理被增强到能接纳 protocol level segment；
② 接纳的手段是 `USE_PROTOCOL` 语句。**

**它做什么**（逐字）：

> 「It will integrate the referred protocol level segment to the equation system.」

**`USE_PROTOCOL` 把一个「被引用的」protocol level segment 并进 equation system。**
**注意 `referred` 这个词**：它**不是新建**一个 segment，是把**别处已经定义好的**那个引进方程系统。
**所以这条路有前提**：那个 protocol level segment 得先存在——**它存在哪儿，见下一节。**

### `.prot_lev` 是被引用的那个文件

原文三句连写（逐字）：

> 「The protocol level definition is saved into a XML file within the corresponding protocol directory of the device. It can be identified by the extension .prot_lev .」

拆成四项：

| 项 | 原文 | 说明 |
|---|---|---|
| **装什么** | `The protocol level definition` | **protocol level definition**（不是整个 level setup） |
| **什么格式** | `a XML file` | XML |
| **放哪儿** | `within the corresponding protocol directory of the device` | device 的**对应 protocol 目录**里 |
| **怎么认** | `It can be identified by the extension .prot_lev` | **靠扩展名 `.prot_lev` 识别** |

**⚠️ 原文在 `.prot_lev` 与句号之间有一个空格**（逐字 `the extension .prot_lev .`），
**本页引文照原样，不替它去掉那个空格**（见 `## 出处`）。

**分工要点**：`.prot_lev` 是**产物/输入文件**，`USE_PROTOCOL` 是**写在另一个文件里的语句**——
**两者不是同一个文件**。`USE_PROTOCOL` 写在 device level setup file 里（下一节）。

### 可以写多条，位置只有两处，禁止一处

原文（逐字）：

> 「Multiple USE_PROTOCOL statements can be used in the SPECS or EQUATIONS sections to cover protocol dependent specification and equation dependencies.」

| | 位置 | 依据 |
|---|---|---|
| ✅ **允许** | `SPECS` section | 上面那句逐字 |
| ✅ **允许** | `EQUATIONS` section | 同上 |
| ❌ **不支持** | `SPECSET` section | 下面那条 `Note` |

**为什么允许多条**：为了 `cover protocol dependent specification and equation dependencies`
——**protocol 相关的 spec 和 equation 依赖**要分开覆盖，一条盖不住。

**唯一一条硬禁止**，原文是一整条 `Note`（逐字，**注意 `Note` 与后面的句子之间没有分隔符**）：

> 「Note It is not supported to enter the USE_PROTOCOL statement within the SPECSET section.」

**写成「不支持」（`not supported`），不是「非法」也不是「报错」**——
**原文没有再说什么情况下会发现这件事、报了会怎样。**
`SPECSET` 段本身是什么，在 [[spec-set]]（L2，stage `level`）那一页。

### 必须手写，没有工具代劳

原文一句（逐字）：

> 「The user has to enter the statement manually into the device level setup file.」

**这是一句操作要求**：`The user has to` ——**这句得你自己敲进去。**
**语料里没有说任何编辑器/工具会自动生成它**；例子里的那一行甚至是一条**注释掉的模板**：

```
#USE_PROTOCOL "<protocolName>:<levelSegmentName>" <portList>
USE_PROTOCOL "MDIO:DefaultPowerLevels" PoMDIO
```

——**上一行是模板（带 `#`），下一行是实际用法。** 这个「模板 + 实例」的成对写法
**是原文例子里唯一的用法示范。**

### 三个参数，以及参数之间的那条依赖

语法节里有三个参数，速查如下（**逐字定义在语法节，这里只说它们之间的关系**）：

| 参数 | 必填 | 原文里那句要紧的 | 关系 |
|---|---|---|---|
| `protocolName` | 是 | `The name of the protocol to use.` | **被引用的 protocol** |
| `levelSegmentName` | 是 | `Must be defined for the protocol specified by protocolName.` | **依赖 `protocolName`** |
| `portList` | 否 | `(optional) List of protocol ports.` | **可省** |

**唯一一条参数间的依赖**（逐字）：

> 「Must be defined for the protocol specified by protocolName.」

**即：level segment 必须是那个 protocol 底下已经定义过的**——
**与上面 `referred` 那个词说的是同一件事的两个面：先有定义，才谈得上引用。**
**原文没有写违反它时发生什么**（没有报错句、没有 `Errors` 段）。

**`portList` 省略时的行为**（逐字）：

> 「If omitted, all ports assigned to the protocol specified by protocolName. will be used.」

**即：不写 portList → 用该 protocol 名下的全部 port。**
**⚠️ 这一句里 `protocolName` 和 `will be used` 之间有一个句号**
（`specified by protocolName. will be used.`），**原文如此**（见 `## 出处`）。

### 引号的位置：整个 `protocolName:levelSegmentName` 被一对引号包住

语法行的形态（**语法节逐字**）：

```
USE_PROTOCOL "<protocolName:<levelSegmentName>" [<portList>]
```

**引号在这一行里包的是 `protocolName:levelSegmentName` 整段**，
**而语法行自己用的占位符括号是 `<…>`**——**两种括号混在同一行里**，
所以照抄时**不要把那对 `<>` 也抄进去**。
例子里的实例是：

```
USE_PROTOCOL "MDIO:DefaultPowerLevels" PoMDIO
```

对回去：

| 参数 | 例子里的值 | 由来 |
|---|---|---|
| `protocolName` | `MDIO` | 冒号**前**半段 |
| `levelSegmentName` | `DefaultPowerLevels` | 冒号**后**半段 |
| `portList` | `PoMDIO` | 引号**外**那个词 |

**（推断）冒号是 `protocolName` 与 `levelSegmentName` 的分隔符，
而两者的分界在语法行的引号内部**——**依据是语法行把 `protocolName:` 和
`<levelSegmentName>` 写在同一对引号里，且例子里的引号内正好有一个冒号**；
**原文没有一句话明写「用冒号分隔」，所以这是推断。**

### 例子给出的上下文（**这是本页最实的部分**）

例子的标题句（逐字）：

> 「The following except shows how to use the USE_PROTOCOL statement within a device level setup file.」

**⚠️ `except` 是原文的写法**，按句意应是 `excerpt`——**本页照原样引，不改**
（见 `## 出处`）。

例子里的 `USE_PROTOCOL` **不是孤零零一行**，它落在一段 setup 里，
**原文用 `...` 省略了若干处**（那些 `...` 是原文自己写的，见 `## 出处`）：

| 例子里的行（**逐字**） | 它在示范什么 |
|---|---|
| `hp93000,level,0.1` | **device level setup file 的文件头** |
| `EQSP LEV,EQN,#9000005436` | 挂 equation specification（[[eqsp]]） |
| `EQNSET 1 "levels equation set"` | 起一个 equation set |
| `SPECS    # starts the declaration of the specs` / `v_il_ctl [V]` | **`SPECS` 段的声明**（`USE_PROTOCOL` 允许的落点之一） |
| `EQUATIONS` / `# put here depend specs, resources in [V] and [mA]` | **`EQUATIONS` 段**（另一个允许的落点） |
| `LEVELSET 1 "normal"` | 起一个 level set |
| `#USE_PROTOCOL "<protocolName>:<levelSegmentName>" <portList>` | **模板行（注释掉）** |
| `USE_PROTOCOL "MDIO:DefaultPowerLevels" PoMDIO` | **实际用法** |
| `PINS std_ins reset_b wse_gen` / `vil= v_il_ctl` | 回到普通的 level 赋值 |

**⚠️ 一处位置对不上，原文没有解释**：正文说 `USE_PROTOCOL` 用在
`SPECS` 或 `EQUATIONS` sections，**而例子里它出现在 `LEVELSET 1 "normal"` 之后**。
**两种可能，原文都没排除、也都没明写**：
**(a) 例子把段的边界省略了**（例子里 `...` 多处，`EQUATIONS` 段可能还没结束）；
**(b) 「段」与例子的排版不是一回事。**
**本页 (a)(b) 并列，不判哪个对。**

## 典型用法

**原文没有 `## Procedure` 段，也没有 `## Before you begin` 段**——
**唯一可依据的是那一个 `## Example`。**
所以下面这份顺序是**从例子的排列 + 正文那两句要求**还原出来的，
**不是原文写成步骤的**（**这是本页的分界线：顺序是推断，每一条的依据是文档事实**）。

| # | 做什么 | 依据 |
|---|---|---|
| 1 | **先有 protocol level definition**（在 device 的对应 protocol 目录里，`.prot_lev`） | 原文：`It will integrate the **referred** protocol level segment`、`The protocol level definition is saved into a XML file …` |
| 2 | **确认 level segment 属于那个 protocol** | 原文 `Must be defined for the protocol specified by protocolName.` |
| 3 | **手动**把 `USE_PROTOCOL` 写进 device level setup file | 原文 `The user has to enter the statement manually into the device level setup file.` |
| 4 | **写在 `SPECS` 或 `EQUATIONS` 段里** | 原文 `can be used in the SPECS or EQUATIONS sections` |
| 5 | **不要写在 `SPECSET` 段里** | 原文 `Note It is not supported to enter the USE_PROTOCOL statement within the SPECSET section.` |
| 6 | **要覆盖多少个 protocol 相关依赖，就写多少条** | 原文 `Multiple USE_PROTOCOL statements can be used …` |
| 7 | **不写 `portList` 就接受「该 protocol 全部 port」** | 原文 `If omitted, all ports assigned to the protocol specified by protocolName. will be used.` |
| 8 | **照例子的形态填**：`"<protocolName>:<levelSegmentName>"`，port 写在引号外 | Example 逐字：`USE_PROTOCOL "MDIO:DefaultPowerLevels" PoMDIO` |

**最小可用的一行**（从例子直接摘，去掉 `#`）：

```
USE_PROTOCOL "MDIO:DefaultPowerLevels" PoMDIO
```

**用模板时记得**：模板里的 `<portList>` 是**可省项**，
**而 `<protocolName:<levelSegmentName>` 那一对尖括号是占位符、不是语法**（见上一节）。

**没有的东西**：原文**没有 `Errors` 段、没有 `Warnings` 段、没有 `Limits` 段**——
**所以「写错了会怎样」，本页和原文一样答不出**（除了 `SPECSET` 那一句 `not supported`）。

## 和谁有关

- [[level-file]] — **本页的边界就在这一页**。`level-file`（`title: Structure of an equation
  based level setup`，`layer: file`，`stage: level`）管的是**泛指 equation set 文件的格式**；
  **本页严格限定在 `USE_PROTOCOL` 语句与 `.prot_lev` 文件**。
  **原文通篇没有出现「equation set file 的通用结构」这个题目**——
  **所以「`USE_PROTOCOL` 之外那部分文件长什么样」，本页一个字都没有，去那一页。**
- [[spec-set]] — **`SPECSET` 段的归宿**。原文那条 `Note` 说
  `It is not supported to enter the USE_PROTOCOL statement within the SPECSET section.`
  ——**这是本页唯一一条禁止**，**而 `SPECSET` 段自己是什么、怎么起，在那一页**
  （`title: Spec sets`，`layer: L2`，`stage: level`）。**本页没读它。**
- [[equation-based-level-setup]] — **上游的概念页，原文自己指过去的**。
  原文 `## Related information` 的第二条链接就是 `Equation based level setup`。
  **本页只有这个链接名**；equation based level setup 整体是什么，在那页。
- [[level-setup-tool]] — **（推断）GUI 侧的入口**。原文 `## Related information` 的第三条
  链接是 `Level tab`——**`Level tab` 不在本 wiki 的链接清单里，所以这里写成反引号**，
  而 `Level tab` 属于哪个工具，**本页没有依据**；
  列在这里只是因为 `level-setup-tool`（`layer: gui`，`stage: level`）是 level 的 GUI 工具页。
  **（推断的依据仅此而已，本页没有那页的任何事实。）**
- [[eqsp]] — **例子里的第一条语句**（`EQSP LEV,EQN,#9000005436`）。
  那一页是 `EQSP, EQSP? - (EQuation SPecification transfer)`（`L1`，`stage: timing`）。
  **本页只有这一行出现而已**——`EQSP` 的参数与语义，本页一个字都没有。
- [[protocol-editor]] — **（推断）protocol 的编辑入口**。原文只写 protocol 目录与 `.prot_lev`，
  **没有任何一句提到编辑器**；**依据只是「那些东西都叫 protocol」。
  本页没有那页的任何事实。**
- [[device-directory]] — **（推断）目录结构的宿主**。原文说 `.prot_lev` 在
  `the corresponding protocol directory of the device`——**device 的 protocol 目录**；
  **device 的目录结构本身在那一页**（`title: Device directory structure`）。
  **本页没读它，所以「protocol 目录在 device 目录树的哪一层」，本页不知道。**
- [[level]] — **stage 页，最近的一段**。本页 frontmatter 的 `stage: level` 是
  **「读者该去哪一段找它的用法」，不是「归属」**（§6）。
  **本页不写流程叙述，顺序只在上一节的表格里以「依据」形式出现。**
- [[smartest-7.1.0]] — **版本页，本页 `## 版本` 唯一的落点**。
- `Setting up your levels`（**未建**）— 原文 `## Related information` 的第一条链接。
  **本页没读它**；它是不是这次 setup 的前置，**原文没有说**。
- `SPECS` / `EQUATIONS` / `LEVELSET` / `EQNSET`（**均未建**）— 例子里的语句与段名。
  **本页只用它们在例子里的位置，没有它们的语法**。
- `XML`（**未建、也不该建**）— `.prot_lev` 的格式，**原文只说了「是 XML 文件」这一句**，
  **元素名、schema、怎么生成，全都没有。**

## 版本

本文档**有** `## Functional changes` 段，**只有一条**（逐字）：

- **Introduced in SmarTest 7.1.0**

**这不是 §11.2 ② 那个哨兵**（哨兵写的是 `Introduced before SmarTest 6.3.2`）——
**`Introduced in SmarTest 7.1.0` 是一条常规的引入条目：本功能在 SmarTest 7.1.0 引入。**
**版本页见 [[smartest-7.1.0]]。**

**与 wiki 面向版本的关系**：本 wiki 面向 **SmarTest 7.10.3**，
**7.1.0 早于 7.10.3**，所以按文档的说法**这个功能在目标版本里已经在**。
**注意 §11 那条**：这只说明**文档这么写**，**不说明某台机台上能用、也没在机台上验过**
（本页 `verified: doc-only`）。

**版本段里没有 `USE_PROTOCOL` 之外的任何条目**——
**`.prot_lev` 这个扩展名、`SPECSET` 那条禁止，各自是哪个版本进来的，语料里没有。**

## 出处

`sources:` 一篇：
`02_System_reference/02.07_Test_Method_Reference/02.07.11.01.05.01_Level_equation_file.md`

**本页没做的：**

- **只读了这一篇。** 原文 `## Related information` 里的三篇
  （`Setting up your levels`、`Equation based level setup`、`Level tab`）
  **一篇都没读**——所以**本页不知道这次 setup 在整条 level 流程里的前后位置**，
  也不知道 `USE_PROTOCOL` 与 equation based level setup 的其它做法是什么关系。
- **`.prot_lev` 文件本身没读**（语料里也没有这么一篇）。**所以它里面长什么样、
  由谁生成、和 `USE_PROTOCOL` 的哪个字段对应，本页一个字都没有**——
  **原文只说「是 XML」和「靠扩展名认」。**
- **protocol 目录没查**。**所以 `.prot_lev` 在 device 目录树的哪一层、
  一个 protocol 目录能放几个，本页不知道。**
- **`SPECSET` 段没读**（[[spec-set]] 那一页没读）——所以**为什么 `USE_PROTOCOL`
  在它里面不被支持**（是语法冲突、还是求值时机），**本页和原文一样只有那句 `Note`。**
- **原文没有 `## Errors` / `## Warnings` / `## Limits` 段**（本页核过）。
  **所以「参数写错、protocol 不存在、segment 不属于该 protocol」各自会发生什么，
  语料里没有**——**这不是本页漏读，是原文没写。**
- **一张图都没看。** 原文没有图片引用（`![` 0 处）。
- **没有交叉验证任何别处的文档**（§11：本页只写这一篇里有的）。
  **尤其：`USE_PROTOCOL` 在别处是否还有第二种用法、`prot_lev` 是否还有别的拼法，
  本页没有去查过。**

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> **① 例子标题句里的 `except` 按句意应是 `excerpt`。** 逐字：
> `The following except shows how to use the USE_PROTOCOL statement within a device level setup file.`
> ——**`except`（除…之外）在句法上接不上后面的 `shows how to use`**，
> 而这一类文档里同一句式惯用 `excerpt`（摘录）。**本页引文照原样，不改。**
>
> **② `.prot_lev` 与句号之间有一个空格。** 逐字：
> `It can be identified by the extension .prot_lev .`
> ——**`.prot_lev` 后面、句号前面多一个空格**。**照原样引。**
>
> **③ `portList` 那一格的说明中间多一个句号。** 逐字：
> `If omitted, all ports assigned to the protocol specified by protocolName. will be used.`
> ——**`protocolName` 后面就是句号，`If omitted` 这个从句被它从中间截断了。**
> **照原样引，本页在散文里按句意读。**
>
> **④ `## Syntax` 那张参数表没有表头，而且表头行被写了两遍。** 逐字（原文开头几行）：
> ```
> Parameter
>  |
>
> Parameter
>
>  |
>
> Description/Range
>
>  |
>  |
> ```
> ——**`Parameter` 出现两次**，`|` 是散落的孤立行。
> **这张表在语法节里照样是这副样子**（语法节逐字抽的），**本页照实说，不替它补表头。**
>
> **⑤ 例子里的 ` ...` 是原文自己写的省略号**，出现 4 处
> （`hp93000,level,0.1` 之后、`v_il_ctl [V]` 之后、`# put here depend specs…` 之后、
> `vil= v_il_ctl` 之后）。**本页引例时照原样保留它们**——
> **按 §11.1，「`…` 出现在引文里的唯一合法场合，是原文自己就写着它」。**
>
> **⑥ `Note` 与它后面的句子之间没有分隔符。** 逐字：
> `Note It is not supported to enter the USE_PROTOCOL statement within the SPECSET section.`
> ——**`Note` 后面直接跟空格和正文**，没有冒号、没有句号、没有加粗标记。
>
> **⑦ `## Related information` 三条链接粘在一起，中间没有分隔符。** 逐字：
> `Setting up your levels` + `Equation based level setup` + `Level tab`
> ——**三对链接首尾相接**（原文里就是 `](<…>)[` 直接相连）。
> **本页在 `## 和谁有关` 里把它们分开写，但引文里的粘法是原文的。**
>
> **⑧ 语法行里占位符括号与字面引号混用。** 逐字：
> `USE_PROTOCOL "<protocolName:<levelSegmentName>" [<portList>]`
> ——**同一个 `<>` 里既有「占位符」的意思（`protocolName`），
> 又有一层是被引号包住的整体**，而 `[<portList>]` 用的是方括号。
> **原文没有说明这两种括号的规矩。本页照实并列，不替它统一。**
>
> **⑨ 正文说的落点与例子里的落点对不上。** 正文（逐字）：
> `Multiple USE_PROTOCOL statements can be used in the SPECS or EQUATIONS sections …`；
> 例子里的 `USE_PROTOCOL` 却在 `LEVELSET 1 "normal"` 之后。
> **原文没有解释这一处。本页并列 (a)(b) 两种可能，不判哪个对，也不替例子挪位置。**
>
> **⑩ 本篇没有 §11.2 ① 那种编码损坏。** 本页查过：**全文没有汉字，也没有 `鈥`**
> （`[一-鿿]` 与 `鈥` 均 0 命中）。**所以本文没有那一族的坏字。**

`verified: doc-only`
