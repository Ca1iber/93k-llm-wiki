---
type: object
title: DTCP, DTCP? - (Define Technology Control Parameters)
layer: L1
stage: project
tags: [dtcp, firmware-command, technology-control-parameters, testpoints, extended-dram-factor, activation, project-setup, l1-command]
related: [dscp, technology-file-for-a-device, project, mapping-project, smartest-6.3.2]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.93_DTCP__DTCP__-__Define_Technology_Control_Parameters.md
created: 2026-09-21
updated: 2026-09-21
verified: doc-only
---

# DTCP, DTCP? - (Define Technology Control Parameters)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,073 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.93_DTCP__DTCP__-__Define_Technology_Control_Parameters.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### DTCP

```
DTCP {"key"}, {"value"}
```

### DTCP?

```
DTCP? {"key"}
```

returns:

```
DTCP {"key"}, {"value"}
```

### Parameters

| key  | The string specifies the system control parameter.

Currently, the only supported control parameters are testpoints and extended_dram_factor.

For more information, refer to `testpoints`（raw: `../../01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.01.02_Technology_file_for_a_device.md#_49363__row_testpoints`） and `extended_dram_factor`（raw: `../../01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.01.02_Technology_file_for_a_device.md#_49363__row_extended_dram_factor`） in `Technology file for a device`（raw: `../../01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.01.02_Technology_file_for_a_device.md`）.

 |
 | value   | The value to be set as string. |

### Examples

```
> DTCP? "testpoints"
< DTCP "testpoints", "0"
> DTCP "testpoints", "100"
> DTCP? "testpoints"
< DTCP "testpoints", "100"
> *RST
> DTCP? "testpoints"
< DTCP "testpoints", "100"
```

```
> DTCP "extended_dram_factor","90"
> *RST
> DTCP? "extended_dram_factor"
< DTCP "extended_dram_factor","90"
```

<!-- 语法节 end -->

## 是什么

**`DTCP` 是 `DSCP` 的补充命令。** 原文第一句：

> 「This command serves to control certain system control parameters. It supplements the
> DSCP command. The values that are defined with DTCP must be activated with the *RST command.」

**`supplements` 只说明两命令有关系**——**哪些参数为什么放在 `DTCP` 而不是 `DSCP`，本篇没说。**

### 两个值：selected 与 active

整篇最要紧的是第二段：

> 「The DTCP? query returns the currently selected value of a specified parameter.
> Note that this is not the active value, if a new value has been defined,
> but not yet been activated with *RST.」

**`DTCP` 写下去的值先进入「已选（selected）」，`*RST` 之后才成为「生效（active）」；
而 `DTCP?` 读的是 selected，不是 active。**

**后果：`DTCP?` 不能用来确认激活成功没有**——**本篇没有给任何读 active 值的命令。**

### 目前只支持两个 key

> 「Currently, the only supported control parameters are testpoints and extended_dram_factor.」

**这两个名字的定义不在本篇**：原文用两个**带锚点**的链接把它们指到
`01.01.07.02.01.02_Technology_file_for_a_device.md`，即已建的 [[technology-file-for-a-device]]。

## 典型用法

**① 写：`DTCP {"key"}, {"value"}`。** 两个参数**都是字符串**
（参数表：`The value to be set as string.`）——**所以数字也要带引号**。
例：`DTCP "testpoints", "100"`。

**② 读：`DTCP? {"key"}`**，返回形如 `DTCP {"key"}, {"value"}`。

**③ 写完必须 `*RST`**，否则只改到 selected 那一层。

**④ 原文的例子正好演示了「读的是 selected」这件事**——逐字：

```
> DTCP? "testpoints"
< DTCP "testpoints", "0"
> DTCP "testpoints", "100"
> DTCP? "testpoints"
< DTCP "testpoints", "100"
> *RST
> DTCP? "testpoints"
< DTCP "testpoints", "100"
```

**看第 3 次和第 5 次查询：`*RST` 之前就回 `100`，`*RST` 之后还是 `100`。**
**这不是例子写错了——它是那句 `this is not the active value` 的演示。**
**代价是：这个例子本身看不出 `*RST` 起了什么作用**，
因为能读到的那个值从头到尾没变过。

**⑤ 两个 key 的含义在别篇**：`testpoints` / `extended_dram_factor` 的取值与单位见
[[technology-file-for-a-device]]（**该页本页没读**）。

