---
type: object
title: PSSR, PSSR? -(Power Supply Slew Rate)
layer: L1
stage: level
tags: [pssr, l1, firmware-command, level, dps, dc-scale, slew-rate, voltage-ramp, settling-time, connect-to-connect, dfps, pslv]
related: [level, pslv, dfps, dscp, dpspins-resources, drlv, rclv, level-setup-tool, command-reference, smartest-6.5.3, smartest-7.10.3]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.197_PSSR__PSSR__-_Power_Supply_Slew_Rate.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# PSSR, PSSR? -(Power Supply Slew Rate)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,330 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.197_PSSR__PSSR__-_Power_Supply_Slew_Rate.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### PSSR

```
PSSR {dps_No|dps_set_id}, [rise_tm_per_v], [rise_settm], [fall_tm_per_v], [fall_settm], [rise_t_per_v_c2c], [rise_setup_t_c2c], [fall_t_per_v_c2c], [fall_setup_t_c2c], (pinlist)
```

### Parameters

Note The rise_... and fall_... parameters of the PSSR command and the settling time parameter (setup_time) of the `PSLV`（raw: `02.06.02.02.195_PSLV__PSLV__-__Power_Supply_LeVel.md`） command exclude each other. This also applies to the t_ms equation parameter (see `DPSPINS`（raw: `../02.08_Setup_and_Result_Tools/02.08.04.14.02.03.07_DPSPINS.md`） and `DPSPINS resources`（raw: `../02.08_Setup_and_Result_Tools/02.08.04.14.02.03.07.01_DPSPINS_resources.md`）). Note All time values have a resolution of microseconds (floating point values are rounded to three decimal places).

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/120504.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：11 行 × 2 列。
> 首行（上游原文）：dps_No | Needed for non-equation-based setup. The identification number of the DPS set which you want to modify. The number must not exceed the maximum number a…
> 表内引用（1 条，供检索）：`DFPS`（raw: `02.06.02.02.65_DFPS__DFPS__-__DeFine_Power_Supply.md`）

### Example

```
PSSR PRM,10,50,20,70,(Vcc)
```

This example sets the following parameters for the primary set of DPS pin Vcc:

- rise_tm_per_v = 10 ms/V
- rise_settm = 50 ms
- fall_tm_per_v = 20 ms/V
- fall_settm = 70 ms

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.197_PSSR__PSSR__-_Power_Supply_Slew_Rate.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

- The DPS set number is out of range
- A programmed parameter is out of range

<!-- 报错节 end -->

## 是什么

**`PSSR` 管的是「DPS 的输出电压怎么爬上去、怎么落下来」——斜率与建立时间。** 原文第一句：

> 「The PSSR command allows you to define voltage ramps (or slew rate settings) for DPS-slot DPS channels and for DC Scale channels, which were previously configured with the DFPS command in DPS mode. The PSSR? query returns the existing settings.」

（原句里 `DFPS` 是个链接，本页按 §11.1 ② 剥掉标记。**本页没有读 `DFPS` 那一篇。**）

一句话里四件事：① 它设的是 **voltage ramp（电压斜坡）/ slew rate**；② 对象是 **DPS-slot DPS 通道**和 **DC Scale 通道**；
③ 前置是 **`DFPS`，而且是 `in DPS mode` 配的**；④ **`PSSR` 写、`PSSR?` 读**。

**它和 [[pslv]] 是一对互斥的命令**——两边各写了一遍这条规矩。本篇这边的 `## Parameters` 开头 Note 逐字：

> 「Note The rise_... and fall_... parameters of the PSSR command and the settling time parameter (setup_time) of the PSLV command exclude each other.」

（`rise_...` 里的三连点是**原文自己写的**——§11.1 允许引文里出现原文自带的 `...`；**本页一个省略号都没自己加。**
括号里原来还有两个链接（`DPSPINS` / `DPSPINS resources`），已按 §11.1 ② 剥掉标记；**那两篇本页没读。**）

