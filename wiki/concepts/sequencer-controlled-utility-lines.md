---
type: concept
title: Sequencer-controlled utility lines
layer: n/a
stage: pattern
tags: []
related: []
sources:
  - 03_Use_cases_and_application_papers/03.09_How_to_set_up_sequencer__ontrolled_utility_lines/03.09.01_Sequencer-controlled_utility_lines.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# Sequencer-controlled utility lines

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **9,248 字符逐字取自** `<03_Use_cases_and_application_papers/03.09_How_to_set_up_sequencer__ontrolled_utility_lines/03.09.01_Sequencer-controlled_utility_lines.md>` 及其子主题 `<03_Use_cases_and_application_papers/03.09_How_to_set_up_sequencer__ontrolled_utility_lines/03.09.01.04_Mask_mode_of_sequencer-controlled_utility_lines.md>`、`<03_Use_cases_and_application_papers/03.09_How_to_set_up_sequencer__ontrolled_utility_lines/03.09.01.05_Setting_up_sequencer_control_of_utility_lines.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example 1: SmarTest 7 dynamic mask（取自子主题 Mask mode of sequencer-controlled utility lines）

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

### Example 2: SmarTest 7 static mask（取自子主题 Mask mode of sequencer-controlled utility lines）

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

### Example 1: Setup for SmarTest 7（取自子主题 Setting up sequencer control of utility lines）

The following example sets up three digital pins named D1, D2 and D3 to act as serial inputs to the utility line controller on the active wiring board, refer also to the graphic in `Sequencer-controlled utility lines`（raw: `03.09.01_Sequencer-controlled_utility_lines.md`）. The controller acts as the DUT in this case.

Pin D4 is a receive pin. It is also set up in the pin configuration but is not used in the rest of the example. The example programs utility lines 1, 3, and 15 on utility block 1 to turn on LEDs connected to these lines.Note This example uses 2-row pogo blocks.

Serial pins for sequencer control of utility lines
 | Digital pin  | Serial pin description  | Direction |
 | SCLK  | Serial clock  | Input |
 | FRAMn  | Serial frame enable  | Input |
 | SINP  | Serial data in  | Input |
 | SOUT  | Serial data out  | Output |

-  Make the following entry in the `GLOBAL section`（raw: `../../02_System_reference/02.04_Model_File_and_Licensing/02.04.01.03.02.01_GLOBAL_section.md`） of the SmarTest 7 model file:

utility_lines = 128, type = sequencer_controlled, pogo_size = 16

pogo_size specifies the number of utility lines per pogo block and utility_lines specifies the total number of utility lines (pogo_size multiplied by the number of utility blocks). Usual combinations are 64/16, 128/16 and 256/32.

Note If you were to use 4-row utility pogo blocks, the values for utility_lines and pogo_size would need to double. Combinations such as 128/32 or 256/16 are invalid. Note The default for the model file is 128 utility lines and 16 utility lines per pogo block. This applies if you omit the utility_lines entry.

Make the following entry in the `.technology file`（raw: `../../01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.01.02_Technology_file_for_a_device.md`）:

utility_lines_per_pogo_block: 16

Alternatively you could edit the Utility Block Size entry in the Change Device dialog window, in this case refer to `Editing technology data`（raw: `../../01_Getting_started/01.01_SmarTest_Work_Center/01.01.10.03.03_Editing_technology_data.md`）.

Refer also to `Configuration of 4-row or 2-row utility pogo blocks`（raw: `../../02_System_reference/02.03_DUT_board_design_reference/02.03.04.07.02_Configuration_of_4-row_or_2-row_utility_pogo_blocks.md`）.

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

Bit 0 of SINP specifies utility line 1, bit 15 specifies utility line 16. Thus to turn on relays on lines 0, 12 and 14, the pattern on SINP (D3) must drive a 0 on vectors 34 & 35, 10 & 11 and 6 & 7. The rest of the vectors must remain at 1. Each relay coil must be connected between the UP5V line and the corresponding utility line as shown in example `Controlling user relay on a DUT board (V93000 systems)`（raw: `../../02_System_reference/02.03_DUT_board_design_reference/02.03.04.03.03_Utility_line_example_circuits.md#_98018__s_Controlling_user_relay_on_a_DUT_board`） of `Utility line example circuits`（raw: `../../02_System_reference/02.03_DUT_board_design_reference/02.03.04.03.03_Utility_line_example_circuits.md`）. For additional details refer to `Utility line interface circuitry`（raw: `../../02_System_reference/02.03_DUT_board_design_reference/02.03.04.03_Utility_line_interface_circuitry.md`）.

