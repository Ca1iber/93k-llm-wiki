---
type: object
title: UPAS, UPAS? - (Utility Purpose ASsignment for multi-site)
layer: L1
stage: pin
tags: [upas, l1, firmware-command, pin, utility-purpose, multi-site, setup-focus, buffer-then-activate, pste]
related: [dfup, dfut, psfc, pste, flsh, utility-lines, utility-purpose-editor, utility-pins-editor, pin, command-reference, site-focus-required-before-command, smartest-6.3.2, smartest-7.10.3, dfpr, pslv]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.304_UPAS__UPAS__-__Utility_Purpose_ASsignment_for_multi-site.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# UPAS, UPAS? - (Utility Purpose ASsignment for multi-site)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,807 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.304_UPAS__UPAS__-__Utility_Purpose_ASsignment_for_multi-site.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### UPAS

```
UPAS {site}, ["{setting}"], {(purpose_name)}
```

### UPAS?

```
UPAS? {site}, {(purpose_name)}
```

returns:

```
UPAS {site}, "{setting}", {(purpose_name)}
```

### Parameters

| site |

The site parameter is an integer that defines the number of the site where the channels are to be defined.

The integer must be greater than 1.

When specified as part of the UPAS? query, you can use the parameter ALL to read the standard output states for all sites.

 |
 | setting |

Output states for each member of the utility purpose on the specified site.

Set the output state of each utility line with the following specifiers:

- 0: Sets the corresponding (write) channel to high (high impedance state)
- 1: Sets the corresponding (write) channel to low
- X (x): No action

The number and order of characters must correspond to the ch_No_list parameter of the `DFUP`（raw: `02.06.02.02.69_DFUP__DFUP__-__DeFine_Utility_Purpose.md`） command.

If this parameter is omitted, the specified site is set to the same states as site 1.

 |
 | purpose_name |

Name of a utility purpose defined by the `DFUP`（raw: `02.06.02.02.69_DFUP__DFUP__-__DeFine_Utility_Purpose.md`） command.

In the query, the symbol @ can be used to list all defined utility purposes.

 |

### Example

```
> DFUP (101,102,103,104),"11XX",(AWG_CNCT)
> UPAS 2,"XX11",(AWG_CNCT)
> UPST ,(AWG_CNCT)
> FLSH
> UPST? (AWG_CNCT)
< UPST "11XX", (AWG_CNCT)
> PSFC 2
> UPST ,(AWG_CNCT)
> FLSH
> UPST? (AWG_CNCT)
< UPST "XX11", (AWG_CNCT)
```

In this example, the `DFUP`（raw: `02.06.02.02.69_DFUP__DFUP__-__DeFine_Utility_Purpose.md`） command defines a utility purpose AWG_CNCT and output states for site 1. The UPAS command defines the output states of AWG_CNCT for site 2. First the settings of site 1 are activated. Then the setup focus is restricted to site 2, and the output states for site 2 are activated.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.304_UPAS__UPAS__-__Utility_Purpose_ASsignment_for_multi-site.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

- A multisite setting is not performed with the `PSTE`（raw: `02.06.02.02.199_PSTE__PSTE__-__Parallel_SiTe_Enable.md`） command.
- The specified site number is less than 0 or greater than that of the max site.
- The given name is not allocated to any utility purpose.
- The given name has already been assigned to a digital pin, analog pin, DPS pin, or utility name.
- Inconsistent settings are specified for one channel (for an example, see the `DFUP`（raw: `02.06.02.02.69_DFUP__DFUP__-__DeFine_Utility_Purpose.md`） command).
- The setting contains characters other than "0", "1" and "X (or x)".
- The number of characters in the setting is not equal to that of the channel list in the `DFUP`（raw: `02.06.02.02.69_DFUP__DFUP__-__DeFine_Utility_Purpose.md`） command.

<!-- 报错节 end -->

## 是什么

**`UPAS`（Utility Purpose ASsignment）解决的是一件事：同一个 utility purpose，在不同 site 上要不同的输出状态。**

> 「The UPAS command serves to assign different standard output states to the same utility purpose for sites > 1.」

**句子末尾那个 `for sites > 1` 是关键**——**site 1 不归它管**，原文下一段直接说了：

> 「The utility purpose must have been defined with the DFUP command. DFUP also sets the standard output states for site 1.」

| 谁 | 管什么 |
|---|---|
| [[dfup]] | **定义** utility purpose（一组 utility line 通道）；**并且设定 site 1 的标准输出状态** |
| `UPAS` | 给 **site > 1** 赋**不同的**标准输出状态 |

