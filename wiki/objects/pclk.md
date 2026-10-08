---
type: object
title: PCLK, PCLK? - (Pin CLocK)
layer: L1
stage: timing
tags: [timing, period, pclk, l1-command, firmware-command, fixed-timing, equation-based-timing, period-resolution]
related: [clkr, tsus, wsus, vclk, dfgp, timing, timing-setup-commands]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.175_PCLK__PCLK__-__Pin_CLocK.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# PCLK, PCLK? - (Pin CLocK)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **3,353 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.175_PCLK__PCLK__-__Pin_CLocK.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### PCLK

Fixed timing:

```
PCLK{waveform_set}, {timing_set}, {period}, {(pinlist)}
```

Equation-based timing:

```
PCLK {specset_id|"multi-port_spec"}, {timing_set}, {period}, {(pinlist)}
```

### PCLK?

Fixed timing:

```
PCLK?{waveform_set},{timing_set},{(pinlist)} [,query_mode]
```

returns:

```
PCLK {waveform_set}, {timing_set}, {period}, {(pinlist)}
```

Equation-based timing:

```
PCLK? {specset_id|"multi-port_spec"}, {timing_set}, {(pinlist|portlist)} [,query_mode]
```

returns:

```
PCLK {specset_id|"multi-port_spec"}, {timing_set}, {period}, {(pinlist)}
```

### Parameters

| waveform_set | Waveform Set Number. Enter PRM for the Primary Waveform Set, or an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）. For the query command you can also enter ALL for all waveform sets. |
|---|---|
| specset_id | Used for equation based timing. It is derived as follows:<br><br>100 * equation_set_no + specset_no<br><br>Note that if you change the period for an equation based timing setup, PCLK will only change the runtime value, not the setup value specified in the timing set. |
| multi-port_spec | In the command, you cannot enter a multi-port specification unless the specification is associated with the default port, and no other ports are configured. This restriction does not apply to the query. |
| timing_set | Timing Set Number. Enter PRM for the Primary Timing Set, ALL for all timing sets, or an integer in the range 1 to the maximum number of allowed timing sets. The maximum number is determined by `TSUS`（raw: `02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`）. |
| period | Enter the test system period in ns. The period range depends on the model. For the Pin Scale 800, the range is 2.5 ns to 31250 ns. All values entered (or queried regardless of query_mode) are in ns and will be rounded to nine digits after the decimal point (atto-seconds) according to the accuracy of the firmware. The power-on default value for all configured pins also depends on the model. |
| pinlist | The name of the pin or pins whose period you want to define or read back. This parameter can also include groups previously created by `DFGP`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）. If more than one pin is to be included, the names must be separated with a comma. The symbol @ can be used to set or read the periods for all configured pins. If you do not use @, the firmware assumes asynchronous operation. |
| portlist | In the query, you must specify a list of ports, if you have specified a multi-port specification for the first parameter. |
| query_mode | In the query, you can specify whether the period specified by the user or the corrected period calculated by the system is to be returned. The allowed values are:<br><br>WANT: The period defined by the user is returned. This is also the default.<br><br>EXACT: The period calculated by the system is returned. |

### Example 1

```
PCLK 101,1,20,(@)
```

This example sets the test system period for specification 101 to 20 ns.

### Example 2

```
PCLK 101,1,40,(S1)
```

This example sets the test system period of pin S1 for specification 101 to 40 ns.

The `VCLK?`（raw: `02.06.02.02.319_VCLK__-__Verify_CLocK.md`） query checks whether a PCLK command with the specified parameter values was accepted with or without auto-correction.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.175_PCLK__PCLK__-__Pin_CLocK.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

- waveform_set is greater than the range allowed by the `WSUS`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） command.
- timing_set is greater than the range allowed by the `TSUS`（raw: `02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`） command.
- The period lies outside the given range.

<!-- 报错节 end -->

## 是什么

**PCLK 设的是「一个 test cycle 有多长」——也就是 test system period。**
它按 waveform set（或 equation set）与 timing set 定位，再指定改哪些 pin。原文第一句：

> 「The PCLK (Pin CLocK) command defines the test system period for the specified
> waveform set/equation set and timing set.」

**三个定位坐标：第几号 waveform set（或 `specset_id`）+ 第几号 timing set + 哪些 pin。**
一句话概括它管的那一段：**timing setup 里「周期」这一个元素**（见 [[timing]] 的 L1 表）。

### `@` 与「异步」的分水岭

> 「All pins will have the same period if you use the all specifier (@) for the pin list.
> Otherwise a pin specific periods will be programmed.」

