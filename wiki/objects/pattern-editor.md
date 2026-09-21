---
type: object
title: Pattern Editor
layer: gui
stage: pattern
tags: [pattern, pattern-editor, gui, collapsed-mode, expanded-mode, sequencer-instruction, x-mode, failure-data, status-line, zoom]
related: [pattern, pattern-explorer, multiport-burst-editor, pattern-master-file, vector-setup-file, wavetable, timing-file, sequencer, signal-analyzer, mapping-pattern, primary-status]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02_Pattern_Editor.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# Pattern Editor

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **10,758 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02_Pattern_Editor.md>` 及其子主题 `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.01_Collapsed_and_expanded_mode.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.02_Signal_and_pin_group_representations.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.03_Pattern_editor_properties_view.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.04.03_STATEMAP_section_of_the_wavetable.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.06.10.01_Inserting_counted_match_loops.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.06.16_Creating_a_Digital_Source_setup.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Collapsed and expanded mode）

The following two figures show the same pattern in collapsed mode and in expanded mode.

 !`Collapsed mode`（raw: `../../../../raw/101904.png`）

The pattern contains the sequencer instruction RPTV 3 2, which means the next three vectors are performed twice.

In the figure below, which shows the same pattern in expanded mode, you can see the resolved sequencer instruction and the Cycle# column.

 !`Expanded mode`（raw: `../../../../raw/101911.png`）

### Example（取自子主题 Signal and pin group representations）

The following figure shows the signals Pin 1, Pin 2 and Pin 3 in three different formats. The signal column headers contain the signal name (for example Pin 1) and the format (SC, DVC, PW).

 !`Pattern Editor showing xN example pattern`（raw: `../../../../raw/100465.png`）

### Examples（取自子主题 Pattern editor properties view）

### Vector properties

The graphic below shows the properties of a vector in device cycle (DVC) format.

 !`Device cycle properties view`（raw: `../../../../raw/129366.png`）

On vector properties views you cannot edit any parameters. Do this in the pattern editor.

The vector properties view always shows the physical waveform. Drive edges and receive edges appear on two different lines. In collapsed mode the view is based on the `base wavetable`（raw: `02.08.04.16.04.05.01_Function_of_the_base_wavetable.md`）, in expanded mode the properties are taken from the primary wavetable.

Any abbreviations you may use in your wavetables, are translated into the proper action code for `drive edges`（raw: `../02.06_Command_Reference/02.06.06.01.03.01.01.01_Drive_actions.md`） and `receive edges`（raw: `../02.06_Command_Reference/02.06.06.01.03.01.01.02_Receive_actions.md`）.

 |

Drive edges

 |

 |

 |

Receive edges

 |

 |
 |

Abbreviation

 |

Action code

 |

 |

Abbreviation

 |

Action code

 |
 |

0

 |

F00

 |

 |

L

 |

E0

 |
 |

1

 |

F10

 |

 |

H

 |

E1

 |
 |

!Z

 |

FN0

 |

 |

M

 |

EI

 |
 |

Z

 |

FNZ

 |

 |

U

 |

EU

 |
 |

. (period)

 |

N

 |

 |

X

 |

EX

 |
 |

 |

 |

 |

. (period)

 |

N

 |

### Test point properties

The graphic below shows the properties of a test point, in this case the highlighting of a force value in a dynamic DC test setup.

 !`Specifying the Force Value in the Properties view`（raw: `../../../../raw/113304.png`）

The properties view of a dynamic DC measure test point will also show the measure result. See below:

 !`Pattern editor properties view example`（raw: `../../../../raw/114630.png`）

### Vector variable properties

The properties view of a vector variable (see below) allows to edit for example, the assigned pins, the transfer mode, and other parameters. To display additional data upload formatting parameters (Upload Parameters) click the Show Advanced Properties icon. For a definition of the vector variable parameters see `Creating a Digital Capture setup`（raw: `02.08.01.02.07.02.05.01_Creating_a_Digital_Capture_setup.md`）.

 !`Vector variable properties view`（raw: `../../../../raw/116397.png`） Note The Upload Parameters shown here are the last which were used by the system. If you stop a testflow at a particular test suite and then open the pattern editor, the vector variable data is shown exactly as it was last uploaded from any test method or any command line operation.

