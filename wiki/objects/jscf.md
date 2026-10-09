---
type: object
title: JSCF, JSCF? - (Jitter Set ConFiguration)
layer: L1
stage: timing
tags: [timing, jitter, jitter-injection, jscf, l1-command, firmware-command]
related: [jsdf, jspr, psfc, timing]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.147_JSCF__JSCF__-__Jitter_Set_ConFiguration.md
created: 2026-09-18
updated: 2026-09-20
verified: doc-only
---

# JSCF, JSCF? - (Jitter Set ConFiguration)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,180 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.147_JSCF__JSCF__-__Jitter_Set_ConFiguration.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### JSCF

```
JSCF {"jitter_set_name"}, {"property"}, {"property_value"}, {(pinlist)}
```

### JSCF?

```
JSCF? {"jitter_set_name"|ALL|PRM}, {"property"|ALL}, {(pinlist)}
```

returns:

```
JSCF {"jitter_set_name"}, {"property"}, {"property_value"}, {(pinlist)}
```

### Parameters

| jitter_set_name | Specifies the name of a jitter set that must have been defined with JSDF. |
|---|---|
| property | Specifies a property of the jitter set. For a list see the table below. |
| ALL | This value can be specified in the query to retrieve the configuration data of all jitter sets. |
| PRM | This value can be specified in the query to retrieve the configuration of the current primary jitter set. |
| property_value | Specifies the value for the specified property. The values that are admitted for the individual properties are listed in the table below. |
| pinlist | Specifies the pins to which this configuration is to be applied. |

### Example

```
> JSCF? "my_J_SET",ALL,(Pin1)
< JSCF "my_J_SET",MODE,CONT,(Pin1)
< JSCF "my_J_SET",WAVEFORM,"-100,-50,0,50,100,50,0,-50",(Pin1)
< JSCF "my_J_SET",PERIODFACTOR,25,(Pin1)
```

This example defines a simple sawtooth waveform with a peak-to-peak value of 200ps for a STDDIFF or STD pin.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.147_JSCF__JSCF__-__Jitter_Set_ConFiguration.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if no jitter set with the specified name exists.

<!-- 报错节 end -->

## 是什么

**JSCF 是「把抖动（jitter）注入到指定 pin 上」的配置命令。** 原文第一句就是它的全部职责：

> 「This command serves to define and query the jitter injection for the specified pins.」

**两个前提是硬性的，缺一个这条命令就没有意义：**

| 前提 | 原文依据 | 不满足会怎样 |
|---|---|---|
| **目标 jitter set 必须已经存在** | `The specified jitter set must have been defined with JSDF.` | 报错：`An error is generated if no jitter set with the specified name exists.` |
| **只对「有 setup focus 的 site」生效** | `With this command you configure setups of those sites that have the setup focus` | **焦点之外的 site 不受影响**——**命令不报错，只是改到了别处（推断，依据是原文那句 `those sites that have the setup focus`；原文没有描述「焦点没设对」时会发生什么）** |

**带 `?` 与不带 `?` 是同一件事的两半**：`JSCF` 写，`JSCF?` 读，
**回复的格式与写入格式逐字一致**（原文 `## JSCF?` 一节只写了 `returns:`，下面就是把写入格式抄了一遍）：

```text
JSCF {"jitter_set_name"}, {"property"}, {"property_value"}, {(pinlist)}
```

### 十个属性：**一半是「抖动长什么样」，一半是「什么时候抖」**

`## Properties and their values` 一节列了全部可写属性。**这是本页最该记住的一张表**——
「语法 / 参数」节里只有参数名，**取值一个都没有**，全在这一节：

| 属性 | 取值 | 说明 |
|---|---|---|
| **MODE** | `OFF`（默认）/ `CONT` / `RESTART` | **什么时候抖**，见下面那三行 |
| **MODULATION_SETS** | 一个或两个 modulation set 名 | **与其它属性互斥**，见下面那条硬约束 |
| **WAVEFORM** | 逗号分隔的偏移量列表，**最多 512 项**；或关键字 `SINUSOIDAL` / `RECTANGLE` / `TRIANGLE` | 要么自定义波形，要么选一个预定义波形 |
| **PERIODFACTOR** | 整数 n，默认 **1**，最大 **1024** | **只对自定义波形有效**；步长 = `n` 倍的 `2 * clock_resolution` |
| **PHASE** | 度数，**最大 360°** | **只对预定义波形有效**，且是为 `RESTART` 模式准备的 |
| **AMPLITUDE** | 最大 **200 ps**，默认 **100 ps** | 预定义波形的幅度（**原文：`half of the peak-to-peak value`**） |
| **PERIOD** | 最大 `2 * clock_resolution * 1024 * 512` ps | 预定义波形的周期 |
| **DUTYCYCLE** | 默认 **50%** | **只对 `TRIANGLE` 与 `RECTANGLE` 有效** |
| **NOISE** | 最大 **400 ps**，默认 **0** | 给每个波形叠加随机噪声 |
| **ALLOWED_NOISE** | — | STD / STDDIFF pin 上，预定义波形**两个采样点之间的最大允许步宽**；超了**发错误信息** |