**用 `@` → 所有已配置的 pin 共用一个 period；不用 `@` → 逐个 pin 各设各的。**
参数释义把这一条的后果说死了：

> 「If you do not use @, the firmware assumes asynchronous operation.」

**即：不给 `@` 就意味着「这些 pin 的周期互不同步」——所以这不只是写法差异，是两种模式**，
而两个模式之间怎么选，本篇没有给判据（**语料未写**）。

### 改 period 会顺带动 period resolution（**本页最容易踩的一处**）

这一段是 PCLK 最重的机制。原文按 **timing set 是不是 1** 分成两种行为：

| 你改的是 | 附加条件 | 后果 |
|---|---|---|
| **timing set 1** | 用 `@`，且**没有显式定义过 period resolution**（原文举的例子是 `CLKR`） | **period resolution 被重算**，好让新 period 是它的整数倍 |
| **timing set 1**（同上） | — | **`> 1` 的 timing set 的 period 会跟着被重新 auto-correction** |
| **timing set > 1** | — | **你给的值不是当前 period resolution 的整数倍时，会被改正** |

原文两句话逐字：

> 「If you change the period of timing set 1 with PCLK for all pins (@), and if no period
> resolution has been explicitly defined (for example, with CLKR), then the period resolution
> will be recalculated in order that the new period be an integer multiple of the period
> resolution. This can also lead to new auto-corrections for the periods of timing sets > 1.」

> 「In contrast, if you change the period of a timing set > 1 with PCLK, then the specified
> value will be corrected if it is not an integer multiple of the actual period resolution.」

**两句话的分岔点只有一个词：`In contrast`。**

- **改 timing set 1 = 改基准**：resolution 跟着动，而且**别的 set 被连带改正**。
- **改 timing set > 1 = 只改自己**：不合 resolution 就被改正。

**所以「我明明写了 20 ns，回读却不是 20」的第一嫌疑对象就是这里。**
（第二嫌疑见下面「period 的单位、范围与取整」。）

**两处细节只能照着念、本页答不了：**

- `if no period resolution has been explicitly defined`——**「怎样才算显式定义过」本篇只举了 `CLKR` 一个例子**，
  而且 [[clkr]] 那一篇本页没读（见「出处」）。
- **这段没有按 timing 类型分支**（fixed / equation based 都算），只按 **timing set 号**分支。

### 超范围时是「报错」还是「新建」——原文两处口径相反

正文说一句、`## Errors` 说一句，方向相反：

> 「In fixed timing, new timing sets are created, if the timing set number specified is greater
> than the maximum number of allowed timing sets as defined with TSUS. New waveform sets are
> also created if the given waveform set is greater than the maximum number of allowed
> waveform sets as defined with WSUS.」

而 `## Errors` 第一条写的是 `timing_set is greater than the range allowed by the TSUS command.`

**正文说「号超了就新建一个」，报错段说「号超了就报错」。**
**两句能不能同时成立，本篇一个字没解释。**
一种读法是「大于 TSUS 当前计数 = 扩容，大于 TSUS 允许的硬范围 = 报错」，
**但这是本页的推断，依据只有两句里 `as defined with TSUS` 与 `the range allowed by the TSUS command`
的用词差别，原文没有一句话支持它。本页两处并列照记，不替它调和。**

> **这段的前三个词是 `In fixed timing`**——**所以「新建」这条行为原文只给了 fixed timing 一侧**；
> **equation based 场合超范围会怎样，本篇没说**（**语料未写**）。

### `PCLK?` 回读的可能是两个不同的值

> 「The PCLK? query can return the values specified by the user, and for timing sets > 1,
> also the corrected values that are actually used.」

`query_mode` 就是选这个的开关：

| 取值 | 回什么 |
|---|---|
| **`WANT`** | `WANT: The period defined by the user is returned. This is also the default.` |
| **`EXACT`** | `EXACT: The period calculated by the system is returned.` |

**注意这条只在 timing set > 1 那一侧才成立**（`and for timing sets > 1, also the corrected values`）——
**timing set 1 上没有「系统改正后的值」这个概念**，这与上一节「改 1 号是改基准」是一件事的两面。

### period 的单位、范围与取整

| 项 | 原文 |
|---|---|
| **单位** | `Enter the test system period in ns.` |
| **范围** | `The period range depends on the model.`；**Pin Scale 800 是 `2.5 ns to 31250 ns`** |
| **取整** | **一律 ns，保留到小数点后 9 位（atto-seconds）**，按固件精度取整 |
| **上电默认** | `The power-on default value for all configured pins also depends on the model.` |

取整那一句逐字：

