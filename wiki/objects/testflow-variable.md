---
type: object
title: Testflow variable mapping table
layer: file
stage: testflow
tags: [testflow-variable, mapping-table, mtpt, stpm, stpm-mcm, flowvars-csv, system-flags, user-flags, stp, mtp, smartest-7.1.4, smartest-7.2.1]
related: [mtpt, stpm, testflow, testflow-file, testflow-master-file, mapping-testflow, structure-of-a-tmlimits-csv-file, smartest-7.1.4, smartest-7.2.1]
sources:
  - 02_System_reference/02.09_Test_Program_Management/02.09.03.04.08_Testflow_variable_mapping_table.md
created: 2026-09-21
updated: 2026-09-21
verified: doc-only
---

# Testflow variable mapping table

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,192 字符逐字取自** `<02_System_reference/02.09_Test_Program_Management/02.09.03.04.08_Testflow_variable_mapping_table.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

Each row in the testflow variable mapping table describes the mapping of a specific variable or flag. The table contains these columns:

- STP: The name of the STP from which the variable is imported

For system testflow flags, this column contains SYSTEM_FLAGS.

- STP Var: The name of the variable or flag in the STP

For system testflow flags, this column is empty.

- MTP Var: The name of the MTP variable or flag to which the STP variable or flag is mapped
- Type: The data type of the MTP variable or flag
- Value: The value to which the MTP variable or flag is set

For system flags, the value may initially be empty if a flag was defined in none of the STPs or had different settings in different STPs. You must fill in any empty cells in this column; otherwise, STPM will generate an error when creating the MTP.

- Notes: This column allows both you and STPM MCM to add remarks about the variable or flag. These notes are just for human consumption and are never processed automatically by STPM MCM. They may be overwritten when the tables are updated, so they are not a suitable place for storing important information.

STPM MCM notes here any conflicts and other issues detected.

<!-- 语法节 end -->

## 是什么

**这一页讲一张表：它把**各个 STP 里的 testflow 变量与 flag** 映射到**主测试程序（MTP）**的
变量与 flag**。定义句（逐字）：

> 「The testflow variable mapping table of the MTPT (STPM MCM mapping tables) describes how the testflow variables and flags from the STPs (source test programs) are mapped to the MTP (master test program).」

**一句里有三个缩写，逐个交代**（**每个都是原文括号给的**）：

| 缩写 | 原文的展开 | 在句子里扮演什么 |
|---|---|---|
| `MTPT` | `STPM MCM mapping tables` | **这张表所属的那一套表**（原文：`the … table **of the MTPT**`） | 
| `STP` | `source test programs` | **映射的**来源**侧** |
| `MTP` | `master test program` | **映射的**目标**侧** |

**⚠️ 原文只展开了这三个；`STPM MCM` 这个组合它没有展开**（见 `## 出处` ③）。

**方向只有一个：STP → MTP。** 原文用的是 `are mapped to`，
**而反过来说（MTP 的变量怎么回到 STP）本篇一个字都没有。**

### 物理形态：一个叫 `flowvars.csv` 的文件，由一条命令生成

原文两句（逐字）：

> 「The table is stored in a file named flowvars.csv in the MTPT directory. It is created by the generate_template command.」

| 项 | 原文 | 要点 |
|---|---|---|
| **文件名** | `flowvars.csv` | **是个 CSV**，不是二进制 |
| **放在哪** | `in the MTPT directory` | **MTPT 那一套表的目录**（[[mtpt]]） |
| **谁生成** | `It is created by the generate_template command.` | **`generate_template` 生成的**（**那一条命令本身不在本页**） |

**⚠️ 两件事要分清**：**这张表是**生成**出来的，不是手写从零建的**——
**（推断）所以它的行来自「STP 里有什么」，而不是来自「你想映射什么」；
依据只是 `It is created by the generate_template command.` 这一句，
原文没有说生成之后能不能加行、删行。**

### 表里有三类东西（**原文是三个 bullet**）

原文（逐字）：

