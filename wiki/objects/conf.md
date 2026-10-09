---
type: object
title: CONF, CONF? - (CONFiguration)
layer: L1
stage: project
tags: [command, pin-configuration, mode-context, dc-scale, sequencer]
related: [ctxt, dfpn, dfps, sqst, pin-config-requires-sequencer-off, pin, dc-scale-xps256-card]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.31_CONF__CONF__-__CONFiguration.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# CONF, CONF? - (CONFiguration)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **3,199 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.31_CONF__CONF__-__CONFiguration.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### CONF

```
CONF ["context",]{pin_type},[pin_oper_mode],{(pinlist)}

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98510.htm`
> 中**第 3 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 2 列。

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98510.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 2 列。
```

### CONF?

```
CONF? ["context"|ALL,] {(pinlist)}
```

returns:

```
CONF ["context",]{pin_type},{pin_oper_mode},{(pinlist)}
```

### Parameters

| context |

This extra parameter specifies a mode context. If it is omitted, the default mode context DEFAULT is set or read. If DEFAULT is the only context defined, the parameter is omitted in the query reply.

The default mode context is predefined. All other mode contexts must be defined with the CTXT command.

If you specify ALL in the query, CONF? will display all mode contexts.

 |
 | pin_type |

The mandatory parameter assigns channel resources to the pin. This can be:

 | I  | Configures a drive pin. |
 | O  | Configures a receive pin. |
 | IO  | Configures a bidirectional pin. |
 | DC |

Configures a pin for DC measurements. The pin is only connected to the PMU, and no driver or receiver resources are allocated to it.

For DC Scale channels (power or signal pins) the mode is always DC.

This option is not allowed for Smart Scale pins.

 |
 | OFF  | The pin is not available for measurements.  | |
 |

pin_oper_mode

 |

The mandatory parameter defines or indicates the operating mode of the pins in pinlist. The operation mode can be:

 | DCSIGNAL  | In the query this indicates that the pin is associated with a DC Scale channel and has been configured in PMU mode with DFPN. |
 | POWER  | In the query this indicates that the pin is associated with a DC Scale channel and has been configured in DPS mode with DFPS. |
 | CMON  | Configures the pin as current monitor output. For more information, refer to `XPS256 current monitor`（raw: `../02.05_Test_Head_Cards/02.05.05.03.03.02_XPS256_current_monitor.md`）. |
 | F160 |

Specifies Standard operating mode. This is the default. It must be selected for pins on PS1600 boards.

 |
 | F330  | Not valid. |
 | FAST |

This operation mode must be selected for fast pins. Note that no pin can be set to FAST in the default mode context DEFAULT, and that no IO pin can be set to FAST.

For Smart Scale pins this mode will be mapped to F160.

   | |
 | pinlist |

The name of the pin or pins to be configured or listed. If more than one pin is to be included, the names must be separated with a comma.

The symbol @ can be used in the query to list all pins that were previously either explicitly configured with the CONF command, or (in the case of DC Scale pins) implicitly with the DFPN or DFPS command.

 |

### Example 1

```
> CONF IO,F160,(D0,D1)
```

This example configures pins `D0` and `D1` as bidirectional pins operating in Standard Mode for the default mode context.

### Example 2

```
> CONF? (sdd,vdd)
< CONF DC,DCSIGNAL,(sdd)
< CONF DC,POWER,(vdd)
```

This example queries the DC Scale channels `sdd` and `vdd`, which were set with `DFPN`（raw: `02.06.02.02.63_DFPN__DFPN__-__DeFine_Pin_Name.md`） to PMU mode (`DCSIGNAL`) and with `DFPS`（raw: `02.06.02.02.65_DFPS__DFPS__-__DeFine_Power_Supply.md`） to DPS mode (`POWER`), respectively.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.31_CONF__CONF__-__CONFiguration.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if you attempt to configure pins while the sequencer is in the run or the break state (see the SQST command).

<!-- 报错节 end -->

## 是什么

**CONF 给针分配「类型」和「工作模式」，而且是「在某个 mode context 里」分配的。** 原文第一句：

> 「The CONF command assigns a **pin type** and an **operating mode** to the specified pins in a
> certain **mode context**. The CONF? query returns the present settings of the named pins.」

**「in a certain mode context」这半句是理解本命令的钥匙**——
同一个针在 `DEFAULT` 和别的 context 里可以是不同类型/模式，
**而 context 本身由 [[ctxt]] 定义**。

### 命令骨架（**这两段不在上面的「语法 / 参数」节里**）

**上面那一节只收了 `## Parameters` 与 `## Examples` 两节**——
**命令本身的语法块没有被脚本收进去**。原文逐字：

