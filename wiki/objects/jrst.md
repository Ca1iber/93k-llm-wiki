---
type: object
title: JRST - (Jitter modulator ReseT)
layer: L1
stage: timing
tags: [timing, jitter, jitter-injection, jitter-modulator, jrst, l1-command, firmware-command]
related: [jscf, mscf, msdf, timing]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.146_JRST_-__Jitter_modulator_ReseT.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# JRST - (Jitter modulator ReseT)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **315 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.146_JRST_-__Jitter_modulator_ReseT.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
JRST {(pin_list)}
```

### Parameters

|

pin_list

 |

The pins for which the jitter modulator is to be reset. Typically, this must be done for all configured pins, so that you will usually specify @ for the pin list.

 |

### Example

```
JRST (@)
```

This example resets the jitter modulator of all configured pins to its default state OFF.

<!-- 语法节 end -->

## 是什么

**JRST 是抖动调制器（jitter modulator）的复位命令。** 它复位到的不是「没有抖动」，
而是**抖动注入的默认态 `OFF`**——原文第一句：

> 「The JRST command serves to reset the jitter modulator to its default state OFF.」

**这一句里有一个容易读漏的地方：复位的目标是 `OFF`，不是「上一次的设置」。**
`## Parameters` 里唯一那一栏（`pin_list`）选的是**哪些 pin**，
**不是复到什么值**——**本页没有第二个参数**。

### 它解决的是一个具体的时间问题：**每次执行都从同一个起点开始**

原文第二句才是它存在的理由，逐字：

> 「If jitter injection is running continuously (CONT option for the MODE property of the jitter set)
> and JRST is issued between repeated executions of the same pattern,
> this will ensure that every execution starts from the same initial conditions.」

**拆开读：三个条件 + 一个结果。**

| 条件 | 原文用词 |
|---|---|
| 抖动注入**在连续跑** | `jitter injection is running continuously` |
| 那是用 **`CONT`** 选项开起来的 | `(CONT option for the MODE property of the jitter set)` |
| JRST **发在同一个 pattern 的两次重复执行之间** | `issued between repeated executions of the same pattern` |
| → 结果 | `every execution starts from the same initial conditions` |

**所以 JRST 不是「关掉抖动」，是「把连续抖动归零」**——**它让重复执行可复现。**
（**推断**：`the same initial conditions` 指的是调制器的内部状态，
依据是这句的主语 `jitter injection` 与动词 `starts from`；
**原文没有说「不复位会怎样」——那一条语料未写。**）

**`MODE` 与 `CONT` 是别人的地盘**：本篇**只提到这两个词，没有定义它们，
也没有说是哪条命令设的**（见「和谁有关」）。

### 作用范围：由 `pin_list` 决定，而惯例是**全给**

> 「The pins for which the jitter modulator is to be reset. Typically, this must be done for all
> configured pins, so that you will usually specify @ for the pin list.」

**`Typically` 与 `usually` 两个词都在这一句里**：原文把「配了抖动的 pin 要一起复位」
写成**惯例**，**不是硬性要求**。
**`@` 就是「all configured pins」的写法。**
**只复位一部分 pin 会怎样，原文没写——语料未写。**

### 一条容易被当成「漏抄」的东西：`## Application` 只有两个词

原文 `## Application` 一节的全文是：

> 「Jitter injection.」

**它在本篇里就长这样**（对照 [[jscf]] 那一页的 `## Application` 也是 `Jitter injection.`——
**那是本页读到的另一页，不是本页的 raw**）。
**它指的是「抖动注入」这个专题，不是一个动作序列**；
专题正文在 `Principles of jitter injection`（**本篇点名的去向，本页没读**）。

## 典型用法

**1. 最小用法**（`## Example` 与参数释义拼起来）：**一行、只有一个 pin 列表**。

```
JRST (@)
```

> 「This example resets the jitter modulator of all configured pins to its default state OFF.」

