---
type: object
title: DSCP, DSCP? - (Define System Control Parameter)
layer: L1
stage: project
tags: [dscp, firmware-command, sequencer-memory, parameter-set, project-setup, resource-limits]
related: [technology-file-for-a-device, sequencer, sequencer-status, waveform-set, timing-setup-commands, level-setup-tool, equation-based-level-setup, dtcp, smartest-6.3.2]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md
created: 2026-09-18
updated: 2026-09-20
verified: doc-only
---

# DSCP, DSCP? - (Define System Control Parameter)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **4,100 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### DSCP

```
DSCP `[device_cycle`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_device_cycle`）], `[waveform_set`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_waveform_set`）], `[timing_set`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_timing_set`）], `[level_set`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_level_set`）], `[dps_set`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_dps_set`）], `[pmu_set`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_pmu_set`）],
                        `[devicecycle_set`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_devicecycle_set`）], `[routing_set`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_routing_set`）], `[period_res_prec`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_period_res_prec`）],

```

### DSCP?

```
DSCP?
```

returns:

```
DSCP {device_cycle}, {waveform_set}, {timing_set}, {level_set}, {dps_set},
       {pmu_set}, {devicecycle_set}, {routing_set}, [period_res_prec],
       [period_res_compatibility_model]
```

### Parameters

| device_cycle  | The device_cycle parameter is an integer that defines the absolute maximum number of device cycles that you can create for one pin.

Default: 256

Maximum: 16384

Note that the total number of device cycles gets evenly divided between the combined number of waveform sets and wavetables. If you use the default values, then 256 device cycles divides into the total number of 32 `waveform sets and wavetables`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_waveform_set`） to give you 8 device cycles per waveform set/wavetable. If you choose values that do not divide evenly, then the number of device cycles will be rounded up to the next multiple of the `waveform_set`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md#_98578__row_waveform_set`） parameter.

 |
 | devicecycle_set |

The devicecycle_set parameter is an integer that defines the maximum number of device cycle sets that you can create. Device cycle sets are needed for selective digital capture.

Default: 1

Maximum: 128

 |
 | dps_set |

The dps_set parameter is an integer that defines the maximum number of DPS sets you can create.

Default: 32

Maximum: 256

 |
 | level_set |

The level_set parameter is an integer that defines the combined total of level sets for fixed and equation based levels that you can create.

Default: 32

Maximum: 256

 |
 | period_res_prec |

This parameter defines the precision with which the period resolution is calculated by the system. It has no effect on a user defined period resolution (using, for example, the period_res keyword in the equation set).

The default is 4, if the .technology file does not contain this parameter.

If it does, the value of the .technology file is the default.

This value is set to 9, the greatest possible value, when a device is created.

 |
 |

pmu_set

 |

The pmu_set parameter is an integer that defines the maximum number of actions that can be contained in all measurement sets of all PPMU DC sets.

Default: 1024

Maximum: 12800

 |
 | routing_set |

Defines the number of routing sets managed by the firmware, provided by the MCD.

Default: 256

Maximum: 512

 |
 | timing_set |

The timing_set parameter is an integer that defines the maximum combined total of timing sets for fixed and equation based timing you can create.

Default: 256

Maximum: 999

The number of timing sets must be equal to or greater than the number of waveform sets, as there must be at least one timing set per waveform set.

 |
 | waveform_set |

The waveform_set parameter defines the maximum combined total of waveform sets (fixed timing) and wavetables (equation based timing) you can create. Thus, if you specify a value of 32, you could, for example, create 10 waveform sets and 22 wavetables.

Default: 32

Maximum: 128

 |

### Example

```
DSCP 256,16,256,32,32,1024,16,1,256,
```

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

- The number of device cycles defined is out of range.
- The number of waveform sets defined is out of range.
- The number of timing sets defined is out of range.
- The number of level sets defined is out of range.
- The number of DPS sets defined is out of range.
- The specified set size is too large for the memory configuration.
- The specified number of timing sets is smaller than the number of waveform sets.

<!-- 报错节 end -->

## 是什么

**`DSCP` 是固件命令：说明各类 parameter set「最多能有几个实例」，并在 Sequencer Memory 里
为它们预留空间。** 原文逐字：

> 「The DSCP command serves to define the maximal number of instances for the different types of
> so called parameter sets, and to reserve the necessary space for them in the Sequencer Memory.
> The space can be calculated from the number of instances because every instance of the same type
> has the same size. The DSCP? query returns the existing settings. This command replaces the
> command CNTR, CNTR? used in previous releases.」

