---
type: object
title: ETIM, ETIM? - (Edge TIMing)
layer: L1
stage: timing
tags: [timing, edge-timing, etim, l1-command, firmware-command, superseded, equation-based-timing, edge-order]
related: [etds, tsus, wsus, dfgp, spst, wavetable, psfc, timing-setup-commands, waveform-set, timing]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.118_ETIM__ETIM__-__Edge_TIMing.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# ETIM, ETIM? - (Edge TIMing)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,234 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.118_ETIM__ETIM__-__Edge_TIMing.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### ETIM

```
ETIM {waveform_set},{timing_set}, [t1], [t2], [t3], [t4], [t5], [t6], {(pinlist)}
```

### ETIM?

```
ETIM? {waveform_set}, {timing_set}, {(pinlist)}
```

returns:

```
ETIM {waveform_set},{timing_set}, [t1], [t2], [t3], [t4], [t5], [t6], {(pinlist)}
```

or:

```
ETIM? {specset_id}, {timing_set_no}, {(pinlist)}
```

returns:

```
ETIM {specset_id}, {timing_set_no}, [t1], [t2], [t3], [t4], [t5], [t6],{(pinlist)}
```

Parameters
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98600.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 2 列。
> 首行（上游原文）：waveform_set | Waveform Set Number. Enter PRM for the Primary Waveform Set, or an integer in the range 1 to the maximum number of allowed waveform sets. The max…
> 表内引用（2 条，供检索）：`WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） · `ETIM, ETIM? - (Edge TIMing)`（raw: `02.06.02.02.118_ETIM__ETIM__-__Edge_TIMing.md`）

### Example

```
ETIM 1,1,2,4,8,6,10,,(DATA)
```

This example sets the edge delays for the pin group DATA specified for waveform set 1 and timing set 1. Edges 1 to 5 are set to 2,4,8,6 and 10 ns respectively, edge 6 is unused. If no previous setting for edge 6 exists in waveform set 1 and timing set 1, then its delay remains at 0.0 ns.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.118_ETIM__ETIM__-__Edge_TIMing.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

- waveform_set is greater than the range allowed by the `WSUS`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）command.
- timing_set is greater than the range allowed by the `TSUS`（raw: `02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`）command.
- The selected primary timing set is not defined for the specified waveform set.
- The edge order is wrong; for instance a window open must come before a window close - a mismatch exists between edge delays of the selected timing set and the waveform definition - `WFDF, WFDF? - (WaveForm DeFinition)`（raw: `02.06.02.02.334_WFDF__WFDF__-__WaveForm_DeFinition.md`）, or the break waveform definition - `BWDF, BWDF? - (Break Waveform DeFinition)`（raw: `02.06.02.02.13_BWDF__BWDF__-__Break_Waveform_DeFinition.md`）.
- Edge placement is outside the allowed range.
- All edges of the same direction in the specified timing set do not lie within one period.
- specset_id does not reference a defined wavetable.
- specset_id is invalid because equation_set_no, specset_no, or both are invalid.

<!-- 报错节 end -->

## 是什么

**ETIM 是 ETDS 的前任：同样改 edge delay，但只到 6 条 edge，而且已经被替代。**
原文第一句就是这个身份：

> 「This command is replaced by the command ETDS, ETDS? from release 2.1 onwards when 14-edge setups are used.」

**这一句是本页与 [[etds]] 那一页的接口**，也是**本页最该先读的一句**。
**注意它和 [[etds]] 那一篇的说法对不上**（`2.1` vs `2.0`、`14-edge setups` vs `more than 6 edges`）——
**两篇的原文都在「出处」里逐字并列，本页不替它们调和。**

它做什么，原文第二段：

> 「The ETIM(Edge TIMing) command defines the edge timing for the specified waveform set, timing set and pins. The number of defined waveform and timing sets is not modified.」

**两句都要读**：它改的是 **edge 的时序**；
**它不改「有几个 waveform set」、也不改「有几个 timing set」**——
后者分别是 [[wsus]] 与 [[tsus]] 的事。

### 三条行为规则（与 [[etds]] 几乎逐字相同的一段）

> 「The edge delay parameters are optional. Missing delays are supplied by the system from a data base. Any not previously set delays default to 0.0 ns. No auto-corrections are performed, invalid values are rejected.」

| 规则 | 原文 |
|---|---|
| **延迟参数是可选的** | `The edge delay parameters are optional.` |
| **缺的由系统从数据库补** | `Missing delays are supplied by the system from a data base.` |
| **没设过的默认 `0.0 ns`** | `Any not previously set delays default to 0.0 ns.` |
| **不做 auto-correction；非法值直接拒** | `No auto-corrections are performed, invalid values are rejected.` |

### 一条只属于本篇的语法要求：**省略的参数也要留逗号**

> 「Make sure you include a comma for any omitted or unused timing parameter.」

**这是 ETIM 与 ETDS 最大的一处写法差别**：ETIM 用**位置**定 edge
（第 3 个参数就是 t1、第 4 个就是 t2，依此类推），
**所以中间空掉一个也必须写逗号占位**。
**示例里就这么写的**：`ETIM 1,1,2,4,8,6,10,,(DATA)` ——
**`10` 与 `(DATA)` 之间那两个逗号夹着一个空位，那个空位就是没用的 `t6`。**
（ETDS 用的是 `d1:0 d2:2` 这种**带名字**的写法，**所以 ETDS 不需要占位逗号**——
**ETDS 那一侧见 [[etds]]。**）

### `ETIM?` 与 `ETDS?` 回读范围不同（**一句原文说死**）

> 「The ETIM? query returns delays for all events.」

**`all events`——全回。**
（对照：[[etds]] 那一篇的回读**只回 wavetable 里用到的、或值不为 0 的**。
**两篇的差别就在这里，本页只引本篇这一句，对照的另一半请去 [[etds]] 看。**）
**所以「ETIM? 回得全」不等于「ETIM? 更清楚」**——
**它回的是「全部 edge 的延迟」，包括那些你根本没动过的。**

### `t1..t6`：**最多 6 条 edge，这是 ETIM 的硬边界**

语法式里 edge 参数只有 `[t1]` 到 `[t6]` 六个位置，参数节的原文是：

> 「Edge delay in ns. Note that the positions of some edges may be affected by the use and position of previously defined edges as explained in "Restrictions" in ETIM, ETIM? - (Edge TIMing).」

**这一格有一处语料瑕疵：它把读者指向了 `ETIM, ETIM? - (Edge TIMing)`——也就是本篇自己。**
（见「出处」⚠️③。）

而**超过 6 条 edge 会怎样**，`## Equation Based Testing` 一节里写死了：

