---
type: object
title: Debug View
layer: gui
stage: run
tags: [debug-view, smatest-work-center, testflow-debugging, breakpoint, step-over, gui]
related: [debug-perspective, setup-perspective, testflow, run, smartest-7.1.0]
sources:
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.08.06_Debug_View.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# Debug View

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **818 字符逐字取自** `<01_Getting_started/01.01_SmarTest_Work_Center/01.01.08.06_Debug_View.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Tables（脚本逐字抽取，第 1 张）

| Icon | Description |
|---|---|
| !`Debug view: Remove terminated testflows`（raw: `../../../../agent-html/125022.png`） | Click to remove all terminated testflows in the Debug view |
| !`Debug view: restart`（raw: `../../../../agent-html/125023.png`） | Click Restart to restart testflow execution |
| !`Debug view: resume`（raw: `../../../../agent-html/125024.png`） | Click Resume to continue testflow execution with no stops unless there are enabled breakpoints in a test method |
| !`Debug view: suspend`（raw: `../../../../agent-html/125025.png`） | Click Suspend to stop testflow execution |
| !`Debug view: terminate`（raw: `../../../../agent-html/125026.png`） | Click Terminate to abort testflow execution |
| !`Debug view: step over`（raw: `../../../../agent-html/125027.png`） | Click Step over to execute exact one (next) test suite in testflow |

<!-- 语法节 end -->

## 是什么

**定义句逐字（本篇正文第 1 句）：**

> 「This view allows you to control the debugging process of a program or testflow.」

**`a program or testflow`——两个对象。** 而这篇文档**只展开了其中一个**：

| 对象 | 本篇怎么处理 |
|---|---|
| **testflow** | **`## Testflow debugging` 一节 + 6 个按钮 + 1 张截图**（本文档的主体） |
| **program**（测试方法，C++） | **`## Test method debugging (C++ debugging)` 只有一句话，指向 Eclipse 自己的帮助** |

**第 2 句讲「挂起时显示什么」**，逐字：

> 「If a class or function is suspended, its stack frames are shown as child elements of the
> program or testflow.」

**即：这个视图是一棵树**——挂起时，**栈帧（stack frames）作为子节点挂在程序 / testflow 底下**。
**（推断）这句话是 `## Test method debugging` 那一半的机制说明**，
**依据是它讲的是 `a class or function`（类 / 函数，是测试方法里的东西），
而下一节 `## Testflow debugging` 讲的是 testflow。原文没有把这句归给哪一节。这是推断。**

**第 3 句讲按钮还有第二个地方能按**，逐字：

> 「You can also use the corresponding debugging buttons on the main toolbar of the Setup
> perspective.」

**⚠️ `also` 这个词很关键**：**这些调试按钮除了在这个视图里，还在 [[setup-perspective]] 的主工具栏上**
——**即「调试按钮在哪儿」这件事有两个答案，本篇两个都给了。**

### `## Testflow debugging`

**这一节只有一句话加一张图加一张表。第一句逐字：**

> 「For testflow execution, SmarTest automatically displays the Debug view.」

**⚠️ `automatically`——跑 testflow 时这个视图是**自己弹出来**的，不用你去开。**
（**本篇没有 `## Procedure` 节，也没有一步手动打开它的说明。**）

**配图**：题注 `Debug view for testflow execution`、文件 `raw/125021.png`。
**本页看过这一张**，图中能看到两样东西：

| 看到的 | 说明 |
|---|---|
| **顶上一排按钮** | 一排调试按钮（**其中若干看着是灰的/不可按的**）；**正文的表只讲了 6 个，而图里不止 6 个**——**多出来的是哪些，本页认不出来** |
| **一棵两层的树** | 根节点逐字读出 `Testflow (Full) [Testflow (Full)]`，**它底下一个子节点叫 `FTest`，图里是选中（蓝色高亮）状态** |

**（推断）树根那个名字是「名字 + `[` 名字 `]`」的重复写法**（`Testflow (Full) [Testflow (Full)]`），
**依据只是图上就是这么写的，以及正文第 2 句说「栈帧显示为子元素」；
`[ ]` 里那一份是什么，本篇没有说。这是推断，本页不引任何原文。**

#### 6 个按钮，逐字

**表格的题注是这一行**（**它就压在表头上，见 `## 出处` ②**），逐字：

> 「Debug view icons for testflow debugging」

**⚠️ 这张表在转 markdown 时被拆散了——一个单元格一行、单元格之间还夹着空行。
所以它没有进上面的「语法 / 参数」节**（原因见 `## 出处` ③）。
**下面这张表是本页按「题注（图的 alt）+ 说明」两列重建的，每个字都逐字来自原文：**