**四件事**：报**实例数量** → 在 Sequencer Memory 里**预留空间** → **`DSCP?` 是查询** →
**它取代了旧版的 `CNTR` / `CNTR?`。**

**「预留空间」能算出来，是因为同类实例大小相同**——**数量 × 单实例大小 =
要预留的空间**（原文的 `The space can be calculated from the number of instances because every
instance of the same type has the same size.`）。

### 调用时机，和一条「会清空」的硬警告

**时机**：`DSCP is called every time you switch to another device.`
——**每次切到另一个 device 都会调一次。**

**值从哪来**：可以写进 device 主目录下的 `.technology` 文件；
`For parameters not defined in the technology file, DSCP uses the defaults specified below.`
——**没写的用下面那些默认值。**

**最重的一条**，原文逐字（`Note`，**行首还多一个空格**）：

> 「Note Every call of DSCP deletes all data that were previously contained in the Sequencer
> Memory. Therefore, you have to reload the device setup after changing parameters using the DSCP
> command.」

**即：每调一次就删掉 Sequencer Memory 里原有的一切数据；所以用 DSCP 改完参数必须重载
device setup。**

### 九个位置参数，顺序固定（**顺序只在原文正文，不在语法节**）

`DSCP` 的用法行（原文里在 `## DSCP` 一节，**语法节没有抽这一节**）：

```
DSCP [device_cycle], [waveform_set], [timing_set], [level_set], [dps_set], [pmu_set],
     [devicecycle_set], [routing_set], [period_res_prec],
```

**九个都是位置参数，逗号分隔。`DSCP?` 不收参数，返回十个值**：

```
DSCP {device_cycle}, {waveform_set}, {timing_set}, {level_set}, {dps_set},
     {pmu_set}, {devicecycle_set}, {routing_set}, [period_res_prec],
     [period_res_compatibility_model]
```

**多出来的第十个是 `period_res_compatibility_model`，原文没有给它任何说明**（见 `## 出处` ③）；
**而且返回串里 `{}` 与 `[]` 两种括号混用**（前八个 `{}`、后两个 `[]`），
**原文没说这个差别是什么意思。**

### 九个参数：默认值 / 上限 / 一句话

| 位置 | 参数 | 数的是什么（**原文**） | 默认 | 上限 |
|---|---|---|---|---|
| 1 | `device_cycle` | 每个 pin 能创建的 device cycle 的**绝对最大数** | `256` | **`16384`** |
| 2 | `waveform_set` | waveform set（fixed timing）+ wavetable（equation based timing）**合计** | `32` | `128` |
| 3 | `timing_set` | timing set：fixed 与 equation based **合计** | `256` | **`999`** |
| 4 | `level_set` | level set：fixed 与 equation based **合计** | `32` | `256` |
| 5 | `dps_set` | DPS set 数 | `32` | `256` |
| 6 | `pmu_set` | **所有 PPMU DC set 的所有 measurement set 里的动作总数** | `1024` | **`12800`** |
| 7 | `devicecycle_set` | device cycle set 数（**选择性数字捕获要用它**） | **`1`** | `128` |
| 8 | `routing_set` | **固件管理的 routing set 数，由 MCD 提供** | `256` | `512` |
| 9 | `period_res_prec` | 系统算 period resolution 的**精度** | **`4`**（或 `.technology` 里的值） | **`9`**（原文说它是 `the greatest possible value`） |

**五条要紧的：**

**① `device_cycle` 与 `waveform_set` 联动。** 逐字：

> 「Note that the total number of device cycles gets evenly divided between the combined number of
> waveform sets and wavetables. If you use the default values, then 256 device cycles divides into
> the total number of 32 waveform sets and wavetables to give you 8 device cycles per waveform
> set/wavetable. If you choose values that do not divide evenly, then the number of device cycles
> will be rounded up to the next multiple of the waveform_set parameter.」

**即：`device_cycle` 是「一个 pin 的总量」，按「waveform set + wavetable 的总数」均分；
除不尽就向上取整到 `waveform_set` 的倍数。默认值下是 `256 / 32 = 8`。**

**② `timing_set` 与 `waveform_set` 有硬大小关系。** 逐字：

> 「The number of timing sets must be equal to or greater than the number of waveform sets, as
> there must be at least one timing set per waveform set.」

