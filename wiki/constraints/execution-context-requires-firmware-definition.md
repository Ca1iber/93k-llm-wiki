---
type: constraint
title: 执行上下文必须先在固件级定义过，才能被引用
layer: L1
stage: pattern
tags: [constraint, pattern, execution-context, multiport, sequencer]
related: [[execution-context]], [[pattern]], [[sequencer]], [[label-edit-requires-tstl-selection]]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.135_NB_DIGITAL_CAPTURE_START.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.134_NB_DIGITAL_CAPTURE_END.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.136_NB_FUNCTIONAL_TEST.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.231.08_SMC_DIGITAL_CAPTURE_TEST.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.138_ON_FIRST_INVOCATION_BEGIN.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.139_ON_FIRST_INVOCATION_END.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.140_ON_LAST_INVOCATION_BEGIN.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.70_FOR_EACH_SITE_BEGIN.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# 执行上下文必须先在固件级定义过，才能被引用

## 约束是什么

有些 test method API 收一个 `exec_context` 参数。**这个上下文不能随用随起名字**——
它必须**先被定义出来**，而且文档要求定义发生在**固件级**。

文档把这条写成了三句话，**一句管定义、一句管端口归属、一句管名字怎么对上**：

> The context must have been defined on the firmware level (with the SQEC command), or as a SEQUENCER_CONTEXT_ITEM object. In the latter case this object must have been included in a SEQUENCER_CONTEXT object, and must also have been activated on the firmware level with the apply() function of this SEQUENCER_CONTEXT object. If the context has been defined as a SEQUENCER_CONTEXT_ITEM object, you must use the name specified for its name parameter.

> The ports of the context must be included in the current start label (which must be a multiport burst).

> NB_DIGITAL_CAPTURE_START and NB_DIGITAL_CAPTURE_END must be used as a pair.

## 在什么条件下成立

**这是 §2.4 的 D2（状态前提），不是 D1（顺序前置）**——
它要求的不是「先执行某条命令」，而是**「此刻这个上下文存在，且是在固件级存在的」**。
两者的差别很实在：**D1 你按顺序写就对了；D2 你要确认「它已经在那儿了」。**

### 定义有**两条路**，文档都写出来了

| 路 | 怎么定义 | 还要做什么 |
|---|---|---|
| 一 | 用 `SQEC` 命令 | —— |
| 二 | 建一个 `SEQUENCER_CONTEXT_ITEM` 对象 | ① 它必须被**收进**一个 `SEQUENCER_CONTEXT` 对象；② 那个对象必须**在固件级用 `apply()` 激活过** |

> **第二条路的三步是「必须」串起来的**，少一步都不算定义完成。
> 这是本页最容易漏的地方：**建了对象不等于激活了**，
> 文档单独用了一个从句说 `must also have been activated`。

### 名字有两种来源，**用错就引不上**

> If the context has been defined as a SEQUENCER_CONTEXT_ITEM object, you must use the name specified for its name parameter.

**这是 D3 一致匹配**：上下文的名字**必须与定义时的那个名字逐字相同**。
`SQEC` 定义的和对象定义的名字来源不同，**文档点明了这一条只在后者成立**。

### 端口有归属要求

> The ports of the context must be included in the current start label (which must be a multiport burst).

**这一条把上下文和 label 绑在一起**——上下文里的端口，
**必须是被当前 start label 覆盖的端口**；而那个 label **必须是 multiport burst**。
括号里的那半句本身又是一条前置条件（不是 multiport burst 就不成立）。

## 违反了会怎样

> **⚠️ 本次未找到任何描述报错形态的原文。**

我在这 13 篇文档里**没有找到**「上下文没定义会报什么错」的句子。
按 §11.1，**本页不猜**。工程上可能的形态（命令被拒 / 上下文为空 / 走默认）
**都是推断，不写进文档事实栏**。

**⚠️ 但要区分两件事**：这条约束**没有报错句**，
和 [[referenced-set-requires-prior-definition]]（那种集合**有**逐字报错句）
**不是一回事**。「文档没写」只等于「这篇没写」，
**不等于「违反了不报错」**——§2.1 那条铁律在这里就是本页的边界。

