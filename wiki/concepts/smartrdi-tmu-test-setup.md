---
type: concept
title: SmartRDI: TMU test setup
layer: n/a
stage: testmethod
tags: [smartrdi, tmu, test-method-api, rdi, timing-measurement, ps1600, dc-scale, edge-measurement]
related: [smartrdi, ps1600, rdi-call-requires-begin-end-block, rdi-configure-file, dps128-dps64-cards, dc-scale-xps256-card, dc-scale-uhc4t-card, testmethod]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.21_SmartRDI__TMU_test_setup.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# SmartRDI: TMU test setup

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **752 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.13.21_SmartRDI__TMU_test_setup.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Examples

### Creating an independent TMU measurement

```
RDI_BEGIN();

    rdi.tmu("1").pin("PVI8_1")
            .vth(3.0 V, 5.0 V)
            .samples(4)
            .measMode(TA::PULSE_HIGH)
            .execute();

    rdi.wait(1 ms);

RDI_END();
```

The `execute()` here means the start of the TMU measurement. The TMU measurement takes place in the next event within this RDI_BEGIN/END() block.

### Inserting a TMU measurement into an existing pattern

```
RDI_BEGIN();

    rdi.tmu("id").label("func1").pin("DATA1")
            .insertVec(200)
            .vth(1.5 V)
            .samples(2)
            .measMode(TA::RISE_FALL)
            .execute();

RDI_END();
```

In this example, a TMU measurement is inserted into a copy of the func1 pattern.

<!-- 语法节 end -->

## 是什么

**SmartRDI 的 TMU 类：在 Smart Scale 数字卡和部分 DC Scale 卡上做 TMU（时间测量）测量。**

> 「The SmartRDI TMU class provides APIs for TMU measurements based on Smart Scale digital cards and selected DC Scale cards.」

**它能干的只有两件事，原文列成了清单**：

> 「- Create an independent TMU measurement.」

> 「- Insert a TMU measurement into an existing pattern.」

**硬件范围原文没写全，它把你推给了别处**：

> 「The TMU class supports the digital cards.」

> 「See Supported hardware for all the digital cards that SmartRDI supports.」

（`Supported hardware` 是 [[smartrdi]] 那一篇里的一个锚点，**本页没读它**——
所以「具体哪些数字卡支持 TMU」本页没有依据。）

### 这两件事的差别，全在 `execute()` 之后发生什么

这是本页的地基句：

> 「The execute() here means the start of the TMU measurement. The TMU measurement takes place in the next event within this RDI_BEGIN/END() block.」

**`execute()` = 开始，测量落在块内的下一个 event。** 有了这句，两种用法的差别就清楚了：

| | **独立测量** | **插进已有 pattern** |
|---|---|---|
| 例子里怎么起头 | `rdi.tmu("1").pin("PVI8_1")` | `rdi.tmu("id").label("func1").pin("DATA1")` |
| 关键的一句 | 直接 `vth(3.0 V, 5.0 V).samples(4).measMode(TA::PULSE_HIGH).execute()` | 前面多一个 `.label("func1")`，中间多一个 `.insertVec(200)` |
| 测的是谁 | 就是下一个 event 的那一刻 | **`func1` 这份 pattern 的一个副本** |
| 原文怎么说 | — | `In this example, a TMU measurement is inserted into a copy of the func1 pattern.` |

**`copy`（副本）这个词很要紧**：插进去的是一份**副本**，
所以**被插的那份 `func1` 本身没有被改**。
（**推断**，依据就是上面那句里的 `a copy of`；**原文没有第二处说这件事**。）

### 测完必须等够

> 「After the TMU execution, you must set a wait time long enough for the TMU to capture all samples.」

例子里的写法是 `rdi.wait(1 ms);`。

**为什么必须有**：`execute()` 只是「开始」，**采集还没结束**（`takes place in the next event`）。
**原文没有给「等多久」的算法**——**语料未写**，本页不猜。

### 一条默认值要记住

> 「Note that the default sequencer timeout is 900 s (see SQTO, SQTO? - (SeQuencer TimeOut)).」

