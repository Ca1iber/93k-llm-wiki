---
type: object
title: FW_TASK
layer: L2
stage: testmethod
tags: [testmethod, l2, fw-task, firmware-command, extension, fw-resultdata, mcd, break]
related: [begin-extension, end-extension, command-reference, testmethod, report-window, smartest-7.1.0]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.77_FW_TASK.md
created: 2026-09-21
updated: 2026-09-21
verified: doc-only
---

# FW_TASK

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **4,932 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.77_FW_TASK.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

For setting:

```
FWTASK_STATUS FW_TASK(const STRING& command);
```

For query:

```
FWTASK_STATUS FW_TASK(const STRING& command, STRING& answer);
```

To retrieve binary data:

```
FWTASK_STATUS FW_TASK(const STRING& command, FW_ResultData & resultdata);

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/29362.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：4 行 × 3 列。
```

  Parameters

 | I/O  | Parameter  | Description |
 | I  | command |

Command string with one or more commands. Each string can be limited by a newline (\n) or a semicolon.

Multiple FW commands, delimited with a newline (\n) or a semicolon, can be combined in the command string.

 |
 | O  | answer  | Answer string as the response to the firmware command. Its maximum length is 1 MB. If the answer string exceeds the limit of the length, a system error will occur. |
 | O  | resultdata |

A reference to an existing object of type FW_ResultData. The function fills this object with the retrieved data.

The FW_ResultData object provides the following parameters:

| Parameter | Type | Description |
|---|---|---|
| Answer | String | The FW answer string without the binary data part |
| BinaryDataLength | unsigned int | The data length |
| BinaryData | char* | The data string |

See also `Example 3: Retrieve DPS current measurement results`（raw: `02.07.04.01.77_FW_TASK.md#_29362__ex_retrive_binary_data`） below.

   |  Return value The following enumerators of type FWTASK_STATUS are returned:

- FW_PASSED: The firmware commands are successfully executed.
- FW_WARNING: A warning has been generated from execution of the firmware commands. The `Message Concentrator and Distributor (MCD)`（raw: `../02.06_Command_Reference/02.06.01.01_V93000_Firmware_Overview.md#_10402__p_MCD`） generates the warning and it is output to the report window. You may have to confirm the contents of the warning and modify the test method program.
- FW_BREAK: If the break has occurred during the firmware execution, this is returned. When you press the Break button in the SmarTest Main Menu, the break signal is sent to the MCD and the digital sequencer is changed to the BRK state. The system hardware operation stops and the digital channels continue to output the break vectors. Then, control returns to the test method and program execution will be continued. If the firmware execution fails for reasons not mentioned above, an error will occur. For details, see the `Command Reference`（raw: `../02.06_Command_Reference/02.06_Command_Reference.md`） Manual. When an error occurs, the test method execution aborts. In other words, program execution terminates at this point. Note that two kinds of error message are output to the report window. One is the error message generated from the test method if error messages have been activated by the `ENABLE_ERROR_MESSAGE`（raw: `02.07.04.01.58_ENABLE_ERROR_MESSAGE.md`） API. The other is the message generated from the MCD.

### Example 1: Execute setting command

```
FW_TASK("UTOT 1, 65535, 12345\n");
```

This API sets output lines URW15, 14, UW13 to 7 and URW06 to 00, to 53190 (inverted value of 12345) at the firmware level. Note that you need to terminate the command string with "\n" (newline) or ";"(semicolon) even if the only single command string is used.

### Example 2: Execute querying command

```
STRING answer;

if (FW_TASK("DFPS?(@)\n", answer) == FW_PASSED)
{
// continue the processing ....
}
```

If the firmware command DFPS? is executed successfully and the FW_TASK returns FW_PASSED, the statements in the "if" block are executed.

### Example 3: Retrieve DPS current measurement results

```
FW_ResultData data;

FW_TASK("DPSE 1,(dps1),#150,1,2");
FW_TASK("PSST ON");
FW_TASK("PSEE 1,,,(dps1)");
FW_TASK("PSER? 1,pval", data);

cout << "Answer: " << data.Answer << endl;
cout << "BinaryData: " << endl;

for ( unsigned int i = 0; i < data.BinaryDataLength; i++ )
{
cout << data.BinaryData[i];
}
```

To retrieve the binary data, the API executes the DPSE, PSST, and PSEE commands followed by the PSER? query. The result contains the properties of the retrieved data.

