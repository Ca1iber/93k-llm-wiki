---
type: object
title: SPST? - (SPecset STatus)
layer: L1
stage: level
tags: [spst, firmware-query, specset, status-bits, violation-check, timing-level]
related: [sprm, svlr, pslv, drlv, rclv, pclk, clkr, etim, etds, term, spec-tool, level-setup-tool, timing-setup-tool, smartest-6.3.2]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.23_SPST__-__SPecset_STatus.md
created: 2026-09-21
updated: 2026-09-21
verified: doc-only
---

# SPST? - (SPecset STatus)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **3,665 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.05.02.23_SPST__-__SPecset_STatus.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
SPST? {spec_type}, {equation_set_no}, {specset_no}
```

returns:

```
SPST {spec_type}, {equation_set_no}, {specset_no}, {status}
```

or, for multiport specifications:

```
SPST? {spec_type}, , {"multi-port_spec"}
```

or

```
SPST? {spec_type}, PRM,
```

returns:

```
SPST {spec_type},, {"multi-port_spec"}, {status}
```

### Parameters

|

spec_type

 |

Which specification type to use. Use:

 |
 |

LEV

 |

to specify levels, or

 |
 |

TIM

 |

to specify timing.

 |
 |

equation_set_no

 |

Equation set number. An integer in the range 0 to 256.

Use ALL to refer to all defined equation sets. Use PRM to specify the primary equation set. In the latter case, the specset_no parameter is ignored.

Equation set 0 is used for compatibility with a non-equation based testing environment. In this case, when equation set 0 is used and spec_type is LEV, specset_no is meaningless, while when equation set 0 is used and spec_type is TIM, specset_no is interpreted as the number of a waveform set.

 |
 |

specset_no

 |

Spec set number. An integer in the range 1 to 99. Use ALL to refer to all defined spec sets.

 |
 |

multi-port_spec

 |

In a multi-port setup, enter the name of a specification instead of a spec set number. In this case, the equation_set_no parameter must be left empty.

 |
 |

status

 |

An integer that indicates the settings of the status bits. Every set bit is represented by a power of 2, as described in the table below. The integer is the sum of these powers.

For example, if 768 = 512 + 256 is returned, then bits 8 and 9 are set, and all other bits are cleared.

 |

Status bits for the status parameter
 |

Bit

 |

Description

 |

Value

 |
 |

0

 |

Not available/defined.

 |

1

 |
 |

1

 |

Drive 1 period limit violation.

 |

2

 |
 |

2

 |

Receive 1 period limit violation.

 |

4

 |
 |

3

 |

Drive 2 period limit violation.

 |

8

 |
 |

4

 |

Receive 2 period limit violation.

 |

16

 |
 |

5

 |

Drive edge order violation.

 |

32

 |
 |

6

 |

Tri-state edge order violation.

 |

64

 |
 |

7

 |

Window edge order violation.

 |

128

 |
 |

8

 |

It is possible to modify the timing or level data with `ETIM`（raw: `02.06.02.02.118_ETIM__ETIM__-__Edge_TIMing.md`）(`ETDS`（raw: `02.06.02.02.117_ETDS__ETDS__-__Edge_Timing_Definition_String.md`）), `PCLK`（raw: `02.06.02.02.175_PCLK__PCLK__-__Pin_CLocK.md`）, `CLKR`（raw: `02.06.02.02.24_CLKR__CLKR__-__CLocK_Resolution.md`）, `DRLV`（raw: `02.06.02.02.89_DRLV__DRLV__-__DRive_LeVel.md`）, `RCLV`（raw: `02.06.02.02.204_RCLV__RCLV__-__ReCeive_LeVel.md`）, `TERM`（raw: `02.06.02.02.257_TERM__TERM__-__TERMination_mode.md`）, and `PSLV`（raw: `02.06.02.02.195_PSLV__PSLV__-__Power_Supply_LeVel.md`）. If any of these commands are executed, this bit is set automatically for the affected specset, and the restore should bring back the original SPST status.

 |

256

 |
 |

9

 |

Modified with `SHVL`（raw: `02.06.02.02.222_SHVL__SHVL__-__SHmoo_spec_VaLues.md`）.

 |

512

 |
 |

10

 |

Modified with `SVLR`（raw: `02.06.02.02.252_SVLR__SVLR__-__Spec_VaLues_at_Runtime.md`）.

 |

1024

 |
 |

12

 |

Absolute range violation.

 |

2048

 |
 |

13

 |

Relative range violation

 |

4096

 |
 |

14

 |

Drive 10 period limit violation

 |

8192

 |
 |

15

 |

Receive 10 period limit violation

 |

16384

 |

### Example 1

```
> SPST? lev,all,all
< SPST LEV,1,1,0
```

### Example 2

```
> SPST? tim,all,all
<  SPST TIM,1,1,0
< SPST TIM,2,22,0
```

### Example 3

```
> SPST? TIM,,"mu_burst"
< SPST TIM,,"mu_burst",6
```

In this last example, a multi-port specification is queried. The answer says that bits 1 and 2 have been set. This has the effect that a drive or receive period 1 limit violation will be ignored, and only a period 2 limit violation will be recorded.

<!-- 语法节 end -->

## 是什么

**`SPST?` 问的不是「某个 spec 的数值是多少」，而是「这个 specset 现在处于什么状态」。**
原文定义句逐字：

> 「The SPST? query returns the current settings of the status bits. Most of these bits determine
> what kind of violation checks are performed with respect to edge order and periods when a test is
> executed; the check is performed when its associated bit is cleared, and omitted when it is set.
> The rest of the bits indicate if the timing has been modified by certain firmware commands.」

**这句话里有两类位，而且第一类的语义是反的：**

| 类 | 位 | 语义 |
|---|---|---|
| **违例检查开关** | 位 1–7、12–15 | **位被清零 → 执行检查；位被置位 → 跳过检查** |
| **被改过的痕迹** | 位 8、9、10 | 位被置位 = 有某条命令动过这个 specset |

**「清零才查、置位不查」是本页要记住的第一件事**——
**注意这与直觉相反**（一般会以为「置位 = 打开开关」）。
原文把它写在同一句里：`the check is performed when its associated bit is cleared, and omitted
when it is set.`

**位 0 是空的**：原文 `Not available/defined.`，占着 `1` 这个值。

### 一整张位表（**语法节里已逐字，本页只做读法**）

**`status` 是一个整数，是各位之和**（原文：`The integer is the sum of these powers.`）。
原文给的读法例子逐字：

> 「For example, if 768 = 512 + 256 is returned, then bits 8 and 9 are set, and all other bits are
> cleared.」

**所以 `768` 要读成「位 8 + 位 9」，不是「768 这个量」。**

**按「谁管什么」重排**（**位号与值逐字来自语法节那张表**）：

| 组 | 位 | 值 | 原文描述 |
|---|---|---|---|
| **空位** | 0 | 1 | `Not available/defined.` |
| **period 违例（前段）** | 1 | 2 | `Drive 1 period limit violation.` |
| | 2 | 4 | `Receive 1 period limit violation.` |
| | 3 | 8 | `Drive 2 period limit violation.` |
| | 4 | 16 | `Receive 2 period limit violation.` |
| **edge order 违例** | 5 | 32 | `Drive edge order violation.` |
| | 6 | 64 | `Tri-state edge order violation.` |
| | 7 | 128 | `Window edge order violation.` |
| **被命令改过** | 8 | 256 | `ETIM`(`ETDS`) / `PCLK` / `CLKR` / `DRLV` / `RCLV` / `TERM` / `PSLV` 之一动过 |
| | 9 | 512 | `Modified with SHVL.` |
| | 10 | 1024 | `Modified with SVLR.` |
| **范围违例** | 12 | 2048 | `Absolute range violation.` |
| | 13 | 4096 | `Relative range violation` |
| **period 违例（后段）** | 14 | 8192 | `Drive 10 period limit violation` |
| | 15 | 16384 | `Receive 10 period limit violation` |

**三处要注意的：**

**① 位 11 在这张表里根本没有。** 表从位 10 直接跳到 12
（**见 `## 出处` ①**）。**原文没有解释位 11 是什么、为什么空着。**

