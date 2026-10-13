---
type: object
title: SQST, SQST? - (SeQuencer STate)
layer: L1
stage: pattern
tags: [sequencer, state, sqst, execution-context, global-context, run, brk, halt, off, ac-test, dps128-dps64]
related: [execution-context, sequencer-status, sequencer, dps128-dps64-cards, smartest-7.2.0, smartest-6.3.2]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.241_SQST__SQST__-__SeQuencer_STate.md
created: 2026-09-18
updated: 2026-09-20
verified: doc-only
---

> ⚠️ **本页若干处记的是 2026-10-10【之前】的语料形态。**
> 那一轮把语料里的表格一律换成了**指向上游 HTML 的指针**
> （见 `extract/PLAN-表格指针化.md`）。所以下文凡是说「表格被压平 / 被摊平 /
> 一格一行」的地方，指的是**更换之前**的样子 —— 现在语料里那个位置是**一句指针**，
> 真表仍在 `tdc-html/raw/` 的上游 HTML 里。**页码/引文都不受影响。**

# SQST, SQST? - (SeQuencer STate)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **533 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.241_SQST__SQST__-__SeQuencer_STate.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### SQST

SQST {seq_state} [,"exec_context"]

### SQST?

```
SQST? ["exec_context"]
```

returns:

```
SQST {seq_state}
```

### Parameters

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98752.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：9 行 × 3 列。
> 首行（上游原文）：seq_state | Gives the state of the sequencer:
> 表内引用（2 条，供检索）：`SQGB, SQGB? - (SeQuencer GloBal)`（raw: `02.06.02.02.232_SQGB__SQGB__-__SeQuencer_GloBal.md`） · `Using execution contexts`（raw: `02.06.07.01.08.05.03.02.03_Using_execution_contexts.md`）

### Example

```
SQST RUN
```

This example starts a global sequencer run.

<!-- 语法节 end -->

## 是什么

**`SQST` 是「控制一组 sequencer 的状态」的 L1 命令；`SQST?` 是它的查询版。**

> 「The SQST command serves to control the state of a set of sequencers.」

### 第一件要知道的事：**「一组 sequencer」= 一个 execution context**

> 「This sequencer set is determined by an execution context which consists of a list of ports;
> it comprises the sequencers that belong to these ports. The ports of a user defined execution
> context must be a subset of the ports that are contained in the current start label.
> **The port set of this label constitutes the global execution context.**」

**这一段里藏着本页最关键的等价关系**：

| 概念 | 原文定义 |
|---|---|
| **execution context** | **`a list of ports`**；**它包含「属于这些 port 的那些 sequencer」** |
| **user defined execution context** | **端口必须是当前 start label 端口的子集** |
| **global execution context** | **`The port set of this label`**——**即：当前 start label 的端口集** |

**所以「全局」不是「所有 sequencer」，而是「当前 start label 那一组」。**
**这条区分决定了下一条规矩。**

### 第二件事：**哪些状态能按 context 设，哪些不能**

> 「Some sequencer states can be set only for the global execution context, and this implies that
> all user defined contexts will also be set into this state. But the RUN and (indirectly also)
> the BRK state can be assigned on the execution context level.」

| 状态 | 能指定到 context 吗 | 后果 |
|---|---|---|
| **`OFF`** / **`HALT`** / **`BRK`** | **不能——只能对全局** | **一把设下去，所有 user defined context 一起进这个状态** |
| **`RUN`** | **能**（`can be assigned on the execution context level`） | 可以只起一个 context |
| **`BRK`（间接）** | **「indirectly also」**——**因为 `ABRT` 是把某个 context 从 `RUN` 打到 `BRK`** | 见下 `ABRT` |

> **⚠️ 表里 `BRK` 这一格原文自己是有张力的**：前一句说「有些状态只能全局设」，
> 后一句又说 **`the RUN and (indirectly also) the BRK state can be assigned on the execution
> context level`**。而参数表里 `BRK` 那一条写的是
> `This option can only be applied to all execution contexts.`
> **即：`BRK` 作为「状态」只能全局设，而通过 `ABRT` 这个「指令」可以在 context 级达到 `BRK`。
> 原文用 `indirectly also` 正是这个意思。本页照实并列，不替它调和。**

### 六个 `seq_state`：**四个是状态，两个不是**

