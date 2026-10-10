---
type: object
title: Sharing configuration file
layer: file
stage: pin
tags: [pin, sharing, file-format, mtp, dps, fixture-delay]
related: [pin, sharing-configuration, shared-continuity-test, shared-leakage-parallel-test, utility-line-assignments]
sources:
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.07.02_Sharing_configuration_file.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# Sharing configuration file

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **2,288 字符逐字取自** `<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.07.02_Sharing_configuration_file.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

The format of the sharing configuration file, using the keywords described below:

```
pin_configuration:
<pin config file name><context>

fixture_delay_files:
[+<baseboard fixture delay file>]
<fixture delay file> # position x=0,y=0
<fixture delay file> # position x=1,y=0
...
[; # starts next increment of y value
<fixture delay file> # position x=0,y=1
<fixture delay file> # position x=1,y=1
...]
...

domains:
<site number><site number> ...[; <site number><site number> ... ] ... # for z=0
... # for increments of z

[utility_control:
<name>[; (<equation>)] ; (<utility setting>) [; (<pin substitution>)]
...]

topology:
<topo definition> ; <pin group>
...

[fxdl_ignore_pins:
<pin>[, <pin>...] ]

[groups:
<pins or channels> ; offset=<group offset>
...]

[rss_buffer_pins:
<site no>; [<tmp src buffer>], <source buffer>, <global buffer 1>, <global buffer 2> [; ...]
...]
```

Note that # indicates comments that are not part of the syntax but serve to explain the semantics.

Keywords
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/96971.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：20 行 × 4 列。
> 首行（上游原文）：Field | Type | Description

### Example

This sample file works for a 4,2,2 structure; that is, a topology that can has daisy chains with up to four sites, up to two daisy chains connected to one driver pin, and repeats this structure over two domains.

```
pin_configuration:
./128Mx8_Moscato4.pin_forFXDL

fixture_delay_files:
./TSE_FXDL/Y2/FXDL1.txt
./TSE_FXDL/Y2/FXDL2.txt
./TSE_FXDL/Y2/FXDL3.txt
./TSE_FXDL/Y2/FXDL4.txt
;
./TSE_FXDL/Y2/FXDL5.txt
./TSE_FXDL/Y2/FXDL6.txt
./TSE_FXDL/Y2/FXDL7.txt
./TSE_FXDL/Y2/FXDL8.txt

domains:
1 2 3 4; 5 6 7 8
9 10 11 12; 13 14 15 16

utility_control:
idd; (y<=0); (U7=0x222&0xfff); (DEVICE_SUPPLY=VDD)
idd; (y>=1); (U7=0x111&0xfff); (DEVICE_SUPPLY=VDD)
iddq; (y<1); (U7=0x777&0xfff); (DEVICE_SUPPLY=VDD)
iddq; (y>=1); (U7=0xbbb); (DEVICE_SUPPLY=VDD)
leakage; (U5=0x001&0x001)
oc_reset; (U5=0x000&0x400,U5=0x400&0x400,U7=0x000&0xfff,U5=0x000&0x400)
default; (U7=0x000,U5=0x000&0x401)

topology:
x=4,y=2, actterm=VTERM ; SharedGrp
x=4,y=2, cross ; CrossTermGrp

fxdl_ignore_pins:
A3, A4

groups:
22601, 22602 ; offset=3
22701-22716 ; offset=-4
A0, A1 ; offset=4.7

