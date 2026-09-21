---
type: concept
title: Concepts of logical boards
layer: n/a
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.04_Model_File_and_Licensing/02.04.01.02_Concepts_of_logical_boards.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# Concepts of logical boards

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

**没有加标记的语法段。** 定义文档里没有 `Syntax` / `Parameters` / `Example`
这类**段标记**，跟着 `Subtopics` 找一层也没有。
**所以本脚本一个字都不收录**——没有段标记时「哪一段是语法」是猜，而猜就是编（§4）。

<!-- 语法节 end -->

## 是什么

**logical board（逻辑板）是一个软件概念，不是一块真板子。**

原文两条定义，各一句话：

> 「For cards that provide **more than 16 channels**, the channels will be **divided into units of
> 16 channels**.」
>
> 「A group of **16 digital channels** forms a **logical board**.」

**所以：逻辑板 = 16 个数字通道打包成的一个寻址单位。**
一块超过 16 通道的卡，会被切成若干个这样的单位。

### 逻辑板 ↔ 地址：一一对应，且地址不许复用

- **每个逻辑板要占最多 16 个唯一地址。** 原文对「唯一」的定义写得很死：
  `unique address = only used once, therefore not used to address any other resource in the
  test system`——**这个地址在整个测试系统里不能再寻址别的资源**。
- **地址范围写作 `1 01 01 ... 8 64 16`**。
- **这些地址通常同时也标出了该通道 pogo 块在 DUT 接口上的物理位置。**

> ⚠️ **原文没有解释 `1 01 01` 里这三段数字各代表什么。** 本页只照抄这个形态，
> **不替这三段做解释**。下面那两个例子也一样，**本页读不出三段的含义**——
> 要判断请回 raw 读那四篇 `Related information`。

### 物理块装不下时：virtual pogo block

**判据是一条**：

> 「If a pogo block provides pogo pins for **more than 16 channels** (= 1 logical board),
> **2 or more unique addresses are required**.」

**原文给的例子**（同一个地址范围里取的两段）：

| 地址段 | 原文的说法 |
|---|---|
| `4 31 01 ... 4 63 16` | **physical location** of the channel's pogo block in the DUT interface |
| `5 32 01 ... 5 64 16` | **virtual pogo block**——`not physically used in the DUT interface, but **required by the software to address the channels**` |

**virtual pogo block 的定义**：

> 「Virtual pogo blocks are block locations that **SmarTest uses to address pins that it cannot
> address physically**.」

**一句话**：物理上够不着的针，软件再给它一个块位置来寻址。
**它不是硬件，是软件为了把通道凑成一个完整逻辑板而补出来的地址。**

### ⚠️ 原文这两个例子自相矛盾，本页照实并列、没有替它调和

原文 `## Virtual pogo blocks` 只给了两个例子，**两条都写着 32 通道/物理块，却给出不同的块数**：

| 原文写的 | 通道数 | 需要的块数 | 卡片 |
|---|---|---|---|
| **High-density pogo (HD)** blocks | **32 channels per physical pogo block** | **Two**（1 物理 + 1 虚拟） | PS1600、PS5000、**XPS256、DPS64** |
| **Very-high-density pogo (HD)** blocks | **32 channels per physical pogo block** | **Four**（1 物理 + **3** 虚拟） | PS1600、PS5000 |

**这两条对不上**：**同样是 32 通道，按「16 通道一个逻辑板」算只可能是 2 块**
（32 ÷ 16 = 2），**不可能是 4 块**。而且第二条**自称 very-high-density，缩写却仍写着 `(HD)`**。

**本页不猜哪个对、也不替它改成 `(VHD)` 或改通道数。** 三种可能都列在这儿：

- 第二条的**通道数**印错了（若真需要 4 块，应当是 64 通道）；
- 第二条的**块数**印错了；
- 第二条的 **`(HD)`** 是 `(VHD)` 的笔误，**而正因为它是另一档密度，4 块才对**——
  第三种解释最顺，**但原文没写，所以它只是解释，不是事实**。

**要用这个数，请回 raw 看那一段。**

## 典型用法

**1. 什么时候翻这一页**：算**地址分配**、或遇到**「这块 pogo 上的针为什么分在两个块里」**
这类问题时。它是**寻址模型**，不是操作步骤。

**2. 本页回答的那个问题**：
**「一块物理 pogo 块上超过 16 个通道时会发生什么」**——
答案：**会多出 virtual pogo block，通道被拆到多个逻辑板地址上去寻址。**

**3. 和 [[utility-line-assignments]] 的分工**：
那一页讲 **utility pogo block**（基础设施通道）；本页讲 **digital channel** 的逻辑板划分。
**两者都叫 pogo block，但不是同一批块**——**别把这两套编号混起来用**。

**4. 本页不回答**：某个具体地址段对应哪块卡、哪个物理位置
（那要读 `POGOCABLING section` 那几篇，**本页没读**）。

## 和谁有关

- [[pin]] — 本页 `stage: pin` 的理由：讲的是**通道寻址与 pogo 块分配**
- [[utility-line-assignments]] — **同样有「16 通道一块」的数**，但那是 utility line 的块；
  两页可对照读，**编号体系不同**
- [[pogo-pad-and-via-design]]、[[pogo-block-compatibility]]、[[inter-layer-via-design]] —
  同属 DUT board / pogo 这一族，讲的是**物理设计**；本页讲**软件寻址**
- [[dps128-dps64-cards]] — 原文第一个例子里点了 **`DPS64`** 这张卡
- [[xps256-status-flags]] — 同上，第一个例子里点了 **`XPS256`**
  （**注意两张卡片清单不一样**：`XPS256`/`DPS64` 只出现在第一条里）
- [[ps1600]] / [[ps5000]]（**均未建**）— 两张卡名原文各点了一次
- [[sharing-configuration-file]]（**未建**）— 那份文件里有 `domainsGetSiteAtPos` 之类的
  三维定位函数（见 [[mtp-shared-test-commands]]），**和本页的地址模型可能相关，本页不判**

## 版本

- **Introduced in SmarTest 7.10.0**

> **注意这个版本号很新**——语料是 SmarTest **7.10.3** 的文档，
> 也就是说**这一套寻址模型是 7.10 才写进文档的**。
> **本页据此不做任何推断**（例如「7.10 之前怎么办」——**原文没说**）。

## 出处

`sources:` 一篇：
`02_System_reference/02.04_Model_File_and_Licensing/02.04.01.02_Concepts_of_logical_boards.md`

**本页没做的**：

- **`## Related information` 那四篇一篇都没读**：
  `Conversions: pogo mapping file <-> POGOCABLING`、
  `Pogocabling entries for various card types`、
  `POGOCABLING section`、`GLOBAL section`。
  **所以「地址三段数字各是什么」「某个地址段怎么落到物理位置」本页一个字都没有。**
- **一张图都没有**（本篇也没有图）。
- **`PS1600` / `PS5000` / `XPS256` / `DPS64` 四张卡本页只知道名字**，
  没有它们的通道数或别的规格——**上面那个矛盾正是卡在这上面**：
  原文说了「32 channels per physical pogo block」，**但没说这句话对着哪张卡**。
- **`02.04_Model_File_and_Licensing` 底下其余篇本页没读。**

`verified: doc-only`