**② period 违例只给了 1、2、10 三档，中间 3–9 没有。** 位 1–4 覆盖
`Drive 1` / `Receive 1` / `Drive 2` / `Receive 2`，位 14–15 直接跳到
`Drive 10` / `Receive 10`。**`Drive 3` 到 `Drive 9` 有没有对应位，原文没说。**

**③ 位 8 是唯一一条把命令清单写进描述里的。** 逐字：

> 「It is possible to modify the timing or level data with ETIM(ETDS), PCLK, CLKR, DRLV, RCLV,
> TERM, and PSLV. If any of these commands are executed, this bit is set automatically for the
> affected specset, and the restore should bring back the original SPST status.」

**「这七条命令动过 → 位 8 自动置位」**，而且**原文说 restore 应当把这个位恢复回去**
（`the restore should bring back the original SPST status`）——
**但「restore」是什么动作、由谁发起，原文没说。**

### 站点相关：只对当前 focus 的那个 site

原文第二段逐字：

> 「With this command you can retrieve site specific information (only one site can be in focus at a
> time). For the site in focus, SmarTest displays results in the Testflow Editor and in the result
> tools. Also, any firmware queries report setup and results for the site currently in focus only.」

**即：查出来的状态只属于「当前 focus 的那个 site」。**
**这句不只是关于 `SPST?`**——原文说的是 `any firmware queries`（**所有固件查询**）。
**所以同一个 setup 上换一个 focus 的 site，查询结果可能不同。本页只有这一句，
focus 怎么切在别处。**

