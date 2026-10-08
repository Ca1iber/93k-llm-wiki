---
type: object
title: The model file
layer: file
stage: project
tags: [project, model-file, hardware-configuration, licensing, pogo-pins, device-license]
related: [report-window, device-license-file, testflow-analyzer-tool, technology-file-for-a-device, logical-boards, global-section, pogocabling-section]
sources:
  - 02_System_reference/02.04_Model_File_and_Licensing/02.04.01_The_model_file.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# The model file

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **6,066 字符逐字取自** `<02_System_reference/02.04_Model_File_and_Licensing/02.04.01_The_model_file.md>` 及其子主题 `<02_System_reference/02.04_Model_File_and_Licensing/02.04.01.03.01_Model_file_reference__tester.model.md>`、`<02_System_reference/02.04_Model_File_and_Licensing/02.04.01.03.02_Model_file_reference__model_legacy.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Model file sections › Model file reference  tester.model）

The following is an example of a tester.model file:

```
GLOBAL
   testhead = TH_8CC
   dut_interface = SOC_8GROUP
   hpib_interface = vxi11/e5810a/192.168.0.100/gpib0
   utility_lines = 64, type=static, pogo_size=16
   mux_boards = 8, type=PMUX01, pogoblocks=866,868,870,872,881,883,885,887

CARD_CONFIGURATION
   slot = 301, HW=PS1600, pogoblocks=101-108
   slot = 303, HW=WSMX,   pogoblocks=HS:(231 631) HR:(233 633), type=HD2x32
   slot = 310, HW=DPS128, pogoblocks=HC:(201-208)
   slot = 116, HW=WSRF,   pogoblocks=901-902, source=933

```

The default tester.model provided in /etc/opt/hp93000/soc/ is a template model file for illustration purposes only. For example, the PS5000 card can only be used in EXA Scale™test systems. PS1600 and PS5000 cards cannot be installed simultaneously in an EXA Scale™test system. For details, refer to the dedicated model file sections for each card using the links in the section `Detailed model file information`（raw: `02.04.01_The_model_file.md#_55954__model_file_links`）.

```
# Example for a tester.model file, see detailed syntax description in the TDC

GLOBAL
  testhead = TH_8CC                          # TH_1CC | TH_2CC | TH_4CC | TH_8CC | TH_9Slot | TH_18Slot | TH_27Slot
  dut_interface = SOC_8GROUP                 # SOC_4GROUP | SOC_8GROUP
  hpib_interface = vxi11/e5810a/192.168.0.100/gpib0
#  utility_lines = 64, type=static, pogo_size=16
#  mux_boards = 8, type=PMUX01, pogoblocks=866,868,870,872,881,883,885,887

CARD_CONFIGURATION
  slot = 301, HW = PS1600, pogoblocks = 111-118
  slot = 310, HW = DPS128, pogoblocks = HV:(201-208)

#  slot = 102, HW = PS1600B, pogoblocks = 125-132
#  slot = 310, HW = DPS128,  pogoblocks = HC:(201-208)
#  slot = 303, HW = DPS64,   pogoblocks = HC:(201-204),                         type=REDIRECT, subtype=E8023PF, config=  1:(201 202)   2:(203 204)
#  slot = 304, HW = DPS128,  pogoblocks = HC:(225 657 425 857 229 661 429 861), type=REDIRECT, subtype=E8023PC, config=225:(225 657) 425:(425 857) 229:(229 661) 429:(429 861)
#  slot = 306, HW = DPS64,   pogoblocks = HC:(211 643 212 644),                 type=REDIRECT, subtype=E8023PD, config=211:(211 643) 212:(212 644)

ETC
#  REFERENCECLOCK : input = INTERNAL

DMM
#  1: cardcage=1, type=HP3458A, address=18
#  2: cardcage=2, type=HP3458A, address=19
#  3: cardcage=3, type=HP3458A, address=24
#  4: cardcage=4, type=HP3458A, address=25
#  5: cardcage=5, type=HP3458A, address=26
#  6: cardcage=6, type=HP3458A, address=27
#  7: cardcage=7, type=HP3458A, address=28
#  8: cardcage=8, type=HP3458A, address=29

#End of example model file
```

### Example（取自子主题 Model file sections › Model file reference  model legacy）