> 「It contains mapping information for:
> - Testflow variables defined in the STPs
> - User testflow flags set for the STPs (testflow flags prefixed by the user keyword)
> - System testflow flags (testflow flags without the user keyword)」

**三类拆开看**：

| 类 | 原文 | 与另一类的分界 |
|---|---|---|
| **① 变量** | `Testflow variables defined in the STPs` | **这是「变量」**（另两类是 flag） |
| **② 用户 flag** | `User testflow flags set for the STPs (testflow flags prefixed by the user keyword)` | **带 `user` 关键字的 flag** |
| **③ 系统 flag** | `System testflow flags (testflow flags without the user keyword)` | **不带 `user` 关键字的 flag** |

**②与③的分界就是那一个关键字**：**加 `user` 前缀的是用户 flag，不加的是系统 flag**——
**这是原文用两个括号注解说清的唯一一条判据**（`prefixed by the user keyword` 对
`without the user keyword`）。
**⚠️ 那个关键字的**拼法**（是不是就是字面 `user`、大小写如何、写在哪儿），原文没有给示例**，
**本页不替它写成一条语法。**

**「系统 flag 永远在表里」是一条硬规矩**（原文单独一句，逐字）：

> 「System testflow flags are always listed in the mapping table, whether they are set for the STPs or not.」

**即：第③类不受「STP 里设没设」影响，一律出现在表里。**
**（推断）这条规矩解释了为什么下面 `Value` 列会**空着**——
系统 flag 在 STP 里可能没定义／各 STP 设得不一样，所以生成时填不出值；
依据是语法节里 `Value` 那一句 `the value may initially be empty if a flag was defined in none
of the STPs or had different settings in different STPs`，**原文没有把这两句连起来说，
所以这是推断。**

### 六列（**语法节里逐字列了，这里只说它们的分工**）

**语法节**里有每一列的逐字定义，**这里只把「谁填、填什么」摊平**：

| 列 | 原文一行定义的主体 | 谁来填 |
|---|---|---|
| `STP` | `The name of the STP from which the variable is imported` | **生成时带出来**；**系统 flag 那几行这一列是 `SYSTEM_FLAGS`**（原文：`For system testflow flags, this column contains SYSTEM_FLAGS.`） |
| `STP Var` | `The name of the variable or flag in the STP` | 生成时带出来；**系统 flag 那几行这一列**空着**（`For system testflow flags, this column is empty.`） |
| `MTP Var` | `The name of the MTP variable or flag to which the STP variable or flag is mapped` | **映射的目标名** |
| `Type` | `The data type of the MTP variable or flag` | **类型**（**原文没有列出有哪些类型**，见 `## 出处` ⑤） |
| `Value` | `The value to which the MTP variable or flag is set` | **要你填**（见下） |
| `Notes` | `This column allows both you and STPM MCM to add remarks about the variable or flag.` | **人 + STPM MCM 都能写**（见下） |

**⚠️ 六列里有**三列**的 bullet 后面还跟着一段没有缩进的说明**
（`STP` / `STP Var` / `Value` 各一段），**`Notes` 那一条后面跟了两段**——
**在原文的 markdown 里那些说明段与 bullet 是分开的两块**（见 `## 出处` ①）。

### `Value` 列：空着会挡住 MTP 的创建（**本篇唯一一条「会报错」**）

原文（逐字，是 `Value` 那一列后面的续段）：

> 「For system flags, the value may initially be empty if a flag was defined in none of the STPs or had different settings in different STPs. You must fill in any empty cells in this column; otherwise, STPM will generate an error when creating the MTP.」

**条件 → 结果**：

| 条件 | 结果（**原文**） |
|---|---|
| 某个 flag 在**任何 STP 里都没定义过**，或者**各 STP 设的值不一样** | **`Value` 这一格生成时可能是空的**（`may initially be empty`） |
| **你把空格子填满** | 正常 |
| **你不填** | **`STPM will generate an error when creating the MTP`**——**STPM 在建 MTP 时报错** |

