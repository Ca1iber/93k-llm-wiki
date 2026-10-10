---
type: object
title: Utility power supplies
layer: n/a
stage: project
tags: [utility-power-supply, dut-board, exa-scale, pogo-block, hardware, power, up5v, xp-pins]
related: [utility-card, utility-pogo-block-utility-card-v93000-exa-scale-systems, error-utility-power-supply-not-enabled, pin-utility, sequencer-controlled-utility-lines, dut-board-design-reference, pogo-block-compatibility, connect, disconnect, smartest-7.5.2, smartest-8.3.4]
sources:
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.05_Utility_power_supplies.md
created: 2026-09-18
updated: 2026-09-20
verified: doc-only
---

# Utility power supplies

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

**没有加标记的语法段。** 定义文档里没有 `Syntax` / `Parameters` / `Example`
这类**段标记**，跟着 `Subtopics` 找一层也没有。
**所以本脚本一个字都不收录**——没有段标记时「哪一段是语法」是猜，而猜就是编（§4）。

<!-- 语法节 end -->

## 是什么

**Utility power supply（utility 电源）是给 DUT 板/探针卡上的「有源器件」供电的固定电压电源。**
原文第一段就是全部定义，**而且它一半的篇幅在讲「它不是什么」**：

> 「Utility power supplies are used to power active components like relays, operational
> amplifiers, and buffer on the DUT board or probe card. In contrast to device power supplies,
> the utility power supplies provide fixed voltages and do not provide a programmable clamp
> current or measurement functionalities.」

**两句话两块内容**：

| 它是什么 | 它不是什么（**与 device power supply 的分界**） |
|---|---|
| 给 DUT 板 / 探针卡上 **relay、运放、buffer** 这类有源器件供电 | **电压固定**（不可 program）；**没有可 program 的 clamp 电流**；**没有测量功能** |

**这条分界是本页最该记住的一句**：**要 program 电压、要 clamp 电流、要测量，
那不是 utility power supply，是 device power supply（DPS）。**

### 一象限特性：**它压不到 0 V，也放不掉板上的电**

这是「固定电压」之外**第二个、也是后果最重**的机制。原文：

> 「Utility power supplies can work in only one quadrant: They can force a positive voltage and
> drive a current, or they can force a negative voltage and sink a current. The output can be
> switched on or off.」

**所以**：

> 「As a result, the utility power supplies cannot force 0 V at the output and cannot discharge
> circuitry on the DUT board.」

**「one quadrant」= 只能 source 正压，或 sink 负压**，**不能同时、也不能既 source 又 sink**——
**于是 0 V 是一个它做不到的电压。**

**原文紧接着列了四条「因此必须注意」**，这四条是本页最实用的部分：

| 注意 | 原文要点 |
|---|---|
| **降到 0 V 要多久，看板上** | **大负载电流会缩短这个时间，大电容会拉长它**（`High load currents will decrease the time. Large capacitors will increase the time.`） |
| **短时间关掉电源会造成危险压降** | `Switching off a utility power supply for only a short time can lead to a critical voltage drop.` |
| **brownout 会让数字电路进入未定义状态** | `The critical drop in the supply voltage, also known as brownout, can bring digital circuits into an undefined state.` |
| **关掉的电源可能被「顶」到未知电压** | **已停用的 utility 线，其内部上拉电阻上的电流 + DUT 板上连着的东西，**可以把这个关掉的电源输出**顶高到一个未定义的值** |

**（推断）这四条串起来是一条工程警告**：**utility 电源关掉 ≠ 板上那一路没电。**
**依据是第二条（压降）与第四条（被顶高）合起来说明「关电源」这个动作**在关掉的瞬间和关掉之后
**都有非零电压残留**；**这四条原文自己是并列给的，没有一句把它们串成结论，所以这是推断。**

### 四组电压 / 接口 / 两种机型：**一张表就是全部**

原文 `## Overview` 表（**本页照抄，链接已剥成纯文本**）：