**每个 waveform set 至少要有一个 timing set，所以 `timing_set ≥ waveform_set`。**
**违反它会报错**（见下 `Errors` 第 7 条）。**这也解释了默认值为什么是 `256` 与 `32`。**

**③ `period_res_prec` 的默认值有两个来源。** 原文三句逐字：

> 「The default is 4, if the .technology file does not contain this parameter.」
> 「If it does, the value of the .technology file is the default.」
> 「This value is set to 9, the greatest possible value, when a device is created.」

**前两句**：`.technology` 里没有 → `4`；有 → 用文件里的。
**第三句**：创建 device 时它被设成 `9`。
**（推断）所以「默认 4」是命令这一侧的默认，而实际建出来的 device 上是 9**——
**依据只是前两句说 default、第三句说 `when a device is created`；
原文没把这两件事对齐，所以这是推断，不是原文明写的。**

**它还只管系统自己算的那一份**：逐字
`It has no effect on a user defined period resolution (using, for example, the period_res keyword
in the equation set).` ——**用户自己定义的 period resolution 不受它影响。**

**④ `pmu_set` 数的不是 set 的个数。** 原文写它是
`the maximum number of actions that can be contained in all measurement sets of all PPMU DC
sets` ——**是所有 PPMU DC set 里所有 measurement set 里**动作**的总数**。
**和 `dps_set` / `level_set` 那几个「set 有几个」不是一个量纲。**

**⑤ `routing_set` 是唯一一条措辞不合群的。** 其余八条一律以
`The xxx parameter is an integer that defines …` 开头，
**只有它是 `Defines the number of routing sets managed by the firmware, provided by the MCD.`**
——**没有「它是整数」这个主句，而且把「谁提供」写进了定义里（MCD）。**

### `Errors`：七种情况会报错

原文 `## Errors` 是 `An error is generated if:` 加七条 bullet（**这七条不在语法节里**）：

| # | 报错条件（**原文**） |
|---|---|
| 1 | `The number of device cycles defined is out of range.` |
| 2 | `The number of waveform sets defined is out of range.` |
| 3 | `The number of timing sets defined is out of range.` |
| 4 | `The number of level sets defined is out of range.` |
| 5 | `The number of DPS sets defined is out of range.` |
| 6 | `The specified set size is too large for the memory configuration.` |
| 7 | `The specified number of timing sets is smaller than the number of waveform sets.` |

**两处要注意：**

- **只有五个参数有「out of range」条目**：`device_cycle` / `waveform_set` / `timing_set` /
  `level_set` / `dps_set`。**`pmu_set` / `devicecycle_set` / `routing_set` / `period_res_prec`
  超范围时报不报错，原文没说。**
- **第 6 条换了一个维度**：不是「超出自己的上限」，而是
  `too large for the memory configuration` ——
  **即九个参数各自都在上限内，总量仍可能装不进 Sequencer Memory。**
  **它和第 7 条是两条独立于「范围检查」的约束。**

### `Application`

原文 `## Application` 只有一句：`Test Setup, see Introduction to firmware commands.`
——**它属于 Test Setup 阶段**（与 frontmatter 的 `stage: project` 对应）。

## 典型用法

**原文有一个 `## Example`（已在语法节里逐字），没有 `## Procedure`、没有 `## Before you begin`。**
例子只有一行：

```
DSCP 256,16,256,32,32,1024,16,1,256,
```

**按 `## DSCP` 那行的顺序对回去**：

| 位置 | 参数 | 例子里的值 | 对照默认 |
|---|---|---|---|
| 1 | `device_cycle` | `256` | = 默认 |
| 2 | `waveform_set` | `16` | 默认 `32` 的一半 |
| 3 | `timing_set` | `256` | = 默认 |
| 4 | `level_set` | `32` | = 默认 |
| 5 | `dps_set` | `32` | = 默认 |
| 6 | `pmu_set` | `1024` | = 默认 |
| 7 | `devicecycle_set` | `16` | 默认 `1`——**这一项是主动放大的** |
| 8 | `routing_set` | `1` | 默认 `256`——**这一项是主动缩小的** |
| 9 | `period_res_prec` | `256` | **超出上限 `9`**（见 `## 出处` ④） |

**例子末尾还多一个逗号**，**第十个值（`period_res_compatibility_model`）没给。**

**从原文能落成的动作：**

