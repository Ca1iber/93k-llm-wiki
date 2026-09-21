---
type: object
title: Structure of a TMLimits CSV file
layer: file
stage: testmethod
tags: [tmlimits, csv, file-format, test-number, binning, test-mode, data-logging, test-method]
related: [tmlimits, bin, test-suite, testflow, test-program-explorer, software-bin-summary-tab, hardware-bin-summary-tab, smartest-data-formatter]
sources:
  - 02_System_reference/02.10_Data_Logging/02.10.01.08.01.01.03.01_Structure_of_a_TMLimits_CSV_file.md
created: 2026-09-18
updated: 2026-09-20
verified: doc-only
---

# Structure of a TMLimits CSV file

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **2,049 字符逐字取自** `<02_System_reference/02.10_Data_Logging/02.10.01.08.01.01.03.01_Structure_of_a_TMLimits_CSV_file.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example

The example shown below is part of a bigger TMLimits CSV file. Only a few tests and just one test mode are shown:

```
"Suite name",  "Test name",       "Test number", "Units", "Lsl",   "Usl",   "Test_remarks"
"Test mode",   "",                "",            "QA",    "QA",    "QA",    ""
"Continuity2", "DC_CONT_P",       "555",         "UNIT",  "-0.1",  "0.1",   "WalkZP"
"Continuity2", "DC_CONT_N",       "565",         "UNIT",  "-0.1",  "0.1",   "WalkZP"
"DC_FreeVI",   "IDD_Shutdown",    "575",         "uA",    "-1",    "6.88",  "FreerunVI"
"DC_FreeVI",   "IDD_FREG_PWR_ON", "585",         "mA",    "1",     "10",    "FreerunVI"
"DC_FreeVI",   "FREG_OUT_PWR_ON", "595",         "V",     "1.6",   "2.1",   "FreerunVI"
"DC_FreeVI",   "VDD_ALDO_PWR_ON", "605",         "V",     "1.25",  "1.6",   "FreerunVI"
"DC_FreeVI",   "VDD_DREG_PWR_ON", "615",         "V",     "1.085", "1.315", "FreerunVI"
"ATECtrl",     "ATECtrl",         "625",         "",      "-0.1",  "0.1",   "ATEctrlEdl"
```

This is the same example with an added user-defined column "Status":

```
"Suite name",  "Test name",       "Test number", "Units",  "Status", "Lsl",   "Usl",   "Test_remarks"
"Test mode",   "",                "",            "QA"      "",       "QA",    "QA",    ""
"Continuity2", "DC_CONT_P",       "555",         "UNIT",   "4",      "-0.1",  "0.1",   "WalkZP"
"Continuity2", "DC_CONT_N",       "565",         "UNIT",   "3",      "-0.1",  "0.1",   "WalkZP"
"DC_FreeVI",   "IDD_Shutdown",    "575",         "uA",     "3",      "-1",    "6.88",  "FreerunVI"
"DC_FreeVI",   "IDD_FREG_PWR_ON", "585",         "mA",     "0",      "1",     "10",    "FreerunVI"
"DC_FreeVI",   "FREG_OUT_PWR_ON", "595",         "V",      "1",      "1.6",   "2.1",   "FreerunVI"
"DC_FreeVI",   "VDD_ALDO_PWR_ON", "605",         "V",      "4",      "1.25",  "1.6",   "FreerunVI"
"DC_FreeVI",   "VDD_DREG_PWR_ON", "615",         "V",      "2",      "1.085", "1.315", "FreerunVI"
"ATECtrl",     "ATECtrl",         "625",         "",       "4",      "-0.1",  "0.1",   "ATEctrlEdl"
```

<!-- 语法节 end -->

## 是什么

**一句话：TMLimits CSV 文件就是一个普通 CSV 文件，额外规定了一套列结构。** 原文用三句话把这个骨架钉死：

> 「A TMLimits CSV file is a standard CSV file with a specified column structure.」

> 「Data fields in a TMLimits CSV file are separated by commas; records are separated by newline characters.」

> 「A TMLimits CSV file contains two header rows plus one row for each test.」

**所以文件形状是「2 行表头 + 每个测试 1 行」**——**这两行表头是这张表最需要看懂的地方**，本页大半篇幅在讲它们。

### 表头两行各管什么

**第一行：列名。**

> 「The first header row contains the names of the columns. Which columns you include is optional, but appropriate key columns are required (see Key columns, below).」

**第二行：每一列属于哪个 test mode。**

> 「The second row contains the test mode assigned to each column. If no test mode is specified in this row, the values in the column apply to all test modes. If a test mode is specified, the values are used only when the specified test mode is chosen.」

**「留空 = 对所有模式都生效」**——**这是第二行的全部语义**。

原文还专门给了一段 GUI 操作提示（注意 `Note` 是原文的标签，粘在句子上）：

> 「Note To add a test mode row in the SmarTest GUI (if one is not present), add an empty row at the top and enter "Test mode" (without the quotes) in the first cell.」

**这一段是原文唯一一处「怎么在界面里造出这张表」的步骤**——**它说的是补一个第二行表头，不是补一个普通数据行**。

**关于 test mode 的三条要点，原文列得很清楚**：

> 「- You can specify any number of test modes.」
> 「- You can have multiple columns with the same header if you specify different test modes for them in the second row.」
> 「For example, you can have one column named "Lsl" with the test mode "QA" and a second column named "Lsl" with the test mode "DT".」
> 「- You must not specify a test mode for key columns. You cannot have multiple versions of a key column.」

**这一组是本页最反直觉的一条**：**同名列可以出现任意多次**（靠第二行的 mode 区分），**唯独 key 列不行**。**换句话说，一张表里可以有三个 `Lsl` 列，但不能有两个 `Suite name` 列。**

### 哪些列是必需的

> 「The columns in a TMLimits CSV file are user-definable. Most are optional, but a minimum set is required for useful operation of TMLimits:」

- **Identifying columns**（原文：`Normally, this means the Suite name and Test name columns, but other combinations are possible`）
- **Test number**
- **Lsl**
- **Usl**
- **Units**

**注意这个「必需」是「useful operation 所必需」，不是「文件格式合法所必需」**——**原文的说法是 `a minimum set is required for useful operation`，本页照抄，不替它加强。**

### 20 个支持的列

原文说「These columns can occur in a TMLimits CSV file:」，然后逐个定义。**照抄成表**：

| 列名 | 原文说什么 | 缺省时 |
|---|---|---|
| `Limit key` | 「The name of the row. You can enter any string.」 | 无 |
| `Suite name` | 「The name of the test suite. By default, Suite name is the primary key」 | 无 |
| `Test name` | 「The name of the test to which the limits apply. By default, Test name is the secondary key」 | 无 |
| `Pins` | 「The pins to which the test applies. If it is present, it is used as an additional key, in combination with either Suite name and Test name or with Limit key」 | 无 |
| `Test number` | 「The test number that has been assigned to this test. Test numbers can be assigned either manually or automatically」 | 「If no test number is specified, -1 is assigned as the test number.」 |
| `Units` | 「The units for the test results and spec limits.」 | 无 |
| `Lsl` | 「The lower spec limit.」 | **「1e23 is assumed and the test always fails.」** |
| `Lsl_typ` | 「The type of the lower limit:」`GT` / `GE` / `NA`（原文逐条给了各自的判 PASS 条件） | 「If you do not specify this parameter, the default of GE is used.」 |
| `Usl_typ` | 「The type of the upper limit:」`LT` / `LE` / `NA` | 「If you do not specify this parameter, the default of LE is used.」 |
| `Usl` | 「The upper spec limit.」 | **「-1e23 is assumed and the test always fails.」** |
| `Offset` | 「A fixed value that is added to the test result before it is tested against the specified limits.」 | 无 |
| `Bin_s_num` | 「The number of the software bin specified by Bin_s_name. This information is only evaluated if there is a multibin in the fail branch of the test.」 | 无 |
| `Bin_s_name` | 「The name of the software bin specified by Bin_s_number. This information is not normally evaluated by the software; it is intended mainly for human readers.」 | 无 |
| `Bin_h_num` | 「The number of the hardware bin for the device in case of a failed test.」 | 「If no number is specified, -1 is assumed.」 |
| `Bin_h_name` | 「The name of the hardware bin specified by Bin_h_number. This information is not normally evaluated by the software; it is intended mainly for human readers.」 | 无 |
| `Bin_type` | 「The type of the bin, good or bad.」 | 「If this value is missing, the default is bad.」 |
| `Bin_reprobe` | 「Whether the device is to be retested when this bin is reached.」 | 「The default is no.」 |
| `Bin_overon` | 「Whether the overon behavior applies to this bin (continuing testing even if a stop bin has reached).」 | 「The default is yes and invalid values are also considered as yes.」 |
| `Test_remarks` | 「Any comments for explaining the test row. This column is not evaluated by the software; it is intended only for human readers.」 | 无 |
| `Exec` | 「Whether this test is to be executed (Y) or not (N).」 | **原文没给** |

**四条读这张表要抓的重点**：

1. **「缺限值 = 测试永远失败」，不是「不做判断」。** `Lsl` 缺省补 `1e23`、`Usl` 缺省补 `-1e23`，原文两处都写「the test always fails」。**（推断）这两个哨兵值的符号是相反的**（下限给正无穷大、上限给负无穷大），**但效果都是「任何结果都不合格」**；**原文没有解释这个设计，也没说这是刻意的。本页照抄，不猜。**
2. **多列是常规操作，不是特例。** `Units` / `Lsl` / `Lsl_typ` / `Usl_typ` / `Usl` / `Offset` 六列的说明里都挂着一句「As with Units, above, there may be multiple × columns.」——**「同一个参数按 mode 分成多列」是这张表的标准用法**，也是第二行表头存在的理由。
3. **bin 相关的列有一半是给机器用的，一半是给人看的**：`Bin_s_num` / `Bin_h_num` 才被求值，`Bin_s_name` / `Bin_h_name` / `Test_remarks` 原文都明写「is not normally evaluated by the software; it is intended mainly for human readers」。
4. **硬件 bin 号和软件 bin 号必须同时给**，原文在两处重复同一句：

> 「To use multibinning, you must specify both the software bin number and the hardware bin number.」

**`Bin_s_num` 的取值范围带一个括号注释，值得逐字读**：

> 「The number can be between 0 and 32767. (SmarTest itself also supports other alphanumerical strings of five characters and less, but only integers from 0 to 32767 are compatible with the SmarTest Data Formatter.)」

**自定义列是明确支持的**，原文最后一句：

> 「Additional user-defined columns are supported. The possible values and meanings of these values must also be specified by the user and can be freely chosen.」

**本页「语法 / 参数」节里的第二个例子就是加了一列 `Status` 的效果。**

### Key 列：四选一，按优先级从上往下

原文的规则是一句话加一个编号列表：

> 「Each TMLimits file must contain a column or combination of columns that can act as a key, that is, that uniquely identify each of the tests (rows). There are different possibilities for this; a combination is evaluated only if none of the combinations listed above it is present:」

1. **Suite name, Test name, Pins**
2. **Suite name, Test name** — 原文标注：「This is the recommended combination. If you create a TMLimits CSV file in SmarTest, this combination is used to identify tests.」
3. **Limit key, Pins**
4. **Limit key**

**「按顺序试，上面那组存在就不看下面那组」是本节的唯一机制**——**原文的说法是 `a combination is evaluated only if none of the combinations listed above it is present`。**

**注意标着「recommended」的是第 2 组，不是第 1 组**——**（推断）因为第 2 组是「不看 Pins 也能唯一确定」的那一组，而第 1 组只是它的细分**；**依据只有原文那句 `If you create a TMLimits CSV file in SmarTest, this combination is used`，原文没有解释为什么推荐它。**

**这四组和 TMLimits API 侧的 `setDefaultLookupKeys()` 列的四组是同一组**（见 [[tmlimits]]）。

## 典型用法

> **原文没有 `## Procedure` 段**，也没有编号步骤。
> **可操作的规则散在定义里**，本节把它们收成五条。**本页的「语法 / 参数」节已经逐字收了原文两个完整例子（2,049 字符），不重抄。**

