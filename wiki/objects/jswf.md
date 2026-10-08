---
type: object
title: JSWF? - (Jitter Set WaveForm)
layer: L1
stage: timing
tags: [timing, jitter, jitter-set, jswf, l1-command, firmware-command, clock-resolution, ps1600]
related: [timing, jscf, jsdf, jsud, jspr, clkr, psfc, ps1600, mapping-timing, waveform-set, smartest-7.0.1]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.16.02.06_JSWF__-__Jitter_Set_WaveForm.md
created: 2026-09-21
updated: 2026-09-21
verified: doc-only
---

# JSWF? - (Jitter Set WaveForm)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,752 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.16.02.06_JSWF__-__Jitter_Set_WaveForm.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
JSWF? {"jitter_set_name"}, {clock_resolution}, {(pinlist)}
```

returns:

```
JSWF {"jitter_set_name"}, {"offset_sequence"}, {(pinlist)}
```

### Parameters

| jitter_set_name | Specifies the name of a jitter set that must have been defined with JSDF. |
|---|---|
| clock_resolution | Specifies the clock resolution on which the calculation will be based. The admitted range is between 880 and 1750 ps.<br><br>You can retrieve the clock resolution for a specification with the CLKR? EXACT query.<br><br>Note that the unit is pico seconds, not nano seconds. |
| offset_sequence | The list of the calculated offsets that is returned. |
| pinlist | Specifies the pins for which the offset sequence is calculated. |

### Example 1

```
> jscf? "test",,(IO0)
< JSCF "test",WAVEFORM,SINUS,(IO0)
< JSCF "test",PERIOD,20,(IO0)
< JSCF "test",AMPLITUDE,100,(IO0)
> CLKR? EXACT,101,(@)
< CLKR 101,2.4,1.2,(@)
> jswf? "test",1200,(IO0)
< JSWF "test","0,29,47,47,29,0,-30,-48,-48,-30,-1,29,47,47,29,0,
  . . .
  -1,-30,-48,-48,-30,0,29,47,47,29,0,-30,-48,-48,-30",(IO0)
