---
type: object
title: TESTSET().testname()
layer: L2
stage: results
tags: [results, l2, test-method-api, testset, test-name, datalog, edl, stdf, tsr, smc, hidden-datalog-mode]
related: [results, testset, test, test-summary-tab, mapping-results, testname-requires-matching-limits, edl-file, stdf, smartest-data-formatter, alphabetical-list-of-flags, test-number-generator-and-tmlimits, smartest-7.1.2, smartest-7.5.2, smartest-6.3.2]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244.23_TESTSET__.testname.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# TESTSET().testname()

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,289 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244.23_TESTSET__.testname.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
TESTSET & testname(const STRING &name);
TESTSET & testname(const STRING &name, const bool forceSTDFTestName);
```

 |

Parameter

 |

Description

 |
 |

name

 |

The test name that is stored in the EDL as a `TestNameAttribute`（raw: `../02.10_Data_Logging/02.10.01.06.05.61_TestNameAttrType.md`） for a test result. Used when one of the `TEST`（raw: `02.07.04.01.241_TEST.md`） methods is subsequently called.

Test names can contain any printable ASCII characters, that is, characters with codes from 32 to 126. This includes the space, digits, lowercase letters, uppercase letters, and these punctuation characters: !"#$%&'()*+,-./:;<=>@?[\]^_`{|}~ There is no fixed maximum length for the names in SmarTest. However, STDF limits test names to 255 characters, so test names should not be longer if STDF data logging is intended.

 |
 |

forceSTDFTestName

 |

If this parameter is true, the data formatter writes the name value name directly into the TEST_NAM field of the `TSR record`（raw: `../02.10_Data_Logging/02.10.03.05.26_Test_Synopsis_Record__TSR.md`）.

If the parameter is false, the data formatter calculates the content of the TEST_NAM field from the test suite name, test name, and pin name.

This parameter is optional. The default is false.

 |

### Example

```
TESTSET().testname("Sample_test");
```

<!-- 语法节 end -->

## 是什么

**`testname()` 是 `TESTSET` 的一个成员函数：它给一条 test result 起名字，名字直接进数据日志。**
原文第一句就是全部机制：

> This member function of TESTSET sets a test name for a test result that is specified by the name parameter directly, which is then stored in the EDL as a TestName attribute.

**三个要点拆开**：

| 原文的措辞 | 读出来的事 |
|---|---|
| `of TESTSET` | **它是 `TESTSET` 的成员**——不是独立 API，**先有 `TESTSET` 对象才有它**（宿主见 [[testset]]） |
| `specified by the name parameter directly` | **名字是你直接给的**（不是系统生成的、也不是从别处推出来的） |
| `stored in the EDL as a TestName attribute` | **落点是 EDL 里的一个属性**——名字先写进数据日志，才谈得上后面怎么显示 |

### 它解决的问题：`TEST()` 那个「没有 test name」的情形

原文第二句把「为什么要用它」讲得比较绕，**逐字引一次、再拆**：

> It is useful for assigning a desired test name to a test result, instead of using a value that is automatically assigned in the TEST() API, which does not have a test name, such as a functional test result, when you have used the testnumber (INT number) member function or the testnumber (TESTNUMBER &testnumber) member function to assign numerical values to the corresponding test result.

**能确定的两半**：

| 半句 | 说的是 |
|---|---|
| `It is useful for assigning a desired test name to a test result` | **用途**：给结果起一个「你想要的名字」 |
| `instead of using a value that is automatically assigned in the TEST() API` | **替代**：不用那个「自动给的值」 |
| 原文点到 `testnumber` 的那两个重载 | **场景**：**当你用 `testnumber` 给对应结果编了号**（编号和名字是两件事，见下） |