**⚠️ 同一条规矩在 [[pslv]] 那边的措辞是反的**：那一篇把 `PSLV` 的 `setup_time` 写在前面、`PSSR` 的 `rise_...` / `fall_...` 写在后面。
**两句话说的是同一件事，主语顺序与措辞都不同**（引文见 [[pslv]] 的「是什么」节；**本页没读 `PSLV` 的原文**）。

### 八个参数分两族：**基本族** 与 **connect-to-connect 族**

（每个参数的原文说明都在「语法 / 参数」节，脚本逐字抽的。本页只讲那八格里抽不出来的结构。）

| 族 | 语法位 | 参数 | 单位 | 原文范围 |
|---|---|---|---|---|
| 基本 | 2 | `rise_tm_per_v` | **ms/V** | `0 to 10000 ms/V` |
| 基本 | 3 | `rise_settm` | **ms** | `0 to 10000 ms` |
| 基本 | 4 | `fall_tm_per_v` | **ms/V** | `0 to 10000 ms/V` |
| 基本 | 5 | `fall_settm` | **ms** | `0 to 10000 ms` |
| c2c | 6 | `rise_t_per_v_c2c` | **ms/V** | `0 to 10000 ms/V` |
| c2c | 7 | `rise_setup_t_c2c` | **ms** | **`-10000 to 10000 ms`** |
| c2c | 8 | `fall_t_per_v_c2c` | **ms/V** | `0 to 10000 ms/V` |
| c2c | 9 | `fall_setup_t_c2c` | **ms** | **`-10000 to 10000 ms`** |

**两族一一对应**：一族一个上升沿斜率、一个上升沿建立时间、一个下降沿斜率、一个下降沿建立时间。

**两族唯一的差别在建立时间的下限**：基本族 `0 to 10000 ms`，**c2c 族 `-10000 to 10000 ms`**。
**负的建立时间是什么意思，本篇一个字没写**（见「出处」）。

**「斜率」是倒数（`inverse`），单位是 ms/V。** 四个斜率参数的原文都以同一句式起句，逐字两例：
`Sets the inverse slew rate for the rising edge in ms/V.` 与 `Sets the inverse slew rate for the falling edge in ms/V.`
——**不是 V/ms**。
（**推断**：按单位读，`ms/V` 是「每伏要多少毫秒」，所以**数越大越慢**；原文只给了单位和 `inverse` 这个词，没有把这句话写出来。）

**时间分辨率是全篇的**（`## Parameters` 开头第二个 Note，逐字）：

> 「Note All time values have a resolution of microseconds (floating point values are rounded to three decimal places).」

**⚠️ 这一条和 [[pslv]] 的 `setup_time` 连粒度都不一样**：那一篇的 `setup_time` 是 **ms、浮点四舍五入到整数**；
本篇**所有时间值都是 µs 分辨率、保留三位小数**。两条互斥的命令，时间的粒度也不同。

### `dps_No` 那一格：**四个关键字压在一段散文里**

`dps_No` 不像 [[pslv]] 那样分列成 `dps_No` / `ALL` / `PRM` / `ACT` 四个条目，
**它把四件事写成一整段**（逐字见「语法 / 参数」节）。要点：

| 写法 | 原文 |
|---|---|
| 一个数字 | 要改的那个 DPS set 编号；**上限由 `DSCP` 定** |
| `ALL` | `Entering ALL modifies all the existing fixed DPS sets.` |
| `PRM` | `Entering PRM modifies the primary DPS set.` |
| `ACT` | **只有 `PSSR?` 能写**：`Entering ACT (only for PSSR?) displays the settings of the actual enabled DPS set.` |

> ⚠️ **同一格里两个名字**：这一格开头写的是 `Needed for non-equation-based setup.`，
> 后半句又写 `all the existing fixed DPS sets`——**`non-equation-based` 与 `fixed` 指的是同一批 set**
> （同族毛病见 [[pslv]] 的「出处」⚠️ ⑥）。

### c2c 族：**只管「连着的时候换电压」**

四个 c2c 参数各写了一段**几乎一样**的话（**逐字；四段只有末尾回退的那个参数名不同**）：

