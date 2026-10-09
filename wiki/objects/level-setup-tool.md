---
type: object
title: Level setup tool
layer: gui
stage: level
tags: [level, level-setup-tool, gui, equation-based, dpspins, context, pin-alias-set, ungang]
related: [level, level-file, level-master-file, equation-based-level-setup, dpspins-resources, spec-tool, constraint-level-mode-context-match, mapping-level]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14_Level_setup_tool.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# Level setup tool

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **11,312 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14_Level_setup_tool.md>` 及其子主题 `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.02.02.01_Syntax_of_expression.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.02.03.05_Pin_alias_set__PIN_ALIAS_SET.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.02.03.07_DPSPINS.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.02.05.01_Master_file_format_for_level_setup.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.04.02_Specifying_the_context_for_levels.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.04.03_How_to_create_an_equation_set_using_the_Equation_editor.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.04.04_Creating_new_specification_sets.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.06.01.03_Using_the_UNGANG_connect_state_with_DC_Scale_DPS_cards.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Equation based level setup › Elements of Equation Based Level Setup › Syntax of expression）

shsp32

-10.00

ref+sp12*(shmsp5/sp5)

shsp18sp19>shsp32+ct3?shsp18sp19:shsp32+ct3

### Syntax（取自子主题 Equation based level setup › Structure of an equation based level setup › Pin alias set  PIN ALIAS SET）

!`PIN_ALIAS_SET`（raw: `../../../../agent-html/112434.png`）

 |

Pin alias set name

 |

The default pin alias set.

The pin alias defined in this alias set is used as the default in the equation set.

   | Note You can use pin aliases from sets other than the default pin alias set, by adding the set name in front of the pin alias: <pin_alias_set_name>::<pin_alias>`.` If you use a package pin name, add `"::"` before it: `::<`package_pin_name`>`.

### Examples（取自子主题 Equation based level setup › Structure of an equation based level setup › Pin alias set  PIN ALIAS SET）

### Alias set: alias_set_1

In this example, the involved pins are: `clock`, `io_pin`, and `mode`.

| Alias | Pin |
|---|---|
| io_pin_1 | io_pin |
| mode_1 | mode |

### Alias set: alias_set_2

In this example, the involved pins are: `clock`, `io_pin`, and `mode`.

| Alias | Pin |
|---|---|
| io_pin_2 | io_pin |
| mode_2 | mode |

The following is the timing equation set using the pin aliases.

```
EQNSET tim_eqn_set1
PIN_ALIAS_SET alias_set_1
TIMINGSET 1
PINS  ::clock  io_pin_1  alias_set_2::mode_2
...
```

In this example, the keyword PIN_ALIAS_SET specifies `alias_set_1` as the default alias set.

- To use a pin alias from the default alias set, specify the alias pin name without any prefix (for example, `io_pin_1`).
- To use a pin alias from an alias set which is not the default set, explicitly specify the alias set name (for example, `alias_set_2::mode_2`).
- To use a package pin name, add the prefix "::" (for example, `::clock`).

### Example 1: Copy/paste example with all resource keywords（取自子主题 Equation based level setup › Structure of an equation based level setup › DPSPINS）

```
EQNSET 1 "Example equation set 1"

DPSPINS Example_DPS_pin

    vout                        =  5.0      # [V]       Forced output voltage
    ilimit                      = 20.0      # [mA]      Source and sink current limit
    ilimit_source               = 20.0      # [mA]      Source current limit (DC Scale pins)
    ilimit_sink                 = 10.0      # [mA]      Sink   current limit (DC Scale pins)

    t_ms                        = 5.0       # [ms]      Connect setup time

    vout_rise_t_ms_per_volt     = 0.1       # [ms/V]    Inverse slew rate for the rising edge
    vout_rise_t_ms_per_volt_c2c = 0.2       # [ms/V]    Inverse "connect-to-connect" slew rate
    vout_fall_t_ms_per_volt     = 0.1       # [ms/V]    Inverse slew rate for the falling edge
    vout_fall_t_ms_per_volt_c2c = 0.2       # [ms/V]    Inverse "connect-to-connect" slew rate
    vout_rise_settling_t_ms     = 0.5       # [ms]      Settling time for the rising edge
    vout_rise_settling_t_ms_c2c = 0.9       # [ms]      "connect-to-connect" settling time
    vout_fall_settling_t_ms     = 0.5       # [ms]      Settling time for the falling edge
    vout_fall_settling_t_ms_c2c = 0.9       # [ms]      "connect-to-connect" settling time

    offcurr                     = act_min   #           act | min | open | act_min | act_open
                                            #           Defines current to apply in disconnected state

    vout_frc_rng                =  8.0      # [V]       Force voltage range
    iout_clamp_rng              = 50.0      # [mA]      Clamp current range

    disable_const_curr_check                #           Switch off constant current check
    ms_const_curr_disconnect    = 10.0      # [ms]      Delay for constant current flag (UHC4T + XPS256)

    connect_state               = ungang    #           norm (see note below) | himp | ungang |
                                            #           hdig (UHC4T) | hdig (UHC4T)

    ms_fast_preload             = 8.0       # [ms]      Full current (40A) for the specified time (UHC4T)
    max_voltage_drop_force      = 3.0       # [V]       Upper FS drop limit (UHC4T + XPS256)
    max_voltage_drop_return     = 3.0       # [V]       Lower FS drop limit (UHC4T + XPS256)
    protect                                 #           Current limiter (UHC4T)
    voltage_filter_frequency    = 2000.0    # [Hz]      Force voltage or clamp voltage filter (XPS256))
    current_filter_frequency    = 2000.0    # [Hz]      Force current or clamp current filter (XPS256))

    #
    # Parameters supported only by XPS256
    #
    capacitance                 = 100       # [uF]      Specifies the load capacitance on the DUT board.
    load_step_mode              = std       #           std, fast
    open_loop_protection        = diode     #           diode, none
    pulldown                    = on        #           on, off
    voltage_slew_rate           = 50        # [mV/us]
    warn_voltage_drop_force     = 0.3       # [V]
    warn_voltage_drop_return    = 0.2       # [V]

LEVELSET 1 "Example level set 1"            # Dummy for this example: At least one level set needs to be specified
```