rss_buffer_pins:
1,3,5,7; A.00, A.01, A.02
2,4,8,9; A.03, A.04, A.05
```

<!-- 语法节 end -->

## 是什么

- **定义 load board 的 sharing 结构**的文件。原文：*"The sharing configuration file defines
  the sharing structure of the load board. It is used by all sharing test methods as well as
  the fd_merge tool."*
- **内容**（原文列表）：引脚的物理设置 / fixture delay 文件名 / 每条 chain 上的 site 数 /
  y-shared 的引脚或 chain 数 / 每条 chain 上 site 的顺序 / **可选**：用于 rapid source sync
  的 buffer pins。
- **位置是硬要求**：原文 *"This file must be stored in the configuration directory under the
  current device."* —— 即 `<device>/configuration/`。
  （多处引用文档把路径写成 `<device directory>/configuration/`。）
- **属于哪一段**：load board 的引脚与 sharing 结构 → [[pin]]。
  即：它描述的是**硬件怎么接的**，不是测试怎么写。测试文档只是**引用**它。

## 典型用法

原文给了一个可直接照着改的**完整样例**（`4,2,2` 结构：每条 daisy chain 最多 4 个 site、
最多 2 条 daisy chain 接到同一个 driver pin、该结构在两个 domain 上重复），
逐字收在上面「语法 / 参数」一节的 `Example` 里——**本页不重述它**。

使用路径（全部来自入边原文）：

1. **fd_merge 工具**以该文件为输入，合并 fixture delay 文件
2. 各 sharing test method 用 `sharingConfigFile()` 指定用哪一份
3. `Measuring fixture delay` 的步骤是：先按 FXDL 文件写好本节这段
   `fixture_delay_files`，**再启动 SmarTest**，然后载入本文件里指定的 pin configuration file

## 和谁有关

**读它的 L2 API** —— [[sharing-configuration]] 类就是这份文件的访问器。原文：
*"The SHARING_CONFIGURATION class provides an API for accessing the data contained in the
Sharing configuration file."* 已知成员：`utilitySearchFirst()` / `utilitySearchNext()` /
`utilitySubstitutePins()` / `utilityActionExecute()` / `utilityGetApplicableSitesString()` /
`getTerminatedPinList()` …

**指向它的 test method**（每个都有 `sharingConfigFile()`）：
[[shared-continuity-test]]、`SHARED_IDD_TEST`、[[shared-leakage-parallel-test]]、
`SHARED_VBUMP_TEST`、`SOURCESYNC_TEST`。
（**只链已经进 backlog 的**——`SHARED_IDD_TEST` / `SHARED_VBUMP_TEST` / `SOURCESYNC_TEST`
三个入度不够、不在 `unowned.csv` 里，链了就是造永远不会建的悬空目标。
链接规则见 `schema.md` §2.2。）
其中 SharedVBump **依赖** `utility_control` 段里的 `vbump` 关键字才能把 DPS32 通道正确接到
VDD / VDDQ（原文：*"SharedVBump relies on the proper setup of the vbump keyword in the
utility control section"*）。

**用它的 L1 命令**：`FOR_EACH_TEST_BEGIN` / `FOR_EACH_TEST_BEGIN_WITH_RESET` /
`FOR_EACH_TEST_END` / `GET_CURRENT_UTILITY_CONTROL` —— 待测的 shared site
**按 `utility_control` 的设置分组**。

**工具**：`fd_merge`（要求本文件作为输入）、`DPS Sharing Diagnostic`。

**⚠️ 一条反复出现的覆盖规则（原文出现 5 次，逐字）**：

> "This parameter is ignored for DPS-shared load boards for which there is a utility_control
> section in the Sharing configuration file."

出现在 `SHARED_CONTINUITY_TEST.terminationDPS()` / `.supplyDPS()`、
`SHARED_IDD_TEST.vdd()` / `.vddq()`、`SharedContinuity syntax`、`SharedIDD syntax` 上。
**意思是：DPS-shared load board 且本文件里有 `utility_control` 段时，这些 API 参数被忽略，
以文件里的 utility 设置为准。** 两处都配了谁赢——这条值得记牢，它会让人「改了 API 参数
却没反应」。

**同一套语法的别处**：`Diagnostic configuration file` 原文明确说
*"The same syntactic options as for other utility control statements in the Sharing
configuration file apply"*（但**不做 pin substitution**）。

**`utility_control` 段里的 utility line 本身是什么** → [[utility-line-assignments]]。
本文件只写「哪条 utility line 在什么条件下设成什么值」，**line 的物理定义在那边**。

## 版本

- **Introduced before SmarTest 6.3.2**
- **MTP 3.0.1**：引入**全新语法**以支持 **Y sharing 和 hybrid sharing**
- **MTP 3.0.3**（MTP on SOC 103.0.0）：加入 **rapid source sync buffer pins** 段

> 注意第 2 条：**语法被整体换过一次**。看到网上/旧工程里的 sharing 配置文件写法时，
> 先确认它是不是 MTP 3.0.1 之前的。本 wiki 面向 SmarTest **7.10.3**，用的是新语法。

## 出处

- 定义文档：`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.07.02_Sharing_configuration_file.md`
  （TDC `96971.htm`，3,554 字节）
- 入边 39 篇的来源与原句：`extract/pack/03-sharing-configuration-file.md`
- 所属：**Memory Test Plus**（`02.12`），不是通用 93K 功能
- 本页 `verified: doc-only` —— 只在 TDC 文档里确认存在，未在真实机台上写过这份文件。