> 「All values entered (or queried regardless of query_mode) are in ns and will be rounded to
> nine digits after the decimal point (atto-seconds) according to the accuracy of the firmware.」

**两个要点**：① **写入与读回都取整**（`or queried regardless of query_mode`，不管你选 `WANT` 还是 `EXACT`）；
② **这是「回读值 ≠ 写入值」的第二条成因**（第一条是上面那个 auto-correction）。
**Pin Scale 800 以外的机型范围是多少，本篇没写**（`depends on the model` 就是它的全部交代）。

### `specset_id`：equation based timing 的定位方式

> 「Used for equation based timing. It is derived as follows: 100 * equation_set_no + specset_no」

**`specset_id` 是个算出来的数，不是自由命名。**
**而 equation based 场合另有一条与 fixed timing 不同的行为**：

> 「Note that if you change the period for an equation based timing setup, PCLK will only change
> the runtime value, not the setup value specified in the timing set.」

**即：equation based 下 PCLK 只改 runtime 值，timing set 里的 setup 值不动。**
（**同一族里 [[wave]] 的 `ALLOW_EQ` 讲的是同一类事**——`only the runtime settings are affected;
the definitions in the wavetable are not changed`；**两篇各说一遍，本页这一条只出自 PCLK 本篇。**）

### multi-port 的限制只压「写」

> 「In the command, you cannot enter a multi-port specification unless the specification is
> associated with the default port, and no other ports are configured. This restriction does
> not apply to the query.」

**写命令不许随便用 multi-port spec；查询不受这条限制。**
**多端口场合查询时要另给 `portlist`**：

> 「In the query, you must specify a list of ports, if you have specified a multi-port
> specification for the first parameter.」

### `pinlist` 的三种写法

> 「The name of the pin or pins whose period you want to define or read back. This parameter can
> also include groups previously created by DFGP. If more than one pin is to be included, the
> names must be separated with a comma. The symbol @ can be used to set or read the periods for
> all configured pins. If you do not use @, the firmware assumes asynchronous operation.」

| 写法 | 意思 |
|---|---|
| 单个 / 逗号分隔的 pin 名 | **这些 pin 各自设置**（不要 `@` 就进异步模式） |
| 一条 [[dfgp]] 建的 group | **可以整组当 pinlist 用** |
| `@` | **所有已配置的 pin** |

**没有 `@`、也没有逗号分隔时的默认位是怎么回事，本篇没有写**（**语料未写**）。

## 典型用法

**1. 先定三个坐标**：第几号 waveform set（或 `specset_id`）→ 第几号 timing set → 哪些 pin。
**pin 位用不用 `@` 决定了是同步改还是异步改**（见「是什么」）。

**2. 改周期**（原文 `## PCLK` 那两行语法）：

| 你想干什么 | 怎么写 |
|---|---|
| **所有 pin 一个周期** | `PCLK{waveform_set}, {timing_set}, {period}, {(pinlist)}`，pinlist 写 `@` |
| **只改某些 pin** | 同上，pinlist 写 pin 名或 group |
| **equation based timing** | `PCLK {specset_id\|"multi-port_spec"}, {timing_set}, {period}, {(pinlist)}` |

**3. 回读**：`PCLK?{waveform_set},{timing_set},{(pinlist)} [,query_mode]`
——**要「你写的值」就不加 `query_mode`（默认 `WANT`），要「系统真在用的值」就加 `EXACT`**。

**4. 改完核对**（原文给的那条路）：

> 「The VCLK? query checks whether a PCLK command with the specified parameter values was
> accepted with or without auto-correction.」

**这句在原文里是 `## Examples` 的收尾，也是它唯一给出的「怎么知道被改正过」的答案。**
（[[vclk]] 那一篇本页没读，所以 [[vclk]] 具体怎么用、回什么，本页没有。）

**5. 回读值不对时的排查顺序**（本页按「是什么」三节排的，**顺序本身是建议**）：

1. **是不是 timing set > 1**——那一侧会被 auto-correct（改价只改自己）。
2. **是不是写入就被取整**——一律保留 9 位小数，按固件精度。
3. **改的是不是 timing set 1 且没显式定义 period resolution**——resolution 会被重算，
   而且别的 set 会被连带改正。
4. **用 [[vclk]] 查这一次改动到底被没被 auto-correction。**

**6. 原文的两个示例（`## Examples`，逐字）**：

```
PCLK 101,1,20,(@)
```
```
PCLK 101,1,40,(S1)
```

