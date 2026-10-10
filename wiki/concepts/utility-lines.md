---
type: concept
title: Utility lines
layer: n/a
stage: pin
tags: [concept, utility-lines, dut-board, infrastructure, pogo-block, sequencer-control, grounding]
related: [utility-line-assignments, sequencer-controlled-utility-lines, dut-interface-layout, utility-card, utility-pogo-block-utility-card-v93000-exa-scale-systems, dut-board-grounding, spec-tool, pin]
sources:
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.04_Utility_lines.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# Utility lines

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **12,252 字符逐字取自** `<02_System_reference/02.03_DUT_board_design_reference/02.03.04_Utility_lines.md>` 及其子主题 `<02_System_reference/02.03_DUT_board_design_reference/02.03.04.02_Utility_line_characteristics.md>`、`<02_System_reference/02.03_DUT_board_design_reference/02.03.04.05.04_Mask_mode_of_sequencer-controlled_utility_lines.md>`、`<02_System_reference/02.03_DUT_board_design_reference/02.03.04.05.05_Galvanic_separation_between_utility_line_serial_interface_and_digital_pi.md>`、`<02_System_reference/02.03_DUT_board_design_reference/02.03.04.05.06_Setting_up_sequencer_control_of_utility_lines.md>`、`<02_System_reference/02.03_DUT_board_design_reference/02.03.04.07.01_Designing_compatible_utility_lines.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example 1: Utility line circuitry (Active wiring board of V93000 systems)（取自子主题 Utility line characteristics）

The diagram shows the typical utility line interface circuitry on a system fitted with the active wiring board.Note Utility lines URW00 …nbsp;URW15 feature an additional pull-up resistor to +5 V on some utility pogo blocks. For devices with higher input impedance, we therefore strongly recommend adding an external pull-up resistor in the region of several hundred Ohms, depending on the type of device used. For more information, refer to table `Internal pull‑up resistor of utility lines`（raw: `02.03.04.02_Utility_line_characteristics.md#_21418__s_Pull-up_resistor_of_utility_lines_V93000_systems`） above.!`Utility read/write line - active wiring board`（raw: `../../../../raw/136929.png`）

"+5V" is the `Internal utility power supply (V93000 systems)`（raw: `02.03.05.05_Internal_utility_power_supply__V93000_systems.md`） that is available at pogo pins "UP5V" of all utility pogo blocks.

### Example 2: Utility line circuitry (Passive wiring board of V93000 systems)（取自子主题 Utility line characteristics）

The diagram shows the utility line interface circuitry on a system fitted with the passive wiring board.

 !`Utility read/write line - passive wiring board`（raw: `../../../../raw/74690.png`）

"+5V" is the `Internal utility power supply (V93000 systems)`（raw: `02.03.05.05_Internal_utility_power_supply__V93000_systems.md`） that is available at pogo pins "UP5V" of all utility pogo blocks.

### Example 1: SmarTest 7 dynamic mask（取自子主题 Sequencer-controlled utility lines › Mask mode of sequencer-controlled utility lines）

The following SmarTest 7 example shows how the dynamic mask is enabled for utility block 1 and for block 2 to 5:

```
UTILITY_SEQ_MODE        utiSeqModeOn;
UTILITY_SEQ_MODE        utiSeqModeOff;

ON_FIRST_INVOCATION_BEGIN();

    //
    // Set utility block 1      in sequencer‑controlled masked reading and writing mode.
    // Set utility block 2 to 5 in sequencer‑controlled masked reading mode.
    //
    utiSeqModeOn.pogoBlock(1).mode(TM::SEQ_POGO_MASK_MODE_RW );
    utiSeqModeOn.pogoBlock(2,5).mode(TM::SEQ_POGO_MASK_MODE_RD );
    utiSeqModeOn.execute();

    //
    // Perform the functional test
    //
    FUNCTIONAL_TEST();

    //
    // Disable the sequencer‑controlled mode of all utility blocks
    //
    utiSeqModeOff.pogoBlock().mode(TM::SEQ_POGO_MODE_OFF);
    utiSeqModeOff.execute();

ON_FIRST_INVOCATION_END();
```

### Example 2: SmarTest 7 static mask（取自子主题 Sequencer-controlled utility lines › Mask mode of sequencer-controlled utility lines）

The following SmarTest 7 example shows how the static mask is set for utility block 1 and 2:

```
UTILITY_SEQ_MODE        utiSeqModeOn;
UTILITY_SEQ_MODE        utiSeqModeOff;
UTILITY_SEQ_STATIC_MASK utilitySeqStaticMask;

ON_FIRST_INVOCATION_BEGIN();

    //
    // Set utility block 1      in sequencer‑controlled masked reading and writing mode.
    // Set utility block 2 to 5 in sequencer‑controlled masked reading mode.
    //
    utiSeqModeOn.pogoBlock(1).mode(TM::SEQ_POGO_MASK_MODE_RW );
    utiSeqModeOn.pogoBlock(2,5).mode(TM::SEQ_POGO_MASK_MODE_RD );
    utiSeqModeOn.execute();

    //
    // Set the static mask for pogo blocks 1 and 2
    //
    utilitySeqStaticMask.pogoBlock(1).mask(0x000E);
    utilitySeqStaticMask.pogoBlock(2).mask(0x00E0);
    utilitySeqStaticMask.execute();

    //
    // Perform the functional test
    //
    FUNCTIONAL_TEST();

    //
    // Disable the sequencer‑controlled mode of all utility blocks
    //
    utiSeqModeOff.pogoBlock().mode(TM::SEQ_POGO_MODE_OFF);
    utiSeqModeOff.execute();

ON_FIRST_INVOCATION_END();
```

