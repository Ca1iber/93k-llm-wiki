---
type: object
title: DFUP, DFUP? - (DeFine Utility Purpose)
layer: L1
stage: pin
tags: [pin, l1, firmware-command, utility-purpose, utility-line, utility-pogo-block, upst, flsh, exa-scale]
related: [pin, dfut, flsh, pals, dut-interface-layout, utility-pogo-block-utility-card-v93000-exa-scale-systems, utility-purpose-editor, mapping-pin, smartest-6.3.2, smartest-7.10.1]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.69_DFUP__DFUP__-__DeFine_Utility_Purpose.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# DFUP, DFUP? - (DeFine Utility Purpose)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **844 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.69_DFUP__DFUP__-__DeFine_Utility_Purpose.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### DFUP

```
DFUP {(ch_No_list)}, "{setting}", {(purpose_name)}
```

### DFUP?

```
DFUP? {(purpose_name)}
```

returns

```
DFUP {(ch_No_list)}, "{setting}", {(purpose_name)}
```

### Parameters

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98559.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：3 行 × 2 列。
> 首行（上游原文）：ch_No_list | Utility line channel numbers to be defined as the members of a utility purpose and specified with five digits. The channels must be separated with …

### Example

```
> DFUP (16501,16502,16503,16504),"0110",(AWG_CNCT)
> UPST ,(AWG_CNCT)
> FLSH
> UPST? (AWG_CNCT)
< UPST "0110",(AWG_CNCT)
```

This example defines a utility purpose AWG_CNCT and activates its standard settings.

The members and the setting values are as follows:

```
Member:      16501  16502  16503  16504
---------------------------------------
Setting:     0      1      1      0
```

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.69_DFUP__DFUP__-__DeFine_Utility_Purpose.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

- The channel number is out of range.
- The given name is already assigned to a digital pin, analog pin, DPS pin, or utility name.
- The specified channel has already been defined in the DFUT command as READ ONLY capability.
- Incompatible settings are specified for a channel (for example, `DFUP (101,101),"10", (bad)`).
- The setting contains characters other than "0", "1" and "X (or x)".
- The number of characters in the setting is not equal to that of the channel list.

<!-- 报错节 end -->

## 是什么

**`DFUP`（DeFine Utility Purpose）把若干条 utility line 收成一个具名的组（utility purpose），
并给组里每条线定一个「标准输出状态」。** 本篇的第一句里塞了三件事：

> The DFUP command defines a group (utility purpose) of utility line channels and assigns a standard output state to each of the specified channels. These standard settings must be activated with UPST followed by FLSH.

拆开看：

| 原文分句 | 含义 |
|---|---|
| `defines a group (utility purpose) of utility line channels` | **做的是「多条线 → 一个名字」的编组**，名字叫 **utility purpose** |
| `assigns a standard output state to each of the specified channels` | **每条线各给一个输出状态**——不是整组一个状态，是**逐个给** |
| `These standard settings must be activated with UPST followed by FLSH.` | **发完 `DFUP` 不等于生效**——必须再走 `UPST` 和 `FLSH` 两步 |

**第三句是本页最要紧的一条。** 它在本篇里被写了两遍（定义段一次、`setting` 参数格一次）：

> Note that the settings must be explicitly activated with UPST and FLSH.

**所以 `DFUP` 只完成「定义」这一半**；「让硬件真的照这个状态走」是 `UPST` + `FLSH` 那一半。
**两条命令的文档本页都没读**（见「出处」），**本页只知道这个顺序与这两个名字。**

### 两个方向的命令：`DFUP` 定、`DFUP?` 查

| 命令 | 原文语法（见上面「语法 / 参数」节） | 说明 |
|---|---|---|
| **`DFUP`** | `DFUP {(ch_No_list)}, "{setting}", {(purpose_name)}` | 定义 / 覆盖一个 utility purpose |
| **`DFUP?`** | `DFUP? {(purpose_name)}`，returns `DFUP {(ch_No_list)}, "{setting}", {(purpose_name)}` | **查询，回的是完整定义**——通道列表、状态串、名字三样都回 |

**三个参数的包装符号各不相同，这是语法的硬要求**：
通道列表与 purpose 名在**圆括号**里，`setting` 在**双引号**里。

### 通道号：两套位数，同一套语义