**两句都写 `101`**——按 `100 * equation_set_no + specset_no`，`101` 是 equation set 1、specset 1；
**而原文的说明把它们叫 `specification 101`**（见「出处」⚠️ ②）。
**例 1 用 `@`（全部 pin、20 ns，走同步），例 2 只给 `S1`（40 ns，走异步）**——
**两个例子正好各占模式一侧。**

## 和谁有关

- [[tsus]] — **上限的来源之一（前置）**。本篇两处点名它：正文那句 `as defined with TSUS`
  与 `## Errors` 第一条。**TSUS 管「一个 waveform set 里有几个 timing set」。**
- [[wsus]] — **另一条上限（前置）**，同样两处点名（正文 + `## Errors`）。
  参数释义里还再点一次：`The maximum number is determined by WSUS.`
  **WSUS 管「用到第几号 waveform set」。**
- [[clkr]] — **period resolution 的显式定义入口（前置/上游）**。本篇只在讲重算时举了它一个例子
  （`for example, with CLKR`）。**`CLKR` 那一篇本页没读**，
  **所以「CLKR 怎样定义 resolution」本页没有。**
- [[vclk]] — **核对手段（下游）**：改完 period 之后用它查这次改动是否被 auto-correction。
  **本篇只在示例末尾提了一句，没有示范怎么用。**
- [[dfgp]] — **pinlist 的另一种写法（并列）**：
  `This parameter can also include groups previously created by DFGP.` **DFGP 那一篇本页没读。**
- [[timing]] — **`stage: timing` 的阶段页**。本页是它 L1 表里
  `fixed timing 路线：逐个元素定义 edge / period / waveform` 那一行中的 `period` 一环
  （**本页读到的 wiki 页**）。
- [[wave]] — **同族姊妹命令（并列）**。**本篇一次没提 `WAVE`**；
  「同族」的依据是 [[timing]] 阶段页把它们列在同一个 L1 单元里（**本页读到的 wiki 页**）。
  **两篇在「只改 runtime」这一点上措辞呼应**（见「是什么」末节）。
- [[timing-setup-commands]] — **上游入口**。本篇 `## Application` 一节全文就一句：
  > 「Timing Setup, see Timing Setup Commands.」
  **本篇没有说 PCLK 在 timing setup 流程里排第几步。**
- `Determining the period resolution`（**未建，故用反引号，§9.1**）— 正文那句
  `For more information see` 指向它。**本页没读**，
  **所以「period resolution 到底怎么定、怎么重算」本页一个字没有。**

> **一条指向别处的线索，本页只能标成线索**：[[timing]] 阶段页记着一条与 PCLK 有关的事实
> （该页注明它出自 `UPTD` 那一篇）——**大意是：使用 PCLK / DFPN / CONF 这三条命令，
> 会把某个 up-to-date 标志打回 0，直到 setup 被保存或装入为止。**
> **本页没读 `UPTD` 那一篇**，**所以这条不作为本页的文档事实**——
> 它只说明「PCLK 会打回 timing 的 up-to-date 标志」这件事另有一处出处，
> **要引用请去 [[timing]] 或 `UPTD` 那一篇，不要在别的页上引本页转述的这句话。**

## 版本

**本文档有 `## Functional changes` 段，段里只有一条**：

- `Introduced before SmarTest 6.3.2`

> **这一条是 §11.2 ② 说的哨兵值，不是「6.3.2 新增了 PCLK」。**
> 措辞是 `before`，意思是「**在本套文档集覆盖范围开始之前就已经有了**」。
> **只可以说：7.10.3 上有它，而且它比 6.3.2 更老** → [[smartest-6.3.2]]。
> **不许把它读成「6.3.2 引入了 PCLK」。**

**版本段里没有的东西（照实记，不替它补）**：没有第二条。
**所以「`query_mode` 的 `EXACT` 是哪一版加的」「Pin Scale 800 那个 `2.5 ns to 31250 ns`
是哪一版的范围」「period 的 9 位取整是哪一版改的」在本篇里查不到。**

## 出处

`sources:` 一篇：

- `02_System_reference/02.06_Command_Reference/02.06.02.02.175_PCLK__PCLK__-__Pin_CLocK.md`
  （frontmatter 的 `source_topic` 是 `98682.htm`；**5,707 字节 / 173 行，整篇读完**——
  字节按 `st_size`、行数按 `wc -l`，§11.5 口径）
- 本页的「语法 / 参数」节与「报错条件」节是脚本从这一篇抽的（**本页一个字没动**）。

**本页没做的**：

- **`CLKR` 那一篇没读。** 所以：period resolution **怎么定义、被重算成什么**，本页一个字没有；
  本页只保证「本篇拿 `CLKR` 举过一个例子」。
