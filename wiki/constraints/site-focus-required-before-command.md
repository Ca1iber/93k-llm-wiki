---
type: constraint
title: 用站点焦点的命令，执行前必须先设站点焦点
layer: L1
stage: run
tags: [constraint, site-focus, setup-focus, multi-site, firmware]
related: [[psfc]], [[results]], [[testmethod]], [[run]], [[level]]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.01.05_Site_dependent_firmware_commands.md
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.09.21_HpFwTask.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# 用站点焦点的命令，执行前必须先设站点焦点

## 约束是什么

多 site 测试里，**固件命令不是对所有 site 一视同仁的**——
有一批命令**只作用于「当前焦点里的 site」**。所以用它们之前，
**必须先设焦点**：

> This topic lists the firmware commands, which make use of the site focus. That means you have to set the site focus before you can execute the command.

**这是 §2.4 的 D1（顺序前置）**：先设焦点，再执行命令。

## 在什么条件下成立

### 这是**一整批**命令共有的前置条件，不是某一条的特性

文档把它写成了**章首的总规矩**，后面跟一张**命令清单表**
（两列：`Command site focus` / `Query site focus`）。
**本页不讲那条规矩本身，而是讲它覆盖的面有多大**——
`02.06.01.05` 那一章里逐个列出支持「设焦点」和「查焦点」的命令，
**表里每一行都是一条实例**。

### 「焦点」有两种，文档分得很清

> With this command you configure setups of those sites that have the setup focus:

- **setup focus** —— 决定「**配置改的是哪些 site 的 setup**」。
- **query（结果）焦点** —— 决定「**取回的是哪个 site 的结果**」，
  文档同一段里写明了它的可见后果：
  > With this command you can retrieve site specific information (only one site can be in focus at a time). For the site in focus, SmarTest displays results in the Testflow Editor and in the result tools. Also, any firmware queries report setup and results for the site currently in focus only.

> **「同一时刻只能有一个 site 在焦点里」**是这一句里最容易漏掉的半句
> （括号里那句）。它决定了**多 site 取结果必须逐 site 轮流来**，
> 而不是一次拿全。

### 覆盖率：这一条规矩在语料里很大

支持设焦点的命令示例句 **98 处 / 51 篇独立文档**；
章首那条总规矩句 **4 处 / 3 篇**。
数字出自 `extract/rule_evidence.py`（键 `S-setupfocus` / `S-general`），可重跑。

> **98 处比 3 篇大得多，这两个数说的是两件事，别混**：
> 「51 篇」是**这条规矩触及的文档面**（每篇的命令页里都有一句
> 「configure setups of those sites that have the setup focus」）；
> 「3 篇」是**把它当规矩明确写出来的位置**。
> **页面上只写「N 处」而不说清是哪个口径，就是 §13.1 ②的假绿。**

## 违反了会怎样

**这是本 wiki 里少见的——文档把「不设焦点会怎样」逐条写出来了。**
`HpFwTask` 那一篇整段在讲这件事：

> Firmware commands executed via `HpFwTask` without site focus setup command will not automatically get the system site focus. If you use `HpFwTask` without a site focus setup command:

> - All setup commands executed via `HpFwTask` take the default setup focus (usually all sites) and apply setups accordingly

> - All result query commands executed via `HpFwTask` take the result of default site in focus (the first available site, usually site 1), therefore the result of all sites will be identical.

**这不报错——它走默认值。** 两个后果形状不同：

| 情形 | 后果 | 危险程度 |
|---|---|---|
| 不设焦点、跑 **setup 命令** | 默认焦点是**全部 site**，配置**被应用到所有 site** | **改多了** |
| 不设焦点、跑 **查结果命令** | 取**默认焦点 site**（通常是 site 1）的结果 | **所有 site 看起来一样** |

> **第二行是本页最该记住的一条**：结果查询会**静默地拿一个 site 的结果冒充全部**。
> 文档的原话是 `the result of all sites will be identical`——
> **它不会报错，只会让多 site 数据看起来整齐得可疑。**
> 这与 [[smc-background-process-locks-config]] 同属「静默做错」类。

**为什么会有这个差别**——文档解释了根因：

> This procedure allows direct access from a C program to the system hardware at firmware level, but will not automatically handle site focus as test method APIs do.

**test method API 会自动处理焦点，`HpFwTask` 不会。**
所以这条约束**在 `HpFwTask` 路径上最容易踩**，而这正是它被写在那里的原因。

## 数字口径与范围

| 键 | 命中 | 独立文档 |
|---|---|---|
| `S-general`（章首总规矩句） | 4 处 / 4 行 / 4 文件 | **3 篇** |
| `S-setupfocus`（配置句） | 98 处 / 98 行 / 98 文件 | **51 篇** |
| `S-hpfw`（不设焦点的后果） | 3 处 / 3 行 / 1 文件 | **1 篇** |

> **最后一行要特别注意**：`S-hpfw` 只在 **1 篇**文档里。
> **「文档写清了后果」这件事本身只出现在 `HpFwTask` 一篇里**，
> 上面那张「两种后果」的表是**从这一篇读出来的**，
> **不是从 3 篇或 51 篇里归纳的**。
> 按 §2.1，本页说的是「这一篇这么写」，**不是「语料一致这么写」**。

## 与 [[psfc]] / [[results]] 的关系

- [[psfc]] 是**设/查 focal 的固件命令**本身；本页讲**它为什么必须先执行**。
- [[results]] 讲结果怎么组织；本页讲**取结果时的焦点决定了你取到谁的结果**。

## 出处

| raw | 里面的原句 |
|---|---|
| `02.06.01.05_Site_dependent_firmware_commands.md` | 章首总规矩句、setup focus 句、查询焦点句、命令清单表 |
| `02.09.01.09.21_HpFwTask.md` | 不设焦点的两条后果、`will not automatically handle site focus` 句 |

文档事实，`verified: doc-only`。

## 这条约束怎么被发现的

**这一族是「先立数」直接改了结论的一例。**

我先前记的是「**108 处**」。跑 `rule_evidence.py` 得到的是 **98 处 / 51 篇**——
**先前的数错了**。若照先前的记法直接写页，
页面里会有一个**来源不明、且偏大**的数，而**十三类检验一条都不会报它**
（没有哪一类在核「页面里的计数对不对」）。

> **这就是为什么这一批先把数立起来再建页。** 换个顺序，
> 错的那个数会一路绿着走进 wiki。