### Example circuit（取自子主题 Sequencer-controlled utility lines › Galvanic separation between utility line serial interface and digital pi）

The following example circuits use the inverting FODM8071 optocoupler together with the SN74LVC1T45 level shifter to connect the serial interface to four digital channels.Note Since this example circuits influence the behavior and timing of the control signals, we recommend the implementation only if galvanic separation is really necessary. If this cannot be clarified beforehand, appropriate jumpers for activating or bridging the circuits are reasonable. Some rules must be observed when using these circuits:

- The FODM8071 optocoupler inverts the digital control signals SCLK, FRAMn and SINP and also the output of the optional SOUT pin.
- You must therefore invert the digital states in your control patterns. Control patterns that are automatically generated by `SmartRDI`（raw: `../02.07_Test_Method_Reference/02.07.13_SmartRDI.md`） are not supported.
- The FODM8071 optocoupler requires a minimum of 5 mA input current to switch the output pin to the low level.
- The forward voltage of the FODM8071 optocoupler is maximum 1.8 V at 10 mA.
- In combination with the shown 820 Ω series resistor an input voltage of 6.5 V results in an input current of about 5.4 mA.
- For higher data rates, we recommend reducing the value of the series resistor. However, the maximum forward current of 16 mA of the optocoupler input must be observed.
- This arrangement adds some propagation delay to the signals of the serial interface that have to be included in the timing setup for the SOUT line. Note that variances between the propagation delays of the different lines might lead to a degradation of the maximum data rates.

!`Utility line serial interface ground isolation inputs`（raw: `../../../../raw/343163.png`）

!`Utility line serial interface ground isolation output`（raw: `../../../../raw/343164.png`）

### Example 1: Setup for SmarTest 7（取自子主题 Sequencer-controlled utility lines › Setting up sequencer control of utility lines）

The following example sets up three digital pins named D1, D2 and D3 to act as serial inputs to the utility line controller on the active wiring board, refer also to the graphic in `Sequencer-controlled utility lines`（raw: `../../03_Use_cases_and_application_papers/03.09_How_to_set_up_sequencer__ontrolled_utility_lines/03.09.01_Sequencer-controlled_utility_lines.md`）. The controller acts as the DUT in this case.

Pin D4 is a receive pin. It is also set up in the pin configuration but is not used in the rest of the example. The example programs utility lines 1, 3, and 15 on utility block 1 to turn on LEDs connected to these lines.Note This example uses 2-row pogo blocks.

Serial pins for sequencer control of utility lines
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/124758-1.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 3 列。
> 首行（上游原文）：Digital pin | Serial pin description | Direction

-  Make the following entry in the `GLOBAL section`（raw: `../02.04_Model_File_and_Licensing/02.04.01.03.02.01_GLOBAL_section.md`） of the SmarTest 7 model file:

utility_lines = 128, type = sequencer_controlled, pogo_size = 16

pogo_size specifies the number of utility lines per pogo block and utility_lines specifies the total number of utility lines (pogo_size multiplied by the number of utility blocks). Usual combinations are 64/16, 128/16 and 256/32.

Note If you were to use 4-row utility pogo blocks, the values for utility_lines and pogo_size would need to double. Combinations such as 128/32 or 256/16 are invalid. Note The default for the model file is 128 utility lines and 16 utility lines per pogo block. This applies if you omit the utility_lines entry.

Make the following entry in the `.technology file`（raw: `../../01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.01.02_Technology_file_for_a_device.md`）:

utility_lines_per_pogo_block: 16

Alternatively you could edit the Utility Block Size entry in the Change Device dialog window, in this case refer to `Editing technology data`（raw: `../../01_Getting_started/01.01_SmarTest_Work_Center/01.01.10.03.03_Editing_technology_data.md`）.

Refer also to `Configuration of 4-row or 2-row utility pogo blocks`（raw: `02.03.04.07.02_Configuration_of_4-row_or_2-row_utility_pogo_blocks.md`）.

Note If you were to use 4-row utility pogo blocks, the value for utility_lines_per_pogo_block would need to double.
- Set up the pins as shown:  !`Pin configuration for the serial interface`（raw: `../../../../raw/128789.png`）
- Use the following code to set up the levels.

```
EQNSET 1 "drive_receive"

SPECS

EQUATIONS

LEVELSET 1

    PINS SCLK FRAMn SINP
        vil = 0
        vih = 1.8

    PINS SOUT
        vol = 0.7
        voh = 1.1
```

- Use the following code to set up the timing.

```
EQNSET 1

    SPECS
        Frequency [MHz] # max 20 MHz

    TIMINGSET 1
        period = 1000/Frequency

    PINS SCLK FRAMn SINP
        d1 = 0

    PINS SOUT
        r1 = 1000/Frequency*0.5+100
```

- Use the following code to set up the wavetable

```
WAVETBL drive

    DCDT nop

    PINS SCLK FRAMn SINP
        0 "d1:0"
        1 "d1:1"
        2 "d1:Z"
        3 "d1:Z"
        4 "d1:Z"

    PINS SOUT
        2 "r1:L"
        3 "r1:H"
        4 "r1:X"
```

- Assign the clocking frequency for the serial control lines to your equation set and wavetable.Note The utility line controller on the wiring board is able to handle a maximum frequency of 10 MHz. The clock input to the controller is filtered and higher frequencies are ignored.  !`Assign the frequency of 10 MHz for the serial control lines`（raw: `../../../../raw/128790.png`）
- Enter the pattern shown below into the Pattern editor. It shifts 16 bits into the utility line shift register via SINP. Note that one bit is represented by two vectors in the pattern. Thus the waveform at SCLK (D1) requires a 0 and a 1 to generate a single cycle, see for example vectors 4 and 5.

