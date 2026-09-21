---
type: object
title: Starting the formatter
layer: file
stage: results
tags: [stdf, standard-test-data-format, smartest-data-formatter, global-conf, edl, formatter, results-file]
related: [smartest-data-formatter, edl-file, event-formatter, data-retrieval-library, edf, alphabetical-list-of-flags, smartest-6.3.2, smartest-7.4.5]
sources:
  - 02_System_reference/02.10_Data_Logging/02.10.03.02.01_Starting_the_formatter.md
created: 2026-09-21
updated: 2026-09-21
verified: doc-only
---

# Starting the formatter

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

**没有加标记的语法段。** 定义文档里没有 `Syntax` / `Parameters` / `Example`
这类**段标记**，跟着 `Subtopics` 找一层也没有。
**所以本脚本一个字都不收录**——没有段标记时「哪一段是语法」是猜，而猜就是编（§4）。

<!-- 语法节 end -->

## 是什么

**本篇给了 STDF 的定义句，而且这个定义句有一半是否定句。** 原文逐字：

> 「STDF is the Standard Test Data Format, an industry-standard data log format. It is not the
> abbreviation for "SmarTest Data Formatter".」

**拆成三件：**

| # | 原文 | 含义 |
|---|---|---|
| 1 | `STDF is the Standard Test Data Format` | **`STDF` = `Standard Test Data Format`** |
| 2 | `an industry-standard data log format` | **它是一个数据记录格式，且是行业标准级的** |
| 3 | **`It is not the abbreviation for "SmarTest Data Formatter".`** | **它不是 `SmarTest Data Formatter` 的缩写**——**原文为这一条专门写了一个否定句** |

**第 3 条是本篇最要紧的一句。** 本篇正文里那个程序全称就叫
`SmarTest Data Formatter`，**首字母恰好也是 S·D·F**，
**原文显然是预料到会有人把 `STDF` 读成那个程序名的缩写，所以写了这一句把两者分开。**
**本页照它写：`STDF` 是格式，`SmarTest Data Formatter` 是产出这个格式的程序，是两个东西。**

**本页 slug 叫 `stdf`，而 `title` 是 `Starting the formatter`**——
**本篇讲的是「怎么把一个 formatter 跑起来」，不是「STDF 格式长什么样」**
（见 `## 出处` ①）。

### 本篇实际的范围：STDF 的**生成端**

**本篇没有一节在讲 STDF 格式本身**——**没有字段、没有 record 类型、没有版本（v4 / v5）、
没有一条语法**。本篇的三个正文节全在讲「怎么让那个程序跑起来、怎么配置它」：

| 节（**逐字**） | 讲什么 |
|---|---|
| `## Enabling the data formatter for automatic startup` | **让它随 SmarTest 自动启动** |
| `## Changes to the STDF configuration` | **配置改动什么时候生效** |
| `## Command line formatting of a saved EDL stream` | **命令行处理存下来的 EDL stream** |

**所以本页的事实边界是「STDF 是怎么被生成出来的」**——
**「STDF 里面长什么样」本篇一个字都没有，本页也不能写。**

### 生成链：`EDL` → formatter → `STDF`

**原文把上游写在一句里**，逐字：

> 「In order for the EDL to generate the necessary events and attributes in the data stream, the
> correct data log flags need to be set and the formatter needs to be enabled.」

**这句话里有两个并列的条件，缺一个就没有 STDF：**

| 环节 | 原文（**逐字**） | 谁负责 |
|---|---|---|
| 上游 `EDL` | `the EDL ... generate the necessary events and attributes in the data stream` | **`the correct data log flags need to be set`** |
| 中游 formatter | `the formatter needs to be enabled` | **启用 + 配置** |
| 下游 `STDF` | 命令行 `-d` 的说明：`the name of the EDL file to be processed into STDF` | **产出物** |

**注意 `in order for … need to be set` 这个句式**：**flag 是必要条件，不是开关本身**——
**flag 对了但 formatter 没启用，一样没有 STDF**（这条链的第二环在本篇另一处被单独强调了
三遍，见下）。

### 怎么让它自动跑起来：`global.conf` 里的一个开关

