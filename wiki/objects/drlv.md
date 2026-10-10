---
type: object
title: DRLV, DRLV? - (DRive LeVel)
layer: L1
stage: level
tags: [drlv, l1, firmware-command, level, drive-levels, fixed-levels, equation-based, svlr, pin-group, site-focus]
related: [level, dfgp, dscp, svlr, psfc, site-focus-required-before-command, rclv, pslv, ps1600, ps5000]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.89_DRLV__DRLV__-__DRive_LeVel.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# DRLV, DRLV? - (DRive LeVel)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,334 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.89_DRLV__DRLV__-__DRive_LeVel.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### DRLV

```
DRLV {level_set_no | level_set_id}, [logic_0_level], [logic_1_level], [v3h_level | range,] {(pinlist)}
```

### DRLV?

```
DRLV? {level_set_no | level_set_id}, {(pinlist)}
```

returns:

```
DRLV {level_set | level_set_id}, [logic_0_level], [logic_1_level], [v3h_level | range,] {(pinlist)}
```

### Parameters

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98577.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 2 列。
> 首行（上游原文）：level_set_no | The identification number of the level set (fixed levels) in which you want the levels to be included. The number must not exceed the maximum num…
> 表内引用（2 条，供检索）：`DSCP`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md`） · `DFGP`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）

For card specifications, like level ranges, see `Digital Cards`（raw: `../02.02_Specifications/02.02.04_Digital_Cards.md`）, for example:

- `Pin Scale 1600`（raw: `../02.02_Specifications/02.02.04.01.03_PS1600_driver.md`）
- `Pins Scale 5000`（raw: `../02.02_Specifications/02.02.04.03.04_Pin_Scale_5000_driver.md`）

### Example 1

```
DRLV 1,-1750,-850,(Q0,Q1,Q2,Q3)
```

This example sets the driver levels for level set 1 for pins Q0, Q1, Q2 and Q3. The logic 0 level is set to -1750 mV and the logic 1 level to -850 mV.

### Example 2

```
DRLV 1,-1750,-850,8000,(avi64Pin1)
```

This example shows how the 8 V drive range of an AVI64 pin is selected.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.89_DRLV__DRLV__-__DRive_LeVel.md>` 的 `## Errors`、`## Warnings` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

- The high or low level is out of range;
- The swing limitations are exceeded;
- The set number is out of range;
- The set number is out of the range defined by the DSCP command;
- The set number is out of the used range of sets (DRLV? only).
- The parameter "range" exceeds the hardware defined maximum range.

### Warnings

A warning is generated if:

- Auto-correction of logic level 1 or 0 occurs.
- The logic 1 or 0 level for a pin lies outside the specification.

<!-- 报错节 end -->

## 是什么

**`DRLV` 是 fixed 路线上的驱动电平命令：给数字 pin 的驱动放大器设低电平与高电平，值落进你指定的那个 level set。**

> 「The DRLV command defines the low and the high voltage levels for the driver amplifiers. You can set levels for one or more pins within the same command. This command can also be used to set the drive levels for a group of pins previously defined by the DFGP, DFGP? - (DeFine GrouP) command. These levels are included in the level set you specify. The DRLV? query returns the present voltage levels for the set and pins specified.」

**三件事一句话**：一条命令可以设**多个 pin**；也可以按 [[dfgp]] 定义过的**组**来设；
**值进 level set**（不是进 pin 本身）。

### 两条只写在正文里、语法节一个字都没有的警告

**这两句是本页最要紧的内容**——它们决定了「在 testflow 里调 `DRLV` 会付出什么代价」。

**① 每调一次就要「激活 level set」，多 site 并行时会拖慢测试；文档给的出路是 `SVLR`。**

> 「Note Each call of the DRLV FW command requires an activation of the level set. This could lead to increase in the test time in particular when high number of sites are tested in parallel. In such cases, use the SVLR FW command.」

