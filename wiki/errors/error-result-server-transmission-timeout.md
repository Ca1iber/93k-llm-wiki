---
type: error
title: 报 "error occurs during data transmission with Result Server"
tags: [error, results, reconstruction, memory-test, timeout]
related: [[results]], [[report-window]], [[run]]
sources:
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.08.01_Result_Server_transmission_timeout.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# 报 "error occurs during data transmission with Result Server"

## 症状

**report window 里出现这条：**

> Warning: error occurs during data transmission with Result Server.

**紧跟三行解释**（原文代码块，整段照抄）：

```
Warning: error occurs during data transmission with Result Server.
The bitmap file generated may be incomplete.
Possible reason: the current Timeout setting is too short.
Please set RESULT_SERVER_TIMEOUT longer and try again.
```

**注意第二行才是后果**：`The bitmap file generated may be incomplete.`——
**这个报错的意思是「你手上那份结果可能是不全的」，不是「这次测试失败了」。**
两种情形的处置完全不同（测试失败要重测；结果不全要重取或重跑），
**所以别看到 Warning 就当运行出错。**

## 触发条件

文档给的三个条件**是「与」的关系**（三个同时满足才可能出现）：

> With the reconstruction file type .rec, massively failing devices and using online reconstruction the following message can be displayed: Error occurs during data transmission with Result Server.

拆开是：① 用了 `.rec` 这个 reconstruction 文件类型；② 器件大面积失败；
③ 走的是 online reconstruction。→ [[results]]

**为什么「大面积失败」会牵出这个错**：失败多 → 要传的 bitmap 数据量大 →
超过 Result Server 的默认超时。文档没写这句因果，**这是本页的推断**（见「文档没写清的地方」）。

## 怎么办

**第一步是「先让 Result Server 结束掉」，不是改超时：**

> To solve this problem first make sure that the Result Server gets finished by killing the Result Server process (hsmresultsrv) manually.

**然后有两条路**（原文："Then there are two possible ways how to continue:"）：

**① 换编译参数、重跑测试**——

> - Recompile the pattern with parameter -r2 and re-run your test

**② 把超时调大**——

> - Set a higher timeout value (for example 30 minutes instead of the default 7.5 minutes) by typing the command

```
`export RESULT_SERVER_TIMEOUT=30`,restart SmarTest and re-run your test.
```

> ⚠️ **上面这行是原文，包括那一对反引号、以及逗号后面那个没有空格。**
> 本页没有「修正」它——§11.1：引文里不修排版。**不要照抄这对反引号去敲命令**，
> 它在这行里是排版残留，命令本身是 `export RESULT_SERVER_TIMEOUT=30`。
> （这一行是**格式被破坏但内容可读**的实例：反引号该包住命令，原文却包在了逗号前。）

**默认值是 7.5 分钟**，文档给的建议值是 30 分钟。**这条是文档事实**
（"the default 7.5 minutes" / "for example 30 minutes"）。

## 文档没写清的地方

1. **`-r2` 是什么意思、和超时是什么关系，文档一个字没写。**
   本页**不猜**——「重编译一遍就能少传点数据」是合理联想，**但本页找不到依据**。
2. **两条路该选哪条，文档没给判据。** 只说 "two possible ways"。
3. **`RESULT_SERVER_TIMEOUT` 的单位文档没写。** 例子里的 `30` 对应
   "30 minutes instead of the default 7.5 minutes"，**所以看起来是分钟**，
   但这一句是**推断**，不是文档明写的单位。
4. **改完要不要重启 SmarTest？** 原句里 "restart SmarTest" 和命令在同一行、
   被逗号连着，**读起来像「敲完命令要重启」**——但**这条也是推断**，不是明写。

## 出处

| 说法 | raw |
|---|---|
| 症状、三个触发条件、两步处置、`-r2` / `RESULT_SERVER_TIMEOUT` / 7.5 分钟默认值 | `02.12.02.08.01_Result_Server_transmission_timeout.md` |
| 完整报错代码块、`The bitmap file generated may be incomplete.` | 同上 |

文档事实，`verified: doc-only`。原文在 `02.12_Memory_Test_Plus_7.10.2` 章下
（`02.12.02.08.01`），**本篇没有 `Functional changes` 段**，
所以「哪个版本起有这条报错」**本次未找到**——本页不写版本。

## 相关

- [[results]]——reconstruction 与 bitmap 属于结果层；本页是这个层的一个已知故障。
- [[report-window]]——报错出现的位置（**概念/工具页尚未建立**，是 `extract/dangling.csv` 里的悬空目标）。
- [[run]]——「测试失败」和「结果不全」是两件事，run 页负责的是前者。