### Examples（取自子主题 DUT oriented view - xN and x1 N mode › STATEMAP section of the wavetable）

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
- x1/N-mode: N hex numbers, comma separated, N 鈮?1024

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

### Example（取自子主题 Pattern Editor tasks › Inserting  editing  and deleting sequencer instructions › Inserting counted match loops）

Note that the compare event shown below in row 67, is supported by DPS128 only. In this example the Compare Type is set to High.

 !`Counted match loop in pattern editor`（raw: `../../../../raw/122707.png`）

### Examples（取自子主题 Pattern Editor tasks › Creating a Digital Source setup）

### Digital Source setup of audio device

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

<!-- 语法节 end -->

## 是什么

**Pattern Editor 是 pattern 的编辑器窗口。** 它把当前载入的 setup 里的 pattern 显示成
「信号列 × 向量行」的表格，让你在上面看向量、编辑向量、插删 sequencer instruction、分析失败数据。
`layer: gui` / `stage: pattern`——管的是 pattern 这一段**看得见、点得动的那一层**。

原文对自己能力的清单只有三行：

> 「With the Pattern Editor you can:」

| 原文条目 | 做什么 |
|---|---|
| `Display the patterns of the currently loaded setup` | 显示**当前载入的** setup 里的 pattern |
| `Edit the patterns` | 编辑这些 pattern |
| `Analyze errors` | 分析错误 |

**第三条后面直接挂着本页的主图**（原文写作 `- Analyze errors`，**后面紧跟着一个 `Pattern Editor overview` 的图片引用**）——
**这一篇没有 `## Example` 段**，全篇唯一一张整窗截图挂在这条能力上。
所以三条能力里**只有「分析错误」有配图**，另外两条各只有一行字。

### 两条模式：collapsed 与 expanded（**本页最要紧的一件事**）

折叠 / 展开那个图标的说明，把两条模式的差别一次说完了：

> 「Toggles between Collapsed and expanded mode. Only the current primary pattern (start label) can be viewed in expanded mode. Expanded mode shows the cycles as they are executed. Collapsed mode does not display the dynamic behavior of the sequencer instructions.」

四句话各管一件事：

| 原文句子 | 读出来的 |
|---|---|
| `Only the current primary pattern (start label) can be viewed in expanded mode.` | **expanded 一次只能看一个 pattern——当前 primary 那个**（原文把 primary 与 start label 当同一个东西说）。**别的 label 切不过去** |
| `Expanded mode shows the cycles as they are executed.` | expanded 显示的是**执行时真正发生的那些 cycle** |
| `Collapsed mode does not display the dynamic behavior of the sequencer instructions.` | collapsed **不显示** sequencer instruction 的动态行为 |

**把上面第一句和第三句并起来，实际后果是：要看清楚 sequencer instruction 让机器跑了几拍，必须进 expanded；而进 expanded 的前提是那个 pattern 正好是当前 primary。**
原文没有把这两件事连成一句话写，**这条因果是本页并出来的（推断），依据就是同一条图标说明里的两句话。**

`Enable expand selection mode` 那个图标是**展开功能里的一个例外**，而且**只在 burst 里有效**：

> 「Available only for bursts in pattern editor.」

它管的是**只展开选中的那些 `CALL` instruction**（转述：原文说 enabled 之后展开页里会多出
`Expand Selection Mode` 这一项）。**换句话说 expanded 的「展不展」在 burst 里可以逐条 `CALL` 挑**。

### 工具栏：16 个图标，分四组

原文在 `The toolbar of the Pattern Editor provides the following icons:` 底下给的表一共 16 行
（`99926` 那张图标被引用两次——它同时出现在 `Enable expand selection mode` 的说明里）。按它们管的事分组：

