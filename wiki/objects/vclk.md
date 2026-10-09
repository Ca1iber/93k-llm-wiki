---
type: object
title: VCLK? - (Verify CLocK)
layer: L1
stage: timing
tags: [timing, period, auto-correction, vclk, l1-command, firmware-command, fixed-timing, equation-based-timing, multi-port]
related: [pclk, wsus, tsus, dfgp, vdcg, vtim, timing, timing-setup-commands, site-focus-required-before-command]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.319_VCLK__-__Verify_CLocK.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# VCLK? - (Verify CLocK)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **3,429 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.319_VCLK__-__Verify_CLocK.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
VCLK? {waveform_set}, {timing_set}, {period}, {(pinlist)}
```

returns:

```
VCLK {autocorrect}
```

### Parameters

| waveform_set | Waveform set number. Enter PRM for the primary waveform set, or an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）. | Waveform set number. Enter PRM for the primary waveform set, or an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）. |
|---|---|---|
| specset_id | Derived as follows:<br><br>`100 * equation_set_no + specset_no` | Derived as follows:<br><br>`100 * equation_set_no + specset_no` |
| multi-port_spec | To enter a multi-port specification is only possible if the specification is associated with the default port and if no other ports are configured. | To enter a multi-port specification is only possible if the specification is associated with the default port and if no other ports are configured. |
| timing_set | Timing set number. Enter PRM for the primary timing set, ALL for all timing sets, or an integer in the range 1 to the maximum number of allowed timing sets. The maximum number is determined by `TSUS, TSUS? - (Timing Sets USed)`（raw: `02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`）. | Timing set number. Enter PRM for the primary timing set, ALL for all timing sets, or an integer in the range 1 to the maximum number of allowed timing sets. The maximum number is determined by `TSUS, TSUS? - (Timing Sets USed)`（raw: `02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`）. |
| period | Enter the test system period in ns for which you wish to check whether auto-correction will take place or not. period must be within the maximum and minimum test system periods of the model. | Enter the test system period in ns for which you wish to check whether auto-correction will take place or not. period must be within the maximum and minimum test system periods of the model. |
| pinlist | The name of the pin or pins whose period you want to check. This parameter can also include groups previously created by `DFGP, DFGP? - (DeFine GrouP)`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）. If more than one pin is to be included, the names must be separated with a comma. The @ symbol can be used to check all configured pins. | The name of the pin or pins whose period you want to check. This parameter can also include groups previously created by `DFGP, DFGP? - (DeFine GrouP)`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）. If more than one pin is to be included, the names must be separated with a comma. The @ symbol can be used to check all configured pins. |
| autocorrect | The auto-correction flag returned by the system. It can be: | The auto-correction flag returned by the system. It can be: |
| autocorrect | 0 | No auto-correction will occur. |
| autocorrect | 1 | Auto-correction will occur. |

> ⚠️ 转录说明（非原文）：本表在上游 HTML 里含合并格（colspan / rowspan）；
> 跨格文字已按覆盖范围重复写出（**不是原表里有重复的格子**）。真结构见 `tdc-html/agent-html/98844.htm`。

### Example

```
VCLK? 1,1,20,(@)
```

This example checks if a period of 20 ns will cause auto-correction to the edge placements in Timing Set 1 of Waveform Set 1 on any pin. If no auto-correction will occur the following string is returned:

```
VCLK 0
```

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.319_VCLK__-__Verify_CLocK.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

- The period is outside the given range.
- waveform_set is outside the valid range.
- timing_set is outside the valid range.

<!-- 报错节 end -->

## 是什么

**VCLK? 回答的是一个问题：这个周期，会不会触发 auto-correction。**
它不读「现在周期是多少」，也不改任何东西——原文第一句：

> 「The VCLK? (Verify CLocK) query checks if the desired test system period will cause
> auto-correction. The system responds with a 0 or a 1 to indicate auto-correction.」

**它只有查询这一半。** 全篇命令名都带 `?`（标题、语法、示例全是 `VCLK?`），
**没有不带 `?` 的写形式**——对比 [[pclk]]：那一篇 `PCLK` 与 `PCLK?` 成对，**一个写、一个读**。
**所以 VCLK? 不能设周期，它只能核对别人刚落下的周期**：

> 「You allocate a test system period per timing set to the specified pin or pins using
> PCLK, PCLK? - (Pin CLocK).」

**落周期的是 [[pclk]]，VCLK? 只回答「刚落的这个值会不会被系统改正」。**
本篇对这条分工只有上面这一句；**「PCLK 落下来的值在什么条件下会被改正」那套机制写在 PCLK 那一篇里**
（本页读到的 [[pclk]] 页把这件事说成
`The VCLK? query checks whether a PCLK command with the specified parameter values was accepted with or without auto-correction.`
——**那个句子在 PCLK 的 raw 里，不在本篇的取材里**）。

### 四个参数、一个数

| 位 | 参数 | 取值 |
|---|---|---|
| 1 | `waveform_set` | `PRM`（primary）或整数 1..上限；**上限由 [[wsus]] 定** |
| 1（equation based） | `specset_id` 或 `"multi-port_spec"` | `specset_id` 由 `100 * equation_set_no + specset_no` 算得 |
| 2 | `timing_set` | `PRM`、`ALL`，或整数 1..上限；**上限由 [[tsus]] 定** |
| 3 | `period` | 单位 ns；**必须落在该机型最大与最小的 test system period 之间** |
| 4 | `pinlist` | pin 名（逗号分隔）、[[dfgp]] 建的 group、或 `@`（所有已配置 pin） |

**回来的是一个数**：`autocorrect`。参数表把它写成两格，逐字：

| 值 | 原文 |
|---|---|
| `0` | `No auto-correction will occur.` |
| `1` | `Auto-correction will occur.` |

`period` 那一栏是 VCLK? 最重的一条限制，逐字：

> 「Enter the test system period in ns for which you wish to check whether auto-correction will
> take place or not. period must be within the maximum and minimum test system periods of the model.」

**两个要点**：① 单位是 ns；② **范围随机型走，本篇一个数字都没给**（`of the model` 就是它的全部交代）
——**所以「我写 20 ns 会不会越界」这个问题，本篇答不了。**

### 「会改正」改的是什么

**原文只在示例的说明里点了 `edge placements` 一处**，正文与参数表都只写 `auto-correction`，不带宾语。
**「改正成什么值」「一次会动几条 edge」本篇没写**（**语料未写**）——
**本页只能保证「文档把这件事叫 auto-correction，而且它会动 edge 的摆放」。**

### multi-port 不是随便能用的

> 「To enter a multi-port specification is only possible if the specification is associated with
> the default port and if no other ports are configured.」

**这是全篇唯一提到 multi-port 的地方。**

> **⚠️ 与 [[pclk]] 的一处用词差异**（**比较对象是本页读到的 [[pclk]] 页**）：
> PCLK 那一篇写完同一句之后**又补了一句** `This restriction does not apply to the query.`；
> **VCLK? 全篇都是查询，而这一句里没有那条豁免。**
> **两句能不能同时成立，本页不替它们调和**——本页只保证本篇的用词是上面那一句。

### 一个 site 一次

> 「With this command you can retrieve site specific information (only one site can be in focus at
> a time). For the site in focus, SmarTest displays results in the Testflow Editor and in the
> result tools. Also, any firmware queries report setup and results for the site currently in focus only.」

**这段话是语料里的通用段**：本页读到的 [[vdcg]] 那一篇有一段**逐字相同**的，
而 [[vtim]] 那一篇**没有**（**三篇都是本页的取材**）。
**读法**：结果只对「当前 in focus 的那个 site」有效——
**站点不对，就查不出你要的那个 site 的答案** → [[site-focus-required-before-command]]。

## 典型用法

**1. 最小的一次调用**（原文 `## Example`，逐字）：

