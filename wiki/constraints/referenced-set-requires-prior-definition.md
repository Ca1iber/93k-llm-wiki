---
type: constraint
title: 引用型集合必须先定义再引用，定义过的不能再定义
layer: L1
stage: pattern
tags: [constraint, pattern, setup, spec-set, jitter, transition-test]
related: [[pattern]], [[spec-set]], [[jsdf]], [[jscf]], [[jspr]], [[timing]], [[level]]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.11_BSVE_-__Bulk_Set_Value_Evaluation.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.12_BSVR__BSVR___Bulk_Set_Value_at_Runtime.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.92_DSVS__DSVS__-__Define_Spec_Value_Set.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.86_DPSR__DPSR__-__Define_Parallel_SeaRch.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.121_EXSR_-__EXecute_SeaRch.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.148_JSDF__JSDF__-__Jitter_Set_DeFinition.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.149_JSPR__JSPR__-__Jitter_Set_PRimary_set.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.288_TTDF__TTDF__-__Transition_Test_set_DeFinition.md
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.286_TTCF__TTCF__-__Transition_Test_ConFiguration.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# 引用型集合必须先定义再引用，定义过的不能再定义

## 约束是什么

固件命令里有一类**「集合」对象**——spec value set、search set、jitter set、
transition test set 等。它们**不是**在命令行里现写现用的，而是：

**先用一条「定义」命令建出来、起个名字；之后别的命令靠这个名字去引用它。**

于是有一条成对的约束，**两个方向都写进了 `## Errors` 段**：

| 方向 | 规矩 | 文档逐字报错 |
|---|---|---|
| 引用一个**没定义**的集合 | **报错** | `An error is generated if no jitter set with the specified name exists.` |
| 定义一个**已存在**的集合 | **报错** | `An error is generated if a jitter set with the specified name already exists.` |

> **这两句是本页的核心，而且它们是「同一条规矩的两面」。**
> 定义命令与引用命令**对同一个集合的存在性做方向相反的检查**——
> 这正是 §2.4 记的 **D3 一致匹配**：两处说法必须彼此相容，否则中间一定有一处是错的。

## 在什么条件下成立

**这是 §2.4 的 D1（顺序前置），不是 D2（状态前提）**——
它管的是「先后」，不是「此刻处于什么状态」。**先定义，后引用，顺序不能反。**

### 四个集合族的完整三段链

语料把这类对象写成了 **定义 → 配置 → 引用** 三段，命令名各有各的族：

| 集合 | 定义 | 配置 | 引用/使用 | 只用不配 |
|---|---|---|---|---|
| **spec value set** | `DSVS` | `BSVR` | `BSVE` | — |
| **search set** | `DPSR` | — | `EXSR` | ✅ 没有中间段 |
| **jitter set** | `JSDF` | `JSCF` | `JSPR` | — |
| **transition test set** | `TTDF` | `TTCF` | `TTPR` | — |

**「先定义」这句话在文档里是逐字写着的**，就在 `## Predependencies` 段：

> The spec value set must have been defined with the DSVS command, and the values must have been assigned with the BSVR command.

> The spec value set must have been defined with DSVS.

> The search set must have been defined with DPSR.

**定义命令的那一侧则写在 `## Postdependencies` 段**（同一件事，从另一头说）：

> After defining the spec value set, you must:

> - Define its value assignments with the BSVR command.

> - Trigger recalculation of the equation system with the BSVE command.

> **注意 `DSVS` 这条把「定义」和「赋值」分成了两步**——
> 定义只建壳，值要靠 `BSVR` 塞进去，最后还要 `BSVE` 触发重算。
> **三步少一步都不完整**，而文档只在前置段提了前两步、
> 第三步（`BSVE`）藏在后置段里。**这是只读一段就会漏的又一处**。

### 报错形态：**用「不存在」，不用「未定义」**

引用侧命令的报错句里，谓语是 `does not exist` / `exists`，
**不是** `is not defined`（我按后者 grep 过，**0 命中**，见下）：

> - The spec value set number does not exist.

> An error is generated if the spec value set number does not exist.

> - The specified search set does not exist

> An error is generated if no transition test set with the specified name exists.

**最后一句末尾没有句号，原文如此**（§11.1：不补标点）。

### 同一族里还有一条**容量**上限，别和存在性混起来

定义命令还会因为**数量到顶**而报错：

> - A transition test set with this name already exists,

> - The existing sets already exhaust the maximum number of transition test sets.

