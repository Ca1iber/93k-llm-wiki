---
type: object
title: GetUtilityLines
layer: L2
stage: pin
tags: [pin, testmethod, api, utility-line, utility-pogo-block, universal-test-method, report-window, l2]
related: [set-utility-lines, flex-relay, utility-line-view, hardware-view, utility-pins-editor, utility-card, utility-pogo-block-utility-card-v93000-exa-scale-systems, report-window, test-suite, pin, smartest-6.5.2, smartest-7.2.1, smartest-7.10.2]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.05.04.05_GetUtilityLines.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

> ⚠️ **本页若干处记的是 2026-10-10【之前】的语料形态。**
> 那一轮把语料里的表格一律换成了**指向上游 HTML 的指针**
> （见 `extract/PLAN-表格指针化.md`）。所以下文凡是说「表格被压平 / 被摊平 /
> 一格一行」的地方，指的是**更换之前**的样子 —— 现在语料里那个位置是**一句指针**，
> 真表仍在 `tdc-html/raw/` 的上游 HTML 里。**页码/引文都不受影响。**

# GetUtilityLines

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,945 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.05.04.05_GetUtilityLines.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Parameters

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/111063.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 3 列。
> 首行（上游原文）：Parameter | Type | Description
> 表内引用（3 条，供检索）：`Utility Card`（raw: `../02.05_Test_Head_Cards/02.05.08.04_Utility_Card.md`） · `Utility pogo block mapping`（raw: `../02.03_DUT_board_design_reference/02.03.06.08.02_Utility_pogo_block_-_Utility_Card__V93000_EXA_Scale_systems.md#_347642__s_Utility_pogo_block_mapping`） · `Utility pogo block - Utility Card (V93000 EXA Scale systems)`（raw: `../02.03_DUT_board_design_reference/02.03.06.08.02_Utility_pogo_block_-_Utility_Card__V93000_EXA_Scale_systems.md`）

### Example

### Output for two utility cards of an V93000 EXA Scale system

 Output with parameter blockId of the test method set to 0. The pogo blocks of the second optional `Utility Card`（raw: `../02.05_Test_Head_Cards/02.05.08.04_Utility_Card.md`） are listed as 265 to 272.

```
get utility block 1             =01111100101110100100010010011010
get utility block 2             =10000110110110010001101100111000
get utility block 3             =01110100010101011011111110110101
get utility block 4             =00111011101100011001010011110010
get utility block 5             =11010100110011111000100111100010
get utility block 6             =11101110100001011111010001010011
get utility block 7             =10010001011011000101101011010011
get utility block 8             =10001110010111000011001010111011
get utility block 265           =00001101000000110101001000000001
get utility block 266           =11000100010111010111011011111101
get utility block 267           =00000100110101111001100110111110
get utility block 268           =01000000100110101010011000111100
get utility block 269           =01001100010101101010011001100011
get utility block 270           =11100000010000000100100000111000
get utility block 271           =10001000000101000001110001010101
get utility block 272           =11101011100101100011100010011001
```

<!-- 语法节 end -->

## 是什么

**`GetUtilityLines` 是把 utility line 的当前状态读出来、打进 report window 的 L2 test method。** 原文第一句就是全部动作：

> 「This test method reads the states of up to 512 utility lines and displays the state in report window.」

**两个动作、一个规模**：

| 词 | 说的是什么 |
|---|---|
| `reads the states of up to 512 utility lines` | **读状态**（读，不写） |
| `displays the state in report window` | **落点是 [[report-window]]**——**不是返回值**（至少本篇没写返回值） |
| `up to 512 utility lines` | **规模上限 512 条** |

### 两个 `Note`（原文里都被压平成了正文的普通句子）

原文紧跟着两条提示，**两处都被压平成正文的普通句子，而且两处形态还不一样**
（raw 里的形态见「出处」⚠️ ③）：

> 「 It is only available for universal test method.」

> 「Note When using this test method, the primary sets specified in this test suite are not used.
> The primary sets of the previously executed test suite are used.」

**第二条是本页最容易被忽略、后果最脏的一条**：

