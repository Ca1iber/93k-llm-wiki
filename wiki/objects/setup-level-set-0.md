---
type: object
title: SetupLevelSet0
layer: L2
stage: level
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.05.04.06_SetupLevelSet0.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# SetupLevelSet0

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」节是脚本逐字抽的（§4），**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,602 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.05.04.06_SetupLevelSet0.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Parameters

|

Pins[]

 |

string

 |

array of pins

Separate pins with semicolon (;). Valid pin types include I, O, or IO digital pin.

 |
 |

ClampVoltage.Mode[]

 |

string

 |

array of clamp mode. It can be:

ON: Clamp is set to on with low/high voltage.

OFF: Clamp is set to off.

To specify different configuration for different pins, separate the values with semicolon (;).

 |
 |

ClampVoltage.Low_V[]

 |

string

 |

array of low clamp voltage in unit [V]

To specify different configuration for different pins, separate the values with semicolon (;).

 |
 |

ClampVoltage.High_V[]

 |

string

 |

array of high clamp voltage in unit [V]

To specify different configuration for different pins, separate the values with semicolon (;).

 |
 |

ActiveLoad.Mode[]

 |

string

 |

array of active load mode. It can be:

ON: set up active load setting, Vt, Iol and Ioh

OFF: turn off active load

To specify different configuration for different pins, separate the values with semicolon (;).

 |
 |

ActiveLoad.CommutationVoltage_V[]

 |

string

 |

array of commutation voltage (Vcom), in unit [V]

To specify different configuration for different pins, separate the values with semicolon (;).

 |
 |

ActiveLoad.SourceCurrent_A[]

 |

string

 |

array of active load source current (Ioh), in unit [A]

To specify different configuration for different pins, separate the values with semicolon (;).

 |
 |

ActiveLoad.SinkCurrent_A[]

 |

string

 |

array of active load sink current (Iol), in unit [A]

To specify different configuration for different pins, separate the values with semicolon (;).

 |

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
