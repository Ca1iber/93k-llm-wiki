---
type: object
title: UDVP - (UnDefine Virtual Pin)
layer: L1
stage: pin
tags: [udvp, l1, firmware-command, pin, virtual-pin, undefine]
related: [vpin, udef, udpr, udps, udpt, udup, udut, pin, command-reference, smartest-7.10.0]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.03.02.29_UDVP_-__UnDefine_Virtual_Pin.md
created: 2026-09-24
updated: 2026-09-28
verified: doc-only
---

# UDVP - (UnDefine Virtual Pin)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **468 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.03.02.29_UDVP_-__UnDefine_Virtual_Pin.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### UDVP

```
UDVP (pinlist)
```

### Parameters

| pinlist | The names of the pins to undefine. The @ symbol can be used to undefine all pins that were previously defined by the VPIN command. |
|---|---|

> ⚠️ 转录说明（非原文）：本表在上游 HTML 里含合并格（colspan / rowspan）；
> 跨格文字已按覆盖范围重复写出（**不是原表里有重复的格子**）。真结构见 `tdc-html/raw/353743.htm`。

### Example

- To undefine a virtual pin:

```
> UDVP (VPIN1)
```

- To undefine multiple virtual pins:

```
> UDVP (VPIN2,VPIN3)
```

- To undefine all virtual pins:

```
> UDVP (@)
```

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.03.02.29_UDVP_-__UnDefine_Virtual_Pin.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error occurs if:

- The specified pin is not a virtual pin.
- The specified pin has not been defined.

<!-- 报错节 end -->

## 是什么

**`UDVP`（UnDefine Virtual Pin）把一个或一串已经定义过的 virtual pin 从当前配置里撤掉。**
原文一句话说完：

> 「The UDVP command removes a defined virtual pin or list of virtual pins from the current
> configuration.」

| 要素 | 值 |
|---|---|
| **动作** | `removes`——**撤，不是改** |
| **对象** | `a defined virtual pin or list of virtual pins`——**一次可以撤一串** |
| **作用域** | `the current configuration`——**动的是配置** |
| **产物** | **本篇未写有什么产物**——没有返回示例、没有状态查询 |

**⚠️ 本篇是本族六页里唯一「有独立 `## Related information` 段」的一页**（它指向 [[vpin]]），
**也是本族里唯一把正命令写在自己参数说明里的一页之一**（另一页是 [[udps]]）。

### 参数只有 `pinlist`，而 `@` 的射程**被明确限定了**

逐字（见上面「语法 / 参数」节）：

> 「The names of the pins to undefine. The @ symbol can be used to undefine all pins that were
> previously defined by the VPIN command.」

| 你写什么 | 效果 |
|---|---|
| **一个 pin 名** | 撤掉那一个（`## Example` 里是 `VPIN1`） |
| **多个 pin 名**（**逗号分隔**） | 撤掉那几个（`## Example` 里是 `VPIN2,VPIN3`） |
| **`@`** | **撤掉「所有由 `VPIN` 定义过的 pin」**——**射程被这一句卡死在 `VPIN` 上** |

**`@` 的射程这一句，是本篇最值得与同族对照的地方**：

| 命令 | `@` 的原文说法 | 射程 |
|---|---|---|
| **`UDVP`** | `all pins that were previously defined by the VPIN command` | **只限「`VPIN` 定义过的」** |
| [[udef]] | `the symbol @ which removes all pins` | **全部 pin** |
| [[udps]] | `the symbol @ which undefines all DPS pins` | 全部 **DPS** pin |

**所以 `UDVP (@)` 不会碰普通的 digital pin**——**它由 `VPIN` 划界，不是由「是不是 pin」划界**。
**这是本篇的文档事实，不是本页的推断。**