**即：`DRLV` 不是「改个值就完了」——每次调用背后都跟一次 level set 激活。**
**高 site 数并行时这个开销会显出来，文档指定改用 [[svlr]]。**

**② 方程路线下只改运行时值，不改 level set 里的 setup 值。**

> 「In connection with equation based timing, note that DRLV only changes the runtime values, not the setup values specified in the level set.」

参数表里 `level_set_id` 那一格说的是同一件事，**但换了一个词**——逐字：
`Note that if you use the command for an equation based level setup, you modify only the runtime values, not the value in the level set.`
**两处一个说 `timing`、一个说 `level`，本页并列，见「出处」⚠️③。**

### 六个位（第 4 位是**二选一**）

| 位 | 参数 | 单位 | 原文要点 |
|---|---|---|---|
| 1 | `level_set_no` | — | 另可写 `ALL` / `PRM`；上限由 [[dscp]] 定 |
| 1' | `level_set_id` | — | 方程路线专用：`100000 * equation_set_no + 1000 * specset_no + level_set_no` |
| 2 | `logic_0_level` | **mV** | `An integer (in mV) which sets the low level voltage for the drive amplifier.` |
| 3 | `logic_1_level` | **mV** | `An integer (in mV) which sets the high level voltage for the drive amplifier.` |
| 4 | `v3h_level` **或** `range` | mV | **同一个位置的两种含义，见下** |
| 5 | `pinlist` | — | **I 与 IO 类型** pin；`@` = 该 level set 里**全部 input pin** |

`level_set_no` 那一格的两条附加写法：`ALL` = `sets the levels for all existing level sets`；
`PRM` = `sets the drive voltage levels for the primary level set`。

### 第 4 位：`v3h_level` 与 `range` 抢同一个位置

语法行写的是 `[v3h_level | range,]`——**那个竖线是「二选一」**。原文对两者的判决是：

| 写法 | 是什么（原文） | 原文对它的判决 |
|---|---|---|
| `v3h_level` | `Input (drive) 3rd level definition (high level voltage shift). The expression of this extra parameter must define a value in millivolts (mV).` | **`This parameter is no longer used.`** |
| `range` | 选驱动量程（下表） | **`This parameter is currently not available.`** |

**两个都被判了「别用」**：一个「不再使用」，一个「当前不可用」。
**而 `range` 偏偏出现在 `## Examples` 的 Example 2 里**（见「典型用法」3 与「出处」⚠️①）。

`range` 的选择规则（值按 mV 给）：

| 写的值 | 选中哪个量程 |
|---|---|
| `-8000.0 ... 8000.0` | **8 V 档** |
| `-30000.0 ... 30000.0` | **30 V 档** |
| `all other values` | **-40 V ... +80 V 档** |

两条附带规则逐字：

> 「If not specified the best fit range will be selected based on logic_0_level and logic_1_level.」

> 「The query returns the parameter only if it is defined for the queried level set.」

**不给就按两个 logic 电平自动挑最合适的档**；`DRLV?` **只在它被显式定义过时才把它报回来**。

### `pinlist`：**`@` 指的是 input pin**

> 「The symbol @ sets or reads the drive levels of all input pins in the level set. You can include I and IO pin types in pinlist.」

**两个要点**：`@` = 该 level set 里**全部 input pin**；能进 `pinlist` 的是 **`I` 与 `IO`** 两类 pin。
**（对照 [[rclv]]：那边 `@` 指全部 output pin、收的是 `O` 与 `IO`——两条命令的 `@` 不是同一个集合。）**
也可以写 [[dfgp]] 建过的组名，多个名字用逗号分隔。

### 两段 site 相关的标准段落

原文与 [[pslv]] / [[rclv]] 同位置有两段**在所有站点焦点命令里都出现**的话：

> 「With this command you configure setups of those sites that have the setup focus:」

