---
type: object
title: TERM, TERM? - (TERMination mode)
layer: L1
stage: level
tags: [level, termination, pin, ps1600, ps5000, dc-scale, command, l1]
related: [level, pin, psfc, spst, clmp, lsus, dscp, setup-level-set-0]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.257_TERM__TERM__-__TERMination_mode.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# TERM, TERM? - (TERMination mode)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,736 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.257_TERM__TERM__-__TERMination_mode.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### TERM

```
TERM {level_set_no | level_set_id}, [term_mode], [term_pulldown,] [param_1], [param_2], [param_3],
 [l_range], [h_range], [hr_mode,] {(pinlist)}
```

### TERM?

```
TERM? {level_set_no | level_set_id}, {(pinlist)}
```

returns:

```
TERM {level_set_no | level_set_id}, {term_mode}, [term_pulldown,] [param_1], [param_2], [param_3],
 [l_range], [h_range], [hr_mode,] {(pinlist)}
```

### Parameters

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98771.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：10 行 × 2 列。
> 首行（上游原文）：level_set_no | The identification number of the level set in which you want the definitions to be included. The number must not exceed the maximum number of lev…
> 表内引用（3 条，供检索）：`DSCP`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md`） · `LSUS`（raw: `02.06.02.02.155_LSUS__LSUS__-__Level_Sets_USed.md`） · `Defining a level set for sequencer state OFF`（raw: `02.06.05.01.05.05_Controlling_high-Z_behavior_of_digital_pins_while_the_sequencers_are_OFF.md`）

### Example 1

```
TERM 1,T,-1500,,,,,(Q1)
```

This example terminates the output pin Q1 to -1500 mV in level set 1.

### Example 2

```
TERM 3,A,3000,1500,1000,I3E4,I3E4,(out)
```

This example sets the active load level of the pin group out to 3V, and sets Iol and Ioh current to 1.5 and 1.0 mA respectively. The 0 to 30 mA range is used for both the low and the high range.

### Example 3

```
TERM 1,CT,2000,,,,,(o1,o1-)
```

This example terminates the differential output pair (the o1 and o1- pins) to 2000 mV with center tap termination in level set 1.

### Example 4

```
TERM 1,OFF,PULLDOWN,,,,,,(Q1,Q2)
```

On a PS1600 card, this example switches on the pulldown resistor on the specified pins.

```
TERM 1,OFF,NONE,,,,,,(Q1,Q2)
```

On a PS1600 card, this example switches off the pulldown resistor on the specified pins.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.257_TERM__TERM__-__TERMination_mode.md>` 的 `## Errors`、`## Warnings` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

- You use the wrong current range for the selected current.
- You use an incorrect parameter combination.
- You use too many parameters for the selected mode.
- The clamp voltage is out of range.
- The active load voltage is out of range.
- The active load current is out of range.
- The termination voltage is out of range.
- The low level voltage is higher than the high level voltage in clamp mode.
- You use the termination mode H or L for an o pin. Use the termination mode T.
- Parameter hr_mode is used for instruments other than AVI64.

### Warnings

A warning is generated if:

- Auto-correction of high or low level clamp voltage occurs.
- The range is auto-corrected due to an incompatible range and current combination.
- You enter too many parameters for the selected termination mode (see the table above).

<!-- 报错节 end -->

## 是什么

**`TERM` 设定 output 与 IO pin 的终结模式（termination mode）。**

> 「The TERM command sets the termination mode for the output and IO pins.」

**它一条命令同时管三件事**：pin 的终结方式（`term_mode`）、终结/钳位/主动负载的**电压电流值**
（`param_1`–`param_3`、`l_range`、`h_range`）、以及**这些定义写进哪一个 level set**。
**它管的是「终结」，不是「驱动电平」**——驱动电平属于 level 那一段的其它命令，本页不写。

### 它按「站点焦点」写配置（**一条运行期前提**）

> 「With this command you configure setups of those sites that have the setup focus」

> 「With this command you can retrieve site specific information (only one site can be in focus at a time).」

> 「Also, any firmware queries report setup and results for the site currently in focus only.」

**三句合起来是一件事**：`TERM` 写的、`TERM?` 读的，**都只针对「当前有 setup 焦点的那一个 site」**。
文档把读者指到 [[psfc]]（`PSFC, PSFC?`）去设焦点；
**「先设焦点、再发命令」这条前置本页不展开**，它在 [[psfc]] 与
[[site-focus-required-before-command]] 里。

