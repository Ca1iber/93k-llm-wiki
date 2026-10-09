---
type: object
title: PACT, PACT? - (Parallel ACTivities control)
layer: L1
stage: pin
tags: [pact, l1, firmware-command, pin, multi-site, site, mask, active, site-control, tpi, pals, results]
related: [pin, site-control-window, pals, pals-before-other-setup, stme, pqfc, psfc, controlling-multiple-sites, command-reference, smartest-6.3.2]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.171_PACT__PACT__-__Parallel_ACTivities_control.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# PACT, PACT? - (Parallel ACTivities control)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **2,262 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.171_PACT__PACT__-__Parallel_ACTivities_control.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### PACT

PACT {control}, {site|ALL}

PACT {"site_string"}

### PACT?

```
PACT?
```

returns

```
PACT {control}, {site}
```

Or:

```
PACT?STR
```

returns

```
PACT {"site_string"}
```

### Parameters

| control | The control parameter is: | The control parameter is: |
|---|---|---|
|  | ACTIVE | When a site is ACTIVE it receives all test data, and generates results for the tests. |
|  | MASKED | When a site is MASKED, it receives all test data, as with the ACTIVE parameter. However, the receivers for the site are disabled and no result information is available. |
| site | A single integer representing a site number. | A single integer representing a site number. |
| site_string | A string consisting of "0" and "1". One character must be given for every site that is configured in the pin configuration. "0" indicates that the respective site is (to be) masked. "1" indicates that the respective site is (to be) activated. | A string consisting of "0" and "1". One character must be given for every site that is configured in the pin configuration. "0" indicates that the respective site is (to be) masked. "1" indicates that the respective site is (to be) activated. |
| ALL | means that all configured sites that are available for testing (that is, do not use a channel that is inactivated in the MCDIgnore file) are to be activated or masked.<br><br>For the MCDIgnore file see MCDIgnore usage and restrictions in Service Guide Part 1. | means that all configured sites that are available for testing (that is, do not use a channel that is inactivated in the MCDIgnore file) are to be activated or masked.<br><br>For the MCDIgnore file see MCDIgnore usage and restrictions in Service Guide Part 1. |
| STR | forces the query to return a site string instead of a single line for every site. | forces the query to return a site string instead of a single line for every site. |

> ⚠️ 转录说明（非原文）：本表在上游 HTML 里含合并格（colspan / rowspan）；
> 跨格文字已按覆盖范围重复写出（**不是原表里有重复的格子**）。真结构见 `tdc-html/agent-html/98678.htm`。

### Example

```
> PACT ACTIVE, 1
> PACT MASKED, 2
> PACT MASKED, 3
```

This example masks site 2 and site 3, and makes site 1 active.

```
> PACT?
< PACT ACTIVE,1
< PACT MASKED,2
< PACT MASKED,3
> PACT? STR
< PACT "100"
```

This example shows the impact of the optional STR parameter for the query.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.171_PACT__PACT__-__Parallel_ACTivities_control.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if not all pins at the site have had their channels assigned by the `PALS`（raw: `02.06.02.02.173_PALS__PALS__-__Pin_ALlocation_for_multiple_Sites.md`） command.

<!-- 报错节 end -->

## 是什么

**`PACT` 管的是「哪些 site 算数」——把 site 置成 `ACTIVE` 或 `MASKED`。** 原文：

> 「The PACT command allows you to mask or activate specific sites. It is used by the Site Control window, and also during testflow execution if the test suite is requested to run serially, or if after a branch, some sites follow a different execution path.」

四件事：① 动作只有两个——**activate** / **mask**；② 它是 **Site Control window**（[[site-control-window]]）用的；
③ **testflow 执行时也会用它**，两个场景：**test suite 被要求串行跑**、
**分支之后各 site 走了不同的执行路径**；④ `PACT?` 查状态：

> 「The PACT? query returns the current status of the sites.」

### ⚠️ 两条「用之前必须知道」的话

**第一条：每执行一次就清所有 site 的结果。**

> 「Note that every execution of the PACT command resets the results of all sites, even if only one site is specified in the command.」

**就算你只指定一个 site，所有 site 的结果都会被 reset。**
（`resets` 到什么程度、清的是哪一类结果，**本篇没写**——见「出处」。
**推断**：按字面读，下面例子那三行命令就是三次 reset；**原文没有把这两处并排说。**）

**第二条：程序里别用它。**

> 「Note This command implements the tpi interface for multisite testing. Use the tpi call instead of this firmware command.」