| 组 | 图标（原文 alt 文字） | 做什么 |
|---|---|---|
| **模式与选择** | `Expand/collapse button` | 切 collapsed / expanded（上面那段全在这条里） |
| | `Enable expand selection mode` | 只在 burst 里，挑着展开选中的 `CALL` |
| **失败数据分析** | `Refresh result display button` | 失败太多时注解数受限，**标一行再按它**，就在那一行周围生成注解 |
| | `Align display button` | 在 expanded 里显示失败数据时，**与别的结果分析工具对齐** |
| | `Next annotation button` / `Previous annotation button` | 跳到下 / 上一个注解 |
| **显示开关（5 个 toggle）** | `Hide all instructions in current editor button` | 开关**所有 header instruction** |
| | `Hide all vectors in current editor button` | 开关**所有向量** |
| | `Hide all formats in current editor button` | 开关**所有 x-mode area**（原文如此，见「出处」③） |
| | `Hide all protocols in current editor` | 开关**所有 protocol** |
| | `Hide all comments in current editor button` | 开关**所有 header comment** |
| **缩放与导航** | `Zoom in button` / `Zoom out button` | 放大 / 缩小（缩小的后果见下节） |
| | `Navigator view - back button` / `Navigator view - forward button` | 后退 / 前进 |
| | `Switch to horizontal pattern view button` | 切到**横向 pattern 视图** |

**注解那一条值得单独读一遍原文**——它是「为什么我按了按钮却只出来一部分注解」的答案：

> 「This button can be used when Displaying failure data in expanded mode (see Collapsed and expanded mode). If you have acquired a large number of failures, the number of annotations is limited. When you mark a line in Pattern Editor, you can generate the annotations around the marked line by pressing this button.」

**失败数据只在 expanded 里显示**（`in expanded mode`），而且**注解数量有上限**——
所以「注解不全」不是 bug，是原文写明的行为。

**工具栏与主菜单是两份入口，同一批功能**：

> 「Most of the functions you can also find in the main menu, for example Navigate > Next Annotation/Previous Annotation corresponds to theicons」

**这句里的 `theicons` 是原文自带的粘连**（原文这里紧跟着两个图标引用，中间没有空格），
照实引，**本页没替它补空格**（见「出处」①）。

### 状态行：在 SmarTest **主窗口**的底部

> 「The status line of the Pattern Editor is at the bottom of the SmarTest main window.」

**注意主语是「SmarTest 主窗口的底部」，不是「编辑器面板的底部」**——
它是全应用共享的那一条，不是编辑器自己的页脚。
**这一篇没有说状态行上显示什么**；图 `99923.png` 上那一格显示的是 `ADC_parallel`，
**与打开的编辑器页签同名**（图证见下）。
`## Related information` 把 `Editor status line` 单列成一篇，**那篇本页没读**——
**状态行里每一段各显示什么，本页一个字没有。**

### 缩小到一定程度会「吃掉」数据（原文自己单列了 `## Zooming out` 一节）

> 「Starting at a certain zoom-out level, the zooming combines multiple vector rows or cycle rows into a single row, and the vector/cycle-count numbering changes from continuous (1, 2, 3, 4, 5, ...) to discontinuous, for example 1, 3, 5,... or even to 1, 5, 9, .... The vector data (including error information) of the hidden vector/cycle rows disappear. To see them you have to zoom in again.」

拆成「条件 → 结果」：

| 条件 | 结果 |
|---|---|
| 缩到某个级别**之后** | 多个 vector 行 / cycle 行**被合并成一行** |
| 同上 | 行号**从连续变跳号**：`1, 2, 3, 4, 5, ...` → `1, 3, 5,...` → 甚至 `1, 5, 9, ....` |
| 同上 | **被隐藏那些行的向量数据（含错误信息）消失** |
| 想再看到 | **只能放大回去** |

**这一条的实际用法是一句警告：屏幕上「看得见的行」不等于「全部的行」。**
原文用的是 `disappear`，不是「变淡」或「折叠」。

### 图证：本页从 raw 的截图里读到的（④ 图证）

