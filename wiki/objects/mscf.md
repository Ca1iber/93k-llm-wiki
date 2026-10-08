---
type: object
title: MSCF, MSCF? - (Modulation Set ConFiguration)
layer: L1
stage: timing
tags: [timing, jitter, jitter-injection, modulation-set, mscf, l1-command, firmware-command]
related: [msdf, jscf, jrst, timing]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.162_MSCF__MSCF__-__Modulation_Set_ConFiguration.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# MSCF, MSCF? - (Modulation Set ConFiguration)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **812 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.162_MSCF__MSCF__-__Modulation_Set_ConFiguration.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### MSCF

```
MSCF {"modulation_set_name"}, {"property"}, {"property_value"}
```

### MSCF?

```
MSCF? {"modulation_set_name"|ALL}, {"property"|ALL}
```

returns:

```
MSCF {"modulation_set_name"}, {"property"}, {"property_value"}
```

### Parameters

| modulation_set_name | Specifies the name of a modulation set that must have been defined with MSDF. |
|---|---|
| property | Specifies a property of the modulation set. For a list see the table below. |
| ALL | This value can be specified in the query to retrieve the configuration data of all modulation sets. |
| property_value | Specifies the value for the specified property. The values that are admitted for the individual properties are listed in the table below. |

### Example

```
> MSCF? "mod1",ALL
< MSCF "mod1",SHAPE,SINE
< MSCF "mod1",PERIOD,250
< MSCF "mod1",PHASE,180
< MSCF "mod1",AMPLITUDE,305
```

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.162_MSCF__MSCF__-__Modulation_Set_ConFiguration.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if no modulation set with the specified name exists.

<!-- 报错节 end -->

## 是什么

**MSCF 是 modulation set（调制集）的**属性**命令——写它的属性，或者把属性读回来。**
原文第一句一次讲完「写」与「读」，并顺手给出两条硬前提：

> 「This command serves to define and query the parameters of a modulation set.
> The specified modulation set must have been defined with MSDF.
> The modulation set must be referenced in a jitter set with the JSCF command.
> For more information see Two ways of organizing jitter setup data.」

**四句话、三条链**（这是本页最该记住的结构）：

| 顺序 | 谁 | 干什么 | 原文 |
|---|---|---|---|
| ① | **MSDF** | **先把 modulation set 的名字定义出来** | `must have been defined with MSDF` |
| ② | **MSCF**（本页） | **再配它的属性** | — |
| ③ | **JSCF** | **把它挂到一个 jitter set 上** | `must be referenced in a jitter set with the JSCF command` |

**「定义」与「配置」是两步、两条命令**：**MSDF 只给一个名字，属性全归 MSCF。**
顺序不能反——② 要 ① 先存在，否则报错（见「报错条件」节：
`An error is generated if no modulation set with the specified name exists.`）。
**③ 缺了会怎样，本篇没写后果**（只写了 `must be`）。

### 写与读的格式

| 方向 | 写法 |
|---|---|
| 写 | `MSCF {"modulation_set_name"}, {"property"}, {"property_value"}` |
| 读 | `MSCF? {"modulation_set_name"\|ALL}, {"property"\|ALL}` |
| 读的回复 | `MSCF {"modulation_set_name"}, {"property"}, {"property_value"}` |

**两个位置都能写 `ALL`，但原文只解释了其中一个**：

- **set 名位写 `ALL`** → `This value can be specified in the query to retrieve the configuration data of all modulation sets.`
- **属性位写 `ALL`** → **原文没有单独解释它**，参数表里那条 `ALL` 说的只是「取所有 set 的配置」。
  **而示例用的恰恰是属性位**（`MSCF? "mod1",ALL`）。**（推断）**：属性位的 `ALL` 就是
  「把这个 set 的全部属性列出来」，依据是示例那四行回复正好是四个属性各一行；
  **原文没有一句定义它。**

### 四个属性，以及「取值在哪」

`## Parameters` 里对属性和属性值只写了一句话「看下面那张表」：

> 「Specifies a property of the modulation set. For a list see the table below.」

> 「Specifies the value for the specified property. The values that are admitted for the individual
> properties are listed in the table below.」

**那张表叫 `## Properties and their values`，排在 `## Parameters` 之后**——
**但它不在本页「语法 / 参数」节里**（脚本只逐字抽了 `Parameters` 与 `Example` 两节）。
**所以下面这张表是本页照着原文写的散文，不是逐字抽取**——
**要逐字核对请回 raw（第 67 行起）**。

