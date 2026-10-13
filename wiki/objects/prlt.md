---
type: object
title: PRLT? - (request Parallel ResuLTs)
layer: L1
stage: pin
tags: [prlt, l1, firmware-command, results, pass-fail, parallel, multi-site, query-only, site-mask]
related: [results, pin, command-reference, psas, get-functional-result, dps-aux-pin-task, execution-context, smartest-6.3.2, smartest-7.10.3, pslv]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.183_PRLT__-__request_Parallel_ResuLTs.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

> ⚠️ **本页若干处记的是 2026-10-10【之前】的语料形态。**
> 那一轮把语料里的表格一律换成了**指向上游 HTML 的指针**
> （见 `extract/PLAN-表格指针化.md`）。所以下文凡是说「表格被压平 / 被摊平 /
> 一格一行」的地方，指的是**更换之前**的样子 —— 现在语料里那个位置是**一句指针**，
> 真表仍在 `tdc-html/raw/` 的上游 HTML 里。**页码/引文都不受影响。**

# PRLT? - (request Parallel ResuLTs)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **582 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.183_PRLT__-__request_Parallel_ResuLTs.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
PRLT? ["exec_context",] {site}
```

returns:

```
PRLT {site}, {"result"}
```

### Parameters

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98689.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：exec_context | An execution context. For more information on execution contexts see Using execution contexts.
> 表内引用（1 条，供检索）：`Using execution contexts`（raw: `02.06.07.01.08.05.03.02.03_Using_execution_contexts.md`）

### Example

```
PRLT? ALL
```

returns:

```
PRLT ALL, "PF0"
```

In this example, site 1 passed the last test, site 2 failed it, and site 3 was masked during the test.

<!-- 语法节 end -->

## 是什么

**`PRLT?` 是一条只读命令：一次把「上一次执行的测试」在**所有 site** 上的全局 pass/fail 全取回来。**
它的存在理由就是「**不用切 focus**」——原文第一句把机制和动机一起写了：

> 「The PRLT? query returns the global pass/fail results of the last executed test for the specified sites in parallel. You can use this command to find out the global results of all sites (not only the one that has the query focus) in one step.」

| 原文的措辞 | 说的是什么 |
|---|---|
| `the last executed test` | 看的是**上一次执行的测试**，不是累计、不是当前 |
| `in parallel` / `all sites` | **一条命令拿多 site**（`parallel` 指的是这个，不是并行执行） |
| `not only the one that has the query focus` | **绕开 focus 限制**——这正是它存在的理由 |
| `in one step` | **一步**，不用逐 site 轮着查 |

**焦点 site 那一个的结果另有命令管**，原文紧跟着一句：

> 「The global result for the site with the query focus is also given by FTST?.」

**即：`PRLT?` 不是 `FTST?` 的替代品**——`FTST?` 给的是**焦点 site**那一份，
`PRLT?` 给的是**一次要多 site**的那一份。**`PRLT?` 不要求你先把 focus 切到谁身上。**

### 三个参数：`exec_context` / `site` / `result`

| 参数 | 位置 | 原文要点 |
|---|---|---|
| `exec_context` | **可选的**（语法行里写成方括号包起来的那一段） | 原文只给一句：`An execution context.` + 指向 [[execution-context]] 那篇（`For more information on execution contexts see Using execution contexts.`） |
| `site` | **必填** | 一个整数，或 `ALL`（见下） |
| `result` | **回读里才有** | 一串字符，**一个 site 一个字符** |

**`site` 的两个取值**，原文逐字两句（**这两句在 raw 里本来就是「项 / 释义」两格，见「出处」⚠️ ①**）：

> 「A single integer representing the site number.」

> 「Means that all the results of all configured sites are returned.」

**`ALL` 是「所有已配置的 site」**——不是「所有 site」。`configured` 这个词是本页特意点出来的。

### `result` 串：一个 site 一个字符

> 「The result parameter is a string containing one character for every site.」

> 「The nth character stands for site n.」

**两句话定了串的长度和下标**：**第 n 个字符就是第 n 个 site**，串长 = site 数。
例子里回读的 `"PF0"` 是三个字符，所以那是三个 site。

三个可能字符，原文逐字（**同样是「项 / 释义」两格**）：

| 字符 | 原文 | 含义 |
|---|---|---|
| `P` | `P If the last test passed on all pins.` | **上一次测试在这个 site 上全 pin 通过** |
| `F` | `F If the last test failed at any pin.` | **任意一个 pin 失败** |
| `0` | `0 If the site was masked during the last test.` | **这个 site 在上一次测试里被 masked** |

**`0` 不是「失败」也不是「通过」，是「没测」**——这一格最容易读错：
它**不代表结果，代表这个 site 当时被屏蔽了**。

### 一条时序硬约束：读到的结果会被 `CSAS` / `PSAS` 作废

**这是本页最该记住的一条。** 原文用一整段 Note 加一条建议写明：

> 「Pass/fail results that are retrieved by command PRLT are invalidated by commands CSAS and PSAS.」

> 「We recommend therefore using the command PRLT directly after the related functional test and before command CSAS or PSAS are performed.」

**流程上就是：functional test 跑完 → 立刻 `PRLT?` → 之后才轮到 `CSAS` / `PSAS`。**
**顺序反了，`PRLT?` 拿到的结果就不是那份结果了。**
（`CSAS` = Channel Slot Accumulated Status、`PSAS` = Power Supply Accumulated Status —— **这两个全名出自 `CSAS` / `PSAS` 自己的文档，本篇只给缩写**；`PSAS` 有页：[[psas]]。**`CSAS` 没有页、也不在 allowlist 里**。）

**同一条约束在 API 那一侧也成立**，原文第三段逐字：

> 「This behavior applies not only to the commands but also to the related APIs: Function GET_FUNCTIONAL_RESULT() must be performed before any of the DPS_AUX_PIN_TASK.check...() functions is called or the results of GET_FUNCTIONAL_RESULT() are invalid.」

**即：`GET_FUNCTIONAL_RESULT()`（[[get-functional-result]]）与 `DPS_AUX_PIN_TASK.check...()`（[[dps-aux-pin-task]]）之间是同样的先后关系。**
—— **命令侧和 API 侧是同一件事的两个入口**，原文自己说了 `This behavior applies not only to the commands but also to the related APIs`。

> ⚠️ **上面那句引文里的 `...` 是原文自带的**（`check...()` 就是这么写的），**不是本页的省略**（§11.1）。

### 例子

```
PRLT? ALL
```

returns:

```
PRLT ALL, "PF0"
```

> 「In this example, site 1 passed the last test, site 2 failed it, and site 3 was masked during the test.」

**回读的格式是 `PRLT {site}, {"result"}`**：先把你问的那个 `site`（这里是 `ALL`）原样吐回来，
再给结果串。**串里第 1 个字符 `P` 对应 site 1、第 2 个 `F` 对应 site 2、第 3 个 `0` 对应 site 3**
（按上面 `The nth character stands for site n.` 那条规则对回去）。

## 典型用法

**本篇没有 `## Procedure` / `## Before you begin` / `## What to do next`**——
用法全部来自正文那五段散文、`## Parameters` 那张表与 `## Example` 一条。
**现在文档给的其实是一个「什么时候读」的时序，不是一组步骤。**