```
CONF ["context",]{pin_type},[pin_oper_mode],{(pinlist)}
```

```
CONF? ["context"|ALL,] {(pinlist)}
```

**返回**：

```
CONF ["context",]{pin_type},{pin_oper_mode},{(pinlist)}
```

**符号记法**：`{}` = 必需、`[]` = 可选。
（**这是推断**：依据是原文把 `pin_type` 称作 `The mandatory parameter` 而它在 `{}` 里，
而 `["context",]` 那一段的说明写 `If it is omitted…`。**原文没有给符号表**。）

### 四个参数

| 参数 | 取值 | 关键说明（原文） |
|---|---|---|
| `context` | 一个 mode context 名；查询时可用 `ALL` | 省略 = `DEFAULT`；**`If DEFAULT is the only context defined, the parameter is omitted in the query reply.`** |
| `pin_type` | `I` / `O` / `IO` / `DC` / `OFF` | **必需**；「assigns channel resources to the pin」 |
| `pin_oper_mode` | `DCSIGNAL` / `POWER` / `CMON` / `F160` / `F330` / `FAST` | 见下 |
| `pinlist` | 逗号分隔的针名；查询时可用 `@` | `If more than one pin is to be included, the names must be separated with a comma.` |

**`pinlist` 里 `@` 的含义**（原文）：
> 「The symbol @ can be used in the query to list all pins that were previously either explicitly
> configured with the CONF command, or (in the case of DC Scale pins) implicitly with the DFPN or
> DFPS command.」

**即 `@` 的覆盖面比「CONF 配过的」宽**——**DC Scale 的针是用 [[dfpn]] / [[dfps]] 隐式配的，
也算数**。

### `pin_type` 的五个取值

| 值 | 原文 |
|---|---|
| `I` | `Configures a drive pin.` |
| `O` | `Configures a receive pin.` |
| `IO` | `Configures a bidirectional pin.` |
| `DC` | `Configures a pin for DC measurements. The pin is only connected to the PMU, and no driver or receiver resources are allocated to it.` |
| `OFF` | `The pin is not available for measurements.` |

`DC` 另有三条边界（原文）：
- **`For DC Scale channels (power or signal pins) the mode is always DC.`**
- **`This option is not allowed for Smart Scale pins.`**

### `pin_oper_mode` 的取值

| 值 | 用途 |
|---|---|
| `DCSIGNAL` | **查询里**表示：该针属于 DC Scale 通道、**已用 [[dfpn]] 配成 PMU 模式** |
| `POWER` | **查询里**表示：该针属于 DC Scale 通道、**已用 [[dfps]] 配成 DPS 模式** |
| `CMON` | 把针配成电流监视输出；指向 `XPS256 current monitor`（**那篇本页没读**） |
| `F160` | **Standard 模式，这是默认值**；原文：`It must be selected for pins on PS1600 boards.` |
| `F330` | 原文只有三个字：`Not valid.` |
| `FAST` | 快针必选。**两条禁令**：`no pin can be set to FAST in the default mode context DEFAULT`、`no IO pin can be set to FAST`。**Smart Scale 的针会被映射成 `F160`** |

### DC Scale 的针：**只能读回模式，类型改不了**

这是本页最容易用错的一处。原文：

> 「CONF can also be applied to power or signal pins, that is, pins that are associated with a
> DC Scale channel. **However, you can only confirm the operation mode (power pin or signal pin)
> that is determined by the command with which they were defined (DFPN or DFPS).** You can use the
> query to retrieve the operation mode. Note that **the operation mode of power and signal pins is
> always the same in all mode contexts**.」

**两条推论**：

