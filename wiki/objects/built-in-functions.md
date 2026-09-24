---
type: object
title: Built-in functions
layer: gui
stage: testflow
tags: [testflow, gui, built-in-functions, flow-control-node, test-suite, equation, level-set, timing-set, waveform-set, result-access]
related: [testflow, flow-control-node, test-suite, lsus, dsus, tsus, wsus, svlr, spst, waveform-set, timing-equation-set, spec-set, testflow-variable, smartest-6.3.2]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.02.01_Built-in_functions.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# Built-in functions

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

**没有加标记的语法段。** 定义文档里没有 `Syntax` / `Parameters` / `Example`
这类**段标记**，跟着 `Subtopics` 找一层也没有。
**所以本脚本一个字都不收录**——没有段标记时「哪一段是语法」是猜，而猜就是编（§4）。

<!-- 语法节 end -->

## 是什么

**testflow 内置函数（built-in functions）是 Testflow Editor 提供的一组函数**——
**在 testflow 执行期读内部数据（例如某个 test suite 的结果），用来在 flow control node 里做更复杂的流程控制。**

> 「The Testflow Editor provides a number of built-in functions you can use to access internal data during testflow execution like, for example, test suite results. You can use these functions in the flow control nodes for more sophisticated testflow control.」

**这一句里三个限定词就是本页的全部边界**：
**提供者是 Testflow Editor**（→ 本页 `layer: gui`）、
**读取时机是 testflow 执行期**（→ `stage: testflow`）、
**使用场所是 flow control node**。

### 先说「语法 / 参数」节为什么是空的（**本页第一个要知道的事实**）

**本篇的两个函数表直接跟在散文后面，一个标题都没有**——
raw 里**没有 `## Syntax`、`## Parameters`、`## Example` 这类段标记**
（`#### Subtopics` 也没有）。
**所以脚本按 §4 一个字都不收，函数清单只能放在本页正文里。**
**这不是脚本漏了，是这篇文档本来就没有可抓的段。**

### 第一组：五个「test suite 执行结果」函数

> 「The following built-in functions allow you to retrieve information on the execution of individual test suites.」

| 函数 | 原文那一格 |
|---|---|
| `tf_result(<test_suite_name>, <result_index>)` | 「Access the result array of the given test suite and return the value of that array with the index result_index.」 |
| `pass(<test_suite_name>)` | 「Return 1, if the test suite has passed, otherwise return 0.」 |
| `fail(<test_suite_name>)` | 「Return 1, if the test suite has failed, otherwise return 0.」 |
| `has_run(<test_suite_name>)` | 「Return 1, if the test suite has already been executed during the current testflow execution, otherwise return 0.」 |
| `has_not_run(<test_suite_name>)` | 「Return 1, if the test suite has not been executed during the current testflow execution, otherwise return 0.」 |

**这一组五个函数回答三个问题**：
**过了没有**（`pass` / `fail`）、**跑过没有**（`has_run` / `has_not_run`）、
**某个测量值是多少**（`tf_result`）。**入参都是 test suite 名。**

**`tf_result` 只有一个例子，而且它带来两个坑**：

> 「For example, `tf_result(hold_time,0)` returns the minimum measured hold time.」

- **结果数组的下标只有 `0` 被说明了**（= 最小测得值）。
  **`1`、`2` 是什么，本篇没写 → 语料未写。**
  **所以「最大值 / 均值怎么取」在本页答不了**（见 `## 出处` ⚠️③）。
- **例子里的 `hold_time` 没有引号**，而同一张表的其它函数写的是 `<test_suite_name>`。
  **test suite 名到底要不要引号，本篇没说**（见 `## 出处` ⚠️②）。

### 第二组：十个名字、十一行「当前 testflow 的进一步信息」

> 「The following built-in functions allow you to retrieve further information on the current testflow:」

