---
type: object
title: DC Scale UHC4T card
layer: n/a
stage: pin
tags: [test-head-card, dc-scale, dps, ultra-high-current, ganging, protection, hardware-view]
related: [dc-scale-xps256-card, dps128-dps64-cards, hardware-view, pin, dc-test-programming, hv-protection]
sources:
  - 02_System_reference/02.05_Test_Head_Cards/02.05.05.02_DC_Scale_UHC4T_card.md
created: 2026-09-18
updated: 2026-09-20
verified: doc-only
---

# DC Scale UHC4T card

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **950 字符逐字取自** `<02_System_reference/02.05_Test_Head_Cards/02.05.05.02_DC_Scale_UHC4T_card.md>` 及其子主题 `<02_System_reference/02.05_Test_Head_Cards/02.05.05.02.04_UHC4T_hardware_overview.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 UHC4T hardware overview）

### UHC4T hardware view

Only the UHC4T supports the Curr Limiter protection option. Therefore, only the DCS-UHC4T hardware view shows this option and the Equation Set and Spec Set fields.

 !`UHC4-T hardware view`（raw: `../../../../raw/146923.png`）

The hardware views are interactive.

The Profile field for example, allows you to measure and display current and voltage waveforms during pattern execution in the Hardware perspective. For details see `Profiling of DC Scale cards with Hardware view`（raw: `../../01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.05.03.05_Profiling_of_DC_Scale_cards_with_Hardware_view.md`）.

The underlying sequences also generate sample test method code for the executed measurement in the Sample Code view. You can directly copy and paste the code from the view into your test method program. For details see `Sample Code view`（raw: `../../01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.05.07_Sample_Code_view.md`）.

<!-- 语法节 end -->

## 是什么

**UHC4T 是一张「超高压电流」的 DPS（device power supply）卡。** 原文第一句：

> 「The DC Scale UHC4T is a device power supply card that addresses your needs for **ultra high
> currents**.」

**规格两句话说完**（原文）：

> 「The DC Scale UHC4T power supply card has **4 channels per card** that provide a maximum current
> of **40 A each (160 A per card)**. The **ganging of channels across UHC4T cards** allows even
> higher currents.」

| 规格 | 值 |
|---|---|
| 每卡通道数 | **4** |
| 每通道最大电流 | **40 A** |
| 每卡最大电流 | **160 A** |
| 更高电流怎么来 | **跨卡 ganging**（`ganging of channels across UHC4T cards`） |

**注意「跨卡」这两个字**：原文说的是 `across UHC4T cards`——
**这一句只提了跨卡，没提「一张卡内 4 个通道并起来」**。
**卡内能不能并、并多少，本篇没写**（推断：别把 `across` 读成「只能跨卡」，
**原文没说「只能」**）。

### 它和普通 DPS 的**唯一**差别：保护

**这是本页最该记住的一段**，原文写得很直白：

> 「During the execution of a test flow the UHC4T **acts like a normal device power supply (DPS)**.
> The main difference between a normal DPS and an ultra high current DPS is **the need to protect
> the ATE equipment in case of a shortage**, for example the needles on a probe card.
> Therefore, UHC4T card provides additionally:」

**「in case of a shortage」举的例子是探针卡上的针**——
**即：大电流一旦短路，先烧的是探卡/针，不是 DUT。** 所以它额外给了三样东西：

| 额外能力 | 原文 |
|---|---|
| **若干报警** | `Several alarms to protect your test equipment` |
| **高速采样器** | `A high-speed sampler for differential voltage monitoring` |
| **压降测量** | `Measurement of voltage drop on force/return line` |

**三样里有一样和别处对得上**：语法节（**取自子主题 `…02.04_UHC4T_hardware_overview.md`**）
里说 **`Only the UHC4T supports the Curr Limiter protection option.`**——
**`Curr Limiter` 就是上表「若干报警」里的一个**（推断：两者都是「保护」这一类，
**但原文没有把这两处名字对应起来**）。

**④ 图证（2026-09-20 补）——三样东西在硬件视图那张图上都能找到落点。**
依据是语法节里那张 `UHC4-T hardware view`（`146923.png`，652×458）。
**图上的字 raw 里 grep 不到**，要核只能自己开
`F:\master-dev\dorm-wsl-sytest\tdc-html\raw\146923.png`：

| 原文那三样（上表） | 在图（`146923.png`）上找得到的东西 | 图上那些字在 raw 里搜得到吗 |
|---|---|---|
| `Several alarms to protect your test equipment` | `Check Status Flags` 按钮 + 一块空白状态区 | **本篇搜不到**：`Check Status Flags` 全语料只出现 2 篇，都是 XPS256 编程那两篇 |
| `A high-speed sampler for differential voltage monitoring` | `Sampler` → 放大级 → 两个开关 → `DSO+` / `DSO-`（一对） | **`DSO+` 全语料 0 命中**——这个写法 raw 里根本没有 |
| `Measurement of voltage drop on force/return line` | `Measure Voltage Drop` 按钮，旁边 `Force` / `Return` 两个结果框 | `Measure Voltage Drop` 搜得到（含本卡那两篇） |

**这半张表里，「图上有这些控件名」是图证；「哪一样对哪一个控件」是我的推断**——
**原文只列了三样的名字，一处都没有把它们和硬件视图里的控件名对应起来**（推断）。

**图里另有几处是只有图上才有的**（都 grep 不到）：
`Curr Limiter` 在图上是一个字段、**取值写作 `unprotect`**
（`unprotect` 在 raw 里只出现 2 篇——`Layout_recommendations.md` 与 `PSLR` 那篇，**都不是 UHC4T 那几篇**）；
抬头写 **`Channel: 12501 ganged`**（`12501` 全语料只出现过一次，在
`Model_file_reference__model_legacy.md` 里，与这张卡无关）。
**但「`Curr Limiter` 的具体行为」这张图仍然答不了**——图上只有字段名和那一个取值。

### 硬件视图里它比别的卡多两块设置

语法节里那段（**来自子主题，不是定义文档自己写的**）：

> 「Only the UHC4T supports the Curr Limiter protection option. Therefore, **only the DCS-UHC4T
> hardware view shows this option and the Equation Set and Spec Set fields.**」

**照这句话读：`Equation Set` / `Spec Set` 两个字段是 UHC4T 独有的**
（推断：原文用 `Therefore` 把「独有 Curr Limiter」和「独有那两个字段」连成因果）。

**④ 图证（2026-09-20 补）**：`146923.png` 抬头那行就是
`DPS/Level Set 1`、`Equation Set 2`、`Spec Set 1`——**这两个字段在这张硬件视图上确实看得见**，
而且截图里**分别填着 `2` 和 `1`**。
**字段名在 raw 里搜得到**（`Equation Set` 见于 27 篇、`Spec Set` 见于 17 篇，
含本篇语法节那篇子主题）；**但截图里的取值 `2` / `1` 搜不到**——
**它们是画在像素里的，要核只能自己开 `F:\master-dev\dorm-wsl-sytest\tdc-html\raw\146923.png`**。

**一张反面对照图**（**不是本篇的 `sources:`**，来自 [[dc-scale-xps256-card]] 那边）：
XPS256 的硬件视图 `354251.png` 抬头只有 `Site` / `Pin` / `Channel` / `DC-Scale` / `PinType` 五项，
**没有 `Equation Set` / `Spec Set` 这一行**。
**两张图方向一致，但两张图证明不了「只有 UHC4T 有」**——
**那句全称句的依据是语法节引的原文，不是这两张图**（推断；全称否定不能靠抽样图证）。

> **2026-09-20 更正**：本页上一版这里写的是「**本页没有 Hardware view 的页面可查**」，**这句站不住**：
> **有一页 [[hardware-view]]（本页没读）**，raw 里也确实有专门讲 Hardware view 的两篇——
> `02.05.05.04.01_Hardware_view_diagram_of_DC_Scale_channels_in_DPS_operating_mode.md` 与
> `02.05.05.05.01_Hardware_view_diagram_of_DC_Scale_channels_in_PMU_operating_mode.md`
> （**都在 1.2 KB 以下，本页没读**）。**而那张图本页现在看了**，见上。

注意名字写法：**硬件视图里它叫 `DCS-UHC4T`**（带 `DCS-` 前缀），
**而页面标题和正文一律叫 `DC Scale UHC4T` / `UHC4T`**——**两种写法并存**。

## 典型用法

**原文没有 `## Procedure` / `## Before you begin` 段**，也没有任何命令或代码。
**本篇是一张卡的「入口页」**——它的用法全在它 `#### Subtopics` 列的七个子页里：