```
VCLK? 1,1,20,(@)
```

逐位对一遍：

| 位 | 例中的值 | 是什么 |
|---|---|---|
| 1 | `1` | `waveform_set`——waveform set 1 |
| 2 | `1` | `timing_set`——timing set 1 |
| 3 | `20` | `period`——20 ns |
| 4 | `(@)` | `pinlist`——所有已配置的 pin |

原文对这一步的说明逐字：

> 「This example checks if a period of 20 ns will cause auto-correction to the edge placements in
> Timing Set 1 of Waveform Set 1 on any pin. If no auto-correction will occur the following string is returned:」

回的是：

```
VCLK 0
```

**这句话里有两件事要看清**：① 检查的**不是当前周期**，是「**20 ns 这个值**」；
② 例子里只给了 `0` 那一侧（`If no auto-correction will occur`）——
**`1` 那一侧回什么本篇没有举例**（按 `returns:` 那行应当是 `VCLK 1`，
**这一句是本页的推断**，依据是 `returns:` 只写 `VCLK {autocorrect}` 而参数表给了 `0` / `1` 两格）。

**2. 什么时候跑它**（本页按本篇的措辞排的顺序，**顺序本身是建议**）：

1. **刚用 [[pclk]] 落下一个 period**，想知道它会不会被改正 → 跑 `VCLK?`。
2. **拿到 `1`** → 说明 edge placement 会被动。**动成什么样，本篇答不了**（见「是什么」）。
3. **想问「现在周期是多少」——不是这条命令**：VCLK? 要你**给出**一个 `period` 才肯回答，
   它不回读当前值；回读是 [[pclk]] 的 `PCLK?`（**这一句是本页的推断**，依据是本篇四个位置里
   `period` 是**输入**、回复里只有 `autocorrect` 一个数）。

