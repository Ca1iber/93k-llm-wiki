---
type: object
title: Testflow master file
layer: file
stage: testflow
tags: [testflow, file-format, master-file, split-merge, setup-management-tool, parallel-development]
related: [testflow, testflow-file, setup-management-tool, testflow-tool, stpm, stpm-control-file, stpm-merge-rules-file, group-node, test-suite, testflow-variable, flag, bin, level-master-file, pattern-master-file, pin-configuration-master-file, timing-master-file, mapping-testflow, smartest-6.3.2, smartest-6.5.2]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.06_Testflow_master_file.md
created: 2026-09-21
updated: 2026-09-21
verified: doc-only
---

# Testflow master file

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **347 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.06_Testflow_master_file.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example

```
hp93000,testflow_master_file,0.1

testerfile: testflow

information: files/general.tfl
flags: files/general.tfl
bins: files/general.tfl
setup: files/general.tfl
VAR_Default: files/vars.tfl

GROUP group1: files/group1.tfl
VAR myvar1: files/group1.tfl
VAR myvar2: files/group1.tfl

GROUP group2: files/group2.tfl
VAR myvar3: files/group2.tfl
```

<!-- 语法节 end -->

## 是什么

**testflow master file 是「testflow 被拆成多个文件之后，把它们重新拉在一起的那份索引」。**
原文第一段就是全部机制，逐字：

> 「The testflow can be organized as one single file, or its parts can be be stored in separate
> files. In the latter case the parts that make up a complete testflow are pulled together by a
> master file which contains references to the individual files. This structure has the advantage
> that several users can work on the same testflow in parallel.」

**（上面引文里那个重复的 `be` 是原文的，不是本页抄错——见「出处」瑕疵①。）**

**三个要点**：

| # | 事实 | 原文 |
|---|---|---|
| 1 | **它是「拆开时才存在」的东西**——单文件组织时不需要它 | `The testflow can be organized as one single file, or its parts can be be stored in separate files.` |
| 2 | **它本身不含 testflow 内容，只含「引用」** | `a master file which contains references to the individual files` |
| 3 | **它存在的理由是「多人并行」** | `the advantage that several users can work on the same testflow in parallel` |

**三种文件的关系必须分清**（否则这一族文件名会互相指错）：

| 文件 | 是什么 | 本 wiki 的页 |
|---|---|---|
| **testflow file**（也叫 tester setup file） | **testflow 的全部内容**——单文件组织时就是它一个 | [[testflow-file]] |
| **master file**（本页） | **拆开之后的那份索引**，指着一堆子文件 | 本页 |
| **子文件**（subfile） | **被拆出来的每一个部件**，扩展名 `.tfl`（例子里是 `files/group1.tfl`） | **没有专页**（本页只讲索引，不讲子文件内容的格式） |

### 头两行是固定的

原文用两句话把前两行钉死了：

> 「The first line of a testflow master file must be:」`hp93000,testflow_master_file,0.1`

> 「The second line has the format:」`testerfile: <tester_file_name>`

**第二行的作用与它「名字无所谓」的那一条**，原文逐字：

> 「This line specifies the tester setup file which is to be split or into which the subfiles are
> to be merged. If you manage the master file from the Test Program Explorer the name specified
> here is of no particular importance, but it must be present.」

**读法**：**这一行指向的是「被拆的那个整体」**（`the tester setup file which is to be split`）——
**拆的时候从它来，合的时候回它去**。**而从 Test Program Explorer 管理时，这个名字写什么都不重要，
但这一行必须在**（`but it must be present`）——**「可以有意义地省略」和「必须存在」是两件事。**

### 哪些部件可以拆出去：**六种，而且有个硬限制**

原文的清单（`The smallest parts of a testflow that can be stored in separate subfiles are:`）逐字：

| 可拆的部件 | 原文 |
|---|---|
| **Test suite groups** | `Test suite groups` |
| **Information** | `Information` |
| **Flags** | `Flags` |
| **Bins** | `Bins` |
| **Setup** | `Setup` |
| **Variables** | `Variables` |

**紧接着就是那条硬限制**，原文两句，一句说不能拆什么、一句说因此必须怎样：

> 「Note that individual test suites or bins cannot be stored in separate files. Therefore, all top
> level objects must be groups.」