**⚠️ 两点**：
**① 报错发生在「建 MTP」时，不在「编辑表」时**——原文写的是
`when creating the MTP`，**所以表可以带着空格子存在**；
**② 错误文本、错误码、在哪儿显示，原文一个字都没有**
（**本篇没有 `Errors` 段**）。

### `Notes` 列：人能写，但它不是存东西的地方

原文（逐字）：

> 「This column allows both you and STPM MCM to add remarks about the variable or flag. These notes are just for human consumption and are never processed automatically by STPM MCM. They may be overwritten when the tables are updated, so they are not a suitable place for storing important information.」
> 「STPM MCM notes here any conflicts and other issues detected.」

**拆成四条**：

| # | 原文 | 要点 |
|---|---|---|
| 1 | `allows both you and STPM MCM to add remarks` | **两个写者：人 + STPM MCM** |
| 2 | `just for human consumption and are never processed automatically by STPM MCM` | **纯给人看，永不自动处理** |
| 3 | `They may be overwritten when the tables are updated, so they are not a suitable place for storing important information.` | **表一更新就可能被覆盖**——**不许当存档位** |
| 4 | `STPM MCM notes here any conflicts and other issues detected.` | **STPM MCM 把发现的冲突写在这里** |

**第 4 条是本页最有用的一句**：**「这张表哪里有问题」，STPM MCM 会写在 `Notes` 列**——
**（推断）所以排查映射问题时，先看这一列**；
**依据只是这句话本身，原文没有说它写入的格式（也没有说它用什么措辞），
所以这是推断。**

### 怎么编辑：原文给了两条路，一条推荐

原文（逐字）：

> 「The file is best edited by importing it into the OpenOffice spreadsheet located in the MTPT folder. Editing is also possible in text editors, but this requires you to make sure yourself that all formatting is correct.」

| 路 | 原文 | 代价 |
|---|---|---|
| **推荐**：导入 MTPT 文件夹里那份 **OpenOffice 电子表格** | `is best edited by importing it into the …` | — |
| **也可以**：文本编辑器 | `Editing is also possible in text editors` | **`this requires you to make sure yourself that all formatting is correct`——格式正确与否自己负责** |

**⚠️ 原文这一句里用的是 `folder`**（`located in the MTPT folder`），
**而同一篇开头写的是 `in the MTPT directory`**——**两个词指同一个地方，原文混用了**
（见 `## 出处` ②）。

## 典型用法

**原文没有 `## Procedure`、没有 `## Before you begin`、没有 `## Example`**——
**可依据的只有「它是谁生成的」「六列怎么分工」「哪一格必须填满」这三处散文。**
**所以下面这份顺序是本页还原的**（**每条的依据都逐字列在后面**）：

| # | 做什么 | 依据（**原文**） |
|---|---|---|
| 1 | **先有 STP**（要映射的变量/flag 得先在 STP 里存在） | `Testflow variables defined in the STPs` / `User testflow flags set for the STPs` |
| 2 | **用 `generate_template` 生成这张表** | `It is created by the generate_template command.` |
| 3 | **去 MTPT 目录找 `flowvars.csv`** | `stored in a file named flowvars.csv in the MTPT directory` |
| 4 | **别漏掉系统 flag 那几行**（它们在表里一定存在） | `System testflow flags are always listed in the mapping table, whether they are set for the STPs or not.` |
| 5 | **把 `Value` 列的空格子全部填满** | `You must fill in any empty cells in this column` |
| 6 | **用 MTPT 里那份 OpenOffice 表编辑（推荐）** | `The file is best edited by importing it into the OpenOffice spreadsheet located in the MTPT folder.` |
| 7 | **要拿文本编辑器改，就自己保证格式** | `Editing is also possible in text editors, but this requires you to make sure yourself that all formatting is correct.` |
| 8 | **别把重要信息放 `Notes`** | `they are not a suitable place for storing important information` |
| 9 | **冲突/问题看 `Notes`** | `STPM MCM notes here any conflicts and other issues detected.` |
| 10 | **建 MTP**（`Value` 没填满会在这时报错） | `otherwise, STPM will generate an error when creating the MTP` |