> **⚠️ 中间那个从句 `which does not have a test name, such as a functional test result` 挂靠不明**：
> 语法上它可能修饰 `the TEST() API`，也可能修饰前面的 `a test result`。
> **两种读法给出的是两件不同的事**（「`TEST()` 本来就没有 test name」vs「有一类 test result 没有 test name，
> 比如 functional test result」）。**原文没有写清，本页不替它选**
> （§11.1：规格/原文没写的地方，不许自己发明一个答案）。
> 另外记一条**口径对照**（**只登记差异，不判谁对**）：本 wiki 的 [[test]] 那一页，语法节里
> 以 `Boolean TEST(` 开头的签名**我实测 37 行，其中 15 行带 `const STRING& testname` 形参**——
> **也就是说 `TEST()` 在不少重载里是能收到一个名字的**，与本篇那句 `which does not have a test name` 口径不同。
> **两种可能（那句修饰的是 test result，或者它说的是「自动给不出名字」）本页都不选**；
> **本页也不去改 [[test]]**（那一页的 raw 本页没读，§13.1：改判要带证据）。

**编号与名字的关系（本篇能说的）**：原文用的词是 **instead of**（替代）——
**它替的是「自动给的那个值」，而编号是另一条线**（`testnumber` 给的是数字，`testname` 给的是名字；
本页 raw 里两个 `testnumber` 成员函数点名了，**但它们各自的行为不在本篇**）。

### 两个重载 + 一个可选的开关

| 签名（逐字见「语法 / 参数」节） | 参数 |
|---|---|
| `TESTSET & testname(const STRING &name);` | 只有名字；`forceSTDFTestName` 走默认值 |
| `TESTSET & testname(const STRING &name, const bool forceSTDFTestName);` | 多一个布尔开关 |

**返回类型是 `TESTSET &`，不是 `void`**——**所以它可以链在别的成员函数后面**
（本 wiki 的 [[testset]] 那一页把它列进 `member_func()` 能放的 8 个成员函数里，
**正是这个用法的依据**；见「典型用法」）。

**名字那一格的原文**：

> The test name that is stored in the EDL as a TestNameAttribute for a test result. Used when one of the TEST methods is subsequently called.

**两个信息**：① 它存的**就是** EDL 里那个 `TestNameAttribute`（同一篇的首段说的是 `a TestName attribute`，
**同一个目标、两个链接文本**，见「出处」⚠️①）；
② **它在「随后调用某个 `TEST` 方法」时才被用上**——**这句话直接给出了顺序**（见「典型用法」）。

### 名字能写什么：**32 到 126 的可打印 ASCII，长度两套口径**

原文对 `name` 那**一个**参数格子里写了两整句，**这是本页最该记住的一张对照**：

> Test names can contain any printable ASCII characters, that is, characters with codes from 32 to 126.

**也就是「空格 + 数字 + 大小写字母 + 标点」**（原文还逐个列了标点，那一串里有反引号、
方括号、花括号——**它已经在上面「语法 / 参数」节里逐字，本页不重抄**：
把那一串搬进正文容易把 markdown 的代码跨度弄坏，而**采信它不需要第二份副本**）。

> There is no fixed maximum length for the names in SmarTest. However, STDF limits test names to 255 characters, so test names should not be longer if STDF data logging is intended.

**两套长度口径摊平**：

| 场景 | 上限 | 原文 |
|---|---|---|
| **SmarTest 自己** | **没有固定上限** | `There is no fixed maximum length for the names in SmarTest.` |
| **要落成 STDF** | **255 个字符** | `However, STDF limits test names to 255 characters, so test names should not be longer if STDF data logging is intended.` |

**注意第二句的条件是 `if STDF data logging is intended`**——**不打算出 STDF 就不受这条约束**
（这是原文自己的条件，不是本页加的）。**EDL 那一侧有没有长度上限，本篇没有写。**

### `forceSTDFTestName` 开关：**只影响 STDF 里那个字段怎么来**

| 取值 | 原文（逐字） | 结果 |
|---|---|---|
| **`true`** | `If this parameter is true, the data formatter writes the name value name directly into the TEST_NAM field of the TSR record.` | **`TEST_NAM` 里就是你给的名字** |
| **`false`**（**默认**） | `If the parameter is false, the data formatter calculates the content of the TEST_NAM field from the test suite name, test name, and pin name.` | **`TEST_NAM` 由 test suite 名 + test name + pin 名算出来** |

> `This parameter is optional. The default is false.`

**所以两个取值的效果差别很具体**：`false` 时，STDF 里那个字段**不是你给的名字本身**，
而是**三个来源拼算出来的**（**怎么拼、用什么分隔符，本篇没有写**）；
**`true` 才是「照我给的写」**。