**所以两者是接力的：`UPAS` 的硬前置是「这个 purpose 已经被 `DFUP` 定义过」。**
（原文用 `must have been defined`——这是前提，不是建议。）

### 三段语法

| 段 | 参数 | 原文要点 |
|---|---|---|
| 1 | `site` | 整数，**必须大于 1**；**只有查询能用 `ALL`**（见下） |
| 2 | `setting` | 每条线一个字符：`0` / `1` / `X (x)`；**长度与顺序必须对应 [[dfup]] 的 `ch_No_list`**；**省略 = 与 site 1 相同** |
| 3 | `purpose_name` | 由 [[dfup]] 定义的名字；查询里写 `@` = 列全部已定义的 purpose |

**`site` 那格的三句原文逐字：**

> 「The site parameter is an integer that defines the number of the site where the channels are to be defined.」

> 「The integer must be greater than 1.」

> 「When specified as part of the UPAS? query, you can use the parameter ALL to read the standard output states for all sites.」

**`ALL` 只写在 `UPAS?` 里**——原文限定得很死（`When specified as part of the UPAS? query`），
**写的那一侧（`UPAS`）没有这个取值**。

### `setting`：三个字符，`0` 不是「关」

> 「Output states for each member of the utility purpose on the specified site.」

> 「Set the output state of each utility line with the following specifiers:」

| 字符 | 原文逐字 | 效果 |
|---|---|---|
| `0` | `0: Sets the corresponding (write) channel to high (high impedance state)` | **高 / 高阻** |
| `1` | `1: Sets the corresponding (write) channel to low` | **低** |
| `X (x)` | `X (x): No action` | **不动** |

**两个容易记反、也容易漏的点：**

1. **`0` 是「高/高阻」，不是「关断」**——**它和 `1` 是一对「电平」，不是一对「开/关」。**
2. **`X` 是唯一「什么都不做」的取值**——**不写 `X` 就等于你要求那一位变成某个确定状态**。
   例子里两个 site 用的是**互补**的串（`11XX` / `XX11`），**就是靠 `X` 让两个 site 各管一半的线**
   （**这一步是本页按上面那张表解读的，不是原文的分析**，见「典型用法」）。

**串的形状是死的**：

> 「The number and order of characters must correspond to the ch_No_list parameter of the DFUP command.」

**即：串长 = 通道数，第 k 个字符对应 `ch_No_list` 里第 k 条通道。**
**串长不对是报错条件里的一条**（逐字：`The number of characters in the setting is not equal to that of the channel list in the DFUP command.`）；
**「顺序错了会怎样」本篇没写**——原文只说了 `must correspond`，
**报错条件里没有对应「顺序」的那一条**。

**省略这个参数的默认行为原文也写了**：

> 「If this parameter is omitted, the specified site is set to the same states as site 1.」

**「不给」= 「照抄 site 1」**，**不是「保持原样」**——两者容易混，原文写的是前者。

### 赋值 ≠ 生效：要另走三步

**`UPAS` 自己不把状态推到硬件上。** 原文把激活路径写在一个句子里：

> 「In order to activate the output states, first restrict the setup focus to the site in question with PSFC, and then activate the settings with UPST and FLSH.」

| 步 | 做什么 | 靠谁 |
|---|---|---|
| ① | **把 setup focus 限制到目标 site** | [[psfc]] |
| ② | **激活**设置 | `UPST`（**未建页、不在 allowlist**） |
| ③ | **flush** | [[flsh]] |

**这三步缺一不可**；而且**①②③ 全都在 site 的层面上工作**——
原文紧接着的两段是**所有 site 相关命令里都会出现的两段话**（同批 [[pslv]] 也有）：

> 「With this command you configure setups of those sites that have the setup focus: For more information, see also: PSFC, PSFC?.」

> 「With this command you can retrieve site specific information (only one site can be in focus at a time). For the site in focus, SmarTest displays results in the Testflow Editor and in the result tools. Also, any firmware queries report setup and results for the site currently in focus only.」

**要紧的是括号里那半句：同一时刻只有一个 site 在焦点里。**
**所以「给 site 2 赋值」这件事本身，必须先让 focus 落在 site 2 上才算数。**
这条前因后果见 [[site-focus-required-before-command]]。

**还有一条前置藏在报错条件里**（本页「报错条件」节第 1 条，脚本逐字取）：

