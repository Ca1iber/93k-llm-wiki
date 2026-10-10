---
type: object
title: DSUS, DSUS? - (Dps Sets USed)
layer: L1
stage: level
tags: [dsus, l1, firmware-command, level, dps, dps-sets, resource-limits, level-setup]
related: [level, dscp, conf, pslv, lsus, drlv, rclv]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.91_DSUS__DSUS__-__Dps_Sets_USed.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# DSUS, DSUS? - (Dps Sets USed)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **422 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.91_DSUS__DSUS__-__Dps_Sets_USed.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### DSUS

```
DSUS {ds_No}
```

### DSUS?

```
DSUS?
```

returns:

```
DSUS {ds_No}
```

### Parameters

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98580.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：ds_No | DPS Set Number. This is the highest number currently allocated to a DPS set, or the highest number of set you want to load. The number you type must not…

### Example

```
DSUS 2
```

This example defines a maximum of 2 DPS sets.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.91_DSUS__DSUS__-__Dps_Sets_USed.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

-  The ds_No is greater than the range allowed by the `DSCP`（raw: `02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.md`） command.
-  The ds_No is smaller than one.

<!-- 报错节 end -->

## 是什么

**`DSUS` 管的是「DPS set 有几个」，不是「某个 set 里是什么」。**

> 「The DSUS (Dps Sets USed) command sets the number of defined DPS sets to the given value. The new value has to be an integer in the range of 1 to the Maximum allowed DPS sets as set by CONF, CONF? - (CONFiguration) (default is 32, maximum is 256).」

**`DSUS` 写、`DSUS?` 读。** 但 `DSUS` 的写还带一个副作用，原文单独给了一段：

> 「You can use the DSUS command to delete sets. If the level setup file that you want to load to hardware contains more DPS sets than you require, you can use the DSUS command to delete all the sets above the number you specify.」

**即 `DSUS n` 同时是两件事**：① 把 DPS set 的**上限**设成 `n`；
② **把 `n` 以上的 set 全部删掉**。
**文档给的场景很具体**：要 load 进来的 level setup 文件里 DPS set 比你要的多，
**用 `DSUS` 把多余的那批裁掉**——它不是「先删再 load」，而是「用一个数把上面全砍掉」。

> 「The DSUS? query returns the number of DPS sets currently defined.」

**`DSUS?` 不带参数**，回答是 `DSUS {ds_No}`。

### `ds_No` 是双向的：既是你想 load 到几号，也是当前的最高号

> 「DPS Set Number. This is the highest number currently allocated to a DPS set, or the highest number of set you want to load.」

| 什么时候看它 | 它是什么（原文） |
|---|---|
| **写入时** | 你**想 load 到几号** |
| **读出 / 内部状态** | **当前已经分配出去的最高编号** |
| **新建一个 DPS set 时** | `This number is automatically updated to include any new DPS set as it is created.`——**自动跟着变大** |
| **上电时** | `At power-on only one DPS set (containing the default values) is available.`——**只有 1 个，内容是默认值** |

**最后一行是这一页最该记住的一条**：**上电时不是「有 32 个空的」，而是「只有 1 个」。**
所以程序里用到 `DSUS` 之前，**DPS set 的个数是 1 而不是上限**。

### ⚠️ 上限是谁定的：**本篇自己说了两种答案**

**这是本页最需要读者自己留神的一处**——正文、参数表、Errors 三处的归属不一致：

| 位置 | 原文逐字 | 它说上限归谁 |
|---|---|---|
| **正文第一段** | `as set by CONF, CONF? - (CONFiguration) (default is 32, maximum is 256)` | **`CONF`** |
| **`## Parameters`** | `must not exceed the maximum number of DPS sets allowed (defined by the DSCP command)` | **`DSCP`** |
| **`## Errors`** | `The ds_No is greater than the range allowed by the DSCP command.` | **`DSCP`** |

**三处里两处指 [[dscp]]、一处指 [[conf]]。**
**本页把三处并列，不替它选一个**（⚠️①）。
**另外注意**：「**默认 32、上限 256**」这两个数**只出现在正文第一段那一句里**，
参数表与 Errors 都只有「不许超过上限」而没有数。

