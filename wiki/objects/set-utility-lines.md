---
type: object
title: SetUtilityLines
layer: L2
stage: pin
tags: [pin, testmethod, api, utility-line, utility-pogo-block, universal-test-method, relay, waittime, l2]
related: [get-utility-lines, flex-relay, utility-line-view, hardware-view, utility-pins-editor, utility-purpose-editor, utility-card, utility-pogo-block-utility-card-v93000-exa-scale-systems, test-suite, pin, smartest-6.5.2, smartest-7.2.1, smartest-7.10.2]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.05.04.07_SetUtilityLines.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# SetUtilityLines

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **2,814 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.05.04.07_SetUtilityLines.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Parameters

|

Parameter

 |

Type

 |

Description

 |
 | type  | STRING |

The type of the utility line. It can be:

-

UtilitylineName: The utility line name defined in the `Pin setting editors`（raw: `../02.08_Setup_and_Result_Tools/02.08.04.18.03.01_Pin_setting_editors.md`）.

 The utility lines to be set to on or to off can be defined by parameters

  - utilityLineNameOn,
  - utilityLineNameOff, or
  - utilityPurpose.

All three parameters can be filled with data at the same time.

-

UtilitylineChannel: Utility lines are defined by the channel number.

 The utility channels to be set to on or to off can be defined by parameters

  - utilityLineChannelOn or
  - utilityLineChannelOff.

Both parameters can be filled with data at the same time.

 |
 | utilityLineNameOn  | STRING |

A single utility pin or a comma‑separated list of utility pins to be set to on or to off.

Valid names are defined in the `Utility Pins editor`（raw: `../02.08_Setup_and_Result_Tools/02.08.04.18.03.01.04_Utility_Pins_editor.md`）.

 |
 | utilityLineNameOff |
 | utilityPurpose  | STRING |

A utility purpose or a comma‑separated list of utility purposes to be applied.

Valid names are defined in the `Pin setting editors`（raw: `../02.08_Setup_and_Result_Tools/02.08.04.18.03.01_Pin_setting_editors.md`） and configured in the `Utility Purpose Editor`（raw: `../02.08_Setup_and_Result_Tools/02.08.04.18.03.01.05_Utility_Purpose_Editor.md`）.

 |
 | utilityLineChannelOn  | STRING |

A single utility channel or a comma‑separated list of utility channels to be set to on or to off.

The utility channels are to be defined like `UTI101`, `UTI102`.

The format using three digits for the pogo blocks is also supported. For this format, the utility pins are to be defined as `UTI16501` or `UTI16502`, for example.

For the second optional `Utility Card`（raw: `../02.05_Test_Head_Cards/02.05.08.04_Utility_Card.md`） of EXA Scale systems, the utility pins can be defined only using the three‑digit format of the pogo blocks. The valid range for the second card is `UTI26501` ... `UTI27232`.

See also `Utility pogo block mapping`（raw: `../02.03_DUT_board_design_reference/02.03.06.08.02_Utility_pogo_block_-_Utility_Card__V93000_EXA_Scale_systems.md#_347642__s_Utility_pogo_block_mapping`） in `Utility pogo block - Utility Card (V93000 EXA Scale systems)`（raw: `../02.03_DUT_board_design_reference/02.03.06.08.02_Utility_pogo_block_-_Utility_Card__V93000_EXA_Scale_systems.md`）.

 |
 | utilityLineChannelOff |
 | waittime  | DOUBLE |

The time to wait after controlling all relays. It must not be negative.

Default value is 0.0.

Units are seconds.

 |

For a coding example see the file /opt/hp93000/soc/testmethod/library/miscellaneous_tml/SetUtilityLines.cpp in `Miscellaneous test methods (miscellaneous_tml)`（raw: `02.07.05.04_Miscellaneous_test_methods__miscellaneous_tml.md`）

<!-- 语法节 end -->

## 是什么

**`SetUtilityLines` 是把 utility line 开到 on 或 off 的 L2 test method。** 原文第一句就是全部动作：

> 「This test method sets a maximum of 512 utility lines.」

**规模与写侧的对偶**：本页**写**、[[get-utility-lines]] **读**，
**两篇的首句都以 `512` 收尾**（那一篇是 `reads the states of up to 512 utility lines`，
本篇是 `sets a maximum of 512 utility lines`）。见「和谁有关」。

