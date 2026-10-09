---
type: object
title: Sharing configuration file
layer: file
stage: pin
tags: [pin, sharing, file-format, mtp, dps, fixture-delay]
related: [pin, sharing-configuration, shared-continuity-test, shared-leakage-parallel-test, utility-line-assignments]
sources:
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.07.02_Sharing_configuration_file.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# Sharing configuration file

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **9,403 字符逐字取自** `<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.07.02_Sharing_configuration_file.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

The format of the sharing configuration file, using the keywords described below:

```
pin_configuration:
<pin config file name><context>

fixture_delay_files:
[+<baseboard fixture delay file>]
<fixture delay file> # position x=0,y=0
<fixture delay file> # position x=1,y=0
...
[; # starts next increment of y value
<fixture delay file> # position x=0,y=1
<fixture delay file> # position x=1,y=1
...]
...

domains:
<site number><site number> ...[; <site number><site number> ... ] ... # for z=0
... # for increments of z

[utility_control:
<name>[; (<equation>)] ; (<utility setting>) [; (<pin substitution>)]
...]

topology:
<topo definition> ; <pin group>
...

[fxdl_ignore_pins:
<pin>[, <pin>...] ]

[groups:
<pins or channels> ; offset=<group offset>
...]

[rss_buffer_pins:
<site no>; [<tmp src buffer>], <source buffer>, <global buffer 1>, <global buffer 2> [; ...]
...]
```

Note that # indicates comments that are not part of the syntax but serve to explain the semantics.

Keywords
 |

 |

Field

 |

Type

 |

Description

 |
 |

pin_configuration

 |

<pin config file>

 |

String

 |

Name of the V93000 pin configuration file used to calculate fixture delay.

This pin configuration file is normally identical to the standard pin configuration file. You must, however, remove all shared pins from it that are not part of the daisy chain.

 |
 |

<context>

 |

String

 |

The context name in the pin configuration file, for example FAST.

 |
 |

fixture_delay_files

 |

<baseboard fixture delay file>

 |

String

 |

The name of the fixture delay file for the baseboard.

The fixture delays in this file must be measured between lower pogo and upper pogo.

This is an optional parameter. It must be prefixed with a plus sign (+).

 |
 |

 |

<fixture delay file>

 |

String

 |

Fixture delay file names, separated by line breaks.

If a baseboard fixture delay file has been specified (see above), the measurements in these files must be from upper pogo to socket pin. If there is no baseboard file, the measurements in these files must be from lower pogo to socket pin.

There must be one file for each device. Files must be listed in the order of the devices - first the file for the device at the x0,y0 location, then for x1,y0, then x2,y0 etc. When files for all devices with a y0 coordinate have been listed, add a semicolon and list all devices with a y1 coordinate (x0,y1 x1y1, ...), then for y2 and so on.

For information on determining the coordinates of a device, see `Identifying sites`（raw: `02.12.02.05.06.07.07.04_Identifying_sites.md`）.

 |
 |

domains

 |

<site number>

 |

Integer

 |

A site number.

- The domains keyword is followed by the sites each pin drives.:

Sites for one pin must be listed on one line in the order of the signal propagation.

- Different Y-branches driven by the same pin are separated by semicolons.
- Sites are numbered according to their coordinates: x0,y0 is numbered 1, x1,y1 is numbered 2, and so on.

For information on determining the coordinates of a device, see `Identifying sites`（raw: `02.12.02.05.06.07.07.04_Identifying_sites.md`）.

 |
 |

utility_control

 |

<name>

 |

String

 |

The entire utility control block is required only for DPS shared load boards and can otherwise be omitted.

Each entry in this section specifies the utility line settings to apply before a particular test method is executed.

<name> is the name of a utility control.

Different test methods may use different names. The name "default" is used by all test methods to specify the default utility line settings.

For details, see the description of the test method you will be using.

 |
 |

 |

<equation>

 |

String

 |

This is an optional parameter.

It specifies a condition that must be true in order to apply the action described in that line.

Conditions can include values and operators.

Supported values are:

- Decimal numbers (for example, 123)
- Hexadecimal numbers (for example, 0xff)
- The variables x and y. They evaluate to the respective coordinate of a site. For example, `x < 5` is true for all sites with an x-coordinate from 0 to 4.

For information on determining the coordinates of a device, see `Identifying sites`（raw: `02.12.02.05.06.07.07.04_Identifying_sites.md`）.

Supported operators include:

- ==
- <
- <=
- >
- >=
- &&
- | |

Four forms of equations are supported:

- <value><op><value>. For example: `x > 2`
- <value><op><value><op><value>. For example: `0x77 < x <= 0xff`
- (<value><op><value>) <op> (<value><op><value>). For example: `(x < 5) && (y > 2)`
 |
 |

 |

<utility setting>

 |

String

 |

The utility setting is a list of comma-separated commands that are executed when the equation evaluates to true. If there is no equation, the commands are always executed.

Parameters can be specified with or without a mask:

- Without mask: For example, `U5=0x400`. A mask of 0xffff in implicitly applied.
- With a mask: For example, `U5=0x400&0xf00`.
 |
 |

 |

<pin substitution>

 |

String

 |

A comma-separated list of assignments of device pin names to pin aliases from the test method. For example: `DEVICE_SUPPLY=VDD`

Which pin aliases are available (here: DEVICE_SUPPLY) depends on the test method.

 |
 |

topology

 |

<topo definition>

 |

String

 |

A specification of the sharing topology used.

Topology definitions have three elements:

- `x=`n, where n is the x-dimension of the sharing setup.
- `y=`n, where n is the y-dimension.
- The type of termination:

  - noterm: no termination
  - cross: cross-termination
  - actterm`=`<pin>: active termination, where <pin> is the termination pin

 |
 |

 |

<pin group>

 |

String

 |

The pin group in which the pins have this topology.

 |
 |

fxdl_ignore_pins

 |

<pin>

 |

String

 |

A pin that will be ignored by fd_merge.pl and OnlineCompensation.

In other words, these tools will not calculate additional compensation for the pin.

You can specify multiple pins; separate them by commas.

 |
 |

groups

 |

<pins or channels>

 |

String

 |

A specification either of one or more tester channels or of one or more pins or pin groups to which the offset is applied.

You can specify:

- A single tester channel. For example: `22601`
- Multiple tester channels separated by commas. For example: `22601, 22603, 22605`
- A range of tester channels indicated by a dash. For example: `22601-22604`
- A pin or pin group. For example: `A1`
- Multiple pins or pin groups. For example: `A1, A3, DQo`

Channels, pins and pin groups can be mixed in the same specification, for example: `A1, DQo, 22601`

 |
 |

 |

<group offset>

 |

Double

 |

The offset that is added to every specified pin or channel. The unit is nanoseconds (ns).

The offset can be a positive or negative number, and it can be an integer or a decimal fraction. These are all valid values: 3, -3, 2.5, -2.5

 |
 |

rss_buffer_pins

 |

<site no>; [<tmp src buffer>], <source buffer>, <global buffer 1>, <global buffer 2>

 |

String

 |

The site or sites for which you specify the rapid source sync buffer pins.

You can specify:

- A single site by providing the number of the site, for example, 3.
- Multiple sites by providing their numbers in a comma-separated list, for example, 3, 5, 7.
- A range of sites using a dash, for example, 3-6.

The site specification is followed by the buffer specification (described below). There can either be one buffer specification or different buffer specifications for multiple domains in the site. If there are multiple specification for different domains, they must be separated by semicolons.

Note that sites 241-256 are not available for rapid source sync.

Also note that any buffer pin specification in the BufferPins test method parameter overrides this setting in the sharing configuration file.

 |
 |

 |

<tmp src buffer>

 |

String

 |

A temporary source buffer pin.

This is an optional parameter: If only three pins are listed, it is assumed that no temporary source buffer is specified. If four pins are listed, the first is the temporary source buffer.

 |
 |

 |

<source buffer>

 |

String

 |

The source buffer pin.

 |
 |

 |

<global buffer 1>

 |

String

 |

The first global buffer pin.

 |
 |

 |

<global buffer 2>

 |

String

 |

The second global buffer pin.

 |

### Example

This sample file works for a 4,2,2 structure; that is, a topology that can has daisy chains with up to four sites, up to two daisy chains connected to one driver pin, and repeats this structure over two domains.

```
pin_configuration:
./128Mx8_Moscato4.pin_forFXDL

