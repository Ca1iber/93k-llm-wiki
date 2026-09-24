---
type: object
title: TSUS, TSUS? - (Timing Sets USed)
layer: L1
stage: timing
tags: [timing, timing-set, waveform-set, command, l1]
related: [timing, dscp, conf, wsus, clkr, lsus, wavetable, waveform-set]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# TSUS, TSUS? - (Timing Sets USed)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,855 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### TSUS

```
TSUS {waveform_set},{timing_set}
```

### TSUS?

```
TSUS? {waveform_set}
```

returns:

```
TSUS {waveform_set},{timing_set}
```

Or:

```
TSUS? {specset_id}
```

returns:

```
TSUS {specset_id},{timing_set}
```

Or, for multiport specifications:

```
TSUS? {"multiport_spec"}[,(portlist)]
```

returns:

```
TSUS {"multiport_spec"},{timing_set}[,(port)]
```

### Parameters

|

waveform_set

 |

Waveform Set Number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）. For the query command you can also enter ALL for all waveform sets.

 |
 |

specset_id

 |

Derived as follows: `100 * `equation_set_no `+ `specset_no

 |
 |

multiport_spec

 |

To query a multiport specification, enter the name of the specification.

 |
 |

timing_set

 |

Timing set number. This is the highest number currently allocated to a timing set or the highest number of timing set you want to associate with a given waveform set. The number you enter must be less than or equal to the maximum number of timing sets allowed (as defined by the `DSCP`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md`） command). This number is automatically updated to include any new timing set as it is created. At power-on only one timing set (containing the default values and belonging to the single waveform set) is available.

 |
 |

portlist

 |

For multiport specifications, you can specify a list of the ports for which the number of the timing sets used is to be displayed.

 |

### Example

```
TSUS 3,7
```

This example defines a maximum of 7 timing sets in waveform set 3.

```
TSUS? "spefc",(ARMPort)
TSUS "spefc",3,(ARMPort)
```

This example queries the number of timing sets defined for port ARMPort in the multiport specification spefc.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

- timing_set is greater than the range allowed by the `DSCP`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md`） command.
- waveform_set is greater than the range allowed by the `WSUS`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） command.
- waveform_set is smaller than 1.
- specset_id is invalid because equation_set_no, specset_no, or both are invalid.
- specset_id does not reference a defined wavetable.

<!-- 报错节 end -->

## 是什么

**`TSUS` 定义「一个 waveform set 里装几个 timing set」。**

> 「The TSUS (Timing Sets USed) command defines the number of timing sets contained in a given waveform set. The number of defined waveform sets is not modified.」

**两句都重要**：它改的是 **timing set 的数量**，
**不动 waveform set 的数量**——后者是 [[wsus]] 的事。
（**推断**：它也不改任何一条 timing set 的**内容/值**，只改「用到第几号」——
依据是参数节把 `timing_set` 定义成「the highest number currently allocated to a timing set」；
**原文没有一句话这么说。**）

### 它是一笔**共享预算**：总数由 `DSCP` 定，各 waveform set 分着用

原文的四句话要合起来读：

> 「The DSCP command defines the number of timing sets for all waveform sets.」

> 「The maximum number of all timing sets belonging to all waveform sets is 512. The default number is 256.」

> 「The maximum number of timing sets for one waveform set is 256. The maximum number in a single waveform set also equals the number of timing sets as determined by DSCP minus the timing sets used in the remaining waveform sets.」

| 约束 | 原文的值 / 来源 |
|---|---|
| 全体 waveform set 的 timing set **总数** | **上限 512，默认 256** |
| **单个** waveform set 内 | **上限 256** |
| **单个** waveform set 的实际最大值 | **= `DSCP` 定的数 − 其它 waveform set 已经用掉的** |
| 每个 waveform set **至少** | **1 个** |
| 各 waveform set 之间 | **可以不同** |

**最后那条减法是关键**：**「我这一个 waveform set 能放几个」取决于别的 waveform set 已经占了多少**。
（**这是本页对原文四句话的归纳**——「共享预算」这个词原文没有，
**但那个减法是原文逐字写的**，放在这里是为了让读的人一眼看到耦合。）

> 「There must be at least one timing set in each waveform set. Various waveform sets can have different numbers of timing sets (see also Data organization of fixed timing).」

### 上限又出现两个命令（**与 [[lsus]] 同一款的矛盾**）

| 出处 | 这一篇怎么写 |
|---|---|
| 正文第一段 | 「The new value has to be an integer in the range of 1 to Maximum allowed timing sets as set by CONF, CONF? - (CONFiguration).」 |
| 同一段的下一句 | 「The DSCP command defines the number of timing sets for all waveform sets.」 |
| Parameters 节的 `timing_set` | 「must be less than or equal to the maximum number of timing sets allowed (as defined by the DSCP command)」 |
| `## Errors` 段 | 上限是 `DSCP` 给的 |

**`CONF` 与 `DSCP` 是两个不同的命令，而它们在同一篇里各出现一次以上。**
按 §10，**本页并列写、不选一个当答案**。
**这个形状与 [[lsus]] 那一篇一模一样**（正文说 `CONF`、参数与报错说 `DSCP`）——
**但两篇是两处独立的瑕疵，本页只记本页的，不合并、不互相「佐证」。**

### 它同时是删除入口（**与 [[lsus]] 同形**）

> 「You can use the TSUS command to delete timing sets. If the waveform set you are using, or the timing setup file that you want to load to hardware, contains more timing sets than you require, use TSUS to delete all the sets above the number you specify.」

**编号以上的 timing set 被删掉。** 注意它比 `LSUS` 多一个场景：
**除了「要 load 的文件里太多」，还有「你正在用的那个 waveform set 里太多」**。

### 查询：三种入参，返回同一个形状

> 「The TSUS? query returns the number of timing sets currently defined for the given waveform set.」

| 查谁 | 怎么写 | 返回 |
|---|---|---|
| 一个 waveform set | `TSUS? {waveform_set}`（也可写 `ALL`） | `TSUS {waveform_set},{timing_set}` |
| 一个 specset（equation-based） | `TSUS? {specset_id}` | `TSUS {specset_id},{timing_set}` |
| 一个 multiport specification | `TSUS? {"multiport_spec"}[,(portlist)]` | `TSUS {"multiport_spec"},{timing_set}[,(port)]` |

**`portlist` 的用途**（参数节逐字）：
「For multiport specifications, you can specify a list of the ports for which the number of the timing sets used is to be displayed.」

### equation based testing：用 `specset_id` 指 **wavetable**，不指 waveform set

> 「In equation based testing, you must identify the appropriate wavetable instead of a waveform set.」

> 「The appropriate wavetable is determined by looking at which wavetable is referenced by equation_set_no and specset_no in the timing specification file.」

**第二句给了「怎么知道该用哪个 `specset_id`」的答案**：
**去看 timing specification file 里 `equation_set_no` 与 `specset_no` 引的是哪个 wavetable**。
`specset_id` 的算法是 `100 * equation_set_no + specset_no`。
相关页：[[timing-specification]]、[[timing-equation-set]]、[[wavetable]]。

### 与 `CLKR` 的分工（**这是本页的整理，不是文档的说法**）

`TSUS` 管 timing set 的**数量**，[[clkr]] 管 **period resolution**。
**两篇文档之间没有互相链接**——这个并列关系是本页替读者理的，
**不是这两篇里任何一句说的**（见 `## 和谁有关`）。

## 典型用法

**先说范围：这一篇没有 `## Procedure`，也没有 `## Before you begin`。**
唯一的过程线索是 `## Application`：
`Timing setup, see `Timing Setup Commands`（raw: `02.06.06_Timing_Setup_Commands.md`）`，
对应 [[timing-setup-commands]]。**所以本页不写流程顺序**（那是 [[timing]] 的事）。

**1. 设定数量**（原文例 1，逐字）

```
TSUS 3,7
```

> 「This example defines a maximum of 7 timing sets in waveform set 3.」

**读法**：第一个数是 **waveform set 编号**，第二个数是 **timing set 的最高编号**——
`TSUS 3,7` = 「3 号 waveform set 里用到 7 号」，
**不是「3 号 waveform set 里有 7 个 timing set」**（同 [[lsus]] 的 `level_set_no` 语义）。

**2. 查 multiport 里某个 port 的数量**（原文例 2，逐字）

```
TSUS? "spefc",(ARMPort)
TSUS "spefc",3,(ARMPort)
```

> 「This example queries the number of timing sets defined for port ARMPort in the multiport specification spefc.」

**这一例有个读法上的坑**：两行**都没有 `>` / `<` 提示符**，
所以**哪一行是「我发的查询」、哪一行是「返回」原文没说**——
**只能靠语法式推**：第一行是 `TSUS? {"multiport_spec"}[,(portlist)]`（查询式），
第二行是 `TSUS {"multiport_spec"},{timing_set}[,(port)]`（返回式）。
（同章的 [[clkr]] 例子是带 `>` / `<` 的——**这篇没带**，见 `## 出处` ⚠️④。）

**3. 三种查法对号入座**（全部出自语法式）

| 你在哪种工程里 | 用哪种查法 |
|---|---|
| 普通（按 waveform set） | `TSUS? {waveform_set}`；全部就要 `ALL` |
| equation based | `TSUS? {specset_id}`——**先回 timing specification file 查 `specset_id` 对应哪个 wavetable** |
| multiport | `TSUS? {"multiport_spec"}[,(portlist)]` |

**4. 顺序：语料未写。**
「先 `TSUS` 定数量、再往里写 timing set」还是反过来，**这一篇和 [[lsus]] 一样没写**。
（推断）从「delete all the sets above the number you specify」看，
**它裁的是已经存在的 set**，所以「裁」发生在**已经定义之后**；
**但这是推断，不是文档说的。**

## 和谁有关

| 页 | 是什么关系 | 依据 |
|---|---|---|
| [[dscp]] | **总数与上限的来源（文档事实）**：全体 waveform set 的 timing set 数由 `DSCP` 定，单个的上限也引它 | 本页文档正文第一段 + 参数节 + `## Errors` |
| [[conf]] | **上限的另一个来源（文档事实，但与 `DSCP` 冲突）** | 本页文档正文第一段 |
| [[wsus]] | **上游**：`waveform_set` 的取值范围由 `WSUS` 定；**`TSUS` 不改 waveform set 的数量** | 本页文档参数节 + `## Errors` + 正文第一段 |
| [[waveform-set]] | **本页的主角概念**：一个 waveform set 里装几个 timing set、各 set 可以不同 | 本页文档正文 |
| [[clkr]] | **同章同段的兄弟命令**：`CLKR` 定 period resolution、`TSUS` 定 set 数量 | 两篇各自的文档；**两篇之间没有互相链接，这个并列是本页理的** |
| [[lsus]] | **结构同形的命令**：`LSUS` 管 level set 数、`TSUS` 管 timing set 数，**且两篇都由 `DSCP` 给上限、都在正文里误引 `CONF`** | 两篇各自的文档；**「同形」是本页的观察，不是文档的说法** |
| [[tsux]] | **同族命令**（`TSUX, TSUX? - (Timing Sets Used eXtended)`） | **只有名字**；**本页没读它的定义文档，它多做了什么本页不写** |
| [[wavetable]] | **equation-based 下的对应物**：`TSUS? {specset_id}` 查的就是某个 wavetable 的 timing set 数 | 本页文档 `## Equation based testing` |
| [[timing-specification]] | **找对应关系的依据在那儿**：`equation_set_no`/`specset_no` 引的是哪个 wavetable，写在 timing specification file 里 | 本页文档 `## Equation based testing` |
| [[timing-setup-commands]] | **本章归属**：`## Application` 指向 Timing Setup 那一章 | 本页文档 |
| [[timing]] | **本页 `stage: timing` 的理由** | frontmatter |
| `Data organization of fixed timing`（raw: `02.06.06.01.07.01_Data_organization_of_fixed_timing.md`） | **「为什么各 waveform set 的 timing set 数可以不同」的组织方式在那篇里** | 本页文档正文；**未读** |

**本页没有引用 `edges.jsonl` 的入边/出边数字**（没读边数据，故不报条数）。

## 版本

**本文档有 `## Functional changes` 段，里面只有一行**：

- `Introduced before SmarTest 6.3.2`

**这是哨兵值，不是「6.3.2 新增了 TSUS」**——意思是「在本语料覆盖范围开始之前就已经有了」
（§11.2②，说明在 [[smartest-6.3.2]]）。**所以本页没有版本门槛可报。**
（推断）`TSUS` 在 **SmarTest 7.10.3** 上可用——依据是它早于 6.3.2 这条文档事实；
**这是推断，不是机台核对。**

## 出处

`sources:` 一篇：
`02_System_reference/02.06_Command_Reference/02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.md`
（TDC `98817.htm`，4,802 字节，147 行）。**整篇读完。**

**本页没做的**：

- **文档里链到的四篇一篇都没读**：`CONF, CONF? - (CONFiguration)`（`02.06.02.02.31`）、
  `DSCP, DSCP? - (Define System Control Parameter)`（`02.06.02.02.90`）、
  `WSUS, WSUS? - (Waveform Sets USed)`（`02.06.02.02.342`）、
  `Data organization of fixed timing`（`02.06.06.01.07.01`）。
  **所以「`CONF` 与 `DSCP` 哪个定 timing set 上限」本页答不了**，
  也**答不了「512 这个总数按什么规则分给各 waveform set」**——只抄到了那句减法。
- **图一张没看**（本篇没有图）。
- **没有 `## Procedure` / `## Before you begin` 可读**，所以本页没有任何流程叙述。
- **没有用 `edges.jsonl`**，故不报入边/出边条数。
  `[[clkr]]`、`[[lsus]]` 两条「同形/兄弟」关系是**本页的整理**，不是边数据、也不是文档的说法。

> ⚠️ **本篇的语料瑕疵，照实记下、一处都没替它改**：
>
> ① **同一段里，timing set 上限的归属自相矛盾**：正文第一段先说
> 「The new value has to be an integer in the range of 1 to Maximum allowed timing sets as set by CONF, CONF? - (CONFiguration).」，
> **紧接着的下一句**就说「The DSCP command defines the number of timing sets for all waveform sets.」。
> **两句挨着、两个命令**，本页不判哪个对（§10）。
> （**`CONF` 与 `DSCP` 是两个不同的命令**；同族的 [[lsus]] 有同款矛盾，**但那是另一篇的另一处**。）
> ② **`specset_id` 那一格的 markdown 标记被打散**。原文逐字是：
>
> ```
> Derived as follows: `100 * `equation_set_no `+ `specset_no
> ```
>
> 而**同一篇**的 `## Equation based testing` 一节写的是干净的 `100 * equation_set_no + specset_no`
> （反引号包住整个式子）。**同一个式子、同一篇文档、两种写法**，前一种的标记位置明显错乱。
> 本页照实记，**两处都没替它改**。
> ③ **一句语法笔误**：参数节写 `the highest number of timing set you want to associate with a given waveform set`——
> **`timing set` 应为 `timing sets`**。（同族的 [[lsus]] 写的是 `the highest number of set`，
> **两篇的单复数写法还不一样**。）本页正文引这句时**原样抄，没改**。
> ④ **例子的两行没有提示符**：`TSUS? "spefc",(ARMPort)` 与 `TSUS "spefc",3,(ARMPort)`
> **都没有 `>` / `<`**，而说明句只说「queries」——
> **哪一行是查询、哪一行是返回，原文没说**，只能靠语法式推。
> （**同章的 [[clkr]] 例子是带 `>` / `<` 的**——同一章两种排版。）
> ⑤ **例子里的规格名叫 `spefc`**（同章 [[clkr]] 的例子用 `spec_port_1_port_2`）。
> **背景：会不会是 `spec` 的笔误，原文没说，本页不判**；
> 但如果照抄这个例子，**规格名要换成你自己的**，别把 `spefc` 当成关键字。
> ⑥ **大小写不一致**：语法式里两处写 `Or:`（大写 O），
> 而同族的 [[lsus]] 写的是 `or:`（小写）——**同一章里两种写法。**
