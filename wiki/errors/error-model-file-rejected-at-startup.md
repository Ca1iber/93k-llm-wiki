---
type: error
title: 启动 SmarTest 报 model file 错误（四种类型，都会让软件起不来）
tags: [error, startup, model-file, iochannel, parser, feature-dependency, hardware, license]
related: [[model-file]], [[pogocabling-section]], [[error-flexlm-license-codes]], [[project]], [[timing]]
sources:
  - 02_System_reference/02.04_Model_File_and_Licensing/02.04.05.09_Error_handling.md
  - 02_System_reference/02.04_Model_File_and_Licensing/02.04.05.09.01_Model_file_error_messages.md
  - 02_System_reference/02.04_Model_File_and_Licensing/02.04.05.09.01.01_Parser_syntax_error.md
  - 02_System_reference/02.04_Model_File_and_Licensing/02.04.05.09.01.02_Feature_dependency_error.md
  - 02_System_reference/02.04_Model_File_and_Licensing/02.04.05.09.01.03_Hardware_error.md
  - 02_System_reference/02.04_Model_File_and_Licensing/02.04.05.09.01.04_License_number_error.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# 启动 SmarTest 报 model file 错误（四种类型，都会让软件起不来）

## 症状

**没有可搜的报错串**——文档给的是**四种类型**，不是四句话。
共同症状是**软件起不来**（或弹一个 model file 错误窗口）：

> Model file error messages, also called IOCHANNEL error messages, belong to one of four types:

> These error types are explained in the topics of this section, along with the steps to correct the problem.

**四种是**：parser syntax error / feature dependency error / hardware compatibility error /
license number error。**每种的"起不来"长得不一样**，所以下面按类型分开写。

> **⚠️ 但入口不是从报错串找**：文档说这些错误**出现在 report window**，
> 并且**会指名道姓**告诉你哪里不对（`The error message, which will appear in the report
> window, tells you specifically which installed hardware is incompatible with your request.`）
> ——**遇到这类问题，读那个窗口，不要搜报错串。**

## 触发条件与怎么办：四种类型

### 一、parser syntax error —— model file 语法/必填项不对

> A parser syntax error indicates that the model file does not have the correct syntax and mandatory settings.

> If a required feature is not defined in the model file - if the entry is left blank - a parser syntax error message will be displayed and SmarTest will not start.

**「必填项留空」会报这一条**——原文举的例子是：

> Speed is a mandatory feature for example, while differential is an optional feature.

**怎么办**（原文三步）：

> -  Identify the incorrect syntax or undefined parameters in the model file.

> -  Correct the syntax and save the model file.

> -  Restart SmarTest.

> ⚠️ **原文这三行的列表符后面是**两个空格 **（`-  Identify`）**，
> 不是常见的**一个空格**。**本页照抄，不替它统一**——`- ` 算原文的一部分（§11.1）。

### 二、feature dependency error —— model file 里几项参数互相不兼容

> A feature dependency error indicates that parameters shown in the model file are not compatible with each other. If incompatible features are detected, a model file error window will be displayed and SmarTest will not start.

**要查哪几项**，处置步骤里点名了：

> -  Examine the IOCHANNEL parameters in the model file to identify where an inconsistency exists between hardware, speed, memory, and timing bundle parameters.

**原文给了一个具体例子**（这是本类型最有用的信息）：

> Since the same timing bundle configuration must be used for all channels in a model file, a feature dependency error will occur if different timing bundle configurations are entered in the model file.

→ [[timing]]（timing bundle 属于 timing 段）

### 三、hardware error —— 机台里的硬件和 model file 对不上

> A hardware error indicates one of three possible problems:

> - the requested hardware is not present,

> - the wrong hardware is installed, or

> - the model file contains an incorrect hardware description.

**报文会写清是哪一种**：

> - If the hardware is incompatible, the message names the installed hardware versus the requested hardware.

