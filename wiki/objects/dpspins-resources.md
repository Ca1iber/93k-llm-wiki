---
type: object
title: DPSPINS resources
layer: L2
stage: pin
tags: [dps, level-setup, resources, equation-based-level-setup, xps256, uhc4t, dpspins]
related: [dpspins-resources, equation-based-level-setup, level-setup-tool, dc-scale-uhc4t-card, dc-scale-xps256-card, dps128-dps64-cards, dps-power-flags-get-functions, connect, disconnect, pslv, smartest-7.10.1, smartest-7.10.3]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.02.03.07.01_DPSPINS_resources.md
created: 2026-09-18
updated: 2026-09-20
verified: doc-only
---

# DPSPINS resources

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **728 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.02.03.07.01_DPSPINS_resources.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example 1: All resource keywords

See `Example 1: Copy/paste example with all resource keywords`（raw: `02.08.04.14.02.03.07_DPSPINS.md#_16886__copy_paste_example`） in `DPSPINS`（raw: `02.08.04.14.02.03.07_DPSPINS.md`） for a copy/paste example with all resource keywords.

### Example 2: Using the voltage ramp parameters

Parameter t_ms cannot be specified in combination with one of the parameters vout_rise_t_ms_per_volt(_c2c), vout_fall_t_ms_per_volt(_c2c), vout_rise_settling_t_ms(_c2c), and vout_fall_settling_t_ms(_c2c). Valid examples are

```
t_ms=50
```

or

```
vout_rise_t_ms_per_volt=10
vout_fall_t_ms_per_volt=10
vout_rise_settling_t_ms=50
vout_fall_settling_t_ms=70
```

For further details see also `DPS connect setup time and voltage ramps`（raw: `02.08.04.14.06.01.02_DPS_connect_setup_time_and_voltage_ramps.md`）.

<!-- 语法节 end -->

## 是什么

**DPSPINS resources 是 DPS pin 在「基于等式的电平设置」（equation based level setup）
里的行为参数集。** 原文第一句：

> 「Parameters of the DPSPINS resources define the behavior of DPS pins in the equation based
> level setup. Specific keywords and values are to be used to define the resource parameters.」

**两个词定死了它的位置**：**DPS pin**（不是 digital pin、不是 utility pin）和
**equation based level setup**（不是 GUI 里填表）。
**所以这一页讲的是「往电平设置等式里写什么关键字」**，不是「界面上点哪个按钮」。

### 两个入口，33 个参数，9 个功能组

原文给了两套组织方式，**用途不同**：

| 节 | 组织方式 | 用途 |
|---|---|---|
| `## Resource parameters grouped by function` | **按功能分 9 组** | **「我要做 X，该用哪些参数」** |
| `## Resource parameter table` | **按字母序**（`capacitance` → `connect_state` → …） | **查单个参数的定义** |

> ⚠️ **`## Resource parameters grouped by function` 那一段在语料里是一张坏掉的表**
> （9 个组被塞进 3 个 2 列表格里，见 `## 出处`）。**上面这张 9 组表是本页按它的
> 标题与 bullet 重新整理的，分组名逐字取自原文。**

### 9 个功能组

| 组 | 参数（**逐字**） |
|---|---|
| **Connections and timing** | `connect_state`、`t_ms` |
| **Current** | `ilimit`、`ilimit_sink`、`ilimit_source`、`iout_clamp_rng`、`offcurr` |
| **Constant current check** | `disable_const_curr_check`、`ms_const_curr_disconnect`、`ms_const_curr_time_to_alarm` |
| **Dynamic behavior** | `capacitance`、`load_step_mode`、`current_filter_frequency`、`voltage_filter_frequency` |
| **Maximum voltage drop** | `max_voltage_drop_force`、`max_voltage_drop_return`、`warn_voltage_drop_force`、`warn_voltage_drop_return` |
| **Other** | `ms_fast_preload`、`open_loop_protection`、`protect`、`pulldown` |
| **Voltage** | `vout`、`vout_frc_rng` |
| **Voltage settling time** | `vout_rise_settling_t_ms`、`vout_rise_settling_t_ms_c2c`、`vout_fall_settling_t_ms`、`vout_fall_settling_t_ms_c2c` |
| **Voltage slew rate** | `vout_rise_t_ms_per_volt`、`vout_rise_t_ms_per_volt_c2c`、`vout_fall_t_ms_per_volt`、`vout_fall_t_ms_per_volt_c2c`、`voltage_slew_rate` |

