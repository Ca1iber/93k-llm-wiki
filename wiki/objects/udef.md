---
type: object
title: UDEF - (UnDEFine pin)
layer: L1
stage: pin
tags: [udef, l1, firmware-command, pin, pin-configuration, undefine, sequencer-off, channel, virtual-pin]
related: [pin, command-reference, pin-config-requires-sequencer-off, sqst, dfpn, udvp, smartest-7.10.3]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.295_UDEF_-__UnDEFine_pin.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# UDEF - (UnDEFine pin)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **431 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.295_UDEF_-__UnDEFine_pin.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
UDEF {(pinlist)}
```

### Parameters

| pinlist | Consists of single or multiple pin names or the symbol @ which removes all pins. If more than one pin is required, the names must be separated with a comma. |
|---|---|

### Example

```
UDEF (Q3)
```

This example causes pin Q3 to be removed from the current configuration. If you subsequently redefine the channel using the same or a different name, it assumes its former operating mode and the pin type OFF.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.295_UDEF_-__UnDEFine_pin.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if you attempt to undefine pins while the sequencer is in the run or the break state. See the command `SQST, SQST? - (SeQuencer STate)`（raw: `02.06.02.02.241_SQST__SQST__-__SeQuencer_STate.md`） for details.

<!-- 报错节 end -->

## 是什么

**`UDEF`（UnDEFine pin）只做一件事：把一个已经定义过的 pin 从当前配置里撤掉。**
原文一句话就是全部机制：

> 「The UDEF (UnDEFine pin) command removes a defined pin from the current configuration.」

| 要素 | 值 |
|---|---|
| **动作** | `removes`——**撤掉一个已有的定义** |
| **对象** | `a defined pin`——**只对「已经定义过」的 pin 有意义** |
| **作用域** | `the current configuration`——**动的是配置** |
| **产物** | **没有产物**（不产生、不返回、不改硬件设置） |

**原文只说它动的是 `the current configuration`，没有说它在硬件上做了什么**——
**所以「撤掉之后那条通道物理上怎么样」本篇答不了**（**语料未写**）。
下文那条例外（重新定义会拿回旧 mode）是本篇唯一一句讲到「撤掉之后还剩下什么」的话。

### 参数只有 `pinlist` 一个，而它有三种写法

> 「Consists of single or multiple pin names or the symbol @ which removes all pins.
> If more than one pin is required, the names must be separated with a comma.」

| 你写什么 | 效果 |
|---|---|
| **一个 pin 名** | 撤掉那一个 |
| **多个 pin 名**（**必须逗号分隔**） | 撤掉那几个 |
| **`@`** | **`which removes all pins`——撤掉全部 pin** |

**`@` 不是「加进列表里的一个元素」**：原文说的是 `the symbol @ which removes all pins`，
**`@` 自己就代表「全部」这个意思**。
**「`@` 能不能和一串 pin 名混在同一张列表里」——语料未写**，本页不判。

**注意 `pinlist` 这个词的第一句是 `Consists of …`，它没有主语句**——
参数表在 raw 里被压平成「一格一行」（见「出处」⚠️ ①），
**所以这一句读起来像悬空的**，但它就是 `pinlist` 那一格的说明。

### 语法的括号：`{}` 和 `()` 不是一回事

原文的语法行与例子写法不同：

| 处 | 逐字 |
|---|---|
| 语法行 | `UDEF {(pinlist)}` |
| 例子 | `UDEF (Q3)` |

**读法（推断）**：**圆括号是要照写的字面字符，花括号是「这里填东西」的占位框**。
依据是**本篇自己**的两处——例子是**实际发出去的命令行**，那里只有圆括号；
**花括号在例子和正文里一次都没出现过**。
**原文没有解释这两种括号的分工**（用了符号却没有符号说明表），**所以这一步是本页的推断，不是文档事实。**
**实操上的后果**：照着例子写 `UDEF (Q3)`，**不要把花括号也打进命令里**。

### 例子讲了「撤掉之后会怎样」——这是本页最有用的一句

> 「This example causes pin Q3 to be removed from the current configuration.
> If you subsequently redefine the channel using the same or a different name, it assumes
> its former operating mode and the pin type OFF.」

| 时点 | 原文 | 读出来是什么 |
|---|---|---|
| `UDEF (Q3)` 发生时 | `causes pin Q3 to be removed from the current configuration` | 撤掉 |
| **之后再定义回来时** | `it assumes its former operating mode and the pin type OFF` | **operating mode 沿用它原来的；pin type 是 `OFF`** |

**两处最容易读错的地方：**

> **① 「同名或不同名都行」——原文写的是 `using the same or a different name`。**
> **也就是说那个 operating mode 不是挂在名字上的**，它是跟着**那条 channel** 走的：
> 换个名字重新定义，照样拿回旧 mode。
> （**推断**，依据就是这一句自己。**原文没有正面解释这个机制是怎么实现的**，
> 也没有说「换一条 channel 会不会也拿回旧 mode」。）

> **② 「mode 保住」不等于「什么都没丢」。** 原文只列了**两样**：
> operating mode **沿用旧的**、pin type 变成 **`OFF`**。
> **`OFF` 是这一句里唯一大写写的取值**（§11：命令与取值大小写敏感，原样保留）。
> **level / timing / 属于哪个 group / 是不是 virtual pin 这些会不会也回退——语料未写。**
> **所以「UDEF 一下就能把通道恢复出厂」是读多了**：这篇只担保了 mode 一样、type 是 OFF。

### 什么时候会报错：**只有一条，而且它点名了另一个命令**

（全文见上面「报错条件」节，脚本逐字取自本篇 `## Errors`。）

