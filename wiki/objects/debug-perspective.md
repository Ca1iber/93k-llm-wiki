---
type: object
title: Debug perspective
layer: gui
stage: run
tags: [debug-perspective, smatest-work-center, perspective, test-method-debugging, eclipse, breakpoint, gui]
related: [debug-view, setup-perspective, project-explorer-view, test-program-explorer, waveform-view, testflow-properties-view, smartest-6.3.2]
sources:
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.04_Debug_perspective.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# Debug perspective

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

**没有加标记的语法段。** 定义文档里没有 `Syntax` / `Parameters` / `Example`
这类**段标记**，跟着 `Subtopics` 找一层也没有。
**所以本脚本一个字都不收录**——没有段标记时「哪一段是语法」是猜，而猜就是编（§4）。

<!-- 语法节 end -->

## 是什么

**定义句逐字（本篇正文第 1 句）：**

> 「The Debug Perspective contains the views to debug a test method.」

**一句话两件事：**

| # | 原句（**逐字**） | 含义 |
|---|---|---|
| 1 | `contains the views` | **perspective 是「一组视图的摆放」，不是一个功能** |
| 2 | `to debug a test method` | **这一组视图的用途是调试**测试方法**（C++），不是别的** |

**第 2 条是这一页的定位**：**它是 [[debug-view]] 那个视图所在的「工作台摆放」，
而它的用途写明了是 `a test method`。**
（**⚠️ 这里和 [[debug-view]] 那一篇的侧重不一样，见 `## 和谁有关` 里那一条。**）

**第 2 句是「怎么改它」的出口**，逐字：

> 「For more information on available perspectives and how you can customize a perspective,
> see Perspectives.」

**即：还有别的 perspective，而且这一个可以自己改**——
**具体怎么改、还有哪些，本篇推给了 `01.01.07_Perspectives.md`**（**那一篇本页没读**）。

**配图**：题注 `Default Debug Perspective`、文件 `raw/122038.png`。**本页看过这一张。**

### 12 个视图，逐字

**引导句逐字**：

> 「This perspective contains the following views:」

**12 项，逐字**（**加粗的是这一条给的机制**）：

| # | 视图（**逐字**） | 原文的一行说明（**逐字**） |
|---|---|---|
| 1 | `Project Explorer` | `It shows the test method projects and devices in the current workspace. It allows easy navigation to the desired program code. You can create a new test method project and class from this view. You can create a new test method project and class from the view.` |
| 2 | `Test Program Explorer` | `It shows all the device setup tools like Pin Configuration Tool, Level Setup Tool, Pattern Tool etc.` |
| 3 | `Editor` | 见下面单独一段（**三条**） |
| 4 | `Problems` | `This view shows errors or warnings and the locations of them in the list form. If you double-click an error in the list, the cursor moves to the line with the error in the editor.` |
| 5 | `Firmware` | `This view allows entering and executing firmware commands during debugging.` |
| 6 | `Breakpoints` | `This view lists all breakpoints that you set.` |
| 7 | `Console` | `This view shows the output of the execution of your program and enables you to enter input for the program.` |
| 8 | `Error Log` | `It shows all the errors coming from the test system and from the Eclipse plug-ins.` |
| 9 | `Waveform` | `This view shows the contents of an array selected in the editor graphically. You can graphically view the captured wave form or calculated results. You can open the Signal Analyzer tool from here for more analysis if necessary.` |
| 10 | `Variables` | `This view shows values of variables in the executed test method.` |
| 11 | `Debug` | `This view shows the process of the test method executions and debugging. You can control the test method execution here.` |
| 12 | `Properties` | `This view shows the properties of an object that you are highlighting. For example, the location and modified date of a test method project (depending on the context, for examples, see Testflow Properties view or Pattern editor properties view).` |

**11 项在原文里是链接，1 项不是**：
**第 12 项 `Properties` 是唯一一个**没有链接**的**（**其余 11 项都链到各自的视图页**）。
**⚠️ 所以「Properties 那一项有没有自己的页」本篇给不出答案**，见 `## 出处` ③。