For the mapping of utility lines on utility blocks refer to the links in `step 2`（raw: `03.09.01.05_Setting_up_sequencer_control_of_utility_lines.md#_124758__cmd_Routing_of_digital_pins`） of the procedure above. SOUT (D4) is not used and is therefore set to high-Z for all vectors in the sequence.

  !`Control pattern for a single utility line block`（raw: `../../../../raw/124940.png`）  Note If you were to use 4-row utility pogo blocks, the pattern would need to be extended to shift 32 bits into the utility line shift register instead of 16. Note Entering a pattern manually can be a tedious and error-prone method, but is the simplest way if controlling just one or two utility blocks. If you need many utility lines you may consider other methods such as `d2s`（raw: `../../02_System_reference/02.07_Test_Method_Reference/02.07.09_d2s-framework.md`） or `Protocol Aware`（raw: `../../02_System_reference/02.07_Test_Method_Reference/02.07.11_Protocol_Aware_ATE.md`）.
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

### Example 2: Ganging utility blocks in SmarTest 7（取自子主题 Setting up sequencer control of utility lines）

If you were to gang two 2-row utility line blocks together you would need to set up a pattern of twice the length as you would have to shift in 32 bits instead of just 16. Then, to enable for example utility line blocks 1 and 2 for serial control, you would need to implement the following API call into your test methods:

```
UTILITY_SEQ_MODE utiSeqModeOn;

utiSeqModeOn.pogoBlock(1,2).mode(TM::SEQ_POGO_MODE_RW );
utiSeqModeOn.execute();
```

Note If you were to gang two 4-row utility pogo blocks, the above API calls would shift 64 bits into the utility line shift register instead of 32.

<!-- 语法节 end -->

## 是什么

**utility line 有两种访问方式，本页讲第二种：**

| | 静态访问（static access） | **动态访问（dynamic access）** |
|---|---|---|
| 谁在控制 | 主机写寄存器 | **pattern sequencer** |
| 能否与 pattern 同步 | **不能** | **能** |

原文对动态访问的定义是：utility line 由 pattern sequencer **经内部数据通路**、
或**借数字引脚 + utility 块上的专用串行接口**来控制。相对静态访问的好处就是
**能把 utility line 的动作与 pattern sequencer 同步**。

### 走哪条路，取决于机台代次

| 机台 | SmarTest | 控制路径 |
|---|---|---|
| V93000 **EXA Scale** + Utility Card | **8** | **内部数据通路** |
| V93000 **EXA Scale** + 可选 Utility Card | **7** | utility pogo block 的串行接口 |
| V93000 **EXA Scale**（无 Utility Card） | 7 | 同上（原文列在「同样适用」一句里） |
| V93000 **Smart Scale / Pin Scale** | 7 或 8 | **utility pogo block 的串行接口** |

**串行接口在「active wiring board」上**，用数字引脚驱动。
它的连接点是 **`FRAMn`、`SCLK`、`SINP`**，以及 **`SOUT`（SmarTest 7 下可选）**。
这些引脚**必须在 DUT board 上接到数字引脚**。串口**至少要为一个 utility pogo block 布线**，
另外还有**内部菊花链**可以让一组数字引脚管多个 utility pogo block（见「Ganging utility blocks」）。

> **EXA Scale 上的差异**：串行接口的功能由 **Utility Card（Variant `EK051A`）**自己提供，
> **对一张卡的全部八个 utility pogo block 都可用**。该串口**只在 SmarTest 7 下用**；
> SmarTest 8 走内部数据通路，**数字引脚接上去也不使用**（接了也接受，但不用）。

### 支持的机台配置

