---
type: concept
title: Direct-Probe stiffener
layer: n/a
stage: project
tags: [concept, dut-board, direct-probe, stiffener, hardware-design]
related: [dut-board-design-reference, layout-information-dut-board, pogo-block-compatibility, pogo-pad-and-via-design, inter-layer-via-design]
sources:
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.12.01.02_Direct-Probe_stiffener.md
created: 2026-09-18
updated: 2026-09-20
verified: doc-only
---

# Direct-Probe stiffener

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

**没有加标记的语法段。** 定义文档里没有 `Syntax` / `Parameters` / `Example`
这类**段标记**，跟着 `Subtopics` 找一层也没有。
**所以本脚本一个字都不收录**——没有段标记时「哪一段是语法」是猜，而猜就是编（§4）。

<!-- 语法节 end -->

## 是什么

**stiffener（加强板）是 Direct-Probe 方案里承受探针接触力的那块结构件；本篇不是讲它怎么工作，
而是它「图纸和规格从哪拿」的入口页。** 原文第一句把这一点说得直白（**那句里有一处编码损坏，见 `## 出处` ⚠️①**）：

> 「Below you find the Direct-Probe鈩?stiffener related drawings. They provide the specs and dimensions required for your design tasks.」

**注意这页本身不含任何尺寸数字**——**尺寸在图纸包里**，本页只负责把它们列出来。

### 两条现行方案

| 名称 | 产品号 | 原文给的适用范围 | 包里的形态 |
|---|---|---|---|
| **Direct Probe universal stiffener** | `E7018DP` / `E7018-64170` | **full-capability 与 RF** | 一批 `.dxf` + `E7018-64170_K.pdf` + `E7018-64170_K.stp`（**rev K**） |
| **SECRON Direct Probe digital stiffener** | `E5150-60221` | **原文未写** | 一批 `.dxf` + `E5150-60221_G.pdf` + `E5150-60221_G.stp`（**rev G**） |

**整篇的选型总则只有一句：**

> 「For full-capability and RF applications use the 'Universal Stiffener'.」

**这句话把 Universal 钉死在「full-capability」和「RF」两个场景上。**
**至于 SECRON 那个什么时候用，原文没有配对的另一句**——**本页不替它补**
（**能推的只有「不属于上面两类时才轮到它」，这是（推断），依据就是原文只给了这一条单向的选型句**）。

### 两个 legacy：不要用在新设计上

原文先给一句总的话，再在每条下面各写一遍：

> 「Please do not use the following stiffeners for new designs.」

| Legacy stiffener | 产品号 | 原文的标注 |
|---|---|---|
| **Direct Probe dedicated non RF Stiffener** | `N2360-61076` | `(no Advantest product)`；`N2360-61076 is a legacy stiffener that should not be used for new designs.` |
| **Direct Probe dedicated RF Stiffener** | `N2360-61097` | `(no Advantest product)`；`N2360-61097 is a legacy stiffener that should not be used for new designs.` |

**两条的替代品是同一个，原文也各写了一遍：**

> 「Please use the E7018DP stiffener for new designs.」

**两个 legacy 的标题里都带 `(no Advantest product)`，且包名都叫 `3rd Party Fabrication Package`**
——**原文等于告诉你这两块板不能从 Advantest 订，只能照包里的图去第三方加工。**
（**这与现行两条的 `…_3rd_Party_Fabrication_Package.zip` 是同一套做法**，见下。）

**一个容易想当然的地方**：**「legacy」不等于「不再维护」。**
版本记录里 `N2360-61097_H` 那个 legacy 包**到 7.6.2 / 7.10.2 / 8.4.4 还在更新**
（见 `## 版本`）——**原文两处都留着，没有解释。**

### 图纸包里到底是什么

原文的办法是**把每个包的清单原样贴出来**（`.dxf` 一行四个）。**这里不重贴清单，只把形态说清**：

| 包 | 清单里出现的文件类型 |
|---|---|
| **现行的两个**（`E7018-64170_K` / `E5150-60221_G`） | 一批 `.dxf`（`E2812-*` / `E6978-*` / `E6980-*` / `N2360-*` 号）+ 一份 `.pdf` + 一份 `.stp`（3D） |
| **legacy 的两个**（`N2360-61076_L` / `N2360-61097_H`） | 一批 `.dxf` + `.IGS` + `.PDF` + 一份 `REVISION NOTES & BOM.xls`，另外各带一份 `V93000 Direct Probe Probe-Card Specifications.PDF` 和一套 **PCB Template Information** |

**两代包的差别是实打实的两样**：legacy 多 `REVISION NOTES & BOM.xls`（改版记录 + 物料表）和
那份 `Probe-Card Specifications.PDF`。**现行包的清单里没有这两样——原文没说它们是不是搬去了别处。**

**两个 legacy 包共用同一批底图号**（`E2812-23753`、`E6978-21791`、`E6980-26101` 等在两份清单里都出现），
**且它们的清单里都带一份 `V93000 Direct Probe Probe-Card Specifications.PDF`，以及一份
「PCB Template Information」（non RF 那份是 `N2360-90104/90105`，RF 那份是 `N2360-90119/90120`）。**

