---
type: object
title: Pin configuration master file
layer: file
stage: pin
tags: [pin-configuration, master-file, config-master-file, package-file, alias-file, setup-management-tool, merge, multi-user, smartest-6.5.2]
related: [pin-configuration-file, setup-management-tool, pin-configuration-tool, mapping-pin, dfpn, dfpr, pste, conf, device-directory, smartest-6.5.2]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.05_Pin_configuration_master_file.md
created: 2026-09-21
updated: 2026-09-21
verified: doc-only
---

# Pin configuration master file

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,652 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.05_Pin_configuration_master_file.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Examples

### package.cfg

The following example shows how the Setup Management Tool assembles three pin configuration files according to the master file.

The file `package.cfg` is the package file, and the other two files, `TRANSIO.cfg` and `USB.cfg,` are the alias files.

```
hp93000,config,0.1
DFPN 10201,"",(Data_in_2)
DFPN 10202,"",(Data_in_1)
DFPN 10212,"",(Data_in_5)
DFPN 10213,"",(Data_in_4)
DFPN 10214,"",(Data_in_3)
PSTE 1
CONF OFF,F160,(Data_in_2,Data_in_1,Data_in_5,Data_in_4,Data_in_3)
RDIV 0,(Data_in_2,Data_in_1,Data_in_5,Data_in_4,Data_in_3)
NOOP "6.5.2",,,
```

### transio_file.cfg

```
hp93000,config,0.1
DFPN 10202,"",(Data1)
DFPN 10201,"",(Data2)
PSTE 1
CONF IO,F160,(Data1,Data2)
RDIV 0,(Data1,Data2)
NOOP "6.5.2",,,
```

### usb_file.cfg

```
hp93000,config,0.1
DFPN 10214,"",(Data3)
DFPN 10213,"",(Data4)
DFPN 10212,"",(Data5)
PSTE 1
CONF IO,F160,(Data3,Data4,Data5)
RDIV 0,(Data3,Data4,Data5)
NOOP "6.5.2",,,
```

The pin configuration master file is the following:

```
hp93000,config_master_file,0.1
testerfile:demo.cfg

Package:package.cfg

TRANSIO:transio_file.cfg
USB:usb_file.cfg
```

The pin configuration file assembled from the above files looks like this:

```
hp93000,config,0.1
DFPN 10201,"",(Data_in_2)
DFPN 10202,"",(Data_in_1)
DFPN 10212,"",(Data_in_5)
DFPN 10213,"",(Data_in_4)
DFPN 10214,"",(Data_in_3)
DFPR "TRANSIO","Data2",(Data_in_2)
DFPR "TRANSIO","Data1",(Data_in_1)
DFPR "USB","Data5",(Data_in_5)
DFPR "USB","Data4",(Data_in_4)
DFPR "USB","Data3",(Data_in_3)
PSTE 1
CONF OFF,F160,(Data_in_2,Data_in_1,Data_in_5,Data_in_4,Data_in_3)
RDIV 0,(Data_in_2,Data_in_1,Data_in_5,Data_in_4,Data_in_3)
NOOP "6.5.2",,,
```

<!-- 语法节 end -->

## 是什么

**pin configuration master file 是一份「清单」：它自己不含任何 pin 定义，只写「这次组装
要用哪几个 pin 配置文件、谁当 package、谁当 alias」。** 原文逐字：

> 「A pin configuration can be organized as one single file, or different parts of the pin configuration can be stored in separate files. In the latter case, the respective pin configuration files can be merged through a master file which contains references to the individual files. The Setup Management Tool uses the master file to assemble the in configuration files.」

**第一句给了两种组织方式**，**本页只管第二种**：

| 组织方式 | 产物 | 本页管不管 |
|---|---|---|
| 一份单一文件 | 一个 pin configuration file | ❌ **不管**——那是 [[pin-configuration-file]] |
| **分开几份 + 一份 master file** | **由 master file 合并出来** | ✅ **本页只管这一份 master file** |