原文参数表列了六个值。**原文自己分得很清**——`ABRT` 与 `CBRK` 两条都以
**`This is not a sequencer state, but …`** 开头：

| 值 | 是状态吗 | 原文 |
|---|---|---|
| **`OFF`** | 是 | `In the OFF state, both the sequencers and the clock are off. All pins go into the high-z state.` + `This option can only be applied to all execution contexts.` |
| **`HALT`** | 是 | `In the HALT state, both the sequencer and the clock are off, and the drivers keep their last level or remain in high-z state if already in high-z state.` + 一条禁令（见下）+ `This option can only be applied to all execution contexts.` |
| **`BRK`** | 是 | `In the BRK state, the clock is on and the break waveform is applied to the DUT.` + `This option can only be applied to all execution contexts.` |
| **`RUN`** | 是 | `In the RUN state, the clock is on and the sequencer applies vectors to the DUT. This option can be applied to a specified execution context.` |
| **`ABRT`** | **不是** | `This is not a sequencer state, but an instruction to change the state of an execution context from RUN to BRK. ABRT requires that an execution context is specified.` |
| **`CBRK`** | **不是** | `This is not a sequencer state, but a conditional instruction. If no context is in BRK or RUN state, the state of the global context will be changed to BRK. If any context is in BRK or RUN state, nothing will be done.` |

**四个状态的「时钟 / 引脚」对照（这是本页最实用的一张表）**：

| 状态 | 时钟 | 引脚 |
|---|---|---|
| **`OFF`** | **off** | **`All pins go into the high-z state.`** |
| **`HALT`** | **off** | **保持上一电平**；**如果本来就在 high-z 就留在 high-z** |
| **`BRK`** | **on** | **`the break waveform is applied to the DUT`** |
| **`RUN`** | **on** | **`the sequencer applies vectors to the DUT`** |

> **`OFF` 与 `HALT` 的差别就在引脚上**：**`OFF` 把引脚全推成 high-z，`HALT` 保持住**。
> **`BRK` 与 `RUN` 的差别也在引脚上**：**`BRK` 送的是 break 波形，`RUN` 送的是向量**
> （两者的时钟**都是 on**）。

### 一条**路径禁令**：`HALT` 和 `OFF` 不能直达

> 「Note that you cannot pass directly from HALT to OFF or from OFF to HALT.
> You must first pass to BRK in both cases.」

**即 `OFF ⇄ HALT` 必须经过 `BRK`：`OFF → BRK → HALT`、`HALT → BRK → OFF`。**
**（这也解释了为什么 `BRK` 被原文列进「indirectly also」那一档。）**

### 一条**隐含前置**：`OFF` / `BRK` → `RUN` 时**用的是 `SQGB` 的全局设置**

这一条在原文里**写在参数表的 `RUN` 那一格下面**（**不是独立段落**）：

> 「Note that if the sequencer state changes from OFF or BRK to RUN, the sequencer runs with the
> global settings that have previously been defined with SQGB, SQGB? - (SeQuencer GloBal).」

**所以「起 sequencer」这件事**同时**依赖 `SQGB` 里先前定义过的全局设置**——
**本页与 `SQGB` 的依赖关系原文开头也点了一次**：
`There are dependencies to the command SQGB, SQGB? - (SeQuencer GloBal), see below.`

### `exec_context` 参数：**只能配 `RUN` 和 `ABRT`**

> 「An execution context. In the command, this parameter can only be added to the sequencer state
> RUN and the instruction ABRT. **It must be added if ABRT is specified.** For more information on
> execution contexts see Using execution contexts .」

**两句硬规矩**：① 命令里它**只能**跟在 `RUN` 或 `ABRT` 后面；
② **`ABRT` 时是**必须**给的**（`It must be added`）——**`ABRT` 不带 context 是非法的**。

**查询侧另有一条**（`exec_context` 那一格的最后一句）：

> 「If the query is issued without a context, then RUN will be returned if there is at least one
> context that is in the RUN state.」

**即：`SQST?` 不带 context 时，只要有**任意一个** context 在 `RUN`，就回 `RUN`。**
**而原文开头把这条概括成一句**：

> 「The SQST? query returns the maximum current state.」

**两句话说的是同一件事**——**「最大值」就是「只要有一个在跑就算在跑」**
（推断：依据是两句并列，**原文没有用这种措辞解释「maximum」**）。

