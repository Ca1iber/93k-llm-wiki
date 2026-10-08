---
type: object
title: STME, STME? - (SiTe Match Enable)
layer: L1
stage: pin
tags: [stme, l1, firmware-command, pin, multi-site, site-match, fast-sync, match-loop, auto, nife, sqst]
related: [pin, match-loops, sqst, pact, controlling-multiple-sites, smartest-6.3.2, smartest-7.4.0, smartest-7.10.3, command-reference]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.250_STME__STME__-__SiTe_Match_Enable.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# STME, STME? - (SiTe Match Enable)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,096 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.250_STME__STME__-__SiTe_Match_Enable.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### STME

```
STME {ON|OFF|AUTO|FAST},
```

### STME?

```
STME?
```

returns:

STME {ON|OFF|FAST),

### Parameters

| ON | Turns the site match function on. |
|---|---|
| OFF | Turns the site match function off. |
| AUTO | Starting the sites successively affects the test negatively if the pin configuration contains at least one shared digital channel for triggering an analog module. The AUTO option checks if such a shared channel exists. If it does, the match site function is set to OFF; if not, it is set to ON. AUTO is the default. |
| FAST | Activates the `Fast Sync`（raw: `02.06.07.01.08.04.03.03_Fast_Sync.md`） feature (local synchronization) of the test processor. After setting this option," STME ON" is required to turn on the site match function. |

### Example

```
> STME AUTO,
> STME?
< STME ON,
```

This example sets the site match function to AUTO, then reads the actual setting. Since the actual setting is ON, the pin configuration cannot contain a shared digital channel.

```
>SQST OFF
>NIFE 2
>STME FAST,
>STME ON,
```

This example configures the Fast Sync feature, and sets two independent Fast Sync ports on each test processor.

<!-- 语法节 end -->

## 是什么

**`STME` 管的是「各 site 是同时起，还是依次错开一点起」。** 原文第一段三句：

> 「The STME command defines the state of the site match function. The site match function controls if all sites are started simultaneously (option OFF), or successively with a slight delay (option ON). The command does nothing if a single site is configured.」

| 要的启动方式 | 选哪个 |
|---|---|
| 所有 site **同时**起 | **`OFF`** |
| 所有 site **依次**起（`with a slight delay`） | **`ON`** |

**⚠️ 这里最容易记反**：**`ON` 开的不是「同时」，`ON` 开的是 site match 功能本身，效果是各 site 依次起**；
**`OFF` 才是「大家一起起」。** 两个取值名指的是 **site match 这个功能**，不是「同时性」。

**上游把这条说得更直白**——**这句在本篇的 md 里没有**：它是 `Controlling the site match function`
那一篇（**本页没读**）的开头摘要，**本页是从上游 `98760.htm` 那个链接的 `title` 属性读到的**，逐字：
`When you execute a multisite test in parallel, you can either start all sites simultaneously, or you can start them one after the other successively, each with a small offset. This is controlled by the setting of the Site Match test suite flag. If this flag is set to OFF, all sites are started simultaneously; if it set to ON, they are started successively.`

**这条摘要里还有两件本篇没有的事**：① `with a slight delay` = **`each with a small offset`**；
② **它由 `Site Match` test suite flag 控制**（除 `STME` 之外还有 test suite flag 这条路）。
**那个 flag 长什么样、在 test suite 的哪一处——讲它的那几篇本页都没读**（见「出处」）。

**第三句是硬边界**：`The command does nothing if a single site is configured.` —— **单 site 配置下它什么也不做。**

### 三个选项各自的「什么时候必须要它」

原文对 `ON` / `OFF` / `FAST` 各给了一句「必须」：

> 「The ON option is required for evaluation of match loops per site in a multisite test (on match loops see Match loops). For if all sites are started simultaneously, the decision if a match was obtained will be based on the compare results of all sites.」

> 「The OFF option is required if one digital channel is shared among several sites for triggering a shared analog module. For details see Controlling the site match function.」