| 属性 | 取值 / 限制 | 原文要点 |
|---|---|---|
| **SHAPE** | ①**一串偏移量**（ps、逗号分隔、**最多 3072 项**、**只支持 STDDIFF pin**）②或**预定义波形**：`SINE` / `RANDOM` | 见下两小节 |
| **PHASE** | **度数**，**最大 `360掳`**（原文如此，见「出处」） | **给 `RESTART` 模式用的相位偏移** |
| **AMPLITUDE** | **最大 200 ps，默认 100 ps** | **幅度 = 峰峰值的一半** |
| **PERIOD** | **最大 `2 * clock_resolution * 1024 * 512` ps** | 抖动周期 |

### `SHAPE` 的两种写法：一串数，或一个关键字

**写法 (a)：自己给一串偏移量。** 原文逐字：

> 「defines a list of offsets (in picoseconds) from the edge delays specified in the currently
> active timing set」

> 「In case (a), the list items must be separated by a comma, and the maximum number of items is 3072.
> Note that case (a) is only supported for STDDIFF pins.」

**而这串数不是延迟本身，只是比例**：

> 「The list items of case (a) do not define the actual delays, but only their mutual proportions.
> The actual values are computed from the list and the required maximum value (AMPLITUDE property) by」

> `list_item * ( max_value / max_item),`

> 「where max_item is the greatest item in the specified list.」

**原文给了完整的算术例子（数值本页照抄）**：列表 `0, 10, 20, 10, 0, -5, -10, -5, 0`、
要求最大值 **30 ps** → 按 `list_item * ( 30 / 20)` 算出来是
`0, 15, 30, 15, 0, -7.5, -15, -7.5, 0`（ps）。**紧跟着那句要一起记**：

> 「picoseconds. If no amplitude is specified, the default of 100ps is assumed.」

**也就是说：不写 `AMPLITUDE`，(a) 式列表就按 100 ps 这个默认幅度去缩放。**

**写法 (b)：给一个预定义波形的关键字。** 原文只列了两个：

| 关键字 | 原文 |
|---|---|
| `SINE` | `Creates a sinusoidal waveform.` |
| `RANDOM` | `Generates random jitter within delay - amplitude and delay + amplitude,` + `where delay is the delay that is defined in the currently active timing set for the pins that are associated with the modulation set in the respective jitter set, and amplitude is the value of the AMPLITUDE property.` |

**`RANDOM` 那一句是全篇信息密度最高的一句**：它把 **timing set**（延迟从哪来）、
**jitter set**（哪些 pin 受它管）、**AMPLITUDE**（抖多大）三样东西一次串上——
**MSCF 的一个属性值，牵出另外两个对象。**

### `PERIOD` 与那个「你控制不了」的 clock resolution

上限不是一个数，是一条公式：

> 「In general, the maximum period depends on the clock resolution as follows:」

> 「2 * clock_resolution * 1024 * 512」

**而 `clock_resolution` 不是你能直接设的量**：

> 「The clock resolution is calculated from the period resolution, but also takes other parameters
> into account. Therefore a different clock resolution may be calculated from the same period
> resolution in different circumstances.」

**原文只给了一条「想完全掌控它」的路**：

> 「If you want to have complete control over the clock resolution, you must specify a period
> resolution not greater than 2 * minimal_clock_resolution manually (with the period_res keyword).
> Then the clock resolution will equal the period resolution.」

**这句话里有两个本篇没解释的东西**：① **`period_res` 是哪条命令的关键字，本篇没说**；
② **`minimal_clock_resolution` 是多少，本篇也没说**。
（**推断**：`period_res` 属于 period resolution 的设置入口，
依据是括号里那句 `with the period_res keyword`；**具体归哪条命令，本页不写。**）

## 典型用法

**1. 完整的顺序**（照「是什么」那三条链拼）：
**`MSDF` 先定义名字** → **`MSCF` 逐条写属性** → **`JSCF` 把它挂到 jitter set 上** →
`MSCF?` 回读确认。
**缺 ① 直接报错**（`no modulation set with the specified name exists`）；
**缺 ③ 原文的措辞是「必须」**（`must be referenced in a jitter set with the JSCF command`），
**但后果本篇没写**（**语料未写**）。

**2. 回读的两种写法**：

| 想查什么 | 怎么写 |
|---|---|
| **一个 set 的全部属性** | `MSCF? "<name>",ALL` ← **原文示例用的就是这个** |
| **所有 set 的配置** | `MSCF? ALL,ALL`（**推断**：set 名位的 `ALL` 是原文定义的，属性位按同一读法给；**原文没有给出这一行的示例**） |

**3. 原文示例（`## Example`，逐字）——一条查询、四行回复**：

```
> MSCF? "mod1",ALL
< MSCF "mod1",SHAPE,SINE
< MSCF "mod1",PERIOD,250
< MSCF "mod1",PHASE,180
< MSCF "mod1",AMPLITUDE,305
```

**读这个例子要注意两点**：
**① 回复是「属性各占一行」，不是一条多参数的写命令**——回读一次就是四行。
**② `AMPLITUDE,305` 越过了原文自己写的 `The maximum is 200 ps.`**——
**本页照抄这个数，不替它改、也不替它解释**（见「出处」的 ⚠️ ②）。