| 要做的 | 依据 |
|---|---|
| **改参数之前先接受「会清空」** | 原文 `Note`：每调一次 DSCP 就删掉 Sequencer Memory 里原有的数据 |
| **改完必须重载 device setup** | 同一句 `Note` 的后半 |
| **要让它每次切 device 时自动生效** | 把值写进 `.technology` 文件；**没写的参数用原文那套默认值** |
| **设 `timing_set`** | **必须 ≥ `waveform_set`**，否则报错（`Errors` 第 7 条） |
| **设 `device_cycle`** | 记住它会被 `waveform_set + wavetable` 的总数均分，除不尽向上取整到 `waveform_set` 的倍数 |
| **要选择性数字捕获** | 需要 `devicecycle_set`——**默认只有 `1`** |
| **排完九个值之后** | 还要保证总量装得进 Sequencer Memory（`Errors` 第 6 条，独立于范围检查） |

## 和谁有关

- [[technology-file-for-a-device]] — **上游，值的来源**。原文两处点它：
  `You can specify the parameter values of this call in the technology file (.technology), which
  is located in the main directory of every device.`，
  以及 `For parameters not defined in the technology file, DSCP uses the defaults specified below.`
  **而 `period_res_prec` 的默认值直接取决于 `.technology` 里有没有它。**
  **本页只有「能写在那儿、没写就用默认」这两句，文件本身的结构在那页。**
- [[sequencer]] — **被预留、又被清空的那块内存的宿主**。
  原文说 DSCP 的作用是 `to reserve the necessary space for them in the Sequencer Memory`，
  而且**每调一次就 `deletes all data that were previously contained in the Sequencer Memory`**。
  **本页只有这块内存的容量语义（几个实例、多大），sequencer 本身怎么跑在那页。**
- [[sequencer-status]] — **（推断）状态侧**。
  `DSCP?` 返回的是「当前设置」（`the existing settings`），
  [[sequencer-status]] 从名字看是 sequencer 的状态；
  **依据只是「一个是设置、一个是状态，都落在 sequencer 上」。本页没有那页的任何事实。**
- [[waveform-set]] — **`waveform_set` 数的那种对象**。
  原文那格逐字说它数的是
  `the maximum combined total of waveform sets (fixed timing) and wavetables (equation based
  timing)`；**`device_cycle` 的均分规则也是按「waveform set + wavetable 的总数」算的。**
  **本页只有「能有几个」，一个 waveform set 里面是什么在那页。**
- [[timing-setup-commands]] — **（推断）`timing_set` 的同族命令**。
  `timing_set` 那格说它数的是 fixed 与 equation based 两种 timing set 的合计；
  **依据是页名指向时序设置命令。本页没有那页的任何事实。**
- [[level-setup-tool]] / [[equation-based-level-setup]] — **`level_set` 那一格的两个来源**。
  原文逐字说它数的是
  `the combined total of level sets for fixed and equation based levels`；
  **fixed 与 equation based 这两条路各自怎么走，在那两页。**
- [[dtcp]] — **（推断）同族的另一个定义命令**。原文 `Related information` 直接链到
  `DTCP, DTCP? - (Define Technology Control Parameters)`；
  **从名字看是本命令在 technology 那一侧的对应物。本页没有那页的任何事实。**
- [[smartest-6.3.2]] — **版本页**。本页 `## 版本` 唯一的落点。
- `Introduction to firmware commands`（**未建**）— **原文 `Application` 指向它**：
  `Test Setup, see Introduction to firmware commands.`
  **本页只有 `Test Setup` 这个阶段名，固件命令整体的用法与前置在那篇，本页没读。**
- `System preparation by firmware commands`（**未建**）— **原文把「参数怎么选」推给它**：
  `Refer to System preparation by firmware commands for details about parameter selection.`
  **那条「会清空」的 `Note` 就是以它为出口的，本页没读。**
- `CNTR` / `CNTR?`（**未建**）— **本命令取代的旧命令**。原文只有一句
  `This command replaces the command CNTR, CNTR? used in previous releases.`
  **两者的参数、单位、上限差别，本页一个字都没有。**
- `MCD`（**未建**）— `routing_set` 那格里唯一的来源方（`provided by the MCD`），
  **原文没解释 MCD 是什么，本页也不知道。**
- `period_res_compatibility_model`（**未建**）— **`DSCP?` 返回的第十个值**，
  **原文没有给它任何说明**（见 `## 出处` ③）。

## 版本

本文档**有** `## Functional changes` 段，**只有一条**（逐字）：

