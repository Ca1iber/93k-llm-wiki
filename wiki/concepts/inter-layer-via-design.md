---
type: concept
title: Inter-layer via design
layer: n/a
stage: pin
tags: [pin, dut-board, via, stackup, hardware-design]
related: [pin, pogo-pad-and-via-design, pogo-block-compatibility]
sources:
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.07.07.02_Inter-layer_via_design.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# Inter-layer via design

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

**没有加标记的语法段。** 定义文档里没有 `Syntax` / `Parameters` / `Example`
这类**段标记**，跟着 `Subtopics` 找一层也没有。
**所以本脚本一个字都不收录**——没有段标记时「哪一段是语法」是猜，而猜就是编（§4）。

<!-- 语法节 end -->

## 是什么

> **一句话**：**信号要在板子内部换一层走线时，那个「过孔（via）」该怎么做。**
> 和 pogo via 的区别只有一个字：**自由度**——原文 *"unlike pogo via design, the design of
> inter-layer vias allows more freedom."*
> 为什么 pogo via 没自由而它有的原因原文没写；**可推断的理由**是 pogo via 要被 pogo 针
> 顶着（位置由针的网格定死），而层间 via 只走信号、不用对针，所以位子可以挪。
> **这句是推断，不是文档事实。**

**它是 [[pogo-pad-and-via-design]] 的子主题**（`#### Subtopics` 里声明的唯一一个），
所以本页归在同一个 `stage: pin` 下——**都是画 DUT board 的规则**。

### 变量清单（原文，这就是这一页的全部内容）

原文给的不是尺寸表，是**八个可以调的变量**：

| 变量 | 说明 |
|---|---|
| Number of ground vias | 接地 via 数量 |
| Pitch between signal and ground vias | 信号 via 与接地 via 的间距 |
| Drill size of the signal via | 信号 via 钻孔尺寸 |
| Drill size of the ground via | 接地 via 钻孔尺寸 |
| Pad size if the via goes to the top or bottom layer | 走到顶层/底层时的焊盘尺寸 |
| Removal of non-functional pads (NFPs) | 去不去非功能焊盘（Yes / No） |
| Back drilling | 背钻（Yes / No） |
| Reference plane clearance or swell | 参考层避让（clearance / swell） |

**注意它和 [[pogo-pad-and-via-design]] 的关系**：前六项在 pogo via 的设计表里
**也有对应的行**（via 长度、接地 via 数、间距、钻孔尺寸、去 NFP、背钻）。
两页不是重复——**同一个变量，在两个场景下的约束强度不同**：
pogo via 那页给的是**具体数值**（26 +1/-3 mil 等），本页给的是**变量名**，
数值要按叠层自己定。

## 典型用法

**这一页没有可照抄的数值，所以它的用法是「去哪里拿数值」。**

原文最后一句给了唯一出路：参考 `Inter-layer via examples`
（raw: `02.03.07.07.02.01_Inter-layer_via_examples.md`）——**那是图例，不是文字**，
本 wiki **不为它建页**（建出来会是一个没有正文的空页）。
要看具体做法，**回 raw 看那几张图**。

## 和谁有关

**入边只有 1 条**——来自父文档 [[pogo-pad-and-via-design]]。
**这是本 wiki 里入边最少的页之一，而它仍然建了**，理由要写清楚，免得下次被当成误建：

1. **它是父文档 `Subtopics` 里明确声明的子主题**（§9.1 的第 4 类可链目标）——
   **语料自己给的关系，不是我猜的**。
2. 它讲的是**画板子必须定的一件事**（层间换层怎么做），不是流程细节。
3. 它的入边少，是因为**父文档把流量全吃掉了**：所有 pogo 页都指向父页，
   父页再指向它。**入度低 ≠ 没人需要**——这一点对「按入度建页」的规矩是个反例，
   所以本页是**按 Subtopics 建**的，不是按入度建的。

**并列**：[[pogo-block-compatibility]]（同为父页的子主题）。
**上行**：[[pin]]。

**不链的**：`Inter-layer via examples`（raw: `02.03.07.07.02.01_Inter-layer_via_examples.md`）
——**它不在任何一份可建页清单里**（不在 `dangling.csv`、不在 `unowned.csv`），
按 §9.1 只能写成反引号 + 路径，**不许把它写成双中括号链接**，
否则就是造一个永远不会建的悬空目标。
（**这里刻意不写出那个链接的字面形式**：第九类检查**会**把反引号里的双中括号链接
当真链接——那是故意的，因为这份语料里真正的链接就写在反引号里。
所以**正文里连「举例说明」都不许写出链接的样子**，只能描述它。）

## 版本

- **Introduced before SmarTest 6.3.2**（`Functional changes` 段，仅此一条）

> 和 [[pogo-pad-and-via-design]] 一样，**这是板子的物理设计规则**，
> 文档的版本号不代表规则会跟着软件版本变。**看到旧板子别急着怀疑这页过时。**
> （这句是**推断**，文档没写。）

## 出处

- 定义文档：`02_System_reference/02.03_DUT_board_design_reference/02.03.07.07.02_Inter-layer_via_design.md`
  （TDC `91611.htm`，**922 字节，27 行——全 wiki 最小的定义文档之一**）
- **入边 1 条 / 1 篇**（`inline` 口径，无目录边）
- 所属：**DUT board design reference**（`02.03`）
- 本页 `verified: doc-only`。**页短是因为文档短，不是因为没查**——
  「八个变量」就是这篇文档的全部；**没有的下文不许我编**（§4）。
