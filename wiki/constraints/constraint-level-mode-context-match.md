---
type: constraint
title: level setup 的 mode context 必须与 pin configuration 一致
layer: L1
stage: level
tags: [constraint, mode-context, level, setup-consistency]
related: [[level]], [[pin]], [[timing]], [[ctxt]], [[constraint-timing-mode-context-match]]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.03.01.03.01_Mode_contexts.md
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.04.02.02_Mode_context_in_level_setup.md
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.04_Data_Organization_of_Equation_Based_Levels.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# level setup 的 mode context 必须与 pin configuration 一致

## 约束是什么

**一个测试要用哪个 mode context，必须在 level / timing / pattern 三处分别指定，而且三处必须相同。**
文档原句（**这是整条约束的总纲**）：

> Which of these contexts is to be used in a test, must be specified separately for the level, the timing and the vector setup. The selected context must be the same for all setup components. It is up to the user to ensure that this condition is met.

**本页只讲 level 侧**；timing 侧见 [[constraint-timing-mode-context-match]]。
pattern 侧由 `SQLA` 的 `PARA_MCTX` 属性给出（同一篇原文）：

> The mode context of a label (pattern) is defined with the PARA_MCTX attribute of the SQLA command.

## 在什么条件下成立

- **context 先在 pin configuration 里创建**：

  > User defined mode contexts are created in the pin configuration with the CTXT command.

  → [[ctxt]]

- **level setup 必须指派给它**。文档对 **fast / fast differential pin** 明写：

  > The level setup must be assigned to the mode contexts introduced in the pin configuration.

- **fast 与 fast differential 通道的 level 必须是 equation based**（同一篇，独立一句）：

  > A level setup with fast and fast differential pins must be equation based.

- **`MODECONTEXT` 行有位置要求**（同一篇）：

  > The mode context can be specified by keyword MODECONTEXT followed by the context name in quotes. This line must follow the line with the EQNSET keyword.

  **两句是同一段原文**：「`MODECONTEXT` 行必须跟在 `EQNSET` 行后面」。

## 违反了会怎样

> **⚠️ 系统不报错。** 文档把责任明确交给用户，原句是：

> It is up to the user to ensure that this condition is met.

**这是本页最要紧的一句。** 三处 context 不一致时，**没有一条文档说会报错**——
唯一给的检查手段是查询命令：

> You can retrieve the mode context of all setup components or a selected setup component with the GCTX? query.

**工程含义**：这类不一致**不会在加载/编译时拦住你**，只会在结果上错。
所以**建 setup 的自动化脚本必须自己调 `GCTX?` 做这一步校验**——
这正是「全栈自动化」里最容易被漏掉的一环：**文档明说了它不替你保证。**

> `GCTX?` 目前没有对象页，也不在 `extract/dangling.csv` 里 →
> 按 §9.1 本页写反引号、不写 `GCTX?`。

## 与 timing 侧的分工

| | level 侧（本页） | timing 侧 |
|---|---|---|
| 指定位置 | equation set 里的 `MODECONTEXT` 行（必须在 `EQNSET` 行之后） | wavetable 与 equation set **两处**都要写 |
| 一致性要求 | 与 pin configuration 里 `CTXT` 建立的 context 一致 | equation set 与 base wavetable 的 context 必须相同 |
| 谁保证 | **用户**（文档明写系统不保证） | 同左 |

## 出处

| 说法 | raw |
|---|---|
| 三处必须相同 / 用户自己保证 / `GCTX?` | `02.06.03.01.03.01_Mode_contexts.md` |
| `CTXT` 创建 context | 同上 |
| `PARA_MCTX` 定 pattern 的 context | 同上 |
| level 侧指派、fast 必须 equation based、`MODECONTEXT` 位置 | `02.06.05.01.04.02.02_Mode_context_in_level_setup.md` |
| equation based level 的数据组织 | `02.06.05.01.04_Data_Organization_of_Equation_Based_Levels.md` |

文档事实，`verified: doc-only`。

## 同类的一条：level 用了自定义 context，timing 也必须定义

`02.06.05.01.04.02.02` 里另有一句：

> If you use user defined mode contexts in the pin configuration and level setup, you must also define the timing for these contexts.

**这条把 level 侧和 timing 侧扣在了一起**：自定义 context 不是「level 里配上就行」，
timing 也必须为它定义。**违反后果同样未在文档里写明**——
和上面那条一样，属于「文档只给要求、不给报错」的一类。见
[[constraint-timing-mode-context-match]]。