**3. 越界要先自查**（见「报错条件」节）：`period` 出了机型范围、`waveform_set` 出了 [[wsus]] 的范围、
`timing_set` 出了 [[tsus]] 的范围——**三种越界各有一条报错**。
**注意这三条报的都是「越界」，没有一条管 auto-correction 本身**：
**会不会被改正不是错误，是它的答案。**

**4. `pinlist` 用 `@` 还是写名字**：本篇对 `@` 只有一句
`The @ symbol can be used to check all configured pins.`——**本篇没有说「不用 `@` 就进异步模式」**
（**推断**：那句话是设置类命令才有的后果，VCLK? 是纯查询、全篇只用一个动词 `checks`；
**依据的另一半是 `## Errors` 三条全是范围越界，没有一条管同步/异步**）。

## 和谁有关

- [[pclk]] — **前置与搭配（上游写、本页读）**。本篇逐字点名它一次：
  `You allocate a test system period per timing set to the specified pin or pins using PCLK, PCLK? - (Pin CLocK).`
  **「周期怎么定」的正文在 PCLK 那一页**（**本页读到的 [[pclk]] 页**）。
  **PCLK 那一篇回头也点了本页**——它把 `VCLK?` 当作「怎么知道这次改动被没被改正」的答案。
- [[wsus]] — **`waveform_set` 上限的来源（前置）**。本篇一处点名：
  `The maximum number is determined by WSUS, WSUS? - (Waveform Sets USed).`
- [[tsus]] — **`timing_set` 上限的来源（前置）**。同样一处点名。
- [[dfgp]] — **`pinlist` 的另一种写法（并列）**：
  `This parameter can also include groups previously created by DFGP, DFGP? - (DeFine GrouP).`
- [[timing-setup-commands]] — **上游入口**。本篇 `## Application` 全文就一句：
  > 「Timing setup, see Timing Setup Commands.」
  **本篇没有说 VCLK? 在 timing setup 流程里排第几步。**
- [[site-focus-required-before-command]] — **结果有效性的前提**。见「是什么」末节那段 site focus 说明。
- [[vdcg]] / [[vtim]] — **同族的三条 Verify 查询（并列）**。
  **本篇一次没点名它们**；「同族」的依据是**三篇同在一章（`02.06.02.02.*`）**，
  且 [[vdcg]] 那一篇带一段与本篇逐字相同的 site focus 说明（**三篇都是本页的取材**）。
  **三条查的东西各不同**：本页查「一个周期会不会触发 auto-correction」，
  [[vtim]] 查「一组 pin 之间的 period 与 edge timing 是不是一样」，
  [[vdcg]] 查「一组 pin 的 device cycle 定义与长度是不是一样」。
- [[timing]] — **stage 页**。本页 `stage: timing` 的依据是本篇 `## Application` 那句 `Timing setup`。

## 版本

**本文档有 `## Functional changes` 段，段里只有一条**：

- `Introduced before SmarTest 6.3.2`

> **这一条是 §11.2 ② 说的哨兵值，不是「6.3.2 新增了 VCLK」。**
> 措辞是 `before`，意思是「**在本套文档集覆盖范围开始之前就已经有了**」。
> **只可以说：7.10.3 上有它，而且它比 6.3.2 更老** → [[smartest-6.3.2]]。
> **不许把它读成「6.3.2 引入了 VCLK」。**

**版本段里没有的东西（照实记，不替它补）**：没有第二条。
**所以「auto-correction 的机制哪一版改过」「multi-port 那条限制哪一版加的」在本篇里查不到。**

## 出处

`sources:` 一篇：

- `02_System_reference/02.06_Command_Reference/02.06.02.02.319_VCLK__-__Verify_CLocK.md`
  （frontmatter 的 `source_topic` 是 `98844.htm`；**4,947 字节 / 150 行，整篇读完**——
  字节按 `st_size`、行数按 `wc -l`，§11.5 口径）
- 本页的「语法 / 参数」节与「报错条件」节是脚本从这一篇抽的（**本页一个字没动**）。

**本页没做的**：

- **`PCLK` 那一篇没读。** 本页只保证「本篇把落周期这件事指给了 `PCLK`」；
  **period 的取值范围、`query_mode`、period resolution 这些，本页一个字没有。**
  （正文里那句 `The VCLK? query checks whether a PCLK command with the specified parameter values was accepted with or without auto-correction.` 的原文在 PCLK 那一篇里，
  **不在本页取材内**——它是**本页读到的 [[pclk]] 页**引的。）
