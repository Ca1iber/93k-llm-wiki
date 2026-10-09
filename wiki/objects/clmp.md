---
type: object
title: CLMP, CLMP? - (CLaMP level)
layer: L1
stage: level
tags: [level, clamp, command, l1, pin, level-set, equation-based-level-setup, pin-scale-800, pin-scale-3600, pin-scale-9g]
related: [level, term, pin, dscp, dfgp, psfc, setup-level-set-0, site-focus-required-before-command, command-reference, dcdt]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.26_CLMP__CLMP__-__CLaMP_level.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# CLMP, CLMP? - (CLaMP level)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **2,527 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.26_CLMP__CLMP__-__CLaMP_level.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### CLMP

```
CLMP {level_set|level_set_id}, [clamp_mode], [low_clamp_level], [high_clamp_level], {(pinlist)}
```

### CLMP?

```
CLMP? {level_set|level_set_id}, {(pinlist)}
```

returns:

```
CLMP {level_set|level_set_id}, [clamp_mode], [low_clamp_level], [high_clamp_level], {(pinlist)}
```

### Parameters

|

level_set

 |

The identification number of the level set in which you want the levels to be included. The number must not exceed the maximum number of level sets allowed (as defined by the DSCP command). Specifying ALL sets the clamp levels for all existing level sets (except level set 0). Specifying PRM sets the clamp levels for the primary level set.

Standard level sets have a number > 0. Level set 0 is a dedicated level set for the high-Z state of digital pins. For more information see `Defining a level set for sequencer state OFF`（raw: `02.06.05.01.05.05_Controlling_high-Z_behavior_of_digital_pins_while_the_sequencers_are_OFF.md`）.

 |
 |

level_set_id

 |

Used in equation based level setup. It is derived as follows:

100000 * equation_set_no + 1000 * specset_no + level_set_no

Note that if you use the command for an equation based level setup, you modify only the runtime values, not the value in the level set.

 |
 |

clamp_mode

 |

ON | OFF

For the Pin Scale 3600, the clamps can be set to ON when std/fast mode is set to std, and termination mode is set to OFF or A (active load).

Pin Scale 9G cards do not have clamps. Setting clamp levels will be ignored.

For termination mode, see `TERM, TERM? - (TERMination mode)`（raw: `02.06.02.02.257_TERM__TERM__-__TERMination_mode.md`）.

 |
 |

low_clamp_level

 |

An integer (in mV) which sets the low clamp level.

For the Pin Scale 800, the range is -1800 to 6800. At power-on this parameter assumes a default value of -250.

 |
 |

high_clamp_level

 |

An integer (in mV) which sets the high clamp level. For the Pin Scale 800, the range is -1800 to 6800, and the difference of high_clamp_level - low_clamp_level must be in the range 0 to 8.6 V.

 |
 |

pinlist

 |

The name of the pins for which the clamp levels are to be set. This parameter can also include groups previously created by the DFGP (DeFine GrouP) command. If more than one pin is to be included, the names must be separated by a comma. The symbol @ refers to all pins. You can include O and IO pin types in pinlist.

 |

### Example

```
CLMP 1,ON,-10,5100,(Q0,Q1,Q2,Q3)
```

This example sets the clamp levels for level set 1 for pins Q0, Q1, Q2 and Q3. The low clamp level is set to -10 mV, and the high clamp level is set to 5100 mV.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.26_CLMP__CLMP__-__CLaMP_level.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

- The high or low clamp level is out of range.
- The swing limitations are exceeded.
- The set number is out of range.
- The set number is out of the range defined by the DSCP command.
- The set number is out of the used range of sets (CLMP? only).

<!-- 报错节 end -->

## 是什么

**`CLMP` 是 level 段里「钳位」那一条命令。** 它一条命令管三件事：
**钳位的开与关**（`clamp_mode`）、**钳位的高/低压**（`low_clamp_level` / `high_clamp_level`）、
以及**这些定义写进哪一个 level set**。原文第一句把这个范围说全了：

> 「The CLMP(CLaMP level) command defines the low and the high clamp voltage levels and switches the clamp on and off for the specified pins. These levels are included in the level set you specify.」

**查询侧只回答「现在是什么」**：

> 「The CLMP? query returns the actual clamp levels of the level set and pins specified, as well as the clamp mode (on|off).」