The following is an example of a model file:

```
GLOBAL
   testhead = TH_8CC
   dut_interface = SOC
   device_maintenance = OFF
   multiport = ON
   noise_figure = OFF
   memory_stacker = OFF
   multisite = ON
   memorytest = OFF
   timing_bundle = w256-d8-r8
   psrf_pa_library = OFF
   xpressdata = OFF
   S&S_value_package = ON
   protocol_aware = ON

   utility_lines = 256, type = sequencer_controlled, pogo_size = 32

IOCHANNEL

   10101-10816:HW = PS1600, speed =  max-rate,  smem = 224M, diff, tmu, loopback
   10901-11616:HW = PS1600, speed =  max-rate,  smem = 224M, diff, tmu, loopback
   11701-12416:HW = PS1600, speed =  max-rate,  smem = 224M, diff, tmu, loopback
   12501-13216:HW = PS1600, speed =  max-rate,  smem = 224M, diff, tmu, loopback
   20101-20816:HW = PS1600, speed =  max-rate,  smem = 224M, diff, tmu, loopback
   20901-21616:HW = PS1600, speed =  max-rate,  smem = 224M, diff, tmu, loopback
   21701-22416:HW = PS1600, speed =  max-rate,  smem = 224M, diff, tmu, loopback
   40901-41616:HW = PS1600, speed =  max-rate,  smem = 224M, diff, tmu, loopback

DPS

   22501-22516: type = DCS-DPS128HC
   22601-22616: type = DCS-DPS128HC
   22901-22916: type = DCS-DPS128HC
   23001-23016: type = DCS-DPS128HC

   30101-30316: type = DCS-DPS128HC
   30401-30416: type = DCS-DPS128HC
   30501-30716: type = DCS-DPS128HC
   30801-30816: type = DCS-DPS128HC
   30901-32416: type = DCS-DPS128HC

   34101-34816: type = DCS-DPS128HC
   42501-43216: type = DCS-DPS128HC
   45901-46216: type = DCS-DPS128HC

POGOCABLING

   101: pogoblocks = "165,166,167,168,169,170,171,172",type=UTILITY
   102: pogoblocks = "109,110,111,112,113,114,115,116"
   103: pogoblocks = "320,324,303,307,230,226,316,312"
   104: pogoblocks = "217,218,219,220,221,222,223,224"
   105: pogoblocks = "309,310,425,429,301,302,305,306"
   106: pogoblocks = "225,657,229,661", type=REDIRECT,subtype=E8023PD, config="225=225,657;229=229,661"
   107: pogoblocks = "311,313,426,427,428,430,431,432"
   108: pogoblocks = "409,410,411,412,413,414,415,416"
   109: pogoblocks = "209,210,211,212,213,214,215,216"

   201: pogoblocks = "304,736,308,740", type=REDIRECT,subtype=E8023PD, config="304=304,736;308=308,740"
   202: pogoblocks = "459,460,341,342", type=REDIRECT,subtype=E8023PF, config="5=459, 460;1=341, 342"
   203: pogoblocks = "461,462,343,344", type=REDIRECT,subtype=E8023PF, config="6=461, 462;2=343, 344"
   204: pogoblocks = "125,126,127,128,129,130,131,132"
   205: pogoblocks = "117,118,119,120,121,122,123,124"
   206: pogoblocks = "101,102,103,104,105,106,107,108"
   207: pogoblocks = "201,202,203,204,205,206,207,208"
   208: pogoblocks = "314,315,317,318,319,321,322,323"
   209: pogoblocks = "345,346,347,348", type=REDIRECT,subtype=E8023PF, config="3=345, 346;8=347, 348"

#   110: pogoblocks = "304,736,308,740", type=REDIRECT,subtype=E8023PD, config="304=304,736;308=308,740"
#   111: pogoblocks = "459,460,341,342", type=REDIRECT,subtype=E8023PF, config="5=459, 460;1=341, 342"
#   112: pogoblocks = "461,462,343,344", type=REDIRECT,subtype=E8023PF, config="6=461, 462;2=343, 344"
#   113: pogoblocks = "125,126,127,128,129,130,131,132"
#   114: pogoblocks = "117,118,119,120,121,122,123,124"
#   115: pogoblocks = "101,102,103,104,105,106,107,108"
#   116: pogoblocks = "201,202,203,204,205,206,207,208"
#   117: pogoblocks = "314,315,317,318,319,321,322,323"
#   118: pogoblocks = "345,346,347,348", type=REDIRECT,subtype=E8023PF, config="3=345, 346;8=347, 348"

```

