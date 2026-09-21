---
type: concept
title: Setting up DC Scale pins with SmartRDI
layer: n/a
stage: testmethod
tags: [smartrdi, dc-test, dc-scale, pmu, dps, test-method-api, rdi, code-based, pattern-based]
related: [smartrdi, dps-pins-editor, rdi-call-requires-begin-end-block, rdi-configure-file, dc-test-programming, xps256-pmu-operating-mode, xps256-programming-dps-operating-mode, dc-scale-xps256-card, dps128-dps64-cards, dc-scale-uhc4t-card, spmu-pin-task-mode, dc-scale-limits-editor]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02_Setting_up_DC_Scale_pins_with_SmartRDI.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# Setting up DC Scale pins with SmartRDI

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **804 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02_Setting_up_DC_Scale_pins_with_SmartRDI.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Examples

### PMU (SIG) operating mode

```
rdi.dc().pin("DCS_SIG").vForce(2 V).vForceRange(25 V).iForceRange(100 uA).execute();

RDI_BEGIN();

    rdi.dc().pin("DCS_SIG").iMeasRange(100 uA).execute();
    rdi.dc().pin("DCS_SIG").vForce(10 V).execute();
    rdi.dc().pin("DCS_SIG").iMeas().execute();
    rdi.dc().pin("DCS_SIG").vForce(8 V).execute();
    rdi.dc().pin("DCS_SIG").iMeas().execute();

RDI_END();

rdi.dc().pin("DCS_SIG").disconnect().execute();
```

### DPS operating mode

```
rdi.dc().pin("DCS_DPS").connect().execute();

RDI_BEGIN();

    rdi.dc().pin("DCS_DPS").vForce(10 V).execute();
    rdi.dc().pin("DCS_DPS").iMeas().execute();
    rdi.dc().pin("DCS_DPS").vForce(8 V).execute();
    rdi.dc().pin("DCS_DPS").iMeas().execute();

RDI_END();

rdi.dc().pin("DCS_DPS").disconnect().execute();
```

<!-- 语法节 end -->

## 是什么

**这是 SmartRDI 侧做 DC 测试的「怎么做」页：用 `rdi.dc()` 在 DC Scale 卡上做静态和动态 DC 测试。**
第一句就把范围钉死了：

> 「SmartRDI supports both static and dynamic DC tests with DC Scale cards. Both the PMU (SIG) operating mode and the DPS operating mode are supported.」

**两个「二选一」叠在一起，这是本页最容易配错的地方**：

| 维度 | 取值 | 在哪定 |
|---|---|---|
| **卡的工作模式** | **PMU (SIG)** / **DPS** | **pin 配置里定**（DPS 模式要在 [[dps-pins-editor]] 里配） |
| **测试是静态还是动态** | **code-based（静态）** / **pattern-based（动态）** | **你在测试方法里怎么写** |

**这两组不是一回事，不要混。** 第一组是**硬件通道怎么工作**，
第二组是**测量点落在哪里**（改电平 vs 在 pattern 里插测试点）。

### code-based 与 pattern-based 的差别，三条

| | **code-based（静态）** | **pattern-based（动态）** |
|---|---|---|
| 干什么（原文逐字） | `the level setting is changed` | `test points will be created in the pattern` |
| 能不能动继电器 | **能** | **不能** |
| 模式专属函数（原文给的清单，逐字） | `vForce()` / `iForce()` / `vMeas()` / `iMeas()` / `relay()` / `vForceRange()` / `iForceRange()` / `vMeasRange()` / `iMeasRange()` / `average()` / `clamp()` / `measWait()` / `connectSense()` / `ungang()` / `preCharge()` / `execute()` | `iForce()` / `vForce()` / `iMeas()` / `vMeas()` / `vForceRange()` / `iForceRange()` / `iMeasRange()` / `vMeasRange()` / `restoreRange()` / `average()` / `clamp()` / `measWait()` / `execute()` |

**一条顺序前置（§2.4 的 D1）**：