| 你以为 | 实际 |
|---|---|
| 用**本**test suite 里配置的 `primary set` | **不用**——原文 `are not used` |
| —— | **用「上一次执行过的 test suite」的 `primary set`**（`The primary sets of the previously executed test suite are used.`） |

**⚠️ `primary set` 是什么，本篇没有定义**（见「和谁有关」）——
**本页只照原文记下这个继承规则，不替它解释语义。**

### 除了 report window，还有一条 GUI 路

> 「You can view the status of the utility lines in the Utility Line view of 93000 Hardware perspective.」

**所以同一个状态有两个入口**：这个 test method（进 testflow 里读），
与 `Utility Line view`（在 `93000 Hardware perspective` 里看）——见 [[utility-line-view]]。

### 唯一的参数 `blockId`（INT）：三个取值区间

`blockId` 是**唯一的参数**，它的说明也是一格里塞了四种情形（逐字见「语法 / 参数」节）：

| 写法 | 有效范围 | 原文要点 |
|---|---|---|
| **默认（不写三位块号）** | **0 – 8** | 「The valid value is from 0 to 8.」 |
| **三位块号格式** | **165 ... 172** | 「If the three鈥慸igit format for pogo blocks is used, the valid range is 165 ... 172.」（**坏字照原样引，见「出处」⚠️ ①**） |
| **第二块可选 [[utility-card]]**（EXA Scale 系统） | **`265` ... `272`** | 「the utility pogo blocks can be defined using only the three鈥慸igit format」（**坏字照原样引**，见「出处」⚠️ ①） |
| **`0` 的含义** | —— | 「0 means all utility line blocks and other valid number means the specified utility block.」 |

**读这张表的三个要点：**

1. **`0` 不是「第一块」，是「全部」**——原文用的是 `all utility line blocks`。
2. **第二块卡只能用三位格式**（`using only`）——**这一条是硬约束，不是建议**。
3. **两个区间的长度一样、都对得起来**：`1…8` 与 `165…172` 各 8 个值，`265…272` 也是 8 个
   （**推断，依据是这三个区间的端点本身**；原文没有把「8」这个数单独写成一句话）。

### 输出长什么样：每块一行、每行 32 位

原文 `## Example` 给了一整段输出，**16 行**（块 `1`–`8` 与 `265`–`272`），每行形如：

```
get utility block 1             =01111100101110100100010010011010
```

**每行等号后面是 32 个二进制位**（**本页数过**：这一行是 32 个字符，全部由 `0` / `1` 组成）。

> **（推断）「up to 512」这个上限是这么来的：16 块 × 32 位 = 512。**
> 依据是 ① 原文首句的 `up to 512`；② 示例输出的 16 行（`1`–`8` 与 `265`–`272`）；
> ③ 每行 32 位。**本篇没有写「每块多少条 utility line」这句话**，所以这只是把三个可见的数乘起来，**不是文档事实**。

**示例的标题与正文**（逐字）：

> 「Output with parameter blockId of the test method set to 0. The pogo blocks of the second optional Utility Card are listed as 265 to 272.」

（原句前有一个行首空格、`Utility Card` 是链接，本页按 §11.1 ①② 处理。）
**它顺带证明了一件事**：**`blockId = 0` 确实会把第二块卡的块号（265–272）一起读出来**
（推断，依据就是这一段说明与它下面那 16 行输出）。

## 典型用法

**本篇没有 `## Procedure` / `## Before you begin` / `## What to do next`**——
它是一篇 test method 参考，**只有一个 `## Parameters` 与一个 `## Example`**。能落成动作的只有这些：

| 要做的 | 怎么做 | 依据 |
|---|---|---|
| **读全部 utility line block 的状态** | `blockId = 0` | 「0 means all utility line blocks and other valid number means the specified utility block.」+ 示例标题逐字 `set to 0` |
| 只读某一块 | 给 `blockId` 一个有效块号（1–8，或三位格式的 165–172） | 「other valid number means the specified utility block.」 |
| 读**第二块卡**（EXA Scale 系统） | **必须用三位格式**（265–272） | 「can be defined using only the three鈥慸igit format」（**坏字照原样引**，见「出处」⚠️ ①） |
| 看结果 | **去 report window 找** | 首句 `displays the state in report window` |
| 不想跑 test、只想看状态 | 用 `Utility Line view`（GUI） | 「You can view the status of the utility lines in the Utility Line view of 93000 Hardware perspective.」 |