The copy/paste example above shows all available keywords for the DPS pin resources and the DPS modulation set. The example is not valid for all types of DPS and must be adapted to the really used DPS.

The default value norm of DPS pin resource connect_state can be selected for the conn state column in the `DPS Setup window`（raw: `02.08.04.14.03.02_How_to_read_the_DPS_Setup_window.md`） of the Level setup tool and can be programmed by the related command `PSLR`（raw: `../02.06_Command_Reference/02.06.02.02.194_PSLR__PSLR__-__Power_Supply_Level_Ranges.md`） but cannot be programmed explicitly in the level setup equations. The parameter connect_state must be omitted to define the default value norm in the level setup equations.

### Example（取自子主题 Equation based level setup › Level setup master file › Master file format for level setup）

### Level master file

```
hp93000,level_master_file,0.1

# this is a comment
testerfile: demo.lev

EQNSET 1 [PIN_ALIAS_SET usb_set]: files/eqnset01.lev
EQNSET 2 : files/eqnset02.lev
EQNSET 3 : files/eqnset_34.lev
EQNSET 4 : files/eqnset_34.lev
TESTDATA : files/testdata.lev
DEFINES : files/defines.lev
GENERAL: GENERAL.lev
```

In the assembled level setup file `demo.lev`, the alias set `usb_set` is used in the equation set 1. When `demo.lev` is splitted, the alias set `usb_set` is removed from the generated sub-file `eqnset01.lev` and package pin names are used.

### Examples（取自子主题 Opening and using the Level Setup Tool › Specifying the context for levels）

### Context "DEFAULT"

The level equation set shown in the figure below defines the levels for the context DEFAULT. Because it is a conventional level setup for std pins, it is not, in fact, necessary to define any context as the DEFAULT context will be automatically assumed when no context is defined.

This level equation set represents a DEFAULT context, and it defines the levels for all std mode pins without any FAST mode pins in a single-ended configuration.

 !`Standard-Level Setup for Single-Ended Pins (DEFAULT Context)`（raw: `../../../../agent-html/55992.png`）

### Context "differential"

The name differential is an arbitrary context name given here to describe a differential setup but any other name except DEFAULT could also be used.

The level setup for this example includes differential pins in FAST mode and a termination chosen to be center_tap to set up a differential configuration.

 !`Level File: FAST mode, Differential Pins, Center Tap Termination`（raw: `../../../../agent-html/55993.png`）

### Example（取自子主题 Opening and using the Level Setup Tool › How to create an equation set using the Equation editor）

- In the Test Program Explorer, double-click the <Levels> icon.

The Level Setup window opens.

- In the Level Setup window, click on the menu

Select > Edit Equations.

The equation editor (NEdit) opens.

- In the first line, type:

EQNSET 1 "NonSpecs"

- Enter data for the DPS pin Vcc:

```
DPSPINS Vcc
 vout = 4.5
 ilimit = 1000
 t_ms =4
 offcurr = act
```

- Create the level set (every level set must contain information for all pins defined in your pin configuration)

LEVELSET 1 "nominal"

- Enter information for the input pins:

```
PINS ctrl ser_in
 vil = 0
 vih = 4.3
```

- Enter information for the output pins:

```
PINS ser_out
 vol = 2.4
 voh = 2.6
```

- Enter information for the I/O pins:

```
PINS io_pins
 vil = 0
 vih = 4.3
 vol = 2.4
 voh = 2.6
```

- On the menu, click Shell > Downloadto download the level to the tester hardware and make sure you correct any reported error in the Report window.
- Save your changes in the Test Program Explorer:

  - Right-click <Levels...>.
  - Click Save As.
  - In the Enter or select NEW file name window type the file name (for example: levels).
  - Click OK.

 !`Save Level setup`（raw: `../../../../agent-html/135366.png`）

_Do not use the File > Save option of NEdit. In order to save your work you must first download the changed data, and then save them from the Test Program Explorer.

