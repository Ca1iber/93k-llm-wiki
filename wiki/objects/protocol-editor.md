---
type: object
title: Protocol editor
layer: gui
stage: pattern
tags: [protocol-editor, pattern, protocol, transaction, pin-role, gui]
related: [test-program-explorer, pattern, wavetable, timing, level, pattern-editor, smartest-7.1.0]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.22_Protocol_editor.md
created: 2026-09-18
updated: 2026-09-20
verified: doc-only
---

# Protocol editor

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **721 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.22_Protocol_editor.md>` 及其子主题 `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.22.02_Transaction_details.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Parameters（取自子主题 Transaction details）

Transaction parameters can be used within test methods to pass variables to a transaction. This way one can create dynamic transactions. Typical parameters of read/write transactions are register address, physical address and register data.

The order of the parameter definition has an impact to the corresponding transaction and the resulting state character sequence.

The state character sequence representing a decoded field will be mapped back to transaction parameters during parameter reconstruction in order to be readable from test methods.

Properties
> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/126135.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：5 行 × 2 列。
> 首行（上游原文）：Property | Description

<!-- 语法节 end -->

## 是什么

**Protocol editor 是编协议的图形界面。** 原文第一句：

> 「The protocol editor is the **graphical user interface** used to **set up and edit protocols**
> as well es **protocol specific levels, timing and wavetable**.」
> （**`as well es` 是原文的写法**，见 `## 出处` 瑕疵①。）

**这一句里有两组东西：**

| 组 | 内容 |
|---|---|
| **主对象** | **protocol（协议）本身** |
| **附带三类** | **protocol 专属的 `levels` / `timing` / `wavetable`** |

**关键在于「protocol specific」这个限定**：它编的不是通用的 level/timing/wavetable，
**是这份协议专属的那一套**（推断，依据是 `protocol specific` 这个定语，
以及下面「底部 tab」一节里那三个 tab 的存在）。

**它一打开落在哪个 tab 上，原文也写明了**：

> 「It opens with the **Protocol Definition tab** per default.」

### 三个区域

**界面按「左结构 / 右详情 / 底 tab」分成三块**，原文各有小节：

| 区域 | 位置 | 干什么（原文） |
|---|---|---|
| **Overview area** | **左** | `shows the structure of the protocol **currently selected in the test program explorer**` |
| **Details area** | **右** | `will show different sections with different content **related to the selected element**` |
| **tabs** | **下** | 在四个 tab 之间快速切换 |

> **第一行的定位短语是本节最要紧的一句**：
> **左边那棵结构树的根，来自 `test program explorer` 里当前选中的那个协议**——
> **不是本编辑器自己决定的。所以「先在 test program explorer 里选协议」是隐含的第一步**
> （推断，依据就是这个定位短语）。

### 左：结构树的图标

**原文给了一张图标表。它其实是「五种元素 × 有没有错」的组合：**

| 元素 | 正常图标 | 出错时的图标 |
|---|---|---|
| **protocol** | protocol 图标（`126129.png`） | protocol error 图标（`130385.png`） |
| **transactions** | transaction 图标（`126130.png`） | transaction error 图标（`130386.png`） |
| **pin roles** | pin role 图标（`126131.png`） | pin role error 图标（`130387.png`） |
| **fields** | field 图标（`126132.png`） | field error 图标（`130388.png`） |
| **pin role groups** | pin role group 图标（`126141.png`）—— `used with **parallel protocols**` | ——（原文没给） |

**外加一个单独的状态图标：**

> **`Undefined protocol element`**（未定义的元素，图标 `126152.png`）
> ——原文给了**可能的原因**：
> `Possible cause: **name mismatch of pin role in protocol details and pin role details**`

> **最后这一条是本页最具体、最能拿去做事的一句**：
> **协议结构里出现「未定义元素」，先查 `Protocol details` 与 `Pin role details` 两处的
> pin role 名字是不是对不上。** 原文用的是 `Possible cause`（可能原因），**不是确定结论**。