| 子页 | 管什么（**按标题读，本页都没读**） |
|---|---|
| `UHC4T sitemap` | 导航 |
| `UHC4T specifications` | 规格 |
| `UHC4T functionality and features` | 功能与特性 |
| `UHC4T hardware overview` | 硬件总览（**语法节里那段就是从这一篇抽的**） |
| `UHC4T specific setup tasks` | **具体 setup 任务——「怎么用」的答案在这一篇** |
| `UHC4 / UHC4T recommendations for use` | 使用建议 |
| `UHC4T pogo pin assignment` | pogo 针分配 |

**一条本篇给出的「怎么用」**：**跑 testflow 时就当它是普通 DPS 用**——
`During the execution of a test flow the UHC4T acts like a normal device power supply (DPS).`
**它的特殊性只在保护与监控那一层。**

**另一条来自「Related information」的入口**（原文列了三篇）：
`Filling rules for DC Scale cards (Pin Scale & Smart Scale)`（**填充规则**）、
`UHC4 / UHC4T pogo pin assignment`、`DC Scale UHC4 / UHC4T card`（DUT 板设计规则侧）。

**还有一份 PDF**：原文给了一个下载链接
`Download specifications PDF: V93000 SOC Device Power Supplies (V93000_SOC_Device_Power_Supplies_and_VI_Cards.pdf)`
（**本页没有打开这份 PDF**）。

