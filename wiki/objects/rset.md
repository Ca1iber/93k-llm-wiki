---
type: object
title: RSET - (ReSET)
layer: L1
stage: level
tags: [level, timing, command, l1, power-on-defaults, reset, uhc4t, test-program-explorer]
related: [level, timing, test-program-explorer, dc-scale-uhc4t-card, xps256-status-flags, command-reference, smartest-6.3.2, smartest-7.0.3]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.210_RSET_-__ReSET.md
created: 2026-09-24
updated: 2026-09-28
verified: doc-only
---

# RSET - (ReSET)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **2,341 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.210_RSET_-__ReSET.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
RSET {specifier}
```

### Parameters

| specifier | The specifier can be: | The specifier can be: |
|---|---|---|
| specifier | DPS | Loads the default power supply setup for standard DPSs. |
| specifier | FCR | Loads the default clock routing. |
| specifier | LEV | Loads the default power supply setup for standard DPSs.<br><br>Level: 0 V<br><br>Current: 50 mA<br><br>Off state: minimum current<br><br>Setup time: 0 ms<br><br>This default states are:<br><br>UHC4T<br><br>- Connect state: normal<br>- Level: 0 V<br>- Range: 4 V<br>- Clamp: 4 A<br>- Clamp-Range: 40 A<br>- Disconnect state: HIZ<br>- Voltage drop force: 250 mV<br>- Voltage drop return: 250 mV<br>- Clamp mode: limit (see `UHCM`（raw: `02.06.02.02.303_UHCM__UHCM__-__Ultra_High_Current_power_supply_Modes.md`）)<br>- DUT capacitor mode: off<br><br>Fast preload: 0 ms |
| specifier | TIM | Loads the default timing setup. The settings are:<br><br>Timing Sets<br><br>- Defined Timing Sets: 1<br>- Allowed Timing Sets: 256<br><br>Waveform Sets<br><br>- Defined Waveform Sets: 1<br>- Allowed Waveform Sets: 16<br><br>Waveforms: not defined<br><br>Breakwaveform: defined<br><br>Events<br><br>- Action: NOP<br>- Timing: 0 ns<br><br>Min Period: 4 ns<br><br>- This is dependent on the test system hardware configuration.<br><br>Device Cycles: not defined<br><br>Default Device Cycle: "" |
| specifier | VEC | Loads the default vector setup. The Vector Memory contains:<br><br>No vectors<br><br>No tests (and therefore no labels)<br><br>No comments<br><br>No sequencer programs (no instructions) |
| specifier | ATR | Loads the default edge attributes.<br><br>Pin attribute: set to 0 |
| specifier | PDL | Loads the default path delay attributes.<br><br>Cable assembly delay attribute: set to 0<br><br>Fixture delay attribute: set to 0<br><br>System attribute: set to 0 |
| specifier | CAL | Loads the default calibration data.<br><br>Level calibration data<br><br>Timing calibration data |
| specifier | MTPP | Resets memory test and per-pin sequencer subroutine data. |

> ⚠️ 转录说明（非原文）：本表在上游 HTML 里含合并格（colspan / rowspan）；
> 跨格文字已按覆盖范围重复写出（**不是原表里有重复的格子**）。真结构见 `tdc-html/raw/98723.htm`。

### Example

```
RSET TIM
```

This example resets all waveform sets and timing sets and loads the hardware with the default vector rate and edge placement values. Only waveform set 1 and timing set 1 in waveform set 1 is active.

<!-- 语法节 end -->

## 是什么

**`RSET`（ReSET）是一条「把硬件载回上电默认值」的命令——它只问你一件事：哪一类文件。**

> The RSET (ReSET) command loads the hardware with the power-on defaults of the specified type of file.

**三个词各承载一件事：**

| 原文 | 意思 |
|---|---|
| `loads the hardware with` | **落点是硬件**——它是一次「载入」，不是查询 |
| `the power-on defaults` | 载的是**上电默认值**，不是你当前手上那份 setup |
| `of the specified type of file` | **换的是「哪一类」，由唯一的参数 `specifier` 决定** |

**`RSET` 没有查询形态。** 本篇的标题头只有 `RSET`（不像同批的 `EDSP` / `LSUS` / `LSUX` / `PSSL`
那样带 `?`），全篇 `RSET?` 出现 **0** 次。**「怎么读回当前设置」本篇没有一句——语料未写。**

### 九个 `specifier`，九种「被拨回上电那一刻的东西」

依据全在上「语法 / 参数」节的参数表里；下表只做归纳，**逐字值请回那一节**：

| `specifier` | 重置的是什么 | 里头的关键默认值 |
|---|---|---|
| `DPS` | 标准 DPS 的**电源 setup** | 原文只给一句 `Loads the default power supply setup for standard DPSs.`——**没有列值** |
| `FCR` | **时钟布线** | 原文只给一句 `Loads the default clock routing.` |
| `LEV` | **电平 setup** | `Level: 0 V` / `Current: 50 mA` / `Off state: minimum current` / `Setup time: 0 ms`，外加一整块 **`UHC4T`**（`Connect state: normal`、`Level: 0 V`、`Range: 4 V`、`Clamp: 4 A`、`Clamp-Range: 40 A`、`Disconnect state: HIZ`、`Voltage drop force: 250 mV`、`Voltage drop return: 250 mV`、`Clamp mode: limit`、`DUT capacitor mode: off`）与 `Fast preload: 0 ms` |
| `TIM` | **timing setup** | `Defined Timing Sets: 1` / `Allowed Timing Sets: 256` / `Defined Waveform Sets: 1` / `Allowed Waveform Sets: 16` / `Waveforms: not defined` / `Breakwaveform: defined` / `Events`（`Action: NOP`、`Timing: 0 ns`）/ `Min Period: 4 ns` / `Device Cycles: not defined` / `Default Device Cycle: ""` |
| `VEC` | **vector setup**（Vector Memory） | `No vectors` / `No tests (and therefore no labels)` / `No comments` / `No sequencer programs (no instructions)` |
| `ATR` | **edge attributes** | `Pin attribute: set to 0` |
| `PDL` | **path delay attributes** | `Cable assembly delay attribute: set to 0` / `Fixture delay attribute: set to 0` / `System attribute: set to 0` |
| `CAL` | **校准数据** | `Level calibration data` / `Timing calibration data` |
| `MTPP` | **memory test 与 per-pin sequencer 的 subroutine 数据** | `Resets memory test and per-pin sequencer subroutine data.` |

**三点从这张表能读出来的：**

1. **九个里只有 `LEV` / `TIM` / `VEC` 三个在原文里列了具体的默认值**；
   `DPS`、`FCR`、`ATR`、`PDL`、`CAL`、`MTPP` 各只有一句话。
2. **`MTPP` 与另外八个不是一类**：另外八个写的都是「载默认值」（`Loads …`），
   只有它写的是 `Resets memory test and per-pin sequencer subroutine data.`——**是「重置」，不是「载入」**。
3. **`Min Period: 4 ns` 有一条附注**：`- This is dependent on the test system hardware configuration.`
   ——**所以这个数不是固定值**；它是 `TIM` 那一段里唯一的附注。

### `LEV` 那一段的两处「对不上」

**第一处（上游就错的）**：`LEV` 的第一句逐字是

> Loads the default power supply setup for standard DPSs.

**它与 `DPS` 那一格逐字相同**——而 `LEV` 后面紧跟着列的全是**电平**的默认值
（`Level: 0 V` / `Current: 50 mA` / `Off state: minimum current` / `Setup time: 0 ms` / `UHC4T` 那一整块）。
**上游 `.htm` 里就是这样**（核法见「出处」）。

**第二处（语法）**：`LEV` 那一格在列 `UHC4T` 默认值之前写着

> This default states are:

**`This` 应为 `These`。上游 `.htm` 里就是这样。**

### `## Application`：谁在调它