**这条命令是为 tpi 接口服务的；程序里应当调 tpi，而不是发这条固件命令。**
（`tpi` 是什么、那个 call 长什么样，**本篇一个字没写**。开头的 `Note` 是上游那个 note 块的标题，
不是句子的一部分——同族的转换现象见「出处」⚠️ ④ 那一族。）

### 两个动作的差别**只在「收不收结果」**

> 「When a site is ACTIVE it receives all test data, and generates results for the tests.」

> 「When a site is MASKED, it receives all test data, as with the ACTIVE parameter. However, the receivers for the site are disabled and no result information is available.」

| 动作 | 收测试数据 | 出结果 |
|---|---|---|
| `ACTIVE` | **收** | **出** |
| `MASKED` | **收**（与 `ACTIVE` 一样） | **不出**——`the receivers for the site are disabled` |

**⚠️ `MASKED` 不是「不跑」。** 两格的头一句都是 `it receives all test data`——
**差别在 receivers 被禁用，所以没有结果信息。** 这是最容易读错的一处。

### 三种写法：单个 site、site 串、`ALL`

| 写法 | 原文 |
|---|---|
| `site` | `A single integer representing a site number.` |
| `site_string` | `A string consisting of "0" and "1". One character must be given for every site that is configured in the pin configuration. "0" indicates that the respective site is (to be) masked. "1" indicates that the respective site is (to be) activated.` |
| `ALL` | `means that all configured sites that are available for testing (that is, do not use a channel that is inactivated in the MCDIgnore file) are to be activated or masked.` |

**`site_string` 有三条硬要求**：① 只由 `0` / `1` 组成；② **pin configuration 里配置了的 site 每个都要占一个字符**；
③ `0` = masked、`1` = activated。

**⚠️ `ALL` 不等于「所有 site」**：括号里排除了一批——**用到了 `MCDIgnore` 文件里被停用通道的 site 不算**。
原文紧接着给出处：`For the MCDIgnore file see MCDIgnore usage and restrictions in Service Guide Part 1.`
（**这一句在 md 里已经掉成纯文本、没有链接**，见「出处」⚠️ ⑥；**那一段本页没读**。）

### 查询的两种形态：`PACT?` 与 `PACT?STR`

| 形态 | 回什么 |
|---|---|
| `PACT?` | **每个 site 一行**：`PACT {control}, {site}` |
| `PACT?STR` | **一个 site 串**：`PACT {"site_string"}` |

`STR` 那一格的原文：

> 「forces the query to return a site string instead of a single line for every site.」

**例子把两种形态并排给了**（原文 `## Example` 第二段，逐字）：

```
> PACT?
< PACT ACTIVE,1
< PACT MASKED,2
< PACT MASKED,3
> PACT? STR
< PACT "100"
```

**⚠️ 语法块里写的是 `PACT?STR`（`?` 后没有空格），例子里写的是 `PACT? STR`（有空格）。**
（**已核上游 `98678.htm`：上游就是这两种写法**，见「出处」⚠️ ①。）

### 报错与警告各一条，**但只有一条进了「报错条件」节**

| 段 | 逐字 | 进没进本页的「报错条件」节 |
|---|---|---|
| `## Warnings` | 「If a site is unavailable, PACT will issue a warning.」 | **没有**（52 字符，脚本的阈值是 60） |
| `## Errors` | 见下面的「报错条件」节（176 字符） | **有** |

**两条都要读**：错误那条说的是 **`PALS` 没把 site 上的通道分完**；
警告那条说的是 **site 不可用**（`a site is unavailable`——**「不可用」的判据本篇没写**）。

## 典型用法

**原文没有 `## Procedure` / `## Before you begin` / `## What to do next` 段。** 用法全部来自 `## Example` 两段。

**1. 逐个 site 设**（原文第一段例子，逐字）：

```
> PACT ACTIVE, 1
> PACT MASKED, 2
> PACT MASKED, 3
```

> 「This example masks site 2 and site 3, and makes site 1 active.」

**⚠️ 这里正是「每执行一次清一次结果」撞上的地方**：上面是**三条命令**，按开头那句 Note，
**每一行都会 reset 所有 site 的结果**。**原文没有提醒这一点。**

**2. 一次看全部**（原文第二段例子，逐字见「是什么」）：`PACT?` 逐 site 一行；`PACT? STR` 一行串。

**3. site 串怎么读**：`PACT "100"` 与上面三条命令**对得上**——
site 1 = `1` = ACTIVE、site 2 = `0` = MASKED、site 3 = `0` = MASKED。
**串长 = pin configuration 里配置的 site 数**（`## Parameters` 明写）。