## 典型用法

**1. 唯一一个例子**（原文 `## Example`）：

```
DSUS 2
```

> 「This example defines a maximum of 2 DPS sets.」

**2. 典型场景：load 之前先裁。** 用法就是原文那段：
level setup 文件里的 DPS set 多于你要的 → **用 `DSUS n` 把 `n` 以上的删掉** → 再 load。
**注意顺序**：`DSUS` 是**先于 load** 的动作，不是事后收拾。

**3. 读回**：`DSUS?`（**不收参数**），返回 `DSUS {ds_No}`。

**4. 两条 Errors** 在下面的「报错条件」节：`ds_No` 大于允许范围、或小于 1。
**本篇没有 `## Warnings` 段。**

**5. 归属**：原文 `## Application` 一节全文只有一句——
`Level Setup, see Level Setup Commands.`
（`Level Setup Commands` 那篇本页没读。）

**6. 与 [[pslv]] 的分工**（**推断**，依据见「和谁有关」）：
**`DSUS` 定「有几个」，`PSLV` 定「某一个里是什么」。**
**先有编号才谈得上填内容**——所以在这个意义上 `DSUS` 在前。

## 和谁有关

- [[level]] — **`stage: level` 是「最近的一段」，不是归属**（§6）。
  依据是 `## Application` 那唯一一句 `Level Setup, see Level Setup Commands.`
- [[dscp]] — **正文的参数说明与 `## Errors` 都指它**。
  最实际的一条：**`DSUS` 的上限被记在 `DSCP` 名下**（而正文第一段又说 `CONF`）。
- [[conf]] — **正文第一段指它**，还顺带给出「默认 32、最大 256」这两个数。
  **同一个上限的另一个说法，本页两处并列。**
- [[pslv]] — **分工**：`DSUS` 定 DPS set 的**个数**，`PSLV` 定**某一个 set 里是什么**。
  **（推断）依据**：两篇的 `## Application` 都指向同一章首页 `Level Setup Commands`，
  且两者作用在同一个对象（DPS set）上；**`DSUS` 本文档没有提 `PSLV`。**
- [[drlv]] / [[rclv]] — **同章同族**（level setup 下的 L1 命令）。
  **（推断）依据**：三篇的 `## Application` 是同一句；**`DSUS` 本文档没有提这两条命令。**
- [[lsus]] — **最接近的姐妹页：一个数 level set、一个数 DPS set。**
  **（推断）依据**：两篇的骨架是同一套模板（`{x_No}` + `x?` + 「上限由某命令定」+
  「`At power-on only one … (containing the default values) is available.`」+ 两条 Errors）；
  **`DSUS` 本文档没有提 `LSUS`。**
- `Level Setup Commands`（**未建、不在 allowlist 里**）—— 章首页，`## Application` 指它。

## 版本

本文档**有** `## Functional changes` 段，**只有一条**：

- **`Introduced before SmarTest 6.3.2`**

**这一条是 §11.2 ② 的哨兵**——它的意思是「**早于本文档集覆盖范围**」，
**不是「6.3.2 新增」**。**所以 `DSUS` 成立于哪个版本，这份语料里没有。**

**版本段里只有这一条**，因此 **6.3.2 之后到 7.10.3 之间它有没有改过，本篇没有任何依据**。
「默认 32、上限 256」这两个数**也没有配任何版本条目**——
**它们是不是 6.3.2 之前就有的值，语料里没有。**

## 出处

`sources:` 一篇：
`02_System_reference/02.06_Command_Reference/02.06.02.02.91_DSUS__DSUS__-__Dps_Sets_USed.md`

**本页没做的：**

- **`CONF` 与 `DSCP` 都没读** —— **这是本页最大的空缺**：
  「上限到底归谁定、值是多少」本篇给了两个归属和一组数，
  **本页只能把三处并列，判不了哪个对、也给不出除「默认 32、上限 256」之外的任何信息。**
