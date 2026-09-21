---
type: object
title: Hidden upload
layer: L2
stage: testmethod
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.10.04.05_Hidden_upload.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# Hidden upload

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

**没有加标记的语法段。** 定义文档里没有 `Syntax` / `Parameters` / `Example`
这类**段标记**，跟着 `Subtopics` 找一层也没有。
**所以本脚本一个字都不收录**——没有段标记时「哪一段是语法」是猜，而猜就是编（§4）。

<!-- 语法节 end -->

## 是什么

**它不是一条命令、不是一个类，是一个机制。** 原文的定义：

> 「Uploading the packages are done by SmartCalc APIs, which know start and end times of sequencer
> executions. These are required in order to upload data during the currently running test.
> This technique is called hidden upload, as the upload is hidden behind the sequencer execution
> of the next test.」

**要解决的问题**：数据要传给测试系统控制器，但传输本身要花时间。
硬等的写法会把主测试流拖慢。hidden upload 的做法是**把上传塞进「下一个 test 的
sequencer 正在跑」的那段窗口里**——用本来就在跑的时间，不额外等。

**四个环节：**

| 环节 | 谁做 | 原文要点 |
|---|---|---|
| **分包大小** | SmartCalc 自动定 | 依据是**下一个 test 的 sequencer 预计运行时间**，目标是**把这段时间用满 100%** |
| **捆 / 拆** | SmartCalc | 小了就**捆**、大了就**拆**（`bundle smaller or split bigger packages automatically`） |
| **什么时候传** | SMC | `whenever it does not effect the throughput of the main test flow` |
| **装载在哪** | 你 | **upload task 必须是 test method 里 SmartCalc（SMC）段的成员** |

**时间是怎么估出来的**：执行 test flow 的过程中，SmartCalc **每次 test 执行都会自动测量并缓存
sequencer 执行时间**；缓存值**会在同一个 sequencer run 的下一次执行时被动态补偿一次**。
**上传结束后，系统回到默认包大小；如果你指定了 user package size，就回到你指定的那个。**

**预估可以被覆盖**：`SMC_SET_TEST_EXECUTION_TIME()`。
它把下一个 test 的 sequencer 执行时间设成你给的值，**并且控制「预估时间过了、
但 sequencer 还在跑」时上传要不要继续**。原文点名它**在自动算法算不准时用，例如用了
Match Loops 的场合**。

## 典型用法

**1. 前置条件**：upload task 得放进 test method 的 **SMC 段**。不放进去，这套机制与你无关。

**2. 与 Mode context 切换有硬性次序**（原文三条，口气一条比一条强）：

> **Note** Hidden uploads, **controlled and started by `SMC_ARM()`**，
> **must be finished before a Mode context is changed.**

- **test suite 内部换 Mode context**：原文**建议**在切换**之前**调
  `SMC_SYNCHRONIZE_WITHOUT_BINNING()`。
- **跨多个 test suite 换 Mode context**：原文**建议**插一个新的 test suite，
  **这个 test suite 不定义任何 level、timing、pattern 信息**，并给它指派
  **系统预备好的 test method `smartCalc.SMC__SYNCHRONIZE`**。

> **注意三条的强度不一样**：第一条是 **must**，后两条是 **recommend**。
> 本页照原文的口气写，**没有把它们拉平成同一条规则**。

**3. 一条硬件前提**（原文以 `Note` 形式给，中间夹着它在语料里的形式）：

> For FPGA compatibility refer to **service note `E8001-140611A`** when using hidden upload
> with **MBAV8+**

**这条只是「去看那份 service note」**，service note 本身不在语料里，**本页也没有它的内容**。

## 和谁有关

- `SMC_SET_TEST_EXECUTION_TIME()`（**未建**）— 覆盖预估执行时间；本页把它做的事说了，
  **它的语法与参数本页一个字都没有**
- `SMC_ARM()`（**未建**）— 原文说 hidden upload **由它控制并启动**；
  **它怎么启动、什么时候调，本篇没讲**
- `SMC_SYNCHRONIZE_WITHOUT_BINNING()`（**未建**）— test suite 内换 Mode context 前建议调
- [[testmethod]] — 本页 `stage: testmethod` 的理由：装载位置是 test method 的 SMC 段
- [[smartcalc]]（**未建**）— 干这件事的主体
- [[match-loops]]（**未建**）— 原文点名「用了它，自动算法可能算不准」
- [[run]] — 被隐藏在上传背后的那个东西是**下一个 test 的 sequencer 执行**；
  sequencer 与 test flow 的关系在那边

## 版本

- **Introduced in SmarTest 6.5.3**
- **SmarTest 7.2.0**：SMC 的默认行为**改成自动决定优化后的包大小**
  （`Default behavior of SMC changed to automatically determined optimized package sizes.`）
- **SmarTest 7.2.1**：`FPGA compatibility needs to be ensured.`

## 出处

`sources:` 一篇：
`02_System_reference/02.07_Test_Method_Reference/02.07.10.04.05_Hidden_upload.md`

**本页没做的**：

- **`SMC_SET_TEST_EXECUTION_TIME()` / `SMC_ARM()` / `SMC_SYNCHRONIZE_WITHOUT_BINNING()`
  三个 API 的语法、参数、返回值，本页一个字都没有。** 它们在原文里是**链接**，
  各自有独立文档，**本页一篇都没读**。本页只用原文对它们的那一句话。
- **那份 service note `E8001-140611A` 不在语料里**，本页无从读起。
- **`smartCalc.SMC__SYNCHRONIZE` 这个预备 test method 是什么，原文只给了名字**，
  没有内容、没有指向。本页照抄名字，**没有替它解释**。
- **`## 语法 / 参数` 节是空的，这是对的**：本篇是**机制说明**，
  语料里没有 `Syntax` / `Parameters` / `Example` 段标记，
  脚本因此一个字都不收（§4：没有段标记时「哪一段是语法」是猜）。

> ⚠️ **语料形式提示**：本篇正文里有**裸的 ` Note ` 标记**（`...MBAV8+ Note Note` 这种），
> 是 HTML 转换留下的痕迹；还有一条**指向自己的链接**
> （`[Hidden upload](<02.07.10.04.05_Hidden_upload.md>)`，就在讲 Mode context 的那一段里）。
> 用 grep 找原文时按**坏掉的那个形态**找。

`verified: doc-only`