> 「The command will be disabled for pin and waveform sets containing more than 6 edges.」

**`disabled`——不是报错，是这条命令不工作。**
**`## Errors` 八条里没有任何一条讲这个**，
**所以「为什么我的 ETIM 没生效」的答案在这一段散文里，不在报错表里。**

### `## Restrictions`：edge 顺序的两条规则

> 「Actions which use the same resource in one waveform (drive, tri-state or window formatter) must be ordered according to the specifications made in the WFDFand BWDFcommands.」

> 「All receive edges in a waveform used for a window compare must be physically ordered. For instance, the edge closing the window must come after the edge that opens it. See also Selecting and ordering edges.」

| 规则 | 管谁 |
|---|---|
| **同一个 resource 的 action 要按 `WFDF` / `BWDF` 的规定排序** | drive / tri-state / window formatter |
| **window compare 的 receive edge 必须在物理上排好** | **开窗的 edge 必须先于关窗的** |

> **`WFDFand BWDFcommands` 里少两个空格**（原文如此，见「出处」⚠️②）。
> **另注意本篇引的兄弟命令是 `WFDF` / `BWDF`（`WaveForm DeFinition`），
> 而 [[etds]] 那一篇报错段引的是 `WFDS` / `BWDS`（`WaveForm Definition String`）。**
> **两组名字在语料里都存在，本篇与那一篇各引各的**——
> **本页只记本篇引的是哪一组，不判两篇谁对。**

**注意 `## Restrictions` 是 ETIM 有、[[etds]] 没有的一节**——
`t1..t6` 那一格就是把你指向这里。

### `## Equation Based Testing`：`specset_id` 指 wavetable，不是 waveform set

> 「In Equation Based Testing, you must identify a wavetable instead of a waveform set. This is achieved by supplying a specset_id, calculated from equation set number and specset number as follows:」

```
100 * equation_set_no + specset_no
```

> 「The appropriate wavetable is determined by looking at which wavetable is referenced by equation_set_no and specset_no in the Timing Specification File.」