| 格式 | 通道号怎么写 | 原文 |
|---|---|---|
| **现行（五位）** | 前三位 = utility pogo block，后两位 = 该块上的通道号 | `In the five鈥慸igit format, the first three digits of the channel numbers specify the utility pogo block.` |
| **legacy（三位）** | **第一位**（1 ... 8）= utility pogo block，后两位 = 通道号 | `The legacy three鈥慸igit format is also supported: The first digit (1 ... 8) specifies the utility pogo block UTIL鈥? ... UTIL鈥?.` |
| **两者共有** | 后两位是通道号 | `The last two digits specify the channel number 01 ... 32 of the utility line.` |

**pogo block 上有一条 −1 的偏移要算**：

> On the utility pogo blocks, an offset of -1 is to be considered and the channel number is URW00 ... URW31.

**即：pogo block 上印的编号与命令里写的通道号差 1**，且块上通道号的写法是 `URW00` 到 `URW31`
（**00 起、31 止，共 32 条**）。**这与「后两位 01 到 32」不是同一套编号**——
**原文没有解释这两套编号怎么对上**（见「出处」⚠️）。

**查询回来的永远是五位的**，`PALS?` 也一样：

> When reading the defined utility lines with the DFUP? command, the data returned always have the five鈥慸igit format. The same applies to the PALS? command.

**含义**：你按 legacy 三位写进去，`DFUP?` 也回五位。
**所以脚本回读的解析器只按五位写就够了**（这一步是（推断），依据就是上面这一句原文）。

### 两个通道号「不应用」，只能走 I2CA / BDID

> The channel numbers 16515 and 16516 should not be used. They should only be accessed with the I2CAor the BDIDfirmware command.

**这是本篇唯一一处「点名禁用值」**：
`16515` / `16516` **不许出现在 `DFUP` 的通道列表里**，
它们**只能由 `` `I2CA` `` 或 `` `BDID` `` 这两条固件命令去访问**
（raw：`02.06.02.02.142_I2CA__I2CA__-__I2CA_bus.md`、`02.06.02.02.09_BDID__BDID__-__BoarD_ID.md`，
**两篇本页都没读**——所以「为什么不能用」「它们是什么线」本页答不出来）。
**注意这一句原文缺了两个空格**，见「出处」⚠️。

### `setting`：一个字符一条线，顺序就是通道顺序

> Output states for each channel in the ch_No_list. Specify the setting of each utility line with the following specifiers:

| 字符 | 原文（逐字） | 含义 |
|---|---|---|
| **`0`** | `0: sets the corresponding (write) channel to high (high impedance state)` | 置高 |
| **`1`** | `1: sets the corresponding (write) channel to low` | 置低 |
| **`X`（`x`）** | `X (x): no action` | **不动**——不是「置某个状态」，是**这一条线这次不参与** |

**两条硬要求**（原文相邻两句）：

> Specify the setting values corresponding to the definition order of the ch_No_list parameter.

> The number of characters must be equal to the number of the utility line channels in the ch_No_list parameter.

**合起来就是：`setting` 是「位置对应」的**——
第 n 个字符管 `ch_No_list` 里第 n 个通道，**因此字符数必须与通道数相等**。
（不等就是报错，见上面「报错条件」节的第六条。）

> **⚠️ 大小写两边都收**：语法与三个取值都写 `X (x)`——**大写小写都行**。
> 但 **`0` / `1` 没有这回事**，它们只有一种写法。

### `purpose_name`：16 个字符，一张禁用字符表

> Name of the utility purpose. In the query you can use the symbol @ to list all defined utility purposes.

> This parameter can have up to 16 alphanumeric characters and must not contain blank spaces, or any of the following characters: `# ; ( ' ' ) ? @ ,`

| 限制 | 值 |
|---|---|
| 长度上限 | **16 个字母数字字符** |
| 空格 | **不许有** |
| 禁用字符 | `# ; ( ' ' ) ? @ ,`（**原文如此，本页照录**） |
| 查询里的 `@` | **列全部已定义的 utility purpose**——`@` 本身是禁用字符，**只在查询参数位的 `@` 有意义** |

**名字的命名空间不止 utility purpose 一家**——见下。

### 报错条件那六条，有三条说明了别处的规矩

上面「报错条件」节是脚本逐字抽的。**这里只做一件脚本做不了的事：指出哪几条泄露了本篇正文没写的信息。**