**共 33 个参数。** 注意 **`Current` 组有 5 个、`Maximum voltage drop` 组有 4 个、
`Voltage slew rate` 组有 5 个**——**每组里的参数是「选一个用」还是「可以叠加」，
原始分组表没说**，要逐个看参数自己的那一格。

### 适用范围：一张表定「这个参数能写在哪儿」

原文在参数表末尾给了 `Some parameters are valid for selected DUT power supplies:` 一段
（**5 条，不是全部 33 个参数，覆盖面不全，见 `## 出处`**）：

| 能用在哪儿 | 参数 |
|---|---|
| **DPS-slot DPS（非 DC Scale）+ DC Scale pin 都可以** | `vout`、`ilimit`、`t_ms`、`vout_rise_t_ms_per_volt`、`vout_fall_t_ms_per_volt`、`vout_rise_settling_t_ms`、`vout_fall_settling_t_ms`、`offcurr`、`disable_const_curr_check` |
| **只有 DC Scale pin** | `vout_frc_rng`、`iout_clamp_rng`、`connect_state` |
| **只有 DC Scale UHC4T** | `ms_const_curr_disconnect`、`ms_fast_preload` |
| **只有 DC Scale UHC4T 和 DC Scale XPS256** | `max_voltage_drop_force`、`max_voltage_drop_return` |
| **只有 DC Scale XPS256** | `current_filter_frequency`、`voltage_filter_frequency` |

**剩下 16 个参数（`capacitance`、`load_step_mode`、`ms_const_curr_time_to_alarm`、
`pulldown`、`protect`、`open_loop_protection`、`voltage_slew_rate`、
`warn_voltage_drop_force`、`warn_voltage_drop_return`，以及 4 个 `_c2c` 变体等）
不在这张表里** —— **它们的适用范围要从各自那一格里那句
`This parameter is for …` / `This optional parameter is supported only by the … card.` 逐条读。**

**（推断）**：**4 个 `_c2c` 变体大概率跟着它们的基础参数走**——
`vout_rise_settling_t_ms_c2c` 那一格写的是「如果指定了就用它，否则用
`vout_rise_settling_t_ms`」，**依据是这句原文**。**但原文没把 `_c2c` 列进那张适用范围表，
所以这是推断，不是文档事实。**

### 参数值的三种形态

| 形态 | 例子（**逐字**） | 说明 |
|---|---|---|
| **带单位的数值表达式** | `Current in milliamperes (mA)`、`Time in milliseconds (ms)`、`Frequency in hertz (Hz)`、`Inverse slew rate in milliseconds per volt (ms/V)`、`Capacitance in microfarads …` | **等式右边写数值** |
| **关键字（多选一）** | `Keyword:` 后跟 bullet 列表 | 见下 |
| **只有 `none`** | `disable_const_curr_check`、`protect` 的 Expression 列写 `none` | **不是「不重要」，是「没有取值」——写上这个参数名本身就是动作** |

**（推断）**：**第三种形态的含义**——`disable_const_curr_check` 的说明是
`Switches off the constant current check.`，**是一个开关，不是一个值**；
**依据是它那格的 Expression 列写着 `none` 而 Description 是一句「关掉什么」**。

### 五个关键字型参数，取值逐字如下