### 四条语法形态（**语法节里已逐字**）

| # | 形态 | 说明（原文） |
|---|---|---|
| 1 | `SPST? {spec_type}, {equation_set_no}, {specset_no}` | 常规；返回 `SPST {spec_type}, {equation_set_no}, {specset_no}, {status}` |
| 2 | `SPST? {spec_type}, PRM,` | 主 equation set；**`specset_no` 被忽略** |
| 3 | `SPST? {spec_type}, , {"multi-port_spec"}` | 多端口；**`equation_set_no` 必须空着** |
| 4 | 返回形态 | 多端口时返回 `SPST {spec_type},, {"multi-port_spec"}, {status}` |

**参数范围**（**逐字来自语法节**）：
`spec_type` 取 `LEV` 或 `TIM`；`equation_set_no` 是 **0 到 256**，
另有 `ALL`（所有已定义的 equation set）与 `PRM`（主 equation set）；
`specset_no` 是 **1 到 99**，另有 `ALL`。

**`equation_set_no = 0` 那一格有一段特例**，逐字：

> 「Equation set 0 is used for compatibility with a non-equation based testing environment. In this
> case, when equation set 0 is used and spec_type is LEV, specset_no is meaningless, while when
> equation set 0 is used and spec_type is TIM, specset_no is interpreted as the number of a
> waveform set.」

**即：equation set 0 = 「非 equation based 的老环境」兼容位。**
**此时同一个 `specset_no` 位置在 `LEV` 与 `TIM` 下含义不同**——
**`LEV` 下无意义，`TIM` 下改读成 waveform set 编号。**

### `Application`

原文 `## Application` 列四项：**Level setup / Timing setup / Testflow / Spec tool**。
**（注意：本篇的 `Application` 是四项，而 [[uptd]] / [[dscp]] 那两篇各自只有一句。）**

## 典型用法

**原文有 `## Examples`（三个，已在语法节里逐字），没有 `## Procedure`、没有 `## Before you begin`。**

| 例 | 请求 | 返回 | 读法 |
|---|---|---|---|
| 1 | `SPST? lev,all,all` | `SPST LEV,1,1,0` | 所有 equation set / spec set——**但只回了一行**（equation set 1、spec set 1、状态 0） |
| 2 | `SPST? tim,all,all` | `SPST TIM,1,1,0` 与 `SPST TIM,2,22,0` | **回两行**：equation set 1 与 2；**第二行的 spec set 是 22，不是 1** |
| 3 | `SPST? TIM,,"mu_burst"` | `SPST TIM,,"mu_burst",6` | `6 = 2 + 4` → **位 1 与位 2 置位** |

**例 1 与例 2 的差别值得注意**：两次都问 `all,all`，**例 1 只回一行，例 2 回两行**。
**原文没有解释为什么——两台环境的 equation set 数量不同是（推断），
因为 `all` 说的是「所有**已定义**的」。**

**例 3 的读法原文自己给了**，逐字：

> 「In this last example, a multi-port specification is queried. The answer says that bits 1 and 2
> have been set. This has the effect that a drive or receive period 1 limit violation will be
> ignored, and only a period 2 limit violation will be recorded.」

**这句话把「置位 = 跳过检查」坐实了**：
位 1（`Drive 1 period limit violation`）与位 2（`Receive 1 period limit violation`）被置位
→ **period 1 的 drive/receive 违例**不报**，只剩 period 2 会记录。
**这是本页唯一一处由原文给出的「位 → 后果」的完整例子。**

**从原文能落成的动作：**

| 要做的 | 依据 |
|---|---|
| 查某个 specset 有没有违例、有没有被改过 | `SPST? {spec_type}, {equation_set_no}, {specset_no}` |
| **想「关掉」某一类检查** | **把对应位**置位**（不是清零）**——原文 `omitted when it is set` |
| 想一次查完 | 两个编号位都用 `ALL` |
| 查主 equation set | 第二个参数写 `PRM`，**第三个参数会被忽略** |
| 查多端口 spec | `SPST? TIM,,"名字"`——**中间那个逗号不能省**（例 3 逐字如此） |
| 想兼容非 equation based 环境 | 用 equation set `0`；**`TIM` 下 `specset_no` 当 waveform set 编号读** |
| **解读返回的整数** | **拆成 2 的幂之和**，再对位表——`768` → 位 8 + 位 9 |
| 要改状态 | **本页给不出语法**——见下 |

