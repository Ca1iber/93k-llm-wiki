---
type: object
title: MSDF, MSDF? - (Modulation Set DeFinition)
layer: L1
stage: timing
tags: [timing, jitter, jitter-injection, modulation-set, msdf, l1-command, firmware-command]
related: [mscf, jscf, jrst, timing]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.163_MSDF__MSDF__-__Modulation_Set_DeFinition.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# MSDF, MSDF? - (Modulation Set DeFinition)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **572 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.163_MSDF__MSDF__-__Modulation_Set_DeFinition.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Parameters

| ms_set_name | In the command, this is the name of a new modulation set. In the query, it is a name of an existing modulation set. If you omit this parameter in the query, MSDF? will return the names of all user defined modulation sets. |
|---|---|
| modulation_type | Currently, the only allowed modulation type is TIM (for "timing"). |
| ALL | With this parameter, the query returns all existing modulation sets. |

### Example

```
> MSDF   "ms_set1",TIM
> MSDF   "ms_set2",TIM
> MSDF   "ms_set3",TIM

> MSDF?
< MSDF   "ms_set1",TIM
< MSDF   "ms_set2",TIM
< MSDF   "ms_set3",TIM

```

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.163_MSDF__MSDF__-__Modulation_Set_DeFinition.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if a modulation set with the specified name already exists.

<!-- 报错节 end -->

## 是什么

**MSDF 只干一件事：给一个 modulation set 起名字。** 原文第一句就是它的全部职责：

> 「MSDF creates a modulation set by defining a unique name for it.」

**它不配属性**——属性全在 [[mscf]] 那边。**本篇从头到尾没有提到 `MSCF`**
（**「属性归 MSCF」这条分工的原文在 MSCF 那一篇里，不在本篇**）。
**所以「定义一个 modulation set」在这里等于「占下一个名字」**，
**而这个名字是后面找它的唯一凭据。**

### 硬件里只有 128 个位子，**超了会挤掉最早那一个**

原文第二、三句是本页最要紧的机制，**它是一条会静默替换的规则**：

> 「Up to 128 modulation sets can be stored in the hardware.
> If you exceed this number by selecting a modulation set that is not yet stored in the hardware,
> the new set will replace the set that was downloaded first.」

**读法（推断，依据是这两句的字面）**：
**名字可以定义超过 128 个，但硬件只存 128 个**；
**第 129 个（以及之后任何「硬件里还没有的」）被用到时，会顶掉最早下载进去的那一个**。
**原文用词是 `will replace`（会替换）、不是 `will fail`（会失败）**——
**也就是说这一步不报错。**
**顶掉的到底是「最早下载的」还是「最早定义的」——原文写的是 `downloaded`**，
**本页照它写「下载」，不换成「定义」。**

> ⚠️ **这条替换规则没有对应的报错**：`## Errors` 一节唯一的报错是「名字已经存在」（见下），
> **没有任何一条管「超出 128」**。**两件事合起来读，这就是一个静默的坑。**
> **而「替换」发生在什么时候（定义时还是下载/使用时），本篇没写。**

### `MSDF?` 是查询，而它**名字可以省略**

> 「MSDF? returns the name of the specified or the names of all defined modulation sets.」

参数表把几个位置讲全了，逐字：

| 位置 | 原文 |
|---|---|
| **命令里的 `ms_set_name`** | `In the command, this is the name of a new modulation set.` |
| **查询里的 `ms_set_name`** | `In the query, it is a name of an existing modulation set.` |
| **查询里省略它** | `If you omit this parameter in the query, MSDF? will return the names of all user defined modulation sets.` |
| **`ALL`** | `With this parameter, the query returns all existing modulation sets.` |

**注意最后两行是两条不同的路、措辞也不一样**：
**省略** → `all user defined modulation sets`；**写 `ALL`** → `all existing modulation sets`。
**这是不是同一批 set，本篇没有说**——**见「出处」的 ⚠️ ②**。

### 唯一的参数 `modulation_type`，**目前只有一种取值**

> 「Currently, the only allowed modulation type is TIM (for "timing").」

**`Currently` 说明这是个会长的枚举**——
**但本篇没写它会怎么长、有没有第二种在路上**（**语料未写**）。

### 两段语法（**本页的「语法 / 参数」节里没有它们**）

本篇给的语法块，在原文里的段标题是 `## MDSF` 与 `## MDSF?`（**少了一个 `S`**，见「出处」⚠️ ①）：

```
MSDF {"ms_set_name"} ,{modulation_type}
```

```
MSDF? ["ms_set_name"|ALL]
```

returns:

```
MSDF {"ms_set_name"} ,{modulation_type}
```