The whole pattern is surrounded by high-Z vectors. The pattern section required to drive the 16 utility lines present on a single block starts with vector 4 and ends with vector 35. During this period the signal on FRAMn (D2) is driven to 0.

Bit 0 of SINP specifies utility line 1, bit 15 specifies utility line 16. Thus to turn on relays on lines 0, 12 and 14, the pattern on SINP (D3) must drive a 0 on vectors 34 & 35, 10 & 11 and 6 & 7. The rest of the vectors must remain at 1. Each relay coil must be connected between the UP5V line and the corresponding utility line as shown in example `Controlling user relay on a DUT board (V93000 systems)`（raw: `02.03.04.03.03_Utility_line_example_circuits.md#_98018__s_Controlling_user_relay_on_a_DUT_board`） of `Utility line example circuits`（raw: `02.03.04.03.03_Utility_line_example_circuits.md`）. For additional details refer to `Utility line interface circuitry`（raw: `02.03.04.03_Utility_line_interface_circuitry.md`）.

For the mapping of utility lines on utility blocks refer to the links in `step 2`（raw: `../../03_Use_cases_and_application_papers/03.09_How_to_set_up_sequencer__ontrolled_utility_lines/03.09.01.05_Setting_up_sequencer_control_of_utility_lines.md#_124758__cmd_Routing_of_digital_pins`） of the procedure above. SOUT (D4) is not used and is therefore set to high-Z for all vectors in the sequence.

  !`Control pattern for a single utility line block`（raw: `../../../../raw/124940.png`）  Note If you were to use 4-row utility pogo blocks, the pattern would need to be extended to shift 32 bits into the utility line shift register instead of 16. Note Entering a pattern manually can be a tedious and error-prone method, but is the simplest way if controlling just one or two utility blocks. If you need many utility lines you may consider other methods such as `d2s`（raw: `../02.07_Test_Method_Reference/02.07.09_d2s-framework.md`） or `Protocol Aware`（raw: `../02.07_Test_Method_Reference/02.07.11_Protocol_Aware_ATE.md`）.
- Add the test method code to the test method class as shown below.

```
UTILITY_SEQ_MODE utiSeqModeReset;
UTILITY_SEQ_MODE utiSeqModeOn;
UTILITY_SEQ_MODE utiSeqModeOff;

ON_FIRST_INVOCATION_BEGIN();

    //
    // Reset previous settings
    //
    utiSeqModeReset.pogoBlock().mode(TM::SEQ_POGO_MODE_OFF);
    utiSeqModeReset.execute();

    //
    // Enable utility block 1 for serial control
    //
    utiSeqModeOn.pogoBlock(1).mode(TM::SEQ_POGO_MODE_RW );
    utiSeqModeOn.execute();

    //
    // Perform the functional test
    //
    FUNCTIONAL_TEST();

    //
    // Disable the sequencer‑controlled mode of all utility blocks
    //
    utiSeqModeOff.pogoBlock().mode(TM::SEQ_POGO_MODE_OFF);
    utiSeqModeOff.execute();

ON_FIRST_INVOCATION_END();
```

### Example 2: Ganging utility blocks in SmarTest 7（取自子主题 Sequencer-controlled utility lines › Setting up sequencer control of utility lines）

If you were to gang two 2-row utility line blocks together you would need to set up a pattern of twice the length as you would have to shift in 32 bits instead of just 16. Then, to enable for example utility line blocks 1 and 2 for serial control, you would need to implement the following API call into your test methods:

```
UTILITY_SEQ_MODE utiSeqModeOn;

utiSeqModeOn.pogoBlock(1,2).mode(TM::SEQ_POGO_MODE_RW );
utiSeqModeOn.execute();
```

Note If you were to gang two 4-row utility pogo blocks, the above API calls would shift 64 bits into the utility line shift register instead of 32.

### Example（取自子主题 Utility line compatibility  configuration  and capability › Designing compatible utility lines）

Refer to `Utility line example circuits`（raw: `02.03.04.03.03_Utility_line_example_circuits.md`）.

<!-- 语法节 end -->

## 是什么

**utility line 是 V93000 基础设施伸到 DUT 板上的一批通用开关/读回线**，
用来**控制或读回 DUT 板上的外部器件**：

> 「Using utility lines allows you to control or read the states of external devices such as relays, EEPROMS and indicators on your DUT board. Utility lines can be controlled statically (workstation鈥慶ontrolled) or dynamically (sequencer鈥慶ontrolled).」

（`鈥慶ontrolled` 是坏字，读作 `-controlled`，见 `## 出处` ⚠️①。）

**注意这一页的定位。** 本篇归在 `02_System_reference/02.03_DUT_board_design_reference/`，
**它是写给「画 DUT 板的人」看的**——所以本页只写**和测试工程师相关**的那几件事：
**这批线凭什么不问 connect/disconnect、谁在控制它、板子那边要给什么条件**。
**本页不是「utility line 的操作步骤」**——操作在 [[sequencer-controlled-utility-lines]] 与那边挂着的用例篇里。

### 三件事：谁提供、从哪访问、拿什么编程

| 问题 | 原文 |
|---|---|
| **谁提供** | 见下 |
| **从哪访问** | 见下 |
| **拿什么编程** | 见下 |