**两个前提，缺一条就不对：**

1. **只能在 universal test method 里用**（`It is only available for universal test method.`）——
   **`universal test method` 是什么，本篇没有定义**（见「和谁有关」）。
2. **`primary set` 用的是「上一次执行过的 test suite」的那一套**，不是本 test suite 的
   （逐字见上一节）。**这一条不是「怎么调」的问题，是「调出来的数为什么和你想的不一样」的问题。**

**读 / 写是两条方法**：本页只读；要改状态用 [[set-utility-lines]]
（互见关系原文写在两篇各自的 `## Related information` 里）。

## 和谁有关

- [[set-utility-lines]] —— **写侧，也是本页唯一的同族方法**。两篇互为 `## Related information`，逐字：
  > 「GetUtilityLines: Gets the status of the utility lines」
  > 「SetUtilityLines: Sets the status of the utility lines」
  （这两句来自 `02.07.05.04_Miscellaneous_test_methods__miscellaneous_tml.md` 的入边；
  **本页那一篇的 `## Related information` 里写的是** `SetUtilityLines` 与 `GET_UTILITY_LINES_STATUS`
  **两条首尾相接的链接**，见「出处」⚠️ ④。）
- [[flex-relay]] —— **另一条控制 utility line 的 L2 路**。它出现在 [[set-utility-lines]] 那一篇的
  `## Related information` 里（**本页这一篇没有它**）。**它怎么用不在本页**——
  「task 容器 / 靠 `execute()` 生效」这个说法引自 [[flex-relay]] 那一页，**不是本篇**（**本页未读该页的 raw**）。
- [[utility-line-view]] —— **原文点名的 GUI 入口**：`Utility Line view of 93000 Hardware perspective`。
- [[hardware-view]] —— 原文写的是 **`93000 Hardware perspective`**；**本页没读 [[hardware-view]]**，
  **所以「这个名字与 `Hardware view` 是不是同一件事」本页不判**。
- [[utility-pins-editor]] —— **入边那一侧的原话**（来自 `02.08.04.18.03.01.04_Utility_Pins_editor.md`，本页没读）：
  > 「You can access the utility pins with the test method library (GetUtilityLines and SetUtilityLines), test method API or your own test method.」
  ——**它把本页与 [[set-utility-lines]] 并列为「用 test method library 访问 utility pin」的两条路**。
- [[utility-card]] / [[utility-pogo-block-utility-card-v93000-exa-scale-systems]] ——
  **本篇两处点名的外部文档**：前者讲第二块可选卡，后者的 `Utility pogo block mapping` 一节讲块号怎么映射。
  **两篇本页都没读**——所以 **`165…172` / `265…272` 这些块号具体对应 DUT 板上哪些 pogo，本页不知道**。
- [[report-window]] —— **输出落点**（首句）。**本页没读它**，所以「为什么有些行没打出来」这类问题本页答不了。
- [[test-suite]] —— **那条 `primary set` 继承规则的双方**（`this test suite` 与 `the previously executed test suite`）。
- `primary set` —— **用反引号写，不链**：**本篇没有定义它是什么**
  （allowlist 里最接近的是 `pals`，但那一页的标题是 `PALS, PALS? - (Pin ALlocation for multiple Sites)`，
  **字面就对不上**，**本页不据词面去接那一页**）。
- `universal test method` —— 同一条纪律：**本篇只写了这个限定，没有定义它**。
  allowlist 里名字最近的是 [[universal-test-method-library]]，**但那一页的标题是
  `Developing a universal test method library`（讲怎么开发一个库）**——
  **和本篇这句限定是不是一回事，本页不判**。
- `GET_UTILITY_LINES_STATUS` —— **本篇 `## Related information` 的另一半**（那个名字**不在 allowlist 里，用反引号**）。
  **本篇没说它和本页是什么关系**（名字看着是另一条 API），**本页没读它，也不替它定性**。