- **`Determining the period resolution` 没读。** 同上——
  **「resolution 与 period 的整数倍关系」本页只有那句话的字面。**
- **`TSUS` / `WSUS` / `DFGP` / `VCLK` 四篇都没读。** 它们都只是本篇点名的邻居：
  **上限怎么算（TSUS / WSUS）、group 怎么建（DFGP）、怎么核对（VCLK），本页全无。**
- **`Timing Setup Commands` 那一篇没读。** 本篇 `## Application` 只给了它的标题。
- **`Port` / multi-port 那一套没读。** 本篇写了 multi-port 的两条限制，
  **但「port 怎么配、多端口 setup 长什么样」本页没有。**
- **图 0 张。** 实测 `![` / `<img` / `.png` / `.jpg` / `.gif` / `raw/` 六种写法在本篇
  **全部 0 命中**。**所以本页没有任何来自图的结论**——
  **这张「没有图」是查过的事实，不是「够不着」（§11.4）。**
- **没在机台上跑过 `PCLK` / `PCLK?`**（`verified: doc-only`）。
  **所以「写了 20 ns 之后回读到底是 20 还是别的值」本页答不了（§11）。**
- **本篇没有 `## Warnings` 段**，所以「报错条件」节里只有 `## Errors` 的三条——不是漏写。

### §10 重复投放：本篇在语料里有**三份**（本页查过）

| 路径 | `source_topic` | 字节 | 与**本页这一份**的正文 |
|---|---|---|---|
| `02.06_Command_Reference/02.06.02.02.175_PCLK__PCLK__-__Pin_CLocK.md`（**本页的出处**） | `98682.htm` | 5,800 | — |
| `02.06_Command_Reference/02.06.06.02.20_PCLK__PCLK__-__Pin_CLocK.md` | `98682_2.htm` | 5,801 | **把篇内相对链接的前缀归一化后，`diff` 报 0 行差异** |
| `02.08_Setup_and_Result_Tools/02.08.04.34.02.02.20_PCLK__PCLK__-__Pin_CLocK.md` | `98682_3.htm` | 6,082 | **同上——0 行差异** |

**三份的差别只有两处**：① frontmatter 的 `source_topic` / `source_html`；
② **篇内相对链接的前缀**（第三份多一层 `../02.06_Command_Reference/`，字节数差的就是它）。
**本页的结论全部只来自第一份**；另两份只核了 frontmatter、字节数与 `diff` 行数，
**没有读它们的正文**（§12 不越取材边界）。
**顺带一条**：[[timing]] 阶段页引的是**第二份**（`02.06.06.02.20`）——
**两页指同一篇命令的不同投放，正文一致。**

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
> **① 一个数字、三种称法。** 语法里第一位参数叫 `waveform_set`，
> 参数释义里 equation based 场合叫 `specset_id`（由 `100 * equation_set_no + specset_no` 算得），
> 而 `## Examples` 的说明里把它叫 **`specification 101`**，逐字：
> ```
> This example sets the test system period for specification 101 to 20 ns.
> ```
> **`waveform_set` / `specset_id` / `specification` 三个词指同一个位置，本篇不替它统一。**
> **② 一句语法错误照实引。** 第一句的 `Otherwise a pin specific periods will be programmed.`
> ——**`a pin specific periods` 单复数不搭**（本页正文引了它整句，**按原文照抄，没修**）。
> **③ 报错段与正文的「超范围」口径相反**（详见「是什么」那一节），
> `## Errors` 那一侧的原句是
> `timing_set is greater than the range allowed by the TSUS command.`
> **本页把它列为瑕疵而不是裁定它，正因为本篇自己没裁定。**
> **④ 语法行的空格两种写法。** fixed timing 那两行贴着写
> （`PCLK{waveform_set}, {timing_set}, {period}, {(pinlist)}`），
> equation based 那两行在 `PCLK` 后加了空格
> （`PCLK {specset_id|"multi-port_spec"}, {timing_set}, {period}, {(pinlist)}`）；
> `PCLK?` 的 fixed 那行连逗号后都不加空格
> （`PCLK?{waveform_set},{timing_set},{(pinlist)} [,query_mode]`）。
> **同一篇、同一组语法，排版不齐——本页照原样引，不替它补空格。**
> **⑤ 坏字：本篇 0 个。** 照 §11.2 ① 那条判据（**英文文档里出现任何汉字，都是坏字**）逐字查过：
> **本篇一个汉字都没有**——**但这是「本页读到的」，不是「本篇没有」**（§13.1：没找到 ≠ 没有）。

`verified: doc-only`