> 「Relays cannot be switched in the pattern鈥慴ased mode. So make sure the relay connection is programmed in the code鈥慴ased mode and is correct before the burst execution of the pattern鈥慴ased mode.」

**⚠️ 上面这一句引文里有 3 个坏字 `鈥慴`，是语料自带的，本页原样留着没改**
（它本来是 `‑b`，即 `-based`）。**理由与全篇的坏字清单见「出处」。**

**读法**：不是「建议先配」，是「**relays 在动态模式下根本不让切**」——
所以继电器的配置**只能在静态模式下做，而且必须在 burst 之前做对**。

**三处「只对某些卡」的限制，原文写在脚注里，正文清单看不出来**：

> 「1) Only for AVI64.」

> 「2) Only for AVI64 and DPS128.」

> 「3) Only for DPS128.」

| 脚注 | 落在哪个函数上 | 限制 |
|---|---|---|
| 1 | `vForceRange()` / `iForceRange()` | **只有 AVI64** |
| 2 | `restoreRange()` | **只有 AVI64 与 DPS128** |
| 3 | `clamp()` | **只有 DPS128** |

**这是本页一条容易漏的东西**：同一个函数在两个模式清单里出现，**但可能只在你那台卡的型号上有效**。

### 参数可以随便写，**但执行顺序是固定的**

原文给了一条一眼看不出来的规矩：

> 「These functions can be arranged in an arbitrary order after pin(), but SmartRDI always follows its own order of setting parameters as follows:」

它自己的顺序（原文表格，逐条）：

| 顺序 | 参数类别 | 函数 |
|---|---|---|
| 1 | `force mode` | `mode()` |
| 2 | `force range` | `iForceRange()` / `vForceRange()` |
| 3 | `force / clamp` | `vClamp()` / `iClamp()` / `vForce()` / `iForce()` |
| 4 | `meas range` | `vMeasRange()` / `iMeasRange()` |
| 5 | `meas wait` | `measWait()` |
| 6 | `meas` | `meas_waveform()` / `measure/compare()` |
| 7 | `restore range` | `restoreRange()` |

**这条规矩的实际意义**：链式写法里的**先后不影响结果**。
所以你**看不出**「为什么我先写 `iMeasRange()` 再写 `vForce()` 也对」——
原文的例子就是把顺序打乱的：

> 「rdi.dc().pin("DCS_PIN").vForce(1.3 V).clamp(-195 mA).iMeasRange(200 mA).average(8).iMeas().measWait(0.5*1 ms).execute();」

**注意这一行里没有 `connect()`**，见下。

### 连接：`connect()` 只属于 DPS 模式

> 「Function connect() is to be used only for DC Scale pins that are configured for the DPS operating mode in the DPS Pins editor.」

> 「There is no connect() function for DC Scale signal pins in the PMU (SIG) operating mode. Use iForce() or vForce() to connect a pin.」

**两件事一起读**：

- **「怎么连上」两种模式写法不同**：DPS 用 `connect()`，PMU (SIG) 用**一次 force**。
- 后半句里压着一条**前置**：DPS 模式的 pin **必须先在 [[dps-pins-editor]] 里配成 DPS 模式**。
  **这不是本页能做的动作**——它是 pin 配置阶段的产物。

### 测量与继电器：code-based 的三条注意事项

> 「The measurement functions iMeas() and vMeas() are supported for both the code鈥慴ased mode and the pattern鈥慴ased mode. Controlling the relays differs for the two modes:」

**⚠️ 这一句引文里也有 2 个坏字 `鈥慴`，同样原样保留**（见「出处」的坏字清单）。

