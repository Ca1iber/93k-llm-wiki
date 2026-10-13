---
type: object
title: Digital Pins editor
layer: gui
stage: pin
tags: [gui, pin-configuration, mode-context, dc-scale, pmu, ganging, pin-name]
related: [conf, dfpn, ctxt, pin, dc-scale-xps256-card, dps128-dps64-cards, ganging, pin-configuration-file]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01.02_Digital_Pins_editor.md
created: 2026-09-18
updated: 2026-09-20
verified: doc-only
---

> ⚠️ **本页若干处记的是 2026-10-10【之前】的语料形态。**
> 那一轮把语料里的表格一律换成了**指向上游 HTML 的指针**
> （见 `extract/PLAN-表格指针化.md`）。所以下文凡是说「表格被压平 / 被摊平 /
> 一格一行」的地方，指的是**更换之前**的样子 —— 现在语料里那个位置是**一句指针**，
> 真表仍在 `tdc-html/raw/` 的上游 HTML 里。**页码/引文都不受影响。**

# Digital Pins editor

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **200 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01.02_Digital_Pins_editor.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Examples

### DC Scale pin (PMU mode) setup

The following table shows an example configuration for DC Scale pins in PMU mode.


### Utility DC pin setup

  !`Utility DC pin setup`（raw: `../../../../raw/355197.png`）

<!-- 语法节 end -->

## 是什么

**Digital Pins editor 是「配针」的 GUI**——配的是**数字针**，外加**PMU 模式下的 DC Scale 针**。
原文第一句就把范围划死了：

> 「**Digital pins and DC Scale pins in PMU operating mode** are configured in the Digital Pins
> editor.」

**注意这句话里没有 DPS 模式**——**DC Scale 针只有在 PMU 模式下才归这个编辑器管**
（推断：原文限定语只写了 `in PMU operating mode`；
**DPS 模式那一边本页没有依据，所以本页不说它归谁管**）。

### 界面：一块表 + 一个下拉

原文：

> 「The editor consists mainly of **the tabular pin configuration area**. The **CONTEXT drop-down
> list at the top right** allows you to select a **mode context**.」

**「右上角那个 CONTEXT 下拉」是它和 [[ctxt]] / [[conf]] 那条线接上的地方**——
**下拉里选的就是 mode context**，也就是 `CONF ["context",]…` 里那个 `context`
（推断：原文只说「allows you to select a mode context」，
**没说这个下拉和 `CTXT` 命令是同一份数据**；但 context 由 `CTXT` 定义这件事在 `CTXT` 那篇里写着）（推断）。

### 界面长什么样（④ 图证 · `355141.png`）

**原文在讲完「一块表 + 一个下拉」之后紧接着挂了这张界面图**（`355141.png`，alt 文字就是 `Digital Pins editor`，原图 642 × 405）。**本页原先写「连编辑器长什么样、有哪几个 tab 都不知道」——那张图现在读了，它答的就是这件事：**