**三个角色名要说清**（它们在本篇里都只是名字）：

- **`the data formatter`**——原文两处用到它。**本篇没有出现 `SmarTest Data Formatter` 这个产品名**，
  所以「原文的 `the data formatter` 就是本 wiki 的 [[smartest-data-formatter]] 那一页」**这一步是（推断）**，
  依据**只是名字相同**（那一页的 raw 本页没读）。
- **`the TEST_NAM field of the TSR record`**——STDF 的一个字段。**`TSR` 是什么本篇没有展开**
  （raw 里它是一个链接，指向 `02.10_Data_Logging/02.10.03.05.26_Test_Synopsis_Record__TSR.md`，
  **本页没读**）。
- **`test suite name` / `pin name`**——**这两个名字从哪一级取，本篇没有写**（语料未写）。

### 一条 SMC 前提（**这是全篇唯一的「不能用」**）

> This function is not supported within the SMC_backgroundProcessing() test method when flag hidden_datalog_mode is set to 0. (It is supported with hidden_datalog_mode set to 1 or 2.)

| 条件 | 结果 |
|---|---|
| 在 `SMC_backgroundProcessing()` 这个 test method 里 + `hidden_datalog_mode = 0` | **不支持**（`not supported`） |
| 同一个地方 + `hidden_datalog_mode = 1 or 2` | **支持**（原文的括注明写） |

**即：在 SMC 后台里想用 `testname()`，得先看那个 flag 是不是 0。**
`hidden_datalog_mode` 各取值是什么意思，**本篇没有写**——原文只给了那个链接
（指向 `Alphabetical list of flags` 的一个锚点），**本页没读那一页的 raw**。
**「不支持」是报错还是静默失效——本篇也没写**（语料未写）。

### 一处**没有**的东西：本篇不给头文件路径

**本篇没有一句以 `This API is defined in the header file` 开头的说明**（别的 L2 页常有那一句）。
**所以 `layer: L2` 这一步不是本篇的正文给的**——它的依据是**它属于 `TESTSET` 那一族**
（raw 路径 `02.07.04.01.244.23`，父篇 `02.07.04.01.244_TESTSET.md` 是 L2）。
**这一步是（推断），依据只有路径与父子关系。**

## 典型用法

**本文档没有 `## Procedure` 段、没有 `## Before you begin` 段、也没有 `## Important points` 段。**
`## Example` 段**只有一行代码**（已在上面「语法 / 参数」节里逐字）：

```
TESTSET().testname("Sample_test");
```

**从这一行 + 参数说明能排出的顺序只有两步，但这两步是文档明写的：**

| # | 做什么 | 依据（原文） |
|---|---|---|
| 1 | **在调用 `TEST` 之前，先 `testname()` 把名字定下来** | `Used when one of the TEST methods is subsequently called.` |
| 2 | 随后调用某个 `TEST` 方法，**这个名字就被用上** | 同上 |

**⚠️ 第 1 步的「先」是原文的 `subsequently` 给的**——**名字是「备着」的，
不是调完 `testname()` 就立刻写了一条结果**。原文没有写「如果先 `TEST` 再 `testname` 会怎样」。

**例子里用的是临时对象写法**：`TESTSET().testname("Sample_test");`——
**一个 `TESTSET` 临时对象直接链上 `testname()`，不用变量接**（返回值是 `TESTSET &`，所以能这么链）。

**wiki 上现成的四种调用形态在 [[testset]] 那一页**（它那一篇的 `## Syntax descriptions` 一节）：
`TESTSET().member_func().judgeAndLog_xxx()` / `TESTSET(false, site).member_func().judgeAndLog_xxx()` /
系统预置的 `TestSet.member_func().judgeAndLog_xxx()` / 用户自建的 `TESTSET obj;` 再 `obj.member_func().judgeAndLog_xxx()`。
**本篇只出现第一种**（`TESTSET()` + `.testname()`）。