### Example 4: Enable the trace function / MCDLog

The following code enables and disables the `trace function`（raw: `../02.06_Command_Reference/02.06.01.03.05_Using_the_Trace_Function.md`） using the `DIAG`（raw: `../02.06_Command_Reference/02.06.02.02.74_DIAG_-__DIAGnostics.md`） command and writes some annotations to the MCDLog file using the `NOOP`（raw: `../02.06_Command_Reference/02.06.02.02.169_NOOP__NOOP__-__NO_OPeration.md`） command.

```
string testSuiteName;

GET_TESTSUITE_NAME(testSuiteName);

//
// Open the MCDLog, write the first annotation
//
FW_TASK("DIAG 2");

FW_TASK("NOOP \"##########\",\"" + testSuiteName + "\",\"Start\",");

//
// Execute tests and write some annotations
//
...
...
FW_TASK("NOOP \"##########\",\"" + testSuiteName + "\",\"Step\",1");
...
...
FW_TASK("NOOP \"##########\",\"" + testSuiteName + "\",\"Step\",2");
...
...
//
// Close the MCDLog
//
FW_TASK("DIAG -2");
```

Note: You must use a backslash "\" as escape character to insert strings that are enclosed in quotation marks into the command string.

<!-- 语法节 end -->

## 是什么

**一句话：FW_TASK 是 L2 那条「从测试方法直接对硬件说固件命令」的口子。**
原文第一句就是它的定义：

> 「This API allows direct access from the test method to the system hardware at firmware level.」

**两个词要抠准**：`direct`（**不经过 L1 的大多数包装**）与 `at firmware level`
（**说出去的是固件命令，不是 GUI 动作**）。
**所以它的用法不是「调一个功能」，而是「把命令串塞进去」**——
本页后面的东西全是围着那根命令串转的。

**它声明在这个头文件里**（原文给了绝对路径）：

> 「This API is defined in the header file `/opt/hp93000/soc/prod_com/include/MAPI/Extension.h`.」

### 为什么要有它：原文 `## Application note` 三条

| # | 原文（逐字） | 读出来的事 |
|---|---|---|
| 1 | `Sometimes several firmware commands must be used in the test method program. If so, this API provides the environment where you can execute one or more firmware commands when necessary.` | **它存在的理由是「一次要用好几条固件命令」**——**`one or more`，一条也行** |
| 2 | `BEGIN_EXTENSION and END_EXTENSION APIs are always used together with the FW_TASK function.` | **它俩不是可选的搭档**——原文用的是 `always` |
| 3 | `Beside the firmware command, you can also execute the functions that you have originally created between BEGIN_EXTENSION and END_EXTENSION APIs.` | **在那对括号里，除了固件命令，还能跑自己写的函数** |

> **第 2 条是硬话**（`always`），**但它说的是「那对 API 与 FW_TASK 一起用」，
> 不是「FW_TASK 只能写在那一对里面」**——
> **原文没有说「FW_TASK 必须包在 BEGIN_EXTENSION / END_EXTENSION 里」这句**。
> **本页不做这个加强**（§11：全称否定/加强句的举证责任在写的人）。
> 第 3 条只是说「那里面还能干别的」。

### 三个重载 = 三种用途

本页「语法 / 参数」节列了**三个** `FW_TASK`：

| 用途（原文的引导词） | 签名 | 多出来的东西 |
|---|---|---|
| **For setting** | `FWTASK_STATUS FW_TASK(const STRING& command);` | — |
| **For query** | `FWTASK_STATUS FW_TASK(const STRING& command, STRING& answer);` | 一个 `STRING& answer` 接回答 |
| **To retrieve binary data** | `FWTASK_STATUS FW_TASK(const STRING& command, FW_ResultData & resultdata);` | 一个 `FW_ResultData&` 接**二进制**数据 |

**选择规则一句话：只下命令用第一个；要读回字符串用第二个；要读回二进制数据用第三个。**

> **（推断）第三个重载是 SmarTest 7.1.0 才有的。**
> **依据有两条，都在本篇里**：① `## Functional changes` 写着
> `SmarTest 7.1.0: New class: FW_ResultData`；
> ② 第三个重载的参数类型正是 `FW_ResultData`。
> **类是 7.1.0 才加进来的，那么用这个类的重载不可能早于 7.1.0**。
> —— **原文没有直接这么说，所以这是推断，不是文档事实。**

### 命令串的三条硬规矩