### Example 1 (without using variables)（取自子主题 Opening and using the Level Setup Tool › Creating new specification sets）

- In the Level Setup tool, select the menu item Select > Edit Specifications.

Alternatively you can go <93000> <Setup> <Spec Tool>.

If the Select specification window opens:

  !`Select specification`（raw: `../../../../agent-html/131014.png`）  In the window click done.

You access `The Spec Tool window`（raw: `02.08.04.30.01_The_Spec_Tool_window.md`）.

- On the menu, click Change > Create Specification.
- Click the equation set 1 NonSpecs in the Eqn Description area.
- Click create.

The Create level spec set window opens.

- Select "1" in the Unused Numbers area.

The line of the selected number will be highlighted in red.

- In the Description field, enter nospecs.
- Click Create.
- In the Select level equation set window, click done.

In the Levels line, the Spec Tool shows the message "modified, download required".

- Click Download(the Down arrow icon in the Spec Tool).

Since the specification "nospecs" has no values, no further action is required.

This level specset is now ready to use in SmarTest.

- In the Test Program Explorer save the levels file.

### Example 1 (using a variable)（取自子主题 Opening and using the Level Setup Tool › Creating new specification sets）

- From the Level Setup window select Select > Edit Specifications. This opens the Spec Tool.
- In the SpecTool, select Change > Create Specification.
- Select the Equation Set 2 specs.
- Click create.

You now see a window with the heading Create level spec set.

- Select 1.

You are defining a specification that points to spec set 1.

- In the Description field, enter Vcc = 4.5V.
- Click create.
- Click done in the Select level equation set window.

You see the variable names for this spec set in the SpecTool Name column.

- Repeat the procedure for all spec variables accordingly.

After you have defined the specifications:

- Click the Download icon (the down arrow in the SpecTool) and check the Report window for errors.
- In the Test Program Explorer right-click the level file and Save.

### Description（取自子主题 Level setup related use cases › Setting up the Device Power Supply › Using the UNGANG connect state with DC Scale DPS cards）

Here are three examples applying different voltage and ampere values for 32 ganged DPS128 channels and `connect_state = UNGANG`

### Example 1: 2.5 V, 5 A（取自子主题 Level setup related use cases › Setting up the Device Power Supply › Using the UNGANG connect state with DC Scale DPS cards）

```
vout_frc_rng = 2.5V, iout_clamp_rng = 5A
```

At 2.5 V, each channel can source or sink 1.0 A.

|  | Number of channels | = ceil(5A / 1.0A) = 5 |
|---|---|---|
|  | Current per channel | = 5A / 5 = 1.0A |

Five channels will be set to the 1.0 A clamp range, 27 channels will be detached.

### Example 2: 7 V, 5 A（取自子主题 Level setup related use cases › Setting up the Device Power Supply › Using the UNGANG connect state with DC Scale DPS cards）

```
vout_frc_rng = 7V, iout_clamp_rng = 5A
```

At 7 V, each channel can source or sink 0.5 A.

|  | Number of channels | = ceil(5A / 0.5A) = 10 |
|---|---|---|
|  | Current per channel | = 5A / 10 = 0.5A |

Ten channels will be set to the 1.5A clamp range, 22 channels will be detached.

### Example 3: 7 V, 100 µA（取自子主题 Level setup related use cases › Setting up the Device Power Supply › Using the UNGANG connect state with DC Scale DPS cards）

```
vout_frc_rng = 7V, iout_clamp_rng = 100µA
```

At 7 V, each channel can source or sink 0.5 A.

|  | Number of channels | = ceil(100µA / 0.5A) = 1 |
|---|---|---|
|  | Current per channel | = 100µA / 1 = 100µA |

One channel will be set to the 100 µA clamp range, 31 channels will be detached.

The 100 µA current clamp range is allowed, because only one channel remains active so this is effectively a single channel and no longer a gang.

<!-- 语法节 end -->

## 是什么

**Level Setup tool 是 SmarTest 里配 level（电平）的那个工具**——从器件级的驱动 / 比较电平（`vil` / `vih` /
`vol` / `voh` / `vt` / `term`），到 Device Power Supply 的输出电压、电流限、连接状态与斜坡，
都在它这里配。

定义文档 `02.08.04.14_Level_setup_tool.md` 只有一句正文：

> 「This section gives you the information to set up the level for your device: background information, interface descriptions and task related information.」

### 定义文档自己声明的六个子主题（这六项就是这个工具的功能面）

| 子主题（raw） | 管什么 |
|---|---|
| `02.08.04.14.01_Basic_concepts_of_levels.md` | 概念（导语说的 background information） |
| `02.08.04.14.02_Equation_based_level_setup.md` | **equation based 的 level setup** |
| `02.08.04.14.03_Elements_of_the_Level_Setup_window.md` | 窗口元素（interface descriptions） |
| `02.08.04.14.04_Opening_and_using_the_Level_Setup_Tool.md` | **怎么开、怎么用**（task related information） |
| `02.08.04.14.05_Level_setup_related_card_specifications.md` | 卡相关规格 |
| `02.08.04.14.06_Level_setup_related_use_cases.md` | 用例 |

