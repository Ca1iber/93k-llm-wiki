---
type: object
title: DPS Pins editor
layer: gui
stage: pin
tags: [pin, gui, dps, dc-scale, pin-configuration, tester-channel]
related: [pin, pin-configuration-tool, pin-configuration-file, digital-pins-editor, utility-pins-editor, mapping-pin, dfps, dps128-dps64-cards, dc-scale-xps256-card, dc-scale-limits-editor]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01.03_DPS_Pins_editor.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# DPS Pins editor

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **95 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01.03_DPS_Pins_editor.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example

See `DC Scale pin (DPS mode) setup`（raw: `02.08.04.18.03.01.03.01_DC_Scale_pin__DPS_mode__setup.md`）

<!-- 语法节 end -->

## 是什么

**DPS Pins editor 是给 DPS 通道（直流电源针）配针的 GUI。**
一根 DPS 针在这里拿到**名字、极性、负载电容**，并绑到一个 DPS 通道上；
`HW` 那一列再把「实际配到了什么硬件」回报给你。

**先说一条结构事实：本篇 raw 没有一句定义这个编辑器是干什么的。**
开门第一句就是那张参数表的引子：

> 「The following table describes the parameters of DPS Pins editor.」

**所以「这是什么」只能从六个列各自的说明里读出来**（推断）。能当依据的只有四句：
`Pol` 那句（`This specifies the polarity of the DPS pin`）、
`Tester Channel` 那句（`Specify a DPS channel.`）、
`HW` 那句（`In the DPS Pins editor, the following items may be displayed:` 加三个值）、
以及 `Name` 那句（别的 SmarTest 窗口用这个名字指这根针）。
**加起来的职责就是：把 DPS 通道绑成一根有名字、有极性的 DUT 针。**

### 六个列

**这张表是我从 raw 的散文里转述的，不是逐字**——原表**没有进本页的「语法 / 参数」节**
（脚本只收了 `## Example`，见「出处」）。凡加 `>` 的才是原文。

| 列 | 原文要点 |
|---|---|
| **`Name`** | 描述性名字，**最多 16 个字母数字字符**；空格与 `# ; ( ' ' ) ? @ ,` 不允许。别的窗口引用这根针时显示的就是它 |
| **`Pol`** | **极性**。原文只给了一个取值 `POS`——**另一个取值是什么，本篇一个字没写** |
| **`C[uF]`** | **负载电容**。「留空还是填，看是哪种 DPS」——判据**不在这篇里**，被推给两篇 Subtopics |
| **`HW`** | **不可编辑**。填了 tester channel 之后自动显示该通道的硬件信息。本篇列出的可能值：`DCS-DPS128HC` / `DCS-UHC4T` / `DCS-XPS256` |
| **`Comment`** | 可选描述 |
| **`Tester Channel`** | **指定一个 DPS channel。原文对它的全部说明就是这一句。** |

三句用原文说清：

> 「The pin name can have up to 16 alphanumeric characters. Spaces and the following characters are not allowed:」

> 「Other SmarTest windows will always display the Pin name when they refer to a pin of the DUT.」

> 「This column is not editable. After you enter the tester channel, it automatically shows the hardware information of this channel. In the DPS Pins editor, the following items may be displayed:」

`C[uF]` 那一格原文是：

> 「The load capacitance. Either keep this field blank or fill it in depending on the DPS.」

**后半截就是它绕开判据的办法**——`depending on the DPS` 指的是哪篇，原文紧接着给了两条链接
（`Load capacitance connected to the DC Scale DPS128/DPS64` 与
`Load capacitance connected to the DC Scale XPS256`），**那两篇本页没读**。

### 本篇没写的：`Tester Channel` 那五位数怎么读

图上（下节）填的是 `22510` / `22504` 这样的**五位数**，
而本篇正文对它的全部说明只有 **`Specify a DPS channel.`** 一句——
**前三位是什么、后两位是什么、合法范围是多少，本篇一个字没有。**

对照：[[digital-pins-editor]] 那篇有完整的一套（`aaabb`，前三位 pogo block、
后两位块内通道号，并给了四组 pogo block 号范围与块内通道号的范围）。
**本页不把那套搬过来**——**那是数字通道的读法；DPS 通道是不是同一套，本页没有依据。**

### 界面长什么样（④ 图证 · `354609.png`）

原文在参数表前挂了一张界面图（`354609.png`，alt 文字就是 `DPS Pins editor`，原图 578 × 191）。
**逐格读过**，它答掉的是三件事：

