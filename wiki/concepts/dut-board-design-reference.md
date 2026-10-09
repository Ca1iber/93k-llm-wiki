---
type: concept
title: DUT board design reference
layer: n/a
stage: project
tags: [concept, dut-board, hardware-design, design-guide, v93000, interface]
related: [direct-probe-stiffener, layout-information-dut-board, dut-board-grounding, pogo-pad-and-via-design, pogo-block-compatibility, inter-layer-via-design]
sources:
  - 02_System_reference/02.03_DUT_board_design_reference/02.03_DUT_board_design_reference.md
created: 2026-09-18
updated: 2026-09-20
verified: doc-only
---

# DUT board design reference

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **14,689 字符逐字取自** `<02_System_reference/02.03_DUT_board_design_reference/02.03_DUT_board_design_reference.md>` 及其子主题 `<02_System_reference/02.03_DUT_board_design_reference/02.03.04.02_Utility_line_characteristics.md>`、`<02_System_reference/02.03_DUT_board_design_reference/02.03.04.05.04_Mask_mode_of_sequencer-controlled_utility_lines.md>`、`<02_System_reference/02.03_DUT_board_design_reference/02.03.04.05.05_Galvanic_separation_between_utility_line_serial_interface_and_digital_pi.md>`、`<02_System_reference/02.03_DUT_board_design_reference/02.03.04.05.06_Setting_up_sequencer_control_of_utility_lines.md>`、`<02_System_reference/02.03_DUT_board_design_reference/02.03.04.07.01_Designing_compatible_utility_lines.md>`、`<02_System_reference/02.03_DUT_board_design_reference/02.03.06.03.07_PSSL_pogo_cable_assembly__pogo_pin_layout_and_model_file_configuration.md>`、`<02_System_reference/02.03_DUT_board_design_reference/02.03.07.01.04_DPS_layout_rules_for_high_frequency_designs.md>`、`<02_System_reference/02.03_DUT_board_design_reference/02.03.07.08.02_Leakage_and_crosstalk_of_RF_signals.md>`、`<02_System_reference/02.03_DUT_board_design_reference/02.03.11.01.02_Direct-Probe_PSRF_probe_card_specifications.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example 1: Utility line circuitry (Active wiring board of V93000 systems)（取自子主题 Utility lines › Utility line characteristics）

The diagram shows the typical utility line interface circuitry on a system fitted with the active wiring board.Note Utility lines URW00 …nbsp;URW15 feature an additional pull-up resistor to +5 V on some utility pogo blocks. For devices with higher input impedance, we therefore strongly recommend adding an external pull-up resistor in the region of several hundred Ohms, depending on the type of device used. For more information, refer to table `Internal pull‑up resistor of utility lines`（raw: `02.03.04.02_Utility_line_characteristics.md#_21418__s_Pull-up_resistor_of_utility_lines_V93000_systems`） above.!`Utility read/write line - active wiring board`（raw: `../../../../raw/136929.png`）

"+5V" is the `Internal utility power supply (V93000 systems)`（raw: `02.03.05.05_Internal_utility_power_supply__V93000_systems.md`） that is available at pogo pins "UP5V" of all utility pogo blocks.

### Example 2: Utility line circuitry (Passive wiring board of V93000 systems)（取自子主题 Utility lines › Utility line characteristics）

The diagram shows the utility line interface circuitry on a system fitted with the passive wiring board.

 !`Utility read/write line - passive wiring board`（raw: `../../../../raw/74690.png`）

"+5V" is the `Internal utility power supply (V93000 systems)`（raw: `02.03.05.05_Internal_utility_power_supply__V93000_systems.md`） that is available at pogo pins "UP5V" of all utility pogo blocks.

### Example 1: SmarTest 7 dynamic mask（取自子主题 Utility lines › Sequencer-controlled utility lines › Mask mode of sequencer-controlled utility lines）

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

### Example 2: SmarTest 7 static mask（取自子主题 Utility lines › Sequencer-controlled utility lines › Mask mode of sequencer-controlled utility lines）

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

### Example circuit（取自子主题 Utility lines › Sequencer-controlled utility lines › Galvanic separation between utility line serial interface and digital pi）

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

### Example 1: Setup for SmarTest 7（取自子主题 Utility lines › Sequencer-controlled utility lines › Setting up sequencer control of utility lines）

The following example sets up three digital pins named D1, D2 and D3 to act as serial inputs to the utility line controller on the active wiring board, refer also to the graphic in `Sequencer-controlled utility lines`（raw: `../../03_Use_cases_and_application_papers/03.09_How_to_set_up_sequencer__ontrolled_utility_lines/03.09.01_Sequencer-controlled_utility_lines.md`）. The controller acts as the DUT in this case.

Pin D4 is a receive pin. It is also set up in the pin configuration but is not used in the rest of the example. The example programs utility lines 1, 3, and 15 on utility block 1 to turn on LEDs connected to these lines.Note This example uses 2-row pogo blocks.

Serial pins for sequencer control of utility lines
| Digital pin | Serial pin description | Direction |
|---|---|---|
| SCLK | Serial clock | Input |
| FRAMn | Serial frame enable | Input |
| SINP | Serial data in | Input |
| SOUT | Serial data out | Output |

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

### Example 2: Ganging utility blocks in SmarTest 7（取自子主题 Utility lines › Sequencer-controlled utility lines › Setting up sequencer control of utility lines）

