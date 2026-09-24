---
type: object
title: PDIV? - (Period DIVider)
layer: L1
stage: timing
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.176_PDIV__-__Period_DIVider.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# PDIV? - (Period DIVider)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」节是脚本逐字抽的（§4），**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,161 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.176_PDIV__-__Period_DIVider.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
PDIV? {specset_id|"multi-port_spec"|"wavetbl"} [,spec_type][,(pinlist)]
```

returns:

```
PDIV {specset_id|"multi-port_spec"}, {period_div}
```

### Parameters

|

specset_id

 |

Identifier of a timing specification, which is derived as follows:

100 * equation_set_no + specset_no

 |
 |

multi-port_spec

 |

To query a multi-port specification, enter the name of the specification.

 |
 |

wavetbl

 |

Name of a wavetable. This requires that spec_type is set to WFT.

 |
 |

period_div

 |

Possible values are -1 (for standard pins), 2, 3, 4, 6, 8 (only for fast pins).

 |
 |

spec_type

 |

Possible values are:

 |
 |

TIM

 |

Returns the period divider of the timing sets (fast pins). If not all timing sets have the same period divider for the same fast pin, PDIV? returns an error.

 |
 |

WFT

 |

Returns the implicit period divider of the wavetable specified as the first parameter.

 |
 |

pinlist

 |

This parameter is only applicable to fast pins. For standard pins,`-1` is returned.

 |

### Example

```
> PDIV? "fast",WFT,(I1)
< PDIV "fast",WFT,6,(I1)
```

This example queries the implicit period divider of the fast pin I1 in the wavetable `fast`. The factor is 6.

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
