---
type: object
title: Pattern Tools
layer: gui
stage: pattern
tags: [pattern-tools, pattern-explorer, pattern-editor, multiport-burst-editor, pattern-debug, gui-tool, f330-scan, klipper]
related: [pattern-explorer, pattern-editor, multiport-burst-editor, pattern, smartest-6.3.2, smartest-7.1.3]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16_Pattern_Tools.md
created: 2026-09-21
updated: 2026-09-21
verified: doc-only
---

# Pattern Tools

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **16,357 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16_Pattern_Tools.md>` 及其子主题 `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.06_Cloning_a_pattern.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.07_Moving_or_copying_pattern_files.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.08_Deleting_pattern_files.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.14.01_Moving_vectors_to_another_memory_type.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.01_Collapsed_and_expanded_mode.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.02_Signal_and_pin_group_representations.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.03_Pattern_editor_properties_view.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.04.03_STATEMAP_section_of_the_wavetable.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.06.16_Creating_a_Digital_Source_setup.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.04.05.01_Function_of_the_base_wavetable.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Pattern Explorer › Cloning a pattern）

The following examples explain the transformation to NOP instructions in more detail.

- For the instruction `SSRC dsm_data_pattern`, if the port of the pattern `dsm_data_pattern` is also the port of the target pattern, the `SSRC` instruction is cloned to the target pattern without change.
- For the instruction `JSUB sub_pattern`, as the port of the pattern `sub_pattern` is not the same as that of the source pattern, in the target pattern, the `JSUB` instruction is replaced by an `NOP` instruction and a warning message is displayed on the console tab.

If an instruction is replaced by `NOP` in the target pattern (for example, the `JSUB sub_pattern` instruction), you must modify the instruction manually:

- Create a new subroutine pattern `sub_pattern_clone` by cloning the `sub_pattern` pattern with the port of the target pattern.
- Replace `NOP` with the `JSUB` instruction using the new pattern: `JSUB sub_pattern_clone.`

### Example（取自子主题 Pattern Explorer › Moving or copying pattern files）

Update of pattern master file when moving `pattern 4` from the `patterns_a` folder to the `patterns_b ` folder`:`

 |

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/129118.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。

Before

 |

After

 |
 |

```
hp93000,pattern_master_file,0.1
 
path:
  ../data/patterns_a
 
files:
  pattern1
  pattern2
  pattern3
  pattern4
 
path:
  ../data/patterns_b
 
files:
  pattern5
  pattern6
```

 |

```
hp93000,pattern_master_file,0.1
 
path:
  ../data/patterns_a
 
files:
  pattern1
  pattern2
  pattern3
 
path:
  ../data/patterns_b
 
files:
  pattern4
  pattern5
  pattern6
```

 |

### Example（取自子主题 Pattern Explorer › Deleting pattern files）

"Cannot delete ..." error message:

 !`Error: Cannot delete because referenced ...`（raw: `../../../../raw/129371.png`）

Confirmation dialog:

 !`Confirm Delete dialog`（raw: `../../../../raw/129372.png`）

### Usage（取自子主题 Pattern Explorer › Editing properties in the Pattern Explorer › Moving vectors to another memory type）

The general format of the call is:

conv_vector -target <option><source_file><target_file>

<option> will usually be

- SM for conversion to SM or
- VM for conversion to VM

Rules:

- If you use port names in your vector file you must also specify a pin configuration file with the option -p.

You may specify a pin configuration file in any case.

- conv_vector does not accept a pattern master file.
- When the source file came from a single-density (SD) V93000 system, you must use the -sdvectors option.

For more details, type conv_vector without any parameters:

```
Tool to convert the vector file to the specified target format
conv_vector Revision: 5.4.33 (26-May-2017)
conv_vector [options] source-file [dest-file]
Converts the vector file <source-file> to the specified target format
and writes it to <dest-file> or stdout if no <dest-file> is specified.
-target <str>   The conversion target; one of MCU, C200...P1000, F330,
                SM(Sequencer Memory), VM(Vector Memory), UMM (Unified Memory Mode), SHMEM(Shared Memory)
-quiet          Warnings and messages are suppressed
-log <str>      All messages are written to a log file
-compress       The resulting vector file is compressed
-novectors      No vector data is emitted
-noscan         Scan vectors and labels containing scan calls are removed
-nomemtest      Memory tests are removed
-toascii <str>  Print waveform DC/DC power units of specified label and pin
-reorder        Puts SQPG's directly after defining label
-escan2 <str>   Pins in external scan memory with 2 bit/vector
-escan4 <str>   Pins in external scan memory with 4 bit/vector
-p <str>        Pin Configuration File
-keep           The resulting vector file will not be removed in case of error during conversion
-sdvectors      Source vector file originates from a V93000 Single Density (SD) test system.

```

### Example（取自子主题 Pattern Explorer › Editing properties in the Pattern Explorer › Moving vectors to another memory type）

conv_vector -target SM -p pins_soc pattern_vm pattern_sm

### Example（取自子主题 Pattern Editor › Collapsed and expanded mode）

The following two figures show the same pattern in collapsed mode and in expanded mode.

 !`Collapsed mode`（raw: `../../../../raw/101904.png`）

The pattern contains the sequencer instruction RPTV 3 2, which means the next three vectors are performed twice.

