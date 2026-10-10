---
type: object
title: Timing equation set reference
layer: file
stage: timing
tags: [timing, equation-set, timing-setup-file, spec-variable, timingset, dscp, mode-context]
related: [timing, timing-file, timing-master-file, timing-setup-tool, spec-tool, timing-specification, dscp]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.02.01_Timing_equation_set_reference.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# Timing equation set reference

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

**没有加标记的语法段。** 定义文档里没有 `Syntax` / `Parameters` / `Example`
这类**段标记**，跟着 `Subtopics` 找一层也没有。
**所以本脚本一个字都不收录**——没有段标记时「哪一段是语法」是猜，而猜就是编（§4）。

<!-- 语法节 end -->

## 是什么

**equation set 是 timing setup file 里的一块正文，由一行 `EQNSET` 头引出来。**
原文第一句就把这件事定死：

> 「Equation sets are identified by a header in the following format:」

头格式本体 = `EQNSET` + 编号 + 可选的描述。**这一行的字面写法本页没有逐字抄，理由见「出处」⚠️ ②**
（原文那行含一组双方括号，抄进来会被链接检查读成一个悬空目标）。

编号与描述的限制在同一段里给全：

> 「<equation_set_number> is a number > 0 that identifies the equation set within the timing setup file. You can define up to 256 timing equation sets in one setup file. <equation_set_description> is an optional description for the equation set. It can contain up to 60 characters. If it contains spaces, it must be enclosed by double quotes. Note that semicolons are not allowed in the description.」

| 项 | 约束 |
|---|---|
| 编号 | **> 0**；**一个 setup file 里最多 256 个 equation set** |
| 描述 | 可选；**最多 60 字符**；含空格必须用双引号括起来；**不许有分号** |

### 一块 equation set 里装六样，**顺序是定的**

> 「A timing equation set contains, in this order:」

| # | 段 | 关键字 | 可选? | 装什么 |
|---|---|---|---|---|
| 1 | mode context | `MODECONTEXT "<mode_context>"` | 可选 | 这块 equation set 基于哪个 mode context |
| 2 | 端口声明 | `DEFINES <port_1> [<port_2> ... <port_n>]` | 可选 | 供 SmarTest 做**端口级完整性检查** |
| 3 | 基变量（spec 变量） | `SPECS` | 可选 | **只声明，不赋值** |
| 4 | 派生变量 | `EQUATIONS` | 可选 | 形如 `var_name = expression` |
| 5 | 主时钟周期 / period resolution / 时钟源 | `period_res`、`clocksrc` | 可选 | **原文标注：只对 Smart Scale 有意义** |
| 6 | **timing set** | `TIMINGSET` | **必需，一个或多个** | 边沿延时与周期 |

第 1 段不写时的默认值是原文明说的：

> 「If no mode context is defined, the default mode context, in which all pins are configured as standard pins, is assumed.」

第 2 段是**检查用**的，不是赋值：

> 「This entry is used by SmarTest to check if the equation set supplies the required information for all pins of the specified ports.」

### 第 3 段 `SPECS`：只声明、单位只是给人看的、变量名大小写敏感

> 「The variables, which are also called briefly specs, are only declared in the equation set, they are not assigned a value here; the values are assigned in the timing specification」

**值不在这一块里给**——这一段只给名字。三条细节：

> 「The units in brackets are optional and only used for the display in the spec tool; they have no further function.」

> 「Variable names are case sensitive, that is, f and F are different variables.」

> 「Note that the variable names must not begin with a keyword of the level or timing setup file. These keywords are:」

**下面这张表照原文的三列排**（原文是一张三列管道表，本页**没有合并行**），26 个词逐一列出：

