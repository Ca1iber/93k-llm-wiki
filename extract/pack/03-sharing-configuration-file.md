# 建页资料包 03 — 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.07.02_Sharing_configuration_file.md

## 0. 元信息

- 标题（frontmatter）：Sharing configuration file
- H1：Sharing configuration file
- 字节：10983；出度：3；入边：70
- frontmatter：`{"source_html": "02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.07.02_Sharing_configuration_file.htm", "source_topic": "96971.htm", "title": "Sharing configuration file"}`
- 标题结构：Sharing configuration file / Syntax / Example / Functional changes

## 1. 定义文档全文（raw，禁止修改）

```markdown
---
title: "Sharing configuration file"
source_topic: "96971.htm"
source_html: "02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.07.02_Sharing_configuration_file.htm"
---
# Sharing configuration file

The sharing configuration file defines the sharing structure of the load board. It is used by all sharing test methods as well as the fd_merge tool.

The sharing configuration file contains information on:

- The physical setup of the pins
- The names of the fixture delay files
- The number of sites in each chain
- The number of y-shared pins or chains
- The sequence of sites on each chain
- Optionally, buffer pins for rapid source sync

This file must be stored in the configuration directory under the current device.

The available keywords are listed in the table below:

## Syntax

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

For information on determining the coordinates of a device, see [Identifying sites](<02.12.02.05.06.07.07.04_Identifying_sites.md>).

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

For information on determining the coordinates of a device, see [Identifying sites](<02.12.02.05.06.07.07.04_Identifying_sites.md>).

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

For information on determining the coordinates of a device, see [Identifying sites](<02.12.02.05.06.07.07.04_Identifying_sites.md>).

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

## Example

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

## Functional changes

- Introduced before SmarTest 6.3.2
- MTP 3.0.1: Introduced completely new syntax to support Y and hybrid sharing
- MTP 3.0.3: (MTP on SOC 103.0.0) Added rapid source sync buffer pins section
```

## 2. 语法 / 参数段落（脚本逐字抽取，§4 —— 进页面时照抄，不重写）

### 〔Syntax〕

```text
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

For information on determining the coordinates of a device, see [Identifying sites](<02.12.02.05.06.07.07.04_Identifying_sites.md>).

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

For information on determining the coordinates of a device, see [Identifying sites](<02.12.02.05.06.07.07.04_Identifying_sites.md>).

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

For information on determining the coordinates of a device, see [Identifying sites](<02.12.02.05.06.07.07.04_Identifying_sites.md>).

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
```

### 〔Example〕

```text
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
```

## 3. 入边 39 篇（谁引它、引它的原句 —— 「和谁有关」的唯一来源）

### ← SharedContinuity syntax
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.09.09_SharedContinuity_syntax.md`（引 4 次）

- L44：See [Sharing configuration file](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>) for details on the configuration file.
- L165：This parameter is ignored for DPS-shared load boards for which there is a utility_control section in the [Sharing configuration file](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>).
- L184：This parameter is ignored for DPS-shared load boards for which there is a utility_control section in the [Sharing configuration file](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>).
- L280：For information on the syntax, see [Sharing configuration file](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>).

### ← Measuring fixture delay
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.07.05.01_Measuring_fixture_delay.md`（引 3 次）

- L18：Prepare the [Sharing configuration file](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>) by referencing in the fixture_delay_files section the FXDL files received from the fixture manufacturer. If you have repaired or otherwise modified the fixture, instead reference the repaired fixture FX
- L23：Start SmarTest and load the pin configuration file specified in the [Sharing configuration file](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>).
- L28：Load the pin configuration file specified in the [Sharing configuration file](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>).

### ← SharedIDD syntax
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.09.14_SharedIDD_syntax.md`（引 3 次）

- L62：This parameter is ignored for DPS-shared load boards for which there is a utility_control section in the [Sharing configuration file](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>).
- L79：This parameter is ignored for DPS-shared load boards for which there is a utility_control section in the [Sharing configuration file](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>).
- L179：For information on the syntax, see [Sharing configuration file](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>).

### ← FOR_EACH_TEST_BEGIN
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.04_FOR_EACH_TEST_BEGIN.md`（引 3 次）

