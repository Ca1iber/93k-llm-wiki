---
type: constraint
title: timing 的 equation set 与 base wavetable 必须同 mode context
layer: L1
stage: timing
tags: [constraint, mode-context, timing, wavetable]
related: [[timing]], [[level]], [[pattern]], [[ctxt]], [[constraint-level-mode-context-match]]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.03.01.03.01_Mode_contexts.md
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.05_Mode_context_in_timing_setup.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# timing 的 equation set 与 base wavetable 必须同 mode context

## 约束是什么

**一个 primary timing setup 指向的 timing equation set 和 base wavetable，必须属于同一个
mode context。** 文档原句（它在原文里是**一个 `Note`**，本节照抄正文）：

> The specification of a primary timing setup must include a pointer to a timing equation set and to a base wavetable of the same mode context. You cannot define a specification pointing to a wavetable and an equation set of different mode contexts.

**为什么**——同篇下一句给了机制：

> The mode context attribute of the timing equation set (which must be identical to the mode context attribute of the base wavetable) determines the overall mode context of a primary timing setup (timing context) containing that equation set.

**这个** primary timing setup **的 context 是从 equation set 继承来的**，
所以两者 context 不同时，这个 setup 的 context 就没有定义。
**本页只讲 timing 侧**；level 侧见 [[constraint-level-mode-context-match]]。

## 在什么条件下成立

- **context 写两处，而且必须一致**：

  > The mode context for the timing must be specified in both the wavetable and the equation set, and must of course be identical in both.

  **"must of course be identical in both"——原文如此**，语气词 `of course` 是原文的一部分（§11.1）。

- **每个 equation set 和每个 wavetable 都带一个 context**：

  > The timing setup specifies mode contexts in the timing equation sets and in the wavetables. That is, every timing equation set and every wavetable is associated with a mode context.

- **写在哪**（同篇，**完整一句**）：

  > The mode context can be specified by keyword MODECONTEXT followed by the context name in quotes. This line must follow the line with the EQNSET keyword and is to be added to the timing equation set and the wavetable.

  **注意后半句：timing 侧的 `MODECONTEXT` 行要加到「equation set **和** wavetable」两处。**
  这比 level 侧同一条**更严**——level 侧只说位置（`This line must follow the line with the
  EQNSET keyword.`），timing 侧还规定了要写进两个地方。见
  [[constraint-level-mode-context-match]]。

  > **⚠️ 本页初稿在这里差点写出一句假话，记一笔。**
  > 我当时看到的引文末尾是 `is to be added to the timin`，就准备写「**raw 里这句是断的**」。
  > 实际是**我自己打印时按 1900 字符截断的**——raw 里这句是完整的。
  > **`is to be added to the timin` 这种断法，语料和我自己的工具长得一模一样。**
  > 差一点就把「我的工具截断了」写成「语料截断了」，而那是一条**关于语料的主张**，
  > 会被下一个 agent 当成事实用（§13 第十次的同族：**漏的不是范围，是我没分清
  > 这个数是页面算的还是我算的**）。**发现途径**：写进去之前回去 `grep` 了那半句的结尾。
  > → 第五个常设问题：**「我引的这半句，是语料断了，还是我印断了？」**

## DEFAULT context 是什么

> If you do not explicitly specify a mode context, the mode context "DEFAULT" is set.

> The timing equation set and the wavetable for the mode context "DEFAULT" define the timing for all pins with a mode = std (not FAST pins), that is for pins without any FAST specifics.

**工程含义**：**不写 `MODECONTEXT` = 只覆盖 std pin，FAST pin 不在内**。
用了 FAST 通道却没建自定义 context，**timing 就没有覆盖到那些 pin**——
**这个坑不是「报错」，是「静默不覆盖」。**

> 上面这条「静默不覆盖」的措辞是**本页的推断**（两句文档事实合起来得出的），
> 文档没有直接写「FAST pin 会没有 timing」。**推断链**：① 不写 context 就是 DEFAULT；
> ② DEFAULT 只定义 mode = std 的 pin 的 timing。→ FAST pin 不在 DEFAULT 的覆盖范围内。
> **上机验证**：建一个含 FAST pin 的 setup，不写 `MODECONTEXT`，用 `GCTX?` 查它的 context，
> 再看 FAST pin 的 timing 从哪里来。

## 违反了会怎样

> **⚠️ 文档只写了 "You cannot define"，没写报错形态。**

"You cannot define a specification pointing to a wavetable and an equation set of different mode contexts."
——**这句是禁止，不是后果描述**。它是「工具不许你这么定义」，还是「你定义了但不生效」，
**本次未找到说明**。

**同族的一条总纲**（`Mode_contexts` 那篇，也适用于 timing）：

> The selected context must be the same for all setup components. It is up to the user to ensure that this condition is met.

**系统不替你保证**；查的手段是 `GCTX?`（同上）。**自动化里必须自己调它做校验。**

## 出处

| 说法 | raw |
|---|---|
| equation set 与 base wavetable 同 context / 继承机制 / `MODECONTEXT` 行 / DEFAULT 语义 | `02.08.04.34.05_Mode_context_in_timing_setup.md` |
| 三处必须相同、用户自己保证、`GCTX?`、两处都要写且必须相同 | `02.06.03.01.03.01_Mode_contexts.md` |

文档事实，`verified: doc-only`。

## 相关约束

- [[constraint-level-mode-context-match]]——level 侧的那一半。
- [[ctxt]]——在 pin configuration 里创建 context 的命令（**尚未建页**，是悬空目标）。
- [[pattern]]——pattern 侧的 context 由 `SQLA` 的 `PARA_MCTX` 给出。
