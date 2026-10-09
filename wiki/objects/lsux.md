---
type: object
title: LSUX, LSUX? - (Level Sets Used eXtended)
layer: L1
stage: level
tags: [level, level-set, command, l1, system-only, test-flow-optimization, level-setup]
related: [level, lsus, dscp, command-reference, smartest-6.3.2]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.156_LSUX__LSUX__-__Level_Sets_Used_eXtended.md
created: 2026-09-24
updated: 2026-09-28
verified: doc-only
---

# LSUX, LSUX? - (Level Sets Used eXtended)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **880 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.156_LSUX__LSUX__-__Level_Sets_Used_eXtended.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### LSUX

```
LSUX {level_set_no|SWAP|NONE}
```

### LSUX?

```
LSUX?
```

returns:

```
LSUX {level_set_no}
```

### Parameters

| level_set_no | Level Set Number. If the number is smaller than the current value of LSUS then LSUX is set to this value. Otherwise it is set to the current value of LSUS. | Level Set Number. If the number is smaller than the current value of LSUS then LSUX is set to this value. Otherwise it is set to the current value of LSUS. |
|---|---|---|
| level_set_no | SWAP | This command parameter causes the values set by LSUS and LSUX to be switched, that is, LSUS is set to the current value of LSUX, and LSUX to that of LSUS. |
| level_set_no | NONE | This command parameter sets the value of LSUX back to 1. |

> ⚠️ 转录说明（非原文）：本表在上游 HTML 里含合并格（colspan / rowspan）；
> 跨格文字已按覆盖范围重复写出（**不是原表里有重复的格子**）。真结构见 `tdc-html/raw/98642.htm`。

### Example

```
LSUX 4
```

This example defines a maximum of 4 level sets.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.156_LSUX__LSUX__-__Level_Sets_Used_eXtended.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

- The level_set_no is greater than the range allowed by the `DSCP`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md`） command.
- The level_set_no is smaller than one.
- The level_set_no is undefined.

<!-- 报错节 end -->

## 是什么

**`LSUX` 是一条「只给系统用」的命令**——本篇开头唯一一句带感叹号的话就在这儿：

> The LSUX (Level Sets Used eXtended) command is only for use by the system, not the user. Do not attempt to execute it from the hpt utility! You may execute the query.

**三句话拆开读：**

| 原文 | 意思 |
|---|---|
| `only for use by the system, not the user` | **只给系统用**，不是给工程师用的 |
| `Do not attempt to execute it from the hpt utility!` | **不要从 `hpt` 手工执行 `LSUX`** |
| `You may execute the query.` | **但查询（`LSUX?`）可以执行** |

**`hpt` 是什么，本篇没有解释——语料未写。**

**这一篇为什么还要写出来，原文自己也说了：**

> The following information is provided to improve your understanding of any hpt output listings you may make.

**所以本页的定位不是「教你怎么用」，而是「让你看懂 `hpt` 的输出里那两个数是什么」。**

### 它和 `LSUS` 打的是两个不同的数

> During test flow optimization the LSUX command is used internally by the Test Flow Optimizer to generate additional (optimized) level sets. The LSUS? query (see LSUS, LSUS? - (Level Sets USed)) returns the number of all level sets, including those that are optimized. Thus LSUX? is used to return the original number of level sets, that is, those before optimization. The Test Flow Executor then calculates the number of optimized level sets.

**拆成表：**

| 谁 | 数出来的是什么 |
|---|---|
| `LSUS?`（[[lsus]]） | **全部** level set 的数量——**包含被优化出来的那些** |
| `LSUX?`（本页） | **优化之前**的、**原始**的 level set 数量 |
| `Test Flow Executor` | 由它去**算**「优化出来几个」（原文：`then calculates the number of optimized level sets`） |

**（推断，依据是上面三条之间的关系）**：优化出来的数量 = `LSUS?` 的结果 − `LSUX?` 的结果。
**原文只说 Test Flow Executor「计算」这个数，没有给公式**——所以这一步是本页的推断，不是文档事实。

**一条生效条件：**

> The command is not active unless optimized test flows are used.

**`## Application` 一节只有一行**，逐字是 `Optimized testflows.`——**不用 optimized test flow，这条命令就是死的。**

### 三个参数，其中一个的语义是「只降不升」