`../../../../raw/x.png` 往上四层正好是 `tdc-html/`，图就在 `tdc-html/raw/` 里（`schema.md` §11.4）。
**本页读了 4 张**，逐张说清它答了什么、哪些字在 raw 里 grep 不到：

| 图 | 出自 | 它答了什么 |
|---|---|---|
| `99923.png` | `02.08.04.16.02`（**本页 sources 唯一那篇**） | 整个 SmarTest 窗口的布局：菜单栏里有 `Pattern` 一项；红框 `Pattern Editor related icons` 指向工具栏中段的一小段按钮；红框 `Pattern Editor` 圈住信号/向量表；底部一条红框 `Status line` |
| `101904.png` | `02.08.04.16.02.01_Collapsed_and_expanded_mode` | **collapsed 长什么样** |
| `101911.png` | 同上 | **expanded 长什么样** |
| `100465.png` | `02.08.04.16.02.02_Signal_and_pin_group_representations` | **三种信号格式在表头里怎么并排** |

**（a）`99923.png` 回答了三件正文没写的事：**

- **状态行的内容**：图最底下那一格逐字是 `ADC_parallel`，而编辑器页签也是 `ADC_parallel`
  ——**状态行显示的是当前 pattern 的名字**。（**推断**：依据是两个同名字符串同屏出现；
  原文只写了它在哪，没写它显示什么。）
- **表的行头长什么样**：信号表左侧从上到下逐字是 `Signal`、`X-Mode Area`、`Protocol`，
  再往下是 `Vector#` / `Instruction` / `Comment` 三列的行。
  **`X-Mode Area` 与 `Protocol` 是两条独立的横带**——这正好对上工具栏那两个 toggle
  （`Hide all formats in current editor button` 那条管 x-mode area、`Hide all protocols in current editor` 那条管 protocol）。
- **信号列头带格式后缀**：逐字有 `CT1_DPM (SC)`、`CT2_DPM (SC)`、`DB01 (SC)` 等，
  末尾带括号里的格式码。

**grep 不到的字**：`ADC_parallel`（0 命中）、`CT1_DPM`（0 命中）、`DB01`（0 命中）。

**（b）`101904.png` / `101911.png` 是同一个 pattern 的同一段，两张并排就是 collapsed 与 expanded 的全部差别：**

| | `101904.png`（collapsed） | `101911.png`（expanded） |
|---|---|---|
| 行号列 | 只有 `Vector#` | **多一列 `Cycle#`**，排在 `Vector#` 左边 |
| instruction | `RPTV 3 2` 占**一整行**，另一行是 `REPEATED` | 拆成**两行**：`RPTV 3 1/2` 与 `RPTV 3 2/2` |
| 别的指令 | 这两行之外没看到第三条 | **`GENV 3`、`GENV 30`** 出现在 `Instruction` 列里 |

**「resolved」的实形就是这两张图的差**：一条 `RPTV 3 2` 在 expanded 里被摊成两趟，
趟号写成 `1/2` 与 `2/2`；多出来的 `Cycle#` 列，正是本页「语法 / 参数」节里
（取自子主题 `16.02.01`）那句 `you can see the resolved sequencer instruction and the Cycle# column`
指着的东西。**两张图的信号列头带的是 `(DC)` 后缀**（逐字如 `DS0 (DC)`、`I/O0 (DC)`、`_MR (DC)`）。

**grep 不到的字**：`RPTV 3 1/2`（0 命中）、`RPTV 3 2/2`（0 命中）、`GENV 30`（0 命中）、
`REPEATED`（0 命中）、`I/O0 (DC)`（0 命中）。`RPTV` 与 `(DC)` 各自能搜到，
**但搜到的是别处的正文，不是这两张图**。

**（c）`100465.png` 把三种信号格式的名字补全了。** 图上三个黄标签分别指向三列，
逐字是 `x-mode format`（指 `Pin 1 (SC)`）、`device cycle name format`（指 `Pin 1 (DVC)`）、
`physical waveform indices format`（指 `Pin 1 (PW)`）；列头逐字是
`Pin 1 (SC)` / `Pin 1 (DVC)` / `Pin 1 (PW)` / `Pin 2 (SC)` 等，三根 pin 各三列。
另外还有一个标签 `X-Mode Area line` 指向 `X-Mode Area` 那一行，那一行的每格填的是 `(x2)` / `(x1)` / `(x3)` / `(x4)` 这种 x-mode 值。