**原文 `## Enabling the data formatter for automatic startup` 一节，逐字：**

> 「You must enable the SmarTest Data Formatter for it to start automatically when SmarTest
> starts. To enable the SmarTest Data Formatter:」

**四条操作（原文 bullet，逐字）——但它们在原文里并不相邻。**
**第 1、2 条之间夹着一句 root 权限说明，第 2、3 条之间夹着一句「不是缩写」的澄清**，
**两句都不是 bullet、也没有标题**；**下面连这两句一起引，才是原文的连续形状**：

> 「- Open the file /etc/opt/hp93000/soc_common/datalog/global.conf.
>
> Editing this file requires root permissions.
>
> - Change the STDF generation configuration option to `formatter.stdf.generateStdf=true`
>
> STDF is the Standard Test Data Format, an industry-standard data log format. It is not the
> abbreviation for "SmarTest Data Formatter".
>
> - Save and close the file.
> - Restart SmarTest.」

**照原文读，「四步」是被两句话切开的**：**改这个文件要 root**（夹在第 1 步后面），
**`STDF` 不是 `SmarTest Data Formatter` 的缩写**（夹在第 2 步后面）。
**前者是权限前提，后者是名词澄清，原文都只靠「另起一段」把它从步骤里分出来。**

**四步里两处要记住的：**

- **路径是 `/etc/opt/hp93000/soc_common/datalog/global.conf`**——
  **它在 `/etc/opt/` 底下，改它要 root**。
- **开关的键名逐字是 `formatter.stdf.generateStdf=true`**——
  **`formatter.stdf.` 这个前缀带着自己所属的组**。

**启用之后的表现，逐字（原文紧接着的段落）：**

> 「After this configuration change, the SmarTest Data Formatter automatically starts when SmarTest
> starts. The formatter runs in the background, and attaches to the current data stream. This
> behavior applies both for on-line and off-line (hardware not connected) testing.」

**三条：随 SmarTest 自动启动 / 在后台跑 / 挂到当前 data stream；
且「在线测试与离线（没接硬件）测试都这样」。**

**还有两条关于配置本身的话**（原文同节末段），逐字：

> 「After SmarTest has initialized and the data formatter is ready to begin capturing data, the
> behavior is controlled by configuration files. These format configuration files enable you to
> create a custom STDF format.」

> 「The configuration options also allow you to turn off the STDF formatter if you choose not to
> output any STDF records.」

**即：初始化之后它的行为由配置文件决定（可以定制 STDF 的形态），而且配置文件里也能把它关掉**——
**所以「启用」与「产不产 STDF」是两层：`global.conf` 管「启不启动」，
配置文件的选项管「出不出记录」。**

### 改完配置什么时候生效

**原文 `## Changes to the STDF configuration` 一节全文只有一句**，逐字：

> 「If you make changes to the STDF configuration, in most cases these changes will take effect at
> the next TestProgramStart event. However, any changes that you make to the STDF configuration
> settings that are in the global.conf file will not take effect until you shut down and restart
> SmarTest.」

**一句里两个时机，要分清：**

| 改的是 | 什么时候生效（**逐字**） |
|---|---|
| STDF 配置（**一般情况**） | `at the next TestProgramStart event` |
| **`global.conf` 里的 STDF 配置** | `will not take effect until you shut down and restart SmarTest` |

**所以 `global.conf` 是特例**——**它不跟着 `TestProgramStart` 走，必须重启 SmarTest**
（这与上面四条操作里的 `Restart SmarTest` 是同一件事的两处写法）。

### 它有两种输入：当前的流，或存下来的流

**原文 `## Command line formatting of a saved EDL stream` 一节开头，逐字：**

> 「The data formatter can either read a current data log stream generated by the test system during
> the production test or a saved data log stream. This allows you to generate real-time and
> post-processed STDF files.」

**两种输入 → 两种产物：`real-time` 的 STDF 与 `post-processed` 的 STDF。**

**存下来的那条流在哪**——原文一句（**行首就是 `Note`，见 `## 出处` ④**），逐字：

> 「Note The saved EDL stream can be found in the data collection file located at
> /var/opt/hp93000/soc/tmp/93k.xxxxx/, where 93k.xxxxx is the session name.」

