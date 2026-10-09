---
type: object
title: EQFS - (EQuation FileS command transfer)
layer: L1
stage: timing
tags: [timing, level, equation-based, load-save, firmware-command, editor-tool]
related: [timing, level, level-equation-file, timing-equation-set, timing-file, eqsp, spec-tool, report-window, equation-based-level-setup, mapping-timing, smartest-6.3.2]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.09_EQFS_-__EQuation_FileS_command_transfer.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# EQFS - (EQuation FileS command transfer)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,407 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.05.02.09_EQFS_-__EQuation_FileS_command_transfer.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
EQFS {spec_type}, {part}, {operation},{"eqn_filename"}, ["error_filename"]
```

### Parameters

| spec_type | Which specification to use: | Which specification to use: |
|---|---|---|
| spec_type | LEV | to specify levels, or |
| spec_type | TIM | to specify timing. |
| part | Which part of the specification type to use: | Which part of the specification type to use: |
| part | WVT | to specify wavetable (only for spec_type = TIM), |
| part | EQN | to specify equations, or |
| part | SPS | to specify specs. |
| part | operation | Use LOAD or SAVE. |
| eqn_filename | The absolute filename of the temporary equation based timing file. | The absolute filename of the temporary equation based timing file. |
| error_filename | The absolute filename of the file to which error reports are written.<br><br>Use UI_REPORT to direct error reports to the report window.<br><br>If this parameter is not specified, only a summarized error message is reported. | The absolute filename of the file to which error reports are written.<br><br>Use UI_REPORT to direct error reports to the report window.<br><br>If this parameter is not specified, only a summarized error message is reported. |

> ⚠️ 转录说明（非原文）：本表在上游 HTML 里含合并格（colspan / rowspan）；
> 跨格文字已按覆盖范围重复写出（**不是原表里有重复的格子**）。真结构见 `tdc-html/raw/98592_2.htm`。

### Example

```
EQFS LEV,EQN,LOAD,"/tmp/level_equation",
```

This example loads the level equation file from /tmp/level_equation.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.05.02.09_EQFS_-__EQuation_FileS_command_transfer.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

- eqn_filename does not exist.
- error_filename does not exist.

<!-- 报错节 end -->

## 是什么

**`EQFS` 是一条 L1 固件命令，做的是「整块搬运」：把 equation based 的配置在临时文件和编辑器之间 load / save。**
原文第一句就是它的完整定义：

> 「The EQFS command provides the load/save operations required by the editor tools for loading/saving the equation based testing files from/to temporary files.」

**拆开这句话的三个要点，就是本页的全部：**

| 要点 | 原文里的词 | 意思 |
|---|---|---|
| **它是干什么的** | `load/save operations` | **只有搬，没有编**——它不定义方程、不定义 spec，只是把**整块**搬进搬出 |
| **谁在用它** | `required by the editor tools` | **调用者是编辑器工具**（见下） |
| **搬的是什么** | `equation based testing files` 与 `from/to temporary files` | **equation based 的测试配置**，而且**经手的是「临时文件」（temporary files）** |

**最后那个 `temporary` 很要紧**：`EQFS` 不是「把配置存成正式 setup file」的那一步，
它是**编辑器与临时文件之间的那一趟**。**临时文件后来怎么变成正式 setup file，本篇没写**（见「出处」）。

### 谁在调它 —— 原文有一节专门回答（`## Application`）

> 「- Editor tools」

> 「- The Spec tool」

**这是本页最值钱的一条信息**：**`EQFS` 的调用者是 GUI 侧的编辑器工具本身**——
不是「测试工程师在 hpt 里手敲的命令」，而是**编辑器按按钮时走的 L1 通路**。
**这一点让它在三层对照里有一格很硬的位置**（见「和谁有关」的 [[mapping-timing]]）。

> ⚠️ **注意 `## Application` 这一节不在本页的「语法 / 参数」节里。**
> 本篇的语法节只抽了 `## Syntax` / `## Parameters` / `## Example` 三段
> （脚本口径如此，**本页没改它**），**`## Application` 与 `## Errors` 两条都在语法节之外**
> （后者被抽进了本页的「报错条件」节）。**本页在正文里把 `## Application` 引一次。**

