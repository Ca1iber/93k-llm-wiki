---
type: object
title: PSSL, PSSL? (Power Supply Safety Limits)
layer: L1
stage: pin
tags: [pin, dps, pmu, safety-limit, command, l1, dc-scale, xps256, uhc4t]
related: [pin, dfps, dfpn, pslv, dps128-dps64-cards, xps256-status-flags, dc-scale-uhc4t-card, dpspins-resources, command-reference, smartest-7.2.1]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.196_PSSL__PSSL___Power_Supply_Safety_Limits.md
created: 2026-09-24
updated: 2026-09-28
verified: doc-only
---

# PSSL, PSSL? (Power Supply Safety Limits)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **776 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.196_PSSL__PSSL___Power_Supply_Safety_Limits.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### PSSL

```
PSSL [min_voltage | OFF], [max_voltage | OFF], [max_source_current | OFF], [max_sink_current | OFF], {(pin_list)}
```

### Parameters

|

min_voltage

 |

Lowest allowed voltage in V. Must be 鈮?0.

 |
 |

max_voltage

 |

Highest allowed voltage in V. Must be 鈮?0.

 |
 |

max_source_current

 |

Highest allowed source current in A. Must be > 0.

 |
 |

max_sink_current

 |

Highest allowed sink current in A. Must be > 0.

 |
 |

pin_list

 |

Comma separated list of DPS power pins, previously defined by the `DFPS`（raw: `02.06.02.02.65_DFPS__DFPS__-__DeFine_Power_Supply.md`） command, and of DC signal (PMU) pins defined by the `DFPN`（raw: `02.06.02.02.63_DFPN__DFPN__-__DeFine_Pin_Name.md`） command.

 |

### Example

```
PSSL OFF,OFF,OFF,OFF,(DPS_1)
PSSL -2,5,0.5,0.5,(DPS_2)
PSSL -1.5,3,0.5,0.5,(SIG_1A)
```

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.196_PSSL__PSSL___Power_Supply_Safety_Limits.md>` 的 `## Warnings` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Warnings

The firmware displays an error message when the safety limits specified by PSSL are exceeded by other firmware commands (for example `PSLV`（raw: `02.06.02.02.195_PSLV__PSLV__-__Power_Supply_LeVel.md`）).

<!-- 报错节 end -->

## 是什么

**`PSSL`（Power Supply Safety Limits）给电源针设一圈安全限值——越界时它自己不报错，是别的命令撞上来才报。**

> The PSSL command allows to set safety limits for the force voltage and for both current clamps of DPS power pins and of DC signal (PMU) pins. The default setting of all limit values is OFF.

**拆开读：**

| 原文 | 意思 |
|---|---|
| `for the force voltage and for both current clamps` | 管**力电压**与**两个电流钳位**（source / sink 各一）——**共四个量** |
| `of DPS power pins and of DC signal (PMU) pins` | **两类针都管**：DPS 电源针 **与** DC signal（PMU）针 |
| `The default setting of all limit values is OFF.` | **四个限值默认都是 `OFF`**——即**默认不设限** |

### 两道检查：软件一道，硬件一道（后者分卡）

> In the first place, the PSSL command implements a software check. For newer DC Scale DPS cards this is additionally accompanied by a hardware settings check, which provides additional safety for the unlikely case of a software bug violating the software limits. This capability is supported by the DPS128/DPS64 series, the XPS256, and the UHC4T card.

| 层 | 谁有 | 干什么 |
|---|---|---|
| **软件检查** | **所有**（原文：`In the first place`） | 固件里的软件限值检查 |
| **硬件设置检查** | **`DPS128/DPS64 series` / `XPS256` / `UHC4T card`** 这三种较新的 DC Scale DPS 卡 | **额外**一道——原文给的理由是 `for the unlikely case of a software bug violating the software limits` |

**这条分界线是本页最要紧的一条**：**不是每张卡都有第二道**。
三种卡在 wiki 里都有页：[[dps128-dps64-cards]]、[[xps256-status-flags]]、[[dc-scale-uhc4t-card]]。

### 四个限值，以及它们各自的约束