| 触发条件 | 原文 |
|---|---|
| **sequencer 处在 run 或 break 状态时去 undefine pin** | `An error is generated if you attempt to undefine pins while the sequencer is in the run or the break state.` |

**后面还跟了半句，指到另一个命令**：

> 「See the command SQST, SQST? - (SeQuencer STate) for details.」

**即：为什么「run / break 时不许改 pin 配置」，以及那两个状态各是什么，本篇不解释，推给了 [[sqst]]。**
**这不是 `UDEF` 一条命令的规矩**，是整个 pin configuration 命令族共有的——
**那条约束已经单独建了页**（[[pin-config-requires-sequencer-off]]，
它把本篇这句 `## Errors` 原句收进去当证据）。**本页只负责说清「错在哪一步」。**

> ⚠️ **一个容易读反的地方**：报错条件是「**不许在 run / break 时 undefine**」，
> **不是「不许 undefine」**。**sequencer 在 OFF 时，这条命令没有任何前置条件。**
> ——「run / break 之外还有哪些状态、`OFF` 怎么确认」在本篇里没有，得看 [[sqst]]。

## 典型用法

**本篇没有 `## Procedure` / `## Before you begin` / `## What to do next`**——
用法全部来自 `## Example` 一条、`## Parameters` 那张（压平的）表、以及正文前两句。

**顺序是死的，而且只有三步**：

```
① 确认 sequencer 是 OFF（否则命令会报错）   ← 依据：本篇 ## Errors
② UDEF (Q3)   或   UDEF (@)                ← 依据：本篇 ## Syntax / ## Example
③ 需要时再定义回来（同名或换名）            ← 依据：本篇 ## Example 的第二句
```

| 要做的事 | 怎么写 | 依据 |
|---|---|---|
| **撤掉一个 pin** | `UDEF (Q3)` | `## Example` |
| 撤掉多个 pin | `UDEF (p1,p2)`——**逗号分隔** | `If more than one pin is required, the names must be separated with a comma.`——**原文没有给多 pin 的完整例子** |
| **撤掉全部 pin** | `UDEF (@)` | `the symbol @ which removes all pins`——**原文没有给 `@` 的命令行例子**（把两个事实合起来写是本页的整理，**不是原文的一条示例**） |
| 先看有哪些 pin 可以撤 | **语料未写**——本篇没有任何「列出已定义 pin」的查询语法 | — |
| 撤掉之后再定义回来 | 再发一次定义命令（**同名或不同名**） | `If you subsequently redefine the channel using the same or a different name` |
| **撤掉一条 virtual pin 的定义** | **本篇没有这个语法**——见「和谁有关」的 `UDVP` | — |

**三条容易踩的约束**：

1. **sequencer 必须在 OFF**（本篇 `## Errors` 唯一一条；细节在 [[sqst]]）。
   **run / break 是原文点名的两个状态**——**其余状态会不会也报错，本篇没有列全。**
2. **`@` 是「全部」，不是「某一个叫 @ 的 pin」**——**它一条不留**。
3. **撤掉不等于清空**：重新定义时 **operating mode 会拿回旧的，pin type 是 `OFF`**（见「是什么」）。

**归属**：原文 `## Application` 一节全文只有一句——
`Pin configuration, see Configuration Setup Commands.`
**即本篇把自己归进「pin 配置」那一族命令**（`Configuration Setup Commands` 那篇**本页没读**）。
**这一句是 [[pin]] 与 [[command-reference]] 两个 `related` 的依据。**

**出错时**：**本篇 `## Errors` 只有一条**（就是上面那条），而且没有 `## Warnings` 段
（已核：`## Warnings` 在本篇 0 命中）。**所以「还有什么别的错法」本篇答不了。**

## 和谁有关

- [[pin]] / [[command-reference]] —— **归属**：`stage: pin` 的依据是 `## Application`
  指向 `Pin configuration, see Configuration Setup Commands.`（配置类命令章）；
  文档本身在 `02.06_Command_Reference` 下。（§6：`stage` 填的是**最近的一段**，不是归属。）