| 函数 | 原文那一格 |
|---|---|
| `lsus()` | 「Return the number of level sets used.」 |
| `dsus()` | 「Return the number of DPS equation sets used.」 |
| `tsus(waveset_no)` | 「Return the number of timing sets used.」（并附「`waveset_no` may also be an expression.」） |
| `wsus()` | 「Return the number of waveform sets used.」 |
| `burstfirst(burstlabel)` | 「Return a string that is the first label of `burstlabel`.」 |
| `burstnext(burstlabel)` | 「Return a string that is the next label of `burstlabel` in the current burst sequence, or an empty string if `burstlabel` is the last label in the sequence.」 |
| `spst_timing(eqst_no, spst_no)` | 「Return 1 if the equation set number `eqst_no` and the spec set number `spst_no` define a valid combination in the timing equation system, otherwise return 0.」 |
| `spst_level(eqst_no, spst_no)` | 「Return 1 if the equation set number `eqst_no` and the spec set number `spst_no` define a valid combination in the level equation system, otherwise return 0.」 |
| `svlr_timing(eqst_no, spst_no, "variable_name")` | 「Return the value of the timing equation variable specified by the equation set number `eqst_no`, the spec set number `spst_no` and `variable_name`.」 |
| `svlr_timing("specification", "variable_name@port")` | 「Return the value of the timing equation variable specified by the multiport specification `specification` for the port `port`.」 |
| `svlr_level(eqst_no, spst_no, "variable_name")` | 「Return the value of the level equation variable specified by the equation set number `eqst_no`, the spec set number `spst_no` and `variable_name`.」 |

**三件在表里一眼看不出来、但要先知道的事：**

- **`svlr_timing` 占了两行**——它是**两个重载**：
  一个按 `equation set × spec set`，一个按 `multiport specification × port`。
  **按名字去搜会搜到两处，这不是重复。**
- **分组标题比它的成员宽**（观察）：这一组叫「further information on the current testflow」，
  可成员里有**数数**（`lsus` / `dsus` / `tsus` / `wsus`）、
  **burst 里的标签字符串**（`burstfirst` / `burstnext`）、
  **组合是否合法**（`spst_timing` / `spst_level`）、
  **方程变量的值**（`svlr_timing` / `svlr_level`）。
  **只有前四个真是「当前 testflow 的计数」。**
- **`burstfirst` / `burstnext` 两格都带着同一句指引**：
  「See Identifying fail labels in a burst.」（那一篇，raw: `02.08.04.32.02.01.14`，**本页没读**）。

### 哪些参数可以是表达式（**只有三处写明**）

| 函数 | 原文 |
|---|---|
| `tsus(waveset_no)` | 「`waveset_no` may also be an expression.」 |
| `spst_timing(eqst_no, spst_no)` | 「`eqst_no` and `spst_no` may also be expressions.」 |
| `spst_level(eqst_no, spst_no)` | 「`eqst_no` and `spst_no` may also be expressions.」 |

**其余函数有没有这个待遇，本篇没说**——`tf_result` 的 `result_index`
与 `svlr_*` 的 `variable_name` 都没有这句话（见 `## 出处`）。
`lsus()` / `dsus()` / `wsus()` 这三行**括号里是空的，本来就没有参数**。

### 两条 `Note`，是本页的硬约束

> 「Built-in functions are used in much the same way as variables in Flow control nodes.」

> 「Note Built-in functions must be specified using lower case characters.」

**第一条说「怎么用」**：**写法上与 flow control node 里的变量同一种用法**（→ [[flow-control-node]]）。
**第二条说「必须怎么写」**：**全小写**。原文的 `Note` 后面**没有冒号**，照原样引。

**第二条要和一个事实并排看**：这十个名字里有四个（`lsus` / `dsus` / `tsus` / `wsus`）
**与本 wiki 里的命令页同名**。
**本篇只把它们叫「内置函数」、只说了要小写——
它们与那些同名命令是不是同一套东西，本篇一个字没写（语料未写）。**
（同期的 `match-loops` 页有一句可作参照的字面事实：那里的 firmware 命令
`SQST OFF` / `NIFE` 是按大写写的，**但那是另一篇文档，本页不拿它当依据**。）

## 典型用法

**先说范围**：这一篇**没有 `## Procedure`，也没有 `## Before you begin`**，
**也没有 `## Application`、没有任何以 `## Example` 为标题的例子段**。
**全篇唯一一个用法例，是嵌在 `tf_result` 那一格里的 `tf_result(hold_time,0)`。**