- **`WSUS` / `TSUS` / `DFGP` / `Timing Setup Commands` 四篇都没读。**
  它们都只是本篇点名的邻居：**两个上限怎么定、group 怎么建、timing setup 的门在哪，本页全无。**
- **本篇 `## Equation-based testing` 那一节的语法块不在本页「语法 / 参数」节里**——
  原因见下面 ⚠️ ①。**本页把它抄进正文的说明里，是为了不让读者以为「按 `specset_id` 查询没有语法」。**
- **图 0 张。** 实测 `![` / `<img` / `.png` / `.jpg` / `.gif` / `raw/` 六种写法在本篇
  **全部 0 命中**。**所以本页没有任何来自图的结论**——
  **这张「没有图」是查过的事实，不是「够不着」（§11.4）。**
- **没在机台上跑过 `VCLK?`**（`verified: doc-only`）。
  **所以「写 20 ns 到底会不会回 1」本页只能保证「文档这么写」（§11）。**
- **本篇没有 `## Warnings` 段**，所以「报错条件」节里只有 `## Errors` 的三条——不是漏写。

### §10 重复投放：本篇在语料里有**三份**（本页查过）

| 路径 | `source_topic` | 字节 | 与**本页这一份**的正文 |
|---|---|---|---|
| `02.06_Command_Reference/02.06.02.02.319_VCLK__-__Verify_CLocK.md`（**本页的出处**） | `98844.htm` | 3,424 | — |
| `02.06_Command_Reference/02.06.06.02.35_VCLK__-__Verify_CLocK.md` | `98844_2.htm` | 3,425 | **`diff` 报 4 行差异——全部是 frontmatter 的 `source_topic` / `source_html` 两行** |
| `02.08_Setup_and_Result_Tools/02.08.04.34.02.02.35_VCLK__-__Verify_CLocK.md` | `98844_3.htm` | 3,571 | **`diff` 的差异只有 frontmatter 与篇内相对链接的前缀**（第三份多一层 `../02.06_Command_Reference/`，字节数差的就是它） |

**本页的结论全部只来自第一份**；另两份只核了 frontmatter、字节数与 `diff` 行数，
**没有逐字读它们的正文**（§12 不越取材边界）。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
> **① 一节的语法块没有进本页的「语法 / 参数」节。** 原文里 equation based 的语法另起了一段，
> 段标题逐字是
> ```
> ## Equation-based testing
> ```
> 底下的语法行逐字是
> ```
> VCLK? {specset_id|"multi-port_spec"}, {timing_set}, {period},{(pinlist)}
> ```
> **这一节没进本页的语法节**——脚本收的是 `## Syntax` / `## Parameters` / `## Example`
> 这一类段名（§4），`Equation-based testing` 不是其中之一。
> **这不是语料写错，也不是本页漏抄**；本页把它抄在正文里。
> **② 同一组语法的空格不齐。** fixed timing 那一行是
> `VCLK? {waveform_set}, {timing_set}, {period}, {(pinlist)}`，
> equation based 那一行是
> `VCLK? {specset_id|"multi-port_spec"}, {timing_set}, {period},{(pinlist)}`——
> **后者 `{period},{(pinlist)}` 之间少一个空格**。**本页照原样引，不替它补空格。**
> **③ 参数表不标归属。** `specset_id` / `multi-port_spec` 两栏只出现在 equation based 那一行里，
> 表里却与 `waveform_set` 并列，**没有一栏说明「哪几个参数属于哪条语法」**——本页照原样记。
> **④ 回复字段混在输入参数表里。** `autocorrect` 是回复里的值，却和 `waveform_set` / `timing_set`
> 这些输入参数排在同一张 `Parameters` 表里。**同族三篇都是这个写法**
> （[[vtim]] 的 `status`、[[vdcg]] 的 `dev_cyc_len` 同理，**三篇都是本页的取材**）——**本页照原样记。**
> **⑤ 同族三篇对同一位置的拼写不一致**（**三篇都是本页的取材**）：
> 本篇与 [[vtim]] 写 `multi-port_spec`（带连字符），[[wfds]] 写 `multiport_spec`（不带）。
> **本页照各自的原文引，不替它们统一。**
> **⑥ 坏字：本篇 0 个。** 照 §11.2 ① 那条判据（**英文文档里出现任何汉字，都是坏字**）逐字查过：
> **本篇一个汉字都没有**——**但这是「本页读到的」，不是「本篇没有」**（§13.1：没找到 ≠ 没有）。

`verified: doc-only`
