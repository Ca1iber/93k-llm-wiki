---
type: object
title: HWTY? - (HardWare TYpe)
layer: L1
stage: pin
tags: [pin, hwty, hardware, test-head, card-cage, dut-interface, query, l1, exa-scale]
related: [pin, command-reference, hardware-view, smartest-7.0.1, smartest-7.10.0]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.141_HWTY__-__HardWare_TYpe.md
created: 2026-09-24
updated: 2026-09-28
verified: doc-only
---

> ⚠️ **本页若干处记的是 2026-10-10【之前】的语料形态。**
> 那一轮把语料里的表格一律换成了**指向上游 HTML 的指针**
> （见 `extract/PLAN-表格指针化.md`）。所以下文凡是说「表格被压平 / 被摊平 /
> 一格一行」的地方，指的是**更换之前**的样子 —— 现在语料里那个位置是**一句指针**，
> 真表仍在 `tdc-html/raw/` 的上游 HTML 里。**页码/引文都不受影响。**

# HWTY? - (HardWare TYpe)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **260 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.141_HWTY__-__HardWare_TYpe.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
HWTY?
```

returns:

```
HWTY {machine}, {testhead}, {dut_if}
```

### Parameters

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98636.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 3 列。
> 首行（上游原文）：machine | Returns PS

### Example

```
> HWTY?
< HWTY VS,TH_4CC,SOC
```

<!-- 语法节 end -->

## 是什么

**`HWTY?`（HardWare TYpe）查「这台机器长什么样」——返回三个硬件标识，不改变任何状态。**
全文只有一句话：

> 「The HWTY? query displays properties of the hardware.」

**它只有查询形态，没有设置侧**（页标题就是 `HWTY?`，不是 `HWTY`）。
返回三段：

```
HWTY {machine}, {testhead}, {dut_if}
```

**本页的实际价值几乎全在 `testhead` 那一段**——它是唯一一段有枚举值可背的。

### `testhead`：五个取值，就是五档卡笼数

原文 `Options are:` 底下**逐条列了五个**，这是本页最有用的一张表：

| 取值 | 原文说明（逐字） | 卡笼数 | 旧名 | EXA Scale 名 |
|---|---|---|---|---|
| `TH_1CC` | `TH_1CC for the A-test head or CX test head (containing one card cage)` | 1 | A-test head | CX |
| `TH_2CC` | `TH_2CC for the compact test head or SX test head (containing two card cages)` | 2 | compact test head | SX |
| `TH_3CC` | `TH_3CC for the LX test head (containing three card cages)` | 3 | — | LX |
| `TH_4CC` | `TH_4CC for the small test head (containing four card cages)` | 4 | small test head | — |
| `TH_8CC` | `TH_8CC for the large test head (containing eight card cages).` | 8 | large test head | — |

**三条读法**：

- **`CC` = card cage**（**推断**，依据是五条括号里统一写 `containing N card cage(s)`；
  **原文没有把 `CC` 这个缩写展开过**）。
- **取值是封闭的五个**（`Options are:` + 五条，没有「例如」这类词）。
  **注意没有 `TH_5CC` / `TH_6CC` / `TH_7CC`** —— **跳号是因为不产这些档，不是本篇漏列**
  （**推断**，依据是 `Options are:` 这措辞；**本篇没有明说「只有这些」**）。
- **前三条各写了两个名字**：`A-test head` 与 `CX`、`compact test head` 与 `SX`、`LX`（只给一个）。
  能与版本段那条 `SmarTest 7.10.0: Support of the V93000 EXA Scale test heads CX, SX, and LX added.`
  对上：**CX/SX/LX 是 EXA Scale 的新名字，A-test head / compact 是旧名字**
  （**推断**，依据是那两条并排在同一个 cell 里 + 7.10.0 那条 Functional change；**本篇没有一句把两套名字的关系讲明**）。

### `machine`：**表格说 `PS`，例子说 `VS`——本篇自相矛盾**

`machine` 那一格全文逐字只有两个词：

> 「Returns PS」

**而 `## Example` 的输出是 `HWTY VS,TH_4CC,SOC`** —— 第一段是 `VS`。

**⚠️ 已核上游 `raw/98636.htm`：两处在 htm 里就是这么写的**——
`Returns <span class="keyword">PS</span>` 与 `< HWTY VS,TH_4CC,SOC`
——**上游就矛盾，不是 md 转换丢字**。**本页不判哪个对**：本篇没有第三处证据
（既没有第三处提到 `machine` 的取值，也没有 `## Errors` 段）。详见「出处」⚠️ ①。

### `dut_if`：只有一个取值，而且解释等于没解释

`dut_if` 那一格里，参数说明是：

> 「Specifies the DUT interface type」