**所以本页这一节是「按要回答的问题挑函数」，不是文档给的流程。**
**用法上的唯一硬规矩只有两条**（见上）：**写在 flow control node 里**、
**名字全小写**。

| 你想问 | 用哪个 | 返回值 |
|---|---|---|
| 某个 test suite 过了吗 | `pass(<test_suite_name>)` | 过 → `1`，否则 `0` |
| 某个 test suite 失败了吗 | `fail(<test_suite_name>)` | 失败 → `1`，否则 `0` |
| 某个 test suite 跑过吗 | `has_run` / `has_not_run` | 跑过 / 没跑过 → `1`，否则 `0` |
| 某个测量值是多少 | `tf_result(<test_suite_name>, <result_index>)` | 结果数组里第 `result_index` 个值；**下标 `0` 是最小测得值** |
| 这套配置用了多少 level set | `lsus()` | 个数 |
| 用了多少 DPS 方程集 | `dsus()` | 个数 |
| 用了多少 timing set | `tsus(waveset_no)` | 个数（**按 waveform set 问**） |
| 用了多少 waveform set | `wsus()` | 个数 |
| 某个 `equation set × spec set` 组合在 timing 方程系统里合不合法 | `spst_timing(eqst_no, spst_no)` | 合法 → `1`，否则 `0` |
| 同上，level 方程系统 | `spst_level(eqst_no, spst_no)` | 合法 → `1`，否则 `0` |
| 某个 timing 方程变量的值 | `svlr_timing` | 值（**两个重载：按 eqst/spst 或按 multiport spec + port**） |
| 某个 level 方程变量的值 | `svlr_level(eqst_no, spst_no, "variable_name")` | 值 |
| burst 里第一个 / 下一个 fail label | `burstfirst(burstlabel)` / `burstnext(burstlabel)` | 字符串；`burstnext` 到最后一个 label 时返回**空串** |

**三个容易写错的点：**

1. **`tsus` 要带一个参数**（`waveset_no`），而同样数东西的 `lsus` / `dsus` / `wsus` 不带。
2. **字符串参数要加双引号**（`svlr_timing("specification", "variable_name@port")`
   那一格里是 `"variable_name@port"`——**`@port` 写在引号里面**），
   而 `burstfirst(burstlabel)` / `burstnext(burstlabel)` 那一格**没有引号**。
   **到底哪些要引号，本篇没有统一说明**（见 `## 出处` ⚠️④）。
3. **`tf_result` 的下标只有 `0` 有说明**；要取别的下标，本篇给不了依据。

## 和谁有关

| 页 | 是什么关系 | 依据 |
|---|---|---|
| [[testflow]] | **本页 `stage: testflow` 的理由**：这些函数在 testflow 执行期求值 | frontmatter + 本篇第一句 |
| [[flow-control-node]] | **唯一的去向**：本篇正文最后一句把读者指到它——「Built-in functions are used in much the same way as variables in Flow control nodes.」（**这一篇是本页的父篇**：路径编号 `02.08.04.32.01.02.02` 正是本篇 `02.08.04.32.01.02.02.01` 的上一层）**本页没读** | 本篇末句 |
| [[test-suite]] | **第一组五个函数的入参都是 test suite 名**（`<test_suite_name>`） | 本篇第一组表 |
| [[lsus]] | **同名页**：内置函数 `lsus()` 与本 wiki 的命令页同名。**两者是不是同一套东西，本篇没写** | 本篇第二组表 + 页名 |
| [[dsus]] | 同上（`dsus()`） | 同上 |
| [[tsus]] | 同上（`tsus(waveset_no)`） | 同上 |
| [[wsus]] | 同上（`wsus()`） | 同上 |
| [[svlr]] | **同名页**：`svlr_timing` / `svlr_level` 与本 wiki 的 `svlr` 命令页同名同前缀。**关系同上，本篇没写** | 本篇第二组表 + 页名 |
| [[spst]] | **同名页**：`spst_timing` / `spst_level` 的前缀是 `spst`。**关系同上，本篇没写** | 本篇第二组表 + 页名 |
| [[waveform-set]] | **`wsus()` 数的是它**；`tsus(waveset_no)` 也是按它问 | 本篇第二组表 |
| [[timing-equation-set]] | **`spst_timing` / `svlr_timing` 说的 `equation set number` 指的东西**——**（推断）依据是页名与本篇的 `equation set number` 对应**，**本页没有去核那一页** | 本篇第二组表 |
| [[spec-set]] | **`spst_no` 被原文叫 `spec set number`** | 本篇第二组表 |
| [[testflow-variable]] | **（推断）末句那个 `variables` 的落点**：原文只说「much the same way as variables in Flow control nodes」，**没说那些变量是 `testflow variable`** | 本篇末句 + 页名 |
| [[smartest-6.3.2]] | **版本页**：本篇唯一那条 `## Functional changes` 落在它身上 | 本篇 `## Functional changes` |
| `Flow control nodes`（raw: `02.08.04.32.01.02.02_Flow_control_nodes.md`） | **本页的父篇**；**未读**——所以「内置函数在 flow control node 里具体怎么填、有没有编辑器补全」本页没有 | 本篇末句的链接 |
| `Identifying fail labels in a burst`（raw: `02.08.04.32.02.01.14`） | **`burstfirst` / `burstnext` 两格唯一的指引**；**未读** | 本篇第二组表 |
| `test suite results` / `internal data` / `DPS equation sets`（**未建，不链**） | 本篇提到但没有链接的三个概念 | 本篇正文 |