**1. 要动这张表，先确认有没有第二行表头。** 原文给的 GUI 路径是：**在 SmarTest GUI 里加一个空行到最上面，第一格填 `Test mode`**（不带宽引号）。**原文说的是「if one is not present」**——**也就是说没有第二行的表也是合法的**（那时所有列对所有模式生效）。

**2. 手写时的三条硬格式**：逗号分列、换行分行、**两行表头**。**缺任何一条都不是这张表**——原文的 `a standard CSV file with a specified column structure` 就是这个意思。

**3. 要按 mode 分不同限值，就加同名列。** 例：一列 `Lsl` 标 `QA`，另一列 `Lsl` 标 `DT`。**前提是这两列的第一行名字完全相同**（`You can have multiple columns with the same header`）。**反过来，key 列绝不能这么干**。

**4. 要加自定义列，直接加。** 原文只提了一个要求：**值的含义得由你自己定义**（`The possible values and meanings of these values must also be specified by the user`）。**这些列怎么被 API 读到，在本页的源文档里没有写**——**本页的源只说了「支持」。**

**5. 要用 multibin，软件 bin 号和硬件 bin 号要成对出现**，而且**这两个列只在「fail 分支里有 multibin」时才被求值**——**原文对 `Bin_s_num` 和 `Bin_h_num` 各写了一遍同一句条件**：

