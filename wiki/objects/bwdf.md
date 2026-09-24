---
type: object
title: BWDF, BWDF? - (Break Waveform DeFinition)
layer: L1
stage: timing
tags: [timing, break-waveform, bwdf, l1-command, firmware-command, fixed-timing, edge-actions]
related: [bwds, wsus, waveform-set, pclk, wave, timing, timing-setup-commands]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.13_BWDF__BWDF__-__Break_Waveform_DeFinition.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# BWDF, BWDF? - (Break Waveform DeFinition)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,820 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.13_BWDF__BWDF__-__Break_Waveform_DeFinition.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### BWDF

```
BWDF {wvf_set}, {a1}, {a2}, {a3}, {a4}, {a5}, {a6}, {(pinlist)}
```

### BWDF?

```
BWDF? {wvf_set|"wavetable_name"|specset_id|"multiport_spec"}, {(pinlist)}
```

returns:

```
BWDF {wvf_set|"wavetable_name"|specset_id|"multiport_spec"}, {a1}, {a2}, {a3}, {a4}, {a5}, {a6}, {(pinlist)}
```

### Parameters

|

wvf_set

 |

Waveform Set Number. Enter ALL for all waveform sets, or an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by the command `WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）.

 |
 |

specset_id

 |

Derived as follows:

`100 *` equation_set_no `+ ` specset_no

 |
 |

wavetable_name

 |

The wavetable name. Enter a string of up to 40 alphanumeric characters (upper or lower case) enclosed in double quotes.

 |
 |

multiport_spec

 |

To query a multi-port specification, enter the name of the specification.

 |
 |

a1..a6

 |

Edge action. The actions you can define are:

 |
 |

N

 |

no action

 |
 |

F0N

 |

drive 0, no tri-state action

 |
 |

F1N

 |

drive 1, no tri-state action

 |
 |

FN0

 |

no drive action, tri-state off

 |
 |

FNZ

 |

no drive action, tri-state on

 |
 |

F00

 |

drive 0, tri-state off

 |
 |

F0Z

 |

drive 0, tri-state on

 |
 |

F10

 |

drive 1, tri-state off

 |
 |

F1Z

 |

drive 1, tri-state on

 |
 |

pinlist

 |

The name of the pin or pins for which break waveform definitions are to be made or read back. The symbol @ can be used to specify all configured input and IO pins. If more than one pin is to be included, the names must be separated with a comma.

 |

### Example

```
BWDF 1,N,N,N,F1N,F0N,N,(D0,D1,D2,D3)
```

This example defines a pulse for waveform set 1, and for pins D0 to D3, driving to 1 at edge action 4 and to 0 at edge action 5. The tri-state formatter is not used.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.13_BWDF__BWDF__-__Break_Waveform_DeFinition.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

- waveform_set is greater than the range allowed by the command `WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）.
- There is a mismatch between the edge actions and edge order in the specified waveform.
- A tri-state action is defined or implicitly required on edge 2 or 5.
- specset_id is invalid because equation_set_no, specset_no, or both are invalid, or because specset_id does not reference a defined wavetable.

<!-- 报错节 end -->

## 是什么

**BWDF 定义 break waveform 的动作，一共六个边沿位（`a1` 到 `a6`）。**
**而它最要紧的事实是「已经被替代了」**——原文用一整段 `Note` 交代这件事：

> 「Note This command is replaced by BWDS, BWDS? from release 2.1 onwards when 14-edge setups
> are used. The command will be disabled for pin and waveform sets containing more than 6 edges.
> The query can still be used, but will return only the first 6 edges.」

**这段是三个事实叠在一起**：

| 事实 | 原文 |
|---|---|
| **14-edge setup 要用 [[bwds]] 代替它** | `is replaced by BWDS, BWDS? from release 2.1 onwards when 14-edge setups are used` |
| **超过 6 个 edge 的 pin / waveform set 上，本命令被禁用** | `will be disabled for pin and waveform sets containing more than 6 edges` |
| **但 `BWDF?` 还能用——只回前 6 个 edge** | `The query can still be used, but will return only the first 6 edges` |

**「6」这个数不神秘**：语法里就是 `{a1}` 到 `{a6}` 六个位——
**命令本身写死了六条边沿，所以 7 个以上 edge 的 setup 它接不住。**

**注意三个事实的方向不一样**：写命令是**被禁用**（不是「不推荐」），
查询是**照旧可用但被截断**。**「禁用」的确切后果**（报错？还是被忽略？）**本篇没说**（**语料未写**）。