> 「With this command you can retrieve site specific information (only one site can be in focus at a time). For the site in focus, SmarTest displays results in the Testflow Editor and in the result tools. Also, any firmware queries report setup and results for the site currently in focus only.」

**要紧的是括号里那半句**：**同一时刻只有一个 site 在焦点里**，
所以 `DRLV?` 在多 site 下**只能逐 site 轮着查**。前因后果见 [[site-focus-required-before-command]]。

## 典型用法

**1. 顺序：组要先定义。** `pinlist` 里如果要写组名，那个组必须是 [[dfgp]] 已经建好的
（原文 `groups previously created by the DFGP ... command`）。

**2. Example 1 —— 一次设四个 pin：**

```
DRLV 1,-1750,-850,(Q0,Q1,Q2,Q3)
```

> 「This example sets the driver levels for level set 1 for pins Q0, Q1, Q2 and Q3. The logic 0 level is set to -1750 mV and the logic 1 level to -850 mV.」

**注意两个电平都是负值**（`-1750` / `-850` mV）。**原文没有解释为什么是负的，本页不猜。**

**3. Example 2 —— 选 8 V 档：**

```
DRLV 1,-1750,-850,8000,(avi64Pin1)
```

> 「This example shows how the 8 V drive range of an AVI64 pin is selected.」

**第 4 位 `8000` 照 `range` 那张表落在 `-8000.0 ... 8000.0` 区间里 → 选中 8 V 档。**
**但参数表同时说 `range`「currently not available」**——两处并列，本页不判（⚠️①）。

**4. 改完要「激活」。** 见上面警告①：`DRLV` **每次调用都需要一次 level set 激活**；
批量改值的场合文档指定改用 [[svlr]]。
**这是 `DRLV` 与 [[pslv]] 的一个分界**：`PSLV` 那边明写「primary DPS set 立即生效」，
`DRLV` 这边明写「每次调用都要激活」。

**5. 出错与警告**在下面的「报错条件」节（脚本逐字取）。
**两条 Warning 一条讲自动修正、一条讲超规格**，逐字：
`Auto-correction of logic level 1 or 0 occurs.` 与 `The logic 1 or 0 level for a pin lies outside the specification.`
**两条都不是「参数写错」而是「参数被系统动过或落在规格外」——它们不会让命令失败。**

**6. 归属**：原文 `## Application` → `Level Setup, see Level Setup Commands.`

**7. 卡规格去哪查**：原文在 `pinlist` 那格下面指了路——
`For card specifications, like level ranges, see Digital Cards, for example:`，
后面举了两张卡：[[ps1600]] 与 [[ps5000]]（**原文的显示名见「出处」⚠️⑤**）。

## 和谁有关

- [[level]] — **`stage: level` 是「最近的一段」，不是归属**（§6）。
  依据是 `## Application` 那唯一一句 `Level Setup, see Level Setup Commands.`
- [[dfgp]] — **上游 / 前置**：组必须先定义，`DRLV` 才能按组设电平。
  `DRLV` 是「组定义好之后怎么给组设值」。
- [[dscp]] — **上游 / 上限的定义方**：`level_set_no` 的允许范围由它给出；
  `## Errors` 里也有一条专讲「超出 `DSCP` 定的范围」。
- [[svlr]] — **文档指定的替代路径**（不是可选优化）：多 site 并行时不要反复调 `DRLV`，
  改用 `SVLR`——**这一条只在正文那段 Note 里，语法节没有**。
- [[psfc]] — **另一条前置**：本命令只配置 `setup focus` 里的 site，焦点由 `PSFC` 设；
  踩错的后果见 [[site-focus-required-before-command]]。
- [[rclv]] — **同类、管的是另一侧**：`DRLV` 是**驱动**（往 DUT 里灌电平），
  `RCLV` 是**接收**（比 DUT 吐出来的电平）。两条命令的 `@` 集合正好互补
  （`DRLV` 全部 input、`RCLV` 全部 output），可用来记「谁管谁」。
