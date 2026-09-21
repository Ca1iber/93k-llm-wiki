---
type: error
title: 报 "Data Queue Empty"
tags: [error, memory-test, pattern, compiler, vector-memory]
related: [[pattern]], [[smartest-6.3.2]]
sources:
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.05.02.01_Data_Queue_Empty_error.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# 报 "Data Queue Empty"

## 症状

**`Data Queue Empty` 是一条 execution error**（执行期报错，不是编译期）。
文档的定义原句：

> Data Queue Empty is a situation where the per-pin processor runs out of vectors in the queue.

**注意是 per-pin**：报错是**逐个通道**的，所以「哪几个通道报了」本身就是线索。

**报错句原文有一处粘连**（照抄，不修）：

> If the queue for the processor cannot be filled in a timely manner, the Data Queue Empty execution erroroccurs.

`erroroccurs` 中间没有空格——**这是 raw 里的排版缺陷，不是本页打错的**（§11.1：引文里不修排版）。

## 触发条件

**base rate 越高越容易出**：

> The higher the base rate, the greater the risk of Data Queue Empty errors.

**机理**（文档原句）：per-pin processor 的队列要**及时**被填上；
填不上（供数据的速度赶不上消耗）就报这个错。**要传的数据量由 pattern 展开后的体积决定**，
所以真正的旋钮是 **expansion size**。

## 怎么办

**主手段：把 expansion size 调大。** 文档原句：

> Data Queue Empty errors can usually be eliminated by increasing the expansion size. There are two ways of doing so:

**两条路按「错在几个通道上」分**（这一句是原文的两句）：

> This is appropriate in situations where the error is occurring on many pins.

「**多通道**」→ 用 `-e` 编译器设置，或在 GUI 里改 `Expansion Size` 选项。
「**少通道**」→ 用 `exps` 这个 pin 属性（**只对报错的那几个通道调**）。

**为什么调大 expansion size 有用**（文档原句，机理在这里）：

> The expansion size controls the maximum length of loop bodies.

> Larger expansion sizes decrease the risk of Data Queue Empty errors at the expense of requiring more vector memory.

**也就是「拿向量内存换安全性」**——**这是本页最该记住的一句**：
调大不是免费的，**memory pattern 的向量内存会被吃掉**。

**取值范围与建议序列**：

> The expansion size value is proportional to the loop lengths and can range from 60 to 1,000,000.

> We recommend trying the values from this series in turn until you have found a setting that does not produce an error: 100, 250, 500, 1,000, 10,000, 50,000, 100,000, 500,000, 1,000,000.

**注意这不是「越大越好」**：文档给的是**从 100 起逐步往上试**的序列，
**先在小的那头找到不报错的点**——因为调大的代价是向量内存（上面那句）。

**改完必须重编译**：

> Recompile your memory pattern after each change of the expansion size setting.

**怎么知道是哪些通道在报**（文档原句，同一段里的 Note）：

> Note You can find out on which pins the errors occur by noting the affected channels in SmarTest's report window and looking up the corresponding pins in the Pin configuration file.

→ [[report-window]]（悬空目标）。**注意 raw 里 `Note` 和正文是粘在一起的一行**，
本页照抄，不拆。

## 文档没写清的地方

1. **默认的 expansion size 是多少，文档没写。** 只给了范围（60–1,000,000）
   和建议序列的起点（100）。**不知道默认值，就不知道「调大」是从哪儿往上调。**
2. **「多通道」和「少通道」的分界线在哪，文档没给数。** 原文只说
   "many pins" / "only one or a few pins"。**这是本页要提醒的**：
   自动化脚本如果要替人做这个判断，**得自己定一个阈值，那个阈值不在文档里。**
3. **`-e` 和 GUI 的 `Expansion Size` 是不是同一个东西，文档没说。**
   原文是 "or check the Expansion Size option"——**从措辞看是一回事**，
   但**本页不写成文档事实**。

## 版本

> **⚠️ 这一篇的 `## Functional changes` 写的是 `- Introduced before SmarTest 6.3.2`。**

**这是哨兵值，不是版本事实。** §11.2 ②：全库 **2,677 条** `Introduced before SmarTest 6.3.2`
里绝大多数是「比 6.3.2 还早，具体哪版不知道」的占位写法。
**所以本页不写「SmarTest 6.3.2 起有此错」**——文献里没有这句话。
放在这儿是因为**读这一篇的人一定会看到那一行**，得先知道它不可用。

→ [[smartest-6.3.2]]（版本页；**它讲的是 6.3.2 那一版改了什么，不是这一条**）

## 出处

| 说法 | raw |
|---|---|
| 定义、触发条件、两种调法、expansion size 机理与取值序列、重编译要求、`report window` 那句 Note | `02.12.03.05.02.01_Data_Queue_Empty_error.md` |
| 出处指向 | 同上，原文还指了 `02.06.07.01.09_Managing_the_data_queue.md` 与 MTL 编译器两篇（`02.12.03.02.05` / `02.12.03.02.04.01`） |

文档事实，`verified: doc-only`。

## 相关

- [[pattern]]——expansion size 是 pattern 编译期的量；`exps` 是 pattern 侧的 pin 属性。
- [[report-window]]——「哪几个通道在报」只能从这儿读出来（悬空目标，未建）。
- [[smartest-6.3.2]]——**只因为那一行哨兵值而链**，不是因为它讲了这条错。