```

This example first queries the jitter waveform for pin `IO0`, and also the clock resolution for timing specification 101. It then calculates the offset sequence for this waveform and clock resolution. Note that CLKR? returns the clock resolution as nano seconds, but that JSWF? expects it to be specified as pico seconds. The reply is displayed in abbreviated form. The total length of the sequence is about 500 items.

### Example 2

```
> JSCF? "test",WAVEFORM,(IO1)
< JSCF "test",WAVEFORM,"150,110,80,70,0"
> JSWF? "test",880,(IO1)
< JSWF "test","150,120,90,70,40",(IO1)
```

This example shows how JSWF? corrects the offset list if the second of two consecutive items is smaller than the first, and the maximum difference is exceeded.

<!-- 语法节 end -->

## 是什么

**`JSWF?` 是查询命令：给它一个 jitter set、一个 clock resolution 和一串 pin，它返回这些 pin 上
jitter 波形的「偏移序列」（offset sequence）。** 原文第一句，逐字：

> 「The JSWF? query returns the offset sequence of the jitter waveforms for the specified pins in
> dependence of a specified clock resolution.」

**它不定义任何东西、不改任何东西——它是这一族里唯一「把已经配好的抖动换算成一串偏移量」的那一步。**
（**同族另有四条命令**：`JSDF` 起名 / `JSCF` 配波形 / `JSPR` 指 primary / `JSUD` 删——见「和谁有关」。）

**而且同一个 jitter set + 同一串 pin，换一个 clock resolution 就换一串偏移量**——
`in dependence of a specified clock resolution` 这半句就是全部理由。**为什么依赖、依赖成什么样，
是本篇第一段余下的全部内容**（下一节）。

### 它是怎么把 clock resolution 算进去的：**两条规则 + 一条纠正承诺**

原文接着说 `The clock resolution enters into the calculation of the offset sequence in two ways:`，
两条规则逐字如下（**第一条的 `4 * clock_resolution`、第二条的公式，都是原文**）：

| # | 原文（逐字） | 本页的读法 |
|---|---|---|
| **①** | `The distance between two items of the offset list must be an integer multiple of 4 * clock_resolution.` | **相邻两项的距离必须是 `4 × clock_resolution` 的整数倍** |
| **②** | `If the second of two consecutive items is smaller than the first, the maximum allowed difference max_diff between the two depends on the clock resolution as follows`，下一行是 `max_diff = clock_resolution/2 - 410 ps.` | **下降（后一项小于前一项）时，允许的最大差是 `clock_resolution/2 − 410 ps`** |

**然后是那条承诺**：

> 「If this restriction is not observed in a user defined waveform, JSWF? will correct the list.」

**三个关键词**：`user defined waveform`（**只要是人写的那种波形才有这个问题**）、
`will correct`（**它自己改，不报错**）、`the list`（**改的是返回的那串列表**）。
**「怎么改」原文只在 Example 2 里演示，没有文字规则**——本页把那一步算了一遍，见下。

### Example 2 的算术：**`max_diff` 就是那个 30 ps**（**推断，但算得出来**）

Example 2 把「修正」演示了。**它的 clock resolution 是 880 ps**，代进规则②算一次：
**880 ÷ 2 − 410 = 440 − 410 = 30**，**即 `max_diff` = 30 ps**
（**这个算式是本页做的，不是原文——原文只给了那条公式，没代过任何一个数**）。

**把它和例子的输入输出逐项对上**：

| 项 | 输入（`JSCF?` 查出来的波形，逐字） | 输出（`JSWF?` 修正后，逐字） | 相邻变化（输入 → 输出） | 是否违反规则② |
|---|---|---|---|---|
| 1 | `150` | `150` | — | — |
| 2 | `110` | **`120`** | −40 → **−30** | **违反**（40 > 30）→ **压到 −30** |
| 3 | `80` | **`90`** | −40 → **−30** | **违反** → **压到 −30** |
| 4 | `70` | `70` | −20 | 不违反（20 ≤ 30）→ **原样** |
| 5 | `0` | **`40`** | −70 → **−30** | **违反** → **压到 −30** |

**输入 `150,110,80,70,0` → 输出 `150,120,90,70,40`，与原文的返回值逐字一致。**
**而且每一处被改的地方，改后的下降量恰好是 30 ps**——
**所以「correction」在这里的行为是「把超过 `max_diff` 的下降压到 `max_diff`」**
（**推断**：依据是上表五项的算术；**原文没有一个字描述这个行为**）。
**唯一没被改的下降是 −20**（因为它在 30 之内）——**这一项的存在正是这个推断的反证检验点。**

> **⚠️ 规则①在例子里看不出效果，本页照实说。** 按字面读，规则①要求相邻两项的距离是
> `4 × clock_resolution` 的整数倍——对 880 ps 就是 **`4 × 880 = 3520 ps`**；
> **而例 2 输出里的距离是 30 / 30 / 20 / 30（ps），一个都不是 3520 的整数倍**；
> 例 1（clock resolution 1200 ps → 4800）里的数（0 / 29 / 47 / −30 / −48 …）**同样对不上**。
> **两条规则与例子之间这一处对不上，本篇没有一个字解释**
> （**可能是两条规则作用在不同层次、也可能是换算时把单位或前提丢了——两种都可能，本页不选**）。
> **本页只把「规则①按字面读与两个例子都不符」这一点记下来**（见「出处」瑕疵⑤）。

### 参数四格（细节在「语法 / 参数」节里，这里只说读法）

| 参数 | 要点 | 原文依据 |
|---|---|---|
| `jitter_set_name` | **名字必须是 `JSDF` 定义过的**——`Specifies the name of a jitter set that must have been defined with JSDF.` | 参数表（**文档事实**） |
| `clock_resolution` | **范围 `880`–`1750 ps`**；**拿它要用 `CLKR? EXACT` 查**；**单位是 ps 不是 ns** | 参数表三句（**文档事实**） |
| `offset_sequence` | **这是「返回值」那一格**——`The list of the calculated offsets that is returned.` | 参数表（**文档事实**） |
| `pinlist` | `Specifies the pins for which the offset sequence is calculated.` | 参数表（**文档事实**） |

**「单位是 ps 不是 ns」这一条原文用了整整一句去强调**（`Note that the unit is pico seconds, not nano seconds.`）
——**因为它的上游 `CLKR?` 返回的是 ns**（见「典型用法」里的换算），**这是这一族最容易填错的参数。**

**还有一个形状上的细节**：语法的**命令是 `JSWF?`，而回复的前缀是 `JSWF`**（没有 `?`）——
这一条在「语法 / 参数」节的 `returns:` 那一块里逐字写着，本页不重复抄。

### `## Predependencies`：**两条前置，来自两条不同的命令**