In the figure below, which shows the same pattern in expanded mode, you can see the resolved sequencer instruction and the Cycle# column.

 !`Expanded mode`（raw: `../../../../raw/101911.png`）

### Example（取自子主题 Pattern Editor › Signal and pin group representations）

The following figure shows the signals Pin 1, Pin 2 and Pin 3 in three different formats. The signal column headers contain the signal name (for example Pin 1) and the format (SC, DVC, PW).

 !`Pattern Editor showing xN example pattern`（raw: `../../../../raw/100465.png`）

### Examples（取自子主题 Pattern Editor › Pattern editor properties view）

### Vector properties

The graphic below shows the properties of a vector in device cycle (DVC) format.

 !`Device cycle properties view`（raw: `../../../../raw/129366.png`）

On vector properties views you cannot edit any parameters. Do this in the pattern editor.

The vector properties view always shows the physical waveform. Drive edges and receive edges appear on two different lines. In collapsed mode the view is based on the `base wavetable`（raw: `02.08.04.16.04.05.01_Function_of_the_base_wavetable.md`）, in expanded mode the properties are taken from the primary wavetable.

Any abbreviations you may use in your wavetables, are translated into the proper action code for `drive edges`（raw: `../02.06_Command_Reference/02.06.06.01.03.01.01.01_Drive_actions.md`） and `receive edges`（raw: `../02.06_Command_Reference/02.06.06.01.03.01.01.02_Receive_actions.md`）.

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/114627.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：8 行 × 5 列。
> 首行（上游原文）：Drive edges | Receive edges

### Test point properties

The graphic below shows the properties of a test point, in this case the highlighting of a force value in a dynamic DC test setup.

 !`Specifying the Force Value in the Properties view`（raw: `../../../../raw/113304.png`）

The properties view of a dynamic DC measure test point will also show the measure result. See below:

 !`Pattern editor properties view example`（raw: `../../../../raw/114630.png`）

### Vector variable properties

The properties view of a vector variable (see below) allows to edit for example, the assigned pins, the transfer mode, and other parameters. To display additional data upload formatting parameters (Upload Parameters) click the Show Advanced Properties icon. For a definition of the vector variable parameters see `Creating a Digital Capture setup`（raw: `02.08.01.02.07.02.05.01_Creating_a_Digital_Capture_setup.md`）.

 !`Vector variable properties view`（raw: `../../../../raw/116397.png`） Note The Upload Parameters shown here are the last which were used by the system. If you stop a testflow at a particular test suite and then open the pattern editor, the vector variable data is shown exactly as it was last uploaded from any test method or any command line operation.

### Examples（取自子主题 Pattern Editor › DUT oriented view - xN and x1 N mode › STATEMAP section of the wavetable）

### STATEMAP section with X1 waveforms

```
WAVETBL mytable
PINS io_pins
0 "d1:0 r1:X" 0
1 "d1:1 r1:X" 1
2 "d1:Z r1:L" L
3 "d1:Z r1:H" H
4 "d1:Z r1:X" X
brk ""
STATEMAP
#physSeq statechars x-mode selector
0 0 x1
1 1 x1
2 L x1
3 H x1
4 X x1
```

The five STATEMAP lines of above example define X1 waveforms.

The second STATEMAP example below defines xN and x1/N mode waveforms.

```
WAVETBL mytable
P1NS a11
0 "{d:1:0 d2:0 r1:H} {d3:0 d4:0 r3:H} {d5:0 d6:0 r5:H}" drv0-3
1 "{d1:1 d2:0 r1:H} {d3:1 d4:0 r3:H} {d5:1 d6:0 rS:H}" drv1-3
2 "{d1:0 d2:0 r1:H} {d3:0 d4:0 r3:H} {d5:0 d6:0 r5:H} {d7:0 d8:0 r7:H}" drv0-4
3 "{d1:1 d2:0 r1:H} {d3:1 d4:0 r3:H} {d5:1 d6:0 r5:H} {d7:1 d8:0 r7:H}" drv1-4
4 "{d1:0 r1:H} {d2:0 r2:H} {d3:0 r3:H} {d4:0 r4:H} {d5:0 r5:H} {d6:0 r6:H} {d7:0 r7:H} {d8:0 r8:H}" drv0-8
5 "{d1:1 r1:H} {d2:1 r2:H} {d3:1 r3:H} {d4:1 r4:H} {d5:1 r5:H} {d6:1 r6:H} {d7:1 r7:H} {d8:1 r8:H}" drv1-8
6 "d1:FOO" drv0
7 "d1:F10" drv1
STATEMAP
#physSeq statechars x-mode se1ector
0 000 x3
1 111 x3
2 0000 x4
3 1111 x4
4 00000000 x8
5 11111111 x8
6,6,6,6 0 x1/4
7,7,7,7 1 x1/4
6{8} 0 x1/8
7{8} 1 x1/8
6{16} 0 x1/16
7{16} 1 x1/16
```

The first six lines of above example STATEMAP section define xN waveforms and the last six lines define x1/N waveforms.

### General

The STATEMAP section is appended after the PINS statement containing all waveform definitions. The STATEMAP ends when a new WAVETBL or PINS keyword is found or at end-of-file (equation setup file).

Within a single WAVETBL several PINS and corresponding waveform definitions may be defined. All edges belonging to the same X-waveform are enclosed in {} braces (see also `Representing a pattern in device orientation`（raw: `../02.06_Command_Reference/02.06.06.01.03.05_Representing_a_pattern_in_device_orientation.md`）). The STATEMAP may also be defined per PINS statement.