### 两个 `Note`（原文里都被压平成了正文的普通句子）

> 「 It is only available for universal test method.」

> 「Note When using this test method, the primary sets specified in this test suite are not used.
> The primary sets of the previously executed test suite are used.」

**第二条与 [[get-utility-lines]] 那一篇逐字相同**——**读和写用的是同一套 `primary set` 继承规则**：

| 你以为 | 实际 |
|---|---|
| 用**本**test suite 里配置的 `primary set` | **不用**（原文 `are not used`） |
| —— | **用「上一次执行过的 test suite」的 `primary set`** |

**⚠️ `primary set` 是什么，本篇没有定义**（见「和谁有关」）。

### 另一条路：Utility Line view 的 write mode

> 「You can also change the status of the utility line using the Utility Line view write mode of 93000 Hardware perspective.」

**`also` 这个词点明了两条路并存**：test method（本篇）与 GUI（那个视图的 write mode）。见 [[utility-line-view]]。

### 参数分成**两组**，由 `type` 决定用哪一组

**这是本页最要紧的结构**。`type`（STRING）有两种取值，**两种取值各带一组参数**（逐字见「语法 / 参数」节）：

| `type` 取值 | 这一组里有 | 能不能同时填 | 名字从哪来 |
|---|---|---|---|
| **`UtilitylineName`** | `utilityLineNameOn`、`utilityLineNameOff`、`utilityPurpose` | **三个可以同时填**（「All three parameters can be filled with data at the same time.」） | on/off 名字来自 [[utility-pins-editor]]；purpose 来自 `Pin setting editors` + [[utility-purpose-editor]] |
| **`UtilitylineChannel`** | `utilityLineChannelOn`、`utilityLineChannelOff` | **两个可以同时填**（「Both parameters can be filled with data at the same time.」） | **按 channel 号**，不按名字 |

**原文对两种取值的完整说明**（逐字，去掉链接标记）：

> 「UtilitylineName: The utility line name defined in the Pin setting editors.
> The utility lines to be set to on or to off can be defined by parameters
> - utilityLineNameOn,
> - utilityLineNameOff, or
> - utilityPurpose.
> All three parameters can be filled with data at the same time.」

> 「UtilitylineChannel: Utility lines are defined by the channel number.
> The utility channels to be set to on or to off can be defined by parameters
> - utilityLineChannelOn or
> - utilityLineChannelOff.
> Both parameters can be filled with data at the same time.」

（这两段在 raw 里被拆成很多短行——`-` 列表符**单独占一行**、内容在下一行，见「出处」⚠️ ⑤；
本页按 §11.1 ① 折叠空白后引，**没有增删一个字**。）

**「可以同时填」这一条是本页的实用价值**：**一次调用里能让一部分 line 开、另一部分关**
（推断，依据是这两句 `at the same time` 与本篇把参数成对写成 On / Off 这件事）。

### 两组参数各自的取值格式

| 参数 | 原文对取值的说明 |
|---|---|
| `utilityLineNameOn` | 「A single utility pin or a comma鈥憇eparated list of utility pins to be set to on or to off.」+「Valid names are defined in the Utility Pins editor.」 |
| `utilityPurpose` | 「A utility purpose or a comma鈥憇eparated list of utility purposes to be applied.」+ 名字在 `Pin setting editors` 定义、在 [[utility-purpose-editor]] 配置 |
| `utilityLineChannelOn` | 「A single utility channel or a comma鈥憇eparated list of utility channels to be set to on or to off.」 |

**channel 号有两种写法**（原文逐字）：

> 「The utility channels are to be defined like UTI101, UTI102.」

> 「The format using three digits for the pogo blocks is also supported. For this format, the utility pins are to be defined as UTI16501 or UTI16502, for example.」

| 写法 | 例子 | 段数 |
|---|---|---|
| **块号两位** | `UTI101`、`UTI102` | 块 `1` / `01`…`02` |
| **块号三位** | `UTI16501`、`UTI16502` | 块 `165` / `01`…`02` |
| **第二块可选 [[utility-card]]**（EXA Scale 系统） | `UTI26501` ... `UTI27232` | **只能用三位格式**（`can be defined only using`） |