> ⚠️ **这张表在本 wiki 依据的 raw markdown 里被转成了多行 ` |` 的形式**
> （见 `## 出处` 瑕疵⑤）——**行列关系要按内容判断，本页已按内容重新排版**。

### 右：详情区，四选一

**原文说右边显示什么，取决于左边选中了什么元素**，并且**列出了四种可能**：

| 选中的元素 | 右边显示 |
|---|---|
| protocol | **`Protocol details`** |
| transaction | **`Transaction details`** |
| pin role | **`Pin role details`** |
| field | **`Field details`** |

**两条附带规则：**

| 规则 | 原文 |
|---|---|
| **四块是展开还是折叠，由偏好设置控制** | `The protocol editor's preference settings control if sections are displayed extended or collapsed.` |
| **协议有错时会就地提示** | `In case the protocol definition is erroneous the details area will provide further information **when moving the mouse over the highlighted field**.` |

> **注意第二条的机制**：**不是弹窗，是「把鼠标移到被高亮的字段上」才出信息**。
> 原文配了一张图，图题就点明了它要讲的那种错：
> `Error if symbol's directions is left undefined.`

**另有一条替代路径**，落在别处的视图上：

> 「Alternatively you may also use the **Problems View**. By **double-clicking on a
> `Protocol Marker` type of error** the cursor jumps to the error in the corresponding editor.」

**所以排错有两条路**（推断）：**在编辑器里用鼠标悬停逐个看**，或
**去 Problems View 里按 `Protocol Marker` 类型双击跳过去**。

### 底：四个 tab

> 「The tabs at the bottom of the protocol editor allow you to quickly switch between:」

**原文这里是四个列表项，不是一行**（本页照原文列成列表；后三个在原文里各是一个链接）：

- **Protocol Definition (default)**
- `Level`（raw: `02.08.04.22.05_Level_tab.md`）
- `Wavetable`（raw: `02.08.04.22.06_Wavetable_tab.md`）
- `Timing`（raw: `02.08.04.22.07_Timing_tab.md`）

**原文给了这三个额外 tab 存在的理由，这一句值得逐字读：**

> 「This way you can enter protocol relevant details, such as specific levels, timing, etc.
> **very efficiently without leaving the protocol editor**.」

> **`without leaving the protocol editor` 是这句的目的**：
> **level / timing / wavetable 不是只能在本编辑器里改**——
> **那三个 tab 是为了「不用切出去」而存在的**（推断，依据就是这句 `without leaving`）。

### 十一条子主题，分成四组

| 组 | 子主题 |
|---|---|
| **四种元素详情**（4） | `Protocol details` / `Transaction details` / `Pin role details` / `Field details` |
| **三个 tab**（3） | `Level tab` / `Wavetable tab` / `Timing tab` |
| **两块专题**（2） | `Protocol wrapper` / `Build feature of the protocol editor and test program explorer` |
| **两条用法**（2） | `Using the protocol editor` / `Working with Protocols` |

> **这个分法和界面对得上**（推断）：**第一组就是右边详情区的四选一，第二组就是底部那四个 tab
> 里除默认页以外的三个**。**换句话说：这篇主文档讲的界面，在那七篇子主题里一笔一笔展开。**
> **第三组两块是本页完全没有的东西**——尤其 `Build feature …`，从标题看
> **它牵涉到 `test program explorer`**（推断，依据是标题里并列的两个名字）。

## 典型用法

**原文没有 `## Procedure` / `## Before you begin` / `## What to do next`。
下面几条都是从正文里直接读出来的。**

**1. 打开时你已经在一个 tab 上了**：默认落在 **`Protocol Definition`**。
**要改 level / timing / wavetable，切底部对应 tab**——**不用离开这个编辑器**。