> Test Program Explorer.

**一句话，一个调用者**：[[test-program-explorer]]。
**这句话的信息量不小**：`RSET` **不是给人手敲的**，它是**测试程序浏览器**在做某类动作时发出来的。
（推断，依据是这一句 + `RSET` 载的是「上电默认值」这件事）**它落在「开一套新 setup 的起点」那个位置上。**
**但原文没有写「什么时候会发它」**——所以这一步是推断，不是文档事实。

## 典型用法

**先把范围说清：本篇没有 `## Procedure`、没有 `## Before you begin`、没有 `## What to do next`。**
能给的只有 `## Application` 一行、唯一一个例子、以及参数表里各 `specifier` 列出的默认值。

**1. 调用者**：`## Application` 逐字是 `Test Program Explorer.`——**由 [[test-program-explorer]] 调用**。

**2. 唯一的例子**在 `## Example` 段里（脚本已整段收进上「语法 / 参数」节，本页不重复抄）。
它的说明逐字是：

> This example resets all waveform sets and timing sets and loads the hardware with the default vector rate and edge placement values. Only waveform set 1 and timing set 1 in waveform set 1 is active.

**这句说明回答了一件参数表答不了的事**：`RSET TIM` **不只是**把 `TIM` 那几行默认值写回去，
它在同一刻还让 `Only waveform set 1 and timing set 1 in waveform set 1 is active`。
（推断，依据就是这一句说明）**所以它做的是「把这一类设置整体拨回上电那一刻」**，
而不是「往当前设置里补几条默认值」——**原文没有把这句话上升成一般规则，所以这里标推断。**

