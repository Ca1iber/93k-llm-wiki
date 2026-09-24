---
type: object
title: RESULT_CONFIGURATION
layer: L2
stage: results
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.191_RESULT_CONFIGURATION.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# RESULT_CONFIGURATION

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」节是脚本逐字抽的（§4），**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,906 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.191_RESULT_CONFIGURATION.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example

```
// Declare a new result configuration object:
RESULT_CONFIGURATION config1;
STRING exceptionPins("pin1,pin2");

// Use member functions to specify the needed settings for port "port1":
config1.setNumberOfResultsPerCycle( RESULT_CONFIGURATION::RPC8, "port1" );
config1.setResultWidth( RESULT_CONFIGURATION::_2Bit, "port1" );
config1.setResultStorageLocation( RESULT_CONFIGURATION::TP, "port1" );
config1.setResultGranularity( RESULT_CONFIGURATION::cycle, "port1" );

// Pins excepted from the above  storage locations settings:
config1.setResultStorageLocationExceptionPinList( exceptionPins );

// Global settings:
config1.setResultStorageIncompleteBehavior( RESULT_CONFIGURATION::ErrorImmediate );
config1.setMultipleExecutions( true );

// Enable the configuration specified in the object "config1":
config1.enable();

// Use convenience constructor to specify a new result configuration
// for a single port and the global settings:
STRING exceptionPins("pin1,pin2");
RESULT_CONFIGURATION config2( "port2",
                              RESULT_CONFIGURATION::RPC1,
                              RESULT_CONFIGURATION::_1Bit,
                              RESULT_CONFIGURATION::TP,
                              "",
                              RESULT_CONFIGURATION::edge,
                              "",
                              RESULT_CONFIGURATION::ErrorOnRequest,
                              false );

// Make some adjustments:
config2.setResultStorageLocationExceptionPinList( exceptionPins );

// Specify some additional settings for another port:
config2.setResultGranularity( RESULT_CONFIGURATION::cycle, "port1" );

// Enable the configuration specified in the object "config2":
config2.enable();

// A newly created configuration contains the default settings.
// This can be used to reset the result configuration:
RESULT_CONFIGURATION  defaultConfig;
defaultConfig.enable();

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