**`MODE` 的三个取值就是「什么时候抖」的全部答案：**

| 取值 | 原文 | 读法 |
|---|---|---|
| `OFF` | `No jitter injection takes place. This is the default.` | **不抖。默认值。** |
| `CONT` | 「Jitter injection is started with the first functional test and then keeps running until it is explicitly terminated.」 | **跑起来就不停**，直到被显式终止 |
| `RESTART` | 「Jitter injection is stopped after every functional test and restarted with the next functional test.」 | **每个 functional test 重来一次** |

### 一条硬约束：`MODULATION_SETS` 一写，别的属性基本都不能写

原文在**正文和属性表里各说了一次**，措辞不同、意思相同：

> 「Note that there are certain incompatibilities between the properties that can be defined with JSCF.
> The MODULATION_SETS property excludes all the other properties except MODE.」

> 「Note also that when you specify this property, you cannot specify any of the other properties except MODE.」

**即：`MODULATION_SETS` + `MODE` 是一组，其余八个属性是另一组，两组不能混着写。**
原文把它讲成**两条组织 jitter setup 数据的路子里的一条**
（`Two ways of organizing jitter setup data`）——
**这是互斥的两套写法，不是两种风格。**

### 自定义 `WAVEFORM` 的数值限制（**原文给了公式**）

`WAVEFORM` 写成一串数时，这些数是 **相对当前 active timing set 的 edge delay 的偏移，单位 ps**
（原文：`a list of offsets from the edge delays specified in the currently active timing set`）。三条限制：

| 限制 | 原文 |
|---|---|
| **偏离 timing set 的上限** | `The maximum offset from the delay defined in the timing set is 200 ps in either direction.` |
| **后一项比前一项小时的差值上限** | `max_diff = clock_resolution/2 - 410 ps` |
| **项数上限** | `the maximum number of items is 512` |

**`clock_resolution` 不是你能直接设的量**（原文：`The clock resolution is calculated from the period resolution, but also takes other parameters into account.`）。
要完全掌控它，原文只给了这一条路：

> 「If you want to have complete control over the clock resolution, you must specify a period resolution not
> greater than `2 * minimal_clock_resolution` manually (with the period_res keyword). Then the clock
> resolution will equal the period resolution.」

### site 焦点：一句管辖**所有固件查询**的话

原文把焦点的规矩写成了通用行为，**不是只对 JSCF 说的**：

> 「With this command you can retrieve site specific information (only one site can be in focus at a time).
> For the site in focus, SmarTest displays results in the Testflow Editor and in the result tools.
> Also, any firmware queries report setup and results for the site currently in focus only.」

**推论（推断）：`JSCF?` 的回复只代表「当前焦点 site」的配置。**
依据是最后那句 `any firmware queries report setup and results for the site currently in focus only.`——
`JSCF?` 属于固件查询（frontmatter `layer: L1`），**故被这句盖住**。
**原文没有单独为 `JSCF?` 说这句话**，本页不把它升格成文档事实。

### `JSCF?` 的两个特殊取值

| 写什么 | 得到什么 | 原文 |
|---|---|---|
| `ALL` | **所有** jitter set 的配置数据 | `This value can be specified in the query to retrieve the configuration data of all jitter sets.` |
| `PRM` | **当前 primary jitter set** 的配置 | `This value can be specified in the query to retrieve the configuration of the current primary jitter set.` |

**`PRM` 说明「primary jitter set」这个概念是存在的**——
**但本页只见到这个概念，没见到「谁把它设成 primary」。「语法 / 参数」节里那条 `[[jspr]]` 是命名上的推测，不是本页读到的。**

## 典型用法

**1. 最小可用序列**（照原文的两条前提拼出来）：

**设好 setup focus**（`[[psfc]]`）→ **确认目标 jitter set 已经定义过**
（`The specified jitter set must have been defined with JSDF.`）→
**逐条写属性** `JSCF "<name>",<property>,<value>,(<pin>)` → **回读确认**（见下）。