### 写进哪个 level set：三条取值规则 + 两条硬边界

参数节对 `level_set_no` 的原文是：

> 「The identification number of the level set in which you want the definitions to be included. The number must not exceed the maximum number of level sets allowed (as defined by DSCP) and the level sets used (as defined by LSUS).」

| 你写的 | 结果（原文） |
|---|---|
| 一个普通编号 | 写进这一个 level set |
| `ALL` | 「Entering ALL in this field sets the termination mode for all existing level sets (except level set 0).」 |
| `PRM` | 「Entering PRM in this field defines the termination mode for the primary level set.」 |

**两条硬边界，都是文档事实：**

- **上限是双重的**：既要 ≤ `DSCP` 允许的**最大**数，也要 ≤ `LSUS` 定义的**已用**数——
  即「**这个 level set 得先存在**」。这是**运行期状态**上的前提，不是书写顺序；
  两条上限各自的出处见 [[dscp]] 与 [[lsus]]。
- **level set 0 不受 `ALL` 管**（上面 `ALL` 那句逐字写着 `except level set 0`），
  而且它是专用的：
  > 「Level set 0 is a dedicated level set for digital pins in high-Z state.」
  同段还写了「Level set 0 only supports the termination modes OFF (the default), T, C, and A.」——
  **即 0 号 set 上只有这四种模式**。更细的用法，文档把读者指到
  `Defining a level set for sequencer state OFF`（raw: `02.06.05.01.05.05_Controlling_high-Z_behavior_of_digital_pins_while_the_sequencers_are_OFF.md`，**本页没读**）。

### 模式与参数是**联合**的，不是自由组合

> 「The termination mode has dependencies to pin types and to the parameters (term_pulldown and param_1 to param_3 - see the syntax). The allowed combinations are shown in the Termination modes table, below.」

**这句是本命令的核心**：`term_mode` 决定**哪些 `param_*` 有意义**，也决定**哪些 pin 类型能用**。
**组合不对不是「多余参数被忽略」，而是报错**（见 `## 报错条件`，那里列了 10 条）。

### 全部终结模式一张表

**依据是原文 `## Termination modes` 一节**（那一节的表**不在本页的「语法 / 参数」节里**——
脚本只收 `Syntax` / `Parameters` / `Example` 这类**段标记**下面的内容，
`## Termination modes` 不在其中。要看原表回 raw 那一节）。
**下表是转述，引号里的短句是逐字。**

| `term_mode` | 做什么 | pin 类型 | 用到的参数 |
|---|---|---|---|
| `OFF` | 「Off」 | `o, io` | — |
| `OFF,PULLDOWN` | 「PS1600 and PS5000 only: To switch on the pulldown resistor, use OFF,PULLDOWN」 | `i, o, io` | — |
| `OFF,NONE` | 「PS1600 only: To switch off the pulldown resistor, use OFF,NONE」 | `i, o, io` | — |
| `DIFHIZ` | 「High-impedance unterminated differential receiver」 | `o, io` | — |
| `DIFHIZ,PULLDOWN` | 「PS1600 only: To switch on the pulldown resistor, use DIFHIZ,PULLDOWN」 | 表中该行空白 | — |
| `DIFHIZ,NONE` | 「PS1600 only: To switch off the pulldown resistor, use DIFHIZ,NONE」 | 表中该行空白 | — |
| `T` | 「Terminated with the specified voltage:」 | `o, io` | `param_1` 终结电压 |
| `H` | 「High terminated (by driver).」 | `io` | — |
| `L` | 「Low terminated (by driver).」 | `io` | — |
| `A` | 「Active load.」 | `o, io` | `param_1` 换向电压、`param_2` Iol、`param_3` Ioh、`l_range`、`h_range` |
| `CT` | 「Differential receiver center tap termination with the specified termination voltage.」 | `o, io` | 表里 `param_2`/`param_3` 都写「Not currently supported.」（**与同一行的说明句矛盾，见 `## 出处`**） |
| `XSE` | 「Single-ended cross-termination」 | `o` | — |
| `X` | 「Cross-termination」，并注明「Currently not in use.」 | `o` | — |
| `C` | 「Clamp.」 | `o, io` | `param_1` 钳位低、`param_2` 钳位高 |