**要让 STDF 里的 `TEST_NAM` 照你给的名字写**（而不是三个来源拼算的）：
**用带第二个参数的重载，传 `true`**——即 `forceSTDFTestName`。
**要留在默认（`false`）也行，但要知道那时字段内容不是这个名字本身**（见「是什么」最后那张表）。

**在 SMC 后台里用**：先确认 `hidden_datalog_mode` 不是 `0`（原文的括注明写 1 与 2 可以）。

**本篇没给的**：名字和 limit 表怎么对上（见「和谁有关」）、名字在 GUI 上显示成什么样
（[[test-summary-tab]] 那一页记着 `Test` 列由它给出，**但那不是本篇的话**）、
以及「同一个名字用两次会怎样」——**都没有**。

## 和谁有关

- [[results]] — **stage 页，也是本页 `stage: results` 的理由**。本页的落点全在结果侧
  （EDL 的属性、STDF 的字段）。**那条流程不在本页**（§2.2）。
- [[testset]] — **宿主类，唯一真正的上游**。本页 raw 的 `## Related information` **整节只有它一条**。
  那一页把 `testname()` 列进 `member_func()` 能放的 **8 个成员函数**之一
  （`cont()` / `port()` / `reliabilty()` / `testname()` / `testname_default()` / `testnumber()` /
  `testnumber_default()` / `testnumber_none()`），并记着「设一次、后面都继承」的机制。
  **本页没有读 `TESTSET` 那一篇的 raw**，所以上面这些是**那一页的记载**。
  ⚠️ **那一页还有一句现在过时了**：它说 `TESTSET()` 的 **33 个子主题`一篇没读、也都没有页`**——
  **而本页（`02.07.04.01.244.23`）正是那 33 个之一，且已经建了**。
  **本页只记这件事，不去改那一页**（§13.1：改判要带证据）。
- [[test]] — **名字的使用者**。原文那句 `Used when one of the TEST methods is subsequently called.`
  把顺序钉死了：**先 `testname()`，后 `TEST`**。**本页没有读 `TEST` 那一篇的 raw**——
  所以「`TEST()` 自己那个 `testname` 形参和这里设的名字谁优先」**本页答不出来**（见「是什么」那条 ⚠️）。
- [[test-summary-tab]] — **名字的第一处可见落点**：那一页记着它那一篇写着
  Test summary tab 的 `Test` 列是 `The test name as specified by the TESTSET.testname()`。
  **那句话不在本篇的 raw 里**（本篇没有出现任何界面名），**本页只登记它来自哪一页**。
- [[mapping-results]] — **跨层对照表**：它把本页填在「统计评估与下钻到单条记录」那一行的 L2 格，
  与 `PUT_DATALOG`、`TESTSET` 并列。**本页没有读那一页的 sources。**
- [[testname-requires-matching-limits]] — **另一条「名字」规矩的页，但两页的关系没有文档依据**：
  它讲的是「limit 名字必须与 test suite 上的同名」那类约束。
  **本篇没有一句说这个名字必须与 limit 表对上**——所以**本页不据此声称两者管的是同一个名字**。
  （**可核对的两条**：① [[testset]] 那一页把这条关系标成**（推断）**，
  依据只是「那条约束的标题」；② 我核过 [[testname-requires-matching-limits]] 那一页的正文，
  **`TESTSET` 与 `testname()` 在它里面出现 0 次**——**这条关系是单向的记载，不是双向的。**
  **那一页的 raw 本页没读。**）
- [[edl-file]] / [[stdf]] — **名字的两个去向**：EDL 里的 `TestNameAttribute`（首段）
  与 STDF 里的 `TEST_NAM` 字段（参数表）。
  **两页的 raw 本页都没读**——EDL 里那个属性长什么样、STDF 里 255 字符怎么截断，**本页都没有**。
- [[smartest-data-formatter]] — **（推断）原文那个 `the data formatter`**。依据只是名字相同
  （见「是什么」）。**本篇没有点任何产品名 / 界面名**，**本页也没读那一页**。
- [[alphabetical-list-of-flags]] — **`hidden_datalog_mode` 的定义页**：本篇给的链接就指向它
  （带锚点 `#_342556__row_hidden_datalog_mode`）。
  **本页没读那一页**，所以**各取值的含义、以及「不支持」的表现，本页都答不出来**。