> 「Utility lines are provided by
>
> - the internal wiring board of V93000 Pin Scale and Smart Scale systems, or by
> - the internal utility resources or the optional Utility Card of V93000 EXA Scale systems.」

> 「Depending on the system configuration, the utility lines can be accessed via the utility pogo blocks UTIL 1 鈥?nbsp;UTIL 8 of the DUT interface. On V93000 EXA Scale systems that are equipped with a second Utility Card, utility lines are also available on the pogo blocks DPS 1 鈥?nbsp;DPS 8.」

> 「Utility lines can be programmed by
>
> - dedicated utility instrument properties or test methods of SmarTest 8 or by
> - dedicated firmware commands, routing sets or test methods of SmarTest 7.」

**这三条合起来说明一件事：utility line 的落点与编程手段都不是固定的**——
它随 **Pin Scale / Smart Scale / EXA Scale** 三档系统、**有没有第二张 Utility Card** 而变。
**EXA Scale 上多出来的是 `DPS 1 鈥?nbsp;DPS 8` 这两组 pogo 块**
（那两组号的来龙去脉见 `DUT interface layout`，raw: `02.03.03.01_DUT_interface_layout.md`）。

### 最重要的一条：utility line 不随 connect / disconnect 变

> 「Utility lines are not affected by standard connect/disconnect sequences.」

**这是本页对测试工程师最值钱的一句。** 它说的是：
**utility line 的开关状态不由标准的 `CONNECT()` / `DISCONNECT()` 序列决定**——
所以「测试程序里有没有 connect」和「DUT 板上那个继电器现在是什么状态」**是两件事**。
**原文只写了这一句**，**没有说那它由什么决定**（静态由主机写寄存器、动态由 pattern sequencer，见下），
**也没有说 disconnect 之后线会不会回到某个默认状态——本页答不了。**

### 静态控制与动态控制

原文在 `## Sequencer鈥慶ontrolled utility lines` 一节里给了动态那条路的机制，
**按机台分两种**：

> 「On V93000 EXA Scale systems equipped with the optional Utility Card, the pattern sequencer controls utility lines via an internal data path.」

> 「On Pin Scale and Smart Scale systems equipped with an active wiring board, utility lines are generated by a controller on this board and can be controlled dynamically by the pattern sequencer.」

| 机台 | 动态控制的路径（原文） |
|---|---|
| V93000 EXA Scale ＋ 可选 Utility Card | `the pattern sequencer controls utility lines via an internal data path` |
| Pin Scale / Smart Scale ＋ active wiring board | `utility lines are generated by a controller on this board`，由 pattern sequencer 动态控制 |

**这句话里有一个前提容易被漏读**：Pin Scale / Smart Scale 那条**要求板上是 `active wiring board`**——
**`active` 是这块板的名字的一部分，不是形容词**（两张板的电路差别见下）。

原文把动态控制那一半的完整说明推给了另一篇：

> 「For more information, refer to Sequencer-controlled utility lines.」

### 板子那边必须给什么条件：两个电气点

**这一节是本页离「画板子的人」最近的地方**，也是本页对测试工程师的第二处相关点——
**板子做错了，表现会落在 level 精度和测量噪声上**。

> 「The GND connection and the noise level of utility lines need your attention:」

> 「The ground pins of the utility pogo blocks (UGND) can be connected to digital ground planes (DGND) of the DUT board, however you may need to insert galvanic separation circuitry on the DUT board between the two ground domains. This is to prevent a negative impact on level accuracy and the introduction of noise into your measurements, due to ground loops. An example of such circuitry is provided in Galvanic separation between utility line serial interface and digital pins.」

**逐句拆开看**：

| 原文的话 | 含义 |
|---|---|
| `can be connected` | `UGND` 接 `DGND` **是允许的**，不是禁止 |
| `however you may need to insert galvanic separation circuitry` | **可能要**加隔离电路——**原文用的是 `may`，不是 `must`** |
| `to prevent a negative impact on level accuracy and the introduction of noise` | **代价落在 level 精度与测量噪声上** |

**⚠️ 原文没有给「什么时候该加、什么时候不用加」的判据**——`may need` 后面没有条件从句。
**所以「我这块板要不要加隔离」本页答不了**，只能看那个 example 电路。

第二点是**上拉**。下面这段出自本页语法节里取自子主题 `Utility line characteristics` 的段落
（**原文逐字，`鈥?nbsp;` 是坏字**）：

> 「Utility lines URW00 鈥?nbsp;URW15 feature an additional pull-up resistor to +5 V on some utility pogo blocks. For devices with higher input impedance, we therefore strongly recommend adding an external pull-up resistor in the region of several hundred Ohms, depending on the type of device used.」

**两条限制都在字面上**：**只有 `URW00` 到 `URW15` 这 16 根**有额外上拉，而且**只在 `some utility pogo blocks` 上**；
**推荐值原文写的是 `in the region of several hundred Ohms`，而且带 `depending on the type of device used`**。

### 两条板的电路差别（**只能从图里读到**）

本页语法节里那两段取自子主题 `Utility line characteristics` 的图和文字，只说「这是 active / passive 接线板的典型电路」，
**一个数值都没给**。**下面这些数值是把图打开读出来的**：

| | active wiring board | passive wiring board |
|---|---|---|
| 图 | `../../../../raw/136929.png` | `../../../../raw/74690.png` |
| 内部上拉 | **`+3.3V`，`12.1kΩ`** | **`+5V`，`10kΩ / 271kΩ`** |
| 读回通路 | 一只三极管 ＋ 二极管，`Utility Write` 从基极进 | 一只三极管，`Utility Read` 经 **`10kΩ`** 串阻 |
| 其他 | 板上 `5.6V` 稳压二极管、`100nF`；`12.1kΩ` 出现在读回侧 | 另一只 `+5V` 二极管 |