**① 必须以 `\n` 或 `;` 结尾——哪怕只有一条命令。** 这是最容易漏的一条，原文专门点了：

> 「Note that you need to terminate the command string with `"\n"` (newline) or `";"`(semicolon)
> even if the only single command string is used.」

**② 多条命令可以合成一个串，分隔符同样是 `\n` 或 `;`**：

> 「Multiple FW commands, delimited with a newline (\n) or a semicolon, can be combined
> in the command string.」

**③ 要在串里插带引号的字符串，得用反斜杠转义**：

> 「Note: You must use a backslash `"\"` as escape character to insert strings that are
> enclosed in quotation marks into the command string.」

**这三条合起来说明一件事：`command` 那一栏收的是「一整段固件脚本」，不是「一个命令名」。**
（**推断**；依据是原文 `command` 那一栏的说明：
`Command string with one or more commands.`。）

### 返回值 `FWTASK_STATUS`：三个枚举，**难度不一样**

原文 `## Return value` 给三个。**它们不是「三种同等的结果」，后两个要动脑子：**

| 枚举 | 原文说什么 | 你该怎么办 |
|---|---|---|
| **`FW_PASSED`** | `The firmware commands are successfully executed.` | 正常 |
| **`FW_WARNING`** | `A warning has been generated from execution of the firmware commands.` —— 由 **MCD** 生成、**输出到 report window** | 原文：`You may have to confirm the contents of the warning and modify the test method program.` **即要去看、可能要改程序** |
| **`FW_BREAK`** | `If the break has occurred during the firmware execution, this is returned.` | **这是一条完整的机制描述**，见下 |

**`FW_BREAK` 那一条是整篇最长的一句，它讲的是「按了 Break 按钮之后会发生什么」：**

> 「When you press the Break button in the SmarTest Main Menu, the break signal is sent to the
> MCD and the digital sequencer is changed to the BRK state. The system hardware operation stops
> and the digital channels continue to output the break vectors. Then, control returns to the
> test method and program execution will be continued.」

**拆成四步**：**按 Break → 信号送 MCD、数字 sequencer 进 `BRK` 状态 → 硬件停、但数字通道继续输出 break vectors → 控制权回到测试方法，程序继续跑。**
**注意最后一步：`will be continued`——break 不是中止，是暂停后继续。**

**同一条里还有一段「不是 break 的失败怎么办」**，这段比 break 本身更要紧：

> 「If the firmware execution fails for reasons not mentioned above, an error will occur.
> For details, see the Command Reference Manual.」

**中间这一句原文是指向 Command Reference 的**（这一步本页没读那篇），**后面接着说的是：**

> 「When an error occurs, the test method execution aborts. In other words, program execution
> terminates at this point.」

**即：break 之外的失败是 error，而且 `the test method execution aborts`（程序在这里终止）。**
原文还说这时 report window 会有**两条**错误消息：

> 「Note that two kinds of error message are output to the report window. One is the error message
> generated from the test method if error messages have been activated by the
> `ENABLE_ERROR_MESSAGE` API. The other is the message generated from the MCD.」

**这里有个前提容易读漏**：来自测试方法的那一条**要先由 `ENABLE_ERROR_MESSAGE` 打开**才会出现。

### 两个出参各自的边界

| 出参 | 边界（原文） |
|---|---|
| **`answer`** | `Its maximum length is **1 MB**. If the answer string exceeds the limit of the length, **a system error will occur**.` |
| **`resultdata`** | `A reference to an existing object of type FW_ResultData. The function fills this object with the retrieved data.` |

**`answer` 那条是硬上限**：**超过 1 MB 不是截断，是 `a system error`**。
**`resultdata` 那条的要点是「你必须先有一个对象」**——原文用的是
`A reference to an **existing** object`，而且原文的例子是先 `FW_ResultData data;` 再传进去。

**`FW_ResultData` 里有什么（原文那张表，三个字段）：**

| Parameter | Type | Description |
|---|---|---|
| `Answer` | `String` | `The FW answer string without the binary data part` |
| `BinaryDataLength` | `unsigned int` | `The data length` |
| `BinaryData` | `char*` | `The data string` |

**注意第一行**：`Answer` 是**去掉二进制段之后的**回答串——
**即二进制那份数据不在这三个字段里重复，它在 `BinaryData`。**

## 典型用法

**原文 `## Examples` 给了四个例子，它们是四种不同的用法，不是四个变体。**