> - The search set number is greater than 128.

**「已存在」和「到上限」是两种不同的拒绝理由**，文档把它们并排列在同一段里。
`DPSR` 那句顺手给出了 search set 的**具体上限 128**——
**这是文档事实，不是推断**，但**它只写给了 search set，其他集合的上限文档没写数**。

## 违反了会怎样

**报错，句子逐字。** 这是本页与前两页的差别所在：

| 约束 | 报错形态 |
|---|---|
| 本页 | **文档逐字写了**（存在性与容量两类） |
| [[label-edit-requires-tstl-selection]] | 文档逐字写了（措辞两种） |
| [[pin-config-locked-during-test]] | **文档未写**，页面只能标 ⚠️ |

**同一批文档里，有没有写报错形态并不一致。**
所以「找不到报错句」**不等于**「违反了不报错」——只等于「这篇没写」。

## 范围：**本页只覆盖 4 个集合族，语料里这个形状比 4 族宽得多**

`must have been defined with` 这个措辞在语料里横跨 **22 篇命令文档**，
除上表四族外还出现在 `CFCF`（clock forwarding）、`PRCF`（PRBS）、`MSCF`（modulation set）、
`TSCF`（TMU set）、`WAVE`（waveform）、`VCAT`、`UPAS`、`SQLA`、`SQPG`、`TPSE`、
`MVVA`、`JSWF`、`RRSC`、`DFPC`、`DIDT`、`TTVD` 等。

> **⚠️ 本页对那另外约 18 篇不声称任何事。** 我只逐句读了上表四族，
> 它们的「三/两段链」是我**打开原文核过**的。
> 其余篇目只是被同一条正则扫到，**我没有读过它们的段**——
> 它们可能属于同一条规矩，也可能是别的形状。**§2.1：分不清就分开写。**

数字口径：报错段 21 处 / 21 文件 / **12 篇独立文档**；
前置措辞 55 处 / 38 文件 / **22 篇独立文档**。均出自 `extract/rule_evidence.py`
（键 `H-error` / `H-predep`），可重跑。

## 与 [[spec-set]] / [[jsdf]] / [[jscf]] / [[jspr]] 的关系

这四个对象页讲的是**集合本身是什么、有哪些参数**；本页讲的是
**它们的生命周期顺序**。**对象页回答「是什么」，约束页回答「什么时候能用」。**

## 出处

| raw | 里面的原句 |
|---|---|
| `02.06.02.02.11_BSVE_-__Bulk_Set_Value_Evaluation.md` | Predependencies 三段链句、`does not exist` |
| `02.06.02.02.12_BSVR__BSVR___Bulk_Set_Value_at_Runtime.md` | `must have been defined with DSVS.` |
| `02.06.02.02.92_DSVS__DSVS__-__Define_Spec_Value_Set.md` | Postdependencies 两步、`already exists` |
| `02.06.02.02.86_DPSR__DPSR__-__Define_Parallel_SeaRch.md` | `greater than 128` |
| `02.06.02.02.121_EXSR_-__EXecute_SeaRch.md` | Predependencies、`does not exist`（无句号） |
| `02.06.02.02.148_JSDF__JSDF__-__Jitter_Set_DeFinition.md` | `already exists` |
| `02.06.02.02.149_JSPR__JSPR__-__Jitter_Set_PRimary_set.md` | `no jitter set … exists` |
| `02.06.02.02.288_TTDF__TTDF__-__Transition_Test_set_DeFinition.md` | `already exists` + 到上限 |
| `02.06.02.02.286_TTCF__TTCF__-__Transition_Test_ConFiguration.md` | `no transition test set … exists` |

文档事实，`verified: doc-only`。

## 这条约束怎么被发现的

**靠 §2.4 的 D3 形状**——先注意到「同一族命令里，定义命令报『已存在』、
引用命令报『不存在』」，**这个对称太整齐，不像巧合**，顺着去核才发现
每组都配着一条 `must have been defined with`。

> **一次失败的尝试记在这里**：我最初按 `is not defined` / `not yet defined`
> 去 grep 报错句，**0 命中**（见 `extract/rule_evidence.py` 之外的那次全文扫描）。
> 语料用的是 `does not exist`。**如果我只跑一次 grep 就下结论，
> 会得出「文档没写报错形态」这个完全错误的结论。**
> 这与 §13.1 常设问题⑦同源：**给一个「没找到」找原因之前，先确认自己的模式对不对。**