- [[pin-config-requires-sequencer-off]] —— **本篇唯一那条例外条件的专页**。
  那页把本篇 `## Errors` 的**原句**收进去当证据（它自己 `sources:` 里就有本篇的 rel 路径），
  并把 `DFPN` / `UDEF` / `CONF` / `PALS` **四个命令的同一条锁**并列起来。
  **关系是「本页产生证据 / 那页给结论」**——**「为什么必须是 OFF」本页不解释，那页解释。**
- [[sqst]] —— **本篇 `## Errors` 点名的命令**（`See the command SQST, SQST? - (SeQuencer STate) for details.`）。
  **`run` / `break` 两个状态的定义、怎么查、怎么退出，全在那一页。**
  **本页没读它**，所以本页只写「有这两个状态」，不写它们的内容。
- `Configuration Setup Commands`（**未建、且不在 allowlist 里**）——
  `## Application` 只指向它，**本篇对它的说明就那半句**。**本页没读。**
- [[dfpn]] —— **`（推断）`：定义侧的对家**。**本篇一个字没提 `DFPN`**
  （已核：`DFPN` 在本篇 0 命中）。依据有两条，都在本篇之外或本篇的名字里：
  ① **命令名自己的前缀**——本篇标题写的是 `UnDEFine pin`，
  有 `Un` 前缀就说明存在一个「define」侧；
  ② **本页 `related` 里那几个同类页**（[[pin-config-requires-sequencer-off]] 把 `DFPN` 与 `UDEF`
  并列为同族）。
  **「拿 `DFPN` 定义、拿 `UDEF` 撤掉」这个配对本身是对的，但它是推断，不是本篇的文档事实**——
  **`DFPN` 的语法本页一个字没有。**
- [[udvp]] —— **`（推断）`：虚拟 pin 侧的同类命令**。`UDVP` 是 `UnDefine Virtual Pin`，
  **和本篇只差一个 `V`**。**本篇一个字没提 `VPIN` / `UDVP`**（已核，0 命中）。
  这条关系的依据是**命令名的构造相同 + 同为 `stage: pin`**，
  **不是本篇的任何一句话**——**所以标推断，不当文档事实用。**
- `UDVP - (UnDefine Virtual Pin)` 在**本篇里不存在**；
  **`VPIN` 那篇的 `Related information` 才点名 `UDVP`**（见 [[vpin]]）——
  **所以「虚拟 pin 怎么撤」的答案在 [[udvp]]，不在本页。**

> **本页只有上面两条 `（推断）`。** 其余每条都能在本篇里指到原句；
> **`（推断）` 那两条的依据写在条目里，不藏在句子里**（§11 的三种话要分开标）。

## 版本

本文档**有** `## Functional changes` 段，**只有一条，逐字**：

```
- Introduced before SmarTest 6.3.2
```

**按 §11.2 ②，这不是「6.3.2 的变更记录」，是一个哨兵值。**
那 2,677 条同款写法（`Introduced before …`）的意思是
「**在本文档集覆盖范围开始之前就已经有了**」——
**照字面读会生成一条「6.3.2 新增了 `UDEF`」的假信息，而且格式齐整。**

**所以：`UDEF` 究竟成立于哪个版本，这份语料里没有。**
本页只能记「**至少早于 6.3.2 的覆盖起点**」，**不能记成「6.3.2 引入」。**

**与 wiki 面向版本的关系**：本 wiki 面向 **SmarTest 7.10.3**（[[smartest-7.10.3]]），
**而本篇的版本段一条变更都没有**——**所以「6.3.2 之后 `UDEF` 有没有变过」语料里答不了。**

## 出处

`sources:` 一篇：
`02_System_reference/02.06_Command_Reference/02.06.02.02.295_UDEF_-__UnDEFine_pin.md`
（TDC `98821.htm`；**md 1,205 字节 / 46 行**，上游 htm 3,270 字节）。**整篇读完——本篇只有 46 行。**

**本页没做的**：

- **图：本篇没有内嵌图片。** 判据可核：本篇 md 里 `.png` / `.jpg` / `![` **0 命中**。
  **所以本页没有任何来自图的结论**（§11.4）。
- **`Configuration Setup Commands` 没读**——`## Application` 唯一的指向。
  **所以「pin 配置那一族还有哪些命令、它们什么关系」本页没有。**
- **[[sqst]] 的原文没读**——**`run` / `break` 是什么、怎么查、还有哪些状态，本页一个字没有**；
  本页只有本篇 `## Errors` 点名它的那半句。
