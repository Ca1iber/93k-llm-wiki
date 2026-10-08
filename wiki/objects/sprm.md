---
type: object
title: SPRM, SPRM? - (Set PRiMary sets)
layer: L1
stage: level
tags: [sprm, firmware-command, primary-sets, multiport, equation-based-testing, set-id]
related: [aprm, dscp, conf, wsus, tsus, lsus, dsus, spst, spec-set, timing-specification, waveform-set, equation-based-level-setup]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.22_SPRM__SPRM__-__Set_PRiMary_sets.md
created: 2026-09-21
updated: 2026-09-21
verified: doc-only
---

# SPRM, SPRM? - (Set PRiMary sets)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **4,579 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.05.02.22_SPRM__SPRM__-__Set_PRiMary_sets.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### SPRM

```
SPRM [waveform_set_no], [timing_set_no], [level_set_no|level_set_id], [dps_set_no|dps_set_id]
```

or:

```
SPRM {timing_specset_id}, [timing_set_no], [level_set_no|level_set_id], [dps_set_no|dps_set_id]
```

or, for multiport specifications:

```
SPRM {"multi-port_spec"}, [timing_set_no|"timing_set_list"], [level_set_id|level_set_no],[dps_set_id|dps_set_no] [,(port)]
```

### SPRM?

```
SPRM?
```

returns:

```
SPRM {waveform_set_no}, {timing_set_no}, {level_set_no|level_set_id}, {dps_set_no|dps_set_id}
```

or:

```
SPRM {timing_specset_id}, {timing_set_no}, {level_set_id|level_set_no}, {dps_set_id|dps_set_no}
```

or, for multiport specifications:

```
SPRM? [(port)]
```

returns:

```
SPRM {"multi-port_spec"}, {timing_set_no|"timing_set_list"}, {level_set_id|level_set_no},{dps_set_id|dps_set_no} [,(port)]
```

### Parameters