**然后紧接着另起一格，取值 `SOC`，说明也写 `SOC`** —— 逐字两格都是 `SOC`。
**所以「`dut_if` 能取哪些值、`SOC` 是什么意思」= 语料未写。**
本篇**只出现 `SOC` 这一个取值**，而它是例子里的、也是表格里的（两处都是 `SOC`）。

### 例子：把三段串起来读

`## Example` 逐字：

```
> HWTY?
< HWTY VS,TH_4CC,SOC
```

按参数表的顺序对号入座：**`machine` = `VS`**（表格说 `PS`，见上）、
**`testhead` = `TH_4CC`**（四个卡笼）、**`dut_if` = `SOC`**。

**这个例子是全篇唯一一处「怎么读返回串」的示范**，而它恰好落在那个矛盾上。

## 典型用法

**本篇没有 `## Procedure` / `## Before you begin` / `## What to do next`，
也没有 `## Application`、没有 `## Errors` / `## Warnings`。**
用法只有一条：**发 `HWTY?`，按参数表的顺序读三段返回。**

**读返回串的三步**：

| 段 | 看什么 | 去哪查 |
|---|---|---|
| 1 `machine` | 机器类型 | **本页给不了** —— 参数表说 `Returns PS`，例子却是 `VS` |
| 2 `testhead` | **卡笼数** | 上面那张五行表（本篇最实用的一处） |
| 3 `dut_if` | DUT 接口类型 | **只知道有 `SOC` 这一个值** |

**什么时候用：本篇一个字没写。**
（**建议**，不是文档要求：它只读不改、返回的是「我连的是哪台机、哪个 test head」，
所以适合作**日志/记录**里的一行；`testhead` 那一段还可以用来对「这台机的卡笼够不够插我要的卡」。
**本条是建议，依据只有「它没有副作用」这一点，文档没有给出任何使用场景。**）

**⚠️ 一条容易踩的**：拿例子里的 `VS` 去参数表里对，**对不上**——表里只有 `PS`。
**所以「`machine` 字段怎么解读」这件事，本篇答不了。**

**没有实跑过**（见「出处」）：**「你这台机器实际返回什么」本页不知道**（§11：「文档里有」≠「这台机器上能用」）。

## 和谁有关

- [[pin]] — `stage: pin` 的落点：[[pin]] 那一页把它列进「**辅助查询命令（验证用）**」
  （与 `CHIN?` / `GCTX?` / `PFND?` / `PRLT?` 并列）。**它在那里的用途是「验证」**，
  与本页「只读不改」的性质一致。
- [[command-reference]] — **归属**：本篇在 `02.06_Command_Reference` 下。
- [[hardware-view]] — **推断**：`HWTY?` 报的是硬件形态（机台 / test head / DUT 接口），
  [[hardware-view]] 是硬件侧那个 GUI（[[pin]] 那一页里它被列在硬件章节）。
  **本篇一个字没提过 `Hardware view`**，这条并置的**唯一依据是「两边都在讲硬件」**；
  **本页没读 [[hardware-view]] 的原文。**
- [[smartest-7.0.1]] / [[smartest-7.10.0]] — **版本落点**，见下。
- **卡笼里插的那些卡**（`XPS256`、`DPS128/64`、`PS1600`、`TP360` 这些）——
  **`testhead` 的取值决定的正是「有几个卡笼」**，所以本页与那些卡页在**物理层**上确实相邻；
  但**本篇一个字没提任何一张具体的卡**，`TH_4CC` 也没说明是哪四张。
  **所以本页不做「哪个值配哪些卡」的对应** —— 那属于**语料未写**，不是本页省略。

## 版本

`## Functional changes` 段有，**三条**，逐字：

```
- Introduced before SmarTest 6.3.2
- SmarTest 7.0.1: Discontinuation of single-density systems
- SmarTest 7.10.0: Support of the V93000 EXA Scale test heads CX, SX, and LX added.
```

**第一条是哨兵值**（§11.2 ②）：`before` 说明它在本文档集覆盖范围开始之前就已经有了，
**具体哪个版本引入，语料里没有**。

**第二条：**`Discontinuation of single-density systems`（7.0.1 起不再有 single-density 系统）。
**⚠️ 它和上面那张取值表的对应关系，本篇没写** ——
`TH_1CC`（单卡笼）算不算 `single-density`、`single-density` 与 `density` 在别处怎么定义，
**本篇一个字没有**。**本页不替它接。**

**第三条：**`Support of the V93000 EXA Scale test heads CX, SX, and LX added.`（7.10.0 起支持）。
**这一条是上面「一个取值两个名字」那三行的解释**（`CX`/`SX`/`LX` 就是 7.10.0 加进来的新名字）——
**推断**，依据是「那三行各写了两个名字」＋「这一条点名了同样那三个名字」；
**本篇没有一句把两者连起来说。**