| Voltages | Interface | **V93000 EXA Scale systems** | **V93000 systems** |
|---|---|---|---|
| **`+5 V`** | **`UP5V` pin on all utility pogo blocks** | `Utility power supply - UP5V pins` | `Internal utility power supply` |
| **`+5 V`, `+3.3 V`, `-5 V`** | **`XP...` pins on all 4-row utility pogo blocks** | `Utility power supply - XP pins` | `External utility power supply` |
| **`+15 V`, `-15 V`, `24 V floating`** | **`UPP15V`, `UPM15V`, `F24V...` pins on selected 4-row utility pogo blocks** | `Utility power supply - UPP15V / UPM15V / F24V pins` | **`n.a.`** |
| **`+5 V`, `+12 V`, `+15 V`, `-15 V`** | **DPS pogo block (3 rows)** | `Internal Utility Power Option` | `Internal Utility Power Supply (SE-UDPS)` |

**三处读表要点：**

1. **第三行是 EXA Scale 独有的**——**`V93000 systems` 那格写 `n.a.`**，
   即 **`+15 V` / `-15 V` / 浮空 `24 V` 在老 V93000 上没有**。
2. **最后一行的接口不是 utility pogo block，是 DPS pogo block（3 行）**——
   **同一组电源横跨两种 pogo block**（见 `## Pogo pin assignment` 那节的说法：
   `The utility power supplies are available on utility pogo blocks and DPS pogo blocks:`）。
3. **`+15 V, -15 V, 24 V floating` 那一行里，「浮空」只修饰 `24 V`**——
   **本页照原文的三个逗号并列读，不替它断句。**

### 枚举：这一族有 7 个子主题（本页一篇都没展开）

原文 `#### Subtopics` 列了 **7 篇**：

| 子主题 | 机型 |
|---|---|
| `Utility power supply - UP5V pins (V93000 EXA Scale systems)` | EXA Scale |
| `Utility power supply - XP pins (V93000 EXA Scale systems)` | EXA Scale |
| `Utility power supply - UPP15V / UPM15V / F24V pins (V93000 EXA Scale systems)` | EXA Scale |
| `Internal Utility Power Option (V93000 EXA Scale systems)` | EXA Scale |
| `Internal utility power supply (V93000 systems)` | 老 V93000 |
| `External utility power supply (V93000 systems)` | 老 V93000 |
| `Internal Utility Power Supply (SE-UDPS) (V93000 systems)` | 老 V93000 |

**每一组电源的电压范围、电流能力、pin 定义，全在那 7 篇里，本页一个字都没有。**

### 开关行为：**逐路独立还是整组，取决于哪一组**

原文 `## Power on/off behavior` 那一节是**本页最乱也最重要的一段**。
**能控制的粒度，四组电源分三档**：

| 电源 | 能怎么开关 | 默认态 |
|---|---|---|
| **`UP5V`**（EXA Scale） | **所有 utility pogo block 上同时开关**（Utility Card 的所有块，或卡笼的所有块），**用 SmarTest 的 API** | 见下（**看兼容设置**） |
| **`XP...`**（EXA Scale，3 路输出） | **逐路、逐张 Utility card 独立开关**；**开了 Pin Scale / Smart Scale 兼容设置就只能整组控** | **默认关** |
| **`UPP15V` / `UPM15V` / `F24V...`**（EXA Scale，4 路输出） | **逐路、逐张 Utility card 独立开关** | **默认关** |
| **`Internal Utility Power Option`**（EXA Scale，DPS pogo block） | **只能整组、且逐张 Utility card** | **默认关** |
| **`External utility power supply`**（老 V93000） | **只能整组** | **默认关** |
| **`Internal utility power supply`**（老 V93000 的 `UP5V`） | **测试头加电且 SmarTest 加载后自动开** | **自动开** |
| **`SE-UDPS`**（老 V93000，3 路输出） | **P# 到 PS# 的 sense 连接在 docked DUT 板上建立后自动开** | **自动开** |

**`UP5V` 的默认态是全页最容易读错的一格**，原文：

