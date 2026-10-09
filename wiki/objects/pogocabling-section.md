---
type: object
title: POGOCABLING section
layer: file
stage: pin
tags: [model-file, pogo, pogocabling, pin-configuration, dps128, dps64, test-head, dut-interface]
related: [model-file, logical-boards, dps128-dps64-cards, pogo-block-compatibility, pogo-pad-and-via-design, pin, project, index-versions]
sources:
  - 02_System_reference/02.04_Model_File_and_Licensing/02.04.01.03.02.02_POGOCABLING_section.md
  - 02_System_reference/02.04_Model_File_and_Licensing/02.04.01.03.02.02.01_Pogocabling_entries_for_various_card_types.md
  - 02_System_reference/02.04_Model_File_and_Licensing/02.04.01.03.02.02.02_Conversions__pogo_mapping_file__-__POGOCABLING.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# POGOCABLING section

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **6,082 字符逐字取自** `<02_System_reference/02.04_Model_File_and_Licensing/02.04.01.03.02.02_POGOCABLING_section.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
`<physical_location>`（raw: `02.04.01.03.02.02_POGOCABLING_section.md#_106944__row_Physical_location`）: `pogoblocks`（raw: `02.04.01.03.02.02_POGOCABLING_section.md#_106944__row_Pogoblocks`） = "<pogoblock_list>", `type`（raw: `02.04.01.03.02.02_POGOCABLING_section.md#_106944__row_Type`） = SD | HD1x256 | HD2x32 | HD4x32 | VHD1x128 | VHD4x32 | REDIRECT, subtype
```

Parameters
| <physical_location> | Specifies the physical channel card position within the test head and the respective control segment. For more information regarding the control segments refer to `pogo mapping`（raw: `../02.05_Test_Head_Cards/02.05.01.04_Pogo_mapping.md`）.<br><br>The format of the number is CSS:<br><br>- C represents the control segment (1 to 4).<br>- SS represents the control segment slot number (01 to 18).<br><br>Refer to table `Card cage allocation based on test head type`（raw: `02.04.01.03.02.02_POGOCABLING_section.md#_106944__t_Card_cage_allocation`） below for the assignment of the control segment and the control segment slot number.<br><br>SS=09 and SS=18 address the two slots reserved for the legacy DPS cards, such as the MS-DPS. |
|---|---|
| pogoblocks | Specifies the pogo pin blocks. <pogoblock_list> is a double quoted string defining the ordered list of pogo blocks or pogo block ranges. Use commas (,) to specify a list, like `"101, 103"`. Use hyphens (-) to specify a pogo block range, like `"101-104"`. You can also mix pogo blocks and pogo ranges, like `"101, 210-212"`.<br><br>The total pogo block range is N MM, with N=1 to 8, MM=01 to 64. See also topic `DUT interface layout`（raw: `../02.03_DUT_board_design_reference/02.03.03.01_DUT_interface_layout.md`）.<br><br>The physically addressable pogo block range depends on the selected pogo cable.<br><br>Note The order of list must correspond to the structure of the pogo cable assembly. The first pogo block of the list defines always pogo block A of the cable. The last pogo block of the list defines always the last pogo block of the cable. |
| type | Specifies the pogo cable type.<br><br>- SD is used for the standard pogo cable with 16 channels per pogo block. Depending on the channel card, one SD pogo cable ends in 1-8 pogo blocks with 16 channels each.<br>- HD2x32 is presently not used by any channel card.<br>- HD4x32 describes a pogo cable with 32 channels per pogo block. One HD4x32 pogo cable ends in 4 pogo blocks with 32 channels each.<br>- VHD1x128 describes a PS1600 pogo cable with two VHD pogo blocks and 64 channels per pogo block that is to be used for special configurations only.<br>- VHD4x32 is not yet used. It describes a DPS128 pogo cable with four pogo blocks and 32 channels per pogo block.<br>- REDIRECT, subtype is used for special DPS pogo cables which shall work also on older software revisions.<br><br>If the software detects a "redirect" statement, the software will start, even if the information following redirect is unknown to this software revision.<br><br>The type parameter is optional. If not specified, the system defaults to SD. |

The following table shows the location of digital logical boards and DPS card based on the POGOCABLING syntax.