- **[[dfpn]] 的原文没读**——那条配对关系是**跨篇推断**，依据写在「和谁有关」里。
- **[[udvp]] / [[vpin]] 的原文没读**——同上，**纯名称推断**。
- **没有 `## Warnings` 段**（已核，0 命中），只有 `## Errors` 一条。
  **脚本那条报错节的抬头写的是 `## Errors` / `## Warnings` 两个段名——
  对本篇来说 `## Warnings` 是空的。**
- **没有实跑。** 没有在机台上发过 `UDEF`、没触发过「sequencer 在 run 时 undefine」那条报错、
  也没验证过「换个名字重新定义会不会真拿回旧 operating mode」。
  `verified: doc-only` 说的就是这件事（§11：文档里有 ≠ 这台机器上能用）。

> ⚠️ **本篇的语料瑕疵与两处结构上要注意的地方，本页照实记下、一处都没替它改**（§11.2）。
> **本篇 md 的 CJK 字符数实测为 0**——**没有 §11.2 ① 那一族编码乱码。**
>
> **① `## Parameters` 那张表在 raw 里被压平，而且 `pinlist` 那一格没有表头。**
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
> Consists of single or multiple pin names or the symbol @ which removes all pins. If more than one pin is required, the names must be separated with a comma.
>
>  |
> ```
> ——**每一格独占一行，中间夹着孤立的 ` | `**。
> **「语法 / 参数」节里那个孤零零的 ` | ` 就是它**（同批的 [[dfut]] / [[dfpr]] / [[pslv]] 同一形态）。
> **说明文字一个字没丢**，但**本篇 raw 里没有表头行**（没有 `Parameter` / `Description` 之类）——
> **所以「哪一列是什么」是从位置读出来的，不是原文写的。**
>
> **② 同一个词在一篇里大小写不一致：`UnDEFine` 与 `undefine`。**
> 逐字两处：
> `The UDEF (UnDEFine pin) command removes a defined pin from the current configuration.`（**正文第一句，`UnDEFine`**）
> 对
> `An error is generated if you attempt to undefine pins while the sequencer is in the run or the break state.`（**`## Errors`，`undefine`**）。
> **本篇另外三处 `UnDEFine` 是 frontmatter 的 `title:`、frontmatter 的 `source_html:` 文件名、
> 以及 H1 标题行（`# UDEF - (UnDEFine pin)`）——实测四处，逐行是第 2、4、6、8 行。**
> **§11 说命令大小写敏感、原样保留——本页两处各照各的引，不替它统一，也不判哪个对。**
> （上面「是什么」里引第一句时用的是 `UnDEFine`，引报错时用的是 `undefine`，**两处都与 raw 一致**。）
>
> **③ `{}` 与 `()` 两种括号并存，而且原文没有符号说明。**
> 逐字两处：语法行 `UDEF {(pinlist)}` 对例子 `UDEF (Q3)`。
> **这不是错字，是排版**（同族的 `DFUT` / `VPIN` 语法行用的是同一套 `{}` 写法），
> **但本篇没有任何一句解释 `{}` 指什么**——**所以上面「是什么」里那条读法标了 `（推断）`。**
>
> **④ `pin` 与 `channel` 在同一句里换词。** 逐字：
> `removes a defined pin from the current configuration`（**pin**）
> 对 `If you subsequently redefine the channel using the same or a different name`（**channel**）。
> **两句说的是同一个被撤掉的东西**，原文没有说明这两个词在这里是不是同义——
> **本页并列两处，不替它划等号。**（这也是上面「mode 跟着 channel 走」那条推断的**唯一**依据。）
>
> **⑤ 同一篇文档在语料里投放了两份，本页只用了其中一份。**
> 另一份是 `02.06_Command_Reference/02.06.03.02.24_UDEF_-__UnDEFine_pin.md`
> （`source_topic: "98821_2.htm"`，**1,206 字节**）。
> **实测 `diff`：两份正文逐行完全相同，差别只有 frontmatter 的第 3、4 行
> （`source_topic` / `source_html`）**，那 1 字节的差就是 `98821` → `98821_2`。
> **两份上游也各有一个 `.htm`，而且 `cmp` 报 `98821.htm` 与 `98821_2.htm` 完全一致**
> （都是 3,270 字节）——**所以这是上游 TDC 就有的重复投放，不是转换产生的**（§11.2 ⑥ 的判法）。
> **本页的 `sources:` 用的是 `02.06.02.02.295` 那一份**；
> **另一份的内容本页没有另读一遍**（因为实测正文相同）。
> **⚠️ 但 [[chin]] 的情形正好相反**：那一篇本页的 `sources:` 用的是 `02.06.02.02.22`，
> 而 `wiki/stages/pin.md` 的 `sources:` 列的是同篇文档的另一份投放 `02.06.03.02.01`
> （见 [[chin]] 的「出处」）。**两页指向同一篇文档的两份投放，
> 这是语料的结构，不是谁引错了。**

`verified: doc-only`