- [[udut]] / [[udup]] —— **（推断）utility line 在 L1 侧的撤销命令**（页标题分别是
  `UDUT - (UnDefine UTility line)` 与 `UDUP - (UnDefine Utility Purpose)`）。
  **本篇一个字没提过它们**，列在这一节只为提醒「改 utility line 不只 L2 一条路」——
  **这两页本页都没读**，它们怎么用、和本页什么关系，**本页不知道**。
- [[utility-lines]] / [[sequencer-controlled-utility-lines]] —— **utility line 的概念页与 sequencer 控制页**。
  **本篇没有提过 sequencer 控制**（实测 `sequencer` 0 命中），**本页不据词面接那一页**；
  列在这里是说明本页的读者可能还需要它们（**两页本页都没读**）。
- [[pin]] —— **本阶段（`stage: pin`）的脊椎页**。

## 版本

`## Functional changes` 段有，**三条**（逐字，放在代码块里以免误改标点）：

```
- Introduced in SmarTest 6.5.2
- SmarTest 7.2.1: The maximum number of utility lines increases to 256.
- SmarTest 7.10.2: Maximum 512 utility lines and three鈥慸igit utility pogo block designator.
```

**三条连起来是一条「上限抬升史」**：

| 版本 | 上限 | 备注 |
|---|---|---|
| **6.5.2** | **引入**（取值未写） | 措辞是 `Introduced in`，**不是哨兵值**（对照 §11.2 ②） |
| **7.2.1** | **256** | 「increases to 256」 |
| **7.10.2** | **512**，且**块号支持三位格式** | 与首句 `up to 512` 对得上 |

> ⚠️ **第三条的措辞和第二条不一样，本页照实并列、不替它们统一**：
> 7.2.1 那条是**完整句**（`The maximum number of utility lines increases to 256.`），
> 7.10.2 那条是**名词短语**（`Maximum 512 utility lines and three鈥慸igit utility pogo block designator.`，**没有动词**）。
> **两处都带坏字，见「出处」⚠️ ①。**

## 出处

`sources:` 一篇：
`02_System_reference/02.07_Test_Method_Reference/02.07.05.04.05_GetUtilityLines.md`
（TDC `111063.htm`，**3,125 字节 / 81 行**）。**整篇读完**——本页引文全部来自这一篇 + `edges.jsonl` 里带原句的边。

**入边 7 条 / 5 篇**（`inline` + `toc` 口径）：
`02.07.05.04_Miscellaneous_test_methods__miscellaneous_tml`（2 条）、
`02.07.02.08_List_of_predefined_universal_test_methods`、
`02.07.04.01.108_GET_UTILITY_LINES_STATUS`、`02.07.05.04.07_SetUtilityLines`、
`02.08.04.18.03.01.04_Utility_Pins_editor`、`02_System_reference/index.md`。

**本页没做的**：

- **`## Parameters` 之外的四篇引用文档一篇没读**：`Utility Card`、`Utility pogo block - Utility Card (V93000 EXA Scale systems)`
  （含它的 `Utility pogo block mapping` 锚点）、`SetUtilityLines`、`GET_UTILITY_LINES_STATUS`。
  **所以块号 → pogo 的对应关系、以及 `GET_UTILITY_LINES_STATUS` 是什么，本页一个字没有。**
- **`Utility Line view` / `93000 Hardware perspective` 两篇没读**（只读了 [[utility-line-view]] 那一页的**页标题**）。
- **`Miscellaneous test methods (miscellaneous_tml)` 那篇没读**——**本页引它的那两句，
  引的是 `edges.jsonl` 里带原句的边**，**没有回原文核上下文**。
- **`[[report-window]]`、`[[test-suite]]`、`[[universal-test-method-library]]`、`[[utility-lines]]`、
  `[[sequencer-controlled-utility-lines]]`、`[[udut]]`、`[[udup]]`、`[[flex-relay]]` 各页都没读**
  （其中 [[flex-relay]] 那一句说法是**照抄它那一页的现有正文**，不是本页的核对结论）。
- **图：本篇没有内嵌图片**——判据可核：本篇 md 里 `.png` / `![` **0 命中**。
- **没有实跑。** 没有在任何机台上调过这个 test method、没有看过 report window 的输出、
  没有数过真机上到底有几条 utility line。`verified: doc-only` 说的就是这件事。