### break waveform 是什么——**语料未写**

**本篇通篇在用 `break waveform` 这个词，但没有一处定义它。**
本页能拼出来的只有三条**性质**，全部出自本篇开头那一句：

> 「The BWDF (Break Waveform DeFinition) command defines the actions for the break waveform for
> the specified waveform set. Only drive actions are allowed. The break waveform must not
> contain data dependent actions. Edges with delays that are incompatible with the defined
> actions will be auto-corrected to fit.」

| 性质 | 原文 |
|---|---|
| **只许 drive 动作** | `Only drive actions are allowed.` |
| **不许依赖 data 的动作** | `The break waveform must not contain data dependent actions.` |
| **延迟不相容时自动改正** | `Edges with delays that are incompatible with the defined actions will be auto-corrected to fit.` |

**「它什么时候用、为什么叫 break、和普通波形什么关系」——本篇一个字没有。**
（**推断**：从 `## Errors` 那条 `A tri-state action is defined or implicitly required on edge 2
or 5.` 看，第 2 与第 5 个边沿在 break waveform 里有特殊地位；
**但本篇没有一句解释这件事，本页只把报错照记。**）

**第 2 条性质值得单独记一笔**：`Only drive actions are allowed.` 与
`must not contain data dependent actions.` 是**两句、两个限制**——
**「只许 drive」管的是动作的种类，「不许 data dependent」管的是动作的来源。**
**而示例里出现的 `F1N` / `F0N` 正是纯 drive 的取值**（见「典型用法」）。

### 六个位与九种动作

`a1` 到 `a6` 是**边沿动作（Edge action）**，可取值原文列了 9 个
（逐值见上面「语法 / 参数」节的 `a1..a6` 那一栏）：

| 值 | 原文释义 |
|---|---|
| `N` | `no action` |
| `F0N` | `drive 0, no tri-state action` |
| `F1N` | `drive 1, no tri-state action` |
| `FN0` | `no drive action, tri-state off` |
| `FNZ` | `no drive action, tri-state on` |
| `F00` | `drive 0, tri-state off` |
| `F0Z` | `drive 0, tri-state on` |
| `F10` | `drive 1, tri-state off` |
| `F1Z` | `drive 1, tri-state on` |

**和 [[wave]] 的驱动侧取值比一比**（**两张表都在各自页的「语法 / 参数」节里**）：

| | 取值个数 | 有没有 `N`（no action） |
|---|---|---|
| **BWDF 的 `a1..a6`** | **9 个** | **有 `N`** |
| **WAVE 的 `DD1` / `DD2`** | 8 个 | **没有** |

**（推断）**：`N` 是「这一条边沿不做任何事」，**是「边沿位」才有的概念**——
依据是 BWDF 的 `a1` 到 `a6` 每位都必须给一个值（示例里第 1、2、3、6 位全是 `N`），
而 WAVE 的 `DD1` / `DD2` 是**可选**参数（`These are optional parameters`），
**「不填」本身就表达了这个意思。原文没有把这两张表放在一起比过。**

### 「六个位」是位置，不是编号

**`a1` 到 `a6` 是按顺序对应的，不是让你自己填边沿名**——
这从示例的说明就能读出来：`driving to 1 at edge action 4` 指的是**第 4 个位 `a4`**。
**而「第 4 个位对应 cycle 里哪条边沿」本篇没写**——
**它把这件事交给了别处**（**语料未写**，见「出处」）。

### 写与读

| 方向 | 写法 | 回什么 |
|---|---|---|
| **写** | `BWDF {wvf_set}, {a1}, {a2}, {a3}, {a4}, {a5}, {a6}, {(pinlist)}` | — |
| **读** | `BWDF? {wvf_set\|"wavetable_name"\|specset_id\|"multiport_spec"}, {(pinlist)}` | `BWDF {wvf_set\|"wavetable_name"\|specset_id\|"multiport_spec"}, {a1}, {a2}, {a3}, {a4}, {a5}, {a6}, {(pinlist)}` |

> 「The BWDF? query returns the definitions for the current break waveform.」

**`BWDF?` 不带边沿位**——**只能整个读回来，不能指定读第几位**。