> 「The FAST option is required if the local synchronization of the test processor is enabled for match loops and conditional jumps. For details see Fast Sync.」

（**第一句里的 `For if all sites are started simultaneously` 原文如此**——`For` 后面直接跟 `if`，读起来像漏了一个词。
**已核上游 `98760.htm`：上游也这样**，见「出处」⚠️ ④。）

| 情况 | 必须选 | 原文的理由 |
|---|---|---|
| multisite 里要**按 site 逐个判定 match loop** | **`ON`** | 否则 `the decision if a match was obtained will be based on the compare results of all sites` |
| **一个数字通道被多个 site 共用**去触发一个共享模拟模块 | **`OFF`** | 依次起会 `affects the test negatively`（这句在 `AUTO` 那一格里） |
| 开了 **test processor 的本地同步（Fast Sync）**、用于 match loop 与条件跳转 | **`FAST`** | 见下 |

**`ON` 那一句是本页最值钱的一条**：不用 `ON`（即各 site 同时起）时，
**「是否 match」的判定会落在所有 site 的比较结果上**——也就是**一个 site 没 match 会牵动整体判断**。
（**推断**：原文只写了 `will be based on the compare results of all sites`，
**没有写「会互相影响」这几个字**。）

### `AUTO`：**默认值**，它自己去看 pin configuration

> 「Starting the sites successively affects the test negatively if the pin configuration contains at least one shared digital channel for triggering an analog module. The AUTO option checks if such a shared channel exists. If it does, the match site function is set to OFF; if not, it is set to ON. AUTO is the default.」

| pin configuration 里 | `AUTO` 落到 |
|---|---|
| **有至少一个**共用数字通道（用来触发模拟模块） | **`OFF`** |
| 没有 | **`ON`** |

**`AUTO` 是默认值**（`AUTO is the default.`）——所以**默认行为是「按 pin configuration 自动在两个值里选一个」**。
这也解释了为什么 `AUTO` 那一格比其余三格长得多：**它是唯一一格要解释判断逻辑的**。

**⚠️ `AUTO` 不在查询返回的取值表里。** `STME?` 的返回逐字是 `STME {ON|OFF|FAST),`（语法节；**注意那个 `)`**）——
**`AUTO` 不在其中**。（**推断**：查询回来的应当是**已经定下来的值**，不会回 `AUTO`；
依据是返回行的取值表 ＋ 原文那个例子（`STME AUTO,` 之后 `STME?` 回的是 `STME ON,`）。**原文没有正面写这句。**）

### `FAST`：7.4.0 新加的，**而且开完还得再补一条 `STME ON`**

> 「Activates the Fast Sync feature (local synchronization) of the test processor. After setting this option," STME ON" is required to turn on the site match function.」

（**逐字里引号的位置是 `option," STME ON" is required`**——逗号之后才起引号。**已核上游：上游如此**，见「出处」⚠️ ③。）

**两句各是一条**：① `FAST` 打开的是 **Fast Sync（test processor 的本地同步）**；
② **设了 `FAST` 之后还要再发一条 `STME ON`**，site match 才真的开着——**`FAST` 自己不开 site match**。

**上游那条 `title` 还给了 `Fast Sync` 的适用面**（**这句在本篇的 md 里没有**：它是 `Fast Sync`
那一篇（**本页没读**）的开头摘要，**本页是从上游 `98760.htm` 读到的**），逐字：
`Serial interfaces on many DUTs require non-deterministic handling. Normally they consist of a small number of pins (1, 2 or 4). Fast Sync enables the local synchronization of the test processor (TP). It enables up to 8 sync ports reacting independently on non-deterministic DUT responses per test processor.`
**即：Fast Sync 面向的是「响应不确定的串行接口」，每台 test processor 最多 8 个同步端口。**

### 查询：回「当前生效的设置」

> 「The query returns the active settings.」

例子里回的是 `STME ON,`（**结尾那个逗号见「出处」⚠️ ②**）。

## 典型用法

**原文没有 `## Procedure` / `## Before you begin` / `## What to do next` 段。** 用法来自两个例子。

