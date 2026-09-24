---
type: object
title: RCLV, RCLV? - (ReCeive LeVel)
layer: L1
stage: level
tags: [rclv, l1, firmware-command, level, compare-levels, threshold, fixed-levels, equation-based, comparator, range, site-focus]
related: [level, dfgp, dscp, lsus, drlv, pslv, term, psfc, site-focus-required-before-command, ps1600, ps5000]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.204_RCLV__RCLV__-__ReCeive_LeVel.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# RCLV, RCLV? - (ReCeive LeVel)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **4,008 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.204_RCLV__RCLV__-__ReCeive_LeVel.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### RCLV

```
RCLV {level_set_no | level_set_id}, [vth | logic_0_level], [logic_1_level], [range,] {(pinlist)}
```

### RCLV?

```
RCLV? {level_set_no | level_set_id}, {(pinlist)}
```

returns:

```
RCLV {level_set | level_set_id}, [vth | logic_0_level], [logic_1_level], [range,] {(pinlist)}
```

### Parameters

|

level_set

 |

The identification number of the level set in which you want the low and high threshold levels to be included. The number must not exceed the maximum number of level sets allowed (as defined by `DSCP, DSCP? - (Define System Control Parameter)`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md`）). If you enter a level set number that is outside the used range of sets defined by the LSUS command, a new level set is created. Typing ALL in this field sets the low and high threshold levels for all existing level sets (except level set 0). Typing PRM sets the low and high threshold levels for the primary level set.

Standard level sets have a number greater than 0. Level set 0 is a dedicated level set for sequencer state OFF. For more information see `Defining a level set for sequencer state OFF`（raw: `02.06.05.01.05.05_Controlling_high-Z_behavior_of_digital_pins_while_the_sequencers_are_OFF.md`）.

 |
 |

level_set_id

 |

Used in equation based level setup. It is derived as follows:

100000 * equation_set_no + 1000 * specset_no + level_set_no

Note that if you use the command for an equation based level setup, you modify only the runtime values, not the value in the level set.

 |
 |

vth

 |

Output threshold for FAST comparator (single threshold as opposed to high and low). The expression must define a value in millivolts (mV).

 |
 |

logic_0_level

 |

An integer (in mV) which sets the logic 0 threshold level of the comparator. This parameter represents the point where the comparator distinguishes between logic 0 and an intermediate level.

 |
 |

logic_1_level

 |

An integer (in mV) which sets the logic 1 threshold level of the comparator. This parameter represents the point where the comparator distinguishes between logic 1 and an intermediate level.

 |
 |

range

 |

This extra parameter selects the receive range in mV.

This parameter is currently not available.

Ranges of the high-speed voltage comparator:

- -8000.0 ... 8000.0 selects the 8 V range
- -40000.0 ... 80000.0 selects the -40 V ... +80 V range

Ranges of the high-resolution voltage comparator:

- -3000.0 ... 3000.0 selects the 3 V range
- -10000.0 ... 10000.0 selects the 10 V range
- -30000.0 ... 30000.0 selects the 30 V range
- -40000.0 ... 80000.0 selects the -40 V ... +80 V range

If not specified the best fit range will be selected based on logic_0_level and logic_1_level if a voltage comparator is selected.

Range of the high-resolution current comparator:

- A fixed range of 200 mA is set.

The query returns the parameter only if it is defined for the queried level set.

 |
 |

pinlist

 |

The name of the pin or pins whose threshold level you want to set. This parameter can also include groups previously created by the command `DFGP, DFGP? - (DeFine GrouP)`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）. If more than one pin is to be included, the names must be separated with a comma. The symbol @ sets or reads the threshold levels for all output pins. You can include O or IO pins in pinlist.

 |

For card specifications, like level ranges, see `Digital Cards`（raw: `../02.02_Specifications/02.02.04_Digital_Cards.md`）, for example:

- `Pin Scale 1600`（raw: `../02.02_Specifications/02.02.04.01.03_PS1600_driver.md`）
- `Pins Scale 5000`（raw: `../02.02_Specifications/02.02.04.03.04_Pin_Scale_5000_driver.md`）

### Example 1

```
RCLV 1,-1300,-750,(Q0)
```

This example sets the low level compare threshold for pin Q0 to -1300 mV and the high level compare threshold to -750 mV.

### Example 2

```
TERM 1,,,,,,HRV,(avi64Pin1)
RCLV 1,-1300,-750,3000,(avi64Pin1)
```

This example for an AVI64 pin sets the low level compare threshold to -1300 mV, the high level compare threshold to -750 mV, and the range to the 3 V range.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.204_RCLV__RCLV__-__ReCeive_LeVel.md>` 的 `## Errors`、`## Warnings` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

- The low level threshold is out of range.
- The high level threshold is out of range.
- The threshold swing is out of range.
- The level set number smaller than one.
- The level set number is outside the range defined by the DSCP command.
- For the query the level set number is outside the used range of sets defined by the LSUS command.
- The parameter "range" exceeds the hardware defined maximum range.

### Warnings

A warning is generated if

- Auto-correction of logic 1 or 0 threshold occurs.
- A range is defined for the high-resolution current comparator. This range will be ignored.

<!-- 报错节 end -->

## 是什么

**`RCLV` 是 fixed 路线上的比较阈值命令：给数字 pin 的比较器设低阈值与高阈值，值落进你指定的那个 level set。**

> 「The RCLV command defines the logic 1 and logic 0 threshold levels for the comparator. You can set levels for one or more pins within the same command. This command can also be used to set the threshold levels for a group of pins previously defined by the DFGP, DFGP? - (DeFine GrouP) command. The threshold levels are included in the level set you specify. The RCLV? query returns the present threshold levels for the level set and the pins specified.」

**三件事一句话**：一条命令可以设**多个 pin**；也可以按 [[dfgp]] 定义过的**组**来设；
**阈值进 level set**。

### 一条只有本文档写的机制：串阻的压降**自动补偿**

> 「If a series resistor (resistive divider) is used on the DUT board, the receiver levels will automatically be adjusted to compensate for the voltage drop across the series resistor.」

**即：DUT 板上有串阻（阻性分压）时，你写进去的阈值会被系统自动调过来，
以抵掉串阻上的那部分压降。**
**换句话读：你写的是「DUT 那端想要的阈值」，不是「比较器端子上的电压」。**
（这是文档事实。**补偿量怎么算、在哪一步做、有没有开关，本篇都没说。**）

### 第二条正文独有的警告（与 [[drlv]] 同一条）

> 「In connection with equation based timing, note that RCLV only changes the runtime values, not the setup values specified in the level set.」

**方程路线下改的只是运行时值，不是 level set 里存的 setup 值。**
参数表 `level_set_id` 那一格说的是同一件事，**但换了个词**
（`Note that if you use the command for an equation based level setup, you modify only the runtime values, not the value in the level set.`）。
**两处一个说 `timing`、一个说 `level`，见「出处」⚠️⑦。**

### 六个位（第 2 位是**二选一**）

| 位 | 参数 | 单位 | 原文要点 |
|---|---|---|---|
| 1 | `level_set_no`（本文档写作 `level_set`） | — | 另可写 `ALL` / `PRM`；上限由 [[dscp]] 定 |
| 1' | `level_set_id` | — | 方程路线专用：`100000 * equation_set_no + 1000 * specset_no + level_set_no` |
| 2 | `vth` **或** `logic_0_level` | **mV** | 单阈值 vs 双阈值的低端，见下 |
| 3 | `logic_1_level` | **mV** | 双阈值的高端 |
| 4 | `range` | mV | 三套比较器三张表，见下 |
| 5 | `pinlist` | — | **O 与 IO 类型** pin；`@` = **全部 output pin** |

**第 2 位到底写哪个，取决于你用的是哪种比较器**——这不是「都写」。

| 写什么 | 给谁用 | 原文怎么判 |
|---|---|---|
| `vth` | **FAST 比较器** | `Output threshold for FAST comparator (single threshold as opposed to high and low). The expression must define a value in millivolts (mV).` |
| `logic_0_level` + `logic_1_level` | 常规双阈值比较器 | 两个点；低端 `the point where the comparator distinguishes between logic 0 and an intermediate level`，高端同形（`between logic 1 and an intermediate level`） |

**一句话：FAST 是「一个阈值」，常规是「两个阈值 + 中间那段算 intermediate」。**

### `pinlist`：**`@` 指的是 output pin**

> 「The symbol @ sets or reads the threshold levels for all output pins. You can include O or IO pins in pinlist.」

**能进 `pinlist` 的是 `O` 与 `IO` 两类 pin**；`@` = **全部 output pin**。
**（对照 [[drlv]]：那边 `@` 指全部 input pin、收的是 `I` 与 `IO`。
两条命令的 `@` 不是同一个集合，正好互补。）**
也可以写 [[dfgp]] 建过的组名，多个名字用逗号分隔。

### 两条**互相反着**的编号规则：「写」会建新 set，「读」会报错

原文把这对称的两句放在相隔很远的两处，**必须成对读**：

| 你在做什么 | 编号超出 LSUS 定义的已用范围时 |
|---|---|
| **`RCLV`（写）** | 逐字：`If you enter a level set number that is outside the used range of sets defined by the LSUS command, a new level set is created.`——**默默地多出一个 level set** |
| **`RCLV?`（读）** | 逐字：`For the query the level set number is outside the used range of sets defined by the LSUS command.`——**这是 `## Errors` 里的一条** |

**即：写一个越界编号是「建」，读一个越界编号是「错」。** 判据都在 [[lsus]]。
**这条差别不读全篇就看不出来**：`LSUS` 出现在两处，一处在参数说明里、一处在 Errors 里。

`ALL` 有一条排除：逐字
`Typing ALL in this field sets the low and high threshold levels for all existing level sets (except level set 0).`
`PRM` = `sets the low and high threshold levels for the primary level set`。

**`level set 0` 是什么**，原文专门给了一句：

> 「Standard level sets have a number greater than 0. Level set 0 is a dedicated level set for sequencer state OFF. For more information see Defining a level set for sequencer state OFF.」

（`Defining a level set for sequencer state OFF`（raw: `02.06.05.01.05.05_Controlling_high-Z_behavior_of_digital_pins_while_the_sequencers_are_OFF.md`）**本页没读**。）

### `range`：**三套比较器、三张表**（这是与 [[drlv]] 最大的不同）

[[drlv]] 的 `range` 只有一张三行的表；**`RCLV` 的 `range` 按比较器种类分成三组**：

| 比较器 | 可选范围（原值，mV） |
|---|---|
| **高速电压比较器** | `-8000.0 ... 8000.0` → 8 V 档；`-40000.0 ... 80000.0` → -40 V ... +80 V 档 |
| **高分辨率电压比较器** | `-3000.0 ... 3000.0` → 3 V 档；`-10000.0 ... 10000.0` → 10 V 档；`-30000.0 ... 30000.0` → 30 V 档；`-40000.0 ... 80000.0` → -40 V ... +80 V 档 |
| **高分辨率电流比较器** | `A fixed range of 200 mA is set.`——**固定，不给选** |

> 「If not specified the best fit range will be selected based on logic_0_level and logic_1_level if a voltage comparator is selected.」

> 「This parameter is currently not available.」

> 「The query returns the parameter only if it is defined for the queried level set.」

**三个要点**：
① **自动挑档只对「电压比较器」成立**——原文那半句 `if a voltage comparator is selected` 是条件。
② **电流比较器是固定 200 mA 档**；给它写 `range` **不会生效，只会得到一条 warning**（见「报错条件」节的 Warning 第 2 条）。
③ `This parameter is currently not available.` 与 Example 2 实际用了它**并列**（⚠️①）。

## 典型用法

**1. 顺序：组要先定义。** `pinlist` 里写组名时，组必须已由 [[dfgp]] 建好（同 [[drlv]]）。

**2. Example 1 —— 一个 pin、两个阈值：**

```
RCLV 1,-1300,-750,(Q0)
```

> 「This example sets the low level compare threshold for pin Q0 to -1300 mV and the high level compare threshold to -750 mV.」

**3. Example 2 —— AVI64、3 V 档，而且是两条命令连写：**

```
TERM 1,,,,,,HRV,(avi64Pin1)
RCLV 1,-1300,-750,3000,(avi64Pin1)
```

> 「This example for an AVI64 pin sets the low level compare threshold to -1300 mV, the high level compare threshold to -750 mV, and the range to the 3 V range.」

**`3000` 照高分辨率电压比较器的表落在 `-3000.0 ... 3000.0` 里 → 3 V 档。**

> **原文没有解释第一行 `TERM` 为什么在那儿。** `TERM` 没有出现在本篇任何一节
> （`## Parameters` 没提它，本篇也**没有** `## Related information` 一节），
> 那一串空参数与 `HRV` 的含义**本篇一个字都没给**（⚠️②）。**本页不猜。**

**4. 读回**：`RCLV? {level_set_no | level_set_id}, {(pinlist)}`。
**回读只在「该 level set 定义过 `range`」时才把 `range` 带回来**
（`The query returns the parameter only if it is defined for the queried level set.`）——
**所以回读结果里没有 `range` 不等于没设过，只是没定义。**

**5. 七条 Errors 与两条 Warnings** 在下面的「报错条件」节（脚本逐字取）。
**两条 Warning 值得单独记**：

| Warning（原文） | 说的是什么 |
|---|---|
| `Auto-correction of logic 1 or 0 threshold occurs.` | 阈值被系统**自动修正**了 |
| `A range is defined for the high-resolution current comparator. This range will be ignored.` | **给电流比较器写了 `range`——被忽略**（正好对应上面那条「固定 200 mA」） |

**两条都不会让命令失败**，所以不看 report 就不会知道。

**6. 归属**：原文 `## Application` → `Level setup, see Level Setup Commands.`
（**这一句的 `setup` 是小写，见「出处」⚠️⑥。**）

**7. 卡规格去哪查**：与 [[drlv]] 同一句指路——`For card specifications, like level ranges, see Digital Cards`，
例子里给了 [[ps1600]] 与 [[ps5000]]。

## 和谁有关

- [[level]] — **`stage: level` 是「最近的一段」，不是归属**（§6）。
  依据是 `## Application` 那唯一一句 `Level setup, see Level Setup Commands.`
- [[dfgp]] — **上游 / 前置**：组必须先定义，`RCLV` 才能按组设阈值。
- [[dscp]] — **上游 / 上限的定义方**：`level_set` 编号的上限由它给出；
  `## Errors` 里有一条专讲「超出 `DSCP` 定的范围」。
- [[lsus]] — **本文档两次点名它，而且是两个相反方向的判据**：
  「写越界会新建 level set」「读越界会报错」这两条的分界线都是它。
  **`RCLV` 是这一对称规则写得最清楚的一篇**（同批另外三条命令都没有这个对照）。
- [[drlv]] — **同类、管的是另一侧**：`DRLV` 是**驱动**、`RCLV` 是**接收**。
  两处可直接对照：**`@` 的集合**（input / output）与 **`range` 表的张数**（1 张 / 3 张）。
- [[pslv]] — **同批同族**：管 DPS 供电。
- [[term]] — **只在 Example 2 里出现过一次**，原文没有任何说明与链接（⚠️②）——
  本页把它列出来，**只声明「这里出现了它」，不声明两者是什么关系**。
- [[psfc]] — **另一条前置**：本命令只配置 `setup focus` 里的 site；
  踩错的后果见 [[site-focus-required-before-command]]。
- [[ps1600]] / [[ps5000]] — **下游（规格侧）**：原文举的两张卡。
- `Digital Cards`、`Level Setup Commands`、`Defining a level set for sequencer state OFF`
  （**均未建、且不在 allowlist 里**）—— 三篇原文点过名的文档，本页都没读。

## 版本

本文档**有** `## Functional changes` 段，两条，**逐字**：

| 条目 | 说明 |
|---|---|
| `Introduced before SmarTest 6.3.2` | **§11.2 ② 的哨兵值**，见下① |
| `SmarTest 7.4.0: New extra parameter range.` | **对得上**：`range` 是语法行的第 4 位；**但与正文的「当前不可用」并列**，见下② |

**① `Introduced before SmarTest 6.3.2` 不是「6.3.2 的变更」。** 按 §11.2 ②，
它是「**早于本文档集覆盖范围**」的哨兵——**`RCLV` 成立于哪个版本，这份语料里没有。**

**② 7.4.0 说 `range` 是「新增的额外参数」，而正文说它 `currently not available`。**
两句并不同义（「新增」讲的是历史、「当前不可用」讲的是现状），**但正文与例子又对不上**
（Example 2 用了它）——**三处并列，见「出处」⚠️①。本页不替它们排时间线。**

**③ 与 wiki 面向版本的关系**：本 wiki 面向 **SmarTest 7.10.3**（[[smartest-7.10.3]]），
而这一篇版本段**停在 7.4.0**。**7.4.0 之后 `RCLV` 有没有再变，语料里没有。**
「`range` 在 7.10.3 上能不能用」**本篇答不了**。

## 出处

`sources:` 一篇：
`02_System_reference/02.06_Command_Reference/02.06.02.02.204_RCLV__RCLV__-__ReCeive_LeVeL.md`

**本页没做的：**

- **`DFGP` 没读** —— 组怎么建、能不能混 pin 类型，本页没有。
- **`DSCP` 没读** —— `level_set` 编号的上限**具体是多少**，本页不知道。
- **`LSUS` 没读** —— **这是本页最大的空缺**：本页只知道它划定了
  「写会建新 set / 读会报错」的那条界线，**不知道那条界线是怎么算出来的、
  以及「新建的 level set」长什么样**。
- **`TERM` 没读** —— Example 2 里那行 `TERM 1,,,,,,HRV,(avi64Pin1)` 的含义，
  本页与原文一样不知道（⚠️②）。
- **`Defining a level set for sequencer state OFF` 没读** ——
  所以 level set 0 除了「`ALL` 不含它」「给 sequencer OFF 用」之外还有什么规矩，本页没有。
- **`Digital Cards`、`Pin Scale 1600`、`Pins Scale 5000` 三篇都没读** ——
  所以各卡的量程、以及**这几种比较器分别在哪张卡上**，本页只有「去哪查」。
- **`Level Setup Commands`（`02.06.05`）章首页没读** —— `## Application` 指向的内容面本页没有。
- **没有图。** 原文没有图片。
- **一条 `RCLV` 都没在真机上跑过**（`verified: doc-only`）——
  §11：**文档里有 ≠ 这台机器上能用**。尤其「串阻自动补偿」这一条，
  **补多少、什么时候不补，本篇没有任何边界**，动手前必须先量。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> **① `range` 被判「当前不可用」，Example 2 却用它。** 逐字两条并列：
> `This parameter is currently not available.`（`range` 那一格）
> / `RCLV 1,-1300,-750,3000,(avi64Pin1)`（Example 2），
> 后者的解释是 `This example for an AVI64 pin sets the low level compare threshold to -1300 mV,
> the high level compare threshold to -750 mV, and the range to the 3 V range.`
> ——**原文没说这个例子还有效、还是旧版遗留。本页不判。**
>
> **② Example 2 的第一行 `TERM` 在本篇里完全没有着落。** 逐字：
> `TERM 1,,,,,,HRV,(avi64Pin1)`
> ——**`TERM` 不出现在 `## Parameters`、不出现在 `## Application`、
> 也不出现在任何一节里**（本篇没有 `## Related information` 段）；
> 那一行的六个空参数与 `HRV` 的含义**本篇一个字都没解释**。
>
> **③ 「level set 编号」在四个地方换了三种写法。** 逐字：
> `RCLV {level_set_no | level_set_id}`（命令，**`level_set_no`**）
> / `RCLV {level_set | level_set_id}`（返回串，**变成 `level_set`**）
> / 参数表的条目名也是 `level_set`（**而 [[drlv]] 同一格写的是 `level_set_no`**）。
>
> **④ `## Errors` 里有一条缺动词。** 逐字：
> `- The level set number smaller than one.`
> ——**按同篇其他条目的句式，这里应有一个 `is`**（同批 [[drlv]] 的对应条目缺的正是另一个东西，
> 两篇的 `## Errors` 句式也不同）。**本页照原样引，不替它补。**
>
> **⑤ Warnings 的起句没有冒号。** 逐字：
> `A warning is generated if`
> ——**而 [[drlv]] 同一位置写的是 `A warning is generated if:`（有冒号）。**
>
> **⑥ `## Application` 那一句的 `setup` 是小写。** 逐字：
> `Level setup, see Level Setup Commands.`
> ——**同批的 [[pslv]] / [[drlv]] / [[dsus]] 三篇在这个位置都写 `Level Setup,`（大写 `S`）。**
>
> **⑦ 同一件事在正文里换了个词：`timing` / `level`。** 逐字：
> `In connection with equation based timing, note that RCLV only changes the runtime values, not the setup values specified in the level set.`
> / `Note that if you use the command for an equation based level setup, you modify only the runtime values, not the value in the level set.`
> ——**与 [[drlv]] 是同一个毛病、同样的两句。**
>
> **⑧ `-40000.0 ... 80000.0` 那一档在两张表里出现两次。** 逐字：
> `- -40000.0 ... 80000.0 selects the -40 V ... +80 V range`
> ——**「高速电压比较器」与「高分辨率电压比较器」两张表里各有一行这个数，
> 数字完全相同**；而高分辨率那张表另外多了 3 V / 10 V / 30 V 三档，高速表没有。
> **原文没说这两处是同一档还是两档。**
>
> **⑨ 本篇没有 `## Related information` 段**（对照 [[pslv]] 有）。
> 所以 [[dfgp]] / [[lsus]] / [[dscp]] / 两张卡 的指向**全靠正文内联链接承载**——
> **把链接一剥（如语法节那种 `文本（raw: 路径）` 改写），这些名字就消失了。**
>
> **⑩ 「高分辨率电流比较器」那一组只有一个列表项，且没说清口径。** 逐字：
> `- A fixed range of 200 mA is set.`
> ——**没说是源向还是汲向，也没说 200 mA 是上限还是范围宽度**；正文也没再提它。
>
> **⑪ 文件名里标题的问号变成了 `_`。** 本页 `title` 是
> `RCLV, RCLV? - (ReCeive LeVeL)`，而语料文件名是
> `02.06.02.02.204_RCLV__RCLV__-__ReCeive_LeVeL.md`。
> **这是语料的命名约定（问号进不了文件名），不是错字，但按名字找文件的人搜不到 `RCLV?`。**

`verified: doc-only`