- 窗口上是**一个 tab，标题 `Digital Pins`**（截图里只有这一个 tab，**不是多 tab 并列**）。
- **右上角一个 `CONTEXT:` 加下拉框**，**图里选中的值是 `DEFAULT`**（**`DEFAULT` 这个字符串在本篇 raw 里 grep 不到，只在图上**）。
- 表头从左到右：行号、`Name`、`No`、`Type`、`Mode`、**`Scaling[V/A]`**、`HW`、`Connection Set`、`Comment`、**`Tester Channel`**——**九个列名与正文的 `## Parameters` 表逐个对得上**。
- **`Tester Channel` 那一格在图上被拆成两个子列：`Site 1` 与 `Site 2`**——**一个 pin 一行里给出每个 site 各自的通道号**（图上第 1 行 `CP` 是 `10509` / `10609`）。**这一点本篇正文一个字都没写**（**整篇 raw 里 `site` 这个词出现 0 次**）：正文 `## Examples` 那张表只有**一个** `Tester Channel` 列（`10104`）——**图说明那张表被压平过**（`Site 1` / `Site 2` 这两个字符串在本篇 raw 里也 grep 不到）。
- 图上看得见的 15 行：`CP`(No 12) / `DS7`(18) / `DS0`(11) / `S1`(19) / `S0`(1) / `MR`(9) / `Q7`(17) / `Q0`(8) / `I/O7`(16) / `I/O6`(4) / `I/O5`(15) / `I/O4`(5) / `I/O3`(14) / `I/O2`(6) / `I/O1`(13)。**`Type` 是 `i` 六个、`o` 两个、`io` 七个；`Mode` 全是 `std`；`HW` 全是 `PS1600`；`Scaling[V/A]` / `Connection Set` / `Comment` 三列全空。**（`PS1600` 这个值正文里列过；**`10509` / `10609` / `Site 1` / `Site 2` 这些在 raw 里是 0 次**。）
- **注意图上这份配置不是正文那张示例表**：正文 `## Examples` 那张表是 `Vdd_1` / `Vdd_2` 两行（DC Scale，`dc` + `SIG`）；**图上 15 行全是数字 pin**（`i` / `o` / `io`）。**所以图上 `Scaling[V/A]` 全空，不能拿来反驳「`Scaling` 只对 `CMON` 有意义」**——那份配置里本来就没有 `CMON`。

**（推断）这张图与 [[pin-configuration-file]] 那篇的多 port 例子像是同一个器件。** 依据：图上这 15 个 pin 名与那篇 `DFPT` 例子里的 pin 名**逐个对得上**（那篇多一个 `IO0`），而且图上 `CP` 的 `No` 是 `12`，那篇例子里 `DFPN 10102,"12",(CP_1)` 的 `No` 也是 `12`。**但两处的 Tester Channel 不同**（图上 `10509`/`10609`，那篇是 `10102`/`10302`），**所以这只是推断：同一个器件、两份不同接线的配置——「同一器件」没有被任何一句话说过。**（那篇不在本页 `sources` 里；本页只核了这几个名字，见「出处」。）

**这张图答不了的**：它对 `Scaling` 的取值、`CMON` 长什么样、`UTIDC` 针长什么样**都不给**（图上没有任何一行是 `CMON` 或 `UTIDC`）；**它是一次具体配置的截图，不是格式规范**——**「哪列必填、哪些组合非法」图答不了。**

### 九个列，分成两类

原文把列分成了**两组**，这个分法本身是信息：

> 「In the pin configuration area, the **Name**, **No**, and **Type** parameters **configure the
> DUT pins**. The **Mode** and **Tester Channel** parameters **give instructions to the software
> about how it must configure the test system channels**. The **HW** parameter shows the tester
> channel hardware information. The **Connection Set** parameter adds the ability to sequentially
> reuse DC Scale channels in other pin definitions.」

| 类 | 列 | 性质 |
|---|---|---|
| **描述 DUT 那一侧** | `Name` / `No` / `Type` | 你在描述「DUT 上这是根什么针」 |
| **指挥测试系统那一侧** | `Mode` / `Tester Channel` | 你在说「软件该把系统通道配成什么」 |
| **回报** | `HW` | **只读**，系统告诉你配到了什么硬件 |
| **其它** | `Connection Set` / `Comment` | 见下 |

**这个分法有用**：`Type` 是 `dc` 而 `Mode` 是 `SIG` 这种组合，
一边是「DUT 侧分类」、一边是「系统侧模式」，**两列不是一回事**。

### 逐列（原文那张表）