> 「This information is only evaluated if there is a multibin in the fail branch of the test.」

**6. 选定键的顺序不能自己乱定。** key 列是从那四组里按优先级挑的，**不是你随便指定一组就算**（`a combination is evaluated only if none of the combinations listed above it is present`）。**所以「表里有 `Pins` 列」这件事本身会影响用哪一组键。**

## 和谁有关

- [[tmlimits]] — **读这张表的 API 那一侧。** 那张页说的「表里一行 = 一个测试的限值」
  和本页的「2 行表头 + 每测试一行」是同一件事的两面。
  **（两页的对照处，见「出处」第 2 条说明。）**
- [[bin]] — `Bin_s_num` / `Bin_s_name` / `Bin_h_num` / `Bin_h_name` / `Bin_type` / `Bin_reprobe` /
  `Bin_overon` 七列全是 bin 语义；`Bin_reprobe` 直接说「the device is to be retested」
- [[software-bin-summary-tab]] / [[hardware-bin-summary-tab]] — **软/硬 bin 在结果那一侧的两个页**
  （**本页没读它们，不主张具体关系**）
- [[smartest-data-formatter]] — **`Bin_s_num` 那个 0–32767 的范围就是为它定的**：
  原文写「only integers from 0 to 32767 are compatible with the SmarTest Data Formatter」