**三个可变的要记住：路径 `/var/opt/hp93000/soc/tmp/93k.xxxxx/`、
`93k.xxxxx` 是 session 名（占位符），而它说的是 `the data collection file`。**

### 名字：本篇对同一个程序用了四种写法

**这一点要在本页说清，因为它直接影响照着做的人能不能敲对命令：**

| 写法（**逐字**） | 出现处 | 次数 |
|---|---|---|
| `SmarTest Data Formatter` | 正文与标题（其中一次在被否定的那句里，带引号） | 4 |
| `the data formatter` | `## Command line formatting of a saved EDL stream` 的正文、与括注 | 3 |
| `the formatter` | 多处，单独用 | 3 |
| **`dataformatter`** | **只有代码块里**：`%dataformatter -d <EDL filename>` | 2 |

**（推断）代码块里的 `dataformatter` 才是那个可执行文件的名字**——
**依据是同一节紧接着的括注 `(The data formatter program is located in the directory
/opt/hp93000/soc/formatter/bin.)`，两者指的是同一个东西。**
**原文没有把「`SmarTest Data Formatter` 这个名字」与「`dataformatter` 这条命令」明确对齐，
所以这是推断，不是文档事实。**

## 典型用法

**本篇没有 `## Procedure`、没有 `## Before you begin`**，
但**「怎么开始」正是本篇的主题**，所以下面两条路都是原文的正文，不是本页的归纳。

### 路一：让它随 SmarTest 自动启动（四条，**逐字**）

| # | 操作（**逐字**） | 备注（**原文**） |
|---|---|---|
| 1 | `Open the file /etc/opt/hp93000/soc_common/datalog/global.conf.` | `Editing this file requires root permissions.` |
| 2 | `Change the STDF generation configuration option to formatter.stdf.generateStdf=true` | 原文这一条**末尾没有句号**（另三条有，见 `## 出处` ⑥） |
| 3 | `Save and close the file.` | — |
| 4 | `Restart SmarTest.` | **必须重启才生效**（见 `## Changes to the STDF configuration` 那句） |

**做完之后的动作是「什么都不用做」**：原文逐字
`the SmarTest Data Formatter automatically starts when SmarTest starts`，
而且 `This behavior applies both for on-line and off-line (hardware not connected) testing.`

**但还有一个前置**（原文另一段，逐字）：
`In order for the EDL to generate the necessary events and attributes in the data stream, the
correct data log flags need to be set and the formatter needs to be enabled.`
——**所以「改了 `global.conf`」≠「有 STDF 了」，data log flags 也要对。**

### 路二：命令行处理一份存下来的 EDL stream（两条，**逐字**）

原文逐字给的用法行：

```
%dataformatter -d <EDL filename>
```

```
%dataformatter -d <EDL filename> -c <STDF configuration file directory>
```

| 要素 | 原文（**逐字**） |
|---|---|
| 程序位置 | `(The data formatter program is located in the directory /opt/hp93000/soc/formatter/bin.)` |
| `-d` | `The -d option is required and allows you to specify the name of the EDL file to be processed into STDF.` |
| `-c` | `You are not required to specify an STDF format configuration at the command line, but you may do so by using the -c option and giving the name of the directory containing the STDF format configuration files as follows:` |

**两处要提醒的：**

- **`%` 是 shell 提示符，不是命令的一部分。** **原文只写了 `%dataformatter`，没有解释这个 `%`**
  ——**（推断）它是提示符；依据是同篇其余地方写命令时都不带它，
  而这两行出现在代码块里（代码块常连提示符一起抄）。这是推断，原文没说。**
- **`-d` 是必填，`-c` 是可选的**——**原文用 `is required` 与 `You are not required to`
  两个相反的措辞分别交代了它们。**

### 从原文能落成的动作