| 图 | 题注（**逐字**，语料如此） | 原文说明（**逐字**） | 本页看图的观察 |
|---|---|---|---|
| `raw/125022.png` | `Debug view: Remove terminated testflows` | `Click to remove all terminated testflows in the Debug view` | 两个叠在一起的深色叉形——**「移除」的意象与说明对得上** |
| `raw/125023.png` | `Debug view: restart` | `Click Restart to restart testflow execution` | 两个黄色环状箭头——**重跑的意象对得上** |
| `raw/125024.png` | `Debug view: resume` | `Click Resume to continue testflow execution with no stops unless there are enabled breakpoints in a test method` | **一个黄色竖条 + 一个绿色三角，「两个字形的并排」**——见下面那条 ⚠️ |
| `raw/125025.png` | `Debug view: suspend` | `Click Suspend to stop testflow execution` | **两个黄色竖条**（经典的「暂停」符号）——对得上 |
| `raw/125026.png` | `Debug view: terminate` | `Click Terminate to abort testflow execution` | **一个红色方块**——对得上 |
| `raw/125027.png` | `Debug view: step over` | `Click Step over to execute exact one (next) test suite in testflow` | **一个黄色弧形箭头 + 左下角一个小蓝块**（经典「步过」符号）——对得上 |

> **⚠️ `resume` 那个图标本页拿不准，照实记下来。** 它的 PNG 里是**两个字形的并排**
> （一个黄色竖条 + 一个绿色三角），而按 Eclipse 那一套惯例，
> **绿三角是「继续/Resume」，黄竖条一族是「暂停/Suspend」**（同表下一行的 `suspend`
> 才是两个黄竖条）。**本页在 `raw/125021.png` 那一排按钮里没能把它单独认出来**，
> **所以不判它是不是题注错位**——**这一条是一个未解决的观察，不是缺陷指控。**
> **⚠️ 别把它和 `hardware-view` 那种「题注整列错位」混为一谈**：那一处有**三行**互相印证，
> 这里只有一行看着别扭。

**这 6 条里有三条是本页认为最要紧的机制**，逐字：

- **`resume` 不是无条件的「继续」**：
  `Click Resume to continue testflow execution with no stops unless there are enabled
  breakpoints in a test method`
  ——**「不停」有一个例外：测试方法里设了断点，它照样停。**
  **即：testflow 的步进调试与 C++ 的断点调试是同一套执行，不是两套。**
- **`step over` 的粒度是「一个 test suite」，不是一行**：
  `Click Step over to execute exact one (next) test suite in testflow`
  ——**⚠️ 原文写的是 `exact one`（应为 `exactly one`），见 `## 出处` ④。**
  **这是本页最该记住的一句**：在 testflow 这一半里，你「单步」一步走的是**一个 test suite**；
  **一行一行地走是 C++ 那一半（Eclipse 调试器）的事**——
  两半的「步」不是同一个单位。**（推断）依据是两节的原文：这一节说 `one (next) test suite`，
  而 `## Test method debugging` 把整件事推给了 Eclipse 的调试器。这是推断。**
- **`suspend` 与 `terminate` 是两件事**：
  `Click Suspend to stop testflow execution`（**停**，可再继续）
  vs `Click Terminate to abort testflow execution`（**中止**）。
  **原文的动词分别是 `stop` 与 `abort`。**

**表格的第一条与其余五条在写法上不一样**，逐字并列：

- 第一条：`Click to remove all terminated testflows in the Debug view`
- 其余五条：**都是「`Click` + 按钮名 + `to` + 动词短语」**——
  `Click Restart to restart testflow execution`、
  `Click Resume to continue testflow execution with no stops unless there are enabled breakpoints
  in a test method`、
  `Click Suspend to stop testflow execution`、
  `Click Terminate to abort testflow execution`、
  `Click Step over to execute exact one (next) test suite in testflow`

**⚠️ 五条都写了按钮名（`Click` + 按钮名 + `to`），只有第一条没写**——
**所以那个按钮叫什么，本篇没有给**（**题注里叫 `Remove terminated testflows`，
但那不是 `Click` + 按钮名 + `to` 那个句式里的名字**）。见 `## 出处` ⑤。

### `## Test method debugging (C++ debugging)`

**这一节整节只有一句话，逐字：**

> 「For details on the Debug view for test method debugging, refer to Help > Help Contents > C/C++ Development User Guide > Reference > Debug views > Debug view.」