**1. 例子一：用 `AUTO` ＋ 查询反推 pin configuration**

```
> STME AUTO,
> STME?
< STME ON,
```

> 「This example sets the site match function to AUTO, then reads the actual setting. Since the actual setting is ON, the pin configuration cannot contain a shared digital channel.」

**原文最后那句 `Since the actual setting is ON, the pin configuration cannot contain a shared digital channel.`
本身就是一条用法**：**查询回 `ON` → pin configuration 里没有共用数字通道；回 `OFF` → 有。**

**2. 例子二：配 Fast Sync**

```
>SQST OFF
>NIFE 2
>STME FAST,
>STME ON,
```

> 「This example configures the Fast Sync feature, and sets two independent Fast Sync ports on each test processor.」

**四行里只有后两行是 `STME`**：`STME FAST,` 开本地同步 → `STME ON,` 才真的开 site match
（正好用上 `FAST` 那格的第二句）。**前两行是别的命令，原文没有解释它们**：

| 行 | 命令 | 本篇写了什么 |
|---|---|---|
| `SQST OFF` | [[sqst]] 那一页的命令（`SeQuencer STate`） | **一个字没写**——**为什么 Fast Sync 之前要关 sequencer，本篇没有** |
| `NIFE 2` | `NIFE`（`Number of Independent Fast Error`，**未建、不在 allowlist 里**） | 只在解释句里以「两个独立 Fast Sync 端口」的形式出现 |

**⚠️ 解释句与命令的对应不是逐字的**：解释句说 `sets two independent Fast Sync ports on each test processor`，
而命令里那个 `2` **本篇没有明写就是「端口数」**。（**推断**：依据是 `NIFE` 的名字里有 `Number of`，以及解释句里那个 `two`。
**已核上游 `98760.htm`：`NIFE` 那个链接的 `title` 属性写的是**（**这句是 `NIFE` 那一篇的开头摘要，本篇 md 里没有**）
`The NIFE command defines the number of independent error propagations.`
——**它说的是 `error propagations`，不是 `Fast Sync ports`**。**本页不替它把两者画等号。**）

**3. 顺序上的两条**：
- **`FAST` 之后要补一条 `STME ON`**（`## Parameters` 明写）。
- **不设就是 `AUTO`**（默认值）。

**4. 出错**：原文 `## Errors` 全文一句 —— `An error is generated if the argument is invalid.`
（**这一条没进本页的「报错条件」节**，原因见「出处」⚠️ ⑤。）

**5. 归属**：原文 `## Application` 全文一句 —— `Multisite testing`。

## 和谁有关

- [[pin]] — `stage: pin` 的落点：它读的是 **pin configuration** 里有没有共用数字通道。
- [[match-loops]] — **`ON` 是为它**：`The ON option is required for evaluation of match loops per site in a multisite test`。
  **本页没读 [[match-loops]]**；那一页的标题在 allowlist 里所以链得上，
  **但 match loop 的机制本页一个字没有**。
- [[sqst]] — 例子二的第一行是它。**本页没读 [[sqst]]**；**本篇也没说为什么要先 `SQST OFF`**——
  两者在本页只是**同一个例子里的邻居**，**不是原文明说的关系**。
- [[pact]] — **同章的另一条多 site 命令，管的是另一件事**：`PACT` 管「哪个 site 出结果」，`STME` 管「各 site 怎么起」。
  **两条都在 `02.06.03.01.01_Introduction` 同一行的 `Commands for multi-site setups:` 串里**（见「出处」）。
- [[controlling-multiple-sites]] — **多 site 的上位概念页**。**本页没读**；`STME` 在那一页里怎么讲，本页不知道。
- [[smartest-7.4.0]] — **`FAST` 的版本落点**（见下）。
- `Fast Sync` / `How to use Fast Sync` / `NIFE`（**均未建、不在 allowlist 里**）——
  原文 `## Related information` 的三条 ＋ 例子二里的那条。**三篇本页都没读**；
  本页关于 Fast Sync 的两句都来自上游链接的 `title`（**md 里搜不到**，见「是什么」）。