> **（推断）末两位是「块内第几条」**，依据是：① `UTI27232` 的末两位是 **`32`**；
> ② [[get-utility-lines]] 那一篇的示例输出**每块一行、每行 32 个二进制位**（本页的数法见那一页）。
> **本篇没有写「一块 32 条」这句话**，所以这是两个可见数字的合读，**不是文档事实**。

### `waittime`：控制完之后等一会儿

四件事，逐字（原文四句）：

> 「The time to wait after controlling all relays. It must not be negative.」
> 「Default value is 0.0.」
> 「Units are seconds.」

| 要点 | 原文 |
|---|---|
| **时机** | **控制完所有 relay 之后**（`after controlling all relays`） |
| **取值** | **不许为负**（`must not be negative`） |
| **默认** | **`0.0`** ——**不写就是不等待** |
| **单位** | **秒**（`seconds`）**——不是毫秒** |

**⚠️ 两处本篇没写**：① **正值上限有没有**（`must not be negative` 只划了下界）；
② **负值会怎样**（报错？当 0 处理？）——**语料未写，本页不填**。

### 本篇没有 `## Example`，只有一个 `.cpp` 的指针

原文最后一行（在「语法 / 参数」节的末行，**不在任何段标记底下**）：

> 「For a coding example see the file /opt/hp93000/soc/testmethod/library/miscellaneous_tml/SetUtilityLines.cpp in Miscellaneous test methods (miscellaneous_tml)」

**即：本篇给不出可抄的调用串**，**唯一的代码示例在那个 `.cpp` 里**（**本页没读它，也没读那篇文档**，见「出处」）。

## 典型用法

**本篇没有 `## Procedure` / `## Before you begin` / `## What to do next`，也没有 `## Example`**——
能落成动作的全部来自 `## Parameters` 那张表。**按目的查**：

| 要做的 | 填哪个参数 | 依据 |
|---|---|---|
| **按名字**把某些 utility line 打开 | `type = UtilitylineName` + `utilityLineNameOn` | 「A single utility pin or a comma鈥憇eparated list of utility pins to be set to on or to off.」 |
| **按名字**关掉某些 | `type = UtilitylineName` + `utilityLineNameOff` | 参数名本身（**说明见「出处」⚠️ ④**） |
| **按 purpose** 开/关一批 | `type = UtilitylineName` + `utilityPurpose` | 「A utility purpose or a comma鈥憇eparated list of utility purposes to be applied.」 |
| **按 channel 号**开 / 关 | `type = UtilitylineChannel` + `utilityLineChannelOn` / `utilityLineChannelOff` | 「Utility lines are defined by the channel number.」 |
| **开一批、同时关另一批** | on / off 两个参数**同时填** | 「All three parameters can be filled with data at the same time.」/「Both parameters can be filled with data at the same time.」 |
| **继电器的状态稳定下来再往下走** | `waittime`（正数，秒；默认 `0.0`） | 「The time to wait after controlling all relays. It must not be negative.」+「Units are seconds.」 |
| 看结果 | **去 report window / `Utility Line view` 看** | 建议（**不是本篇的话**）：本篇只写了那条 GUI 路（`You can also change the status of the utility line using the Utility Line view write mode of 93000 Hardware perspective.`），**读回状态要用 [[get-utility-lines]]** |

**两个前提，缺一条就不对：**

1. **只能在 universal test method 里用**（`It is only available for universal test method.`）——
   **`universal test method` 是什么，本篇没有定义**。
2. **`primary set` 用的是「上一次执行过的 test suite」的那一套**，不是本 test suite 的——
   **与 [[get-utility-lines]] 同一条规则、逐字相同。**

**⚠️ 本页给不出「一行代码长什么样」**：本篇没有 `## Example`，
**要抄代码只能去看那个 `.cpp`**（见「出处」）。

## 和谁有关

- [[get-utility-lines]] —— **读侧**。两篇互为 `## Related information`，逐字：
  > 「GetUtilityLines: Gets the status of the utility lines」
  > 「SetUtilityLines: Sets the status of the utility lines」
  （两句来自 `02.07.05.04_Miscellaneous_test_methods__miscellaneous_tml.md` 的入边；
  **本篇自己的 `## Related information` 里写的是** `GetUtilityLines` 与 `FLEX_RELAY`
  **两条首尾相接的链接**，见「出处」⚠️ ⑥。）