**本页没有引用 `edges.jsonl` 的入边/出边数字**（没读边数据，故不报条数）。

## 版本

**本文档有 `## Functional changes` 段，只有一条，逐条转录**：

- `Introduced before SmarTest 6.3.2`

**这一条是哨兵值**（§11.2 ②）：它的意思是
「**在本文档集覆盖范围开始之前就已经有了**」，
**不是「SmarTest 6.3.2 新增了这些内置函数」**。
**照字面读会生成一条「6.3.2 一口气加了十来个内置函数」的假信息，而格式齐整、看不出来。**

**所以本页只知道一件事：这些内置函数早于本文档集覆盖范围。**
**它们当中哪些是后来加的（`burstfirst` / `burstnext` 这种和 burst 挂钩的，
`svlr_*` 这种和方程挂钩的），本篇没有记录——
「没记录」不等于「一开始就都有」**（§13.1）。

版本页：[[smartest-6.3.2]]。

## 出处

`sources:` 一篇：
`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.02.01_Built-in_functions.md`
（TDC `16753.htm`；**3,752 字节 / 178 行**，全文 CRLF，末行带换行。
**本节的行数口径是 `wc -l`（= `splitlines()`），不加 1**，见 §11.5）。**整篇读完。**

**本页没做的**：

- **`Flow control nodes`（父篇）没读**：raw: `02.08.04.32.01.02.02_Flow_control_nodes.md`（`02.08.04.32.01.02.02` 正是本页路径的上一层）。
  **所以「内置函数写在 flow control node 的哪个字段里」「写成什么样才算一个表达式」
  「有没有语法检查」——本页一个字都没有。**
- **`Identifying fail labels in a burst` 没读**（raw: `02.08.04.32.02.01.14`）：
  **`burstfirst` / `burstnext` 在什么场景下用、`burstlabel` 长什么样，本页没有。**
- **图一张没看——因为这一篇里没有图**（全文 **0 处** `.png` / `.jpg` / `raw/`）。
  **所以本页没有任何来自图的结论**；这与「图够不着」不是一回事（§11.4）。
- **没有 `## Procedure` / `## Before you begin` / `## Application` / `## Example` 段**，
  所以「典型用法」那一节是**本页按两张函数表拼的**，不是文档给的流程。
- **函数清单只有两张表、没有签名段**：本篇**没有一处给出返回类型**
  （只有「返回 `1`，否则返回 `0`」与「返回一个字符串」这两种描述），
  **也没有一处说明参数能不能省、类型不对会怎样。**
- **两个名字没有展开**：`tf_result` 里的 `tf`、`svlr_*` 里的 `svlr`，
  **本篇一个字都没展开**（`lsus` / `dsus` / `tsus` / `wsus` 这一族的名字也没有）。