**3. 用法上的三个选择**：

| 你想干什么 | 发什么 | 依据 |
|---|---|---|
| 把 timing 那一套拨回上电默认 | `RSET TIM` | **原文唯一的例子** |
| 把电平那一套拨回上电默认 | `RSET LEV` | 参数表的 `LEV` 那一格（**原文没有例子**） |
| 把 DPS 电源那一套拨回上电默认 | `RSET DPS` | 参数表的 `DPS` 那一格（**原文没有例子**） |

**表里只有第一行有原文例子**，后两行是按参数表推的。

**4. 顺序：语料未写。** 发之前要不要先 disconnect？要不要在某个 site focus 下？
**本篇一个字没说。**

**5. 报错条件：本篇没有。** `RSET` 这一篇**没有 `## Errors` 段、也没有 `## Warnings` 段**
（这是事实：实测两个词在篇内各出现 **0** 次）——**所以本页没有「报错条件」那一节。**
**这不等于「`RSET` 不会失败」**，只能说**本篇没写失败条件**。

## 和谁有关

| 页 | 是什么关系 | 依据 |
|---|---|---|
| [[level]] | **本页 `stage: level` 的理由**。**但要看清楚**：`RSET` 管的不止 level——九个 `specifier` 里只有 `LEV` 一个是 level，另有 `TIM`（timing）、`VEC`（vector）、`CAL`（校准）等。**`stage` 填的只是「最近的一段」**（§6） | frontmatter + 本篇参数表 |
| [[timing]] | **`RSET TIM` 那一半的 stage**：`## Application` 没有分侧，但 `TIM` 这个 `specifier` 落在 timing 那一段 | 本篇参数表（**文档事实**） |
| [[test-program-explorer]] | **原文点名的唯一调用者**（`## Application` 逐字就是它）。**本页与它是「被调用 ↔ 调用」** | 本篇 `## Application`（**文档事实**） |
| [[dc-scale-uhc4t-card]] | **`LEV` 那一段里唯一被点名的卡**：`RSET LEV` 的默认值里有一整块 `UHC4T`（10 条） | 本篇参数表（**文档事实**） |
| [[command-reference]] | **本篇定义文档所在的章**（`02.06_Command_Reference`）。这一章**不逐篇建页**（§12.1） | §12.1 + 本页 `sources:` 的路径（**项目约定**） |
| [[smartest-6.3.2]] | **版本哨兵值**指向的版本页（见下节） | 本篇 `## Functional changes`（**文档事实**） |
| [[smartest-7.0.3]] | **本命令唯一一条真变更**所在的版本页（见下节） | 本篇 `## Functional changes`（**文档事实**） |
| `UHCM`（**未建页、也不在链名清单里**） | **`LEV` 那一段里 `Clamp mode: limit` 后面括号指的那一篇**（原文：`Clamp mode: limit (see UHCM)`）。**本页没读它** | 本篇参数表（**文档事实**） |
| `RST`（**未建页、也不在 `[[ ]]` 清单里**） | **最容易和本页混的那一条** | 见下 |

