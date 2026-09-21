---
type: object
title: Wavetable file
layer: file
stage: timing
tags: [timing, protocol, wavetable, timing-file, use-protocol, file-format]
related: [timing, timing-file, timing-equation-set, wavetable, eqsp, eqfs, timing-setup-tool, mapping-timing, smartest-7.1.0]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.11.01.05.03_Wavetable_file.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# Wavetable file

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,097 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.11.01.05.03_Wavetable_file.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

USE_PROTOCOL "<protocolName>" [<portList>] for wavetables

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

portList

 |

(optional) List of protocol ports.

If omitted, all ports assigned to the protocol specified by protocolName. will be used..

 |

### Example

The following except shows how to use the USE_PROTOCOL statement within a device timing setup file.

```
hp93000,timing,0.1
 ...

EQSP TIM,WVT,#9000015411

WAVETBL "wavetable 1"
DEFINES  parallel

PINS  xmit std_ins wse_gen reset_b
  0 "d1:!Z d2:F0N"  0
 ...

# Note, that only one wavetable is supported per protocol. Therefore no segment is given
WAVETBL "wavetable 1"
DEFINES  mdio_port

#USE_PROTOCOL "<protocolName>" <protocolPort>
USE_PROTOCOL "MyMDIO" PoMDIO

EQSP TIM,CLK,#9000000278
 ...

EQSP TIM,EQN,#9000011543
EQNSET 1 "equation set 1"
DEFINES mdio_port

SPECS
TSetup     	[ns]
 ...
TIMINGSET 1 "eq 1 ts 1"
period=TPer

#USE_PROTOCOL "<protocolName>:<timingSegmentName>" <protocolPort>
USE_PROTOCOL "MyMDIO:DefaultTiming" PoMDIO
 ...

EQSP TIM,SPS,#9000006739
  ...
```

<!-- 语法节 end -->

## 是什么

> **先说最要紧的一件事：这一篇的标题叫 `Wavetable file`，但它不是一份文件格式的字段表。**
> 它的正文第一句就把主题讲清了——**它讲的是「协议 wavetable 怎么进 device timing 文件」，
> 讲的是 `USE_PROTOCOL` 这条语句**。

> 「The device timing file handling has been enhanced to handle protocol wavetable specifications using the USE_PROTOCOL statement.」

**所以本页回答的问题是**：*我有一个协议（比如 MDIO），它的 wavetable / statemap 要接到这个 device 的
timing 里去，语句写在哪、写成什么样、能写几条、有没有不能写的地方。*
**它不回答的问题**：*wavetable 文件的列是什么、`PINS` 行怎么排、PhyIndex / Action / DevCyc 是什么*——
**本篇一个字都没写**。

### 机制：`USE_PROTOCOL` 把协议 wavetable 接进 timing equation system

原文的三句连起来就是完整机制：

> 「It will integrate the referred protocol wavetable to the timing equation system. The protocol wavetable is saved into the protocol specific timing a XML file within the corresponding protocol directory of the device. It can be identified by the extension .prot_tim .」

拆成三条：

| | 事实 |
|---|---|
| **谁被接进去** | 被引用的**协议 wavetable** |
| **接到哪** | **timing equation system** |
| **它落到什么文件** | device 的**对应 protocol 目录**下的一份**协议专属 timing XML 文件**，**扩展名 `.prot_tim`** |

**`It` 的主语是「device timing file 的处理」**（第一句的主语）——不是 `USE_PROTOCOL` 语句本身。
**本页按原样读，不替它改。**

### 两条 `Note`：一条数量限制、一条位置限制

| 限制 | 原文（逐字） | 意思 |
|---|---|---|
| **数量** | `Only one unique wavetable/statemap definition per protocol setup is permitted.` | **每个 protocol setup 只允许一份**唯一的 wavetable/statemap 定义 |
| **位置** | `It is not supported to enter the USE_PROTOCOL statement within the SPECSET section of the timing file.` | **`USE_PROTOCOL` 不许写在 timing file 的 `SPECSET` 段里** |