- [[flex-relay]] —— **另一条控制 utility line 的 L2 路**（本页 `## Related information` 点名的第二个）。
  **它怎么用不在本页**——「task 容器 / 靠 `execute()` 生效」这个说法引自 [[flex-relay]] 那一页的现有正文，
  **不是本篇**（**本页未读该页的 raw**）。**两边的分工本篇一个字没说**，本页不替它们分。
- [[utility-pins-editor]] —— **`utilityLineNameOn` 的名字来源**（「Valid names are defined in the Utility Pins editor.」）。
  入边那一侧还有一句把本页与 [[get-utility-lines]] 并列的话（来自 `02.08.04.18.03.01.04_Utility_Pins_editor.md`，本页没读）：
  > 「You can access the utility pins with the test method library (GetUtilityLines and SetUtilityLines), test method API or your own test method.」
- [[utility-purpose-editor]] —— **`utilityPurpose` 的配置处**（「configured in the Utility Purpose Editor.」）。
- `Pin setting editors` —— **用反引号写，不链**（这个名字**不在 allowlist 里**；raw:
  `../02.08_Setup_and_Result_Tools/02.08.04.18.03.01_Pin_setting_editors.md`）。
  它在本篇里出现**两次**：一次在 `type` 的说明里（`UtilitylineName` 的定义处），一次在 `utilityPurpose` 那格。
  **注意本篇的写法是小写 `s`**（`Pin setting editors`）。
- [[utility-line-view]] —— **原文点名的 GUI 路**（`Utility Line view write mode`）。
- [[hardware-view]] —— 原文写的是 **`93000 Hardware perspective`**；**本页没读 [[hardware-view]]**，
  **所以「这个名字与 `Hardware view` 是不是同一件事」本页不判**。
- [[utility-card]] / [[utility-pogo-block-utility-card-v93000-exa-scale-systems]] ——
  **本篇两处点名的外部文档**（第二块可选卡、pogo block 映射）。**两篇本页都没读**——
  **`UTI16501` / `UTI26501` 这些编号具体对应 DUT 板上哪些 pogo，本页不知道**。
- [[test-suite]] —— **那条 `primary set` 继承规则的双方**（`this test suite` 与 `the previously executed test suite`）。
- `primary set` —— **用反引号写，不链**：**本篇没有定义它是什么**
  （最接近的 allowlist 名字是 `pals`，但那一页标题是 `PALS, PALS? - (Pin ALlocation for multiple Sites)`，
  **字面就对不上**，**本页不据词面去接那一页**）。
- `universal test method` —— 同一条纪律：**本篇只写了这个限定，没有定义它**。
  名字最近的是 [[universal-test-method-library]]，**但那一页的标题是
  `Developing a universal test method library`（讲怎么开发一个库）**——
  **和本篇这句限定是不是一回事，本页不判**。
- `Miscellaneous test methods (miscellaneous_tml)` —— **用反引号写，不链**（那个名字**不在 allowlist 里**）。
  本篇最后一行把 `.cpp` 示例指向它；**本页没读它**。
- [[udut]] / [[udup]] —— **（推断）utility line 在 L1 侧的撤销命令**（页标题分别是
  `UDUT - (UnDefine UTility line)` 与 `UDUP - (UnDefine Utility Purpose)`）。
  **本篇一个字没提过它们**；列在这里只为提醒「utility line 不只 L2 这一条路」——
  **这两页本页都没读**。
- [[utility-lines]] / [[sequencer-controlled-utility-lines]] —— **utility line 的概念页与 sequencer 控制页**。
  **本篇没有提过 sequencer**（实测 `sequencer` 0 命中），**本页不据词面接那一页**；
  列在这里是说明本页的读者可能还需要它们（**两页本页都没读**）。
- [[pin]] —— **本阶段（`stage: pin`）的脊椎页**。

## 版本

`## Functional changes` 段有，**三条**（逐字，放在代码块里以免误改标点）：

```
- Introduced in SmarTest 6.5.2
- SmarTest 7.2.1: The maximum number of utility lines increases to 256.
- SmarTest 7.10.2: Maximum 512 utility lines and three鈥慸igit utility pogo block designator.
```

