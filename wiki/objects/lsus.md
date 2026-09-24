---
type: object
title: LSUS, LSUS? - (Level Sets USed)
layer: L1
stage: level
tags: [level, level-set, command, l1, level-setup]
related: [level, dscp, conf, term, equation-based-level-setup]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.155_LSUS__LSUS__-__Level_Sets_USed.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# LSUS, LSUS? - (Level Sets USed)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **936 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.155_LSUS__LSUS__-__Level_Sets_USed.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### LSUS

```
LSUS {level_set_no}
```

### LSUS?

```
LSUS? [level_set_no]
```

returns:

```
LSUS {level_set_no}
```

or:

```
LSUS? [equation_set_no]
```

returns:

```
LSUS {level_set_no}
```

### Parameters

|

level_set_no

 |

Level Set Number. This is the highest number currently allocated to a level set or the highest number of set you want to load. The number you type must not exceed the maximum number of level sets allowed (defined by the `DSCP`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md`） command).

This number is automatically updated to include any new level set as it is created. At power-on only one level set (containing the default values) is available.

 |
 |

equation_set_no

 |

The level equation set number for which the number of currently defined level sets is to be determined. Enter an integer in the range 1 to 99. Valid for Equation based testing only.

 |

### Example

```
LSUS 4
```

This example defines a maximum of 4 level sets.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.155_LSUS__LSUS__-__Level_Sets_USed.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

- The level_set_no is greater than the range allowed by the `DSCP`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md`） command.
- The level_set_no is smaller than one.
- The equation_set_no is undefined.

<!-- 报错节 end -->

## 是什么

**`LSUS` 只改一个数：这台机上有几个 level set。** 原文第一句就是全部：

> 「The LSUS (Level Sets USed) command sets the number of defined level sets to the given value.」

**这个「数」是最高编号，不是个数。** 参数节逐字是
`Level Set Number. This is the highest number currently allocated to a level set or the highest number of set you want to load.`
—— 所以 `LSUS 4` 的意思是「**4 号及以下都算**」，不是「我数了数有 4 个」。
**读错这一条，就会把它当成一个只读的统计量。**

### 它同时是删除入口（**本命令最容易读漏的一条**）

> 「You can use the LSUS command to delete sets. If the level setup file that you want to load to hardware contains more level sets than you require, you can use the LSUS command to delete all the sets above the number you specify.」

**机制：编号以上的 set 被删掉。** 名字读起来像「在用多少个」，
实际是「**把上限调到这儿，多的删掉**」——所以往低处设是**丢配置**，不是无损查询。
**被删掉的 set 里的值会不会被清空、能不能恢复，原文一个字没写——语料未写。**

### 上限由谁定：**同一篇文档给了两个不同的命令**

| 出处 | 这一篇怎么写 |
|---|---|
| 正文第一段 | 上限由 `CONF, CONF? - (CONFiguration)` 设定：「as set by CONF, CONF? - (CONFiguration) (the default is 32, the maximum is 256)」 |
| Parameters 节的 `level_set_no` | 「must not exceed the maximum number of level sets allowed (defined by the DSCP command)」 |
| `## Errors` 段 | 上限由 `DSCP` 给 |

**正文说 `CONF`，参数节与报错节说 `DSCP`——两个不同的命令。**
按 §10，**本页两种说法并列、各自附出处，不自行选一个当答案**；
`verified: doc-only`，也没有在任何机台上核对过。

### 两个环境下 `LSUS?` 返回的东西不同

> 「In a non-equation-based environment, the LSUS? query returns the number of level sets currently defined. In an equation-based environment, the LSUS? query returns the number of level sets currently defined in the specified level equation set.」

| 环境 | `LSUS?` 返回 |
|---|---|
| 非 equation-based | **全局**当前已定义的 level set 数 |
| equation-based | **指定的那一个 level equation set 里**已定义的 level set 数 |

**所以 equation-based 工程里，`LSUS?` 的结果取决于你给的是哪个 `equation_set_no`。**
该参数的原文：「Enter an integer in the range 1 to 99. Valid for Equation based testing only.」

### 这个数自己会涨；上电只有一个 set

> 「This number is automatically updated to include any new level set as it is created. At power-on only one level set (containing the default values) is available.」

- **新建 level set 会让这个数自己涨**——不必每次新建之后再补一条 `LSUS`。
- **上电只有一个 set，内容全是默认值。** 原文**没说那一个是几号 set**——
  「level set 0 是 digital pins 在 high-Z 时的专用 set」这句写在 [[term]] 那一篇里，
  **本页的文档一个字没提它，所以本页不把「上电那一个」接到 level set 0 上。**
- **`LSUS` 管的范围从 1 起**：报错条件里有「The level_set_no is smaller than one.」——
  **`0` 不在它管的范围里**（0 号是那个专用 set）。

### 它只碰「数量」，不碰「值」

本页读的这一篇里，`LSUS` 只出现三种语义：**设上限、删多余、查数量**。
**没有任何一处把电平值挂在它名下**；值的命令在哪，`## Application` 把它指向
`Level Setup Commands` 那一章（**该章本页没读**）。
（本页只读了一篇，**所以这是「本页没见到」，不是「它不存在」**。）

## 典型用法

**先把范围说清：这一篇没有 `## Procedure`，也没有 `## Before you begin`。**
唯一的过程性线索是 `## Application` 一行：
`Level Setup, see `Level Setup Commands`（raw: `02.06.05_Level_Setup_Commands.md`）`。
**所以「先干什么再干什么」本页不写**——按 §2.1，流程是 stage 页的事。

**1. 设定上限**（原文唯一的例子）

```
LSUS 4
```

> 「This example defines a maximum of 4 level sets.」

**2. 裁掉多余的 set**（原文给的第二条用法，**不给例子**）

场景的原文是「If the level setup file that you want to load to hardware contains more level sets than you require」——
**「文件里的 set 比你要的多」时**，用 `LSUS` 把上面那些删掉。

| 你想干什么 | 用哪条 | 出处 |
|---|---|---|
| 把上限调到 N（N 以上的删掉） | `LSUS N` | 语法节 + 正文 |
| 查当前已定义几个 | `LSUS?` | 正文（非 equation-based） |
| 查某个 level equation set 里定义了几个 | `LSUS? [equation_set_no]` | 正文（equation-based） |

**3. 顺序：语料未写。**
「先 `LSUS` 再 load 文件」还是「先 load 进来再 `LSUS` 裁掉」，**这一篇一个字都没说**。
（推断）从「delete all the sets above the number you specify」看，
**要裁的对象得先在文件里**，所以「裁」发生在 load 之前或之时更合理；
**但这是推断，不是文档说的。**

**4. 数一下报错边界**：`level_set_no` 超上限、小于 1、`equation_set_no` 未定义，
三种都会报错——**细节照 `## 报错条件` 一节，本页不复述。**

## 和谁有关

**每条都写清是什么关系，以及它是文档事实还是本页的观察。**

| 页 | 是什么关系 | 依据 |
|---|---|---|
| [[dscp]] | **上限的来源之一（文档事实）** | 本页文档的 Parameters 与 Errors 两节各写了一次 |
| [[conf]] | **上限的另一个来源（文档事实，但与 `DSCP` 冲突）** | 本页文档正文第一段 |
| [[term]] | **下游**：`TERM` 往 level set 里写终结模式，而 `TERM` 的 `level_set_no` 上限被写成「同时受 `DSCP` 与**已用的 level set 数（由 `LSUS` 定）**约束」 | [[term]] 那一篇的参数节（**不是本页文档**） |
| [[equation-based-level-setup]] | **改变本命令语义的概念**：equation-based 与非 equation-based 下 `LSUS?` 返回的东西不同 | 本页文档正文第三段 |
| [[lsux]] | **同族命令**（`LSUX, LSUX? - (Level Sets Used eXtended)`） | **只有名字与同章位置**；**本页没读它的定义文档，它多做了什么本页不写** |
| [[setup-level-set-0]] | **相邻但不同的一件事**：level set 0 是 digital pins 在 high-Z 时的专用 set | **依据在 [[term]] 那一篇**（本页文档没提 level set 0），**所以本页只把它记成「相邻」** |
| [[level]] | **本页 `stage: level` 的理由**：它是 level 这一段里「集合数量」那一格 | frontmatter |
| `Level Setup Commands`（raw: `02.06.05_Level_Setup_Commands.md`） | **本章归属**：`## Application` 指向它 | 本页文档；**该章未读、未建页** |

**本页没有引用 `edges.jsonl` 的入边/出边数字**——那要读了边数据才能写，
**本页没读，所以一个条数都不报。**

## 版本

**本文档有 `## Functional changes` 段，里面只有一行**：

- `Introduced before SmarTest 6.3.2`

**这一行是哨兵值，不是「6.3.2 新增了 LSUS」。** 按 §11.2②，
`Introduced before SmarTest 6.3.2` 的意思是「**在本语料覆盖范围开始之前就已经有了**」——
语料里 2,677 条可用性行都写这同一个版本号，照字面读会读出一条假信息。
**所以本页没有版本门槛可报**；哨兵值本身的说明在 [[smartest-6.3.2]]。
（推断）`LSUS` 在 **SmarTest 7.10.3** 上可用——依据是「它早于 6.3.2」这条文档事实，
加上 7.10.3 晚于 6.3.2；**但这是推断，本页没有在任何机台上印证过。**

## 出处

`sources:` 一篇：
`02_System_reference/02.06_Command_Reference/02.06.02.02.155_LSUS__LSUS__-__Level_Sets_USed.md`
（TDC `98641.htm`，2,498 字节，89 行）。**整篇读完。**

**本页没做的**：

- **文档里链到的三篇一篇都没读**：`CONF, CONF? - (CONFiguration)`（`02.06.02.02.31`）、
  `DSCP, DSCP? - (Define System Control Parameter)`（`02.06.02.02.90`）、
  `Level Setup Commands`（`02.06.05`）。
  **所以「`CONF` 与 `DSCP` 到底哪个定 level set 上限」这个问题本页答不了**，
  只能并列两句原文——上面那个 ⚠️ 就是这么来的。
- **图一张没看**（本篇没有图）。
- **没有 `## Procedure` / `## Before you begin` 可读**，所以本页没有任何流程叙述。
- **没有用 `edges.jsonl`**，故本页不报入边/出边条数。
  `[[term]]` 那条关系是从两篇文档自己的文字里读出来的，**不是从边数据来的**。

> ⚠️ **本篇的语料瑕疵，照实记下、一处都没替它改**：
>
> ① **同一篇文档内，level set 上限的归属自相矛盾。** 正文第一段：
> 「The new value has to be an integer in the range of 1 to the Maximum allowed level sets as set by CONF, CONF? - (CONFiguration) (the default is 32, the maximum is 256).」
> 而参数节写「(defined by the DSCP command)」、报错节写「the range allowed by the DSCP command」。
> **`CONF` 与 `DSCP` 是两个不同的命令**，本页不判哪个对（§10）。
> ② **一句语法笔误**：参数节写 `the highest number of set you want to load`——
> **`set` 应为 `sets`**。本页正文引这句时**原样抄，没改**。
> （同族的 [[tsus]] 写的是 `the highest number of timing set you want to associate`，
> **也是单数；两篇的写法还不一样**。）
> ③ **大小写不一致**：正文写 `the Maximum allowed level sets`（`Maximum` 大写），
> 参数节写 `the maximum number of level sets allowed`（小写）。**同一篇文档两处写法不同。**