**照这条路线做，最容易踩的一处是第 5 步**：
**`Value` 的空格子不是「可以稍后补」的**——**它是建 MTP 的**门**。
**而空格子从哪来，原文也交代了**：某个 flag「在任何 STP 里都没定义」或「各 STP 设得不一样」。

**没有的东西**：本篇**没有 `Errors` 段、没有 `Warnings` 段、没有 `Limits` 段、
没有 `## Application` 段**；**也没有任何一行示例**——
**所以 `flowvars.csv` 的一行**长什么样**（列怎么分隔、有没有表头），本页和原文一样答不出**（见 `## 出处` ④）。

## 和谁有关

- [[mtpt]] — **这张表所属的那一套表，也是它存放的地方**。
  原文两处点它：`the MTPT (STPM MCM mapping tables)` 与
  `in the MTPT directory`（raw：`02.09.03.04_MTPT__STPM_MCM_mapping_tables.md`）。
  **本页只讲这一张表**；**MTPT 一共几张表、各自管什么，在那一页。**
  **本页没读它。**
- [[stpm]] — **生成者与校验者**。原文两处把动作派给它：
  `It is created by the generate_template command.`（**`generate_template` 是 STPM 的命令**）
  与 `STPM will generate an error when creating the MTP`。
  **本页没读 [[stpm]]**，**所以 `generate_template` 的参数、以及「建 MTP」是哪条命令，本页不知道。**
- [[testflow]] — **stage 页，本页 `stage: testflow` 所指**。
  **§6：`stage` 填的是「读者该去哪一段找它的用法」，不是「归属」**——
  **本页的产物是 testflow 变量/flag 的映射，最近的一段是 testflow。**
  **本页不写流程叙述。**
- [[testflow-file]] / [[testflow-master-file]] — **（推断）映射两端的文件形态**。
  表里映射的是 `testflow variables` 与 `testflow flags`，
  **而这两页分别是 testflow 文件与 testflow 主文件的页**；
  **依据只是名字里都有 testflow，原文没有点任何一页**。
  **本页没读那两页，所以「表里的 MTP Var 与那一页的什么对应」，本页答不出。**
- [[mapping-testflow]] — **名字最像的一页，必须说清差别**：
  **本页讲的是 MTPT 里那张 `flowvars.csv`（STP → MTP 的变量映射表）**；
  **[[mapping-testflow]] 是本 wiki 的**映射页类**（GUI ↔ 文件 ↔ 命令 ↔ API 的对照表）**。
  **（推断）两者不是一回事——依据是「一个讲 STP→MTP 的数据映射，
  一个讲三层接口的对照」，但本页没读那一页，所以这是推断，不是结论。**
- [[structure-of-a-tmlimits-csv-file]] — **（推断）同族的另一张 CSV 结构页**。
  **依据只是「本页的产物也是 CSV（`flowvars.csv`），而那一页的题目是某个 CSV 的结构」**——
  **原文一个字都没提 TMLimits，也没提那一页。本页没读它。**
- [[smartest-7.1.4]] / [[smartest-7.2.1]] — **版本页**，本页 `## 版本` 两条条目的落点。
- `generate_template`（**未建**）— **生成这张表的那条命令**。
  原文里它是一个链接（raw：`02.09.03.03.02_generate_template.md`）。**本页没读。**
- `OpenOffice spreadsheet for editing the CSV files`（**未建**）—
  **原文推荐的编辑入口**（raw：`02.09.03.04.15_OpenOffice_spreadsheet_for_editing_the_CSV_files.md`）。
  **本页没读**，所以那份表格怎么用、它管几张 CSV，本页不知道。
- 同目录下的另外十几张表（**均未建**，本页一篇都没读）：
  `STP_table` / `Pin_mapping_table` / `Group_mapping_table` / `Test_mapping_table` /
  `Test_suite_table` / `Bin_mapping_table` / `Test_number_mapping_table` /
  `Special_tests_table` / `Shared_pins_table` / `Test_flag_table` /
  `Off_DC_levels_table` / `STP_test_information_table` / `MTPT_configuration_file`。
  **它们与这张表同属 MTPT**（**这是本页从文件名看出来的，原文没有列这份清单**）——
  **本页不知道它们各自的列与规则。**