### 语法两行（**原文的写法不对称**）

原文给了两段：

```
SQST {seq_state} [,"exec_context"]
```

```
SQST? ["exec_context"]
```

returns：

```
SQST {seq_state}
```

**⚠️ 注意 `SQST` 那一行在原文里**没有**放进代码块**（是裸文本），
而 `SQST?` 与返回值那两段都在代码块里。**本页照原样引了两者的内容，
但在上面按同一形状排了版——原文的形状不是这样**（见「出处」⚠️②）。

**语法行与参数说明之间有一处不严丝合缝**：语法行把 `exec_context` 写成**可选**（方括号），
**而参数表说它**只能**配 `RUN` / `ABRT`**。
**两者不矛盾**（可选 ≠ 处处可用），**但只看语法行会以为任何状态都能带 context。
本页照实并列，不替它改写语法行。**

### `## Application`：**AC 测试**

> 「AC tests.」

> 「Connect or disconnect the test system, see Relays Control Commands.」

**即原文把本命令的应用场景写作「AC 测试」，并把「连接 / 断开测试系统」指向
`Relays Control Commands`**——**那一篇本页没读。**

### 一条针对 DPS128/DPS64 的警告

> 「Note that the DPS128/DPS64, when starting the sequencer with `SQST RUN` or with the
> SEQUENCER_STATUS run() test method, cannot execute dynamic and static DC actions in parallel.
> Use profiling for measurements in parallel to a dynamic pattern.」

**这条把本页（L1 命令）与 [[sequencer-status]]（L3 test method API）在**同一句话里并列**了**——
**两条路起 sequencer 的效果一样，限制也一样。**（见「和谁有关」）

## 典型用法

**⚠️ 本文档的 `## Example` 只有一行、一句说明：**

```
SQST RUN
```

> 「This example starts a global sequencer run.」

**所以本文档给的「用法」只有这一个**：**`SQST RUN` = 起一次全局 sequencer run。**
**下面四条是本页从语法 / 参数两节拼出来的，原文没有给成对的步骤。**

**1. 起全局**：`SQST RUN`（不带 `exec_context`）——
**按参数表的说明，这就是对全局 context 设 `RUN`。**
**注意前置**：`OFF` / `BRK` → `RUN` 时**用的是 `SQGB` 先前定义的全局设置**。

**2. 只起某一个 context**：`SQST RUN,"context名"`——
**`RUN` 是唯一能配 `exec_context` 的状态**。
（**这个用法在 [[execution-context]] 那篇的示例里出现过**，
**但那篇本页没读、本页也没从那儿引任何内容**；**此处只说本页原文允许它。**）

**3. 把某个 context 从 `RUN` 打到 `BRK`**：`SQST ABRT,"context名"`——
**`ABRT` 必须带 context**。

**4. 条件性地打进 `BRK`**：`SQST CBRK`——
**「没有任何 context 在 `BRK` 或 `RUN` 时才把全局打到 `BRK`，否则什么都不做」**。
**这是一个「只在空转时才打断」的指令**（**推断**：这是对原文
`If no context is in BRK or RUN state, the state of the global context will be changed to BRK.
If any context is in BRK or RUN state, nothing will be done.` 的字面改写，**原文没有给用途**）。

**5. 关掉**：`SQST OFF`——**引脚全 high-z**。
**要从 `RUN` 到 `OFF`，必须先经过 `BRK`**（`OFF ⇄ HALT` 的禁令加上 `RUN → BRK` 的自然路径）。

**6. 查状态**：`SQST?` 或 `SQST? "context名"`，回 `SQST {seq_state}`。
**不带 context 时是「取最大」**——只要有一个 context 在 `RUN`，就回 `RUN`。

**7. 顺序上的两个约束（本页最该记住的两条）**：

- **`OFF ⇄ HALT` 必须过 `BRK`**——**不能直达**。
- **`ABRT` 必须带 context**——**不带就是错的**。

## 和谁有关

**同一套机制的两个入口（L1 命令 vs L3 API）**：