If you were to gang two 2-row utility line blocks together you would need to set up a pattern of twice the length as you would have to shift in 32 bits instead of just 16. Then, to enable for example utility line blocks 1 and 2 for serial control, you would need to implement the following API call into your test methods:

```
UTILITY_SEQ_MODE utiSeqModeOn;

utiSeqModeOn.pogoBlock(1,2).mode(TM::SEQ_POGO_MODE_RW );
utiSeqModeOn.execute();
```

Note If you were to gang two 4-row utility pogo blocks, the above API calls would shift 64 bits into the utility line shift register instead of 32.

### Example（取自子主题 Utility lines › Utility line compatibility  configuration  and capability › Designing compatible utility lines）

Refer to `Utility line example circuits`（raw: `02.03.04.03.03_Utility_line_example_circuits.md`）.

### Example（取自子主题 Pogo pin assignment › Pogo pin assignment - Digital cards › PSSL pogo cable assembly  pogo pin layout and model file configuration）

### PSSL card configuration in the model file

For the syntax of standard density (SD) pogo block entries in a model file, refer to the SD section in `PS1600 card configuration in the model file`（raw: `../02.05_Test_Head_Cards/02.05.04.01.07.02_PS1600_card_configuration_in_the_model_file.md`）.

```
CARD_CONFIGURATION
# PSSL card has standard-density pogos per filling rules in S2 locations
  slot = 105, HW = PSSL,     pogoblocks = 317 321
  slot = 106, HW = PSSL15G,  pogoblocks = 301 305
```

### Example 1: Optimum DPS routing at the DPS block（取自子主题 Electrical design  General rules › DC DUT board design › DPS layout rules for high frequency designs）

A horizontal layout structure near a DPS block, as shown in the example graphic below, must be an integral part of a carefully designed Optimum Board Layer Structure stack-up.

For example, you may route every other (that is, every second) DPS signal in Layer 8, followed by a ground layer with similarly shaped and slightly overlapping polygons in Layer 9.

DPS signals left out in the first DPS signal layer are routed in the next signal layer, Layer 10, with differently shaped polygons; followed by appropriate and overlapping ground polygons in Layer 11, and so on.

This way, the return path concept is rigorously followed.

 !`DPS layout example`（raw: `../../../../raw/128772.png`）

### Example 2: Sparing a ground layer in the stack-up（取自子主题 Electrical design  General rules › DC DUT board design › DPS layout rules for high frequency designs）

A widely used method to save a ground layer in the stack-up is the design of a ground island polygon as shown in the graphic below.

In that graphic, ground layer G12 follows a similar shape as the "combined" lines of Force, Sense, and Ground Sense in both adjacent signal layers (S1 and S2). The same applies for ground layer G34 and its signal layers S3/S4, or G56 and S5/S6, respectively.

This design saves every other ground layer. The return path concept is still satisfied, since a ground island polygon is placed in at least one of the adjacent layers to each Force, Sense, and Ground Sense structure.

 !`DPS layout example`（raw: `../../../../raw/128773.png`）

### Example（取自子主题 Electrical design  General rules › RF DUT board design › Leakage and crosstalk of RF signals）

This example uses a fast rising edge aggressor signal to measure the two crosstalk values. NEXT has the same phase and FEXT has the 180 degree shifted (opposite) phase. The graphic shows typical microstrip NEXT and FEXT data:

 !`NEXT and FEXT microstrip data`（raw: `../../../../raw/128734.png`）

### Examples（取自子主题 Wafer prober interfaces › Direct-Probe interface › Direct-Probe PSRF probe card specifications）

### 48 RF Ports - using center connector locations

 !`48 RF Ports - using only center connector locations`（raw: `../../../../raw/123270.png`）

### 96 RF Ports - using inner and outer connector locations

 !`96 RF Ports - using inner and outer connector locations`（raw: `../../../../raw/123271.png`）

<!-- 语法节 end -->

## 是什么

**这是 V93000 接口件的设计指南入口页**——不是某个接口件的说明书，而是**一整套「怎么自己做出合格接口件」的手册的首页**。
原文把范围说得很清楚：

> 「Advantest is committed to providing high quality interfacing solutions for the V93000 test systems. These interfacing solutions include DUT boards, wafer prober interface boards, and wafer probe cards which can be obtained directly from Advantest or from other manufacturers that specialize in dedicated interfacing components.」

**三类接口件**：**DUT board**、**wafer prober interface board**、**wafer probe card**。
**而「从哪来」原文留了两个口子**：`either … directly from Advantest or from other manufacturers that specialize in dedicated interfacing components`
——**要么找 Advantest，要么找专做接口件的第三方。这份指南存在的理由就是后一条路。**

> 「This design guide provides the information needed to design and manufacture these devices such that they maintain the high-performance testing capabilities of the V93000.」

**这句话是整页的立身之本**：目标不是「能造出来」，而是**造出来还能保住 V93000 的高性能测试能力**。
**它同时决定了本页的性质——本页是入口，真正的设计规则在 12 个子主题里。**

### 12 个子主题（就是本页的目录）

| # | 子主题 | 原文里的分类 |
|---|---|---|
| 1 | `DUT board design overview` | 概览 |
| 2 | `Test heads` | 硬件 |
| 3 | `DUT interfaces` | 硬件 |
| 4 | `Utility lines` | 布线 |
| 5 | `Utility power supplies` | 电源 |
| 6 | `Pogo pin assignment` | 引脚分配 |
| 7 | `Electrical design: General rules` | 电气规则（通用） |
| 8 | `Electrical design: Product-specific rules` | 电气规则（按产品） |
| 9 | `DUT board docking` | 机械 |
| 10 | `DUT board stiffeners and inlay plates` | 机械件 |
| 11 | `Wafer prober interfaces` | 晶圆侧 |
| 12 | `Drawings, product numbers and commercial parts` | 图纸与物料 |