**下面五条是表里读快了一定会漏的细节。**

#### `T` 在 `o` 与 `io` 上是两套机制

> 「For the o pin: The driver is used for the termination.」

> 「For io pin: The third level of the driver is used for the termination.」

并且 io 那一侧还带一句限制：
「For io pin the driver output is the third level, only while high-Z is specified for the driver.」

#### `H` / `L` 的三条反直觉行为

> 「term_mode=H (or L) does not control the driver; you have to drive a 1 in order to terminate with vih (or you have to drive a 0 in order to terminate with vil).」

> 「The driver is never set to high-Z in term_mode=H (or L), even if it is specified.」

**配套报错**：`H`/`L` 用在 `o` pin 上直接报错——「You use the termination mode H or L for an o pin. Use the termination mode T.」

#### `A`（主动负载）的两条卡片限制

> 「For io pin, the active load is enabled, only while the driver is set to high-Z. The active load is set to high-Z while the driver is set to logic 1 or 0.」

> 「Pin Scale 5000: Active load and highZ is not available in fast mode.」

**第三条限制在 `l_range` 那一项里**：「This parameter is not supported for AVI64.」

#### `CT` 是「终结 + 切接收器」两件事

> 「CT is also used to switch to differential receiver (comparator/capture) from single-ended receivers.」

> 「The power-on default value of param_2 (swing) is 3.2 V, and the power-on default value of param_3 (offset) is 1.2 V.」

**后一句与同一行表里的参数栏打架**（表里写 `Not currently supported.`）——见 `## 出处` 的 ⚠️。

#### `C` 是**覆盖**语义，不是叠加

> 「Note that this sets clamps as termination mode of the specified pins. Only the latest setting of term_mode for the specified pins is used. To use both the clamps and termination, or to set clamps independently from termination mode, use the CLMP command.」

**所以 `C` 与其它终结模式是「后者覆盖前者」**：
一个 pin 上只有**最后一条** `term_mode` 算数。
**要钳位与终结并存，得改走 [[clmp]]**——文档明写了这条路。

### 参数的单位（**原文在这里自相矛盾**）

| 参数 | 单位（原文） |
|---|---|
| `param_1` | 「The units are mV.」——终结电压 / 主动负载换向电压 / 钳位低电压 |
| `param_2` | 正文写「The units are mA or mV respectively.」，**紧接着的项目符号却写**「the active load Iol current in 碌A,」 |
| `param_3` | 「The units are 碌A.」（`term_mode = A` 的 Ioh）/ mV（`CT` 与 `bidir_receiver` 的接收器偏移） |
| `l_range` / `h_range` | 无单位标注，取值是 `I5E3`（0–5 mA）、`I3E4`（0–30 mA）、`AUTO` |

**`碌` 是坏字，应为 `µ`**（§11.2①）——**本页照原样抄，没替它改。**
**mA 与 µA 差 1000 倍，这条不核对就不能照着抄**（见 `## 出处` ⚠️②）。

### `hr_mode`：**语法、报错、版本三处都有，参数节里没有**

`hr_mode` 在本篇出现四次：语法式里两处（`TERM` 与 `TERM?` 的返回式各一处），
`## Functional changes` 里一条（`SmarTest 7.4.0: New extra parameter hr_mode.`），
`## Errors` 里一条（「Parameter hr_mode is used for instruments other than AVI64.」）。
**但 `## Parameters` 一节里没有它的条目，`## Termination modes` 的参数栏里也没有它。**

**所以「`hr_mode` 是什么、能取哪些值」本篇答不了——语料未写。**
（推断）把它与 `l_range` 的「This parameter is not supported for AVI64.」对起来看，
**它像是 AVI64 专有的一条路**；**但原文没有一句话这么说，这是推断不是文档事实。**

### equation based testing 下多两件事

> 「In equation based testing, you must identify level set ID instead of level set number.」

`level_set_id` 的算法（参数节逐字）：`100000 * equation_set_no + 1000 * specset_no + level_set_no`。

**并且会留下一个状态位**：

> 「Note The TERM command sets bit 8 of the status bits to indicate that the equation based values have been overridden.」

**即：被 `TERM` 改过的 equation-based 值会被标成「已覆盖」，标在第 8 位**，
查法在 [[spst]]（`SPST?`）那一篇。
（**原文这句没有在 `Note` 后面加冒号**，本页引用时照原样，**没补标点**。）