**这六项是文档事实**（正好对上导语点名的三类信息）。**本页没读这六篇**——
本页的依据是本页「语法 / 参数」节，它逐字抽了这六棵子树里的**八篇**（来源写在段名里）。

### 入口：从 Test Program Explorer 的 `<Levels>` 图标进

语法节里的例子第一句就是入口：

> 「In the Test Program Explorer, double-click the <Levels> icon.」

**保存也在那儿**（见下面「保存的规矩」）——**这个工具的打开与保存都不在它自己里面**。

### 两条编辑路线

| 路线 | 入口 | 在本页语法节里的痕迹 |
|---|---|---|
| **写 equation** | `Select > Edit Equations`，打开 **NEdit** 编辑器 | **完整例子**（`.14.04.03`：`EQNSET` / `DPSPINS` / `LEVELSET` / `PINS`） |
| **改 GUI 上的列** | 直接在 Level Setup window 的列里改 | 只有一句：`conn state` 列（DPS Setup window） |

**「两条路线」是本页的归纳（推断）**：语法节里两条路各有一处痕迹，但**没有一句把它们并列为两条路线**。
本页并列它们，理由是同阶段的 [[mapping-level]] 主表也是按「GUI 列 ↔ 文件关键字」两轴组织的。

### equation set 与 context（④ 图证填了语法节没给的那个关键字）

原文对 context 的说明只有两句（都在语法节里）：

- **DEFAULT 不用写**：因为 std pin 的常规 level setup「it is not, in fact, necessary to define any context
  as the **DEFAULT context will be automatically assumed when no context is defined**」。
- **别的 context 名字随便取**：「The name **differential** is an arbitrary context name given here
  to describe a differential setup but **any other name except DEFAULT** could also be used.」

**但语法节从头到尾没有出现「文件里用什么关键字写 context」**。**本页开了语法节嵌的那两张 level 文件的图，
这个洞由图填上了**（详见下面 ④ 图证那一节）：关键字是 **`MODECONTEXT`**。

### equation 里的表达式（语法节的四个例子）

语法节给的表达式例子有四个：常量 `-10.00`；引用 spec 变量的 `ref+sp12*(shmsp5/sp5)`；
`shsp32`；以及带 `?:` 的 `shsp18sp19>shsp32+ct3?shsp18sp19:shsp32+ct3`。
**运算符的含义本页没读**——那是 `.14.02.02.01_Syntax of expression` 那篇的事，**本页没有它的依据**。

### DPS 资源：`DPSPINS` 块

语法节里有一份**逐关键字带单位注释的 copy/paste 例**（`DPSPINS` 块，含 `vout` / `ilimit` /
`ilimit_source` / `ilimit_sink` / `t_ms` / 四个斜坡参数 / 四个 settling 参数 / `offcurr` /
`vout_frc_rng` / `iout_clamp_rng` / `connect_state` 等，末尾注明「Parameters supported only by XPS256」
的一组）。原文对这份例子的定性是：

> 「The copy/paste example above shows all available keywords for the DPS pin resources and the DPS modulation set. The example is not valid for all types of DPS and must be adapted to the really used DPS.」

**一条容易踩的规矩**（原文专门写了一段）：`connect_state` 的默认值 **`norm`** **不能显式写在 equation 里**——

> 「The default value norm of DPS pin resource connect_state can be selected for the conn state column in the DPS Setup window of the Level setup tool and can be programmed by the related command PSLR but cannot be programmed explicitly in the level setup equations. The parameter connect_state must be omitted to define the default value norm in the level setup equations.」

**即：要 `norm` 就不要写 `connect_state`。**（`PSLR` 是命令侧的做法，**本页没读它**。）

### 一个用例：32 通道 ganged DPS128 + `UNGANG`

语法节末尾是 `UNGANG` 的三个例子（`connect_state = UNGANG`，32 通道 ganged DPS128）。
**结论很实用**：`UNGANG` **不是让 32 个通道一起并联**，而是**按需要的电流算出要几个通道、剩下的 detach**：

| 例 | 每通道能力 | 需要的通道数 | 被设到哪个 clamp 档 | detach 掉几个 |
|---|---|---|---|---|
| 2.5 V / 5 A | 1.0 A | `ceil(5A / 1.0A) = 5` | 1.0 A | 27 |
| 7 V / 5 A | 0.5 A | `ceil(5A / 0.5A) = 10` | **1.5A** | 22 |
| 7 V / 100 `碌`A | 0.5 A | `ceil(100碌A / 0.5A) = 1` | 100 `碌`A | 31 |

三例的通道数都恰好凑回 32（5+27 / 10+22 / 1+31）——**这是原文自己给的算式**。
第三例还多讲了一句为什么小电流档允许：
「The 100 碌A current clamp range is allowed, because only one channel remains active so this is effectively a single channel and no longer a gang.」
（**`碌` 是坏字，应为 `µ`**——见「出处」的瑕疵区。）

### 保存的规矩：先 Download，再从 Test Program Explorer 保存

语法节里这条是**加了下划线的强调句**：

