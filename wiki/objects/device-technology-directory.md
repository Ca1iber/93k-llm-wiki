---
type: object
title: Device Technology Directory
layer: file
stage: project
tags: [device-technology-directory, dev-tech, cmos, ecl, template, defaults, subdirectory-list, project-setup, smartest-6.3.2, smartest-7.0.3]
related: [device-directory, technology-file-for-a-device, new-device-wizard, change-device-wizard, project, pin-configuration-file, level-file, timing-file, testflow-file, device-license-file, error-map, pattern-explorer, shmoo-tool, data-logging-profiles, smartest-6.3.2, smartest-7.0.3]
sources:
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.01.01_Device_Technology_Directory.md
created: 2026-09-21
updated: 2026-09-21
verified: doc-only
---

# Device Technology Directory

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,711 字符逐字取自** `<01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.01.01_Device_Technology_Directory.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Tables（脚本逐字抽取，第 1 张）

| Subdirectory | Contains |
|---|---|
| .project | Configuration of the device project |
| .settings/vectors | Layout data for the Pattern Debug Tool and Pattern Explorer |
| .technology | See `Technology file for a device`（raw: `01.01.07.02.01.02_Technology_file_for_a_device.md`） for details. |
| analog_control | Analog setup file |
| applicat | Application data for production mode |
| calibration | Calibration data. For the ACTCatr file, see `ACTCatr`（raw: `../../02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.04.01.01_ACTCatr.md`）. |
| ch_attributes | See `Channel attributes files`（raw: `../../02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.04.01_Channel_attributes_files.md`） for details. |
| configuration | Pin file |
| data_set | (Reserved) |
| di_report | (Reserved) |
| error_map | Exported error maps in ASCII format |
| format | Pin display information for GUI tools |
| levels | Level file |
| license | License file |
| lock_file | Lock file for the device |
| pin_attributes | Edge delays for each pin, used for calibration |
| profiles | Date logging configuration |
| report | Log file |
| routing | Analog and relay routing information |
| scan_res | (Reserved) |
| shmoo | Shmoo setup and result files |
| testflow | Testflow file |
| testfunc | Customer-defined connect and disconnect sequences |
| testmethod | Test method file |
| testprog | Test program file |
| testtable | Test table file |
| timing | Timing file |
| timing_dgrm | (Reserved |
| vectors | Vector file |
| vectors/.cache | Cached pattern file dependencies |
| wafertyp | Wafer description file |
| waste | Default temporary directory |
| waveform | Waveform file |
| waveform/.result | Result waveform file |

<!-- 语法节 end -->

## 是什么

**device technology directory 是「一份现成的 device 目录样板」：
在 `/opt/hp93000/soc/dev_tech` 下按工艺分两份——`cmos` 与 `ecl`——
它们提供新建 device 时用的那一套默认值。**
原文第一句（逐字）：

> 「This topic lists the path and subdirectories of a device directory for cmos and ecl.」

**⚠️ 这句话里写的是 `a device directory`（一个 device 目录）——**
**所以它讲的是「device 目录」的一种，而不是另一种叫「technology directory」的东西。**
**本页与 [[device-directory]] 的分工是**：
**`device-directory` 讲把一个 device 目录**拆开看**是什么结构**（各类子目录、各装什么）；
**本页讲的是 `/dev_tech` 下那两份**样板**（`cmos` / `ecl`）——**
**原文的题目正是「这份样板里有什么」，而且它多给了一条 `device-directory` 不会讲的事：
这些目录里装的是**默认值**。**
**两页不是同一页，也没有把两篇合成一页**（**本页没有读 [[device-directory]] 那一页**）。

### 路径：只有一个，而且是「两条目共用的父路径」

原文 `Path of the default device technology directories cmos and ecl:` 后面是**一条** bullet（逐字）：

- `/opt/hp93000/soc/dev_tech`

**⚠️ 原文只给了这一条路径，而句子说的是「cmos 和 ecl 两个目录的路径」。**
**两个目录各自的完整路径（例如是否写作 `/opt/hp93000/soc/dev_tech/cmos`）原文没有写出来**——
**（推断）`cmos` 与 `ecl` 是这条路径下的两个子目录**，
**依据是那句标题把两者并列、而路径只有一条，且 `dev_tech` 这个目录名本身是复数概念；
原文没有把拼法写出来，所以这是推断。**

### 目录里有什么：原文是一张两列的表，本页照抄成表

原文（逐字）引出这张表的句子：

> 「Subdirectories and files in the device technology directory」

**下表 34 行**（**原文是一张两列的表，表头是 `Subdirectory` / `Contains`；
本页把每一格照原样搬进表里，一处都没有改写**。
**⚠️ 其中三处格子里原文自己带着链接、两处括号不完整，见 `## 出处`**）：

