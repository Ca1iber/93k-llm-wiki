---
type: object
title: PRLT? - (request Parallel ResuLTs)
layer: L1
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.183_PRLT__-__request_Parallel_ResuLTs.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# PRLT? - (request Parallel ResuLTs)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」节是脚本逐字抽的（§4），**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **844 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.183_PRLT__-__request_Parallel_ResuLTs.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
PRLT? ["exec_context",] {site}
```

returns:

```
PRLT {site}, {"result"}
```

### Parameters

| exec_context  | An execution context. For more information on execution contexts see `Using execution contexts`（raw: `02.06.07.01.08.05.03.02.03_Using_execution_contexts.md`）. |
 | site  | The site parameter is number A single integer representing the site number. ALL Means that all the results of all configured sites are returned. |
 | result  | The result parameter is a string containing one character for every site. The nth character stands for site n. Possible characters are: P If the last test passed on all pins. F If the last test failed at any pin. 0 If the site was masked during the last test. |

### Example

```
PRLT? ALL
```

returns:

```
PRLT ALL, "PF0"
```

In this example, site 1 passed the last test, site 2 failed it, and site 3 was masked during the test.

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