### ⚠️ 一条最容易混的：`RST` 不是本页

`extract/edges.jsonl` 里有两篇（`02.06.02.02.345_RST_-__ReSeT.md` 与 `02.06.05.02.28_RST_-__ReSeT.md`）
把 `RSET` 当链接目标。本页**只读了其中一篇的第一段**（**这是本页第二处、也是最后一处
`sources:` 之外的材料**，声明见「出处」），逐字是：

> The *RST (ReSeT) command resets the firmware and all calibration data. This causes power-up default values to be loaded in the hardware. For default values see the RSET command.

**分工就此定下**：`*RST` **重置固件与全部校准数据**（其后果之一是上电默认值被载进硬件），
而**「默认值具体是什么」要来看 `RSET`**——`*RST` 那一篇自己把读者指到本页。
**所以两篇不是别名，是「谁触发重置」与「谁定义默认值」的分工。**

## 版本

**本文档有 `## Functional changes` 段，里面是两行**：

- `Introduced before SmarTest 6.3.2`
- `SmarTest 7.0.3: Removed MTST parameter option`

**第一行是哨兵值，不是「6.3.2 新增了 RSET」。** 按 §11.2②，
`Introduced before SmarTest 6.3.2` 的意思是「**在本语料覆盖范围开始之前就已经有了**」——
语料里 2,677 条可用性行都写这同一个版本号，照字面读会读出一条假信息。
**所以这一行不带版本门槛**；哨兵值本身的说明在 [[smartest-6.3.2]]。

**第二行是真变更，而且它自带验证。** `SmarTest 7.0.3: Removed MTST parameter option`——
**`MTST` 这个 `specifier` 在现在的参数表里确实已经不在了**：
实测 `MTST` 在**全篇只出现 1 次**，就是这一行变更记录本身（参数表里没有它）。
**两处对得上**，所以这条变更记录是可信的。版本页见 [[smartest-7.0.3]]。

**版本段里没有的东西**：**`7.0.3` 之后没有一条变更记录**。
所以「`MTPP` 是哪个版本加的」「`CAL` 的默认数据是哪一版改成现在这样的」**本篇查不到——语料未写**。

（推断）`RSET` 在 **SmarTest 7.10.3** 上可用——依据是「它早于 6.3.2」这条文档事实，
加上 7.10.3 晚于 6.3.2；**本页没有在任何机台上印证过。**

## 出处

`sources:` 一篇：
`02_System_reference/02.06_Command_Reference/02.06.02.02.210_RSET_-__ReSET.md`
（TDC `98723.htm`）。**整篇读完。**

### 数是怎么量的（§11.5 的口径）

| 数 | 值 | 怎么量的 |
|---|---|---|
| 字节 | **2,589** | `len(path.read_bytes())`（即 `st_size`）。**不是** `len(read_text())` |
| 行数 | **196** | `wc -l`（**不 +1**；本语料末行都带换行） |
| 换行 | **196 个全 CRLF、裸 LF 0 个** | 所以 `len(read_text())` 会给出 **2,393**（**恰好少 196 = 行数**）——本页不拿 2,393 当字节数 |
| 代码块 | **2** | `docs.jsonl` 的 `code_blocks` |
| 标题 | **6**（1 个 H1 + 5 个 H2） | `docs.jsonl` 的 `heading_count` |
| 出边 | **1** | `docs.jsonl` 的 `out_degree: 1`、`link_kinds: {"doc": 1}`——**正文里只有一个链接**（`LEV` 那一段里的 `UHCM`） |