**语法的括号：本篇的语法行里没有花括号。**
语法行逐字是 `UDVP (pinlist)`（见上面「语法 / 参数」节），**没有 `{ }`**；
而它的**三个例子**逐字是 `UDVP (VPIN1)` / `UDVP (VPIN2,VPIN3)` / `UDVP (@)`——**也没有花括号**。
**对照同族**：[[udps]] / [[udpt]] / [[udup]] / [[udut]] 的语法行都是 `{(pinlist)}` 这种
**「花括号包圆括号」**的写法，[[udpr]] 那篇又是另一种写法（直接写参数名加引号与竖线）。
**即：本族六页的语法行写法各不相同，本篇是其中最干脆的一页——语法行和例子写法完全一致。**
（**推断**：本篇因此**没有 `{}` 与 `()` 分工这个歧义**——
**这是从「语法行与三个例子用的是同一套括号」读出来的**，**原文没有解释过括号的用法**。）

### `## Syntax` 这个标题在本篇里叫 `## UDVP`

**本篇 H2 逐字是 `## UDVP`（命令名），不是 `## Syntax`**——见上面「语法 / 参数」节的
`### UDVP` 那一个小标题。**⚠️ 已回上游 `raw/353743.htm` 核过**：
那里就是 `<h2>UDVP</h2>`，**是上游如此，不是脚本抓错、也不是转换改的**。
**所以本族的 H2 命名是不统一的**：其余五页都是 `## Syntax`，只有本页用命令名。

### 两个报错条件，其中一条是**类型检查**——本族里只有本页有

（逐字见上面「报错条件」节，脚本取自本篇 `## Errors`。）

> 「An error occurs if:」

> 「- The specified pin is not a virtual pin.」

> 「- The specified pin has not been defined.」

| 条件 | 性质 |
|---|---|
| `The specified pin is not a virtual pin.` | **类型检查**：你写的名字存在、但它不是 virtual pin → **报错** |
| `The specified pin has not been defined.` | **存在性检查**：名字根本没定义过 → **报错** |

**第一条是本页独有的。** 同族的 [[udpr]] / [[udup]] / [[udut]] 的 `## Errors`
**都只有一句存在性检查**，而本页多一条**「它不是这一类东西」**。
**「所以 `UDVP` 不会误删一个普通 pin——它会先报错」这个读法是有原文依据的**
（原文那一节逐字是 `An error occurs if:`，底下才是条目
`- The specified pin is not a virtual pin.`——**两句在 raw 里是分开的两行**，
本页不把节首句和条目合成一句）。
**⚠️ 但「报错之后命令是整条中止、还是只跳过那一个名字」本篇没写**
（**语料未写**：第二个条件里的 `The specified pin` 是单数，而 `pinlist` 可以写多个——
**多个名字里混一个普通 pin 会怎样，本篇答不了**）。

**注意措辞**：本篇用 `An error occurs if:`（**occurs**），
而 [[udpr]] / [[udup]] / [[udut]] 用 `An error is generated if`（**is generated**）。
**同一个族、两种写法**（本页照原样引，不替它统一）。

## 典型用法

**本篇没有 `## Procedure` / `## Before you begin` / `## What to do next`**——
用法只有 `## Example` 那三条 + `## Parameters` 那一格。
**⚠️ 本篇的例子格式与本族其它页不同：它是一条一行的说明 + 一个带提示符的代码块**，
而且**三条例子给全了三种粒度**（单个 / 多个 / 全撤）——**这是本族六页里唯一给全的**。

| 要做的 | 发什么（逐字） | 原文章节 |
|---|---|---|
| **撤掉一个 virtual pin** | `> UDVP (VPIN1)` | `- To undefine a virtual pin:` |
| **撤掉多个 virtual pin** | `> UDVP (VPIN2,VPIN3)` | `- To undefine multiple virtual pins:` |
| **撤掉全部 virtual pin** | `> UDVP (@)` | `- To undefine all virtual pins:` |

**⚠️ 三个代码块里都带一个 `>` 提示符**（逐字就是 `> UDVP (VPIN1)`）——
**那是命令行提示符，不是要敲进去的字符**（见「出处」⚠️ ③）。
**原文没有说明这个 `>` 是什么**，**所以这一步是推断，不是文档事实**。