> 「The parameter is optional. If specified, it is used for "connect-to-connect-" cases, that is for level changes caused by a reprogramming of the output voltage within one DPS set, or by a switch to another DPS set while the DPS is connected. If omitted, the above vout_rise_t_ms_per_volt parameter is used instead.」

**`connect-to-connect` 的定义原文给全了**（就是 `that is` 后面那半句）：

| 情形 | 原文 |
|---|---|
| 在**同一个 DPS set 内**重新编程输出电压 | `a reprogramming of the output voltage within one DPS set` |
| DPS **还连着**的时候切到另一个 DPS set | `a switch to another DPS set while the DPS is connected` |

**即：「基本族」管从断开到连上，「c2c 族」管连着的时候换挡。**（**推断**：原文没用「基本族」这种词作对比，
只用 `connect-to-connect` 划了第二种情形。**这四个参数还各带一句 `This parameter is for both DPS-slot DPS and DC Scale pins.`**）

| c2c 参数 | 省略时回退到（**原文写的名字**） |
|---|---|
| `rise_t_per_v_c2c` | `vout_rise_t_ms_per_volt` |
| `rise_setup_t_c2c` | `vout_rise_settling_t_ms` |
| `fall_t_per_v_c2c` | `vout_fall_t_ms_per_volt` |
| `fall_setup_t_c2c` | `vout_fall_settling_t_ms` |

**⚠️ 这四个回退名在本篇的参数表里一个都没有。** 本篇的八个参数叫 `rise_tm_per_v` 这些（见上表），
**`vout_*` 这一族名字只活在这四句话里**。原文的措辞是 `the above` + 那个名字（**「上面那个」**），
**可「上面」并没有同名的参数**。**本页不替它们对应**（照实并列）。

**已核上游 `120504.htm`：这不是 md 转换搞的，而上游留了一条线索。** 本篇 `## Related information` 里
`Voltage ramps` 那个链接的 `title` 属性逐字写着：
`The inverse slew rate parameters vout_rise_t_ms_... and vout_fall_t_ms... of the DPSPINS resources can be used to define voltage ramps that are calculated and applied by the system controller.`
—— **`of the DPSPINS resources`**：那族名字属于 **`DPSPINS resources`（方程路线）**，不是本篇的参数。
**⚠️ 这句在本篇的 md 里没有**（`title` 属性没进 md）——它是链接目标那一篇（`Voltage ramps`）的开头摘要，
**而那一篇本页没读**；**本页是从上游 `120504.htm` 读到的**，所以**拿这句话到本篇里搜是搜不到的**。
而且**上游两处写法也不一致**：`title` 里是 `vout_rise_t_ms_...`，正文里是 `vout_rise_t_ms_per_volt`。
**本页没有读 `DPSPINS resources` 那一篇**，所以那族参数到底是什么样，本页一个字没有。

### `pinlist`：**`@` 指的是 DC Scale 的针**（与 [[pslv]] 不是同一批）

> 「pinlist must contain the names of pins previously defined by the DFPS command. If a pin is associated with a DPS-slot DPS, it is ignored. @ refers to all pins that are associated with a DC Scale channel.」

**三句**：① pin 必须先由 `DFPS` 定义；② **属于 DPS-slot DPS 的 pin 会被忽略**；
③ **`@` = 所有与 DC Scale 通道关联的 pin**。

**⚠️ 和 [[pslv]] 的 `pinlist` 对照，同一个 `@` 不是同一批针**：那一篇写的是
`The character @ can be used to set the levels for all DPS pins.`（所有 DPS pin），
本篇写的是 **DC Scale 通道的 pin**。（那一句见 [[pslv]] 的「语法 / 参数」节；**本页没读 `PSLV` 的原文**。）

**⚠️ 这里还有一处原文自己的张力，本页照实并列、不替它调和：**

| 位置 | 原文说 |
|---|---|
| 第一句（正文） | 管 **DPS-slot DPS 通道** *和* DC Scale 通道 |
| `pinlist` 那一格 | `If a pin is associated with a DPS-slot DPS, it is ignored.` |
| 四个 c2c 参数那一格 | `This parameter is for both DPS-slot DPS and DC Scale pins.` |
| `## Example` | `PSSR PRM,10,50,20,70,(Vcc)` ＋ `for the primary set of DPS pin Vcc` |