- [[pslv]] — **同批同族**：`PSLV` 管 DPS，`DRLV` 管数字 pin；
  两者的差别之一是**「改完要不要额外激活」**（见「典型用法」4）。
- [[ps1600]] / [[ps5000]] — **下游（规格侧）**：原文把「量程这类卡规格」指给它们，
  并说细表在 `Digital Cards`。
- `Digital Cards`（**未建、不在 allowlist 里**）—— 原文指定的卡规格总入口。
- `Level Setup Commands`（**未建、不在 allowlist 里**）—— 章首页，`## Application` 指它。

## 版本

本文档**有** `## Functional changes` 段，三条，**逐字**：

| 条目 | 说明 |
|---|---|
| `Introduced before SmarTest 6.3.2` | **§11.2 ② 的哨兵值**，见下① |
| `SmarTest 7.0.1: No single-density support` | **含义不明**，见下② |
| `SmarTest 7.4.0: Usage of the fourth parameter extended: v3h_level changed to v3h_level \| range.` | **对得上**：语法行第 4 位就是 `[v3h_level \| range,]`，见下③ |

**① `Introduced before SmarTest 6.3.2` 不是「6.3.2 的变更」。** 按 §11.2 ②，
它是「**早于本文档集覆盖范围**」的哨兵——**`DRLV` 成立于哪个版本，这份语料里没有。**

**② `No single-density support` 这一条本页解释不了。**
「单密度（single-density）」在本篇正文、参数表、例子里**一个字都没有**，
**也没有任何一段被这条改动对应到**。本页照实转录，不替它编含义。

**③ 7.4.0 那条给了一条有用的时间线**：第 4 位的「二选一」形态是 **7.4.0** 才有的；
**在那之前第 4 位只有 `v3h_level`**。
但**正文同时说 `v3h_level` 已不再使用、`range` 当前不可用**——
**7.4.0 之后第 4 位到底还能不能写、写了会怎样，本篇没有正面回答**（⚠️①、⚠️②）。

**④ 与 wiki 面向版本的关系**：本 wiki 面向 **SmarTest 7.10.3**（[[smartest-7.10.3]]），
而这一篇版本段**停在 7.4.0**。**7.4.0 之后 `DRLV` 有没有再变，语料里没有。**

## 出处

`sources:` 一篇：
`02_System_reference/02.06_Command_Reference/02.06.02.02.89_DRLV__DRLV__-__DRive_LeVeL.md`

**本页没做的：**

- **`DFGP` 没读** —— 组怎么建、组里能不能混 pin 类型，本页一个字都没有；
  本页只有「`pinlist` 可以写组名」这一句。
- **`DSCP` 没读** —— `level_set_no` 的上限**具体是多少**，本页不知道。
- **`SVLR` 没读** —— 所以「改用 `SVLR`」具体怎么写、语义上与 `DRLV` 差在哪，
  **本页只有那句 Note 的指向，没有内容**。
- **`PSFC` 没读** —— 「怎么设焦点」本页不知道。
- **`Digital Cards`、`Pin Scale 1600`、`Pins Scale 5000` 三篇都没读** ——
  所以各卡支持哪些量程、`v3h` 在哪张卡上有，**本页只有「去哪查」**。
- **`Level Setup Commands`（`02.06.05`）章首页没读** —— `## Application` 指向的内容面本页没有。
- **一条 `DRLV` 都没在真机上跑过**（`verified: doc-only`）——
  §11：**文档里有 ≠ 这台机器上能用**。尤其那条「每次调用都要激活」的开销，
  **大到什么程度、什么 site 数下该换 `SVLR`，本篇没有给数**。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> **① `range` 被判「当前不可用」，Example 2 却用它。** 逐字两条并列：