| 条件 | 结果 |
|---|---|
| code-based 里 pin 已连接 | **一直保持连接，直到跑 `disconnect()`** |
| **首次** code-based 测量与**首次** `iForce()` / `vForce()` 写在**同一条** RDI 命令行里 | **测量一完，pin 立刻被断开** |
| 所以：首次 force 与首次测量**必须分成两条命令行、各自 `execute()`** | 原文逐字：`The initial force function and the code鈥慴ased measurement must be placed in separate RDI command lines, each terminated with function execute().`（**`鈥慴` 是语料坏字，原样保留**） |
| pin **已经**连上之后再写 | 测量与 force **可以合在一条命令行里** |
| pattern-based | 继电器完全不动（`Relays are not changed in the pattern鈥慴ased mode.`——**`鈥慴` 是语料坏字，原样保留**），测量函数只是「在 pattern 里定义测试点」 |

**第二 / 第三条是本页最值钱的一条**：它是一个**只在你写第一条命令行时才犯**的错，
而且症状是「测完就被断开」——看起来像硬件问题，其实是你把两句写在了一行。

### 7.5.2 起执行时间变了

> 「Starting from SmartRDI 7.5.2, some execution times are changed:」

| 卡 | 变了什么（原文逐字） |
|---|---|
| **AVI64** | `For AVI64: The setting time of rdi.dc().pin(pin).iMeas()/vMeas() is changed from 1 us to maximum (1 us, 8 cycles). This is important for slow cycle times.` |
| **FVI16** | `rdi.dc().pin(pin).iMeas()/vMeas(): The settling time is changed from 1 us to maximum (1 us, 8 cycles). This is important for slow cycle times.` |
| **FVI16** | `Force mode change between vForce and iForce: 0 us to 10 u` |

**原文自己解释了一句为什么重要**：`This is important for slow cycle times.`
**最后一行原文就写成 `10 u`**（没有单位后半截），**本页照录**。

## 典型用法

**先说依据的性质**：原文**没有 `## Procedure`、没有 `## Before you begin`**。
下面这个顺序是从正文的规则句 + 两个完整例子里拼出来的（**推断**，依据逐条附在后）。

### 三步骨架

| 步 | 做什么 | 依据 |
|---|---|---|
| **1** | **先在 pin 配置里定模式**（PMU SIG 或 DPS）——**这一步不在本页** | `connect()` 那条前置：`configured for the DPS operating mode in the DPS Pins editor` |
| **2** | **连上**：DPS 用 `connect().execute()`；PMU (SIG) 用一次 `iForce()` / `vForce()`，**且这次 force 必须单独一条命令行** | `There is no connect() function for DC Scale signal pins in the PMU (SIG) operating mode.` + 上面那张表 |
| **3** | **跑测量**：`vForce()` 改电平 → `iMeas()` / `vMeas()` 读回；**pattern-based 里不能夹 `relay()`** | 模式清单 + 上面那条顺序前置（引文见「是什么」） |
| **4** | **断开**：`disconnect().execute()` | 两个例子的最后一句 |

### 两个骨架，逐字（原文 `## Examples` 的两段）

**PMU (SIG) 模式**：

> 「rdi.dc().pin("DCS_SIG").vForce(2 V).vForceRange(25 V).iForceRange(100 uA).execute();」

> 「RDI_BEGIN();」

> 「    rdi.dc().pin("DCS_SIG").iMeasRange(100 uA).execute();」

> 「    rdi.dc().pin("DCS_SIG").vForce(10 V).execute();」

> 「    rdi.dc().pin("DCS_SIG").iMeas().execute();」

> 「RDI_END();」

> 「rdi.dc().pin("DCS_SIG").disconnect().execute();」

**DPS 模式**：开头换成 `rdi.dc().pin("DCS_DPS").connect().execute();`，其余同形
（`vForce(10 V)` → `iMeas()` → `vForce(8 V)` → `iMeas()`，然后 `RDI_END()`、
`disconnect().execute()`）。

### 一条写法上的观察，原文没解释

PMU 那个例子里**第一句 `vForce(2 V).vForceRange(25 V).iForceRange(100 uA).execute()` 在 `RDI_BEGIN()` 之外**，
而块内每一句都以 `execute()` 结尾。**原文没有一句说这个安排为什么这样。**
**语料未写**——本页不替它推，只把它记下来，因为**照抄例子时这处最容易被「整理」掉**。