**最紧的一处是那个例子**：它把 `PRM`（set 号形态）与 `(Vcc)`（pinlist）写在一起，
并把结果说成「设到了 **DPS pin `Vcc`** 身上」——**可 `pinlist` 那格刚说 DPS-slot 的 pin 会被忽略。**

**一种读得通的解释（推断，不是原文的话）**：**DPS-slot 用 set 号寻址、DC Scale 用 pinlist 寻址**——
依据是 `dps_No` 那格讲的全是 set 号、`pinlist` 那格讲的全是 DC Scale 的针，而例子同时用了两种形态。
**原文没有把这句话写出来。**

### 两条报错

见下面「报错条件」节（脚本从 `## Errors` 逐字取）：**DPS set 号越界**、**某个编程参数越界**。
两条的原文都**没有句尾句号**（`The DPS set number is out of range` / `A programmed parameter is out of range`），
**这是本篇的排版，不是本页漏抄**。（对照 [[pslv]] 的「报错条件」节——那一篇的条目更多，**但本页没读它的原文**。）

## 典型用法

**原文没有 `## Procedure` / `## Before you begin` / `## What to do next` 段。** 用法来自 `## Example` 与 `## Parameters`。

**1. 前置：`DFPS` 先定义 pin，而且是在 DPS 模式下。** 原文第一句的定语逐字是
`which were previously configured with the DFPS command in DPS mode.`
（**`in DPS mode` 管的是 `DFPS` 的配置方式还是卡的工作模式，本篇没写清**——见「出处」。）

**2. 完整例子**（原文唯一的例子，逐字）：

```
PSSR PRM,10,50,20,70,(Vcc)
```

> 「This example sets the following parameters for the primary set of DPS pin Vcc:」

> 「- rise_tm_per_v = 10 ms/V」

> 「- rise_settm = 50 ms」

> 「- fall_tm_per_v = 20 ms/V」

> 「- fall_settm = 70 ms」

（**列表符 `- ` 是原文的一部分**，§11.1。）

**照位置对回去**：`PRM` = `dps_No` 那格里的 `Entering PRM modifies the primary DPS set.`；
`10` / `50` / `20` / `70` = 前四个**基本族**参数；`(Vcc)` = `pinlist`。
**八个 c2c 参数一个都没给**——所以**回退规则（用 `vout_*` 那些名字）在这个例子上一句都看不到**。

**3. 查询**：`PSSR? {dps_No|dps_set_id}, (pinlist)`（语法节逐字）。
`ACT` **只有查询能写**——原文逐字：`Entering ACT (only for PSSR?) displays the settings of the actual enabled DPS set.`

**4. 想「立刻生效」？本篇没写。** 对照 [[pslv]]：那一页记着 primary DPS set 上的改动会立刻落到硬件，
**本页没读 `PSLV` 的原文**，也没在本篇里找到对应的一句——**语料未写**。

**5. 与 `PSLV` 二选一**：`setup_time`（[[pslv]]）与 `rise_...` / `fall_...`（本篇）互斥；方程路线里的 `t_ms` 与两者也互斥。
**这是硬约束**——原文的动词是 `exclude each other`。

**6. 归属**：原文 `## Application` 全文一句 —— `Level setup, see Level Setup Commands.`
（`Level Setup Commands` 那篇章首页**本页没读**。）

## 和谁有关

- [[level]] — `stage: level` 的落点：`## Application` 那句 `Level setup, see Level Setup Commands.`
- [[pslv]] — **互斥的另一半**：`PSLV` 的 `setup_time` 与本篇的 `rise_...` / `fall_...` 不能同时用；
  它也是本篇**唯一的实质入边来源**（见「出处」）。**`PSLV` 的原文本页没读。**