- [[sequencer-status]] — **原文在同一句话里把两者并列**：
  `when starting the sequencer with SQST RUN or with the SEQUENCER_STATUS run() test method,
  cannot execute dynamic and static DC actions in parallel.`
  **即：`SQST RUN` 与 `SEQUENCER_STATUS.run()` 是「起 sequencer」的两条路，
  连限制都共用同一条。** 本页是命令侧，那页是 test method API 侧。
  **那页本页没读**——**两页的状态词是不是同一套，本页不判**
  （**本页这一篇里用到的状态是 `OFF` / `HALT` / `BRK` / `RUN` 四个**）。
- [[execution-context]] — **本页的 `exec_context` 参数就是它**：
  原文两处指过去（`For more information on execution contexts see Using execution contexts`），
  **并且本页开头那段「sequencer set = execution context」「全局 context = start label 的端口集」
  就是那套概念在本命令里的用法。**
  **那页本页没读。**

**被本页点名、本页没读的（均未建，不链）**：

- `SQGB, SQGB? - (SeQuencer GloBal)` — **本页与它有明确依赖关系**：
  **`OFF` / `BRK` → `RUN` 时 sequencer 用的是 `SQGB` 先前定义的全局设置。**
  **本页只转述了原文这一句，`SQGB` 里那些设置是什么本页不知道。**
- `Relays Control Commands` — **`## Application` 一节指向它**
  （`Connect or disconnect the test system`）。
  **本页只有这一句转述。**
- `Profiling of DC Scale cards with Hardware view` — **DPS128/DPS64 那条说要改用
  profiling**；**profiling 是什么本页没有。**

**同一条线上的**：

- [[sequencer]] — 本页控制的是**那些跑 sequencer program 的东西的状态**；
  **那页是「程序里写了什么」，本页是「跑不跑、停在哪一态」。**（**那页本页没读**）
- [[dps128-dps64-cards]] — **本页那条警告针对的就是这张卡**：
  **用 `SQST RUN` 起 sequencer 时，它不能并行执行 dynamic 与 static DC 动作。**
  **那页本页没读。**
- [[smartest-7.2.0]] — **本页版本记录里的那一版**（见「版本」）。
  **执行 context 与 `ABRT` 都是 7.2.0 进来的**，**所以「按 context 控制状态」这个用法
  在 7.2.0 之前不存在。**

> **本页的「和谁有关」全部来自这一篇原文里点到的名字。**

## 版本

本文档有 `## Functional changes` 段，**全部内容两条**：

- **`Introduced before SmarTest 6.3.2`**
- **`SmarTest 7.2.0: An execution context can now be specified for the RUN and the new ABRT option.`**

> **第一条 `Introduced before SmarTest 6.3.2` 是哨兵值，不是「6.3.2 的变更」。**
> 按 §11.2 ②，`before` 的意思是「**在本文档集覆盖范围开始之前就已经有了**」——
> 全语料 2,677 条可用性行都是这个写法，**照字面读会造出一条格式齐整的假信息。**
> **所以本页只能说：`SQST` 本身在本文档集覆盖范围之前就存在。**
>
> **第二条是一条**真版本记录**（措辞是 `SmarTest 7.2.0:`，不是 `before`）**，
> **而且它一次记了两件事**：
> **① `RUN` 现在可以指定 execution context；② `ABRT` 是新增的选项。**
>
> **把这一条和正文对起来读，能得出一条**硬结论**：
> **7.2.0 之前，`SQST` 只能对全局 context 操作，也没有 `ABRT`。**
> **即本页「典型用法」里的第 2 条（只起某一个 context）与第 3 条（`ABRT`）
> 在 7.2.0 之前都写不出来。**
> （**推断**：依据是版本记录只说了 `RUN` 与 `ABRT` 两项，
> **而 `CBRK` 不在其中——`CBRK` 是不是 7.2.0 一起进来的，本文档没说，本页不推断。**）
>
> **对照页**：[[smartest-7.2.0]] / [[smartest-6.3.2]]（**均未建**）——
> **两版的覆盖范围本页都没读。**

## 出处

`sources:` 一篇：
`02_System_reference/02.06_Command_Reference/02.06.02.02.241_SQST__SQST__-__SeQuencer_STate.md`
（raw 的 `source_topic: "98752.htm"`）。

**本页没做的**：

- **`Using execution contexts`（[[execution-context]]）没读**——
  **而本页开头整段概念（context、全局 context、port 子集）都建立在这一篇的转述上。**
  **那篇里 context 怎么定义、怎么起、有哪些限制，本页一个字都没有。**