**三个格式码的展开只有图上齐**：本页「语法 / 参数」节里那段（取自子主题 `16.02.02`）
只写了 `the format (SC, DVC, PW)` 三个缩写，**没有展开**；
`SC = state character` 能在别处搜到，而 `device cycle name format`（0 命中）与
`physical waveform indices format`（0 命中）**只有这张图上写着**。

**（d）一处本页不判的差异，照实记：** `99923.png` 里那张 Pattern Explorer 表的列头是
`Name` / `Port` / `Type` / `Memory` / `WaveTable` / `Layout on Patt`（最后这一格被列宽截断），
而 [[mapping-pattern]] 里从 `99506.png` 读到的八列是
`Name` / `Port` / `Sync Group` / `Type` / `WaveTable` / `Memory` / `State` / `Location`。
**两张图不是同一套列**，本页**不判哪一套是现行版**（`Pattern Explorer` 自己那一页的版本记录里
有 `Additional columns: State and Location.` 一条，**本页只指路，不替它对号**）。

## 典型用法

**这一篇是参考页，不是步骤页**：它没有 `## Procedure`，也没有 `## Before you begin`。
所以下表每一条只能到「按哪个图标 / 在哪一条带」，**「先做什么、再做什么」本篇没有，本页也不替它编**。

| 想干什么 | 按什么 | 依据 |
|---|---|---|
| 看这个 pattern 执行时到底跑了几拍 | `Expand/collapse button` 切到 **expanded** | 文档事实 |
| 看别的 pattern 的展开视图 | **做不到**——expanded 只显示当前 primary pattern | 文档事实（`Only the current primary pattern (start label) can be viewed in expanded mode.`） |
| 在 burst 里只展开某几条 `CALL` | `Enable expand selection mode`（**只在 burst 里活**） | 文档事实 |
| 失败数据看不清、注解太少 | **先标一行**，再按 `Refresh result display button` | 文档事实 |
| 跳到下 / 上一个失败注解 | `Next annotation button` / `Previous annotation button`（或主菜单 `Navigate > Next Annotation` / `Previous Annotation`） | 文档事实 |
| 把注解位置和另一个结果工具对上 | `Align display button`（**要在 expanded 里显示失败数据时**） | 文档事实 |
| 表格太挤，把某几条带收起来 | 五个 `Hide all` 开头的 toggle（instruction / vector / format / protocol / comment） | 文档事实 |
| 换横向看 | `Switch to horizontal pattern view button` | 文档事实 |
| 看全貌 | 用 `Zoom out button`，**但缩过头会合并行、丢数据** | 文档事实 + 上面那张「条件 → 结果」表 |

**两条顺序上的提醒（推断，依据是上面引的那几句原文）：**

- **想分析失败数据，先切到 expanded。** 原文把 `Displaying failure data` 与 `in expanded mode`
  写在同一句里，注解跳转那两条也各带 `when displaying failure data in expanded mode`
  ——**失败分析这一整组按钮都挂在 expanded 上**。
- **想分析的是「当前 primary pattern」以外的东西，先解决 primary。** 因为 expanded 只认当前 primary
  （那一条 `Only the current primary pattern (start label) can be viewed in expanded mode.`）。**「怎么换 primary / start label」本页源文档一个字没写**，
  见「和谁有关」里 [[primary-status]] 那一条。

**本页答不了的用法问题**（一条也不替它编）：**instruction 有哪些、`RPTV` / `MACT` 各是什么语义**
——那些在本页的兄弟子主题 `16.02.06.10.02_Sequencer_instructions` 一线，**本页没读**；
**properties view 里能看什么、能不能改**——那在 `16.02.03`，**本页没读**（本页只知道自己「语法 / 参数」节里
脚本抄来的那几句）。