Card cage allocation based on test head type
| Control segment | Card cages (cc), physical locations (CSS-CSS) | Card cages (cc), physical locations (CSS-CSS) | Card cages (cc), physical locations (CSS-CSS) | Card cages (cc), physical locations (CSS-CSS) | Card cages (cc), physical locations (CSS-CSS) | Card cages (cc), physical locations (CSS-CSS) | Card cages (cc), physical locations (CSS-CSS) | Card cages (cc), physical locations (CSS-CSS) |  | Default location for DPS | Default location for DPS | Default location for DPS | Default location for DPS |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Control segment | LTH | LTH | STH | STH | CTH | CTH | ATH | ATH |  | LTH | STH | CTH | ATH |
| Control segment | Card cage | Location | Card cage | Location | Card cage | Location | Card cage | Location |  | LTH | STH | CTH | ATH |
| 1 | 5 | 101-109 | 1 | 101-109 | 1 | 101-109 | 1 | 101-109 |  | 4 | 3 | 1 | 1 |
| 1 | 1 | 110-118 | 3 | 110-118 | 2 | 110-118 |  |  |  | 3 | 1 | 2 |  |
| 2 | 2 | 201-209 | 2 | 201-209 |  |  |  |  |  | 8 | 2 |  |  |
| 2 | 6 | 210-218 | 4 | 210-218 |  |  |  |  |  | 7 | 8 |  |  |
| 3 | 3 | 301-309 |  |  |  |  |  |  |  | 1 |  |  |  |
| 3 | 7 | 310-318 |  |  |  |  |  |  |  | 5 |  |  |  |
| 4 | 8 | 401-409 |  |  |  |  |  |  |  | 6 |  |  |  |
| 4 | 4 | 410-418 |  |  |  |  |  |  |  | 2 |  |  |  |

> ⚠️ 转录说明（非原文）：本表在上游 HTML 里含合并格（colspan / rowspan）；
> 跨格文字已按覆盖范围重复写出（**不是原表里有重复的格子**）。真结构见 `tdc-html/raw/106944.htm`。

For more information refer to parameter `physical_location`（raw: `02.04.01.03.02.02_POGOCABLING_section.md#_106944__row_Physical_location`） in table `Parameters`（raw: `02.04.01.03.02.02_POGOCABLING_section.md#_106944__t_Parameters`） above.

For the default relationship between card cages and groups see:

`Test Head sizes - Compact Test Head`（raw: `../02.02_Specifications/02.02.03.04_Test_Head_sizes_-_Compact_Test_Head.md`）

`Test Head sizes - Small Test Head`（raw: `../02.02_Specifications/02.02.03.05_Test_Head_sizes_-_Small_Test_Head.md`）

`Test Head sizes - Large Test Head`（raw: `../02.02_Specifications/02.02.03.06_Test_Head_sizes_-_Large_Test_Head.md`）

`Test Head sizes - A-Test Head`（raw: `../02.02_Specifications/02.02.03.03_Test_Head_sizes_-_A-Test_Head.md`）

`Test Head sizes - Compact Test Head with DUT scale interface`（raw: `../02.02_Specifications/02.02.03.08_Test_Head_sizes_-_Compact_Test_Head_with_DUT_scale_interface.md`）

`Test Head sizes - Small Test Head with DUT scale interface`（raw: `../02.02_Specifications/02.02.03.09_Test_Head_sizes_-_Small_Test_Head_with_DUT_scale_interface.md`）

For drawings of all test heads, see Mapping physical resources.

### Example

The following example illustrates the pogocabling entry of a double density digital card. 32 channels (2 logical boards) are routed via two pogo blocks of 16 channels each.

```
101: pogoblocks= "101,102"
```

For further examples see `Pogocabling entries for different card types`（raw: `02.04.01.03.02.02.01_Pogocabling_entries_for_various_card_types.md`）.

<!-- 语法节 end -->

## 是什么

**model file 里的一个段**，管的是**通道卡插在哪 ↔ DUT 接口上哪个 pogo 块**的对应关系：

> In the POGOCABLING section of the model file you define the mapping between card slots (the physical position of the channel cards within the card cage respective the control segment) and pogo blocks on the DUT interface. This feature allows flexible routing between card cage slots and pogo blocks on the DUT interface.