**⚠️ 本篇只有查询，没有设置语法。** 原文标题、`## Syntax` 四段、三个例子
**全部是 `SPST?`（带问号）**，返回串才是 `SPST`（不带问号）。
**所以「怎么把某个位置位」这篇文档没有给**——
**尽管它的定义句明确说这些位是用来「决定执行哪些检查」的，也就是说必须能被设置。
本页不替它编语法。**

## 和谁有关

- [[sprm]] — **语法上的一处咬合**：本篇 `SPST?` 的 `equation_set_no` 可以写 `PRM`
  （**primary equation set**）。**`SPRM` 的名字正是 `Set PRiMary sets`**，
  **（推断）两篇讲的是同一个「主 set」概念的两侧（一个负责设、一个负责查）**；
  **依据只有名字与 `PRM` 这个缩写，两篇原文都没有互相引用。**
- [[svlr]] — **位 10 的所指**：`Modified with SVLR.`——**spec 值在运行期被改过**。
  **本页只有这一个名字，`SVLR` 怎么改在那页。**
- [[pslv]] / [[drlv]] / [[rclv]] / [[pclk]] / [[clkr]] / [[etim]] / [[etds]] / [[term]] —
  **位 8 那七条命令的全部所指**（**加上 `ETIM(ETDS)` 里的两条，共七条**）。
  **原文把七条并列在同一个位里，没有区分谁改电平、谁改时序——
  尽管位 8 的描述里同时提到了 `timing or level data` 两类。**
  **本页只有「这七条会置位 8」，各自改什么在各自那页。**
- [[waveform-set]] — **`equation set 0` + `spec_type = TIM` 时 `specset_no` 改读成它**。
  **本页只有这一句「改读」，waveform set 本身在那页。**
- [[spec-tool]] / [[level-setup-tool]] / [[timing-setup-tool]] — **`## Application` 四项里的三项**。
  **原文只给了名字，没有一句说明本命令在这三处怎么用。**
- [[testflow]] — **`## Application` 第四项**；
  原文第二段还说 focus site 的**结果显示在 `Testflow Editor` 和 result tools 里**。
- [[equation-based-level-setup]] — **`equation set` 这件事的那一侧**。
- [[term]] — **位 8 那七条里的最后一条**（原文写 `TERM`，全称 `TERMination mode`）。
  **本页只有「它会置位 8」，`TERM` 改的是什么在那页。**
- `SHVL`（**未建**）— **位 9 的所指**（`Modified with SHVL.`）。**不在 allowlist，用反引号。**
- `Testflow Editor`（**未建**）— 原文第二段点名它显示 focus site 的结果。
- `restore`（**未建、原文也没解释**）— 位 8 那句里的 `the restore should bring back the
  original SPST status`。**这个动作是什么、谁发起，原文没说。**

## 版本

`## Functional changes` **只有一条，逐字**：

- Introduced before SmarTest 6.3.2

**这一条是 §11.2 ② 那个哨兵。** `Introduced before SmarTest 6.3.2` 的意思是
**「早于语料覆盖范围」**，**不是「6.3.2 新增」**——
**所以 `SPST?` 本身成立于哪个版本，这份语料里没有。**

**本篇再无别的版本条目**，**也没有一条提到位表变过**——
**位 11 的空缺、period 3–9 的缺口，到底是一直如此还是被删过，语料里没有依据。**

详见 [[smartest-6.3.2]]。

## 出处

`sources:` 一篇：
`02_System_reference/02.06_Command_Reference/02.06.05.02.23_SPST__-__SPecset_STatus.md`

**本页没做的：**

- **语法节这一次抽得很全（3,665 字符，几乎是整篇）。**
  `## Syntax` / `## Parameters`（含整张位表）/ 三个 `### Example` **都在语法节里**。
  **所以本页正文里没有重新抄那两张表，只做重排与读法**——
  **要精确到位号与值，看语法节，不要看本页的转述。**
- **`## Application` 的四项没读** —— 原文只有名字，
  **本命令在 Level setup / Timing setup / Testflow / Spec tool 各怎么用，本页一个字都没有。**
- **位 8 那七条命令（`ETIM`/`ETDS`/`PCLK`/`CLKR`/`DRLV`/`RCLV`/`TERM`/`PSLV`）一条都没读** ——
  **所以「置位 8 之后具体哪一份数据变了」本页不知道。**