**第二句才是可操作的**：**「该用哪个 `specset_id`」要去 Timing Specification File 里查
`equation_set_no` 与 `specset_no` 引的是哪个 wavetable。**
相关页：[[wavetable]]、[[timing-specification]]（**两篇本页都没读**）。

### 一个副作用：它会改状态位（**这一步原文写在一句 `Note` 里**）

> 「Note The ETIM command sets bit 8 of the status bits to indicate that the equation based values have been overridden. Refer to the SPST? query for a description of these.」

**两条信息**：① **ETIM 会置状态位的第 8 位**，含义是
**「equation based 的值被覆盖了」**；② 这些位的说明在 **`SPST?` 查询**那一篇（[[spst]]，**本页没读**）。
**`Note` 后面没有冒号**——原文如此（见「出处」⚠️④）。

**这一条在 [[etds]] 那一篇里没有**：**ETDS 的文档没有提状态位。**

### 「四条命令一起才能产生时序」——**但哪四条，本篇没说**

> 「See also the following commands:」

原文这句之后只列了**两条**：

- `WFDF, WFDF? - (WaveForm DeFinition)`
- `WAVE, WAVE? - (WAVEform).`

紧接着的下一句却是：

> 「All four commands are required to generate DUT test signal timing.」

**「四条」，而 `See also` 只列了两条。**
**另外两条是哪两条，本篇没说**（**语料未写**）。
（**推断**：与「ETIM 被 ETDS 替代」这条线合起来看，
最可能的读法是 `ETIM` + `ETDS` + `WFDF` + `WAVE` 这四条——
**但这是本页的猜测，原文一个字也没有支持它，所以本页不写成结论。**）
[[wave]] 是这四条里唯一在 [[timing]] 那一族里有页的（[[wave]]、[[wfds]] 已建）。

## 典型用法

**先说范围**：本篇**没有 `## Procedure`、没有 `## Before you begin`**。
`## Application` 一节全文一句：

> 「Timing setup, see Timing Setup Commands.」

对应 [[timing-setup-commands]]（**那篇本页没读**）。
**所以「ETIM 在 timing setup 流程里排第几步」本篇没说。**

**而更要紧的一条前置判断是**：**这条命令已经被替代了**——
`replaced by the command ETDS, ETDS? from release 2.1 onwards when 14-edge setups are used`。
**下面这些步骤照文档抄，是否该用 ETIM 而不是 [[etds]]，本篇没有给判据**
（**它只说 `14-edge setups` 这个条件**）。

**1. 定位三个坐标**：waveform set（或 `specset_id`）→ timing set → pinlist。

| 场合 | 第一格写什么 |
|---|---|
| 普通 | `{waveform_set}`（`PRM` 表示 primary waveform set） |
| equation based | `{specset_id}`，由 `100 * equation_set_no + specset_no` 算出 |

**2. 数清楚要写几条 edge，最多 6 条**（`[t1]` 到 `[t6]`），
**并且按上面说的「省略也要写逗号」占位**。

**3. 写**：

```
ETIM {waveform_set},{timing_set}, [t1], [t2], [t3], [t4], [t5], [t6], {(pinlist)}
```

**4. 读**：`ETIM? {waveform_set}, {timing_set}, {(pinlist)}`；
equation based 场合用另一条形式 `ETIM? {specset_id}, {timing_set_no}, {(pinlist)}`。
**回读是「所有 event」都回**（见「是什么」）。

**5. 原文的示例（`## Example`，逐字）**：

```
ETIM 1,1,2,4,8,6,10,,(DATA)
```

> 「This example sets the edge delays for the pin group DATA specified for waveform set 1 and timing set 1. Edges 1 to 5 are set to 2,4,8,6 and 10 ns respectively, edge 6 is unused. If no previous setting for edge 6 exists in waveform set 1 and timing set 1, then its delay remains at 0.0 ns.」

**把这一例拆开读**（这是本页唯一一个逐字示例，值得逐个位置对）：

| 位置 | 值 | 是什么 |
|---|---|---|
| 1 | `1` | waveform set 1 |
| 2 | `1` | timing set 1 |
| 3–7 | `2,4,8,6,10` | **t1..t5 各 2、4、8、6、10 ns** |
| 8 | **（空）** | **t6 未用**——原文正是靠这个空位配前面那个逗号 |
| 9 | `(DATA)` | **pinlist**；原文把 `DATA` 叫 **`pin group`** |