**④ 图证**：`+3.3V`、`12.1kΩ`、`-3.3V`、`5.6V`、`100nF`、`10kΩ`、`+5V`、`10kΩ / 271kΩ`、`To DUT Board`、`Utility Write`、`Utility Read`
这些字**在 raw 里 grep 不到**（已核：对该篇 raw 搜 `12.1k` / `271k` 均无匹配）。
**两张图都没有版本标注**，所以这些数值**只能当「这张图上的数值」**，不能当 7.10.3 的当前设计值（§11.4）。

**⚠️ 图与正文有一个对不上的数**（这是本页从图里读出来的第一条硬结论）：
active board 那张图的右上角有一个虚线框，框里写的是

| 图上的字（`136929.png`） |  |
|---|---|
| `Recommended value: 1kΩ - 3.3kΩ` | 旁边虚线框注 `On DUT Board if drive levels above +3.3 V are required`，接 `+5V` |

**而正文同一段里写的推荐值是** `in the region of several hundred Ohms`。
**一个是「几百欧」，一个是「1 kΩ – 3.3 kΩ」——两个数差一个量级。**
**原文没有说这两处指的是不是同一个电阻**（正文那句的条件是 `For devices with higher input impedance`，
图那句的条件是 `if drive levels above +3.3 V are required`），**所以本页不判谁对**，只把两处照实并列。

## 典型用法

**成色先说清**：本篇（父主题）**没有 `## Procedure`，也没有 `## Before you begin`**，
正文只有「谁提供 / 怎么访问 / 怎么编程 / 不受 connect 影响 / 动态控制 / GND 与噪声」六小段。
**所以下面第 1、2 条是从父主题读出来的，第 3 条起是从语法节那几段子主题里读出来的，来源逐条标明。**

**1. 先确认你这台机器上 utility line 从哪来、落在哪。**
EXA Scale 看**有没有第二张 Utility Card**（有则 `DPS 1 鈥?nbsp;DPS 8` 上也有），
Pin Scale / Smart Scale 看**接线板是 active 还是 passive**。

**2. 判断你需要静态还是动态。**
要「与 pattern 同步」就必须走动态（sequencer-controlled）；**父主题对这一条只给了一句
`For more information, refer to Sequencer-controlled utility lines.`**。
**纯静态的线与 pattern 无关**——但**别把它和 connect/disconnect 混起来**（它不受那两者影响）。

**3. 走动态控制时，板子上必须先把串口引脚接到数字引脚。**
语法节里取自子主题 `Setting up sequencer control of utility lines` 的那段说：
三个数字引脚 `D1, D2, D3` 作为 utility line control 的串行输入，`D4` 是接收引脚。
**引脚配置长什么样，本页语法节的图只说「Set up the pins as shown」**——
**把那张图打开，能读到的比正文多**：

**④ 图证（`../../../../raw/128789.png`，alt 写作 `Pin configuration for the serial interface`）**

| 图里的列 | 图里的值 |
|---|---|
| `Name` | `SCLK` / `FRAMn` / `SINP` / `SOUT` |
| `Type` | 前三行 `i`，`SOUT` 行 `o` |
| `Mode` | 四行都是 `std` |
| `HW` | 四行都是 **`PS400`** |
| `Comment` | `serial clock` / `serial frame` / `serial data in` / `serial data out` |
| `Tester Channel`（`Site 1`） | **`11701` / `11702` / `11703` / `11704`** |

**这张表里的 `PS400` 与 `11701`–`11704` 在 raw 里 grep 不到**（已核：对该篇 raw 搜 `PS400` 与 `11701` 均无匹配）。
**它填的是正文一个字的空**：正文只有一句「Set up the pins as shown」，**没给卡型、没给通道号**；
图把「四个引脚落在同一张 `PS400` 的连续四个通道上、且只有 `SOUT` 是输出」这件事摆出来了。
**⚠️ 按 §11.4 那条坑**：这张截图**没有版本标注**，列名 `Type` / `Mode` / `HW` / `Comment` / `Tester Channel`
是不是 7.10.3 的当前列名，**本页没核**——**本篇的 `## Functional changes` 里没有任何一条改名记录**，
但这只说明「本篇没记」，不说明「没改过」。

**4. 频率必须落在 10 MHz 以内，而且要同时写进 equation set 与 wavetable。**
语法节那段说：`The utility line controller on the wiring board is able to handle a maximum frequency of 10 MHz. The clock input to the controller is filtered and higher frequencies are ignored.`
**「滤掉、忽略」不是「报错」**——超了不会有提示。

**④ 图证（`../../../../raw/128790.png`，alt 写作 `Assign the frequency of 10 MHz for the serial control lines`）**：
这张图是 **`SpecTool`** 的窗口（见 [[spec-tool]]），里面能看到
`Timing` → `Specification 1` `1` 填的是 `10MHz`，`Wavetable` 选的是 `drive`，`Equation` 是 `1`，
下面那张表的列头是 `Name` / `Actual` / `Minimum` / `Maximum` / `Measured` / `Unit` / `Comment`，
表里一行是 `Frequency` / `10` / `MHz`。
**`SpecTool`、`Timing` `Specification`、`drive`、`Frequency` 这些字 raw 里 grep 不到**（已核：搜 `SpecTool` 无匹配）。
**图填的空是「频率写在哪」**：正文只说
「Assign the clocking frequency for the serial control lines to your equation set and wavetable.」，
**图指出它在 SpecTool 的 Timing Specification 里，且 Wavetable 框选的是 `drive`**（与语法节那段 wavetable 代码的 `WAVETBL drive` 同名）。