**写与读的第一位参数不一样，这是本篇的一处不对称**：
`BWDF?` 的第一位可以写**四种**（号 / wavetable 名 / `specset_id` / multi-port spec），
**而写命令 `BWDF` 只写了 `{wvf_set}` 一种**。
**参数释义里 `specset_id` 与 `wavetable_name` 两条都没有说「只在查询里可用」**——
**这一点和 [[bwds]] 不同**：那一篇明写了 `wavetable_name can only be specified in the query.`
与 `specset_id can only be specified in the query.`
**两篇同一位置的限制写法不一致，本页不替它们统一。**

### `pinlist` 的 `@` 只展开到 input / IO pin

> 「The name of the pin or pins for which break waveform definitions are to be made or read
> back. The symbol @ can be used to specify all configured input and IO pins. If more than one
> pin is to be included, the names must be separated with a comma.」

**`@` 在这里是「所有已配置的 input 与 IO pin」，不是「所有 pin」。**
**[[bwds]] 写的是同一个短语**（`all configured input and IO pins`），
**而 [[wave]] 写的是 `all configured pins`**——**同族命令里 `@` 的展开范围不一致**，
**本页三处照记、不替它统一。**

**另一个「读了才知道」的点**：这一栏的单词是 `read back`，
**说明这就是同一份定义的两半**——`BWDF` 写、`BWDF?` 读，对象是同一个。

## 典型用法

**1. 第一步永远是数边沿**：

| 这条 wave 有几个 edge | 该用什么 |
|---|---|
| **≤ 6 个** | **`BWDF` 可用**（`The command will be disabled for pin and waveform sets containing more than 6 edges.`） |
| **7 到 13 个** | **两篇都没写**（**语料未写**） |
| **≥ 14 个** | **必须换 [[bwds]]**（`when 14-edge setups are used`） |

**注意中间那一段是空的**：本篇给的两个数是 `more than 6` 与 `14-edge`，
**7 到 13 这段归谁管，本篇与 [[bwds]] 都没交代**。

**2. 写**：`BWDF {wvf_set}, {a1}, {a2}, {a3}, {a4}, {a5}, {a6}, {(pinlist)}`
——**六个位一位不能少**，用不到的位写 `N`；**第一个位就是 `a1`，不是 0**。

**3. 原文示例（`## Example`，逐字）——全篇唯一一个例子，而且是写命令**：

```
BWDF 1,N,N,N,F1N,F0N,N,(D0,D1,D2,D3)
```

> 「This example defines a pulse for waveform set 1, and for pins D0 to D3, driving to 1 at
> edge action 4 and to 0 at edge action 5. The tri-state formatter is not used.」

**逐位对一遍**：

| 位 | 值 | 原文怎么说 |
|---|---|---|
| **`a1` `a2` `a3`** | `N,N,N` | 前三个边沿**不做动作** |
| **`a4`** | `F1N` | `driving to 1 at edge action 4` |
| **`a5`** | `F0N` | `driving to 0 at edge action 5` |
| **`a6`** | `N` | 第六个边沿**不做动作** |
| **tri-state 侧** | — | `The tri-state formatter is not used.` ← **对应 `F1N` / `F0N` 里那个 `N`（no tri-state action）** |

**这个例子只用了 9 个动作里的三个（`N` / `F1N` / `F0N`）**——
**`FN0` / `FNZ` / `F00` / `F0Z` / `F10` / `F1Z` 六种在本篇里一个例子都没有。**
**注意它定义的是一条「pulse」**（原文用词），也就是 `a4` 起、`a5` 落。

**4. 回读**：**原文 `## Example` 只示范了写命令，`BWDF?` 一个例子都没有**（**语料未写**）。
按语法行，它的形式是 `BWDF? {wvf_set|"wavetable_name"|specset_id|"multiport_spec"}, {(pinlist)}`。

**5. 出错先看的两条**（`## Errors` 里与内容有关的）：

- **edge 动作与 edge 顺序不搭**：`There is a mismatch between the edge actions and edge order
  in the specified waveform.`
- **第 2 或第 5 个边沿上出现（或隐含需要）tri-state 动作**：
  `A tri-state action is defined or implicitly required on edge 2 or 5.`

**第 2 条和第 3 条性质是同一个话题的两面**：`Only drive actions are allowed.` 是总则，
**这条报错说的就是「哪里最容易违」**——第 2 与第 5 个边沿。

## 和谁有关