**`DATA` 是「pin group」**——与 [[dfgp]] 建的 group 是同一套东西
（参数节的 `pinlist` 那一格写的就是 `groups previously created by the DFGP (DeFine GrouP) command`）。
**说明句还交代了「没设过就留在 0.0 ns」这一条**，正好印证上面那条默认值规则。

**6. 顺序要按 `## Restrictions` 那两条排**，
**而且 `t1..t6` 那一格明说「有些 edge 的位置会被已定义的 edge 影响」**——
**怎么影响，本篇把你指向 `"Restrictions"` 那一节，也就是本节。**

**7. 报错时看哪一条**：`## Errors` 八条（比 [[etds]] 多两条），
前六条与 [[etds]] 那一篇同款，**多的两条都是 `specset_id` 的**：

- `specset_id does not reference a defined wavetable.`
- `specset_id is invalid because equation_set_no, specset_no, or both are invalid.`

**——「equation based 场合 `specset_id` 写错」是本篇单独覆盖的两种情况。**

## 和谁有关

- [[etds]] — **替代它的那条命令（后继/下游）**。本篇第一句就说了替代关系；
  [[etds]] 那一篇第一段也说了。
  **两篇的版本号与范围对不上**：本篇 `from release 2.1 onwards when 14-edge setups are used`，
  [[etds]] 那一篇 `from release 2.0 for waveforms with more than 6 edges`。
  **本页两处并列照记，不替它们调和**（见「出处」⚠️①）。
  **另外两处差别也一起记**：本篇**回读是 `all events`**、
  **引的兄弟命令是 `WFDF`/`BWDF`**；[[etds]] 那一篇**回读只回用到的或非 0 的**、
  **引的是 `WFDS`/`BWDS`**。
- [[wsus]] — **上限来源（前置）**。`waveform_set` 的最大值由它定；
  参数节与 `## Errors` 第一条各点它一次。
- [[tsus]] — **另一条上限（前置）**。`timing_set` 的最大值由它定；
  参数节与 `## Errors` 第二条各点它一次。
- [[spst]] — **状态位的说明在那一篇（下游）**。
  本篇那句 `Note` 说 ETIM 会置**第 8 位**表示 `the equation based values have been overridden`，
  并让你去 `SPST?` 查这些位。**[[spst]] 本页没读**，所以那些位分别是什么意思本页没有。
- [[dfgp]] — **`pinlist` 的另一种写法（并列）**：
  `groups previously created by the DFGP (DeFine GrouP) command`；示例里的 `DATA` 就是这种 group。
  **那一篇本页没读。**
- [[wavetable]] / [[timing-specification]] — **equation based 的两个落点（下游）**：
  `specset_id` 指的是 wavetable，而「哪个 `specset_id` 对应哪个 wavetable」
  要去 Timing Specification File 里查。**两篇本页都没读。**
- [[wave]] — **同一条时序链上的另一条命令（并列）**。
  本篇 `See also` 列了它，并说 `All four commands are required to generate DUT test signal timing.`
  **但「四条」是哪四条本篇没说**（见「是什么」末节）。
- [[wfds]] / [[bwds]] — **`WFDF`/`BWDF` 的兄弟**。
  **注意这不是笔误关系**：本篇（`## Restrictions` 与 `## Errors`）引的是
  `WFDF, WFDF? - (WaveForm DeFinition)` 与 `BWDF, BWDF? - (Break Waveform DeFinition)`，
  而 [[etds]] 那一篇引的是 `WFDS` / `BWDS`（`Definition String`）——
  **两组名字在语料里都存在，本篇没解释两者的关系。**
  `wfds` / `bwds` 有页；**`WFDF` 那一篇本页没读**，也不在本页的 `sources:` 里。
- [[psfc]] — **site 聚焦机制（上游）**。本篇两段 `setup focus` 的说明都指向它。
  **那一篇本页没读。**
- [[timing-setup-commands]] — **本章归属（上游）**：`## Application` 指向 Timing Setup 那一章。
- [[waveform-set]] — **本篇两次点名的东西**：
  「`The number of defined waveform and timing sets is not modified.`」
  与「`disabled for pin and waveform sets containing more than 6 edges.`」。
- [[timing]] — **`stage: timing` 的依据**（frontmatter；§6：`stage` 填最近的一段，不是归属）。

**本篇点到名字、本页没读的还有两篇**（用反引号，**未建页，§9.1**）：

- `Selecting and ordering edges`（raw: `02.06.06.01.03.01.02_Selecting_and_ordering_edges.md`）
  —— `## Restrictions` 把 receive edge 的排序规则指向它。