<!-- 语法节 end -->

## 是什么

**model file 是「这台测试系统的硬件清单」。** 原文第一段一口气说完了它的职责：

> The model file contains the tester hardware configuration. It specifies what test head cards are installed, their features, and the mapping of these cards to pogo pins on the DUT board interface. It also specifies the reference clock signal for the test system. SmarTest needs this information in order to set the configuration and features of the test system resources for your addressed tests.

拆成四项：

| # | 文件里写什么 | 原文片段 |
|---|---|---|
| 1 | **装了哪些 test head 卡** | `what test head cards are installed` |
| 2 | **这些卡有什么特性** | `their features` |
| 3 | **卡到 DUT 板接口 pogo pin 的映射** | `the mapping of these cards to pogo pins on the DUT board interface` |
| 4 | **测试系统的参考时钟信号** | `It also specifies the reference clock signal for the test system.` |

**为什么非有它不可**（同段末句）：

> SmarTest needs this information in order to set the configuration and features of the test system resources for your addressed tests.

**即：SmarTest 靠它把「你要用的资源」配成正确的形态。文件不对，资源就不对。**

### 文件在哪、叫什么名字

| 项 | 值 | 依据 |
|---|---|---|
| **默认位置** | `/etc/opt/hp93000/soc/model` | 原文 |
| 另一种部署 | `/etc/opt/hp93000/soc/model` 可以是**指向** `/etc/opt/hp93000/soc_common/model` 的链接 | 原文 |
| **文件名** | `model` 或 `tester.model`，**取决于用哪种语法** | 原文 |
| **换名字的办法** | 设环境变量 `V93000_MODEL` | 原文 |

逐字：

> The default location of the model file is: /etc/opt/hp93000/soc/model

> Alternatively, /etc/opt/hp93000/soc/model can be a link to: /etc/opt/hp93000/soc_common/model

> The file name for the model file is: model or tester.model depending on the syntax, see 353017Model file sections.

> If you want to use a different file name, set the environment variable `V93000_MODEL` and specify the actual file name that you want to apply, for example, model.offline.

**「文件名取决于语法」这句要留意**：`model` 与 `tester.model` **不是同一套语法的两个叫法**——
原文写的是 `depending on the syntax`，**即两代语法各用一个文件名**。

> **哪一代用哪个名字，本篇没有正面写。** 本页的推断链是：
> ① 上面「语法 / 参数」节里有两个逐字例子，段名分别写着 `tester.model` 与 `model legacy`
> （**来源写在段名里，是页面的一部分**）；② 原文的 `#### Subtopics` 里有一条
> `Converting legacy model files`。→ **`tester.model` 配新语法，`model` 配 legacy 语法。**
> **这是推断，原文没有把这两个名字和两代语法一一对应过。** 要坐实得读 `Model file sections`（本页没读）。

### 在线 / 离线，report window 里显示的东西不同

> When SmarTest is started up in online mode, it reads the model file and reports the detected test system hardware in the report window in the MAXIMUM POSSIBLE CONFIGURATION table. In offline mode it shows the requested configuration defined by the model file. It also lists the referenced model file or a link pointing to it:

| 启动模式 | report window 里显示什么 |
|---|---|
| **online** | **探测到的**测试系统硬件，表是 `MAXIMUM POSSIBLE CONFIGURATION` |
| **offline** | **model file 请求的**配置 |

**两种模式读的是同一个文件**（原文紧跟着的一句）：

> Whether starting SmarTest online or offline, the same model file is used - the file located at or linked from the default location or the model file specified by the environment variable `V93000_MODEL`, if set.

**「或它链到的那个」这句话把上面那条「可以是个链接」接上了**——链接的目标也算同一个文件。
**（`report window` 那边还有一条：`In offline mode it shows the requested configuration defined by the model file.` 以及
`It also lists the referenced model file or a link pointing to it`——即窗口里能直接看到用的是哪份文件。
这条关系在两个页面上都有，见 [[report-window]]。）**

