---
type: object
title: CHIN? - (CHannel INformation)
layer: L1
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.22_CHIN__-__CHannel_INformation.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# CHIN? - (CHannel INformation)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」节是脚本逐字抽的（§4），**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **2,719 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.22_CHIN__-__CHannel_INformation.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
CHIN? {channel_nr|ALL}
```

returns:

CHIN {channel_nr}, {channel_type}, [phys_location], {board_no}, [clk_board], [chan_info_1], [chan_info_2]

### Parameters

|

channel_nr

 |

The number that identifies the channel.

Specify ALL if you want information about all channels.

For a digital channel, specify it with the test system channel number, which is five digits (see `DFPN, DFPN? - (DeFine Pin Name) for the number)`（raw: `02.06.02.02.63_DFPN__DFPN__-__DeFine_Pin_Name.md`）.

For a DPS channel, specify it with the test system channel number, which is two digits (see `DFPS, DFPS? - (DeFine Power Supply)`（raw: `02.06.02.02.65_DFPS__DFPS__-__DeFine_Power_Supply.md`） for the number).

 |
 |

channel_type

 |

Returns the type of the channel. It can be:

 |
 |

CPIO

 |

Pin Scale 1600 digital channel

 |
 | PYIO  | Pin Scale 5000 digital channel |
 |

WZ_FDIFF_I

 |

Fast differential input channel

 |
 |

WZ_FDIFF_O

 |

Fast differential output channel

 |
 |

PPS

 |

Precision Parallel Source channel

 |
 |

HVP

 |

High Voltage PMU

 |
 |

DPS128HC

 |

DC Scale DPS128-HC or DPS64-HC

 |
 | XPS256  | DC Scale XPS256 |
 |  UHC4T  | DC Scale UHC4T |
 |

phys_location

 |

The channel's physical location.

NOTE: For PS1600 and DPS128 SmarTest returns always "-1"!

This format is TCSSPP.

Where:

 |
 |

T

 |

test head (1)

 |
 |

C

 |

card cage (1 - 8)

 |
 |

SS

 |

slot (01 - 18) in the card cage

 |
 |

PP

 |

hardware pin number of the digital channel

For DPS, this is the channel number in the DPS board.

 |
 |

board_no

 |

Board number of the board to which the channel belongs. For the DPS, this is the DPS board number. For details, see the board_no parameter in `*OPT? - (hardware OPTions)`（raw: `02.06.02.02.344_OPT__-__hardware_OPTions.md`）.

 |
 |

clk_board

 |

Board number of the clock board in the card cage to which the channel belongs.

 |
 |

chan_info_1

 |

First information of the channel.

 |
 |

For digital channels:

Sequencer memory (SM) depth in blocks of 128k vectors (or 0.125M vectors).

DC Scale DPS channels behave like a digital channel and return the sequencer memory depth.

 |
 |

For PPS channels:

Pattern memory depth in blocks of 1k words (16 bit).

 |
 |

For HVP channels:

DAC/ADC RAM depth in blocks of 1k words (16 bit).

 |
 |

chan_info_2

 |

Second information of the channel.

 |
 |

For digital channels:

Sequencer memory (SM) depth in blocks of 128k vectors (or 0.125M vectors).

 |

### Examples

```
CHIN? 10901
```

returns:

```
CHIN 10901,PSIO,120601,109,21,512,0
```

```
CHIN? ALL
```

  Return (for example):

```
CHIN 10101,PYIO,110301,101,11,3551,0
CHIN 10102,PYIO,110302,101,11,3551,0

CHIN 21701,DPS128HC,-1,217,31,191,0
CHIN 21702,DPS128HC,-1,217,31,191,0

```

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.22_CHIN__-__CHannel_INformation.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if a wrong value is given for channel_nr.

<!-- 报错节 end -->

## 是什么

（待补）

## 典型用法

（待补）

## 和谁有关

（待补）

## 版本

（待补）

## 出处

（待补）