> 「Do not use the File > Save option of NEdit. In order to save your work you must first download the changed data, and then save them from the Test Program Explorer.」

**即：NEdit 自己的 `File > Save` 不能用**；顺序是「**先 Download → 再在 Test Program Explorer 里保存**」。

### ④ 图证：语法节嵌的 5 张图，本页全看了

**这 5 张图都在本页「语法 / 参数」节里**，本页逐张打开
（目录都是 `F:\master-dev\dorm-wsl-sytest\tdc-html\raw\`）。
**先给结论：图填掉了一个语法节没给的洞（`MODECONTEXT`），另有两条图注是语法节没有的规矩。**

**（a）`55992.png` 与 `55993.png` —— 两张 level 文件的截图，填掉了 `MODECONTEXT` 这个洞。**

两张图的画面都是**一个 equation set 的正文**，第一行就是语法节里从来没有的那个关键字：

| 图 | 图注（alt） | 图上第一行 |
|---|---|---|
| `55992.png` | `Standard-Level Setup for Single-Ended Pins (DEFAULT Context)` | `EQNSET 3 "SE_DEFAULT"`，紧接 `MODECONTEXT "DEFAULT"` |
| `55993.png` | `Level File: FAST mode, Differential Pins, Center Tap Termination` | `EQNSET 1 "DIFF_fastI_fasto"`，紧接 `MODECONTEXT "differential"` |

两张图上 `MODECONTEXT "<名字>"` 都**紧跟在 `EQNSET` 行之后**，并各带一个红框批注：
`55992.png` 上是 `"Default" context definition optional`，`55993.png` 上是 `Context definition`。

**所以「文件里怎么指定 context」的答案是 `MODECONTEXT`——语法节答不了，图答了。**

**这两张图还给了 equation set 的实际骨架（语法节只有片断）**：

- `55992.png`（单端 / DEFAULT）：`EQNSET` → `MODECONTEXT` → **`SPECS` 段**（声明
  `v_il` / `v_ih` / `v_ol` / `v_oh` / `v_term` / `v_threshold` 六个 spec 变量，各带 `[V]`）→
  **`EQUATIONS` 段**（图上只有两行注释：`# put here depend specs` / `# resources in [V] and [mA]`）→
  `LEVELSET 1 "single_ended"` + **`PINS all`**（`vil = v_il` / `vih = v_ih` / `vol = v_ol` / `voh = v_oh`，
  **即「资源 = spec 变量」这种绑定**；`#vch =` 与 `#vcl =` 是**注释掉的**；另有
  `vt = (v_il + v_oh) / 2`、`iol = 10`、`ioh = 10`）→
  `LEVELSET 2 "single_cross"` + `PINS DrvAll_SiSo` + `PINS RcvAll_SiSo`（内含 `term single_ended_cross`，
  图注写 `Single ended cross termination ("o" pins)`）。
- `55993.png`（差分 / FAST）：`MODECONTEXT "differential"` → `SPECS` 段（`v_com_drv` / `v_swing_drv` /
  `v_term` / `v_threshold` / `v_com_rec` / `v_swing_rec`）→ `LEVELSET 2 "diff_center"` +
  **`PINS A0@diff # I-pins, differential pair (A0,A0-)`**（`vil = v_com_drv - v_swing_drv`、
  `vih = v_com_drv + v_swing_drv`，图注 `Differential drive levels`）+
  **`PINS A1@diff # O-pins, differential pair (A1,A1-)`**（`term center_tap`、`vt = v_term`、
  `rec_swing = v_swing_rec`、`rec_offset = v_com_rec`，图注 `Differential compare`）。

**两条图注是语法节没有的规矩**：

- `55992.png` 上 `PINS all` 那行旁边写着 **`No "term" definition required for "single ended", "std" pins`**
  ——**单端 std pin 不必写 `term`**。
- `55993.png` 给出了差分那一套的**算法形状**：驱动侧 `vil` / `vih` 是**共模 ± 摆幅**算出来的，
  比较侧用 `term center_tap` + `vt` + `rec_swing` / `rec_offset`。

**哪些字在 raw 里 grep 不到（这是 §11.4 ④ 档的判据）**：

| 图上读到的串 | 9,398 篇 raw md 里的命中篇数 |
|---|---|
| `SE_DEFAULT` | **0** |
| `DrvAll_SiSo` | **0** |
| `RcvAll_SiSo` | **0** |
| `DIFF_fastI_fasto` | **0** |
| `diff_center` | **0** |
| `v_com_drv` / `v_swing_drv` / `v_com_rec` / `v_swing_rec` | **各 0** |
| `MODECONTEXT` | 24（**但没有一篇在本页 `sources:` 里**） |
| `single_ended_cross` / `center_tap` / `v3h` | 4 / 11 / 22 |
| `rec_swing` / `rec_offset` | 各 8 |
| `A0@diff` / `A1@diff` | 2 / 1 |

**严格够「grep 不到」这条判据的是上表上半那七个串。** 下半那些能搜到，
**但一篇都不在本页 `sources:` 里**——**本页照样把它们算图证：本页的来源是图，不是那 24 篇**
（**那 24 篇本页一篇没读**）。**要核只能自己再开那两张图。**