- `Controlling the site match function`（**未建、不在 allowlist 里**）—— `OFF` 那句 `For details see` 指向它，
  也是「`Site Match` test suite flag」那条的来处。**没读。**

## 版本

`## Functional changes` 段有，**两条**，逐字：

```
- Introduced before SmarTest 6.3.2
- SmarTest 7.4.0: New option FAST.
```

**两条的性质完全不同**：

- 第一条是 **§11.2 ② 的哨兵值**（`before`）——**`STME` 本身成立于哪个版本，语料里没有。**
- 第二条是**真版本号**：**`FAST` 是 SmarTest 7.4.0 新增的选项**。
  **即 7.4.0 之前的机器上没有 `STME FAST`。**
- （**推断**）**`ON` / `OFF` / `AUTO` 都早于 7.4.0**：依据是版本段**只**为 `FAST` 记了一条新增，
  其余三个选项没有任何版本记录。**原文没有正面这么写。**

**本 wiki 面向 SmarTest 7.10.3**（[[smartest-7.10.3]]）：**`FAST` 在 7.10.3 上有**（本篇的取值表与例子都写着），
但这是**文档事实**，不是「这台机器上一定能用」（§11）。

## 出处

`sources:` 一篇：
`02_System_reference/02.06_Command_Reference/02.06.02.02.250_STME__STME__-__SiTe_Match_Enable.md`
（TDC `98760.htm`，**2,940 字节 / 107 行**）。**整篇读完**——本页引文全部来自这一篇 ＋ `edges.jsonl` 里带原句的边。

**入边 11 条 / 10 篇**（`inline` + `toc` 口径，`edges.jsonl` 原始行数）。
**其中 `SQSL`（`SeQuencer_Start_Label`）那两篇是同一条命令的两个投放副本**，引用句逐字相同。

**四条实质入边，逐条**（**都来自 `edges.jsonl` 里带原句的边；那几篇本页一篇都没读**）：

- `How_to_use_Fast_Sync`，逐字：`In the test method, use the STME FAST firmware command to enable the Fast Sync feature.`
  —— **`FAST` 的用法在本篇之外还有一处记载，而且那一处的措辞是 `firmware command`。**
- `SQSL`（两份，逐字相同）：
  `The synchronous or asynchronous start of different sites for the same pin is controlled with the site match function. For details see the STME command.`
  —— **它把 site match 说成「同一个 pin 在不同 site 上同步还是异步起」**，**这是本篇没有的一句。**
- `03_Use_cases_and_application_papers/03.08`（用例文档），逐字：
  `"Site match" is an optional feature whereby each site is independent. Without site match, every site will "move together". It is activated via suite flags or the STME firmware command.`
  —— **两个本页没有的点**：① site match 是**可选功能**；② **除了 `STME`，suite flags 也能开它**
  （与上游那条 `title` 里的 `Site Match test suite flag` 对得上）。
- `NIFE` / `Fast_Sync` 两条是 `## Related information` 的成对链接，**没有句子**。

**本页没做的**：

- **`Match loops` / `Fast Sync` / `How to use Fast Sync` / `NIFE` / `SQST` / `Controlling the site match function` 六篇一篇都没读** ——
  所以「match loop 怎么按 site 判」「Fast Sync 怎么配」「`Site Match` flag 在 test suite 的哪一处」本页都没有。
  本页关于 Fast Sync 的两句（`small offset`、`up to 8 sync ports`）**来自上游 htm 里链接的 `title` 属性**
  ——它们其实是那几篇（`Controlling the site match function`、`Fast Sync`）的开头摘要，**本篇的 md 里没有**。