> `This parameter is currently not available.`（`range` 那一格的末尾）
> / `DRLV 1,-1750,-850,8000,(avi64Pin1)`（`## Examples` 的 Example 2），
> 后者的解释是 `This example shows how the 8 V drive range of an AVI64 pin is selected.`
> ——**原文没说例子的写法还有效、还是旧版遗留。本页不判。**
>
> **② `v3h_level` 被判「不再使用」，但它仍在语法行、参数表与语法节里。** 逐字：
> `This parameter is no longer used.`，而语法行是
> `DRLV {level_set_no | level_set_id}, [logic_0_level], [logic_1_level], [v3h_level | range,] {(pinlist)}`
> ——**第 4 位仍写着 `v3h_level`。**
>
> **③ 同一件事在正文里换了个词：`timing` / `level`。** 逐字：
> `In connection with equation based timing, note that DRLV only changes the runtime values, not the setup values specified in the level set.`
> / `Note that if you use the command for an equation based level setup, you modify only the runtime values, not the value in the level set.`
> ——**`equation based timing` 与 `equation based level setup` 指的不是同一个东西，
> 但这里说的是同一件事。**
>
> **④ 两句话被粘在一起，`set.` 与 `Note` 之间没有分隔符。** 逐字：
> ` In connection with equation based timing, note that DRLV only changes the runtime values, not the setup values specified in the level set.Note Each call of the DRLV FW command requires an activation of the level set.`
> ——**`level set.Note Each call` 这里没有换行也没有空格**
> （对照 [[pslv]] 里同类的毛病，那篇是 `0.Note`）。
>
> **⑤ `Pins Scale 5000` 这个显示名多一个 `s`，它自己的链接目标不带。** 逐字两处：
> `[Pins Scale 5000](<../02.02_Specifications/02.02.04.03.04_Pin_Scale_5000_driver.md>)`
> ——显示名是 `Pins Scale 5000`，**文件名是 `Pin_Scale_5000_driver.md`**。
> 同一行的上一条是 `Pin Scale 1600`（**不带 `s`**）。**本页照实转两个名字，不替它统一。**
>
> **⑥ 「level set 编号」在四个地方换了三种写法。** 逐字：
> `DRLV {level_set_no | level_set_id}`（命令）
> / `DRLV {level_set | level_set_id}`（返回串，**`level_set_no` 少了 `_no`**）
> / `The set number is out of range;`（`## Errors` 第三条，**又变成 `set number`**）。
>
> **⑦ `## Errors` 六条的标点不齐。** 逐字：
> ```
> - The high or low level is out of range;
> - The swing limitations are exceeded;
> - The set number is out of range;
> - The set number is out of the range defined by the DSCP command;
> - The set number is out of the used range of sets (DRLV? only).
> - The parameter "range" exceeds the hardware defined maximum range.
> ```
> ——**前四条以 `;` 结尾，第五条却以 `.` 结尾，而它后面还有第六条。**
>
> **⑧ `## Parameters` 那张表的第一个格子是一个孤立的 ` | `。** 逐字：
> ```
>  |
>
> level_set_no
> ```
> ——**表头位置只有一个竖线**。**「语法 / 参数」节里那个孤立的 ` | ` 就是它。**
>
> **⑨ 本篇没有 `## Related information` 段**（对照 [[pslv]] 有）。
> 所以 [[dfgp]] / [[dscp]] / [[svlr]] / 两张卡 的指向**全靠正文内联链接承载**，
> 把链接一剥（如语法节那种 `文本（raw: 路径）` 改写），读者就再也找不到它们。
>
> **⑩ 文件名里标题的问号变成了 `_`。** 本页 `title` 是
> `DRLV, DRLV? - (DRive LeVeL)`，而语料文件名是
> `02.06.02.02.89_DRLV__DRLV__-__DRive_LeVeL.md`。
> **这是语料的命名约定（问号进不了文件名），不是错字，但按名字找文件的人搜不到 `DRLV?`。**

`verified: doc-only`