**这 12 项里有 3 项是本页认为最要紧的：**

#### ① `Editor` 是这一页的中心：编辑 + 调试同一个窗口

**它的三条逐字：**

> 「This view can have multiple editors. The editors are stacked in the editor tabbed pane and
> individual editors can be activated by clicking the tab for the editor.」

> 「The editor has specialized features for editing and debugging test method programs. Hence,
> you can edit and debug your test method programs in one editor.」

> 「On debugging, this editor operates as the debugger's source viewer. You can set the
> breakpoints in this editor and debug your test application with the Console, Variables,
> Expressions, Breakpoints, and Waveform views quickly and efficiently.」

**三条各说一件事**：

| 条 | 机制 |
|---|---|
| 1 | **可以有多个 editor，叠在同一排标签里**，点标签切换 |
| 2 | **一个窗口里既能改也能调**（`edit and debug your test method programs in one editor`） |
| 3 | **调试时这个 editor 就变成调试器的源码窗口**（`the debugger's source viewer`），断点在这里设 |

> **⚠️ 第三条里点名的五个视图，有一个不在上面的 12 项清单里。** 逐字：
> `debug your test application with the Console, Variables, Expressions, Breakpoints, and
> Waveform views`
> —— **`Console` / `Variables` / `Breakpoints` / `Waveform` 四个都在清单里**（第 7、10、6、9 项），
> **而 `Expressions` 不在这篇列出的 12 项里**（清单里没有它，`## Related information` 也没有）。
> **本页照实并列，不替它补也不替它删。见 `## 出处` ②。**

> **⚠️ 同一句里的 `test application` 是全篇唯一一次。** 逐字并列：
> 这一句写 `debug your test application`，而本篇别处一律写 `test method`
> （第 1 句 `to debug a test method`、`test method projects` ×2、`test method programs` ×2、
> `test method` ×2）。**同一个东西两个词，只在这一句换了。见 `## 出处` ④。**

#### ② `Firmware`：调试期间能敲固件命令

逐字：

> 「This view allows entering and executing firmware commands during debugging.」

**即：这个 perspective 里有一个能**直接在调试期间敲固件命令**的视图**——
**它和 [[debug-view]] 那是两件事**（一个是命令入口，一个是执行控制）。
**⚠️ 固件命令有哪些、怎么敲，本篇一个字都没有。**

#### ③ `Error Log` 和 `Problems` 不是一回事

| 视图 | 逐字说明里的**来源** |
|---|---|
| `Problems` | `errors or warnings and the locations of them`——**来源没写**，但双击会跳到 editor 里那一行 |
| `Error Log` | `all the errors coming from the test system and from the Eclipse plug-ins.`——**来源写明了：测试系统 + Eclipse 插件** |

**两者的分工本篇没有直接对比**，但 `Error Log` 那一句**把来源限定成了两类**
（`the test system` 与 `the Eclipse plug-ins`），这是本篇唯一一处交代「错误从哪来」。
**（推断）依据就是这一句里的 `from the test system and from the Eclipse plug-ins` 这个两来源句式，
以及 `Problems` 那一句完全不提来源。这是推断。**

### 图里看到的（`Default Debug Perspective` 那张）

**本页看过 `raw/122038.png`**（§11.4：raw 里的图该读）。图上能看到：