（**raw 路径都在 `02_System_reference/02.03_DUT_board_design_reference/` 下，文件名就是上面这些名字的 `_` 连写形式。**
**这 12 篇本页一篇都没读**，见 `## 出处`。）

**注意第 7、8 两条是一对**：**通用规则**和**按产品的规则**分开——
**也就是说「同一个电气设计规则，EXA Scale 和 Pin Scale 可能不一样」这件事，原文是用目录结构承认的**，
**而不是在正文里逐个交代。**

### 覆盖哪些系统，以及「不是每节都对你适用」

原文专门用一节说这件事，**核心是「这份指南与 SmarTest 版本无关」**：

> 「Many sections of the guide apply to all generations and variants of the V93000 system and are independent of the installed SmarTest version. This common guide contains therefore topics that may not apply to your system or SmarTest version.」

**覆盖的系统（原文列了五行）：**

| 系统 | 括号里的 SmarTest |
|---|---|
| V93000 EXA Scale system | **SmarTest 8** |
| V93000 Smart Scale system | **SmarTest 8** |
| V93000 Smart Scale system | **SmarTest 7** |
| V93000 Pin Scale system | **原文未标** |
| V93000 HSM system | **原文未标** |

> **两个细节值得单独点出来**：
> ① **`V93000 Smart Scale system` 出现两次**，两次唯一的区别是 **SmarTest 8 / SmarTest 7**——
> **同一代次配两代软件，是这份指南要同时覆盖的形态**；
> ② **`Pin Scale` 和 `HSM` 两行没有版本标注**——**原文没说为什么**，**本页不猜**。

**「不适用」怎么认出来，原文给了一条判据：**

> 「The involved topics are structured accordingly in an overview topic or otherwise marked.」

**即：相关主题会被组织进一个 `overview topic` 里，或者另有标记。**
**原文举的例子是 `Pogo pin assignment` 那一篇**——**这是本篇唯一点了名的子主题。**

### 对读者的前提：得会做受控阻抗 PCB

> 「This design guide assumes that the reader has knowledge of the design and manufacture of controlled impedance printed circuit boards.」

**这是原文对读者唯一的资格假设。** 换句话说：**这份指南不教 PCB 怎么做，只教 V93000 的接口件要怎么做。**

紧跟着是**一条推荐**和**一条硬要求**：

> 「Although Advantest recommends that you obtain stiffeners and inlay plates used in the interface assemblies directly from Advantest, information needed to manufacture these components is also provided.」

| 件 | 原文的立场 |
|---|---|
| **stiffener、inlay plate** | **推荐直接向 Advantest 拿**（`recommends`）；**但自己造所需的信息也给了**（`also provided`） |

> 「These mechanical components must be manufactured within the tolerances specified in this design guide and in the referenced technical drawings.」

**`must` + `tolerances`：机械件必须做在公差之内**，而且**公差写在两个地方**——
**本指南里**，以及**它引用的技术图纸里**。**只查一处是不够的。**

**最后一层是「为什么」：**

> 「The electrical and mechanical characteristics of the described parts are critical to the test system's proper operation. Be sure to carefully follow all instructions in this design guide and in all referenced technical drawings.」

**这些件的电气与机械特性对测试系统能否正常工作 critical**——
**这是整篇里唯一解释「为什么不能自己发挥」的一句**，
**也是上面那条「推荐向 Advantest 拿」的真正分量所在：推荐不是客套，是风险提示。**

### 要设计服务时找谁

原文末尾给了四个地区的邮箱：

| 地区 | 邮箱 |
|---|---|
| Americas | `support-americas@advantest.com` |
| Asia | `support-asia@advantest.com` |
| Europe | `support-eu@advantest.com` |
| Japan | `support-jpn@advantest.com` |

**原文的用词是 `To obtain additional DUT board design and custom interface services`**——
**这里要的是「服务」，不是「资料」；资料在本指南里。**

## 典型用法

**原文没有 `## Procedure`，也没有 `## Before you begin`。**
**它是一份指南的首页，不是一个操作流程**——所以「用法」只有下面四条：

1. **先确认你的系统在不在覆盖范围内**（上表五行）。
   **不在里面不等于整份指南作废**——原文说的是常见主题仍然适用，**但单个主题可能不适用**。
2. **按 12 个子主题找你要的那一支**。
   **原文没有给阅读顺序**，**也没说这 12 篇之间谁先谁后**——
   **「先读哪一篇」本页给不出**（见 `## 出处`）。
3. **要自己造 stiffener / inlay plate**：原文允许（制造信息给了），
   **但必须做在公差内**，**公差要看本指南 + 被引用的图纸两处**。
4. **要的是设计服务（不是资料）**：找四个邮箱之一。

**原文没有 `## Related information` 段，也没有 `## What to do next`**——
**它的出边就是那 12 个 `Subtopics`**，这一点和其他页不一样。