### 三个参数位是三张取值表

| 位置 | 参数 | 取值 | 原文 |
|---|---|---|---|
| 1 | `spec_type` | **`LEV`**（levels）/ **`TIM`**（timing） | `Which specification to use:` |
| 2 | `part` | **`WVT`** / **`EQN`** / **`SPS`** | `Which part of the specification type to use:` |
| 3 | `operation` | **`LOAD`** / **`SAVE`** | `Use LOAD or SAVE.` |
| 4 | `eqn_filename` | **绝对路径** | `The absolute filename of the temporary equation based timing file.` |
| 5 | `error_filename` | **绝对路径**，或 **`UI_REPORT`** | 见下 |

**第 2 位的三张取值各自带一句限制**（原文逐字）：

- `WVT` —— **`to specify wavetable (only for spec_type = TIM),`**
- `EQN` —— `to specify equations, or`
- `SPS` —— `to specify specs.`

> **`(only for spec_type = TIM)` 是这一层唯一的组合限制**：
> **`LEV,WVT` 这一格不存在。**2 × 3 = 6 种组合里，**合法的只有 5 种**。

### `error_filename` 的三种行为（这部分原文写得比别处细）

原文给了三句：

> 「The absolute filename of the file to which error reports are written.」

> 「Use UI_REPORT to direct error reports to the report window.」

> 「If this parameter is not specified, only a summarized error message is reported.」

| 你写什么 | 结果 |
|---|---|
| **一个绝对路径** | 错误报告**写进那个文件** |
| **`UI_REPORT`** | 错误报告**进 report window** |
| **不写这个参数** | **只有一条汇总错误信息**（细节丢掉） |

**这是一个「调试时该加、平时可以省」的参数**——省掉它不会失败，只是报错变粗。

### 报错条件只有两条（**逐字见本页上方「报错条件」节，本页不重复**）

两条都是「文件不存在」：**`eqn_filename` 不存在**、**`error_filename` 不存在**。
**原文没有区分 `LOAD` 与 `SAVE`**——
**`SAVE` 时目标文件是否也要求已经存在，本篇没说**（见「出处」）。
**第二条尤其反直觉**：如果 `error_filename` 是**要写进去的那个文件**，
那「不存在就报错」意味着**得先把那个文件建出来**——**原文就这一句，本页不替它补。**

### 一条必须显式记的「别混」

**`EQFS` ≠ `EQSP`。**两条名字只差一个字母、同属 equation based 配置这一族：

| | 干什么 |
|---|---|
| **`EQFS`**（本页） | **编辑器与临时文件之间的 load / save**（`## Application` 段点名的调用者是编辑器工具） |
| **`EQSP`**（[[eqsp]]，**本页未读**） | 把 setup 数据在 setup file 与测试机之间下载 / 上传——**本页对它的全部认知来自 [[mapping-timing]]** |

## 典型用法

### 原文只给了一个例子

`## Example` 段一共两行：

```
EQFS LEV,EQN,LOAD,"/tmp/level_equation",
```

> 「This example loads the level equation file from /tmp/level_equation.」

**读这一行时注意三件事：**

1. **它是 `LEV,EQN,LOAD`**——`spec_type` / `part` / `operation` 三位各取了什么值，一目了然。
2. **路径是绝对路径**（`/tmp/level_equation`），和参数说明里 `The absolute filename of the temporary equation based timing file.` 对得上。
3. **这一行末尾多一个逗号**（第三个参数位空着、逗号还在）。
   **上游 `98592.htm` 里就是这个带逗号的写法**（实测）——**原文如此，本页照原样引**（见「出处」瑕疵②）。

### 其余组合（**按三张取值表拼的，原文没给例子——这是本页的推断**）

**下面这张表里只有第一行是原文的例子**，其余四行是**按 `spec_type` / `part` / `operation`
三张取值表拼出来的**（依据：`part` 那一格逐字写了 `WVT` / `EQN` / `SPS` 各是什么、
`operation` 那一格写了 `Use LOAD or SAVE.`）。
**原文没有给它们的例子，本页不声称它们都试过。**