| Errors 里的条目 | 它顺带说明的事 |
|---|---|
| `The specified channel has already been defined in the DFUT command as READ ONLY capability.` | **`DFUT` 会给通道定能力（如 READ ONLY），而它定的能力会挡住 `DFUP`。** 这是两条命令之间的**跨命令前置**——**本篇正文一个字都没写这条**，只在报错里出现 |
| `The given name is already assigned to a digital pin, analog pin, DPS pin, or utility name.` | **purpose 名与 pin 名共用一个命名空间**：数字 pin、模拟 pin、DPS pin、utility name **四类都占名字**。**本篇正文只说「16 个字符、禁几个符号」，没说会撞名** |
| `Incompatible settings are specified for a channel (for example, DFUP (101,101),"10", (bad)).` | **同一个通道在列表里出现两次、给了不同状态 → 报错。** 例子用的是 **legacy 三位写法 `101`**，可见 legacy 格式在报错例子里也是合法输入 |
| `The setting contains characters other than "0", "1" and "X (or x)".` | 把上面那张取值表说成是**闭合的**——**只有这三个字符** |
| `The number of characters in the setting is not equal to that of the channel list.` | 对应上面那条「字符数 = 通道数」 |
| `The channel number is out of range.` | **没有写范围是多少**——**「out of range」的界线本篇未写**，本页不猜 |

**⚠️ 「utility name」这个说法在别处叫 `util_name`、在正文里叫 utility purpose**——
四种名字并列时它写的是 `utility name`。**本页不判它是不是指同一批名字**（见「出处」⚠️）。

## 典型用法

**本文档没有 `## Procedure` 段，也没有 `## Before you begin` 段。**
**能当流程读的只有 `## Example` 段那五行命令**——**它本身就是一条完整的四步**：

```
> DFUP (16501,16502,16503,16504),"0110",(AWG_CNCT)
> UPST ,(AWG_CNCT)
> FLSH
> UPST? (AWG_CNCT)
< UPST "0110",(AWG_CNCT)
```

原文对这五行只有一句说明：

> This example defines a utility purpose AWG_CNCT and activates its standard settings.

**拆成四步：**

| # | 命令 | 干什么 | 文档依据 |
|---|---|---|---|
| 1 | `DFUP (16501,16502,16503,16504),"0110",(AWG_CNCT)` | **定义** purpose `AWG_CNCT`，四条线，状态串 `0110` | `## Example` 命令行 + 定义段 |
| 2 | `UPST ,(AWG_CNCT)` | **激活**这个 purpose 的标准设置 | 定义段 `must be activated with UPST followed by FLSH`；`UPST` 的写法**只出现在例子里**（**`UPST` 自己的文档本页没读**） |
| 3 | `FLSH` | **刷下去**（缓冲命令落硬件） | 同上 |
| 4 | `UPST? (AWG_CNCT)` | **回读**，确认生效 | 例子第 4 行 + 它的回复 |

**第 1 步的成员与状态对应关系，原文单独给了一块**：

```
Member:      16501  16502  16503  16504
---------------------------------------
Setting:     0      1      1      0
```

原文引出它的话是 `The members and the setting values are as follows:`。
**两块合起来看，`0110` 是「位置对应」这件事在例子里的样子**：
16501→`0`、16502→`1`、16503→`1`、16504→`0`。

**回读那一行的形态值得抄下来**（`< UPST "0110",(AWG_CNCT)`）：

- **回复里没有通道号列表**——只有 `"setting"` 与 `(purpose_name)`；
  这**与 `DFUP?` 的返回形态不同**（`DFUP?` 回的是三个参数齐全的那一行）。
- **两个形态都是本篇文章自己给的**，本页并列录出，**不替它们调和**。

**查询用 `@` 列全部**：`Name of the utility purpose. In the query you can use the symbol @ to list all defined utility purposes.`
——**本篇没给 `DFUP? (@)` 的例子**，**它的回复长什么样本页不知道**。

**本篇没写的操作细节**（照实说，不填）：`UPST` 的完整语法、
`FLSH` 要不要紧跟、顺序反了会怎样、能不能连着定义多个 purpose——
**本篇一个字都没有**（`## Application` 段只有一句 `For details about utility purposes, see Configuration Setup Commands.`）。