- `STPM MCM`（**未建**）— **原文用了 5 次而一次都没有展开**（见 `## 出处` ③）。
  **它在 `Notes` 列里写东西，也参与了 MTPT 的名字**，**但本页不知道它是什么。**

## 版本

本文档**有** `## Functional changes` 段，**两条**（**逐字**）：

- **Introduced in SmarTest 7.1.4**
- **SmarTest 7.2.1: Added handling of system flags to the table**

**第一条不是 §11.2 ② 那个哨兵**（哨兵写 `Introduced before SmarTest 6.3.2`）——
**`Introduced in SmarTest 7.1.4` 是常规引入条目：这张表在 SmarTest 7.1.4 引入。**
**版本页见 [[smartest-7.1.4]]。**

**第二条正好解释了本页正文里最显眼的那一段**：
**7.2.1 才把**系统 flag** 加进表里**——
**（推断）所以「`STP` 列写 `SYSTEM_FLAGS`」「`STP Var` 列留空」
「系统 flag 永远在表里」「`Value` 可能初始为空」这四条规矩，
都是 7.2.1 之后才有的形态**。
**依据只是这一条版本条目 + 那四条规矩本身都在讲 system flags；
原文没有把这层因果写出来，所以这是推断。**

**与 wiki 面向版本的关系**：本 wiki 面向 **SmarTest 7.10.3**，
**7.1.4 与 7.2.1 都早于 7.10.3**——**按文档的说法，这两条在目标版本上都已经在**。
**注意 §11**：这只说明**文档这么写**，**不说明某台机台上的 MTPT 就是这副形态**
（本页 `verified: doc-only`）。

## 出处

`sources:` 一篇：
`02_System_reference/02.09_Test_Program_Management/02.09.03.04.08_Testflow_variable_mapping_table.md`

**本页没做的：**

- **只读了这一篇。** 原文里的三处链接目标**一个都没读**：
  `generate_template`（`02.09.03.03.02_generate_template.md`）、
  `OpenOffice spreadsheet for editing the CSV files`（`02.09.03.04.15_…`）、
  `MTPT (STPM MCM mapping tables)`（`02.09.03.04_MTPT__STPM_MCM_mapping_tables.md`，[[mtpt]]）。
  **所以：表怎么生成、电子表格怎么用、MTPT 一共几张表，本页一个字都没有。**
- **同目录下另外十几张 MTPT 表一篇都没读**（清单见 `## 和谁有关` 最后几条）——
  **所以「这张表在 MTPT 里排第几、和别的表有没有先后关系」，本页答不出。**
- **⚠️ 本页**没有**写下面这三样，因为**本篇里一个字都没有**（**本页逐字核过，都是 0 命中**）：
  - **`Userflag`**（0 命中）——**「用户 flag 分哪几种」本篇没有**
  - **`String` / `Double` / `integer`**（均 0 命中）——**`Type` 列只被定义为
    `The data type of the MTP variable or flag`，本篇**没有列出有哪些类型****
  - **`TMLimit`（0 命中）与 `RDI_CONFIGURE`（0 命中）**——
    **本篇没有出现这两个名字，也没有说有哪些变量/flag 的名字是固定的。**
  **如果这三样属别处（例如 MTPT 概览或别的表页），**本页按 §11 不写它们**——
  **本页只有这一篇的依据。**
- **一行示例都没有**：本篇**没有 `## Example`**，**也没有任何一行 CSV**——
  **所以 `flowvars.csv` 的表头、分隔符、引号规则，本页答不出**。
- **错误形态没读**：本篇**没有 `Errors` 段**，
  正文里只有一句 `STPM will generate an error when creating the MTP`——
  **错误码、错误文本、显示在哪里，本页和原文一样没有。**