**5. 用 pattern 手动移位时，一个 bit 占两个 vector。**
语法节那段说：`Note that one bit is represented by two vectors in the pattern. Thus the waveform at SCLK (D1) requires a 0 and a 1 to generate a single cycle`，
并给了起止：`The pattern section required to drive the 16 utility lines present on a single block starts with vector 4 and ends with vector 35.`

**④ 图证（`../../../../raw/124940.png`，alt 写作 `Control pattern for a single utility line block`）**：
图上是一张 pattern 编辑器的表，`Size: 48 bytes`，四列分别写作
`FRAMn (DVC)` / `SCLK (DVC)` / `SINP (DVC)` / `SOUT (DVC)`；
`Comment` 列在 vector `4` 标 `bit 15`、`12` 标 `bit 11`、`20` 标 `bit 7`、`28` 标 `bit 3`，末尾 `43` 行写 `STOP`。
**`(DVC)`、`Size: 48 bytes`、`STOP`、`bit 15` 这些字 raw 里 grep 不到**（已核：搜 `DVC` 无匹配）。
**图核上了正文那句「one bit is represented by two vectors」**：相邻两个 bit 注释之间隔 8 个 vector，
8 vector ÷ 4 bit = **2 vector/bit**。
**⚠️ 图不解决的问题**：`(DVC)` 是什么缩写、`bit 2` / `bit 1` / `bit 0` 那几行的注释位置、以及
`4` 这个数据值是不是就等于高阻，**图上没有说明**——**本页不替它猜**（正文的 wavetable 代码里有 `4 "d1:Z"`，
但那是另一段内容，**本页不据此下结论**）。

**6. 需要地隔离时，电路长什么样只能看图。**
语法节那段给了规则（`The FODM8071 optocoupler inverts the digital control signals SCLK, FRAMn and SINP`、
`In combination with the shown 820 惟 series resistor an input voltage of 6.5 V results in an input current of about 5.4 mA.`），
但**输入侧与输出侧是两张图**：

**④ 图证（`../../../../raw/343163.png` 输入侧、`../../../../raw/343164.png` 输出侧）**

| | 输入侧（`343163.png`） | 输出侧（`343164.png`） |
|---|---|---|
| 信号名 | `UL_SCLK` / `UL_FRAM` / `UL_SINP` | `UL_SOUT_buffered` → `UL_SOUT` |
| 串阻 | **`R1` / `R3` / `R8` 都是 `820`** | **`R2` 是 `120`** |
| 光耦 | `U1` / `U8` = `FODM8071`，`VDD` 接 **`UTILITY_5V`**，`C` 接 `UGND` | `U4` = `FODM8071`，`VDD` 接 **`3V3`**，`C` 接 `UGND`，`GND` 接 `DGND` |
| 电平转换 | `U2` / `U5` / `U9` = `74LVC1T45`，一侧 `UTILITY_5V`、另一侧 `1V8` | **没有**——输出侧直接由光耦出到 `UL_SOUT` |

**`820` 与语法节那段文字对得上**（那段逐字写 `the shown 820 惟 series resistor`）；
**而 `120`、`1V8`、`3V3`、`UTILITY_5V`、`UL_SCLK`、`FODM` 这些字在本篇 raw 里 grep 不到**
（已核：对 `02.03.04_Utility_lines.md` 搜这几个串，**均无匹配**）。
**图填的空是两处正文没写的**：① **输出侧串阻是 `120` 而不是 `820`**——正文只提了 `820`，
**读者很容易以为两侧同值**；② **输出侧光耦的 `VDD` 是 `3V3`，而输入侧是 `UTILITY_5V`**。

**7. 本页答不上来的（语料未写 / 本页未读）：**

- **静/动态之间有没有依赖**——父主题一句没提；语法节里有一段的段名是
  `Setting up sequencer control of utility lines`，但**它底下那个 `SmarTest 7 dependencies between static and dynamic access` 子主题本页没读**。
- **`UGND` 与 `DGND` 什么时候该隔离、什么时候不用**——原文只有 `may need`。
- **utility line 的电气定额**（驱动能力、耐压、速率上限）——父主题一个字没有，
  **`Utility line characteristics` 的正文本页没读**（只在语法节里见到三段摘录 ＋ 一张表名）。
- **`Utility lines and DUT board EEPROMs` 讲什么**——本页一个字没有。
- **utility line 在 SmarTest 里到底用什么 API / 固件命令开**——父主题写的是
  `dedicated utility instrument properties or test methods of SmarTest 8` 与
  `dedicated firmware commands, routing sets or test methods of SmarTest 7`，
  **一个命令名都没给**；那是 `Utility line control software` 子主题的事，**本页没读**。

## 和谁有关

- [[utility-line-assignments]] — **本篇的子主题之一，也是最近的一页**：**线数、块型（16/32 线、2 排/4 排）、
  上拉电阻配置**在那一页；本页只讲「这批线是什么、谁在管、板子要给什么条件」
- [[sequencer-controlled-utility-lines]] — **本篇点名的下游**：父主题在 `## Sequencer鈥慶ontrolled utility lines`
  一节末尾写 `For more information, refer to Sequencer-controlled utility lines.`；
  **动态控制那一半的完整说明在那儿，不在本页**