**所以这里有两条相反的规则**：**`Bins` 作为一个「部件」可以拆，但「某一个 bin」不能单独成文件；
test suite 也一样**（**能拆的粒度是 group，不是 suite，也不是单个 bin**）。
**`Therefore, all top level objects must be groups` 就是这条限制的后果**——
**顶层不许是单个 suite 或单个 bin。**

### 每一行怎么写：类型 + 名字 + 子文件

原文那段（逐字要点）：

> 「Each of these parts is associated with a subfile by a line which specifies the type of the part,
> its name (except for general information such as flags and the setup files), and the associated
> subfile. Different parts can be associated with the same subfile. The group subfiles are merged
> in the order of the master file entries.」

**三条读法**：

1. **`flags` 与 `setup` 这类「一般信息」没有名字那一格**（`except for general information such as
   flags and the setup files`）——**它们的行是 `类型: 子文件`，不是 `类型 名字: 子文件`。**
2. **多个部件可以指向同一个子文件**（`Different parts can be associated with the same subfile.`）——
   **例子就是这么干的**：`information` / `flags` / `bins` / `setup` 四行**全部指向 `files/general.tfl`**。
3. **合并顺序 = master file 里的书写顺序**（`in the order of the master file entries`）——
   **这是一条有后果的顺序规则**（**而原文只说「按顺序」，没说顺序错了会怎样**）。

### `## Format of different parts`：三组行格式

原文那一节用一张表把行的写法给全了（**细节在「语法 / 参数」节之外，本页逐字引三组**）：

| 组 | 行（逐字） | 原文的说明 |
|---|---|---|
| **group** | `GROUP <group_name> [open|closed]: <file_name>` | `The optional parameter defines whether the group is displayed in full detail (open option) or as a single node (closed option) in the testflow editor.` |
| **五个全局项** | `information: <file_name>` / `bins: <file_name>` / `flags: <file_name>` / `setup: <file_name>` | `Each of these global entries must occur only once in the master file.` |
| **变量** | `VAR <variable_name>: <file_name>` / `VAR_default: <file_name>` | `VAR_default collects all variables that are not specified explicitly by a VAR entry.` |

**三处要注意的**：

- **`[open|closed]` 是可选项，而且它影响的是 testflow editor 的显示**
  （**展开成细节还是收成一个节点**）——**它不影响内容，只影响看**。
- **`information` / `bins` / `flags` / `setup` 四项「每项只能出现一次」**（`only once`）——
  **而 `GROUP` 与 `VAR` 可以出现多次**（例子里 `GROUP` 两次、`VAR` 三次）。
- **`VAR_default` 是「兜底桶」**：**没有用 `VAR` 显式指过的变量全归它**。

### 自动生成的文件名：`group_<group_name>.tfl` 加一个环境变量前缀

原文这一节讲的是**工具自己造文件时怎么起名**：

> 「When the Setup Management Tool splits a testflow file and finds a group for which no entry
> exists in the master file, it must create not only a new subfile for this part, but also a name
> for it. These automatically created file names are constructed as follows:」`group_<group_name>.tfl`

> 「You can add a user defined prefix to the names with the environment variable
> `VERIGY93000_MFH_PREFIX`.」

**所以「没登记的 group」不是报错，是自动补一个新子文件 + 一个新名字**
（**这是本篇给出的唯一一条「工具自己动手」的行为**）。
**前缀的设置办法原文也给了**（逐字）：`export VERIGY93000_MFH_PREFIX=<prefix>`，
**时机是 `before starting SmarTest`**——**即：前缀必须在启动 SmarTest 之前设好。**

### 注释与路径

| 事实 | 原文（逐字） |
|---|---|
| **注释写在行首** | `You can insert comments anywhere in the file. They are identified by the hash (#) character at the start of a line.` |
| **路径可相对可绝对** | `The paths for the subfiles can be relative or absolute.` |
| **相对路径的基准目录** | `The reference directory for relative paths is the directory of the master file.` |

**第二条要连着第三条读**：**相对路径不是相对 device 目录，也不是相对当前工作目录，
而是相对「master file 自己所在的那个目录」**——**master file 一挪，子文件的解析基准就跟着挪。**

## 典型用法

### 例子（**在「语法 / 参数」节里，本页只走一遍**）

原文的 `## Example` 是一份完整的 master file，**逐行读下来正好把上面那些规则演示了一遍**：