| 参数 | 原文定义（逐字） | 约束（**md 逐字**） |
|---|---|---|
| `min_voltage` | `Lowest allowed voltage in V.` | `Must be 鈮?0.` |
| `max_voltage` | `Highest allowed voltage in V.` | `Must be 鈮?0.` |
| `max_source_current` | `Highest allowed source current in A.` | `Must be > 0.` |
| `max_sink_current` | `Highest allowed sink current in A.` | `Must be > 0.` |

**⚠️ 上面两个电压格里的 `鈮` 是坏字，而它把两个本来不同的符号压成了同一个。**
上游 `.htm` 逐字是 **`Must be ≤ 0.`**（`min_voltage`）与 **`Must be ≥ 0.`**（`max_voltage`）——
**一个是 `≤`、一个是 `≥`**。`鈮` 是 GBK 误读留下的两字节残骸，只能给出区间
（`extract/encoding-map.csv` 记它落在 **U+2240–U+227F**），**单看 md 判不出是哪一个**；
是上游 `.htm` 把它定下来的（**核法与结论见「出处」**）。
**本页一个字都没动那一节**（它在「语法 / 参数」节里，按 §4 不许改），只在旁边记下正字。

**读法**：`min_voltage` 只能 ≤ 0（最低允许电压得落在 0 或负的一侧），`max_voltage` 只能 ≥ 0——
**两个约束是围着 0 张开的**，**不重合**。
（推断，依据是上面两条约束 + 例题本身）因此例子里的 `PSSL -2,5,…` 与 `PSSL -1.5,3,…` 都合法：
第一个数 ≤ 0、第二个数 ≥ 0。

### `pin_list`：两类针，而且必须**先定义过**

> Comma separated list of DPS power pins, previously defined by the DFPS command, and of DC signal (PMU) pins defined by the DFPN command.

**`previously defined by` 是本页唯一一条「先后顺序」**：
`pin_list` 里的针**必须已经**被 [[dfps]] 或 [[dfpn]] 定义过。

### 越界时是谁在报——看 `## Warnings` 那一节

> The firmware displays an error message when the safety limits specified by PSSL are exceeded by other firmware commands (for example PSLV).

**主语不是 `PSSL`**：是**别的固件命令**（原文举的例子是 [[pslv]]）越了 `PSSL` 设的界，
**由固件弹一条错误信息**。**所以本页没有 `## Errors` 段**——
上「报错条件」那一节取的是本篇的 `## Warnings` 段（脚本按段名取的）。

### `PSSL?`：问回当前限值

`PSSL?` 的形态是 `PSSL? {(pin_list)}`，返回

```
PSSL [min_voltage | OFF], [max_voltage | OFF], [max_source_current | OFF], [max_sink_current | OFF], {(pin_list)}
```

**这两行本页的「语法 / 参数」节里没有**——**不是本篇没有**，是脚本侧的已知盲区（**根因本页核过，见「出处」**）。
**这不是页面的缺陷，也不是语料的缺陷**，本页照实记。

## 典型用法

**先把范围说清：本篇没有 `## Procedure`、没有 `## Before you begin`。**
过程材料只有三处：`## Application` 一行、`pin_list` 的 `previously defined by`、以及 `## Example` 的三行。

**1. 归属**：`## Application` 逐字是 `Pin configuration, see Pin configuration setup commands.`
——**它是 pin 配置那一类命令**。

**2. 顺序**：[[dfpn]] / [[dfps]] **先定义针，`PSSL` 后设限**——
依据是 `pin_list` 那句里的 `previously defined by` 与 `defined by`。

**3. 三种典型设置**（原文 `## Example` 段，脚本已整段收进上「语法 / 参数」节）：

| 例子行 | 对象 | 读法 |
|---|---|---|
| `PSSL OFF,OFF,OFF,OFF,(DPS_1)` | 一个 DPS 电源针 | **四个限值全关**——这就是「不设限」的写法 |
| `PSSL -2,5,0.5,0.5,(DPS_2)` | 另一个 DPS 电源针 | 电压 −2…+5 V，source / sink 各 0.5 A |
| `PSSL -1.5,3,0.5,0.5,(SIG_1A)` | **一个 DC signal（PMU）针** | 同样四个量，**对象换成了 PMU 针** |

**第三行是本页最该记住的一行**：`PSSL` **不是 DPS 专用**——
PMU 针一样可以设，原文首句就写了 `and of DC signal (PMU) pins`。

