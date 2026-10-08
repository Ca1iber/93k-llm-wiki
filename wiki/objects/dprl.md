---
type: object
title: DPRL, DPRL? - (Default PRimary Level sets)
layer: L1
stage: level
tags: [dprl, l1, firmware-command, level, default-primary, level-set, dps-set, screen-select, internal-command, test-flow-editor]
related: [level, dprt, level-setup-tool, level-set-selector, pslv, pssr, dfps, dscp, testflow-tool, command-reference]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.82_DPRL__DPRL__-__Default_PRimary_Level_sets.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# DPRL, DPRL? - (Default PRimary Level sets)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **679 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.82_DPRL__DPRL__-__Default_PRimary_Level_sets.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### DPRL

```
DPRL {level_set}, {dps_set}, [screen_select]
```

### DPRL?

```
DPRL?
```

returns:

```
DPRL {level_set}, {dps_set}, [screen_select]
```

### Parameters

| level_set | Level Set number. | Level Set number. |
|---|---|---|
| dps_set | DPS Set number. | DPS Set number. |
| screen_select | LEV | level |
| screen_select | DPS | DPS |
| screen_select | DOV | DPS overvoltage |
| screen_select | FST | FAST Eqn & Spec Results |

> ⚠️ 转录说明（非原文）：本表在上游 HTML 里含合并格（colspan / rowspan）；
> 跨格文字已按覆盖范围重复写出（**不是原表里有重复的格子**）。真结构见 `tdc-html/raw/98569.htm`。

### Example

```
DPRL?
```

returns:

```
DPRL 1,2,LEV
```

On sending a query, the system reports that the default primary level set is 1 and the default primary DPS set is 2.

<!-- 语法节 end -->

## 是什么

**`DPRL` 干的事只有一件：把 level setup tool 挪到指定的那一组 set 上。** 原文第一句就是全部机制：

> 「The DPRL (Default PRimary Level sets) command is used to place the level setup tool on the specified set.」

**注意它挪的是「工具」，不是「电平」。** 原文 `## Application` 一节全文只有一句，把这条命令的身份写死了：

> 「Internal communication between the Test Flow Editor and level setup.」

**即：这是 Test Flow Editor 与 level setup 之间的内部通信命令**（文档事实）。
所以本页要回答的是「**谁、在什么时候会发它**」，而不是「**你的测试程序该不该发它**」。

**`DPRL` 写、`DPRL?` 读**，两句话各说一半：

> 「The DPRL? query is used to display the appropriate level set information.」

`DPRL?` **不带参数**（见「语法 / 参数」节）——**查询回的是「当前那两个号」加「一个屏幕选择」，不是「你问的那个 set」**。

### 名字里的 `sets` 是复数：**一次管两组编号**

| 参数 | 原文说明 | 花括号还是方括号 |
|---|---|---|
| `level_set` | `Level Set number.` | **必给** |
| `dps_set` | `DPS Set number.` | **必给** |
| `screen_select` | 四个取值（见下） | **可选** |

原文唯一的例子把三者对上了：

> 「On sending a query, the system reports that the default primary level set is 1 and the default primary DPS set is 2.」

它回的逐字是 `DPRL 1,2,LEV`。**照位置对回去**：`1` = `level_set`、`2` = `dps_set`、`LEV` = `screen_select`。

**这两组的「默认 primary」是谁定的，本篇一个字没写**（见「出处」）。

### `screen_select` 四个取值：**选的是「哪一屏」**

| 取值 | 原文第二行 | 本页的读法 |
|---|---|---|
| `LEV` | `level` | level 那一屏 |
| `DPS` | `DPS` | DPS 那一屏 |
| `DOV` | `DPS overvoltage` | DPS overvoltage 那一屏 |
| `FST` | `FAST Eqn & Spec Results` | 「FAST 方程与规格结果」那一屏 |

**原文给的就只有这四行字**：每屏里有什么、`FAST Eqn` 指的是什么，**本篇都没有展开**（见「出处」）。

### ⚠️ 一条反直觉的报错行为：**越界不报错**

原文 `## Errors` 一节全文只有一句，**而且它是否定式**：

> 「No errors are generated if the given sets are out of range.」

**即：给一个超出范围的 set 号，系统不报错。**

**这条和同章的 [[pssr]] 正好相反**——`PSSR` 的 `## Errors` 第一条逐字是 `The DPS set number is out of range`，
那是**会**报错的。**【推断】**两处的 `dps_set` / `dps_No` 指同一样东西：依据是两篇对它的说明都落在「DPS set 编号」上
（`DPS Set number.` 与 `The identification number of the DPS set`）。**本篇没有写这条对比**，所以只当推断。