| 报错原文 | 意思是 |
|---|---|
| `A multisite setting is not performed with the PSTE command.` | **multi-site 没先用 [[pste]] 打开，就报错** |

**即：`UPAS` 是「多 site 模式」下的命令**——**单 site 环境里它连门都进不去。**

### `UPAS?`：回读**带上 site**

`UPAS?` 的语法与它的 `returns:` 行（逐字在「语法 / 参数」节）说明回读长这样：

```
UPAS {site}, "{setting}", {(purpose_name)}
```

**回读里带 `site`**——所以**同一页里多个 site 的状态不会混**：
你问哪个 site，它就把那个 site 的串吐回来。
`purpose_name` 那格还写了查询的另一种用法：

> 「In the query, the symbol @ can be used to list all defined utility purposes.」

**`@` = 列全部已定义的 utility purpose**（**原文没有给 `@` 的命令行例子，本页不编**）。

## 典型用法

**本篇没有 `## Procedure` / `## Before you begin` / `## What to do next`**——
用法全部来自 `## Example` 那一段（**本页唯一的实操材料**）与正文那几段散文。

### 例子的原文（一整段会话）

```
> DFUP (101,102,103,104),"11XX",(AWG_CNCT)
> UPAS 2,"XX11",(AWG_CNCT)
> UPST ,(AWG_CNCT)
> FLSH
> UPST? (AWG_CNCT)
< UPST "11XX", (AWG_CNCT)
> PSFC 2
> UPST ,(AWG_CNCT)
> FLSH
> UPST? (AWG_CNCT)
< UPST "XX11", (AWG_CNCT)
```

原文对这段的说明逐字：

> 「In this example, the DFUP command defines a utility purpose AWG_CNCT and output states for site 1. The UPAS command defines the output states of AWG_CNCT for site 2. First the settings of site 1 are activated. Then the setup focus is restricted to site 2, and the output states for site 2 are activated.」

### 逐步对回去

| 行 | 做了什么 | 依据 |
|---|---|---|
| `DFUP (101,102,103,104),"11XX",(AWG_CNCT)` | **定义 purpose `AWG_CNCT`**：四条通道 `101,102,103,104`，**site 1 的状态 `11XX`** | 「DFUP also sets the standard output states for site 1.」 |
| `UPAS 2,"XX11",(AWG_CNCT)` | **给 site 2 赋 `XX11`**——这就是本命令的唯一动作 | 本命令的定义 |
| `UPST ,(AWG_CNCT)` + `FLSH` | **激活 site 1 的状态** | 「First the settings of site 1 are activated.」+ 那三步路径 |
| `PSFC 2` | **把 setup focus 限制到 site 2** | 「Then the setup focus is restricted to site 2」 |
| `UPST ,(AWG_CNCT)` + `FLSH`（再来一遍） | **激活 site 2 的状态** | 「and the output states for site 2 are activated」 |
| `UPST? (AWG_CNCT)` → `< UPST "11XX", (AWG_CNCT)` | **读回来是焦点 site 的状态** | 两次读回分别给 `11XX` / `XX11` |

**这张表里最值钱的一行是第 5 行：`UPST` 同一条命令出现了两次，做的事不一样。**
**决定它作用在哪个 site 上的，是当时焦点在哪**——第一次之后没有 `PSFC`，
第二次之前有 `PSFC 2`。**这正是「赋值靠 `UPAS`、生效靠 `UPST` + 焦点」那句的实证。**

> **（推断）第一次 `UPST` 时焦点在 site 1。** 依据是**原文自己说
> `First the settings of site 1 are activated.`**，而激活要经过「先把 focus 限制到目标 site」
> ——**这一段里第一次 `UPST` 之前没有任何 `PSFC`**。**「默认焦点是 site 1」这句
> 本篇 md 里没有**（本篇只说 `only one site can be in focus at a time`）。

### 按 `0`/`1`/`X` 把两个串解开

**（下面是本页照字符含义做的解码，不是原文的分析。）**

| 通道 | site 1 的 `11XX` | site 2 的 `XX11` |
|---|---|---|
| `101` | `1` → **low** | `X` → 不动 |
| `102` | `1` → **low** | `X` → 不动 |
| `103` | `X` → 不动 | `1` → **low** |
| `104` | `X` → 不动 | `1` → **low** |