**4. 一次只作用于一组针**：`pin_list` 是 `Comma separated list`，
所以**同一条 `PSSL` 只给一组针设一套限值**；要给两组不同的限值就发两条——**例题正好是三条**。

**5. 报错边界**：**`PSSL` 自己不会报错**（没有 `## Errors` 段）；
越界是**别的命令**撞上来的那一刻弹消息。细节照上「报错条件」一节，本页不复述。

**6. 查询**：`PSSL? {(pin_list)}` 按针问回当前四个值（形态见上「是什么」）。
**原文没有给 `PSSL?` 的例子**——所以输出长什么样本页给不出。

## 和谁有关

| 页 | 是什么关系 | 依据 |
|---|---|---|
| [[pin]] | **本页 `stage: pin` 的理由**：`## Application` 把它归到 pin configuration | frontmatter + 本篇 `## Application` |
| [[dfps]] | **前置**：DPS power pin **必须先用它定义过**，才能出现在 `pin_list` 里 | 本篇参数节（**文档事实**） |
| [[dfpn]] | **前置**：DC signal（PMU）pin 同理 | 本篇参数节（**文档事实**） |
| [[pslv]] | **原文 `## Warnings` 点名的那个例子**：`PSLV` 越界时固件弹错误信息 | 本篇 `## Warnings`（**文档事实**） |
| [[dps128-dps64-cards]] | **有硬件设置检查的三者之一**（原文：`the DPS128/DPS64 series`） | 本篇正文（**文档事实**） |
| [[xps256-status-flags]] | **同上**（原文：`the XPS256`）。那页讲的是**这张卡自己的保护标志**，与本页的「安全限值」是同一台硬件上的两层保护——**一层的界由本页设、另一层的标志由它报** | 本篇正文（**文档事实**）+ 该页定位 |
| [[dc-scale-uhc4t-card]] | **同上**（原文：`the UHC4T card`） | 本篇正文（**文档事实**） |
| [[dpspins-resources]] | **本篇 `## Related information` 列的四篇之一**（逐字是 `DPSPINS resources`） | 本篇 `## Related information`（**文档事实**） |
| [[command-reference]] | **本篇定义文档所在的章**（`02.06_Command_Reference`）。这一章**不逐篇建页**（§12.1） | §12.1 + 本页 `sources:` 的路径（**项目约定**） |
| [[smartest-7.2.1]] | **本页是「新增命令」**——见下节 | 本篇 `## Functional changes`（**文档事实**） |
| `DPSPINS` / `Pin configuration setup commands`（**前者未建页、后者是章**） | **`## Related information` 列的另外两个名字**，以及 `## Application` 指向的那一章 | 本篇（**文档事实**）；**两处本页都没读** |
| `DFPN` / `UDEF` / `DFPS` / `UDPS`（原文那一行里的同组命令） | **同属「DC Scale pins 的命令」这一组**（`UDEF` / `UDPS` 无页；`DFPS` 本页已列） | **对外核对**：`02.06.03_Pin_configuration_setup_commands.md` 第 20 行（本页只 `grep` 了这一行与同篇第 41 行，见「出处」） |

**入边只有 4 条**（来源 `extract/edges.jsonl`）：`02.06.02.02_List_of_commands.md` 与
`02_System_reference/index.md` 各 1 条（都是清单 / 索引），
以及 `02.06.03.01.01_Introduction.md` 与 `02.06.03_Pin_configuration_setup_commands.md` 各 1 条
——**后两条的链接文本都是 `PSSL`，都出现在「DC Scale pins 的命令」那一句里**。
**本页没有读那两篇**，用的是「对外核对」那一行的逐字依据。

## 版本

**本文档有 `## Functional changes` 段，只有一行**：

- `Introduced in SmarTest 7.2.1`

**这一条是真的版本门槛，不是 §11.2② 那个哨兵值**：措辞是 `in`，不是 `before`。
**`PSSL` 是 SmarTest 7.2.1 新增的命令**，**7.2.1 之前的版本上没有它**。版本页见 [[smartest-7.2.1]]。

**佐证（本页核过）**：`Pin configuration setup commands` 那一章的 `## Functional changes` 里有一条
逐字为 `- SmarTest 7.2.1: New command: PSSL`——**两处对得上**（见「出处」的「对外核对」）。