| 第 1 列 | 第 2 列 | 第 3 列 |
|---|---|---|
| `ADJUST` | `LEVELSET` | `period_res` |
| `CHECK` | `master_clock` | `SPECIFICATION` |
| `CLKSET` | `MODECONTEXT` | `SPECS` |
| `clockSrc` | `MODULATION` | `SPECSET` |
| `DEFINES` | `PDC` | `SYNC` |
| `DPSPINS` | `PHYDVCTBL` | `TIMINGSET` |
| `EQNSET` | `PINS` | `v3_delay_register_value` |
| `EQUATIONS` | `PORT` | `WAVETBL` |
| `fract` | `period_div` | — |

**原文随即自认这张表里不全是 equation set 的词**：

> 「Not all of these keywords belong to the timing equation set. Those that Do not (and do not belong to obsoleted functions) are either used in the timing specification」

（`Those that Do not` 的 `Do` 是大写，照原样；表里的 `clockSrc` 与正文的 `clocksrc` 大小写不一样，见「出处」⚠️ ①。）

### 第 4 段 `EQUATIONS`：派生变量，上限 4096

> 「This part of the equation set is identified by the keyword EQUATIONS. The derived variables are defined by expressions that can contain base variables and derived variables already defined. The header keyword is due to the fact that the definitions have the form」

> 「The maximum total number of variables, both base and derived variables, is 4096.」

**4096 是「基变量 + 派生变量」的总数**，不是派生变量自己的上限。

### 第 5 段：主时钟周期、period resolution、时钟源

> 「The master clock period is fixed in SmarTest 7.10. For multiple clock domains, use different period_res.」

> 「The clock source is defined with the clocksrc keyword. Possible values are INT (internal clock), which is the default, and AMC (alternate master clock).」

`period_res` 可以给常数，也可以给表达式（原文例：`period_res = 4`）。

### 第 6 段 `TIMINGSET`：唯一必需的一段

> 「Mandatory: One or more timing sets.」

> 「Timing sets are identified by a number that counts all the timing sets of a given equation set. They define edge delays and periods by assigning expressions, which can contain base variables and derived variables, to keywords identifying edges.」

> 「A timing set has the following general format:」

一条 timing set 里可以出现五种语句（原样写在下面，**用列点不用表格**，因为其中几条含 `|`）：

- `TIMINGSET <timing_set_number>`（后面可跟一个可选描述）——
  「This statement indicates the start of a timing set within an equation set.」
  描述**最多 60 字符**、含空格要加双引号、**不许有分号**（与 `EQNSET` 的描述同规矩）。
- `period = <expression>|fract(<spec_var1>,<spec_var2>,<spec_var3>)` ——
  「This statement specifies the period, that is, the tester cycle length. <expression> is built up from numerical constants, base variables, and derived variables by arithmetical operators.」
- `PINS <pin_list> [-( <exclude pin list> )]` ——
  「This statement defines the pins to which the following block of edge delays is to be applied. Pin groups can also be specified in the list. The optional exclude list allows you to restrict the definition to a proper subset of a pin group」
- `period_div = <number>` ——
  「This statement defines the number of edges for Pin Scale fast pins」
- `(f|s|d|r)<edge_no_i_j> = <expression_i_j>` —— 一条驱动或接收边沿的延时。

**那个字母前缀的含义，原文逐条给了**：

> 「d specifies a drive edge on a Pin Scale card」

> 「f and s define a drive edge on a Pin Scale 9G card」

> 「r defines a receive edge on both card types.」

> 「Edges are counted starting from 1. The maximum number is 8 for both drive and receive edges.」

**最后一条上限不在本页也不在 `EQNSET` 里，在 `DSCP` 命令上**：

> 「The maximum total number of all timing sets in all equation sets and all waveform sets is defined with the DSCP command.」

（即 `DSCP` 定的是**全局总数**——所有 equation set × 所有 waveform set 的 timing set 加起来。）

## 典型用法

**本文档没有 `## Procedure` 段，也没有 `## Before you begin`。** 它给的是**格式**加**三段可照抄的片段**——
所以这一节写的就是「按格式拼」，不是操作步骤。

**1. 顺序不能换。** 上面那张六行表就是执行顺序（原文 `in this order`）；
唯一必需的是最后一段 `TIMINGSET`，前五段缺了就用默认值。