| 行（逐字） | 它在干什么 |
|---|---|
| `hp93000,testflow_master_file,0.1` | **第一行**（固定） |
| `testerfile: testflow` | **第二行**：被拆 / 要合并回去的那个 tester setup file 叫 `testflow` |
| `information: files/general.tfl`<br>`flags: files/general.tfl`<br>`bins: files/general.tfl`<br>`setup: files/general.tfl` | **四个全局项，全指向同一个子文件**（演示「不同部件可以共用子文件」）；**每项只出现一次** |
| `VAR_Default: files/vars.tfl` | **变量兜底桶** → `files/vars.tfl`（**注意这一行的写法，见「出处」瑕疵②**） |
| `GROUP group1: files/group1.tfl`<br>`VAR myvar1: files/group1.tfl`<br>`VAR myvar2: files/group1.tfl` | **group1 + 两个变量**，同指 `files/group1.tfl` |
| `GROUP group2: files/group2.tfl`<br>`VAR myvar3: files/group2.tfl` | **group2 + 一个变量** |

**例子里的路径全是相对路径**（`files/...`）——**按上面那条基准规则，它们相对的是 master file 自己所在的目录**。

### 拆分与合并：两套通道（**第二套不是本页 raw 的内容**）

**本篇 raw 自己提到的只有一件**：**拆/合这个动作是 Setup Management Tool 做的**
（`When the Setup Management Tool splits a testflow file …`），
**而且第二行那个 `testerfile` 就是「拆分 / 合并的对接点」**。

**下面是本 wiki 别的页给出的两条通道**（**都不是本页 raw 的内容，逐条标明来源**）：

| 通道 | 谁做 | 依据 |
|---|---|---|
| **`smartest_mfh` 命令行** | [[setup-management-tool]]。[[mapping-testflow]] 的主表那一行写着：**「把 testflow 拆成子文件 / 合并回 tester file」→ GUI 列 `[[setup-management-tool]]`、文件列 `[[testflow-master-file]]`、L3 列是 `smartest_mfh` CLI（`testflow` file_type）** | [[mapping-testflow]] 的主表（**本页读过的 wiki 页**） |
| **`smartest_mfh` 的四种模式** | [[setup-management-tool]]：`assemble`（把 master file 里的子文件合并成 tester file 并下载）/ `split`（反向拆分）/ `assemble_all` / `split_all`（对 device 目录下所有 master file）/ `create`（建空 master file） | [[testflow]] 的 stage 页 的「产物」一节（**本页读过的 wiki 页**；**那一页的依据是 `01.01.07.02.02.04.03`，本页没读**） |
| **另一条合并通道（不是 master file）** | [[stpm]]：`STPM control file` 的 `mtp_device_testflow` 指定要合并进 master test program 的 testflow；[[stpm-merge-rules-file]] 管合并规则 | [[testflow]] 的 stage 页（**本页读过的 wiki 页**） |

**两套通道不要混**：**`smartest_mfh` 干的是「同一个 testflow 拆开/合回」**，
**`stpm` 干的是「把这个 testflow 并进一个更大的 master test program」**——
**两件事的输入输出都不一样**（**这条区分是 [[mapping-testflow]] 与 [[testflow]] 的 stage 页 一起给出的，不是本页 raw 的**）。

### 照本篇能确证的顺序

| # | 做什么 | 依据 |
|---|---|---|
| 1 | **第一行写 `hp93000,testflow_master_file,0.1`** | 原文 `must be`（**文档事实**） |
| 2 | **第二行写 `testerfile: <tester_file_name>`**（`must be present`） | 原文（**文档事实**） |
| 3 | **往下逐条登记部件**：`GROUP <组名> [open\|closed]: <子文件>`；四个全局项各一次；`VAR` / `VAR_default` 指变量 | 原文格式表（**文档事实**） |
| 4 | **要用自动起名前缀的话，先 `export VERIGY93000_MFH_PREFIX=<prefix>`，再启动 SmarTest** | 原文（**文档事实**） |
| 5 | **要拆 / 合，用 [[setup-management-tool]]** | 原文提到它是执行者（**文档事实：只提了名字**）；**CLI 细节来自 wiki 页** |

**本篇没有 `## Procedure`、没有 `## Before you begin`**——
**所以「什么时候该把 testflow 拆开」「拆开之后各子文件怎么协同」本篇一个字没有。**

## 和谁有关

