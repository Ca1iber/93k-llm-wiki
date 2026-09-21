---
type: object
title: Flow Sequence Editor
layer: gui
stage: testflow
tags: [testflow, gui, flow-sequence-editor, palette, testflow-component, insertion-point, zoom, testflow-tool]
related: [testflow-tool, flow-data-editor, testflow, flow-control-node, bin, testflow-properties-view, test-suite, hardware-response-file, shmoo-tool, integrated-result-tool, mapping-testflow]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.02_Flow_Sequence_Editor.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# Flow Sequence Editor

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

**没有加标记的语法段。** 定义文档里没有 `Syntax` / `Parameters` / `Example`
这类**段标记**，跟着 `Subtopics` 找一层也没有。
**所以本脚本一个字都不收录**——没有段标记时「哪一段是语法」是猜，而猜就是编（§4）。

<!-- 语法节 end -->

## 是什么

**Flow Sequence Editor 是 Testflow Tool 里那个「画着看、直接改」的进程编辑器。** 定义文档的正文一共三段：

> 「This editor displays the testflow sequence in graphical form and allows you to edit it.」

**这句是它的定位**：testflow 的图形化表示 + 可直接编辑。**编辑器只有三个部件**，
原文逐个点了名：

| 部件 | 原文说的是什么 |
|---|---|
| **Palette**（左侧） | 用它把 Testflow components 插进 testflow |
| **窗口主体** | 显示图形化的 testflow 序列；**由 insertion points 与 testflow components 组成** |
| **主工具栏上的缩放** | `Zoom in` / `Zoom out` 两个按钮，**或按钮旁边那个框里填一个百分比** |

> 「The main part of the window displays the graphical testflow sequence. The graphical testflow representation consists of insertion points and testflow components. You can enlarge or reduce it by clicking the Zoom in and Zoom out buttons on the main toolbar or by entering the desired zoom level as a percentage in the field beside the buttons.」

**注意这一篇讲的全是「显示」**：编辑动作（插入、删除、挪节点）自己一个字没写，
**全在 `## Related information` 那五条里**（见「典型用法」）。

### 图证：这张图里有正文一个字都没写的 Palette（④ 图证）

本篇有 **2 张图**：`110936.png`（图形化 testflow 表示）与 `111915.png`（缩放按钮）。
路径 `../../../../raw/<n>.png` 从 md 往上四层正好是 `tdc-html/`，文件在 `tdc-html/raw/`——
**有些页曾写「图在语料树之外」，那是错的**（`schema.md` §11.4）。**两张都读了。**

**`110936.png` 是这一页最值钱的一张图**，因为**Palette 里那 15 项，正文一项都没列**：

| 图里读到的（raw 文本里没有） | |
|---|---|
| **窗口标题** | `tf_functional`（全语料 0 命中） |
| **Palette 15 项，从上到下** | `Select`、`Run Test`、`Run and Branch`、`Good Bin`、`Bad Bin`、`Multi Bin`、`Print`、`Print to Datalog`、`If/Then`、`Repeat Loop`、`While Loop`、`For Loop`、`Assign Value`、`Assign Level Value`、`Assign Timing Value` |
| **两个蓝色注记** | `testflow component` 带两个箭头，**一个指 test suite 节点、一个指 bin 节点**——即**两者都叫 testflow component**；`insertion point` 指连线上那个小圆圈 |
| **节点形状** | test suite 节点是圆角矩形；**带 P / F 两个出线端点的就是分支节点**；good bin 是绿色三角（图里标 `1`），bad bin 是红色八边形（图里标 `2`） |

**这张图里的字，哪些搜得到、哪些搜不到**（本页拿它们去全语料 grep 过，
**这是本页为「图里的字搜不搜得到」做的一次检索，不是本页 `sources:` 里的内容**）：

- **Palette 的项名大多搜得到**：`Print to Datalog`（11 篇）、`Run and Branch`（29 篇）、
  `Assign Value`（14 篇）、`Repeat Loop`（3 篇）、`Zoom out`（8 篇）都有命中；
  **`If/Then` 与 `Assign Level Value` 各只 1 处**。
- **0 命中的是这两个**：**窗口标题 `tf_functional`**，以及同页 `111915.png` 里那个 **`125%`**
  ——**这两个字串全语料一处都没有**。
- **两个注记词都搜得到**：`insertion point`（15 篇）、`testflow component`（4 篇）。
- ⚠️ **Palette 的大小写有两套写法**：**这张图里是 Title Case**（`Good Bin` / `Bad Bin` /
  `Run Test` / `While Loop` 各项都是首字母大写），而**全语料里 `goodbin` / `badbin` 这种全小写写法
  只出现 1 处**（`02.08.04.32.02.01.05_Inserting_a_bin_into_the_testflow.md` 第 31 行：
  `click goodbin or badbin on the Palette`）——**而同一篇文档第 67 行又写
  `On the Palette, click Multi Bin.`（Title Case）**。
  **一处小写、一处 Title Case，在同一篇文档里并存**；本页照实并列，不替它选一个。

