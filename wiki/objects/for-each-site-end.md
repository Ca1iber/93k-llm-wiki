---
type: object
title: FOR_EACH_SITE_END
layer: L2
stage: testmethod
tags: [testmethod, test-method-api, mapi, multi-site, site-loop, loop-block]
related: [for-each-site-begin, on-first-invocation-begin, on-first-invocation-end, controlling-multiple-sites, testmethod]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.72_FOR_EACH_SITE_END.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# FOR_EACH_SITE_END

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **198 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.72_FOR_EACH_SITE_END.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
FOR_EACH_SITE_END();
```

List of parameters

There are no parameters.

Return value

There is no return value.

### Example

See the examples in `FOR_EACH_SITE_BEGIN`（raw: `02.07.04.01.70_FOR_EACH_SITE_BEGIN.md`）.

<!-- 语法节 end -->

## 是什么

**FOR_EACH_SITE_END 是 L2（test method API）里的一个「块结束」标记，它自己什么都不做。**
它唯一的职责是**闭合 `FOR_EACH_SITE_BEGIN` 开出来的那个「逐 site 循环」块**。原文：

> 「This API declares the end of the each site loop block that is started by FOR_EACH_SITE_BEGIN.」

> 「This API is used together with FOR_EACH_SITE_BEGIN as a pair to declare the each site loop block.」

**「成对」是本页唯一拿到全文的机制**：`BEGIN` 开块、`END` 闭块，
两个标记之间那一段才是「每个 site 各跑一遍」的代码。

**它没有参数、也没有返回值**（语法节已逐字收）。这件事不是巧合，而是一条设计事实：
**「循环几次、循环谁、循环体是什么」全部由 `FOR_EACH_SITE_BEGIN` 那一侧承载**，
`END` 只是一个闭合括号。（**推断**，依据是本文档语法节的
`There are no parameters.` 与 `There is no return value.`，
以及原文把**细节和示例都推给了 `FOR_EACH_SITE_BEGIN`**——见下。）

**定义位置**（原文）：

> 「This API is defined in the header file /opt/hp93000/soc/prod_com/include/MAPI/MapiUtil.h.」

路径里的 `MAPI/` + 头文件名 `MapiUtil.h` 说明它是 **MAPI 层的工具头**，
不是固件命令、也不是独立库。

### 本页拿不到的东西——**原文自己说了在哪**

> 「For details on the each site loop block enclosed by FOR_EACH_SITE_BEGIN and FOR_EACH_SITE_END, see FOR_EACH_SITE_BEGIN.」

> 「See the examples in FOR_EACH_SITE_BEGIN.」

**这两句是本页最要紧的一条信息。** 本 wiki 的使用方式是「查一页就够」，
而**这一页是故意不完整的**：循环体的语义、示例代码、参数，
原文一条都没有放在这里。**读到本页的人必须再翻 [[for-each-site-begin]]。**

### 一页只有四节

这篇 raw（`29350.htm`）全文 40 行，只有 `## Syntax`、`## Example`、
`## Related information`、`## Functional changes` 四节。
**`## Example` 一节的全部内容就是上面那句 `See the examples in FOR_EACH_SITE_BEGIN.`。**
所以本页「是什么」就这么长——**不是我漏了，是文档就这么多**。

## 典型用法

**本页给不出步骤，这是文档事实而不是缺口**：原文没有 `## Procedure`、没有 `## Before you begin`，
`## Example` 一节指向 `FOR_EACH_SITE_BEGIN`。

能确认的只有两条：

| 要点 | 依据（逐字） |
|---|---|
| **它必须和 `FOR_EACH_SITE_BEGIN` 成对出现** | `This API is used together with FOR_EACH_SITE_BEGIN as a pair` |
| **用法示例去 `FOR_EACH_SITE_BEGIN` 看** | `See the examples in FOR_EACH_SITE_BEGIN.` |

**`CURRENT_SITE_NUMBER()` 在本页没有任何用法说明。**
它出现在 `## Related information` 里（见下节），
但本文档**没有一句话**说它和 `FOR_EACH_SITE_END` 怎么配合。
**语料未写（在这篇里）**，本页不替它推。

## 和谁有关

下面这一批，**全部是原文 `## Related information` 一节自己给的 9 个目标**——
一条不是我挑的，也一条不是我从别处搬的。
原文把它们**挤在没有空格的同一行里**（一条 `](<路径>)` 结束后直接接下一个 `[`，见「出处」）；
本页按「关系是什么」拆开写。