**这是本页与 `pin-configuration-file` **两篇文档、两页**的边界**：
**master file 讲「怎么把这些文件拼起来」，被拼的那些文件自身长什么样在另一页。**
**本页正文只写 master file 自己的东西**（头部行、条目格式、四条校验规则、一个完整例子）；
**单个 pin 配置文件里的命令语义，本页不解释、也没有读那篇。**

**⚠️ 原文第三句里有一个错字**（逐字）：`to assemble the in configuration files`
——**按上下文应是 `the pin configuration files`**。**本页照原样引，不改**（见 `## 出处`）。

### 谁在干这件事：Setup Management Tool

**合并不是人手工做的，是一个工具做的**——原文点名的执行者只有一个：
`The Setup Management Tool uses the master file to assemble the in configuration files.`
**（`Setup Management Tool` 就是原文那个超链接的目标，链到 `01.01.07.02.02.04_Setup_Management_Tool.md`。）**
**它也是下面那四条校验规则的执行者**（原文：`The Setup Management Tool verifies that the following conditions are true for all files:`）。
**本页没有读 [[setup-management-tool]] 那一页**，所以那个工具本身的用法不在本页。

### 两种角色：package file 与 alias file

原文逐字：

> 「One of the individual pin configuration files is the "package file", which contains the specification for the complete package. The other files are referred to as "alias files". The pin names in the alias files are taken as pin aliases in the assembled file.」

| 角色 | 原文定义 | 在组装结果里 |
|---|---|---|
| **package file** | `contains the specification for the complete package` | **它的 pin 名全部进结果**（`The pin names specified in this file are all used in the assembled file.`） |
| **alias file** | `The other files are referred to as "alias files".` | **它的 pin 名变成「pin alias」**（`The pin names in the alias files are taken as pin aliases in the assembled file.`） |

**package file 是必有的、且只有一个**（原文：`The Package keyword refers to the package file.`，
**关键字是 `Package`，单数**）；**alias file 可以有多个**（条目格式里写成 `1 … X`）。

### 为什么要拆：多个人并行改

原文一句（逐字），这是整件事的动机：

> 「Splitting the pin configuration into multiple individual files allows multiple users to work on the configuration in parallel.」

**即：拆文件的目的是让多个用户并行工作。**（**原文没有写随之而来的代价或冲突处理**——
**只看得到下面那四条校验规则是「组装时」才检查的。**）

### 四条校验规则（**原文里是四个 bullet，条件 → 后果都写明了**）

原文逐字引出：`The Setup Management Tool verifies that the following conditions are true for all files:`
**四个 bullet 逐字抄在下表**，**原文没有给这四条编号，本页的编号是为了引用**：

| # | 条件（**原文逐字**） | 它管什么 |
|---|---|---|
| 1 | `The numbers of sites specified in different files are same.` | **各文件的 site 数必须相同** |
| 2 | `All the channels in the alias files occur in the package file.` | **alias 文件里的 channel 必须都在 package 文件里出现过** |
| 3 | `The contexts specified in different files are not same, except for the "DEFAULT" context.` | **各文件的 context 不许重名，`"DEFAULT"` 除外** |
| 4 | `The channel must be defined as I/O in the package file to allow both I and O directions for the different alias pins. If the channel is defined to be either only I or only O, then all aliases must have the same specification. None of the aliases must have the opposite direction or I/O.` | **方向（I/O）的相容性**——**第 4 条自己就是三句话** |

**违反的后果，原文一句（逐字）**：

> 「If any of the rules is violated, the assembly process is aborted and an error message is generated.」

**即：任何一条不满足 → 组装中止 + 生成一条错误信息。**
**原文没有写那条错误信息长什么样、也没有写它在哪儿显示**（**本篇没有 `## Errors` 段**）。

**第 4 条单独拆开**（它是四条里唯一有三句话的，**三句话是三件不同的事**）：