**位置限制只说了「不许写在哪」，没说「必须写在哪」。**允许写在哪，靠下一句读出来：

> 「Multiple USE_PROTOCOL statements can be used in the SPECS or EQUATIONS sections to cover protocol-dependent specification and equation dependencies.」

→ **可以写多条，位置是 `SPECS` 段或 `EQUATIONS` 段**，用途是覆盖**依赖协议**的 spec 与 equation。

> **⚠️ 这里有一处本页读出来的不一致，照实摆出来、不替语料调和**
> （详见「出处」的瑕疵⑤）：上面那句说可以写在 `SPECS` **或** `EQUATIONS`，
> 而例子里的**第一条** `USE_PROTOCOL` 落在 **wavetable 段**（`WAVETBL` / `DEFINES mdio_port` 之后、
> `EQSP TIM,CLK` 之前的那一块），**既不是 `SPECS` 也不是 `EQUATIONS`**。
> **原文没有解释这两处怎么统一**——本页只记下来。

### 一条「推荐但不强制」

> 「Utilizing port-based setups is not mandatory. However, it is recommended to be used to simplify the leverage and reuse of protocol setups.」

**用 port-based setup 不是必须的，但推荐**——理由是**复用**（`simplify the leverage and reuse of protocol setups`）。
（`portList` 这个参数就是这条路：省它 = 协议下所有 port 都用；写它 = 只对列出的 port 生效。）

### 语法与两个参数（本节在「语法 / 参数」节里，本页不重复）

| 参数 | 原文 | 本页的读法 |
|---|---|---|
| `protocolName` | `The name of the protocol to use.` | **协议名**——写错会指到不存在的协议（**报什么错，本篇没写**） |
| `portList` | `(optional) List of protocol ports.` | **可选**；省掉时的行为原文写的是 `If omitted, all ports assigned to the protocol specified by protocolName. will be used..` |

**语法行末尾那三个词 `for wavetables` 是原文的一部分**（不是本页加的注）：
`USE_PROTOCOL "<protocolName>" [<portList>] for wavetables`——**回上游 `126387.htm` 核过，确实是原文**。

### 一句本页答不了的

**`protocolName` 指的那些「协议」、`portList` 指的那些「protocol port」，是在哪里定义的**——
**本篇没写**。它只说了「protocol 目录」在 device 下面。
**所以「先在哪配好协议和 port，再来写 `USE_PROTOCOL`」这一步，本页给不出来**（见「出处」）。

## 典型用法

### 例子就是一份 device timing setup 文件（**整段在「语法 / 参数」节里，这里只走一遍**）

例子的骨架是 `hp93000,timing,0.1` 开头的一份 timing setup file，里面靠三条 `EQSP` 分段：
`EQSP TIM,WVT` / `EQSP TIM,EQN` / `EQSP TIM,SPS`。**协议 wavetable 这件事在头两段里各出现一次。**

### 两个写法（**差别只有一个：协议名后面带不带 `:<timingSegmentName>`**）

例子里**每一处都是两行**：上面一行是**注释掉的模板**（以 `#` 开头），下面一行是**真正执行的语句**。

| 写法 | 模板行（原文，**是注释**） | 实例行（原文，**是语句**） |
|---|---|---|
| **不带 segment** | `#USE_PROTOCOL "<protocolName>" <protocolPort>` | `USE_PROTOCOL "MyMDIO" PoMDIO` |
| **带 segment** | `#USE_PROTOCOL "<protocolName>:<timingSegmentName>" <protocolPort>` | `USE_PROTOCOL "MyMDIO:DefaultTiming" PoMDIO` |

**两处用的都是同一个 port：`PoMDIO`。**差别只在协议名后面多了 `:DefaultTiming`。

### 例子里的位置与上下文（**这是本页最实用的一节**）