**这三块没有出现在本页「语法 / 参数」节里**——
**对比 [[wsus]] / [[mscf]] 那两页：它们的 `## WSUS` / `## MSCF` 两节都进了各自的语法节，
只有本篇没有。**（**推断**：脚本按文档标题里的命令名认段
——`objpack.title_aliases` 取的就是标题头那串名字（`MSDF` / `MSDF?`），
**而 raw 那两节的标题写的是 `MDSF` / `MDSF?`，差一个字母就对不上**。
**依据**：另三节（`## Parameters` / `## Example` / `## Errors`）都进了页面，
**只有标题拼错的那两节没进**。**本页不替语料改，只把内容抄在这里并指明它不在语法节里。**）

**还有一处记号不齐**：**命令那一段用花括号包住占位符，查询那一段用方括号**
——**同一篇文档里两种记号**（见「出处」⚠️ ③）。

## 典型用法

**1. 最小序列**（原文 `## Example` 本身就是完整例子，逐字）：

```
> MSDF   "ms_set1",TIM
> MSDF   "ms_set2",TIM
> MSDF   "ms_set3",TIM

> MSDF?
< MSDF   "ms_set1",TIM
< MSDF   "ms_set2",TIM
< MSDF   "ms_set3",TIM
```

**读这个例子有三个点**：

- **三次定义、三个名字、同一个 `TIM`**——`modulation_type` 目前只有这一个可选值。
- **`MSDF?` 不写参数就返回全部**——这正是参数表那句 `If you omit this parameter in the query`。
- **回复的格式与命令逐字一样**（原文 `returns:` 那段也是这么写的）。

**2. 报错只有一种情形：名字撞了。**
见「报错条件」节：`An error is generated if a modulation set with the specified name already exists.`
**所以 `MSDF` 不是幂等的**——**同一个名字定义两次就报错**。
**要改写一个已经存在的 set，得用别的命令；是哪条，本篇没说**（**语料未写**）。

**3. 删除 / 改名：本篇没有。**
本篇**没有出现**任何 `UNDEFINE` / 删除类的兄弟命令，
**所以「定义错了怎么办」本页答不了**（**语料未写**）。

**4. 定义之后怎么走：本篇一个字没写。**
**配属性、挂到 jitter set 上这两步都不在本篇里**（那是别的命令的事）。
**本页不替它写那两步**——见「和谁有关」，那里只给「往哪走」，不给步骤。

## 和谁有关

- [[mscf]] — **成对的那一条（下游）**。分工是「**MSDF 给名字 / MSCF 给属性**」。
  **本篇没有点名 `MSCF`**——这一点要说清楚。
  判它们成对的依据有三处：
  ① [[mapping-timing]] 的「抖动注入」那一行把 `mscf` / `msdf` 与其他六条并列
  （**本页读到的 wiki 页**）；
  ② **MSCF 那一篇的正文逐字写着** `must have been defined with MSDF`
  （**这句在 MSCF 那一篇里；本页的取材只有 MSDF 这一篇，本页只核到它的存在**）；
  ③ 名字上一个是 `DeFinition`、一个是 `ConFiguration`（**推断**，依据是两条命令的标题全称）。
- [[jscf]] — **再下游**（MSCF 配好的东西由它挂到 pin 上）。**本篇没提它**；
  依据同 ②，**在 MSCF 那一篇里**。
- [[jrst]] — **同章家族的另一条（并列）**。**本篇没提它**；
  同族的依据是 [[timing]] 的 L1 子专题（**本页读到的 wiki 页**）
  与文件层面的同名投放（见「出处」）。
- [[timing]] — **stage 页**。本页 `stage: timing` 的依据是
  `## Application` 那句 `Jitter test`，以及 `modulation_type` 只允许 `TIM (for "timing")`
  ——**`timing` 这个词在本篇里只以这两种形式出现**。
- `TIM` — **模组类型，目前唯一取值的那个**。**本篇没有展开它**（**语料未写**）。

## 版本

**本文档有 `## Functional changes` 段，段里只有一条**：

- **Introduced in SmarTest 7.3.0** — MSDF 是 7.3.0 引进的 → [[smartest-7.3.0]]。

**版本段里没有的东西（照实记，不替它补）**：没有第二条。
**所以「128 这个上限哪一版定的」「`TIM` 之外的类型什么时候会加」本篇查不到。**
**同族其他命令的版本条目也不在本篇里**——**每一篇只管自己那一条命令。**

**一条本页只能照记、不能核的**：本篇正文那句 `Currently, the only allowed modulation type is TIM`
里的 `Currently` **是个时间戳**，**它是对哪一版说的，本篇没写**（**语料未写**）。

## 出处

`sources:` 一篇：