| 目标 | 是什么关系 | 写法 |
|---|---|---|
| `FOR_EACH_SITE_BEGIN` | **配对的那一半**：块的开头，循环体语义和示例都在它那儿 | [[for-each-site-begin]] |
| `FOR_EACH_SITE_BEGIN_WITH_QUERY`（raw: `02.07.04.01.71`） | **同族的第三条命令**：带查询地开块 | 不在允许名单，写名字 |
| `CURRENT_SITE_NUMBER()`（raw: `02.07.04.01.20`） | **同族取数 API**：拿当前 site 号 | 不在允许名单 |
| `ON_FIRST_INVOCATION_BEGIN` / `ON_FIRST_INVOCATION_END` | **另一对块标记**：「整个程序只跑一次」那一对 | [[on-first-invocation-begin]] / [[on-first-invocation-end]] |
| `FOR_SEMI_PARALLEL_TEST_BEGIN` / `FOR_SEMI_PARALLEL_TEST_END`（raw: `02.07.04.01.73` / `02.07.04.01.74`） | **第三对块标记**：「半并行」那一对 | 不在允许名单 |
| `Controlling Multiple Sites`（raw: `02.07.03.13`） | **上游**：多 site 的总述 | [[controlling-multiple-sites]] |
| `Site States and Test Method Programs`（raw: `02.07.03.13.06`） | **上游**：site 状态与 test method 程序的关系 | 不在允许名单 |

### 四对块标记之间怎么嵌套，语料未写

上表里 `FOR_EACH_SITE_*` / `ON_FIRST_INVOCATION_*` / `FOR_SEMI_PARALLEL_TEST_*` 是**三对**块标记。
原文**没有一句话**说它们能不能互相嵌套、能不能交叉、谁必须在谁里面。
**语料未写**——本页不猜，也不替它排。

### `layer: L2` / `stage: testmethod` 的含义

§6 说 `stage` 填的是「**读者该去哪一段里找它的用法**」，**不是归属**。
本页是测试方法（L2）里怎么写的问题，所以最近的一段是 [[testmethod]]。

## 版本

本文档 `## Functional changes` 段**只有一条**：

> 「- Introduced before SmarTest 6.3.2」

**这一条是哨兵值，不是「6.3.2 新增了它」**（§11.2 ②）：
`before` 的意思是「**在本文档集覆盖范围开始之前就已经有了**」。
**照字面读会生成一条「6.3.2 新增」的假信息，而且格式齐整。** 本页把这条机制写在明处。

**注意它和 `Introduced in SmarTest X.Y.Z` 是两种写法**：
后者才是「那一版新加的」，前者不是。本页这条是前者。

## 出处

`sources:` **一篇**：
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.72_FOR_EACH_SITE_END.md`
（raw 的 `source_topic` 是 `29350.htm`）。**整篇读完**——全文 **40 行**。

**本页没做的**：

- **`FOR_EACH_SITE_BEGIN` 没读**（`02.07.04.01.70`）。**这是本页最大的一个缺**——
  原文把**循环体语义、示例代码、参数**全部放在那一篇里。
  所以「循环体能写什么、`BEGIN` 有几个参数、逐 site 的写法长什么样」**本页一个字都没有**。
- **`## Related information` 里那 7 个目标一篇没读**：
  `FOR_EACH_SITE_BEGIN_WITH_QUERY`、`CURRENT_SITE_NUMBER()`、
  `ON_FIRST_INVOCATION_BEGIN` / `ON_FIRST_INVOCATION_END`、
  `FOR_SEMI_PARALLEL_TEST_BEGIN` / `FOR_SEMI_PARALLEL_TEST_END`、
  `Controlling Multiple Sites`、`Site States and Test Method Programs`。
  **它们那一列的「是什么关系」是按名字读出来的（推断）**，
  不是从它们自己的文档里读的——这一点必须说清。
- **图：本文档一张图都没有**（正文里 `../../../../raw/` 引用 **0 个**）。
  **所以本页没有任何来自图的结论。** 这是「**本页没用图**」，不是「图够不着」（§11.4）。
- **没有实跑。** 没在机台上写过 `FOR_EACH_SITE_END()`、没有多 site 跑过。
  `verified: doc-only` 指的就是这件事。

**⚠️ 语料瑕疵，照实记**：

- **坏字（§11.2 ①，判据 `[一-鿿]`）：本篇 0 处。** 查过，不是没看。
- **整词替换（§11.2 ⑤，`DC/DC power units`）：0 命中。** **本篇没有这两族毛病。**

另记一处**不是错、但读的时候会绊一下**的排版：
`## Related information` 那 9 条链接之间**一个空格都没有**，全部挤在一行。
原文逐字是这样接的——**下面是完整子串，没有省略**：

`](<02.07.04.01.70_FOR_EACH_SITE_BEGIN.md>)[FOR_EACH_SITE_BEGIN_WITH_QUERY]`

**注意 `]` 和 `[` 之间没有空格**——这是语料的排版如此，**本页照记、没替它加空格**。

**图里的字不进 `>` 引文块（§11.4）**——本篇没有图，这一条在本页为空。

`verified: doc-only`