原文用的是 `actual` 这个词。（推断）**`CLMP?` 读回的应当是「当前生效值」，不是「你上次写的值」**——
依据是 `actual` 这个词，以及下面 equation-based 那条「只改运行期值、不改 set 里的值」的对照。
**本篇没有一句话挑明这个区别，所以这里是推断，不是文档事实。**

### 一条运行期前提：setup 焦点（**两段话，一段管写、一段管读**）

> 「With this command you configure setups of those sites that have the setup focus: For more information, see also: PSFC, PSFC?.」

> 「With this command you can retrieve site specific information (only one site can be in focus at a time). For the site in focus, SmarTest displays results in the Testflow Editor and in the result tools. Also, any firmware queries report setup and results for the site currently in focus only.」

**第一段管「写」，第二段管「读」**：`CLMP` 配置的是**当前有 setup 焦点的那些 site**；
`CLMP?` 与任何 firmware 查询报告的也**只有焦点 site**。
设焦点的动作，文档把读者指到 `PSFC, PSFC?` 那一篇（**本页没读**，见 `## 出处`）。
**「先设焦点、再发命令」这条前置本页不展开。**

### 写进哪个 level set：三个取值 + 两条边界

原文（参数 `level_set` 那一格）：

> 「The identification number of the level set in which you want the levels to be included. The number must not exceed the maximum number of level sets allowed (as defined by the DSCP command). Specifying ALL sets the clamp levels for all existing level sets (except level set 0). Specifying PRM sets the clamp levels for the primary level set.」

| 你写的 | 结果（原文） |
|---|---|
| 一个普通编号 | 写进这一个 level set |
| `ALL` | 「Specifying ALL sets the clamp levels for all existing level sets (except level set 0).」 |
| `PRM` | 「Specifying PRM sets the clamp levels for the primary level set.」 |

**两条边界，都是文档事实：**

- **上限只看 `DSCP`**：本文档写的上限来源**只有 `DSCP` 一条**（`as defined by the DSCP command`），
  **没有提 `LSUS`**。`DSCP` 在正文里是个**纯文本名字**，**原文没有给它链接**。
- **level set 0 不受 `ALL` 管**（逐字：`except level set 0`），而且它是专用的：

> 「Standard level sets have a number > 0. Level set 0 is a dedicated level set for the high-Z state of digital pins.」

  同一格还把读者指到 `Defining a level set for sequencer state OFF`
  （raw: `02.06.05.01.05.05_Controlling_high-Z_behavior_of_digital_pins_while_the_sequencers_are_OFF.md`，**本页没读**）。

### equation based level setup：多一条 ID 算法，也多一条「只改运行期」

`level_set_id` 那一格给的算法是（**逐字**）：

> `100000 * equation_set_no + 1000 * specset_no + level_set_no`

**并且这个 ID 下写进去的只是运行期值**：

> 「Note that if you use the command for an equation based level setup, you modify only the runtime values, not the value in the level set.」

**同一件事本篇说了两遍，措辞不同**：正文开头那次写的是
`In connection with equation based timing, note that CLMP only changes the runtime values, not the setup values specified in the level set.`
——**一处说 `equation based timing`、另一处说 `equation based level setup`**（见 `## 出处` ⚠️③）。

### 三张卡、三套说法（**本页最该先看的一张表**）

`clamp_mode` 与两个 clamp level 三格加起来点了三张卡，每张说的话都不一样：

| 卡片（原文写法） | 原文 | 含义 |
|---|---|---|
| `Pin Scale 3600` | 「For the Pin Scale 3600, the clamps can be set to ON when std/fast mode is set to std, and termination mode is set to OFF or A (active load).」 | **开钳位有前置**：std/fast 模式要是 `std`，终结模式要是 `OFF` 或 `A` |
| `Pin Scale 9G` | 「Pin Scale 9G cards do not have clamps. Setting clamp levels will be ignored.」 | **这张卡根本没有钳位**；写了**不报错，是被忽略** |
| `Pin Scale 800` | 「For the Pin Scale 800, the range is -1800 to 6800. At power-on this parameter assumes a default value of -250.」 | **只有它给了范围与上电默认值** |

**`clamp_mode` 的全部取值就是 `ON | OFF` 这一行**，没有第三种。
这一格还把读者指到终结模式那一篇：

> 「For termination mode, see TERM, TERM? - (TERMination mode).」

→ [[term]]。

### 电压范围与「差值」那条约束