| 看到的 | 说明 |
|---|---|
| **布局：四块** | 左列上下两块、中间 editor（标签 `Test_set.cpp`）、右列上下两块、右下角一块 |
| **左列上：标签被界面截成 `Project Expl` 与 `Test Progra`** | **两个视图叠在同一排标签里**——**正好对上前 2 项**；树里是 `training (current device)` 及 `training.xml` / `Binaries` / `Includes` / `Debug` / `Dps_constant.cpp` / `Error_map.cpp` / `mapi.hpp` |
| **中间：`Test_set.cpp`** | 一个 C++ 测试方法类的源码，能看到 `#include "mapi.hpp"`、`class Test_set : public testmethod`、`virtual void initialize()` 这一套骨架——**印证了 `Editor` 那一条的 `test method programs`** |
| **右下：`Waveform` 与 `Variables`** | **对得上第 9、10 项**；`Waveform` 面板上是 `no data` 的一张空图（坐标 `1000 / 500 / 0` 与 `0 / 100 / 200`） |
| **左下：`Problems` / `Firmware` / `Breakpoints`** | **三个视图叠在同一排标签里，`Problems` 是选中的**，面板里写着 `0 errors, 0 warnings, 0 infos`——**对得上第 4、5、6 项** |
| **右下：`Console` 与 `Error Log`** | **对得上第 7、8 项**；`Console` 里是 `C-Build [training]` |
| **右上：`Properties` 与 `Outline`** | `Properties` **对得上第 12 项**；**⚠️ `Outline` 不在上面那 12 项清单里**——见下面那条 ⚠️ |
| **菜单栏里有 `93000` 一项** | 逐字读出这一排：`File` / `Edit` / `Navigate` / `Search` / `Project` / `Run` / `93000` / `Window` / `Help`——**`93000` 是这一套 UI 自己加的那一项** |
| **状态栏** | 逐字读出：`training` / `Writable` / `Smart Insert` / `63 : 35`（**最右边那对数看着像光标位置**，本篇没有说） |

> **⚠️ 图上有一个视图名不在本篇的 12 项清单里：`Outline`。**
> 右上那块并排着两个标签 `Properties` 与 `Outline`，**而 `Outline` 在本篇里一次都没出现**
> （清单里没有、`## Related information` 也没有）。
> **（推断）两种读法本页都不排除**：一是清单漏了它，二是它属于别的 perspective 的残留摆放。
> **依据只是这一张图，原文没有承认也没有否认。本页不替它补进清单。见 `## 出处` ⑤。**
>
> **⚠️ 另有一处本页读不实，照实说**：左列中间有一条**收起来的**视图条，
> 上面那串字**看着像 `Debug`，但同一个截图里项目树中也有一个叫 `Debug` 的目录**，
> 两者本页分不开。**所以「第 11 项 `Debug` 在这张图上是不是也摆着」这件事，
> 本页不给结论。**

## 典型用法

**本篇没有 `## Procedure`、没有 `## Before you begin`，没有一个命令行、没有一个操作步骤。**
**它是一份「这个 perspective 里摆了哪些视图」的清单**——
**下面这些是从原文那一句定义 + 那 12 条里落出来的东西。**

| 要做的 | 依据（**原文**） |
|---|---|
| **进到调试的摆放** | 本篇没有说怎么切过去——**它的第 2 句把这件事推给了 `Perspectives`**（**那一篇本页没读**） |
| **改这个摆放** | 同上：`how you can customize a perspective, see Perspectives` |
| **改测试方法代码** | `Editor`——`edit and debug your test method programs in one editor` |
| **设断点** | `Editor`——`You can set the breakpoints in this editor`；**断点清单在 `Breakpoints` 视图** |
| **看变量** | `Variables`——`shows values of variables in the executed test method` |
| **看程序输出 / 给它输入** | `Console`——`shows the output of the execution of your program and enables you to enter input for the program` |
| **看数组 / 抓到的波形** | `Waveform`——`shows the contents of an array selected in the editor graphically`；还能从这里开 `Signal Analyzer tool` |
| **敲固件命令** | `Firmware`——`entering and executing firmware commands during debugging` |
| **跳到出错那一行** | `Problems`——双击列表里的一条，光标跳到 editor 里那一行 |
| **看测试系统 / Eclipse 插件报的错** | `Error Log`——`all the errors coming from the test system and from the Eclipse plug-ins` |
| **看某个对象的信息** | `Properties`——`the properties of an object that you are highlighting` |
| **新建测试方法工程 / 类** | `Project Explorer`——`You can create a new test method project and class from this view.` |
| **找某个器件设置工具** | `Test Program Explorer`——`all the device setup tools like Pin Configuration Tool, Level Setup Tool, Pattern Tool etc.` |
| **控制测试方法执行** | `Debug`（第 11 项）——`You can control the test method execution here.`（**那一篇见 [[debug-view]]**） |