| 参数 | 取值 | 关键约束（逐字或紧贴原文） |
|---|---|---|
| `connect_state` | `himp` / `hdig` / `norm_hdig` / `ungang` | **`hdig` 和 `norm_hdig` 只给 UHC4T**；`himp`（高阻测量，可当电压表用）和 `ungang` 是所有 DC Scale 卡都有 |
| `offcurr` | `min` / `act` / `open` / `act_min` / `act_open` | **断开时给什么电流**；`act` 对应 `PSLV` 的 `LOZ`、`min` 对应 `HIZ`、`open` 对应 `HIZ_R` |
| `load_step_mode` | `STD` / `FAST` | **只给 XPS256**；`STD` 的动态行为「similar to DC Scale DPS128/DPS64 cards」 |
| `open_loop_protection` | `diode` / `none` | **只给 XPS256**；`diode` 是默认，`none` 把 force-sense 内部连接断开 |
| `pulldown` | `on` / `off` | **只给 XPS256**；`on` 是 `"HIZ"` 断开态下的默认，`off` 是 `"LOZ"` 断开态下的默认 |

**`offcurr` 有一条值得单拎出来的建议**，原文（`act` 那一格）逐字：

> 「Note This is the recommended default setting for the off-state of DPS pins. Only act
> discharges capacitors on the DUT board. Use min or open carefully and only for selected tests.」

**即：只有 `act` 会放掉 DUT 板上的电容。`min` / `open` 要小心用。**

**`connect_state=ungang` 有一条行为细节**，原文：

> 「Note that on DPS128/64 and XPS256 you cannot execute a current compare on a ganged group of
> channels in unganged mode. Already activated comparators are silently disabled in unganged mode.
> A user notification (Error or warning) is omitted in this case, to avoid any interrupt in the
> testflow. The previous state of the comparators is automatically restored after the ganged group
> has been restored.」

**这条的实操含义：ungang 下比较器被静默关掉，不报错、不警告**——
**测试流程不会被打断，但你也收不到通知**。

### 最大压降那一套：4 个参数、两条规则、一张图

**这一组是 DPSPINS 里最复杂的一处**，`max_voltage_drop_force` /
`max_voltage_drop_return` 是**断开阈值**，`warn_voltage_drop_force` /
`warn_voltage_drop_return` 是**警告阈值**（**后者只给 XPS256**，
默认 `150 mV` / `50 mV`）。

**UHC4T 上是比较器**（原文：`A comparator defines if the voltage drop is small enough or not.`），
**量的是 pogo 线 + DUT 板的压降和**，范围 `0.0 … 0.5 V`、分辨率 `1 mV`、默认 `0.25 V`，
**值/flag 对整组 ganged 通道有效**。
**XPS256 上是 ADC 测量**：force 线上量压降、比较器取绝对值，到最大值就断通道。

**两条规则只对 UHC4T 生效**（原文 `Two rules apply for the two parameters …`）：

| 规则 |
|---|
| **两个阈值都必须落在 `0.0` 到 `0.5 V` 之间** |
| **两者之和受 program 的 force 电压限制**，**只有图里红色区域内的值才允许** |

**XPS256 的对应约束是另外一套**：可 program 范围到 `1.0 V`，
但**两条线加起来不得超过 `1.0 V`**；**压降要超过 `0.5 V` 还得额外改两处设置**——
`openLoopProtection` 必须设成 `none`，且 `DC Scale Safety editor` 里的
`Vdrop Disco` 必须设成 `ON`。**`open_loop_protection` 参数那一格里把这个反过来写了一遍**
（`none` 那一项要求 `Vdrop Disco` 必须 disabled，且这是
「`max_voltage_drop_force` 或 `max_voltage_drop_return` 设成 ≥ 0.5 V 时的必需设置」）。

### 三条全局规矩

原文在参数表之后给了三句不针对单个参数的话，**这三句最容易踩**：

> 「Note Resource values may be specified in any order, but must not be specified more than once
> for any DPS pin. If they are, an error is reported.」

**顺序随便，但同一个 DPS pin 上不许重复定义同一个参数——重复是报错，不是覆盖。**

> 「If any DPS pins are not listed within an equation set, a warning is issued and the default
> setting is used.」