| 句 | 原文逐字 | 条件 → 结果 |
|---|---|---|
| 4a | `The channel must be defined as I/O in the package file to allow both I and O directions for the different alias pins.` | **想在不同 alias pin 上同时用 I 和 O** → **该 channel 在 package file 里必须定义成 I/O** |
| 4b | `If the channel is defined to be either only I or only O, then all aliases must have the same specification.` | **package 里只定义成 I（或只 O）** → **所有 alias 必须同规格** |
| 4c | `None of the aliases must have the opposite direction or I/O.` | **任何 alias 都不许取相反方向、也不许是 I/O** |

**（推断）这三句合起来是一条「方向向下收敛」的链**：package 定成 I/O 时下方才可自由选方向；
package 定成单向时下方只能同向。**依据是 4a 与 4b 的 `to allow` 与 `then` 两个连接词——
原文没有用一句话把这层关系说出来，所以这是推断。**

### 头部两行：格式是固定的

原文 `## Header rows` 一节。**第一行是固定内容**（逐字）：

```
hp93000,config_master_file,0.1
```

**注意关键字是 `config_master_file`**——**两个下划线**，
**而组装出来的 pin configuration file 用的是 `config`**（例子里逐字
`hp93000,config,0.1`）。**两者不是同一个头部，别抄混。**

**第二行指定「被拆的那个文件」**（逐字）：

```
testerfile: <tester_file_name>
```

**原文对它只说了一件事**：`It specifies the tester setup file which is to be split.`
——**即：master file 处理的是「怎么把一个 tester setup file 拆开」这件事**；
**`testerfile:` 后面那个文件是「源」，不是产物。**
**（例子里写的是 `testerfile:demo.cfg`，而语料里没有给 `demo.cfg` 的例子——
所以那个源文件长什么样，本页不知道。）**

### 条目格式：`Package:` 一行 + `别名: 文件名` 若干行

原文（逐字）：

```
Package: <package_file_name.cfg>
alias_set_name_1: <alias_file_name_1.cfg>
...
alias_set_name_X: <alias_file_name_X.cfg>
```

**原文对这两类条目的说明**（逐字）：

> 「The Package keyword refers to the package file. The pin names specified in this file are all used in the assembled file.」
> 「The subsequent lines in the master file specify that the alias set named with "alias_set_name_X" is generated with the information extracted from the file "alias_file_name_X.cfg".」

**拆成两半**：

| 行 | 冒号左边 | 冒号右边 | 左边的作用 |
|---|---|---|---|
| `Package: …` | 固定关键字 `Package` | package 文件名 | **指认 package file** |
| `alias_set_name_X: …` | **一个名字（自己起的）** | alias 文件名 | **这个名字就是「alias set 名」**，组装时用它标出这批 alias |

**第二半那句里的 `is generated with the information extracted from` 是本页最要紧的一句**：
**alias set 名不是从文件里读出来的，是 master file 这一行「赋」给它的**——
**所以同一个 alias 文件换一个左边名字，组装出来的东西就带另一个 alias set 名。**

### 路径与注释

| 项 | 原文逐字 |
|---|---|
| **子文件路径** | `The paths for the subfiles can be relative or absolute.` |
| **相对路径的基准** | `The reference directory for relative paths is the directory of the master file.` |
| **注释** | `You can insert comments anywhere in the file. They are identified by the hash (#) character at the start of a line.` |

**注意注释的判据是「行的开头」（`at the start of a line`），不是行内任意位置**——
**而「可以插在任何地方（`anywhere in the file`）」指的是文件里的任何一行，
不是一行里的任何位置。** **（这两句是原文两句话拼起来的，本页把它们并列，
不替原文合并成一句。）**

### 一个例子走完全程（**原文的 `## Examples` 就是干这个的**）

例子的题头句（逐字）：`The following example shows how the Setup Management Tool assembles three pin configuration files according to the master file.`
**三份输入 → 一份 master file → 一份组装结果**，**四份全都给了**：