**2. 片段一：`SPECS`（两行，单位是可选的）**。原文逐字如下：

```
SPECS

f [MHz]

D [ns]
```

**3. 片段二：`EQUATIONS`（用片段一的 `f` 算 `p`）**。原文逐字如下：

```
EQUATIONS

p= 1/f*1000
```

**4. 片段三：一整块 timing set（用了上面两个片段定义的变量）**。原文逐字如下：

```
TIMINGSET 1 "example"

period= p

PINS mode -( S0 )

d1= 0

d2= p/3

d3= p/2 + D
```

> 「This timing set fragment defines edge delays for the pin group mode, with the exception of S0.」

**5. 动笔前先知道四条上限**（前三条各自有出处的，第四条是算出来的）：

| 上限 | 由谁定 | 值 |
|---|---|---|
| equation set 个数 | 本页语料明说 | **256 / setup file** |
| 变量个数（基 + 派生） | 本页语料明说 | **4096** |
| timing set 总数（全局） | `DSCP` 命令 | **文档没给数** |
| 边沿编号 | 本页语料明说 | **驱动 8 个以内、接收 8 个以内** |

**6. 一条自查**：变量名**不许以那 26 个关键字开头**；单位写在方括号里只是给 spec tool 看的，写错不影响测试。

## 和谁有关

- [[timing]] —— 本页 `stage: timing`；equation set 是这一阶段里「定义 timing 内容」的那一块正文。
- [[timing-file]] —— 原文把 equation set 说成「within the timing setup file」，即它是 setup file 里的一块。
  **注意口径**：本文档**没有出现任何一条固件命令**（`EQSP` / `EQFS` 通篇 0 命中），
  也没有出现 `timing-file` 这个文件名——它只说 `the timing setup file`。
- [[timing-master-file]] —— 同一套 setup 的**拆文件侧**，两页是文档集的分章关系。
  **本文档里 `master file` 三个字一次都没出现**（通篇 0 命中），
  所以「equation set 能单独成子文件」这件事**本页不写**，那是那一页的语料说的。
- [[spec-tool]] —— 原文说变量名后的 `[unit]` 「only used for the display in the spec tool」。
- [[timing-specification]] —— spec 值的赋值处；原文两处（第 3 段与 `period` 语句）把读者指过去。
- [[timing-setup-tool]] —— `stage: timing` 的 GUI 侧入口（**本文档没有提到它**，
  这条关系来自本页的 `stage` 归属，不是语料明说）。
- [[dscp]] —— timing set 的**全局总数上限**由它定，原文点名。
- `Mode contexts`（**未建**）—— 第 1 段不写时那个默认 context 的定义处。
- `Defining the timing specification`（**未建**）—— 第 3 段与 `period` 语句两处都指它。
- `Period resolution, clock resolution, and master clock period`、`Determining the period resolution`、
  `Avoiding rounding problems with the fract() function`、`Pin exclusion`、
  `Defining the edge delays for Pin Scale 3600 fast pins`、`Defining edge delays for Smart Scale pins`
  以及两篇 `Defining waveform shapes ...`（**均未建**）—— 第 5、6 段各自的展开篇，**本页一篇没读**。
- [[mapping-timing]] —— 那张对照表把 equation set 与 `EQSP TIM,EQN` 挂在一起。
  **那个依据（glossary 词条）不在本页的 `sources` 里**，所以本页正文不写它；
  两页的口径是：**本页只管格式，挂命令的那一步在 mapping 页。**

## 版本

本文档有 `## Functional changes` 段，三条：

- `Introduced before SmarTest 6.3.2`
- `SmarTest 7.0.3: Pin exclusion introduced`
- `SmarTest 7.2.0: Obsoletes the soc_mts keyword.`

**第一条是哨兵值，不是「6.3.2 的变更」**（§11.2②）：`before` 的意思是
「在本文档集覆盖范围开始之前就已经有了」。