## 和谁有关

- [[pin]] — **stage 页，也是本页 `stage: pin` 的理由**。
  **依据是文档事实**：本篇 `## Application` 段只有一句
  `For details about utility purposes, see Configuration Setup Commands.`，
  而那句指的是 pin 配置那一章（raw：`02.06.03_Pin_configuration_setup_commands.md`，**本页没读**）。
- [[dfut]] — **上游命令，而且这条边是报错段点名的**。
  `DFUT` 定义 utility line 的**名字与能力**（本篇 Errors 第三条：
  `The specified channel has already been defined in the DFUT command as READ ONLY capability.`）；
  `DFUP` 则把若干条线**收成 purpose 并给输出状态**。
  **即：`DFUT` 管「这条线是什么」，`DFUP` 管「这组线输出什么」**——
  **这一步是（推断）**，依据是本篇 Errors 段那句里的 `READ ONLY capability` 与
  `DFUT`（DFUT 的文档本页没读，**它的完整取值 `W` / `R` / `RW` 不在本页的依据里**）。
- [[flsh]] — **生效的第二步**。定义段与 `setting` 参数格两处都点名它；
  例子里的第 3 行就是它。**本篇只说「要 FLSH」，没说为什么、也没说它的语法。**
- [[pals]] — **同类格式的一条边**：`The same applies to the PALS? command.`——
  **`PALS?` 回读时也总是五位**。这一句是把两个查询命令的返回格式绑在一起说的。
- [[utility-pogo-block-utility-card-v93000-exa-scale-systems]] — **有哪几个合法 pogo block 的出处**。
  本篇 `ch_No_list` 那一格把读者指过去（还指了它里面的
  `Utility pogo block mapping` 一节，以及 raw：`02.03.06.08.02_Utility_pogo_block_-_Utility_Card__V93000_EXA_Scale_systems.md`）。
- [[dut-interface-layout]] — **同一格里指的另一篇**：`For valid pogo blocks, refer to DUT interface layout and to Utility pogo block mapping in Utility pogo block - Utility Card (V93000 EXA Scale systems).`
- [[utility-lines]] — **被编组的那个对象本身**（concept 页）。
  **本篇没用 `utility lines` 当页名点名它**，只说 `utility line channels`；
  「utility line 是什么、在 DUT 板上干什么」在那一页，**本页没有那些事实**。
- [[utility-purpose-editor]] — **（推断）GUI 侧的同一个对象**。
  **本篇 raw 里一个界面名字都没有**（连 `editor` 这个词都没有）；
  依据只是 [[mapping-pin]] 把本页与那一页排在同一行
  （`utility purpose（一组 utility line + 标准状态） | utility-purpose-editor | pin-configuration-file | dfup | — | —`）。
  **那一行的「GUI ↔ 命令」对应是它推的，不是本篇写的。**
- [[pin-configuration-file]] — **[[mapping-pin]] 把本页的产物落在它上面**（同一行）。
  **本篇一个字都没提文件**；这条关系**本页没有依据**。
- [[mapping-pin]] — **跨层对照表**，本页在那张主表里占一行（见上一条引的那一行）。
- `UPST`（**不在 allowlist，故不链**）— **生效的第一步**，本篇两处点名、例子第 2/4 行用它。
  raw：`02.06.02.02.305_UPST__UPST__-__Utility_Purpose_STate.md`。**本页没读**——
  所以**「怎么激活、激活了怎么取消、`UPST?` 与 `DFUP?` 的区别」本页答不出来**。
- `I2CA` / `BDID`（**均不在 allowlist，故不链**）— **16515 / 16516 仅有的两个访问口**。
  raw：`02.06.02.02.142_I2CA__I2CA__-__I2CA_bus.md`、`02.06.02.02.09_BDID__BDID__-__BoarD_ID.md`。**两篇都没读。**
- `Configuration Setup Commands`（未建）— **`## Application` 段指的那一章**，
  也是「utility purpose 到底为什么存在」的答案所在。**本页没读。**
- [[set-utility-lines]] / [[get-utility-lines]] — **名字里有 utility line 的同族页**。
  **本篇 raw 里这两个名字出现 0 次**；**是不是与本页同一批东西，本页没有依据**（按页名并列列出，不代表同物）。