本篇**专门有一节**写前置（**这是同族里少见的**——同批的 [[jsud]] 就没有这一节），全文逐字：

> 「A jitter waveform must have been defined with JSCF. In the case of a predefined waveform,
> amplitude and period must also have been defined.」

| 前置 | 原文 | 谁提供 |
|---|---|---|
| **jitter 波形必须先定义** | `A jitter waveform must have been defined with JSCF.` | **`JSCF`**（[[jscf]]） |
| **若是预定义波形，幅度与周期也必须有** | `In the case of a predefined waveform, amplitude and period must also have been defined.` | **`JSCF` 的 `AMPLITUDE` / `PERIOD` 两格**（例 1 里就是这么查的：`JSCF "test",PERIOD,20,(IO0)` / `JSCF "test",AMPLITUDE,100,(IO0)`） |

**注意这里有一个容易读漏的错位**：**参数表说 jitter set 名要「用 `JSDF` 定义过」
（`must have been defined with JSDF`），而前置节说波形要「用 `JSCF` 定义过」**——
**两条前置指的不是同一个东西**：**名字归 `JSDF`、内容归 `JSCF`**
（**这一条与本 wiki 别的页对得上**：[[jsdf]] 那一页写着它「只干一件事：给一个抖动配置起个名字」，
而 [[jscf]] 那一页写着它「把抖动注入配置到指定 pin 上」）。
**本篇没有一句话把这两条前置并列解释过**，是**本页把它们摆在一起的**（**文档事实的拼接，不是推断**：
两句都在本篇里，各自逐字引在上面）。

### 关于 site 焦点：**两段话，一段与「查询」这个身份不符**

本篇正文里有两段讲 site 焦点的话（**在 `## Predependencies` 之前**），逐字如下：

> 「With this command you configure setups of those sites that have the setup focus: For more
> information, see also: PSFC, PSFC?.」

> 「With this command you can retrieve site specific information (only one site can be in focus at a
> time). For the site in focus, SmarTest displays results in the Testflow Editor and in the result
> tools. Also, any firmware queries report setup and results for the site currently in focus only.」

**第二段读起来是查询命令该有的**（`you can retrieve site specific information`、
`any firmware queries report … for the site currently in focus only`）。

**⚠️ 第一段写的是 `you configure setups`——「配置」——而 `JSWF?` 是一条只查不改的命令**
（它的语法是 `JSWF?`，返回值是 `offset_sequence`，**本篇没有任何一个参数是用来设值的**）。
**本页的判断（推断）**：**这一段是与同族其它命令共用的模板文字被抄了过来**；
**依据**是措辞与命令身份直接冲突，**而且 [[jscf]] 那一页的正文里也有同一句话**
（**那是另一篇 raw，本页没读**——本页是从那页 wiki 页面上看到它引的）。
**本页照原样引，不替它改成「retrieve」。**

## 典型用法