| 和谁 | 什么关系 | 依据 |
|---|---|---|
| [[testflow-file]] | **它指着的那份整体（tester setup file）**。原文第二行就是它：`the tester setup file which is to be split or into which the subfiles are to be merged`。**它是内容，本页是索引** | 本篇（**文档事实**）；[[testflow-file]]（**本页读过的 wiki 页**，只用来说明两页的分工）——**那一篇的 raw 本页没读** |
| [[setup-management-tool]] | **执行拆 / 合的工具，也是那句「自动起名」的主语**。本篇两处点名它：`When the Setup Management Tool splits a testflow file …` | 本篇（**文档事实：名字与那句行为**）；`smartest_mfh` 的模式细节来自 [[mapping-testflow]] / [[testflow]] 的 stage 页（**wiki 页**）——**那篇 raw 本页没读** |
| [[testflow-tool]] | **同族的另一个工具**（Testflow Tool）。**本篇 raw 里出现的 GUI 只有 Test Program Explorer 与 testflow editor 两处，没有 Testflow Tool** | 本篇（**文档事实：无此名**）；[[testflow-file]]（**本页读过的 wiki 页**） |
| [[group-node]] | **能拆出去的最小顶层单位**。`all top level objects must be groups`——**本页的 `GROUP` 行就是它** | 本篇（**文档事实**）；**`group-node` 那一篇的 raw 本页没读** |
| [[test-suite]] | **不能单独成文件的那个**（`individual test suites or bins cannot be stored in separate files`）——**所以它只能被包在 group 子文件里** | 本篇（**文档事实**） |
| [[testflow-variable]] | **`VAR` / `VAR_default` 管的对象** | 本篇（**文档事实**）；**那一篇的 raw 本页没读** |
| [[flag]] / [[bin]] | **两个「可拆部件」的名字**（`Flags` / `Bins`），它们各有自己的子文件行 | 本篇（**文档事实**） |
| [[level-master-file]] / [[pattern-master-file]] / [[pin-configuration-master-file]] / [[timing-master-file]] | **「master file」这一族的兄弟**——**同一套「拆开 + 索引」的模式**，只是主子系统不同。**四页与本页的 raw 互不相同，本页一篇都没读** | [[mapping-level]] / [[mapping-pattern]] 的主表里逐行出现（**本页读过的 wiki 页**）；**四页 raw 本页没读（取材边界）** |
| [[stpm]] / [[stpm-control-file]] / [[stpm-merge-rules-file]] | **另一条合并通道（并进 master test program），与本页的拆/合不是一件事** | [[testflow]] 的 stage 页（**本页读过的 wiki 页**）——**三篇 raw 本页没读** |
| [[mapping-testflow]] | **跨层对照表，而且它读过本页的 raw**（本页的出处那一篇在它的 `sources:` 里）。它的主表把「拆成子文件 / 合并回 tester file」排成了一行 | [[mapping-testflow]]（**本页读过的 wiki 页**） |
| [[testflow]] | **stage 页**。它的「涉及对象」里已经有本页：`[[testflow-master-file]]` `file` ——「把 testflow 拆成多个子文件时的主文件，供多人并行开发」 | [[testflow]] 的 stage 页（**本页读过的 wiki 页**） |
| [[smartest-6.3.2]] / [[smartest-6.5.2]] | **版本页**：本篇 `## Functional changes` 的两条分别指这两版 | 本篇版本段（**文档事实**） |
| `Top-level control structures`（**未建，语料自己声明的子主题**） | **本篇唯一的正式下钻**（讲顶层控制结构）。**本页没读**——**而且 [[mapping-testflow]] 也记着它没读** | 本篇 `#### Subtopics`（**文档事实：篇名与链接**）。**这个名字不在 `prose-allowlist.txt` 里**，故用反引号写（§9.1） |

## 版本

本文档**有** `## Functional changes` 段，段里**两条**，逐字如下：

- `Introduced before SmarTest 6.3.2`
- `SmarTest 6.5.2: Renamed macro variable AGILENT93000_MFH_PREFIX to VERIGY93000_MFH_PREFIX.`

**两条的性质完全不同，必须分开读：**