| 参数 | 原文（逐字） | 读法 |
|---|---|---|
| `level_set_no` | `Level Set Number. If the number is smaller than the current value of LSUS then LSUX is set to this value. Otherwise it is set to the current value of LSUS.` | **`LSUX` 取 `min(你给的数, LSUS 的当前值)`**——**它永远不会超过 `LSUS`** |
| `SWAP` | `This command parameter causes the values set by LSUS and LSUX to be switched, that is, LSUS is set to the current value of LSUX, and LSUX to that of LSUS.` | **把两个数对调** |
| `NONE` | `This command parameter sets the value of LSUX back to 1.` | **把 `LSUX` 拨回 `1`** |

**第一行是本命令与 `LSUS` 最要紧的分别**：[[lsus]] **直接把那个数设成你给的值**，
而 `LSUX` 是**夹紧**——**高的那一头被 `LSUS` 压住**。
**所以 `LSUX N` 与 `LSUS N` 不等价**，哪怕 `N` 一样。

**两处原文没写：**

- **`LSUS` 在这里指「那条命令」还是「那个值」——原文没交代。** 原句是
  `If the number is smaller than the current value of LSUS`。（推断）它指的是**那个值**（当前的 level set 数），
  依据是后半句 `Otherwise it is set to the current value of LSUS` 里的 `value of`；**原文没有点明。**
- **被压掉的那些 level set 会怎样——语料未写。** 原文没有一句讲「多出来的那些去哪了」。

## 典型用法

**先把范围说清：本篇没有 `## Procedure`、没有 `## Before you begin`、没有 `## What to do next`。**
按 §2.1，流程是 stage 页的事。本篇能给的只有**一条纪律**、**三种操作**和**一个生效前提**。

**1. 纪律——这是本命令最重要的一条用法**：

| 形态 | 能不能手工执行 | 原文 |
|---|---|---|
| `LSUX …`（设置） | **不能** | `Do not attempt to execute it from the hpt utility!` |
| `LSUX?`（查询） | **可以** | `You may execute the query.` |

**2. 三种操作**（依据都在上「语法 / 参数」节的参数表里）：

| 目的 | 写法 | 效果 |
|---|---|---|
| 把 `LSUX` 设到一个值 | `LSUX {level_set_no}` | 取 `min(该值, LSUS 当前值)` |
| 把 `LSUS` 与 `LSUX` 对调 | `LSUX SWAP` | 两个值互换 |
| 把 `LSUX` 拨回初始 | `LSUX NONE` | `LSUX = 1` |

**3. 原文唯一的例子**在 `## Example` 段里（脚本已整段收进上「语法 / 参数」节，本页不重复抄），
它的说明句逐字是：

> This example defines a maximum of 4 level sets.

**⚠️ 这一句与参数表对不上**：参数表说 `LSUX` 是**夹紧到 `min(数, LSUS)`**，不是在「define a maximum」；
而且这一句与 [[lsus]] 那篇的例子说明**逐字相同**——见「出处」瑕疵①。

**4. 生效前提：必须是 optimized test flow。**

> The command is not active unless optimized test flows are used.

**5. 顺序：语料未写。** 「什么时候该 `SWAP`」「`NONE` 之后要不要重算」——本篇一个字没说。

## 和谁有关

| 页 | 是什么关系 | 依据 |
|---|---|---|
| [[lsus]] | **同族，也是本命令存在的理由**：`LSUS?` 数「全部（含优化）」，`LSUX?` 数「优化之前」——**两个数之差就是优化出来的量** | 本篇正文（**文档事实**）+ 本页（推断）那一步 |
| [[level]] | **本页 `stage: level` 的理由**：它管的是 level set 的计数 | frontmatter |
| [[dscp]] | **上限的来源**：报错条件写 `The level_set_no is greater than the range allowed by the DSCP command.`——**与 [[lsus]] 的报错措辞一致** | 上「报错条件」一节（**文档事实**） |
| [[command-reference]] | **本篇定义文档所在的章**（`02.06_Command_Reference`）。这一章**不逐篇建页**（§12.1） | §12.1 + 本页 `sources:` 的路径（**项目约定**） |
| [[smartest-6.3.2]] | **版本哨兵值**指向的版本页（见下节） | 本篇 `## Functional changes`（**文档事实**） |
| `Test Flow Optimizer` / `Test Flow Executor` / `hpt`（**三个名字都未建页、也都不在链名清单里**） | **本命令的调用方、算账方、以及被明令不许用来敲 `LSUX` 的那个工具** | 本篇正文（**文档事实**）；**三个名字本篇都没有展开解释**，它们各自是什么本页给不出 |