| 列 | 关键内容 |
|---|---|
| **`Name`** | 描述性且**唯一**的名字。**最多 64 个字母数字字符**。**不允许的字符**：`# ; ( ' ' ) ? @ ,`。**另外不建议用 `< >`**——原文：`as it will not be possible to save the Pattern Debug Tool configuration layout using these` |
| **`No`** | **可选**。DUT 封装上的针号 |
| **`Type`** | `off` / `i` / `o` / `io` / `dc` |
| **`Mode`** | `std` / `fast` / `SIG` / `CMON` |
| **`Scaling`** | **只对 `CMON` 有意义**：XPS256 电流监视输出的缩放系数，**单位 V/A** |
| **`HW`** | **不可编辑**。显示 `PS1600` / `PS5000` / `DCS-DPS128HC, XPS256` / `DMM` |
| **`Connection Set`** | **可选字符串**；原文一句：`This parameter is currently not supported.` |
| **`Comment`** | 可选字符串，自由描述 |
| **`Tester Channel`** | 见下（本节最长的一块） |

**`Type` 的五个取值**（原文）：`off` = `No pin type set.`；
`i` = 输入；`o` = 输出；`io` = 双向（`You can receive or drive a signal on this pin at any time
during the test.`）；`dc` = **两种东西之一**——`A DC Scale pin in PMU operating mode` 或
`a utility DC pin`。

**`Mode` 的四个取值**（原文）：

| 值 | 原文 |
|---|---|
| `std` | `Set the channel to standard mode for digital channels.` |
| `fast` | `Set the channel to fast mode for Pin Scale 5000 channels.` |
| `SIG` | `Set the channel to PMU operating mode for DC Scale pins.` |
| `CMON` | `The pin is configured as current monitor output. **This mode applies only to XPS256 pins.**` |

**`HW` 的四个可能值说明「这个编辑器管哪些硬件」**：
`PS1600`（Pin Scale 1600 数字通道）/ `PS5000`（Pin Scale 5000 数字通道）/
`DCS-DPS128HC, XPS256`（DC Scale 通道）/ `DMM`（Utility DC pin）。

### `Tester Channel`：五位数怎么读

**这是本页最实用的一段**。原文：

> 「The software uniquely identifies each channel in the system using a **five-digit channel-ID**.
> The syntax for the channel specification of an IO channel is **aaabb** where:」
> - 「**aaa**: The physical pogo block number (range **101 ... 132, 201 ... 232, 301 ... 332 and
>   401 ... 432**) or a virtual pogo block number.」
> - 「**bb**: The channel number (range **01 ... 16**).」
>
> 「For example, **10301** refers to the channel 01 of the pogo block 103.」

| 位 | 含义 | 范围 |
|---|---|---|
| `aaa`（前 3 位） | pogo block 号（或虚拟 pogo block 号） | 101..132 / 201..232 / 301..332 / 401..432 |
| `bb`（后 2 位） | 块内通道号 | 01..16 |

**Utility DC 针是另一套写法**：`UTIDC` + 三位数字（utility block 号）——
原文：`For Utility DC pins the channel id is UTIDC, followed by a three digit number,
specifying the utility block of the card cage.`

### ganging 规则（原文 `Tester Channel` 那一格里最长的一块）

**先看总规则**（原文，**注意这条只适用于 DC Scale**）：

| 规则 | 原文 |
|---|---|
| 组内顺序 | **除 XPS256 外**，只能并**同一张 DC Scale 卡内的连续通道** |
| 最短链 | `The gang chain can start at any channel and have a minimum of 2 successive channels.` |
| 怎么写范围 | **`-`（连字符）** 或 **`,`（逗号）** 逐个列 |
| 谁是 master | **序列里第一个通道自动是 master，其余是 slave** |

**再分卡看**：

- **`DPS128` / `DPS64`**：`Ganging is possible for any number of successive channels within a
  card, **but not across cards**.` + **通道必须是同一类型（HC 或 HV）**。
- **`XPS256`**：**不适用上面那套**，原文把规则**外链**到
  `XPS256 ganged` 的 `Ganging characteristics` 一节（**那篇本页没读**）。
  这解释了为什么总规则里那两条都写着 `With exception of XPS256`。