**漏写一个 pin：警告 + 用默认值**，**不是报错**。**（实操含义：漏 pin 不会拦住你，
只会让那一个 pin 悄悄用默认值。）**

> 「No check is made that the units of all specs used in expression are compatible with each
> other or that they have been scaled correctly. It is up to the user to ensure that the
> expression is defined correctly.」

**单位兼容性完全不校验。** 这一条要和下面 `## 出处` 里 `voltage_slew_rate` 那个单位写错
的瑕疵放在一起看：**文档自己都会写错单位，工具也不会替你查。**

## 典型用法

**1. 用法就是「把参数写进电平设置等式」**（原文第一句的 `in the equation based level setup`）。
**原文没有给 `## Procedure` 或 `## Before you begin` 段**，所以本页没有「先点哪里再点哪里」的步骤。

**2. 完整写法看 `Example 1`**，而它**不在这篇文档里**：

> 「See Example 1: Copy/paste example with all resource keywords in DPSPINS for a copy/paste
> example with all resource keywords.」

**即：全参数的可粘贴例子在 `DPSPINS` 那篇里，本页没有**（那篇本页没读）。

**3. 画电压 ramp：`t_ms` 和 4 组 ramp 参数互斥。** 这是 `Example 2` 的全部内容，原文：

> 「Parameter t_ms cannot be specified in combination with one of the parameters
> vout_rise_t_ms_per_volt(_c2c), vout_fall_t_ms_per_volt(_c2c), vout_rise_settling_t_ms(_c2c),
> and vout_fall_settling_t_ms(_c2c). Valid examples are」

**两种合法写法**（原文两块代码）：

```
t_ms=50
```

或

```
vout_rise_t_ms_per_volt=10
vout_fall_t_ms_per_volt=10
vout_rise_settling_t_ms=50
vout_fall_settling_t_ms=70
```

**一句话记法：要么给一个绝对的时刻（`t_ms`），要么给「斜率 + 建立时间」这一套。**

**4. 一次 connect 用的是哪几个参数**（按分组推）：
`connect_state` 决定「连上时给什么电流」→ `t_ms` 或 ramp 那 4 组决定「什么时候到、怎么爬」
→ `vout` / `ilimit` 决定到哪个电平、限多少流。
**（推断）这条链路是本页按 9 个分组名拼出来的**，
**原文没有一段把它们串起来的话**，所以标为推断。

**5. 选参数的三步问法：**

| 你要做的 | 去看哪组 |
|---|---|
| 控制连上/断开的电流与时刻 | **Connections and timing** + **Current** |
| 限流并防止恒流跑太久 | **Current** + **Constant current check** |
| 让环路对负载阶跃反应更快 / 改带宽 | **Dynamic behavior** |
| 防止板上压降过大而烧板 | **Maximum voltage drop** |
| 调电压爬升的形状与精度 | **Voltage** + **Voltage settling time** + **Voltage slew rate** |
| 卡专属的开关（保护、下拉、force-sense 连接） | **Other** |

**6. 一条容易漏的前提**：**`## 版本` 里那 20 条里有一大半是「某个参数只在哪张卡上有」**——
**先确认你手上的卡，再确认那个参数在那张卡上存在**，否则会写出一个当前卡不认的参数。

## 和谁有关

- [[equation-based-level-setup]] — **上位概念**。本页第一句说的就是「DPS pin 在它里面的行为」；
  **本页只讲 DPS 这一侧的参数，等式本身怎么写不在这篇文档里。**
- [[level-setup-tool]] — **应用侧**。原文在脚注里说 `connect_state` 的默认值 `norm`
  可以在它的 `DPS Setup window` 里选，**但不能在等式里显式写出**。
  **本页没有 Level setup tool 的任何界面信息。**
- [[dc-scale-uhc4t-card]] / [[dc-scale-xps256-card]] — **下游，硬件侧**。
  本页的关键词里有相当一部分是**卡专属**的（`hdig` / `norm_hdig` 只给 UHC4T；
  `load_step_mode` / `pulldown` / `open_loop_protection` / `warn_voltage_drop_*` 只给 XPS256）。
  **本页只有「哪个参数属于哪张卡」，没有这两张卡自身的功能。**