## 典型用法

**原文没有 `## Procedure`，也没有 `## Before you begin`。** 能确定下来的只有下面四步，
**且第一步到第四步是从原文的选型句和文件清单反推的（推断）**：

1. **先选型**：full-capability 或 RF → **Universal**（`E7018DP` / `E7018-64170`）；
   **不要在新设计上用 `N2360-61076` / `N2360-61097`。**
2. **拿包**：每个条目后面挂一个 `.zip`（`…_3rd_Party_Fabrication_Package.zip`，
   legacy 的是 `…_FABRICATION_PACKAGE.zip`）——**加工方式写在包名里：第三方加工。**
3. **按文件类型分工取用**：`.dxf` 给机械加工、`.pdf` 给人看图纸、`.stp` / `.igs` 给 3D 建模。
4. **用版本记录对 rev**：**图纸包是按 rev 命名的**（`revK` / `revG` / `_L` / `_H`），
   版本记录里逐条写着每一次 rev 的变更——**先看这里，再决定拿哪一版图。**

**原文的 `## Related information` 列了四篇**：`Direct-Probe probe card layout information`、
`Advantest product numbers`、`Direct-Probe PMUX design kit`、
`Wave Scale RF PCB layout and stiffener info for Direct-Probe`——**本页一篇都没读**（见 `## 出处`）。

**一个使用上的前提**：**这一页给不出任何尺寸**。原文第一句承诺的
`the specs and dimensions required for your design tasks` **在图纸包里**，
**所以「照着这一页画板」这件事做不到**。

## 和谁有关

- [[dut-board-design-reference]]（**未建**）— **上级**：本篇在 raw 里就归在
  `02.03_DUT_board_design_reference/` 这一组下（这是路径事实，不是推断）
- [[layout-information-dut-board]]（**未建**）— **同类**：DUT board 侧的布局信息页；
  **本篇是 stiffener 侧的图纸入口**。**这一条只凭命名与归属相邻，本篇原文没提它**
- [[pogo-block-compatibility]] / [[pogo-pad-and-via-design]] / [[inter-layer-via-design]]（**均未建**）—
  同属 DUT board 设计的另外几支（pogo 块、pogo pad / via、层间 via）；
  **本篇原文一个字没提它们**，这一组只是同组邻居
- `Direct-Probe probe card layout information`（**未建，且不在本 wiki 的建页清单里**）—
  原文 `Related information` 的第一条；**本页没读**，
  所以**「探针卡的 layout 信息」和「stiffener 的图」怎么配合，本页给不出**
- `Advantest product numbers`（**未建，且不在建页清单里**）— **上面那些 `E7018DP` / `N2360-61076`
  之类的号去哪查真伪，原文指向它**；**本页没读**
- `Direct-Probe PMUX design kit`（**未建**）— 原文 `Related information` 之一，
  **它链的是 MUX cards design data 那一篇里的一个 `DirectProbe stiffener` 锚点**
- `Wave Scale RF PCB layout and stiffener info for Direct-Probe`（**未建**）— **和本篇最贴**：
  RF 场景下的 stiffener 信息在那儿，**而本篇的选型句正好写着「RF 用 Universal」**——
  **两页是同一个问题的两头，本页没读那篇**
- `3rd Party Fabrication Package`（**不是页，是 raw 层的 `.zip`**）— 本页只给出它们的**文件名**，
  **一个都没打开**（见 `## 出处`）

## 版本

原文**有** `## Functional changes`，十条：

- **Introduced in SmarTest 7.2.1**
- **SmarTest 7.4.0**：`Update to Revision F of Direct Probe Universal Stiffener`
- **SmarTest 7.4.1**：`Update to Revision G of Direct Probe Universal Stiffener - 3rd Party Fabrication Package`
- **SmarTest 7.4.1**：`New drawing Direct Probe SECRON Direct Probe Digital Stiffener`
- **SmarTest 7.4.4**：`New drawing for V93000 Direct-Probe probe card specifications N2360-90117_C`
- **SmarTest 7.5.0 / 8.1.3**：`E7018-64170 updated to revision J`
- **SmarTest 7.5.1 / 8.2.1**：`N2360-90120 in file N2360-61097_H_FABRICATION_PACKAGE.zip updated to revision D`
- **SmarTest 7.5.2 / 8.2.2**：`E7018-64170_revJ_Direct_Probe_Universal_Stiffener-3rd_Party_Fabrication_Package.zip updated to revision K`
- **SmarTest 7.5.2 / 8.2.3**：`E5150-60221_revD_SECRON_Direct_Probe_Digital_Stiffener_-_3rd_Party_Fabrication_Package.zip updated to revision G`
- **SmarTest 7.6.2 / 7.10.2 / 8.4.4**：包 `N2360-61097_H FABRICATION PACKAGE` 更新到 `…_2021-06-02`：
  `N2360-90119` 从 rev D 到 rev 5，`N2360-90120` 从 rev D 到 rev E

**四点从这十条里读出来的东西：**