**三条与 [[get-utility-lines]] 那一篇逐字相同**（同一族的两个方法，同一串版本记录）。
**第二条与第三条的措辞不一样**（一句是完整句、一句是名词短语），见那一页的 ⚠️。
**7.10.2 那一条是本篇 `UTI16501` 这种写法的来处**：那一条里写的是坏字 `three鈥慸igit`
（= `three-digit`，照原样引，见「出处」⚠️ ①）+ `pogo block designator`——
**即「三位块号」是 7.10.2 起才有的**（**推断**，依据是这一条与 `utilityLineChannelOn` 那格的
`The format using three digits for the pogo blocks is also supported.` 对读；**本篇没有把这两处连起来写**）。

## 出处

`sources:` 一篇：
`02_System_reference/02.07_Test_Method_Reference/02.07.05.04.07_SetUtilityLines.md`
（TDC `111065.htm`，**3,861 字节 / 109 行**）。**整篇读完**——本页引文全部来自这一篇 + `edges.jsonl` 里带原句的边。

**入边 6 条 / 5 篇**（`inline` + `toc` 口径）：
`02.07.05.04_Miscellaneous_test_methods__miscellaneous_tml`（2 条）、
`02.07.02.08_List_of_predefined_universal_test_methods`、`02.07.05.04.05_GetUtilityLines`、
`02.08.04.18.03.01.04_Utility_Pins_editor`、`02_System_reference/index.md`。

**本页没做的**：

- **`set-utility-lines.cpp`（`/opt/hp93000/soc/testmethod/library/miscellaneous_tml/SetUtilityLines.cpp`）没看**——
  **所以本页一个调用示例都给不出来**，连「参数怎么摆」都不知道。
- **`Miscellaneous test methods (miscellaneous_tml)` 那篇没读**（`.cpp` 就在它名下）。
- **`Pin setting editors` 与 [[utility-purpose-editor]] 两篇 GUI 文档没读**——
  所以**「合法的 utility pin 名 / purpose 名长什么样」本页一个字没有**。
- **`[[utility-pins-editor]]`、`[[utility-line-view]]`、`[[hardware-view]]`、`[[report-window]]` 各页没读**
  （只读了它们的**页标题**）。
- **`[[get-utility-lines]]` 那篇 raw 读了**（它是本页的姊妹篇），**其余四条入边文档没读**：
  本页引它们的话，只引 `edges.jsonl` 里带原句的边，**没有回原文核上下文**。
- **图：本篇没有内嵌图片**——判据可核：本篇 md 里 `.png` / `![` **0 命中**。
- **没有实跑。** 没有在任何机台上发过这个 test method、**没有真的开 / 关过一条 utility line**、
  没有量过 `waittime` 到底等了多久、没有触发过任何一条约束。
  §11 那句「文档里有 ≠ 你这台能用」在这一页尤其要记住——**utility line 是接 DUT 板继电器的，
  动它之前先看现场**。`verified: doc-only` 说的就是这件事。
- **没有动 `wiki/index.md`**，也没有把本页挂进 [[pin]]。