**4. 什么时候会用它**：`## Application` 一句 `Site Control window.` ＋ 正文那句（test suite 串行 / 分支后各 site 走不同路径）。
**所以正常路径是 GUI 的 Site Control window 发它**；程序里另有一条 Note 说改用 tpi（见「是什么」）。

**5. `ALL` 的坑**：它排除了 `MCDIgnore` 里被停用通道的 site——
**所以 `PACT MASKED, ALL` 与「把所有 site 都 masked」不是一回事**
（**推断**，依据是 `ALL` 那一格的括号补充；**原文没有这句对比**）。

**6. 出错**：见「报错条件」节那一条——**`PALS` 没把 site 上的通道分完就报错**。
**这条把 `PACT` 与 `PALS` 的先后绑上了**（同族的顺序约束见 [[pals-before-other-setup]]）。

## 和谁有关

- [[pin]] — `stage: pin` 的落点：它管的是 **site 与通道（pin channel）**的关系，报错也报在通道分配上。
- [[site-control-window]] — **GUI 侧，也是 `## Application` 唯一的指向**（原文：`Site Control window.`）。
  **本页没读那一页**，所以窗口长什么样、还有哪些操作会发 `PACT`，本页没有。
- [[pals]] — **前置**：`## Errors` 逐字说报错的条件是
  `not all pins at the site have had their channels assigned by the PALS command`。
  **已核上游 `98678.htm`：那个 `PALS` 链接的 `title` 属性写着**
  `The PALS command defines the channel numbers for pins on sites other than site 1.`
  ——**即 `PALS` 管的是 site 1 以外那些 site 的通道号**。**这条在 md 里搜不到。** **本页没读 [[pals]]。**
- [[pals-before-other-setup]] — **同族的顺序约束页**（`PALS` 必须在其他 setup 命令之前）。**本页没读。**
- [[stme]] — **同章的另一条多 site 命令，管的是另一件事**：`STME` 管「各 site 同时起还是依次起」，
  `PACT` 管「哪个 site 出结果」。**两条都出现在 `02.06.03.01.01_Introduction` 同一行的
  `Commands for multi-site setups:` 串里**（见「出处」的入边）。
- [[pqfc]] / [[psfc]] — **同一串 `Commands for multi-site setups:` 里的另外两条**
  （`PQFC` = 并行查询焦点、`PSFC` = 并行 site 焦点；**这里用的是页标题**）。**两页本页都没读。**
- [[controlling-multiple-sites]] — **多 site 的上位概念页**。**本页没读**；`PACT` 在那一页里怎么讲，本页不知道。
- `tpi` / `MCDIgnore`（**均不在 allowlist 里，按 §9.1 用反引号**）—— 前者是那条 Note 让程序改用的接口，
  后者决定哪些 site 算 `available for testing`。
- [[command-reference]] — **归属**：本篇在 `02.06_Command_Reference` 下。

## 版本

`## Functional changes` 段有，**只有一条**，逐字：

```
- Introduced before SmarTest 6.3.2
```

**哨兵值**（§11.2 ②）：`before` 说明它在本文档集覆盖范围开始之前就已经有了，
**具体哪个版本引入，语料里没有**；**7.10.3 上有没有变，本篇也没有记录**。

## 出处

`sources:` 一篇：
`02_System_reference/02.06_Command_Reference/02.06.02.02.171_PACT__PACT__-__Parallel_ACTivities_control.md`
（TDC `98678.htm`，**3,763 字节 / 157 行**）。**整篇读完**——本页引文全部来自这一篇 ＋ `edges.jsonl` 里带原句的边（下面逐条注明）。

**入边 6 条 / 6 篇**（`inline` + `toc` 口径，`edges.jsonl` 原始行数）：
`02.06.02.02.121_EXSR_-__EXecute_SeaRch`、`02.06.09.02.07_EXSR_-__EXecute_SeaRch`、
`02.06.02.02_List_of_commands`、`02.06.03.01.01_Introduction`、
`02.06.03_Pin_configuration_setup_commands`、`02_System_reference/index.md`。
**`EXSR` 那两篇是同一条命令的两个投放副本**（两条引用句逐字相同）。

**实质入边只有两处，都值得记**：

- **`EXSR` 那句给了一条本篇没有的事实**，逐字（**`PACT` 与 `command` 粘在一起，那是原文如此**，见下 ⚠️ ⑧）：
  `The active sites are those that were activated by the last execution of the PACTcommand. By default, only the first site is active.`
  —— **「默认只有第一个 site 是 active」**（**本页没读 `EXSR`**，只引 `edges.jsonl` 里那条带原句的边）。