> 「With compatibility settings for Pin Scale and Smart Scale systems enabled, the UP5V output of
> the first card cage or of the first Utility Card is switched on by default. With standard
> settings for V93000 EXA Scale systems selected, the outputs of the utility power supply are
> disabled by default.」

**即：默认态取决于兼容设置，而兼容设置默认是开着的**——脚注 [1] 说：

> 「By default, the settings for compatibility with Pin scale and Smart Scale are active: The new
> behavior for V93000 EXA Scale systems must explicitly enabled.」

**所以出厂状态下 `UP5V` 在第一卡笼/第一张 Utility Card 上是「默认开」的；
要 EXA Scale 的标准行为（默认关），得**显式**去开那个设置。**

### 过载行为：**两种，别混**

**两种过载后的行为在原文里并存**，原文两句逐字：

| 行为 | 原文 |
|---|---|
| **自动关，`必须用 API 重新使能`** | `With an overload condition detected, the supply is automatically switched off. It must be enabled again using the API.` |
| **自动关，`故障条件消失后自动开`** | `The supply is automatically switched off if an overload condition is detected and is automatically switched on as soon as the faulty condition has been corrected.` |

**再加一条老 V93000 上的**：`When reloading SmarTest or resetting the system, the supply is switched off for a short time.`

**（推断）第二种（自恢复）**是老 V93000 那几路的行为——
**依据是「自动重开」那句出现在老 V93000 那一列，而 DPS pogo block 那一行两列正好各给了一种**；
**但前几张表的「两种行为」两列写的是同一句，所以哪一路是哪一种，本页不能逐路断言。**

### 控制入口：SmarTest 7 与 8 各一套 API

> 「The switchable utility power supplies can be controlled by test method API UTILITY_POWER_STATUS
> of SmarTest 7 or by Device Test API IUtilityPower of SmarTest 8.」

**注意「switchable」这个词**：**上表里标「自动开」的那两路（老 V93000 的
`Internal utility power supply` 和 `SE-UDPS`）属于不可切换的那一档。**

**（推断）**：**能写进代码去开关的，只有上表里标「默认关 / 看设置」的那几路**，
**依据是原文这句限定了 `The switchable utility power supplies`**，
**以及 `Internal utility power supply` 那格写的是 `automatically switched on`。**

## 典型用法

**原文没有 `## Procedure`、没有 `## Before you begin`、没有 Example。**
它给的是四个 `## ` 节：`Overview` / `Common characteristics` / `Pogo pin assignment` /
`Power on/off behavior`。**所以本页没有「一步步怎么做」，只有原文里那几条硬约束。**

**能落成动作的只有下面这些：**

**1. 板子设计阶段：先确认你需要的电压在哪一组、在哪个 pogo block 上。**
`+5 V` 走 `UP5V`（所有 utility pogo block）；`+5 / +3.3 / -5 V` 走 `XP...`
（所有 **4 行** utility pogo block）；`+15 / -15 / 24 V 浮空` 走
`UPP15V` / `UPM15V` / `F24V...`（**只在选定的** 4 行 utility pogo block 上）；
`+5 / +12 / +15 / -15 V` 走 **DPS pogo block（3 行）**。

**2. 用之前先看默认态，别假设它是关的。**
`XP...` / `UPP15V` 那几组 / `Internal Utility Power Option` / `External` **默认关**；
但 **`UP5V` 的默认态跟着兼容设置走，而出厂时兼容设置是开的 → 第一卡笼/第一张卡上 `UP5V` 默认开**。

**3. 过载了要分清是「要手动重开」还是「会自己恢复」。**
原文给的是两种行为，**不确认的话，一次过载之后你会以为电源坏了，
其实它可能在等一次 API 使能**。

**4. 判断板上那一路还有没有电，不能只看电源开关。**
**一象限特性决定了它压不到 0 V**（大电容会拖长时间），
**而且关掉的那一路本身还可能被上拉电阻和板上电路顶到未知电压**。