- [[bwds]] — **后继命令，本篇 `Note` 段逐字点名**：
  `is replaced by BWDS, BWDS? from release 2.1 onwards when 14-edge setups are used`。
  **这是本页最重要的一条关系**：**BWDF 是「6 个边沿以内」的那条老路，14 个边沿以上由 [[bwds]] 接。**
  **`BWDS` 那一篇的正文里还有反方向的一句**（`This command replaces the command BWDF, BWDF?`）——
  **本页的取材只有 BWDF 这一篇，那一句不在本页的 raw 里**，见「出处」的说明。
- [[wsus]] — **`wvf_set` 的上限来源（前置）**：
  `The maximum number is determined by the command WSUS, WSUS? - (Waveform Sets USed).`
  **`## Errors` 第一条也指着它。**
- [[waveform-set]] — **本页的作用域（同类）**：break waveform 是按 waveform set 定义的
  （正文 `for the specified waveform set`），`wvf_set` 指的就是它。
  **「waveform set 装什么」的正文在那一页，本页没有。**
- [[pclk]] / [[wave]] — **同族姊妹命令（并列）**。
  **本篇一次没提 `PCLK`，也没提 `WAVE`**；
  「同族」的依据是 [[timing]] 阶段页把它们列在同一个 L1 单元里
  `fixed timing 路线：逐个元素定义 edge / period / waveform`（**本页读到的 wiki 页**）。
  **它们与本页的关系只在「同属 fixed timing 的逐元素定义命令」这一层**——
  **`WAVE` 那一边（`DD` / `ED` / data 参数）与 break waveform 是两套东西。**
- [[timing]] — **`stage: timing` 的阶段页**（同上）。
- [[timing-setup-commands]] — **上游入口**。本篇 `## Application` 全文一句：
  > 「Timing Setup, see Timing Setup Commands.」
  **本篇没有说 BWDF 在 timing setup 流程里排第几步。**
- `Timing Setup Commands` 那一篇（**未读**）— 见「出处」。

## 版本

**本文档有 `## Functional changes` 段，段里只有一条**：

- `Introduced before SmarTest 6.3.2`

> **这一条是 §11.2 ② 说的哨兵值，不是「6.3.2 新增了 BWDF」。**
> 措辞是 `before`，意思是「**在本套文档集覆盖范围开始之前就已经有了**」。
> **只可以说：7.10.3 上有它，而且它比 6.3.2 更老** → [[smartest-6.3.2]]。
> **不许把它读成「6.3.2 引入了 BWDF」。**

**而这里有一条该对着看的**：**版本段写的版本号与正文写的版本号不是一套编号**——

| 出处 | 版本号 |
|---|---|
| `## Functional changes` | **`SmarTest 6.3.2`** |
| 正文 `Note` 段 | **`release 2.1`**（本篇）；`release 2.0`（[[bwds]] 那一篇） |

**两套编号怎么对应，本篇一个字没说**（**语料未写**）。
**本页两处并列照记，不替它换算。**

**版本段里没有的东西（照实记，不替它补）**：没有第二条。
**所以「本命令是哪一版被 BWDS 取代的」在本篇里查不到**——
**正文只说 `from release 2.1 onwards`，而那个 `release 2.1` 对应哪个 SmarTest 版本，本篇没有换算。**

## 出处

`sources:` 一篇：

- `02_System_reference/02.06_Command_Reference/02.06.02.02.13_BWDF__BWDF__-__Break_Waveform_DeFinition.md`
  （frontmatter 的 `source_topic` 是 `98497.htm`；**3,796 字节 / 193 行，整篇读完**——
  字节按 `st_size`、行数按 `wc -l`，§11.5 口径）
- 本页的「语法 / 参数」节与「报错条件」节是脚本从这一篇抽的（**本页一个字没动**）。

**本页没做的**：

- **`BWDS` 的 raw 不在本页的 `sources:` 里。** 本页只在「和谁有关」里为对照提过它有一句
  反方向的话（`This command replaces the command BWDF, BWDF?`）——
  **那一句出自 [[bwds]] 那一页的 raw，本页按「读到的另一篇」标注，不作为本页的取材。**
  **所以「14-edge setup 上怎么定义 break waveform」本页只有本篇 `Note` 段那一句。**
- **`WSUS` / `WAVE` / `PCLK` 三篇都没读。** 上面「9 个 vs 8 个动作」「`@` 展开范围」两处对照，
  **依据是各自页的「语法 / 参数」节（本页读到的 wiki 页），不是本页的 raw。**