- [[dfps]] — **前置**：`pinlist` 里的 pin 必须是它定义过的；`in DPS mode` 那个定语也挂在它身上。**本页没读。**
- [[dscp]] — `dps_No` 的上限由它定（本篇那一格逐字点了 `DSCP`）。**本页没读。**
- [[dpspins-resources]] — **方程路线的 DPS 模块**，也是 c2c 那四个回退名的来处（**推断**，依据是上游 `Voltage ramps` 链接的 `title`，见「是什么」）。
  本篇的 Note 也点了它（与 `t_ms` 一起）。**本页没读。**
- [[drlv]] / [[rclv]] — 同章的 level 命令：`DRLV` 管驱动电平、`RCLV` 管比较阈值、本篇管 **DPS 的斜坡**。**两篇本页都没读。**
- [[level-setup-tool]] — level setup 的 GUI 侧。**本页没读。**
- `Level Setup Commands`（**未建、不在 allowlist 里**）—— `## Application` 指定的章首页。**没读。**
- `Voltage ramps` / `DPSPINS`（**均未建、不在 allowlist 里**）—— `## Related information` 里的两条。**都没读。**

## 版本

`## Functional changes` 段有，**只有一条**，逐字：

```
- Introduced in SmarTest 6.5.3
```

**这一条不是哨兵值**：措辞是 `Introduced in`（**不是 `before`**），按字面读就是「**6.5.3 引入**」。

**它对得上 [[pslv]] 版本段里的一条**：那一页记着 `PSLV` 在 6.5.3 有一条「解除与 `PSSR` 的依赖」
（**这一条见 [[pslv]] 的「版本」节，本页没读 `PSLV` 的原文**）。
**同一个版本号 6.5.3 下**：新命令 `PSSR` 引入，老命令 `PSLV` 记了一条「解除依赖」。
**两句并排读讲得通**（引入新命令时把老命令的依赖解开）——**但这是推断，原文没有把两句连起来。**

**与 wiki 面向版本的关系**：本 wiki 面向 **SmarTest 7.10.3**（[[smartest-7.10.3]]），
而本篇的版本段**停在 6.5.3**——**6.5.3 之后 `PSSR` 有没有变，语料里没有。**

## 出处

`sources:` 一篇：
`02_System_reference/02.06_Command_Reference/02.06.02.02.197_PSSR__PSSR__-_Power_Supply_Slew_Rate.md`
（TDC `120504.htm`，**3,009 字节 / 200 行**）。**整篇读完**——本页引文全部来自这一篇 ＋ `edges.jsonl` 里带原句的边。

**入边 6 条 / 4 篇**（`inline` + `toc` 口径，`edges.jsonl` 原始行数）：
`02.06.02.02.195_PSLV__PSLV__-__Power_Supply_LeVel`（2 条）、
`02.06.05.02.15_PSLV__PSLV__-__Power_Supply_LeVel`（2 条）、
`02.06.02.02_List_of_commands`、`02_System_reference/index.md`。
**四条实质入边全部来自 `PSLV` 那篇的两个投放副本**（`02.06.02.02.195` 与 `02.06.05.02.15`，两条引用句逐字相同）——
**除了 `PSLV`，没有任何别的文档引过它。**

**本页没做的**：

- **`PSLV` / `DFPS` / `DSCP` / `DPSPINS` / `DPSPINS resources` / `Level Setup Commands` 六篇原文都没读。**
  本页对 `PSLV` 的三处提及（互斥、`pinlist` 的 `@`、时间粒度、立刻生效），**全部只依据 [[pslv]] 那一页的语法节引文**。
- **`Voltage ramps` 那一篇只核了一句**：为了定位 c2c 回退名（`vout_*`）的出处，本页定位到
  `02.08.04.14.06.01.02.02.01_Voltage_ramps.md` 开头那一句，**确认它逐字在那里**；**整篇没读**，
  所以「电压斜坡在系统里怎么算、怎么施加」本页一个字没有。
- **四条入边文档一篇没读**：本页提它们，只提 `edges.jsonl` 里那四条边本身。
- **图：本篇没有内嵌图片**——判据可核：本篇 md 里 `.png` / `![` **0 命中**。所以**没有图可看，也没有图证**。
- **编码坏字：本篇 0 处**（`[一-鿿]` 扫过整篇，一个汉字都没有）；
  **整词替换（`DC/DC power units`）本篇 0 命中**。两条都是实测结果，不是没查。