- `DUT interface layout`（raw: `02.03.03.01_DUT_interface_layout.md`）— **落点**：
  本页说 utility line 经 `UTIL 1 鈥?nbsp;UTIL 8`（EXA 还有 `DPS 1 鈥?nbsp;DPS 8`）访问；
  **⚠️ 这个名字不在 `extract/prose-allowlist.txt` 里**（本页 frontmatter 的 `related` 里留着它，
  因为那一页确实存在、slug 就是 `dut-interface-layout`），**所以正文里不写成 wikilink**（§9.1）；
  **这些号本身属于那一页**
- [[utility-card]] — **原文点名的硬件前提**：EXA Scale 上 utility line 的来源之一就是 `the optional Utility Card`；
  **而且第二张卡还会把 utility line 带到 `DPS 1 鈥?nbsp;DPS 8` 上**
- [[utility-pogo-block-utility-card-v93000-exa-scale-systems]] — **同族、讲同一批块**：
  utility line 落在 utility pogo block 上，**那些块的 pogo 针分配在那一页**（本页原文没点名这篇）
- [[dut-board-grounding]] — **同族、接在本页的 GND 那节上**：`UGND` / `DGND` 之间要不要隔离，
  是 DUT board 接地设计的一部分；**本页只给了「可能要加」和「加错了会怎样」**
- [[spec-tool]] — **只由图证建立的关系**：`128790.png` 那张图上的窗口是 `SpecTool`，
  **父主题正文里没有 `SpecTool` 这个词**——这条关系来自图，不是来自文字（图里的字 grep 不到）
- [[pin]]（**本页的 `stage`**）— 依据是「串行接口必须接到数字引脚」这一条：
  语法节那段写三个数字引脚 `D1, D2, D3` 作为串行输入、`D4` 作为接收引脚，
  而 `128789.png` 给出的正是**数字引脚的 pin configuration 表**（`PS400`，通道 `11701`–`11704`）。
  **⚠️ 父主题正文没有讲引脚配置**，这一条关系是从语法节的两段子主题内容推出来的
- `Utility line control software`、`Utility line interface circuitry`、`Utility lines and DUT board EEPROMs`、
  `Utility line compatibility, configuration, and capability`、`Utility line characteristics`
  — **本篇自己列的七个子主题里的五个，本页一篇都没读**（剩下两个已各有一页，见上）
- `Internal utility power supply (V93000 systems)`（raw: `02.03.05.05_Internal_utility_power_supply__V93000_systems.md`）
  — 语法节那两段电路图里 `+5V` 的来源，**原文点名、本页没读**
- `Reducing noise on utility lines`（raw: `02.03.04.03.02_Reducing_noise_on_utility_lines.md`）
  — 父主题在 GND 那节的第一条里点的名，**本页没读**
- `Galvanic separation between utility line serial interface and digital pins`
  （raw: `02.03.04.05.05_Galvanic_separation_between_utility_line_serial_interface_and_digital_pi.md`）
  — 同上，是 `343163.png` / `343164.png` 那两张图的出处篇，**本页没读**
- **`UTIL 1` 到 `UTIL 8` / `DPS 1` 到 `DPS 8` / `URW00` 到 `URW15` / `UGND` / `DGND` 不是 wiki 页面**，
  只是本页出现的编号与针名——**它们不该链、也没有页**

## 版本

原文**有** `## Functional changes`，四条（逐字）：

- `Introduced before SmarTest 6.3.2`
- `SmarTest 7.1.0: Sequencer鈥慶ontrolled utility lines introduced`
- `SmarTest 7.2.0: 256 sequencer鈥慶ontrolled utility lines introduced on ATH/CTH/STH DUT Scale and on LTH`
- `SmarTest 7.2.0: External utility power introduced on ATH/CTH/STH DUT Scale and on LTH`

读法上三件事：

| 要点 | 说明 |
|---|---|
| **第一条是哨兵，不是「6.3.2 的变更」** | `Introduced before SmarTest 6.3.2` 按 §11.2 ② 读＝**「在本文档集覆盖范围开始之前就已经有了」** |
| **动态控制是 7.1.0 才有的** | `SmarTest 7.1.0: Sequencer鈥慶ontrolled utility lines introduced`——**所以本页讲的静态/动态两条路，动态那条是后加的** |
| **两条 7.2.0 都限定在 `ATH/CTH/STH DUT Scale` 与 `LTH`** | `SmarTest 7.2.0: 256 sequencer鈥慶ontrolled utility lines introduced on ATH/CTH/STH DUT Scale and on LTH`——**原文把适用范围写进了这一条里**，不是全机台 |

**本页答不上来的版本问题**：**`7.1.0` 之前怎么动态控制（有没有别的路）本篇没说**；
**`7.2.0` 之前这些机台上是多少根线，本篇也没说**。
**`256` 这个数只有在这里出现一次**——它和 [[utility-line-assignments]] 里那套「4 排块 ＋ 256 线」的关系，**本篇没有连起来**。

## 出处

`sources:` 一篇：
`02_System_reference/02.03_DUT_board_design_reference/02.03.04_Utility_lines.md`
（TDC `20406.htm`，**58 行**，**整篇读完**）

**本页没做的（按缺口大小排）：**

- **七个子主题，正文一篇都没读**：`Utility line assignments`、`Utility line characteristics`、
  `Utility line interface circuitry`、`Utility line control software`、`Sequencer-controlled utility lines`、
  `Utility lines and DUT board EEPROMs`、`Utility line compatibility, configuration, and capability`。
  **这是本页最大的缺口**：父主题 58 行里，凡是「怎么用」的细节都在那七篇里。