**2. 该放在哪里**：原文把时机讲成了一个位置关系——
`between repeated executions of the same pattern`（**同一个 pattern 的两次执行之间**）。
照这句读，用法只能有一条：
**让抖动连续跑（`CONT`）→ 每次重复执行同一 pattern 之前发一次 `JRST` → 每次同起点。**
（**推断**：把 `between repeated executions` 落成「下次执行前发一次」，
依据是这句要保证的 `every execution starts from the same initial conditions`；
**原文没有给出任何一条 testflow 步骤或命令序列，本页不替它编一条。**）

**3. 别指望它做的事：**

- **它不是「开抖动」的开关**——本篇只说那件事归 `MODE` 的 `CONT` 选项，
  **没说是哪条命令去设的**。
- **它也不是「关抖动」**——它把调制器置成默认态 `OFF`，
  但**「置成 OFF 之后连续注入就停了」这句原文没写**（**语料未写**，本页不替它补）。

**4. 顺序要求、回读确认：语料未写。**
而且**本篇没有 `?` 形式的查询**（标题写的就是 `JRST - (Jitter modulator ReseT)`，
**没有 `JRST?`**）——**所以「复位成功了没有」，这条命令自己答不了。**
（**推断**：依据是 `### Syntax` 那栏只有 `JRST {(pin_list)}` 一条、`## Parameters` 只有一栏；
**原始文档里没有任何一处出现 `JRST?`。**）

## 和谁有关

- [[jscf]] — **同族里与它咬得最紧的一条，但本篇没有点名它。**
  本篇只出现 **`the MODE property of the jitter set`** 与 **`CONT`** 两个词
  ——**那是 jitter set 的属性，不是 JRST 的参数**。
  **所以本页不写「JSCF 的 MODE」**：`MODE` 归谁设，**本篇一个字都没写**。
  （**本页读到的 [[jscf]] 那一页上有 `MODE` 属性与它的三个取值（含 `CONT`）**——
  但**那是另一页的 raw，不是本页的依据**。）
- [[mscf]] / [[msdf]] — **同章家族的其他成员（并列）**。
  **本篇一个字都没提它们。** 判它们同族的依据是**文件层面**的：
  `02.06_Command_Reference/02.06.16.02.01_JRST_-__Jitter_modulator_ReseT.md`
  这份**与 JRST 同名的投放**就落在 jitter 命令章里
  （**本页核过这份的 frontmatter 与字节数，没有读它的正文**）；
  [[timing]] 的 L1 子专题也把 [[jrst]] 与 [[mscf]] / [[msdf]] 列成
  `02.06.16_Commands_for_jitter_injection` 家族（**本页读到的 wiki 页**）。
- [[timing]] — **stage 页**。本页 `stage: timing` 的依据是 frontmatter 与
  `## Application` 那句 `Jitter injection`（§6：`stage` 填最近的一段，不是归属）；
  [[timing]] 的 L1 子专题里已经有本页的名字（**本页读到的 wiki 页**）。
- `Principles of jitter injection`（**未建**）— **本篇点名的唯一去处**：
  > 「For general information on jitter injection see Principles of jitter injection.」
  **本页没读它**，所以「抖动注入的原理」本页一个字都没有。
  **这个名字不在 `extract/prose-allowlist.txt` 里，故用反引号写，不做成链接**（§9.1）。
- `Jitter injection` — **原文 `## Application` 的全部内容**；
  **它没有对应的页，本页也不为它编内容。**

## 版本

**本文档有 `## Functional changes` 段，段里只有一条**：

- **Introduced in SmarTest 7.0.1** — JRST 是 7.0.1 引进的 → [[smartest-7.0.1]]。

**版本段里没有的东西（照实记，不替它补）**：没有第二条。
**所以「`OFF` 这个默认态哪一版定的」「`CONT` 是从哪一版起有的」本篇查不到。**