**2. 换个对象看，不需要重开窗口**：**在左边结构树里选另一个元素，右边就换一套详情区**
（protocol → Protocol details；transaction → Transaction details；pin role → Pin role details；
field → Field details）。

**3. 前提顺序（推断）**：**左边那棵树显示的是 `test program explorer` 里当前选中的协议**
（原文 `the protocol currently selected in the test program explorer`）——
**所以顺序是：先在 test program explorer 里选中协议，再在这里编**。

**4. 排错的三条路，按「从轻到重」排：**

| 路径 | 怎么做 | 原文依据 |
|---|---|---|
| **一眼看出** | 看结构树上的**错误图标**（protocol / transaction / pin role / field 各有各的 error 图标） | 图标表第三列 |
| **就地看细节** | **把鼠标移到被高亮的字段上**，详情区给出进一步信息 | `when moving the mouse over the highlighted field` |
| **跳到出错处** | 去 **Problems View**，**双击 `Protocol Marker` 类型的错误**，光标跳到对应编辑器里的错处 | `By double-clicking on a Protocol Marker type of error the cursor jumps to the error` |

**5. 「未定义元素」先查名字**：结构树里出现 `Undefined protocol element` 时，
**先对一下 `Protocol details` 和 `Pin role details` 两处的 pin role 名字**
（原文 `Possible cause: name mismatch of pin role in protocol details and pin role details`）。

**6. 详情区被折叠了？** 那多半是偏好设置的事——
原文说 `control if sections are displayed extended or collapsed`，
**但怎么改，本页没读那一篇**（`Protocol Editor preference page`）。

**7. 一组细节本页讲不了**：**transaction 的参数机制**（方向、长度、解码函数、显示格式）
**在本页「语法 / 参数」节里有一节完整的表格，但它取自未读的子主题 `Transaction details`**——
**本页正文没有展开它**（§11：不把没读的文档的内容写进正文）。

## 和谁有关

- [[test-program-explorer]] — **结构的来源，本页最要紧的一条关系。**
  原文 `the structure of the protocol currently selected in the test program explorer`。
  **它同时还是那条未读子主题标题里并列出现的第二个名字**
  （`Build feature of the protocol editor and test program explorer`）——
  **说明这两者之间还有一层本页不知道的牵连。**
- [[pattern]] — 本页 `stage: pattern` 的落点：它编的是 protocol，属于 pattern 侧。
- [[wavetable]] — 底部 tab 之一（`Wavetable tab`）。
  **原文把 wavetable 列为它要编的三类附带物之一**；
  **本页讲的只是「有这么一个 tab」，wavetable 本身是什么由那一页讲**（推断）。
- [[timing]] — 底部 tab 之一（`Timing tab`），同样被列为三类附带物之一。
- [[level]] — 底部 tab 之一（`Level tab`），同样。
- [[pattern-editor]] — **同类页**：**本页 `layer: gui` 意义上的邻居**。
  **原文没有提过它**（推断：都是 pattern 侧的编辑器，**但关系是本页推的**）。
- [[pin-group-editor]] — 图标表里有 `pin role groups`，原文标注它
  `used with parallel protocols`。**本页把它接到 [[pin-group-editor]] 是推断**
  （依据是名字对应），**pin role group 本身是什么，本页讲不出来。**
- [[smartrdi-vector-and-protocol-programming]] — **同主题页**（名字里有 protocol programming）。
  **原文没有提过它**，**这是推断。**
- [[smartest-7.1.0]] — 本页版本段第一条（引入版本）。
- `Protocol details` / `Transaction details` / `Pin role details` / `Field details`
  （**均未建、未读**）— **详情区的四块，也就是结构树四种元素各自的那一节**。
  **本页只讲了「选谁出谁」，四节里有什么一个字都没有。**