## 典型用法

**先说范围**：这一篇**没有 `## Procedure`，也没有 `## Before you begin`**。
唯一的过程线索是 `## Application`：`Level setup, see `Level Setup Commands`（raw: `02.06.05_Level_Setup_Commands.md`）`。
**所以本页不写流程顺序**（那是 [[level]] 的事）。

**写一条 `TERM` 要凑齐三样**：`{level_set_no}`、中间的 `term_mode` 与它的参数、末尾的 `(pinlist)`。
**中间都是位置参数，空位要用逗号占住**——原文 4 个例子里的逗号个数**不一样**，
而那是同一个规则的自然结果（下表后说）。

**1. 原文的 4 个例子（含原文说明）**

| 例 | 命令 | 原文的说明 |
|---|---|---|
| 1 | `TERM 1,T,-1500,,,,,(Q1)` | 「This example terminates the output pin Q1 to -1500 mV in level set 1.」 |
| 2 | `TERM 3,A,3000,1500,1000,I3E4,I3E4,(out)` | 「This example sets the active load level of the pin group out to 3V, and sets Iol and Ioh current to 1.5 and 1.0 mA respectively. The 0 to 30 mA range is used for both the low and the high range.」 |
| 3 | `TERM 1,CT,2000,,,,,(o1,o1-)` | 「This example terminates the differential output pair (the o1 and o1- pins) to 2000 mV with center tap termination in level set 1.」 |
| 4 | `TERM 1,OFF,PULLDOWN,,,,,,(Q1,Q2)` | 「On a PS1600 card, this example switches on the pulldown resistor on the specified pins.」 |
| 4 | `TERM 1,OFF,NONE,,,,,,(Q1,Q2)` | 「On a PS1600 card, this example switches off the pulldown resistor on the specified pins.」 |

**2. 空位怎么数（这是 4 个例子逗号个数不同的原因）**

按语法式，`(pinlist)` 之前是**位置参数**。其中
`level_set_no`、`term_mode`、`param_1`、`param_2`、`param_3`、`l_range`、`h_range`
是**七个常规槽位**，而 `[term_pulldown,]` 与 `[hr_mode,]` 是**两个把逗号写在方括号里面**的槽位。

（推断）读法就是：**常规空位必须用逗号占住；那两个槽省略时连逗号一起去掉、给了才多占一位。**
于是字段数会变——**这正是 4 个例子不一致的来源**：

| 例 | 在 `(pinlist)` 之前有几个字段 | 对得上吗 |
|---|---|---|
| 1 | `1` / `T` / `-1500` + **4** 个空位 = **7** | 对得上（`param_1` = `-1500`，`param_2`–`h_range` 空着；`term_pulldown`/`hr_mode` 都省掉） |
| 2 | `3` / `A` / `3000` / `1500` / `1000` / `I3E4` / `I3E4` = **7**，无空位 | 对得上（`param_1`–`param_3` 与两个 range 都给了） |
| 3 | `1` / `CT` / `2000` + **4** 个空位 = **7** | 对得上 |
| 4 | `1` / `OFF` / `PULLDOWN` + **5** 个空位 = **8** | 对得上（**给了 `term_pulldown`，比前三个多占一位**） |

**依据**是三个事实：四个例子各自的逗号数、`[term_pulldown,]` 的逗号在方括号内、
以及例 4 比例 1 多出的那一位正好是 `PULLDOWN`。
**这是推断，不是原文的一句话**（原文字面只说「见下面的表」）。
**没有任何例子用到 `hr_mode`，所以「给了它字段会怎么排」本篇没有例子可看。**

**3. 查回来**

`TERM? {level_set_no | level_set_id}, {(pinlist)}` 返回完整的 `TERM` 式。
两处要点（参数节逐字）：

- `term_pulldown`：「The query returns the parameter only if it is defined for the queried level set.」
- `pinlist` 的 `@`：「The @ character can be used to read all configured power supply pins.」

**4. 常见的三种用法**（照 `term_mode` 分）

- **纯终结** → `T`（例 1）。
- **主动负载** → `A`，**必须同时给 `l_range`/`h_range`**（例 2 给的是 `I3E4` 两边，
  即 0–30 mA 档）。
- **差分对内终结** → `CT`，pinlist 写一对（例 3 的 `(o1,o1-)`）。

