---
type: object
title: DFPC, DFPC? - (DeFine Pin Comment)
layer: L1
stage: pin
tags: [pin, dfpc, pin-comment, comment, pin-configuration, command, query, l1]
related: [pin, dfpn, pin-configuration-tool, digital-pins-editor, command-reference, smartest-6.5.0]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.62_DFPC__DFPC__-__DeFine_Pin_Comment.md
created: 2026-09-24
updated: 2026-09-28
verified: doc-only
---

# DFPC, DFPC? - (DeFine Pin Comment)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **564 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.62_DFPC__DFPC__-__DeFine_Pin_Comment.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### DFPC

```
DFPC {(pin)}, {"comment"}
```

### DFPC?

```
DFPC? {(pinlist)}
```

returns:

```
DFPC {(pin)}, {"comment"}
```

### Parameters

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/131109.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：pin | In the command, this is the pin to which a comment is to be added. In the query reply, it is the pin whose comment is returned.

### Example

```
> DFPC (pin1), "This is a comment to pin1"
> DFPC? (pin1,pin2)
< DFPC (pin1), "This is a comment to pin1"
```

Since no comment has been defined for pin `pin2`, it is ignored in the reply.

<!-- 语法节 end -->

## 是什么

**`DFPC`（DeFine Pin Comment）给 pin 挂一段自由文本注释；`DFPC?` 按 pin 把注释查回来。**
全文只有两句话，一句说写、一句说读：

> 「Thie DFPC command serves to add a comment to a pin definition.」

> 「The DFPC? query returns the comments that are attached to one or more pins.」

**⚠️ 第一句正文第一个词就是错字**：`Thie` 应为 `The`。**它是上游就错的，不是 md 转换弄坏的**——
已核上游 `raw/131109.htm`，那里的 `<p>` 逐字就是 `<p>Thie <span class="keyword">DFPC</span> command serves to add a comment to a definition.</p>`。详见「出处」⚠️ ①。

**前置条件只有一条，而且它在 `## DFPC` 之前**（原文属 `## Predependencies` 一节）：

> 「The pin must have been defined with DFPN.」

**即：pin 得先用 `DFPN` 定义过。**
注意这一节**不落在本页的「语法 / 参数」节里**——脚本按 `Syntax` / `Parameters` / `Example`
这类**段标记**抽（§4），`Predependencies` 不是标记之一，所以这句话是本页正文的引用，不是语法节的引用。

### 一条注释，两格：`pin` 与 `comment`

语法逐字是 `DFPC {(pin)}, {"comment"}`。三格说明全在「语法 / 参数」节那张 `## Parameters` 表里，
**其中 `pin` 这一格是全篇写得最细的地方——它把命令侧与查询侧两个意思并排写在一格里**：

| 参数 | 命令侧（写） | 查询侧（读） |
|---|---|---|
| `pin` | 「In the command, this is the pin to which a comment is to be added.」 | 「In the query reply, it is the pin whose comment is returned.」 |
| `pinlist` | — | 要查注释的 pin 列表；**`@` = 所有配置过的 pin**；**没定义过注释的 pin 被忽略** |
| `comment` | 「The comment to the pin. The maximal length of the comment string is 2048 characters.」 | — |

**`comment` 有一个硬上限：2048 字符，这是本篇唯一的数量约束。**
超过会怎样，**语料未写**——本篇**没有 `## Errors` 段**，也没有 `## Warnings` 段。

### `@` 与「被忽略的 pin」：查询为什么可能短一行

`pinlist` 那一格其实是**两个段落**（raw 里同属一格，中间空一行）：

> 「A query parameter that specifies the pins for which the comments are to be returned.
> You can also specify @ for all configured pins.」
>
> 「Pins for which no comments have been defined are ignored.」

**第二段是查询侧最实用的一句**：它说的是**没有注释的 pin 不补空行**。
所以 `DFPC? (@)` 的返回行数**小于等于**配置过的 pin 数——`@` 不是「每个 pin 都回一行」。
例子正是这条的实例：例子问的是 `(pin1,pin2)`，只回了一行。

**`@` 圈定的范围写的是 `all configured pins`**，与上面那句 `must have been defined with DFPN`
指向同一批 pin（**推断**，依据是两处都在说「已经定义过的那些 pin」；**本篇没有把两者并排说**）。

### 回复模板与命令模板一个字都不差（容易读混）