### physSeq

Defines the sequence of physical waveforms. Each value of the physSeq column references an existing physical waveform defined in the PINS section. Similarly, each waveform defined in the PINS section must be represented at least once in the STATEMAP section. That is full consistency between the waveforms defined in the PINS section and the STATEMAP section.

The physSeq specifications must match the x-mode as follows:

- xN-mode: one hex number
- x1/N-mode: N hex numbers, comma separated, N ≤1024

When defining x1/N-mode, you can use the following syntax:

- Wildcard string *

Example 1: when defining x1/4-mode: 0,A*,2 represents 0,A,A,2

Example 2: when defining x1/16-mode: 2*,F,3 represents 2,2,2,2,2,2,2,2,2,2,2,2,2,2,F,3

- Repetition factor in curly braces {n}

Example: when defining x1/16-mode: 2{14},F,3 represents 2,2,2,2,2,2,2,2,2,2,2,2,2,2,F,3

### statechars

Defines the state characters displayed in the Pattern Editor. The Pattern Editor and the Configure Layout dialog list state characters (statechars) as SC. The state characters consist of the characters [a-z][A-Z][0][1]. The length is:

- always one character for x1/N-mode and
- N characters for xN-mode.

Examples:

- when defining x1/8 mode: 0
- when defining x8-mode: 00000000

### x-mode

Defines the x-mode. The maximum values are:

- for xN-mode: x8
- for 1/N-mode: x1/1024.

### selector

The selector is optional and not used in these examples.

It allows to assign the same state character to different tester waveforms (waveform sequences) with the same x-mode. In this case the two waveforms (waveform sequences) are uniquely identified by the selector. This is required for a unique translation of state characters to indexes and vice versa.

### Examples（取自子主题 Pattern Editor › Pattern Editor tasks › Creating a Digital Source setup）

### Digital Source setup of audio device

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/112906.htm`
> 中**第 4 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 1 列，含 colspan。

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/112906.htm`
> 中**第 3 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 1 列，含 colspan。

 !`Data frame format of audio device`（raw: `../../../../raw/22434.png`）

Setup in the Setup Wizard
 |

Create source port and new data container

 |
 |

Data Container

 |

New DSRC label

 |
 |

Pins

 |

datain

 |
 |

Matching port

 |

dataport

 |
 |

Offset

 |

0

 |
 |

Number of frames

 |

256

 |

 |

Create new configuration

 |
 |

Configuration

 |

audio_vvc

 |
 |

Type

 |

Serial

 |
 |

Option

 |

MSB first

 |
 |

Variable(width)

 |

VVLeft(8)

VVRight(8)

 |
 |

Map "0" to

 |

d0

 |
 |

Map "1" to

 |

d1

 |

After you finish, the Digital Source setup `audio_vcc` appears in the Outline view. Open it, the VVC `audio_vvc` is shown as the following:

```
ATTR DIGDATA #Source type

#Declaration of variables
VARIABLES VVLeft,VVRight

PINS datain
SOURCE_DATA_TEMPLATE VVLeft[7-0],VVRight[7-0]
MAPPING
0 d0
1 d1
```

According to the frame structure, you need use semicolon in the `SOURCE_DATA_TEMPLATE` section. You can open the Digital Source setup in the Outline view and edit it as the following:

```
SOURCE_DATA_TEMPLATE L[7-0];R[7-0]
```

The semicolon means only the bits of frame section #2 and #4 included in the source memory, and the bits of frame section #3 not included.

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/112906.htm`
> 中**第 6 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 1 列，含 colspan。

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/112906.htm`
> 中**第 5 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 1 列，含 colspan。

### VVC of video device

 !`Data frame format of video device`（raw: `../../../../raw/112781.png`）

Setup in the Setup Wizard
 |

Create source port and new data container

 |
 |

Data Container

 |

New DSRC label

 |
 |

Pins

 |

R_In

G_In

B_In

 |
 |

Matching port

 |

dataport

 |
 |

Offset

 |

0

 |
 |

Number of frames

 |

256

 |

 |

Create new configuration

 |
 |

Configuration

 |

video_vvc

 |
 |

Type

 |

Parallel

 |
 |

Option

 |

MSB first

 |
 |

Variable(width)

 |

VV_Red(8)

VV_Green(8)

VV_Blue(8)

 |
 |

Map "0" to

 |

d0

 |
 |

Map "1" to

 |

d1

 |

After you finish, the Digital Source setup `video_vcc` appears in the Outline view. Open it, the VVC `video_vcc` is shown as the following:

```
ATTR DIGDATA #Source type

#Declaration of variables
VARIABLES VV_Red,VV_Green,VV_Blue

PINS R_In
SOURCE_DATA_TEMPLATE VV_Red[7-0]
MAPPING
0 d0
1 d1

PINS G_In
SOURCE_DATA_TEMPLATE VV_Green[7-0]
MAPPING
0 d0
1 d1

PINS B_In
SOURCE_DATA_TEMPLATE VV_Blue[7-0]
MAPPING
0 d0
1 d1
```