**版本段里没有的东西**：**没有一条 `SmarTest 7.2.2` 之后的变更记录**。
所以「硬件设置检查是哪一版加进来的」「`UHC4T` 是哪一版进的支持列表的」**本篇查不到——语料未写**。

## 出处

`sources:` 一篇：
`02_System_reference/02.06_Command_Reference/02.06.02.02.196_PSSL__PSSL___Power_Supply_Safety_Limits.md`
（TDC `143177.htm`）。**整篇读完。**

### 数是怎么量的（§11.5 的口径）

| 数 | 值 | 怎么量的 |
|---|---|---|
| 字节 | **2,654** | `len(path.read_bytes())`（即 `st_size`）。**不是** `len(read_text())` |
| 行数 | **100** | `wc -l`（**不 +1**；本语料末行都带换行） |
| 换行 | **100 个全 CRLF、裸 LF 0 个** | 所以 `len(read_text())` 会给出 **2,550**（**恰好少 100 = 行数**）——本页不拿 2,550 当字节数 |
| 代码块 | **4** | `docs.jsonl` 的 `code_blocks` |
| 标题 | **9**（1 个 H1 + 8 个 H2） | `docs.jsonl` 的 `heading_count` |
| 出边 | **8** | `docs.jsonl` 的 `out_degree: 8`、`link_kinds: {"doc": 8}`——`DFPS`、`DFPN`、`Pin configuration setup commands`、`PSLV`、`Related information` 那四篇各算上 |

### 这一篇在语料里有 2 份投放（本页核过）

| 路径（相对 `by-category/` 的尾巴） | `source_topic` | `st_size` |
|---|---|---|
| **`…/02.06_Command_Reference/02.06.02.02.196_PSSL__PSSL___Power_Supply_Safety_Limits.md`（本页 source）** | **`143177.htm`** | **2,654** |
| `…/02.06_Command_Reference/02.06.03.02.21_PSSL__PSSL___Power_Supply_Safety_Limits.md` | `143177_2.htm` | 2,655 |

**两份剥掉 frontmatter 之后逐字节相同**（body 都是 **2,447** 字节，
`sha256` 前 16 位同为 `890db32b93b2c988`）。判据是 §10 第 0 条。
**本页只把 `02.06.02.02.196` 当来源**，另一份只做了哈希核对，**没有当成证据读**。

### 上游 `.htm` 核过：**这一页的坏字，上游是好的——可救**

`raw/143177.htm` 与 `143177_2.htm` **都存在，各 7,130 字节**，**两份逐字节同长**。
把 `.htm` 与 md 都拆成词、取集合差：**只出现在 `.htm` 里的只有 `Topic` 与 `143177` 两个词**，
**只出现在 md 里的只有链接路径的字面**——**正文没有第三处差异**。

**所以内容没丢，但有一个字节级的坏点，而上游把它定死了**：

| md 逐字 | 上游 `.htm` 逐字 |
|---|---|
| `Lowest allowed voltage in V. Must be 鈮?0.` | `Lowest allowed voltage in V. Must be ≤ 0.` |
| `Highest allowed voltage in V. Must be 鈮?0.` | `Highest allowed voltage in V. Must be ≥ 0.` |

**这是 §11.2 ① 那一类（转换损坏），不是 ⑤⑥ 那一类（上游就坏）**——
判据就是 §11.2 ⑥ 那张表：**上游 `.htm` 里是干净的** → **将来重做一次正确编码的转换就能救回来**。
**md 把 `≤` 与 `≥` 压成了同一个 `鈮?`**，所以**只看 md 会以为 min 与 max 的约束一样**——
这是本页核 `.htm` 唯一真正的收获，**也是本页最该记住的一条**。

> ⚠️ 另记一处**只在 `.htm` 里有、md 里没有**的东西（**不是文字丢失，是属性被丢了**）：
> md 的 `## Related information` 那一行是**四个链接连排、中间没有任何分隔符**，
> 而上游 HTML 里它们是四个并列的 `<div>`（**每篇独占一行**）；
> 更要紧的是，每个 `<a>` 带一个 **`title=` 属性**，里面正是那两篇文档的第一句话
> （逐字如 `The DFPS (DeFine Power Supply) command tells the software which DPS channel is connected to the specified device pin, and the polarity of the channel.`）——
> **`title=` 属性在 md 里整个不见了**。**本页把这一条记下来**：
> 要那两句说明，得回 `.htm`。**md 一个字符没丢**（丢的是属性与行结构），所以这不算瑕疵。