**顺序上的前提**：
1. **先有、后撤**：`## Errors` 第二条 `The specified pin has not been defined.` 说的就是它。
2. **而且必须先由 `VPIN` 定义过**：`@` 那句明写 `previously defined by the VPIN command`。
   **即：`UDVP` 的合法对象集合是由 `VPIN` 划出来的**（见「和谁有关」的 [[vpin]]）。

**「virtual pin 是什么、怎么建」本篇不定义、也不教**——它的 `## Application` 只有一句（逐字）：

> 「Managing virtual pins, see Virtual pins.」

**即：本篇把「virtual pin 怎么管」推给了 `Virtual pins` 那一篇**（**本页没读它**，见「出处」）。

**「怎么列出已有的 virtual pin」本篇答不了**：本篇**没有任何查询命令**
（已核：本篇 `?` **0 命中**）。**但 `VPIN` 那一侧有 `VPIN?`**——
依据是 [[vpin]] 的页标题 `VPIN, VPIN? - (Virtual PIN)` 与本篇 `## Related information` 指向它的那个链接名
（**本页没读 `VPIN` 的 raw**，见「出处」）。

**一条家族级的锁**：[[pin-config-locked-during-test]]。
**⚠️ 但本页要把适用范围说准**——那一句
`The firmware does not accept any configuration changes while a test is running.`
写在 `Pin configuration setup commands`（TDC `10649.htm`）的章首，
**而 `UDVP` 并不在那一章的分组表里**（实测 0 命中，见下）。
**它出现在 `02.06.03.02_List_of_configuration_commands.md` 那一份配置命令清单里**（实测在列）。
**所以「这一条锁管不管 `UDVP`」，本页只能记「它被归在配置命令清单里」这个事实，
不能替文档说它一定受管**（这是 [[pin-config-locked-during-test]] 自己那条
「范围没被文档限定的」的边界，本页不越界）。

## 和谁有关

### 这一族的结构：`UDxx` 是 `DFxx` 的撤销面——**而 `UDVP` 是唯一不属于那个分组索引的一页**

**这六个页面（[[udvp]] / [[udpr]] / [[udps]] / [[udpt]] / [[udup]] / [[udut]]）是同一族命令的撤销侧。**
族的划分**不是本页猜的**：`02.06.03_Pin_configuration_setup_commands.md` 逐条给了分组，
逐字（已剥链接标记）：

| 分组（逐字） | 命令 |
|---|---|
| `Commands for pin alias:` | `DFPR`, `UDPR` |
| `Commands for DPS pins:` | `DFPS`, `UDPS` |
| `Commands for pin groups and ports:` | `DFGP`, `UDGP`, `DFPT`, `UDPT` |
| `Commands for utility lines:` | `DFUT`, `UDUT`, `DFUP`, `UPAS`, `UDUP` |
| — | **`UDVP` 不在这个索引里**（实测 0 命中） |

**⚠️ 本页是这一族里唯一「不被那份 pin 配置分组表收录」的一页。**
`UDVP` 出现在**另一份清单**里——`02.06.03.02_List_of_configuration_commands.md`
（那一份把它排在 `UDUT` 与 `UPAS` 之间）。**本页没读那一份的正文**，
只从 `edges.jsonl` 里看到它有一条指向本页的边（见「出处」）。

**所以本页的正命令是 [[vpin]]**，而这一条配对关系**在本篇自己的正文里就写着**——
参数说明那一句 `previously defined by the VPIN command` 就是它，
而 `## Related information` 更是直接列出（逐字）：

> 「VPIN, VPIN? - (Virtual PIN)」

**⚠️ 注意 [[vpin]] 不是 `DFxx`**：本族其余五页的正命令都是 `DF` 打头
（`DFPR` / `DFPS` / `DFPT` / `DFUP` / `DFUT`），**只有本页的对家叫 `VPIN`**。
**这不是笔误，是命令名的构造本来就不一样**——`Virtual PIN` 不是靠 `DeFine` 建的。

