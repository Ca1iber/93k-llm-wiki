---
type: object
title: GCTX? - (Get ConTeXt))
layer: L1
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.129_GCTX__-__Get_ConTeXt.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# GCTX? - (Get ConTeXt))

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」节是脚本逐字抽的（§4），**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,321 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.129_GCTX__-__Get_ConTeXt.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
GCTX? {setup_type},[setup_comp]
```

returns:

GCTX {setup_type}{,setup_nr|"name"},"[context_name]"

### Parameters

|

setup_type

 |

The type of the setup component for which the mode context is queried. Possible values are:

 |
 |

TIM

 |

Timing equation set

 |
 |

LEV

 |

Level equation set

 |
 |

WAVE

 |

Wavetable

 |
 |

LBL

 |

Sequencer label

 |
 |

SPCF

 |

Multi-port specification

 |
 |

CURR

 |

The mode context for the current primary sets (as defined with the SPRM command) and the current start label (as defined with the SQSL command).

 |
 |

setup_nr

 |

The number of a setup component. This parameter is ignored for setup type CURR.

 |
 |

name

 |

The name of a wavetable, or the name of a multi-port specification. This parameter is ignored for setup type CURR.

 |
 |

context_name

 |

The name of the mode context. If you specified CURR for the setup_type parameter, and the current mode context is not correct, GCTX? returns an empty string.

The context is only correct when all primary sets (defined by SPRM) and the current start label (defined by SQSL) are associated with the same mode context. Furthermore, if there exists a primary multi-port specification, the mode context must be the same for all ports of this specification.

 |

### Example

```
> GCTX? TIM,101
< GCTX TIM,101,"High-Speed"
```

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