**`111915.png` 只把正文那句画出来，没有新信息**，但它把「两个按钮 + 一个框」的**并排关系**坐实了：
图里是放大镜 `+`、放大镜 `-`、**一个写着 `125%` 的输入框**、右侧一个下拉箭头——
**正文说的 `the field beside the buttons` 就是它**。`125%` 这个值**全语料 0 命中**（只是那一次的取值）。

## 典型用法

**本篇没有 `## Procedure` / `## Before you begin` / `## What to do next`**，
所以「怎么用」只能拆成两半：**编辑器里那三步**（正文写的）+ **编辑动作的落点**（`## Related information` 那五条）。

**正文能给出的三步**：

1. **在左边的 Palette 里选一个 component。**
2. **把它插到 insertion point 上**——图 `110936.png` 里那个注记指的就是主区连线上那些小圆圈
   （**正文没有解释 insertion point 长什么样，那是图里看出来的**）。
3. **要看清整体或只看一段，用主工具栏的 `Zoom in` / `Zoom out`，
   或在旁边那个框里直接填百分比**（图 `111915.png` 里那次填的是 `125%`）。

**编辑动作本身要去哪找**——`## Related information` 给的五条，逐条就是一件事：

| 要做什么 | 原文指的文档 |
|---|---|
| 打开这个编辑器 | `Opening the Testflow Tool` |
| 插一个 test suite 进流程 | `Inserting a test suite into the testflow` |
| 处理节点（**工作方式**） | `Working with nodes` |
| 删节点 | `Deleting nodes` |
| 与另一个编辑器对齐 | `Synchronization between the Flow Data Editor and the Flow Sequence Editor` |

**这五篇本页一篇都没读**（见「出处」）——**「怎么删一个节点」「两个编辑器怎么同步」本页一个字都没有。**

## 和谁有关

**入边 33 条 / 23 篇**（`inline` 口径，`extract/edges.jsonl`）——**比它的父页 [[testflow-tool]] 还密**。
引用它的文档分五类：

- **SmarTest Work Center 的工具导航**：`01.01.09_Editors`、`01.01.14.30_Testflow_Tool_preference_page`、
  `01.03.04_Working_with_testflows_efficiently`——**它是「Editors」里的一个条目**。
- **Shmoo / 结果工具那一支**（`02.08.04.25.03.10.01`–`.03`、`02.08.04.25.03.11`）：
  把 test suite 在 Shmoo Tool 与本编辑器之间搬来搬去。
- **testflow 章内部**：`02.08.04.32.03.03_Synchronization_between_the_Flow_Data_Editor_and_the_Flow_Sequence_Edito.md`、`02.08.04.32.03.04_Testflow_Properties_view`、
  `02.08.04.32.03_Elements_of_the_Testflow_Tool`（2 处）、`02.08.04.32.01.02.06_Bins`（3 处）、
  `02.08.04.32.02.01.04.03_Creating_a_floating_test_suite`、
  `02.08.04.32.02.01.13_Printing_a_graphical_representation_of_the_testflow`、
  `02.08.04.32.02.06.01_Preparing_Hardware_Response_files`。
- **`03.04` 那一支用例**：`03.04.01.04.01_Implementing_bin_disconnect_to_overcome_the_pass_or_fail_site_dependency.md`。
- **`99_Unlisted_or_Unreferenced` 六篇**：搜索类任务（`Searching for a group node` / `bin node` /
  `test suite` / `variable`）、`Using_the_Bins_page`、`Configuring_the_Testflow_Tool`、
  `Using_the_Flow_Sequence_Editor`。**最后那两篇标题看着像本页的专页，本页没读。**

**出边 6 条**：正文里 1 条（`Testflow components`）+ `## Related information` 5 条。

- [[testflow-tool]] — **父页**。本编辑器的定义文档挂在他底下（`Elements of the Testflow Tool` 那一支）
- [[flow-data-editor]] — **同级的另一个编辑器**；`Related information` 最后一条讲的就是两者同步。
  **「两个编辑器各管什么」本篇没写**
- [[testflow]] — 本页 `stage: testflow`；那页是本阶段的脊椎
- [[flow-control-node]] / [[bin]] / [[test-suite]] — **Palette 里插的就是这些**（图证里有它们的形状）
- [[testflow-properties-view]] — 图 `110936.png` 里选中节点后右侧那块属性面板的落点
- [[hardware-response-file]] / [[shmoo-tool]] / [[integrated-result-tool]] — 入边里那几类文档讲的事，
  **本页只证明「它们会指向这个编辑器」，不证明细节**