| 参数 | 单位与范围（原文） |
|---|---|
| `low_clamp_level` | 「An integer (in mV) which sets the low clamp level.」范围与默认值：`-1800 to 6800`（Pin Scale 800）；**上电默认 `-250`** |
| `high_clamp_level` | 「An integer (in mV) which sets the high clamp level.」范围同为 `-1800 to 6800`；**另有差值约束**：`the difference of high_clamp_level - low_clamp_level must be in the range 0 to 8.6 V` |

**两处要停一下：**

- **单位混用**：两个 clamp level 都以 **mV** 计（`-1800 to 6800`），
  而同一句里的差值上限写的是 **`8.6 V`**。
- （推断）**那条差值约束在数值上等于「两端各自落在范围内」**：
  `6800 - (-1800) = 8600 mV`，正好是 `8.6 V`。
  **依据是这三个数之间的算术关系**——**原文没有一句话这么说**，所以这是推断。

**范围与默认值只给了 `Pin Scale 800` 一张卡**；另外两张卡的钳位电压范围，本篇一个字没有。

### `pinlist`：什么 pin 能用、怎么写

> 「The name of the pins for which the clamp levels are to be set. This parameter can also include groups previously created by the DFGP (DeFine GrouP) command. If more than one pin is to be included, the names must be separated by a comma. The symbol @ refers to all pins. You can include O and IO pin types in pinlist.」

**四件事**：① 可以用 `DFGP` 建的组（**原文没给 `DFGP` 链接**）；② 多个名字用逗号分隔；
③ `@` 代表全部 pin；④ **只有 `O` 与 `IO` 两种 pin 类型能进 `pinlist`**。

### 报错五条，按对象只有两类

`## Errors` 五条（逐字见本页「报错条件」节）**按对象分只有两类**：
**电平/摆幅越界**（`The high or low clamp level is out of range.` 与 `The swing limitations are exceeded.`）
和 **set 号越界**（另三条，两条点名 `DSCP`，一条只在 `CLMP?` 上出现）。

⚠️ **`swing` 那一条本篇解释不了**：报错写 `The swing limitations are exceeded.`，
而**本篇没有一处说明 `swing` 是什么、上限是多少**（见 `## 出处` ⚠️④）。
**所以「摆幅上限是多少」在本篇是语料未写**，要答只能去卡规格那一侧查。

## 典型用法

**先说范围**：这一篇**没有 `## Procedure`，也没有 `## Before you begin`**。
唯一的过程线索是 `## Application`：

> 「Level Setup, see Level Setup Commands.」

**即：它归属 level setup 那一章**（`Level Setup Commands` 那篇**本页没读**，
所以「这条命令在流程里排第几步」本页不写）。

**原文只给了 1 个例子，而且是 `CLMP` 的；`CLMP?` 一个例子都没有。**

| 命令 | 原文的说明 |
|---|---|
| `CLMP 1,ON,-10,5100,(Q0,Q1,Q2,Q3)` | 「This example sets the clamp levels for level set 1 for pins Q0, Q1, Q2 and Q3. The low clamp level is set to -10 mV, and the high clamp level is set to 5100 mV.」 |

**1. 五个位置各是什么**（**按语法式的括号拼的，原文没有对应的分步说明**）：

| 位置 | 是什么 | 能不能省 |
|---|---|---|
| 第 1 个 | `{level_set\|level_set_id}` | **不能省**（原文用花括号，不是方括号） |
| 第 2 个 | `[clamp_mode]` = `ON` / `OFF` | 可省（方括号） |
| 第 3 个 | `[low_clamp_level]`，整数，单位 mV | 可省 |
| 第 4 个 | `[high_clamp_level]`，整数，单位 mV | 可省 |
| 末尾括号 | `{(pinlist)}`，逗号分隔、可用 `DFGP` 组、`@` = 全部、只收 `O`/`IO` | **括号本身也带花括号**，原文没说省略它会怎样 |

**例子逐位对得上**：`1` = level set 1、`ON` = 开钳位、`-10` = 低压、`5100` = 高压、
`(Q0,Q1,Q2,Q3)` = 四个 pin。

**2. 查询**

`CLMP? {level_set|level_set_id}, {(pinlist)}`，
返回**与 `CLMP` 同形**的式子（含 `[clamp_mode]`、`[low_clamp_level]`、`[high_clamp_level]`），
**原文说它返回的是 `actual` 值**（见「是什么」）。

**3. 三种常见用法**

- **给一批 pin 开钳位** → 第 2 位写 `ON`，并给出两个电平（例子就是这样）。
- **整批统一** → `level_set` 写 `ALL`（**绕开 set 0**）或 `PRM`（只改 primary set）。
- **不重写、只核对** → 用 `CLMP?` 读回 `actual` 值。