- [[smartest-6.3.2]] / [[smartest-7.10.1]] — **版本页**：本篇 `## Functional changes` 的两条分别落在它们身上。

## 版本

本文档有 `## Functional changes` 段，**两条，逐条转录**：

- `Introduced before SmarTest 6.3.2`
- `SmarTest 7.10.1: Three-digit utility pogo block designator on V93000 EXA Scale systems.`

**两条都要留意：**

- **第一条是哨兵值**（§11.2 ②）：意思是「**在本文档集覆盖范围开始之前就已经有了**」，
  **不是「SmarTest 6.3.2 新增了 `DFUP`」**。照字面读会生成一条假信息。
- **第二条和正文里的位数规则对得上，但「three-digit」这个词在两处指的不是同一件事**：

| 出处 | 原文里的 `three-digit` 修饰谁 | 意思是 |
|---|---|---|
| `## Functional changes` | **`utility pogo block designator`**（pogo block 的编号） | **新格式里 pogo block 用三位数写**（`165` 这样的前三位） |
| 参数表的 `ch_No_list` 格 | **`format`**（整个通道号的写法） | **legacy 的通道号只有三位**（第一位是 block，1 ... 8） |

**同一个词，一处说「block 号是三位」，一处说「整个通道号是三位」。**
**本页并排列出，不替语料改字（§1.1、§11.2）。**
（把它读通的（推断）是：7.10.1 引入的是**五位通道号格式**，
其中 pogo block 占了**三位**；而 legacy 是**三位通道号**、block 只占**一位**。
**依据是两处各自的上下文，尤其是 `The first digit (1 ... 8)` 与 `the first three digits` 的对比。**）

**本篇没有记录 7.10.1 之后 `DFUP` 被改过**——**「没记录」不等于「没改过」**（§13.1 第 ⑥′）。

## 出处

`sources:` 一篇：
`02_System_reference/02.06_Command_Reference/02.06.02.02.69_DFUP__DFUP__-__DeFine_Utility_Purpose.md`
（TDC `98559.htm`，73 行 / 4,497 字节）。**整篇读完。**

**本页没做的：**

- **`UPST` 那一篇没读**（`02.06.02.02.305_UPST__UPST__-__Utility_Purpose_STate.md`）——
  **这是本页最大的缺口。** 定义段说「必须用 `UPST` 和 `FLSH` 激活」，
  但**「怎么激活、激活时还要不要带参数、激活完怎么取消」本篇一个字都没写**，
  本页也就给不出来。例子里那行 `UPST ,(AWG_CNCT)` 的写法**只出现在例子里，没有语法定义**。
- **`FLSH` 那一篇没读**（`02.06.02.02.124_FLSH_-__FLuSH_buffered_commands.md`）。
  所以「为什么必须刷」「不刷会怎样」「它和别的缓冲命令什么关系」本页没有。
- **`DFUT` 那一篇没读**（`02.06.02.02.70_DFUT__DFUT__-__DeFine_UTility_line.md`）。
  本页关于 `DFUT` 的**唯一依据是 Errors 段第三条那句话**（`as READ ONLY capability`）——
  **`DFUT` 的完整能力取值、语法、报错，本页一个字都没有**（上面「和谁有关」里那条推断已标出）。
- **`PALS?` 那一篇没读**（`02.06.02.02.173_PALS__PALS__-__Pin_ALlocation_for_multiple_Sites.md`）。
  本页只知道「它的返回也是五位」这一句。
- **`I2CA` / `BDID` 两篇没读**（`02.06.02.02.142` / `02.06.02.02.09`）。
  所以**为什么 16515 / 16516 不能用、它们到底是哪两条线，本页答不出来**。
- **`DUT interface layout` 与 `Utility pogo block - Utility Card (V93000 EXA Scale systems)` 两篇没读**
  （`02.03.03.01` / `02.03.06.08.02`）——**「有哪些合法 pogo block」这张表本页没有**，
  本页只有「前三位是 block 号」这条规则。
- **`Configuration Setup Commands`（`## Application` 段指的整章）没读**
  （`02.06.03_Pin_configuration_setup_commands.md`）。**所以「utility purpose 用来干什么」
  「实际工程里怎么组织它」本页没有**——本页只有命令本身的机制。