### 它还管许可证（`## Requests the licenses`）

> For those test system resources and features that require licenses, SmarTest first generates the license requests based on the model file, then reads the *.lic license files to check out the requested licenses from the license server.

**顺序是三步**：**先按 model file 生成许可请求 → 再读 `*.lic` → 再向 license server 去 check out。**
**所以 model file 写多了，许可证就会多要。**

**多要的后果，原文用一个模板讲清了**：

> A model file template at /var/opt/hp93000/soc_<version>/model_template, which is generated at every online start up, shows the maximum possible configuration. A model file or device license file based on this template will request and block all licenses which possibly might be used.

**`request and block`——要了就会占住。**
**照这份模板抄一份 model file（或 device license file）= 把「可能用到」的许可证全占了。**
这是一条实打实的运维后果，**不是配置风格问题**。

> An example model file at /opt/hp93000/soc_<version>/pws/data/model.def illustrates proper model file syntax.

**注意这两个路径不是同一层**：模板在 `/var/opt/hp93000/soc_<version>/`，
例子在 `/opt/hp93000/soc_<version>/pws/data/`。

### 和 device license file 的关系（原文一整段 `Note`）

**这一段是本页最要紧的一块**，逐字：

> Note In addition to the model file you may use one or more device license files for licensing-per-device. The concept of licensing-per-device is based on a licensing file for each device, the device license file. This concept allows you to better utilize your licenses by requesting only those licenses from the license server that are really required for a device.

> Licensing-per-device does not break the model file concept and mechanisms. It is rather an add-on and enhancement of that concept. Therefore the device license file must contain only license relevant entries. To ensure compatibility the device license file uses the same syntax as the model file.

> Important: If a device license file exists, its parameters will be evaluated and any licensing parameters in the model file will be ignored. To develop a device license file we recommend to use the Testflow Analyzer Tool (TAT).

| 问题 | 答案（文档事实） |
|---|---|
| 两者什么关系 | **device license file 是 model file 概念的加装与增强**（`It is rather an add-on and enhancement of that concept.`），**不破坏原机制** |
| 它解决什么 | **按 device 精确申请**：`requesting only those licenses from the license server that are really required for a device` |
| 写法 | **同一套语法**（`the device license file uses the same syntax as the model file`） |
| 里面能写什么 | **只能写与许可证有关的条目**（`must contain only license relevant entries`） |
| **同时存在时谁说了算** | **device license file 优先**：它的参数会被求值，**model file 里的许可参数被忽略** |

**最后一行是整段里最容易读漏的一句**：`any licensing parameters in the model file will be ignored.`
**不是「合并」，是「忽略」。** 两处都改了参数、却只改在 model file 里，**是不生效的**。

**做 device license file 的推荐工具**也是原文给的：`we recommend to use the Testflow Analyzer Tool (TAT)`
（`Recommendation` 语气，**是建议不是要求**）。→ [[testflow-analyzer-tool]]

### 「Detailed model file information」段：按卡给细节

原文用一张表把「哪张卡的 model file 细节在哪」列出来。**卡名照抄**：

`DPS64` / `DPS128` / `XPS256` / `Ext. GBIP DPS` / `PS1600` / `PS5000` / `SE-UDPS` / `UHC4T`

**这张表在语料里是坏的**（断行、行跑到表格外，见「出处」）——**本页只抄卡名，不抄表结构**。
**表里每一格指向的细节文档本页一篇都没读**，所以**各张卡在 model file 里到底怎么写，本页一个字都没有**。

## 典型用法

**本文档没有 `## Procedure` 段，也没有 `## Before you begin` 段。**
它讲的是「这个文件是什么、怎么被读到」，**不是「怎么建一个」**——
建 / 改的那件事在子主题 `Editing the model file`（`02.04.01.01`）里，**本页没读**。

**按本文档能确定的三条：**

1. **放 / 换一份 model file** —— 放到默认位置 `/etc/opt/hp93000/soc/model`
   （或让这个路径指向 `/etc/opt/hp93000/soc_common/model`），
   **或者另起一个文件名并用环境变量 `V93000_MODEL` 指过去**（文档给的例子是 `model.offline`）。
