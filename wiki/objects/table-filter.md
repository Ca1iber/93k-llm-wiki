---
type: object
title: Table filter
layer: gui
stage: results
tags: []
related: []
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02.06_Table_filter.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# Table filter

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」节是脚本逐字抽的（§4），**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,313 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02.06_Table_filter.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

In the fields of the table filter, you can enter:

- Plain text (for text columns).

Only those rows are displayed where the content in the filtered column contains the text you have entered.

- Regular expression (for text columns).

Only those rows are displayed where the content in the filtered column matches the regular expression. You can use Content Assist (Ctrl+Space) to insert common regular expression terms.

- Number (for number columns).

Only those rows are displayed where the content in the filtered column is exactly the number you entered.

- Range; two numbers separated by a ~ tilde (for number columns).

Only those rows are displayed where the content in the filtered column is greater than the first number you entered and less than the second number.

If you leave out one of the numbers, the range is open-ended. For example, entering ~2 displays all row with a value smaller than 2 in the column.

- Multiple numbers, separated by commas (for number columns).

Only those rows are displayed where the content in the filtered column is exactly any of the numbers you entered. (This is an "or" query.)

You can use both simple numbers and ranges. For example, 3~,3 finds all rows with values greater than 3 or equal to three. -1,-1~1,1 finds all numbers from -1 to 1, including -1 and 1.

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