| 要做的 | 依据 |
|---|---|
| **要在每次跑生产测试时都自动出 STDF** | 改 `global.conf` 的 `formatter.stdf.generateStdf=true`，然后重启 SmarTest |
| **只想临时把一份已存的 EDL 转成 STDF** | 命令行 `%dataformatter -d <EDL filename>`，**不用起 SmarTest 的自动流程** |
| **要指定一套 STDF 格式配置** | 加 `-c <STDF configuration file directory>` |
| **改了 STDF 配置想让它生效** | 一般等到下一个 `TestProgramStart`；**改的是 `global.conf` 就必须重启 SmarTest** |
| **完全不要 STDF 记录** | `The configuration options also allow you to turn off the STDF formatter` |
| **不知道配置文件怎么填** | 原文两次把出口指向同一篇：`See STDF Configuration for more information.`（**本页没读**） |
| **发现改了 flag 还是没数据** | 回头核 `In order for the EDL to generate the necessary events and attributes … the formatter needs to be enabled.`——**两个条件都要满足** |

## 和谁有关

- [[smartest-data-formatter]] — **原文用一句否定句把它和 `STDF` 分开，这是本篇最直接的一处关系**。
  逐字：`It is not the abbreviation for "SmarTest Data Formatter".`
  **即：`STDF` 是格式、`SmarTest Data Formatter` 是程序。**
  **本页只有这一句否定式的关系声明，那个程序自己怎么用、有哪些界面，
  本页没有——那一页本页也没读。**
- [[edl-file]] — **上游，也是命令行的输入**。
  原文逐字：`the name of the EDL file to be processed into STDF`、
  `the saved EDL stream can be found in the data collection file located at
  /var/opt/hp93000/soc/tmp/93k.xxxxx/`。
  **本页只有「它吃 EDL」这个方向，EDL 文件自己是什么、里面装什么，本页没有。**
- [[event-formatter]] — **（推断）同章的另一个 formatter**。
  依据：两页的 frontmatter 同组（`layer: file`、`stage: results`），
  且都叫 formatter。**本篇一个字都没提 `Event Formatter`，那一页本页也没读**——
  **这是推断，不是文档事实；两者共用什么、区别在哪，本页没有依据说。**
- [[data-retrieval-library]] — **（推断）同章**。
  依据：本篇 `sources:` 路径的前两级是 `02_System_reference/02.10_Data_Logging/`，
  **从路径看它落在 Data Logging 这一章里**。
  **本篇没有提过它（也没有提过任何读库）——它的名字没在本篇出现过一次。**
- [[edf]] — **（推断）名字同族**。
  依据只是：本篇把上游叫 `EDL`，而 wiki 另有一页叫 `Event Data Logging Format (EDF)`。
  **本篇一个字都没提 `EDF`，那一页本页也没读**——
  **按页名相邻列出，不代表同物。**
- [[alphabetical-list-of-flags]] — **（推断）本篇提到的 flags 的清单可能在那儿**。
  依据：本篇点名了 `data log flags`（一般说法）与 `stdf_generation`（版本段），
  **但没有列任何清单、也没有给任何一个 flag 的取值**；
  **那一页收不收这两个名字，本页没有依据判断。**
- [[smartest-6.3.2]] / [[smartest-7.4.5]] — **版本页**。本页 `## 版本` 两条各落一个：
  `Introduced before SmarTest 6.3.2` 落前者，`SmarTest 7.4.5: Removed stdf_generation flag` 落后者。
- `STDF Configuration`（**未建、不在 allowlist，故用反引号**）— **原文两次把出口指向它**，
  两处措辞一字不差：`See STDF Configuration for more information.`
  **它链到 `02.10.03.04_STDF_Configuration.md`，本页没读**——
  **所以「STDF 格式配置怎么写」本页一个字都没有，而那正是本篇唯一指定的出口。**
- `global.conf`（**未建**）— **本页那条启动开关所在的文件**，
  路径逐字 `/etc/opt/hp93000/soc_common/datalog/global.conf`。
  **本篇只说「改它要 root」与「改完要重启才生效」，它的其它配置项本页没有。**
- `TestProgramStart`（**未建**）— **STDF 配置改动的默认生效点**（`at the next
  TestProgramStart event`）。**本篇没有解释这个事件什么时候发生、由谁发。**
- `dataformatter`（**未建**）— **命令行里那个可执行文件的名字**，
  与正文的 `SmarTest Data Formatter` 是同一个东西（**推断**，见 `## 是什么` 里那张名字表）。