- [[dps128-dps64-cards]] — **对照组**。原文拿它当基准：
  XPS256 的 `load_step_mode=STD` 的动态行为「similar to DC Scale DPS128/DPS64 cards」；
  而且 **DPS128/64 也在 `ungang` 比较器静默关闭那条规则里**。
- [[dps-power-flags-get-functions]] — **下游，状态侧**。
  本页的 `max_voltage_drop_force` / `max_voltage_drop_return` / `ms_const_curr_disconnect`
  **正是那边三个 flag（`Voltage drop force` / `Voltage drop return` /
  `Current limit disconnect`）的阈值定义处**——**本页定阈值，那边读结果。**
- [[xps256-status-flags]] — **下游**。`warn_voltage_drop_force` / `warn_voltage_drop_return`
  的说明直接指向它；`ms_const_curr_time_to_alarm` 也指向它。**本页只说「阈值送到哪儿」，
  flag 自己怎么工作在那两页里。**
- [[connect]] / [[disconnect]] — **直接相关**。本页多个参数只在 connect / disconnect 场景下用
  （ramp 参数原文写 `The parameter is always used for connect and disconnect cases.`），
  `offcurr` 干脆就是「断开时给什么电流」。
- [[pslv]] — **同一件事的命令侧**。`offcurr` 的 5 个取值逐个对应 `PSLV` 的
  `HIZ` / `LOZ` / `HIZ_R` / `LOZ_HIZ` / `LOZ_HIZ_R`；
  `connect_state=ungang` 也对应 `PSLV` 的一条。
  **（推断）等式参数与命令两条路是同一套底层设置**，**依据是 `offcurr` 那 5 格的原文一一映射**。
- [[pin]] — **对象侧**。本页所有参数都是「per DPS pin」的
  （原文：`must not be specified more than once for any DPS pin`）。
- [[smartest-7.10.1]] / [[smartest-7.10.3]] — **版本页**。XPS256 支持与最后一条参数都在这里。
- `DPSPINS`（**未建**）— **父文档**。本页是它的一个子主题（文件名 `…07.01_DPSPINS_resources`），
  `Example 1` 的全量例子正文在它里面；**本页没读它。**
- `DPS Setup window` / `DPS connect setup time and voltage ramps` /
  `Using the UNGANG connect state with DC Scale DPS cards` /
  `Voltage ramps` / `IO PINS resources` / `UHCM` / `PSLR`（**均未建**）—
  原文 `Related information` 与参数格里点名的那几篇。**尤其是 `IO PINS resources`：
  它是对照物（数字 pin 的资源长什么样），本页没读，所以本页无法回答「DPS 和 digital 的资源
  有什么异同」。**

## 版本

本文档**有** `## Functional changes` 段，**20 条**（末条之后粘着一条脚注，见下）：