- `Timing Specification File` —— 本篇把它当成 `specset_id` 与 wavetable 的对应表来引，
  **但它不是一个命令、也不是一篇文档名**；`timing-file` / `timing-master-file` 两个名字在清单里，
  **本篇用的词与它们是否指同一个东西，本页不判。**

**本页没有引用 `edges.jsonl` 的入边/出边数字**（没读边数据，故不报条数）。

## 版本

**本文档有 `## Functional changes` 段，段里只有一条**：

- `Introduced before SmarTest 6.3.2`

> **这一条是 §11.2 ② 说的哨兵值，不是「6.3.2 新增了 ETIM」。**
> 措辞是 `before`，意思是「**在本套文档集覆盖范围开始之前就已经有了**」。
> **只可以说：7.10.3 上有它，而且它比 6.3.2 更老** → [[smartest-6.3.2]]。
> **不许把它读成「6.3.2 引入了 ETIM」。**

**版本段里没有的东西（照实记，不替它补）**：没有第二条。
**所以「哪一版把它降级成 `disabled` for >6 edges」「第 8 位是哪个版本加的」
「`release 2.1` 对应哪个 SmarTest 版本」在本篇里查不到。**

> **一处要提醒的读法**：`## Functional changes` 说它 `Introduced before SmarTest 6.3.2`，
> **而正文说它 `replaced by ETDS from release 2.1`**。
> **`release 2.x` 不是 SmarTest 版本号**——**两套编号本篇没说怎么换算**（**语料未写**）。

## 出处

`sources:` 一篇：

- `02_System_reference/02.06_Command_Reference/02.06.02.02.118_ETIM__ETIM__-__Edge_TIMing.md`
  （frontmatter 的 `source_topic` 是 `98600.htm`；**5,819 字节 / 155 行，整篇读完**——
  字节按 `st_size`、行数按 `wc -l`，§11.5 口径）
- 本页的「语法 / 参数」节与「报错条件」节是脚本从这一篇抽的（**本页一个字没动**）。
  **顺带一条**：脚本抽出来的是 `Parameters` 这个裸行而不是 `### Parameters` 标题——
  **那是本篇的原文就少一个 `##`**（原文里这一行就是普通的 `Parameters`），不是脚本漏了。

**本页没做的**：

- **文档里链到的八篇一篇都没读**：`ETDS, ETDS?`、`WSUS`、`TSUS`、
  `WFDF, WFDF? - (WaveForm DeFinition)`、`WAVE, WAVE? - (WAVEform)`、
  `BWDF, BWDF? - (Break Waveform DeFinition)`、`Selecting and ordering edges`、
  `SPST?`、`PSFC, PSFC?`。
  所以：**那些命令各自怎么做、状态位分别是什么、接收 edge 的排序规则是什么
  ——本页一个字都没有。** 本页只保证「本篇分别点过它们的名字」。
- **`ETDS` 那一篇的 raw 不在本页的 `sources:` 里**——本页只读了自己这一篇。
  它的内容见 [[etds]] 那一页；**本页与它的四处差别
  （版本号 `2.1` vs `2.0`、范围 `14-edge setups` vs `more than 6 edges`、
  回读范围、兄弟命令族 `WFDF`/`WFDS`）都并列照记**，
  **其中「那一侧」的原文取自本批另一页 [[etds]] 的 raw**，
  **本页没有把 [[etds]] 的其它内容搬进来。**
- **`Timing Setup Commands` 那一篇没读。** 本篇 `## Application` 只给了它的标题。
  **所以「ETIM 在流程里排第几步」本页没有。**
- **图 0 张。** 实测 `![` / `<img` / `.png` / `.jpg` / `.gif` / `raw/` 六种写法在本篇
  **全部 0 命中**。**所以本页没有任何来自图的结论**——
  **这张「没有图」是查过的事实，不是「够不着」（§11.4）。**
- **没在机台上跑过 `ETIM` / `ETIM?`**（`verified: doc-only`）。
  **所以「打到一台 9G 上 ETIM 到底是 disabled 还是报错」本页答不了（§11）。**
- **本篇没有 `## Warnings` 段**，所以「报错条件」节里只有 `## Errors` 的八条——不是漏写。

### §10 重复投放：本篇在语料里有**三份**（本页查过）