### VVC of parallel audio device

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/112906.htm`
> 中**第 7 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 1 列，含 colspan。

 !`Data frame format of parallel audio device`（raw: `../../../../raw/112784.png`）

Setup in the Setup Wizard
 |

Create new data container and pin configuration

 |
 |

Data Container

 |

Re-use DSRC label

 |
 |

Pins

 |

R_In

G_In

B_In

 |
 |

Matching port

 |

dataport

 |
 |

Offset

 |

0

 |
 |

Number of frames

 |

256

 |

 |

Create new configuration

 |
 |

Configuration

 |

p_audio_vvc

 |
 |

Type

 |

Custom (from Template)

 |

If you want to use two variables, you cannot set the parameters in the Setup Wizard and then automatically create the VVC. The reason is that the number of variables does not match the number of source pins. You must directly enter the VVC in the editor which is launched by clicking the Custom (from Template) button on the Type panel. The VVC `p_audio_vvc` is shown as the following:

```
ATTR DIGDATA #Source type

#Declaration of variables
VARIABLES Left_VV,Right_VV

PINS datain_7
SOURCE_DATA_TEMPLATE Left_VV[7];Right_VV[7]
MAPPING
0 d0
1 d1

PINS datain_6
SOURCE_DATA_TEMPLATE Left_VV[6];Right_VV[6]
MAPPING
0 d0
1 d1

PINS datain_5
SOURCE_DATA_TEMPLATE Left_VV[5];Right_VV[5]
MAPPING
0 d0
1 d1

PINS datain_4
SOURCE_DATA_TEMPLATE Left_VV[4];Right_VV[4]
MAPPING
0 d0
1 d1

PINS datain_3
SOURCE_DATA_TEMPLATE Left_VV[3];Right_VV[3]
MAPPING
0 d0
1 d1

PINS datain_2
SOURCE_DATA_TEMPLATE Left_VV[2];Right_VV[2]
MAPPING
0 d0
1 d1

PINS datain_1
SOURCE_DATA_TEMPLATE Left_VV[1];Right_VV[1]
MAPPING
0 d0
1 d1

PINS datain_0
SOURCE_DATA_TEMPLATE Left_VV[0];Right_VV[0]
MAPPING
0 d0
1 d1
```

### Example（取自子主题 Pattern Reference Information › Wavetables › Function of the base wavetable）

In the example described here a setup is used, which consists of the pattern` func_first` and the wavetable `gross_func_devcyc_wtb` used as base wavetable.``

When you open the pattern `func_first` with the Pattern Editor, the following actions are performed by the Pattern Debug Tool:

- It checks, which base wavetable is assigned to the pattern `func_first`. The wavetable `gross_func_devcyc_wtb` is assigned.
- It reads the memory
- It reads the physical waveform DC/DC power units of the pattern `func_first` from the vector areas of the channels that are associated with a configured pin. A vector area is part of the tester channel memory.
- It translates the physical waveform DC/DC power units stored in the vector area into device cycle names. Therefore the wavetable `gross_func_devcyc_wtb` is used.
- It displays the device cycle names in the Pattern Editor.
 !`Translating physical waveform DC/DC power units into device cycle names`（raw: `../../../../raw/107914.png`）

When you change a cell in the Pattern Editor, the following actions are performed by the Pattern Debug Tool:

- It checks, which base wavetable is assigned to the pattern `func_first`. The wavetable `gross_func_devcyc_wtb` is assigned.
- It translates the changed device cycle names into physical waveform DC/DC power units. Therefore the wavetable `gross_func_devcyc_wtb` is used.
- It writes the physical waveform DC/DC power units to the vector area of the pin I/O0. The vector area of each tester channel stores the physical waveform DC/DC power units. !`Translating device cycle names into physical waveform DC/DC power units`（raw: `../../../../raw/107913.png`）

<!-- 语法节 end -->

## 是什么

**Pattern Tools 不是一个工具，是三个编辑器的合称：Pattern Explorer、Pattern Editor、
Multiport Burst Editor。** 原文首两句逐字（**第二句以 `are` 结尾、后面直接接三项列表，
没有冒号也没有句号**，见 `## 出处` ①）：

> 「The pattern tools are used to create, edit, and debug patterns and bursts. The pattern tools are」

**所以它们的共同职责是一句话**：`create, edit, and debug patterns and bursts`
——**建、改、查错，宾语是 pattern 与 burst 两样。**

### 三个工具各干什么（原文逐条）

| 工具 | 干什么（原文四条 bullet） |
|---|---|
| **Pattern Explorer** | `Explore patterns contained in the loaded setup` / `Create and delete patterns, port bursts, and multiport bursts.` / `Edit bursts` / **`Start the Pattern Editor and the Multiport Burst Editor`** |
| **Pattern Editor** | `Display the patterns of the loaded setup` / `Edit patterns` / `Analyze errors` |
| **Multiport Burst Editor** | `Create and display port bursts` / `Edit port bursts on both individual pages and the Overview page` / `Display the timeline synchronization of multiport port bursts per sync group` / `Analyze errors` |

**三条从这张表直接读出来的分工**：

**① Explorer 是入口。** 只有它写着 `Start the Pattern Editor and the Multiport Burst Editor`
——**另外两个编辑器是从它这里启动的**（这也是它在 `Subtopics` 里排第一个的原因）。

**② 只有 Explorer 有删的权力。** `Create and delete patterns, port bursts, and multiport
bursts.` **是三个工具里唯一出现 `delete` 的一条**——**Editor 与 Multiport Burst Editor
两条清单里都只有 `Edit` / `Display` / `Analyze`。**

