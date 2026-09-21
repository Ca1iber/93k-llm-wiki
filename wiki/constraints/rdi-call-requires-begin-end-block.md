---
type: constraint
title: RDI 调用必须在 RDI_BEGIN()/RDI_END() 块内，且块内参数必须一致
layer: L1
stage: testmethod
tags: [constraint, testmethod, rdi, tmu, dc-scale]
related: [[testmethod]], [[dps-aux-pin-task]], [[xps256-pmu-operating-mode]]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.01.04_copyLabel.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.21.08_rdi.tmu__.label__.copyLabel.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.21.01_rdi.tmu__.dataRate.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.21.04_rdi.tmu__.initDiscard.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.21.06_rdi.tmu__.interSkip.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.21.12_rdi.tmu__.preScaler.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# RDI 调用必须在 RDI_BEGIN()/RDI_END() 块内，且块内参数必须一致

## 约束是什么

`RDI_*` 这一类调用有**两条规矩，形状不一样，本页把它们分开写**。
（§2.4：**不同形状不合并**。合成一句会让人以为是同一条。）

**规矩一 —— 位置归属（§2.4 的 D4）**：

> It must be used inside a RDI_BEGIN()/RDI_END() block.

**规矩二 —— 块内一致（§2.4 的 D3）**：

> Note For a digital pin, all the parameters must be the same within one RDI_BEGIN() ... RDI_END() block.

**两条管的是不同的事**：规矩一说「写在哪儿」，规矩二说「写在这个区间里的值必须彼此相同」。

## 在什么条件下成立

### 规矩一：块是**唯一合法的位置**

上面那句出自 `copyLabel`——**这个函数跟在 `label()` 命令之后用**，
文档顺带说明了它为什么要这么放（改现有 pattern 以省向量内存）。

**「inside」是排他的**：RDI 调用**不在块里就不合法**，
不是「放在块里更好」。这是 D4 的典型写法，与
[[execution-context-requires-firmware-definition]] 的 D2 不同——
**D4 管的是「在不在这个语法区间里」，D2 管的是「那个东西存不存在」。**

### 规矩二：一致的范围**按 pin 类型分档**，而且档不一样

文档**没有给一条统一的「参数必须一致」**，而是分了两档，
**两档管的参数集不同**：

| pin 类型 | 必须一致的东西 |
|---|---|
| **digital pin** | **all the parameters** —— 全部参数 |
| **受支持的 DC Scale pin** | 点名的几个：`initDiscard()`、`interSkip()`、`preScaler()`、`dataRate()` |

> Note For supported DC Scale pins, the initDiscard(), interSkip(), preScaler(), and dataRate() settings must be the same within one RDI_BEGIN() ... RDI_END() block.

> **⚠️ 「all the parameters」里的 `all` 是文档的原话**，
> 但**文档没有列举**它对 digital pin 具体指哪些参数。
> 本页照抄 `all`，**不替它展开成一张参数表**——展开就是我在替文档发明内容。

### 这一档里还夹着一条**不同形状**的要求

> Note For supported DC Scale pins, the preScaler() and dataRate() settings must be the same within one RDI_BEGIN() ... RDI_END() block. Functions interSkip() and initDiscard() must be omitted or set to 0.

后半句 `must be omitted or set to 0` **不是「一致」，是「不许出现或必须为零」**——
**这是禁令，不是匹配要求**。它和前面那半句并排写在同一句里，
**但形状不同**（§2.4：它是 D2 状态前提那一类，不是 D3）。
**本页照抄整句，并在这里点明它内部就有两种形状。**

> **注意 `...`**：上面三句引文里的 `...`（三个点）**是原文自己写的**，
> 表示「一个块内的连续区间」。§11.1 只允许引用原文本来就有省略号的地方——
> **这里是原文就有的**，不是我抄的时候省掉了字。
> （原文这个写法本身不规范，**照抄，旁边记一笔**。）

## 违反了会怎样

> **⚠️ 本次未找到任何描述报错形态的原文。**

四篇 `rdi.tmu__.*` 文档都把规矩写成 `Note`，
**没有一句写「违反了会怎样」**。本页不猜。

**⚠️ 但这一条的实际后果可能比报错更隐蔽**：规矩二管的是
**同一个块里多个调用之间的取值一致性**——它约束的是**关系**，
不是单个取值。**一致性被破坏时，单看任何一个调用都是合法的**，
这一点与 [[smc-background-process-locks-config]] 那类「静默做错」相近。
**这是推断，不是文档事实，标出来。**

## 数字口径

| 键 | 命中 | 独立文档 |
|---|---|---|
| `R-rdi-inside`（必须在块内） | 6 处 / 6 行 / 6 文件 | **2 篇** |
| `R-rdi-same`（块内必须一致） | 8 处 / 8 行 / 4 文件 | **4 篇** |

**规矩一只有 2 篇独立文档**——6 个文件里 4 个是同一篇 `copyLabel` 的重复投放
（`02.07.13.12.*` 与 `02.07.13.13.*` 两个分类树下）。
**「6 处」听起来比「2 篇」厚，实际按 §10 折掉投放后是 2 篇。**
数字出自 `extract/rule_evidence.py`，可重跑。

## 与 [[testmethod]] / [[dps-aux-pin-task]] 的关系

- [[testmethod]] 讲测试方法类怎么写；本页管**它里面 `RDI_*` 调用的写法**。
- [[dps-aux-pin-task]] 讲 DPS 辅助任务；规矩二里「受支持的 DC Scale pin」
  **指的就是这一类资源**——**但具体哪些 pin「受支持」，本页不判**，
  文档的 `For supported …` 把范围留给了别处。

## 出处

| raw | 里面的原句 |
|---|---|
| `02.07.13.12.01.01.04_copyLabel.md` | 规矩一 |
| `02.07.13.21.08_rdi.tmu__.label__.copyLabel.md` | 规矩一 |
| `02.07.13.21.01_rdi.tmu__.dataRate.md` | 规矩二（DC Scale 档 + digital 档两句都在这里） |
| `02.07.13.21.04_rdi.tmu__.initDiscard.md` | 规矩二 DC Scale 档 + `must be omitted or set to 0` |
| `02.07.13.21.06_rdi.tmu__.interSkip.md` | 规矩二 DC Scale 档 |
| `02.07.13.21.12_rdi.tmu__.preScaler.md` | 规矩二 DC Scale 档 |

**`rdi.tmu__.*` 四篇的规矩二句子是同一段文字**（`R-rdi-same` 在四篇里各命中 2 次，
共 8 处），**与 [[smc-background-process-locks-config]] 里那条 TMLimits CAUTION 同源**——
**多篇不等于多次独立印证**（§10）。

文档事实，`verified: doc-only`。

## 这条约束怎么被发现的

**这一族是「先把数立起来」这个顺序救回来的。**
上一批把 RDI 列进待建族，依据只是一句印象式的「约 14 处」。

这一批先给 `rule_evidence.py` 加了两个键、跑出原文，
**立刻看见它是两条规矩而不是一条**（`inside` 与 `the same within one` 是两个句式），
以及**规矩一其实只有 2 篇**。

> **如果照上一批的记法直接写页**，我会把两条不同形状的规矩合成一段，
> 并且把「6 处」写成「横跨 6 篇」——**两个错都会是绿的**，
> 因为第七类只核引文、第九类只核链接，**它们都不核「我有没有把两条规矩合成一条」。**