- L12：The shared sites under test are divided into several groups according to the utility control settings of the [Sharing configuration file](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>).
- L51：The name of a utility control line in the utility_control section of [Sharing configuration file](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>). Multiple names are separated by commas.
- L122：[Sharing configuration file](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>)[SHARING_CONFIGURATION](<02.12.06.25_SHARING_CONFIGURATION.md>)[FOR_EACH_TEST_BEGIN_WITH_RESET](<02.12.06.05_FOR_EACH_TEST_BEGIN_WITH_RESET.md>)[FOR_EACH_TEST_END](<02.12.06.06_FOR_EACH_TEST_END.md>)

### ← FOR_EACH_TEST_BEGIN_WITH_RESET
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.05_FOR_EACH_TEST_BEGIN_WITH_RESET.md`（引 3 次）

- L12：The shared sites under test are divided into several groups according to the utility control settings of the [Sharing configuration file](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>).
- L51：The name of a utility control line in the utility_control section of [Sharing configuration file](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>). Multiple names are separated by commas.
- L133：[Sharing configuration file](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>)[SHARING_CONFIGURATION](<02.12.06.25_SHARING_CONFIGURATION.md>)[FOR_EACH_TEST_BEGIN](<02.12.06.04_FOR_EACH_TEST_BEGIN.md>)[FOR_EACH_TEST_END](<02.12.06.06_FOR_EACH_TEST_END.md>)

### ← SHARING_CONFIGURATION.utilitySearchFirst()
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.07_SHARING_CONFIGURATION.utilitySearchFirst.md`（引 3 次）