## 与之并列的一条：**成对使用**

同一批文档里还有一条**不同形状**的规矩：

> NB_DIGITAL_CAPTURE_START and NB_DIGITAL_CAPTURE_END must be used as a pair.

**这不是前置条件，是「配对」要求**——两个 API 必须成对出现。
它**不属于本页这条约束**，本页不合并它。

> **但它值得单独记一笔**：`must be used as a pair` 这个句式在语料里横跨 **6 篇独立文档**
> （`NB_DIGITAL_CAPTURE_START/END`、`ON_FIRST_INVOCATION_BEGIN/END`、
> `ON_LAST_INVOCATION_BEGIN/END`、`FOR_EACH_SITE_BEGIN`…），
> **是「BEGIN/END 类 API 成对使用」这个更大形状的一个实例**。
> **本页不替那个形状建页，也不对它声称任何事**——只把数记在这里：
> 出自 `extract/rule_evidence.py` 的 `C-pair` 键。

## 数字口径

| 键 | 命中 | 独立文档 |
|---|---|---|
| `C-execctx-fw`（固件级定义） | 13 处 / 13 行 / 13 文件 | **13 篇** |
| `C-execctx-name`（名字必须对上） | 13 处 / 13 行 / 13 文件 | **13 篇** |
| `C-execctx-port`（端口归属） | 14 处 / 14 行 / 14 文件 | **14 篇** |
| `C-pair`（成对使用） | 6 处 / 6 行 / 6 文件 | **6 篇** |

**三句几乎总是一起出现**（13 / 13 / 14），说明它们**是同一段文档模板**，
不是三篇各自写的三句话——**这削弱了「多篇印证」的强度**，
理由与 [[smc-background-process-locks-config]] 里那条同源（§10）。
数字出自 `extract/rule_evidence.py`，可重跑。

## 与 [[execution-context]] / [[pattern]] 的关系

[[execution-context]] 讲**执行上下文是什么、有哪些端口**；
本页讲**它必须先在哪儿定义出来**。
[[pattern]] 是它最终作用的对象——上下文决定的是「哪些端口一起跑」。

## 出处

| raw | 里面的原句 |
|---|---|
| `02.07.04.01.135_NB_DIGITAL_CAPTURE_START.md` | 定义两句（参数表）+ 端口归属句 + 成对句 |
| `02.07.04.01.134_NB_DIGITAL_CAPTURE_END.md` | 同段模板 |
| `02.07.04.01.136_NB_FUNCTIONAL_TEST.md` | 同段模板 |
| `02.07.04.01.231.08_SMC_DIGITAL_CAPTURE_TEST.md` | 同段模板 |
| `02.07.04.01.138_ON_FIRST_INVOCATION_BEGIN.md` | 成对句 |
| `02.07.04.01.139_ON_FIRST_INVOCATION_END.md` | 成对句 |
| `02.07.04.01.140_ON_LAST_INVOCATION_BEGIN.md` | 成对句 |
| `02.07.04.01.70_FOR_EACH_SITE_BEGIN.md` | 成对句 |

文档事实，`verified: doc-only`。

## 这条约束怎么被发现的

**先前的族名是对的，但我那一遍 grep 的结论差点把它判死。**
我用 `execution context` 去捞，129 处命中里绝大多数是参数表里的
`| exec_context | An execution context. For more information … |`——
**看起来像「这条规矩不存在，只是个参数名」**。

按当时记的行号回原文核，才看见参数表**下面那一格**就是这条规矩。

> **教训（本批第二次踩同一个坑）**：宽正则的命中**被印出来的前 N 条**限住了，
> 我照那 N 条下的判断——**「前 7 条」是一个不声不响的过滤器**，
> 它会让我把「在第 100 条」当成「不存在」。
> 这与 §13.1 常设问题②同源：**我印的这个数是谁算的？它有没有被截断？**