**两个 site 的串互补**：**site 1 驱动前两条、site 2 驱动后两条，互不碰对方**。
**（推断）这看起来就是 `UPAS` 的用途——让不同 site 各驱动自己那几条线。**
**但原文没有对这一层做任何说明**，所以本页只说「串是这样解的」，
**不说「这就是用它做 site 隔离的标准做法」**。

### 一个反问（本页答不了）

`UPST?` 的两次读回，一次给 `11XX`、一次给 `XX11`，**说明它报的是「焦点 site」那一份**。
**而 `UPAS?` 自带 `{site}` 参数**——**两者与「只报焦点 site」这条规则怎么共存，本篇没写。**
**本页不替它编。**

**归属**：原文 `## Application` 一节全文只有一句——
`For more information about utility purposes, see Defining a utility purpose and Accessing Utility Lines.`
（两篇**都没建页、都不在 allowlist 里**，本页也没读。）

## 和谁有关

- [[dfup]] —— **前置，而且是最硬的那一条**：`The utility purpose must have been defined with the DFUP command.`
  **`UPAS` 的对象是 `DFUP` 造出来的**；`ch_No_list` 的**长度与顺序**也在 `DFUP` 那边定。
  **本页没读 [[dfup]]。**
- [[dfut]] —— **同族的另一条岔路**：`DFUT` 定义**单条** utility line（名字 + 方向），
  `DFUP` 定义**一组**（purpose），`UPAS` 再给**多 site** 赋不同状态。
  **本篇一个字没提 [[dfut]] / [[dfup]] 的语法**——三层各管一段，本页只管第三段。
- [[psfc]] —— **激活路径的第一步**：把 setup focus 限制到目标 site。
  **原文点名它，并另给了一条链接（`PSFC, PSFC?`）**。**本页没读。**
- [[pste]] —— **前置（藏在报错里）**：multi-site 没先用它打开，`UPAS` 直接报错
  （报错条件第 1 条逐字：`A multisite setting is not performed with the PSTE command.`）。
  **本页没读。**
- [[flsh]] —— **激活路径的最后一步**：`UPST` 之后要 `FLSH`（原文：
  `activate the settings with UPST and FLSH`）。**本页没读**，
  所以「为什么非要 flush」「flush 的是什么」**本页一个字没有**。
- [[utility-lines]] / [[utility-purpose-editor]] / [[utility-pins-editor]] ——
  **同一条线的另外几页**：utility line 本身、以及 GUI 侧的 purpose / pins 编辑器。
  **这三篇本页都没读**（`utility-purpose-editor` 是 GUI 页，本篇是固件命令）。
- [[pin]] / [[command-reference]] —— **归属**：`stage: pin` 对上的是
  `## Application` 指的那两篇（utility purpose 属于配置 setup）；
  doc 本身在 `02.06_Command_Reference` 下。（§6：`stage` 是「**最近的一段**」，不是归属。）
- [[site-focus-required-before-command]] —— **本命令踩错前置的后果页**：
  `UPAS` 受焦点约束，**焦点不对时它配的是别的 site**。**本页没读那一页。**
- `UPST`（**未建页、且不在 allowlist 里**）—— **激活路径的第二步**，
  也是例子里真正跟硬件对话的那条命令（`UPST ?` / `UPST?`）。
  **本篇没读它的文档，所以 `UPST` 的语法本页没有。**
- `Defining a utility purpose` / `Accessing Utility Lines`（**均未建、不在 allowlist 里**）——
  原文 `## Application` 指定的两处「详情在这」。

## 版本

本文档**有** `## Functional changes` 段，**只有一条**：

```
- Introduced before SmarTest 6.3.2
```

**这一条是 §11.2 ② 的哨兵值**（措辞是 `before`，不是 `Introduced in`）——
**意思是「早于本文档集覆盖范围」**，**所以 `UPAS` 究竟成立于哪个版本，这份语料里没有。**
**7.10.3 上它有没有变，本篇版本段也没写**（本 wiki 面向 [[smartest-7.10.3]]，
而同批 [[dfut]] 的版本段停在 7.10.2）。

## 出处

`sources:` 一篇：
`02_System_reference/02.06_Command_Reference/02.06.02.02.304_UPAS__UPAS__-__Utility_Purpose_ASsignment_for_multi-site.md`
（TDC `98832.htm`；**md 4,436 字节 / 106 行**，上游 htm 9,303 字节）。**整篇读完。**

**本页没做的**：

