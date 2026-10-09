---
type: concept
title: Pogo pad and via design
layer: n/a
stage: pin
tags: [pin, dut-board, pogo, hardware-design, stackup]
related: [pin, pogo-block-compatibility, inter-layer-via-design]
sources:
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.07.07_Pogo_pad_and_via_design.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# Pogo pad and via design

> **一句话**：**DUT board（被测板 / load board）上的布线尺寸规则。**
> pogo 针往下压到 DUT board 上，靠一块**焊盘（pad）**和一条**过孔（via）**把信号引到板内走线；
> 这一页说的是这两样东西**该做多大、多深、接地怎么配**。
> **它和写测试程序无关，是画板子的人用的**（`stage: pin`）。

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **884 字符逐字取自** `<02_System_reference/02.03_DUT_board_design_reference/02.03.07.07_Pogo_pad_and_via_design.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Tables（脚本逐字抽取，第 1 张）

| Minimum pad size: | 56 mil (~1.4 mm)<br><br>Recommendation: For pogo pin landing holes of digital and analog channels use a pad size of at least 1.4 mm to 1.5 mm, for utility and DPS channels at least 1.6 mm to 1.8 mm, with a maximum hole diameter of 0.7 mm. A smaller pad size will cause contact problems with the DUT interface. |
|---|---|
| Signal pogo via drill size: | 26 + 1/-3 mil finished hole size (~0.7 mm) |
| Minimum pogo via length: | 13 mil (~0.33 mm) |
| Number of adjacent ground pogo vias: | 4 |
| Signal via to ground via pitch: | 100 mil |
| Removal of non-functional pads: | Yes / No |
| Back drilling: | Yes / No |
| Ground plane clearance or antipad: | variable |
| Power plane clearance or antipad: | >= ground plane clearance |
| Ground via thermal straps: | No (direct connect to ground plane) |
| Hard Au plating | Min. 30 µinches, Knoop hardness 130-200 |

<!-- 语法节 end -->

## 是什么

- **pogo pad 和 pogo via 的作用**（原文）：*"The pogo pad and via connect the pogo pin to the
  signal trace on the DUT board."*
- **设计取决于两个变量**（原文）：**pogo 针的类型**、**DUT board 的叠层（stackup）**。
  —— 所以同一套规则不能套所有板子，这就是为什么后面还有产品专用的那一篇。
- **本页是「通用规则」**，原文：*"This section covers the general rules for designing pog pads
  and pogo vias. For product-specific rules, refer to …"* → XPS256 VHD 有自己一篇
  （`02.03.08.01.07.04_XPS256_VHD_pogo_pad_and_via_design`，**未建页**，见下「和谁有关」）。

### 机械要求：最小焊盘尺寸（**这一行脚本没抽到，原因见下**）

> 下面这段逐字取自 raw 的 L23–L27。**它不在上面的「语法 / 参数」节里**，因为这一行是**坏的**：
> HTML 转 markdown 时被拆成了 `| Minimum pad size: |` + 空行 + 散文 + 空行 + `|`，
> **不构成连续表格行**，所以 `table_runs()` 抓不到（脚本只抓到下面那 10 行）。
> **缺口不修**——修它要猜那段散文属于哪一行，**猜就是编**。所以这里照抄原文并给出行号：

> *"Minimum pad size: 56 mil (~1.4 mm)*
> *Recommendation: For pogo pin landing holes of digital and analog channels use a pad size of
> at least 1.4 mm to 1.5 mm, for utility and DPS channels at least 1.6 mm to 1.8 mm, with a
> maximum hole diameter of 0.7 mm. A smaller pad size will cause contact problems with the DUT
> interface."*
>
> —— **数字对不上不是矛盾**：`56 mil ≈ 1.42 mm` 是**下限**，后面的 1.4–1.5 / 1.6–1.8 mm
> 是**推荐区间**。**utility 和 DPS 通道的焊盘要更大**，因为它们要过电流。

### ⚠️ 语料里有一个坏字符

脚本抽出来的表最后一行是 `Min. 30 碌inches`。原文是 **30 µinches**（微英寸）——
**`碌` 是 `µ` 的编码损坏**。引用这个数值时不要照抄那个字。

## 典型用法

**这是给板厂 / layout 工程师的检查清单**，不是给测试工程师的。

原文给的流程（三步）：

1. **先满足机械要求**：*"When designing pogo pads and pogo vias for the V93000 you must
   respect certain mechanical requirements."* —— 上面的表格就是这些要求。
2. **想优化性能，做 3D 电磁场仿真**：*"A typical approach for a pogo via design is to
   optimize the via structure through an electromagnetic (EM) field simulation."*
   仿真用 pogo 针 + pogo via 的 3D 模型（原文配了图）。
3. **仿真不是必须的**（原文，重要）：
   > *"An electromagnetic field simulation is time consuming and not required for most
   > applications. A pogo via design optimized for a given stackup can be reused on a
   > different stack-up. Experience shows that the performance of the via will not change."*

   —— **可以复用**：为某个叠层优化好的 via 设计，换到别的叠层上性能不变。
   **这一条是省钱的**：不必每块板子重做仿真。

原文还给了两篇参考文献（DesignCon 2006 / APMC 2006，作者含 Jose Moreira、Heidi Barnes），
需要深究时按上面「语法 / 参数」节里那条路径去 raw 找。

## 和谁有关

**几乎每一个 pogo pin assignment 页都指向本页**——它们页脚统一一行
*"See also Pogo pad and via design."*。这是本页入边的主体，覆盖的针卡/线缆组件包括：

`PS5000` / `PS1600` / `XPS256` / `AVI64` / `FVI16` / `PVI8` / `HSM15/16G` /
`Link Scale USB3` / `Wave Scale RF (10 MHz clock)` / `PSSL`，
以及 `E8023PA`（8 HD 块）/ `E8023PB`（2 VHD 块）/ `E8023PE`（8 MS-DPS 块）/
`E8023PK`（4 VHD 块）四个线缆组件。
→ **含义：这些针卡的 pogo 焊盘/via 都按本页的通用规则做，没有各自一套。**

**明确写「通用规则适用于我」的两处**：

- `Pin Scale 5000 card`：*"The standard recommendations for pogo pads and vias apply to all
  pogo block types of the Pin Scale 5000 pogo cable assemblies."*
- `PS5000 pogo pin assignment`：同一句。

**被当作「默认值」引用的三处**：

- `Layout information: DUT board`：*"For the default pogo pad layout and via design, refer
  also to Pogo pad and via design."*
- `UHC4 / UHC4T DUT board layout`、`Layout recommendations` —— 两处**直接锚到表的某一行**：
  *"refer to [Minimum pad size] and [Signal pogo via drill size] in Pogo pad and via design"*。
  **这说明了上面那张表里哪两行是真正被引用的**（焊盘尺寸、钻孔尺寸）。

**并列引用的两处**（本页 + XPS256 专用版一起给）：

- `XPS256 pogo block specifications`、`XPS256 pogo pin assignment`（各两个副本：
  02.03 与 02.05 两个子树下各一份）：
  *"See also [XPS256 VHD pogo pad and via design] and [Pogo pad and via design]."*

**子主题（本页的下行）**

- [[pogo-block-compatibility]] —— SD / HD / VHD 三种 pogo 块的兼容性
- [[inter-layer-via-design]] —— 层间 via 设计
- `02.03.07.07.03_Pogo_via_examples`、`02.03.07.07.04_Pogo_via_depth_example` —— **图例**。
  **不建页、也不链**：这两篇的内容是**插图**不是文字，单独建页只会得到两个没有正文的页面；
  等 [[inter-layer-via-design]] 建起来时并入它。
- 反向：`Pogo block compatibility` 也指回本页，并进一步指向
  `Layout information: DUT board` 和 `Pogo pin assignment`。

> 以上每条都来自 `edges.jsonl` 里带原句的边。**本页唯一的推断**是「utility/DPS 焊盘要更大
> 是因为要过电流」——原文只说「要更大」，没说为什么。

## 版本

- **Introduced before SmarTest 6.3.2**（`Functional changes` 段，仅此一条）

> **注意这一条的性质**：pogo pad / via 是**板子的物理尺寸**，
> 「SmarTest 6.3.2」只是文档的版本标法，**不代表这块板子的设计规则跟着软件版本变**。
> 换句话说：**看到旧板子也别急着怀疑这一页过时**，机械尺寸不太会变。
> （这句是**推断**，文档没写。）

## 出处

- 定义文档：`02_System_reference/02.03_DUT_board_design_reference/02.03.07.07_Pogo_pad_and_via_design.md`
  （TDC `91610.htm`，3,196 字节，49 行）
- **入边 55 条 / 33 篇文档**：`extract/pack/05-pogo-pad-and-via-design.md`
  （55 是边数，33 是去重后的文档数；口径同 `hubs-dedup.csv`：**只算 `inline` 边**。）
- 所属：**DUT board design reference**（`02.03`）
- 本页 `verified: doc-only` —— 只在 TDC 文档里确认存在，**没有对着任何一块真实板子核过尺寸**。
  **用之前请让做板的人核一遍**（§11：文档里有 ≠ 你这块板子上是这样）。