- `Level tab` / `Wavetable tab` / `Timing tab`（**均未建、未读**）— 底部三个 tab 的内容。
- `Protocol wrapper`（**未建、未读**）— **本页对它是零**：`wrapper`（包装）在这里指什么，本页不知道。
- `Build feature of the protocol editor and test program explorer`（**未建、未读**）—
  一条串起本编辑器与 `test program explorer` 的机制，**本页对它是零**。
- `Using the protocol editor` / `Working with Protocols`（**均未建、未读**）—
  两条用法篇目。**本页的 `## 典型用法` 之所以薄，责任在这两篇身上。**
- `Problems View` / `Protocol Editor preference page`（**均未建、未读**）—
  原文正文里点名的两条替代/配置路径。
- `Pin role` / `Transaction`（**均未建、未读**）— `## Related information` 的前两篇。
- `Pattern Debug Tool` / `TA column`（**均未建**）— 只出现在本页「语法 / 参数」节里
  （那一节取自未读的 `Transaction details`），**本页正文没有使用它们**。

## 版本

`## Functional changes` 段有，**两条**：

> 「**Introduced in SmarTest 7.1.0**」
> 「**SmarTest 7.1.3**: **Enhanced error handling and presentation**」

| 条目 | 性质 | 本页能说的 |
|---|---|---|
| `Introduced in SmarTest 7.1.0` | **确定的版本号** | **7.1.0 引入** |
| `SmarTest 7.1.3: Enhanced error handling and presentation` | **确定的版本 + 一件确定的事** | **7.1.3 改进了错误的处理与呈现** |

> **两条都能和正文对上**（推断）：正文里**与错误有关的机制占了很大比重**——
> 结构树上每个元素都有 error 图标、`Undefined protocol element`、
> 悬停高亮字段出信息、`Problems View` 里双击 `Protocol Marker` 跳转。
> **7.1.3 那一条说的「error handling and presentation」，很可能就是这些东西**——
> **但原文没有把两处连起来说，所以本页只并列，不判定。**

## 出处

`sources:` 一篇：
`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.22_Protocol_editor.md`

**这就是本页正文的全部依据。整篇 117 行**——含 `## Overview area`、`## Details area`、
`## Protocol editor tabs`、`## Related information`、`## Functional changes` 五节，
**外加一张图标表和一张十一行的子主题目录**。

**本页没做的**：

- **十一条子主题一篇都没读**：`Protocol details`（`.01`）、`Transaction details`（`.02`）、
  `Pin role details`（`.03`）、`Field details`（`.04`）、`Level tab`（`.05`）、
  `Wavetable tab`（`.06`）、`Timing tab`（`.07`）、`Protocol wrapper`（`.08`）、
  `Build feature of the protocol editor and test program explorer`（`.09`）、
  `Using the protocol editor`（`.10`）、`Working with Protocols`（`.11`）。
  **直接后果**：**本页只有「界面分哪几块、每块显示哪一节的标题」，
  这十一节里的任何内容一个字都没有。**
- **「语法 / 参数」节那 1,472 字符本页没有当作依据。** 那一节是脚本从**子主题
  `Transaction details`** 逐字抽的（段名里的 `（取自子主题 Transaction details）` 就是标注），
  **那一篇本页没读**。
  **所以 transaction 参数的四个属性（`Direction` / `Length` / `Decode function` /
  `Display mode`）以及 `Pattern Debug Tool` 的 `TA` 列、`BINARY`/`DECIMAL`/`HEX` 这些，
  本页正文一个都没有展开**——**它们在该节里，请直接读那一节。**
- **一张图没看。** 原文里有 **15 处图**：`126124.png`（Protocol Definition 视图）、
  五个元素图标 + 四个 error 图标 + 一个 undefined 图标（共 10 个）、
  `129383.png`（方向未定义时的错误）。
  **本页没有任何来自图的结论**——**界面长什么样、图标画成什么样，本页全不知道，
  只有它们的名字与说明文字。**
- **`## Related information` 的三篇一篇没读**：`Pin role`、`Transaction`、
  `Protocol Editor preference page`。**原文只给了名字，没说是什么关系。**