| 目的 | 命令（**除第一行外均为（推断）**） |
|---|---|
| **载入 level 方程式文件** | `EQFS LEV,EQN,LOAD,"<绝对路径>"` ← **原文的例子** |
| 存 level 方程式文件 | `EQFS LEV,EQN,SAVE,"<绝对路径>"` |
| 载入 timing 方程式文件 | `EQFS TIM,EQN,LOAD,"<绝对路径>"` |
| 载入 timing spec 文件 | `EQFS TIM,SPS,LOAD,"<绝对路径>"` |
| 载入 timing wavetable | `EQFS TIM,WVT,LOAD,"<绝对路径>"` |
| **让错误报告进 report window** | 末参数写 `"UI_REPORT"`（**这一条是原文的**：`Use UI_REPORT to direct error reports to the report window.`） |

**`LEV,WVT` 那一格不存在**——`WVT` 原文写着 `only for spec_type = TIM`。
**所以 6 种组合里合法的是 5 种**（`LEV` 两种 + `TIM` 三种）。

### 顺序 / 前提

**本篇没有 `## Procedure`、没有 `## Before you begin` 段**（这是事实，不是本页漏读）——
**所以「先干什么再 `EQFS`」本篇一个字没写。**
本篇给得出来的只有两条事实：

- **调用者是编辑器工具**（`## Application`）——所以**人一般不会直接敲它**；
- **文件必须已经存在**（`## Errors` 两条）——所以**用 `LOAD` 之前，
  那个临时文件得先由编辑器写出来**。

**至于「`SAVE` 之后临时文件怎么变成正式 setup file」——本篇没写。**
`EQFS` 的说明里 `temporary` 那个词就是这条边界（见「是什么」）。

### `error_filename` 该不该写

| 场合 | 建议（**这是本页的建议，不是文档要求**） |
|---|---|
| **正常跑** | 可以省——省了只有汇总错误信息（原文：`only a summarized error message is reported`） |
| **调试 / 出错了要定位** | 写 `"UI_REPORT"` 让它进 report window，或写一个绝对路径落成文件 |

**两种写法的差别，原文只说了「报告去哪」，没说「报告有多详细」的差别**——
`UI_REPORT` 与写文件**在内容上是否等价，本篇没写**。

## 和谁有关

| 和谁 | 什么关系 | 依据 |
|---|---|---|
| [[spec-tool]] | **原文逐字点名的调用者之一**（`## Application` 的第二行就是 `The Spec tool`）。**所以本页与它是「被调用 ↔ 调用」的关系，不是同类** | 本篇 `## Application`（**文档事实**） |
| [[eqsp]] | **同族的另一条命令，也是本页最容易混的那一条**（那页**未建**）。两条都属 equation based 配置族、都做「整块搬运」；**但本篇没有出现 `EQSP` 这个词**——这条关系来自 [[mapping-timing]] 把它们排在同一行 | [[mapping-timing]] 主表（**本页读过的 wiki 页**）；**本页没读 `EQSP` 那一篇** |
| [[level-equation-file]] | **搬的对象（level 侧）**：原文例子的 `LEV,EQN,LOAD` 载入的就是它（那页未建）。**它的格式、字段本页一个字没有** | 本篇 `## Example`（**文档事实**，仅限「它存在」） |
| [[timing-equation-set]] | **搬的对象（timing 侧）**：`TIM,EQN` 那两位指的就是它 | 本篇参数表 + [[mapping-timing]]（**文档事实 / 读过的 wiki 页**） |
| [[timing-file]] | **`TIM,WVT` / `TIM,SPS` 那两块住在哪里**——它们住在 timing setup file 里（[[mapping-timing]] 的主表就是按这个排的）。**本篇没提这个文件名** | [[mapping-timing]]（**本页读过的 wiki 页**） |
| [[report-window]] | **`UI_REPORT` 指向的那个窗口**：「错误报告进 report window」就是它。**那页本页没读**，本页只知道这个目的地叫 report window | 本篇参数表（**文档事实**，仅限「这个目的地存在」） |
| [[equation-based-level-setup]] | **同一件事的上游概念**（level 侧的 equation based 配置）。**本页没读那篇**，所以「equation based level 配置长什么样」本页给不出来 | 本页未读（**取材边界**） |
| [[mapping-timing]] | **对照表页**（已建）。它把 `EQFS` 排在「下载 / 上传」那一行的 L1 列，**并把本页的 `## Application` 段当作 ① 档证据**（「GUI 的编辑器工具是 `EQFS` 的调用者」） | 那页的证据节与主表（**本页读过的 wiki 页**） |
| [[timing]] | **stage 页**。本页 `stage: timing` 填的是「**最近的一段**」（§6）——**`EQFS` 的 `## Application` 其实横跨 level 与 timing 两侧**（`spec_type` 有 `LEV` 和 `TIM`），填 `timing` 只是取最近的那一段 | frontmatter 约定 + 本篇参数表 |
| [[level]] | **同上，level 那一侧**（本页的 `LEV` 分支指向它） | 本篇参数表（**文档事实**） |