**⚠️ 这一句把「测试方法调试」整件事交给了 Eclipse 的帮助**：
路径是 `Help > Help Contents > C/C++ Development User Guide > Reference > Debug views > Debug view`。
**即：同一个叫 `Debug view` 的东西，本篇讲的是 testflow 那一半，
C++ 那一半的正文在 Eclipse 的文档里，不在 TDC 里。**
**这一半本页一个字都没有**（**那一路帮助本页没读，也不在本地语料里**）。

**（推断）所以「这个视图」其实是两个调试器共用一个窗口位**：
testflow 一侧是 SmarTest 自己的（6 个按钮，本篇讲的），
测试方法一侧是 Eclipse CDT 的（`## Test method debugging` 推出去的那一套）。
**依据就是本篇这两节的原文分工，以及第 1 句的 `a program or testflow`。这是推断。**

## 典型用法

**本篇没有 `## Procedure`、没有 `## Before you begin`，没有一个命令行。**
**它是一张「这个视图里有什么按钮」的说明**——
**下面这些是从原文那两节与那张表里落出来的动作。**

| 要做的 | 依据（**原文**） |
|---|---|
| **让调试视图出现** | **不用做**：`For testflow execution, SmarTest automatically displays the Debug view.` |
| **停住 testflow** | `Suspend`——`to stop testflow execution` |
| **接着跑** | `Resume`——`continue testflow execution with no stops unless there are enabled breakpoints in a test method` |
| **走一步** | `Step over`——`execute exact one (next) test suite in testflow`（**一步 = 一个 test suite**） |
| **中止整个 testflow** | `Terminate`——`to abort testflow execution` |
| **重跑** | `Restart`——`to restart testflow execution` |
| **把已经结束的那几个 testflow 从视图里清掉** | 表格第一条那个按钮——`remove all terminated testflows in the Debug view`（**它叫什么名字本篇没给**） |
| **看挂起的地方在哪** | 第 2 句：栈帧 `are shown as child elements of the program or testflow` |
| **在别的地方按同一批按钮** | `on the main toolbar of the Setup perspective`（[[setup-perspective]]） |
| **调试测试方法（C++）** | **本篇不给正文**，只看 `Help > Help Contents > C/C++ Development User Guide > Reference > Debug views > Debug view` |
| **看单步调试的完整流程** | `## Related information` 指向 `Single step testflow debugging`（**那一篇本页没读**） |

**两处本页要提醒的**：

1. **`Resume` 会被测试方法里的断点拦住**——`unless there are enabled breakpoints in a test method`。
   **所以「按了继续就一路跑完」是错的读法**，除非没有断点。
2. **`Step over` 一步一个 test suite**，**不是一行**。
   **一行一行走要去 Eclipse 那一半**（`## Test method debugging`）。

## 和谁有关

- [[debug-perspective]] — **包含它的那个 perspective**。
  **（推断）依据是 [[debug-perspective]] 那一篇的视图清单里有 `Debug` 这一项，
  它给这一项的一句话是 `This view shows the process of the test method executions and debugging.
  You can control the test method execution here.`——
  即那一篇把它写成「**测试方法**执行的调试」，而本篇自己的正文主体是 **testflow** 调试**
  （6 个按钮的表题注就是 `Debug view icons for testflow debugging`）。
  **两篇对同一个视图的定位不一样。本页只把这件事并列出来，不判谁对**——
  **（推断）两种读法都能自圆其说**：一是「这个视图两半都管，两篇各写了一半」，
  二是「其中一篇的说明没有跟上」。**本篇没有一句话能判这件事。原文没有承认也没有否认。这是推断。**
  **（[[debug-perspective]] 那一篇本页读过；它引的 raw 本页没读。）**
- [[setup-perspective]] — **原文逐字点名**：
  `You can also use the corresponding debugging buttons on the main toolbar of the Setup perspective.`
  **即这批调试按钮在这个视图之外还有一处**。**那一篇本页没读**——
  **所以 Setup perspective 的主工具栏上到底有哪几个按钮，本页没有。**
- [[run]] — 本页 `stage: run` 的理由：**它管的是「跑的时候怎么停、怎么走」**。
  **⚠️ 本篇没有 `## Application` 这类自我定位段**，这条归属是本 wiki 的既有划分。
- [[testflow]] — **本页 6 个按钮里有 5 个的宾语都是 `testflow execution`**。
  **（推断）依据就是那 5 句原文（`to restart / continue / stop / abort testflow execution`）
  和 `execute exact one (next) test suite in testflow`。
  本篇没有直接链 [[testflow]] 那一页，两者的关系是本页按原文的宾语给的。这是推断。**
