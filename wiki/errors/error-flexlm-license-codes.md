---
type: error
title: 许可证侧报 FLEXlm / FLEXnet 负数错误码
tags: [error, license, flexlm, flexnet, license-server, debug-log]
related: [[error-model-file-rejected-at-startup]], [[model-file]], [[project]]
sources:
  - 02_System_reference/02.04_Model_File_and_Licensing/02.04.05.09_Error_handling.md
  - 02_System_reference/02.04_Model_File_and_Licensing/02.04.06.09.01_FLEXlm_license_error_messages.md
  - 02_System_reference/02.04_Model_File_and_Licensing/02.04.06.09.03_Using_the_FLEXlm_debug_log.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# 许可证侧报 FLEXlm / FLEXnet 负数错误码

## 症状

**看到的是一个负数码 + 一句英文**，不是 SmarTest 的报错窗口：

> FLEXlm and FLEXnet provide error messages that can help guide you in diagnosing a problem. Note that FLEXlm and FLEXnet errors with the same numerical code are identical.

**⚠️ 第一句就要记住**：**两个产品名下的同一个数字码是同一件事**——
所以查表时不必管看到的是 `FLEXlm` 还是 `FLEXnet` 的字样。

> **⚠️ 但"是哪个进程报的"文档没说。** 这些码出现在
> **许可证服务器（`lmgrd`）/ 客户端 / 许可证文件**哪一侧，原文没写——
> 它只说 `FLEXlm and FLEXnet provide error messages`。**本页不猜。**

## 常见错误码

> The table below describes some of the more common FLEXlm license error messages. For a complete list, see Appendix E of the FLEXnet Licensing End User Guide.

**下表是转录，不是引文**：raw 里这张表**被摊平成「一格一行」**
（`-1` 一格、说明一格，跨多行），本页按语义重排成表格，**文字逐格照抄，排版是我的**。

| 码 | 说明（原文） |
|---|---|
| −1 | Cannot find license file. |
| −2 | Invalid license file syntax. |
| −3 | No server for this feature. |
| −4 | Licensed number of users already reached. |
| −5 | No such feature exists. |
| −8 | Invalid (inconsistent) license key or signature. The license key/signature and data for the feature do not match. This usually happens when a license file has been altered. |
| −9 | Invalid host. The hostid of this system does not match the hostid specified in the license file. |
| −10 | Feature has expired. |
| −11 | Invalid date format in license file. |
| −13 | No SERVER lines in license file. |
| −14 | Cannot find SERVER host name in network database. The lookup for the host name on the SERVER line in then license file failed. This often happens when the host file, or NIS, or DNS is incorrect. Workaround: Use IP address (for example, 123.456.789.123) instead |
| −15 | Cannot connect to license server. The server (lmgrd) has not been started yet, or the wrong port@host or license file is being used |
| −16 | Cannot read data from license server |
| −18 | License server does not support this feature |
| −21 | Reports FLEXlm license version |
| −26 | Request for more licenses than this feature supports |

**16 个码，编号有缺口**（没有 −6 / −7 / −12 / −17 / −19 / −20 / −22…−25）。
**这不是文档漏了**——它开头就写明是 `some of the more common`，
**完整的表在语料外面**（见下「文档没写清的地方」第 1 条）。

> ⚠️ **`-21` 不是错误。** 它的说明是 `Reports FLEXlm license version`——
> **是"报告版本"，一个信息性输出**，却列在一张标题为
> `FLEXlm License Error Description` 的表里。**本页照录，不替它搬走**：
> **按这张表排查时，看到 −21 不要当成故障。**

> ⚠️ **两处原文瑕疵，本页照抄不修**：
> ① `−14` 里 `on the SERVER line in **then** license file failed`——应为 `the`；
> ② `−14` 的绕过办法给的例子是 `123.456.789.123`——
> **这不是合法 IP**（三个八位组都超过 255）。**本页照录，只提示"这是文档给的例子，不是可用地址"。**

## 怎么办

**⚠️ 这一族和前一类排错页最大的不同：它没有"处置步骤"。**
原文**没有 Procedure 段**，`怎么办` 是**逐码写在说明格里的**——
比如 −9 要你核 hostid、−14 给了换 IP 的 workaround、−15 说先看 `lmgrd` 起没起。

**所以本页不编一套通用步骤。** 按码查上表，表里那句就是该做的方向。

**许可证服务器侧有更细的信息可挖——debug log**：

> In case of problems with the license server, the status and error messages of the FLEXlm debug log will be useful.

> When starting the license server (lmgrd), you can direct any lmgrd text output into a debug log, so you can examine the log if a problem arises. The lmgrd output contains

> - configuration problem messages,

> - daemon software messages, and