| 角色 | 文件（**原文里的名字**） | 语法节里的段名 |
|---|---|---|
| package file | `package.cfg` | `### package.cfg` |
| alias file 1 | `TRANSIO.cfg` | `### transio_file.cfg` |
| alias file 2 | `USB.cfg,` | `### usb_file.cfg` |
| **master file** | （未给文件名） | 正文里那段 `hp93000,config_master_file,0.1` |
| **组装结果** | （未给文件名） | `The pin configuration file assembled from the above files looks like this:` |

**从三份输入到组装结果，作者只改了两处**（**这是本页从例子里比对出来的，
不是原文说的**——**原文没有对比过，也没有给组装算法**）：

| | 输入（三份文件合起来） | 组装结果 |
|---|---|---|
| `DFPN` 行 | package 出了 5 个 pin 名（`Data_in_2/1/5/4/3`）；两个 alias 文件各自用**别名**（`Data1/Data2` 与 `Data3/Data4/Data5`） | **只剩 package 那 5 行 `DFPN`** |
| `DFPR` 行 | **没有** | **多出 5 行**：`DFPR "TRANSIO","Data2",(Data_in_2)` 等 |
| 其余（`PSTE` / `CONF` / `RDIV` / `NOOP`） | 三份文件各有一份，且**三份的 `PSTE` / `CONF` / `RDIV` / `NOOP` 内容各不相同** | **取的是 `package.cfg` 那一份**（逐字相同） |

**⚠️ 那个比对结果里有一处值得单独看**：
两个 alias 文件的 `CONF` 行写的是 `CONF IO,F160,(Data1,Data2)` / `CONF IO,F160,(Data3,Data4,Data5)`，
**而组装结果里的 `CONF` 是 `CONF OFF,F160,(Data_in_2,…)`**——**即取的是 package 的 `OFF`。
原文没有解释为什么，也没有说 alias 文件里那两行去哪了。本页照实并列，不替它解释。**

**关于 `DFPR` 这一行**：它**只出现在组装结果里，三份输入里都没有**；
**本篇没有给 `DFPR` 的语法或参数**——**它长什么样只能从这 5 行实例里看**：

```
DFPR "TRANSIO","Data2",(Data_in_2)
DFPR "TRANSIO","Data1",(Data_in_1)
DFPR "USB","Data5",(Data_in_5)
DFPR "USB","Data4",(Data_in_4)
DFPR "USB","Data3",(Data_in_3)
```

**（推断）三个字段依次是「alias set 名」「alias pin 名」「被别名的 package pin 名」**——
**依据是 master file 里 `TRANSIO` / `USB` 正是那两个 alias set 名，
而 `Data2`/`Data1` 是 transio 文件里的 pin 名、`Data_in_2`/`Data_in_1` 是 package 里的 pin 名，
三者一一对得上**。**原文没有用一句话说这三个字段是什么，所以这是推断。**

**⚠️ 一处组装顺序对不上，原文没有解释**：master file 里 `TRANSIO` 在 `USB` **之前**，
而组装结果里 `USB` 的 5 行 `DFPR` **排在 `TRANSIO` 之后、但 USB 的三行在前**——
**准确地说，结果里是 `TRANSIO` 的两行在前、`USB` 的三行在后（与 master file 同序），
而每个 alias 文件内部的顺序（`Data5,Data4,Data3`）与文件里的书写顺序（`Data3,Data4,Data5`）相反。
原文没有说组装是否重排，本页不判。**

## 典型用法

**原文没有 `## Procedure` 段，也没有 `## Before you begin` 段**——
**可依据的只有 `## Header rows` / `## Format of entries` 两节的规则句，
和 `## Examples` 里的那一个完整例子。**
所以下面这份顺序是**从原文的规则句与例子的形态还原出来的**：