**两处本页要提醒的**：

1. **这一页是「摆放」，不是「动作」。** 原文没有给任何一条操作步骤——
   **所有动作都落在具体视图各自的页里**（本篇只给一行说明 + 一个链接）。
2. **想找 `Expressions` 视图的人在这一页找不到它。**
   它只在 `Editor` 那一条的说明里被点到名字（见上面那条 ⚠️）。

## 和谁有关

- [[debug-view]] — **它是这个 perspective 的第 11 项**。
  **⚠️ 两篇对同一个视图的定位不一样，本页并列出来、不判谁对**：
  本篇给 `Debug` 那一项的一句话是
  `This view shows the process of the test method executions and debugging. You can control the
  test method execution here.`（**测试方法**），
  而 [[debug-view]] 那一篇自己的正文主体是 **testflow 调试**
  （它那张按钮表的题注就是 `Debug view icons for testflow debugging`）。
  **（推断）两种读法都能自圆其说**：一是「这个视图两半都管，两篇各写了一半」，
  二是「其中一篇的说明没有跟上」。**本篇没有一句话能判这件事。这是推断。**
  **（[[debug-view]] 那一篇本页读过；它引的 raw 本页没读。）**
- [[project-explorer-view]] — **第 1 项**（原文有链接）。本页只抄了它那一行说明。
- [[test-program-explorer]] — **第 2 项**。**⚠️ 它那一行里点名的三个工具
  （`Pin Configuration Tool` / `Level Setup Tool` / `Pattern Tool`）**
  **本页都没有核过它们各自有没有页。**
- [[waveform-view]] — **第 9 项**。**⚠️ 它那一行里还提到一个 `Signal Analyzer tool`**——
  **那个不在清单里，本页也没读。**
- [[testflow-properties-view]] — **第 12 项 `Properties` 那条给的两个举例之一**，
  逐字：`depending on the context, for examples, see Testflow Properties view or Pattern editor
  properties view`。**本页只抄了这一句，那一页没有读。**
- [[setup-perspective]] — **（推断）姊妹 perspective**。
  **依据：[[debug-view]] 那一篇的正文点名了它**
  （`You can also use the corresponding debugging buttons on the main toolbar of the Setup
  perspective.`），**说明这一套 UI 里至少有两个 perspective**；
  **而本篇自己只链了 `Perspectives` 那一篇，一次都没有点 `Setup perspective`。
  这条关系是本页自己接的，是推断。**
- [[smartest-6.3.2]] — **版本页**。**本页 `## 版本` 那一条用的正是 §11.2 ② 的哨兵写法，
  而哨兵里写的就是 `6.3.2`**——**见 `## 版本`，那一条不能照字面读。**
- `Editor` / `Problems` / `Firmware` / `Breakpoints` / `Console` / `Error Log` / `Variables` /
  `Properties` / `Outline` / `Expressions`（**均未建、且均不在 allowlist，故用反引号**）——
  **这 10 个视图名在本篇里都出现过，但一篇专页都没有。**
  **⚠️ 其中 `Expressions` 与 `Outline` 是「本篇点过名、但不在那 12 项清单里」的两个**
  （见 `## 出处` ② 与 ⑤）。
- `Perspectives`（**未建、不在 allowlist，故用反引号**）——
  `01.01.07_Perspectives.md`。**本篇两处指向它**（第 2 句 + `## Related information`）。
  **本页没读** —— **所以「还有哪些 perspective」「怎么自定义摆放」本页一个字都没有。**