**这是提醒，不是限制**：TMU 测量如果慢，会撞上 sequencer 的 **900 s** 默认超时。
（原文括号里指的那一篇是 `02.06.02.02.242`，**本页没读**——所以怎么改这个超时，本页没有。）

### PS1600 做**绝对**时序测量时的坑（原文分三段）

| | 原文（逐字） |
|---|---|
| **Phenomena** | `Arming may not work properly and a shift in measurement values or other undefined behaviors may occur.` |
| **Solution** | `When the arming of the TMU starts to be executed on pattern, the input signal through the TMU channel must always have the same level. This means that if the input signal is 0, the next one must be zero too; the same to the input signal 1.` |
| **Workaround** | `Add a vector to the end of the pattern to ensure that the input signal returns to its initial state. In this way, the input remains the same state when the next arming starts.` |
| **不适用** | `Relative timing measurements are not affected by this phenomena.` |

**「Solution 与 Workaround 是两条不同的路」**：
Solution 说的是**激励本身的约束**（输入信号必须始终同一电平），
Workaround 说的是**给 pattern 补尾巴**（加一个 vector 让信号回到初始态）。
**原文没说该用哪条、也没说两条是同一个东西**——本页并列写出，**不替它合并**。

### 链上有什么

从两个例子里能看到的链：

`rdi.tmu(<标识>)` → `.pin(<pin 名>)` → `.vth(<阈值>)` → `.samples(<采样数>)` → `.measMode(<取值>)` → `.execute()`

（`.measMode()` 的取值在两个例子里分别是 `TA::PULSE_HIGH` 与 `TA::RISE_FALL`——
**`TA::` 这个命名空间是什么，原文一个字没解释**。）

插入型多两节：`.label(<名字>)` + `.insertVec(<n>)`。

**⚠️ `.vth()` 不在本页的 `Subtopics` 里。** 见「版本」那一节。

## 典型用法

**原文没有 `## Procedure`、也没有 `## Before you begin`。**
`## Examples` 的两段就是本文档给的**全部写法**——这就是「典型用法」在这篇里的全部内容。

### 写法一：独立测量（例子逐字）

> 「RDI_BEGIN();」

> 「    rdi.tmu("1").pin("PVI8_1")」

> 「            .vth(3.0 V, 5.0 V)」

> 「            .samples(4)」

> 「            .measMode(TA::PULSE_HIGH)」

> 「            .execute();」

> 「    rdi.wait(1 ms);」

> 「RDI_END();」

### 写法二：插进已有 pattern（例子逐字）

> 「    rdi.tmu("id").label("func1").pin("DATA1")」

> 「            .insertVec(200)」

> 「            .vth(1.5 V)」

> 「            .samples(2)」

> 「            .measMode(TA::RISE_FALL)」

> 「            .execute();」

### 顺序上要守的两条

| # | 要守什么 | 依据（逐字） |
|---|---|---|
| 1 | **`.execute()` 之后必须给够等待** | `After the TMU execution, you must set a wait time long enough for the TMU to capture all samples.` |
| 2 | **整段放在 `RDI_BEGIN()` / `RDI_END()` 里** | `The TMU measurement takes place in the next event within this RDI_BEGIN/END() block.` |

**第 2 条不只是「照例子写」**：`execute()` 的语义**本身就绑在这个块上**——
离开了块，「下一个 event」就不存在。（**推断**，依据是上一行那句原文。）

### 本页给不出的

| 想知道的 | 状态 |
|---|---|
| `rdi.tmu(<标识>)` 那个字符串是什么、有没有取值限制 | **语料未写**。两个例子分别用 `"1"` 和 `"id"`，**原文一句解释都没有** |
| `TA::PULSE_HIGH` / `TA::RISE_FALL` 之外还有哪些取值 | **语料未写**。`TA::` 这个命名空间**原文一个字没解释** |
| `.vth()` 的双参数（`3.0 V, 5.0 V`）与单参数（`1.5 V`）差在哪 | **语料未写**。`vth()` 连子主题页都没有（见「版本」） |
| `.insertVec(200)` 的 `200` 是什么单位（event？vector 序号？） | **语料未写** |
| `.samples(4)` 与 `.measNum()` 的分工 | **语料未写**（`measNum()` 只出现在 `Subtopics` 里，正文没提） |