### 这一篇在语料里有 **5** 份投放（本页核过）

| 路径（相对 `by-category/` 的尾巴） | `source_topic` | `st_size` |
|---|---|---|
| **`…/02.06_Command_Reference/02.06.02.02.210_RSET_-__ReSET.md`（本页 source）** | **`98723.htm`** | **2,589** |
| `…/02.06_Command_Reference/02.06.05.02.19_RSET_-__ReSET.md` | `98723_2.htm` | 2,590 |
| `…/02.06_Command_Reference/02.06.06.02.23_RSET_-__ReSET.md` | `98723_3.htm` | 2,590 |
| `…/02.06_Command_Reference/02.06.07.02.22_RSET_-__ReSET.md` | `98723_4.htm` | 2,590 |
| `…/02.08_Setup_and_Result_Tools/02.08.04.34.02.02.23_RSET_-__ReSET.md` | `98723_5.htm` | 2,628 |

**前四份剥掉 frontmatter 之后逐字节相同**（body 都是 **2,435** 字节，
`sha256` 前 16 位同为 `1cb2bf837311d6de`）；**第五份不同（body 2,462 字节）**，
差的那 **27** 字节是**链接前缀**：镜像那一份把
`[UHCM](<02.06.02.02.303_UHCM__…>)` 写成了 `[UHCM](<../02.06_Command_Reference/02.06.02.02.303_UHCM__…>)`
（多一层 `../`），**正文一个字没差**。判据是 §10 第 0 条：`source_topic`
去掉 `_N` 后缀后相同 → 同一篇 TDC 页。

> **所以 `RSET` 这一篇被投放了 5 次，不是 5 处独立证据。**
> **本页只把 `02.06.02.02.210` 当来源**；其余四份只做了哈希与逐行对差，**没有当成证据读**。
> **5 份是本批四页里最多的**（`EDSP` 4 份、`LSUX` 2 份、`PSSL` 2 份）。

### 上游 `.htm` 核过：**逐字比对，内容一个字没丢**

`raw/98723.htm`、`98723_2.htm`、`98723_3.htm`、`98723_4.htm`、`98723_5.htm`
**五份都存在，各 6,313 字节**。把 `.htm` 与 md 都拆成词、取集合差，结果是：
**只出现在 `.htm` 里的只有 `Topic` 与 `98723` 两个词**（页面框架），
**只出现在 md 里的只有链接路径的字面**（`02`、`06`、`303_UHCM__UHCM__`、
`__Ultra_High_Current_power_supply_Modes`、`md` 这几段）。

**结论：这一篇 md 相对上游 `.htm` 没有内容丢失。** 所以下面记的三处瑕疵
**上游 `.htm` 里就是那样**——属于 §11.2 ⑥ 说的「**上游就坏的（救不回来）**」，
**不是** ① 那种转换损坏（本页**没有** ① 类的坏字：全篇没有出现 `鈥` / `鈮` / `碌` / `渭` / `卤` 这一族）。

**具体核到的那一处（`LEV` 那句）**：上游 `98723.htm` 里，
`LEV` 那一格的第一个 `<p>` 逐字就是 `Loads the default power supply setup for standard DPSs. `
——**与 `DPS` 那一格逐字相同**。所以「`LEV` 的第一句写成了 DPS 的话」是**上游的错**，
不是转换造成的，**本页不替它改**。

### 对外核对（本页 `sources:` 之外读了什么，为什么）

本页有一件事 `sources:` 那篇答不了：**`RSET` 与名字极近的 `*RST` 是不是同一条命令**
（这也是「最容易混」那一条的来处）。为此本页**只读了另一篇的第一段**：

