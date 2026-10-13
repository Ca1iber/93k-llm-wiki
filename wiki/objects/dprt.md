---
type: object
title: DPRT, DPRT? - (Default PRimary Timing sets)
layer: L1
stage: timing
tags: [timing, dprt, timing-set, waveform-set, primary-set, multiport, command, query, l1, system-only]
related: [timing, timing-setup-tool, dprl, tsus, dscp, waveform-set, wavetable, sprm, command-reference, smartest-6.3.2]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.83_DPRT__DPRT__-__Default_PRimary_Timing_sets.md
created: 2026-09-24
updated: 2026-09-28
verified: doc-only
---

> ⚠️ **本页若干处记的是 2026-10-10【之前】的语料形态。**
> 那一轮把语料里的表格一律换成了**指向上游 HTML 的指针**
> （见 `extract/PLAN-表格指针化.md`）。所以下文凡是说「表格被压平 / 被摊平 /
> 一格一行」的地方，指的是**更换之前**的样子 —— 现在语料里那个位置是**一句指针**，
> 真表仍在 `tdc-html/raw/` 的上游 HTML 里。**页码/引文都不受影响。**

# DPRT, DPRT? - (Default PRimary Timing sets)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **964 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.83_DPRT__DPRT__-__Default_PRimary_Timing_sets.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### DPRT

```
DPRT {waveform_set}, {timing_set}
```

For equation-based testing:

```
DPRT {specset_id}, {timing_set}
```

For multiport specifications:

```
DPRT {"multi-port_spec"}, [timing_set_no|"timing_set_list"][,(port)]
```

### DPRT?

```
DPRT?
```

returns:

```
DPRT {waveform_set}, {timing_set}
```

For equation-based testing:

```
DPRT?
```

returns:

```
DPRT {specset_id}, {timing_set}
```

For multiport specifications:

```
DPRT? [(port)]
```

returns:

```
DPRT {"multi-port_spec"}, {timing_set_no|"timing_set_list"}[,(port)]

```

### Parameters

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98570.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 2 列。
> 首行（上游原文）：waveform_set | Waveform set number.
> 表内引用（1 条，供检索）：`TSUS, TSUS? - (Timing Sets USed)`（raw: `02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`）

### Example

```
DPRT?
```

returns:

```
DPRT 3,4
```

On sending a query the system reports that the default primary waveform set is 3 and the default primary timing set is 4.

<!-- 语法节 end -->

## 是什么

**`DPRT`（Default PRimary Timing sets）把 timing setup tool「定位」到指定的 set 上；
它是给系统用的，不是给人手打的。** 原文开口第一段就划了这条边界，三句话全在同一行：

> 「The DPRT(Default PRimary Timing sets) is for use by the system, not the user.
> Do not attempt to execute it from the hpt utility! The following information is provided to
> improve your understanding of any hpt output listings you may make.」

> 「The command is used to position the timing setup tool on the given sets.」

再对上 `## Application` 那一句：

> 「Internal communication between the Test Flow Editor and timing and vector setups.」

**三条互相印证，所以「别手发」不是一句客套**：

| 出处 | 说的是什么 |
|---|---|
| 第一段 | `for use by the system, not the user` —— **使用者的边界** |
| 第一段 | `Do not attempt to execute it from the hpt utility!` —— **唯一一条禁令，带感叹号** |
| `## Application` | `Internal communication between the Test Flow Editor and timing and vector setups.` —— **它是谁跟谁之间的通信** |
| 第二段 | `position the timing setup tool on the given sets` —— **它的作用面只有「定位」** |

**另外第一段还交代了本篇存在的理由**：`The following information is provided to improve your
understanding of any hpt output listings you may make.`
—— **这篇文档是给「读 hpt 输出」用的**，不是给「发命令」用的。**这是本页与别的命令页最大的不同。**

**⚠️ 第一句里 `DPRT` 和左括号之间没有空格**（`DPRT(Default PRimary Timing sets)`）。
已核上游 `raw/98570.htm`：**上游就缺这个空格**。见「出处」⚠️ ①。

### 三套语法：普通 / equation-based / multiport

| 场景 | 命令形态（逐字，见「语法 / 参数」节） | 第一个参数是什么 |
|---|---|---|
| 普通 | `DPRT {waveform_set}, {timing_set}` | waveform set 的**编号** |
| equation-based testing | `DPRT {specset_id}, {timing_set}` | **算出来的** spec set ID |
| multiport specifications | `DPRT {"multi-port_spec"}, [timing_set_no|"timing_set_list"][,(port)]` | multiport 规范（**带引号**） |

**`specset_id` 的算法，原文给了公式**：

> 「Derived as follows:」

> 「100 * equation_set_no + spec_set_no」