- `93k.xxxxx`（**未建**）— **session 名的占位符**，
  `where 93k.xxxxx is the session name`。**本篇没有给出真实 session 名的样子。**

## 版本

**本文档有 `## Functional changes` 段，两条**，逐字：

- **Introduced before SmarTest 6.3.2**
- **SmarTest 7.4.5: Removed stdf_generation flag**

**第一条是 §11.2 ② 那个哨兵。** `Introduced before SmarTest 6.3.2` 的意思是
**「早于语料覆盖范围」**，**不是「6.3.2 新增」**——
**所以本篇讲的这套启动方式成立于哪个版本，这份语料里没有。**

**第二条是一条「减法」**：**7.4.5 去掉了 `stdf_generation` 这个 flag。**

**⚠️ 这里有一处对不上，本页照实并列、不替它圆：**
**版本段写的是 `stdf_generation`，而本篇正文里出现的那个键是
`formatter.stdf.generateStdf=true`**——**两个不同的字符串，原文没说它们是同一个东西
（也没说是改名、是两层配置、还是一个 flag 一个键）。**
**（推断）它们相关**，**依据只是两处都带 `stdf` 与「生成」的意思**；
**原文没有把两处对齐，所以这是推断，不是文档事实。**

**（推断）7.4.5 之后「怎么开 STDF」应该另有说法**——
**依据是版本段说 `stdf_generation` 被移除，而本篇正文教的那条路走的是
`global.conf` 里的 `formatter.stdf.generateStdf`，两者对不上；
但 7.4.5 之后该改用什么，本篇一个字都没有。**

**与 wiki 目标版本（SmarTest 7.10.3）的关系**：**本篇最后一条是 7.4.5**——
**7.4.5 到 7.10.3 之间这套启动方式有没有再变，本篇没有依据。**
**尤其：本篇的正文与版本段互相不对齐（见上），所以「照正文做在 7.10.3 上还灵不灵」
本页给不出答案。**

详见 [[smartest-6.3.2]] / [[smartest-7.4.5]]。

## 出处

`sources:` 一篇：
`02_System_reference/02.10_Data_Logging/02.10.03.02.01_Starting_the_formatter.md`

**本页没做的：**

- **本页 slug 叫 `stdf`，而这一篇讲的是「怎么启动 formatter」。**
  **所以「STDF 格式本身」本页一个字都写不出来**——
  **本篇没有 `Syntax` / `Parameters` / `Example` 之类段标记**
  （`## 语法 / 参数` 节已说明，脚本因此一个字都不收录），
  **也没有一节讲字段、record 类型或版本（v4 / v5）。**
  **本页只知道它是 `an industry-standard data log format`，以及怎么把它生成出来。**
- **原文两次指定的那个出口 `STDF Configuration`（`02.10.03.04_STDF_Configuration.md`）没读。**
  **这是本页最大的空缺**：**「配置文件怎么写」「能定制成什么样」本页一个字都没有，
  而本篇把这两件事整个推给了那一篇。**
- **同一节的入口篇（`02.10.03.01_Overview`）没读**，
  **所以 `02.10.03` 这一节的整体结构、以及本篇在其中的位置，本页不知道。**
- **`global.conf` 没读**——所以那个文件里除了 `formatter.stdf.generateStdf` 还有哪些项、
  这个键的取值除了 `true` 还有什么，**本页不知道。**
- **`TestProgramStart` 没读、原文也没解释**——**它是「配置改动默认何时生效」的那个时间点，
  本页只有这个事件名。**
- **`dataformatter` 这个可执行文件没有在真机上核过**——
  **连「正文那个 `SmarTest Data Formatter` 就是命令行的 `dataformatter`」这一点也是推断**（见 `## 是什么`）。
  **本页不写任何本篇没有的选项。**
- **一张图都没有。** 原文没有图片（本页查过：0 处图片语法）。
- **没有交叉验证任何别处的文档**（§11：本页只写这一篇里有的）。
  **尤其：[[smartest-data-formatter]] / [[edl-file]] / [[event-formatter]] /
  [[data-retrieval-library]] 都没读**——
  **本页与它们的关系全部取自本篇这一篇的正文，没有从对面回校过。**