**一条本页必须交代的使用前提**：**这一页（那篇总览原文）给不出任何设计规则、尺寸、公差或图号。**
它只说这些规则「在子主题里、在引用的图纸里」。**所以「照着这一页画板」做不到。**
**（2026-09-20 补**：**本页语法节引到的那些图里确实有具体数值和尺寸**（`12.1kΩ`、`820`、`120`、`2.54 typ` 等），**见 `## 图里说了什么（④ 图证）`——但那是十篇子主题文档的图，不是这篇总览写的。****所以上面这句话对这篇总览仍然成立。**）

## 和谁有关

- [[direct-probe-stiffener ]] — **下游**：stiffener 的图纸页，归在上面第 10 / 12 两支下。
  **本页原文恰好对 stiffener 有明确立场：推荐直接向 Advantest 拿**
- [[layout-information-dut-board ]] — **下游**：DUT board 的布局图纸，
  归在第 12 支 `Drawings, product numbers and commercial parts` 下
- [[dut-board-grounding ]] — **下游**：属第 7 支 `Electrical design: General rules` 那一组；
  **本页原文没点名它**
- [[pogo-pad-and-via-design]] / [[pogo-block-compatibility]] / [[inter-layer-via-design ]] —
  同属本指南；**本页原文只在「哪些主题可能不适用于你的系统」那段点名了 pogo pin assignment 一篇**
- `Pogo pin assignment`（**未建**）— **本篇唯一点了名的子主题**，
  被原文当作「主题可能不适用于你的系统」这个结构的例子
- 其余 11 个子主题（`DUT board design overview`、`Test heads`、`DUT interfaces`、`Utility lines`、
  `Utility power supplies`、`Electrical design: General rules`、`Electrical design: Product-specific rules`、
  `DUT board docking`、`DUT board stiffeners and inlay plates`、`Wafer prober interfaces`、
  `Drawings, product numbers and commercial parts`）（**均未建**）—
  **本页只列了名字，一篇都没读**，所以**每一篇讲什么本页说不了**
  **（2026-09-20 补**：**这 11 支里 `Utility lines`、`Electrical design: General rules`、`Wafer prober interfaces` 三支的图本页看过，见 `## 图里说了什么（④ 图证）`；但看的是图，**这 11 篇的正文仍然一篇没读**，所以这句话不变。**）**

## 版本

**本文档没有 `## Functional changes` 段**（这是事实，不是缺陷）。

**而原文自己解释了为什么可以没有**：

> 「Many sections of the guide apply to all generations and variants of the V93000 system and are independent of the installed SmarTest version.」

**指南的大部分内容与 SmarTest 版本无关**——**（推断）这正是这一篇不需要 `Functional changes` 的原因**，
依据就是上面这句原文加上本文档确实没有该段。
**但注意这句说的是 `Many sections`（多数节），不是「全部」**——
**原文留了少数几节是跟版本走的，只是没说哪几节。**

**顺便说清一件事**：本页 `## 语法 / 参数` 那一大节（14,691 字符）**不是本文档的语法**——
它由脚本按 §4 从**本文档 + 九个子主题**逐字抽来，**段名里带「取自子主题 …」后缀的就是子主题的内容**。
**那九篇子主题本页一篇都没读**（见 `## 出处`）。

## 图里说了什么（④ 图证）

**本节 2026-09-20 补。** 起因是 `schema.md` §11.4 更正了一条错说法：图片路径
`../../../../raw/x.png` **不在语料树之外**——md 往上四层正好是 `tdc-html/`，
**图就在 `tdc-html/raw/` 里，而且读得出来**。

**本节读图的写法**（照 `objects/flags-page.md` 那页定的口径）：**图上读出来的字一律写成行内代码，
不进 `>` 引文块**——引文块的含义是「这段能在 raw 文本里搜到」，**而图上的字搜不到**。
**所以本节所有图内文字都不可 grep**，要核只能自己再开那张图
（本机 `F:/master-dev/dorm-wsl-sytest/tdc-html/raw/<编号>`）。
**图的 alt 文字是另一回事**——它在 md 里，**搜得到**，所以本节引 alt 时照引不误。

**读了 29 张**：本页语法节引到的 **12 张**，加上**这些图的源文档引到、而语法节没抽到的 17 张**
（**23 个 `.png` + 3 个 `.jpg` + 3 个 `.gif`**）。**29 张全在本页语法节署名的那 10 篇源文档里。**

### ④ 图证 · 一、Utility lines 与 utility line 的设置流程（9 张）

- **`136929.png`**（alt：`Utility read/write line - active wiring board`）**④ 图证**：
  正文只有 `The diagram shows the typical utility line interface circuitry on a system fitted with the active wiring board.`
  一句，**元件值全在图上**——
  `Utility Read` 一路经 `12.1kΩ` 串到 DUT 侧、另一路 `12.1kΩ` 上拉到 `+3.3V`；
  `Utility Write` 走一只三极管，基极 `10kΩ`；DUT 侧并了 `5.6V` 钳位与 `100nF`。
  右上角虚线框另写 `Recommended value: 1kΩ - 3.3kΩ`，注
  `On DUT Board if drive levels above +3.3 V are required`，上拉去 `+5V`。
  **⚠️ 图与正文数值对不上**：同一段正文说外挂上拉电阻取 `several hundred Ohms`，
  **图上写的是 `1kΩ - 3.3kΩ`**。**两处都在语料里，本页不替它选一个。**
