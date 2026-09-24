---
type: object
title: RSET - (ReSET)
layer: L1
stage: level
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.210_RSET_-__ReSET.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# RSET - (ReSET)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」节是脚本逐字抽的（§4），**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,930 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.210_RSET_-__ReSET.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
RSET {specifier}
```

### Parameters

|

specifier

 |

The specifier can be:

 |
 |

DPS

 |

Loads the default power supply setup for standard DPSs.

 |
 |

FCR

 |

Loads the default clock routing.

 |
 |

LEV

 |

Loads the default power supply setup for standard DPSs.

Level: 0 V

Current: 50 mA

Off state: minimum current

Setup time: 0 ms

This default states are:

UHC4T

- Connect state: normal
- Level: 0 V
- Range: 4 V
- Clamp: 4 A
- Clamp-Range: 40 A
- Disconnect state: HIZ
- Voltage drop force: 250 mV
- Voltage drop return: 250 mV
- Clamp mode: limit (see `UHCM`（raw: `02.06.02.02.303_UHCM__UHCM__-__Ultra_High_Current_power_supply_Modes.md`）)
- DUT capacitor mode: off

Fast preload: 0 ms

 |
 |

TIM

 |

Loads the default timing setup. The settings are:

Timing Sets

- Defined Timing Sets: 1
- Allowed Timing Sets: 256

Waveform Sets

- Defined Waveform Sets: 1
- Allowed Waveform Sets: 16

Waveforms: not defined

Breakwaveform: defined

Events

- Action: NOP
- Timing: 0 ns

Min Period: 4 ns

- This is dependent on the test system hardware configuration.

Device Cycles: not defined

Default Device Cycle: ""

 |
 |

VEC

 |

Loads the default vector setup. The Vector Memory contains:

No vectors

No tests (and therefore no labels)

No comments

No sequencer programs (no instructions)

 |
 |

ATR

 |

Loads the default edge attributes.

Pin attribute: set to 0

 |
 |

PDL

 |

Loads the default path delay attributes.

Cable assembly delay attribute: set to 0

Fixture delay attribute: set to 0

System attribute: set to 0

 |
 |

CAL

 |

Loads the default calibration data.

Level calibration data

Timing calibration data

 |
 |

MTPP

 |

Resets memory test and per-pin sequencer subroutine data.

 |

### Example

```
RSET TIM
```

This example resets all waveform sets and timing sets and loads the hardware with the default vector rate and edge placement values. Only waveform set 1 and timing set 1 in waveform set 1 is active.

<!-- 语法节 end -->

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