> ⚠️ **本篇的语料瑕疵，照实记、一处都没替它改**（§11.2）：
>
> **① 坏字：`comma鈥憇eparated`，3 处；`three鈥慸igit`，1 处。**
> 四处**分开逐字抄**（**坏字照原样留着**；第四、五两行里的 `Utility Card` 本来是 markdown 链接，
> 本页按 §11.1 ② 剥掉了链接标记）。
> **为什么一处分一块**：这四处在原文里**互不相邻**（三行在三个不同的参数格里，最后一行在
> `## Functional changes`），**本页不把它们拼成一块**（§11.1：块内部必须连续）。
>
> `utilityLineNameOn` 那一格：
>
> ```
> A single utility pin or a comma鈥憇eparated list of utility pins to be set to on or to off.
> ```
>
> `utilityPurpose` 那一格：
>
> ```
> A utility purpose or a comma鈥憇eparated list of utility purposes to be applied.
> ```
>
> `utilityLineChannelOn` 那一格：
>
> ```
> A single utility channel or a comma鈥憇eparated list of utility channels to be set to on or to off.
> ```
>
> 同一个 `utilityLineChannelOn` 格的另一段（**在原文里它前面还隔着两句**——
> 「The utility channels are to be defined like `UTI101`, `UTI102`.」与三位格式那句——
> **所以它和上面那一段也不是连续的行**，本页另起一块）：
>
> ```
> For the second optional Utility Card of EXA Scale systems, the utility pins can be defined only using the three鈥慸igit format of the pogo blocks. The valid range for the second card is `UTI26501` ... `UTI27232`.
> ```
>
> `## Functional changes` 段的最后一条：
>
> ```
> - SmarTest 7.10.2: Maximum 512 utility lines and three鈥慸igit utility pogo block designator.
> ```
>
> ——**按 §11.2 ①**：`鈥憇` 还原出来是 `-s`（**短横把紧随的 `s` 一起吃进去了**），
> 所以 `comma鈥憇eparated` = **`comma-separated`**；`鈥慸` = **`‑d`**，
> 所以 `three鈥慸igit` = **`three-digit`**（同一族的口径见 `extract/encoding-map.csv`）。
> **本页没有替它改一个字**——**要搜 raw，得搜坏掉的那个形态。**
>
> **② `UtilitylineName` / `UtilitylineChannel` 里的 `l` 是小写。** 逐字两处：
> `UtilitylineName: The utility line name defined in the Pin setting editors.`
> `UtilitylineChannel: Utility lines are defined by the channel number.`
> ——**而同一张表里的参数名写的是 `utilityLineNameOn` / `utilityLineChannelOn`（`L` 大写）**。
> **一个名字、同一篇里两种大小写。**（§11 明令「命令大小写敏感，原样保留」——
> 所以本页两处都照原样写，**不替它统一**；**做题时该按哪个写，本篇没有说，本页不判**。）
>
> **③ 两个 `Note` 标签被压平进正文，而且两处写法不一样。** 逐字：
> 一处**行首还多一个空格** —— ` Note It is only available for universal test method.`
> 一处**没有**那个空格 —— `Note When using this test method, the primary sets specified in this test suite are not used. The primary sets of the previously executed test suite are used.`
> （**第二条那整句与 [[get-utility-lines]] 那一篇逐字相同**——两篇的提示是同一段话。）
>
> **④ 两个 `…Off` 参数只有名字，没有类型、没有说明。** 逐字（`Parameters` 表里的两行）：
> ` | utilityLineNameOff |`
> ` | utilityLineChannelOff |`
> ——**它们后面既没有 `STRING`，也没有任何描述文字**（同表的 `…On` 参数都有）。
> **所以「Off 参数怎么用」本篇要靠参数名去猜**（推断，依据是 `utilityLineNameOn` 那句说明写的是
> `to be set to on or to off`——**它把 on / off 两种都写进去了，所以空着的那一格大概就是同一句话的另一半**）。
> **本页不替它补描述。**
>
> **⑤ `type` 那几段里的 `-` 列表符独占一行。** raw 里是「`-` / 空行 / 内容」这种形态
> （所以骨架的「语法 / 参数」节里会出现一个**后面什么都没有的 `-` 项**）。
> **这不是脚本切坏，是 raw 如此**；本页在「是什么」里折叠空白后引了那两段，**没有增删内容**。
>
> **⑥ `## Related information` 里两条链接首尾相接、中间没有任何分隔符。** 逐字：
> `[GetUtilityLines](<02.07.05.04.05_GetUtilityLines.md>)[FLEX_RELAY](<02.07.04.01.68_FLEX_RELAY.md>)`
> ——**渲染出来会是 `GetUtilityLinesFLEX_RELAY`**。**本页照实记。**
>
> **⑦ `## Related information` 这一节不在本页「语法 / 参数」节里。** 脚本按段标记抽（§4），
> 那一节收的**只有 `Parameters`**（本篇没有 `Example`）。**不是脚本漏了**——
> 记在这里，免得读者以为那一节被吞了（本页的「和谁有关」已把它用上）。
>
> **⑧ `Parameters` 表的表头在 raw 里是散的**（`Parameter` / `Type` / `Description` 各占一段，
> 最后才与 `type` 那一行粘在一起）——**同一个毛病在 [[get-utility-lines]] 那一篇里也有**，
> **两篇的压平形态一样**。**说明文字一个字没丢。**

`verified: doc-only`