**图答不了的一处，照实说**：图上输入侧写 `PINS A0@diff`，而 `MODECONTEXT` 那行写 `"differential"`
——**`@diff` 和 `differential` 是不是同一个名字，图上没说，本页 sources 里也没有一句**。
（`A0@diff` 这个串在 raw 里 2 篇能搜到，但那两篇不在本页 `sources:` 里。）**本页不敢断，留在这里。**

**（b）`112434.png` —— `PIN_ALIAS_SET` 语句的构成图。**

语法节里 `PIN_ALIAS_SET` 只有一行例子（`PIN_ALIAS_SET alias_set_1`）。图上是一个流程图：
**`PIN_ALIAS_SET` → `pin alias set name` → `comment` → `end of line marker`**，
**其中 `comment` 那一格有一条绕回去的支路**——即**注释是可选的**。

**这张图有两个串 grep 不到**：`pin alias set name`（**0**）与 `end of line marker`（**0**）。
`PIN_ALIAS_SET` 本身能搜到。**所以本页据图记下的是**：这条语句 = 关键字 + 集合名 + 可选注释 + 行结束标记。

**（c）`131014.png` —— 「选 equation set」对话框。**

alt 写的是 `Select specification`，**图上标题栏读作 `Select level equation set`**
（另有 `Regular Expression Filter` 输入框、`Eqn Description` 列表里一行 `1 NonSpecs`、
四个按钮 `create` / `filter` / `help` / `done`）。**同一张图在 [[spec-tool]] 页也引了，那边逐字列了全表。**

**（d）`135366.png` —— 「Save Level setup」。**

alt 写 `Save Level setup`，图上标题栏是 **`Enter or select NEW file name`**，
`Name:` 里填的是 **`levels`（无扩展名）**，`Save in folder:` 是 `levels`。
**这张图没有一个 0 命中的串**（`Enter or select NEW file name` 2 篇、`Save Level setup` 2 篇），
**所以本页不把它当 ④ 档判据**——它的用处只是**印证**例子第 8 步填的文件名就是 `levels`。

**（e）图整体答不了的**：哪些关键字必填、哪些组合非法、`EQUATIONS` 段真正的语法、
`SPECS` 的 `[V]` 单位声明是否必须——**两张 level 文件图是「某一次具体配置」的截图，不是格式规范**。
**而且 5 张图里没有一条固件命令名、没有一个 API 名**——所以本页的 L1 / L2 两列**一格都没动**。

## 典型用法

### 从零写一个 equation set 并下载（语法节 `.14.04.03` 的完整例子）

| # | 做什么 | 原文要点 |
|---|---|---|
| 1 | 在 Test Program Explorer 里**双击 `<Levels>` 图标** | Level Setup window 打开 |
| 2 | `Select > Edit Equations` | 打开 equation editor（**NEdit**） |
| 3 | 第一行写 `EQNSET 1 "NonSpecs"` | equation set 号 + 描述名 |
| 4 | 写 `DPSPINS` 块（例子里是 `Vcc`：`vout = 4.5` / `ilimit = 1000` / `t_ms = 4` / `offcurr = act`） | |
| 5 | 写 `LEVELSET 1 "nominal"` | **每个 level set 必须含 pin configuration 里所有 pin 的信息**（原文括注：`every level set must contain information for all pins defined in your pin configuration`） |
| 6 | 按 pin 类型分组写 `PINS` 块 | 输入 pin：`PINS ctrl ser_in` + `vil` / `vih`；输出 pin：`PINS ser_out` + `vol` / `voh`；I/O pin：`PINS io_pins` + 四个都给 |
| 7 | `Shell > Download` | **下到硬件，并到 Report window 里把报的错改掉**（原文：`make sure you correct any reported error in the Report window`） |
| 8 | 在 Test Program Explorer 里 Save As | 右键 `<Levels...>` → `Save As` → 填文件名（例子里填 `levels`）→ `OK` |

**第 8 步是本页最容易做错的一处**：**不要用 NEdit 的 `File > Save`**（原文原话见上面「保存的规矩」）。

### 用 context 时怎么走（三条都是从原文读出来的）

1. **std pin 的常规 setup → 不用管 context**：不写就是 `DEFAULT`（原文：没有 context 定义时
   DEFAULT context 会被自动假定）。
2. **差分 / FAST 这类非默认配置 → 自己起一个 context 名**（例子里叫 `differential`），
   **在文件里用 `MODECONTEXT "<名字>"` 指定**（见 ④ 图证）。
3. **`DEFAULT` 这个字是保留的**——原文写「any other name **except DEFAULT** could also be used」。

**⚠️ 一处需要对齐的地方（本页只引了 wiki 页，没读它的 raw）**：
[[constraint-level-mode-context-match]] 那一页说 level / timing / vector **三处的 context 必须相同**，
而 context 是**在 pin configuration 里用 `CTXT` 命令建的**。**本页的 sources 里没有这两句**
（本页的原文只说「名字随便取」）——**两处不必然矛盾**（先建 context、再在 level 里用它），
但**「名字随便取」与「必须先在 pin configuration 里建」的关系，本页没有依据可判**，照实留在这里。