**2. 回读的三种写法：**

| 想查什么 | 怎么写 |
|---|---|
| **一个 set 的一个属性** | `JSCF? "<name>",<property>,(<pin>)` |
| **一个 set 的全部属性** | 属性位写 `ALL` |
| **所有 set** / **只查 primary** | set 名位写 `ALL` / 写 `PRM` |

**3. 原文的示例（`## Example`）——注意它是一条查询、回复三行：**

```text
> JSCF? "my_J_SET",ALL,(Pin1)
< JSCF "my_J_SET",MODE,CONT,(Pin1)
< JSCF "my_J_SET",WAVEFORM,"-100,-50,0,50,100,50,0,-50",(Pin1)
< JSCF "my_J_SET",PERIODFACTOR,25,(Pin1)
```

原文对这个例子的说明是：

> 「This example defines a simple sawtooth waveform with a peak-to-peak value of 200ps for a STDDIFF or STD pin.」

**这里有一处值得注意**：波形列表 `-100,-50,0,50,100,50,0,-50` 的峰峰值正好是 **200**，
**既落在 `WAVEFORM` 的 ±200 ps 偏移上限上，又等于 `AMPLITUDE` 的上限**。
**原文把这两个「200 ps」写在同一篇的两处，没有说它们是不是同一个限制——本页不替它调和（推断标记：无，两处原文都逐字如上）。**

**4. 常见组合：**

- **要一个简单正弦** → `WAVEFORM,SINUSOIDAL`，再用 `AMPLITUDE` / `PERIOD` / `PHASE` 调它
  （**后三个只对预定义波形有效**）。
- **要一个自定义锯齿** → `WAVEFORM,"-100,-50,0,50,100,50,0,-50"` + `PERIODFACTOR`
  （**`PERIODFACTOR` 只作用于自定义波形**）。
- **要它一直抖** → `MODE,CONT`；**要每个 functional test 重来** → `MODE,RESTART`。
- **要随机抖动** → `NOISE`（最大 400 ps）。
- **拿 modulation set 抖** → `MODULATION_SETS`，**此时除 `MODE` 外别的都不能写**。

**5. 属性写入的先后顺序：语料未写。** 原文没有规定 `WAVEFORM` 与 `PERIODFACTOR` 谁先写——
**只说 `PERIODFACTOR` 只对自定义波形有效。本页不替它补一条顺序。**

## 和谁有关

**同族命令（`02.06.02.02.14x` 这一段是 jitter set 家族）**：

- [[jsdf]] — **前置**。本页正文逐字写着 `The specified jitter set must have been defined with JSDF.`，
  `## Errors` 又补了后果：**名字不存在就报错**。**这是本页唯一一条有原文逐字支撑的依赖关系。**
- [[psfc]] — **同样是前置，而且本页正文亲自点名它**：
  `For more information, see also: PSFC, PSFC?`。**JSCF 只改「有 setup focus 的 site」**，
  **焦点没设对会静静地改到别处**（前面已标推断）。
- [[jspr]] / [[jsud]] / [[jswf]] — **同族，但它们的文档本页一篇都没读。**
  **本页只确认一件事**：`JSCF?` 的 `PRM` 取值对应 **current primary jitter set**，
  **所以 primary 这个概念存在**。**「哪条命令设它、怎么设」本页一个字都没有。**
  这三个名字是从 allowlist 得知存在的，**不是本页读到的**，
  **所以它们和 JSCF 的分工本页不写。**

**同 stage 的页**：

- [[timing]] — 本页 `stage: timing` 的理由：**`WAVEFORM` 的偏移量是相对 timing set 的 edge delay 说的**
  （`a list of offsets from the edge delays specified in the currently active timing set`），
  **而且偏移上限 ±200 ps 也是相对它说的**。**但 timing set 本身怎么配，本页不写。**

**本页正文点名、但没有页、故不链的去处（反引号 + raw 路径）**：

- `Principles of jitter injection`（raw: `02.06.16.01_Principles_of_jitter_injection.md`）——
  正文第一段把它指为「更多信息」的落脚点。**本页没读它，所以「抖动注入的原理」本页没有。**
- `Two ways of organizing jitter setup data`（raw: `02.06.16.01.01_Two_ways_of_organizing_jitter_setup_data.md`）——
  `MODULATION_SETS` 那条互斥规矩的去处。**本页只抄了互斥这一句，没读那篇。**