- **`in DPS mode` 管的是哪一层：语料未写。** 本页只能照录那个定语。
- **负的 settling time 是什么意思：语料未写。**
- **「primary 之外怎么生效」「有没有立刻生效」：语料未写。**
- **没有实跑。** 没有在机台上发过 `PSSR` / `PSSR?`，没有量过任何一条斜坡。`verified: doc-only` 说的就是这件事。
- **没有动 `wiki/index.md`。**

> ⚠️ **本篇的语料瑕疵，照实记、一处都没替它改**（§11.2）：
>
> **① 四个 c2c 句里三个写 `"connect-to-connect-"`、一个写 `"connect-to-connect"`。** 逐字两形态：
> `If specified, it is used for "connect-to-connect-" cases, that`（三处，含连字符）／
> `If specified, it is used for "connect-to-connect" cases, that`（`fall_setup_t_c2c` 那一处）。
> **已核上游 `120504.htm`：上游就是这样**（三处连字符在引号内、一处不在）——**不是 md 转换丢的**。
>
> **② 四个 c2c 参数的回退名（`vout_*`）在本文档的参数表里不存在**，原文的措辞却是 `the above` + 那个名字。
> **已核上游**：上游也这样；线索藏在上游 `Voltage ramps` 链接的 `title` 属性里（见「是什么」），**md 里搜不到**。
> 而且**上游两处写法也不一致**：`title` 里是 `vout_rise_t_ms_...`，正文里是 `vout_rise_t_ms_per_volt`。
>
> **③ `expression` 小写起句，四行全是。** 四条逐字：
>
> 「Sets the inverse slew rate for the rising edge. expression must define a value in ms/V.」
>
> 「Sets the settling time for the rising edge. expression must define a value in ms.」
>
> 「Sets the inverse slew rate for the falling edge. expression must define a value in ms/V.」
>
> 「Sets the settling time for the falling edge. expression must define a value in ms.」
>
> ——**句号之后直接跟小写 `expression`**，四条一模一样，**不是偶发笔误**（**已核上游：上游如此**）。
>
> **④ 模板与例子的空格不一致。** 模板逐字里有 `[rise_tm_per_v], [rise_settm]`（**逗号后有空格**），
> 例子逐字是 `PSSR PRM,10,50,20,70,(Vcc)`（**逗号后没有空格**）。
>
> **⑤ `## Related information` 四段链接粘在一行、中间没有分隔符。** 逐字：
> `[DPSPINS](<../02.08_Setup_and_Result_Tools/02.08.04.14.02.03.07_DPSPINS.md>)[DPSPINS resources](<../02.08_Setup_and_Result_Tools/02.08.04.14.02.03.07.01_DPSPINS_resources.md>)[Voltage ramps](<../02.08_Setup_and_Result_Tools/02.08.04.14.06.01.02.02.01_Voltage_ramps.md>)[PSLV, PSLV? - (Power Supply LeVel)](<02.06.02.02.195_PSLV__PSLV__-__Power_Supply_LeVel.md>)`
> ——**四个链接名首尾相接**。**已核上游 `120504.htm`：上游是四个独立的链接块**——
> **粘在一起是 md 转换造成的**（与 [[pslv]] 记的是同一族毛病，那一篇坏法一样）。
>
> **⑥ `Note` 被折进了句子。** `## Parameters` 那一节里有**两个 `Note`**（一个是上游 note 块的标题），
> 它们在 md 里被折进**同一段**：第二个 `Note` 紧跟在前一句的句号之后，
> **中间只有一个空格**，没有任何分隔（同 [[pslv]] ④ 是同一族毛病）。
>
> **⑦ 本篇引 `PSLV` 时标题末位是**小写 `l`：`PSLV, PSLV? - (Power Supply LeVel)`；
> 而 [[pslv]] 自己的标题末位是**大写 `L`**（见 [[pslv]] 的「出处」⚠️ ⑪）。
> **两处都是原文如此**——**同一篇标题，语料里就有两种写法**，本页没有替它统一。

`verified: doc-only`