**两条本页答不住、只能记下来的**：

- **临时文件（`temporary files`）由谁创建、存在哪、什么时候被清掉**——**本篇一个字没写。**
  `EQFS` 只负责搬，**搬运的两端谁负责，本篇没说**。
- **`EQFS` 与「正式 setup file」之间隔着什么**——**本篇没写**。
  所以「编辑器里点了保存之后，机台上的那份配置文件是怎么更新的」这条链，
  **本页只到 `EQFS` 为止。**

## 版本

本文档**有** `## Functional changes` 段，段里**只有一条**：

- **Introduced before SmarTest 6.3.2** → [[smartest-6.3.2]]

> **这一条是 §11.2 ② 说的哨兵值，不是「6.3.2 新增了 `EQFS`」。**
> 措辞是 `before`（不是 `in`），意思是「**在本套文档覆盖范围开始之前就已经有了**」。
> **所以只能说：7.10.3 上有 `EQFS`，而且它比 6.3.2 更老。**

**版本段里没有的东西**：**没有一条 `SmarTest X.Y.Z:` 形式的变更记录**。
所以「`UI_REPORT` 这个取值、`WVT` 那一档、`error_filename` 的省略行为分别是哪个版本进来的」
**在本篇里查不到**。

## 出处

### `sources:` 列了一篇，但这一篇在语料里有 **4 份投放**——本页核过了

本页的 source 是 `02_System_reference/02.06_Command_Reference/02.06.05.02.09_EQFS_-__EQuation_FileS_command_transfer.md`。
把全库扫一遍，`EQFS` 这一篇还有另外三份：

| 路径 | `source_topic` |
|---|---|
| `02.06_Command_Reference/02.06.02.02.108_EQFS_-__EQuation_FileS_command_transfer.md` | `98592.htm` |
| **`02.06_Command_Reference/02.06.05.02.09_EQFS_-__EQuation_FileS_command_transfer.md`（本页 source）** | **`98592_2.htm`** |
| `02.06_Command_Reference/02.06.06.02.13_EQFS_-__EQuation_FileS_command_transfer.md` | `98592_3.htm` |
| `02.08_Setup_and_Result_Tools/02.08.04.34.02.02.13_EQFS_-__EQuation_FileS_command_transfer.md` | `98592_4.htm` |

**核法与本页的结论**：四份**剥掉 frontmatter 之后逐字节相同**——
**都是 2,248 字节**，`sha256` 同为 `7a5553affcdeb71122bd9db05ce99392e86a618bece3483ae8f570d5fa4559f9`。
判据是 §10 第 0 条：**`source_topic` 去掉 `_N` 后缀后相同 → 同一篇 TDC 页**。

> **所以：`EQFS` 这一篇被投放了 4 次，不是 4 处独立证据。**
> **本页只把 `02.06.05.02.09` 当来源**（`sources:` 里那一篇），
> **其余三份只做了去重核对（哈希），没有当成证据读。**
> **[[mapping-timing]] 里也记着同一件事**（「`02.06.06.02.13_EQFS` 在语料里有 4 份」）——
> 本页把那个数**核实到「4 份的正文完全一致」**这一层。