fixture_delay_files:
./TSE_FXDL/Y2/FXDL1.txt
./TSE_FXDL/Y2/FXDL2.txt
./TSE_FXDL/Y2/FXDL3.txt
./TSE_FXDL/Y2/FXDL4.txt
;
./TSE_FXDL/Y2/FXDL5.txt
./TSE_FXDL/Y2/FXDL6.txt
./TSE_FXDL/Y2/FXDL7.txt
./TSE_FXDL/Y2/FXDL8.txt

domains:
1 2 3 4; 5 6 7 8
9 10 11 12; 13 14 15 16

utility_control:
idd; (y<=0); (U7=0x222&0xfff); (DEVICE_SUPPLY=VDD)
idd; (y>=1); (U7=0x111&0xfff); (DEVICE_SUPPLY=VDD)
iddq; (y<1); (U7=0x777&0xfff); (DEVICE_SUPPLY=VDD)
iddq; (y>=1); (U7=0xbbb); (DEVICE_SUPPLY=VDD)
leakage; (U5=0x001&0x001)
oc_reset; (U5=0x000&0x400,U5=0x400&0x400,U7=0x000&0xfff,U5=0x000&0x400)
default; (U7=0x000,U5=0x000&0x401)

topology:
x=4,y=2, actterm=VTERM ; SharedGrp
x=4,y=2, cross ; CrossTermGrp