**⑥ `testpoints` 有一层内存后果**：[[technology-file-for-a-device]] 页记了原文的 `CAUTION`——
testpoints 的内存是在**加载 device 的最开始**、用 `DTCP` 与 `*RST` 预留的，
且**按「所有 testpoints 所需的最大内存」预留，不管后面用不用**。
（**这一条引自那一页；本篇 raw 里没有这段 `CAUTION`。**）

## 和谁有关

- [[dscp]] — **原文 `Related information` 第一条，也是正文第一句的对照物**
  （`It supplements the DSCP command.`）。**那一页本页没读**，
  两者的分工细目本页一个字不写。
- [[technology-file-for-a-device]] — **本篇两个 key 的定义所在**，原文两处带锚点链过去。
  **那页本页没读**；上面 ⑥ 那条 `CAUTION` 是**转引那一页**，页内已注明。
- [[project]] / [[mapping-project]] — 所在阶段与映射层。**两页本页都没读。**
- [[smartest-6.3.2]] — **`## 版本` 唯一的落点**。
- `*RST`（**未建，allowlist 里也没有**）— **激活命令**。
  **它的文档本页没读**；**`*RST` 为什么能激活 `DTCP` 的值，本篇只说「必须」，没说机制。**
- `testpoints` / `extended_dram_factor`（**未建**）— 两个 key 名，
  **不在 allowlist，用反引号。**

## 版本

**一条：`Introduced before SmarTest 6.3.2`。**

**没有精确引入版本，也没有任何改动、废弃或重命名条目。**

## 出处

本页只读了 `sources:` 那一篇。
**本篇没有 `## Errors`，也没有 `## Warnings`**——
「key 不支持会怎样」「value 不合法会怎样」，**这一篇整个没写**。

**本页没有做的事：**

① 没有读 [[dscp]] 的 raw——两者的分工细目本页没有；
② 没有读 [[technology-file-for-a-device]] 的 raw——**两个 key 的取值、单位、上下界本页都没有**；
③ 没有读 `*RST` 的任何文档；
④ 没有验证「只支持这两个 key」在 SmarTest 7.10.3 里是否仍成立
（原文写的是 `Currently`，是一个会过期的说法）；
⑤ 没有找到任何**读取 active 值**的办法。

**引用规模**：`extract/hubs-dedup.csv` 记本篇被 **4 篇**文档引用（`in_src=4`）。

### ⚠️ 语料瑕疵（逐字，本页不代改）

> ① **`## Parameters` 的表是散架的。** raw 第 32 行是
> ` | key  | The string specifies the system control parameter.`，
> 第 39 行单独一个 ` |`，第 40 行才是 ` | value   | The value to be set as string. |`——
> **没有表头行，两行的列结构也不一致**（`key` 那格跨了 3 行）。
> ② **本篇没有 `## Syntax` 段**：语法直接放在 `## DTCP` 与 `## DTCP?` 两个并列的二级标题底下。
> **脚本的段名表只认 `Syntax` / `Parameters` / `Example`**，
> 所以本页「语法 / 参数」节里**只有参数表、没有那两行语法**（见
> `extract/findings-scaffold-syntax.md`）。**§4 规定该节不许手改，故本页把语法写在上面 `## 典型用法` ① 里。**
> ③ **`## DTCP?` 里的 `returns:` 给的是模板、不是返回值**：紧跟的代码块写
> `DTCP {"key"}, {"value"}`；而 `## Examples` 里的真实返回是 `DTCP "testpoints", "0"`。**同篇两种写法。**
> ④ **两个例子的逗号后空格不一致**：testpoints 那组写 `"testpoints", "100"`（有空格），
> extended_dram_factor 那组写 `"extended_dram_factor","90"`（无空格）。
> ⑤ **`## Related information` 两个链接首尾相接、中间没有分隔符**：
> `DSCP, DSCP? - (Define System Control Parameter)` 的收尾 `)` 直接接
> `Technology file for a device` 的开头 `[`。
> ⑥ **正文第一句是循环定义**：`serves to control certain system control parameters`——
> 「控制控制参数」。
> ⑦ **`Currently, the only supported…` 是会过期的说法**，原文**没给这个「目前」的时点**。
> ⑧ **没有 `## Errors` / `## Warnings`**：非法 key、非法 value、越界值的后果全部未写。
> ⑨ **例子无法证明 `*RST` 生效**（见 `## 典型用法` ④）——**因为能读到的只有 selected 值。**