- `Signal Analyzer tool` / `Pin Configuration Tool` / `Level Setup Tool` / `Pattern Tool`
  （**四个，均未建、不在 allowlist**）——**本篇提到但不展开的四个工具。本页都没读。**
- `Default Debug Perspective`（**不是一页，是那张图的题注**）——**见图里那一段。**

## 版本

**本文档有 `## Functional changes` 段，只有一条**，逐字：

- **Introduced before SmarTest 6.3.2**

> **⚠️ 这一条是 §11.2 ② 那个哨兵**——**照字面读会读出一条假信息。**
> 哨兵写的是 `Introduced before SmarTest 6.3.2`（**`before`**），
> 意思是「**在本文档集覆盖范围开始之前就已经有了**」，
> **不是「6.3.2 给它加了什么」。**
> **判据是 `before` 这个词本身**（§11.2 ②），**不需要看别处。**
> **所以「这个 perspective 从哪一版开始有」，本篇给不出答案**——
> **只能读到「至少 6.3.2 之前就有」。**
> **（对照，推断）** 同一批的 [[debug-view]] 那一条写的是 `Introduced in SmarTest 7.1.0`（`in`），
> 那一条就能给出版本号。两篇的写法不一样，正是因为一篇有确切版本、一篇没有。
> **这是本页按 wiki 里已有的同批页给的比较，是推断。**

**（推断）6.3.2 到 wiki 目标版本 7.10.3 之间这个 perspective 改过没有，本篇没有依据**——
**本文档的 `## Functional changes` 只有这一条，再没有第二条。**

详见 [[smartest-6.3.2]]。

## 出处

`sources:` 一篇：
`01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.04_Debug_perspective.md`
（TDC 主题号 `122014`；本地 raw md：**3,548 字节**、**74 行**——
**字节是磁盘上的字节数，行数是换行符个数**）

**本页没做的：**

- **一张图，本页看了**：`raw/122038.png`（题注 `Default Debug Perspective`）——
  **这是本页唯一一张「这个 perspective 长什么样」的依据**，
  它给出的东西列在上面「图里看到的」那一张表里。
  **⚠️ 图上有一处本页读不实**（左列那条收起来的视图条是不是 `Debug`），
  **已在那里照实标明，本页没有据它下任何结论。**
- **12 项里除 `Project Explorer` / `Test Program Explorer` / `Waveform` / `Testflow Properties
  view` / `Debug` 之外的那些，本页一篇专页都没读**（`Editor` / `Problems` / `Firmware` /
  `Breakpoints` / `Console` / `Error Log` / `Variables` / `Properties` / `Outline`）——
  **所以这 9 个视图长什么样、有什么选项、怎么用，本页一个字的实质都没有**，
  上面的表里只有原文给的那一行说明。
- **`Perspectives` 没读** —— **所以「还有哪些 perspective」「怎么自定义摆放」
  「怎么切到这个 perspective」本页全无；而本篇两处都推给了它。**
- **`Signal Analyzer tool` / `Pin Configuration Tool` / `Level Setup Tool` / `Pattern Tool`
  四个都没读** —— **所以它们各自是什么、在哪，本页没有。**
- **`Expressions` 与 `Outline` 这两个「本篇点过名的视图」没有追出去查** ——
  **它们是不是有别的页、属于哪个 perspective，本页只有本篇这一点文字作依据。**
- **没有交叉验证任何别处的文档**（§11：本页只写这一篇里有的）。
  **尤其 [[debug-view]] 那一篇的 raw 没读** ——
  **本页与它的关系全部取自 wiki 里那一页已经写好的内容（本页读过那一页 wiki 页），
  没有从对面回校过。**
- **`system` 一侧没有核过**：**本页没有在任何真实 SmarTest 上打开过这个 perspective，
  也没数过默认摆了几个视图**（`verified: doc-only`）。
  **上面那张布局描述全部来自 `raw/122038.png` 那一张图。**