## 和谁有关

| 页 | 是什么关系 | 依据 |
|---|---|---|
| [[psfc]] | **运行期前置**：`TERM` 只配置「有 setup 焦点」的 site | 本页文档正文（逐字引在上面） |
| [[site-focus-required-before-command]] | 上面那条前提的 constraint 页 | 同一条文档事实的归属页 |
| [[spst]] | **状态出口**：`TERM` 在第 8 位标「equation-based 值被覆盖」，查法在 `SPST?` | 本页文档 `## Equation based testing` |
| [[lsus]] | **上限来源之一**：已用的 level set 数由 `LSUS` 定义 | 本页文档参数节 |
| [[dscp]] | **上限来源之二**：允许的最大 level set 数由 `DSCP` 定义 | 本页文档参数节 |
| [[clmp]] | **替代路径**：`C` 与终结模式互相覆盖，**要并存必须用 `CLMP`** | 本页文档 `C` 那一行 |
| [[setup-level-set-0]] | **专用 set**：level set 0 是 digital pins 在 high-Z 时的专用 set，`ALL` 也绕过它 | 本页文档参数节 |
| [[level]] | **本页 `stage: level` 的理由**：它写的是 level 段里的终结配置 | frontmatter |
| [[pin]] | **前置**：`pinlist` 里的 pin「必须已经定义过」——「which have already been defined」 | 本页文档参数节 |
| [[ps1600]] / [[ps5000]] | **卡片限制的载体**：pulldown 两档、`DIFHIZ` 两档、`fast mode` 下主动负载不可用，都挂在这两种卡上 | 本页文档的 `## Termination modes` 与 `## Functional changes`；**这两页本页没读** |
| `Pin Scale 1600 driver`（raw: `../02.02_Specifications/02.02.04.01.03_PS1600_driver.md`）、`Pin Scale 5000 driver`（raw: `../02.02_Specifications/02.02.04.03.04_Pin_Scale_5000_driver.md`） | **数值的出处**：终结/主动负载的**电压电流范围**文档没给，指到这两篇卡规格 | 本页文档 `T` 与 `A` 两行；**两篇都未读，所以本页一个范围数都没有** |
| `IO PINS resources`（raw: `02.06.05.01.04.02.07_IO_PINS_resources.md`） | **`## Related information` 唯一那一篇** | 本页文档；**未读** |
| `Defining a level set for sequencer state OFF`（raw: `02.06.05.01.05.05_Controlling_high-Z_behavior_of_digital_pins_while_the_sequencers_are_OFF.md`） | **level set 0 的用法页** | 本页文档参数节；**未读** |

**本页没有引用 `edges.jsonl` 的入边/出边数字**（没读边数据，故不报条数）。

## 版本

**`## Functional changes` 段逐条**（原文照抄）：

- `Introduced before SmarTest 6.3.2`
- `SmarTest 7.1.0: New parameters for the PS1600: OFF,PULLDOWN; OFF, NONE`
- `SmarTest 7.1.4: DIFHIZ supported.`
- `SmarTest 7.4.0: New extra parameter hr_mode.`
- `SmarTest 7.4.0: Termination modes for DC Scale AVI64 added.`

**读法两条**：

- 第一行是**哨兵值**，不是「6.3.2 新增了 `TERM`」——意思见 §11.2② 与 [[smartest-6.3.2]]。
- 后四条给了**四个门槛**：`OFF,PULLDOWN`/`OFF,NONE` 要 **7.1.0** 起、
  `DIFHIZ` 要 **7.1.4** 起、`hr_mode` 与 AVI64 的终结模式要 **7.4.0** 起。
  （推断）**本 wiki 面向的 7.10.3 在这四条之后**，所以这四样在这一版上都有；
  **依据是版本号大小，不是机台核对。**

**版本页**：[[smartest-7.1.0]]、[[smartest-7.1.4]]、[[smartest-7.4.0]]。

## 出处

`sources:` 一篇：
`02_System_reference/02.06_Command_Reference/02.06.02.02.257_TERM__TERM__-__TERMination_mode.md`
（TDC `98771.htm`，5,329 字节，139 行）。**整篇读完。**

**本页没做的**：