- [[test-suite]] — `Suite name` 列装的就是它；原文说它「By default … is the primary key」
- [[testflow]] — **test mode（QA / DT / FT）是 testflow 的概念**：本页只管「列怎么标 mode」，
  **「跑测试时怎么选中某个 mode」本页没有**（那在 [[tmlimits]] 那侧）
- [[test-program-explorer]] — 原文两处点名它：`If you create a TMLimits CSV file in SmarTest` 和
  `add a test mode row in the SmarTest GUI`（**但原文没写具体在哪个菜单**）
- `multibin` / `overon behavior` / `stop bin` — **本页的三处核心概念，在语料里都不是独立页**，
  只能写反引号；原文的链接目标是
  `02.08.04.32.02.03.02_Using_the_Overon_feature_while_running_a_testflow.md`（**没读**）
- [[pin]] — `Pins` 列。**「pin group 写在这里算不算匹配」本页没有**（那在 [[tmlimits]] 的参数说明里）
- `Generating Test Numbers` — **原文里 `Test number` 那格的链接目标**
  （raw: `02.10.01.08_Managing_Test_Numbers.md`），**没读**；**所以本页不知道号码是怎么编出来的**
- [[testname-requires-matching-limits]] — **同族话题的页**（**未读，本页不主张关系**）

## 版本

原文有 `## Functional changes` 段，**只有一条**：

- **Introduced in SmarTest 6.5.0**

**这一条是真的版本号，不是哨兵值。** 它写的是 `in`，不是
`Introduced before SmarTest 6.3.2` 那种「本文档集覆盖之前就有」的说法（schema §11.2 ②）。
**和 [[tmlimits]] 那篇的起始版本完全相同（也是 6.5.0）——两张表是同一批上线的。**

**原文没有给任何后续变更条目**——**所以「列结构、默认值、key 优先级在 6.5.0 之后改过没有」
本页没有依据。**

## 出处

`sources:` 一篇：

`02_System_reference/02.10_Data_Logging/02.10.01.08.01.01.03.01_Structure_of_a_TMLimits_CSV_file.md`
（TDC `112490.htm`，共 221 行）

**本页没做的**：

1. **只读了这一篇。** 本页正文里除下面第 2 条声明的那一处外，每个事实都出自这 222 行。
2. **一处跨页对照是例外，在这里说清楚**：本页「和谁有关」里写了
   「这四组键和 `setDefaultLookupKeys()` 列的四组是同一组」、以及
   「`Lsl_typ` 列 ↔ `LslTyp` 字段」这类对照。**对照的另一半来自
   `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.250_TMLimits.md`**——
   **那是本批次另一页（[[tmlimits]]）的 sources，不是本页的 sources。**
   **本页没有从它那里搬任何本页源文档里没有的事实**，只用来做这两页的对齐。