**1. 位置：functional test 之后，`CSAS` / `PSAS` 之前。**

| 顺序 | 做什么 | 依据 |
|---|---|---|
| ① | 跑 functional test | `directly after the related functional test` |
| ② | **立刻** `PRLT? ALL`（或指定 site） | `We recommend therefore using the command PRLT directly after the related functional test` |
| ③ | 之后才可以做 `CSAS` / `PSAS`（或调 `DPS_AUX_PIN_TASK.check...()`） | `before command CSAS or PSAS are performed` / `must be performed before any of the DPS_AUX_PIN_TASK.check...() functions is called` |

**②和③换个位置，②读到的东西就作废了**（原文那个 `invalidated by`）——
**这是本篇唯一一个「做错了不会报错、只会拿到错数据」的地方。**

**2. 查什么就写什么**：

| 想知道 | 写什么 |
|---|---|
| **所有已配置 site** 的全局结果 | `PRLT? ALL`（例子逐字） |
| **某一个 site** 的全局结果 | `PRLT? {site}`（`site` = 一个整数） |
| 焦点 site 的全局结果 | 也可以用 `FTST?`（原文说它也给这一份，**本篇没读 `FTST?` 的文档**） |
| 用 execution context 读 | `PRLT? ["exec_context",] {site}`（**本篇只有这一句 `An execution context.`；`exec_context` 怎么写、能写什么，本篇没有**） |

**3. 去读之前先想一件事**：`0` 是 **masked**，不是 fail。
**把 `0` 当失败读，会把「没测」报成「坏了」**——本页把这条单独写在「是什么」里，就是因为它是这一页最实用的一个字符。