| 观察 | 依据 |
|---|---|
| **多条版本号成对/成组出现**（`7.5.0 / 8.1.3`、`7.5.1 / 8.2.1`、`7.5.2 / 8.2.2`、`7.5.2 / 8.2.3`、`7.6.2 / 7.10.2 / 8.4.4`） | **同一个图纸变更同时落在 7.x 与 8.x 两条线上**——这也对得上 §11.2 ④「同一版本号跨产品线」那条提醒 |
| **Universal 的 rev 轨迹：F → G → J → K** | 与**正文包名 `revK` 一致** |
| **SECRON 的 rev 轨迹：D → G**（`E5150-60221_revD…` → `updated to revision G`） | 与**正文包名 `revG` 一致** |
| **legacy 的 `N2360-61097_H` 包在 7.6.2 / 7.10.2 / 8.4.4 还在更新** | **和正文「不要用于新设计」并存**——原文没解释，本页不替它调和 |

> **一处正文与版本段对不上的地方**：`N2360-90117_C` 这个号**只在版本记录里出现**
> （`New drawing for V93000 Direct-Probe probe card specifications N2360-90117_C`）。
> **正文两个包的文件清单里各有一份 `V93000 Direct Probe Probe-Card Specifications.PDF`，
> 但那份文件没有编号**——**原文没说这两者是不是同一份东西。本页不判。**

## 出处

`sources:` 一篇：
`02_System_reference/02.03_DUT_board_design_reference/02.03.12.01.02_Direct-Probe_stiffener.md`

**本页没做的**：

- **`## Related information` 那四篇一篇没读**（`Direct-Probe probe card layout information`、
  `Advantest product numbers`、`Direct-Probe PMUX design kit`、
  `Wave Scale RF PCB layout and stiffener info for Direct-Probe`）。
- **一个 `.zip` 都没打开。** 本页「包里有哪些文件类型」**全部来自原文贴出的文件名清单**，
  **没有任何一条是解开包核对过的**；**包多大、里面文件是否齐全，本页不知道**。
- **源文档里没有图。** 原文正文里**没有插图**——**所有图纸都在 `.zip` 里**，
  **所以本页没有任何来自图的结论：stiffener 长什么样、怎么装、孔位如何，本页一个字没有。**
- **一个尺寸数字都没有。** 原文第一句承诺的 `the specs and dimensions required for your design tasks`
  **在图纸包里**，**不在这一篇里**。
- **没有 `## Procedure` / `## Before you begin`**，**也没有实装或实做过任何一块板**——
  `verified: doc-only` 指的就是这件事。
- **`N2360-90117_C` 与正文那两份 `Probe-Card Specifications.PDF` 的关系，原文没说，本页也没查。**
- **`SECRON` 是厂商名还是 Advantest 的内部代号，原文没说**，本页不猜。

> ⚠️ **本篇的语料瑕疵五处，本页照实记下、一处都没替它改**：
>
> ① **编码损坏（§11.2 ①），而且吃掉了后面的空格。** 原文第一句写的是：
> `Below you find the Direct-Probe鈩?stiffener related drawings.`
> ——`鈩` 是 **U+9229**，紧跟一个 **ASCII `?`**；**`stiffener` 前面因此没有空格**。
> 形态和 §11.2 ① 记的 `鈥` 系同源（**标点被按 GBK 读了**），
> **但这里坏出来的是 `鈩` 而不是 `鈥`，本页照原样转录**。
> **原字符应为 `™`（推断），依据是这个词的正常写法是 `Direct-Probe™ stiffener`**——
> **但这是推断，不是文档事实；本页正文里给的是原文那个坏字。**
> **本篇这一处（全篇 1 处 `鈩`，0 处 `鈥`）。要拿这个词去 raw 里搜，得搜坏掉的形态。**
>
> ② **`Note` 块又和链接粘在一起**（和 `special-test-suites` 那页**同一形态**）：
> `- [N2360-61076_L_FABRICATION_PACKAGE.zip](…)Note N2360-61076 is a legacy stiffener that should not be used for new designs.`
> ——**`Note` 前面既没有空格也没有换行**。`N2360-61097` 那条一模一样。
>
> ③ **同一句话写了两遍**：`## Legacy stiffeners` 段开头先写
> `Please do not use the following stiffeners for new designs.`
> **两个条目的 `Note` 里又各写了一遍** `…is a legacy stiffener that should not be used for new designs.`
>
> ④ **`Please use the E7018DP stiffener for new designs.` 也写了两遍**（两个 legacy 条目各一次），
> **且两次的链接指向同一个锚点** `#_138465__dle_E7018-64170_E7018DP`。
>
> ⑤ **同一个名字两种写法**：首句写 **`Direct-Probe`**（带连字符），
> **其余所有条目标题写 `Direct Probe`**（不带）；**`Stiffener` 与 `stiffener` 的大小写也混用**
> （`Direct Probe dedicated RF Stiffener` 大写、`Direct Probe universal stiffener` 小写）。
> **原文如此，本页不统一。**

`verified: doc-only`