### Example 1 — 只下命令（setting）

```cpp
FW_TASK("UTOT 1, 65535, 12345\n");
```

原文对它的解释是：

> 「This API sets output lines URW15, 14, UW13 to 7 and URW06 to 00, to 53190
> (inverted value of 12345) at the firmware level.」

**这个例子的价值在 `\n`**：命令只有一条，**结尾那个 `\n` 依然是必须的**
（原文在同一句里就点了这件事）。

### Example 2 — 读回字符串（query）

```cpp
STRING answer;

if (FW_TASK("DFPS?(@)\n", answer) == FW_PASSED)
{
// continue the processing ....
}
```

原文的说明：

> 「If the firmware command DFPS? is executed successfully and the FW_TASK returns FW_PASSED,
> the statements in the "if" block are executed.」

**这个例子给的是标准姿势：用 `== FW_PASSED` 判，再往下走。**
**注意它用的是查询命令（`DFPS?`，问号结尾）配第二个重载。**

### Example 3 — 读二进制（retrieve binary data）

```cpp
FW_ResultData data;

FW_TASK("DPSE 1,(dps1),#150,1,2");
FW_TASK("PSST ON");
FW_TASK("PSEE 1,,,(dps1)");
FW_TASK("PSER? 1,pval", data);

cout << "Answer: " << data.Answer << endl;
cout << "BinaryData: " << endl;

for ( unsigned int i = 0; i < data.BinaryDataLength; i++ )
{
cout << data.BinaryData[i];
}
```

原文的说明：

> 「To retrieve the binary data, the API executes the DPSE, PSST, and PSEE commands followed by
> the PSER? query. The result contains the properties of the retrieved data.」

**这个例子里有三件值得抄下来的事**：
① **前三条命令是准备工作，最后一条 `PSER?` 才是取数**，**只有它带 `data`**；
② **前三条命令（`DPSE` / `PSST ON` / `PSEE`）都没有 `\n` 结尾**
—— 和 Example 1 「必须加 `\n`」的说法**不一致**（见「出处」的 ⚠️）；
③ **读二进制是循环 `BinaryDataLength` 次、逐字节取 `BinaryData[i]`**，
**不是当成一个字符串读**。

### Example 4 — 用固件命令开日志（trace / MCDLog）

这一例用 **`DIAG`** 命令开关 **trace function**，用 **`NOOP`** 命令往 **MCDLog** 里写标注：

```cpp
string testSuiteName;

GET_TESTSUITE_NAME(testSuiteName);

//
// Open the MCDLog, write the first annotation
//
FW_TASK("DIAG 2");

FW_TASK("NOOP \"##########\",\"" + testSuiteName + "\",\"Start\",");

//
// Execute tests and write some annotations
//
...
...
FW_TASK("NOOP \"##########\",\"" + testSuiteName + "\",\"Step\",1");
...
...
FW_TASK("NOOP \"##########\",\"" + testSuiteName + "\",\"Step\",2");
...
...
//
// Close the MCDLog
//
FW_TASK("DIAG -2");
```

**这一例的看点不是命令，是 C++ 字符串的拼法**：**整条固件命令是用 `+` 拼出来的**，
`testSuiteName` 作为一个变量**拼进了命令串中间**，
**而串里每个双引号都写成 `\"`**——这正是上面第 ③ 条规矩的实例。
**它给的用法是「用固件命令给日志打标注」**（`Start` / `Step 1` / `Step 2` 三个标注，
`DIAG 2` 开、`DIAG -2` 关）。

### 起步该按什么顺序

**原文没有 `## Procedure` 段**，但四个例子合起来给出一个可抄的顺序：

1. **确定这一趟要干几件事**——只下命令、要读字符串、还是要读二进制（**决定用哪个重载**）。
2. **把固件命令写成串**，**每条都以 `\n` 或 `;` 结尾**；
   多条合成一个串时，**分隔符也是 `\n` 或 `;`**。
3. **串里有引号字符串就转义成 `\"`**（Example 4）。
4. **判返回值**：`FW_PASSED` 往下走；`FW_WARNING` 去看 report window；
   **`FW_BREAK` 是暂停后继续；其它 error 会直接把测试方法执行中止**。
5. **用 `BEGIN_EXTENSION` / `END_EXTENSION` 把这一段圈起来**（原文说它们
   `always used together with the FW_TASK function`）。

## 和谁有关