- **原文正文里点名的两处没读**：`Problems View`（排错的替代路径）、
  `protocol editor's preference settings`（控制详情区展开/折叠）。
  **所以「双击 Protocol Marker 之后长什么样」「怎么改展开折叠」本页都没有。**
- **没有查 `protocol` 在 SmarTest 里的定义**，**没有查 `pin role` / `field` /
  `transaction` 各自是什么**（它们只在图标表里各占一行），
  **没有查 `Protocol wrapper` 是什么**，**没有查 `parallel protocols` 指什么**。
- **没有查 `SmarTest 7.1.0` / `7.1.3` 在版本线上的位置**。

> ⚠️ **语料瑕疵，照实记下、一处没替它改**（§11.2）：
>
> **① 拼写错**（逐字引）：
> `The protocol editor is the graphical user interface used to set up and edit protocols
> **as well es** protocol specific levels, timing and wavetable.`
> ——**`as well es` 应为 `as well as`**。
>
> **② 一处 `Note` 直接粘在链接后面，中间没有任何分隔**（逐字引）：
> `- [Field details](<02.08.04.22.04_Field_details.md>)Note The [protocol editor's preference settings](<…>) control if sections are displayed extended or collapsed.`
> ——**`…Field_details.md>)` 与 `Note` 之间没有空格、没有换行**，
> **在 Markdown 里会被并进同一个列表项**。
> **本页没有替它加分隔符。**（**本批里第二次遇到同类问题**，另见 [[timing-diagram-tool]]。）
>
> **③ 从句连词用错**（逐字引，紧跟在上一条那句里）：
> `…control **if** sections are displayed extended or collapsed.`
> ——**`if` 在此应为 `whether`**。
>
> **④ `## Related information` 三个链接连排、无分隔**（逐字引全行）：
> `[Pin role](<../02.07_Test_Method_Reference/02.07.11.01.09.08_Pin_role.md>)[Transaction](<../02.07_Test_Method_Reference/02.07.11.01.09.13_Transaction.md>)[Protocol Editor preference page](<../../01_Getting_started/01.01_SmarTest_Work_Center/01.01.14.17_Protocol_Editor_preference_page.md>)`
> ——**三个链接首尾相接，中间没有空格、逗号或换行**。
> **本页没有替它加分隔符。**（**本批里第四次遇到同一种排版缺失**，
> 另三处见 [[test-summary-tab]]、[[raw-data-views]]、[[timing-diagram-tool]]。）
>
> **⑤ 图标表在 raw markdown 里是坏的**：原文那张表（`Symbols of the protocol structure`）
> **被转成了多行孤立的 ` |`**，列与列之间靠空行分隔，
> **`Icon` / `Description` / `Icon indicating an error` 三列的行列关系无法从 markdown 直接读出**
> ——必须靠内容（哪一格是图片、哪一格是文字）反推。
> **本页按内容把它重排成「元素 × 正常/出错」两列**——**这是编辑动作，本页在此声明；
> 原文的实际排版本页没有改，也无权改。**
> （**这一形态在本 wiki 依据的 raw markdown 里是多篇共有的转换产物**，
> 不是本篇独有的问题。）
>
> **⑥ 一处措辞不是通行英语**（逐字引）：`It opens with the Protocol Definition tab **per default**.`
> ——**`per default` 通常写作 `by default`**。
> **这一处本页不判为错**（意思清楚、也不是拼写错），**只记在这里**，
> 并且**在正文里改写成了通顺说法**，**没有逐字引它**。
>
> 链接指向方面：**本页四条子主题/正文内链的路径
> （`…22.01` ~ `…22.04`、`…01.01.14.17_Protocol_Editor_preference_page.md`、
> `…01.01.08.09_Problems_View.md`）与它们各自的名字对应，本页未发现指错。**

`verified: doc-only`