**③ `Analyze errors` 两条 list 里都有。** Pattern Editor 与 Multiport Burst Editor
**各自都写了这一条**——**分析错误是两个编辑器共有的功能，不是某一个独有的。**

**（推断）port burst 与 multiport burst 的建 / 删在 Explorer、改在 Multiport Burst Editor**
——依据是 Explorer 那四条里 `Create and delete patterns, port bursts, and multiport bursts.`
与 Multiport Burst Editor 那四条里 `Edit port bursts on both individual pages and the
Overview page` **合起来正好是一套「建删在一处、改在另一处」**；
**原文没有一句话把这两条对上，所以这是推断。**

### 一个计数问题：`Subtopics` 四个，正文说「工具」三个

**这是本篇最要紧的一处结构事实**：

- `Subtopics` 列**四个**：`Pattern Explorer` / `Pattern Editor` / `Multiport Burst Editor` /
  `Pattern Reference Information`（raw 路径 `02.08.04.16.04_Pattern_Reference_Information.md`）。
- 正文 `The pattern tools are` 后面只列**三个**：`Pattern Explorer` / `Pattern Editor` /
  `Multiport Burst Editor`。

**`Pattern Reference Information` 在本篇里只出现一次**（就是 `Subtopics` 那一行，
本页查过：正文 0 处）——**它既没被叫「工具」，也没进那三项。**
**原文没有解释它算不算工具。本页并列两处，不替它归类**（见 `## 出处` ②）。

### 三条 Note：`500,000`、Klipper、F330

**本篇正文没有 `## Procedure`，也没有小节标题**（除 `## Related information` 与
`## Functional changes`）——**三条 `Note` 就是全部的正文补充**。

**① 一条硬数字：Pattern Editor 打不开超过 50 万条指令的 pattern。** 逐字：

> 「Note Patterns containing more than 500,000 instructions cannot be opened in the Pattern Editor.」

**`more than 500,000 instructions` 就打不开**——**原文没有说替代路径**，
**也没有说 Multiport Burst Editor 有没有同样的限制**（那一条 Note 挂在 Pattern Editor 那组
bullet 后面，见下「结构」）。

**② Klipper 会干扰复制粘贴。** 逐字：

> 「Note How to disable Klipper. Klipper - a clipboard utility for the KDE interface - causes
> problems when working with the SmarTest work center and the pattern debug tool. To avoid copy
> and paste problems, we strongly recommend to switch off Klipper. The steps may vary:」

**原文对 Klipper 的定义只有一处同位语**：`a clipboard utility for the KDE interface`，
**它引起的两处麻烦是** `the SmarTest work center` 与 `the pattern debug tool`，
**处置是建议性的**：`we strongly recommend to switch off Klipper`
（**`strongly recommend`，不是 must**）。**原文给的两步分支是**：

| 分支（原文） | 步骤（原文 bullet） |
|---|---|
| `If installed as application:` | `On the task-bar, right-click the` ＋ 图标链接 ＋ `Klipper icon.` → `Select Quit. The Automatically Start Klipper? dialog box is displayed.` → `In the dialog box click Do Not Start.` |
| `If installed as applet:` | `On the task bar, to open the panel menu, for example, right-click the` ＋ 图标链接 ＋ `Panel button.` → `Select Remove from Panel > Applet > Klipper.` |

**两个分支都没有说是什么操作系统**——**正文只说 Klipper 是 `for the KDE interface`**
（**KDE 是 Linux 桌面环境，但原文没有写出平台名**，见 `## 出处` ⑧）。

**③ F330 scan：三个 Eclipse 工具都不支持。** 逐字：

> 「Note F330 Scan is obsolete since release 7.0.1. Therefore, the Eclipse-based pattern tools do
> not support F330 scan patterns. When trying to load an F330 scan pattern, you will get error
> messages like "Unsupported pattern type" and "WARNING: FW mnemonic [SCAN] not supported for
> label type". To view and edit an F330 scan pattern, you must load it in a SmarTest version
> prior to 6.5.2, which supports the previous legacy pattern debug tool.」

| 项 | 原文 |
|---|---|
| 状态 | `F330 Scan is obsolete since release 7.0.1` |
| 后果 | `the Eclipse-based pattern tools do not support F330 scan patterns` |
| 报错原文 | `"Unsupported pattern type"` 与 `"WARNING: FW mnemonic [SCAN] not supported for label type"` |
| 唯一出路 | `you must load it in a SmarTest version prior to 6.5.2, which supports the previous legacy pattern debug tool` |

**两个要点：**

- **`Eclipse-based pattern tools` 这个说法在本篇只出现这一次**——**它是三个工具的统称，
  原文用它在说「这一整代工具都不支持 F330 scan」。**
- **`the previous legacy pattern debug tool` 是那个替代工具的全部名字**——
  **原文没给它正式名称，也没说它在哪个版本里被取代**（见 `## 出处` ④ ⑤）。

### 结构上最要紧的一处：两条 Note 挂在 Multiport Burst Editor 的清单底下

**Klipper 与 F330 这两条 Note 在 raw 里都接在 `The Multiport Burst Editor is used to:` 的
四条 bullet 之后**，**而两条的内容都不是讲 Multiport Burst Editor 的**：
Klipper 讲剪贴板工具，**F330 讲的是 `the Eclipse-based pattern tools`（三个工具的统称）**。
**原文没有把这两条分成小节、也没有给它们独立标题**——**它们只是 `Note` 开头的段落**
（在 raw 里还带着列表续行的行首空格，见 `## 出处` ③）。