## 和谁有关

- [[mapping-pattern]] — **同阶段的对照表页，本页是它 GUI 列的一个来源。**
  三层（GUI / 文件 / L1）怎么对、**GUI 的 Instruction 列与 `SQPG` 的 `instr` 参数哪里不同**
  （`LOOP`/`LOOPEND`/`RETURN` 对 `LBGN`/`LEND`/`RSUB`、`GENV` 在 GUI 侧隐式那几条），
  **一律记在那一页**；那一页还把本页列为「Instruction 列」「counted match loop」「Digital Source」
  几行的 GUI 格来源之一。**本页的源文档对那套对照一个字都没写。**
- [[pattern-explorer]] — **同章兄弟，且与本页共用设置。** 原文 `## Related information` 第一个就是它；
  更硬的一条在它那篇里（`View Menu → Preferences` 打开的是**两者共用**的首选项对话框）。
  **分工**：它答「这套 setup 里有哪些 pattern」，本页答「pattern 里面长什么样」。
- [[multiport-burst-editor]] — **本页与它唯一的交叠在 burst 上**：`Enable expand selection mode`
  明写 `Available only for bursts in pattern editor`，并且管的是 `the selected CALL instructions
  in a burst (or port burst)`。**burst 本身怎么建、怎么组合，不在本页。**
- [[wavetable]] / [[timing-file]] — **collapsed 与 expanded 用的是两张不同的 wavetable。**
  这条不在本页源文档里，而在本页「语法 / 参数」节里脚本从 `16.02.03` 抄来的那句
  （`In collapsed mode the view is based on the base wavetable, in expanded mode the properties are taken from the primary wavetable.`）——**base 与 primary 的分工见 [[mapping-pattern]] 那一行**。
- [[primary-status]] — **expanded 只认「当前 primary pattern（start label）」，这是本页唯一提到 primary 的地方**；
  **「谁在改 primary、`start label` 怎么指定」本页源文档一个字没写。**
- [[signal-analyzer]] — 只在版本记录里出现一次：`SmarTest 7.0.3: New shortcut menu to edit vectors with Signal Analyzer.`
  ——**「用 Signal Analyzer 编向量」这条捷径长什么样，本页没有。**
- [[sequencer]] — **本页只用到「instruction 的动态行为」这一个概念**（collapsed 里看不到它）。
  **instruction 有哪些、各是什么语义，本页没有**，那在子主题 `16.02.06.10.02`。
- [[pattern-master-file]] / [[vector-setup-file]] — **本页的源文档一次都没提文件**。
  所以「在本页里改的东西落到哪个文件、要不要 pmfl 才能用」**本页答不了**——
  那是 [[pattern-explorer]] 与 [[mapping-pattern]] 的地盘。
- [[pattern]] / [[pattern-tool]] — **stage 页与父页**。pattern 定义侧（label 是什么、有哪些类型）
  在 [[pattern]] 那边；本页是 `02.08.04.16_Pattern_Tools` 下的子主题之一，**那一篇本页没读**。

## 版本

本文档**有** `## Functional changes` 段，4 条，逐条照录：

- `Introduced before SmarTest 6.3.2`
- `SmarTest 7.0.3: New shortcut menu to edit vectors with Signal Analyzer.`
- `SmarTest 7.1.3: Enhanced control of the editor data table.`
- `SmarTest 7.5.1: After a rerun of a test program, the existing positions of any open pattern editor are maintained.`

**第一条是哨兵值，不是「6.3.2 的变更」。** 按 `schema.md` §11.2②，
`Introduced before` 这一整类说法的意思是「**在本文档集覆盖范围开始之前就已经有了**」——
**照字面读会读成「6.3.2 新增了 Pattern Editor」，那是错的。**

剩下三条**全都落在「编辑器用起来怎么样」上**，没有一条是新增能力：

