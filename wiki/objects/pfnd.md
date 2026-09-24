---
type: object
title: PFND? - (Pin FiND)
layer: L1
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.178_PFND__-__Pin_FiND.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# PFND? - (Pin FiND)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」节是脚本逐字抽的（§4），**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **515 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.178_PFND__-__Pin_FiND.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
PFND? [group_type,] {(pin)}
```

returns:

```
PFND {group_type}, {(list)}, {(pin)}
```

### Parameters

|

group_type

 |

The group type can be PRT (for "port") or DIFF (for "differential pair"). PRT is the default.

 |
 |

pin

 |

The name of the pin about which information is to be retrieved.

 |
 |

list

 |

List of the ports that contain the pin, or the differential pair to which the specified pin belongs.

 |

### Example

```
> PFND? (I/O1_1)
< PFND PRT,(port_1,port_1.CP_1),(I/O1_1)
> PFND? DIFF,(P+)
< PFND DIFF,(P+,P-),(P+)
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