- `02_System_reference/02.06_Command_Reference/02.06.02.02.163_MSDF__MSDF__-__Modulation_Set_DeFinition.md`
  （frontmatter 的 `source_topic` 是 `143675.htm`；**1,619 字节 / 84 行，整篇读完**）
- 本页的「语法 / 参数」节与「报错条件」节是脚本从这一篇抽的（**本页一个字没动**）。

**本页没做的**：

- **「语法 / 参数」节里没有本篇的两段语法块**（`MSDF` 与 `MSDF?`，含 `returns:` 那块）——
  **原因见下面的 ⚠️ ①；本页把这两块抄进正文，是为了不让读者以为「MSDF 没有语法」**。
- **`MSCF` / `JSCF` 的 raw 不在本页的 `sources:` 里**：
  所以「属性怎么配」「怎么挂到 pin 上」本页一个字都没有（**只有那两条「必须」的转述**）。
- **本篇 `## Application` 一节全文只有两个词**：`Jitter test.`
  **它不是步骤、也不是顺序**——**本页不把它当成用法来写**。
- **图 0 张。** 实测 `![` / `<img` / `.png` / `.jpg` / `.gif` / `raw/` 六种写法在本篇
  **全部 0 命中**。**本页没有任何来自图的结论。**
- **没在机台上跑过 `MSDF` / `MSDF?`**（`verified: doc-only`）：
  **「第 129 个 set 真的会顶掉第一个吗」本页只能保证「文档这么写」（§11）。**

### §10 重复投放：本篇有一份同名孪生（本页查过）

| 路径 | `source_topic` | 字节 / 行 | 与**本页这一份**的正文 |
|---|---|---|---|
| `02.06_Command_Reference/02.06.02.02.163_MSDF__MSDF__-__Modulation_Set_DeFinition.md`（**本页的出处**） | `143675.htm` | 1,653 / 84 | — |
| `02.06_Command_Reference/02.06.16.02.08_MSDF__MSDF__-__Modulation_Set_DeFinition.md` | `143675_2.htm` | 1,654 / 84 | **`diff` 报 0 行差异（正文逐行相同）** |

**两份正文逐行相同**，差别只在 frontmatter 的 `source_topic` / `source_html`
（**本页只读了第一份的正文；第二份只核了 frontmatter、字节数与 `diff` 行数**）。
**记这一条的用处**：① 按 §10，本篇没有「两篇说法不同」的问题；
② **第二份落在 jitter 命令章里**，**这是本页判「MSDF 与 JRST / MSCF 同族」的文件层面依据**。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
> **① 原文两个段标题把命令名拼错了：`## MDSF` / `## MDSF?`——少了 `S`。**
> 逐字引（**第 12 行与第 18 行**）：
> ```
> ## MDSF
> ```
> ```
> ## MDSF?
> ```
> **同一篇里命令本身写的是 `MSDF`**（标题、正文、`## Errors`、`## Example` 全是 `MSDF`）
> ——**只有这两个段标题是 `MDSF`**。
> **后果是实打实的**：**这两节里的两段语法块没有进本页的「语法 / 参数」节**
> （对比 [[wsus]] / [[mscf]] 那两页的同名小节都进了）——**原因见「是什么」末节那条推断**。
> **本页不替语料改那两个字**（§10：raw 一个字节不动）；
> **代价写在明处：拿 `MDSF` 去搜 raw 能搜到，拿它去搜别的文档搜不到。**
> **② 同一批 set 被两种口径指称。** 逐字并列：
> `MSDF? will return the names of all user defined modulation sets.`（**省略参数**那条）
> 与 `the query returns all existing modulation sets.`（**`ALL`** 那条）。
> **`user defined`（用户定义的）与 `existing`（已存在的）是不是同一批，本篇没有说**——
> **本页两处并列照记，不替它统一**（**推断**：它们指的是同一批，
> 依据是两条都在回答「怎么取全部」；**但本篇没有一句话支撑这个推断。**）
> **③ 同一篇里两种占位记号。** 命令那段是
> ```
> MSDF {"ms_set_name"} ,{modulation_type}
> ```
> 查询那段是
> ```
> MSDF? ["ms_set_name"|ALL]
> ```
> **一个花括号、一个方括号**（另有一处：**命令那段的 `"ms_set_name"` 后面
> 与逗号之间多了一个空格**——`} ,{`）。**本页照原样抄，不替它统一记号。**
> **④ 坏字：本篇 0 个。** 照 §11.2 ① 那条判据（**英文文档里出现任何汉字，都是坏字**）
> 逐字查过：**本篇一个汉字都没有**——
> **但这是「本页读到的」，不是「本篇没有」**（§13.1：没找到 ≠ 没有）。

`verified: doc-only`