| # | 它落在哪一段 | 它前面紧挨着的那几行 | 它后面跟着什么 |
|---|---|---|---|
| 1 | **wavetable 段**（`EQSP TIM,WVT` 之后） | `WAVETBL "wavetable 1"` → `DEFINES  mdio_port` | `EQSP TIM,CLK` |
| 2 | **equation 段**（`EQSP TIM,EQN` 之后） | `EQNSET 1 "equation set 1"` → `DEFINES mdio_port` →（`SPECS` / `TSetup [ns]` / `TIMINGSET 1 "eq 1 ts 1"` / `period=TPer`） | `EQSP TIM,SPS` |

**两处都紧跟一行 `DEFINES mdio_port`**（也叫出那个 port）。
**「`DEFINES` 那一行就是 `USE_PROTOCOL` 的作用对象」是本页的读法（推断）**——
依据是两处都在 `DEFINES` 之后、且原文的 `## Syntax` 把第二个参数说成 `List of protocol ports`。
**原文没有一句话解释 `DEFINES` 与 `USE_PROTOCOL` 的关系。**

**关于写法 1 为什么没有 segment**，原文的注释自己写了（逐字）：

> `# Note, that only one wavetable is supported per protocol. Therefore no segment is given`

→ **「每个协议只有一份 wavetable，所以不需要给 segment」**。
**这是原文给的唯一解释**，它和上面那条 `Note`（`Only one unique wavetable/statemap definition per protocol setup is permitted.`）说的是同一件事。

### 照抄时要注意的三件事

1. **`USE_PROTOCOL` 不是 `WAVETBL` 的替代品。**例子里的协议 wavetable **照样要先写 `WAVETBL "wavetable 1"`**，
   `USE_PROTOCOL` 是加在它后面的**接线**。
2. **`DEFINES` 的拼写在原文里两处不一样**：wavetable 段那处是 `DEFINES  parallel` / `DEFINES  mdio_port`
   （**两个空格**），equation 段那处是 `DEFINES mdio_port`（**一个空格**）。**原文如此，别以为是自己看错。**
3. **配对的顺序**：wavetable 段那处**不带** segment，equation 段那处**带** segment——
   例子里就是这个分工，**原文没有把「为什么这一处带、那一处不带」写成规矩**（见「出处」瑕疵⑥）。

### 一段可直接照搬的最小骨架（**据例子提炼，非原文**）

第一段（wavetable 段里）：

```
WAVETBL "<wavetable 名>"
DEFINES  <protocolPort>
USE_PROTOCOL "<protocolName>" <protocolPort>
```

第二段（equation 段里，同一个协议的另一个位置）：

```
EQNSET <n> "<equation set 名>"
DEFINES <protocolPort>
USE_PROTOCOL "<protocolName>:<timingSegmentName>" <protocolPort>
```

> **⚠️ 上面这两块是本页按例子排的（推断），不是原文的模板。**
> 原文没有给「最小骨架」，它只给了那一整份 setup file 例子；
> **缩略的过程里丢掉了 `SPECS` / `TIMINGSET` / `period=TPer` 这些行**——
> 要真用，回「语法 / 参数」节那份完整例子抄。

## 和谁有关