- **`74690.png`**（alt：`Utility read/write line - passive wiring board`）**④ 图证**：
  这一路**只有 `+5V`，没有 ±3.3V**；`Utility Read` 经缓冲器 + `10kΩ` 串阻，
  上拉标 **`10kΩ / 271kΩ`**，另有二极管钳位到 `+5V`；`Utility Write` 走三极管，基极有对地电阻。
  **「主动板与被动板的差别」在两张图上一眼可见**，正文只说了「这是被动板上那套电路」。
  **⚠️ 图上那个 `271kΩ` 就这么印着**——**本页照实记，不替它改成 `27.1kΩ`。**
- **`343163.png`（inputs）+ `343164.png`（output）** **④ 图证**，**这一对把正文那段 `Example circuit` 补全了**：
  - 三路输入 `UL_SCLK` / `UL_FRAM` / `UL_SINP` 各经一只 **FODM8071**（位号 `U1` / `U6` / `U8`）
    与 **`820`** 串阻（`R1` / `R3` / `R8`），再经 **74LVC1T45**（`U2` / `U5` / `U9`）输出
    `UL_SCLK_buffered` / `UL_FRAM_buffered` / `UL_SINP_buffered`。
  - **地的接法（正文一个字没有）**：输入向那三只光耦的 `C` 脚接 **`DGND`**、`GND` 脚接 **`UGND`**；
    74LVC1T45 的 `GND` 接 **`UGND`**，一侧电源 `UTILITY_5V`、另一侧 **`1V8`**。
  - **方向是接死的**：74LVC1T45 的 `DIR` 脚在图上接在电源轨上，**不是被某个控制信号驱动的**。
  - **返回方向不一样**：`343164.png` 上 `UL_SOUT_buffered` 经 **`120`**（`R2`）进 `U4`，
    `VDD` 接 **`3V3`**、`GND` 接 `DGND`、`C` 接 `UGND`，输出 `UL_SOUT`。
    **正文只给了 820（还拿它算 5.4 mA），`120` 这个值是图给的。**
  - **两张图的地正好互换**：输入向（数字→utility）光耦的输入侧在 `DGND`；
    返回向（utility→数字）光耦的输入侧在 `UGND`。**这就是标题里 galvanic separation 的实际做法**，
    正文只说 `we recommend the implementation only if galvanic separation is really necessary`。
- **`152402.png`**（在 Mask mode 那篇里，**语法节只抽了代码、没抽这张**）**④ 图证**：
  **serial frame 的内容图**——`SCLK` 连续时钟、`FRAMn` 拉低表示帧有效，
  `SINP` 与 `SOUT` 是一条条**交替的 `Mask` 与 `Bit 31` … `Bit 0`**（`Mask` 段在图上画成斜线阴影）。
  **「mask 究竟遮住什么」语法节那两段代码答不了，这张图答了。**
- **`128789.png`**（Pin Configuration 工具截图）**④ 图证**：`SCLK` / `FRAMn` / `SINP` / `SOUT`
  四行的 `No` 都是 `0`，`Type` 依次 `i` / `i` / `i` / `o`，`Mode` 是 `std`，`HW` 是 `PS400`，
  `Connection Set` 空，`Tester Channel` 是 **`11701` / `11702` / `11703` / `11704`**。
  **语法节只有一张「Digital pin ↔ 描述 ↔ 方向」的表，`HW`、`No`、`Tester Channel` 三列全是图补的。**
- **`128790.png`**（SpecTool 截图）**④ 图证**：图上写 `Timing` · `Specification` `1` / `1` = `10MHz`，
  `Wavetable` 填 **`drive`**、`Equation` 填 **`1`**，下方参数表里 `Frequency` 的 `Actual` 是 `10`、
  `Unit` 是 `MHz`。**语法节那句 `Assign the clocking frequency for the serial control lines to your equation set and wavetable.`
  具体填在哪三格，是图给的。**
- **`128792.png`**（同一篇里的波形窗口，语法节没抽到）**④ 图证**：四行 `FRAMn` / `SCLK` / `SINP` / `SOUT`
  的波形，**`SOUT` 那一行是没被驱动的噪声线**，其余三行是方波。**这印证了正文那句
  `SOUT (D4) is not used and is therefore set to high-Z for all vectors in the sequence.`**
- **`124940.png`**（Pattern 编辑器）**④ 图证，并且和图外的正文对不上**：
  - **图里的事实**：列头是 `FRAMn (DVC)` / `SCLK (DVC)` / `SINP (DVC)` / `SOUT (DVC)`，
    `Signal size: 48 bytes`，向量 `0`–`43`、最后一行为 `STOP`；Comment 列只标了
    `bit 15`（v4）、`bit 11`（v12）、`bit 7`（v20）、`bit 3`（v28）、`bit 2`（v30）、
    `bit 1`（v32）、`bit 0`（v34），v36 那一格只写了一个 `-`。
  - **印证了正文三条**：`FRAMn` 列在向量 `4`–`35` 上是 `0`（正文说这段期间 FRAMn 驱动到 0）；
    `SCLK` 每两个向量一个 `0`/`1`（正文说一个 bit 两个向量）；`SOUT` 列整段是 `4`（高阻）。
  - **⚠️ 对不上的一条**：正文说「要打开 line 0、12、14 的继电器，`SINP` 必须在向量
    `34 & 35`、`10 & 11` 和 `6 & 7` 上驱动 `0`」；**图上 `6`、`7` 两行的 `SINP` 是 `1`**，
    `SINP` 为 `0` 的是 `4 & 5`（那一行的 Comment 恰好写 `bit 15`）。
    **图与正文卡在 bit 14 / bit 15 这一位上，本页不替语料选一个。**
  - **⚠️ 还有一处**：图上 `SINP` 为 `0` 的**共 6 组**（`4&5`、`10&11`、`20&21`、`24&25`、
    `28&29`、`34&35`），**正文只点了 3 组**。**照实记。**