| waveform_set_no | The identification number of the waveform set. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）. The number you enter must also be less than or equal to the maximum number of waveform sets allowed - as defined by `CONF, CONF? - (CONFiguration)`（raw: `02.06.02.02.31_CONF__CONF__-__CONFiguration.md`）. |
|---|---|
| timing_specset_id | Derived as follows:<br><br>`100 * equation_set_no + specset_no`<br><br>Note that the spec set ID also identifies the primary wavetable in equation based testing. |
| multi-port_spec | For a multi-port setup, specify a primary multi-port specification. |
| timing_set_no | The identification number of the timing set. Enter an integer in the range 1 to the maximum number of allowed timing sets (of the selected waveform set or timing specification). The maximum number is determined by `TSUS, TSUS? - (Timing Sets USed)`（raw: `02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`）. The number you enter must also be less than or equal to the maximum number of timing sets allowed (as defined by `DSCP`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md`）).<br><br>In a multiport setup, the timing set number applies to all ports of the specification if you do not specify a port. If you do, the number applies to the specified port. |
| timing_set_list | In a multi-port setup, you can specify primary timing sets for all ports of the specification by entering a list of numbers separated by commas. The order of the timing sets must correspond to the order of the ports in the multi-port timing specification.<br><br>In the query, the numbers of the primary timing sets are returned in a list for all ports of the primary specification unless the numbers are identical for all ports or a port has been specified in the query. |
| level_set_no | The identification number of the level set. Enter an integer in the range 1 to the maximum number of allowed level sets. The maximum number is determined by `LSUS, LSUS? - (Level Sets USed)`（raw: `02.06.02.02.155_LSUS__LSUS__-__Level_Sets_USed.md`）. The number you enter must also be less than or equal to the maximum number of level sets allowed (as defined by `DSCP`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md`）). |
| dps_set_no | The identification number of the DPS set. Enter an integer in the range 1 to the maximum number of allowed DPS sets. The maximum number is determined by `DSUS, DSUS? - (Dps Sets USed)`（raw: `02.06.02.02.91_DSUS__DSUS__-__Dps_Sets_USed.md`）. The number you enter must be less than or equal to the maximum number of DPS sets allowed (as defined by `DSCP`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md`）). |
| level_set_id | Derived as follows:<br><br>`100000 * equation_set_no + 1000 * specset_no + level_set_no` |
| dps_set_id | Derived as follows:<br><br>`100000 * equation_set_no + 1000 * specset_no + 1` |
| port | In a multiport setup, you can specify a port of the specification that was entered as the first parameter. In this case, the timing set number specified as the second parameter will only be applied to the specified port. The port parameter is ignored if a timing set list is specified. |

### Example

The following example shows how to define and query primary timing sets for the multi-port specification spec_ClockP_P1_P2, which contains three ports:

```
> SPRM "spec_ClockP_P1_P2","2,1,2",,
> SPRM?
< SPRM "spec_ClockP_P1_P2","2,1,2",101002,101003
> SPRM "spec_ClockP_P1_P2",2,,,(port_1.CP_1)
> SPRM?
< SPRM "spec_ClockP_P1_P2",2,101002,101003
> SPRM? (port_1.CP_1)
< SPRM "spec_ClockP_P1_P2",2,101002,101003,(port_1.CP_1)
```

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.05.02.22_SPRM__SPRM__-__Set_PRiMary_sets.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

- The set number given is greater than the maximum number allowed by the `DSCP`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md`） (Define System Control Parameter) command (the specified set is not configured), or the equivalent for equation based tests where a spec number is out of the allowed range.
- specset_id is invalid because equation_set_no, specset_no, or both are invalid.
- specset_id does not reference a defined wavetable.
- level_set_id does not describe a defined equation set, spec set or level set.
- dps_set_no is undefined or out of range.
- dps_set_id does not describe a defined equation set or spec set.

<!-- 报错节 end -->

## 是什么

**`SPRM` 选「这一轮要用哪几组 set」，但它不改硬件。** 原文两句逐字：

> 「The SPRM (Set PRiMary sets) command is used to define and change the primary sets in a test
> suite or a test that is defined in a user procedure. If, for example, your test involves
> repeating a functional test with varying parameters, you can use the SPRM command to define the
> primary sets for each test run. Unless otherwise specified, the functional test uses the
> parameters defined in the actual primary sets.」

> 「This command does not activate primary sets in the hardware - see APRM, APRM? - (Activate
> PRiMary sets).」

**三件事**：**作用域**是「test suite，或 user procedure 里定义的一个 test」；
**典型场景**是「同一个 functional test 反复跑、每次参数不同」——**每次 run 用 `SPRM` 指一组**；
**它只登记、不激活**——**激活是 [[aprm]] 的事。**

**默认行为**：不另行指定时，functional test 用的就是**当前 primary sets 里的参数**
（`Unless otherwise specified, the functional test uses the parameters defined in the actual
primary sets.`）。

### primary sets 是七项

原文列出（**逐字**）：

- A timing equation set and spec set (equation based testing)
- A multi-port specification (in a multiport setup)
- A waveform set (non-equation based testing)
- A timing set, or (in a multiport setup) a timing set list
- A level equation set, level spec set, and level set (equation based testing)
- A level set (non-equation based testing)
- A DPS set

**这七项里两两成对，分「equation based」与「non-equation based」两条路**：
**时序**一侧，equation based 用 `timing equation set` + `spec set`，
**非** equation based 用 waveform set；
**电平**一侧，equation based 用 `level equation set` + `level spec set` + `level set`，
非 equation based 只用 level set。
**另外多端口时第一项换成 multi-port specification、第四项换成 timing set list。
DPS set 两项都列，不分路。**

### 四条命令「依赖 SPRM，但不需要 APRM 先行」

原文逐字：

> 「The commands in the following list also depend on the SPRM command, however, they do not need
> the APRM command in advance.」

**四条**：`FTST? - (Functional TeST)`、`RCLS? - (ReCeive Level Sensitivity)`、
[[sqst]]（`SQST, SQST? - (SeQuencer STate)`）、`PSST, PSST? - (Power Supply STatus)`。

**即：这四条自己会先要一组 primary sets，所以 `SPRM` 必须先设过；
但它们不像别的命令那样还得等 `APRM` 把 set 激活。**
**「（推断）因为是查状态/做测量，不需要硬件先切过去」——原文没有解释为什么，这是本页的推断。**

### 一条 `Note`：报错归报错，值还是会存

原文那句 `Note` **紧贴在四条命令清单的最后一个链接后面，没有换行也没有分隔符**
（见 `## 出处` ①），逐字：

> 「Note If some of the specified sets do not exist, SPRM may issue an error message. But it will
> always store the values that were passed to it, even if it has detected that (some of) these
> values do not identify an existing set.」

**这是本页最实用的一条**：**「报错」和「存值」是两件独立的事**——
**`SPRM` 明知某个 set 不存在、报了错，仍然会把传进来的值记下。**
**所以「`SPRM` 报错了」不等于「值没进去」。原文没说这种情况下后续会怎样
（`SPRM?` 查回来是那组错值、还是原值，原文没有）。**

### equation based 时，set 用「换算出来的 ID」而不是编号

原文 `## Equation Based Testing` 一节逐字：

> 「In an equation based timing or level setup, you must identify a spec set ID, level set ID and
> DPS set ID instead of waveform set number, level set number and DPS set number.」

**三条换算公式**（**逐字，原文各自的代码块**）：

| 量 | 公式 | 出处 |
|---|---|---|
| `specset_id` | `100 * equation_set_no + specset_no` | 正文（与 `Parameters` 表一致） |
| `level_set_id` | `100000 * equation_set_no + 1000 * specset_no + level_set_no` | 正文 = 表 |
| `dps_set_id` | `100000 * equation_set_no + 1000 * specset_no + 1` | 正文 = 表 |

**`dps_set_id` 的公式末尾是 `+ 1`（不是 `+ dps_set_no`）**——
**所以按这条公式，任何 `dps_set_id` 都以 `001` 结尾。**
**这一点和例子对不上，见 `## 典型用法` 与 `## 出处` ④。**

**wavetable 不是换算出来的**，原文另行说明：

> 「The appropriate wavetable is determined by looking at which wavetable is referenced by
> equation_set_no and specset_no in the Timing Specification File.」

**即：spec set 的 ID 同时就是「主 wavetable」的标识**
（`Parameters` 表里 `timing_specset_id` 那格逐字也写了
`Note that the spec set ID also identifies the primary wavetable in equation based testing.`），
**而具体落到哪个 wavetable 要去 `Timing Specification File` 里查。**
**那份文件本页没读，见 `## 出处`。**

### 参数的取值范围由谁定（**逐字来自语法节 `Parameters` 表**）

| 参数 | 范围 | 上限由谁定 |
|---|---|---|
| `waveform_set_no` | `1` 到允许的最大 waveform set 数 | 由 [[wsus]] 定，且须 ≤ [[conf]] 允许的上限 |
| `timing_set_no` | `1` 到允许的最大 timing set 数（**所属 waveform set 或 timing specification 的**） | 由 [[tsus]] 定，且须 ≤ [[dscp]] 允许的上限 |
| `level_set_no` | `1` 到允许的最大 level set 数 | 由 [[lsus]] 定，且须 ≤ [[dscp]] 允许的上限 |
| `dps_set_no` | `1` 到允许的最大 DPS set 数 | 由 [[dsus]] 定，且须 ≤ [[dscp]] 允许的上限 |

**四个上限全部是「两把尺子取严」**：
**`WSUS` / `TSUS` / `LSUS` / `DSUS` 说的是「这个工程**实际用了**几个」**
（名字里的 `USed`），**`CONF` / `DSCP` 说的是「这台机器**允许**几个」。**
**（推断）两者取小——依据是原文两句都用了 `must also be less than or equal to`；
原文没有明说「取小」这个结论，只是两句都成立就必须同时满足。**

**`multi-port_spec` 与 `port`**（逐字）：
多端口时第一参数给「主多端口 specification 的名字」；
`port` 那格说 `The port parameter is ignored if a timing set list is specified.`
**——给了 timing set 列表，`port` 就没用了。**

**`timing_set_list` 那格额外说了查询侧的行为**，逐字：

> 「In the query, the numbers of the primary timing sets are returned in a list for all ports of
> the primary specification unless the numbers are identical for all ports or a port has been
> specified in the query.」

**即：查询时**只有当「各端口相同」或「查询里指定了某个端口」时才不返回列表**——**
**否则会把所有端口的主 timing set 编号列出来。**

### `Application`

原文 `## Application` 三行：**Defines the primary sets for a test. / AC tests. /
DC measurements, see DC Measurement Commands.** ——
**（注意第一行和本命令的定义句几乎重复；后两行是「哪两类测试会用到它」，
而 DC 那一条把细节推给了 `DC Measurement Commands` 那一章。）**

## 典型用法

**原文只有一个 `## Example`（已在语法节里逐字，四问四答共八行），
没有 `## Procedure`、没有 `## Before you begin`。**
它演的是一件具体的活：**给一个含三个端口的多端口 specification
`spec_ClockP_P1_P2` 定义并查询主 timing set**。

**四问四答逐字拆开：**

| # | 发出 | 收到 | 读到什么 |
|---|---|---|---|
| 1 | `SPRM "spec_ClockP_P1_P2","2,1,2",,` | （无回显） | 三个端口的 timing set 分别是 2 / 1 / 2；**后两个参数（level、dps）留空** |
| 2 | `SPRM?` | `SPRM "spec_ClockP_P1_P2","2,1,2",101002,101003` | timing set 仍以**列表**回（各端口不同）；**后两个数见下** |
| 3 | `SPRM "spec_ClockP_P1_P2",2,,,(port_1.CP_1)` | （无回显） | 只给 `port_1.CP_1` 设成 timing set `2` |
| 4 | `SPRM?` | `SPRM "spec_ClockP_P1_P2",2,101002,101003` | **这次不返回列表**，因为上一步指定了单个端口 |
| 5 | `SPRM? (port_1.CP_1)` | `SPRM "spec_ClockP_P1_P2",2,101002,101003,(port_1.CP_1)` | **带上 `(port)` 查询时，返回串也把 `(port)` 带回来** |

**三条从例子里能读出来的：**

**① 第 2 步与第 4 步返回形态的差别，正好印证了 `timing_set_list` 那格的话**——
**第 2 步没指定端口 → 回列表 `"2,1,2"`；第 4 步指定过端口 → 回单值 `2`。**

**② 第 5 步说明 `(port)` 是回显的**：查询里给了端口，返回串里也有，**且是最后一项、前面多一个逗号**。

**③ 例子里后两个数字，按公式对不上。** 逐字：`101002,101003`。
按上面三条公式（**算式是本页整理的写法**；原文的变量名是 `equation_set_no` /
`specset_no` / `level_set_no`，见「语法 / 参数」节，本页为了排版缩写成 `eq` / `specset`）：
`level_set_id` 形态是 100000×eq ＋ 1000×specset ＋ level_set_no，
取 eq=1、specset=1 得 101000 ＋ level_set_no → **`101002` / `101003` 对应
`level_set_no` = 2 / 3**。
而 `dps_set_id` 按公式末尾是 `+ 1`，取同样 `eq`/`specset` 只能是 **`101001`**——
**`101003` 无论如何不是合法 `dps_set_id`（任何 `dps_set_id` 都以 `001` 结尾）。**
**所以例子第四个返回值与 `dps_set_id` 的公式冲突。**
**原文明说 `If some of the specified sets do not exist, SPRM may issue an error message.
But it will always store the values that were passed to it, even if it has detected
that (some of) these values do not identify an existing set.`——**
**第 1 步确实把后两个参数留空了，所以这两个数是「存下来的旧值」还是「别的东西」，
原文没说。本页把算术摆出来，不判例子对不对**（见 `## 出处` ④）。

**从原文能落成的动作：**

| 要做的 | 依据 |
|---|---|
| 为一次 run 指定 primary sets | `SPRM [waveform_set_no], [timing_set_no], [level_set_no\|level_set_id], [dps_set_no\|dps_set_id]` |
| 让 set 在硬件里真正生效 | **`SPRM` 做不到**，得用 [[aprm]] |
| 查现在的主 set | 非多端口：**裸 `SPRM?`**；多端口：`SPRM? [(port)]` |
| 一次给多个端口不同的 timing set | 第二个参数写带引号的列表 `"2,1,2"`，**顺序必须与多端口 timing specification 里端口的顺序一致** |
| 只改一个端口 | 第五个参数写 `(port_1.CP_1)` |
| 走 equation based | 用换算出来的 `specset_id` / `level_set_id` / `dps_set_id`，**不要写编号** |
| 只查一个端口 | `SPRM? (port)`——**不带参数就只能查全部** |

**⚠️ 两处语法上的不便，本页照实记：**

- **非多端口的查询形态是裸 `SPRM?`，一个参数都不收**——**所以「查某一次特定的主 set」
  这件事，语法上做不到**（只有多端口形态能加 `(port)`）。原文没有解释。
- **`SPRM` 与 `SPRM?` 各有三种形态，代码块总共六段**，**其中四种写的顺序不一致**：
  `SPRM` 第一形态写 `[level_set_no|level_set_id]`，
  **而 `SPRM?` 第一形态写 `{level_set_no|level_set_id}`、第二三形态写
  `{level_set_id|level_set_no}`**——**同一个位置，竖线两边的先后换了**
  （见 `## 出处` ③）。

## 和谁有关

- [[aprm]] — **原文点名的另一半**：`This command does not activate primary sets in the hardware -
  see APRM, APRM? - (Activate PRiMary sets).`
  **分工是「`SPRM` 登记、`APRM` 激活」。本页只有这一句，`APRM` 怎么激活在那页。**
- [[dscp]] — **四个 set 上限的上限**。`Parameters` 表里 `timing_set_no` / `level_set_no` /
  `dps_set_no` 三格都点了它，`Errors` 第一条也是它
  （`The set number given is greater than the maximum number allowed by the DSCP
  (Define System Control Parameter) command`）。
  **`DSCP` 管「这台机器允许几个 set」的容量，本页管「这次用哪几个」。**
- [[conf]] — **`waveform_set_no` 那一格点它**，与 [[wsus]] 配对。
- [[wsus]] / [[tsus]] / [[lsus]] / [[dsus]] — **四个 `xxUSed` 查询**，
  名字里的 `USed` 说的是「这个工程实际用了几个」。**本页只有「上限由它定」这一句，
  四条查询各自怎么用在那四页。**
- [[sqst]] — **「依赖 SPRM 但不需要 APRM 先行」那四条之一**。
  **本页只有这一个名字，`SQST` 本身在那页。**
- [[spst]] — **（推断）同族的查询**：`SPST?` 问的是 specset 的状态位，
  而本页讲的是「哪个 specset 是主」。**依据只有两页都在 level 一侧；
  两篇原文都没有互相引用。**
- [[timing-specification]] — **原文把 wavetable 的查法定在 `Timing Specification File` 里**
  （`The appropriate wavetable is determined by looking at which wavetable is referenced by
  equation_set_no and specset_no in the Timing Specification File.`）。
  **本页只有这一句指向，那份文件的结构在那页。**
- [[waveform-set]] — **「非 equation based testing」一侧的 primary set**，
  也是 `waveform_set_no` 数的对象。**本页只有「它是七个之一」，它本身是什么在那页。**
- [[spec-set]] — **equation based 一侧被 `specset_id` 指的东西**。
- [[equation-based-level-setup]] — **两条路线里 equation based 那一条的总入口**。
- `FTST?` / `RCLS?` / `PSST, PSST?`（**三篇均未建**）— **「依赖 SPRM 但不需要 APRM 先行」
  那四条里的另外三条**。**不在 allowlist，用反引号。**
- `DC Measurement Commands`（**未建**）— **原文 `## Application` 把 DC 那一侧的细节推给它**。
- `Timing Specification File`（**未建**）— **wavetable 的查定处**，见上。
- `multi-port specification` / `timing set list`（**未建**）— **七项 primary set 里
  「只在多端口时才存在」的两项**。

## 版本

`## Functional changes` **只有一条，逐字**：

- Introduced before SmarTest 6.3.2

**这一条是 §11.2 ② 那个哨兵。** `Introduced before SmarTest 6.3.2` 的意思是
**「早于语料覆盖范围」**，**不是「6.3.2 新增」**——
**所以 `SPRM` 本身成立于哪个版本，这份语料里没有。**

**本篇再无别的版本条目**——**尤其：三条 ID 换算公式有没有变过、
`dps_set_id` 那个 `+ 1` 是不是从来如此，语料里没有依据。**

详见 [[smartest-6.3.2]]。

## 出处

`sources:` 一篇：
`02_System_reference/02.06_Command_Reference/02.06.05.02.22_SPRM__SPRM__-__Set_PRiMary_sets.md`

**本页没做的：**

- **`SPRM` / `SPRM?` 六段语法行、`## Equation Based Testing` 三条公式，是本页从原文正文
  转述的**（**其中三条公式与语法节的 `Parameters` 表逐字一致，两处可以互校**）。
  语法节里只有 `### Parameters` 与 `### Example` 两节，
  **原文的 `## Equation Based Testing` / `## SPRM` / `## SPRM?` / `## Application`
  四节都没进语法节**（`## Errors` 进了报错节）。
- **[[aprm]] 没读** —— 所以「登记」与「激活」在实现上差在哪、`APRM` 之后硬件怎么切，
  **本页只有一个 `see` 指过去。**
- **[[wsus]] / [[tsus]] / [[lsus]] / [[dsus]] 四页没读** ——
  **所以「实际用了几个」怎么查、`USed` 与上限的关系，本页只有「由它定」三个字。**
- **`Timing Specification File` 没读** —— **这是本页最大的空缺**：
  原文把「wavetable 到底落到哪一个」这件事定在那份文件里，
  **而本页只能给出「`specset_id` 同时标识主 wavetable」这一句。**
- **`FTST?` / `RCLS?` / `SQST` / `PSST` 四篇里的三篇没读** ——
  **所以「依赖 SPRM 但不需要 APRM 先行」在它们各自那侧是什么后果，本页没有。**
- **`DC Measurement Commands` 那一章没读** —— `## Application` 把它列为 DC 侧的落点。
- **`multi-port specification` / `timing set list` 没有定义** ——
  原文只说了「多端口时用它」，**没有说多端口 specification 怎么建、列表的长度怎么定。**
- **`SPRM` 报错后实际状态如何，本页不知道** —— 原文只说「仍会存值」，
  **没说这种情况下 `SPRM?` 查回来是什么**（见 `## 是什么` 那条 `Note`）。
- **一张图都没有。** 原文没有图片。
- **没有交叉验证任何别处的文档**（§11：本页只写这一篇里有的）。
  **尤其：本页 `layer: L1`、`stage: level`，这个归属是本页照 wiki 的既有划分填的，
  不是本篇文档写出来的**——**原文 `## Application` 把 AC 与 DC 两类测试都列了。**

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> **① `Note` 粘在最后一个链接后面，没有换行、没有分隔符。** 逐字（语法节外，在原文正文里）：
> `…`PSST, PSST? - (Power Supply STatus)`（raw: `02.06.02.02.198_PSST__PSST__-__Power_Supply_STatus.md`）Note If some of the specified sets do not exist, SPRM may issue an error message.`
> ——**`Note` 紧贴 `)`，连一个空格都没有。**
> **（[[dscp]] 那篇是「两个链接粘在一起」，[[uptd]] 那篇是 `Note` 前面多一个表格前缀——
> 三篇的 `Note` 都被破坏了，但破坏方式各不相同。）**
>
> **② `## Parameters` 的表头坏了。** 原文开头逐字：
> ```
>  |
> 
> waveform_set_no
> ```
> ——**第一行是孤立的 ` | `，没有表头行。**
> **与 [[dscp]] / [[uptd]] / [[spst]] 三篇同一处毛病。**
>
> **③ `level_set_no|level_set_id` 的先后顺序，六段语法里不一致。** 逐字对照：
> - `SPRM` 第一形态：`[level_set_no|level_set_id]`
> - `SPRM` 第三形态（多端口）：`[level_set_id|level_set_no]`
> - `SPRM?` 第一形态：`{level_set_no|level_set_id}`
> - `SPRM?` 第二形态：`{level_set_id|level_set_no}`
> - `SPRM?` 第三形态（多端口）：`{level_set_id|level_set_no}`
>
> **同一个参数位，`level_set_id` 在前还是在后，五种写法里翻了两次。**
> **原文没说这两种顺序有区别。本页照实并列，不替它统一。**
> **（`dps_set_no|dps_set_id` 那一处也有同样的翻转，且第三形态里那一对的两项之间
> 没有空格：`[level_set_id|level_set_no],[dps_set_id|dps_set_no]`。）**
>
> **④ 例子里第四个返回值与 `dps_set_id` 的公式冲突。** 逐字：
> ```
> > SPRM?
> < SPRM "spec_ClockP_P1_P2","2,1,2",101002,101003
> ```
> 按原文两条公式（**算式为本页整理写法**，变量名缩写同前）：
> `level_set_id` = 100000×eq ＋ 1000×specset ＋ level_set_no、
> `dps_set_id` = 100000×eq ＋ 1000×specset ＋ 1，取 eq=1、specset=1：
> **`101002` / `101003` 都属于 `level_set_id` 形态（对应 `level_set_no` = 2 / 3）；
> 而任何 `dps_set_id` 都会以 `001` 结尾，取不到 `101003`。**
> **可能的原因原文没排除，也都不是明写的**：
> **(a) 例子是旧版留下的**；**(b) 第四个返回值不是 `dps_set_id`**；
> **(c) 公式里那个 `+ 1` 写错了**。**本页把算术摆出来，三种并列，不判。**
>
> **⑤ 例子第一步把后两个参数留空了，但没说明为什么。** 逐字：
> `> SPRM "spec_ClockP_P1_P2","2,1,2",,` ——
> **末尾两个逗号之间什么都没有**，即 level 与 dps 都没给。
> **而 `Parameters` 表里 `level_set_no` / `dps_set_no` 都没有说「可省略」。**
> **（与 ④ 连起来看：这正是「报错了但还是存了值」那条 `Note` 可能生效的地方，
> 但原文没有把例子和那条 `Note` 对上。）**
>
> **⑥ 非多端口的查询形态是裸 `SPRM?`。** 原文 `## SPRM?` 第一节就是这个裸命令，
> **没有任何参数**；能带参数的只有多端口形态 `SPRM? [(port)]`。
> **所以「查某一组特定的主 set」在非多端口下语法上做不到。
> 原文没有说这是有意还是遗漏。**
>
> **⑦ 多端口 `SPRM` 那段语法的空格不齐。** 逐字：
> `SPRM {"multi-port_spec"}, [timing_set_no|"timing_set_list"], [level_set_id|level_set_no],[dps_set_id|dps_set_no] [,(port)]`
> ——**第三、四个参数之间的逗号后面没有空格，而 `[,(port)]` 前面却多一个空格。**
> **同一行里两种排法。**
>
> **⑧ `## Application` 的第一行与定义句几乎重复。** 逐字：
> `Defines the primary sets for a test.` ——
> **与开篇 `The SPRM (Set PRiMary sets) command is used to define and change the primary sets
> in a test suite or a test that is defined in a user procedure.` 说的是同一件事，
> 只是少了 `and change`。**（开篇这一句本页只引了前半句；原文该句后面还有两句。）
> **AC 与 DC 两行之间没有任何过渡，DC 那一条直接把细节推给
> `DC Measurement Commands`。**
>
> **⑨ 全文没有 `## Related information` 一节。**
> **命令之间的关系全在正文句子与 `Parameters` 表格的说明文字里**
> （`APRM` 在定义句里、`WSUS`/`TSUS`/`LSUS`/`DSUS`/`CONF`/`DSCP` 在表里、
> 四条查询命令在 `Note` 前的那一段里）。
>
> **⑩ 本篇没有 §11.2 ① 那种 `鈥` 形态的编码损坏**（本页通读全篇，0 处）。

`verified: doc-only`