- **两个章首页的 `Commands for multi-site setups:` 串**（`Introduction` 与 `Pin_configuration_setup_commands`，同一句）：
  `PACT` / `PALS` / `PQFC` / `PSFC` / `STME` 五条并列在同一行（引文见「和谁有关」）。

**本页没做的**：

- **`PALS` / `PQFC` / `PSFC` / `STME` / `EXSR` / `Site Control window` / `Controlling Multiple Sites` 一篇都没读** ——
  所以「`PACT` 在多 site 流程里排第几步」本页没有；`tpi` 那个 call 怎么写**本篇也没写**。
- **`MCDIgnore` 那一段（`Service Guide Part 1`）没读** —— 而且它在 md 里连链接都没有（见下 ⚠️ ⑥）。
- **图：本篇没有内嵌图片**——判据可核：本篇 md 里 `.png` / `![` **0 命中**。
- **编码坏字：本篇 0 处**（`[一-鿿]` 扫过整篇，一个汉字都没有）；
  **整词替换（`DC/DC power units`）本篇 0 命中**。两条都是实测结果，不是没查。
- **`resets` 清到什么程度：语料未写**（原文只有 `resets the results of all sites` 这一句）。
- **`a site is unavailable` 的判据：语料未写。**
- **没有实跑。** 没有发过 `PACT` / `PACT?`，没有验过「reset 所有 site 的结果」在真机上是什么表现。`verified: doc-only`。
- **没有动 `wiki/index.md`。**

> ⚠️ **本篇的语料瑕疵，照实记、一处都没替它改**（§11.2）：
>
> **① `PACT?STR` 与 `PACT? STR` 两种写法。** 语法块逐字是 `PACT?STR`（无空格），例子逐字是 `> PACT? STR`（有空格）。
> **已核上游 `98678.htm`：上游语法块就是 `PACT?STR`，例子就是 `PACT? STR`**——**上游如此，不是 md 转换丢的**。
>
> **② 命令侧的两行语法在 md 里没有代码块，查询侧的有。** 逐字：
> `PACT {control}, {site|ALL}` 与 `PACT {"site_string"}` 是**裸文本**，而 `PACT?` / `PACT?STR` / 两个 `returns` 都有围栏。
> **已核上游：上游那两行用的是 `<p>`，而 `PACT?` 那一组用的是 `<pre class="prettyprint copyable singleline">`**——
> **上游如此**，所以「语法 / 参数」节里那两行没有围栏是**忠实**的，不是抽取漏了。
>
> **③ 两行命令语法之间没有任何分隔标。** `PACT {control}, {site|ALL}` 与 `PACT {"site_string"}` 只隔一个空行；
> 而查询一侧的第二种形态前面用了 `Or:`。**版式两边不对称**——读者容易把两行读成一条命令。
>
> **④ `## Parameters` 表里多一个空列。** 已核上游：`control` 那一格是 `colspan="2"`，
> 而 `ACTIVE` / `MASKED` 两行前面**还各有一个空的 `<p>&nbsp;</p>` 格**——
> 「语法 / 参数」节里 `control` 那几行前面孤立的 ` | ` 就是它。**上游如此。**
>
> **⑤ `## Warnings` 那一句没进「报错条件」节。** 它逐字是 `If a site is unavailable, PACT will issue a warning.`，
> **52 字符**；脚本只收 ≥ 60 字符的 `## Errors` / `## Warnings` 段。**内容本页写进「是什么」了。**
>
> **⑥ `## Related information` 在 md 里掉成了纯文本。** 逐字一行：`MCDIgnore usage and restrictions`
> ——**没有链接**。**已核上游 `98678.htm`：那里是一个被 HTML 注释包住的 `<a>`，而且 href 自己也是坏的**：
> `a href="service<87919.htm"` ——**`service<87919.htm` 少一个引号、多一个 `<`**。
> **上游自己就坏的**，所以 md 里只剩那行文字。
>
> **⑦ 本篇没有 `## Related information` 的链接，`## Application` 也只有一句**：`Site Control window.`
> ——**没有「见某某章首页」那种指路句**（对照 [[pssr]] 的 `Level setup, see Level Setup Commands.`）。
>
> **⑧ `EXSR` 那篇的引文里 `PACT` 与后面的 `command` 粘在一起**：逐字是
> `the last execution of the PACTcommand. By default, only the first site is active.`
> ——**`PACT` 与 `command` 之间没有空格**。**已核上游 `98602.htm`：上游逐字就是 `</a>command.`**——
> **上游如此**（链接后少一个空格），**不是转换丢的**。**本页照原样转录，不替它补空格。**

`verified: doc-only`