> 「Note that the spec set ID identifies the primary wavetable in equation based testing.」

（三句在原格里是**三行**，之间隔着换行；语料里那三行的换行现在写作 `<br>`。
**所以它们不是一段连续文字，必须分成三个引文块**——并成一个，
第七类会算「丢字符」。见 `schema.md` §11.1。）

**`timing_set` 有两个上限，一个来自 [[tsus]]、一个来自 `DSCP`**（逐字，本篇里 TSUS 是链接、DSCP 是裸文本）：

> 「The identification number of the timing set. Enter an integer in the range 1 to the maximum number
> of allowed timing sets (of the selected waveform set or timing specification). The maximum number is
> determined by TSUS, TSUS? - (Timing Sets USed). The number you enter must also be less than or equal
> to the maximum number of timing sets allowed (as defined by DSCP).」

（原句里 TSUS 那一段是语料内部链接，本页按 §11.1 ② 剥掉标记；**`DSCP` 在 raw 里本来就不是链接**。）

**所以「最大的 timing set 号」不是一个数**：先看 waveform set（或 timing specification）允许多少个、
再不超过 `DSCP` 允许的上限，**两个都得满足**。**违反了会怎样，本篇没写**——它**没有 `## Errors` 段**。

### multiport 那一套：三个参数各有各的规矩

multiport 的形态多出一个可选的 `port`，且 `timing_set` 可以给一串。原文对这三格各写了一句：

| 参数 | 逐字 |
|---|---|
| `multi-port_spec` | 「In a multi-port setup, a primary multiport specification can be specified.」 |
| `timing_set`（multiport 下的适用范围） | 「In a multiport setup, the timing set number applies to all ports of the specification if no port is specified. Otherwise, the number applies to the specified port.」 |
| `timing_set_list` | 「In a multi-port setup, you can specify primary timing sets for all ports of the specification by entering a list of numbers separated by commas.」 |
| `port` | 「In a multi-port setup, you can specify a port of the specification that was entered as the first parameter. In this case, the timing set number specified as the second parameter will only be applied to the specified port. The port parameter is ignored if a timing set list is specified.」 |

**两条最实用**：

- **不给 `port` 就是「对全部 port 生效」**，给了就只对那一个 port 生效。
- **⚠️ `port` 与 `timing_set_list` 不能同时用** —— `The port parameter is ignored if a timing set
  list is specified.` **是「被忽略」不是「报错」**，所以写错了不会响，只会静默地按列表走。

### 查询侧返回什么，取决于三个条件

`timing_set_list` 那一格还有第二段，讲的是**查询时列表什么时候出现**：

> 「In the query, the numbers of the primary timing sets are returned in a list for all ports of the
> primary specification unless the numbers are identical for all ports or a port has been specified in
> the query.」

**拆成表**：

| 查询时的情形 | 返回的是 |
|---|---|
| 各 port 的号**不相同**、且**没指定 `port`** | **一列号**（`timing_set_list`） |
| 各 port 的号**完全相同** | **一个号**（不展开成列表） |
| **指定了 `port`** | **一个号** |

### 查询那三套，第一套和第二套写法完全一样

「语法 / 参数」节里 `## DPRT?` 底下连着给了三组，**其中前两组是同一个写法**：

| 场景 | 查询 | 返回 |
|---|---|---|
| 普通 | `DPRT?` | `DPRT {waveform_set}, {timing_set}` |
| equation-based testing | **`DPRT?`**（与上一行一字不差） | `DPRT {specset_id}, {timing_set}` |
| multiport | `DPRT? [(port)]` | `DPRT {"multi-port_spec"}, {timing_set_no|"timing_set_list"}[,(port)]` |

**前两组的命令形态都是裸的 `DPRT?`，只有 `returns` 不同。**
这是原文的写法（已核上游），**不是脚本漏抄了一段**——读的时候靠 `returns` 那一行分辨。

## 典型用法

**本篇没有 `## Procedure` / `## Before you begin` / `## What to do next`。**
而且 **`## Example` 只有一条，还是查询**（`DPRT?` → `DPRT 3,4`）。
**所以这一节的「用法」绝大部分是「不要怎么用」。**

**1. 唯一的禁令（逐字）：`Do not attempt to execute it from the hpt utility!`**
**别从 `hpt` 里发它。**（`hpt` 是什么，**本篇一个字没解释** —— 见「出处」。）

**2. 正当用法只有一个方向：读输出，不发命令。**
第一段自己说了本篇的用途——`to improve your understanding of any hpt output listings you may make`。
**所以正确姿势是：在 hpt 的输出里看到 `DPRT` 那一行时，回本页查它是什么意思。**