- **`layer: file` / `stage: results` 不是本篇写的**——
  **本篇没有 `## Application` 这类自我定位段**，这个归属是本 wiki 的既有划分。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> **① 页面 slug 与文档标题不是一回事。** 本页文件名是 `stdf.md`，
> 而 `title` 与 H1 都是 `Starting the formatter`；
> **本篇的正标题是「启动 formatter」，`STDF` 只是它里面一句定义句的主语。**
> **本页照实按 `stdf` 写，并把范围声明放在 `## 出处`。**
>
> **② 那个定义句是一句「不是…的缩写」的否定句，且句内套了引号。** 逐字：
> `It is not the abbreviation for "SmarTest Data Formatter".`
> ——**它出现在一串操作步骤的第 2 条与第 3 条之间**，
> **位置是一段独立正文（不是 bullet、不是 Note、也不是脚注）**，
> **上下文正在讲 `formatter.stdf.generateStdf=true` 这个选项**。
> **一句「澄清缩写」的话被放在步骤中间，原文没有给它任何标题或标记。**
>
> **③ 同一个程序在**一篇**里有四种写法。** 逐字并列：
> `SmarTest Data Formatter`（4 次）、`the data formatter`（3 次）、`the formatter`（3 次）、
> **以及只在代码块里出现的 `dataformatter`（2 次，小写、连写）**。
> **其中 `## Enabling the data formatter for automatic startup` 这个二级标题用的是小写那种，
> 而正文第一句用的是大写那种**——**同一节里两种写法紧挨着。**
> **本页不替它统一，也不替它断定它们都是同一个程序（把这一点标成推断）。**
>
> **④ `Note` 那一行没有分隔符，`Note` 后面直接跟正文。** 逐字（**注意开头**）：
> `Note The saved EDL stream can be found in the data collection file located at
> /var/opt/hp93000/soc/tmp/93k.xxxxx/, where 93k.xxxxx is the session name.`
> ——**`Note` 与正文之间只有一个空格，没有冒号、没有破折号、也没有换行**。
> **（与 [[dscp]] 那篇记的 `Note` 毛病同族；那一条本页引自 wiki 页、不是本篇 raw。）**
>
> **⑤ 代码块里的 `%` 没有解释。** 逐字：
> `%dataformatter -d <EDL filename>`、`%dataformatter -d <EDL filename> -c <STDF configuration file directory>`
> ——**两行都以 `%` 开头，而原文正文里把那一段叫 `the formatter can be called from a command line`，
> 一个字都没说 `%` 是什么。** **本页把「它是提示符」标成推断，不写成文档事实。**
>
> **⑥ 四条操作里只有第 2 条末尾没有句号。** 逐字：
> `- Change the STDF generation configuration option to formatter.stdf.generateStdf=true`
> ——**第 1 / 3 / 4 条都以 `.` 结尾，只有第 2 条没有。**
> **本页引文照原样（本页在这条引文里也没有替它补句号）。**
>
> **⑦ 版本段的 `stdf_generation` 与正文的 `formatter.stdf.generateStdf` 是两个字符串。**
> 版本段逐字：`SmarTest 7.4.5: Removed stdf_generation flag`；
> 正文逐字：`Change the STDF generation configuration option to formatter.stdf.generateStdf=true`。
> ——**一个叫 `stdf_generation`，一个叫 `formatter.stdf.generateStdf`；
> 原文没有说它们是同一个东西的两种写法，也没有说不是。本页并列两处，不替它对上。**
>
> **⑧ 定义句里解释 STDF 的那个短语是 `an industry-standard data log format`，
> 而本篇没有给 STDF 的版本号。** 逐字只有这一句：
> `STDF is the Standard Test Data Format, an industry-standard data log format.`
> ——**`v4` / `v5` 这类版本标识在本篇一次都没出现。**
> **而 wiki 的目标版本是 SmarTest 7.10.3——本篇给不出它对上哪个 STDF 版本。**
>
> **⑨ 本篇没有 §11.2 ① 那种编码损坏**（本页查过：汉字 0 个、`鈥` 0 处）。
> **本篇 3,195 个字符，是本批 7 页里最短的两篇之一。**

`verified: doc-only`