### 一条建议（**建议，不是文档要求**）

| 你的需求 | 选哪个模式 |
|---|---|
| 需要动继电器、或要临时给电 | **code-based** |
| 测量点必须落在 pattern 里的某个位置（跟时序对齐） | **pattern-based** |

依据是各自的能力边界（`relay()` 只在 code-based 清单里；`test points will be created in the pattern`），
**但「该选哪个」这句话原文没说**——这是本页的工程建议，标为建议。

## 和谁有关

| 页 / 名字 | 关系是什么 |
|---|---|
| [[smartrdi]] | **上位页**：SmartRDI 的整体与硬件支持范围。**本页不重复它——本页只写 `rdi.dc()` 这一段怎么做** |
| [[dps-pins-editor]] | **前置**（硬前置）：DPS 模式的 DC Scale pin **必须先在它里面配好**，`connect()` 才有意义 |
| [[rdi-call-requires-begin-end-block]] | **约束**：RDI 的调用要落在 `RDI_BEGIN()` / `RDI_END()` 块里（两个例子都是这么写的） |
| [[rdi-configure-file]] | SmartRDI 的配置文件。**本页没读，只有名字** |
| `SmartRDI timing settings of DC events`（raw: `02.07.13.08.15`） | **原文 `## Related information` 唯一一条**。**本页没读**——所以「DC 事件的时序怎么设」本页没有 |
| `execute()`（raw: `02.07.13.08.01.02`） | **每条链式调用的终点**；两个例子里每一行都以它收尾。**本页没读它的参数** |
| [[dc-test-programming]] | 同段的概念页（DC 测试怎么编程）。**与 [[smartrdi]] / [[spmu-pin-task-mode]] 是两条不同的 API 线**，本页属于 SmartRDI 那条 |
| [[xps256-pmu-operating-mode]] / [[xps256-programming-dps-operating-mode]] | **两种工作模式各自的说明**。本页只写「两种模式都支持」，**它们各自是什么本页没读** |
| [[dc-scale-xps256-card]] / [[dps128-dps64-cards]] / [[dc-scale-uhc4t-card]] / [[spmu-pin-task-mode]] / [[dc-scale-limits-editor]] | **硬件与相邻功能**。脚注里那三个卡名（`AVI64` / `DPS128`）与版本段里的两个（`AVI64` / `FVI16`）**本页只有名字，一篇没读** |
| **51 条子主题** | 本页声明的 `rdi.dc()` 函数页（`average()` / `clamp()` / `connect()` 起，到 `getValue()` 止）。**均未建页**，本页一条没读 |

**一条要说清的**：`source` 那一篇是**一个 51 条函数页的目录**，
**本页的正文事实几乎全来自它的规则性段落**（两种模式、参数顺序、连接、继电器、7.5.2 的时间），
**不来自那 51 篇**。

## 版本

本文档 `## Functional changes` 段**八条**，逐字转录：

> 「- Introduced in SmartRDI 2.1.0」

> 「- SmartRDI 2.2.0: New function preCharge().」

> 「- SmartRDI 2.4.2: New functions iFilter(), vFilter(), iSlewRate(), vSlewRate().」

> 「- SmartRDI 2.4.2: New functions mode(), refPin(), measFilter(), vClamp().」

> 「- SmartRDI 7.5.0: New functions forceSenseLink(), vCompliance(), forceDropMax(), returnDropMax().」

> 「- SmartRDI 7.5.0: New functions vMeasBattery(), vMeasForceDrop(), vMeasReturnDrop().」

> 「- SmartRDI 7.5.1: New functions dcPowerBudget(), pulseEnergyBudget().」

> 「- SmartRDI 7.5.2: Execution times for some actions are changed.」

**三条要注意的**：

- **`SmartRDI 2.4.2` 与 `SmartRDI 7.5.0` 各出现两次**，都是**两条独立的条目**
  （两条 `New functions` 分开写）。**语料如此，本页照录、不合并。**