- **`Level Setup Commands`（`02.06.05`）章首页没读** —— `## Application` 指向的内容面本页没有。
- **`PSLV` 没读** —— 所以「`DSUS` 定了个数之后，`PSLV` 怎么填某个 set」本页只有推断。
- **`LSUS` 没读** —— 所以「level set 侧的姐妹命令」长什么样、共性到什么程度，
  本页只有从骨架模板得来的推断（见「和谁有关」），**没有实质内容**。
- **`DFPS` 没读** —— 所以 DPS set 里的「默认值」具体是什么、pin 是怎么绑上去的，本页没有。
- **没有图。** 原文没有图片。
- **没在真实机台上跑过 `DSUS`**（`verified: doc-only`）——
  §11：**文档里有 ≠ 这台机器上能用**。尤其「`DSUS n` 会删掉 `n` 以上的 set」这条副作用，
  **本页没有在真机上验证过它删的是哪些 set**。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> **① 上限归谁定，本篇给了两个答案。** 逐字三条并列：
> `as set by CONF, CONF? - (CONFiguration) (default is 32, maximum is 256)`
> / `must not exceed the maximum number of DPS sets allowed (defined by the DSCP command)`
> / `The ds_No is greater than the range allowed by the DSCP command.`
> ——**第一处说 `CONF`，后两处说 `DSCP`。本页并列，不替它选一个。**
>
> **② 一句话里少一个复数 `s`。** 逐字：
> `This is the highest number currently allocated to a DPS set, or the highest number of set you want to load.`
> ——**`number of set` 应为 `number of sets`。**
>
> **③ 同一个参数在两条命令里拼法不同。** 逐字两处：
> `DSUS {ds_No}`（本篇）与 `PSLV {dps_No|dps_set_id}, …`（[[pslv]]）
> ——**前者是 `ds_No`，后者是 `dps_No`**。同一个「DPS set 编号」，两种拼法。
>
> **④ 标题的大小写与同批三篇不同。** 逐字四篇并列：
> `DSUS, DSUS? - (Dps Sets USed)`（**`Dps` 只大写首字母**）
> / `PSLV, PSLV? - (Power Supply LeVeL)`
> / `DRLV, DRLV? - (DRive LeVeL)`
> / `RCLV, RCLV? - (ReCeive LeVeL)`
> ——**后三篇是同一套「首字母 + 关键字大写」的写法，本篇的 `Dps` 不合群。**
>
> **⑤ `## Errors` 两条 bullet 的行首是两个空格。** 逐字：
> ```
> -  The ds_No is greater than the range allowed by the DSCP command.
> -  The ds_No is smaller than one.
> ```
> ——**`- ` 后面是两个空格**（同批 [[pslv]] / [[drlv]] / [[rclv]] 三篇都是一个）。
>
> **⑥ `## Parameters` 那张表的第一个格子是一个孤立的 ` | `。** 逐字：
> ```
>  |
>
> ds_No
> ```
> ——**表头位置只有一个竖线**。**「语法 / 参数」节里那个孤立的 ` | ` 就是它。**
>
> **⑦ 同一个限制在正文里有两个名字。** 逐字：
> `the Maximum allowed DPS sets`（正文）/ `the maximum number of DPS sets allowed`（参数表）
> / `the range allowed by the DSCP command`（Errors）
> ——**一处说「个数」，一处说「范围」。**
>
> **⑧ 本篇没有 `## Warnings` 段，也没有 `## Related information` 段。**
> 两条 Errors 里**没有一条是 warning 性质的**（对照 [[drlv]] / [[rclv]]，那两篇都有 Warnings）；
> 而 [[pslv]] 有 `## Related information`、本篇没有——
> **所以 [[dscp]] 与 [[conf]] 的指向全靠正文内联链接承载，
> 链接一剥（如语法节那种 `文本（raw: 路径）` 改写），这两个名字就消失了。**
>
> **⑨ 文件名里标题的问号变成了 `_`。** 本页 `title` 是
> `DSUS, DSUS? - (Dps Sets USed)`，而语料文件名是
> `02.06.02.02.91_DSUS__DSUS__-__Dps_Sets_USed.md`。
> **这是语料的命名约定（问号进不了文件名），不是错字，但按名字找文件的人搜不到 `DSUS?`。**

`verified: doc-only`