- **本文档没有 `## Subtopics` 目录块**（查过：正文里 `Subtopics` 0 处），
  **也没有 `## Procedure` / `## Before you begin`。**
- **`layer: gui` / `stage: run` 不是本篇写的**——
  **本篇没有 `## Application` 这类自我定位段**，这个归属是本 wiki 的既有划分
  （**（推断）`gui` 与「一组视图的摆放」相符；`run` 与「用来调试运行中的测试方法」相符——
  但这是本页的观察，不是原文说的**）。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> **① `Project Explorer` 那一条把同一句话写了两遍。** 逐字：
> `You can create a new test method project and class from this view. You can create a new test
> method project and class from the view.`
> ——**第二遍只把 `this view` 换成了 `the view`，其余逐字相同。**
> **同一段落里连续两句同义，是本篇最明显的一处重复。本页照实并列，不替它删。**
>
> **② `Editor` 那一条点名的五个视图里，有一个不在本篇的 12 项清单里。** 逐字：
> `debug your test application with the Console, Variables, Expressions, Breakpoints, and
> Waveform views quickly and efficiently.`
> ——**`Console`（第 7 项）/ `Variables`（第 10 项）/ `Breakpoints`（第 6 项）/
> `Waveform`（第 9 项）四个都在清单里，`Expressions` 不在。**
> **本篇别处（含 `## Related information`）也没有 `Expressions`。**
> **本页照实并列，不替它补进清单。**
>
> **③ `Properties` 是 12 项里唯一没有链接的那一项。** 逐字：
> `- Properties`
> ——**其余 11 项在原文里都是 `[名字](<路径>)`，只有这一项是光秃秃的一行。**
> **（推断）两种读法**：一是它自己没有专页，二是漏了链接。
> **依据只是这 11 有 / 1 无的形态，原文没有承认也没有否认。本页不判。**
>
> **④ 同一个东西在这一篇里有两个词：`test method` 与 `test application`。** 逐字并列：
> `to debug a test method`（第 1 句）／`debug your test application`（`Editor` 那一条）
> ——**`test application` 全篇只出现这一次，其余一律是 `test method`。**
> **本页照实并列，不替它统一。**
>
> **⑤ 图上有、本篇清单里没有的一个视图名：`Outline`。**
> 逐字（**从 `raw/122038.png` 上读出的标签**）：`Properties` 与 `Outline`。
> ——**`Outline` 在本篇正文里 0 次出现。**
> **（推断）见 `## 是什么` 里那条 ⚠️；本页不替它补进清单。**
>
> **⑥ 标题与正文的大小写不一致。** 逐字并列：源文件 frontmatter 的
> `title: "Debug perspective"`（**小写 `p`**）、正文的
> `The Debug Perspective contains the views to debug a test method.`（**大写 `P`**）、
> 图的题注 `Default Debug Perspective`（**大写 `P`**）。
> ——**同一个名字三处出现，只有文件名 / 标题那一处是小写。本页照实并列。**
>
> **⑦ 一个说法读着别扭：`in the list form`。** 逐字（`Problems` 那一条）：
> `This view shows errors or warnings and the locations of them in the list form.`
> ——**`in the list form` 读起来像少了一个冠词**（常见写法是 `in list form` 或
> `in the form of a list`）。**本页照原样引，不替它改。**
>
> **⑧ `## Related information` 只有一条链接，而且和正文第 2 句指的是同一个目标。**
> 逐字：`## Related information` 那一节整节就是
> `[Perspectives](<01.01.07_Perspectives.md>)`；
> 而正文第 2 句也已经链过同一个 `01.01.07_Perspectives.md`。
> ——**同一个目标在一篇里被链两次，第二次还占了一整节。
> 本页照实并列（这一条不是错，是记法）。**
>
> **⑨ 本篇没有 §11.2 ① 那种编码损坏**（查过：正文里汉字 0 个、`鈥` 0 处、
> U+2026 的省略号 0 处、ASCII 的三个句点 0 处）。

`verified: doc-only`