- **没有动 `wiki/index.md`**，也没有把本页挂进 [[pin]]。

> ⚠️ **本篇的语料瑕疵，照实记、一处都没替它改**（§11.2）：
>
> **① 坏字：`three鈥慸igit`，3 处。** 三处**分两段**逐字抄在下面（**坏字照原样留着**；
> 第二行里的 `Utility Card` 本来是 markdown 链接，本页按 §11.1 ② 剥掉了链接标记）。
> **为什么要分成两块**：这三行在原文里**不连续**（前两行在 `## Parameters` 那一格，第三行在
> `## Functional changes`），**本页不把它们拼成一块**（§11.1：块内部必须连续）。
>
> 第一处与第二处（在 `blockId` 那一格里，**中间只隔一个空行**）：
>
> ```
> If the three鈥慸igit format for pogo blocks is used, the valid range is 165 ... 172.
> For the second optional Utility Card of EXA Scale systems, the utility pogo blocks can be defined using only the three鈥慸igit format. The valid range for the second card is `265` ... `272`.
> ```
>
> 第三处（在 `## Functional changes` 段的最后一条里）：
>
> ```
> - SmarTest 7.10.2: Maximum 512 utility lines and three鈥慸igit utility pogo block designator.
> ```
>
> ——**按 §11.2 ①，`鈥慸` 是「三字节字符丢掉第三字节 + 紧随的字母 `d` 被一起吃进去」**，
> 还原出来是 `three-digit`（同一族的口径见 `extract/encoding-map.csv`）。
> **本页没有替它改一个字**——**代价要写清楚：拿修好的 `three-digit` 去 raw 里搜是搜不到的，要搜坏掉的那个形态。**
>
> **② 示例标题的冠词错了。** 逐字：
> `### Output for two utility cards of an V93000 EXA Scale system`
> ——**`an V93000` 应为 `a V93000`**（`V` 不是元音音素）。**本页照原样记。**
> **⚠️ 这一处本页只看到 md**，**没有回上游 `.htm` 核过**——
> 所以**它属于「转换坏的」还是「上游就坏的」，本页判不了**（§11.2 ⑥ 的判据要去看 `.htm`，本页没看）。
>
> **③ 两个 `Note` 标签被压平进正文，而且两处写法不一样。** 逐字：
> 一处**行首还多一个空格** —— ` Note It is only available for universal test method.`
> 一处**没有**那个空格 —— `Note When using this test method, the primary sets specified in this test suite are not used. The primary sets of the previously executed test suite are used.`
> ——**同一个标签、同一篇里两种形态**。本页照实记。
>
> **④ `## Related information` 里两条链接首尾相接、中间没有任何分隔符。** 逐字：
> `[SetUtilityLines](<02.07.05.04.07_SetUtilityLines.md>)[GET_UTILITY_LINES_STATUS](<02.07.04.01.108_GET_UTILITY_LINES_STATUS.md>)`
> ——**`SetUtilityLines` 那条链接的 `>` 后面紧跟 `[GET_UTILITY_LINES_STATUS]`**，
> **渲染出来会是 `SetUtilityLinesGET_UTILITY_LINES_STATUS`**。**本页照实记。**
>
> **⑤ `## Related information` 这一节不在本页「语法 / 参数」节里。** 脚本按段标记抽（§4），
> 那一节收的是 `Parameters` 与 `Example`。**不是脚本漏了**——记在这里，
> 免得读者以为那一节被吞了（本页的「和谁有关」已把它用上）。
>
> **⑥ `Parameters` 表的表头在 raw 里是散的。** 逐字形态是：
> `|` / 空行 / `Parameter` / 空行 / ` |` / 空行 / `Type` / 空行 / ` |` / 空行 / `Description` / 空行 / ` |` / 空行 / ` | blockId  | INT |`
> ——**一个被压平的表**：三个表头格各占一段，**最后一行才把表头行与数据行粘在一起**。
> **说明文字一个字没丢**（本页已把它写成上面那张取值表）。

`verified: doc-only`