**4. 两种写法怎么选**：**原文没说怎么选**，只说了 **(a) 只支持 `STDDIFF` pin**。
**「(b) 的预定义波形支持哪些 pin」本篇也没写**——
**只有版本记录里提到 `FASTDIFF` 从 7.3.1 起能用「用户定义的波形」**（见「版本」）。

**5. 写入顺序、属性之间会不会冲突、要不要先清零：语料未写。**
本篇没有一句讲属性之间的依赖或先后——**本页不替它排一条顺序**。

## 和谁有关

- [[msdf]] — **前置，而且是本篇正文逐字点名的**：`must have been defined with MSDF`。
  报错也由这条依赖定义（名字不存在就报错）。
  **两页的分工是「MSDF 给名字 / MSCF 给属性」。**
- [[jscf]] — **下游，也是本篇正文逐字点名的**：
  `must be referenced in a jitter set with the JSCF command`；
  而且 `PHASE` 那一栏又点了一次：`(the mode is defined with JSCF)`。
  **MSCF 配出来的东西，要由 JSCF 挂到 pin 上才算数。**
  （**本页的取材只有 MSCF 这一篇**，JSCF 的 raw 不在内——上面两句都逐字出自本篇。）
- [[jrst]] — **同章家族的另一条（并列）**。**本篇一次都没提到 `JRST`**；
  「同族」的依据是 [[timing]] 的 L1 子专题与 [[mapping-timing]] 的一行
  （**本页读到的 wiki 页**）、以及文件层面的同名投放（见「出处」），**不是本篇**。
- [[timing]] — **`SHAPE` 与 `RANDOM` 两处都提到 `the currently active timing set`**：
  **偏移量的基准与 `RANDOM` 的基准延迟都从它那儿来。**
  **所以本页 `stage: timing` 有正文依据**（不只是 frontmatter）。
  **而 timing set 怎么配，本篇一个字没写。**
- `Two ways of organizing jitter setup data`（**未建**）— **本篇正文点名的那一篇**。
  **本页没读它**，**所以「两种组织方式」怎么选，本页一个字都没有**。
  **这个名字不在 `extract/prose-allowlist.txt` 里，故用反引号写，不做成链接**（§9.1）。
- `Period resolution, clock resolution, and master clock period`（**未建**）—
  **`PERIOD` 那一栏点名它**（`See also`）。**本页没读**，
  **所以 clock resolution 到底怎么算出来，本页没有。**
- `STDDIFF` / `FASTDIFF`（**pin 类型，未建页**）— **(a) 式写法只支持 `STDDIFF`**；
  `FASTDIFF` **只出现在版本记录里**。**两种 pin 各自是什么，本篇没写。**

## 版本

**本文档有 `## Functional changes` 段，两条**：

- **Introduced in SmarTest 7.3.0** — MSCF 是 7.3.0 引进的 → [[smartest-7.3.0]]。
- **SmarTest 7.3.1**：`User defined waveforms for FASTDIFF pins can now be defined with MSCF.`
  → [[smartest-7.3.1]]。

> **这一条值得和正文对一下**：正文 `SHAPE` 那一栏写的是
> `Note that case (a) is only supported for STDDIFF pins.`，
> 而版本记录说 **7.3.1 起 `FASTDIFF` pin 也能用「用户定义的波形」**。
> **两者不矛盾**——**正文那句多半是 7.3.0 时的状态，版本记录补了 7.3.1 的放宽**
> （**推断**，依据是版本记录里的 `now` 这个措辞）。
> **但本篇没有把正文那句改掉**，**本页两处并列照记，不替它调和、也不替它改正文。**
> **另记一句**：`FASTDIFF` 这个词**在本篇正文里一次都没出现**——
> 正文提到 pin 的地方只有 `STDDIFF`（`SHAPE` 那两条）。**这一个词只活在版本记录里。**

**版本段里没有的东西（照实记，不替它补）**：没有第三条。
**所以「属性表哪一版加的 `PERIOD`」「3072 这个项数上限哪一版定的」本篇查不到。**

## 出处

`sources:` 一篇：

- `02_System_reference/02.06_Command_Reference/02.06.02.02.162_MSCF__MSCF__-__Modulation_Set_ConFiguration.md`
  （frontmatter 的 `source_topic` 是 `143671.htm`；**4,544 字节 / 196 行，整篇读完**）
- 本页的「语法 / 参数」节与「报错条件」节是脚本从这一篇抽的（**本页一个字没动**）。

**本页没做的**：

- **`## Properties and their values` 那张表不在「语法 / 参数」节的辖区里。**
  脚本只逐字抽了 `## Parameters` 与 `## Example`。**本页那张四属性表是照原文写的散文，
  不是逐字抽取**——要逐字核对请回 raw（**第 67 行起**）。