### 对外核对（本页唯一一处 `sources:` 之外的材料）

本页有一件事 `sources:` 那篇答不了：**`PSSL` 属于哪一组命令**（本篇 `## Application`
只把它指向一章，没有点出同组的其他命令），**以及「7.2.1 新增」能不能被别处印证**。
为此**只 `grep` 了同章一份索引的两行**：

| 打开的是 | 读了什么 | 拿到什么 |
|---|---|---|
| `02_System_reference/02.06_Command_Reference/02.06.03_Pin_configuration_setup_commands.md`（3,305 字节，41 行） | **只 `grep` 了含 `PSSL` 的两行**（第 20 行、第 41 行） | **第 20 行**逐字：`Commands for DC Scale pins: [DFPN](<…>), [UDEF](<…>), [DFPS](<…>), [UDPS](<…>), [PSSL](<…>)` → **`PSSL` 属于「DC Scale pins 的命令」这一组**<br>**第 41 行**逐字：`- SmarTest 7.2.1: New command: PSSL` → **与本篇 `## Functional changes` 对得上** |

**这一份是章首页**（41 行，主体就是几张命令清单），**本页只取了上面那两行**，
**它的正文内容没有进本页**。处置与 `wiki/objects/eqsp.md` 的「对外核对」一节同一套。

### ⚠️ 本篇的四处瑕疵，本页照实记下、一处都没替它改

> **① 参数表里 `min_voltage` 与 `max_voltage` 的约束被压成了同一个坏字串。**
> md 两处逐字都是 `Must be 鈮?0.`；上游 `.htm` 是 `≤ 0` 与 `≥ 0`（**正字见上**）。
> **照实转录**：本页正文**原样保留 `鈮?0.`**，没有替语料改字（§11.2 ①的处置）。
> **代价写清楚**：拿 `≤` 或 `≥` 去 raw 里搜是搜不到的，要搜坏掉的形态 `鈮?0`。

> **② `The PSSL command allows to set safety limits`——`allows to set` 不是英语。**
> 上游 `.htm` 逐字相同，所以**是上游的错**，救不回来。本页引用时**原样抄**。

> **③ `## Warnings` 段里写的是「error message」。**
> 段名是 `Warnings`，正文却是 `The firmware displays an error message…`——
> **段名与内容的口径不一致**（上游如此）。本页照实并列，不替它改段名，
> 也不据此推断「它到底算 warning 还是 error」。

> **④ 标题头缺一个分隔符，而这件事有下游后果。**
> 本篇的标题头逐字是 `PSSL, PSSL? (Power Supply Safety Limits)`；
> **同章兄弟命令页的写法都带 ` - `**（本篇同一批的 `EDSP, EDSP? - (EDge SPecification)`、
> `LSUX, LSUX? - (Level Sets Used eXtended)`、`LSUS, LSUS? - (Level Sets USed)`、`RSET - (ReSET)` 都有）。
> **缺这个 ` - ` 的后果本页核过、也实测过**：脚本抽「以命令名命名的语法段」时，
> 只取标题头**` - ` 之前那截**再按逗号拆（`extract/objpack.py` 的 `title_aliases`）；
> 本篇没有 ` - `，于是第二个名字连解释一起成了
> `PSSL? (Power Supply Safety Limits)`（**34 字符**），**超过 `CMD_NAME_MAX = 24` 被静默丢掉**——
> **实测三个别名是 `['pssl']`，而 `EDSP` / `LSUX` / `LSUS` 都是两个（带 `?` 的那个）。**
> **所以「语法 / 参数」节缺的是 `## PSSL?` 那一节**（见上「是什么」）。
> **这是脚本侧已知盲区家族的另一个形状**——`extract/findings-scaffold-syntax.md`
> 把这一族记成「认不出描述性标题 / 段名笔误 / 空标题 / 标题只给一套形态」几种，
> **本篇属于「给了两套形态、但第二个名字因超长被丢」，与那几种都不同**。
> **本页一个字都没往那一节加**（§4）。

`verified: doc-only`