| 版本 | 原文条目 | 落在本页哪个位置 |
|---|---|---|
| 7.0.3 | `New shortcut menu to edit vectors with Signal Analyzer.` | 只有版本记录这一处；**正文与图标表里一个字都没有**（本页源文档里 `Signal Analyzer` 只出现这一次） |
| 7.1.3 | `Enhanced control of the editor data table.` | **语料未写「增强了什么」**——正文没有任何一处说明这一点 |
| 7.5.1 | `After a rerun of a test program, the existing positions of any open pattern editor are maintained.` | 同上，正文没写；**这一条讲的是重跑测试程序之后编辑器窗口的位置** |

**collapsed / expanded 模式、状态行、缩小合并行这三块，版本记录里一条也没有。**
`Introduced before SmarTest 6.3.2` 是哨兵值（§11.2②），**不能读成「6.3.2 新增」**——
所以**「这几样从哪个版本开始有」本页答不了**。

同批条目也收在 `wiki/versions/` 的 [[smartest-7.0.3]] / [[smartest-7.1.3]] / [[smartest-7.5.1]] 三页里
——**那三页不是本页建的**，这里只指路。

## 出处

- 定义文档（本页 `sources:` 唯一一篇，**整篇读过**）：
  `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02_Pattern_Editor.md`
  （TDC `99157.htm`，5,427 字节 / 137 行）。
- **本篇没有重复投放**：全语料按 `source_topic` 查 `99157.htm`，**只有这一个文件**。

### 本页「语法 / 参数」节的来源（**那一节不是本页写的，也不来自定义文档**）

- **定义文档里没有语法段标记**：它的 `##` 段只有 `## Zooming out`、`## Related information`、
  `## Functional changes`——没有 `Syntax` / `Parameters` / `Example` 这类段标记。
  **Pattern Editor 是 GUI 工具，这一篇本来就没有命令行语法可抽**，脚本不收是正确行为。
- 那一节的 **10,758 字符全部来自 6 个子主题**（来源写在段名里，脚本在节首自己声明了）：
  `16.02.01_Collapsed_and_expanded_mode`、`16.02.02_Signal_and_pin_group_representations`、
  `16.02.03_Pattern_editor_properties_view`、`16.02.04.03_STATEMAP_section_of_the_wavetable`、
  `16.02.06.10.01_Inserting_counted_match_loops`、`16.02.06.16_Creating_a_Digital_Source_setup`。
- **这 6 篇子主题本页一篇都没读。** 所以那一节里的两个 STATEMAP 例子与 `physSeq` / `statechars` /
  `x-mode` / `selector` 四栏、vector / test point / vector variable 三种 properties view、
  counted match loop 那张图、Digital Source setup 的 Setup Wizard 表与三段 VVC 代码，
  **本页正文一句都没有展开，也不该由本页负责**——它们属于那 6 篇子主题自己的页。

### 本页读的图（4 张）

- **sources 那篇引的图共 17 张，本页读了 1 张**：`99923.png`（正文主图）。
  **其余 16 张全是工具栏小图标**（`99926` / `129178` / `99927` / `99928` / `99929` / `99931` /
  `99932` / `99935` / `112654` / `99936` / `99937` / `99938` / `99939` / `99940` / `91706` / `91707`），
  **本页一张没看**——所以**这些图标长什么样，本页只知道名字**。
- **另读了 3 张本页「语法 / 参数」节里出现的图**：`101904.png`、`101911.png`、`100465.png`
  （各自出自哪个子主题见「图证」那张表）。**那 3 篇子主题文档本页没读，只读了它们自带的图。**
- **4 张都整张看完**，图上读到的字**逐条回 9,398 篇 raw md 里查过 grep 命中**——
  本页凡写「grep 不到」的都是实测 0 命中。

### 本页没做的

- **`Subtopics` 那一列 7 篇（以及它们各自的子主题）一篇没读**：`16.02.01`、`16.02.02`、`16.02.03`、
  `16.02.04_DUT_oriented_view_-_xN_and_x1_N_mode`、`16.02.05_Virtual_sequencer_instructions_for_protocol_patterns`、
  `16.02.06_Pattern_Editor_tasks`、`16.02.07_Pattern_Editor_quick_reference`。
  因此 instruction 全表、x-mode / x1/N 的用法、properties view 的字段、protocol pattern 的虚拟
  instruction、Digital Source / Digital Capture 的建法、Pattern Editor 的快捷参考，**本页一个字都没有**。