- **`Timing Setup Commands` 那一篇没读。** 本篇 `## Application` 只给了它的标题。
- **真正的 break waveform 语义没有第二处来源。** 本篇与 [[bwds]] 是语料里唯一两篇讲它的，
  **而两篇都不定义它**——**「break 是什么意思、什么测试会用到、第 4 个位对应哪条边沿」
  本页答不了（语料未写）。**
- **图 0 张。** 实测 `![` / `<img` / `.png` / `.jpg` / `.gif` / `raw/` 六种写法在本篇
  **全部 0 命中**。**所以本页没有任何来自图的结论**——
  **「一条 pulse 的六个位长什么样」本页只有文字（§11.4）。**
- **没在机台上跑过 `BWDF` / `BWDF?`**（`verified: doc-only`）。
  **所以「超过 6 个 edge 时它是报错还是被忽略」本页答不了（§11）。**
- **本篇没有 `## Warnings` 段**，所以「报错条件」节里只有 `## Errors` 的四条——不是漏写。

### §10 重复投放：本篇在语料里有**三份**（本页查过）

| 路径 | `source_topic` | 字节 | 与**本页这一份**的正文 |
|---|---|---|---|
| `02.06_Command_Reference/02.06.02.02.13_BWDF__BWDF__-__Break_Waveform_DeFinition.md`（**本页的出处**） | `98497.htm` | 3,796 | — |
| `02.06_Command_Reference/02.06.06.02.02_BWDF__BWDF__-__Break_Waveform_DeFinition.md` | `98497_2.htm` | 3,798 | **把篇内相对链接的前缀归一化后，`diff` 报 0 行差异** |
| `02.08_Setup_and_Result_Tools/02.08.04.34.02.02.02_BWDF__BWDF__-__Break_Waveform_DeFinition.md` | `98497_3.htm` | 3,971 | **同上——0 行差异** |

**三份的差别只有两处**：① frontmatter 的 `source_topic` / `source_html`；
② **篇内相对链接的前缀**（第三份多一层 `../02.06_Command_Reference/`，字节数差的就是它）。
**本页的结论全部只来自第一份**；另两份只核了 frontmatter、字节数与 `diff` 行数，
**没有读它们的正文**（§12 不越取材边界）。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
> **① `Note` 后面没有标点。** 原文是 `Note This command is replaced by BWDS, BWDS? from
> release 2.1 onwards when 14-edge setups are used.`——**`Note` 与 `This` 之间只有一个空格**，
> 没有句点也没有冒号。**本页正文引了这一整句，照抄。**
> **② 链接被拆成了三段，其中一段的链接文字就是 `, `（逗号加一个空格）。**
> 原文那一处是**三个首尾相连的 markdown 链接**，目标都是同一篇 BWDS，
> **三段链接文字依次是 `BWDS`、`, `、`BWDS?`**——**所以「读成文字」之后才是 `BWDS, BWDS?`。**
> **这种拆法在本篇出现 1 次，在 [[bwds]] 那一篇也出现 1 次**（见「和谁有关」）。
> **本页引这一句时按 §11.1 ② 剥离链接标记后的文字引**（剥完那一句是连续的，见正文）。
> **③ 两套版本编号并存。** 正文写 `release 2.1`（`from release 2.1 onwards`），
> 而 `## Functional changes` 写的是 `SmarTest 6.3.2`——**同一篇里两套编号，本篇不换算。**
> **④ 同一条报错在两篇里带不带限定不一样。** 本篇写的是
> `A tri-state action is defined or implicitly required on edge 2 or 5.`，
> 而 [[bwds]] 那一篇的同一句多了一个限定：`(only for P/C/Ce systems)`
> ——**两条报错文本一模一样，只有括号那一截不同。本页两处照记，不替它们统一。**
> **⑤ 报错段的第一条把参数名写成 `waveform_set`，语法与参数释义里写的是 `wvf_set`。**
> 原文逐字：`waveform_set is greater than the range allowed by the command WSUS, WSUS? - (Waveform Sets USed).`
> ——**同一篇里同一个参数两个名字，本页不替它统一。**
> **⑥ 坏字：本篇 0 个。** 照 §11.2 ① 那条判据（**英文文档里出现任何汉字，都是坏字**）逐字查过：
> **本篇一个汉字都没有**——**但这是「本页读到的」，不是「本篇没有」**（§13.1：没找到 ≠ 没有）。

`verified: doc-only`