**要它干嘛**：

> The pogo mapping feature gives you additional flexibility as it allows different cabling rules for the same DUT board and test head size, but for varying test head content.

**⚠️ 这一条对本 wiki 最要紧（我们是 SmarTest 7.10.3）**：

> SmarTest 6.5.x releases support both the use of pogo mapping files and the POGOCABLING format in the model file. SmarTest 7.0 or later supports only the POGOCABLING format.

**换句话说：7.x 上那个老式的「pogo mapping file」已经不能用了**，
必须把信息写进 model file 的 `POGOCABLING` 段。
（**而"同一个 model file 里两种混用"是启动就退出的错误之一**——那条在下面的
「启动就退出」清单里，也在本页脚本写的那一节里。）

## 典型用法

### 语法与参数

**见本页 `## 语法 / 参数` 一节**——那一节是 `extract/objscaffold.py` **逐字从 raw 抽的**（§4），
包含语法行、`physical_location` / `pogoblocks` / `type` 三个参数的完整说明、
`Card cage allocation based on test head type` 表和例子。**本页不重抄一遍**
（重抄一遍就是把它从"文档事实"降级成"我的转述"，§11）。

### 启动就退出：七种情况

**这一段是本页最实用的一节**——原文没有把它放在 `## Errors` 里，
而是放在 `## Error messages` 里，**且措辞是"启动会终止"，不是"报个错"**：

> SmarTest startup will terminate with explicit error messages in the following cases:

> - an invalid pogo block number is used.

> - both pogo mapping file and POGOCABLING format are used in one model file.

> - in online mode, the provided pogo blocks in the model file do not match the density of the installed card variant.

> - in offline mode, the density of the used hardware variant in the model file does not match the provided pogo blocks in the model file.

> - an S2 pogo block is used to specify the pogo cabling of a UHC4T card.

> - an S1 pogo block is mapped to a UHC4T card, but the corresponding S2 pogo block is occupied by another card.

> - a pogo cable type is specified, which is not supported for the installed channel card.

> **⚠️ 第 3 和第 4 条是一对**：**同一个"密度对不上"，在线模式和离线模式**分别**报。**
> 在线模式查的是「model file 里写的 vs 机台里实际装的」，
> 离线模式查的是「model file 里写的硬件变体 vs model file 里写的 pogo 块」——
> **离线模式没有硬件可对，所以只能自己跟自己比。**

> **⚠️ 第 5、6 条与 UHC4T 有关，而 UHC4T 在 7.10.0 已经停止支持**（见下「版本」）——
> **对 7.10.3 来说这两条是历史条目**，本页照录原文，**不据此说 7.10.3 上还能遇到**。

### 换一种卡就要换一套写法

不同卡型的 `POGOCABLING` 条目**不一样**，原文专门有一篇分册
（`02.04.01.03.02.02.01_Pogocabling_entries_for_various_card_types.md`）。**两条要点**：

**① 有的卡要写"虚拟 pogo 块"，偏移量是固定数字，而且软件会查。**

| 电缆 | 虚拟块偏移 | 软件查什么（原文） |
|---|---|---|
| E8023PB（2 VHD 块，DPS64 或半个 DPS128） | **+400** | — |
| E8023PK（4 VHD 块，DPS128） | **+400** | — |
| E8023PC（4 HD 块，仅 DPS128-HC） | **+432** | `SmarTest checks that eight addresses are entered, that the offset for the virtual pogo blocks is 432 and that the mapping (config) is correctly set up.` |
| E8023PD（2 HD 块，仅 DPS64） | **+432** | `SmarTest checks that four addresses are entered, that the offset for the virtual pogo blocks is 432 and that the mapping (config) is correctly set up.` |
| E8023PE（8 个 MS-DPS 式块，仅 DPS128-HC） | 虚拟三位块号 | `SmarTest checks that eight addresses are entered and that the mapping (config) is correctly set up.` |
| E8023PF（2 个 MS-DPS 式块，仅 DPS64） | 虚拟三位块号 | **原文这一节没有 check 句**——同一族里只有它没写；本页照实留空，不替它补 |
| E8023PG（4 个 MS-DPS 式块，仅 DPS64） | 虚拟三位块号 | `SmarTest checks that four addresses are entered and that the mapping (config) is correctly set up.` |
| E8023PA（8 HD 块，标准）/ E8023PH（4 HD 块，DPS64 标准） | 不用虚拟块 | `There are no special rules and no special checks in the software.` |