- **[[dfup]] 没读**——**`UPAS` 最硬的前置就是它**，而「purpose 是什么、`ch_No_list` 怎么给」
  本页一个字没有；本页只有 `The utility purpose must have been defined with the DFUP command.`
  这一句与「`DFUP` 顺带定 site 1 的状态」。
- **`UPST` 没读**——**激活路径的第二步、例子里真正动手的那条命令，本页没有它的语法。**
- **`FLSH` 没读**——**「为什么非要 flush」本页答不了**（[[flsh]] 有页，但本页没读）。
- **[[psfc]] 没读**——「怎么设焦点、默认焦点在谁」本页没有。
  **例子里「第一次 `UPST` 作用在 site 1」是本页的推断**（推断链写在「典型用法」里）。
- **`Defining a utility purpose` / `Accessing Utility Lines` 都没读**——
  原文 `## Application` 指的这两篇是「utility purpose 是什么、怎么访问」的正文。
- **四条入边一篇没读**（本页的「和谁有关」全部来自本篇原文的链接与报错条件，没有回核别的页）。
- **图：本篇没有内嵌图片**——判据可核：本篇 md 里 `.png` / `.jpg` / `![` **0 命中**。
  **所以本页没有任何来自图的结论。**
- **编码坏字：本篇 0 处**——`[一-鿿]` 扫过整篇 md，**一个汉字都没有**。**实测，不是没查。**
- **没有实跑。** 没有在机台上发过 `UPAS` / `UPAS?`、没配过多 site、没触发过那七条报错。
  `verified: doc-only` 说的就是这件事（§11：文档里有 ≠ 这台机器上能用）。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**（§11.2）：
>
> **① 参数说「必须大于 1」，报错说「小于 0」才报错——`0` 与 `1` 落在两者之间的缝里。**
> 两条逐字并排：
>
> ```
> The integer must be greater than 1.
> ```
>
> ```
> The specified site number is less than 0 or greater than that of the max site.
> ```
>
> ——**按参数那句，`1` 不合法；按报错那句，`1` 不报错**（只有 `< 0` 才报）。
> 而 `site 1` 又是原文明写的「`DFUP` 管的那一个」（`DFUP also sets the standard output states for site 1.`）。
> **核过上游 `raw/98832.htm`：htm 里这两句一字不差，上游就如此**（§11.2 ⑥ 那一类）——
> **救不回来，本页并列两句，不替它调和，也不判哪个对。**
>
> **② 「焦点」那一段的两个冒号中间没有东西。** 逐字：
> ```
> With this command you configure setups of those sites that have the setup focus: For more information, see also: PSFC, PSFC?.
> ```
> ——**前一个冒号后直接接上了另一句**（`For more information, see also:`），
> 读起来像「冒号后面那份清单」被压掉了。
> **核过上游 `raw/98832.htm`：上游一字不差，就是两个冒号连排**（同 ①，上游如此）。
> **本页照原样引。**
>
> **③ 例子里的 `UPST` 与逗号之间有一个空格。** 逐字两处：
> `> UPST ,(AWG_CNCT)`——而同一段里 `DFUP (101,102,103,104),"11XX",(AWG_CNCT)` 与
> `UPAS 2,"XX11",(AWG_CNCT)` 都是**逗号紧贴前一个参数**。
> **本篇没有 `UPST` 的语法段，所以本页不能判这个空格合法与否**——
> **只记下「同一段例子里三种写法不一致」。**
>
> **④ 例子的回读行用 `UPST`，而发出的是 `UPST?`。** 逐字：
> `> UPST? (AWG_CNCT)` 对 `< UPST "11XX", (AWG_CNCT)`。
> ——**这不是错**（查询用设置形的名字回话：同 [[dfpr]] 的 `DFPR?` 回的是 `DFPR`，**末尾没有 `?`**），
> **记在这里是因为读快了会以为「例子里发的是 `UPST`」。**
>
> **⑤ md 转换丢了链接的 `title=` 提示语。** 本篇上游 htm 里，正文里那四个链接
> （`DFUP` / `PSFC` / `UPST` / `FLSH`）**各带一段提示语**（讲各自那条命令干什么），
> **md 里一个字都没有**（§11.2 ① 那一族：上游有、转换后丢）。
> **本页没有把那些提示语的文字写进正文**——**它们不是本篇 `sources:` 里的内容，
> 也不是本页的引文**；若要读，回 `raw/98832.htm` 看那几个 `title=` 属性。
> **（这类内容有个特点：拿它去 md 语料里 grep 是搜不到的。）**

`verified: doc-only`