- **一张图都没看——因为这一篇里没有图。** 实测全文 **0 处** `.png` / `.jpg` / `raw/`。
  **所以本页没有任何来自图的结论。**
- **没有实跑。** 没有在任何机台上发过一条 `DFUP`，也没有验证过
  「不 `UPST` 会怎样」「16515 会不会报错」「`URW00` 到 `URW31` 与 `01` 到 `32` 怎么对上」。
  `verified: doc-only` 指的就是这件事。
- **本文档没有 `## Procedure` / `## Before you begin` 段**——
  上面「典型用法」那四步是**本页按 `## Example` 那五行命令 + 定义段那句话排出来的**，
  **不是文档给的编号流程**。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
> ① **三处坏字，都是 `鈥慸` 那一族**（§11.2 ①）。逐字引如下：
> `In the five鈥慸igit format, the first three digits of the channel numbers specify the utility pogo block.`
> `The legacy three鈥慸igit format is also supported: The first digit (1 ... 8) specifies the utility pogo block UTIL鈥? ... UTIL鈥?.`
> `When reading the defined utility lines with the DFUP? command, the data returned always have the five鈥慸igit format.`
> **`鈥慸` 是「短横 + 后一个字母被一起吃掉」**（`five鈥慸igit` = *five-digit*、
> `three鈥慸igit` = *three-digit*，那个 `d` 并进了第二个坏字里）——
> **所以拿修好的词去 raw 里搜是搜不到的，要搜坏掉的形态。**
> 处置照 §11.2 ①：**页面照原样转录**（本页正文与「是什么」里引的就是坏字）。
> ② **`UTIL鈥? ... UTIL鈥?` 里的 `鈥?` 还原不出唯一一个字**——
> 它是三字节 UTF-8 字符的头两个字节、第三个字节已被替换成 `?`。
> 上下文只说「第一位 1 ... 8」，**所以中间那个字符可能是下划线、也可能是短横，
> 但本页不猜**（§11.2 ① 明令这一类只许报区间、不许当映射用）。
> ③ **原文缺空格（一处两处）**：那句照原文渲染出来是
> `They should only be accessed with the I2CAor the BDIDfirmware command.`
> ——`I2CA` 后面**直接接 `or`**、`BDID` 后面**直接接 `firmware`**，
> 两处的链接标记与下一个词之间**都没有空格**（`I2CA` 那处接的是 `or the`，`BDID` 那处接的是 `firmware`）。
> **两个词被粘住了，原文如此，本页照录。**
> ④ **`setting` 取值的第一个说明里，`high` 与 `high impedance state` 被并写**：
> `0: sets the corresponding (write) channel to high (high impedance state)`——
> **「高电平」与「高阻态」在电学上不是一回事**，原文把两者写在同一个括号里。
> **本页照录，不替它解释**（§10：不自行选一个当正确答案）。
> ⑤ **禁用字符表写作 `# ; ( ' ' ) ? @ ,`**——**中间那个 `' '`（单引号+空格+单引号）读不出是什么**。
> 原文如此，**本页照录**；`DFUT` 那一篇里是同一串（**本页没读那篇，只按本篇记**）。
> ⑥ **编号有两套且原文没说怎么对上**：参数表里是
> `The last two digits specify the channel number 01 ... 32 of the utility line.`，
> 而下一句是 `the channel number is URW00 ... URW31.`——
> **一套 `01` 到 `32`、一套 `URW00` 到 `URW31`**，只有「offset of -1」这一句提示它们差 1。
> **本页并列录出，不替它调和。**
> ⑦ **`utility purpose` 与 `utility name` 两种叫法在本篇里并存**：
> 正文与参数表一律叫 `utility purpose`，**Errors 段第二条写的是
> `The given name is already assigned to a digital pin, analog pin, DPS pin, or utility name.`**
> **本页不判这两个词是不是指同一批名字。**
> ⑧ **本篇没有一处 CJK 之外的坏字**——实测非 ASCII 只有上面 ① ② 那三行（`鈥` 族），
> **没有 `渭` / `碌` 那一族**。**这是「本页量过的」，判据是本篇这一个文件。**

`verified: doc-only`——**本页没有在任何真实机台上发过 `DFUP`**
（§11：文档里有 ≠ 这台机器上能用；尤其 `16515` / `16516` 那条禁令、
以及两套编号的对应关系，**动手前先照实机核对**）。