- [[vpin]] —— **正向命令：那页建 virtual pin，本页撤掉。**
  **配对关系有两条文档依据**：本篇参数里的 `previously defined by the VPIN command`、
  以及本篇 `## Related information` 的链接名 `VPIN, VPIN? - (Virtual PIN)`。
  **而且它是双向的**：实测 `02.06.03.02.35_VPIN__VPIN__-__Virtual_PIN.md` 第 84 行
  有一条指向本页的边。
  **⚠️ 本页没读 `VPIN` 的 raw**——所以「`VPIN` 怎么建、`VPIN?` 返回什么」**本页一个字没有**。
- [[udef]] —— **同族另一支的撤销命令**（`UnDEFine pin`，撤普通 pin）。
  **两者最值得对照的一点正是 `@` 的射程**：`UDEF` 的 `@` 是**全部 pin**、
  `UDVP` 的 `@` 是**只有 `VPIN` 定义过的那些**。
  **⚠️ 本页原文里 `UDEF` 0 命中**（实测），**本页也没读 `UDEF` 的 raw**——
  上面那条对照里的 `UDEF` 引文来自 [[udef]] 那一页本身。

  > **须留意的一处**：[[udef]] 那一页里写着
  > 「`UDVP` 是 `UnDefine Virtual Pin`，和本篇只差一个 `V`」，
  > **并列成「虚拟 pin 侧的同类命令」（标了推断）**。**本页承接这条推论，并补上它的正依据**：
  > **本页的配对关系不是推断**——它在本篇参数与 `## Related information` 里各有一句。
- [[udpr]] / [[udps]] / [[udpt]] / [[udup]] / [[udut]] —— **同一族的另外五页**。
  **本页原文里这五个命令名全部 0 命中**（实测）——族的并列只出现在索引与字母序清单里。
- [[pin]] / [[command-reference]] —— **归属**：本篇在 `02.06_Command_Reference` 下。
  **⚠️ 但本篇的 `## Application` 指的**不是** `Configuration Setup Commands`**——
  它是本族六页里**唯一一页指到别处**的（逐字：
  `Managing virtual pins, see Virtual pins.`）。**所以本页 `stage: pin` 的依据是文档位置，
  不是 `## Application` 的指向。**（§6：`stage` 填的是**最近的一段**，不是归属。）
- `Virtual pins`（`02.08.04.18.02.07.01`，**不在 allowlist 里**）——
  **本篇唯一指向的那一篇**。**本页没读它**，**所以「virtual pin 是什么、在 GUI 里怎么管」本页没有。**
- [[pin-config-locked-during-test]] —— **可能适用的那条锁**，见「典型用法」里那段边界说明。

### 它不在那份 DSL 授权锁的名单里

`02.04.05.08.02_Disabling_a_pin_configuration_license_lock.md` 列出了能作废
pin configuration license 签名的命令（`*RST` / `UDAN` / `UDEF` / `UDPS` / `UDUP` / `UDUT`），
**`UDVP` 不在这份名单里**（本页核过）。**即：撤 virtual pin 不会作废那个签名。**
（**这是「那一篇没列它」这个事实**，**不是「撤 virtual pin 一定不影响签名」这个结论**。）
**这一条与本页不在 pin 配置分组表里，是同一件事的两个侧面。**

> **本页的 `（推断）` 有两处**：三个例子里那个 `>` 是提示符、
> 以及「**语法行与例子用的是同一套括号，所以本篇没有 `{}` 与 `()` 分工那个歧义**」这一点。
> 其余每条都能指到本篇原句，或上面那两篇被声明的文档的原行。

## 版本

`## Functional changes` 段有，**只有一条，逐字**：

```
- Introduced in SmarTest 7.10.0
```

**这一条不是哨兵值**：措辞是 `Introduced in`（**不是 `before`**），
所以按字面读就是「**7.10.0 引入**」——与 §11.2 ② 那种 `Introduced before SmarTest 6.3.2` 的写法**不是一回事**。
**它也是本族里最新的一个版本号**（对照 [[udpr]] 的 `6.5.2`；
[[udps]] / [[udpt]] / [[udup]] / [[udut]] 拿到的都是哨兵值）。

**⚠️ 这里有一个版本断代要说清**：`UDVP` 是 **7.10.0** 才有的，
**而本 wiki 面向 SmarTest 7.10.3**——**所以本页讲的这条命令在 7.10.3 上是存在的。**
**但「7.10.0 到 7.10.3 之间它有没有变过」本篇没写**
（本篇的版本段只有引入这一条，**没有后续变更记录**）。