- **Introduced before SmarTest 6.3.2**

**这一条是 §11.2 ② 那个哨兵。** `Introduced before SmarTest 6.3.2` 的意思是
**「早于语料覆盖范围」**，**不是「6.3.2 新增」**——
**所以 DSCP 本身成立于哪个版本，这份语料里没有。**

**（推断）它不会太晚**：原文说它取代了 `CNTR, CNTR? used in previous releases`，
**说明在被取代的那个版本里就已经有后继了**——
**依据只是这一句，原文没给任何版本号，所以这是推断。**

**版本段里没有 `DSCP?` 的条目**，尽管它是同一篇文档的一节，
而且返回串里多一个没有说明的 `period_res_compatibility_model`——
**那个值是什么时候加进来的，语料里没有。**

**与 wiki 面向版本的关系**：本 wiki 目标是 **SmarTest 7.10.3**，
而这一篇**连一条 7.x 的条目都没有**——**所以本页只能确认「6.3.2 之前就有」；
7.10.3 时的行为与那之前是否一致，语料里没有依据。**

## 出处

`sources:` 一篇：
`02_System_reference/02.06_Command_Reference/02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md`

**本页没做的：**

- **`DSCP` / `DSCP?` 的用法行是本页从原文正文转述的，不是语法节抽的。**
  语法节里只有 `### Parameters` 与 `### Example` 两节（脚本的段标记就是这两个），
  **原文的 `## DSCP` 与 `## DSCP?` 两节的代码块没有进语法节**——
  **所以那两段要精确到逗号与括号，得回原文第 17–34 行。**
- **`## Application` 与 `## Errors` 两节也没进语法节**（同上），
  **本页正文里那七条 Errors 是从原文转述的。**
- **`Introduction to firmware commands` 没读** —— 所以 `Test Setup` 是哪个阶段、
  固件命令怎么发、有什么前置，**本页只有那个阶段名。**
- **`System preparation by firmware commands` 没读** —— **这是本页最大的空缺**：
  原文把它指定为「参数怎么选」的出处，**而本页只能给出九个参数的默认值与上限，
  给不出「该往哪个方向选」。**
- **`.technology` 文件本身没读** —— 所以 `period_res_prec` 的默认值怎么落地、
  **别的参数能不能也写进去、写进去的语法是什么，本页不知道**
  （只知道「能写」与「没写就用默认」）。
- **`DTCP` 没读** —— 所以同族的另一个控制参数命令长什么样、和本命令什么关系，
  **本页只有 `Related information` 里那个名字。**
- **`CNTR` / `CNTR?` 没读（也没有对应文档被链出）** —— 所以**新旧命令在参数、单位、
  上限上的差别，本页一个字都没有。**
- **`Sequencer Memory` 的容量没读** —— 所以 `Errors` 第 6 条
  `The specified set size is too large for the memory configuration.`
  **在什么阈值上触发，本页不知道**；本页只有九个参数各自的上限，**没有总量上限。**
- **`MCD` 没读、原文也没解释** —— 所以 `routing_set` 那格里
  `managed by the firmware, provided by the MCD` 的 MCD 是什么，**本页和原文一样不知道。**
- **一个 waveform set / timing set / level set 的实例里装什么，本页完全没有** ——
  本页只讲「各有几个」。**那部分在 [[waveform-set]] / [[timing-setup-commands]] /
  [[level-setup-tool]] 那几页，本页都没读。**