2. **确认它被读到了** —— 启动后看 **report window**：
   online 模式看 `MAXIMUM POSSIBLE CONFIGURATION` 表，
   并且它会 `lists the referenced model file or a link pointing to it`。
   **这是文档给出的唯一一条「验证读到没有」的路径。**
3. **只在需要按 device 省许可证时**才另做 device license file；
   **一旦它存在，model file 里的许可参数就被忽略**——
   **所以「两份都改」是错的做法**（文档事实：`will be ignored`）。

**动手前要先想清楚的一件事**（机制是文档给的，结论是本页的）：

> `A model file or device license file based on this template will request and block all licenses which possibly might be used.`

**照 `model_template` 抄一份，会把「可能用到」的许可证全占住。**
（推断：想少占许可证，方向是**按实际用到的东西裁**，或**用 device license file 按 device 精确申请**——
后者的目的原文写了：`requesting only those licenses from the license server that are really required for a device`。
**文档没有直接写「照模板抄是错的」，它只写了后果。**）

## 和谁有关

- [[report-window]] — **最紧的一条**。model file 被读的结果**显示在 report window 里**
  （online 看 `MAXIMUM POSSIBLE CONFIGURATION`，offline 看请求的配置），
  而且窗口**会列出被引用的那份 model file 或其链接**。这是「文件改了没有、读的是哪份」的唯一窗口。
- [[device-license-file]] — **本页整段 `Note` 的对象**。同一套语法、`add-on` 关系、
  **存在时覆盖 model file 的许可参数**。本页只写了这一层；**那个文件自己怎么写，本页没读**。
- [[testflow-analyzer-tool]] — **原文点名的工具**（做 device license file 的推荐做法）。
  文档用的是 `we recommend to`，**是建议**。
- [[technology-file-for-a-device]] — `## Related information` 段里的一条。
  **本页的文档没有说明它和 model file 是什么关系**，只是并列放在一起。
- [[logical-boards]] — **本页的一个子主题**（`Concepts of logical boards`）。
  **本页没读**；「逻辑通道板」那套概念是理解 model file 里通道编号（乃至 `DFPN` 的
  五位通道号）的前提，**但那部分不在本页**。
- [[global-section]] / [[pogocabling-section]] — **model file 的「节」各有专页**。
  **语法节里那两个逐字例子里出现的节名**（`GLOBAL` / `CARD_CONFIGURATION` / `ETC` / `DMM`
  与 `GLOBAL` / `IOCHANNEL` / `DPS` / `POGOCABLING`）**就是从这些节拼起来的**。
  **本页的文档只把它们统称为 `Model file sections`，没有逐节讲**——那篇本页没读。
- `Switching model files`（`02.04.01.01.02`，未建页）— 原文 `Further information` 的第一条；
  **本页没读**。
- `SmarTest environment variables`（`01.02.02.02.04`，未建页）— 原文 `Further information` 的第二条；
  **`V93000_MODEL` 的完整说明在那里，本页只有这一句**。
- `The System .lic license files`（未建页）— `## Related information` 第一条；
  **本页只知道 SmarTest 会去读 `*.lic`，读的规则不在本页**。

## 版本

本文档有 `## Functional changes` 段，**三条，逐条转录**：

- `Introduced before SmarTest 6.3.2`
- `SmarTest 6.5.4: Report window lists the referenced model file.`
- `SmarTest 7.5.3: Model file usage introduction updated.`

**两条要留意：**

- **第一条是哨兵值**（§11.2 ②）：`Introduced before SmarTest 6.3.2` 的意思是
  「**在本文档集覆盖范围开始之前就已经有了**」，**不是「SmarTest 6.3.2 新增了 model file」**。
- **`SmarTest 6.5.4` 那一条讲的是 report window 的行为**——
  它记在**本页**的版本段里，而 [[report-window]] 的版本段里**没有这一条**。
  **同一个功能变更只登记在一侧。**（两篇的 `## Functional changes` 不是同一批条目，
  本页照实记这一点，**不把它当成本页自己的功能变更**，也不搬去改别的页。）

## 出处

`sources:` 一篇：
`02_System_reference/02.04_Model_File_and_Licensing/02.04.01_The_model_file.md`

**本页没做的：**