### Example 1：一次完整的「查波形 → 查分辨率 → 换算 → 查偏移序列」

原文的例子（**在「语法 / 参数」节里，本页不重复抄**）四步走得整整齐齐，**第三步是本页最该讲的一步**：

| 步 | 命令（逐字） | 它在干什么 |
|---|---|---|
| 1 | `> jscf? "test",,(IO0)` → 三行 `JSCF` 回复（`WAVEFORM,SINUS` / `PERIOD,20` / `AMPLITUDE,100`） | **查这个 jitter set 上 pin `IO0` 的波形**：正弦、周期 20、幅度 100 |
| 2 | `> CLKR? EXACT,101,(@)` → `< CLKR 101,2.4,1.2,(@)` | **查 timing specification 101 的 clock resolution** |
| 3 | `> jswf? "test",1200,(IO0)` | **把上一步的数换成 ps 再填进来** |
| 4 | `< JSWF "test","0,29,47,47,29,0,-30,…",(IO0)` | **拿到偏移序列**（原文说 `The reply is displayed in abbreviated form`，**整串约 500 项**） |

**第 2 步到第 3 步的换算是本页算出来的（推断）**：
`CLKR?` 的回复里第三个值是 **`1.2`**（原文自己说 `CLKR? returns the clock resolution as nano seconds`），
**`1.2 ns × 1000 = 1200 ps`，正好是下一行 `jswf?` 填的那个数**。
（**依据**：两个数在同一个例子里相邻出现、且单位说明就写在这一段的正文里；
**原文没有把这个换算写成一步**，它只说 `Note that CLKR? returns the clock resolution as nano
seconds, but that JSWF? expects it to be specified as pico seconds.`）
**所以照抄例子时，`1200` 这个数是从 `CLKR?` 的 `1.2` 来的，不是随手写的。**

> **⚠️ 顺带一条**：例 1 用来查 `CLKR?` 的 `101` 是 **timing specification 的编号**
> （`equation_set_no` 与 `specset_no` 合成的那种编号）。
> **而 `JSWF?` 的第一个参数是 jitter set 名（`"test"`）——两个参数不是一个体系的东西**，
> **本篇没有把「哪个 timing specification 的 clock resolution 该配哪个 jitter set」写出来**
> （**语料未写**：它只在例子里把两个数并排摆着）。

### Example 2：修正的那一步（**上一节已把算术做了一遍，这里只说怎么用**）

```
> JSCF? "test",WAVEFORM,(IO1)
< JSCF "test",WAVEFORM,"150,110,80,70,0"
> JSWF? "test",880,(IO1)
< JSWF "test","150,120,90,70,40",(IO1)
```

**用法上的两点**：

1. **`JSCF?` 查出来的那串数（`150,110,80,70,0`）是「用户定义的波形」的原样，
   而 `JSWF?` 返回的（`150,120,90,70,40`）是「按 clock resolution 修正过」的。**
   **两者不等是正常的，不是出错**（原文：`JSWF? will correct the list.`）。
2. **修正只发生在「下降超过 `max_diff`」的地方**——**上升与小幅下降都原样保留**
   （例 2 里第 4 项 `70` 就没被动）。

### 照本篇能确证的顺序

| # | 做什么 | 依据 |
|---|---|---|
| 1 | **`JSDF` 建 jitter set 名** | 参数表 `must have been defined with JSDF`（**文档事实**） |
| 2 | **`JSCF` 定义 jitter 波形**（预定义波形还要给幅度与周期） | `## Predependencies`（**文档事实**） |
| 3 | **`CLKR? EXACT` 取 clock resolution**，并把它**从 ns 换成 ps** | 参数表那两句 + 例 1（**文档事实 + 本页的换算推断**） |
| 4 | **`JSWF? "<jitter set 名>", <clock_resolution_ps>, (<pins>)`** | 语法行（**文档事实**） |