### ④ 图证 · 二、Electrical design: General rules — DPS 布局（3 张）

- **`128773.png`** **④ 图证，这张把正文那句话解开了**：图右侧是一张叠层表，逐行 `Top`、`2Ag1`、
  `3A1`、`5A2`、`7A3`、`9Ag2`、`10A4`、`12Pw-p1`、`13Pw-g12`、`14Pw-p2`、`15Pw-p3`、
  `16Pw-g34`、`17Pw-p4`、`18Pw-p5`、`19Pw-g56`、`20Pw-p6`；图上用引出线把
  **`S1`→`12Pw-p1`、`G12`→`13Pw-g12`、`S2`→`14Pw-p2`、`S3`→`15Pw-p3`、`G34`→`16Pw-g34`、
  `S4`→`17Pw-p4`、`S5`→`18Pw-p5`、`G56`→`19Pw-g56`、`S6`→`20Pw-p6`** 一一对上。
  - **于是「`G12`」这个名字的意思定了**：它就是夹在 `12Pw-p1`（S1）与 `14Pw-p2`（S2）中间那一层；
    `G34` 夹 S3/S4，`G56` 夹 S5/S6。
  - **而 S2（`14Pw-p2`）与 S3（`15Pw-p3`）是相邻的、中间没有地平面**——
    **这正是正文那句 `This design saves every other ground layer.` 在图上的样子。**
  - 图上还可见一个叠层显示工具的界面（`Views` 下拉、`Conductors` / `Planes` 勾选、`Etch Via Pin Dir All`）。
- **`128771.png`**（同一篇里、**语法节没抽到**）**④ 图证**：alt 是 `Force / Sense / Ground lines`，
  画的是 **Force 一大片多边形、`Sense` 与 `Ground Sense` 是两根细线**（底下还有 `Ground Polygon`），
  右下图给出间距 **`3W` / `W` / `3W` / `W`**（以线宽 W 为单位）。
  **正文那句 `the "combined" lines of Force, Sense, and Ground Sense` 里三种线各长什么样、间距多少，
  语法节里没有，是这张图给的。**
- **`128772.png`** **④ 图证**：一块 DPS block 附近的布线视图，**图上可见的标注是块名与针名**——
  上缘一排列号 `06 08 10 12 14 16`，其下 `G6 PS2 P2 VB+ G7 PS3 P3 G8 PS4`，
  下缘 `GS6 GRD2 PS6 TRVB- TR+ NC G3 GS7 GRD3 PS7 NC G4 GS8 GRD4 PS8`，右缘 `MSDPS1`。
  **这些名字是从图上读的，grep 不到。**
  - **⚠️ 但图上没有层号**——正文点的 `Layer 8` / `Layer 9` / `Layer 10` / `Layer 11`，
    **这张图核不了**（见本节末尾）。
- **⚠️ 语料瑕疵（本页照实记）**：**`128772.png` 与 `128773.png` 是两张不同的图，alt 文字一模一样**
  （都是 `DPS layout example`）——**而且图上也没写哪个是 Example 1、哪个是 Example 2**，
  **语料靠正文上下文分**。**搜 alt 文字会同时命中两张。**

### ④ 图证 · 三、Electrical design: General rules — RF 泄漏与串扰（8 张）

- **`128734.png`**（**语法节留下的唯一一张图**）**④ 图证**：图是上下两幅曲线，
  **标题把测量条件写全了（语法节里没有）**——第一幅
  `Microstrip Crosstalk: 50 Ohm, 0.3 mm Traces, 1V Aggressor / 50 pS Risetime, 250 mm Long Crosstalk Length / 1x vs. 5x Trace Width Gap Agressor to Victim`，
  第二幅 `1x Trace Width Gap, 25 mm Short Crosstalk Length / 50 pS vs. 1 nS Risetime`；
  纵轴 `Crosstalk Amplitude, mV`（`-100` … `50`），横轴 `time, nsec`（`0` … `5`）；
  曲线上标 `NEXT >0` 与 `FEXT <0`，另标 `1x` / `5x` 与 `50 pS` / `1 nS`。
  **两幅图右下角都有一句正文没有的注：`Note: In Stripline FEXT << NEXT`。**
- **`129352.png`**（alt：`Coax cable vs. via`）**④ 图证**：左边是**真同轴**
  （中心导体 + 一圈 `Coaxial outer conductor`，红箭头从中心射向外导体），
  右边是**同一个中心加 4 只 `Ground vias`**（虚线圈代表「理想的外导体」）。
  **这就是「把过孔做成同轴」的定义图。**
- **`128719.gif`**（alt：`Ideal via with 4 ground vias`）**④ 图证**：同一构型的**场等值线**图，四瓣对称。
- **`128720.png`**（alt：`Ground pins and signal pins on pogo blocks`）**④ 图证**：
  pogo block 的针阵里，**黑箭头指的 `Ground pins` 与红箭头指的 `Signal pins` 是分色画出来的**。
- **`128724.png`**（alt：`Crosstalk`）**④ 图证**：图上标 `Leakage`（橙色虚线）、
  `Cross-talk`（虚线上那一点）、`Interferes with adjacent signal pin!`（指向旁边另一个同轴结构）。
  **泄漏走哪条路、窜到哪里，是图说清的。**