3. **原文里的链接目标一个都没读**：`Generating Test Numbers`
   （raw: `02.10.01.08_Managing_Test_Numbers.md`）和 `overon behavior`
   （raw: `02.08.04.32.02.03.02_Using_the_Overon_feature_while_running_a_testflow.md`）。
   **所以「测试号怎么自动分配」和「overon 到底是什么行为」本页一个字都没有。**
4. **没有实测**：本页没有打开过任何 TMLimits CSV 文件，没有验证过列名的大小写、
   没有验证过缺省值（`1e23` / `-1e23` / `-1` / `GE` / `LE`）在机台上的实际效果。
   **本页所有默认值都是照抄原文的文档事实（`verified: doc-only`）。**
5. **原文没有一张图**，本页没有任何来自图的结论。
6. **「语法 / 参数」节是原文 `## Example` 那两段（2,049 字符）**，
   **不含列定义表**——列定义在原文里没有段标记，脚本一个字都没收，
   **所以本页在「是什么」里照抄了那 20 列的定义和默认值，否则这个页面会没有任何列名。**

> ⚠️ **本篇的语料瑕疵，照实记，一处都没替它改**：
>
> ① **`Bin_s_name` / `Bin_h_name` 的定义引用了两个不存在的列名，而且两条定义互为循环。**
> `Bin_s_num` 那条写 `The number of the software bin specified by Bin_s_name.`
> （**列名是 `Bin_s_name`，对得上**），
> `Bin_s_name` 那条却写 `The name of the software bin specified by Bin_s_number.`
> ——**`Bin_s_number` 这个列名全篇不存在，实际列名是 `Bin_s_num`。**
> `Bin_h_name` 那条同理，写的是 `specified by Bin_h_number`，而列名是 `Bin_h_num`。
> **两处都是把一个不存在的名字当引用目标；本页照抄，不替它改。**
> ② **第二个例子的第二行少了一个逗号，并且整行少一列。**
> 第一例的第二行是 `"Test mode",   "",                "",            "QA",    "QA",    "QA",    ""`（7 格）；
> 第二例（加了 `Status` 列的那一版，表头 8 列）的第二行是
> `"Test mode",   "",                "",            "QA"      "",       "QA",    "QA",    ""`
> ——**`"QA"` 和后面的 `""` 之间没有逗号**，**这一行只有 7 格，比表头少一格**。
> **从位置看，被吃掉的那个空字段正是新加的 `Status` 列的表头格（应为 `""`）。**
> **本页照抄，不替它补逗号。**
> ③ **列表被句号切断，`and` / 句点被吃进列表项**（`Bin_reprobe` 与 `Bin_overon` 各一处）：
> `Possible values are` 下面是 `- yes and` / `- no.`，
> `Supported values are` 下面是 `- yes and` / `- no`。
> ——**`yes and` 里的连词 `and` 和 `no.` 里的句号都成了列表项的一部分，本该在列表外面。**
> ④ **同两处的列表边界丢失**：`The default is no.` 的下一行直接就是 `- Bin_overon`
> （**没有空行**），`The default is yes and invalid values are also considered as yes.` 的下一行
> 直接就是 `- Test_remarks`（**同样没有空行**）。
> **结果是这两行的下一列被吞进上一列的列表里。本页照实引，不重排。**
> ⑤ **`has reached`（应为 `has been reached`）**：
> `Whether the overon behavior applies to this bin (continuing testing even if a stop bin has reached).`
> ⑥ **`Note` 标签粘在句子上**：`Note To add a test mode row in the SmarTest GUI …`。
> **本篇所有 `Note` 都是这个形态**（原文的提示框标签落进了正文）。
> ⑦ **第二行表头的语义和例子对不上**：原文说「The second row contains the test mode assigned
> to each column.」，**但例子里第二行的第一格是标签 `"Test mode"`，不是模式**
> ——**原文自己的 `Note` 也正是让你往第一格填这个标签。**
> **「第一格是标签」这条规则只出现在 `Note` 里，正文那句没说。**
> ⑧ **链接文字和目标文件名不一致**：链接文字是 `Generating Test Numbers`，
> 目标是 `02.10.01.08_Managing_Test_Numbers.md`（**文件名说的是 Managing**）。
> **照实记，不判哪个才是标题。**
> ⑨ **默认值给得不齐**：`Exec` 列只说了 Y/N，**缺省时算什么原文没写**，
> 而同类的 `Bin_type` / `Bin_reprobe` / `Bin_overon` / `Bin_h_num` / `Test number` /
> `Lsl_typ` / `Usl_typ` 都给了默认值。**本页不替它补。**

`verified: doc-only`