**一条“静默行为”**（**本页最该记住的一条**）：

> 「Note that on **DPS128/64 and XPS256** you **cannot execute a current compare on a ganged group
> of channels in unganged mode**. Already activated comparators are **silently disabled** in unganged
> mode. **A user notification (Error or warning) is omitted in this case, to avoid any interrupt in
> the testflow.** The previous state of the comparators is automatically restored after the ganged
> group has been restored.」

**三个要点**：① 不报错、不警告；② 比较器被**静默**关掉；
③ 恢复 ganged 之后**自动恢复**原状态。
——**原文明确写了「故意不通知」的理由：避免打断 testflow。**

## 典型用法

**原文没有 `## Procedure` / `## Before you begin` 段。** 从正文能拼出这条链：

1. **在右上角的 `CONTEXT` 下拉里选 mode context**（context 本身用 [[ctxt]] 建）。
2. **填 `Name`**（唯一，≤64 字母数字，避开禁用字符）。
3. **填 `Type`**：数字针 `i` / `o` / `io`；DC Scale（PMU）或 utility DC 针填 `dc`。
4. **填 `Mode`**：数字针 `std` / `fast`；**DC Scale（PMU）针必须是 `SIG`**；
   `CMON` 只给 XPS256，并在 `Scaling` 里给 V/A 系数。
5. **填 `Tester Channel`**：五位数 `aaabb`（或用 `UTIDC`+三位数）；
   **要 ganging 就写 `10105-10106` 这种连续区间**（第一个自动当 master）。
6. **`HW` 列自己会显示**配到的硬件（不可编辑）。

**两条硬约束（原文直接给的）**：

- **DC Scale 针在 PMU 模式下，`Type` 必须是 `dc`、`Mode` 必须是 `SIG`**——
  原文在 `## DC Scale pin (PMU mode) setup` 一节里两句话各说一遍：
  `For a DC Scale pin in PMU operating mode, the parameter must be dc.` /
  `For a DC Scale pin in PMU operating mode, it must be SIG.`
- **ganging 的链最短 2 个连续通道**，且**除 XPS256 外不能跨卡**。

**原文 `## Examples` 给的配置样例**（**在「语法 / 参数」节里逐字有**）：

| Name | Type | Mode | HW | Connection Set | Comment | Tester Channel |
|---|---|---|---|---|---|---|
| `Vdd_1` | `dc` | `SIG` | `DCS-DPS128HC` | | | `10104` |
| `Vdd_2` | `dc` | `SIG` | `DCS-DPS128HC` | | | `10105-10106` |

**读这张表能读出三件事**：① PMU 的 DC Scale 针就是 `dc` + `SIG`；
② ganging 写成 `10105-10106`（连字符）；
③ `Vdd_2` 这一行占了**两个通道**——**一行可以对应多个 tester channel**。

原文另有一段 `### Utility DC pin setup`，**只有一张图**（`355197.png`），**没有文字说明**。
**这张图现在读了（④ 图证）——它就是那个缺口的答案。** 整张图只有**一行**，逐格读出来是：

`Name`=`DMM 1`、`No`=`1`、`Type`=`dc`、`Mode`=`std`、`Scaling[V/A]`=**一格灰块**（同一行其它格是白底）、
`HW`=`DMM`、`Tester Channel`=`UTIDC165`（`Tester Channel` 那一格在图上只有 `Site 1` 一个子列）。

**这一行答掉三件事**（**这些字在 raw 里 grep 不到，除了 `dc` / `std` / `DMM` 三个词本身**）：

1. **`dc` 的另一支走 `Mode`=`std`，不是 `SIG`。** 正文只在 `## DC Scale pin (PMU mode) setup` 那一节里说过
   DC Scale（PMU）针的 `Mode` 必须是 `SIG`；**utility DC 针这一支，图上写的是 `std`**——
   所以「`dc` + `SIG`」这一对**只属于 PMU 那一支**。上面「典型用法」第 4 条那条硬约束**本来就只写给 PMU**，
   **图这一行补上的正是它没讲的那一支的取值：`dc` + `std`。**