**本篇没有写「第 1、2 步的先后」**——`JSDF` 与 `JSCF` 的先后是**本页按各自职责排的（推断）**，
依据是 [[jsdf]] 那页说它「只起名」、[[jscf]] 那页说它「要求目标 jitter set 已定义」——
**两页的读法合起来才是这个顺序，本篇只给了「两条前置都必须在」。**

## 和谁有关

| 和谁 | 什么关系 | 依据 |
|---|---|---|
| [[jscf]] | **前置（内容侧）**。`## Predependencies` 第一句就是它：`A jitter waveform must have been defined with JSCF.`；**例 1 与例 2 都是用 `jscf?` 先查出波形再算偏移序列的** | 本篇 `## Predependencies` + 两个例子（**文档事实**）；**那篇 raw 本页没读** |
| [[jsdf]] | **前置（名字侧）**。`jitter_set_name` 那一格写着 `must have been defined with JSDF` | 本篇参数表（**文档事实**）；[[jsdf]]（**本页读过的 wiki 页**，只用来说明「它只起名」） |
| [[clkr]] | **上游（clock resolution 的来源）**。参数表点名 `You can retrieve the clock resolution for a specification with the CLKR? EXACT query.`；例 1 里就是它 | 本篇参数表 + 例 1（**文档事实**）；**`CLKR` 那篇 raw 本页没读** |
| [[jsud]] | **同族（删除侧）**。它是把本页查的这个 jitter set 删掉的那条命令；**同批建的页** | [[jsud]]（**本页读过的 wiki 页**）；**本篇一个字没提 `JSUD`** |
| [[jspr]] | **同族（primary 侧）**。它指定哪个 jitter set 会被用到；**本篇一个字没提 primary** | [[jspr]]（**本页读过的 wiki 页**） |
| [[psfc]] | **本篇正文点名的那一篇**（那句 `see also: PSFC, PSFC?` 里的链接指向它），用来解释「site 的 setup focus」这件事 | 本篇第一段末（**文档事实：链接在**）；**`PSFC` 那篇 raw 本页没读** |
| [[timing]] | **stage 页**。它的 L1「抖动注入（子专题）」一节把本页列在家族名单里；并给出归属判断「属本阶段」、以及「仅 [[ps1600]] 支持、仅对 drive pin 有效」 | [[timing]]（**本页读过的 wiki 页**）——**那一条的出处是 `02.06.16.01`，本页没读** |
| [[mapping-timing]] | **跨层对照表**。它的「抖动注入（本阶段的子专题）」一行 L1 列里就有 [[jswf]]，**其余各列全是 `?`** | [[mapping-timing]] 的主表（**本页读过的 wiki 页**） |
| [[waveform-set]] | **名字像、实质无关——必须点明**。本页名字里的 `WaveForm` 指的是**jitter 波形**（`JSCF` 定义的那种），**与 [[waveform-set]]（内存里的逻辑容器：wavetable + device cycle table + timing set）不是同一个东西**；**本篇一个字没提 waveform set** | [[waveform-set]]（**本页读过的 wiki 页**）；本篇全文（**文档事实：无此词**） |
| [[ps1600]] | **硬件侧的唯一允许型号**（来自 [[timing]] 的转述，**本页 raw 里没出现 `PS1600`**） | [[timing]]（**本页读过的 wiki 页**） |
| `Testflow Editor` / `result tools`（**均未建**） | **本篇说 site 焦点下的结果会显示在这两处**——**这几个词是本篇正文里的**，但**本篇没写它们是什么、在哪** | 本篇第一段（**文档事实：只有那句描述**）。**这两个名字不在 `prose-allowlist.txt` 里**，故用反引号写（§9.1） |
| [[smartest-7.0.1]] | **版本页**：本篇 `## Functional changes` 的唯一一条 | 本篇版本段（**文档事实**） |

## 版本

本文档**有** `## Functional changes` 段，段里**只有一条**：

- `Introduced in SmarTest 7.0.1`