**实际操作上的后果：别拿报错来验证 set 号写对了。** 原文没有解释为什么这样设计（**语料未写**）。

### 本篇的实质内容只有三句

原文 **1,325 字节 / 115 行**；去掉两段语法、参数表、例子与版本段，正文只剩三句：
第一句（干什么）、`## Application` 一句、`## Errors` 一句。
**所以关于 `DPRL` 的语义，本页能给的到此为止**——其余全是「语料未写」，逐条列在「出处」。

## 典型用法

**原文没有 `## Procedure` / `## Before you begin` / `## What to do next` 段。**

| 要做的 | 发什么 | 依据 |
|---|---|---|
| 把 level setup tool 放到某组 set 上 | `DPRL {level_set}, {dps_set}, [screen_select]` | 原文第一句 + 语法节 |
| 换 `screen_select` 那一屏 | 同上，第三个位写 `LEV` / `DPS` / `DOV` / `FST` | `## Parameters` |
| 查当前的默认编号 | `DPRL?`（**不带参数**） | `## Example` |

**顺序与前提：本篇一个都没写。** 没有 `Before you begin`、没有「必须先有那个 set」之类的句子，
`## Errors` 还说越界不报错——**两条路都是空的**（见「出处」）。

**谁会发它**：按 `## Application`，是 **Test Flow Editor 与 level setup 之间**。
**所以正常路径是 GUI 侧在切换 level setup 的显示时由工具发**——
**这是本页唯一一条能算「用法」的结论**，原文没有写「用户什么时候该手打它」。
（**建议**，不是文档要求：既然它自称内部通信，**手写进 test method 前先问一句「我是不是该用 GUI」**。）

**出错时**：**越界也不报错**（见「是什么」第四节）。

## 和谁有关

- [[level]] — `stage: level` 的落点：`## Application` 明写它挂在 level setup 上。
- [[dprt]] — **同族的「默认 primary」命令**（页标题 `DPRT, DPRT? - (Default PRimary Timing sets)`）。
  **本篇一个字没提过它。** 两条命令的同族关系是**【推断】**，依据是名字同构
  （`Default PRimary Level sets` / `Default PRimary Timing sets`）＋语料编号相邻
  （本篇 `02.06.02.02.82`，[[dprt]] 的 `sources:` 是 `02.06.02.02.83`）。**本页没有读 [[dprt]]。**
- [[level-setup-tool]] — **被「放置」的那个工具**（原文 `place the level setup tool on the specified set`）。
  **本页没读那一页**，所以 `LEV` / `DPS` / `DOV` / `FST` 各对应界面上哪一屏，本页没有。
- [[level-set-selector]] — **同类、不同层**：那一页是**测试方法侧**的 level set 选择（`layer: L2`），
  本页是**固件侧的命令**（`layer: L1`）。**这个判断只看页标题，本页没读那一页。**
- [[pslv]] / [[pssr]] — **同章的同族命令，作用面各不相同**：`DPRL` 选**哪一组在显示**、
  `PSLV` 设**某一组里是什么**、`PSSR` 设**那一组的斜率与建立时间**。
  **`PSLV` 的原文本页没读**；`PSSR` 的原文读了（上面那条报错行为的对比就是从它来的）。
- [[dfps]] / [[dscp]] — **`dps_set` 这个编号的上游**。本篇**没有**像 [[pslv]] / [[pssr]] 那样点出
  「编号由 `DFPS` 定义、上限由 `DSCP` 定」——**那两条是从那两篇的语法节引文里看到的，不是本篇的话**。
  **两篇的原文本页都没读。**
- [[testflow-tool]] — **命令的另一端**：原文写的名字是 `Test Flow Editor`。
  **本页不把两者等同**（**本页没读 [[testflow-tool]]**），只照录原文那个名字。
- [[command-reference]] — **归属**：本篇在 `02.06_Command_Reference` 下。

## 版本

本文档**有** `## Functional changes` 段，**只有一条**，逐字：

```
- Introduced before SmarTest 6.3.2
```

**这一条是 §11.2 ② 的哨兵值**：措辞是 `before` 而不是 `Introduced in`，
意思是「**在本文档集覆盖范围开始之前就已经有了**」。
**所以 `DPRL` 到底成立于哪个版本，这份语料里没有**。
**7.10.3 上它有没有变过，本篇同样没有记录**（版本段就这一条）。