2. **`HW` 列在这里是 `DMM`**——与正文那句 `DMM: Utility DC pin` 对上了（**这是本页唯一一次看见 `DMM` 出现在它该出现的那一行上**）。
3. **`Tester Channel` 写成 `UTIDC165`**——`UTIDC` + 三位数，与正文那句写法完全一致（**`UTIDC165` 这个值在 raw 里 grep 不到**）。

**这张图答不了的，照实说**：它只有一行、没有文字，**「`UTIDC` 后面那三位数怎么取」「一个 utility DC 针还能不能配别的列」「`Scaling[V/A]` 那一格为什么是灰块」图上都没有**——**本页不猜那个灰块是不是「不可用」**（图上没有灰块的图例）。

## 和谁有关

- [[conf]] — **同一件事的命令行版本**。本编辑器里的 `Type` / `Mode` / `Tester Channel`
  落到命令上就是 `CONF` 的 `pin_type` / `pin_oper_mode` / `pinlist`
  （推断：`Type` 的 `i`/`o`/`io`/`dc`/`off` 与 `CONF` 的 `I`/`O`/`IO`/`DC`/`OFF`
  **逐项对应，只差大小写**；`Mode` 的 `SIG` 对应 `CONF` 的 `DCSIGNAL`——
  **这一条对应关系原文没有写，是推断**）
- [[ctxt]] — **前置**。`CONTEXT` 下拉里那个 context 要先存在
- [[dfpn]] — **同一批针的另一条定义路径**。`DFPN` 给 DC Scale 通道分配针名并置为 PMU 模式，
  **正是本页 `dc` + `SIG` 那两列的等价物**（推断，依据是 `DFPN` 那篇写的
  `The DC Scale channel will be in PMU mode by this allocation.`）
- [[dc-scale-xps256-card]] — **`CMON` 与 `Scaling` 两列只为它存在**。原文：
  `This mode applies only to XPS256 pins.`
- [[dps128-dps64-cards]] — **ganging 规则单独点名的一张卡**（卡内可以、跨卡不行、同类型 HC/HV）
- [[ganging]] — **本页有一整块 ganging 规则**（含那条「静默关比较器」）
- [[cross-card-ganging-requires-ddic]] — **跨卡 ganging 的前提**（**那页本页没读**）。
  **⚠️ 本页只写了「DPS128/64 不能跨卡」和「XPS256 另见」，
  没有写「跨卡需要 DDIC」**——**那是别的页的事，本页不引**
- `Pin Scale 1600` / `Pin Scale 5000` / `DCS-DPS128HC` / `DMM`（**均未建**）—
  `HW` 列能显示的四种硬件；**本页对它们只有名字**
- `DC Scale pin (PMU mode)` / `Mode contexts`（**均未建**）— **本页正文里两个被链出去的 raw 页**
  （`02.05.05.05_PMU_operating_mode_of_DC_Scale_cards.md`、
  `02.06.03.01.03.01_Mode_contexts.md`），**都没读**
- `XPS256 current monitor`（**未建**）— `Scaling` 列服务的那个输出；**没读**
- `Pattern Debug Tool`（**未建**）— `Name` 里禁用 `< >` 的理由和它有关（原文给的理由）；**没读**
- `DUT interface layout`（**未建**）— 原文 `## Related information` 唯一指向，**没读**；
  `Tester Channel` 里那句 `or a virtual pogo block number` 的详解在那边
- [[utility-pins-editor]] / [[dps-pins-editor]] — **同 `stage: pin` 的 GUI 侧页**。
  **本页明确只管「数字针 + PMU 模式的 DC Scale 针」**，
  所以 `dps-pins-editor` 从名字上看像是 DPS 模式那一边的对应物——
  **但本页的原文没有任何一句提到它**（推断，仅指关系）