> **这一条不是哨兵值**（**对照 §11.2 ②**）：措辞是 **`in`，不是 `before`**——
> **所以它说的是「`JSWF?` 是 SmarTest 7.0.1 引进的」**
> （**同批的 [[jsud]] 那一篇也是 `in SmarTest 7.0.1`**，**同族同版本**）。
> → [[smartest-7.0.1]]

**一条交叉印证（来自别的页，不是本页的 raw）**：[[timing]] 的 L1 抖动注入那一节写着
「SmarTest 7.0.1 引入」——**与本篇这一条是同一个版本号**
（**那一页的依据是 `02.06.16.01_Principles_of_jitter_injection`，本页没读那一篇**）。

**版本段里没有的东西**（照实记，不替它补）：**没有第二条**。
所以「`max_diff` 里那个 `410 ps` 是哪一版定的」「`clock_resolution` 的 880–1750 ps 范围变过没有」
**在本篇里查不到**。

## 出处

`sources:` **一篇**：

- `02_System_reference/02.06_Command_Reference/02.06.16.02.06_JSWF__-__Jitter_Set_WaveForm.md`
  （frontmatter 的 `source_topic` 是 **`119599_2.htm`**，**3,488 字节 / 116 行，整篇读完**——
  按 §11.5 口径：字节是 `st_size`，行数是 `wc -l`）
- 本页的「语法 / 参数」节是脚本从这一篇抽的（**本页一个字没动**）：
  抽的是 `## Syntax` / `## Parameters` / `## Examples` 三段。
  **本篇没有 `## Errors` / `## Warnings` 段**（实测：本篇的 `##` 级标题是
  `## Predependencies` / `## Syntax` / `## Parameters` / `## Application` / `## Examples` /
  `## Functional changes`），**所以本页没有「报错条件」节**——**骨架里本来就没有**，不是漏写。

**⚠️ 一处 §10 的「重复投放」，本页查了，形状与同批的 [[jsud]] 一模一样**：
本篇 `source_topic` 带 **`_2`** 后缀，实测有第二份：

| | 路径 | `source_topic` | 字节 |
|---|---|---|---|
| **本页的出处** | `02_System_reference/02.06_Command_Reference/02.06.16.02.06_JSWF__-__Jitter_Set_WaveForm.md` | `119599_2.htm` | **3,529** |
| **同页的另一份** | `02_System_reference/02.06_Command_Reference/02.06.02.02.151_JSWF__-__Jitter_Set_WaveForm.md`（字母序命令索引章） | `119599.htm` | **3,528** |

**又是差 1 个字节**——**和 [[jsud]]（686 vs 685）是同一个形状**。
**差在哪本页没看**（**只核了另一份的 frontmatter 与大小，没有读它的内容**）。
**两条合起来看，这是这一族的固定形状**：`02.06.16.02.0x` 那份带 `_2`、
`02.06.02.02.15x` 那份不带，**两份差 1 字节**。
（**记这一条是为了下一次遇到 `_2` 的人不必再从头查一遍**；
**本页的结论全部只来自 `119599_2.htm` 这一份。**）

**本页没做的**：

- **`02.06.16` 这一族其它篇的 raw 一篇没读**：`JRST` / `JSCF` / `JSDF` / `JSPR` / `JSUD` /
  `MSCF` / `MSDF`，以及族首的 `02.06.16.01_Principles_of_jitter_injection`、
  `02.06.16.02_List_of_commands_for_jitter_injection`。
  **所以「jitter 注入整体是怎么组织的」本页没有**——**本页只有「查偏移序列」这一个动作。**
- **`CLKR` 那一篇的 raw 没读**——本页只在**本篇**的参数表与例 1 里见过它
  （`CLKR? EXACT` 与 `CLKR 101,2.4,1.2`）。**所以「`CLKR?` 回复里哪个字段是 clock resolution」
  本页是从「1.2 ns → 1200 ps 这个数对上了」推的（已标推断）**，
  **不是从 `CLKR` 的文档读的**。