- 窗口上**一个 tab，标题 `DPS Pins`**；表头从左到右是行号、`Name`、`Pol`、`C[uF]`、`HW`、`Comment`、
  `Tester Channel`——**与正文那张表的六个列名逐个对得上**，**没有 `NO`、没有 `Type`、没有 `Mode`**。
- **`Tester Channel` 那一格被拆成两个子列：`Site 1` 与 `Site 2`**——
  **本篇正文一个字没写这件事**（正文只有 `Specify a DPS channel.`）。
  更关键的是：**同一根针在两个 site 上填的是两个不同的值**——图上第 1 行 `PWR` 是 `22510` / `22511`。
- 图上三行逐格读出来是：
  `PWR` / `POS` / `1.0` / `DCS-DPS128HC` / 空 / `22510` / `22511`；
  `VCC 1` / `POS` / `2.3` / `DCS-DPS128HC` / 空 / `22504` / `22502`；
  `VCC 2` / `POS` / `2.3` / `DCS-DPS128HC` / 空 / `22501` / `22505`。

**哪些字算图证，逐个 `grep -F` 核过**：`Site 1` / `Site 2` / `PWR` / `VCC 1` / `VCC 2` /
`22510` / `22511` / `22504` / `22502` / `22501` / `22505` / `2.3`
**在本篇 raw 里都是 0 次**；而 `DCS-DPS128HC`、以及六个列名本身**是搜得到的**——
**所以列名和 `DCS-DPS128HC` 不算图证**，只有上面那串算（§11.4 要的就是这条分界：
**拿图里的字回 raw 数一遍，能搜到的不算图证**）。

**图答不了的，照实说**：这张图是**一次具体配置的截图，不是格式规范**——
「哪列必填、`C[uF]` 什么时候留空、`22510` 怎么读成通道」图上都没有；
图上**只有 `DCS-DPS128HC` 一种卡**，所以 `HW` 另外两个值（`DCS-UHC4T` / `DCS-XPS256`）长什么样图不给；
`Comment` 列三行全空。

## 典型用法

**原文没有 `## Procedure` / `## Before you begin` / `## What to do next` 段**，
`## Example` 一节也只有一句 `See DC Scale pin (DPS mode) setup`——**指向的那篇本页没读**。
所以下面这条链是**从六个列的说明里拼的**（推断），**顺序即原文列序**：

1. **填 `Tester Channel`**：一个 DPS channel，**每个 site 一格**（④ 图证）。
   填完之后 `HW` **自己就会显示**硬件信息——**这一步不用你做**。
2. **填 `Name`**：≤16 个字母数字字符，**避开 `# ; ( ' ' ) ? @ ,` 与空格**。
   ⚠️ **图上那两行 `VCC 1` / `VCC 2` 的针名里就有空格**——和这条规矩打架（见「出处」⑤）。
3. **填 `Pol`**：原文只给了 `POS`。
4. **决定 `C[uF]`**：留空还是填，**判据在两篇 Subtopics 里，本页没有**。
5. **`Comment` 可选。**

**最后一步是「用」**：DPS 针在 testflow 里是**被通电的那一根**——
但**这一步的文档不在这里**：`C[uF]` 的物理含义在负载电容那两篇，
命令侧在 `02.06`，DC Scale 的电压/电流限值在 [[dc-scale-limits-editor]]。
**本页只到「针配好了」为止。**

## 和谁有关

- [[pin-configuration-file]] — **同一份配置的落盘侧**。GUI 里填的东西写进
  `<device_dir>/configuration` 下的 pin 配置文件——**这两句不是本页 raw 的句子**，
  来自 [[mapping-pin]] 的对照表；**本页没有回那篇原文核**。
- [[mapping-pin]] — 那张对照表把本编辑器排在**「把 DPS channel 绑到器件 pin，并给极性」**那一行：
  GUI 侧是本页、文件侧是 [[pin-configuration-file]]、L1 侧是 [[dfps]]。
  **⚠️ 那张表另有一行（DPS128/DPS64 与 XPS256 的负载电容）把 GUI 格写成
  「DPS Pins 表的 `Load Capacitor [uF] / V-Ramp [us]` 列」——这个列名在本页上已经不成立了**：
  本页的 `## Functional changes` 明写
  `SmarTest 7.1.3: Changed the parameter Load Capacitor [uF]/V-Ramp [us] to C[uF].`，
  正文表与图（`354609.png`）上也都是 **`C[uF]`**。
  **本页照 7.1.3 之后的列名记**（见「版本」第 1 条）；
  另外**那句话在 raw 里斜杠两侧没有空格**（`[uF]/V-Ramp`），**那张表里多加了两个空格**。