- [[pin-configuration-tool]] / [[pin-configuration-file]] — **同一份 pin configuration 的另一侧**
  （GUI 工具 / 落盘文件）；**本页没读它们，不替它们说话**（推断，仅指关系）

## 版本

原文 `## Functional changes` **十二条**：

- **`Introduced in SmarTest 6.5.0`**
- **SmarTest 7.1.3**：`Changed the parameter Instrument to HW.`
- **SmarTest 7.1.3**：`Removed the parameter Ser.R[ohm].`
- **SmarTest 7.1.3**：`Added the HV mode option.`
- **SmarTest 7.2.0**：`Modified pin name length.`
- **SmarTest 7.3.1**：`New parameter "Connection Set".`
- **SmarTest 7.3.1**：`DC Scale PVI8 card added.`
- **SmarTest 7.4.0**：`DC Scale AVI64 card added.`
- **SmarTest 7.5.0**：`DC Scale FVI16 card added.`
- **SmarTest 7.10.0**：`PVI8 not supported, HV mode option not supported`
- **SmarTest 7.10.1**：`DC Scale XPS256 card added.`
- **SmarTest 7.10.2**：`XPS256 current monitor: New option "CMON" for "Mode" column and new "Scaling" column.`

**四条必读：**

1. **第一条不是哨兵值**（不是 `Introduced before SmarTest 6.3.2`）——
   **它是一条真版本事实：这个编辑器是 SmarTest 6.5.0 引入的。**
2. **7.3.1 到 7.5.0 连着三条「加了一张卡」**（PVI8 → AVI64 → FVI16），
   **7.10.0 又把 PVI8 收回去**（`PVI8 not supported, HV mode option not supported`）——
   **同一段里「加」和「撤」都有，而且是两条独立条目。**
3. **`7.10.2` 那条和正文完全对得上**：`Mode` 列的新取值 `CMON` 与新的 `Scaling` 列，
   正文里都在，且 `CMON` 明写 `applies only to XPS256 pins`。
   **这是本篇版本记录与正文自洽的一条。**
4. **`HV mode option` 在 7.1.3 加、7.10.0 撤**，而**正文的 `Mode` 列表里根本没有 `HV`**——
   **所以正文反映的是 7.10.0 之后的状态**（推断）。
5. **（2026-09-20 补 · ④ 图证）两张界面图正好卡在 7.1.3 这条改动的两侧。**
   本篇的 `355141.png` 上有 `HW` 列、**没有** `Ser.R[Ohm]` 列；而
   `02.08.04.18.04_Pin_configuration_file.md` 那篇的界面图 `21671.png` 上**有 `Ser.R[Ohm]` 列（值 `0.0`）和 `Instrument` 列**。
   7.1.3 记的两条正是 `Changed the parameter Instrument to HW.` 与 `Removed the parameter Ser.R[ohm].`
   ——**那两处改动在图上看得见：一张图一个列集。**（**另记一处大小写不一致**：raw 里写的是 `Ser.R[ohm]`，
   而图上那列表头是大写 `Ser.R[Ohm]`。`21671.png` 不是本页 `sources` 里的图，本页只在这一点上引它，见「出处」。）

## 出处

`sources:` 一篇：
`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01.02_Digital_Pins_editor.md`
（`105634.htm`，6,801 字节，105 行）——**整篇读完**。

**本页做了什么（2026-09-20 更新，「两张图都没看」那条是错的，已删）**：

- **两张图都看了，逐张打开过**：`355141.png`（Digital Pins editor 界面）、`355197.png`（Utility DC pin setup）。
  **图片路径 `../../../../raw/x.png` 往上四层正好是 `tdc-html/`，图就在那儿**（`schema.md` §11.4）——
  **本页原先写的「两张图都没看 / 没有任何来自图的结论」现在不成立了。**