- **`JSCF` / `JSDF` 两篇的 raw 没读**——本页对它们的用法全部是**本篇的 `## Predependencies`
  与参数表**说的，外加 [[jscf]] / [[jsdf]] 两页 wiki 页的转述（**已逐处标明**）。
- **`PSFC` 那一篇没读**——所以「site 的 setup focus 怎么设」本页答不了。
- **`Testflow Editor` / `result tools` 没读**——本篇只说了「结果显示在那里」。
- **图**：**本篇对 `raw/` 的引用 0 处**——实测 `.png` / `.jpg` / `.gif` / `!\[` / `<img` / `raw/`
  六种写法在本篇里**全部 0 命中**。**所以本页没有任何来自图的结论，这张「没有图」是查过的事实，
  不是「够不着」。**
- **没有实跑。** 没在机台上敲过 `JSWF?`、没验过那个 30 ps 的修正行为、没验过 `max_diff` 公式
  在别的 clock resolution 下是否一样。**本页的算术是拿例子的数对出来的，不是跑出来的。**
  `verified: doc-only` 指的就是这件事。

**⚠️ 本篇的语料瑕疵，本页照实记下、一处都没替它改**：

> ① **一条查询命令的正文里写着「you configure setups」。**
> 逐字：`With this command you configure setups of those sites that have the setup focus: For more
> information, see also: PSFC, PSFC?.`
> **`JSWF?` 只有 `?` 形态、参数里没有一个能设值、返回值是 `offset_sequence`——
> 「configure」与它的身份直接冲突。**（**推断**：这是与同族其它命令共用的模板文字——
> **依据是 [[jscf]] 那一页的正文里也有同一句话**，而那条命令才真的是 configure。
> **本页照原样引，一个字没改。**）

> ② **同一个例子里，两条 `JSCF` 回复的形状不一样**：
> 例 1 的三行回复**都带 pinlist**（`< JSCF "test",WAVEFORM,SINUS,(IO0)` 等），
> 而**例 2 的回复没有**（`< JSCF "test",WAVEFORM,"150,110,80,70,0"`）——
> **而例 2 的查询是 `> JSCF? "test",WAVEFORM,(IO1)`，明明给了 pin**。
> **同一篇、两个例子、两种回复形状，原文没有解释**。**本页照原样引。**

> ③ **规则②那句以 `as follows` 结尾，而公式行是另起的、前面带一个缩进空格**：
> ` max_diff = clock_resolution/2 - 410 ps.`
> ——**`follows` 后面没有冒号**（同一篇里 `in two ways:` 那处是有冒号的）。
> **原文如此，本页照原样引。**

> ④ **规则①没给单位、也没给例子，而规则②给了 `ps`**：`4 * clock_resolution` 里的 `4` 是纯数，
> **乘出来是什么单位本篇没写**。（**这不是错，是本篇的写法**，记一笔。）

> ⑤ **规则①按字面读与两个例子都对不上**（**这是本页查出来的，不是原文写的**）：
> 规则①要求相邻两项的距离是 `4 × clock_resolution` 的整数倍——
> 例 2 的 clock resolution 是 880 → 要求是 **3520 ps** 的整数倍，
> **而例 2 输出里的距离是 30 / 30 / 20 / 30（ps）**；例 1 是 1200 → 4800，
> **它那串数（0 / 29 / 47 / −30 / −48 …）同样不是 4800 的整数倍**。
> **本篇没有一个字解释这个对不上**，**本页不替它调和**（两种可能都不排除，见「是什么」那节）。

> ⑥ **参数表仍然没有表头行**（从一条空的第一格 ` | ` 直接开始）——
> **与 [[jsud]] / [[wavetable]] / [[waveform-set]] 同一个形状**（这一族文档的 HTML→md 压平共性）。
> **本页照原样留它，没有补表头。**

`verified: doc-only`