**3. 它实际是谁在发**：按 `## Application`，是 **Test Flow Editor 与 timing/vector setup 之间的内部通信**。
**即：切 timing/vector setup 时由工具自己发。**（**推断**，依据就是 `## Application` 那一句；
**本篇没有第二处讲触发时机**。）

**4. 原文唯一的例子，逐字**：

```
DPRT?
```

returns:

```
DPRT 3,4
```

> 「On sending a query the system reports that the default primary waveform set is 3 and the default
> primary timing set is 4.」

**读法**：返回串的两段就是命令语法的两个参数——**默认 primary waveform set = `3`，默认 primary timing set = `4`**。

**5. 顺序上的前提（从参数表推，本篇没有单独列）**：

| 前提 | 依据 |
|---|---|
| 目标 set 号 ≤ 该 waveform set（或 timing specification）允许多少个 | `timing_set` 那格，上限由 `TSUS` 定 |
| 目标 set 号 ≤ `DSCP` 允许的上限 | 同一格，`(as defined by DSCP)` |
| multiport 下 `port` 与 `timing_set_list` 不能同用 | `port` 那格：`The port parameter is ignored if a timing set list is specified.` |

**6. 出错怎么办：本页没有这一节。** 本篇**既没有 `## Errors` 也没有 `## Warnings`**——
所以「号超了会怎样」「`port` 给错了会怎样」**语料未写**。

## 和谁有关

- [[timing]] — `stage: timing` 的落点。[[timing]] 那一页的 L1 命令表里已经有本页，一句话是
  「供系统使用，不要从 hpt 手工执行」——**那是那一页读本篇得出的**，与本页正文一致。
- [[dprl]] — **同族，且是本页唯一一条「名字同构」的旁证**：
  `DPRL` 是 `Default PRimary **Level** sets`（语料编号 `02.06.02.02.82`），本页是
  `Default PRimary **Timing** sets`（`02.06.02.02.83`）—— **编号紧邻、名字同构**。
  **本篇一个字没提过 `DPRL`**，这层同族关系是**推断**（依据就上面两条）。
  [[dprl]] 那一页里也写了对称的一条推断，**两页的口径一致**。**本页没有读 [[dprl]] 的原文。**
- [[timing-setup-tool]] — **被「定位」的那个工具**。原文的作用句就是
  `position the timing setup tool on the given sets`，**工具是被放置的一方**。**本页没读那一页。**
- [[tsus]] — **上限之一，本篇点名且带链接**（`Timing Sets USed`）。**本页没读它的原文。**
- [[dscp]] — **上限之二，本篇点名但没链接**（`(as defined by DSCP)`，裸文本）。**本页没读它的原文。**
- [[waveform-set]] — 第一个参数 `waveform_set` 的落点；`DPRT?` 的返回第一段就是它的编号。
  **本页没读那一页。**
- [[wavetable]] — **equation-based 那一套的落点**：`specset_id` 那格自己说
  `the spec set ID identifies the primary wavetable in equation based testing`。
  **本页没读那一页。**
- [[sprm]] / [[aprm]] — **同族的 primary set 命令**（把 timing equation set + spec set 指成 primary /
  真正激活到硬件）。**本篇一个字没提过它们**；把它们并置的**唯一依据是 [[timing]] 的 L1 命令表**，
  所以这条是**推断**。**两页本页都没读。**
- [[command-reference]] — **归属**：本篇在 `02.06_Command_Reference` 下。
- **`multi-port specification` 的专页**：本篇只给了 `multi-port_spec` 这个占位名，
  **它的定义文档本页没读**，所以「multiport 规范在哪个文件里定义」本页没有。

## 版本

`## Functional changes` 段有，**只有一条**，逐字：

```
- Introduced before SmarTest 6.3.2
```

**这是哨兵值**（§11.2 ②）：`before` 说明它在**本文档集覆盖范围开始之前**就已经有了，
**具体哪个版本引入，语料里没有**。
**本篇只有这一条，所以「7.10.3 上它有没有变」也是无记录**——
注意本页面向 7.10.3，而**这条命令在 6.3.2 之前就存在**，**没有一条 Functional change 说明它后来改过界面或取值**。

## 出处

`sources:` 一篇：
`02_System_reference/02.06_Command_Reference/02.06.02.02.83_DPRT__DPRT__-__Default_PRimary_Timing_sets.md`
（TDC `98570.htm`，**1,958 字节 / 152 行**）。**整篇读完**——本页引文全部来自这一篇；
另**核对过上游 `raw/98570.htm`**（下面 ⚠️ 两条注明了核对结论）。

**入边 2 条 / 2 篇、出边 1 条**（`edges.jsonl` 原始行数）：