| 条目 | 是不是哨兵值（§11.2 ②） | 读法 |
|---|---|---|
| `Introduced before SmarTest 6.3.2` | **是**。措辞是 `before`，意思是「在本套文档集覆盖范围开始之前就已经有了」 | **不许读成「6.3.2 新增了 master file」**。只能说：**7.10.3 上有，且它比 6.3.2 更老** → [[smartest-6.3.2]] |
| `SmarTest 6.5.2: Renamed macro variable …` | **不是**。带版本号 + 冒号，是标准变更行 | **6.5.2 把那个环境变量从 `AGILENT93000_MFH_PREFIX` 改名成 `VERIGY93000_MFH_PREFIX`** → [[smartest-6.5.2]] |

**第二条的实用后果很直接**：**正文里那句 `export VERIGY93000_MFH_PREFIX=<prefix>`
只适用于 6.5.2 及以后**——**7.10.3 上是对的**，
**但在 6.5.2 之前的版本上要写旧名 `AGILENT93000_MFH_PREFIX`**
（**这是本页的读法（推断）**：依据是版本条目说「改名」（`Renamed … to …`），
**而改名意味着旧名在新版本里不再有效**——**本篇没有说旧名在新版本上还有没有别名，
本页不声称这一点**）。

**版本段里没有的东西**（照实记，不替它补）：**没有第三条**。
所以「`VAR_default` 是哪一版加的」「`group_<group_name>.tfl` 这个命名规则变过没有」
**在本篇里查不到**。

## 出处

`sources:` **一篇**：

- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.06_Testflow_master_file.md`
  （frontmatter 的 `source_topic` 是 `91577.htm`，**4,352 字节 / 129 行，整篇读完**——
  按 §11.5 口径：字节是 `st_size`，行数是 `wc -l`）
- **重复投放检查做过**（§10 第 0 步）：全语料里 `source_topic: "91577...` **只有这一份**，
  **没有 `_2` 那样的第二投放**（**同批的 [[jsud]] / [[jswf]] 两篇都有，本页没有**）。
- 本页的「语法 / 参数」节是脚本从这一篇的 `## Example` 段逐字抽的（**本页一个字没动**）。
  **本篇的语法节只有那一份例子**——`## Format of different parts` 与
  `## Format of automatically created file names` 两节**不在语法节里**
  （它们没有 `Syntax` / `Parameters` / `Example` 这类段标记），
  **所以本页在正文里把三组行格式与命名规则逐字引了一遍，语法节一个字没动。**
- **本篇没有 `## Errors` / `## Warnings` 段**（实测标题清单为
  `#### Subtopics` / `## Format of different parts` / `## Format of automatically created file names` /
  `## Example` / `## Related information` / `## Functional changes`），
  **所以本页没有「报错条件」节**——**骨架里本来就没有**，不是漏写。

**本页没做的**：

- **`#### Subtopics` 那唯一一篇没读**：`Top-level control structures`。
  **所以「testflow 的顶层控制结构是什么（除了 group 还有什么）」本页一个字没有**——
  **而这正是本篇的正式下钻**（[[mapping-testflow]] 也记着它没读）。
- **`## Related information` 那四条一篇没读**：
  `Collision handling for the testflow master file`、`Testflow file`、
  `Elements of the Testflow Tool`、`Using the Setup Management Tool from the Command Line`。
  **所以「多人并行时的冲突怎么处理」本页一个字没有**——
  **而「多人并行」正是本篇第一段给出的存在理由**（**这一处缺口最要紧**）。
- **`smartest_mfh` 的命令行细节不是本页 raw 的内容**——本页只在
  [[mapping-testflow]]（含它从那篇文档里读到的图证）与 [[testflow]] 的 stage 页 里看到
  `assemble` / `split` / `assemble_all` / `split_all` / `create` 与 `smartest_mfh` 这个可执行文件名。
  **那两页依据的 raw（`01.01.07.02.02.04.03` 等）本页没读**；
  **那一张「`smartest_mfh` 的参数铁路图」本页没有自己打开看**（**图证是 [[mapping-testflow]] 的**）。
- **`SETUP_MAN` 目录、`<file_type>` 取值、以及「SmarTest 自身不支持 setup 组件的 master file 概念」
  这条更一般的说法，都在 [[testflow]] 的 stage 页 里**（**该页依据 `01.01.07.02.02.04.01`**），
  **本页没读那些 raw**。
- **master file 这一族的其它页没读**：[[level-master-file]] / [[pattern-master-file]] /
  [[pin-configuration-master-file]] / [[timing-master-file]]。**所以「这一族是不是同一套写法」
  本页答不了**——**本页只讲 testflow 这一份。**