## 和谁有关

| 页 / 名字 | 关系是什么 |
|---|---|
| [[smartrdi]] | **上位页**：SmartRDI 的整体与硬件支持范围。**原文把「支持哪些卡」推给它**（`See Supported hardware for all the digital cards that SmartRDI supports.`）——**本页不重复它的内容** |
| [[rdi-call-requires-begin-end-block]] | **约束**：`execute()` 的语义绑在 `RDI_BEGIN()` / `RDI_END()` 上（见「典型用法」第 2 条） |
| [[rdi-configure-file]] | SmartRDI 的配置文件。**本页没读，只有名字** |
| [[ps1600]] | **PS1600 那一节专门讲它**：绝对时序测量的 Phenomena / Solution / Workaround |
| [[testmethod]] | 本页 `stage: testmethod` 的理由。**「最近的一段」，不是归属**（§6） |
| `Supported hardware`（raw: `02.07.13_SmartRDI.md` 的一个锚点） | **原文指向它**说「哪些数字卡支持 TMU」。**本页没读** |
| `digital cards`（raw: `02.05_Test_Head_Cards/02.05.04_Digital_cards.md`） | 原文第一段就链过去。**本页没读** |
| `SQTO, SQTO? - (SeQuencer TimeOut)`（raw: `02.06_Command_Reference/02.06.02.02.242`） | **900 s 默认值那一条的出处**。**本页没读**——所以怎么改超时，本页没有 |
| **22 条子主题** | `rdi.tmu()` 的 13 个函数（`dataRate()` / `disable()` / `enPassFail()` / `initDiscard()` / `insertVec()` / `interSkip()` / `label()` / `label().copyLabel()` / `measMode()` / `measNum()` / `pin()` / `preScaler()` / `samples()`）+ `rdi.id().get*()` 的 9 个（`getArm()` / `getInterSkip()` / `getMultiArm()` / `getPreScaler()` / `getPassFail()` / `getPropDelay()` / `getStamp()` / `getTmuErrorState()` / `getTmuFinished()`）。**均未建页**，本页一条没读 |
| `AVI64` / `FVI16`（DC Scale 卡） | **只出现在 `## Functional changes` 里**（见「版本」）。本页不知道它们是什么 |
| [[dps128-dps64-cards]] / [[dc-scale-xps256-card]] / [[dc-scale-uhc4t-card]] | **同一族 DC Scale 卡的其它型号**。**本页与它们的关系语料未写**——原文只提了 `AVI64` 与 `FVI16`，本页不替它把型号凑齐 |

### 一条要说清的

`rdi.id().get*()` 那一组（`getArm()` / `getInterSkip()` / `getMultiArm()` /
`getPreScaler()` / `getPassFail()` / `getPropDelay()` / `getStamp()` /
`getTmuErrorState()` / `getTmuFinished()`）**是「读回测量状态与结果」的那一半**——
**这是本页的一个明显缺口**：TMU 测量跑完**怎么把值取出来**，本页一个字没有。
原文把它们的名字列在 `Subtopics` 里，**但正文一句都没提它们怎么用**（**语料未写在这篇里**）。

## 版本

本文档 `## Functional changes` 段**五条**，逐字转录：

> 「- Introduced in SmartRDI 2.3.0」

> 「- SmartRDI 2.4.2: DC Scale AVI64 card added」

> 「- SmartRDI 2.4.2: New functions compHyst(), compMode(), ith()」

> 「- SmartRDI 7.5.0: DC Scale FVI16 card added」

> 「- SmartRDI 7.5.1: New function holdOffTime()」

**三条要注意的**：

- **`Introduced in SmartRDI 2.3.0` 不是哨兵值**——它写的是 `in` 不是 `before`
  （§11.2 ② 的哨兵值是 `Introduced before SmarTest 6.3.2` 那种写法）。**本页这条是「2.3.0 就有了」。**