- **`128859.png`**（alt：`Vertical propagation with missing ground vias`）与
  **`128735.gif`**（alt：`Signal leaking out into board layer`）**④ 图证**：**两张都是三维电场仿真图**。
  `128735.gif` 带色标，量程 `1.0000e+000` – `9.3756e+003`（单位 `V/m`），
  **信号过孔周围的强场横向散进了叠层**。
- **`128737.gif`**（alt：`Improved ground via structure`）**④ 图证**：
  **和 `128735.gif` 同一套仿真、加了地过孔之后的样子**；**色标量程降到 `1.0000e+000` – `1.0000e+003` `V/m`**
  ——**峰值场强比上一张低了约一个数量级**（`9.3756e+003` → `1.0000e+003`）。
  **这个前后对比是图给的，正文没有。**

### ④ 图证 · 四、Pogo pin assignment — PSSL（2 张）

- **`143039.jpg`**（alt：`PS-SL pogo cable`）**④ 图证**：实物照片，**一条线束上两只 pogo block**，
  分别标 `Pogo block B` 与 `Pogo block A`。**这和语法节里 `pogoblocks = 317 321`、
  `pogoblocks = 301 305` 每行给两个号对得上**——
  （**推断**：一张 PSSL 卡两个 block；**依据**是这一缆两块 + 语法节两行各两个号；**文档没有明说**。）
- **`143046.png`**（alt：`PSSL pogo block - SD - dimensions`）**④ 图证**：**带尺寸的针位图**——
  4 列 `a` `b` `c` `d`、17 行 `1` … `17`，行距标 `2.54 typ`，横向标 `3.81 typ` 与 `1.27 typ`，
  右下角有 `Orientation mark`。**语法节里那个 model file 例子只给 pogoblock 号，
  针位排布与尺寸全在这张图上。**

### ④ 图证 · 五、Wafer prober interfaces — Direct-Probe（7 张）

- **`123155.png`** **④ 图证**：Direct-Probe 接口的 CAD 图，标注 `Prober head plate`、
  `Bridge beam with Port Scale RF interface adapter`、
  `RF tower, part of the tester, is shown for illustrative purposes only`、`Probe card`、
  `Direct-Probe™ ring insert`。**这一套件名语法节里一个都没有**——
  **它正是本页链到 [[direct-probe-stiffener]] 那一支要用的材料。**
- **`123156.png`** **④ 图证**：同一块板的分区标注：`PSRF outside brackets with connector block 2x12`、
  `PSRF inside brackets with connector block 2x2x12`、`Support blocks (see circles)`、`Cable brackets`。
  **连接器块有 `2x12` 与 `2x2x12` 两种密度——这是图给的。**
- **`123270.png` / `123271.png`** **④ 图证**：两张**同一个底板、不同连接器位选用**的对照图。
  `123270.png`（alt：`48 RF Ports - using only center connector locations`）
  **只有中间那两对连接器位打了孔**；`123271.png`（alt：`96 RF Ports - using inner and outer connector locations`）
  **在左右两块朝内的那条边上又多出连接器位**。
  **「48 口只用中心、96 口再把内外侧用上」在图上是一眼的事，能读到的只有 alt 那一句。**
- **`126199.png`** **④ 图证**：同一底板的局部放大，标出 **`Guide pins`** 的三处位置。
- **`93846.jpg` / `123966.jpg`** **④ 图证**：**实物照片**——Direct-Probe 的环状镶件（米色）
  分别拍在**装进铝板之后**与**单独放在台面上**两种状态；镶件上是一大片**圆形排布的针孔阵**，
  另有几根突出的定位针。**「ring insert 长什么样」的唯一材料就是这两张照片。**

### 图解决不了的（照实说）

- **12 个子主题里只有 4 支留下了图**（`Utility lines`、`Pogo pin assignment` 的 PSSL、
  `Electrical design: General rules` 的 DPS 与 RF、`Wafer prober interfaces` 的 Direct-Probe、
  以及 utility line 的设置流程）。**其余各支本页仍然一个字没有**——
  **「12 个子主题本篇一篇没读」这条不变**（看的是图，不是正文）。
- **正文点的 `Layer 8` / `Layer 9` / `Layer 10` / `Layer 11`（DPS 那两段）图核不了**：
  `128772.png` 上**一个层号都没有**，`128773.png` 的叠层表只从 `Top` 列到 `20Pw-p6`。
  **「哪一路信号走第八层」，图答不了，本页也不猜。**
- **`Pin Scale` / `HSM` 两行为什么没有 SmarTest 版本标注——图一张也答不了。**
- **「12 个子主题先读哪一篇」——图答不了。**
- **「哪些主题会被标成『可能不适用于你的系统』」——图答不了**
  （那是 `Pogo pin assignment` 那篇的 `overview topic` 结构，本页仍未读）。
- **图上读到的字全都不可检索**：本节凡写在行内代码里的图内文字（元件值、位号、层名、
  Tester Channel 号、仿真量程、标注文字），**拿它去 raw 里 grep 是搜不到的**——
  **要核只能自己再开那张图。这是 ④ 档相对 ①②③ 档唯一的毛病，`schema.md` §11.4 要求写明它。**

## 出处

`sources:` 一篇：
`02_System_reference/02.03_DUT_board_design_reference/02.03_DUT_board_design_reference.md`