**4. 一条省事的用法来自 `pinlist` 那一格**：**用 `DFGP` 建过的 pin 组可以直接写进 `pinlist`**，
不必把 pin 一个个列出来。

## 和谁有关

| 页 | 是什么关系 | 依据 |
|---|---|---|
| [[level]] | **本页 `stage: level` 的理由**：它写的是 level 段里的钳位配置 | frontmatter + 本篇 `## Application` |
| [[term]] | **姊妹命令**：本文档在 `clamp_mode` 那一格里把读者指过去——「For termination mode, see TERM, TERM? - (TERMination mode).」 | 本篇参数节 |
| [[psfc]] | **运行期前置**：`CLMP` 只配置「有 setup 焦点」的 site，文档把设焦点指到这页 | 本篇正文（逐字引在「是什么」） |
| [[site-focus-required-before-command]] | 上面那条前提的 constraint 页 | 同一条文档事实的归属页 |
| [[dscp]] | **上限来源**：level set 的上限「as defined by the DSCP command」——**原文没给链接** | 本篇参数节 |
| [[dfgp]] | **pinlist 的来源之一**：可以写 `DFGP` 建过的组——**原文没给链接** | 本篇参数节 |
| [[setup-level-set-0]] | **专用 set**：level set 0 是 digital pins 在 high-Z 时的专用 set，`ALL` 也绕过它 | 本篇参数节 |
| [[pin]] | **前置**：`pinlist` 只收 `O` 与 `IO` 两种 pin 类型 | 本篇参数节 |
| [[command-reference]] | **所属章**（`02.06_Command_Reference` / `02.06.02.02`） | 路径 |
| [[dcdt]] | **同批另建的相邻命令页**（`02.06.02.02.41`）；**本篇一个字都没提它**，关系只是并列 | 路径；**本页不声称任何内容上的关系** |
| `PSFC, PSFC?`（raw: `02.06.02.02.191_PSFC__PSFC__-__Parallel_Setup_FoCus.md`） | **本页没读**（见 `## 出处`）。正文里只写了 `PSFC, PSFC?` 这六个字符，**全名只在路径里**（见 `## 出处` ⚠️⑦） | 本篇正文 |
| `Defining a level set for sequencer state OFF`（raw: `02.06.05.01.05.05_Controlling_high-Z_behavior_of_digital_pins_while_the_sequencers_are_OFF.md`） | **本页没读** | 本篇参数节 |
| `Level Setup Commands`（raw: `02.06.05_Level_Setup_Commands.md`） | **本页没读**——「命令在流程里的位置」在那篇 | 本篇 `## Application` |
| `Pin Scale 3600` / `Pin Scale 9G` / `Pin Scale 800`（**均未建，不链**） | **三条卡片限制的载体**（见「是什么」那张表） | 本篇参数节 |
| `TERM, TERM? - (TERMination mode)`（raw: `02.06.02.02.257_TERM__TERM__-__TERMination_mode.md`） | 见上面的 [[term]] 一行；**本页没读它的 raw** | 本篇参数节 |

**本页没有引用 `edges.jsonl` 的入边/出边数字**（没读边数据，故不报条数）。

## 版本

**本文档没有 `## Functional changes` 段。**

**所以本页一个版本号都没有**：`CLMP` / `CLMP?` 是哪个 SmarTest 版本引入的、
三张卡的限制是哪一版加的、`level_set_id` 的 ID 方案是哪一版定的——**本篇全无记载**。

**一条量过的事实**：本篇全文 **0 处出现 `SmarTest` 这个词**，
**也 0 处出现 `Introduced` 那种哨兵值行**（§11.2 ②）。
（推断）**因此不能从本篇反推 `CLMP` 的引入版本**——
依据就是这两个「0 处」，**不是「它看起来像老命令」这种印象**。

**该去查**：同章相邻命令篇的 `## Functional changes`（**本页没查**）。

## 出处

`sources:` 一篇：
`02_System_reference/02.06_Command_Reference/02.06.02.02.26_CLMP__CLMP__-__CLaMP_level.md`
（TDC `98505.htm`；**4,440 字节 / 127 行**，全文 CRLF，末行带换行。
**本节的行数口径是 `wc -l`（= `splitlines()`），不加 1**，见 §11.5）。**整篇读完。**

**本页没做的**：