| Subdirectory | Contains（**原文逐字**） |
|---|---|
| `.project` | Configuration of the device project |
| `.settings/vectors` | Layout data for the Pattern Debug Tool and Pattern Explorer |
| `.technology` | See Technology file for a device for details. |
| `analog_control` | Analog setup file |
| `applicat` | Application data for production mode |
| `calibration` | Calibration data. For the ACTCatr file, see ACTCatr. |
| `ch_attributes` | See Channel attributes files for details. |
| `configuration` | Pin file |
| `data_set` | (Reserved) |
| `di_report` | (Reserved) |
| `error_map` | Exported error maps in ASCII format |
| `format` | Pin display information for GUI tools |
| `levels` | Level file |
| `license` | License file |
| `lock_file` | Lock file for the device |
| `pin_attributes` | Edge delays for each pin, used for calibration |
| `profiles` | Date logging configuration |
| `report` | Log file |
| `routing` | Analog and relay routing information |
| `scan_res` | (Reserved) |
| `shmoo` | Shmoo setup and result files |
| `testflow` | Testflow file |
| `testfunc` | Customer-defined connect and disconnect sequences |
| `testmethod` | Test method file |
| `testprog` | Test program file |
| `testtable` | Test table file |
| `timing` | Timing file |
| `timing_dgrm` | (Reserved |
| `vectors` | Vector file |
| `vectors/.cache` | Cached pattern file dependencies |
| `wafertyp` | Wafer description file |
| `waste` | Default temporary directory |
| `waveform` | Waveform file |
| `waveform/.result` | Result waveform file |

**从这张表能定的四件事**（**都是表里逐字可见的，不是本页推的**）：

| # | 事实 | 依据（表里那一格） |
|---|---|---|
| 1 | **有四格写 `(Reserved)`**：`data_set` / `di_report` / `scan_res` / `timing_dgrm` | 那四格的 `Contains` |
| 2 | **有两个 `.` 开头的隐藏目录**：`.project` / `.settings/vectors` / `.technology`（**三个**） | 名字本身 |
| 3 | **有两格是「子目录的子目录」**：`vectors/.cache` / `waveform/.result` | 名字里的 `/` |
| 4 | **有两格带「for details」式的指引**：`.technology` 与 `ch_attributes` | 那两格的正文 |

**⚠️ 第 3 件要注意**：**表里共 34 行（本页逐行数过），而 `vectors/.cache` 与
`waveform/.result` 是 `vectors` / `waveform` 的下级**——
**原文没有说这两行是「另开一行」而不是「目录本身」，也没有给缩进或层级标记**；
**本页照原样列成同级行，不替它改层级。**

### 这些目录里装的是「默认值」——这是本页的核心

**原文最后三段（共四句）逐字，说的是这套目录干什么用**：

> 「Some of these directories are generated only when particular tools or options are used, not by default. Additional directories may be present that were created by third-party tools such as version control software.」
> 「Within each of the sub-directories are files (containing firmware commands) which specify the default values.」
> 「Every time you create a new setup file, the defaults are used and, of course, can be changed.」

**三句各管一件事**：

| 句 | 原文 | 说的是 |
|---|---|---|
| 1a | `Some of these directories are generated only when particular tools or options are used, not by default.` | **表里的目录不是全部**——有些只有用了特定工具/选项才生成 |
| 1b | `Additional directories may be present that were created by third-party tools such as version control software.` | **还可能有第三方的目录**（原文举的例子是版本控制软件） |
| 2 | `Within each of the sub-directories are files (containing firmware commands) which specify the default values.` | **每个子目录里的文件装的是固件命令，而这些命令给出的是默认值** |
| 3 | `Every time you create a new setup file, the defaults are used and, of course, can be changed.` | **每次新建 setup file 都用这些默认值；当然可以改** |

**第 2、3 句合起来是本页最有用的一句结论**：
**这套目录是「默认值的来源」，而默认值的形式是**固件命令**——
**即：`cmos` / `ecl` 下的文件是可直接读、可照抄的固件命令文本，不是黑箱的二进制配置。**
**（推断）——依据是原文那句 `files (containing firmware commands)` 的括号注解：
装的是固件命令，说明它是文本、是命令；原文没有一句话说它「可照抄」，所以这是推断。**
（**`containing firmware commands` 是原文的括号注解，本页照引**；
**至于那些命令**具体是哪几条**，本篇一条都没有列**——见 `## 出处`。）

**⚠️ 第 3 句里的 `a new setup file` 与第 1a 句的 `by default` 要一起读**：
**原文没有说「新建 device」这个词**，它说的是 `create a new setup file`——
**（推断）新建 device/工程时会用到这套默认值，
依据是「默认值」这个用途本身 + `dev_tech` 这个目录名；
原文没有一句话把「建 device」和这套目录连起来。**
**建 device 的入口页见 [[new-device-wizard]] / [[change-device-wizard]]（本页都没读）。**

### 表里每一格对应到本 wiki 的哪一页（**只是指路，不是原文的话**）

**下表是本页的索引，不是原文的内容**——**每一行的依据都是「那一格的 `Contains` 词组
与那一页的名字对得上」**（**（推断），本页没有读那些页**）：

| 目录 | 那一格指向的东西 | 本 wiki 里的去处 |
|---|---|---|
| `.technology` | `Technology file for a device`（**原文自己链的**） | [[technology-file-for-a-device]] |
| `configuration` | `Pin file` | [[pin-configuration-file]]（**（推断）：名字相近，本页没读**） |
| `levels` | `Level file` | [[level-file]]（**（推断）同上**） |
| `timing` | `Timing file` | [[timing-file]]（**（推断）同上**） |
| `testflow` | `Testflow file` | [[testflow-file]]（**（推断）同上**） |
| `vectors` | `Vector file` | [[vector-setup-file]]（**（推断）：名字不同，本页没读**） |
| `license` | `License file` | [[device-license-file]]（**（推断）同上**） |
| `error_map` | `Exported error maps in ASCII format` | [[error-map]]（**（推断）：原文没有链任何页**） |
| `.settings/vectors` | `Layout data for the Pattern Debug Tool and Pattern Explorer` | [[pattern-explorer]]（**（推断）：原文只给了名字**） |
| `shmoo` | `Shmoo setup and result files` | [[shmoo-tool]]（**（推断）同上**） |
| `profiles` | `Date logging configuration`（**原文写的是 `Date`**） | [[data-logging-profiles]]（**（推断）同上**） |
| `.project` | `Configuration of the device project` | [[project]]（**（推断）：那是 stage 页，不是这一格的文件页**） |

**⚠️ `waveform` 那一格本页不指任何页**：原文写的是 `Waveform file`，
**而本 wiki 里名字最近的是 `wavetable-file`——（推断）两者是不是同一个东西，
本页没有依据**（**本页没读那一页**）。**宁可写不出来，也不指一个可能是错的页。**

## 典型用法

**原文没有 `## Procedure`、没有 `## Before you begin`、没有 `## Example`**——
**它是一篇「列目录 + 一句用途」的参考页**。
**所以「怎么用」在本页只能给到下面这个粒度**（**每一条的依据都是逐字的**）：

| # | 你要做什么 | 依据（**原文**） |
|---|---|---|
| 1 | **想知道建出来的 device 目录默认长什么样** | **看上面那张表**——原文：`Subdirectories and files in the device technology directory` |
| 2 | **想知道某个默认值从哪来** | 去 `/opt/hp93000/soc/dev_tech/<cmos 或 ecl>/<子目录>` 里看文件；原文：`Within each of the sub-directories are files (containing firmware commands) which specify the default values.` |
| 3 | **想改默认值** | **改完之后新建的 setup file 就不会用老默认了**——原文只说 `can be changed`，**没有说改哪里、改完对已有 device 有没有影响** |
| 4 | **发现实际目录比表里多** | **正常**——原文：`Some of these directories are generated only when particular tools or options are used, not by default.` / `Additional directories may be present that were created by third-party tools such as version control software.` |
| 5 | **找不到某个目录** | **先看 `## 版本`**——**7.0.3 删掉了四个目录**（`bitmap` / `bitmap_conf` / `mem_llapg` / `scrambling`） |

**这张表能做的两件核对**（**本页做的比对，不是原文的话**）：

| 核对 | 结果 |
|---|---|
| **7.0.3 删掉的那四个目录，表里还在不在？** | **不在**——表里没有 `bitmap` / `bitmap_conf` / `mem_llapg` / `scrambling`。**版本条目与表是一致的**（**这是本页核的，原文没有说这两处要对上**）。 |
| **表里哪几格是空的？** | **四个 `(Reserved)`**（`data_set` / `di_report` / `scan_res` / `timing_dgrm`）——**原文没有解释 `Reserved` 是什么意思**（是留给用户、还是留给以后版本），**本页不替它解释。** |

**没有的东西**：本篇**没有 `Errors` / `Warnings` / `Limits` 段，
也没有 `## Application` 段**；**也没有 `Syntax` / `Parameters` / `Example` 段标记**
（这一点语法节里已经说明——**脚本在没有任何段标记时一个字都不收录，理由写在那里**）。

## 和谁有关

- [[device-directory]] — **最容易混的一页，本页把它顶在最前面说清**：
  **`device-directory` 讲的是「device 目录这个结构本身」（各类子目录怎么分、各装什么），
  本页讲的是 `/dev_tech` 下那两份**样板**（`cmos` / `ecl`）以及「它们装的是默认值」。**
  **两篇是两篇文档，本页没有把它们写成一页。**
  **本页没读 [[device-directory]]**——**所以「本页这张表与那一页的结构表重不重叠」，本页答不了。**
- [[technology-file-for-a-device]] — **表里唯一被原文自己链过去的那一格**。
  `.technology` 那一格逐字是
  `See Technology file for a device for details.`——**原文把 `.technology` 的细节全推给它**。
  **本页只有这一行，没有 `.technology` 里任何一个参数。**
- [[new-device-wizard]] / [[change-device-wizard]] — **（推断）用到这套默认值的入口**。
  原文只说 `Every time you create a new setup file, the defaults are used`，
  **没有提任何向导**；**依据只是「建新 device/setup」这件事该有入口，而这两页的名字对得上。
  本页没读那两页。**
- [[project]] — **`.project` 那一格的去处（（推断））**。
  原文那格写 `Configuration of the device project`；
  **而 [[project]] 是 stage 页**，**不是这个 `.project` 文件的文件页**——
  **本页把这一点写明，免得下一个人拿 stage 页来当文件页用。**
- [[pin-configuration-file]] / [[level-file]] / [[timing-file]] / [[testflow-file]] /
  [[vector-setup-file]] / [[device-license-file]] / [[error-map]] — **（推断）表里几格的去处**，
  依据是「那一格的 `Contains` 词组与那一页的名字对得上」（**每一条本页都在上一节的表里标了**）。
  **本页没读它们中的任何一页**，**所以「样板里那个文件与该页讲的是不是同一种文件」，
  本页一条都没有核过。**
- [[pattern-explorer]] / [[shmoo-tool]] / [[data-logging-profiles]] — **（推断）同上**，
  分别对应 `.settings/vectors` / `shmoo` / `profiles` 三格。
  **⚠️ `profiles` 那一格原文写的是 `Date logging configuration`（`Date`），
  本页照原样引，并把它当 `data logging` 去指路——这一步是推断。**
- [[smartest-6.3.2]] / [[smartest-7.0.3]] — **版本页**，本页 `## 版本` 两条条目的落点。
- `Technology file for a device`（**原文链接文字**）、`ACTCatr`、
  `Channel attributes files`、`Application Data`（**原文 `## Related information` 唯一一条**）——
  **四个都是原文里的链接目标**；其中 `ACTCatr` 与 `Channel attributes files` 的 raw 路径分别是
  `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.04.01.01_ACTCatr.md` 与
  `…/02.08.04.04.01_Channel_attributes_files.md`，`Application Data` 是
  `…/02.08.04.01_Application_Data.md`。**这三个本页都没读**
  （`ACTCatr` / `Channel attributes files` / `Application Data` 都不在本 wiki 的链接清单里，
  **所以只写名字与路径，不写链接**）。
- `cmos` / `ecl`（**两个目录名**）— **原文只把它们当作两个并列的样板名**，
  **没有解释这两种工艺是什么、选哪个的判据是什么。本页照原样写，不补。**

## 版本

本文档**有** `## Functional changes` 段，**两条**（**逐字**）：

- **Introduced before SmarTest 6.3.2**
- **SmarTest 7.0.3: Removed bitmap, bitmap_conf, mem_llapg, and scrambling directories**

**第一条是 §11.2 ② 那个哨兵。** `Introduced before SmarTest 6.3.2` 的意思是
**「早于语料覆盖范围」**，**不是「6.3.2 新增」**——
**所以这套目录成立于哪个版本，这份语料里没有。** **版本页见 [[smartest-6.3.2]]。**

**第二条是常规条目**（**版本页见 [[smartest-7.0.3]]**），**它给出四个目录名**：
`bitmap` / `bitmap_conf` / `mem_llapg` / `scrambling`——**这四个在 7.0.3 被删掉了。**
**这是本页唯一一条「某个目录为什么不在表里」的依据**：
**表里确实没有这四个**（**本页核过，见 `## 典型用法`**）。
**⚠️ 但原文没有说「表是哪一版的表」**——**所以「表会不会本来就跟着版本变」，
本页答不了**（见 `## 出处`）。

**与 wiki 面向版本的关系**：本 wiki 面向 **SmarTest 7.10.3**，
**7.0.3 早于 7.10.3**，所以**按文档的说法这四个目录在目标版本上已经不在**。
**注意 §11**：这只说明**文档这么写**，**不说明某台机台的 `/opt/hp93000/soc/dev_tech` 下
真没有这四个目录**（本页 `verified: doc-only`，**没有连过任何机台**）。

## 出处

`sources:` 一篇：
`01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.01.01_Device_Technology_Directory.md`

**本页没做的：**

- **只读了这一篇。** 原文里的五个链接目标**一个都没读**：
  `Technology file for a device`（[[technology-file-for-a-device]]）、
  `ACTCatr`、`Channel attributes files`、`Application Data`（`## Related information` 唯一一条），
  以及那些目录名指向的页（**本页只是指路，见 `## 是什么` 最后一张表**）。
  **所以「样板里每个文件到底装什么、格式是什么」，本页一个字都没有。**
- **[[device-directory]] 没读**——**这是本页最大的空缺**：
  **两页的表重不重叠、`dev_tech` 下的样板与建出来的 device 目录差在哪，本页答不了。**
  本页只能给出「原文自己那三句用途句」（默认值 / 可改 / 第三方目录）。
- **那些「固件命令」一条都没列**：原文只说 `files (containing firmware commands)
  which specify the default values`，**没有给任何一条命令**；
  **所以「默认设备周期是多少、默认 level 怎么设」这类问题，本页一个字都答不出。**
- **没有连过任何机台、也没有看过真实的 `/opt/hp93000/soc/dev_tech`**——
  **本页全部内容都是文档事实**（`verified: doc-only`）。
  **「表里这 34 行是不是目标版本的全部」这件事，只有上机台 `ls` 一遍才知道。**
- **没有查过 `cmos` 与 `ecl` 怎么选**：原文只把两个名字并列，**没有任何一句话讲判据**。
- **没有查过 `(Reserved)` 的含义**（四格）、**也没有查过 `wafertyp` / `applicat` /
  `timing_dgrm` 这三个看着像截断的名字是不是截断**——**原文没有给全称，
  本页不替它猜**（§11.2 ⑤ 的判据是「标识符里出现不可能的东西」，
  **而这三个名字本身语法正常，只是看着短，所以本页不下结论**）。
- **一张图都没看。** 本篇**没有图片引用**（`![` 0 处，本页核过）。
- **没有交叉验证任何别处的文档**（§11：本页只写这一篇里有的）。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> **① 一处 `(Reserved` 少了右括号。** 逐字（`timing_dgrm` 那一格）：
> `(Reserved` ——**同一张表里另外三格写的是 `(Reserved)`（带右括号）**，
> **只有 `timing_dgrm` 这一格是半截的。本页在表里照原样抄 `(Reserved`，不替它补。**
>
> **② `profiles` 那一格写的是 `Date logging configuration`。** 逐字：
> `Date logging configuration`——**按上下文（另一处章名与常见用法）应是 `Data logging`**，
> **`Date` / `Data` 一个字母之差。本页照原样引。**
>
> **③ 路径只给了一条，而它被用来指两个目录。** 逐字：
> `Path of the default device technology directories cmos and ecl:` 后面只有
> `- /opt/hp93000/soc/dev_tech` **一条** bullet。
> **两个目录各自的完整路径原文没有写。本页不替它补 `/cmos`、`/ecl`。**
>
> **④ 表头与数据行的竖线位置不整齐，而且表头行前面多一个孤立的 ` |`。** 逐字（原文开头）：
> ```
> Subdirectories and files in the device technology directory
>  |
>
> Subdirectory
>
>  |
>
> Contains
>
>  |
>  |
> ```
> ——**`Subdirectory` 前面先出现一个孤立的 ` |`**，而它与 `Contains` 之间的分隔也是靠孤立的 `|` 行；
> **数据行同样如此（名字一行、` |` 一行、内容一行、` |` 与 ` |` 两行）**。
> **整张表在 markdown 层面是散的，`语法节` 里没有收录它**（脚本写明「没有段标记就不收录」）。
> **本页把它重排成真正的表格，但每一格的字是原文的；这个重排是排版动作，
> 原样的散法记在这里。**
>
> **⑤ 表里有两行是「子目录的下级」，但看不出层级。** 逐字：`vectors/.cache`、`waveform/.result`
> ——**它们与 `vectors` / `waveform` 平级排在表里，原文没有缩进、没有层级标记、
> 也没有一句话说明这两行的从属关系。本页照原样列成同级行。**
>
> **⑥ `applicat` / `wafertyp` / `timing_dgrm` 三个目录名看着像截断，而原文没有给全称。**
> 逐字：`applicat`（内容写的是 `Application data for production mode`）、
> `wafertyp`（`Wafer description file`）、`timing_dgrm`（`(Reserved`）。
> **本页照原样写，不补 `application` / `wafertype` / `timing_diagram`——
> 补了就是替语料改字（§11.2）。**
>
> **⑦ 表里的 `Contains` 列混了「说明」与「指引」两种写法。** 逐字对比：
> 多数格是名词短语（`Pin file`、`Analog setup file`），
> 而 `.technology` 那格是 `See Technology file for a device for details.`、
> `ch_attributes` 那格是 `See Channel attributes files for details.`
> ——**两句是完整句子、带 `See … for details` 句式，与其它格不同构。
> 本页照原样抄进表里（逗号、句号都在），不替它统一成名词短语。**
>
> **⑧ `calibration` 那一格是两句话。** 逐字：
> `Calibration data. For the ACTCatr file, see ACTCatr.`
> ——**一个说明句 + 一个指引句，中间用句号连**（而其它格要么说明、要么指引）。
> **本页照原样抄进表里。**
>
> **⑨ 本篇没有 §11.2 ① 那种编码损坏。** 本页查过：**全文没有汉字，也没有 `鈥`**
> （`[一-鿿]` 与 `鈥` 均 0 命中）。

`verified: doc-only`