**与 [[xps256-status-flags]] 的对照**（那页也是 7.10.x 引入的）：
那一页的版本段写着「Introduced in SmarTest 7.10.1」并且**另有 7.10.2 的变更**——
**即：同期的文档里，有的给了后续变更、有的只给引入**。**本页属于后者。**

## 出处

`sources:` 一篇：
`02_System_reference/02.06_Command_Reference/02.06.03.02.29_UDVP_-__UnDefine_Virtual_Pin.md`
（TDC `353743.htm`；**md 1,412 字节 / 65 行**，上游 htm 3,517 字节）。**整篇读完——本篇只有 65 行。**

**另外读了两篇 raw（本页 `sources:` 之外，逐条声明）：**

| 篇 | 为什么读 | 字节 / 行数 |
|---|---|---|
| `02.06.03_Pin_configuration_setup_commands.md`（TDC `10649.htm`） | 本页要**判定 `UDVP` 在不在那一族的分组表里**（结论：不在），并核对那条家族级的锁的原文 | 3,305 B / 41 行 |
| `02.06.03.01.01_Introduction.md`（TDC `10650.htm`） | **同一张分组表在它里面也有一份**——两处都不含 `UDVP`，用于排除「只是这一篇漏了」 | 3,061 B / 37 行 |

**还读了三篇 wiki 页（不是 raw）**：`wiki/objects/udef.md`（对照 `@` 的射程与那条已存在的推断）、
`wiki/objects/dfpr.md`（对齐同族写法）、`wiki/objects/xps256-status-flags.md`（对照 7.10.x 的版本写法）。

**本页的入边实测 3 条 / 3 篇**（`inline` + `toc` 口径，来源 `extract/edges.jsonl`）：
`02.06.03.02.35_VPIN__VPIN__-__Virtual_PIN`、`02.06.03.02_List_of_configuration_commands`、
`02_System_reference/index.md`。**三条全是整篇引用，一条锚点都没有**
（`anchor` 字段全为 `null`）。**⚠️ 本页没读这三篇的正文**，只读了边里带的那一行原句。

**本页没做的**：

- **`VPIN` 的 raw 没读**——**本页连 `VPIN` 长什么样都不知道。**
  **所以「virtual pin 怎么定义、`VPIN?` 返回什么、能不能定义多个」本页一个字没有。**
- **`Virtual pins`（`02.08.04.18.02.07.01`）没读**——本篇 `## Application` 唯一指向的那一篇。
  **所以「virtual pin 在 GUI 里怎么管」本页没有**，
  **「virtual pin 是什么」（本篇第一句只说 `a defined virtual pin`）本页也答不了。**
- **`02.06.03.02_List_of_configuration_commands.md` 的正文没读**——
  本页只知道它有一条指向本页的边，**它怎么给命令分组本页不知道**。
- **`02.06.12_Utility_Line_Commands` 那一系的清单没读**——
  本页只用它来确认 `UDVP` **不在** utility line 那一系里（按文件名扫的）。
- **图：本篇没有内嵌图片。** 判据可核：本篇 md 里 `.png` / `.jpg` / `![` **0 命中**。
  **所以本页没有任何来自图的结论**（§11.4）。
- **没有实跑。** 没在机台上发过 `UDVP`、没撤过 virtual pin、
  **也没试过「`pinlist` 里混一个普通 pin」到底报不报错、报错后其余名字有没有被处理**。
  `verified: doc-only` 说的就是这件事（§11：文档里有 ≠ 这台机器上能用）。
- **没有动 `wiki/index.md`**。