## 和谁有关

- [[dc-scale-xps256-card]] — **同族、同批建的兄弟页**。两张都是 DC Scale 的 DPS 卡，
  **但规格量级完全不同**（UHC4T：4 通道 × 40 A；XPS256：256 通道 × 1 A）——
  **这个对比是本页从两篇文档各自的正文读出来的**，**两篇原文都没有互相提对方**（推断）
- [[dps128-dps64-cards]] — **同族卡**。`DPS128` / `DPS64` 也在 DC Scale 的 ganging 规则里
  （**这条来自 [[digital-pins-editor]] 那篇，不是本篇**）（推断——**本页不当它成本篇事实**）
- [[hardware-view]] — **它的独有选项显示在哪**。语法节那句
  `only the DCS-UHC4T hardware view shows this option and the Equation Set and Spec Set fields`
  说的就是这一页（**那页本页没读**）
- `Profiling of DC Scale cards with Hardware view`（**未建**）— 语法节指它作为
  `The Profile field` 的详解（**没读**）
- `Sample Code view`（**未建**）— 语法节说硬件视图底下的序列会
  `generate sample test method code for the executed measurement`，
  代码可以直接拷进 test method（**那页没读**）
- `V93000 SOC Device Power Supplies and VI Cards`（**PDF，未读**）—
  **本篇给的唯一一份规格出处**
- `UHC4T sitemap` / `UHC4T specifications` / `UHC4T functionality and features` /
  `UHC4T specific setup tasks` / `UHC4 / UHC4T recommendations for use` /
  `UHC4T pogo pin assignment`（**均未建**）— **本篇的六个子页，一篇都没读**
- [[dut-board-design-reference]] / [[pogo-pad-and-via-design]] / [[pogo-block-compatibility]] —
  **DUT 板侧的相邻主题**；原文 `## Related information` 里的两条 pogo / DUT 板链接指向那一族
  （**那几页本页没读**）（推断，仅指关系）
- [[pin]] / [[dc-test-programming]] — **同 `stage: pin` / DC 测试主题的页**，
  **但本篇没有任何一句把它们连起来**（推断，仅指归属）

## 版本

原文 `## Functional changes` 两条：

- **`Introduced in SmarTest 6.5.0`**
- **SmarTest 7.3.2**：`Introduction of UHC4T`

> ⚠️ **这两条并列读会打架，本页照抄不调和。**
> 第二条说的是「**UHC4T 是在 7.3.2 引入的**」，
> 而第一条说**本篇（页名就是 UHC4T）**是在 **6.5.0** 引入的。
> **可能的解释有三种，原文一条都没说**，本页不替它选：
> ① 第一条说的是**这张卡的前身 UHC4**（非 T 版），本篇沿用了它的版本记录；
> ② 第一条说的是**这篇文档**的引入版本，第二条说的是**卡**的引入版本；
> ③ 语料错误。
> —— **三种都无法从本篇证实**（推断）。
>
> **对照一下产品线**：`Introduction of UHC4T` 只写了 `SmarTest 7.3.2`，**没有产品线前缀**，
> 所以它属 SmarTest（§11.2④ 说的撞车问题在本篇没有出现）。

## 出处

`sources:` 一篇：
`02_System_reference/02.05_Test_Head_Cards/02.05.05.02_DC_Scale_UHC4T_card.md`
（`106867.htm`，2,211 字节，37 行）——**整篇读完**。

**本页做了什么、没做什么**：

- **「语法 / 参数」节不是从 `sources:` 那篇抽的。** 那篇自己**没有语法段**，
  脚本改从子主题 `02.05.05.02.04_UHC4T_hardware_overview.md` 抄了 **950 字符**（骨架段名里写明了）。
  **那一篇本页没有读原文**——本节凡引语法节内容，依据是**页内那段逐字拷贝**。