- [[smartest-7.1.0]] — **版本页**。本页 `## 版本` 唯一一条落它。
- `Single step testflow debugging`（**未建、不在 allowlist，故用反引号**）——
  `## Related information` 的**第一个**链接，
  目标是 `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.04.01_Single_step_testflow_debugging.md`。
  **本页没读** —— **所以「怎么一步一步调试 testflow」的完整流程本页一个字都没有。**
- `Help > Help Contents > C/C++ Development User Guide > Reference > Debug views > Debug view`
  （**Eclipse 自己的帮助，不在本地语料里**）——
  **`## Test method debugging` 整节指向它。本页没读、也读不到。**
- `Setup perspective` 的主工具栏（**不是一页，是一处 UI**）——见上面 [[setup-perspective]] 那条。

## 版本

**本文档有 `## Functional changes` 段，只有一条**，逐字：

- **Introduced in SmarTest 7.1.0**

**⚠️ 这一条**不是** §11.2 ② 那个哨兵。**
哨兵写的是 `Introduced before SmarTest 6.3.2`（**`before`**），
而这一条写的是 `Introduced in SmarTest 7.1.0`（**`in` + 另一个版本号**）——
**所以这个视图确实是 SmarTest 7.1.0 引入的**。
**判据是 `in` / `before` 这个词本身**（§11.2 ②），**不需要看别处。**

**（推断）7.1.0 到 wiki 目标版本 7.10.3 之间这个视图改过没有，本篇没有依据**——
**本文档的 `## Functional changes` 只有这一条，再没有第二条。**
**（对照：同一族的 summary tab 那几篇各有 4–5 条，所以「只有一条」是这个视图自己的情况。
这是本页按 wiki 里已有的同族页给的比较，不是本篇说的。这是推断。）**

详见 [[smartest-7.1.0]]。

## 出处

`sources:` 一篇：
`01_Getting_started/01.01_SmarTest_Work_Center/01.01.08.06_Debug_View.md`
（TDC 主题号 `107078`；本地 raw md：**2,049 字节**、**71 行**——
**字节是磁盘上的字节数，行数是换行符个数**。**这是本页读的几篇里最短的一篇。**）

**本页没做的：**

- **七张图，本页七张都看了**：`raw/125021.png`（`## Testflow debugging` 那张，
  **整个视图长什么样**）与 6 张按钮图 `raw/125022.png` – `raw/125027.png`。
  **没有发现 `hardware-view` 那种成列的题注错位/重复**；
  **唯一拿不准的是 `resume` 那一张**（见上面那条 ⚠️）——
  **那是一条未解决的观察，本页没有据此下任何结论。**
- **`## Test method debugging (C++ debugging)` 那一半，本页一个字都没有。**
  原文只有一句话，它指向的 `Help > Help Contents > C/C++ Development User Guide >
  Reference > Debug views > Debug view` **在 Eclipse 帮助里，不在本地语料里**——
  **所以「测试方法怎么单步、断点怎么设、变量怎么看待」本页全无。**
- **`Single step testflow debugging` 没读** ——
  **所以「一步一步调试 testflow」的完整流程本页没有；
  而它是 `## Related information` 的两个链接之一。**
- **[[setup-perspective]] 没读** —— **所以「调试按钮在 Setup perspective 主工具栏上也有一份」那句里，
  主工具栏上到底有哪几个按钮、和这 6 个是不是同一批，本页没有。**
- **[[debug-perspective]] 那一篇的 raw 没读** ——
  **本页与它的关系全部取自 wiki 里那一页已经写好的内容（本页读过那一页 wiki 页），
  没有从对面回校过。**
- **`system` 一侧没有核过**：**本页没有在任何真实 SmarTest 上跑过 testflow 调试，
  也没按过这 6 个按钮里的任何一个**（`verified: doc-only`）。
  **按钮在界面上的位置、灰不灰、有没有快键，全部来自 `raw/125021.png` 那一张图和正文的表。**
- **本文档没有 `## Subtopics` 目录块**（查过：正文里 `Subtopics` 0 处），
  **所以「这一章底下还有什么」本页给不出来。**
- **`layer: gui` / `stage: run` 不是本篇写的**——
  **本篇没有 `## Application` 这类自我定位段**，这个归属是本 wiki 的既有划分。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> **① 本篇没有 `#### Subtopics` 目录块。** 本篇正文第 1 行就是定义句。