「语法 / 参数」节里 `## DFPC?` 底下的 `returns:` 那一行是 `DFPC {(pin)}, {"comment"}`——
**它和 `## DFPC` 的命令模板完全相同。**
**这是原文的写法，不是脚本抄重了**（已核上游，上游两处也都是这个串）。
读的时候只能靠紧邻的 `returns:` 那一行分辨哪一行是命令、哪一行是回复。

## 典型用法

**本篇没有 `## Procedure` / `## Before you begin` / `## What to do next`。**
能算「用法」的只有 `## Predependencies`、`## Parameters`、`## Example` 三处。

**顺序是三段，前一段是后一段的前提**：

| 步 | 做什么 | 依据 |
|---|---|---|
| ① | **用 `DFPN` 定义 pin** | `The pin must have been defined with DFPN.` |
| ② | `DFPC (pin), "comment"` 挂注释 | `## DFPC` 语法 + Example 第一行 |
| ③ | `DFPC? (pinlist)` 查回来 | `## DFPC?` 语法 + Example 第二、三行 |

**原文的完整例子，逐字**：

```
> DFPC (pin1), "This is a comment to pin1"
> DFPC? (pin1,pin2)
< DFPC (pin1), "This is a comment to pin1"
```

> 「Since no comment has been defined for pin pin2, it is ignored in the reply.」

（原句里 `pin2` 带反引号，本页按 §11.1 ③ 去掉。）

**三条能从这个例子里读出来的事**：

| 观察 | 依据 |
|---|---|
| **写不回显** —— `>` 那两行是输入，`<` 只有一行 | 例子第一行那条 `DFPC` 命令**没有对应的 `<` 行** |
| **查可以一次问多个 pin** —— `(pin1,pin2)` | Example 第二行 |
| **问两个、回一个** —— `pin2` 被丢掉 | 上面那句说明，逐字 |

**一次只挂一个 pin。** 命令语法的参数是 `{(pin)}`，`pin` 那格的措辞也是单数
（`the pin to which a comment is to be added`），例子同样只给了单 pin 的写法。
**「一条命令能不能一次给多个 pin 挂同一个 `comment`」——语料未写，本页不替它编。**

**注释是自由文本。** 除了 2048 字符这个长度上限，本篇**没有**任何关于内容格式的规定
（没有编码、没有换行、没有转义、没有「不允许哪些字符」）——**这些都是语料未写，不是本页省略。**

## 和谁有关

- [[pin]] — `stage: pin` 的落点。[[pin]] 那一页已把本页列进 pin 配置命令族（一句话：「给 pin 挂注释」）。
- [[dfpn]] — **前置，也是本篇唯一点名的另一条命令**（逐字：`The pin must have been defined with DFPN.`）。
  **本页没有读 `DFPN` 的原文**，所以「`DFPN` 怎么把 pin 定义出来」本页一个字没有；
  而且**那处 `DFPN` 在 raw 里是裸文本、不是链接**（出边 0 条），所以它连「该去看哪一篇」都没指。
- **`Pin configuration GUI`** — 原文 `## Application` 整节只有这一句：`Pin configuration GUI.`
  **注释挂上去之后在 GUI 上哪里看，本篇没说。** wiki 里 pin 配置的 GUI 侧是
  [[pin-configuration-tool]] 一族（**本页没读**）。
- [[digital-pins-editor]] — **推断**：pin 的注释很可能落在数字 pin 表格的 `Comment` 列。
  依据是 `stages/pin.md` 那张表列了 `Name` / `No` / `Type` / `Mode` / `Scaling` / `HW` /
  `Connection Set` / **`Comment`** / `Tester Channel` 这几个列名，其中有一列就叫 `Comment`；
  **那句不是本篇的话**，本篇只说 `Pin configuration GUI.`。**本页没读 [[digital-pins-editor]] 的原文。**
- [[command-reference]] — **归属**：本篇在 `02.06_Command_Reference` 下。
- [[smartest-6.5.0]] — **版本落点**，见下。
- **入边只有两条**（`02.06.02.02_List_of_commands` 与 `02_System_reference/index.md`），
  **两条都是整篇引用、一条锚点都没有**（见「出处」）——所以本页没有「被谁当作入口」这种材料可写。

## 版本

`## Functional changes` 段有，**只有一条**，逐字：

```
- Introduced in SmarTest 6.5.0
```

**这一条不是哨兵值**：措辞是 `Introduced in`（**不是 `before`**），所以按字面读就是「**6.5.0 引入**」。
—— **与 §11.2 ② 那种 `Introduced before SmarTest 6.3.2` 的写法不是一回事**
（对照同批的 [[dprt]] / [[hwty]] / [[pfnd]] 三页：它们拿到的都是哨兵值，只有本页拿到的是真版本号）。