## 出处

`sources:` 一篇：
`02_System_reference/02.06_Command_Reference/02.06.02.02.141_HWTY__-__HardWare_TYpe.md`
（TDC `98636.htm`，**892 字节 / 82 行**）。**整篇读完**——本页引文全部来自这一篇；
另**核对过上游 `raw/98636.htm`**（下面 ⚠️ ①②③ 都注明了核对结论）。

**入边 2 条 / 2 篇，出边 0 条**（`edges.jsonl` 原始行数）：
`02.06.02.02_List_of_commands`（line 150，`inline`）、`02_System_reference/index.md`（line 2109，`toc`）。
**两条都是整篇引用，`anchor` 字段全为 `null`。出边 0 条** —— 本篇正文里**一个语料内部链接都没有**。

**本页没做的**：

- **[[hardware-view]] 没读** —— 所以「`HWTY?` 能不能在 GUI 里点出来、结果显在哪」本页没有。
- **`machine` 的取值表没找到** —— 本篇只给 `PS` 一个词，**`VS` / `PS` 各是什么、还有没有别的，
  语料未写**；本页**没有去别处找**（那会越过 `sources:`）。
- **`dut_if` 的取值表：语料未写**（本篇只出现 `SOC`，且说明也是 `SOC`）。
- **`single-density systems` 的定义：语料未写**（只在版本段出现一次）。
- **卡笼与卡的对应关系：语料未写**（本篇没提任何一张卡）。
- **图：本篇没有内嵌图片** —— 判据可核：本篇 md 里 `.png` / `![` **0 命中**。
- **编码坏字：本篇 0 处**（`[一-鿿]` 扫过整篇，**一个汉字都没有**）；
  **整词替换（`DC/DC power units`）0 命中**；**省略号（U+2026 与三个 ASCII 点）0 命中**。三条都是实测结果，不是没查。
- **没有实跑。** 没有在机台上发过 `HWTY?`，没有拿它对照过任何一台真机的 test head。
  `verified: doc-only`。
- **没有动 `wiki/index.md`**，也没有把本页挂进 [[pin]]。

> ⚠️ **本篇的语料瑕疵，照实记、一处都没替它改**（§11.2）：
>
> **① 参数表说 `PS`，例子返回 `VS` —— 本篇自相矛盾。** 逐字两处：
> `Returns PS` 与 `< HWTY VS,TH_4CC,SOC`。
> **已核上游 `raw/98636.htm`**：上游那一格逐字是
> `Returns <span class="keyword">PS</span>`，
> 而上游那段例子的第二行逐字是 `&lt; HWTY VS,TH_4CC,SOC`
> ——**两处在 htm 里就都在，不是转换丢字**。
> **上游就矛盾的（§11.2 ⑥ 那一类），救不回来**；**本页不判哪个是当前值**。
>
> **② `dut_if` 的取值的说明就是它自己。** 逐字两格：
> `SOC` 与 `SOC` —— **参数值和它的说明完全相同**，等于没有说明。
> **已核上游：那一行的两个 `<td>` 里就是 `SOC` 与 `SOC`**，上游如此。
> 而 `dut_if` 那一格的说明是 `Specifies the DUT interface type` ——
> **所以「DUT 接口类型有哪些」本篇只出现 `SOC` 一个值**。
>
> **③ `## Parameters` 表在 raw 里被压平，而且没有表头。** 逐字看，「一格一行 + 游离 `|`」：
> `machine` / `Returns PS` / `testhead` / `Returns type of the test head. Options are:` / 五个 `TH_*` 行 /
> `dut_if` / `Specifies the DUT interface type` / `SOC` / `SOC`。
> **`testhead` 那五条选项每条各占一个段落**（不是列表、没有编号）；
> **表头本篇 raw 里没有**（已核上游：那张表的 `<caption></caption>` 是空的）。
> **说明文字一个字没丢。**
>
> **④ 五条 `TH_*` 里只有最后一条带句号。** 逐字：
> `TH_4CC for the small test head (containing four card cages)`（**无句号**）
> 与
> `TH_8CC for the large test head (containing eight card cages).`（**有句号**）。
> **已核上游：上游如此。** 同一条列表里标点不一致，**照原样记**。
>
> **⑤ 本篇没有 `## Application` 段。** 同族的 `DFPC` / `PFND` 都有（那两处分别写
> `Pin configuration GUI.` 与 `Pin configuration, see Configuration Setup Commands.`），
> **`HWTY?` 这一篇一个都没有** —— 所以「这条查询在哪个流程里用」本篇没有任何指向。
> **这不是抽取漏了，是 raw 里就没有这一节。**

`verified: doc-only`