| 方向 | 边 |
|---|---|
| 入 | `02.06.02.02_List_of_commands`（line 92，`inline`） |
| 入 | `02_System_reference/index.md`（line 2651 附近，`toc`） |
| 出 | `02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed`（line 106，`inline`）—— 就是 `timing_set` 那格里的 TSUS |

**两条入边的 `anchor` 字段都是 `null`**（整篇引用，没有锚点）。

**本页没做的**：

- **`TSUS` / `DSCP` / `timing-setup-tool` / `waveform-set` / `wavetable` / `SPRM` / `APRM` 一篇都没读** ——
  所以「上限具体是多少」「tool 长什么样」本页没有；`sprm`/`aprm` 的并置是推断（见「和谁有关」）。
- **`DPRL` 的原文没读**（同族那条推断的依据只有名字与编号，已写明）。
- **`hpt` / `hpt utility` 是什么 —— 语料未写。** 本篇两次提到它（`the hpt utility`、`any hpt output listings`），
  **一次也没有解释它是什么、在哪。**
- **multiport specification 的定义文档没读** —— `multi-port_spec` 这个占位名对应哪个文件，本页不知道。
- **`## Example` 只有一条，而且是查询** —— 所以**「怎么设」本篇一个例子都没有**。
- **图：本篇没有内嵌图片** —— 判据可核：本篇 md 里 `.png` / `![` **0 命中**。
- **编码坏字：本篇 0 处**（`[一-鿿]` 扫过整篇，**一个汉字都没有**）；
  **整词替换（`DC/DC power units`）0 命中**；**省略号（U+2026 与三个 ASCII 点）0 命中**。三条都是实测结果，不是没查。
- **没有实跑。** 没有从 hpt 发过 `DPRT`（**文档明令不要那么做**），也没有在机台上验过
  `DPRT?` 的返回格式。`verified: doc-only`。
- **没有动 `wiki/index.md`**，也没有把本页挂进 [[timing]]。

> ⚠️ **本篇的语料瑕疵，照实记、一处都没替它改**（§11.2）：
>
> **① 第一句里 `DPRT` 与左括号之间缺空格。** 逐字：
> `The DPRT(Default PRimary Timing sets) is for use by the system, not the user.`
> —— **`DPRT(` 之间没有空格**。**已核上游 `raw/98570.htm`**：上游那个 `<p>` 的 HTML 逐字是
> `The <span class="keyword">DPRT</span>(Default PRimary Timing sets) is for use by the system, not the user.`
> （原 HTML 里 `not` 与 `the user` 之间夹着一个换行 + 两个制表符，本页按 §11.1 ① 折叠成一个空格）
> ——**上游如此，不是转换丢的。**
>
> **② 命令侧的第二个参数用方括号、返回侧同一个位置用花括号。** 逐字两行：
> `DPRT {"multi-port_spec"}, [timing_set_no|"timing_set_list"][,(port)]`（**命令**）
> 与
> `DPRT {"multi-port_spec"}, {timing_set_no|"timing_set_list"}[,(port)]`（**返回**）
> —— **同一个位置，一个 `[` 一个 `{`**。**已核上游：上游两处就是这么写的**。
>
> **③ multiport 的第一个参数带引号，别的参数不带。** 逐字：
> `DPRT {"multi-port_spec"}, [timing_set_no|"timing_set_list"][,(port)]`
> —— **`"multi-port_spec"` 既有花括号又有引号**，而同一行里的 `{waveform_set}` / `{timing_set}`
> 都是「花括号 + 裸名」。**同一个模板里的记法不一致**（已核上游，上游如此）。
> **`"timing_set_list"` 也是带引号的**，而它的邻居 `timing_set_no` 不带。
>
> **④ 「For equation-based testing」的命令与查询两段语法一字不差。** 逐字两处都是
> `DPRT?`，**只有 `returns` 不同**。**已核上游：上游确实写了两遍同样的 `DPRT?`。**
>
> **⑤ `## Parameters` 表在 raw 里被压平，而且没有表头。** 六格（`waveform_set` / `specset_id` /
> `multi-port_spec` / `timing_set` / `timing_set_list` / `port`）各散成「一格一行 + 游离 `|`」，
> 说明文字一个字没丢；**表头本篇 raw 里没有**（已核上游：那张表的 `<caption></caption>` 是空的）。
>
> **⑥ 本篇对 `DSCP` 只给名字、不给链接，而 `TSUS` 给了链接。** 同一格里的两个上限，
> **一个可点、一个不可点**（`[TSUS, TSUS? - (Timing Sets USed)](<02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md>)` vs 裸写的 `DSCP`）。
> **这不是抽取丢的**——已核上游：`<span class="keyword">DSCP</span>` 本来就不是 `<a>`。

`verified: doc-only`