> - informational messages.

> These status and error messages will be useful when you need to debug the license server.

**怎么只要某一个 daemon 的**：

> The output of the debug log describes events specific to lmgrd and to the current license vendor daemon. You can capture debug information for a particular license daemon by directing the output into a file you specify

（**上句在 `you specify` 处截断**——原文紧跟一个指向 `lmutil` 的链接；
**本页没有加省略号**，§11.1。）

**debug log 的消息清单在哪**：

> For a listing of possible debug log messages see Appendix G of the FLEXlm End User Guide.

## 和「model file 的 license number error」不是一回事（**边界**）

**两者都和许可证有关，但一个是"启动时算总账"，一个是"运行期报单码"**：

| | 本页（FLEXlm / FLEXnet 错误码） | [[error-model-file-rejected-at-startup]] 的第四类 |
|---|---|---|
| 谁报的 | **FLEXlm / FLEXnet 自己** | **SmarTest 启动时** |
| 长什么样 | **一个负数码**（−1…−26） | **一张 required / acquired / missing 表** |
| 后果 | 按码而定 | 起不来，**或"许可证整类退回、系统降级启动"** |
| 出处 | `02.04.06.09.01`、`02.04.06.09.03` | `02.04.05.09.01.04` |

> **两篇的"交汇点"只有一处**：`02.04.05.09_Error_handling.md` 把
> 「model file 错误」和「FlexNet licensing 错误」**并列成"运行测试时可能看到的两类错误"**。
> **它没有说两者会不会同时出现、谁先谁后。本次未找到。**

## 文档没写清的地方

1. **⚠️ 最要紧的一条：完整错误码表不在语料里。**
   两篇都把人往外面指：「Appendix E」（错误码）与「Appendix G」（debug log 消息），
   指向 **FlexNet Licensing End User Guide**，而这本书**不在 raw 语料中**
   （raw 里只有它所在的**网址和导航路径**）。
   **所以"遇到一个表里没有的码"这个场景，本 wiki 答不了**——只能回那本书。
2. **两篇给的导航路径不一样，且都把 `FLEXlm` 写成 `FLEXIm`**（大写 i）。
   原文两处路径分别是
   `Advantest Home > Service & Support > V93000 SOC/HSM > Licensing > …` 与
   `Advantest Home > Global Services > Product Support > V93000 > V93000 Licensing > …`，
   末尾都写 `FLEXIm License Server Software Downloads and Documents > FLEXlm End Users Guide`——
   **同一本书，两套导航、同一个字母打错**。**本页照录，不替它统一**（这大概说明两篇是不同年代写的）。
3. **这些码是谁打印的、打到哪，文档没写。** 是弹窗、是日志、还是标准错误输出——
   **本次未找到**。**这决定了「怎么去看见它」，而文档只讲了排查。**
4. **`lmutil` 的用法没有 wiki 页**（本页只引了它一句），
   原文的 `02.04.06.10.01_lmutil.md` 存在但**没有页**——按 §9.1 写文件名，不写 wikilink。
5. **版本**：两篇的 `## Functional changes` 都是
   `- Introduced before SmarTest 6.3.2`——**哨兵值，不是版本事实**（§11.2 ②）。
   **⚠️ 而且这里的"没有版本"是合理的**：FLEXlm 是第三方产品，
   **它的错误码不由 SmarTest 版本决定**——原文那句
   `FLEXlm and FLEXnet errors with the same numerical code are identical` 说的是同一个意思。

## 出处

| 说法 | raw |
|---|---|
| "两类错误"的并列入口、model file 错误与 licensing 错误的分野 | `02.04.05.09_Error_handling.md` |
| 同码同义、16 个错误码、`some of the more common`、Appendix E | `02.04.06.09.01_FLEXlm_license_error_messages.md` |
| debug log 的用途、`lmgrd` 输出三类、按 daemon 分文件、Appendix G、导航路径 | `02.04.06.09.03_Using_the_FLEXlm_debug_log.md` |

**同族还有几篇没有 wiki 页**（按 §9.1 写文件名）：
`02.04.06.09.02`（FLEXlm 相关）、`02.04.06.10.01_lmutil.md`、
`02.04.05.08_Device_specific_licensing.md`（DSL，被上一页引到）、
`02.04.13_FlexNet_Embedded_licensing.md`（嵌入式许可，是另一套东西）。

文档事实，`verified: doc-only`。

## 相关

- [[error-model-file-rejected-at-startup]]——第四类 `license number error`，
  **同一个主题的另一侧**，边界见上表。
- [[model-file]]——model file 里写着需要哪些许可证；**这一页还没有，但在 `dangling.csv` 里**。
- [[project]]——许可证与工程绑定，属 `project` 段的范围。