**5. 写代码控制开关**：SmarTest 7 用 `UTILITY_POWER_STATUS`，SmarTest 8 用 `IUtilityPower`。

## 和谁有关

- [[utility-card]] — **上游，EXA Scale 上的载体**。本页 Overview 表里 EXA Scale 那三列
  基本都挂在 Utility Card 上（`UP5V` / `XP` / `UPP15V / UPM15V / F24V`），
  **本页讲「有哪些电压、怎么开关」，那张卡讲「硬件长什么样、怎么出去」**。
- [[utility-pogo-block-utility-card-v93000-exa-scale-systems]] — **下游，pin 定义处**。
  本页 `## Pogo pin assignment of utility power supplies` 一节把好几组电源直接指到它
  （`UPP15V, UPM15V, F24V... pins on selected 4-row utility pogo blocks` 那一行）。
  **本页只有「哪个 pin 名在哪种 pogo block 上」，具体 pin 号与排布在它那页。**
- [[pin-utility]] — **对象侧同类**。本页讲的是供电侧，
  而 `## Common characteristics` 里有一条讲「已停用的 utility 线」的内部上拉电阻
  ——**那条靠的是 utility 线自己的特性**（原文指向 `Utility line characteristics`）。
- [[sequencer-controlled-utility-lines]] — **同一批硬件资源的另一侧**。
  本页只讲电**源**（`power supplies`），**utility 线（`utility lines`）只在
  「被停用的线的上拉电阻」那一条里出现一次**。
  **线的控制方式在那页，本页没有。**
- [[error-utility-power-supply-not-enabled]] — **错误侧**。
  **（推断）**：它讲的应该就是本页这套电源「没被使能」时的报错
  （**本页的 `It must be enabled again using the API.` 正是这个动作**），
  **依据只是页名加这一句措辞**；**本页没有关于那个错误的任何事实。**
- [[dut-board-design-reference]] — **本页所在的设计参考族**。
  **本页是 DUT 板设计视角的电源页**，不是软件操作页——原文四条注意事项全部是板上效应
  （电容、负载、brownout、上拉电阻），**没有一条是界面上怎么点**。
- [[pogo-block-compatibility]] / [[pogo-pad-and-via-design]] / [[inter-layer-via-design]] /
  [[layout-information-dut-board]] — **板上设计侧的同族页**。
  本页的 pin 名（`UP5V` / `XP...` / `UPP15V` / `UPM15V` / `F24V...`）
  **是板上布线要落的位置**；**本页没有讲怎么布线。**
- [[connect]] / [[disconnect]] — **相关概念**。
  老 V93000 的 `SE-UDPS` 与本页讲的 `P/PS#` sense 连接、docked DUT 板有关；
  **本页只有那一句「连接建立后自动开」**。
- [[smartest-7.5.2]] / [[smartest-8.3.4]] — **版本页**。本页 `## 版本` 两处落点。
- `Utility power supply - UP5V pins` / `Utility power supply - XP pins` /
  `Utility power supply - UPP15V / UPM15V / F24V pins` /
  `Internal Utility Power Option` / `Internal utility power supply` /
  `External utility power supply` / `Internal Utility Power Supply (SE-UDPS)`
  （**均未建**）— **本页的 7 篇子主题，一篇都没读**（见 `## 出处`）。
- `Utility line characteristics` / `Utility line example circuits`（**均未建**）—
  原文第四条注意事项指向它们；**本页没读，「上拉电阻把电源顶高」的机理本页没有。**
- `Internal utility resources specific setup tasks` /
  `Utility Card specific setup tasks`（**均未建**）— 脚注 [1] 指向的兼容设置说明。
- `UTILITY_POWER_STATUS` / `IUtilityPower`（**均未建**）— 两个 API 页；**没读**，
  **本页没有它们的任何签名或参数。**

## 版本

本文档**有** `## Functional changes` 段，**只有两条**：

- **Introduced in SmarTest 7.5.2**
- **SmarTest 8.3.4：`Utility power supplies for V93000 EXA Scale systems added`**