1. **DC Scale 针的模式是「谁定义的、就是什么」**——`DFPN` 定的就是 `DCSIGNAL`，
   `DFPS` 定的就是 `POWER`，**CONF 改不动它**（推断——原文说的是
   `you can only confirm the operation mode ... that is determined by the command with which they
   were defined`，**只说了「确认/查询」，没说能不能改；本页不把「不能改」写成文档事实**）。
2. **`always the same in all mode contexts` 是有用的硬事实**：
   **DC Scale 的针不受 context 影响**——**所以本命令的 mode context 那一维对它没有意义**。

### 一条硬约束：sequencer 在跑就报错

原文 `## Errors` 只有一句：

> 「An error is generated if you attempt to configure pins while the sequencer is in the **run** or
> the **break** state (see the SQST command).」

**这条不是「建议」，是错误**——见 [[pin-config-requires-sequencer-off]]（**那一页本页没读**）。

## 典型用法

**原文没有 `## Procedure` / `## Before you begin` 段**。从原文的 `## Examples` 能读出的只有两条：

**1. 配针**（`## Example 1`）：

```
> CONF IO,F160,(D0,D1)
```

原文的解说：`This example configures pins D0 and D1 as bidirectional pins operating in Standard Mode
for the default mode context.` ——**没写 context 就是 `DEFAULT`**。

**2. 查针**（`## Example 2`）：

```
> CONF? (sdd,vdd)
< CONF DC,DCSIGNAL,(sdd)
< CONF DC,POWER,(vdd)
```

原文的解说：这两根针是 `set with DFPN to PMU mode (DCSIGNAL) and with DFPS to DPS mode (POWER)`。
**注意回复里 `pin_type` 一律是 `DC`**——**印证上面「DC Scale 的针类型固定是 DC」那条**。

**3. 应用范围**：原文 `## Application` 写
`Pin Configuration, see Configuration Setup Commands`（`02.06.03`，**本页没读**）。

**4. 顺序上的前提**：配针之前 **sequencer 必须是 OFF**（`## Errors` 那句）。
`SQST` 是查这个状态的命令（**那篇本页没读**）。

## 和谁有关

- [[ctxt]] — **前置**。context 由 CTXT 定义；原文：
  `All other mode contexts must be defined with the CTXT command.`
  **`DEFAULT` 是预定义的，不用 CTXT 建**
- [[dfpn]] — **上游 / 同族**。DC Scale 的针在 PMU 模式下由 DFPN 分配；**`DCSIGNAL` 只能从 DFPN 来**
- [[dfps]] — **上游 / 同族**。同上，DPS 模式那一支；**`POWER` 只能从 DFPS 来**
- [[sqst]] — **状态判据**。`## Errors` 那句直接指向它
- [[pin-config-requires-sequencer-off]] — **本命令给出的一条约束**（**那页本页没读**）
- `DFUP`（**未建**）— 原文在 `connectionSet` 的说明里提了一句
  `see DFUP command`；**那是 [[dfpn]] 那篇的正文，不是本篇的**（推断——**本页不该拿它当本篇结论**）
- `Configuration Setup Commands`（`02.06.03`，**未建**）— 原文 `## Application` 指向的唯一入口
- `SQST, SQST? - (SeQuencer STate)`（**未建**）— 见上
- **同 `stage: pin` 的另一批页本页都没读**：[[digital-pins-editor]]、[[dps-pins-editor]]、
  [[utility-pins-editor]]、[[pin-configuration-file]]、[[pin-configuration-tool]]、
  [[pin-group-editor]]——**它们是同一件事的 GUI 侧 / 文件侧**，
  **但本页不能替它们说话**（推断，仅指关系）

## 版本

原文 `## Functional changes` 四条：

- **`Introduced before SmarTest 6.3.2`**
- **SmarTest 7.1.3**：`Added HV option for the pin_oper_mode value`
- **SmarTest 7.3.1**：`New operating modes STDDIFF and FASTDIFF added.`
- **SmarTest 7.10.2**：`New operating mode CMON added.`

**三点必读：**