| 和谁 | 什么关系 | 依据 |
|---|---|---|
| [[timing-file]] | **宿主文件**。`USE_PROTOCOL` 写在 **device timing setup file** 里——例子的第一行是 `hp93000,timing,0.1`，那是 timing setup file 的头 | 例子 + 第一条 `Note` 里那句 `within the SPECSET section of the timing file`（**文档事实**） |
| [[eqsp]] | **分段者（上游）**。例子用三条 `EQSP`（`TIM,WVT` / `TIM,EQN` / `TIM,SPS`）把文件切开，两处 `USE_PROTOCOL` 分别落在前两段里 | 例子的代码块（**文档事实**） |
| [[timing-equation-set]] | **被接进去的那个 system 的一半**。原文说 `USE_PROTOCOL`「integrate the referred protocol wavetable to the timing equation system」；允许写的位置之一就是 `EQUATIONS` 段 | 原文引文（**文档事实**） |
| [[wavetable]] | **概念侧**（那页未建）。本页讲的是 wavetable 的**协议变体**，以及它怎么进 timing；**wavetable 本身是什么、有哪些列，本篇一个字没写** | 本篇的取材边界 |
| [[eqfs]] | **同族的另一条 L1 命令**（EQuation FileS transfer）。两条都属 equation based 配置这一族，**但本篇没有出现 `EQFS`**——这条关系来自 [[mapping-timing]] 把它们排在同一张对照表里 | [[mapping-timing]]（**本页读过的 wiki 页**） |
| [[timing-setup-tool]] | **GUI 侧的对口**。[[mapping-timing]] 的主表把 wavetable 的「GUI ↔ 文件 ↔ L1」三列排在同一行，GUI 列写的是这个工具 + 它的 wavetable editor。**本篇提到的 GUI 是零个**——这个关系来自那张表 | [[mapping-timing]]（**本页读过的 wiki 页**） |
| [[mapping-timing]] | **对照表页**（已建）。`wavetable-file` 出现在它主表第一行的「文件」列，与 `EQSP TIM,WVT` 后面那一段对应起来 | 那页的主表（**本页读过的 wiki 页**） |
| [[timing]] | **stage 页**。本页 `stage: timing` 填的是「**最近的一段**」——`USE_PROTOCOL` 是 timing setup 期的配置动作（§6） | frontmatter 约定 |
| [[smartest-7.1.0]] | **版本页**：本篇的 `## Functional changes` 只有一条，就是它 | 本篇版本段（**文档事实**） |

**两条本页答不住、只能记下来的**：

- **协议与 protocol port 在哪定义**——本篇没写。所以 `protocolName` / `portList` 的**上游**
  （协议建立、port 分配）**本页给不出来**，也**不替它链任何 pin / protocol 配置页**（**本页没读那些篇**）。
- **`.prot_tim` 那份文件在真实 device 目录下长什么样**——本篇只给了扩展名与目录的描述，
  **没有给字段、没有给例子**。**本页没在机台上看过这份文件。**

## 版本

本文档**有** `## Functional changes` 段，段里**只有一条**：

- **Introduced in SmarTest 7.1.0** → [[smartest-7.1.0]]

**这一条不是哨兵值**——措辞是 `in`（不是 §11.2 ② 那个 `before` 的哨兵写法），
所以它确实说的是「**这一版引进的**」。
**引进的东西是 `USE_PROTOCOL` 语句（也就是「协议 wavetable 进 timing」这件事本身）**——
依据是正文第一句把这件事说成是 `has been enhanced to handle` 的增强。

**版本段里没有的东西**（照实记）：**没有一条 `SmarTest X.Y.Z:` 形式的后续变更记录**。
所以 7.1.0 之后这条路有没有改过（`.prot_tim` 有没有换过扩展名、`SPECS`/`EQUATIONS` 之外
有没有放开过别的段）**在本篇里查不到**。

## 出处

`sources:` **一篇**：

- `02_System_reference/02.07_Test_Method_Reference/02.07.11.01.05.03_Wavetable_file.md`
  （TDC `126387.htm`，2,570 字节 / 106 行，**整篇读完**）
- 本页的「语法 / 参数」节是脚本从这一篇的 `## Syntax` / `## Example` 两段逐字抽的
  （**本页一个字没动**）。**本篇有 `## Syntax` 段，所以语法节里有那行签名**——
  这一点和 [[dfps]]（签名挂在自定段名下、语法节里没有）不同。

**本页没做的**：

- **`## Related information` 指的两篇一篇没读**：
  `02.08.04.34.04.03.03_Timing_Wavetables_-_Reference`（timing wavetable 的文件格式参考）
  与 `02.08.04.22.06_Wavetable_tab`（GUI 的 Wavetable 页签）。
  **所以「wavetable 文件到底有哪些列、`PINS` 行怎么排」本页一个字没有**——
  那正是这一篇标题看起来该讲、实际没讲的东西。