- **`SHVL` 没读**（**原文也没解释它做什么**，只说 `Modified with SHVL.`）。
- **[[svlr]] 没读** —— 同上，位 10 的「运行期改过」具体改什么，本页没有。
- **`restore` 没读、原文也没解释** —— 位 8 那句的落点。
- **`Testflow Editor` / result tools 没读** —— 原文第二段点名它们显示 focus site 的结果。
- **`spec` / `specset` / `equation set` 三者的关系，本页没有** ——
  本篇默认读者已经知道，**只给了编号范围，没有给定义**。
- **怎么把状态位设起来，本页没有**（**原文也没有**，见 `## 典型用法` 末尾那一段）。
- **一张图都没有。** 原文没有图片。
- **没有交叉验证任何别处的文档**（§11：本页只写这一篇里有的）。
  **尤其：本页 `layer: L1`、`stage: level`，这个归属是本页照 wiki 的既有划分填的，
  不是本篇文档写出来的**——**原文 `## Application` 同时列了 Timing setup 与 Testflow。**

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> **① 位表里没有位 11。** 表从位 10（`1024`）直接跳到位 12（`2048`）——
> **位 11 的「值」应该是 `2048`，而原文把 `2048` 给了位 12。**
> **两种可能，原文都没明说**：**(a) 位 11 从未定义（像位 0 那样空着但没写出来）；
> (b) 位 11 曾经存在、被删掉了。** **本页并列，不判。**
>
> **② 位 0 是唯一一个「有值但没有用途」的位。** 逐字：
> `0 | Not available/defined. | 1` ——**它占着 `1` 这个值，
> 所以任何奇数状态值都含一个「无意义」的位。** **原文没解释为什么给它留值。**
>
> **③ period 违例的档位不连续。** 位 1–4 是 `Drive 1` / `Receive 1` / `Drive 2` / `Receive 2`，
> 位 14–15 **直接跳到** `Drive 10` / `Receive 10`。
> **`Drive 3` 到 `Drive 9`、`Receive 3` 到 `Receive 9` 有没有对应位，原文没说。**
> **（其中 `Receive 10` 与 `Drive 10` 的描述末尾还没有句号，位 13 那一行也是
> `Relative range violation` 无句号——与位 1–7 那七行都带句号不一致。）**
>
> **④ `## Parameters` 的表头坏了，和 [[dscp]] / [[uptd]] 同一处毛病。** 原文开头逐字：
> ```
>  |
> 
> spec_type
> ```
> ——**第一行是一个孤立的 ` | `，没有 `Option` / `Description` 那样的表头行。**
> **同一张表中间又插了一行 `Status bits for the status parameter` 加
> `Bit` / `Description` / `Value` 三格**，**等于一张表里套了第二张表的表头**，
> **而 `status` 那一段的说明文字就挤在这两段表头之间。**
>
> **⑤ 位 8 的说明文字里有链接被拆断。** 逐字（语法节里也看得出）：
> `[ETIM](...)([ETDS](...))` ——**`ETIM` 后面紧跟一个括号套括号，
> 读起来像是 `ETIM(ETDS)` 是一个整体，但两个都是独立链接。**
> **本页在表里写成 `ETIM`(`ETDS`)，不替它改结构。**
>
> **⑥ 例 2 的第二行返回前面多一个空格。** 逐字：
> ```
> > SPST? tim,all,all
> <  SPST TIM,1,1,0
> < SPST TIM,2,22,0
> ```
> ——**第一行 `<` 后面是两个空格**，第二行是一个。**这是原文就有的。**
>
> **⑦ 状态位「怎么设置」全文缺失。** 定义句说这些位**决定**执行哪些检查
> （`determine what kind of violation checks are performed`），
> **但 `## Syntax` 只有 `SPST?`，三个例子也全是查询。**
> **一篇自称「状态」的命令文档，只给了读、没给写。**
>
> **⑧ 例 1 与例 2 都问 `all,all`，返回行数却不同**（一行 vs 两行）。
> 原文没有解释。**本页按「`all` 指所有**已定义**的」这个（推断）说明，
> 但没有第二处依据。**
>
> **⑨ `Application` 四项之间没有任何说明文字**，只是一列名字加短横线。
> **[[uptd]] / [[dscp]] 那两篇的 `Application` 是句子（虽然极短）**，
> **这三篇的 `Application` 一节写法彼此都不同。**
>
> **⑩ 本篇没有 §11.2 ① 那种 `鈥` 形态的编码损坏**（本页通读全篇，0 处）。

`verified: doc-only`