- **六个子页一篇都没读**（sitemap / specifications / functionality and features /
  specific setup tasks / recommendations for use / pogo pin assignment）。
  **所以「这张卡具体怎么 setup、有哪些功能、pogo 怎么排」本页一个字都没有**——
  **本页只有「它是一张 4×40 A 的卡、多三样保护」这两件事。**
- **一份 PDF 没打开**：`V93000_SOC_Device_Power_Supplies_and_VI_Cards.pdf`（**规格的原始出处**）。
- **两张图都看了（2026-09-20 补）**——**上一版这里写的是「两张图都没看」，并由此写下
  「本页没有任何来自图的结论」；那句话现在是错的，已按实际改动如下**：
  - **`146923.png`（`UHC4-T hardware view`，652×458）——看了，见上文两处「④ 图证」。**
    它答掉的是：硬件视图上确实有 `Equation Set` / `Spec Set` 两个字段、有 `Curr Limiter`
    （截图里取值 `unprotect`）、三样保护各有落点、抬头有 `Channel: 12501 ganged` 与
    `DC-Scale: DCS-UHC4T`。
    **图上那些字在 raw 里 grep 不到**（逐字的实测见「④ 图证」那张表），
    要核只能自己开 `F:\master-dev\dorm-wsl-sytest\tdc-html\raw\146923.png`。
  - **`105777.png`（`Open PDF`，19×19）——看了，它答不了任何问题。**
    整张图就是一个「打开文档」的小图标，**19×19 像素里没有可读文字**。
    **「这张图没给出结论」这次是看图之后的结论**，不是没看的借口。
- **图没答掉的**（下面两条上一版也写着，现在只是把范围说清）：
  - **`Curr Limiter` 的具体行为**——原文只给了名字，**图也只给了字段名和一个取值 `unprotect`**，
    **它怎么配、什么条件下触发，本页一个字写不了**。
  - **卡内 4 个通道能不能并、能并几路**；**「跨卡 ganging 到底怎么接、最多几张卡」**——
    原文只有 `The ganging of channels across UHC4T cards allows even higher currents.` 这一句，
    **图抬头那个 `12501 ganged` 只说明截图里有一个 ganged 通道，不说明怎么接、也不说明能接几个**。
- **`## Related information` 里那三篇都没读**（`Filling rules for DC Scale cards`、
  `UHC4 / UHC4T pogo pin assignment`、`DC Scale UHC4 / UHC4T card`）。
- **语法节里提到的 `Profiling of DC Scale cards with Hardware view`、
  `Sample Code view`、`Hardware perspective` 三处都没读。**

> ⚠️ **本篇的语料瑕疵，照实记、一处没替它改**：
> ① **`## Functional changes` 两条并列会读出矛盾**（见上「版本」）：
>    `- Introduced in SmarTest 6.5.0` 与 `- SmarTest 7.3.2: Introduction of UHC4T`。
>    **同一个对象被「引入」了两次，两个版本号。**
> ② **`shortage` 用词可疑**：原文
>    `the need to protect the ATE equipment in case of a shortage, for example the needles on a
>    probe card`。
>    ——**`shortage`（短缺）在这里读不通**，**上下文说的是短路/短接**
>    （同句举的例子是「探卡上的针」，那是短路的典型现场）。
>    **`short circuit` 才对**。**本页照抄原文用词，不替它改。**
> ③ **`## Related information` 三条链接之间没有任何分隔符**，原文逐字是一整行：
>    `[Filling rules for DC Scale cards (Pin Scale & Smart Scale)](<…>)[UHC4 / UHC4T pogo pin
>    assignment](<…>)[DC Scale UHC4 / UHC4T card](<…>)`
>    —— **三条链接首尾相连，中间没有空格也没有换行**。**别的段落之间是正常的。**
> ④ **卡名写法不统一**：正文一律 `UHC4T`，而**硬件视图的图注写 `UHC4-T`（多了一个连字符）**，
>    硬件视图里它又叫 **`DCS-UHC4T`**（多一个前缀）。原文：
>    `!`UHC4-T hardware view`（raw: `../../../../raw/146923.png`）`
> ⑤ **`#### Subtopics` 这个标题的层级是 4 级**，
>    而它下面直接跟的是正文——**它是本篇最顶层的结构标题，却比正文标题还深**。
>    全语料同此形态（**[[apg-pattern-file]] / [[device-access-file]] 那两篇也是 `#### Subtopics`**），
>    **不是本篇独有**（推断）。
> ⑥ **`## 语法 / 参数` 节里那段标着 `### Example` 的内容，里面没有代码示例**——
>    它逐字是 UHC4T hardware view 的散文（`Only the UHC4T supports the Curr Limiter
>    protection option. …`）。**这是子主题那边的段标记与内容对不上**，**本页不改语法节**。

`verified: doc-only`