- [[dfps]] — 命令侧。**`DFPS` 这个词在本页 raw 里出现 0 次**，
  所以那条对应**本页既不背书也不否认**（依据只在 [[mapping-pin]] 上）。
- [[digital-pins-editor]] — **同一族的另一个编辑器，范围正好互补**。
  那篇把自己的范围写死成「数字针 + **PMU 模式**的 DC Scale 针」，
  而名字上看 DPS 模式那一边就该是本页——**但两篇文档互相都没提对方**（推断，仅指关系）。
  差别的形状看得出来（下面每一条都只取自 [[digital-pins-editor]] 那一页，**本页没有读它的原文**）：
  那页有 `NO` / `Type` / `Mode` 三列和五位数的读法，**本页六列、没有那三列、也没写五位怎么读**。
- [[utility-pins-editor]] — 同 `stage: pin` 的同族 GUI 编辑器。
- [[dc-scale-limits-editor]] — 同族里管 DC Scale **电压/电流限值**的那一页；
  **它管「限值」，本页管「针」**（关系来自 [[mapping-pin]]，**本页没读那篇**）。
- [[dps128-dps64-cards]] / [[dc-scale-xps256-card]] — `HW` 列能显示的三种硬件里的两种
  （第三种 `DCS-UHC4T` 在本 wiki 里没有页）。
- **三篇 Subtopics 一篇没读**：`DC Scale pin (DPS mode) setup`、
  `Load capacitance connected to the DC Scale DPS128/DPS64`、
  `Load capacitance connected to the DC Scale XPS256`——
  **`C[uF]` 的判据、以及 `## Example` 指的那个完整例子，都在那边。**

## 版本

原文 `## Functional changes` **九条**，条目逐字：

- `Introduced in SmarTest 6.5.0`
- **SmarTest 7.1.3**：`Changed the parameter Polarity to Pol.`
- **SmarTest 7.1.3**：`Changed the parameter Load Capacitor [uF]/V-Ramp [us] to C[uF].`
- **SmarTest 7.1.3**：`Changed the parameter Instrument to HW.`
- **SmarTest 7.3.1**：`DC Scale PVI8 card added.`
- **SmarTest 7.3.2**：`DC Scale UHC4T card added.`
- **SmarTest 7.4.0**：`DC Scale AVI64 card added.`
- **SmarTest 7.5.0**：`DC Scale FVI16 card added.`
- **SmarTest 7.10.1**：`DC Scale XPS256 card added.`

**三条必读：**

1. **7.1.3 一口气改了三处列名**：`Polarity` → `Pol`、
   `Load Capacitor [uF]/V-Ramp [us]` → `C[uF]`、`Instrument` → `HW`。
   **所以凡是拿 `Polarity` / `Load Capacitor [uF]` / `Instrument` 当本编辑器列名的地方，
   描述的都不是 7.1.3 之后的界面**——本 wiki 面向 **SmarTest 7.10.3**（§11）。
   本页的图 `354609.png` 上写的是**新名**（`Pol` / `C[uF]` / `HW`），
   **所以那张图是 7.1.3 之后的**（推断：图上三列与正文表逐字一致，而正文表用的是这三条改动之后的名字）。
2. **「加卡」这一串只列到 7.10.1**（PVI8 → UHC4T → AVI64 → FVI16 → XPS256），
   而正文 `HW` 那一格**只给了三个显示值**（`DCS-DPS128HC` / `DCS-UHC4T` / `DCS-XPS256`）——
   **PVI8 / AVI64 / FVI16 三张卡在正文里没有对应的显示值**（⚠️ 见「出处」①）。
3. **第一条不是哨兵值**（不是 `Introduced before SmarTest 6.3.2`）——
   **这个编辑器是 SmarTest 6.5.0 引入的**，是一条真版本事实。

## 出处

`sources:` 一篇：
`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01.03_DPS_Pins_editor.md`
（`105636.htm`，40 行）——**整篇读完**。

**本页做了什么**：