- [[test-number-generator-and-tmlimits]] — **编号那条线的汇总页**。本篇提到 `testnumber` 是
  为了说明**什么时候该用 `testname`**（编号代替不了名字）；**本篇没有点名这一页**，
  **按主题并列，不代表同物**。
- `TESTSET().testnumber()`（**未建**，不在 allowlist）— 原文点了它的两个重载
  （`testnumber (INT number)` 与 `testnumber (TESTNUMBER &testnumber)`），
  raw：`02.07.04.01.244.25_TESTSET__.testnumber.md`。**本页没读它。**
- `TestNameAttrType`（**未建**）— EDL 里那个属性的类型页，raw：`02.10.01.06.05.61_TestNameAttrType.md`
  （首段与参数表**链接文字不同**，见「出处」⚠️①）。**本页没读它。**
- `TSR record`（**未建**）— `TEST_NAM` 所在的那条记录，raw：`02.10.03.05.26_Test_Synopsis_Record__TSR.md`。
  **本页没读它。**
- `SMC_backgroundProcessing()` / `hidden_datalog_mode`（**均未建**）— 那条 SMC 前提的两个词。
- [[smartest-7.1.2]] / [[smartest-7.5.2]] / [[smartest-6.3.2]] — **版本页**：
  本篇 `## Functional changes` 三条的落点（见「版本」）。

## 版本

本文档有 `## Functional changes` 段，**三条**：

- `Introduced before SmarTest 6.3.2`
- `SmarTest 7.1.2: Added forceSTDFTestNam parameter`
- `SmarTest 7.5.2: Renamed forceSTDFTestNam parameter to forceSTDFTestName`

**第一条是 §11.2 ② 那个哨兵值，不是「6.3.2 引入了它」**（措辞是 `before` 不是 `in`），
所以**本页答不出「哪一版才有 `testname()`」**。版本页 [[smartest-6.3.2]] 对这批哨兵
**单列一节、不逐条铺开**，本页这一条不在它正文列出的条目里。

**后两条是正常的版本行，而且它们连起来是一件事**（**照字面读**）：

| 版本 | 原文 | 读法 |
|---|---|---|
| **7.1.2** | `SmarTest 7.1.2: Added forceSTDFTestNam parameter` | **加了第二个参数**——**参数名写的是 `forceSTDFTestNam`**（**少一个 `e`**） |
| **7.5.2** | `SmarTest 7.5.2: Renamed forceSTDFTestNam parameter to forceSTDFTestName` | **把它改名成 `forceSTDFTestName`**（**补上了那个 `e`**） |

> **两行是自洽的**：7.1.2 加的就是那个少 `e` 的名字，7.5.2 才改成带 `e` 的。
> **所以 `forceSTDFTestNam` 那个拼法不是笔误漏字，是「当时真的那么叫」的记录**——
> **（推断）**，依据就是下一行那句 `Renamed` 的说法。
> **本页照原样引这两行、一个字都不替它补**。
> **一处语料未写**：**改名之后旧拼法还能不能用**（有没有兼容别名），**两行都没有说**。

**两条都已收进版本页**（我核过：[[smartest-7.1.2]] 与 [[smartest-7.5.2]] 各收本页一条）。

**「没记录」不等于「没改过」**：三条之后**本篇没有别的版本行**，
所以**「7.5.2 之后它改了没有」本页答不出**。

## 出处

`sources:` 一篇：
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244.23_TESTSET__.testname.md`
（TDC `127794.htm`，72 行 / 2,853 字节）。**整篇读完。**

**本页没做的：**

- **`TESTSET`（`02.07.04.01.244`）没读**——**这是本页最大的缺口**。本页 raw 的
  `## Related information` **整节只有它一条**，而「`testname()` 在哪个函数里调、
  临时对象与系统预置对象怎么选、别的 7 个成员函数各做什么」**全在那一篇里**。
  （本 wiki 有 [[testset]] 那一页，**那是别的批次建的，本页没有读它的 raw**——
  上面「和谁有关」里引它的地方都标了「那一页的记载」。）