**② 用虚拟块时，model file 里要写的块数比电缆上实有的块数多一倍**（原文，见下关于坏字符的说明）：

> Note that in the model file you have to define twice as many pogo blocks as the pogo cable assembly has pogo blocks: All physically available pogo blocks and the same number of virtual pogo blocks that cover the additional channels

> ⚠️ **上句在 `B1 … B16` 处截断，不是原文只到这里。** 原文那半句含
> **GBK mojibake**（`B1 鈥?nbsp;B16`，§11.2 ①），**引它会把坏字符抄进 wiki**。
> **本页只引到坏字符之前的连续部分**（§11.1 允许在引文尾部截取；**本页没有加省略号**——
> `…` 只许出现在原文自己就有的地方）。**raw 一个字节没动。**

**③ UHC4T 的 E8013UHP 电缆还有一条"只写一半"的规矩**：

> Only the S1 position must be entered in the model file, the software blocks the adjacent S2 position automatically.

（原文紧接着用 DPS 段说明：**四个通道在 DPS 段里全记在同一个块号上，
尽管物理上接在两个块上**——`Note The DPS section shows that all four channels are assigned
to pogo block 230 although they are physically wired to the two blocks 230 and 430.`）

### 想知道某张卡占几个 pogo 块，有脚本

> To find out how many pogo blocks are used for a specific HW type, you can run the script: /opt/hp93000/soc/system/config/xoc.hw.cor.detection.ZSIoCardFactory/getDensityForVariants.

### 从老的 pogo mapping file 换过来

**两个方向都有办法**（原文分两节）**，但往下换要起一个 6.5.x 的 SmarTest**：

> - Start a SmarTest version 6.5.x (not 7.x). A log file PogoCabling.log will be created in the directory /opt/hp93000/soc/system/log. The log file contains the current pogo mapping information in the `POGOCABLING` format.

**拿日志里的内容贴进 model file 即可。** 反方向（新→旧）有一支转换脚本，
**并且转换完要记得把 `POGOCABLING` 段删掉**：

> - Refer to the saved pogo mapping file in the model file and remove the `POGOCABLING` section.

> **⚠️ 6.5.x 上不需要转换**：`SmarTest 6.5.x supports both the pogo mapping file and the
> `POGOCABLING` format. A conversion is not required.`——
> **「要转换」和「两种都支持」是同一篇文档里对同一件事的两句话**，
> 分别针对"用 7.x 打开老文件"和"用 6.5.x 打开"两个场景，**不是矛盾。**

## 文档没写清的地方

1. **`HD1x256` 这个类型值，在参数的取值列表里出现了，但正文的逐条说明里没有它。**
   语法行写的是 `type = SD | HD1x256 | HD2x32 | HD4x32 | VHD1x128 | VHD4x32 | REDIRECT`，
   而解释 `type` 的六条里，**有 `HD2x32`（明说 `presently not used by any channel card`）、
   有 `HD4x32`，就是没有 `HD1x256`**。**本次未找到它的说明**——本页照录取值列表，不替它解释。
2. **`REDIRECT` 的 `subtype` 取值有哪些，文档没给完整清单。** 分册里出现的
   `E8024UHPS` / `E8023PB` / `E8023PC` / `E8023PD` / `E8023PE` / `E8023PF` / `E8023PG`
   都是实例，**但"一共有哪些合法取值"没有一张表**。
3. **`config` 关键字的语法没有正式定义。** 它**没出现在语法行里**
   （语法行只有 `physical_location` / `pogoblocks` / `type`），
   只在分册的例子和 `SmarTest checks …` 那句里出现。**它的分号、等号、逗号的规则要靠例子反推**，
   本页不替它总结成语法。
4. **两个 VHD 电缆的"支持版本"写的是四段式版本号**：
   `E8023PB is supported by SmarTest 7.5.4.4, 8.3.4.2, and higher.`——
   **本 wiki 面向 7.10.3，按字面这些早就够了**；但**四段版本号与三段的对应关系文档没讲**。