- `Period resolution, clock resolution, and master clock period`
  （raw: `02.06.06.01.04.01.02.03_Period_resolution__clock_resolution__and_master_clock_period.md`）——
  `PERIODFACTOR` 那段指向它。**clock resolution 究竟怎么算出来，本页没有。**
- `Jitter injection` — 原文 `## Application` 一节**全文就只有这两个词**，
  **它没有对应页，本页也不为它编内容。**

## 版本

**本文档有 `## Functional changes` 段**，四条：

- **Introduced in SmarTest 7.0.1** — **JSCF 是 7.0.1 引进的**（同页的 `JSDF` / `JSPR` 是否同批，
  **本页不知道**——那两篇没读）。
- **SmarTest 7.1.1**：`WAVEFORM parameter SINUS changed to SINUSOIDAL`
  —— **属性表现里写的是 `SINUSOIDAL`**；`SINUS` 是 7.1.1 之前的写法。
  **拿老文档写的 `SINUS` 去问 7.10.3 的机台会不会认，本页不知道。**
- **SmarTest 7.3.0**：`The MODULATION_SETS property was added.`
  —— **本页那条「除 `MODE` 外全互斥」的硬约束，是 7.3.0 之后才存在的。**
- **SmarTest 7.3.1**：`User defined jitter waveforms are now supported for FASTDIFF pins.`
  —— **推断**：**`FASTDIFF` 的 pin 在 7.3.1 之前只能用预定义波形**（依据是 `now supported` 这个措辞）。
  **注意 `FASTDIFF` 这个词在本篇正文里一次都没出现**——正文只提到
  `STDDIFF or STD pin`（`## Example` 的说明里）与 `Smart Scale STDDIFF pins`
  （`AMPLITUDE` / `PERIOD` 两条里）。**这一个词只活在版本记录里。**

## 出处

`sources:` 一篇：
`02_System_reference/02.06_Command_Reference/02.06.02.02.147_JSCF__JSCF__-__Jitter_Set_ConFiguration.md`
（TDC `116890.htm`，265 行）

**本页没做的**：

- **本篇正文指出去的四篇文档，一篇都没读**：
  `Principles of jitter injection`（`02.06.16.01`）、
  `Two ways of organizing jitter setup data`（`02.06.16.01.01`）、
  `Period resolution, clock resolution, and master clock period`（`02.06.06.01.04.01.02.03`）、
  以及被点名的兄弟命令 `PSFC`（`02.06.02.02.191`）。
  **后果：「两种组织 jitter setup 数据的方式」怎么选、clock resolution 怎么算、
  setup focus 怎么设，本页一个字都没有。**
- **零张图。** 本篇没有图片引用（`116890.htm` 只有正文、两张语法块、一个示例块）。
  **所以「预定义波形长什么样」本页只有三个关键字，没有形状、没有时序图。**
- **`## Properties and their values` 那张大表不在「语法 / 参数」节的辖区里。**
  脚本只逐字抽了 `## Parameters` 与 `## Example`。**本页那张十属性表是照着
  `## Properties and their values` 写的散文，不是逐字抽取**——
  要逐字核对请回 raw（第 91 行起）。
- **`period_res` 这个关键字本页没查。** 原文在 `PERIODFACTOR` 里说用它设 period resolution
  （`with the period_res keyword`）。**它是哪条命令的关键字、取值怎么给，本页没有。**
- **没读过任何一页允许清单里的兄弟页**（`jsdf` / `jspr` / `jsud` / `jswf` / `psfc`）。
  **所以「jitter 这一族怎么串起来用」本页只给出 JSCF 自己的那一环。**
- **没有在任何真实机台上跑过 `JSCF`**（`verified: doc-only`）。
  **抖动注入的波形对不对、`PRM` 会不会返回空，本页只能保证「文档这么写」（§11）。**

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
> **① 度数符号坏了。** `PHASE` 那一行原文写的是
> `This value must be specified as a degree. The maximum is 360掳.`
> —— **`掳`（U+63B3）应为 `°`（度符号）**。这是 §11.2 ① 那类「UTF-8 被按 GBK 读」的又一形态：
> 已知的坏字有 `渭` / `碌`（µ）、`鈥慴`（‑b），**`掳` 是第三个**。
> **代价写在明处：拿 `360°` 去 raw 里搜是搜不到的，要搜 `360掳`。**
> **② 本页在 `PHASE` 一行之外没有发现别的坏字**——**但这是「本页读到的」，不是「本篇只有一处」**
> （§13.1 第 ⑥′：没找到 ≠ 没有）。本页正文引用 `PHASE` 那两句时**按坏字原样引**，
> 而在这一行里注出正字。

`verified: doc-only`