- **四个子主题一篇都没读**（`#### Subtopics` 里的四条）：
  `Editing the model file`（`02.04.01.01`）、`Concepts of logical boards`（`02.04.01.02`）、
  `Model file sections`（`02.04.01.03`）、`Converting legacy model files`（`02.04.01.04`）。
  **⚠️ 其中 `Model file sections` 那棵子树尤其要紧**：本页「语法 / 参数」节里的两个逐字例子
  （`tester.model` 与 legacy `model`）**就是从它的子主题（`02.04.01.03.01` / `02.04.01.03.02`）抄的**，
  **本页没有读过那两篇**。所以：
  **model file 有哪几节、每节的语法、`model` 与 `tester.model` 的语法差异，本页一个字都没有。**
- **「Detailed model file information」表里指向的八篇卡细节文档一篇都没读。**
  所以**每张卡在 model file 里怎么写，本页一个字都没有**——本页只抄了卡名。
- **`## Related information` 段的四篇一篇都没读**：
  `The System .lic license files`、`The device license file`、
  `The Testflow Analyzer Tool (TAT)`、`Technology file for a device`。
- **`Further information` 的两篇没读**：`Switching model files`、`SmarTest environment variables`。
- **一张图没看**（`raw/253778.png`，就是 `![Model file (1)]` 那一张）。
  **所以那个「列出被引用 model file」的界面长什么样，本页不知道。**
- **`V93000_MODEL` 的完整语义（默认值、优先级、相对路径怎么算）：语料未写**——
  本篇只有 `If you want to use a different file name, set the environment variable V93000_MODEL and specify the actual file name that you want to apply, for example, model.offline.` 这一句。
- **`model` 与 `tester.model` 各对应哪一代语法：本篇没有正面写**（本页给了推断链并标注为推断）。

> ⚠️ **语料瑕疵，照实记下，一处都没替它改**：
> ① **主题号和链接文字粘在了一起。** 原文那一句是
> `see 353017[Model file sections](<02.04.01.03_Model_file_sections.md>)`——
> **`353017` 与链接文字之间没有空格**（那个数字是本页的 TDC topic id，`source_topic: "55954.htm"` 是同族）。
> 本页引这句时按 §11.1 剥掉链接标记，引文写成 `see 353017Model file sections.`——
> **`353017Model` 这个粘连是原文的**，不是本页排版失误。
> ② **`## Detailed model file information` 那张表在语料里是坏的。** 原文里
> `PS1600` **单独占一行**（那行只有一个孤立的 ` |` 在它前面），而属于它的表格行在**下一行**：
> ` | [PS1600 card configuration in the model file](<../02.05_Test_Head_Cards/02.05.04.01.07.02_PS1600_card_configuration_in_the_model_file.md>)`；
> `| UHC4T |` 那一行的内容同样**跑到表格外另起一行**——
> `[UHC4T configuration in the model file](<../02.05_Test_Head_Cards/02.05.05.02.05_UHC4T_specific_setup_tasks.md#_105188__s_UHC4T_in_the_model_file>)`，
> 后面跟一个孤立的 ` |`。
> **本页因此只抄卡名，不重排这张表**（重排就是替语料补结构）。
> ③ **`Ext. GBIP DPS` 里的 `GBIP` 应为 `GPIB`。** 同一格的链接目标文件名写的是
> `02.05.06_External_device_power_supply__external_GPIB_DPS.md`——**目标里拼的是 `GPIB`**。
> **本页在「Detailed model file information」那一节照原样抄的是 `Ext. GBIP DPS`。**
> ④ **`licensing-per-device` 的首字母大小写在同一段里不一致**：
> 先写 `The concept of licensing-per-device is based on a licensing file for each device, the device license file.`（**小写 `l`**），
> 紧接着 `Licensing-per-device does not break the model file concept and mechanisms.`（**大写 `L`**）。
> **两种写法都在原文里**，本页不统一。
> ⑤ **`Note` 与它后面的句子粘在一起**：原文是
> `Note In addition to the model file you may use one or more device license files for licensing-per-device.`——
> **`Note` 后面没有冒号、也没有换行**。上面那段引文**照原样抄的就是这个样子**。

`verified: doc-only`——**本页没有在任何真实 93K 上打开过 model file**
（§11：文档里有 ≠ 这台机器上是这样；**尤其第 ①③④ 条里的路径与卡名，动手前照实机核对**）。