**入边只有两条，而且都是清单**：`LSUX` 的 2 份投放一共只有 **2 条**入边
（`02.06.02.02_List_of_commands.md` 与 `02_System_reference/index.md` 各 1 条，来源 `extract/edges.jsonl`）。
**所以「谁在正文里讲 `LSUX`」这个问题，语料里没有别的答案**——
这一条与本页「system 专用、用户手册只在 `hpt` 输出那一节提它」的定位是一致的
（**但这属于观察，不算文档事实**）。

## 版本

**本文档有 `## Functional changes` 段，里面只有一行**：

- `Introduced before SmarTest 6.3.2`

**这一行是哨兵值，不是「6.3.2 新增了 LSUX」。** 按 §11.2②，
`Introduced before SmarTest 6.3.2` 的意思是「**在本语料覆盖范围开始之前就已经有了**」——
语料里 2,677 条可用性行都写这同一个版本号，**照字面读会读出一条假信息**。
**所以本页没有版本门槛可报**；哨兵值本身的说明在 [[smartest-6.3.2]]。

**版本段里没有的东西**：**没有一条 `SmarTest X.Y.Z:` 形式的变更记录**。
所以「`SWAP` / `NONE` 是哪个版本进的」「optimized test flow 从哪个版本开始有」**本篇查不到——语料未写**。

（推断）`LSUX` 在 **SmarTest 7.10.3** 上可用——依据是「它早于 6.3.2」这条文档事实，
加上 7.10.3 晚于 6.3.2；**本页没有在任何机台上印证过。**

## 出处

`sources:` 一篇：
`02_System_reference/02.06_Command_Reference/02.06.02.02.156_LSUX__LSUX__-__Level_Sets_Used_eXtended.md`
（TDC `98642.htm`）。**整篇读完。**

### 数是怎么量的（§11.5 的口径）

| 数 | 值 | 怎么量的 |
|---|---|---|
| 字节 | **2,159** | `len(path.read_bytes())`（即 `st_size`）。**不是** `len(read_text())` |
| 行数 | **84** | `wc -l`（**不 +1**；本语料末行都带换行） |
| 换行 | **84 个全 CRLF、裸 LF 0 个** | 所以 `len(read_text())` 会给出 **2,075**（**恰好少 84 = 行数**）——本页不拿 2,075 当字节数 |
| 代码块 | **4** | `docs.jsonl` 的 `code_blocks` |
| 标题 | **8**（1 个 H1 + 7 个 H2） | `docs.jsonl` 的 `heading_count` |
| 出边 | **2** | `docs.jsonl` 的 `out_degree: 2`、`link_kinds: {"doc": 2}`——**指 [[lsus]] 与 [[dscp]] 各一条** |

### 这一篇在语料里有 2 份投放（本页核过）

| 路径（相对 `by-category/` 的尾巴） | `source_topic` | `st_size` |
|---|---|---|
| **`…/02.06_Command_Reference/02.06.02.02.156_LSUX__LSUX__-__Level_Sets_Used_eXtended.md`（本页 source）** | **`98642.htm`** | **2,159** |
| `…/02.06_Command_Reference/02.06.05.02.13_LSUX__LSUX__-__Level_Sets_Used_eXtended.md` | `98642_2.htm` | 2,160 |

**两份剥掉 frontmatter 之后逐字节相同**（body 都是 **1,953** 字节，
`sha256` 前 16 位同为 `9c5c3d263d3de17d`）。判据是 §10 第 0 条：`source_topic`
去掉 `_N` 后缀后相同 → 同一篇 TDC 页。
**本页只把 `02.06.02.02.156` 当来源**，另一份只做了哈希核对，**没有当成证据读**。

### 上游 `.htm` 核过：**逐字比对，内容一个字没丢**

`raw/98642.htm` 与 `98642_2.htm` **都存在，各 5,711 字节**。
把 `.htm` 与 md 都拆成词、取集合差，结果是：
**只出现在 `.htm` 里的只有 `Topic` 与 `98642` 两个词**（页面框架），
**只出现在 md 里的只有链接路径的字面**（`02`、`06`、`155_LSUS__LSUS__`、`__Level_Sets_USed`、
`90_DSCP__DSCP__`、`__Define_System_Control_Parameter`、`md` 这几段）。