**结果**：读这一篇的人若按标题找「Klipper 在哪一节」，**在结构上是找不到的**
——**它唯一的位置就是 Multiport Burst Editor 那组 bullet 的末尾。本页照实说，不替它搬家。**

### `## Related information` 与 `Subtopics` 不是一套

| 出处 | 列了哪些名字 |
|---|---|
| `Subtopics` | Pattern Explorer / Pattern Editor / Multiport Burst Editor / **Pattern Reference Information** |
| `## Related information` | Pattern Explorer / Pattern Editor / Multiport Burst Editor / **`Definitions: Vector, Pattern, Burst, etc. ...`** |

**两个清单前三个一样、第四个不同**：`Subtopics` 给的是**子文档**，
`Related information` 给的是**相关引用**——**本篇正文没有解释这个差别**
（**（推断）**：`Subtopics` 是语料模板给的父子关系，`Related information` 是作者写的相关链接；
**依据只是两处第四个名字不同，原文没有一句话说明它们各自的含义**）。

## 典型用法

**原文没有 `## Procedure`、没有 `## Before you begin`、也没有 `## Example`。**
全篇是**三份用途清单 + 三条 Note**。**所以本节不是原文给的步骤，而是「从原文能落成的动作」。**

| 要做的 | 用哪个工具（**依据：原文那四条 bullet**） |
|---|---|
| **看载入的 setup 里有哪些 pattern** | Pattern Explorer：`Explore patterns contained in the loaded setup` |
| **建 / 删 pattern、port burst、multiport burst** | Pattern Explorer：`Create and delete patterns, port bursts, and multiport bursts.` |
| **改 burst** | Pattern Explorer：`Edit bursts` |
| **打开 Pattern Editor 或 Multiport Burst Editor** | Pattern Explorer：`Start the Pattern Editor and the Multiport Burst Editor` |
| **显示 / 改 pattern** | Pattern Editor：`Display the patterns of the loaded setup` / `Edit patterns` |
| **分析错误** | **两个编辑器都行**：Pattern Editor 与 Multiport Burst Editor 各有一条 `Analyze errors` |
| **建 / 显示 port burst** | Multiport Burst Editor：`Create and display port bursts` |
| **改 port burst** | Multiport Burst Editor：`Edit port bursts on both individual pages and the Overview page` |
| **看多个 port burst 的时间线同步** | Multiport Burst Editor：`Display the timeline synchronization of multiport port bursts per sync group` |
| **开一个超过 50 万条指令的 pattern** | **打不开**——`cannot be opened in the Pattern Editor`；原文没给替代路径 |
| **用 F330 scan pattern** | **三个 Eclipse 工具都不支持**；只能退回 `a SmarTest version prior to 6.5.2` 用 legacy pattern debug tool |
| **在 Linux 上复制粘贴出问题** | 关掉 Klipper（`we strongly recommend to switch off Klipper`） |

**顺序上原文只给了一条入口链**：**Pattern Explorer → Pattern Editor / Multiport Burst
Editor**（`Start the Pattern Editor and the Multiport Burst Editor`）。
**其余九条之间没有先后关系，原文也没有排过顺序。**

**两条硬限制是本页最该记住的**（都在 Note 里，都不在工具清单里）：

- **`more than 500,000 instructions` → Pattern Editor 打不开**（**只说 Pattern Editor**）。
- **F330 scan pattern → 三个工具都不支持**，**唯一出路是版本回退**。

## 和谁有关

- [[pattern-explorer]] — **子主题，也是入口**。原文两处点它：`Subtopics` 第一个；
  正文里它独有 `Start the Pattern Editor and the Multiport Burst Editor`
  与 `Create and delete patterns, port bursts, and multiport bursts.`
  ——**另外两个编辑器由它启动，建删的权力也只有它有**。
  **本页只有这四条 bullet；它自己的界面、面板、菜单在那一页，本页没读。**
- [[pattern-editor]] — **子主题**。原文给它三条（显示 / 编辑 / 分析错误），
  **并附一条硬限制 `more than 500,000 instructions`**。
  **那页自己的界面与本页无关；本页的 50 万限制是从本篇 Note 抄的。**
- [[multiport-burst-editor]] — **子主题，也是本篇 `## Functional changes` 里唯一被点名的工具**
  （`SmarTest 7.1.3: Multiport Burst Editor added`）。**本页只有父页视角的四条 bullet
  ——窗口有几页、工具栏有哪几个图标，在那页；本批次读过那一篇，见 `## 版本`。**
- [[pattern]] — **三个工具的共同宾语**：`create, edit, and debug patterns and bursts`
  ——**pattern 是它们的操作对象**。**本页只有这一句；pattern 本身是什么、由什么构成，在那页。**
- `Pattern Reference Information`（**未建**）— **`Subtopics` 的第四个名字，
  正文一次都没提**（见 `## 出处` ②）。raw 路径
  `02.08.04.16.04_Pattern_Reference_Information.md`。**本页没读，所以它是不是「工具」本页判不了。**