- **图答掉的东西写进了正文**：① 界面与列结构、`Tester Channel` 被拆成 `Site 1` / `Site 2` 两个子列（「是什么」）；
  ② utility DC 针那一行的逐格取值 `dc` + `std` + `DMM` + `UTIDC165`（「典型用法」）；
  ③ 两张图卡在 7.1.3 前后两侧（「版本」第 5 条）；④ `Name` 格里的空格与正文打架（瑕疵⑨）。
- **图里读到的字一律没有进 `>` 引文块。** 引文块的含义是「这段能在 raw 文本里搜到」；
  **图上的字搜不到**，所以它们只出现在正文和表格里；**瑕疵⑨ 整条都是图证，被特意放在那个 `>` 块外面**，标题里写明了理由。逐个核过（`grep -F`）：
  `DEFAULT` / `Site 1` / `Site 2` / `10509` / `10609` / `UTIDC165` / `DMM 1` 在本篇 raw 里**都是 0 次**；
  `PS1600` 与 `Ser.R` **是**搜得到的（分别在 `HW` 那个值列表和版本行里），**所以那两个不算图证**。
- **图答不了的照实写了，没有硬填**：界面图是一次具体配置的截图，**「哪列必填、哪些组合非法、
  `Scaling` 那个灰块是什么意思、`UTIDC` 后面三位数怎么取」图都不给**；
  **本篇也没有第二张界面图可比。**
- **为核两件事，本页另外读了一篇不是 `sources` 的文档**：
  `02.08.04.18.04_Pin_configuration_file.md`（它的界面图 `21671.png` 用来对照 7.1.3 那条版本记录，
  它的多 port 例子用来核 `355141.png` 里那组 pin 名）。**只在「版本」和「是什么」里点名单条事实，
  没有并入正文**；用到的地方**都标明了那不是本篇的东西**。

**本页没做的**：

- **「语法 / 参数」节只收了 399 字符**（**全篇 8,972 字节**）——
  它只抓到了 `## Examples` 那一节（两张表 + 一张图）。
  **`## Parameters` 那张大表（九个列的全部说明）没有进语法节**，
  所以本页正文里那张逐列表**是我从 raw 转述的，不是逐字**；
  凡加 `>` 引号的地方才是逐字原文。
- **`DUT interface layout`（`## Related information` 唯一指向）没读**——
  所以 `Tester Channel` 里那句 `or a virtual pogo block number`
  **具体有哪些虚拟块号，本页没有**。
- **`02.05.05.05_PMU_operating_mode_of_DC_Scale_cards.md` 没读**——
  `Mode` 列里 `SIG` 那一条链向它，**PMU 模式的完整语义本页没有**。
- **`02.06.03.01.03.01_Mode_contexts.md` 没读**——mode context 的总纲。
- **`XPS256 current monitor` 没读**——**`CMON` 的实际输出与 `Scaling` 怎么取值，本页只有名字。**
- **`XPS256 ganged` 那一节的 `Ganging characteristics` 没读**——
  **⚠️ 这是本页最大的缺口**：总 ganging 规则里两条都写着 `With exception of XPS256`，
  **而 XPS256 自己那套规则被外链出去了，本页一个字都没有。**
- **`Connecting DPS channels in parallel`（DUT 板设计规则侧）没读。**
- **`dc` 类型里「utility DC pin」那一支，原文只给了一张图、没有文字**——
  **图现在读了**（`355197.png`，取值见「典型用法」）；**但「`UTIDC` 那三位数怎么取」「还有哪些列能配」图上也还是没有**，
  **本页仍然只有「`UTIDC`+三位数」这一条来自文字的规则。**
- **`## Parameters` 表里 `Name` / `Type` / `Mode` 等格的原始表格结构本页没有逐字引**——
  需要逐字时请看 raw。