- **`Controlling_the_site_match_function.md` 只核了一句**（为了定位 `if it set to ON` 那处错，见 ⚠️ ⑧）；**整篇没读。**
- **`with a slight delay` 里那个 delay 具体多少、由谁定：本篇没写。** 上游 `title` 只说是 `a small offset`，**也没给数**。
- **图：本篇没有内嵌图片**——判据可核：本篇 md 里 `.png` / `![` **0 命中**。
- **编码坏字：本篇 0 处**（`[一-鿿]` 扫过整篇，一个汉字都没有）；
  **整词替换（`DC/DC power units`）本篇 0 命中**。两条都是实测结果，不是没查。
- **没有实跑。** 没有发过 `STME`，没有配过 Fast Sync。`verified: doc-only` 说的就是这件事。
- **没有动 `wiki/index.md`。**

> ⚠️ **本篇的语料瑕疵，照实记、一处都没替它改**（§11.2）：
>
> **① `STME?` 的返回行括号不配对。** 逐字：`STME {ON|OFF|FAST),` —— **`{` 配的是 `)`**。
> **已核上游 `98760.htm`：上游逐字就是 `{ON|OFF|FAST),`**——**上游就坏的，不是 md 转换丢的。**
>
> **② 命令语法行与例子的命令行都带一个多余的尾逗号。** 语法逐字 `STME {ON|OFF|AUTO|FAST},`；
> 例子里逐字 `> STME AUTO,` / `> STME FAST,` / `> STME ON,` / `< STME ON,`。
> **已核上游：语法行的尾逗号在上游 `<pre>` 里就有。**（`STME` 本来没有参数，**这个逗号没有句法作用**。）
>
> **③ `FAST` 那一格的引号位置坏了。** 逐字：
> `After setting this option," STME ON" is required to turn on the site match function.`
> ——**逗号在引号前面**，引号本该包住 `STME ON`。
> **已核上游 `98760.htm`：上游此处逐字是 `After setting this option," STME ON" is required to turn on`——上游如此。**
>
> **④ `For if all sites are started simultaneously` —— `For` 后面直接接 `if`。**
> **已核上游 `98760.htm`：上游逐字就是 `For if all sites are started simultaneously`**——**上游如此。**
> 读起来像漏了一个词，**本页照原样引，不替它补。**
>
> **⑤ `## Errors` 那一句没进「报错条件」节。** 它逐字是 `An error is generated if the argument is invalid.`，
> **49 字符**；脚本只收 ≥ 60 字符的 `## Errors` / `## Warnings` 段。**内容本页写进「典型用法」了。**
>
> **⑥ 例子二里的提示符写法不一致。** **前两行 `>` 后没有空格**（逐字 `>SQST OFF` 与 `>NIFE 2`），
> **后两行有**（逐字 `>STME FAST,` 与 `>STME ON,`）。**已核上游：上游就是这两种写法**——上游如此。
>
> **⑦ `## Related information` 三条链接粘在一起、中间没有分隔符。** 逐字：
> `[Fast Sync](<02.06.07.01.08.04.03.03_Fast_Sync.md>)[How to use Fast Sync](<02.06.07.01.08.04.03.03.01_How_to_use_Fast_Sync.md>)[NIFE, NIFE? - (Number of Independent Fast Error)](<02.06.02.02.167_NIFE__NIFE__-__Number_of_Independent_Fast_Error.md>)`
> ——**三个链接名首尾相接**（[[pslv]] / [[pssr]] 记的是同一族毛病）。
> **已核上游 `98760.htm`：上游是三个独立的链接块**——**粘在一起是 md 转换造成的。**
>
> **⑧ 上游 `title` 属性里有一处语法错**（**这句在本篇的 md 里没有**）：`Controlling the site match function` 那个链接的
> `title` 里逐字有 `If this flag is set to OFF, all sites are started simultaneously; if it set to ON, they are started successively.`
> ——**`if it set to ON` 应为 `if it is set to ON`**。**本页照原样引，不替它改。**
> **另核过一句**：这句话在同名那篇文档里（`02.06.03.01.10.04_Controlling_the_site_match_function.md`）**也逐字一样**，
> 所以它**不只是 `title` 属性里的错，文档正文里也这么写**（**本页只核了那一句，没有读那一篇**）。

`verified: doc-only`
