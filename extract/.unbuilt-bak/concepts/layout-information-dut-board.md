---
type: concept
title: Layout information: DUT board
layer: n/a
stage: project
tags: [concept, dut-board, layout, drawing, hardware-design]
related: [dut-board-design-reference, direct-probe-stiffener, pogo-pad-and-via-design, pogo-block-compatibility]
sources:
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.12.01.08_Layout_information__DUT_board.md
created: 2026-09-18
updated: 2026-09-20
verified: doc-only
---

# Layout information: DUT board

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

**没有加标记的语法段。** 定义文档里没有 `Syntax` / `Parameters` / `Example`
这类**段标记**，跟着 `Subtopics` 找一层也没有。
**所以本脚本一个字都不收录**——没有段标记时「哪一段是语法」是猜，而猜就是编（§4）。

<!-- 语法节 end -->

## 是什么

**这一页是 DUT board 布局图纸的取件入口。** 原文第一句：

> 「Below you find the DUT board related layout information. The drawings provide the specs and dimensions required for your design tasks.」

**和 `Direct-Probe stiffener` 那页几乎同款**（那边的原句是 `They provide the specs and dimensions required for your design tasks.`）——
**两句都指向同一件事：这一页不含尺寸，尺寸在图纸包里。**

### 四张板子：三种尺寸 + 一种 HSSI

| 条目 | TH 号 | DUT IF 号 | 图纸包 | 包里的文件 |
|---|---|---|---|---|
| **DUT Board Half Size** | **原文未写** | `E6980xx` / `E8009xx` | `E6980-96530_Q.zip` | 4 个 `.dxf` + `_bw.pdf` + `_color.pdf` |
| **DUT Board Large** | `E6978BB` / `E8001A,B` | `E6980C,CD` / `E8009B,BD,D,DD` | `E6980-96550_P.zip` | 同上形态 |
| **DUT Board Small** | **原文未写** | `E6980xx` / `E8009xx` | `E6980-96540_Q.zip` | 同上形态 |
| **DUT Board HSSI** | `E6978Ax,Bx` | `E6980B,C` | `D-E6980-96560-1S11B_dxf.zip` | **只有 1 个 `.dxf`**；**`.pdf` 是单独一条链接** |

> **三处不对齐，是本页最该先看清的东西**（细节见 `## 出处` ⚠️③④）：
>
> ① **Half Size 与 Small 的 `DUT IF` 号一模一样**（都是 `E6980xx/E8009xx`），
> **只有包号不同**（`_96530_Q` 与 `_96540_Q`）——**光看机器号分不出这两张板**。
>
> ② **Half Size 与 Small 没有 `TH` 号**，而 Large 与 HSSI 有。
> **原文没说这是「不适用」还是「漏写」。**
>
> ③ **HSSI 那条的形状和另外三条完全不同**：前三条的图 **一包全含**（`.dxf` + 黑白 pdf + 彩色 pdf 都在 zip 里），
> **HSSI 的 `.pdf` 单独挂在外面**，而且**没有黑白/彩色之分**。

**包里那两类 pdf 的用途**（**按文件名推断**）：`_bw.pdf` 是**黑白版**、`_color.pdf` 是**彩色版**——
**原文没有解释这两份为什么并存。** 同理，四个 `.dxf` **（按文件名推断）**是同一块板的四张分图
（`_1<rev>` – `_4<rev>`）——**这两条都是（推断），依据只有文件名本身，本页一个包都没打开。**

### 一条「图里还夹带了别的东西」的提示

原文用一个 `Note` 说了一件容易被漏掉的事：

> 「The drawings provided for the "DUT Board Half Size", "DUT Board Large", and "DUT Board Small" also contain the pogo pin assignment and pogo pad dimensional drawings for selected cards of the legacy Pin Scale system.」

**这句话有两层限制，都得看清：**

| 限制 | 原文的写法 |
|---|---|
| **只限那三个包** | `the "DUT Board Half Size", "DUT Board Large", and "DUT Board Small"`——**HSSI 不在里面** |
| **只限部分卡** | `for selected cards`——**是「选定的卡」，不是全部** |

**然后原文立刻划了边界，把两件事交给别的篇：**

| 你要什么 | 原文指向 |
|---|---|
| **所有可用卡**的 pogo pin 分配，以及更多尺寸图 | `Pogo pin assignment`（raw: `02.03.06_Pogo_pin_assignment.md`） |
| **默认 pogo pad 布局与 via 设计** | `Pogo pad and via design`（raw: `02.03.07.07_Pogo_pad_and_via_design.md`） |

> 「For the pogo pin assignment of all available cards and additional dimensional drawings, refer to Pogo pin assignment. For the default pogo pad layout and via design, refer also to Pogo pad and via design.」

**所以本页的图是「够你开始做布局」的量级，不是唯一来源**——
**pogo 那两件事在别处，而且本页的图只覆盖 legacy Pin Scale 的「选定卡」。**

## 典型用法

**原文没有 `## Procedure`，也没有 `## Before you begin`。** 从这一页能确定的只有四步：

1. **按板型对号**：Half Size / Large / Small / HSSI。
   **注意 Half Size 与 Small 的 `DUT IF` 号相同**——**原文没说这时候怎么选**，
   **本页给不出判据**（见 `## 出处` ⚠️④）。
2. **下对应的 `.zip`**；**HSSI 那条还要另外下那份单独的 `.pdf`。**
3. **按用途分文件**：`.dxf` 拿去布局，`.pdf` 给人看（前三条有黑白与彩色两份）。
4. **本页覆盖不到的两件事按上表去别的篇**（pogo pin 分配、pogo pad 与 via）。