**本页做了的**（**2026-09-20 补**）：

- **加了一节 `## 图里说了什么（④ 图证）`**：把本页语法节引到的 **12 张图**、加上**这些图的源文档引到、
  而语法节没抽到的 17 张**（**共 29 张**）**逐张看过**。**图答得出来的写进那一节，
  图答不出来的单列在那一节末尾。**
- **删掉了一条不成立的理由**（原先「一张图都没看」后面那句），**换成了上面那一节**——
  **改判记录留在下面「本页没做的」那一条里。**
- **本文档本身（`02.03_DUT_board_design_reference.md`，3,486 字节）仍然只读了这一篇**，
  **它的 12 个子主题一篇没读**——**这一点没有变。**

**本页没做的**（**这一节对本页尤其重要，因为本页的语法节很长，而它不属于本页所读的范围**）：

- **`## 语法 / 参数` 节里带「取自子主题 …」后缀的段落，本页一概不能背书。**
  那些内容按 §4 由脚本逐字抽自**九个子主题**（`Utility line characteristics`、
  `Mask mode of sequencer-controlled utility lines`、
  `Galvanic separation between utility line serial interface and digital pins`、
  `Setting up sequencer control of utility lines`、`Designing compatible utility lines`、
  `PSSL pogo cable assembly: pogo pin layout and model file configuration`、
  `DPS layout rules for high frequency designs`、`Leakage and crosstalk of RF signals`、
  `Direct-Probe PSRF probe card specifications` 等），**本页作者一篇都没读**。
  **所以那一节里的 API 调用、参数值、图号、公差，本页一个字都没核**——
  **唯一例外是那一节引到的图**：**29 张逐张看过，见 `## 图里说了什么（④ 图证）`。
  但那是图上的字，不是那一节转抄的字，两件事不能互相背书。**
- **12 个子主题一篇没读。** DUT board 怎么设计、utility line 怎么接、pogo 怎么分配、
  RF 怎么走线、docking 怎么做——**本页一个字没有**。
- **图看了 29 张**（**2026-09-20 改判**，见 `## 图里说了什么（④ 图证）`）。
  **这一条原先写的是：「一张图都没看。原文正文没有插图；语法节里那些 `.png` 引用本页也没打开」。**
  **改的理由**：`原文正文没有插图` 只对**本文档**（那篇总览）成立——**它确实一张图都没有**；
  **但本页语法节那 14,691 字符抽自十篇文档，图上写的东西正在那十篇里**。
  **所以它当时不是理由，只是一句听着体面的话**——**真理由就是本页没去开那些文件**。
  **一个不成立的理由比没有理由更坏**（`schema.md` §11.4 ①：**「本页没用图」是真的，
  「因为图够不着／没有图」是假的**），**本次删掉。**
- **没有 `## Procedure` / `## Before you begin`**，**也没有真的做过一块 DUT board**——
  `verified: doc-only` 指的就是这件事。
- **四个邮箱本页没有验证过是否仍然有效。**
- **`overview topic` 这个结构具体长什么样（`Pogo pin assignment` 那篇），本页没读**——
  **所以「哪些主题会被标成『可能不适用于你的系统』」，本页给不出清单。**
- **`Pin Scale` / `HSM` 两行为什么没有 SmarTest 版本标注，原文没说，本页不猜。**

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改。**
> **其中①②出现在脚本逐字抽来的语法节里（本页不能改那一节，也不替它改）**：
>
> ① **编码损坏（§11.2 ①），共 9 处 `鈥`（U+9225）**：
> - `sequencer鈥慶ontrolled` —— **7 处**（代码注释里 5 处、正文说法里 2 处）；
> - `Internal pull鈥憉p resistor of utility lines` —— **1 处**（坏字 `鈥憉` = `‑u`）；
> - `Utility lines URW00 鈥?nbsp;URW15` —— **1 处**。
>   **这一处是复合损坏**：除编码坏了之外，**`&nbsp;` 这个 HTML 实体压根没被解码**，
>   于是就出现了 `鈥?nbsp;` 这种「坏字 + `?` + 实体名」的形态。**原文如此。**
>
> ② **`惟`（U+60DF）应为 `Ω`，1 处**：`In combination with the shown 820 惟 series resistor`
> ——**上下文（820、串联电阻、欧姆）指向 `Ω`**，**但这属于（推断）；本页照原样转录**。
>
> **合计 10 处**。**要拿这些词去 raw 里搜，得搜坏掉的形态，搜修好的字搜不到**——
> 这正是 §11.2 ① 说的代价。
>
> ③ **标题层级不连号**：`Subtopics` 用的是四级标题 `#### Subtopics`，
> 而正文其余各节是二级标题（`## V93000 systems covered by this guide` 等）——
> **同一篇里出现 `#` → `####` → `##` 的跳级**。原文如此。
>
> ④ **`Generations and variants of the V93000 system covered by this guide:` 这一行以空格开头**
> （原文该行首有一个前导空格）。原文如此。
>
> ⑤ **子主题树排在正文之前，而两段总述没有节标题。** 文档的结构是
> `# DUT board design reference` → `#### Subtopics`（12 条）→ 两段 `Advantest is committed to …`
> ——**这两段总述直接挂在 H1 下面，没有属于自己的节标题**，
> 而**后面每节（`## V93000 systems covered by this guide` 等）都有**。
> 原文如此，本页不替它归并。

`verified: doc-only`