> ⚠️ **本篇的语料瑕疵，照实记、一处没替它改**：
> ① **`Connection Set` 在同一篇里自相矛盾**：
>    开头那段说它
>    `adds the ability to sequentially reuse DC Scale channels in other pin definitions`
>    （**说它能用**），而参数表里那一格只有一句
>    `This parameter is currently not supported.`（**说它不支持**）。
>    **同一篇文档里两种说法。**
> ② **禁用字符清单里的 `' '` 读不通**：原文
>    `Spaces and the following characters are not allowed:` 下一行是
>    `- # ; ( ' ' ) ? @ ,`
>    ——**清单里出现了 `' '`（两个单引号夹一个空格）**。
>    按上下文（这一行是「不允许的字符」）**原意应是双引号和单引号两个字符**
>    （即 `" '`），**语料把它们渲染成了 `' '`**。**本页照抄，不替它改。**
> ③ **`#` 也说「不允许」，而「Spaces」在同一句里已经被点名**——
>    这句的清单里到底哪些是「空格」哪些是「字符」，原文分不清（推断）。
> ④ **一个小标题丢了自己的行**：raw 里那一段逐字是
>    `  Ganging of DC Scale channels Unless otherwise defined below, the following rules are to be
>    followed for defining ganging groups:`
>    —— **`Ganging of DC Scale channels` 是本该独立成行的小标题，**
>    **它和后面的句子被拼成了一行**（中间只有一个空格）。**原文如此。**
> ⑤ **两个坏字组合（§11.2① 那类编码损坏）**，**同一篇里出现三处**：
>    - `The CONTEXT drop鈥慸own list` —— `鈥慸` = **`‑d`**，所以是 **`drop-down`**
>    - `using a five鈥慸igit channel鈥慖D` —— `鈥慸` = `‑d`、`鈥慖` = **`‑I`**，
>      所以是 **`five-digit channel-ID`**
>    **⚠️ 拿 `drop-down` 去 raw 里搜是搜不到的，要搜 `drop鈥慸own`**（§11.2① 的处置）。
> ⑥ **`The pin is configured to either to drive a digital signal…` —— `to` 出现两次**：
>    原文逐字 `The pin is configured to either to` / `drive a digital signal to the DUT … or to` /
>    `connect a PMU channel …`。**同一句里 `to` 重复。**
> ⑦ **7.2.0 那条版本记录只说 `Modified pin name length.`**，
>    **没有说改成多少**——而正文写的是「最多 64 个字母数字字符」。
>    **两处对不上「改动前是多少」（推断）**；
>    另外正文没写 32 位系统上的限制是多少（对照：[[dfpn]] 那篇写了
>    `Maximum number of characters is 16 for 32-bit SmarTest and 64 for 64-bit SmarTest.`
>    —— **但那不是本篇的句子**）。
> ⑧ **`## Examples` 那两张表里 `Connection Set` 和 `Comment` 列全是空的**——
>    而 7.3.1 版本记录说 `Connection Set` 是**新加的**参数。
>    **示例没有演示它**（推断）。

**⑨（这一条是 ④ 图证，所以故意不放进上面的 `>` 块——引文块的含义是「这段能在 raw 文本里搜到」，而图上的字搜不到）**
**`355197.png` 那一行的 `Name` 格带一个空格，正文却说空格不允许。**
逐格读出来是 `DMM` + 一个空格 + `1`（把原图放大到 9 倍核过，**那不是下划线**：
下划线会画成贴着基线的一横，图上那处是齐腰的空白）。而正文写的是
`The pin name can have up to 64 alphanumeric characters. Spaces and the following characters are not allowed:`
——**图和它自己这篇文档的正文，在「pin 名里能不能有空格」这件事上对不上。**
**原文没有解释**，也没说那张图是哪个版本截的；**本页两处并列记下，不替它判定哪一处是对的。**
这一条和上面 ②③ 落在同一段文字上，但**性质不同**：**②③ 说的是那份禁用字符清单本身读不通，这一条是图和正文打架。**

`verified: doc-only`