**4. 归属**：原文 `## Application` 一节全文只有一句——
`Test Results, see Test Result Commands.`
—— 指的那一篇在 wiki 里是 [[results]]（见「和谁有关」）。

## 和谁有关

- [[results]] —— **原文 `## Application` 指定的那一篇**：本篇写的是
  `Test Results, see Test Result Commands.`
  **判据**：wiki 的 [[results]] 页 `sources:` 里第一条就是 `02.06.11_Test_Result_Commands.md`
  （与命令参考章那个路径同名），**所以这里的 `Test Result Commands` 指的就是它**。
  **这一条是本页最实的归属依据——不是从篇名猜的。**
- [[pin]] —— **本页骨架的 `stage: pin`**。**但这条要打个问号**：
  §6 说 `stage` 填的是「**最近的一段**」，而本篇 `## Application` 指向的是**结果**那一段。
  **`stage: pin` 与 `## Application` 是两回事**——本页照骨架留着 `stage: pin`（不许改），
  **同时把这条不一致写在这里，不替它圆**：utility line 这类 pin 侧的对象确实是本章的邻居，
  **但「读上一次测试结果」最近的段更像 [[results]]**。
- [[psas]] —— **会作废本命令结果的两条命令之一**（原文点名 `CSAS` 与 `PSAS`）。
  **`CSAS` 没有页、也不在 allowlist 里**（只能写反引号 `CSAS`）。
- [[get-functional-result]] / [[dps-aux-pin-task]] —— **API 侧的同一件事**：
  原文说命令侧的作废行为`applies not only to the commands but also to the related APIs`，
  并点名这两个（`GET_FUNCTIONAL_RESULT()` 要在 `DPS_AUX_PIN_TASK.check...()` 之前）。
  **本页没读这两篇。**
- [[execution-context]] —— **`exec_context` 那格的出处**：原文说
  `For more information on execution contexts see Using execution contexts.`，
  而 [[execution-context]] 页的 `sources:` 正是那篇
  （`02.06.07.01.08.05.03.02.03_Using_execution_contexts.md`）。**本页没读。**
- [[command-reference]] —— **归属**：本篇在 `02.06_Command_Reference` 下。
- `FTST?`（**未建页、且不在 allowlist 里**）—— **焦点 site 那一份结果的另一条路**；
  **本篇没读它的文档**，所以 `FTST?` 的语法与语义本页一个字没有。
- `CSAS`（**未建页、且不在 allowlist 里**）—— 见上。
- `DPS_AUX_PIN_TASK.check...()` 那一族函数（**具体函数名未建页**）——
  **本页只知道「要在它之前读」，不知道它有哪些函数。**

## 版本

本文档**有** `## Functional changes` 段，**只有一条**：

```
- Introduced before SmarTest 6.3.2
```

**这一条是 §11.2 ② 的哨兵值**：措辞是 `before`，意思是
「**在本文档集覆盖范围开始之前就已经有了**」——**所以 `PRLT?` 到底成立于哪个版本，这份语料里没有。**
**7.10.3 上它有没有变，本篇版本段也没写**（本 wiki 面向 [[smartest-7.10.3]]）。

## 出处

`sources:` 一篇：
`02_System_reference/02.06_Command_Reference/02.06.02.02.183_PRLT__-__request_Parallel_ResuLTs.md`
（TDC `98689.htm`；**md 2,335 字节 / 58 行**，上游 htm 6,683 字节）。**整篇读完。**

**本页没做的**：

- **`Test Result Commands`（命令参考章 `02.06.11`）没读**——原文 `## Application` 指的就是它，
  **它的内容面本页不知道**；本页只知道它在 wiki 里对应 [[results]]（判据见「和谁有关」）。
- **`CSAS` / `PSAS` 都没读**——所以**「它们凭什么会作废 `PRLT` 的结果」本页一个字没有**，
  只有原文那句 `invalidated by`。
- **`FTST?` 没读**——**焦点 site 那一份结果的语法与语义本页没有**。
- **`GET_FUNCTIONAL_RESULT()` / `DPS_AUX_PIN_TASK.check...()` 都没读**——
  API 侧那句话本页只**转述**（并列引原文），**没核过那两个函数的文档**。