- **文档里链到的六篇一篇都没读**（按出现顺序）：`PSFC, PSFC?`（`02.06.02.02.191`）、
  `SPST? - (SPecset STatus)`（`02.06.02.02.229`）、`LSUS, LSUS?`（`02.06.02.02.155`）、
  `DSCP`（`02.06.02.02.90`）、`Defining a level set for sequencer state OFF`（`02.06.05.01.05.05`）、
  `IO PINS resources`（`02.06.05.01.04.02.07`）、
  以及卡规格 `Pin Scale 1600 driver` / `Pin Scale 5000 driver`（`02.02.04.*`）。
  **所以「终结电压/电流的允许范围是多少」本页一个数都没有**——它们都在这几篇里。
  **注意：`CLMP` 在正文里被提到两次（`use the CLMP command`），但原文没给它链接。**
- **图一张没看**（本篇没有图）。
- **`## Termination modes` 那一节的表没有进「语法 / 参数」节**（原因见正文），
  **本页那张模式表是本页的转述**——要逐字核对，回 raw 的 `## Termination modes` 一节。
- **没有 `## Procedure` / `## Before you begin` 可读**，所以本页没有任何流程叙述。
- **没有用 `edges.jsonl`**，故不报入边/出边条数。

> ⚠️ **本篇的语料瑕疵，照实记下、一处都没替它改**：
>
> ① **坏字 `碌`（应为 `µ`）出现 2 次**：
> 「the active load Iol current in 碌A,」与「The units are 碌A.」
> ——**`碌` = `µ`**（§11.2①，对照表 `extract/encoding-map.csv`）。**照原样抄。**
> ② **`param_2` 的单位自相矛盾**：同一格里先写「The units are mA or mV respectively.」，
> 紧接着的项目符号写主动负载 Iol 电流是 `碌A`（即 µA）——**差 1000 倍**。
> 例 2 的说明跟的是 **mA**（「sets Iol and Ioh current to 1.5 and 1.0 mA respectively」）。
> **本页并列两处原文，不判哪个对**（§10）。
> （**推断**：例 2 给的两个数是 `1500` 与 `1000`，而说明把它们读成 `1.5 and 1.0 mA`——
> **只有在「`1500`/`1000` 的单位是 µA」时才成立**，所以参数节里那句 `mA` 更像是错的。
> **但这是本页按例 2 反推的，原文没有一句话纠正它，页面也不替它改字。**）
> ③ **`CT` 那一行自相矛盾**：说明句给了两个上电默认值
> （「The power-on default value of param_2 (swing) is 3.2 V, and the power-on default value of param_3 (offset) is 1.2 V.」），
> 而同一行的参数栏写的是「Not currently supported.」（`param_2`、`param_3` 各一次）。
> ④ **`DIFHIZ` 三行的第一列都印 `DIFHIZ`**，而说明句讲的分别是
> `DIFHIZ`、`DIFHIZ,PULLDOWN`、`DIFHIZ,NONE`；**且后两行的 pin 类型栏是空的**。
> **模式名与说明不一致**，本页照实记（表里已按说明句拆成三行）。
> ⑤ **`hr_mode` 缺参数说明**：语法两处、报错一条、版本一条都有它，
> `## Parameters` 与 `## Termination modes` 的参数栏里都没有它。
> ⑥ **`bidir_receiver` 只在 `param_3` 里出现过一次**：
> 「For term_mode = bidir_receiver, param_3 defines the receiver offset in mV.」——
> **`## Termination modes` 表里没有这个模式**。**这个模式的参数/支持卡片，本篇查不到。**
> ⑦ **`## Functional changes` 段的末行是一个光秃秃的列表符**：最后一行只有一个 `-`，
> **没有内容**（文件就此结束）。**照实记下，未删。**
> ⑧ **大小写/空格不一致**：同一行里 `OFF,PULLDOWN` 无空格、`OFF, NONE` 有空格
> （`SmarTest 7.1.0: New parameters for the PS1600: OFF,PULLDOWN; OFF, NONE`）。
> ⑨ **`Note` 后没有冒号**：「Note The TERM command sets bit 8 of the status bits to indicate that the equation based values have been overridden.」——
> **原文如此**（引文里没替它补冒号）。
> ⑩ **同一个东西两个说法**：正文第一句说的是「the output and IO pins」，
> 而 `pinlist` 那一项说的是
> 「The pin name or names of those power supply outputs which have already been defined.」——
> **`power supply outputs` 与 `output and IO pins` 是不是同一批 pin，本篇没说。**