- **读了本页唯一那张图** `354609.png`（界面图，578 × 191），**逐格读过**。
  **图片路径 `../../../../raw/x.png` 往上四层正好是 `tdc-html/`，图就在那儿**（`schema.md` §11.4）。
  图答掉的三件事（`Tester Channel` 按 site 拆列、同一根针两 site 值不同、三行逐格取值）
  写进了「是什么」；**图里读到的字一律没有进 `>` 引文块**——
  引文块的含义是「这段能在 raw 文本里搜到」，**图上的字搜不到**（§11.4）。
- **为了核一句别人写的话，另外开了一张不属于本页 `sources` 的图**：
  `02.08.04.18.04_Pin_configuration_file.md` 的 `105641.png`。
  **只用来判断 [[mapping-pin]] 那一行写的 GUI 列名是不是本编辑器的当前列名**，
  **结论写在「和谁有关」里，没有并入正文**。

**本页没做的**：

- **`## Parameters` 那张表没有进「语法 / 参数」节。** 脚本只收了 `## Example` 一节（95 字符）——
  **所以本页「六个列」那张表是我从散文里转述的，不是逐字**；凡加 `>` 的地方才是逐字原文。
- **三篇 Subtopics 一篇没读**（清单见「和谁有关」）。
  **`C[uF]` 什么时候留空、什么时候填，本页没有答案**；`## Example` 指的那个完整例子本页也没有。
- **`02.06` 的命令原文一篇没读**，`DFPS` 的用法、参数本页一个字没有。
  **本页正文没有一条命令事实。**
- **没有实跑。** 没有在机台上开过这个编辑器、没有生成过 pin 配置文件。
  `verified: doc-only` 指的就是这件事。
- **没有动 `wiki/index.md`**，也没有把本页挂进 `wiki/stages/pin.md`。

> ⚠️ **本篇的语料瑕疵与对不上的地方，照实记、一处没替它改**：
> ① **`HW` 那一格的三个显示值与五条「加卡」记录对不上。**
>    `HW` 格里逐字是 `DCS-DPS128HC, DCS-UHC4T, DCS-XPS256`，
>    而 `## Functional changes` 从 7.3.1 到 7.5.0 加了 **PVI8 / AVI64 / FVI16** 三张卡、
>    7.10.1 又加了 **XPS256**。**PVI8 / AVI64 / FVI16 在 `HW` 格里没有显示值。**
>    两处并列，**本页不替它判定哪一处是全的**。
> ② **`Pol` 那一栏只给了一个取值**：逐字是 `This specifies the polarity of the DPS pin: POS.`
>    ——**`POS` 之外还有什么，本篇没写**（对照 [[digital-pins-editor]] 那篇的 `Mode` 列，
>    那种列是把取值逐个列出来的）。**这是缺口，不是矛盾。**
> ③ **禁用字符清单那一行读不通**：原文逐字是
>    `# ; ( ' ' ) ? @ ,`
>    ——**两个单引号夹一个空格**。按上下文（这一行是「不允许的字符」）
>    **原意应是双引号和单引号**（即 `" '`），**语料把它渲染成了 `' '`**。
>    **同一份清单在同族的 [[utility-pins-editor]] 那篇里渲染成了另一种坏法**
>    （`# ; (鈥? ) ? @ ,`）——**同一份清单在语料里有两种坏法**。**本页照抄，不替它改**（§11.2）。
> ④ **`## Functional changes` 里那句斜杠两侧没有空格**（`Load Capacitor [uF]/V-Ramp [us]`），
>    **本页按 raw 的写法记**；[[mapping-pin]] 引用它时两侧各加了一个空格（见「和谁有关」）。

**⑤（这一条是 ④ 图证，所以故意不放进上面的 `>` 块——引文块的含义是「这段能在 raw 文本里搜到」，而图上的字搜不到）**
**`354609.png` 上两根针的名字里有空格，正文却说空格不允许。**
逐格读出来是 `VCC` + 一个空格 + `1`、`VCC` + 一个空格 + `2`
（**放大到 6 倍核过**：那个间隙与一个字符同宽，不是字形自带的字距）。
而正文写的是 `Spaces and the following characters are not allowed:`——
**图和它自己这篇文档的正文，在「pin 名里能不能有空格」这件事上对不上。**
**原文没有解释**，也没说那张图是哪个版本截的；**本页两处并列，不替它判定哪一处是对的。**
（**同族的 [[digital-pins-editor]] 页在它那篇的图 `355197.png` 上记到了同一类毛病**：
那里的 `Name` 格是 `DMM 1`。）

`verified: doc-only`