原文给了一张表，要点：**EXA Scale 三种 test head（LX / SX / CX）走 DUT Scale 接口**，
**8 或 16 个 utility block、256 或 512 根线**；
**Pin Scale / Smart Scale 的 A 级（ATH）**在标准接口下是 4 块 / 64 线，在 DUT Scale 接口下是 8 块 /
128 线（2 排块）或 256 线（4 排块）；**CTH / STH / LTH 走 DUT Scale 接口**。

### 一处电气前提：地要隔离

utility pogo block 的**地针 `UGND` 可以接到 DUT board 的数字地 `DGND`**，
但可能需要在 DUT board 上**在两个地域之间插入隔离电路**——目的是防止地环路
**影响 level 精度**、**把噪声带进测量**。原文说，
**用 utility pogo block 的串行接口时可能需要做这个隔离**（Pin Scale / Smart Scale / EXA Scale 都算；
EXA Scale 跑 SmarTest 8 但接了数字引脚的也算）。

## 典型用法

**1. 什么时候需要它**：只有当 utility line 的动作**必须和 pattern 对齐**时才需要。
纯静态的开关与读回，用 [[utility-line-assignments]] 描述的静态访问就够。

**2. 接线次序**：先在 DUT board 上把串口引脚接到数字引脚（EXA + SmarTest 8 不需要额外连接），
再让 SmarTest 把 wiring board 配成动态访问模式。**主时钟板只用于静态 setup
和把 active wiring board 配成动态访问**，之后动态控制由串口上的引脚完成。

**3. 想用一组引脚管多个块**，走内部菊花链（见 `Ganging utility blocks`）。

**4. 静态 / 动态的依赖关系**：原文有专门一节
`SmarTest 7 dependencies between static and dynamic access`——
**SmarTest 7 下两者之间有依赖**。**本节未读**（见「出处」）。

## 和谁有关

- [[utility-line-assignments]] — utility line 的基本形态、线数、块型、上拉；
  **本页是它的「动态」那一半**
- [[pin]] — 串口引脚必须落在 DUT board 的数字引脚上，属 pin 阶段的分配问题
- [[pattern]] — 同步的对象是 **pattern sequencer**，本页因此归 `stage: pattern`
- [[dut-board-grounding]] — `UGND` / `DGND` 之间要不要隔离，是接地设计的一部分
- [[sequencer ]] — 被同步的那个 sequencer 本身

## 版本

- **SmarTest 7 与 SmarTest 8 走的是两条不同的路**（见上表）：7 用串行接口，8 用内部数据通路
- EXA Scale 的 **Utility Card 是可选件**（Variant `EK051A`）；原文说一张或两张
- **本篇 `## Functional changes` 本次未读到**（原文该节在文档末尾，见「出处」）

## 出处

`sources:` 一篇：
`03_Use_cases_and_application_papers/03.09_How_to_set_up_sequencer__ontrolled_utility_lines/03.09.01_Sequencer-controlled_utility_lines.md`

这篇底下挂着**七个子主题**：

- `Serial interface for sequencer-controlled utility lines`
- `Specifications for the serial interface`
- `Ganging utility blocks`
- `Mask mode of sequencer-controlled utility lines`
- `Setting up sequencer control of utility lines`
- `SmarTest 7 dependencies between static and dynamic access`
- `Utility line capabilities in relation to the system hardware`

**本页只覆盖正文（父主题）那部分，七个子主题一篇都没读。** 所以：

- **串口的电气规格（速率、时序、电平）本页一个字都没有。**
- **mask mode** 是什么，**本页不知道**。
- **静态/动态在 SmarTest 7 下的依赖**本页没写。
- **怎么一步步 setup** 本页没写（正文只有「你需要做这几件事」的要点，细则在子主题里）。

以上四条**要读请回 raw**，别拿本页当它们的小结。

> ⚠️ **语料在本篇里有编码损坏**，搜原文时要用坏掉的那个形态：
> `2鈥憆ow`（= `2-row`）、`URW00 鈥?nbsp;URW15`（= `URW00 – URW15`）、
> `sequencer鈥慶ontrolled`（= `sequencer-controlled`）。损坏原因见 [[dps128-dps64-cards]] 里的同一段说明。

`verified: doc-only`