| 版本 | 变更 |
|---|---|
| **`Introduced before SmarTest 6.3.2`** | **哨兵值**（见下），**不是「6.3.2 新增」** |
| SmarTest 6.5.3 | 新增 `vout_rise_t_ms_per_volt`、`vout_fall_t_ms_per_volt`、`vout_rise_settling_t_ms`、`vout_fall_settling_t_ms` |
| SmarTest 6.5.3 | 修改两个 drop 参数（`max_voltage_drop_force`、`max_voltage_drop_return`）的电压限值 |
| SmarTest 6.5.4 | `connect_state=ungang` 的增强与扩展支持 |
| SmarTest 7.1.0 | 新增 4 个 `_c2c` 参数 |
| SmarTest 7.1.0 | 修改 `t_ms` 的定义与范围（**原文**：`Connect setup time now -2147483647 to 217483647 ms.`） |
| SmarTest 7.1.0 | 修改 `vout_rise_settling_t_ms` / `vout_fall_settling_t_ms` 的时间范围（now `-10000 to 10000 ms`） |
| SmarTest 7.1.3 | 新增 off 电流模式 `act_min`、`act_open` |
| SmarTest 7.1.4 | `connect_state=ungang` 的增强与扩展支持（**与 6.5.4 那条正文一字不差**） |
| SmarTest 7.2.1 | 新增或修改 `ilimit`、`ilimit_source`、`ilimit_sink` |
| SmarTest 7.3.1 | 新增或修改 `connect_state`、`voltage_filter_frequency`、`current_filter_frequency` |
| SmarTest 7.3.1 | 支持 DC Scale **PVI8** 卡 |
| SmarTest 7.3.2 | 支持 DC Scale **UHC4T** 卡 |
| SmarTest 7.4.0 | 支持 DC Scale **AVI64** 卡 |
| SmarTest 7.5.0 | 支持 DC Scale **FVI16** 卡 |
| **SmarTest 7.10.1** | **支持 DC Scale XPS256 卡** |
| **SmarTest 7.10.1** | **新增 7 个 XPS256 参数**：`capacitance`、`load_step_mode`、`ms_const_curr_time_to_alarm`、`pulldown`、`warn_voltage_drop_force`、`warn_voltage_drop_return`、`voltage_slew_rate` |
| **SmarTest 7.10.3** | **新增 `open_loop_protection`（XPS256）** |

**两处读法提醒：**

> **① 首条 `Introduced before SmarTest 6.3.2` 是 §11.2 ② 说的哨兵值**，
> 意思是「**在本文档集覆盖范围开始之前就已经有了**」，
> **照字面读会变成「6.3.2 新增了 DPSPINS resources」，那是假的。**
>
> **② `SmarTest 6.5.4` 与 `SmarTest 7.1.4` 两条的正文一字不差**，原文两行分别是：
> `SmarTest 6.5.4: Enhancements and extended support of connect_state=ungang with 6.5.4.10 and SmarTest 7.1.4.0.`
> `SmarTest 7.1.4: Enhancements and extended support of connect_state=ungang with 6.5.4.10 and SmarTest 7.1.4.0.`
> **本页并列两行，不判是重复条目还是真有两个版本各自做了一次。**

> ⚠️ **段末粘着脚注定义**（`[1)](<#fnsrc_1>) The default value norm of DPS pin resource connect_state …`）——
> 又是 §11.2 ③ 那个现象：`## Functional changes` 是最后一个 `## ` 段，脚注被算进来。
> **它不是版本条目**，内容是关于 `connect_state` 默认值 `norm` 怎么设的。

## 出处

`sources:` 一篇：
`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.02.03.07.01_DPSPINS_resources.md`

**本页没做的：**

- **那张 33 个参数的完整表本页没有逐条搬。** 本页只按 9 个功能组列了参数名单，
  再把五个关键字型参数的取值摊开、把「最大压降」那一组讲清。
  **其余参数（`capacitance`、`current_filter_frequency`、`voltage_filter_frequency`、
  `load_step_mode` 的细节、`ms_fast_preload`、`protect`、`pulldown`、`ilimit*`、
  `iout_clamp_rng`、`vout_frc_rng`、`ms_const_curr_time_to_alarm` 等）的完整说明、
  默认值、可 program 范围，本页一个字都没有**——**要看就得回原文那一格。**
  本页有意识地没搬整表（§3：不把整篇文档搬进 wiki）。
- **「语法 / 参数」节里只有两个 `Example` 段。** 也就是说
  **那张参数表根本没有被脚本收进语法节**（它不在 `Syntax` / `Parameters` 这类段标记下）。
  **本页 `## 是什么` 里对参数表的概括，是本页自己读原文写的，不是语法节的内容。**
- **`DPSPINS`（父文档）没读** —— 所以 `Example 1` 那个「全参数可粘贴例子」**本页拿不到**。
- **`Related information` 里那 5 篇一篇没读**：
  `Using the UNGANG connect state with DC Scale DPS cards`、`Voltage ramps`、`PSLV`、
  `IO PINS resources`、以及 `DPSPINS` 自己。**尤其 `PSLV` 与 `IO PINS resources`
  是本页拿来对照的两篇，没读。**