| # | 做什么 | 依据（**原文**） |
|---|---|---|
| 1 | **决定拆不拆**：拆的目的是并行 | `Splitting the pin configuration into multiple individual files allows multiple users to work on the configuration in parallel.` |
| 2 | **写好各个 pin 配置文件**（一份 package + 若干 alias） | `different parts of the pin configuration can be stored in separate files` |
| 3 | **新建 master file，第一行照抄固定头部** | `A pin configuration master file always begins with a header row that must have this content:` + `hp93000,config_master_file,0.1` |
| 4 | **第二行写 `testerfile:` 指向被拆的 tester setup file** | `The second line specifies the tester file which is to be divided.` |
| 5 | **写 `Package:` 行** | `The Package keyword refers to the package file.` |
| 6 | **给每个 alias 文件起一个 alias set 名，写成 `名字: 文件名`** | 条目格式那四行 |
| 7 | **路径相对/绝对都行**；用相对时**基准是 master file 所在目录** | `The reference directory for relative paths is the directory of the master file.` |
| 8 | **要注释就以 `#` 起一行** | `They are identified by the hash (#) character at the start of a line.` |
| 9 | **交给 Setup Management Tool 去合并** | `The Setup Management Tool uses the master file to assemble the … configuration files.` |
| 10 | **合并前它会校验那四条**（site 数 / channel 归属 / context 不重名 / 方向相容） | `The Setup Management Tool verifies that the following conditions are true for all files:` |
| 11 | **任何一条不过 → 组装中止 + 报一条错，改完再来** | `If any of the rules is violated, the assembly process is aborted and an error message is generated.` |

**一份最小的 master file（照原文例子的形态）**：

```
hp93000,config_master_file,0.1
testerfile:demo.cfg

Package:package.cfg

TRANSIO:transio_file.cfg
USB:usb_file.cfg
```

**照抄时注意三处**（**都在上面这七行里**）：
① 头部关键字是 `config_master_file`（**下划线**）；
② **`Package` 首字母大写**，而 alias 行左边是**你起的名**（例子里的 `TRANSIO` / `USB` 是**大写**的）；
③ **冒号后面没有空格**（例子里是 `Package:package.cfg`、`TRANSIO:transio_file.cfg`）——
**而原文 `## Header rows` 里写的是 `testerfile: <tester_file_name>`（冒号后有个空格）**，
**例子里却是 `testerfile:demo.cfg`（没有空格）**。**两种写法都在原文里，
本页不判哪个是规范**（见 `## 出处`）。

**没有的东西**：本篇**没有 `Errors` 段**（那四条规则与「组装中止」写在正文里）、
**没有 `Warnings` 段**、**没有 `Limits` 段**，**也没有 `## Application` 段**
（**所以「master file 在哪一步用、谁生成它」，本篇没有说**）。

## 和谁有关

- [[pin-configuration-file]] — **同一族的另一篇、另一页，边界见 `## 是什么` 第一节**。
  **本页讲的是「把几份 pin 配置文件拼起来的那份清单」**；
  **被拼的那些文件自身（`hp93000,config,0.1` 那些 `DFPN` / `PSTE` / `CONF` / `RDIV` / `NOOP` 行）
  是那一页的题目。两篇是两篇文档，本页没有把它们合成一页。**
  **本页只从例子里引用那些行，不解释它们的语义**（也**没有读那一篇**）。
- [[setup-management-tool]] — **上游的执行者**。原文两处点它：
  `The Setup Management Tool uses the master file to assemble the … configuration files.`
  与 `The Setup Management Tool verifies that the following conditions are true for all files:`
  ——**合并与校验都是它做的**。**本页没读那一页**：
  **master file 在工具里怎么选、报的错显示在哪，本页不知道。**
- [[dfpn]] — **例子里三份输入文件的主要命令**（`DFPN 10201,"",(Data_in_2)` 等）。
  **本页只把它们当「输入文件的形状」引用；`DFPN` 的参数与语义在那一页。**
- [[dfpr]] — **只出现在组装结果里的那条命令**。**本篇没有给它的语法**，
  **本页那三个字段的读法是推断**（依据见 `## 是什么`）。**它自己的页在 [[dfpr]]。**
- [[pste]] / [[conf]] — **例子里每一份文件都有、且组装时按 package 那一份取值**的两条命令。
  **本页只指出「组装结果里取的是 package 的版本」这个现象**（逐字比对得出），
  **这两条命令本身在它们各自的页。**