- **`Introduced in SmartRDI 2.1.0` 不是哨兵值**——它写的是 `in` 不是 `before`
  （§11.2 ② 的哨兵值是 `Introduced before SmarTest 6.3.2` 那种写法）。
  **本页这条是「2.1.0 就有了」。**
- **版本号跨产品线**（§11.2 ④）：本 wiki 的版本页**带产品前缀**。
  上表对应：[[smartrdi-2.1.0]] / [[smartrdi-2.2.0]] / [[smartrdi-2.4.2]] /
  [[smartrdi-7.5.0]] / [[smartrdi-7.5.1]] / [[smartrdi-7.5.2]]。

### ⚠️ 一处对不上，照实记

**版本段点名的 18 个函数里，有 7 个没有自己的子主题页**：
`mode()`、`refPin()`、`forceSenseLink()`、`vCompliance()`、`vMeasBattery()`、
`dcPowerBudget()`、`pulseEnergyBudget()`——它们**不在**这篇的 51 条 `Subtopics` 里。

**同一件事还有第二处**：上面「参数设置顺序」那张表里的
`mode()` / `meas_waveform()` / `measure/compare()` 三个名字，**也都没有子主题页**。
`mode()` 尤其要紧——它是**顺序表的第 1 步**。

**两份清单对不齐是语料的事实**，本页照记，**不判谁漏了**。

## 出处

`sources:` **一篇**：
`02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02_Setting_up_DC_Scale_pins_with_SmartRDI.md`
（raw 的 `source_topic` 是 `141515.htm`）。**整篇读完**——全文 **249 行**。

**本页没做的**：

- **51 条子主题一条没读。** 那 51 篇是 `rdi.dc()` 的每个函数页
  （`average()` / `clamp()` / `connect()` / `iForce()` / `vForce()` / `getValue()` 等 51 个）。
  **所以每个函数的参数、返回值、默认值、报错，本页一个字都没有**——
  本页只有**它们的名字**，以及原文在规则段落里顺带给的那些约束。
- **`## Related information` 那一篇没读**（`SmartRDI timing settings of DC events`，
  `02.07.13.08.15`）。所以 **DC 事件在时序上怎么排**，本页没有依据。
- **`execute()`（`02.07.13.08.01.02`）没读。** 它出现在每一行链式调用的末尾，
  但**它的参数与语义本页只有「本次设置提交」这个印象**——**没有原文依据**。
- **硬件文档一篇没读**：`XPS256` / `DPS128` / `DPS64` / `UHC4T` / `AVI64` / `FVI16`
  **本页只有名字**。所以脚注那三条限制**为什么存在**，本页答不了。
- **没有实跑。** 没在机台上跑过任何一行 `rdi.dc()`、没测过任何一张 DC Scale 卡。
  `verified: doc-only`。

**图：本文档一张图都没有**（正文里 `../../../../raw/` 引用 **0 个**）。
**所以本页没有任何来自图的结论**——这是「**本页没用图**」，不是「图够不着」（§11.4）。

**⚠️ 语料瑕疵，照实记，一处都没替它改（§11.2）。**

**① 坏字（§11.2 ①，UTF-8 被按 GBK 读）：本篇共 13 处，全是同一个形态 `鈥慴`。**
逐行位置与处数如下（**引文原样留着坏字，本页没有一处替它改成 `-`**）：