- **但语法节里那 7 张图，本页 7 张全读了**（`136929` / `74690` / `343163` / `343164` / `128789` / `128790` / `124940`）。
  **⚠️ 要分清楚**：这些图**不在本篇正文里**，它们在脚本从子主题抽来的段内
  （段名写着「取自子主题 `Utility line characteristics`」等）。**本页读的是图，读的是「图上有什么」；
  那些子主题的正文，本页一篇都没读。** 所以本页对这些图**只做图像层面的陈述，不替子主题的正文作任何转述。**
- **没有打开任何 `.htm`**，也没有核过图上数值与上游 HTML 是否一致（§11.2 ⑥ 那条判据要求回 `.htm`；
  **本页没做这一步**）。
- **本篇正文里没有图**——上面那 7 张全部来自子主题。**所以本页没有一处「父子篇正文的图证」。**
- **没有 `## Procedure` / `## Before you begin`**——正文只有六小节 ＋ `Related information` ＋ `Functional changes`。
  **所以 `## 典型用法` 的前两条是照父主题那几段拼的，第 3 条起是照语法节的子主题摘录 ＋ 图拼的。**
- **没有在任何真实机台上开过 utility line**（`verified: doc-only`）。
  **`10 MHz` 是不是真的上限、`PS400` 上是不是真有那四个通道、`1kΩ - 3.3kΩ` 与「几百欧」哪个是现行设计，
  本页只能保证「文档/图这么写」（§11）。**
- **两张接线板图上的数值（`12.1kΩ` / `10kΩ / 271kΩ` / `120` / `3V3` / `1V8`）都是「这张图上的」**，
  **不是本页认定的设计值**——图没有版本标注，而本篇的 `## Functional changes` 里**没有一条讲电气设计变更**。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> **① `鈥` 族坏字 7 处 / 5 行**（第 18、25、34、56、57 行）。按 §11.2 ① 这一类**只许报区间（U+2000–U+203F）**。
> 本篇两种形态：
>
> | 形态 | 逐字例 | 行 | 读作 |
> |---|---|---|---|
> | `鈥?nbsp;`（第三字节被换成 `?`，**并吃掉了 `&nbsp;` 的 `&`**） | `the utility pogo blocks UTIL 1 鈥?nbsp;UTIL 8 of the DUT interface` | 25 | `–` ＋ 一个不换行空格 |
> | `鈥慶`（**吃掉后面那个字母 `c`**） | `controlled statically (workstation鈥慶ontrolled) or dynamically (sequencer鈥慶ontrolled)` | 18 | `-c` |
>
> **⚠️ 两种形态的处置不同**：`鈥慶` 按 `extract/encoding-map.csv` 是**确定映射**（`鈥慶` = `‑c`），
> **所以 `workstation鈥慶ontrolled` 读作 *workstation-controlled***；
> 而 `鈥?nbsp;` 那个**只许报区间**，**不能反解成某个具体的字**。
> **两种都照原样留在引文里。** 同一形态在标题里也出现：`## Sequencer鈥慶ontrolled utility lines`（第 34 行）。
>
> **② `鈥` 之外的坏字：`惟`（＝`Ω`）。** 语法节那段里逐字是
> `In combination with the shown 820 惟 series resistor an input voltage of 6.5 V results in an input current of about 5.4 mA.`
> ——**`惟` 是两字节族、能唯一还原**（`extract/encoding-map.csv`），**读作 `Ω`**，即 `820 Ω`；图上写的也是 `820`。
> **本页照原样引，不在引文里替它改字。**
>
> **③ `## Related information` 那一段四条链接之间一个分隔符都没有。** 第 51 行逐字是把
> `Sequencer-controlled utility lines` / `Utility line capabilities in relation to the system hardware` /
> `Reducing noise on utility lines` / `Galvanic separation between utility line serial interface and digital pins`
> **四条链接首尾直接相连**（后一条的 `[` 紧跟前一条的 `)`）。
> **原文如此，本页不替它补空格。**
> （`layout-information-dut-board` 那页记的 `Files of the package:` 粘连、`dut-interface-layout` 那页记的第 319 行粘连，是同一形态的第三、第四例。）
>
> **④ 链接文字与目录名不一致：** 第 40 行的链接文字是 `Sequencer-controlled utility lines`，
> 而它指向的路径是 `03.09_How_to_set_up_sequencer__ontrolled_utility_lines/03.09.01_Sequencer-controlled_utility_lines.md`
> ——**目录名里写的是 `sequencer__ontrolled`（两个下划线、少一个 `c`）**。
> **原文如此。** 同一条粘连在第 40 行和第 51 行各出现一次。
>
> **⑤ 正文与图对不上的一处数（不是坏字，是内容不一致）**：
> 语法节那段写 `an external pull-up resistor in the region of several hundred Ohms`，
> 而同一段的图 `136929.png` 右上角虚线框里给的推荐值是一个 **1 kΩ 到 3.3 kΩ** 的区间。
> **两个量级。原文没有说这两处是不是同一个电阻，本页照实并列、不判对错。**
> **图上那两处原文逐字，本页放在 `## 是什么` 那张「图上的字（`136929.png`）」表里
> ——图里的字不进引文块（§11.4）。**
>
> **⑥ §11.2 ⑤ 那族「整词替换」（`DC/DC power units`）在本篇没有出现。**
> 记这一条是为了**把「查过」和「没查」分开**（§13.1 ⑥′）：本页确实去找了，**只找到 ① ② 两族**。

`verified: doc-only`