- L8：The utilitySearchFirst() and [utilitySearchNext()](<02.12.06.25.08_SHARING_CONFIGURATION.utilitySearchNext.md>) member functions of [SHARING_CONFIGURATION](<02.12.06.25_SHARING_CONFIGURATION.md>) find the locations of the specified utility control line within the utility_control block in the [Sharin
- L33：The name of a utility control line which you want to find in the [utility control block](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>).
- L39：[SHARING_CONFIGURATION](<02.12.06.25_SHARING_CONFIGURATION.md>)[SHARING_CONFIGURATION.utilitySearchNext](<02.12.06.25.08_SHARING_CONFIGURATION.utilitySearchNext.md>)[Sharing configuration file](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>)

### ← SHARING_CONFIGURATION.utilitySearchNext
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.08_SHARING_CONFIGURATION.utilitySearchNext.md`（引 3 次）

- L8：The utilitySearchNext() and [utilitySearchFirst()](<02.12.06.25.07_SHARING_CONFIGURATION.utilitySearchFirst.md>) member functions of [SHARING_CONFIGURATION](<02.12.06.25_SHARING_CONFIGURATION.md>) find the locations of the specified utility control line within the utility_control block in the [Shari
- L33：The name of a utility control line which you want to search in the [utility control block](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>).
- L39：[SHARING_CONFIGURATION](<02.12.06.25_SHARING_CONFIGURATION.md>)[SHARING_CONFIGURATION.utilitySearchFirst()](<02.12.06.25.07_SHARING_CONFIGURATION.utilitySearchFirst.md>)[Sharing configuration file](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>)

### ← SHARING_CONFIGURATION.utilitySubstitutePins()
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.11_SHARING_CONFIGURATION.utilitySubstitutePins.md`（引 3 次）

- L8：The utilitySubstitutePins() member function of [SHARING_CONFIGURATION](<02.12.06.25_SHARING_CONFIGURATION.md>) returns the names which will replace the other pins's names as defined in the specified utility control line. The utility control line is specified as its location in the utility_control bl
- L31：The location of a utility control line within the utility_control block in a [Sharing configuration file](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>). In this line, pins' substitutions are defined.
- L61：[SHARING_CONFIGURATION](<02.12.06.25_SHARING_CONFIGURATION.md>)[Sharing configuration file](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>)

### ← Creating a sharing configuration file
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.07.03_Creating_a_sharing_configuration_file.md`（引 2 次）

- L12：The fd_merge tool requires a sharing configuration file for your shared driver environment as input. This file must have a format as described in [Sharing configuration file](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>). To create this file, you can use the example file noted below.
- L38：[Sharing configuration file](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>)

### ← Fd_merge tool
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.07.06_Fd_merge_tool.md`（引 2 次）

- L33：The sharing configuration file can be customized to your needs. It is stored in the <device>/configuration/ directory. See [Sharing configuration file](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>) for more information.
- L272：[Sharing configuration file](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>)[Running the fd_merge tool to merge fixture delay files](<02.12.02.05.06.07.07.06.01_Running_the_fd_merge_tool_to_merge_fixture_delay_files.md>)

### ← ResetOverCurrentProtection test method
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.09.07_ResetOverCurrentProtection_test_method.md`（引 2 次）

- L14：The utility line settings needed to reset the relays are specified in the utility control section of the [Sharing configuration file](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>).
- L61：For information on the syntax for utility line settings, see [Sharing configuration file](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>).

### ← Using DPS Sharing Diagnostic
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.07.01_Using_DPS_Sharing_Diagnostic.md`（引 2 次）

- L18：A [Sharing configuration file](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>)
- L91：[Pin configuration file](<02.12.03.03.09.01_Pin_configuration_file.md>)[Sharing configuration file](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>)[DPS Sharing Diagnostic test scopes](<02.12.04.07.02_DPS_Sharing_Diagnostic_test_scopes.md>)[Diagnostic configuration file](<02.12.04.07.03_Diag

### ← Diagnostic configuration file
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.07.03_Diagnostic_configuration_file.md`（引 2 次）

- L24：The available keywords are listed below. The same syntactic options as for other utility control statements in the [Sharing configuration file](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>) apply, that is, you can specify names, equations and utility settings. Pin substitution is not requ
- L174：[Using DPS Sharing Diagnostic](<02.12.04.07.01_Using_DPS_Sharing_Diagnostic.md>)[Sharing configuration file](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>)

### ← SHARED_CONTINUITY_TEST.sharingConfigFile()
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.21.02_SHARED_CONTINUITY_TEST.sharingConfigFile.md`（引 2 次）

- L8：The sharingConfigFile() member function of [SHARED_CONTINUITY_TEST](<02.12.06.21_SHARED_CONTINUITY_TEST.md>) lets you specify the name of the [driver sharing configuration file](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>) used which should be located in <device directory>/configuration/
- L46：[SHARED_CONTINUITY_TEST](<02.12.06.21_SHARED_CONTINUITY_TEST.md>)[Sharing configuration file](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>)

### ← SHARED_IDD_TEST.sharingConfigFile()
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.22.02_SHARED_IDD_TEST.sharingConfigFile.md`（引 2 次）

- L8：The sharingConfigFile() member function of [SHARED_IDD_TEST](<02.12.06.22_SHARED_IDD_TEST.md>) lets you specify the name of the [driver sharing configuration file](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>) used which should be located in <device directory>/configuration/.
- L46：[SHARED_IDD_TEST](<02.12.06.22_SHARED_IDD_TEST.md>)[Sharing configuration file](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>)

### ← SHARED_LEAKAGE_PARALLEL_TEST.sharingConfigFile()
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.23.02_SHARED_LEAKAGE_PARALLEL_TEST.sharingConfigFile.md`（引 2 次）

- L8：The sharingConfigFile() member function of [SHARED_LEAKAGE_PARALLEL_TEST](<02.12.06.23_SHARED_LEAKAGE_PARALLEL_TEST.md>) lets you specify the name of the [driver sharing configuration file](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>) used which should be located in <device directory>/co
- L46：[SHARED_LEAKAGE_PARALLEL_TEST](<02.12.06.23_SHARED_LEAKAGE_PARALLEL_TEST.md>)[Sharing configuration file](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>)

### ← SHARED_VBUMP_TEST.sharingConfigFile()
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.24.02_SHARED_VBUMP_TEST.sharingConfigFile.md`（引 2 次）

- L8：The sharingConfigFile() member function of [SHARED_VBUMP_TEST](<02.12.06.24_SHARED_VBUMP_TEST.md>) lets you specify the name of the [driver sharing configuration file](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>) used which should be located in <device directory>/configuration/.
- L46：[SHARED_VBUMP_TEST](<02.12.06.24_SHARED_VBUMP_TEST.md>)[Sharing configuration file](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>)

### ← SHARING_CONFIGURATION.utilityActionExecute()
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.09_SHARING_CONFIGURATION.utilityActionExecute.md`（引 2 次）

- L31：The location of a utility control line within the utility_control block in the [Sharing configuration file](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>).
- L39：[SHARING_CONFIGURATION](<02.12.06.25_SHARING_CONFIGURATION.md>)[Sharing configuration file](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>)

### ← SHARING_CONFIGURATION.utilityGetApplicableSitesString()
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.10_SHARING_CONFIGURATION.utilityGetApplicableSitesString.md`（引 2 次）

- L31：The location of a utility control line within the utility_control block in the [Sharing configuration file](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>).
- L39：[SHARING_CONFIGURATION](<02.12.06.25_SHARING_CONFIGURATION.md>)[Sharing configuration file](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>)

### ← SHARING_CONFIGURATION.getTerminatedPinList()
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.17_SHARING_CONFIGURATION.getTerminatedPinList.md`（引 2 次）

- L8：The getTerminatedPinList() member function of [SHARING_CONFIGURATION](<02.12.06.25_SHARING_CONFIGURATION.md>) returns a list of pins that are terminated by the specified termination pin in the [topology block](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>).
- L37：[SHARING_CONFIGURATION](<02.12.06.25_SHARING_CONFIGURATION.md>)[Sharing configuration file](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>)

### ← SHARING_CONFIGURATION
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25_SHARING_CONFIGURATION.md`（引 2 次）

- L30：The SHARING_CONFIGURATION class provides an API for accessing the data contained in the [Sharing configuration file](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>).
- L69：[Sharing configuration file](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>)

### ← SOURCESYNC_TEST.sharingConfigFile()
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.29.11_SOURCESYNC_TEST.sharingConfigFile.md`（引 2 次）

- L8：Specifies the name of [a sharing configuration file](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>) for use. If not specifying a file with this function, by default, the source-sync test will not use sharing configuration files.
- L40：[Sharing configuration file](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>)

### ← SourceSync fast mode
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.06.02.05.01_SourceSync_fast_mode.md`（引 1 次）

- L32：This is an optional parameter. It is required only if you want to specify different buffer pins for different sites. If you want to specify the same buffer pins for all sites, you can use this parameter and specify the buffer pins in the [Sharing configuration file](<02.12.02.05.06.07.07.02_Sharing_

### ← Creating an FXDL file for a repaired fixture
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.07.05.02_Creating_an_FXDL_file_for_a_repaired_fixture.md`（引 1 次）

- L24：Load the pin configuration file specified in the [Sharing configuration file](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>).

### ← Fixture delay compensation process
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.07.05_Fixture_delay_compensation_process.md`（引 1 次）

- L21：Set up driver sharing, in particular the [Sharing configuration file](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>).

### ← Running the fd_merge tool to merge fixture delay files
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.07.06.01_Running_the_fd_merge_tool_to_merge_fixture_delay_files.md`（引 1 次）

- L63：[Test methods for driver sharing](<02.12.02.05.06.07.09_Test_methods_for_driver_sharing.md>)[Fd_merge tool](<02.12.02.05.06.07.07.06_Fd_merge_tool.md>)[Sharing configuration file](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>)

### ← Fixture delay measurement on shared drivers
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.07_Fixture_delay_measurement_on_shared_drivers.md`（引 1 次）

- L11：[Sharing configuration file](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>)

### ← SharedLeakageParallel test method
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.09.11_SharedLeakageParallel_test_method.md`（引 1 次）

- L43：For information on the syntax, see [Sharing configuration file](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>).

### ← SharedLeakageParallel syntax
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.09.12_SharedLeakageParallel_syntax.md`（引 1 次）

- L214：For information on the syntax, see [Sharing configuration file](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>).

### ← SharedVBump test method
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.09.15_SharedVBump_test_method.md`（引 1 次）

- L14：SharedVBump relies on the proper setup of the vbump keyword in the utility control section of the [Sharing configuration file](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>) to correctly route the DPS32 channels to VDD and VDDQ (see [SharedVBump syntax](<02.12.02.05.06.07.09.16_SharedVBump

### ← SharedVBump syntax
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.09.16_SharedVBump_syntax.md`（引 1 次）

- L147：For information on the syntax, see [Sharing configuration file](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>).

### ← FOR_EACH_TEST_END
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.06_FOR_EACH_TEST_END.md`（引 1 次）

- L22：[Sharing configuration file](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>)[SHARING_CONFIGURATION](<02.12.06.25_SHARING_CONFIGURATION.md>)[FOR_EACH_TEST_BEGIN](<02.12.06.04_FOR_EACH_TEST_BEGIN.md>)[FOR_EACH_TEST_BEGIN_WITH_RESET](<02.12.06.05_FOR_EACH_TEST_BEGIN_WITH_RESET.md>)

### ← GET_CURRENT_UTILITY_CONTROL
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.07_GET_CURRENT_UTILITY_CONTROL.md`（引 1 次）

- L48：[Sharing configuration file](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>)

### ← MTP_CONTINUITY_TASK.postExecute()
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.10.05_MTP_CONTINUITY_TASK.postExecute.md`（引 1 次）

- L8：The postExecute() member function of [MTP_CONTINUITY_TASK](<02.12.06.10_MTP_CONTINUITY_TASK.md>) must be called at the end of a continuity test after all pins have been measured. postExecute() will restore the settings as specified in the [Sharing configuration file](<02.12.02.05.06.07.07.02_Sharing

### ← MTP_LEAKAGE_TASK.postExecute()
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.14.05_MTP_LEAKAGE_TASK.postExecute.md`（引 1 次）

- L8：The postExecute() member function of [MTP_LEAKAGE_TASK](<02.12.06.14_MTP_LEAKAGE_TASK.md>) must be called at the end of leakage test after all pins have been measured. postExecute() will restore the settings as specified in the [Sharing configuration file](<02.12.02.05.06.07.07.02_Sharing_configurat

### ← SHARED_CONTINUITY_TEST.terminationDPS()
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.21.09_SHARED_CONTINUITY_TEST.terminationDPS.md`（引 1 次）

- L35：This parameter is ignored for DPS-shared load boards for which there is a utility_control section in the [Sharing configuration file](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>).

### ← SHARED_CONTINUITY_TEST.supplyDPS()
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.21.10_SHARED_CONTINUITY_TEST.supplyDPS.md`（引 1 次）

- L35：This parameter is ignored for DPS-shared load boards for which there is a utility_control section in the [Sharing configuration file](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>).

### ← SHARED_IDD_TEST.vdd()
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.22.03_SHARED_IDD_TEST.vdd.md`（引 1 次）

- L33：This parameter is ignored for DPS-shared load boards for which there is a utility_control section in the [Sharing configuration file](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>).

### ← SHARED_IDD_TEST.vddq()
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.22.04_SHARED_IDD_TEST.vddq.md`（引 1 次）

- L33：This parameter is ignored for DPS-shared load boards for which there is a utility_control section in the [Sharing configuration file](<02.12.02.05.06.07.07.02_Sharing_configuration_file.md>).

## 4. 出边 1 个（它引谁）

- [[Identifying sites]] → `02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.07.04_Identifying_sites.md`（Identifying sites）

## 5. 结构段落（Procedure / Dependency / Errors …）

### 〔syntax Syntax〕（L23，8268 字符，已截断）

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

If a baseboard fixture delay file has been specified (see above), the measurements in these files must be from upper pogo to socket pin. If there is n

### 〔syntax Example〕（L486，1135 字符）

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

### 〔version Functional changes〕（L535，190 字符）

- Introduced before SmarTest 6.3.2
- MTP 3.0.1: Introduced completely new syntax to support Y and hybrid sharing
- MTP 3.0.3: (MTP on SOC 103.0.0) Added rapid source sync buffer pins section