| 行 | 那一行的原样片段（坏字保留） | 处数 |
|---|---|---|
| 64（小标题） | `## Code-based mode and pattern鈥慴ased mode` | 1 |
| 66 | `In the static code鈥慴ased mode, the level setting is changed.` 与同句后半 `provided for the code鈥慴ased mode:` | 2 |
| 70 | `In the dynamic pattern鈥慴ased mode, test points will be created in the pattern.` 与同句后半 `can be used in the pattern鈥慴ased mode:` | 2 |
| 74 | `Relays cannot be switched in the pattern鈥慴ased mode. So make sure the relay connection is programmed in the code鈥慴ased mode and is correct before the burst execution of the pattern鈥慴ased mode.` | **3** |
| 180 | `the code鈥慴ased mode and the pattern鈥慴ased mode`（`## Measurements and relay settings` 首句） | 2 |
| 185 | `The first code鈥慴ased measurement must be separated from the initial` 与同句后半 `The initial force function and the code鈥慴ased measurement must be placed in separate RDI command lines` | 2 |
| 188 | `- Pattern-based mode: Relays are not changed in the pattern鈥慴ased mode.` | 1 |

**合计 13 处。** 这张表里**只有那 7 行有坏字**，逐行加得起来——
**它是「回 raw 数一遍」的结果，不是估的。**

**它本来是什么，说清**：`鈥慴` 是 **U+2011（非断行连字符 U+2011）的 UTF-8 三字节的头两个字节**，
而**紧跟其后的 ASCII `b` 被并进了第二个坏字**（§11.2 ① 明写「一个字母会被吃掉」）。
**所以 `code鈥慴ased` 的原字是 `code-based`、`pattern鈥慴ased` 的原字是 `pattern-based`。**

**⚠️ 处置照 §11.2：页面照原样转录，不替它改。**
**代价要写清，这一条最实用**：**拿修好的 `code-based` 去 raw 里搜是搜不到的**，
要搜就得搜坏掉的形态 `code鈥慴ased`（或者搜 `code` 再往后翻）。
**本页正文里的 `code-based` / `pattern-based` 是「读成什么」；
上面两处 `>` 引文块里则原样留着坏字**——两者不冲突，但读者要知道这件事。

**② 整词替换（§11.2 ⑤）**：本篇查过 `DC/DC power units`，**0 命中**。
**这一族的损坏不在这篇上。**

**③ 两处「名字对不上」不是坏字，是语料自己不一致**（见「版本」那节）：
版本段点名 18 个函数，**7 个没有子主题页**；参数顺序表里的
`mode()` / `meas_waveform()` / `measure/compare()` 也都没有子主题页。**照记，不替它调和。**

**④ 图里的字不进 `>` 引文块（§11.4）**——本篇没有图，这一条在本页为空。

**⑤ `connect()` 与 `disconnect()` 被链到两处不同的文件——`Subtopics` 一处、正文一处。
（这一条不是坏字，是语料自己的两处链接对不上。）**

| 出现的地方 | 逐字 | 指向 |
|---|---|---|
| `#### Subtopics`（第 14、15 行） | `- [connect()](<02.07.13.12.02.03_connect.md>)` / `- [disconnect()](<02.07.13.12.02.06_disconnect.md>)` | **`02.07.13.12.02.xx`** |
| 正文 `## Connecting DC Scale signal pins`（第 174 行） | `Function [connect()](<02.07.13.12.01.03.03_connect.md>) is to be used only for DC Scale pins that are configured for the DPS operating mode in the DPS Pins editor.` | **`02.07.13.12.01.03.03`** |
| 正文 `## Measurements and relay settings`（第 184 行） | `the function [disconnect()](<02.07.13.12.01.03.04_disconnect.md>) is executed for the pin` | **`02.07.13.12.01.03.04`** |

**同一个函数名，`Subtopics` 里两篇、正文里另外两篇，四篇的编号只有前两段相同。**
**原文没有说这两组是不是同一个东西的两种写法**（`Subtopics` 那 51 条是本篇自己的函数页清单，
而正文那两条的 `12.01.03` 是 `02.07.13.12.01`（**不是**本页所在的 `12.02`）的下一层）——
**本页照实并列两组路径，不判哪一组是对的、也不替它改链接。**
**代价要写清**：**要查 `connect()` 的参数，看 `Subtopics` 会翻到 `12.02.03`，跟着正文翻会到 `12.01.03.03`——
两处指向的是不同的文件**；**本页两处都没打开**（那 51 篇一条没读）。

`verified: doc-only`