5. **`Card cage allocation based on test head type` 表在 raw 里被摊平得很厉害**
   （`110-118` 单独占了一行、空单元格成串），**本页因此不转述这张表**——
   **要看得回 raw**（路径见「出处」）。摊平是抽取瑕疵，不是文档缺陷。

## 和谁有关

- [[model-file]]——POGOCABLING 是 model file 的一个段。**这一页还没有**，
  但它在 `extract/dangling.csv` 里（**被 4 处引**），**照 §9.1 可以链**。
- [[logical-boards]]——原文反复引 `Concepts of logical boards`；
  「一个 pogo 块 = 多少个通道」和逻辑板概念直接相关。
- [[dps128-dps64-cards]]——分册里**大半篇幅**在讲 DPS128 / DPS64 的各种 pogo 电缆。
- [[pogo-block-compatibility]]、[[pogo-pad-and-via-design]]——pogo 块本身的形状与网格。
- [[pin]]——脊椎里的 pin 段；**这一段是 pin/channel 配置在文件侧的落点**。
- [[project]]——model file 属于工程侧的文件，`project` 段讲的就是这类东西。

## 版本

原文各篇的 `## Functional changes` 汇总（**关键几条**）：

> **逐条照录**（`POGOCABLING_section` 与 `Conversions` 两篇的 `## Functional changes` 完全一致）。

- `Introduced in SmarTest 6.5.0`
- `SmarTest 7.0.1: New pogo cable parameters: type and subtype`
- `SmarTest 7.0.1: New pogo block calculation for Pin Scale 9G cards`
- `SmarTest 7.1.0: New pogo cable parameter for PS1600`
- `SmarTest 7.1.0: New pogo block calculation for PS1600 cards`
- `SmarTest 7.1.3: MCE is added to the analog hardware types.`
- `SmarTest 7.5.4: Support of E8023PB and E8023PK VHD pogo cable assemblies for DPS128`
  （**这两支对本 wiki 是"已经有了"**——7.5.4 < 7.10.3）。
- `SmarTest 7.4.1: : Path and name of the conversion script adapted.`
  （**这条只在 `Conversions` 那一篇里有**，见「出处」里关于 `: :` 双冒号的记录。）
- **`SmarTest 7.10.0: End of support for Single density cards, DC Scale DPS32 / VI32, PVI8, UHC4, RF cards`**

> ⚠️ **最后这一条对本 wiki 最重要**：**7.10.0 起，单密度卡、DPS32/VI32、PVI8、UHC4、RF 卡停止支持**，
> 而我们面向 **7.10.3**——**也就是说 7.10.3 上再配这些卡不会按文档预期的行为走。**
> **本页把它逐字抄出来，但"停支之后会怎样"文档没写**，本页不猜。
> 这也解释了上面「启动就退出」里那两条 UHC4T 的错误**为什么属于历史条目**。

> 完整的版本时间线看 [[index-versions]]（机械汇编，§4）。**本页只挑与"这一段还能不能用"有关的。**

## 出处

| 说法 | raw |
|---|---|
| 段的作用、两种格式的支持边界、启动就退出的七条、语法行与三参数、卡笼表、例子 | `02.04.01.03.02.02_POGOCABLING_section.md` |
| 各卡型条目、虚拟块偏移 400/432、`SmarTest checks …`、两种"no special checks"、密度脚本、UHC4T 的 S1/S2 | `02.04.01.03.02.02.01_Pogocabling_entries_for_various_card_types.md` |
| 两个方向的转换步骤、`PogoCabling.log`、6.5.x 不需转换、`pogo_cabling =` 那一行 | `02.04.01.03.02.02.02_Conversions__pogo_mapping_file__-__POGOCABLING.md` |

> **`02.04.01.03.02.02_POGOCABLING_section.md` 的 `## Syntax` 段含一堆页内锚点链接**
> （`#_106944__row_Physical_location` 这类）。**本页脚本写的那一节已把它们机械改写成
> 反引号 + `（raw: …）`**——那是 `objscaffold.py` 的既定做法，**不是我手改的**。

文档事实，`verified: doc-only`。