- **协议那一族（`protocolName` / protocol port 在哪定义）一篇没读**。
  **所以本页不知道「先在哪配好协议」，也没读 protocol editor 那一族。**
- **`02.07.11.01.05` 这一族的兄弟篇没读**——所以「`Wavetable_file` 与
  `Timing_equation_file` / `Equation_system` 是什么分工」本页答不了。
- **`EQSP` / `EQFS` 两篇命令页没读正文**——本页只在例子里看见 `EQSP` 的名字与它的三个分段参数。
- **两处 `USE_PROTOCOL` 在真实机台上有没有生效，本页不知道。**
- **图**：**本篇对 `raw/` 的引用 0 处**——实测 `.png` / `.jpg` / `.gif` / `!\[` / `<img` / `raw/`
  六种写法在本篇里**全部 0 命中**。**所以本页没有任何来自图的结论，这张「没有图」是查过的事实，
  不是「够不着」。**
- **没有实跑。** 没在机台上写过 `USE_PROTOCOL`、没看过 `.prot_tim` 文件、没跑过带协议 wavetable 的测试。
  `verified: doc-only` 指的就是这件事。

**⚠️ 本篇的六处语料瑕疵，本页照实记下、一处都没替它改**（②③⑤⑥ 本页回上游 `.htm` 核过）：

> ① **`except` 应为 `example`。**原文（`## Example` 段的第一句）逐字：

> `The following except shows how to use the USE_PROTOCOL statement within a device timing setup file.`

> **上游 `126387.htm` 里就是 `except`**（实测 1 次）→
> **属 §11.2 ⑥ 那族（上游就坏，救不回来）**，不是转换坏的。
> （这一句在「语法 / 参数」节里，**本页一个字没动**。）

> ② **两处错**：`protocolName` 后面**多了一个句点**（把句子截断了），末尾**多了第二个句点**。
> 原文（`portList` 那一格）逐字：

> `If omitted, all ports assigned to the protocol specified by protocolName. will be used..`

> **上游 `.htm` 里也是 `will be used..`**（实测）→ §11.2 ⑥ 那族。**同样在语法节里，本页没动它。**

> ③ **`saved into the protocol specific timing a XML file`**——**`a XML` 应为 `an XML`**。
> **上游 `.htm` 里也是 `a XML`**（实测：`a XML` 1 次、`an XML` 0 次）→ §11.2 ⑥ 那族。

> ④ **`It can be identified by the extension .prot_tim .`**——**扩展名与句点之间多一个空格**。
> **上游 `.htm` 里是 `<span class="filepath">.prot_tim</span> .`**（span 与句点之间就有空格）——
> **所以这个空格是上游 HTML 的结构带出来的**（本页照原样引）。

> ⑤ **「能写在哪」两处说法对不齐**：正文说 `in the SPECS or EQUATIONS sections`，
> 而例子里的第一条 `USE_PROTOCOL` 落在 **wavetable 段**（`WAVETBL` / `DEFINES mdio_port` 之后）。
> **原文没有解释这两处怎么统一。本页把两处并列摆着，不替它调和**（正文「是什么」里已记）。

> ⑥ **例子的模板行与 `## Syntax` 行对不齐**：模板行写的是 `#USE_PROTOCOL "<protocolName>" <protocolPort>`
> ——**第三个参数是「单个 port」且没有方括号**；而 `## Syntax` 行写的是 `[<portList>]`
> ——**「port 的列表」且是可选**。参数表的说明也写的是 `(optional) List of protocol ports.`。
> **原文如此，本页照原样两处并列。**

**另一处不算瑕疵、但容易数错的**：例子里 `WAVETBL "wavetable 1"` **出现了两次**
（一次给 `parallel`、一次给 `mdio_port`），**两次用的是同一个名字 `"wavetable 1"`**。
这是原文的写法，**本页照原样引，不判它是不是笔误**。

`verified: doc-only`
