---
type: object
title: DFPC, DFPC? - (DeFine Pin Comment)
layer: L1
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.62_DFPC__DFPC__-__DeFine_Pin_Comment.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# DFPC, DFPC? - (DeFine Pin Comment)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」节是脚本逐字抽的（§4），**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **757 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.62_DFPC__DFPC__-__DeFine_Pin_Comment.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### DFPC

```
DFPC {(pin)}, {"comment"}
```

### DFPC?

```
DFPC? {(pinlist)}
```

returns:

```
DFPC {(pin)}, {"comment"}
```

### Parameters

|

pin

 |

In the command, this is the pin to which a comment is to be added. In the query reply, it is the pin whose comment is returned.

 |
 |

pinlist

 |

A query parameter that specifies the pins for which the comments are to be returned. You can also specify @ for all configured pins.

Pins for which no comments have been defined are ignored.

 |
 |

comment

 |

The comment to the pin. The maximal length of the comment string is 2048 characters.

 |

### Example

```
> DFPC (pin1), "This is a comment to pin1"
> DFPC? (pin1,pin2)
< DFPC (pin1), "This is a comment to pin1"
```

Since no comment has been defined for pin `pin2`, it is ignored in the reply.

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