> **（这是本批四篇里唯一一篇正文第 1 句就是定义句、而**不是**那种「一段话 + 三部件」模板的。）**
>
> **② 那张 6 行的图标表在转 markdown 时结构坏了——「题注」那一格被当成了表头。**
> 逐字并列（**这几行在原文里是分开的行，之间还夹着空行**）：
> `Debug view icons for testflow debugging` ／ ` |` ／ `Icon` ／ ` |` ／ `Description`
> ——**表格的题注 `Debug view icons for testflow debugging` 与真正的列名 `Icon` / `Description`
> 挤在同一张表里，题注站到了第一个格的位置。**
> **本页照实并列，不替它改。**
>
> **③ 整张表被拆成了「一个单元格一行、之间夹空行」。**
> 逐字（**原文就是这么断行的**）：
> ` |  ![Debug view: Remove terminated testflows](<../../../../raw/125022.png>) |`
> 后面紧跟一个空行，然后是 `Click to remove all terminated testflows in the Debug view`，
> 再一个空行，再一行 ` |`。**6 行 × 3 格全部是这个形态。**
> **⚠️ 后果是本页的「语法 / 参数」节一个字都没收到**——
> **但要说清是哪一条原因**：本篇**没有任何** `Syntax` / `Parameters` / `Example`
> 这类标题段（**这一节的样板话对本篇是准的**，和 summary tab 那几篇不一样），
> **所以「抽不到」本来就会发生**；结构拆散是第二层原因。
> **两个原因都在，本页不把它们混成一个。**
>
> **④ `exact one` 应为 `exactly one`。** 逐字：
> `Click Step over to execute exact one (next) test suite in testflow`
> ——**这是本篇唯一一处明确的语法错误。本页引文照原样。**
>
> **⑤ 6 条说明里只有第一条没写按钮名。** 逐字并列：
> `Click to remove all terminated testflows in the Debug view`
> 与
> `Click Restart to restart testflow execution`
> ——**五条是 `Click` + 按钮名 + `to`，第一条是 `Click to`。**
> **所以第一个按钮叫什么，本篇没给。本页照原样引。**
>
> **⑥ 6 张按钮图的题注大小写不一致。** 逐字并列：
> `Debug view: Remove terminated testflows`（**首字母大写 + 三个词**）
> 与 `Debug view: restart` / `Debug view: resume` / `Debug view: suspend` /
> `Debug view: terminate` / `Debug view: step over`（**全小写、单动词**）。
> ——**六张图出自同一排工具栏，题注只有第一条是另一种写法。本页照实并列，不替它统一。**
>
> **⑦ 本篇自己的标题是 `Debug View`（大写 `V`），而正文里两次写的是 `Debug view`（小写 `v`）。**
> 逐字并列：源文件 frontmatter 的 `title: "Debug View"` 与正文的
> `For testflow execution, SmarTest automatically displays the Debug view.`；
> **另外 `## Test method debugging` 那一句指向的 Eclipse 页面也叫 `Debug view`。**
> **同一个名字三种出现位置，大小写不统一。本页照实并列。**
>
> **⑧ `## Related information` 两个链接粘在一起，中间没有任何分隔符。** 逐字：
> `[Single step testflow debugging](<../../02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.04.01_Single_step_testflow_debugging.md>)[Setup perspective](<01.01.07.02_Setup_perspective.md>)`
> ——**两个 markdown 链接首尾相接，`]` 后面直接是 `[`。**
> **（与 [[table-filter]] 那一篇记的同类毛病同形；本页只记本篇这一处。）**
>
> **⑨ 本篇的六张图题注前缀不统一。** 逐字并列：`Debug view for testflow execution`（**无冒号**）
> 与 `Debug view: restart` 等（**有冒号**）。
> ——**同一篇里 6 处用冒号、1 处不用。本页照实并列。**
>
> **⑩ `## Test method debugging (C++ debugging)` 那一句里的路径是 `>` 拼的**，逐字：
> `refer to Help > Help Contents > C/C++ Development User Guide > Reference > Debug views > Debug view`
> ——**一串 `>` 分隔的菜单层级**（`Debug views` 复数指那一级目录，末尾 `Debug view` 单数指页面）。
> **这一条是记法，不是瑕疵**；列在这里是因为**它里面的 `>` 在本页的引文块里要留心**
> （本页把它放在引文块里照原样引了）。
>
> **⑪ 本篇没有 §11.2 ① 那种编码损坏**（查过：正文里汉字 0 个、`鈥` 0 处、
> U+2026 的省略号 0 处、ASCII 的三个句点 0 处）。

`verified: doc-only`