fxdl_ignore_pins:
A3, A4

groups:
22601, 22602 ; offset=3
22701-22716 ; offset=-4
A0, A1 ; offset=4.7

rss_buffer_pins:
1,3,5,7; A.00, A.01, A.02
2,4,8,9; A.03, A.04, A.05
```

<!-- 语法节 end -->

## 是什么

- **定义 load board 的 sharing 结构**的文件。原文：*"The sharing configuration file defines
  the sharing structure of the load board. It is used by all sharing test methods as well as
  the fd_merge tool."*
- **内容**（原文列表）：引脚的物理设置 / fixture delay 文件名 / 每条 chain 上的 site 数 /
  y-shared 的引脚或 chain 数 / 每条 chain 上 site 的顺序 / **可选**：用于 rapid source sync
  的 buffer pins。
- **位置是硬要求**：原文 *"This file must be stored in the configuration directory under the
  current device."* —— 即 `<device>/configuration/`。
  （多处引用文档把路径写成 `<device directory>/configuration/`。）
- **属于哪一段**：load board 的引脚与 sharing 结构 → [[pin]]。
  即：它描述的是**硬件怎么接的**，不是测试怎么写。测试文档只是**引用**它。

## 典型用法

原文给了一个可直接照着改的**完整样例**（`4,2,2` 结构：每条 daisy chain 最多 4 个 site、
最多 2 条 daisy chain 接到同一个 driver pin、该结构在两个 domain 上重复），
逐字收在上面「语法 / 参数」一节的 `Example` 里——**本页不重述它**。

使用路径（全部来自入边原文）：

1. **fd_merge 工具**以该文件为输入，合并 fixture delay 文件
2. 各 sharing test method 用 `sharingConfigFile()` 指定用哪一份
3. `Measuring fixture delay` 的步骤是：先按 FXDL 文件写好本节这段
   `fixture_delay_files`，**再启动 SmarTest**，然后载入本文件里指定的 pin configuration file

## 和谁有关

**读它的 L2 API** —— [[sharing-configuration]] 类就是这份文件的访问器。原文：
*"The SHARING_CONFIGURATION class provides an API for accessing the data contained in the
Sharing configuration file."* 已知成员：`utilitySearchFirst()` / `utilitySearchNext()` /
`utilitySubstitutePins()` / `utilityActionExecute()` / `utilityGetApplicableSitesString()` /
`getTerminatedPinList()` …

**指向它的 test method**（每个都有 `sharingConfigFile()`）：
[[shared-continuity-test]]、`SHARED_IDD_TEST`、[[shared-leakage-parallel-test]]、
`SHARED_VBUMP_TEST`、`SOURCESYNC_TEST`。
（**只链已经进 backlog 的**——`SHARED_IDD_TEST` / `SHARED_VBUMP_TEST` / `SOURCESYNC_TEST`
三个入度不够、不在 `unowned.csv` 里，链了就是造永远不会建的悬空目标。
链接规则见 `schema.md` §2.2。）
其中 SharedVBump **依赖** `utility_control` 段里的 `vbump` 关键字才能把 DPS32 通道正确接到
VDD / VDDQ（原文：*"SharedVBump relies on the proper setup of the vbump keyword in the
utility control section"*）。

**用它的 L1 命令**：`FOR_EACH_TEST_BEGIN` / `FOR_EACH_TEST_BEGIN_WITH_RESET` /
`FOR_EACH_TEST_END` / `GET_CURRENT_UTILITY_CONTROL` —— 待测的 shared site
**按 `utility_control` 的设置分组**。

**工具**：`fd_merge`（要求本文件作为输入）、`DPS Sharing Diagnostic`。

**⚠️ 一条反复出现的覆盖规则（原文出现 5 次，逐字）**：

> "This parameter is ignored for DPS-shared load boards for which there is a utility_control
> section in the Sharing configuration file."

出现在 `SHARED_CONTINUITY_TEST.terminationDPS()` / `.supplyDPS()`、
`SHARED_IDD_TEST.vdd()` / `.vddq()`、`SharedContinuity syntax`、`SharedIDD syntax` 上。
**意思是：DPS-shared load board 且本文件里有 `utility_control` 段时，这些 API 参数被忽略，
以文件里的 utility 设置为准。** 两处都配了谁赢——这条值得记牢，它会让人「改了 API 参数
却没反应」。

**同一套语法的别处**：`Diagnostic configuration file` 原文明确说
*"The same syntactic options as for other utility control statements in the Sharing
configuration file apply"*（但**不做 pin substitution**）。

**`utility_control` 段里的 utility line 本身是什么** → [[utility-line-assignments]]。
本文件只写「哪条 utility line 在什么条件下设成什么值」，**line 的物理定义在那边**。

## 版本

- **Introduced before SmarTest 6.3.2**
- **MTP 3.0.1**：引入**全新语法**以支持 **Y sharing 和 hybrid sharing**
- **MTP 3.0.3**（MTP on SOC 103.0.0）：加入 **rapid source sync buffer pins** 段

> 注意第 2 条：**语法被整体换过一次**。看到网上/旧工程里的 sharing 配置文件写法时，
> 先确认它是不是 MTP 3.0.1 之前的。本 wiki 面向 SmarTest **7.10.3**，用的是新语法。

## 出处

- 定义文档：`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.07.02_Sharing_configuration_file.md`
  （TDC `96971.htm`，11,205 字节）
- 入边 39 篇的来源与原句：`extract/pack/03-sharing-configuration-file.md`
- 所属：**Memory Test Plus**（`02.12`），不是通用 93K 功能
- 本页 `verified: doc-only` —— 只在 TDC 文档里确认存在，未在真实机台上写过这份文件。