- **没有 `## Errors` / `## Warnings` 段**——**所以本页没有「报错条件」节**。
  这是事实，不是缺陷（同批的 `CLMP` / `DCDT` 两页有那一节）。
- **没有实跑。** 没有在任何机台上把这些函数填进 flow control node 试过。
  `verified: doc-only` 指的就是这件事。
- **没有用 `edges.jsonl`**，故不报入边/出边条数。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> ① **两个函数表没有任何段标记**（既没有 `## Syntax`，也没有 `## Parameters`，
> 也没有 `## Example`，连 `#### Subtopics` 都没有）——
> **表直接跟在散文后面**。**这就是本页「语法 / 参数」节为空的原因**，
> 也是它**不能**像同批的 `CLMP` / `DCDT` 两页那样把参数表逐字抄进来的原因。
> **本页照实记，没替它加标题。**
> ② **`tf_result` 的例子与占位符写法不一致**：
> 「For example, `tf_result(hold_time,0)` returns the minimum measured hold time.」
> ——**`hold_time` 没有引号**，而同一张表里其它函数写的是 `<test_suite_name>`。
> **test suite 名要不要引号，本篇没说。**
> ③ **结果数组的下标只交代了一个**：`tf_result` 那一格只说了下标 `0` 是最小测得值，
> **`1`、`2` 是什么，以及数组一共几个元素，本篇没写**。
> ④ **字符串参数有的带引号、有的不带**：
> `svlr_timing("specification", "variable_name@port")` 与
> `svlr_level(eqst_no, spst_no, "variable_name")` 带引号，
> 而 `burstfirst(burstlabel)` / `burstnext(burstlabel)` 不带。
> **判断规则本篇没给。**
> ⑤ **一句里动词不齐**：`tf_result` 那一格以 `Access` 开头
> （「Access the result array of the given test suite and return the value of that array with the index result_index.」），
> **其余函数的格子一律以 `Return` 开头**。
> **同一张表两种句式**，本页照录。
> ⑥ **`Return 1` 后面那个逗号**：`pass` / `fail` / `has_run` / `has_not_run` 四格
> 都写成「Return 1, if the test suite has passed, otherwise return 0.」这种形状——
> **`1` 后面那个逗号在原文里是有的**，本页引用时照原样保留，**没替它删**。
> ⑦ **两个同构句子的收尾标点不一样**：第一组的引子写
> 「The following built-in functions allow you to retrieve information on the execution of individual test suites.」（**句号**），
> 第二组的引子写
> 「The following built-in functions allow you to retrieve further information on the current testflow:」（**冒号**）。
> **两句话结构相同、收尾不同**，本页照录，不替它统一。
> ⑧ **两条 `Note` 前都没有冒号**（`Note Built-in functions must be specified using lower case characters.`），
> 且 raw 里 `Note` 前**有一个前导空格**（折叠空白后就是一个空格）。**引用时照原样。**
> ⑨ **`svlr_timing` 在表里出现两次**：两格同名不同签名
> （`svlr_timing(eqst_no, spst_no, "variable_name")` 与
> `svlr_timing("specification", "variable_name@port")`）。
> **本篇没有一句话说这是两个重载**——（推断）依据是两格的签名不同而名字相同。
> **按名字搜这一篇会搜到两处，不是重复行。**
> ⑩ **`test suite` 与 `testflow` 两个词的写法在正文里不统一**：
> 有的地方写 `test suite`、有的地方写 `test_suite_name` 这种下划线形态
> （后者只出现在占位符里）。**本页照录，不替它统一。**
> ⑪ **本篇没有坏字**：实测 **0 处非 ASCII 字符**（没有 `鈥` / `渭` / `碌` 那一族）。
> **但这是「本页量过的」，判据只是这一个文件**；§11.2 ① 那族在别的篇里大量存在。

`verified: doc-only`——**本页没有在任何真实机台上把这些函数填进 flow control node 跑过，
也没有验证过任何一个返回值**（§11：文档里有 ≠ 这台机器上能用；
尤其 `tf_result` 的下标含义与「全小写」这条硬要求，**动手前先照实机核对**）。