- **`MSDF` / `JSCF` 的 raw 本页没读**（**本页的取材只有 MSCF 这一篇**）：
  所以「MSDF 怎么定义名字」「JSCF 怎么挂上去」本页只有本篇那两行字。
- **`Two ways of organizing jitter setup data`、`Period resolution, clock resolution,
  and master clock period` 两篇都没读**——
  **所以属性怎么组织、clock resolution 怎么算，本页一个字没有。**
- **`period_res` 这个关键字本页没查**（**它是哪条命令的关键字，本页不知道**）。
- **图 0 张。** 实测 `![` / `<img` / `.png` / `.jpg` / `.gif` / `raw/` 六种写法在本篇
  **全部 0 命中**。**本页没有任何来自图的结论**——
  **「`SINE` 与 `RANDOM` 的波形长什么样」本页只有文字。**
- **没在机台上跑过 `MSCF` / `MSCF?`**（`verified: doc-only`）。
  **所以「`AMPLITUDE 305` 这种越界的值机台会不会拒」本页答不了（§11）。**

### §10 重复投放：本篇有一份同名孪生（本页查过）

| 路径 | `source_topic` | 字节 / 行 | 与**本页这一份**的正文 |
|---|---|---|---|
| `02.06_Command_Reference/02.06.02.02.162_MSCF__MSCF__-__Modulation_Set_ConFiguration.md`（**本页的出处**） | `143671.htm` | 4,594 / 196 | — |
| `02.06_Command_Reference/02.06.16.02.07_MSCF__MSCF__-__Modulation_Set_ConFiguration.md` | `143671_2.htm` | 4,595 / 196 | **`diff` 报 0 行差异（正文逐行相同）** |

**两份正文逐行相同**，差别只在 frontmatter 的 `source_topic` / `source_html`
（**本页只读了第一份的正文；第二份只核了 frontmatter、字节数与 `diff` 行数**）。
**记这一条的用处**：① 按 §10，本篇没有「两篇说法不同」的问题；
② **第二份落在 jitter 命令章里**，**这是本页判「MSCF 与 JRST / JSCF 同族」的那条文件层面依据**
（见「和谁有关」）。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
> **① 度数符号坏了。** `PHASE` 那一栏原文写的是
> `The maximum is 360掳.`——**`掳`（U+63B3）应为 `°`（度符号）**。
> 这是 §11.2 ① 那类「UTF-8 被按 GBK 读」的形态之一（[[jscf]] 那一页已记过同一个坏字）。
> **代价写在明处：拿 `360°` 去 raw 里搜是搜不到的，要搜 `360掳`。**
> 实测**本篇含汉字的字符只有这 1 个**（在第 143 行）。
> **本页正文引用它时按坏字原样引**，在这一行里注出正字。
> **② 示例里的 `AMPLITUDE,305` 与属性表里的 `The maximum is 200 ps.` 自相矛盾。**
> 两个数都在本篇里：
> ```
> < MSCF "mod1",AMPLITUDE,305
> ```
> ```
> The maximum is 200 ps. The default is always 100 ps.
> ```
> **305 > 200。哪个对？本篇没有说**——**本页照抄两处，不替它裁定、也不替它改数。**
> （**推断**：示例可能是上限改动之前的遗留；依据是示例里的 `PERIOD,250` 与 `PHASE,180`
> 都在限内、只有 `AMPLITUDE` 越界——**但这只是推断，本篇没有一个字支持它。**）
> **③ `AMPLITUDE` 的适用范围两处不一致。** 属性表里写的是
> `This property determines the amplitude (that is, half of the peak-to-peak value) of a
> predefined shape.`（**说它管的是「预定义波形」**），
> 而 `SHAPE` 写法 (a) 里它又被当成缩放用的 `max_value`：
> `the required maximum value (AMPLITUDE property)`。**两种口径并存，本篇没有调和**——
> **本页两处照引，不替它统一。**
> **④ 属性表被压平成「一格一行」，不是管道行表格。**
> 原文那一段逐字长这样（**`|` 与内容分行、空行隔开**）：
> ```
>  |
>
>  |
>
> SHAPE
>
>  |
> ```
> **所以它连「连续 ≥3 行管道行」都算不上**——[[xps256-status-flags]] 那一页记过同一成因的
> 另一种形态（那张表被拆成 18 段「连续的管道行」，逐字没丢、只是分了段）。
> **本页照原样引用其中的值，不替它重排成表。**
> **⑤ 坏字的覆盖面照实说**：本篇的坏字**只有 ① 那一处**——
> **但这是「本页读到的」，不是「本篇只有一处」**（§13.1：没找到 ≠ 没有）。

`verified: doc-only`