**原文没有说这四步的先后**，也**没有说下载要不要权限、从哪下**——
**它只给了 raw 层的 `.zip` 文件本身。**

**一条本页必须交代的前提**：**这一页给不出任何尺寸**——
原文第一句承诺的 `the specs and dimensions` **在包里**，**「照着这一页画板」做不到。**

## 和谁有关

- [[dut-board-design-reference]]（**未建**）— **上级**：本页在 raw 里归在
  `02.03_DUT_board_design_reference/` 的第 12 支 `Drawings, product numbers and commercial parts` 下（路径事实）
- [[direct-probe-stiffener]]（**未建**）— **同类、平行的另一页**：两页都长成「图纸包清单」的形态，
  **连第一句的措辞都几乎一样**；差别在**它讲 stiffener，本页讲板子本身**
- [[pogo-pad-and-via-design]]（**未建**）— **原文点名的下游之一**：
  **默认 pogo pad 布局与 via 设计**在那儿，**不在本页的图里**
- [[pogo-block-compatibility]]（**未建**）— 同组邻居（pogo 块）；**本页原文没提它**
- `Pogo pin assignment`（**未建**）— **原文点名的下游之一**：
  **本页的图只带 legacy Pin Scale「选定卡」的 pogo pin 分配**，
  **所有可用卡的分配和更多尺寸图都在那一篇**
- `Advantest product numbers`（**未建，且不在本 wiki 的建页清单里**）— 原文 `Related information` 之一；
  **上面那些 `E6980-*` / `E6978*` 号去哪查，原文指向它**；**本页没读**
- **四个板型名**（`DUT Board Half Size` / `DUT Board Large` / `DUT Board Small` / `DUT Board HSSI`）
  **不是 wiki 页面**，只是本页列出的条目——**所以它们不该链、也没有页**

## 版本

原文**有** `## Functional changes`，**只有一条**：

- **Introduced in SmarTest 7.2.1**

**「只有一条」这件事本身值得说一句**：同批的 `Direct-Probe stiffener` 那页有十条 rev 更新记录，
**而本页从 7.2.1 引入之后一条变更都没有**。
**这不等于图纸包没改过，只等于这篇文档没记**（**这是本页的（推断），依据就是本节只有一条**）。

**另一处对不上的地方**：**四个包的 rev 字母（`_Q` / `_P` / `_Q` / `1S11B`）在版本段里一个都没出现**——
**所以「手上这个包是哪一版」本篇给不出**。
**原文 `Related information` 把产品号指向 `Advantest product numbers`（本页没读），
但那是产品号，不是 rev**——**本页不知道 rev 该去哪对，也不猜。**

## 出处

`sources:` 一篇：
`02_System_reference/02.03_DUT_board_design_reference/02.03.12.01.08_Layout_information__DUT_board.md`

**本页没做的**：

- **`Related information` 那两篇没读**（`Advantest product numbers`、`Pogo pin assignment`），
  **`Pogo pad and via design` 那篇也没读**——**所以「pogo 那两件事该怎么做」本页一个字没有**，
  只有原文指路的那两句话。
- **四个 `.zip` 一个都没打开，一份 `.pdf` 都没看。** 本页关于包内文件的说法
  **全部来自原文列出的文件名清单**。
- **源文档里没有图。** 原文正文里没有插图——**所有图纸都在包里**，
  **所以本页没有任何来自图的结论：四张板子长什么样、几层、什么材料，本页一个字没有。**
- **一个尺寸数字都没有**（原文的 `specs and dimensions` 在包里）。
- **没有 `## Procedure` / `## Before you begin`**，**也没有实做过任何一块板**——
  `verified: doc-only` 指的就是这件事。
- **`selected cards` 具体指哪些卡，原文没说，本页也没查。**
- **「四个 `.dxf` 是四张分图」「`_bw` / `_color` 是黑白与彩色」这两条是按文件名的（推断）**，
  **没有打开包核对过。**

> ⚠️ **本篇的语料瑕疵四处，本页照实记下、一处都没替它改**：
>
> ① **`Files of the package:` 和链接粘在一起，四条都是**：
> `- [E6980-96530_Q.zip](…)Files of the package:`
> ——**`zip` 链接和 `Files of the package:` 之间既没有空格也没有换行**。
> `E6980-96550_P.zip`、`E6980-96540_Q.zip`、`D-E6980-96560-1S11B_dxf.zip` 三处一模一样。
> **（`special-test-suites` 那页的 `Note` 粘连、`Direct-Probe stiffener` 那页的 `Note` 粘连，是同一形态的第三例。）**
>
> ② **`Note` 标记自己占一行，且前面有一个空格**：原文该行的内容就是 ` Note`（上下各空一行），
> **正文跟在它后面另起一段。** 原文如此。
>
> ③ **四个条目的机器号与包结构不对齐**：**Half Size 与 Small 没有 `TH` 号**（Large / HSSI 有）；
> **HSSI 的 `.pdf` 不在 zip 里**，前三条的 pdf 在 zip 里且分 `_bw` / `_color` 两份。
> **原文没说这些差别是有意的还是笔误，本页不判。**
>
> ④ **Half Size 与 Small 的 `DUT IF` 号完全相同**（都是 `E6980xx/E8009xx`），
> **包名却不同**（`_96530_Q` / `_96540_Q`）——**原文没说这两张板的区别在哪，本页也不替它推。**

`verified: doc-only`