- **原文链到的四篇一篇都没读**：`PSFC, PSFC?`（`02.06.02.02.191`）、
  `TERM, TERM? - (TERMination mode)`（`02.06.02.02.257`）、
  `Defining a level set for sequencer state OFF`（`02.06.05.01.05.05`）、
  `Level Setup Commands`（`02.06.05`）。
  **所以「怎么设 setup 焦点」「终结模式与钳位怎么配合」「level set 0 怎么用」
  「这条命令在流程里排第几步」——本页一个字都没有**，它们都在这四篇里。
- **`DSCP` 与 `DFGP` 在正文里被点名，但原文没给链接**，**本页也没读那两篇**。
  所以「`DSCP` 允许的最大 level set 数是多少」本页答不了。
- **图一张没看——因为这一篇里没有图**（全文 **0 处** `.png` / `.jpg` / `raw/`）。
  **所以本页没有任何来自图的结论**；这与「图够不着」不是一回事（§11.4）。
- **没有 `## Procedure` / `## Before you begin` 可读**，
  所以「典型用法」那一节的五个位置表是**本页按语法式的括号拼的**，不是文档给的流程。
- **没有 `## Functional changes` 段**，所以本页没有任何版本信息（见「版本」）。
- **没有用 `edges.jsonl`**，故不报入边/出边条数。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> ① **一句话里两个冒号，且第二个冒号后面接的是一个「命令名, 命令?」的提问式名字**：
> 「With this command you configure setups of those sites that have the setup focus: For more information, see also: PSFC, PSFC?.」
> ——`focus:` 后面接大写的 `For`，`also:` 后面接 `PSFC, PSFC?.`。**照原样引，没动标点。**
> ② **报错里的名字与参数表的名字不一致**：`## Errors` 三条写的是
> `The set number is out of range.` / `The set number is out of the range defined by the DSCP command.` /
> `The set number is out of the used range of sets (CLMP? only).` ——**称的是 `the set number`**；
> 而 `## Parameters` 里那个参数叫 **`level_set`**（**不是 `level_set_no`**）。
> **同一个东西两个名字，本篇没说它们是一回事。**
> ③ **同一件事的两处措辞不一致**：正文写
> `In connection with equation based timing, note that CLMP only changes the runtime values, not the setup values specified in the level set.`，
> 而 `level_set_id` 那一格写
> `Note that if you use the command for an equation based level setup, you modify only the runtime values, not the value in the level set.`
> ——**`equation based timing` 对 `equation based level setup`**。
> **这是一条 level 命令，本篇不替它裁定哪个对。**
> ④ **`swing` 未定义**：报错第二条是 `The swing limitations are exceeded.`，
> **本篇没有任何一处说明 `swing` 是什么、上限多少**。
> ⑤ **单位混用**：两个 clamp level 都写 mV（`the range is -1800 to 6800`），
> 而同一格的差值上限写 `the difference of high_clamp_level - low_clamp_level must be in the range 0 to 8.6 V`
> ——**`mV` 与 `V` 混在一句里**。
> ⑥ **三张卡三种命名方式**：`Pin Scale 3600` / `Pin Scale 9G` / `Pin Scale 800`——
> **`9G` 不跟 `NNNN` 的数字形式**，且三张卡分别散在三格里。
> ⑦ **正文只写 `PSFC, PSFC?`，全名只在链接路径里**：路径是
> `02.06.02.02.191_PSFC__PSFC__-__Parallel_Setup_FoCus.md`，里面写的是 **`FoCus`**
> （大小写不统一）。**正文可见的那六个字符一个字都没展开。**
> ⑧ **命令名与括号之间没有空格**：原文第一句是 `The CLMP(CLaMP level) command`——
> **`CLMP` 与 `(` 之间无空格**。（对照同批另建的 `02.06.02.02.41` DCDT 篇，
> 那一篇写的是 `The DCDT (Device Cycle DefaulT) command`，**有空格**；
> **两处本页都照原样引，没替谁补空格。**）
> ⑨ **本篇没有坏字**：实测 **0 处非 ASCII 字符**（没有 `鈥` / `渭` / `碌` 那一族）。
> **但这是「本页量过的」，判据只是这一个文件**；§11.2 ① 那族在别的篇里大量存在。

`verified: doc-only`——**本页没有在任何真实机台上发过 `CLMP`，也没有验证过任何钳位电平与那三张卡的限制**
（§11：文档里有 ≠ 这台机器上能用；尤其 `Pin Scale 9G` 那句 `Setting clamp levels will be ignored.`，
**动手前先照实机核对**）。