**结论：这一篇 md 相对上游 `.htm` 没有内容丢失。** 所以下面两处瑕疵
**上游 `.htm` 里就是那样**——属于 §11.2 ⑥ 说的「**上游就坏的（救不回来）**」，
**不是** ① 那种转换损坏。

### 对外核对（本页唯一一处 `sources:` 之外的材料）

`LSUX` 属于哪一类命令，**本篇的 `## Application` 只写了 `Optimized testflows.`**，答不了。
本页为了给「和谁有关」一个可核的归属，**只 `grep` 了同章一份索引的第 22 行**：

| 打开的是 | 读了什么 | 拿到什么 |
|---|---|---|
| `02_System_reference/02.06_Command_Reference/02.06.05.02_List_of_level_setup_commands.md`（2,823 字节，37 行） | **只 `grep` 了含 `LSUX` 的那一行**（第 22 行） | 一行逐字：`- [LSUX, LSUX? - (Level Sets Used eXtended)](<02.06.05.02.13_LSUX__LSUX__-__Level_Sets_Used_eXtended.md>)` → **`LSUX` 在 level setup commands 的清单里**（同清单第 21 行就是 [[lsus]]） |

**这一份是纯清单**（37 行，整篇就是命令名列表），**本页只取了上面那一条**，
**它的正文内容一个字节都没进本页**。处置与 `wiki/objects/eqsp.md` 的「对外核对」一节同一套。

### 本页没做的

- **没有实跑。** 没在机台上发过 `LSUX` / `LSUX?`，**没有见过任何 `hpt` 输出清单**。
  `verified: doc-only` 指的就是这件事。
- **`hpt` 是什么、怎么用，本页给不出**——本篇没有一句解释它。
- **`Test Flow Optimizer` / `Test Flow Executor` 两者的专页都不存在**，
  **本页也没有读任何讲 test flow optimization 的文档**——所以「优化出来的 level set 长什么样」本页答不了。
- **`LSUS` 那一篇本页没读**（它是本页唯一的「上游」）；本页关于 `LSUS?` 的话全部来自本页这一篇。
- **`DSCP` 那一篇没读**——所以「level set 的上限默认是多少、最大是多少」本页一个数都不报。
- **`02.06.05.02` 这一章的兄弟命令没读**（只 `grep` 了清单里的一行）。
- **图**：本篇对 `raw/` 的引用 **0 处**（`.png` / `.jpg` / `.jpeg` / `.gif` / `![` / `<img` / `raw/`
  七种写法**全部 0 命中**）——**所以本页没有任何来自图的结论，没有图证。**
- **没有动 `wiki/index.md`**，也没有动任何别的页。

### ⚠️ 本篇的两处瑕疵，本页照实记下、一处都没替它改

> **① 例子的说明句与参数表的语义相反，而且与 [[lsus]] 逐字重复。**
> 本篇 `## Example` 段的说明逐字是 `This example defines a maximum of 4 level sets.`；
> 而 [[lsus]] 那一篇的 `## Example` 段说明**逐字也是同一句**。
> **但 `LSUX` 的参数表写的是「夹紧」**：
> `If the number is smaller than the current value of LSUS then LSUX is set to this value.`
> ——**它不是「定义上限」，它是被 `LSUS` 的上限压着。**
> 两句放在一起读是矛盾的（**上游 `raw/98642.htm` 里就是这样**）。
> **本页两边并列，不替它改，也不判哪一句是笔误。**

> **② 同族两条命令的名字展开，大小写不一致。**
> 本篇是 `(Level Sets Used eXtended)`（`Used` 的 `s` 小写）；
> 而 [[lsus]] 那一篇是 `(Level Sets USed)`（`USed` 的 `S` 大写）。
> **两篇在 `List_of_level_setup_commands` 里是紧邻的两行**（第 21、22 行），**写法却不统一**。
> **原文如此**，本页照原样引。

另记一处**不是瑕疵、是留白**：`## Application` 整段只有一个名词短语 `Optimized testflows.`
——**没有动词**。本页按原文照抄，没有替它补成一个句子。

`verified: doc-only`
