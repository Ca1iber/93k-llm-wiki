---
type: object
title: Hardware view
layer: gui
stage: run
tags: []
related: []
sources:
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.05.03_Hardware_view.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# Hardware view

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」节是脚本逐字抽的（§4），**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,146 字符逐字取自** `<01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.05.03_Hardware_view.md>` 及其子主题 `<01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.05.03.05_Profiling_of_DC_Scale_cards_with_Hardware_view.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Profiling of DC Scale cards with Hardware view）

### Utility serial configuration for DC profiling

The following screen shot shows a part of the DPS128 Hardware view.

 !`Profiling in Hardware view`（raw: `../../../../raw/353618.png`）

The Profile button at the bottom is marked in red and opens the DPS Profile dialog.

  !`DPS profile with`（raw: `../../../../raw/353741.png`）

You can define the configuration of sequencer鈥慶ontrolled utility lines, which is programmed to hardware before any pattern execution.

The UTSC firmware syntax is one of the following:

- `UTSC [1-8],[RW|RD][,MASK]`
- `UTSC ([-,1-8),[RW|RD][,MASK]`

For example:

UTSC 1,RW; UTSC (2,3),RW,MASK; UTSC (5-8),RD

After the pattern finishes, SmarTest applies: UTSC ALL,OFF.

Multiple serial buses are supported. Each bus can range from 1 single utility block to up to 8 consecutive blocks.

For example:

- Single bus: 1-8. (Block 1 is master. Blocks 2-8 are slaves)
- Two buses: 2-3,5-7 (Blocks 2 and 5 are masters. Others are slaves)

If the Seq Ctrl'd Util Blocks field is empty, no sequencer control is enabled during profiling.

The content of the Seq Ctrl'd Util Blocks field is not stored/restored after closing the dialog.

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