- **图**：**本篇对 `raw/` 的引用 0 处**——实测 `.png` / `.jpg` / `.gif` / `!\[` / `<img` / `raw/`
  六种写法在本篇里**全部 0 命中**。**所以本页没有任何来自图的结论，这张「没有图」是查过的事实，
  不是「够不着」。**
- **没有实跑。** 没在机台上写过 master file、没跑过 `smartest_mfh split` / `assemble`、
  没设过 `VERIGY93000_MFH_PREFIX`。**「按 master file 顺序合并」这条本页只转录，没验过。**
  `verified: doc-only` 指的就是这件事。

**⚠️ 关于「回上游 `.htm` 核」这件事，本页的做法要说明白**：
**本页没有回上游 `91577.htm` 核任何一处**（**本页按取材边界只读了这一篇 md**）。
**所以下面①③两处，本页分不清它们是「HTML→md 转换坏的」还是「上游 `.htm` 里就坏的」**
（**§11.2 ① 与 ⑥ 的那条判据要求看 `.htm`，本页没看**）。
**本页照原样记录，不猜它们属于哪一族。**

**⚠️ 本篇的语料瑕疵，本页照实记下、一处都没替它改**：

> ① **正文第一句里 `can be be stored`——`be` 重复了一次。** 逐字：
>
> `The testflow can be organized as one single file, or its parts can be be stored in separate files.`
>
> **本页在「是什么」那一节引这句话时，把重复的 `be` 原样留在引文里**（**并在旁边点明了**），
> **一个字没删。**（**是转换坏的还是上游就坏的，本页没核——见上面那段说明。**）

> ② **同一个名字在同一篇里两种大小写**：格式表里逐字是 **`VAR_default:`**、
> 正文说明里也是 **`` VAR_default `` collects all variables …**，
> **而 `## Example` 里那一行逐字是 `VAR_Default: files/vars.tfl`**（**大写 `D`**）。
> 实测计数：**`VAR_default` 出现 2 次、`VAR_Default` 出现 1 次**——
> **即：两处小写、一处大写，而大写那一处在「可以照抄的例子」里。**
> **本页两处并列摆着，不替它统一**（**照抄例子的人会写出大写的那种**，这是这条瑕疵的实际后果）。

> ③ **`In the shell in which you want to smart SmarTest`——`smart` 应为 `start`。** 逐字：
>
> `In the shell in which you want to smart SmarTest, specify the desired prefix before starting SmarTest:`
>
> **后半句用的是 `starting SmarTest`，前半句写成了 `smart SmarTest`**——
> **同一句话里两种写法，前一种不成词。本页照原样引。**

> ④ **第二行那句的句子结构拧着**：`This line specifies the tester setup file which is to be split
> or into which the subfiles are to be merged.`——
> **`which is to be split` 与 `into which the subfiles are to be merged` 两个关系从句共用一个先行词**，
> 读起来要回读一次。**不是错，是原文的行文，本页照原样引。**

> ⑤ **`## Related information` 那四条链接又挤在一行里、中间没有任何分隔**（原文逐字）：
>
> `[Collision handling for the testflow master file](<../../01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02.04.05.04_Collision_handling_for_the_testflow_master_file.md>)[Testflow file](<02.08.04.32.03.05_Testflow_file.md>)[Elements of the Testflow Tool](<02.08.04.32.03_Elements_of_the_Testflow_Tool.md>)[Using the Setup Management Tool from the Command Line](<../../01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02.04.03_Using_the_Setup_Management_Tool_from_the_Command_Line.md>)`
>
> **`](<` 紧接 `[`，四条之间没有逗号、没有换行、没有列表符。**
> **这与同批的 [[waveform-set]]、[[timing-specification]] 是同一个形状**——
> **这一族文档的 HTML→md 压平共性。本页照原样引，没有替它断句。**

> ⑥ **`## Format of different parts` 那张表也没有表头行**（从一条空的第一格 ` | ` 开始）——
> **与 [[wavetable]] / [[jsud]] / [[jswf]] 同一个形状。本页照原样留它，没有补表头。**

> ⑦ **`[open|closed]` 这个可选项在两个例子里都没出现**——
> **本篇给了它的说明，却没有一个用它（或不用它）的对照例子。**
> **这不是错，是例子的覆盖范围，记一笔免得下一个人去找不存在的第二个例子。**

`verified: doc-only`
