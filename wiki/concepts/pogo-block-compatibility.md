---
type: concept
title: Pogo block compatibility
layer: n/a
stage: pin
tags: [pin, dut-board, pogo, hardware-design, compatibility]
related: [pin, pogo-pad-and-via-design, inter-layer-via-design]
sources:
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.07.07.01_Pogo_block_compatibility.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# Pogo block compatibility

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,539 字符逐字取自** `<02_System_reference/02.03_DUT_board_design_reference/02.03.07.07.01_Pogo_block_compatibility.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Tables（脚本逐字抽取，第 1 张）

| Standard‑density (SD) | High‑density (HD) | Very‑high‑density (VHD) |
|---|---|---|
| !`Pogo block - Standard-density`（raw: `../../../../agent-html/350391.png`） | !`Pogo block - High-density`（raw: `../../../../agent-html/350390.png`） | !`Pogo block - Very-high-density`（raw: `../../../../agent-html/350392.png`） |
|  | This is the recommended layout if you expect that your standard‑density DUT board will also be installed on systems with high‑density pogo blocks. | Digital cards and DC Scale cards with higher channel count will use the very‑high‑density pogo blocks to minimize the number of required pogo blocks per test head card.Note If you expect your new DUT board to be installed on systems with very‑high‑density (VHD) pogo blocks, we strongly recommend using this layout, even if currently only lower density pogo blocks are configured. |

### Tables（脚本逐字抽取，第 2 张）

| Standard-density (SD) | High-density (HD) |
|---|---|
| !`Pogo block - Standard-density`（raw: `../../../../agent-html/354972.png`） | !`Pogo block - High-density`（raw: `../../../../agent-html/354971.png`） |
| This is the recommended layout if you expect that your standard‑density (SD) DUT board will also be installed on systems with high‑density (HD) pogo blocks.<br><br>If you expect that you also need to install the DUT board on a test system that is equipped with VHD type pogo blocks, use the design for the HD pogo block shown on the right. | This is the recommended layout if you expect that your high‑density (HD) DUT board will also be installed on systems with very‑high‑density (VHD) pogo blocks. |

<!-- 语法节 end -->

## 是什么

> **一句话**：pogo 块有三档密度，**这一页说的是「板子以后要装到更高密度的机台上，现在该怎么画焊盘」**。
> 结论一句话：**多做出一些焊盘，但不接线。** 那些空焊盘的作用是别让高密度块的针
> 顶到板子的基材或走线上（`stage: pin`，给画板子的人看）。

原文对「兼容」的定义（**这就是本页的主句**）：

> *"compatibility with newer versions of the hardware or other configurations means that
> extra landing pads are provided for the pins of higher density pogo blocks."*

**为什么需要**（原文）：pogo 针密度会随 pogo cable / test head card / 系统的**新版本**提高，
而 V93000 是模块化的，实际会出现**很多种配置组合**。做新板子时不考虑这件事，
板子以后就装不上新硬件。

**那些空焊盘到底防什么**（原文，机制）：*"These extra, unconnected landing pads ensure,
that the pogo pins of pogo blocks with higher density will not directly contact the
substrate, traces, the solder stop mask or other coatings of your DUT board."*
—— 防的是**针尖直接顶到基材 / 走线 / 阻焊 / 涂层**。空焊盘给的是一块落点。

### 三档密度的网格事实（原文）

| | 网格 |
|---|---|
| **SD**（standard-density） | 100 mil (2.54 mm) |
| **HD**（high-density） | **和 SD 同一个** 100 mil 网格 |
| **VHD**（very-high-density） | 网格类似，但**中间多三排、错开 50 mil (1.27 mm)**，且每排只有 **16 个** pogo 针 |

**SD 与 HD 同网格是最关键的一条**：正因为同网格，SD 板加一圈空焊盘就能接 HD 块。

## 典型用法

**这是一张「按你将来打算装什么」查的选择表**，原文给的就是三种情形：

| 你现在做的板子 | 将来可能装到 | 建议 |
|---|---|---|
| SD | HD 系统 | 用 SD 的推荐布局（**这就是「推荐布局」的含义**） |
| HD | VHD 系统 | 用 HD 的推荐布局，**即使现在只配了低密度 pogo 块**（原文：*we strongly recommend*） |
| 任意 | 只要有可能上 VHD | 按 VHD 预留 —— 原文把这条写成了强建议 |

**尺寸与详图去哪查**（原文给的三条路）：

- 尺寸与详细图纸 → `Layout information: DUT board`（raw: `02.03.12.01.08_Layout_information__DUT_board.md`）
- 新针卡的简图 → `Pogo pin assignment`（raw: `02.03.06_Pogo_pin_assignment.md`）
- **焊盘本身的设计规则** → [[pogo-pad-and-via-design]]（本页只管「留不留位置」，不管「焊盘多大」）

**上面「语法 / 参数」节里那张表的三列就是三张插图**，图本身在 raw
（`../../../raw/350391.png` 等，路径已随表附上）。表里的文字是图注，不是参数。

## 和谁有关

**入边 44 条 / 24 篇**（`extract/pack/` 口径：只算 `inline` 边）。

**引用方几乎全是 pogo 线缆组件与针脚分配页**——查它们的依据都在本页的「网格事实」上：

- **PS1600 线缆**：`E8030PSD`（8 SD）/ `E8030PSDL` / `E8030PHD`（4 HD）/ `E8030PVHD`（2 VHD）
- **E8023P 系列**：`E8023PB`（2 VHD 块）/ `E8023PK`（4 VHD 块）——
  原文：*"The VHD pogo block can also connect to DUT boards that are designed for the
  HD pogo block"*，**直接引本页的兼容规则**
- **XPS256**：`XPS256 pogo cable assembly EK751HDA`（16 HD）/ `EK751VHDA`（8 VHD）/
  `XPS256 pogo pin assignment`（**HD 与 VHD 互相兼容那两句都在这里**）
- **发布信息**：`Release information`（`02.03.01.01`）也链了本页

**本页的下行与并列**：

- 父：[[pogo-pad-and-via-design]]（本页是它 `Subtopics` 里声明的子主题）
- 兄弟：[[inter-layer-via-design]]
- 上行流程页：[[pin]]（画 DUT board 属于 pin 这一段）

**不建页的两个**：`02.03.07.07.03_Pogo_via_examples`、`02.03.07.07.04_Pogo_via_depth_example`
——内容是**插图**不是文字，单独建页只会得到没有正文的空页；等 [[inter-layer-via-design]]
扩写时并入。同上，本页「语法 / 参数」表里的三张图也不单独建页。

> 本页**没有推断**：上面每条都是原文或边数据里的原句。

## 版本

- **Introduced before SmarTest 6.3.2**
- **SmarTest 7.5.3 / 8.3.2：加入了 very-high-density (VHD) pogo 块的推荐。**
  —— 这条要读出两层意思：**① 7.5.3 就已经有 VHD 建议了**，所以本 wiki 面向的
  **7.10.3 里它是在的**；② 同时标 `8.3.2` 是因为这条改动**同时进了 7.x 和 8.x 两条线**
  （8.3.2 比 7.10.3 新，**别把 8.3.2 读成「7.10.3 里还没有」**）。

## ⚠️ 语料里有一类坏字符（**本文档每一处 SD/HD/VHD 都中招**）

原文里写作 `Standard鈥慸ensity`、`High鈥慸ensity`、`Very鈥慼igh鈥慸ensity`。
它不是三个怪字，是**「短横 + 后面那个字母」被一起编码坏了**：

| 语料里 | 实际是 | 验算 |
|---|---|---|
| `鈥慸` | `–d` | `Standard鈥慸ensity` = *Standard-density* |
| `鈥慼` | `–h` | `Very鈥慼igh` = *Very-high* |
| `鈥慴` | `–b` | `pattern鈥慴ased` = *pattern-based* |

**早先只记成「`鈥慴` 是 en dash」是不完整的**——它连**后面那个字母一起吃掉了**，
只按「换成 en dash」去替换，会得到 `Standard-ensity` 这种残词。
**这是语料的问题，不是抽取的 bug，raw 只读不许改（§1.1）。**

## 出处

- 定义文档：`02_System_reference/02.03_DUT_board_design_reference/02.03.07.07.01_Pogo_block_compatibility.md`
  （TDC `348112.htm`，3,659 字节，33 行）
- **入边 44 条 / 24 篇**——口径同 `hubs-dedup.csv`，**只算 `inline` 边**
  （目录边 `toc` 不计入；本页没有目录边）
- 所属：**DUT board design reference**（`02.03`）
- 本页 `verified: doc-only` —— 只在 TDC 文档里确认，**没有对着任何一块真实板子核过**。
  要按它画板，**先让人核一遍**（§11：文档里有 ≠ 你这块板子上是这样）。