| 路径 | `source_topic` | 字节 | 与**本页这一份**的正文 |
|---|---|---|---|
| `02.06_Command_Reference/02.06.02.02.118_ETIM__ETIM__-__Edge_TIMing.md`（**本页的出处**） | `98600.htm` | 6,509 | — |
| `02.06_Command_Reference/02.06.06.02.16_ETIM__ETIM__-__Edge_TIMing.md` | `98600_2.htm` | 6,510 | **把篇内相对链接的前缀归一化后，`diff` 报 0 行差异** |
| `02.08_Setup_and_Result_Tools/02.08.04.34.02.02.16_ETIM__ETIM__-__Edge_TIMing.md` | `98600_3.htm` | 6,980 | **同上——0 行差异** |

**三份的差别只有两处**：① frontmatter 的 `source_topic` / `source_html`；
② **篇内相对链接的前缀**（第三份多一层 `../02.06_Command_Reference/`，字节数差的就是它）。
**本页的结论全部只来自第一份**；另两份只核了 frontmatter、字节数与 `diff` 行数，
**没有读它们的正文**（§12 不越取材边界）。

### 上游 `.htm` 核对（2026-09-24 做，这是本页**多出来的**一步）

**下面四条本页全去上游 `F:\master-dev\dorm-wsl-sytest\tdc-html\raw\98600.htm`（16,008 字节）核过。
结论：全部是「上游就坏的」（§11.2 ⑥）——重做一次转换也救不回来，所以页面必须留着它们。**

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> **① 替代关系的版本号与范围，两篇对不上。** 本篇逐字：
> `This command is replaced by the command ETDS, ETDS? from release 2.1 onwards when 14-edge setups are used.`
> [[etds]] 那一篇逐字：
> `This command supersedes the command ETIMfrom release 2.0 for waveforms with more than 6 edges.`
> **`2.1` vs `2.0`；`14-edge setups` vs `more than 6 edges`。**
> **上游核对**：本篇这一句在 `98600.htm` 里出现在三处——
> `<meta name="description">`、正文、以及文末那个自指链接的 `title` 属性——
> **三处都是 `release 2.1` 与 `14-edge`**；
> 另一侧在 `98599.htm` 里是 `release 2.0`（出现 2 次）。
> **两边都是上游的写法。本页两处并列照记，不判定哪个对。**
>
> **② `WFDFand BWDFcommands`——少两个空格。** 原文逐字：
> `Actions which use the same resource in one waveform (drive, tri-state or window formatter) must be ordered according to the specifications made in the WFDFand BWDFcommands.`
> **`WFDF` 与 `and` 之间、`BWDF` 与 `commands` 之间各少一个空格。**
> **上游核对**：`98600.htm` 里就是 `made in the WFDFand BWDFcommands.`
> （纯文本，前后是标签边界） → **上游就坏的。**
>
> **③ `t1..t6` 那一格把自己这一篇当成别处的文档来引。** 原文逐字：
> `Edge delay in ns. Note that the positions of some edges may be affected by the use and position of previously defined edges as explained in "Restrictions" in ETIM, ETIM? - (Edge TIMing).`
> **读者正在读的就是 `ETIM, ETIM? - (Edge TIMing)` 这一篇**——
> **这一格是个自指链接**：它说的 `"Restrictions"` 就是本篇下面那一节，链接指向的也是本篇。
> **上游核对**：`98600.htm` 里这一格的 `<a href="98600.htm"` **指向 98600.htm 自己**，
> `title` 属性是本篇的摘要 → **上游就是自指。**
> （**对照**：[[etds]] 那一篇**没有 `## Restrictions` 这一节**——
> **所以「去 `Restrictions` 看」这条指引在本篇之外不成立。**）
>
> **④ `Note` 后面没有冒号。** 原文逐字：
> `Note The ETIM command sets bit 8 of the status bits to indicate that the equation based values have been overridden. Refer to the SPST? query for a description of these.`
> **`Note` 与 `The` 之间只有一个空格。**
> **上游核对**：`98600.htm` 里 `Note` 起了一个新段（`<p>Note The`），
> **上游把「Note」当段落开头，没有用冒号** → **上游就坏的**（英文里这里该是 `Note:`）。
>
> **⑤ 坏字：本篇 0 个。** 照 §11.2 ① 那条判据（**英文文档里出现任何汉字，都是坏字**）逐字查过：
> **本篇一个汉字都没有**——**但这是「本页读到的」，不是「本篇没有」**（§13.1：没找到 ≠ 没有）。

`verified: doc-only`