> **第二条要单独盯住**：**EXA Scale 那一半（`UP5V` / `XP...` /
> `UPP15V` / `UPM15V` / `F24V...` / `Internal Utility Power Option`）
> 是 SmarTest 8.3.4 才加的**，而**本 wiki 面向 SmarTest 7.10.3**。
> **也就是说：本页 Overview 表右半列的全部内容，以及 `## Power on/off behavior` 里
> EXA Scale 那几格，在 7.10.3 上不成立**——
> **7.10.3 里能用的只有 Overview 表最右那一列（老 V93000 那三种）。**
> **这条是版本段里最该被看见的一句，而原文自己并没有把它标成「注意」。**
>
> **（推断）**：**页首 `stage: project` 与本页两列并排的写法**，
> 说明这一页是**跨两代机型合写的**——**依据是 Overview 表把两种机型并成两列而版本段只给了一条
> EXA Scale 的落点**。**这是推断，原文没说这是合写还是分写。**

> ⚠️ **段末粘着脚注定义**（`[1)](<>) For compatibility settings, refer to …`）——
> 又是 §11.2 ③ 那个现象：`## Functional changes` 是最后一个 `## ` 段，脚注被算进来。
> **它不是版本条目。** 内容是关于兼容设置与那两篇 setup tasks 文档。

## 出处

`sources:` 一篇：
`02_System_reference/02.03_DUT_board_design_reference/02.03.05_Utility_power_supplies.md`

**本页没做的：**

- **7 篇子主题一篇都没读**。**这是本页最大的空缺**：
  **每一组电源的电压范围、电流能力、精度、pin 号，本页一个数字都没有**——
  本页只有 Overview 表里的**电压名**和**pin 名**（`UP5V` / `XP...` / `UPP15V` /
  `UPM15V` / `F24V...`），**连 `XP...` 里的 `...` 具体是哪些 pin 本页都不知道。**
- **`## Common characteristics` 那四条注意事项本页只做了转述与一句标注的推断**，
  **没有更深的电学解释**——原文也没有，它指向 `Utility line characteristics` 和
  `Utility line example circuits`，**那两篇没读。**
- **`## Power on/off behavior` 那张表本页是「读懂之后重排」的，不是照抄。**
  原因见下面的瑕疵③：**原文那张表被拆成了 3 张碎表**。
  **本页的重排有推断成分**——哪些格属于哪一行，本页按 `## 语法 / 参数` 节里
  脚本逐字抽的那 5 张表 + 原文的 `| Supply |` 行头对齐；
  **逐格对应关系本页不能保证全对，原文的结构已经坏了。**
- **过载后的「哪种电源用哪种行为」，本页没有逐路断言**（原文两列同句，分不出来）。
- **两个 API（`UTILITY_POWER_STATUS` / `IUtilityPower`）没读**，
  **所以「怎么调 API 开一路电源」这个本页最该有的操作步骤，本页没有。**
- **兼容设置（compatibility settings）的两篇说明没读**，
  **所以「在哪开这个设置」本页不知道**，只知道「必须显式开」。
- **`## Pogo pin assignment` 一节里的 9 篇 pogo block 文档一篇没读**
  （`Basic configuration` / `Utility Card` / `LTH large DUT interface` /
  `STH` / `CTH` / `ATH` 各 `DUT Scale` 与 `small DUT` 变体）。