## 出处

`sources:` 一篇：
`02_System_reference/02.06_Command_Reference/02.06.02.02.62_DFPC__DFPC__-__DeFine_Pin_Comment.md`
（TDC `131109.htm`，**1,298 字节 / 82 行**）。**整篇读完**——本页引文全部来自这一篇；
另**核对过上游 `raw/131109.htm`**（下面 ⚠️ 三条都注明了核对结论）。

**入边 2 条 / 2 篇**（`inline` + `toc` 口径，`edges.jsonl` 原始行数）：
`02.06.02.02_List_of_commands`（line 71）、`02_System_reference/index.md`（line 2651）。
**两条都是整篇引用，`anchor` 字段全为 `null`。出边 0 条**——
本篇正文里**一个语料内部链接都没有**（`DFPN` 那处是裸文本，不是链接）。

**本页没做的**：

- **`DFPN` 没读** —— 而本篇唯一的前置条件就挂在它身上。**「pin 怎么定义」本页一个字没有。**
- **`Pin configuration GUI` 那篇没读** —— 注释在 GUI 上在哪一列、长什么样，本页没有。
- **[[digital-pins-editor]] 没读** —— 「`Comment` 列」那条是推断，依据写在「和谁有关」里。
- **图：本篇没有内嵌图片** —— 判据可核：本篇 md 里 `.png` / `![` **0 命中**。
- **编码坏字：本篇 0 处**（`[一-鿿]` 扫过整篇，**一个汉字都没有**）；
  **整词替换（`DC/DC power units`）0 命中**；**省略号（U+2026 与三个 ASCII 点）0 命中**。三条都是实测结果，不是没查。
- **没有实跑。** 没有在机台上发过 `DFPC` / `DFPC?`，没有挂过注释、没有试过 2048 字符上限。
  `verified: doc-only`。
- **没有动 `wiki/index.md`**，也没有把本页挂进 [[pin]]。

> ⚠️ **本篇的语料瑕疵，照实记、一处都没替它改**（§11.2）：
>
> **① 上游正文第一个词就是错字。** 逐字：
> `Thie DFPC command serves to add a comment to a pin definition.`
> —— **`Thie` 应为 `The`**。**已核上游 `raw/131109.htm`**：上游那个 `<p>` 逐字是
> `<p>Thie <span class="keyword">DFPC</span> command serves to add a comment to a definition.</p>`
> （原 HTML 里这一句中间夹着一个换行 + 两个制表符，本页按 §11.1 ① 折叠成一个空格；
> 连页面 `<meta name="description">` 里也都是 `Thie`）。**上游就坏的（§11.2 ⑥ 那一类），不是转换丢的**，
> 所以**救不回来**。本页正文照原样引，不替它改。
>
> **② `## Predependencies` 这个段名。** 逐字：
> `## Predependencies`
> —— 按普通英语判断它应是 `Prerequisites`。**已核上游：上游的 `<h2>` 就是 `Predependencies`。**
> 而且**它不是本篇一次的笔误**：实测在 `02.06_Command_Reference` 下**有 43 篇**写着这个段名
> （`grep -rl "Predependencies" .` 数出 43 个文件）。**这是这套文档自己的惯用段名**，照原样记、不替它改。
>
> **③ `returns:` 底下的模板与命令模板完全相同。** 逐字两处都是 `DFPC {(pin)}, {"comment"}`
> —— **同一个串既是命令语法又是回复模板**。**已核上游：上游两处也都是这么写的**，不是转换抄重。
>
> **④ `## Parameters` 表在 raw 里被压平，而且没有表头。** 三格（`pin` / `pinlist` / `comment`）
> 各散成「一格一行 + 游离 `|`」，说明文字一个字没丢；**表头（`Parameter` / `Description` 之类）本篇没有**——
> 已核上游：那张表的 `<caption></caption>` 是**空**的。另外 **`pinlist` 那一格里含空行**
> （两个段落同属一格），压平后看上去像「表断成了两截」，**其实是一个格子**。
>
> **⑤ `## Predependencies` 不在本页的「语法 / 参数」节里。** 脚本按段标记抽（§4），
> 那一节收的是 `## DFPC` + `## DFPC?` + `Parameters` + `Example`。
> **这不是抽取漏了，是它本来就不该进语法节**——本页已把这句话写进「是什么」。

`verified: doc-only`