> - If the capabilities or speed are insufficient, the message says how much memory or speed you need.

> - If hardware is missing, the message says which hardware is missing and which hardware needs to be installed.

**⚠️ 这里有条边界，最容易踩**：

> Hardware errors do not apply in offline mode. Offline mode is a simulation mode and accepts all hardware assignments.

> Note that problems may result if you retain hardware settings when transferring from offline mode to online mode. User-defined parameters are accepted automatically in offline mode, but are checked against actual hardware parameters in online mode.

**意思是：离线模式下硬件随便写，都不会报这一条；一旦切到在线模式，同一份 model file 才开始被核对。**
**「离线调通了」不构成「在线也能起」。** 这条和 [[pogocabling-section]] 里
「启动就退出」的第 3、4 条是同一个形状（在线查实际、离线查自己），**但那是 pogo 块密度的检查，
不是硬件检查**——两处分开报，别混。

**怎么办**（原文给三条路 + 一步）：

> -  To correct the hardware error do one of the following:

>   - Change the description in the IOCHANNEL or CARD_CONFIGURATION section of the model file.

>   - Replace the hardware (if the wrong hardware is installed).

>   - Install the correct hardware (if the hardware is missing).

### 四、license number error —— 许可证不够

> A license number error indicates that not enough licenses are available for the requested configuration and capability. The error message displays the number of required, available, and missing licenses.

**四个可能的原因**（原文列的四条）：

> - Licenses have been checked out for use elsewhere.

> - Not enough licenses were purchased for your addressed tests.

> - The license server is not running.

> - A problem with the network connection to the license server.

**⚠️ 后果比"起不来"更绕**：

> When a license number error occurs the license check-out process for that type is canceled. All licenses of that type, for example, all speed licenses, are returned to the server, and the system starts with reduced capabilities.

**「同一类的许可证全部退回、系统降级启动」**——所以现象可能是
**"软件起来了，但能力少了"**，不是"起不来"。**这一条是本页四种里唯一可能不中断启动的。**

**报文长这样**（原文给的样例，本页按 raw 原样转录，含它的表格线）：

```
   License type                | Required |  Acquired  | Missing
-------------------------------+----------+------------+------------
 Digital_E7945_0_50Mbps        |    32    |   14(  7)  |   18
 Digital_E7945_50_100Mbps      |    32    |   14(  7)  |   18
 Digital_Shared_mem_32_64MB    |    32    |   14(  0)  |   18
```

**括号里的数字是什么**：

> The figure inside the brackets, in the Acquired column, indicate the licenses acquired through device specific licensing. If [Device specific licensing](<02.04.05.08_Device_specific_licensing.md>) (DSL) is not enabled, only the first figure without brackets is shown. The figure in the Missing column indicates the number of missing standard InstaPin licenses.

**怎么办**（原文四条，**每条前面都是 `-  ` 两个空格**，照抄）：

> -  Edit the model license to scale a more limited version of the test, if appropriate. The error message says exactly how many licenses are available for use.

> -  Wait until sufficient licenses are freed up and available from the license server.

> -  Purchase additional licenses to meet the requirements of the current test.

> -  In case of a server or network problem, focus on fixing the hardware or connection problem.

## 这条和「FLEXlm 错误码」不是一回事（**边界**）

**两者都会在许可证上出问题，但观察点完全不同**：

| | 本页（model file · license number error） | [[error-flexlm-license-codes]] |
|---|---|---|
| 谁报的 | **SmarTest 启动时**，对照 model file 的需求算账 | **FLEXlm / FLEXnet 自己**，报一个**负数错误码** |
| 症状 | 起不来，或**降级启动** | 代码 −1…−26，**在许可证服务器/客户端侧** |
| 报文 | **一张 required / acquired / missing 表** | **一个数字码 + 一句英文** |
| 出处 | `02.04.05.09.01.04` | `02.04.06.09.01` |