- `Creating a multiport burst`（**未建**）— **本篇正文唯一一个 `see also`**：
  `The Multiport Burst Editor is used to: see also Creating a multiport burst.`
  **本篇把它挂在 `02.08.04.16.01.04`（Pattern Explorer 的号段）下**；
  **而 [[multiport-burst-editor]] 那篇的 `Subtopics` 把它挂在 `02.08.04.16.03.01` 下**
  ——**同名两路径**（见 `## 出处` ⑥）。**本页没读它。**
- `Definitions: Vector, Pattern, Burst, etc. ...`（**未建**）— **`## Related information`
  的第四个名字**。**本篇正文用了 `pattern` / `burst` / `port burst` / `multiport burst`
  四个词，一个定义都没给**——**那篇可能给定义，本页没有。**
- `Klipper`（**未建**）— **原文只说它是 `a clipboard utility for the KDE interface`**。
  **原文没说它是 SmarTest 的一部分，也没说它属于哪条产品线。**
- `the previous legacy pattern debug tool`（**未建，且原文没给名字**）— **F330 scan 那条
  Note 里唯一的出路**。**原文既没有它的正式名称，也没有它被取代的版本。**
- `SmarTest work center` / `the Automatically Start Klipper? dialog box` / `Panel button`
  （**均未建**）— **Klipper 那两步里点名的界面元素与宿主**，本页没读。

## 版本

原文 `## Functional changes` **两条**，逐字：

- Introduced before SmarTest 6.3.2
- SmarTest 7.1.3: Multiport Burst Editor added

**第一条是 §11.2 ② 那个哨兵。** `Introduced before SmarTest 6.3.2` 的意思是
**「早于语料覆盖范围」**，**不是「6.3.2 新增」**——
**所以 pattern tools 本身成立于哪个版本，这一篇里没有。**

**第二条只给三个工具里的一个记了变更**：`SmarTest 7.1.3: Multiport Burst Editor added`
——**Pattern Explorer 与 Pattern Editor 在这两条里都没有条目**，
**它们各自的变更史不在这一篇里。**

**一处对照**：[[multiport-burst-editor]] 那篇（本批次读过）的 `## Functional changes`
写的是 `Introduced in SmarTest 7.1.3` ——**同一件事、两种措辞**
（父页 `SmarTest 7.1.3: Multiport Burst Editor added` 对子页 `Introduced in SmarTest 7.1.3`）。
**那一条不在本篇 raw 里**，本页引它是为了说明两篇对得上，**不是本页的事实来源。**

**版本段里没有 F330 的条目**，**尽管正文那条 Note 点名了两个版本**：
`F330 Scan is obsolete since release 7.0.1` 与 `a SmarTest version prior to 6.5.2`
（见 `## 出处` ④）——**这两个版本号在本篇的 `## Functional changes` 里一个字都没有。**

**与 wiki 目标版本的关系**：本 wiki 面向 **SmarTest 7.10.3**，
**而本篇最后一条是 7.1.3**——**7.1.3 到 7.10.3 之间这三个工具有没有变，
本篇没有任何条目。** 正文里那条 F330 限制是**按 7.0.1 与 6.5.2 说的**，
**在 7.10.3 上是否仍然如此，本篇没有依据。**

详见 [[smartest-6.3.2]] / [[smartest-7.1.3]]。

## 出处

`sources:` 一篇：
`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16_Pattern_Tools.md`

**本页没做的：**

- **`Subtopics` 的三篇子文档本页都没读**（[[pattern-explorer]] / [[pattern-editor]] /
  [[multiport-burst-editor]]）——**所以三个工具各自长什么样、怎么点、有哪些面板与图标，
  本页一个字都没有；本页只有父页给出的三份用途清单。**
  其中 [[multiport-burst-editor]] 那一篇**在同一批次里另按工作单读过**，
  **本页只用它校了 `## Functional changes` 里的一条（已在正文注明是别篇的），
  没有把那一篇的窗口结构、图标写进本页。**
- **`Pattern Reference Information` 没读** —— 第四个 `Subtopics`，
  **所以「它是不是工具」本页判不了**（见 ②）。
- **一张图都没看。** 原文只有一张图 `raw/99506.png`（图名 `Pattern tools overview`）。
  **§11.4 说 raw 里的图可读、且该读，本页没读**——
  **所以三个工具在界面上摆在哪、那张概览图画了什么，本页不描述。**
- **`Creating a multiport burst` 没读** —— 它在本篇里只出现在一个 `see also` 里。
- **`Definitions: Vector, Pattern, Burst, etc. ...` 没读** ——
  **本篇正文的四个核心名词（pattern / burst / port burst / multiport burst）一个定义都没有**，
  **定义可能在那一篇，本页给不出。**
- **`Klipper` / `the previous legacy pattern debug tool` / `SmarTest work center`
  都没读**（前两个原文也没给正式名字）。
- **没有打开过这三个工具，也没有实机验证。** `verified: doc-only`——
  **50 万条指令那条限制在实机上怎么表现（是拒绝打开还是卡住），本页只有文档依据。**