- **`TEST`（`02.07.04.01.241`）没读**——**顺序那条要求（原文那句 `Used when one of the TEST methods is subsequently called.`）的另一半在它那里**：那个 `testname` 形参与本函数设的名字是什么关系，
  **本页没有**。（[[test]] 那一页已建，本页只按它的语法节做了一次口径对照，**没读它的 raw**。）
- **`Alphabetical list of flags` 没读**（`02.08.04.32.01.02.07.01`，本篇给的链接带锚点
  `#_342556__row_hidden_datalog_mode`）——**`hidden_datalog_mode` 的取值含义本页没有**。
- **`TestNameAttrType`（`02.10.01.06.05.61`）、`TSR record`（`02.10.03.05.26`）都没读**——
  所以**EDL 那个属性长什么样、`TEST_NAM` 在记录里的类型与长度本页都没有**。
- **`SmarTest Data Formatter` 没读**（[[smartest-data-formatter]] 那一页已建，
  **本页没有读它那一篇**）——**「计算」那两个字段到底怎么算，本页没有**。
- **`TESTSET().testnumber()`（`02.07.04.01.244.25`）没读**——本页只按原文那两处链接写了名字。
- **一张图都没看——因为这一篇里没有图。** 实测全文 **0 处** `.png` / `.jpg` / `raw/`。
  **所以本页没有任何来自图的结论。**
- **没有实跑。** 没在任何机台上设过一个 test name，也没验证过 `forceSTDFTestName` 两种取值的实际输出、
  以及 `hidden_datalog_mode = 0` 时那声「不支持」是报错还是静默。
  `verified: doc-only` 指的就是这件事。
- **本文档没有 `## Procedure` / `## Before you begin` / `## Important points` 段，
  `## Example` 段只有一行代码。** 上面「典型用法」那两步是**本页从参数说明里排出来的**
  （依据就是 `subsequently` 那个词），**不是文档给的编号流程**。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
> ① **同一个目标，两个链接文本。** 首段写的是 `stored in the EDL as a TestName attribute`，
> 而参数表那一格写的是 `stored in the EDL as a TestNameAttribute for a test result.`——
> **两处的链接指向同一个文件**（`02.10.01.06.05.61_TestNameAttrType.md`），
> **一处叫 `TestName`、一处叫 `TestNameAttribute`**。**原文如此，本页两处都照引。**
> ② **第二句的从句挂靠不明**（`which does not have a test name, such as a functional test result`）——
> 本页在「是什么」里并列了两种读法，**不替它选**，并附了一条与 [[test]] 页的口径对照。
> ③ **原文那句 `Test names can contain any printable ASCII characters` 后面列的那串标点里带着反引号**，
> 而且它和上下文挤在同一段里（本页实测那一串里含反引号、方括号、花括号与竖线）。
> **本页不把那串重抄进正文**（照抄容易把 markdown 的代码跨度弄坏）——
> **它在上面「语法 / 参数」节里逐字在**，采信它请读那一节。**这是排版处置，不是删内容。**
> ④ **版本行里的 `forceSTDFTestNam` 少一个 `e`**（两行都这么写，且下一行自己说了是 `Renamed`）——
> **照录**，见「版本」。
> ⑤ **本篇没有坏字。** 实测全文 **0 处非 ASCII 字符**（没有 `鈥` / `渭` / `碌` 那一族）；
> **也没有省略号**（U+2026 与三个 ASCII 点的那种写法各 0 处）。
> **但这是「本页量过的」**，判据是本篇这一个文件；§11.2 ① 那族在别的篇里大量存在。
> ⑥ **wiki 内部的一处过时记载**（**不是 raw 的错，是本 wiki 自己的**）：[[testset]] 那一页写着
> `TESTSET()` 的 33 个子主题**「一篇没读、也都没有页」**——**本页正是其中之一，且已建**。
> **本页只记这件事，不去改那一页**（那一页的 raw 本页没读）。

`verified: doc-only`——**本页没有在任何真实机台上设过一个 test name**
（§11：文档里有 ≠ 这台机器上能用；尤其 `forceSTDFTestName` 两种取值的实际输出、
以及 `hidden_datalog_mode = 0` 时那句 `not supported` 的真实表现，
**文档没写全，动手前先照实机核对**）。