- **`DPS connect setup time and voltage ramps` 没读**（`Example 2` 结尾指向它）——
  **所以 ramp 参数的时间语义本页只有参数表里那几句。**
- **`DPS Setup window`（`How to read the DPS Setup window`）没读** ——
  所以 `connect_state` 默认值在界面上怎么选，本页没有。
- **规格文档没读**（`DC Scale Device Power Supplies and VI Cards`、
  `XPS256 other performance characteristics`、`XPS256 force and clamp voltages`、
  `XPS256 programming - Force and clamp voltages` / `Load step response` /
  `Force and clamp currents`）—— 所以**本页所有「可 program 范围」都是原文里顺带写出的那几个数，
  没有一个是去规格书核过的**。
- **一张图看了没有：没有。** 原文 `## Maximum voltage drop on the UHC4T force lines`
  一节里有一张 `151617.png`（`Drop sum plot`），**本页没有看它**——
  所以「两条规则」里**第二条（两者之和受 force 电压限制）的那条曲线长什么样，
  本页完全不知道，只知道「只有红区里的值允许」。** 这是本页最大的空缺。
- **没有交叉验证任何别处的文档**（§11：本页只写这一篇里有的）。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> **① 编码损坏：本篇是本 wiki 见过最密的一篇之一。**
> `鈥` 形态 **17 行**，`渭` / `卤` / `鈮` 等同类损坏 **12 行**（`rg -c` 按行计）。
> **逐字举几个本页正文用到的**：
> - `0.0 鈥?nbsp;1.0 V`（**应为到 `1.0 V` 的一个范围**，本页正文因此只写「到 `1.0 V`」）；
> - `ms_const_curr_disconnect` 的 XPS256 范围：`0 ms 鈥?nbsp;1270 ms`；
> - `t_ms` 的范围：`卤2鈥?47鈥?83鈥?46 ms`（**`卤` 是 `±`**）；
> - `vout_*_settling_t_ms` 的范围：`-10鈥?00 ... 10鈥?00 ms`（**看 `## 版本` 里 7.1.0 那条
>   可推是 `-10000 ... 10000`，但本页不替语料定字**）；
> - `Cadence` 类的词：`Pull鈥慸own`（= `Pull-down`）、`hardware鈥慸efined`、
>   `front鈥慹nd`（= `front-end`）、`卤50 mV`；
> - 单位：`Capacitance in microfarads (渭F)`、`Slew rate in millivolts per microsecond (mV/渭s)`。
> **代价照 §11.2 ① 写清楚：拿「修好的字」去 raw 里搜是搜不到的，要搜坏掉的那个形态。**
>
> **② `t_ms` 的范围，两处对不上。** 参数表里是损坏串 `卤2鈥?47鈥?83鈥?46 ms`；
> `## Functional changes` 里 7.1.0 那条给的是可读的
> `Connect setup time now -2147483647 to 217483647 ms.`
> ——**`217483647` 比 `2147483647` 少一位，而且表里以 `±` 开头、变更条目写的是 `-… to …`。
> 本页并列两处，不替它调和，也不猜表里那串原本是什么。**
>
> **③ `max_voltage_drop_return` 的说明是从 `max_voltage_drop_force` 整段抄来的，没改词。**
> 两条逐字：
> `max_voltage_drop_force`：`Defines a threshold for the voltage drop on the force line above which a channel is disconnected.`
> `max_voltage_drop_return`：`Defines a threshold for the voltage drop on the force line above which a channel is disconnected.`
> **两句一字不差——`return` 那条说的却是 `force` 线。**
> 同一格里还有一句同样没改：
> `The DC Scale UHC4T card and the DC Scale XPS256 card can measure the voltage drop of the force line on the DUT board.`
> （**`return` 那条也写 `force line`。**）
> **本页在正文里按参数名讲 force / return，但引文照原样。**
>
> **④ `voltage_slew_rate` 的默认值单位写错了。** 那一格逐字：
> `Slew rate in millivolts per microsecond (mV/渭s)`（**单位是 mV/µs**），
> 而同一格末尾写 `Default value if not defined: 0 渭F`（**`0 µF`，电容的单位**）。
> **同一格里的 `capacitance` 也写 `Default value if not defined: 0 渭F`** ——
> **看起来是从 `capacitance` 那格抄过来忘了改。**
> **这一条和正文里「单位兼容性完全不校验」那句放在一起看：工具不查，文档自己也会写错。**
>
> **⑤ `voltage_slew_rate` 把同一篇文档推荐了两次。** 那一格逐字：
> `For more information, refer to XPS256 programming - Load step response and XPS256 programming - Load step response.`
> **两处链接指向同一个文件**（`…03.10.11_XPS256_programming_-_Load_step_response.md`）。
>
> **⑥ `## Resource parameters grouped by function` 是一张坏表。**
> 9 个组被塞进 **3 个 2 列表格单元**里（`Connections and timing` + `Current` +
> `Constant current check` 在一个格，`Dynamic behavior` + `Maximum voltage drop` +
> `Other` 在第二个格，`Voltage` + `Voltage settling time` + `Voltage slew rate` 在第三个格），
> 而表格只有两列 —— **本页正文那张 9 组表是按它的标题重新排的，分组名逐字未改。**
>
> **⑦ 组索引里的参数名和参数表里的对不上。** 组索引写的是
> `vout_fall_settling_t_ms__c2c`（**两个下划线**），
> 参数表里的条目是 `vout_fall_settling_t_ms_c2c`（**一个下划线**）。
> **同一篇文档内，同一个参数的两种拼法。**
>
> **⑧ 参数表末尾那句 `Note` 被吞进了最后一个表格单元。** 原文逐字：
> `  |  Note Resource values may be specified in any order, but must not be specified more than once for any DPS pin. If they are, an error is reported.`
> ——**`Note` 和正文之间没有分隔符，而它被放在 `warn_voltage_drop_return` 那一格的第三列上**，
> 于是这句「全局规矩」在结构上成了那个参数的说明。**本页把它当全局规矩讲，是因为它讲的是全局。**
>
> **⑨ `## Related information` 一节里 5 个链接全粘在一起**，中间**没有任何分隔符**。
>
> **⑩ `connect_state` 的适用范围措辞与别人不同**：它写的是
> `This parameter is only for DC Scale cards.`（**cards**），
> 而同一批参数写的是 `This parameter is only for DC Scale pins.`（**pins**）。
> **本页正文照它的「cards」写，未替它统一。**
>
> **⑪ `openLoopProtection` 与 `open_loop_protection` 两种拼法并存。**
> `max_voltage_drop_force` / `max_voltage_drop_return` 两格写的是
> `the openLoopProtection parameter must be set to none`（**camelCase，且链接指向
> `UHCM` 命令参考**），而参数表里的参数名是 `open_loop_protection`（**snake_case，且链接没给**）。
> **本页不判这是同一个东西的两种写法还是两个东西** —— 原文没说。
>
> **⑫ `## Maximum voltage drop on the UHC4T force lines` 一节的标题只提 UHC4T，
> 但讲规则的 `Two rules apply` 里有一句没有卡限定。** 原文：
> `Both max_voltage_drop_force and max_voltage_drop_return must be between 0.0 and 0.5 V.`
> ——**而 XPS256 那一格说自己的可 program 范围到 `1.0 V`**。
> **两处并列看会打架（0.5 V 上限 vs 1.0 V 上限）。**
> **（推断）那句话是 UHC4T 专属的**，**依据是它所在的小节标题写着 `on the UHC4T force lines`，
> 且它上一条 XPS256 的 `0.5 V` 对应的是「超过 0.5 V 要额外改两处设置」而不是「不允许」**。
> **这是推断，原文没有一句话直接说「这条只对 UHC4T」。**

`verified: doc-only`