- **一张图看了没有：没有。** 本篇没有插图。
- **没有交叉验证任何别处的文档**（§11：本页只写这一篇里有的）。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> **① 编码损坏：1 行，同行两处**（`鈥` 形态）。那一行逐字：
> `The current through the internal pull鈥憉p resistor of a deactivated utility lines and the
> connected circuitry on the DUT board can also push up the output voltage of a switched鈥憃ff
> utility power supply to an undefined value.`
> ——**`pull鈥憉p` = `pull-up`，`switched鈥憃ff` = `switched-off`**。
> **代价照 §11.2 ① 写清楚：拿修好的 `pull-up` 去 raw 里搜是搜不到的。**
> **（本篇 `渭` / `卤` / `鈮` 形态 0 处。）**
>
> **② 同一路电源，两处拼法不同：`UP5V` 与 `UPV5`。**
> 原文讲老 V93000 那一格逐字：
> `The UPV5 supply is automatically switched on as soon as the test head is powered up and
> SmarTest is loaded.`
> ——**`UPV5` 是把 `UP5V` 的 `5` 和 `V` 写颠倒了**；本篇其余每一处（含 Overview 表、
> pin 名、子主题标题）都写 **`UP5V`**。**本页正文按 `UP5V` 写，但引文照原样。**
>
> **③ `## Power on/off behavior` 那张表在语料里是碎的。**
> **`## 语法 / 参数` 节里可以看到后果**：脚本把它抽成了**第 3、4、5 三张「表」**，
> 而这三张各自只剩一两行（`| Supply |` 表头、一句过载说明、几个 `n.a.`），
> **`UP5V` / `XP...` / `UPP15V` / `DPS pogo block` 各行的正文全落在表外面。**
> **同一篇文档里 `## Pogo pin assignment` 那张表也一样碎**（见④）。
> **本页正文那张「开关粒度」表是这样还原出来的：以 `## 语法 / 参数` 节里脚本抽的第 3 张表的
> 行头（`UP5V` / `XP...` / `UPP15V` / `DPS pogo block`）为准，把该行之后的散段落归位。**
>
> **④ `## Pogo pin assignment` 表里 `XP...` 那一行**两个格子是空的**。**
> 原文逐字：
> ` | XP... pins on all 4-row utility pogo blocks |`
> 紧接着就是下一行 `UPP15V, UPM15V, F24V...`。
> ——**Overview 表里明明有 `XP...` 这一组的两种机型落点，到 pogo pin assignment 表里
> 这一行却没有任何链接。本页不判是漏了还是本来就没有。**
>
> **⑤ 同一列，两张表的表头写法不同。**
> `## Overview` 表第三列表头是 `V93000 systems`；
> `## Power on/off behavior` 表第三列表头是 `V93000 Pin Scale and Smart Scale systems`。
> **同一个位置、同一篇文档，两种叫法。本页正文照各自的原文引。**
>
> **⑥ 脚注 [1] 里少一个 `be`。** 逐字：
> `The new behavior for V93000 EXA Scale systems must explicitly enabled.`
> ——**`must explicitly enabled` 应为 `must be explicitly enabled`。本页照原样引。**
>
> **⑦ 两列写同一句话，导致「哪一列是哪一种行为」分不出来。**
> `## Power on/off behavior` 表里有三处的两列**逐字相同**，例如：
> `With an overload condition detected, the supply is automatically switched off. It must be
> enabled again using the API.  | With an overload condition detected, the supply is
> automatically switched off. It must be enabled again using the API.`
> **同一句话在两列里各写一遍，看上去像合并单元格。本页因此不敢逐路断言过载行为（见上）。**
>
> **⑧ 大小写不一致：`Utility card` 与 `Utility Card` 并存。**
> 例如 `of the Utility card or (for the internal utility resources) of the card cage` 写的是
> `Utility card`，而 `[[utility-card]]` 那一页的标题是 `Utility Card`。
> **本页正文按各页标题写，引文照原样。**
>
> **⑨ `deactivated utility lines` 里的复数不一致**：原文写
> `a deactivated utility lines`（**`a` 配复数**）。**本页照原样引。**
>
> **⑩ 内链指回自己这一页。** 第三条注意事项里写着
> `See also the description for UP5V on Pin Scale and SmartScale systems in Utility power supplies.`
> ——**`Utility power supplies` 就是本篇自己**（raw 链接目标是 `02.03.05_Utility_power_supplies.md`）。
> **一条「参见」指向了它自己所在的这一页。本页不判这是有意（指页内另一节）还是编错。**

`verified: doc-only`