> **⚠️ 「同一个数字」不要跨页对**：本页的样例里有 `14(  7)` 这种数，
> 而 FLEXlm 的错误码是**负数**（−1、−15…）。**两者不是同一套编号。**
>
> **原文只在一处提到两者的关系**（在 `02.04.05.09_Error_handling.md` 里）——
> 它把 model file 错误和 FlexNet licensing 错误**并列成"运行测试时可能看到的两类错误"**，
> **但没有说两者会不会同时出现、谁先谁后。本次未找到。**

## 文档没写清的地方

1. **四种类型各自的"错误串"一个都没有。** 这篇文档全部在讲**类型和处置**，
   **没有给任何一条可以直接搜的错误文本**——四篇子文档里连一个 `Error:` 开头的句子都没有。
   **本页因此不写"搜索什么"**，只写"看 report window"。
   （**这不是文档缺陷**：报错串大概是动态拼出来的，原文选择不给。）
2. **`## Errors` 段和这四篇的关系文档没说清。** 语料里 431 篇带 `## Errors` 段，
   但**没有任何一篇把这四类错误当成 `## Errors` 的内容**——
   **这两套东西是不是同一件事，本次未找到依据。**
3. **"降级启动"到底降到什么程度，文档只举了 speed licenses。**
   其他类别的许可证（memory、digital…）是不是同样"整类退回"，**文档没写**。
4. **`license number error` 与 `error-flexlm-license-codes` 里的 −15（连不上服务器）**
   在成因上明显重叠（第三条原因就是 `The license server is not running.`），
   **但文档没说这种情况下 SmarTest 报哪一条。本次未找到。**
5. **版本**：这一族六篇的 `## Functional changes` 全部是
   `- Introduced before SmarTest 6.3.2`（**哨兵值，不是版本事实**，§11.2 ②），
   **唯一一条真版本**在 `02.04.05.09.01.04` 里：
   `SmarTest 7.0.1: Report window lists the number of licenses acquired through device specific licensing (DSL)`——
   **也就是说上面那个"括号里的数字"是 7.0.1 起才有的。**

## 出处

| 说法 | raw |
|---|---|
| 四类错误的入口、"运行测试时可能看到的两类错误" | `02.04.05.09_Error_handling.md` |
| 四类的名字、`IOCHANNEL error messages` 这个别称 | `02.04.05.09.01_Model_file_error_messages.md` |
| parser syntax 的定义、留空即报、`Speed` 必填、三步处置 | `02.04.05.09.01.01_Parser_syntax_error.md` |
| feature dependency 的定义、要查的四项、timing bundle 例子、错误窗口 | `02.04.05.09.01.02_Feature_dependency_error.md` |
| hardware 的三种情形、报文会说什么、离线模式不适用、三条处置 | `02.04.05.09.01.03_Hardware_error.md` |
| license number 的定义、四个原因、整类退回、样例表、括号里的数、四条处置 | `02.04.05.09.01.04_License_number_error.md` |

**每篇都还有一节 `## Related information` 指向别的文档**（多为
`02.04.01.01_Editing_the_model_file.md`，**该篇没有 wiki 页**），
本页按 §9.1 写成文件名，不写 wikilink。

**`model-file` 这一页目前不存在**，但它在 `extract/dangling.csv` 里（被 4 处引），
照 §9.1 可以链。文档事实，`verified: doc-only`。

## 相关

- [[error-flexlm-license-codes]]——许可证侧的另一半，**观察点不同，见上面的边界表**。
- [[pogocabling-section]]——**同一个 model file、同样是"启动就退出"**，但是**另一族检查**
  （pogo 块密度/类型/编号），**不在本页四类里**。
- [[model-file]]——本页四类错误全是"这份文件写错了"。
- [[project]]、[[timing]]——`CARD_CONFIGURATION` / timing bundle 这些被点名的对象归它们。