- [[begin-extension]] / [[end-extension]] — **原文点名的固定搭档**：
  `BEGIN_EXTENSION and END_EXTENSION APIs are always used together with the FW_TASK function.`
  **一对 API，要一起用**；而且原文说在它俩之间**还能跑自己写的函数**。
- [[command-reference]] — **命令本身不在本页**。
  本页只讲「怎么把命令送出去、怎么收结果」；
  **具体有哪些固件命令、每条什么参数，在 Command Reference**。
  原文还在 `FW_BREAK` 那一条里把 error 的细节指了过去（`For details, see the Command Reference Manual.`）。
- [[dfps]] — **Example 2 里 `FW_TASK("DFPS?(@)\n", answer)` 用的就是它**。
  **注意这一处的关系是「命令被 FW_TASK 包着送出去」**，
  **不是「FW_TASK 属于 DFPS」**——方向别搞反。
- [[report-window]] — **`FW_WARNING` 和 error 的落点**：
  原文两次说消息输出到 report window（warning 由 MCD 生成；error 有两条，一条来自测试方法、一条来自 MCD）。
- [[testmethod]] — **stage 归属**。frontmatter 的 `stage: testmethod` 是**「最近的一段」**，
  不是「归属」——FW_TASK 是写在测试方法里的 L2 API。
- [[test-method-class]] — **它被写进去的那个壳**：
  本页四个例子的代码都出现在测试方法代码里（原文的例子本身不给类名，但 API 属于这一族）。
- [[smartest-7.1.0]] — **`FW_ResultData` 的引入版本页**：
  第三个重载靠的就是这个类（见「是什么」里那条推断）。
- **原文 `## Related information` 另外两篇**（**均未读**）：
  `DIAG - (DIAGnostics)`、`NOOP, NOOP? - (NO OPeration)`——
  **Example 4 用的就是这两条命令，但本页不解释它们。**
- `Message Concentrator and Distributor (MCD)`（`02.06.01.01` 的锚点，**未读**）——
  warning 的生成者、error 消息的来源之一。
- `ENABLE_ERROR_MESSAGE`（`02.07.04.01.58`，**未读**）——
  **来自测试方法的那条 error 消息要先靠它打开**。
- `FW_ResultData`（**没有单独页**）—— 第三个重载的出参类型；
  三个字段见上面那张表，**但它的完整定义本页没有**。
- `GET_TESTSUITE_NAME`（**没有单独页**）—— Example 4 里用来取名称的那个函数。

> 上面每一条都来自本页读的那一篇 raw。**本页没有查 `edges.jsonl`，也没有从别的文档补事实。**

## 版本

本篇 `## Functional changes` **两条**：

- **`Introduced before SmarTest 6.3.2`**
- **SmarTest 7.1.0**：`New class: FW_ResultData`

**读法（两条，第二条是这一页独有的）：**

1. **第一条是哨兵值，不许读成「6.3.2 新增了 FW_TASK」。**
   按 §11.2 ②：`Introduced before SmarTest 6.3.2` 的意思是
   **「在本文档集覆盖范围开始之前就已经有了」**——
   **所以本页能说的只有「FW_TASK 很早就有」。具体哪一版起有，本篇答不了。**
2. **`SmarTest 7.1.0: New class: FW_ResultData` 这一条虽然只提了一个类，
   但它管到了 FW_TASK 的一个重载**——**第三个重载（`FW_ResultData & resultdata`）
   不可能早于 7.1.0**（**推断**，依据见「是什么」）。
   **也就是说：在 7.1.0 之前的版本上，`FW_TASK` 只有前两个重载。**

## 出处

`sources:` 一篇：
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.77_FW_TASK.md`

**本页没做的**：

- **`## Related information` 的四篇一篇没读**：`BEGIN_EXTENSION`、`END_EXTENSION`、
  `Command Reference`、`DIAG - (DIAGnostics)`、`NOOP, NOOP? - (NO OPeration)`
  （**其实是五篇，原文那一行也是挤在一起的**）。
  **所以「BEGIN_EXTENSION / END_EXTENSION 怎么用」「有哪些固件命令」「DIAG / NOOP 的语法」，
  本页一个字都没有**——本页只有原文那一句「它俩总是和 FW_TASK 一起用」。