- 本页引的每一句都来自上面标注的那一份，**整篇读完**（135 行 / 1,700 字节）。
- 本页的「语法 / 参数」节与「报错条件」节都是脚本从这一篇逐字抽的（**本页一个字没动**）。

### 本页没做的

- **`EQSP` 那一篇没读**（`02.06.02.02.109`，那页在本 wiki 里**还没建**）。
  **所以「`EQFS` 与 `EQSP` 到底怎么分工」，本页只能给出 [[mapping-timing]] 那一行的口径，
  没有回命令原文核过。** → **这是一条待办。**
- **`02.06.05` 这一章的兄弟命令一篇没读**——所以本页不知道 `EQFS` 在这个章里跟谁并列。
- **`02.06.06.02_List_of_timing_setup_commands` 没读**——**所以「`EQFS` 在不在 timing setup 命令的清单里」
  本页没核过**（[[mapping-timing]] 提过那份清单有 46 条，但那是它读的）。
- **编辑器工具与 Spec Tool 那两篇没读**——**所以「编辑器在什么操作下会调 `EQFS`」本页给不出来**，
  只知道调用者是它们。
- **`report window` 那一篇没读**——所以 `UI_REPORT` 写进去之后长什么样，本页不知道。
- **临时文件的生成 / 清理机制、以及它与正式 setup file 的衔接，本篇没写，本页也没去别处找。**
- **图**：**本篇（四份投放都一样）对 `raw/` 的引用 0 处**——实测 `.png` / `.jpg` / `.gif` /
  `!\[` / `<img` / `raw/` 六种写法全部 **0 命中**。**所以本页没有任何来自图的结论。**
- **没有实跑。** 没在机台上敲过 `EQFS`、没让编辑器 load/save 过任何 equation 文件、
  没有验证过 `UI_REPORT` 的落地形态。`verified: doc-only` 指的就是这件事。

### ⚠️ 本篇的五处语料瑕疵，本页照实记下、一处都没替它改（② 回上游 `.htm` 核过）

> ① **语法行里逗号后的空格不一致**：
> `EQFS {spec_type}, {part}, {operation},{"eqn_filename"}, ["error_filename"]`
> ——**`{operation}` 与 `{"eqn_filename"}` 之间没有空格**，其余逗号后面都有。
> 原文如此（它在「语法 / 参数」节里，**本页一个字没动**）。

> ② **例子的行尾多一个逗号**：`EQFS LEV,EQN,LOAD,"/tmp/level_equation",`
> ——第三个参数位留着、逗号还在。**上游 `98592.htm` 里就是这个写法**（实测）
> → **属 §11.2 ⑥ 那族（上游就坏）**，不是转换坏的。**本页照原样引。**

> ③ **参数名与它的说明对不上（`spec_type = LEV` 时尤其明显）**：
> `eqn_filename` 的说明逐字是 `The absolute filename of the temporary equation based timing file.`
> ——**而 `spec_type = LEV` 的例子一样用这个参数名、一样这句说明**
> （例子的两行原文是 `EQFS LEV,EQN,LOAD,"/tmp/level_equation",` 配
> `This example loads the level equation file from /tmp/level_equation.`）。
> **也就是：名字与说明都沿用 timing 侧的措辞，实际指的文件在 level 侧。**
> **原文如此，本页不替它改**——**照抄时按「它就是那个文件的路径」理解即可**（这是本页的读法）。

> ④ **`## Errors` 段不分 `LOAD` / `SAVE`**：两条都写「文件不存在就报错」，
> **`SAVE` 时目标文件是否也要求已存在，本篇没说**。**本页记下这个缺口，不替它判。**

> ⑤ **`## Application` 段只有两个列表项**（`Editor tools` / `The Spec tool`），
> **没有一句说明这两种调用者的差别**——**本页不替它们编区别。**

**另有一条机械事实值得记**：本篇的参数表是 HTML 表格压平出来的**管道行**
（很多行只有一个孤立的 `|`）——**这是语料的结构，不是脚本切错**
（[[xps256-status-flags]] 的「语法 / 参数」节里记过同一种形态，那里被切成 18 张表）。
**本页的语法节里这份表是连着的，没有被切成多张。**

`verified: doc-only`
