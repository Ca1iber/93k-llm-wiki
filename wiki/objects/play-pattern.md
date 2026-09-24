---
type: object
title: playPattern()
layer: L2
stage: pattern
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.149_playPattern.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# playPattern()

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」节是脚本逐字抽的（§4），**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **523 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.149_playPattern.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
void playPattern(const STRING& _burstName);
```

### Example

```
CCTMultiportSync     Sync;
...
GET_TESTSUITE_NAME(tsName);
Sync.registerCCTestMethod(tsName, this);
...
PatternPort::getInstance().setPort(Port);
PatternPort::getInstance().setWaitTemplatePatternName(WaitTemplate);
Sync.registerSyncPort(PatternPort::getInstance());

Sync.start();

if(CCTgetDevelopMode()!=0)
{
        PatternPort::getInstance().playPattern(FlatPatt);
}
Sync.sync();
Sync.flush();
Primary.label(Sync.getMultiPortBurstName());
Sync.dumpMPBGraph();

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