- **`## Related information` 指的两篇没读**：`Pattern Explorer`（`02.08.04.16.01`，[[pattern-explorer]]）
  与 `Editor status line`（`02.08.04.16.04.02`）——**状态行的每一段显示什么，本页不知道。**
- **16 张工具栏图标一张没看**（见上）。
- **没有实跑。** 没有在机台上开过 Pattern Editor、没有切过 collapsed / expanded、
  没有显示过任何失败数据。**`verified: doc-only` 指的就是这件事**——
  「这些图标在真机上点下去会怎样、哪些会变灰」本页一句都不能保证。
- **没有动 `wiki/index.md`**，也没有改别的页。

### ⚠️ 语料瑕疵（照实记，一处都没替它改）

**① 一处漏空格：`theicons`（第 120 行）。**

> 「Most of the functions you can also find in the main menu, for example Navigate > Next Annotation/Previous Annotation corresponds to theicons」

**`to theicons` 之间少一个空格**（原文在这后面紧跟着两个图标引用）。**本页没替它补。**

**② `## Related information` 两条链接之间没有任何分隔符（第 130 行）。**
原文是 `[Pattern Explorer]` 紧接着 `[Editor status line]`——**两个链接挨着，没有空格、逗号或换行**，
渲染出来会贴成一段。

**③ 同一张图标，alt 文字与它的说明写的不是一回事（第 74–76 行）。**
图片引用写作 `![Hide all formats in current editor button](<../../../../raw/99935.png>)`，
说明写的是 `Hides/shows (toggles) all x-mode areas in the current editor.`
——**alt 说 `formats`，说明说 `x-mode areas`**。
**原文如此，本页照录，不判哪个是笔误**（图 `99923.png` 上那条横带逐字是 `X-Mode Area`，
**这条只作旁证，不作判决**）。

**④ 一处语法错（第 61 行）。** 原文：

> 「Aligns the display with another result analysis tools, when displaying failure data in expanded mode.」

**`another result analysis tools` 里 `another`（单数）配 `tools`（复数），数不一致**。本页正文没有引用这一句。

**⑤ 一处数字写法不一致，照录不判（第 126 行，上面已整段引过）。**
同一段里三种省略号写法并存：`(1, 2, 3, 4, 5, ...)`、`1, 3, 5,...`、`1, 5, 9, ....`
——**逗号后的空格一处有一处没有**。**引文里原样保留。**

**⑥ 本页这一篇没有编码坏字（§11.2① 那一族）。** 用 `[一-鿿]` 实测零命中。
对照 §11.2① 的全语料 1,053 / 9,398 篇含坏字，**本篇属于没有的那一批**——
**这不是「没找到」，是查过、结果为零。**

**⑦ 本条不在本页 sources 里，记在这里只为一件事：别把坏串抄进代码块。**
§11.2⑤ 那个整词替换（`Index` → `DC/DC power units`）**本页 sources 零命中**，
但它出现在**本章兄弟文档** `02.08.04.16.02.04.04` 与 `02.08.04.16.02.06.18` 里：

> 「The state characters are displayed in the state character column (SC). The related device cycle names are displayed in the device cycle column (DC) and the related waveform DC/DC power units are displayed in the physical waveform column (PW).」

**`waveform DC/DC power units` 就是那个整词替换（原词是 `indices`）**。
那两篇**是同一个 TDC 页 `100341.htm` 的两次投放**（`100341.htm` 与 `100341_2.htm`，
判据同 `schema.md` §10），**各自含 5 处**这个串——所以这是**一页里的 5 处**，不是「两篇说法一致」。
**那两篇不在本页 sources，本页没读**；记这一笔的用处是：
**图 `100465.png` 上那张标签逐字是 `physical waveform indices format`——图比正文干净**，
**而 `DC/DC power units` 这个串不许抄进任何代码块。**

`verified: doc-only`