1. **第一条是 §11.2② 的哨兵值**，不是「6.3.2 新增了 CONF」。
2. **`7.1.3` 和 `7.3.1` 这两条记的三个取值，在本文档的参数表里一个都查不到**——
   参数表的 `pin_oper_mode` 只列了 `DCSIGNAL` / `POWER` / `CMON` / `F160` / `F330` / `FAST`
   （**见上 ⚠️②**）。
3. **`7.10.2` 那条和参数表对得上**：`CMON` 在表里、并指向 `XPS256 current monitor`。
   ——**四条里只有这一条能在本篇自洽**。

## 出处

`sources:` 一篇：
`02_System_reference/02.06_Command_Reference/02.06.02.02.31_CONF__CONF__-__CONFiguration.md`
（`98510.htm`，4,984 字节，129 行）——**整篇读完**。

**本页没做的**：

- **「语法 / 参数」节只收了 `## Parameters` 和 `## Examples` 两节，134 行里收了 2,769 字符。**
  **`## CONF` / `## CONF?` 两个命令骨架和它们的 `returns` 块没有进那一节**——
  本页正文里那三段是我**从 raw 逐字抄的**（**不在语法节里，所以不算「改语法节」**）。
  同理 `## Application` / `## Errors` / `## Functional changes` 三节也没进。
- **`Configuration Setup Commands`（`02.06.03`）没读**——**CONF 在整场 setup 里的位置本页不知道**。
- **`SQST, SQST?` 那篇没读**——`run` / `break` 之外还有哪些状态、`SQST` 返回什么，本页没有。
- **`XPS256 current monitor` 没读**——**`CMON` 到底把针配成什么，本页只有一个词。**
- **`DFPS`（`02.06.02.02.65`）没读**——**本页凡提 DFPS 处，依据只是本篇的这几句话。**
- **`DFPN`（`02.06.02.02.63`）本页读了**（**见 [[dfpn]]**），但
  **strictly 地说那不是本篇的内容**——本页引它的地方已标明。
- **`Configuration Setup Commands` 里那一族页、以及 GUI 侧那几个 editor 页，一篇都没读。**
- **一张图都没有**（**本篇 raw 里没有图片引用**）。
- **`## Errors` 只有一句**——**除了 sequencer 状态，还有没有别的报错条件，本页写不了。**
- **`HV` / `STDDIFF` / `FASTDIFF` 三个取值本页只能报到名字**，
  **它们的语义本篇一个字没给**（见下 ⚠️②）。

> ⚠️ **本篇的语料瑕疵，照实记、一处没替它改**：
> ① **`pin_oper_mode` 是「必需」还是「可选」，同一篇里两处相反**：
>    正文写 `pin_oper_mode` 那段的第一句是
>    `The mandatory parameter defines or indicates the operating mode of the pins in pinlist.`
>    （**mandatory**），而命令骨架里它是 `CONF ["context",]{pin_type},[pin_oper_mode],{(pinlist)}`
>    —— **方括号，即可选**。**两处不能同时成立，本页不判。**
> ② **三条版本记录记的取值，参数表里全都没有**：`SmarTest 7.1.3: Added HV option for the
>    pin_oper_mode value`、`SmarTest 7.3.1: New operating modes STDDIFF and FASTDIFF added.`
>    —— 而参数表的 `pin_oper_mode` 清单是 `DCSIGNAL` / `POWER` / `CMON` / `F160` / `F330` /
>    `FAST`，**`HV` / `STDDIFF` / `FASTDIFF` 一个都没有**。
> ③ **表里有一行取值的「说明」是「无效」**：`| F330  | Not valid. |`
>    —— **一个列在参数表里的取值，唯一的说明是它无效。**
> ④ **`DC` 那一行的表格结构破了**：raw 里是 `| DC |` 之后**另起一行**写描述
>    （`Configures a pin for DC measurements. …`），**描述没在表格单元里**；
>    `pin_oper_mode` 的 `F160` 那一格同样是断的。**这是 raw 的表格被拆散**，
>    同 [[xps256-status-flags]] 记的那种现象。
> ⑤ **`OFF` 那一行尾部多两个空单元**：`| OFF  | The pin is not available for measurements.  | |`
>    —— **行尾多了一个 `|`**。原文如此。

`verified: doc-only`