| 打开的是 | 读了什么 | 拿到什么 |
|---|---|---|
| `02_System_reference/02.06_Command_Reference/02.06.02.02.345_RST_-__ReSeT.md`（**同一位投放还有 `02.06.05.02.28_RST_-__ReSeT.md`**） | **只读了正文第一段（第 8 行）一行** | 一行逐字：`The *RST (ReSeT) command resets the firmware and all calibration data. This causes power-up default values to be loaded in the hardware. For default values see the [RSET](<02.06.02.02.210_RSET_-__ReSET.md>) command.` → **分工：`*RST` 触发重置，默认值以 `RSET` 为准** |

**两篇 `RST` 文档的其余部分、以及 `RSET` 在别的章里的 4 份投放的上下文，本页都没有读。**
处置与 `wiki/objects/eqsp.md` 的「对外核对」一节同一套。

### 本页没做的

- **没有实跑。** 没在机台上发过 `RSET`，**没有验证过任何一个 `specifier` 载进去之后硬件真的变成那些值**。
  `verified: doc-only` 指的就是这件事。
- **`Test Program Explorer` 那一篇没读**——所以「它在哪个动作上发 `RSET`」本页只有 `## Application` 那一句。
- **`UHCM` 那一篇没读**——所以 `Clamp mode: limit` 里 `limit` 的语义本页给不出。
- **`DPS` / `FCR` / `ATR` / `PDL` / `CAL` 五个 `specifier` 只有一句话**——
  它们各自的默认值是什么，**本篇就没写，本页自然也写不出**。
- **`*RST` 那一篇只读了第一段**（见上）；**它自己有没有 `RSET` 没有的默认值，本页不知道**。
- **`MTST` 是什么**——本篇只说它被移除了，**没有一句解释它原本干什么**。
- **图**：本篇对 `raw/` 的引用 **0 处**（`.png` / `.jpg` / `.jpeg` / `.gif` / `![` / `<img` / `raw/`
  七种写法**全部 0 命中**）——**所以本页没有任何来自图的结论，没有图证。**
- **没有动 `wiki/index.md`**，也没有动任何别的页。

### ⚠️ 本篇的三处瑕疵，本页照实记下、一处都没替它改

> **① `LEV` 的第一句与 `DPS` 逐字相同，而它对 `LEV` 来说是错的。**
> 两格逐字都是 `Loads the default power supply setup for standard DPSs.`；
> 而 `LEV` 后面跟着的全是电平默认值（`Level: 0 V` / `Current: 50 mA` / `UHC4T` 那一块）。
> **上游 `raw/98723.htm` 里就是这样**——**救不回来，只能靠上下文反推**。
> **本页两处并列，不替它改，也不猜它「本来该」是哪一个词。**

> **② `This default states are:`——指示词与名词数不一致**（`This … states`）。
> 逐字如此，**上游 `.htm` 里也一样**。本页引用时**原样抄**，没有改成 `These`。

> **③ 例子说明句里的 `timing set 1 in waveform set 1` 读不通。**
> 逐字是 `Only waveform set 1 and timing set 1 in waveform set 1 is active.`
> ——**单数 `is` 配了两个主语，且 `timing set 1 in waveform set 1` 的所属关系拗口**。
> **上游 `.htm` 里就是这样**。本页照原样引。

另记一处**形态，不是瑕疵**：`## Parameters` 那一节把 9 个 `specifier` 与它们的说明
**压成了一串连续的段落行，层级关系在压平后看不出来**（`specifier` / `The specifier can be:` /
`DPS` / 它的说明 / `FCR` / 它的说明 …）。**这是语料的结构**（上游 HTML 里它们本来是同级的表格行），
同一种形态在 [[xps256-status-flags]] 的「语法 / 参数」节里也记过。
要按 `specifier` 读，**照名字去搜**。

`verified: doc-only`