- [[mapping-testflow]] — 同阶段的对照表页；它把本页当作「插 test suite / 编排流程顺序」的 GUI 侧那一格

## 版本

本篇的 `## Functional changes` 三条：

- `Introduced before SmarTest 6.3.2`
- `SmarTest 6.5.2: The Flow Sequence Editor replaces the Graphical Testflow Editor.`
- `SmarTest 6.5.2: For bin node, the OOC (Out Of Control) rule is not supported.`

> ⚠️ **第一条是哨兵值**（`schema.md` §11.2②）：措辞是 `before`，意思是「**在本文档集覆盖范围
> 开始之前就已经有了**」，**不是「6.3.2 新增」**。
>
> **第二条不是新增，是取代**：`replaces` 说的是**换名/接替**——
> 6.5.2 之前它叫 `Graphical Testflow Editor`。**那个旧名字在全语料里只出现 1 次，
> 就是这一行**。所以本页**不能**据此说「6.5.2 才有了这个编辑器」。
>
> **第三条是一条限制**：从 6.5.2 起，**bin node 不支持 OOC（Out Of Control）规则**。
> `OOC` 与 `Out Of Control` 在本篇之外是什么，本页没读（见「出处」）。

## 出处

`sources:` 一篇：
`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.02_Flow_Sequence_Editor.md`
（TDC `99280.htm`，26 行 / 1,659 字节）。

**本页没做的**：

- **`## Related information` 那五篇一篇没读**。**这是本页最大的缺口**：本篇讲的全是「显示」，
  **编辑动作（插 test suite、改节点、删节点、与 Flow Data Editor 同步）全在那五篇里**，
  所以本页能给的**只有「这个编辑器长什么样」，没有「怎么用它改流程」**。
- **`Subtopics` 段本篇没有**——它给的是 `## Related information`。
  **所以本页的 语法节是空的**（脚本只抽 `Syntax` / `Parameters` / `Example` 段标记，
  本篇一个都没有，跟着段标记找一层也没有）。**那一格空不是本页没写，是本篇没有。**
- **图 2 张全看了**（`110936.png`、`111915.png`），结论在「是什么」里。**不是「本页没用图」。**
- **上面那些「0 命中 / 有命中」，是本页拿那些串去全语料 grep 得到的检索结果**，
  **不是本页 `sources:` 里的内容**——写出来只为说清「图里的字搜不搜得到」（§11.4 的 ④ 档要求）。
  其中 `02.08.04.32.02.01.05_Inserting_a_bin_into_the_testflow.md` 与
  `02.08.04.32.02.01.11_Working_with_nodes.md` 两篇被引到名字，**这两篇本页也没读**。
- **`OOC`（Out Of Control）规则本页没展开**——本篇只说了「bin node 不支持它」，
  **它是什么、在别的节点上怎么配，本页一个字没有**。
- **没有实跑**：没开过这个编辑器、没插过节点、没用过缩放。`verified: doc-only` 指的就是这件事。
- **没有动 `wiki/index.md`**，也没有改 `wiki/stages/testflow.md`。

> ⚠️ **本篇的语料瑕疵，照实记、一处都没替它改**（§11.2）：
>
> ① **`## Related information` 那五条链接，零分隔符挤在 raw 的第 20 行。** 它的开头是
> 「Opening the Testflow ToolInserting a test suite into the testflow」
> ——**一条链接的文字后面直接接上另一条链接的文字，中间一个空格、一个换行都没有**。
> `extract/edges.jsonl` 里这五条边的 `line` 全是 `20`，**正是这件事的机器证据**。
>
> ② **最后那一条的链接文本被截断了**：
> `Synchronization between the Flow Data Editor and the Flow Sequence Edito`
> ——**末尾少了 `r`**。**而且磁盘上的文件名也是这么截断的**
> （`02.08.04.32.03.03_Synchronization_between_the_Flow_Data_Editor_and_the_Flow_Sequence_Edito.md`），
> 所以**这不是坏链，是一个被截断的名字**——链接照样解析得到。**本页照抄，不替它补那个 `r`。**
>
> ③ **正文里 `Palette` 这个词的大小写两套并存**（见「是什么」里那段）：
> 定义文档写的是 `Palette`，图 `110936.png` 里 Palette 的**项目名**是 Title Case，
> 而全语料里 `goodbin` / `badbin` 只有一处全小写。**本页并列，不替它选一个。**
>
> **本页（含空的语法节）0 处编码坏字**（`碌` / `渭` / `卤` / `惟` / `鈥` 那几族逐个查过），
> **0 处 `DC/DC power units`**（§11.2⑤ 那一族）。

`verified: doc-only`