### 建 spec set（这是 Spec Tool 的活）

`Select > Edit Specifications` 打开 **Spec Tool**（或 `<93000> <Setup> <Spec Tool>`），
步骤与两条 `nospecs` / `Vcc = 4.5V` 的例子见 [[spec-tool]]——**本页只给入口**。

## 和谁有关

每条都说清**是什么关系**：

- [[test-program-explorer]] —— **它的开关都在那儿**：双击 `<Levels>` 打开、`Save As` 保存、
  NEdit 的 `File > Save` 不能用。**这是本页最强的两条关系之一。**
- [[report-window]] —— **下游 / 校验口**。`Shell > Download` 之后要去那里看报错并改正。
- [[level-file]] —— **产物**。这个工具编的就是它；语法节里的块（`EQNSET` / `DPSPINS` / `LEVELSET` /
  `PINS` / `SPECS`）是它里面的东西。**它在文件里的完整结构见那一页。**
- [[spec-tool]] —— **配套工具（另一个入口）**。从本工具的 `Select > Edit Specifications` 进 Spec Tool；
  而 spec set 是挂在 **equation set** 上的，equation set 归本工具管。**spec 的 global / local scope 在那边。**
- [[level-master-file]] —— **把它编的东西拆成多文件时用的索引**。本工具出一个整体文件，
  master file 用 `EQNSET <n>: <file>` 把它拆开。**这对关系属于 level 阶段内部的上游/下游。**
- [[equation-based-level-setup]] —— **它支持的第一条路线**（相对的是 fixed level setup）。**概念页。**
- [[dpspins-resources]] —— **DPS 那一族参数的专页**。语法节里 `DPSPINS` 的每个关键字、
  五个 `offcurr` 取值、八个斜坡参数，逐条的解释在那边。
- [[pin-configuration-file]] —— **前置（上游）**。原文那句「每个 level set 必须含 pin configuration 里
  所有 pin 的信息」把两个阶段钉在一起；**level 是 pin 配置的下游。**
- [[constraint-level-mode-context-match]] —— **约束页**。它管的是「level / timing / vector 三处的
  context 必须相同」。**本页只引了那一页的结论，没有读它的 raw**（见「典型用法」里那处 ⚠️）。
- [[mapping-level]] —— **同阶段的对照表页**。本页与它一致：那里的 GUI 格写本工具的列 / 菜单，
  文件格写 [[level-file]]，L1 格写命令。**本页与它没有冲突。**
- [[level]] —— 本页 `stage: level` 的理由：它就是这一段的主工具。
- **定义文档自己声明的六个子主题**（raw 路径见「是什么」那张表）——**本页没读这六篇**。
  它们是本工具的完整说明（概念 / equation based / 窗口元素 / 用法 / 卡规格 / 用例），
  §9.1 第 4 条说这类子主题算「会存在的页」；但它们不在 `extract/prose-allowlist.txt` 里，
  **故按规矩用反引号 + raw 路径，不写双方括号**。
- **本页 `sources:` 之外、但语法节引到的 8 篇**（`02.08.04.14.02.02.01`、`.14.02.03.05`、
  `.14.02.03.07`、`.14.02.05.01`、`.14.04.02`、`.14.04.03`、`.14.04.04`、`.14.06.01.03`）
  —— **全是子主题，本页都没读**。

## 版本

**本文档没有 `## Functional changes` 段。**（定义文档 `02.08.04.14_Level_setup_tool.md` 只有
18 行：frontmatter、`## Subtopics` 六项、一句导语。**这是事实，不是缺陷。**）

**所以本页没有版本条目可记。** 语法节那八篇子主题各自的 `## Functional changes` **本页没读**，
**本页不替它们推断版本**——「Level Setup tool 是哪个版本引入的」在语料里本页**没找到**。

## 出处

`sources:` 一篇：
`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14_Level_setup_tool.md`
（TDC `17694.htm`，**906 字节 / 18 行**）。

**本页「语法 / 参数」节那 11,275 字符不是来自它**——段名里写着来源是**八篇子主题**：
`02.08.04.14.02.02.01_Syntax_of_expression`、`.14.02.03.05_Pin_alias_set__PIN_ALIAS_SET`、
`.14.02.03.07_DPSPINS`、`.14.02.05.01_Master_file_format_for_level_setup`、
`.14.04.02_Specifying_the_context_for_levels`、`.14.04.03_How_to_create_an_equation_set_using_the_Equation_editor`、
`.14.04.04_Creating_new_specification_sets`、`.14.06.01.03_Using_the_UNGANG_connect_state_with_DC_Scale_DPS_cards`。

**本页没做的**：

- **定义文档声明的六个子主题一篇都没读**（概念 / equation based / 窗口元素 / 用法 / 卡规格 / 用例）。
  **所以本页不知道 Level Setup window 里有哪些列、哪些按钮、哪个面板**——
  本页只知道语法节提到的 `conn state` 列这一个。