- **正文里链出去、但本页没读的**：`Message Concentrator and Distributor (MCD)`
  （`02.06.01.01` 的锚点）、`ENABLE_ERROR_MESSAGE`（`02.07.04.01.58`）、
  `Using the Trace Function`（`02.06.01.03.05`）。
  **所以「MCD 是什么」「怎么打开错误消息」「trace function / MCDLog 是什么」，
  本页都没有依据。**
- **一张图没看**——**本篇 raw 里本来就没有图**（整篇 155 行，无 `![` 引用）。
- **`FW_ResultData` 那一篇没读**（**原文里也没有链到它的专页**）——
  **所以这第三个重载的出参有没有别的方法、要不要释放，本页不知道。**
- **⚠️ 本页刻意不挂另一篇同名文档**：语料里另有一篇讲 **`FW_TASK type`** 的文档
  （`02.08.04.32.02.06.01.05`），**它讲的是另一个东西（一个 GUI 对话框）**。
  **本页没有读它，也不对它声称任何事**；`sources:` 里只有上面那一条。
- **`## Syntax` 的「Parameters」表在原文里是压平的**（每个单元格独占一行、夹空行），
  **本页「语法 / 参数」节按脚本原样保留**——**本页正文没有重排它**，
  只在上面用散文把三个出参各说了一遍。
- **本页 `verified: doc-only`**：**没有在任何真实 93K 上跑过这些例子**——
  §11：文档里有 ≠ 你这台能用。**`FW_TASK` 是直通固件层的，动手前先想清楚。**

> ⚠️ **本篇的语料瑕疵，照实记录，一处都没替它改**：
> ① **锚点里有一处拼写错**：正文写 `See also Example 3: Retrieve DPS current measurement results`
>    （原文里这一串是**链接文字**），而它指过去的锚点写的是 **`#_29362__ex_retrive_binary_data`** ——
>    **`retrive` 应为 `retrieve`**（同一句的可见文字里拼的是 `Retrieve`）。
>    **这是链接目标里的字，读者看不见，但抄锚点会抄到错的。**
> ② **`## Parameters` 那张表被压平了**（同 §11.2 那一类）：
>    raw 里是**每个单元格独占一行、行与行之间夹空行**，例如
>    ` | I  | command |` 之后**空行、再接一长段散文、再接一个孤立的 ` |`**。
>    **结果是 `command` 和 `resultdata` 的说明落在表外的散文里。**
>    本页正文是按语义复述的，**逐字的那份在本页「语法 / 参数」节里**。
> ③ **`## Return value` 那一行也是黏的**：raw 里写成
>    `|  Return value The following enumerators of type FWTASK_STATUS are returned:` ——
>    **表头单元和下面的散文黏在同一个管道行里**。
> ④ **同一句里标点不齐**：`terminate the command string with "\n" (newline) or ";"(semicolon)`
>    —— **`"\n"` 与 `(newline)` 之间有空格，`";"` 与 `(semicolon)` 之间没有**
>    （`Example 1` 之外，`command` 那一栏的说明里是 `a newline (\n) or a semicolon`，又是一种写法）。
>    同一句末尾的 **`even if the only single command string is used`** 也不顺
>    （`the only single` 叠了两个限定词）。**原文如此。**
> ⑤ **Example 1 的说明句三个 `to` 并列，读起来含混**：
>    `sets output lines URW15, 14, UW13 to 7 and URW06 to 00, to 53190 (inverted value of 12345)`
>    —— **`to 53190` 那一截挂在哪一段上，句子本身没说清。原文如此，本页不替它解析。**
> ⑥ **Example 3 与 Example 1 的规矩不一致**：Example 1 明确说
>    `you need to terminate the command string with "\n" (newline) or ";"(semicolon) even if the only single command string is used`，
>    而 **Example 3 里的 `FW_TASK("DPSE 1,(dps1),#150,1,2")` / `FW_TASK("PSST ON")` /
>    `FW_TASK("PSEE 1,,,(dps1)")` 三条都没有 `\n` 或 `;` 结尾**。
>    **本页不替它调和**——**两种可能（例子省了、或规矩不普适）本页都不断言**。
> ⑦ **`## Related information` 的五条链接之间没有分隔符**，在 raw 里是连着的一串
>    （**本页只引头三串为止，后面的同样形状**）：
>    `](<02.07.04.01.10_BEGIN_EXTENSION.md>)[END_EXTENSION](<02.07.04.01.59_END_EXTENSION.md>)[Command Reference](<../02.06_Command_Reference/02.06_Command_Reference.md>)`

`verified: doc-only`