## 出处

`sources:` 一篇：
`02_System_reference/02.06_Command_Reference/02.06.02.02.82_DPRL__DPRL__-__Default_PRimary_Level_sets.md`
（TDC `98569.htm`，**1,566 字节 / 115 行**）。**整篇读完**——本页引文全部来自这一篇 ＋ `edges.jsonl` 里带原句的边。

**入边 2 条 / 2 篇**（`inline` + `toc` 口径，`edges.jsonl` 原始行数）：
`02.06.02.02_List_of_commands` 与 `02_System_reference/index.md`。
**两条都是整篇引用，一条锚点都没有**——**本篇没有任何「某页在某句话里引它」的入边**。

**本页没做的**：

- **`DPRT` 没读** —— 同族的 timing 版长什么样、两条命令是不是一一对应，本页不知道。
- **`Level setup tool` / `LevelSetSelector` / `Testflow Tool` 三页都没读** ——
  所以「放上去之后界面上是什么样」「`FST` 那一屏是什么」本页一个字没有。
- **`DFPS` / `DSCP` / `PSLV` / `PSSR` 的原文都没读** ——
  本页对 `PSSR` 的那处对比与对 `PSLV` 的两处提及，**都只依据 [[pslv]] / [[pssr]] 的语法节引文，不是它们的正文**。
- **两条入边文档一篇没读**：本页提它们，只提 `edges.jsonl` 里那两条边本身。
- **图：本篇没有内嵌图片**——判据可核：本篇 md 里 `.png` / `![` **0 命中**。
- **编码坏字：本篇 0 处**（`[一-鿿]` 扫过整篇，一个汉字都没有）；
  **整词替换（`DC/DC power units`）本篇 0 命中**。两条都是实测结果，不是没查。
- **没有实跑。** 没有在机台上发过 `DPRL` / `DPRL?`，没验过「越界不报错」在这台机器上是不是也这样。
  `verified: doc-only` 说的就是这件事。
- **没有动 `wiki/index.md`。**

> ⚠️ **本篇的语料瑕疵，照实记、一处都没替它改**（§11.2）：
>
> **① `## Errors` 是否定式的，而且它没进本页的「报错条件」节。** 逐字：
> `No errors are generated if the given sets are out of range.`
> ——脚本的报错节只收**字符数 ≥ 60** 的 `## Errors` / `## Warnings` 段，**这一段是 59 字符**，
> 于是被跳过（同一台账的 [[stme]] 那条 49 字符的也是同样下场）。
> **内容本页照实写进了「是什么」**；**这不是本页漏了，是脚本的阈值把它滤掉了。**
>
> **② 模板与例子的空格不一致。** 模板逐字是 `DPRL {level_set}, {dps_set}, [screen_select]`
> （逗号后有空格），例子的回值逐字是 `DPRL 1,2,LEV`（**逗号后没有空格**）。**同一篇里两种写法**
> （同族毛病见 [[pssr]] 的「出处」⚠️ ④）。
>
> **③ `## Parameters` 那张表在上游就是「三列、无表头」。** 已核上游 `98569.htm`：
> 它是 `<table class="frame-bottom">` ＋ 三个 `<col>`、**`<caption>` 是空的**；
> `screen_select` 那一格是**内嵌的两列小表**（`LEV`/`level`、`DPS`/`DPS`、`DOV`/`DPS overvoltage`、`FST`/`FAST Eqn & Spec Results`）。
> **所以「语法 / 参数」节里那些孤立的 ` | ` 与没有表头的样子都是上游的**——**不是 md 转换丢的**。
>
> **④ `## Application` 那一句在上游结尾多一个空格。** 已核上游 `98569.htm`：那一句在上游是
> `Internal communication between the Test Flow Editor and level` ＋ 换行 ＋ `setup.` ＋ **一个空格** ＋ `</p>`。
> ——**`setup.` 与标签之间那个空格 md 里看不出来**（转换时被折叠掉了）。
>
> **⑤ 本篇是 `02.06.02.02` 章里少见的「零站内链接」文档。** 判据可核：
> 本篇 md 里 `](` **0 命中**（唯一的方括号是语法里的 `[screen_select]`），
> **也没有 `## Related information` 段**——对照 [[pssr]] / [[pact]] / [[stme]] 三篇都有。
> **所以它的入边只有「命令清单」与「总索引」两条目录性链接**（见上）。
> 已核上游 `98569.htm`：**全篇 `title=` 属性 0 条**，**上游也没有给出任何额外文字**。

`verified: doc-only`