**一条本页只能指出去、不能替它答的**：[[jscf]] 那一页的版本段写的也是
`Introduced in SmarTest 7.0.1`（**本页读到的另一页**）——
**同族命令的版本条目散在各自那一篇里，本篇只对自己这条命令的引入版本负责。**

## 出处

`sources:` 一篇：

- `02_System_reference/02.06_Command_Reference/02.06.02.02.146_JRST_-__Jitter_modulator_ReseT.md`
  （frontmatter 的 `source_topic` 是 `119634.htm`；**1,172 字节 / 44 行，整篇读完**）
- 本页的「语法 / 参数」节是脚本从这一篇抽的（**本页一个字没动**）。

**本页没做的**：

- **`Principles of jitter injection` 没读**（`02.06.16.01`）——
  **本篇正文亲自把它指为「更多信息」的落脚点。所以「抖动到底怎么注进去」本页没有。**
- **图 0 张。** 实测 `![` / `<img` / `.png` / `.jpg` / `.gif` / `raw/` 六种写法在本篇
  **全部 0 命中**。**本页没有任何来自图的结论。**
- **本篇既没有 `## Errors` 段、也没有 `## Warnings` 段**——
  **所以本页没有「报错条件」那一节，这不是漏写**（骨架里本来就没有那一节）。
  **代价要说清楚：`JRST` 在什么情况下会失败，本页答不了。**
- **本页的取材只有 JRST 这一篇。** 其余 jitter 族命令（[[jscf]] / [[jsdf]] / [[jspr]] /
  [[jsud]] / [[jswf]] / [[mscf]] / [[msdf]]）的 raw 都不在 `sources:` 里——
  **上面「和谁有关」里凡是跨页的话，都标了它来自哪一页。**
- **没在机台上跑过 `JRST`**（`verified: doc-only`）：
  **「复位之后波形是不是真的从头开始」本页只能保证「文档这么写」（§11）。**

### §10 重复投放：本篇有一份同名孪生（本页查过）

| 路径 | `source_topic` | 字节 / 行 | 与**本页这一份**的正文 |
|---|---|---|---|
| `02.06_Command_Reference/02.06.02.02.146_JRST_-__Jitter_modulator_ReseT.md`（**本页的出处**） | `119634.htm` | 1,172 / 44 | — |
| `02.06_Command_Reference/02.06.16.02.01_JRST_-__Jitter_modulator_ReseT.md` | `119634_2.htm` | 1,173 / 44 | **`diff` 报 0 行差异（正文逐行相同）** |

**两份正文逐行相同**，差别只在 frontmatter 的 `source_topic` / `source_html`
（**本页只读了第一份的正文；第二份只核了 frontmatter、字节数与 `diff` 行数**）。
**记这一条的用处有两层**：① 按 §10，判「两篇说法不同」之前先做这一步，本篇没有冲突；
② **JRST 同时挂在「字母序命令表」与「jitter 命令章」两个位置**——
**这正是本页判它属于 jitter 家族的那条文件层面的依据**（见「和谁有关」）。

> ⚠️ **本篇的语料瑕疵，本页照实记下**：
> **本篇没有找到错别字、坏字、链接指错或大小写不一致。**
> 照 §11.2 ① 那条判据（**英文文档里出现任何汉字，都是坏字**）逐字查过：
> **本篇一个汉字都没有**——那一族编码损坏**一处都没有**；
> 本篇只有一条内部链接（`Principles of jitter injection`），
> **目标指向对得上**（实测 `02.06.16.01_Principles_of_jitter_injection.md` 这份文件存在）。
> **但「本页没找到」不等于「本篇没有」**（§13.1 那条：没找到 ≠ 没有）——
> 本页只声明**它读到的这几项都没出问题**。
> **另有一处是留白、不是瑕疵**：本篇两次说 `the jitter set` / `jitter injection`，
> **却一次都没点名任何一条命令**，**也没写 `CONT` 怎么设**。**留白照实记，不替它填。**

`verified: doc-only`