> ⚠️ **本篇的语料瑕疵与结构上要注意的地方，本页照实记下、一处都没替它改**（§11.2）。
> **本篇 md 的 CJK 字符数实测为 0**——**没有 §11.2 ① 那一族编码乱码。**
>
> **① H2 标题是命令名 `## UDVP`，不是 `## Syntax`。**
> **⚠️ 已回上游 `raw/353743.htm` 核过**：那里就是 `<h2>UDVP</h2>`——
> **上游如此，不是脚本抓错、也不是转换改的**（§11.2 ⑥ 的判法）。
> **本族其余五页的 H2 都是 `## Syntax`**，所以本族的标题命名不统一。
>
> **② `## Parameters` 那张表在 raw 里被压平，而且缺表头。** 逐字（本篇 `## Parameters`
> 起头那一段的完整原文）：
>
> ```
> ## Parameters
>
>  |
>
> pinlist
>
>  |
>
> The names of the pins to undefine. The @ symbol can be used to undefine all pins that were previously defined by the VPIN command.
>
>  |
> ```
>
> ——**一格一行、中间夹着孤立的 ` | `**。
> **⚠️ 注意它的形态和 [[udup]] / [[udut]] 又不同**：
> 那两篇把 ` | 参数名 |` 挤在同一行，**本篇是名字单独一行**（与 [[udpr]] / [[udps]] / [[udpt]] 同款）。
> **说明文字一个字没丢**，但**本篇 raw 里没有 `Parameter` / `Description` 之类的表头行**——
> **所以「哪一列是什么」是从位置读出来的，不是原文写的。**
> **⚠️ 上游 `.htm` 里这张表是完整的**：`raw/353743.htm` 里写着
> `<table class="frame-bottom">`，里面是 `<colgroup><col><col><col><col></colgroup>`，
> 第二格上还带一个 **`colspan="3"`**（**四列的 colgroup，实际只填了两格**）。
> **所以「压平」是转换侧的产物，不是上游就坏的**（§11.2 ⑥ 的判法：回 `.htm` 核）。
>
> **③ 三个代码块里各带一个行首 `>`。** 逐字三处：
> `> UDVP (VPIN1)` / `> UDVP (VPIN2,VPIN3)` / `> UDVP (@)`
> ——**上游 `raw/353743.htm` 里那三个 `>` 是 HTML 转义过的 `&gt;`，正文里就是这个字符**，
> **不是 markdown 引用块标记**。**本页照原样记**，
> 但**在正文里引用它们时用反引号包住，免得那个 `>` 被本页当成引用块的开头**。
> **⚠️ 第一个例子的行尾空格在转换时被吃掉了**：上游逐字是 `&gt; UDVP (VPIN1)  `
> （**`)` 后面两个空格**），而 md 里逐字是 `> UDVP (VPIN1)`——**两个空格没了**。
> **只有这一个例子有尾随空格，另两个没有**（上游 md 两侧都是如此）。
> **这条属 §11.1 ① 的「折叠空白」范畴，本页不判它对不对，只记这里有这么一处差异。**
>
> **④ 报错句的动词与本族其它页不同。** 逐字：
> `An error occurs if:` ——**`occurs`**，
> 而 [[udpr]] / [[udup]] / [[udut]] 逐字是 `An error is generated if`（**`is generated`**）。
> **同一个族、两种写法，本页照原样引，不替它统一。**
>
> **⑤ 三个例子的说明行是「不定式短语」，与同族各页那种以 `This example` 开头的说明句不同。**
> 逐字三行：`- To undefine a virtual pin:` / `- To undefine multiple virtual pins:` /
> `- To undefine all virtual pins:`；**上游 htm 里这三行是一个 `<ol>` 列表**，
> 而 md 里渲染成了 `-` 开头的无序列表（**`ol` → `-`，这是转换侧的行为**）。
> **本页照 raw 的 md 形态引。**
>
> **⑥ 本篇在语料里只有一份投放。** 实测：`by-category` 下文件名含 `_UDVP_` 的 `.md`
> **只有 `02.06.03.02.29` 这一份**。判据是**文件名扫描**，不是全文比对。
> **所以本页没有「两份投放在哪几行不一致」的问题**（对照 [[udup]] / [[udut]]：那两页各三份）。
> **⚠️ 它也是本族六页里唯一一份落在 `02.06.03.02.*` 系列的**——
> 其余五页的 `sources:` 都在 `02.06.02.02.*` 系列。

`verified: doc-only`