- **`STPM MCM` 没查**（**本篇出现 5 次、一次都没展开**）——
  **所以它是什么、和 STPM 什么关系、它写入 `Notes` 的措辞是什么样，本页不知道。**
- **`user` 这个关键字没查**：原文只说 `prefixed by the user keyword` /
  `without the user keyword`，**没有给写法、大小写或位置**。
- **一张图都没看。** 本篇**没有图片引用**（`![` 0 处，本页核过）。
- **没有交叉验证任何别处的文档**（§11：本页只写这一篇里有的）。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> **① 三列的 bullet 后面跟着**没有缩进的说明段**，在结构上不属于那个 bullet。** 逐字：
> `- STP: The name of the STP from which the variable is imported` 之后**空一行**、
> 再是 `For system testflow flags, this column contains SYSTEM_FLAGS.`；
> `- STP Var: …` 之后同样接 `For system testflow flags, this column is empty.`；
> `- Value: …` 之后接两整句（`For system flags, the value may initially be empty …`）。
> **这些说明段在 markdown 里是**独立段落**，不是 bullet 的续行**；
> **`Notes` 那一条后面更是跟了两段**（含 `STPM MCM notes here any conflicts and other issues detected.`）。
> **语法节里看得见这个形态（脚本逐字抽了这一段）；本页照实记，不替它缩进。**
>
> **② 同一篇里 `directory` 与 `folder` 混用。** 逐字两处：
> `The table is stored in a file named flowvars.csv in the MTPT **directory**.`
> 与 `importing it into the OpenOffice spreadsheet located in the MTPT **folder**.`
> ——**指同一个地方、两个词。本页照原样引。**
>
> **③ `STPM MCM` 出现 5 次，一次都没有展开。** 逐字第一次出现处：
> `The testflow variable mapping table of the MTPT (STPM MCM mapping tables) describes …`
> ——**括号里展开的是 `MTPT`，而 `STPM MCM` 自己没有被解释**；
> 后面还有 `both you and STPM MCM to add remarks`、
> `never processed automatically by STPM MCM`、`STPM MCM notes here any conflicts`。
> **⚠️ 本页按 §11 不替它展开**（展开就是编）。
>
> **④ 标题说「表」，而 `## Syntax` 讲的是「列」，全篇没有一行示例。**
> 逐字：`### Syntax` 下面是
> `Each row in the testflow variable mapping table describes the mapping of a specific variable or flag. The table contains these columns:`
> ——**说了「每一行描述一个映射」，却**没有给任何一行****。
> **所以「列怎么分隔、有没有表头行、引号怎么写」这些**CSV 层面**的规矩，本篇没有。**
> **本页照实记（这一点在本页 `## 出处` 的第一条空缺里已经说明）。**
>
> **⑤ `Type` 列只说「数据类型」，没有列出有哪些类型。** 逐字：
> `Type: The data type of the MTP variable or flag`
> ——**本页核过：`String` / `Double` / `integer` 在本篇均 0 命中。**
> **本页照实记，不替它补一张类型表。**
>
> **⑥ `## Related information` 只有一条链接。** 逐字：`MTPT (STPM MCM mapping tables)`
> ——**只有一条**（**对比同章的其它篇，通常两条以上**）。**本页照实记。**
>
> **⑦ `Value` 那一段用的是 `For system flags`，而不是它上下文的
> `system testflow flags`。** 逐字对比：
> `STP` 列那段写 `For **system testflow flags**, this column contains SYSTEM_FLAGS.`，
> STP Var 那段写 `For **system testflow flags**, this column is empty.`，
> 而 `Value` 那段写 `For **system flags**, the value may initially be empty …`
> ——**同一类东西，三个地方两个写法（一个省掉了 `testflow`）。**
> **本页照原样引，不替它统一。**
>
> **⑧ 本篇没有 §11.2 ① 那种编码损坏。** 本页查过：**全文没有汉字，也没有 `鈥`**
> （`[一-鿿]` 与 `鈥` 均 0 命中）。

`verified: doc-only`