- **`SmartRDI 2.4.2` 出现两次**，是两条独立条目（一条加卡、一条加函数）。**语料如此，照录。**
- **版本号跨产品线**（§11.2 ④）：本 wiki 的版本页**带产品前缀**，
  上表对应 [[smartrdi-2.3.0]] / [[smartrdi-2.4.2]] / [[smartrdi-7.5.0]] / [[smartrdi-7.5.1]]。

### ⚠️ 一处对不上，照实记（**两份清单没有交集**）

| 清单 | 成员 |
|---|---|
| `## Functional changes` 点名的**新函数**（4 个） | `compHyst()` / `compMode()` / `ith()` / `holdOffTime()` |
| 两个例子用到的、**不在 `Subtopics` 里**的函数 | `vth()`（还有 `execute()` / `wait()`） |
| `Subtopics` 列的 22 个函数 | 见「和谁有关」那一格 |

**`## Functional changes` 点名的四个新函数，没有一个在 `Subtopics` 里；
反过来，`Subtopics` 那 22 个函数，`## Functional changes` 一个都没提。
两份清单的交集是空集。** 而且**两个例子的核心方法 `vth()` 也不在 `Subtopics` 里**。

**这是语料的事实，本页照记，不判谁漏了、也不替它把清单补齐。**
**代价要说清**：`vth()` 是每一段 TMU 例子里都出现的方法，
**但它没有参数说明、没有子主题页**——本页只能给例子里的两种用法（见「典型用法」）。

## 出处

`sources:` **一篇**：
`02_System_reference/02.07_Test_Method_Reference/02.07.13.21_SmartRDI__TMU_test_setup.md`
（raw 的 `source_topic` 是 `149090.htm`）。**整篇读完**——全文 **96 行**。

**本页没做的**：

- **22 条子主题一条没读。** 那 22 篇是 `rdi.tmu()` 的 13 个函数与 `rdi.id().get*()` 的 9 个函数。
  **所以每个函数的参数、返回值、默认值、取值范围，本页一个字都没有**——
  本页只有**它们的名字**，以及原文在例子里顺带露出来的那几节链。
  **其中最要紧的一个空是 `rdi.id().get*()` 那一组**：
  **「测完怎么把值读出来」本页没有**（见「和谁有关」末段）。
- **`Supported hardware` 没读**（原文让它管「哪些数字卡支持 TMU」）。
  **所以本页答不了「我这张卡能不能做 TMU」。**
- **`SQTO`（`02.06.02.02.242`）没读。** 所以 **900 s 这个默认超时怎么改、改成多少合适**，本页没有。
- **`digital cards`（`02.05.04`）没读。** 所以「Smart Scale 数字卡」具体是哪些，本页没有。
- **`TA::` 这个命名空间原文一个字没解释**，本页也没有别的依据——
  所以 `TA::PULSE_HIGH` / `TA::RISE_FALL` **是什么、还有哪些取值，本页答不了**。
- **没有实跑。** 没在机台上跑过 TMU 测量、没插过 vector、没看过 TMU 的读数。
  `verified: doc-only`。

**图：本文档一张图都没有**（正文里 `../../../../raw/` 引用 **0 个**）。
**所以本页没有任何来自图的结论**——这是「**本页没用图**」，不是「图够不着」（§11.4）。

**⚠️ 语料瑕疵，照实记（§11.2）**：

- **坏字（§11.2 ①，判据 `[一-鿿]`）：本篇 0 处。** 查过，不是没看。
- **整词替换（§11.2 ⑤，`DC/DC power units`）：0 命中。**
- **一处不是坏字、是「语料自己不一致」的**（见「版本」那节）：
  `## Functional changes` 点名的 4 个新函数**没有一个在 `Subtopics` 里**，
  而 **`Subtopics` 那 22 个函数 `## Functional changes` 一个都没提**——**两份清单交集为空**。
  另外**两个例子都用的 `vth()` 也不在 `Subtopics` 里**。
  **本页照记，不判谁漏了、也不替它补齐。**

**图里的字不进 `>` 引文块（§11.4）**——本篇没有图，这一条在本页为空。

`verified: doc-only`