- [[mapping-pin]] — **映射页，pin 段的三层对照**。
  master file 是**「GUI 操作 ↔ 产物文件」这一层里的一个产物**，
  **它在 GUI 上对应哪一步，本页没有依据**（**本篇一个字都没提 GUI**）。
  **对照表在 [[mapping-pin]]，本页不复制它。**
- [[device-directory]] — **（推断）这些文件放在哪儿**。原文只说
  `The reference directory for relative paths is the directory of the master file.`
  ——**基准是「master file 所在目录」，而那个目录在 device 目录树的哪一层，
  本篇没有说**。**目录结构本身在 [[device-directory]]。**
- [[pin-configuration-tool]] — **（推断）GUI 侧的对应物**。**本篇一个字都没提任何工具界面**；
  **依据只是「名字里都有 pin configuration」。本页没有那页的任何事实。**
- [[smartest-6.5.2]] — **版本页，本页 `## 版本` 唯一的落点**。
  另外，**例子里每一份文件都有一行 `NOOP "6.5.2",,,`**——
  **那个 `6.5.2` 和本页的引入版本是同版本号，但原文没有说这一行是干什么的**，
  **本页不下结论。**
- `01.01.07.02.02.04_Setup_Management_Tool.md`（**raw 路径**）— 原文
  `Setup Management Tool` 那个词链到它。**本页没读**（见上）。

## 版本

本文档**有** `## Functional changes` 段，**只有一条**（逐字）：

- **Introduced in SmarTest 6.5.2**

**这不是 §11.2 ② 那个哨兵**（哨兵写的是 `Introduced before SmarTest 6.3.2`）——
**`Introduced in SmarTest 6.5.2` 是常规的引入条目：pin configuration master file 这一套
在 SmarTest 6.5.2 引入。** **版本页见 [[smartest-6.5.2]]。**

**与 wiki 面向版本的关系**：本 wiki 面向 **SmarTest 7.10.3**，
**6.5.2 早于 7.10.3**，所以按文档的说法**这套做法在目标版本里已经在**。
**注意 §11**：这只说明**文档这么写**，**不说明某台机台上可用**（本页 `verified: doc-only`）。

**版本段里没有别的条目**——**四条校验规则、`config_master_file` 这个头部关键字、
`testerfile:` 这一行，各自是哪个版本进来的，语料里没有。**

## 出处

`sources:` 一篇：
`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.05_Pin_configuration_master_file.md`

**本页没做的：**

- **只读了这一篇。** 与它同族的 `02.08.04.18.04_Pin_configuration_file.md`
  （[[pin-configuration-file]] 那一页的正文来源）**没读**——
  **所以本页只能从例子里引用 `DFPN` / `PSTE` / `CONF` / `RDIV` / `NOOP` 这些行的形态，
  给不出它们的字段含义。**
- **[[setup-management-tool]] 没读**（原文那个超链接的目标
  `01.01.07.02.02.04_Setup_Management_Tool.md` 也没读）——
  **所以「怎么在工具里选 master file」「报的错显示在哪里」「组装是显式动作还是自动的」，
  本页不知道**；**原文只写了「它用 master file 组装」「它校验那四条」。**
- **`DFPR` 的语法没有读**（本篇没给）——**本页那三个字段的读法是推断，
  依据写在 `## 是什么` 里。**
- **`demo.cfg` 没有出现在例子里**——**所以 `testerfile:` 指的那个「被拆的 tester setup file」
  长什么样，本页不知道**；**原文只说它 `is to be divided`。**
- **那四条规则违反后「错误信息」的形态没读**——**本篇没有 `## Errors` 段，
  本页给不出错误文本、也拿不到任何关键字**（这一点是本页排错时的最大空缺）。
- **没有查过 GUI 侧**：本篇**一个字都没提任何界面**，
  **所以 master file 在 GUI 上怎么被创建/被选，本页只有 [[mapping-pin]] 这个去处，没有内容。**