- **`SQGB, SQGB? - (SeQuencer GloBal)` 没读**——
  **所以「`OFF` / `BRK` → `RUN` 时用的那些全局设置」是什么，本页不知道。**
- **`SEQUENCER_STATUS`（[[sequencer-status]]）没读**——
  **DPS128/DPS64 那条把两条路并列了，另一条路的细节本页没有。**
- **`Relays Control Commands` 没读**——**`## Application` 那两行（`AC tests.` 与
  `Connect or disconnect the test system`）指向它，但怎么连怎么断本页没有。**
- **`Profiling of DC Scale cards with Hardware view` 没读。**
- **`DPS128/DPS64` 那张卡本页没读**——**那条警告的全部依据就是原文那一句。**
- **原文没有 `## Procedure`、没有 `Before you begin`、没有 `What to do next`、
  没有 `Related information`。**
  **`## Example` 只有一行 `SQST RUN`。**
  **所以「典型用法」一节的第 1–7 条是本页从语法行与参数表拼出来的，不是原文给的步骤**——
  本页在那一节开头已声明这一点，并在每一条里标了原文依据。
- **没有任何图。** 本篇没有图片引用。
- **`SQST?` 到底回什么字符串、`SQST? "context名"` 的返回形状**——
  **原文只给了 `SQST {seq_state}` 这一个返回模板**，
  **带 context 的查询返回什么，语料未写。**

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> **① `OFF` 与 `HALT` 两条的说明里，`sequencer` 的单复数不一致。** 逐字：
> `In the OFF state, both the sequencers and the clock are off.`（**复数 `sequencers`**）
> 而紧接着的 `HALT` 那条是
> `In the HALT state, both the sequencer and the clock are off, and the drivers keep their last
> level or remain in high-z state if already in high-z state.`（**单数 `sequencer`**）。
> **同一张表相邻两格，一个复数一个单数。**
>
> **② 两段语法行的排版不对称。** 原文的 `## SQST` 一节下，
> `SQST {seq_state} [,"exec_context"]` 是**裸文本行**（没有代码块）；
> 而 `## SQST?` 一节下，`SQST? ["exec_context"]` **在代码块里**。
> **同一种东西两种排法。本页正文把两者都按代码块呈现了，这是本页的排版，不是原文的。**
>
> **③ 一处链接与句号之间多一个空格。** 逐字：
> `For more information on execution contexts see [Using execution contexts](<02.06.07.01.08.05.03.02.03_Using_execution_contexts.md>) .`
> ——**`>` 与 `.` 之间有一个空格。**（**同一篇正文开头引同一个链接时没有这个空格**，
> 见 `For more information on execution contexts see [Using execution contexts](<…>).`）
>
> **④ `## Parameters` 是一张被拆成「一格一行」的大表。**
> 逐字：`|` /（空行）/ `seq_state` /（空行）/ ` |` /（空行）/ `Gives the state of the sequencer:` /
> （空行）/ ` |` /（空行）/ ` |` /（空行）/ `OFF` /（空行）/ ` |` /（空行）/
> `In the OFF state, both the sequencers and the clock are off. All pins go into the high-z state.` /…
> ——**每个单元格各占一行，格与格之间夹空行**；
> 脚本只认连续 ≥3 行的管道行，**所以这一节里的表在「语法 / 参数」节里是散着的**。
> 与 [[xps256-status-flags]] 那 18 张表是同一类成因（HTML 表格转 markdown 被拆散）。
> **逐字没丢，只是形状变了。**
>
> **⑤ 一条重要说明被放进了表格**内的**一格**。**
> 逐字：`Note that if the sequencer state changes from OFF or BRK to RUN, the sequencer runs with
> the global settings that have previously been defined with SQGB, SQGB? - (SeQuencer GloBal).`
> —— 它在语料里紧跟 `RUN` 那格的正文，**是**同一格**的一部分，不是独立段落**。
> **本页在「是什么」里把它单列成一条，那是本页的整理。**
>
> **⑥ 「`BRK` 能不能按 context 设」在原文里两处措辞不一致。**
> 正文写 `But the RUN and (indirectly also) the BRK state can be assigned on the execution
> context level.`，而参数表的 `BRK` 格写
> `This option can only be applied to all execution contexts.`
> **本页照实并列了两处，并在正文里标出这一点。**

`verified: doc-only`