- **一张图都没有。** 原文没有图片。
- **没有交叉验证任何别处的文档**（§11：本页只写这一篇里有的）。
  **尤其：本页 `layer: L1`、`stage: project`，所以本页没有去别处找它的层级定位。**

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> **① `Note` 那一行行首多一个空格，`Note` 后面也没有分隔符。** 逐字（**注意开头的空格**）：
> ` Note Every call of DSCP deletes all data that were previously contained in the Sequencer
> Memory.`
> ——**这个行首空格是原文就有的**（在 markdown 里会让这一行缩进成代码块或段落续行，
> 看渲染器）。**本页引文照原样，正文里改成正常段落。**
>
> **② `## Parameters` 那张表没有表头，而且 `pmu_set` 那一行被孤立的 `|` 打断。** 逐字：
> ```
>  |
>  |
> pmu_set
>  |
> ```
> ——**`pmu_set` 前面少一个 `|`**，所以它的行首与别的参数都不同
> （**这在语法节里也看得出来：别的条目都在 `| xxx |` 里，只有 `pmu_set` 那行是裸的**）。
> **同一处还多出两个孤立的 `|` 行。本页照实说，不替它补竖线。**
>
> **③ `DSCP?` 返回串里多一个没有说明的值。** 逐字：
> `DSCP {device_cycle}, {waveform_set}, {timing_set}, {level_set}, {dps_set},
> {pmu_set}, {devicecycle_set}, {routing_set}, [period_res_prec],
> [period_res_compatibility_model]`
> ——**`period_res_compatibility_model` 在 `## Parameters` 一节里没有任何对应条目**
> （那一节只有九个参数）。**本页并列两处，不替它编说明。**
>
> **④ 例子里最后一个值超出 `period_res_prec` 的上限。** 例子逐字：
> `DSCP 256,16,256,32,32,1024,16,1,256,`
> 按 `## DSCP` 那行的九参数顺序对回去，**第九个 `period_res_prec` = `256`**，
> 而正文说它 `Default: 4`、`the greatest possible value` 是 `9`。
> **两种可能，原文都没排除，也都不是明写的**：
> **(a) 例子是旧命令 `CNTR` 时代留下的**（原文说 DSCP 取代了 CNTR）；
> **(b) 末尾那个 `256` 不是 `period_res_prec`**，即例子的参数顺序与 `## DSCP` 那行不一致。
> **本页把 (a)(b) 并列，不判哪个对，也不替例子改值。**
> **另外例子末尾多一个逗号**（`…,256,`），**第十个值没给。**
>
> **⑤ `DSCP?` 返回串的括号两种混用。** 前八个用 `{}`、后两个用 `[]`；
> **而 `DSCP` 那行的九个参数一律用 `[]`**。
> **原文没说这两组括号的差别是什么意思。本页照实并列，不替它统一。**
>
> **⑥ 官方名字带问号，而文件名里的问号被换掉了。** 本页 `title` 是
> `DSCP, DSCP? - (Define System Control Parameter)`，
> 而语料文件名是 `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md`
> ——**文件名里 `DSCP?` 的问号变成了 `_`。**
> **这是语料的命名约定（问号进不了文件名），不是错字，但会让按名字找文件的人搜不到 `DSCP?`。**
>
> **⑦ `routing_set` 是唯一一条措辞不合群的说明。** 其余八条一律以
> `The xxx parameter is an integer that defines …` 开头，
> **只有它是 `Defines the number of routing sets managed by the firmware, provided by the MCD.`**
> ——**少了「它是整数」这个主句，也少了主语。**
>
> **⑧ `Errors` 只覆盖九个参数里的五个。** 七条 bullet 里前五条分别对应
> `device_cycle` / `waveform_set` / `timing_set` / `level_set` / `dps_set` 的「超范围」，
> **`pmu_set` / `devicecycle_set` / `routing_set` / `period_res_prec`
> 四个超范围时是否报错，原文没说。**
> **而第 6 条换了一个维度**——不是「超自己的上限」，而是「装不进内存」，
> **它和第 7 条是本页两条独立于范围检查的约束。**
>
> **⑨ `## Related information` 两个链接粘在一起**，中间没有分隔符：
> `Technology file for a device` + `DTCP, DTCP? - (Define Technology Control Parameters)`。
> **（这一篇只有两个链接，比同类页少。）**
>
> **⑩ 正文里的指代全靠链接承载。** 原文写
> `Refer to System preparation by firmware commands for details about parameter selection.`
> 与 `For more information on the .technology file refer to Technology file for a device.`
> ——**把链接一去掉（比如语法节那种 `文本（raw: 路径）` 改写），就只剩一个光秃秃的句子。**
> **`Application` 那节更短**：`Test Setup, see Introduction to firmware commands.`
> ——**`see` 后面直接跟名字，没有逗号、没有书名号。**
>
> **⑪ `DSCP?` 一节里的 `returns:` 是一个裸词行**，**既不是标题也不是列表项**，
> 所以在结构上它和后面的代码块是两块，中间没有从属关系。
> **语法节没有抽这一节（见上），所以这个结构问题只留在原文里。**
>
> **⑫ 本篇没有 §11.2 ① 那种 `鈥` 形态的编码损坏**（本页查过 `鈥`，0 处）。
> **注意 `鈮`（`≥`）那一类本篇也没有**——那是 [[global-section]] 那篇的问题，不是这一篇。

`verified: doc-only`