- **八篇语法节来源一篇都没回去读**。本页只**描述这一节的结构与内容**，没有引用它们之外的东西。
- **没有读任何命令 / API 文档**：`PSLR`、`SVLR`、`EQSP`、`EQFS`、`DFTD` 这些名字只作为
  **语法节原文里的串**出现，**它们的参数、语法、返回值本页一个字没有**。
- **看完了语法节嵌的 5 张图**：`112434.png`、`55992.png`、`55993.png`、`131014.png`、`135366.png`
  （逐张的逐字内容与 grep 结果见「④ 图证」那一节）。
  **定义文档 `02.08.04.14_Level_setup_tool.md` 自己一张图都没有**（实测 0 处 `raw/` 引用），
  **所以本页 `sources:` 里没有图；能看的图只有本页语法节带的那 5 张，本页全看了。**
- **没有实跑**：没有开过 Level Setup tool、没有写过 equation set、没有 Download 过、没有生成过 level 文件。
  `verified: doc-only` 指的就是这件事。
- **没有动 `wiki/index.md`**，也没有把本页挂进 `wiki/stages/level.md`。

**⚠️ 本页读到的语料瑕疵，照原样记下、一处都没替它改（§11.2）**：

- **`碌` 是本页语法节里唯一的坏字，共 7 处，它是 `µ`。**（坏字是「UTF-8 被按 GBK 读」那一族，§11.2 ①。）
  7 处里的两个例子照原样写在这里：`vout_frc_rng = 7V, iout_clamp_rng = 100碌A`、
  `One channel will be set to the 100 碌A clamp range, 31 channels will be detached.`
  ——**引文与正文里的 `碌` 一处都没换掉**；**但拿修好的 `µA` 去 raw 里 grep 是搜不到的，要搜 `碌`**。
- **`connect_state` 的取值注释里 `hdig (UHC4T)` 出现了两次**（原文：
  `connect_state               = ungang    #           norm (see note below) | himp | ungang |` 换行
  `#           hdig (UHC4T) | hdig (UHC4T)`）。**两个取值一模一样**——
  是漏了一个、还是语料如此，**原文没说，本页不判**（§10：并列记录，不选一个当正确答案）。
- **两处 `(XPS256))` 多一个右括号**：`voltage_filter_frequency    = 2000.0    # [Hz]      Force voltage or clamp voltage filter (XPS256))`
  与 `current_filter_frequency    = 2000.0    # [Hz]      Force current or clamp current filter (XPS256))`。
- **`Do not use the File > Save option of NEdit.` 这句前面有一个落单的下划线 `_`**
  （原文写成 `_Do not use the File > Save option of NEdit.`，**没有配对的收尾 `_`**）。
- **`UNGANG` 第二例的 clamp 档对不上算式**：7 V 时每通道 0.5 A、`ceil(5A / 0.5A) = 10`，
  但结论写的是「Ten channels will be set to the **1.5A** clamp range」——**`1.5A` 在算式里没有来处**
  （第一例与第三例的档位都与算式对得上）。**可能是「clamp 档位是离散档、要取能覆盖的那个」**，
  **但原文没有档位表，本页不替它解释**（§10：并列记录）。
- **同一个东西在同一份例子里两种文件名写法**：`EQNSET 1 [PIN_ALIAS_SET usb_set]: files/eqnset01.lev`
  与 `EQNSET 2 : files/eqnset02.lev` 用**无下划线**的 `eqnset01` / `eqnset02`，
  而 `EQNSET 3 : files/eqnset_34.lev` 用**有下划线**的 `eqnset_34`（同一份例子里两种写法）。
  全库 grep：`eqnset01.lev` 2 篇、`eqnset_01.lev` 3 篇。
- **取值与行内空格不一致**：`EQNSET 2 : files/eqnset02.lev` 冒号前有空格，
  而 `GENERAL: GENERAL.lev` 冒号前没有（同一份例子里两种写法）。
- **`PIN_ALIAS_SET` 那一段的行内标记错位**：原文在 `<pin_alias>` 后面**紧跟一个反引号、再跟句号**
  （读起来像是行内代码的收尾反引号放错了位置），之后才是
  `If you use a package pin name, add "::" before it: ::<package_pin_name>.`——
  **本页照原样记，不改**。
- **语法节里那条步骤被拆成了两行**：`In the Level Setup window, click on the menu` 后面空一行才是
  `Select > Edit Equations.`——**菜单路径与它的引导句被一个空行断开**。

**本页检查过、但本页没遇到的瑕疵**：**§11.2 ⑤ 的整词替换本页实测 0 处**
（那一族的坏串形如 `DC/DC power units`——**它是被替换坏的 `Index`，不是一个可用的名字，
不许抄进任何代码**），故本页**没有任何坏标识符**；**`渭`（μ）/ `卤`（±）/ `鈥` 一族本页也没遇到**
（本页语法节里的汉字只有 `碌` 这一种，7 处）。

**引文规范化的说明**：本页引用块里的英文，**除 §11.1 允许的六条**（折叠空白、剥 markdown 链接标记、
去 `**` 与反引号、去中日韩引号、统一破折号、统一弯引号）**之外，一个字符都没动**。

`verified: doc-only`