**⚠️ 这一段后面还黏着一个脚注块**（§11.2③ 那一类：本段按模板顺序是最后一个 `## ` 段，
脚注定义紧跟其后）。**这两条脚注恰好是实质内容**，本页把它读成脚注而不是版本条目：

> 「The master clock is fixed to 375 MHz with SmarTest 7.10.」

> 「The functions to which these keywords belong are obsoleted, but the keywords cannot not be used nonetheless.」

（第二条的 `cannot not be used` 是原文的双否定，见「出处」⚠️ ④。）

**所以第 5 段其实带两条版本事实**：7.10 上主时钟固定 375 MHz；被 obsolete 的关键字
**不能因此就不写**。另外 `soc_mts` 在 7.2.0 被 obsolete——而它**不在**上面那张 26 关键字表里，
这两处本页并列，不替语料调和。

## 出处

`sources:` 一篇，**整篇读完**：
`02_System_reference/02.06_Command_Reference/02.06.06.01.02.01_Timing_equation_set_reference.md`
（TDC `104187.htm`，**177 行 / 9,474 字节**）。**没有读 `sources` 之外的任何文档。**

**本页没做的：**

- **一张图都没有。** 本文档对 `raw/` 下 `.png` 的引用是 **0 处**（逐处查过），
  所以**本页没有任何来自图的结论**——**不是图够不着，是这篇文档本来就没配图**（§11.4）。
- **`## Related information` 的两篇没读**：`Defining the global period`、`Setting the edge delays`。
- **正文链出去的八篇子主题一篇没读**（mode context、timing specification、period resolution 三篇、
  `fract()`、pin exclusion、Pin Scale 3600 fast pin / Smart Scale 的边沿延时、两篇 waveform shapes）。
  所以**那六段里每一段的「怎么用」本页都没有**，只有格式与上限。
- **没有实跑。** 没有在机台上写过 equation set、没有跑过 timing check、没有拆过 setup file。
  `verified: doc-only` 指的就是这件事。
- **写这页时没有动 `wiki/index.md`、也没有把本页挂进 `wiki/stages/timing.md`**；**两者已由本批收尾统一挂入**（`index.md` 的对应条目、`stages/timing.md`）。（**2026-09-20 更正**：原文写「那是待办」——**收尾动作把它变成了假话**。）

**⚠️ 本页照实记下、一处都没替语料改的瑕疵：**

**① `clocksrc` 与 `clockSrc` 大小写不一致。** 正文写 `The clock source is defined with the clocksrc keyword.`，而 26 关键字表里那一格写的是 `clockSrc`。**本页两处都按原样引，不统一。**

**② 头格式那一行的双方括号，本页没有逐字抄。** 原文（raw 第 10 行）把格式写成 `EQNSET` 加编号、再跟一个**用双方括号括起来的**可选描述。**那串字面里含一组双方括号，逐字抄进任何内容页都会被链接检查读成一个悬空目标**（§9.1、第八类），所以本页只写 `EQNSET` + 编号 + 可选描述。**这是页面自己的排版约束，不是语料的问题**；要核字面请直接打开 raw。

**③ `TIMINGSET` 的边沿前缀，同一篇里两种写法**：通用格式那几行写 `(d|r)<edge_no_1_1>`，下面逐条说明却写 `(f|s|d|r)<edge_no_i_j>`。**本页照实并列，不替它选一个。**

**④ 两处原文如此、本页照原样引的写法**：`Those that Do not`（`Do` 大写）、`cannot not be used nonetheless`（双否定）。

**⑤ 编码坏字：零处。** 实测这一篇的 CJK 字符数是 **0**（§11.2① 那一族在这篇里一处都没有）；**`DC/DC power units` 那一族（§11.2⑤）也是 0 处**。

**⑥ 两条脚注里第二条的链接目标是空的**：raw 里写作 `[2)](<>)`；第一条脚注的锚点 `#fntarg_1` 与文中 `master_clock` 那一格相对应。

`verified: doc-only`