- **除了 `## 版本` 里明写的那一处对照，本页没有交叉验证任何别处的文档**（§11）。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> **① 正文那句以 `are` 结尾，列表前没有冒号。** 逐字：
> `The pattern tools are used to create, edit, and debug patterns and bursts. The pattern tools are`
> ——**第二句 `The pattern tools are` 后面就是空行与三项 bullet，没有冒号、也没有句号。**
> **对照同篇后三处都是带冒号的**：`The Pattern Explorer is used to:` /
> `The Pattern Editor is used to:` / `The Multiport Burst Editor is used to:`
> ——**只有开头这一句没有。本页引文照原样。**
>
> **② `Subtopics` 四个、正文「工具」三个，数字不一致。** 逐字两处：
> `- [Pattern Reference Information](<02.08.04.16.04_Pattern_Reference_Information.md>)`
> 与
> ```
> - Pattern Explorer
> - Pattern Editor
> - Multiport Burst Editor
> ```
> ——**`Pattern Reference Information` 在本篇里只出现这一处**（本页查过：正文 0 处）。
> **原文没有解释它算不算工具。本页并列两处，不替它归类。**
>
> **③ 三条 `Note` 行首都带一个空格，其中一条还与列表末项粘在一起。** 逐字（**注意每行
> 开头的空格**）：
> ` Note Patterns containing more than 500,000 instructions cannot be opened in the Pattern Editor.`
> ` Note How to disable Klipper. Klipper - a clipboard utility for the KDE interface - causes problems when working with the SmarTest work center and the pattern debug tool.`
> `  - Select Remove from Panel > Applet > Klipper.Note F330 Scan is obsolete since release 7.0.1.`
> ——**三条 Note 都在列表项的续行位置（行首一个空格，`Select Remove from Panel > Applet > Klipper.` 那条是两个空格），
> 所以它们在 markdown 里属于前一个列表项**。
> **Klipper 最后一步与 F330 那条之间没有任何分隔符**：`Klipper.` 后面直接跟 `Note F330 Scan`，
> **没有空格、没有换行、没有句号**。
> **`Note` 后面也一律没有冒号或分隔符**，直接跟正文。
> （[[dscp]] 那页记过「`Note` 行首多一个空格」——**本篇同形**；
> 而 [[multiport-burst-editor]] 那篇**没有 `Note` 行首空格的问题**，两篇形态不同。）
>
> **④ 同一个 `Creating a multiport burst` 在两篇 raw 里挂两个不同路径。** 逐字（本篇）：
> `The Multiport Burst Editor is used to: see also [Creating a multiport burst](<02.08.04.16.01.04_Creating_a_multiport_burst.md>).`
> ——**本篇把它挂在 `02.08.04.16.01.04`（Pattern Explorer 的号段）下**；
> **[[multiport-burst-editor]] 那篇的 `Subtopics` 把它挂在 `02.08.04.16.03.01`
> （Multiport Burst Editor 的号段）下。两条 raw 本批次都读过，同名两路径。**
> **§10 说不要自行选一个当正确答案——本页并列，不判哪个对。**
> **（这两条链接是不是同一篇文档、抓取时哪一篇在那两处路径上，本页都没有依据。）**
>
> **⑤ F330 那条 Note 里两个版本号对不齐。** 逐字两句：
> `Note F330 Scan is obsolete since release 7.0.1.`
> 与
> `To view and edit an F330 scan pattern, you must load it in a SmarTest version prior to 6.5.2, which supports the previous legacy pattern debug tool.`
> ——**一句说「自 7.0.1 起过时」，另一句说「要退回 6.5.2 之前」。**
> **两个阈值之间（6.5.2 到 7.0.1）能不能用，原文没说。
> 本页并列两句、不替它对账**，也**没有替它去别处找答案**。
>
> **⑥ `see also` 被塞在冒号与列表之间。** 逐字：
> `The Multiport Burst Editor is used to: see also [Creating a multiport burst](<02.08.04.16.01.04_Creating_a_multiport_burst.md>).`
> ——**`is used to:` 后面紧跟 `see also` 加一个链接再加句号，之后才是四条 bullet**，
> **所以那个 `see also` 在语法上属于上一句，在语义上属于整节。本页照录。**
>
> **⑦ 那张概览图缩进挂在第三条 bullet 底下。** 逐字：
> ```
> - Multiport Burst Editor
>   ![Pattern tools overview](<../../../../raw/99506.png>)
> ```
> ——**图缩进两格挂在 `Multiport Burst Editor` 这一项下面**，
> **而图名是 `Pattern tools overview`（三个工具的概览）**。
> **本页照录，不替它把图提到列表之外。**
>
> **⑧ Klipper 那两步只给分支条件、不给平台名。** 逐字：
> `The steps may vary:` 后接 `If installed as application:` 与 `If installed as applet:`
> ——**两个分支都没有说是什么操作系统**，**正文只说它是 `a clipboard utility for the KDE
> interface`。本页不替它补平台名。**
>
> **⑨ `## Related information` 的链接首尾相接。** 逐字：
> ```
> [Pattern Explorer](<02.08.04.16.01_Pattern_Explorer.md>)[Pattern Editor](<02.08.04.16.02_Pattern_Editor.md>)[Multiport Burst Editor](<02.08.04.16.03_Multiport_Burst_Editor.md>)[Definitions: Vector, Pattern, Burst, etc. ...](<02.08.04.16.04.01_Definitions__Vector__Pattern__Burst__etc.md>)
> ```
> ——**四个链接之间没有逗号、没有空格**（[[dscp]] 那篇是两个、
> [[multiport-burst-editor]] 那篇是五个，**同一形态、数量不同**）。
>
> **⑩ 本篇没有 §11.2 ① 那种编码损坏。** **本页通读过这一篇，`[一-鿿]` 字符 0 处。**

`verified: doc-only`