- **[[execution-context]] 那篇没读**——`exec_context` 能写什么、怎么写，**本页没有**。
- **图：本篇没有内嵌图片**——判据可核：本篇 md 里 `.png` / `.jpg` / `![` **0 命中**。
  **所以本页没有任何来自图的结论。**
- **编码坏字：本篇 0 处**——`[一-鿿]` 扫过整篇 md，**一个汉字都没有**。
  **这是实测结果，不是没查。**
- **没有实跑。** 没有在机台上发过 `PRLT?`、没有拿它和 `CSAS` / `PSAS` 对过顺序、
  没有验证过 `0` 到底怎么显示。`verified: doc-only` 说的就是这件事（§11：文档里有 ≠ 这台机器上能用）。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**（§11.2）：
>
> **① 两个参数格的内部结构被拍平了，读到的是病句。** 逐字：
>
> ```
> The site parameter is number A single integer representing the site number. ALL Means that all the results of all configured sites are returned.
> ```
>
> ——`number` 与 `A single integer representing the site number.` 之间、
> `ALL` 与 `Means that all the results of all configured sites are returned.` 之间**没有任何标点或分隔**，
> 因为原文里它们是**两项**（`number` / `ALL`），**每项的释义独立成行**。
> 同一格里 `result` 那三个字符也一样，逐字：
>
> ```
> Possible characters are: P If the last test passed on all pins. F If the last test failed at any pin. 0 If the site was masked during the last test.
> ```
>
> ——**三个字符与它们的释义全部连成一句**（`0 If the site was masked` 里的 `0` 就是那个字符）。
> **核过上游 `raw/98689.htm`**：这两处原文是 `<dl>` 里的
> `<dt class="dlterm">number</dt><dd>A single integer representing the site number.</dd>` 这种「项 / 释义」结构，
> **htm 是好的**——**所以这是 md 转换时丢的结构（§11.2 ① 那一族），不是上游就坏的。**
> **说明文字一个字没丢，本页照原样引，只把结构补说在这里。**
>
> **② 上标被拍平：`n` + `<sup>th</sup>` 变成了 `nth`。** 逐字（md 里）：
> `The nth character stands for site n.`；**上游 `raw/98689.htm` 里是**
> `The <span class="keyword">n</span><sup>th</sup> character stands for site <span class="keyword">n</span>.`
> ——**htm 是好的**（同上，转换坏的）。
> 本工程对这一类**立过档**（`extract/findings-corpus-superscript-loss.md`），
> **但那份档记的是「纯数字上标」（`2^48` → `248` 那一批）；本篇这处是字母上标 `th`，
> 不在那一批里，raw 里至今仍作 `nth`。** 本页引文照 md 原样引。
>
> **③ 同一个命令名，标题带 `?`、正文里不带。** 逐字对照：
> 标题（`title:` 与 H1）是 `PRLT? - (request Parallel ResuLTs)`，
> 而 Note 里写的是 `Pass/fail results that are retrieved by command PRLT are invalidated by commands CSAS and PSAS.`
> （**`PRLT`，没有 `?`**）。
> **本页两处各照各的引，不替它统一**（同 [[pslv]] 的 `LeVeL` / `LeVel` 那一处）。
>
> **④ 那一句里的 `PRLT` 链接指向的是本篇自己。** 逐字：
> ```
> Pass/fail results that are retrieved by command [PRLT](<02.06.02.02.183_PRLT__-__request_Parallel_ResuLTs.md>) are invalidated by commands [CSAS](<02.06.02.02.33_CSAS__-__Channel_Slot_Accumulated_Status.md>) and [PSAS](<02.06.02.02.188_PSAS__-__Power_Supply_Accumulated_Status.md>).
> ```
> ——**`PRLT` 那个链接的目标就是本页的来源文件本身**（自链接）。
> **这不是错**，但值得知道：**本篇没有单独的 `PRLT`（非查询）文档**，
> 全文只写查询形态。**本页不据此推断「存在一条非查询的 `PRLT`」。**
>
> **⑤ 本篇没有 `## Errors` 段。** 所以**本页没有「报错条件」节**——
> 按骨架的规矩那是**有材料才写**（§4：`error_block()` 没材料时返回空）。
> **这是事实，不是缺页**：`PRLT?` 的失败情形本篇一个字没写。
>
> **⑥ `DPS_AUX_PIN_TASK.check...()` 里的 `...` 是原文自带**（不是本页省略）。
> 记在这里是给读者和检查器看的：**这一处省略号合法**（§11.1 那条的唯一例外）。

`verified: doc-only`