- **没有查过「不拆」的那条路**：原文说单一文件也可以，**那条路怎么做，本篇没有展开**
  （见 [[pin-configuration-file]]）。
- **一张图都没看。** 本篇**没有图片引用**（`![` 0 处，本页核过）。
- **没有交叉验证任何别处的文档**（§11：本页只写这一篇里有的）。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> **① 正文第三句里有错字。** 逐字：
> `The Setup Management Tool uses the master file to assemble the in configuration files.`
> ——**`the in configuration files` 中间少了一个词**，按上下文应是 `the pin configuration files`
> （同一篇别处写的都是 `pin configuration`）。
> **本页引文照原样，不改；这一处会连累把它当关键字搜的人**（搜 `the pin configuration files`
> 搜不到这一句）。
>
> **② 例子的标题句里，别名文件的文件名后面粘着一个逗号，而且被包进了反引号里。** 逐字：
> ``The file `package.cfg` is the package file, and the other two files, `TRANSIO.cfg` and `USB.cfg,` are the alias files.``
> ——**`USB.cfg,` 的逗号在反引号内部**（即：逗号被当成了文件名的一部分）。
> **照原样引。**
>
> **③ 正文里的文件名与例子里的文件名对不上。** 正文说两个 alias 文件是
> `TRANSIO.cfg` 与 `USB.cfg`，**而 master file 例子里的条目写的是
> `TRANSIO:transio_file.cfg` 与 `USB:usb_file.cfg`**，
> 例子的小节标题又是 `### transio_file.cfg` / `### usb_file.cfg`。
> **两组名字（`TRANSIO.cfg` / `transio_file.cfg`）在同一篇里并存，原文没有说明它们是不是同一个文件。
> 本页并列，不替它统一。**
>
> **④ 头部行的冒号后有没有空格，两处写法不一致。** `## Header rows` 里逐字是
> `testerfile: <tester_file_name>`（**冒号后一个空格**），
> 而例子里逐字是 `testerfile:demo.cfg`（**冒号后没有空格**）；
> 条目格式那一段也给的是 `Package: <package_file_name.cfg>`（**有空格**），
> 例子里却是 `Package:package.cfg`（**没有空格**）。
> **同一篇里两种写法并存，原文没有说哪种是规范。本页照实记，不替它定。**
>
> **⑤ 组装结果与输入文件之间的差别，原文没有解释。** 三份输入里
> `CONF IO,F160,(Data1,Data2)` / `CONF IO,F160,(Data3,Data4,Data5)`，
> 组装结果里是 `CONF OFF,F160,(Data_in_2,…)`——**取了 package 的 `OFF`
> 而两个 alias 文件里的 `IO` 不见了**；`PSTE` / `RDIV` / `NOOP` 同样只保留了 package 那一份。
> **原文只给了「结果长这样」，没有给组装算法，也没有一句话说明为什么这样取。
> 本页照实并列，不替它解释。**
>
> **⑥ 组装结果里 `DFPR` 行的顺序与 alias 文件的书写顺序相反。** 逐字：`usb_file.cfg` 里是
> `Data3,Data4,Data5`，而结果里是 `DFPR "USB","Data5",…`、`"Data4"`、`"Data3"`——
> **倒序**；`transio_file.cfg` 里是 `Data1,Data2`，结果里是 `"Data2"`、`"Data1"`——**同样是倒序**。
> **两处一致地倒序，看起来是有意的，但原文一个字都没说。本页不下结论。**
>
> **⑦ 例子里每一份文件都有一行 `NOOP "6.5.2",,,`，而原文没有解释它。**
> **三个空字段的位置也照原样**（`"6.5.2",,,`）。**这一行和本页的
> `Introduced in SmarTest 6.5.2` 是同版本号，但原文没有把两者联系起来——本页也不联系。**
>
> **⑧ 本篇没有 §11.2 ① 那种编码损坏。** 本页查过：**全文没有汉字，也没有 `鈥`**
> （`[一-鿿]` 与 `鈥` 均 0 命中）。

`verified: doc-only`
