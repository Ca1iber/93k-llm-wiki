---
type: object
title: ON_FIRST_INVOCATION_BEGIN
layer: L2
stage: testmethod
tags: [on-first-invocation-begin, first-invocation-block, multisite, l2, test-method-api, scope-block, parallel-execution, fw-task, judgeandlog]
related: [testmethod, mapping-testmethod, on-first-invocation-end, for-each-site-begin, for-each-site-end, connect, flush, controlling-multiple-sites, level-spec, sequencer-status, dc-result-accessor, smartest-6.3.2]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.138_ON_FIRST_INVOCATION_BEGIN.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# ON_FIRST_INVOCATION_BEGIN

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,590 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.138_ON_FIRST_INVOCATION_BEGIN.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
ON_FIRST_INVOCATION_BEGIN();
```

This API is defined in the header file /opt/hp93000/soc/prod_com/include/MAPI/MapiUtil.h.

  List of parameters There are no parameters. Return value There is no return value.

### Example 1: Minimum code

The following example shows the minimum code for a "first-invocation block". The ellipses ("...") are to be replaced with your code.

```
ON_FIRST_INVOCATION_BEGIN();
    ...
    ...
ON_FIRST_INVOCATION_END();
```

### Example 2: Optional curly brackets

The example utilizes an optional pair of curly brackets "{" and "}". These optional curly brackets are used for simplifying the correct indentation with assistance of the related Eclipse tool.

```
ON_FIRST_INVOCATION_BEGIN();
{
    ...
    ...
}
ON_FIRST_INVOCATION_END();
```

### Example 3

```
//
// Parallel Execution for All Sites - BEGIN
//
ON_FIRST_INVOCATION_BEGIN();

    //
    // Setup and Test Execution
    //
    Routing.pin("Aout").connect(TM::SINGLE);
    Analog.DGT("Aout").enable();
    EXECUTE_TEST(0.1 sec);

    //
    // Retrieve measured analog waveform
    //
    ARRAY_D AnaWave = Analog.DGT("Aout").getWaveform();
    Routing.pin("Aout").disconnect();
    Analog.DGT("Aout").disable();

    FLUSH();

//
// Parallel Execution for All Sites - END
//
ON_FIRST_INVOCATION_END();
...
...
```

ON_FIRST_INVOCATION_BEGIN and ON_FIRST_INVOCATION_END declare the first-invocation block. All APIs in this block are executed for all sites in parallel once only when the program is run for the first tested site. Hence, the analog modules on the all connected site, specified by the "Aout" pin, are enabled and then the measurements are done on all connected sites.

<!-- 语法节 end -->

## 是什么

**`ON_FIRST_INVOCATION_BEGIN()` 是一条作用域块的开始标记。** 块的语义，原文首句一句话说完：

> 「This API declares the beginning of the block that enables you to execute setup and test for all sites in parallel, when the program is run for the first tested site.」

**它单独没有意义——必须与 [[on-first-invocation-end]] 成对**：

> 「ON_FIRST_INVOCATION_BEGIN and ON_FIRST_INVOCATION_END must be used as a pair. The area enclosed by this pair is called "first-invocation block".」

**没有参数、没有返回值**（上面「语法 / 参数」节里逐字写着 `There are no parameters.` 与 `There is no return value.`），定义位置原文写明：

> 「This API is defined in the header file /opt/hp93000/soc/prod_com/include/MAPI/MapiUtil.h.」

### 五条 `## Application note` —— 这一页真正的内容全在这五条里

原文用五条列表把「块什么时候跑、能放什么、绝不能放什么」写完了。**逐条读，不要跳**：

| # | 原文（逐字） | 读法 |
|---|---|---|
| ① | 「This API is meaningful for multisite testing. For single-site testing, this API is ignored.」 | **单 site 时这条 API 被忽略**——不是报错，是忽略 |
| ② | 「You can describe the Setup and Execute APIs within the first-invocation block, in order to achieve them for all active sites in parallel. In addition to the Setup and Execute APIs, you can describe any other function. However, these functions work for the currently-tested site (for example, Result APIs), or regardless of site information (for example, Computation APIs).」 | 放别的东西**可以，但作用域会掉**：要么只对当前 site 生效，要么与 site 无关 |
| ③ | 「All statements in the first-invocation block are executed once only when the program is run for the first tested site.」 | **只跑一次，且跑在第一颗被测 site 上** |
| ④ | 「You can describe the FW_TASK API enclosed by the BEGIN_EXTENSION API with the site parameter and END_EXTENSION API in the first-invocation block for multi-site testing. Note that you should not describe it enclosed by the BEGIN_EXTENSION API with no parameter and END_EXTENSION API.」 | `FW_TASK` **要裹在带 site 参数的那一对里**；**不带参数的那一对不许用** |
| ⑤ | 「Do not make the first-invocation block conditional or make sure to put a dummy first-invocation block in the else branch.CAUTION The TEST() and LIMIT() statements as well as all of the "judgeAndLog_***" statements described in TESTSET must never be used inside a first-invocation block. Using any of these statements carries a high risk of defective devices being declared OK by the test.」 | **别写成有条件的**；**`TEST()` / `LIMIT()` / `judgeAndLog_***` 一律不许放**——原文给了后果 |

**第 ⑤ 条那一句警告是这一页最要紧的一句。** 后果写得很直白：
`Using any of these statements carries a high risk of defective devices being declared OK by the test.`
**——坏片被判成好片。** 这是「判定语句为什么不能进这个块」的**全部理由**：原文**没有给机制，只给了后果**，所以本页也不替它补机制。

### 「能放什么」与「绝不能放什么」

| 能放 | 原文给的边界 |
|---|---|
| Setup 与 Execute API | `in order to achieve them for all active sites in parallel`——**这是这个块存在的理由** |
| 其它函数（例如 Result API） | **只对当前被测的那个 site 生效**（`work for the currently-tested site`） |
| 与 site 无关的函数（例如 Computation API） | `regardless of site information` |
| `FW_TASK` | **必须**裹在**带 site 参数**的 `BEGIN_EXTENSION` / `END_EXTENSION` 里（第 ④ 条） |

| 绝不能放 | 原文的措辞 | 后果 |
|---|---|---|
| `TEST()` / `LIMIT()` / TESTSET 里的 `judgeAndLog_***` | `must never be used inside a first-invocation block` | `high risk of defective devices being declared OK by the test` |
| 用**不带参数**的 `BEGIN_EXTENSION` / `END_EXTENSION` 裹 `FW_TASK` | `you should not describe it` | **原文没说会怎样**（措辞也比上一条轻：`should not`） |
| 把块写成有条件的 | `Do not make the first-invocation block conditional or make sure to put a dummy first-invocation block in the else branch.` | 原文没说 |

**最后一行那个「或者」是原文自己的含糊**：它把「别写成有条件的」与「保证 else 分支里放一个 dummy 块」并列在一句里，**没说要选哪一个**。「要么别条件化、要么给 else 补一个 dummy 块」这个读法是**本页的（推断）**，依据是那一句里 `or` 前后的两个祈使句。**本页不替它补第三种可能。**

### 三个 Example：只有第 3 个带具体 API

**Example 1 / 2 / 3 的代码块都在上面「语法 / 参数」节里逐字，本页不重抄**；**Example 2 的说明本身是一条独立事实**：

> 「The example utilizes an optional pair of curly brackets "{" and "}". These optional curly brackets are used for simplifying the correct indentation with assistance of the related Eclipse tool.」

**那对花括号是可选的**，作用是「配合 Eclipse 工具把缩进弄对」——**不是语法必需**。

**Example 3 是唯一一个带真实 API 调用的**（`Routing.pin("Aout").connect(TM::SINGLE)` → `Analog.DGT("Aout").enable()` → `EXECUTE_TEST(0.1 sec)` → 取波形 → `Routing.pin("Aout").disconnect()` → `Analog.DGT("Aout").disable()` → `FLUSH()`）。段末那段说明把它读成一句话：

> 「ON_FIRST_INVOCATION_BEGIN and ON_FIRST_INVOCATION_END declare the first-invocation block. All APIs in this block are executed for all sites in parallel once only when the program is run for the first tested site. Hence, the analog modules on the all connected site, specified by the "Aout" pin, are enabled and then the measurements are done on all connected sites.」

**这就是这个块的用途原型**：**一次 enable、所有 site 一起测**，而不是逐 site 各 enable 一次。

（Example 1 的说明里那句 `The ellipses ("...") are to be replaced with your code.` —— **代码块里那两行 `...` 是原文自己写的**，不是本页加的省略号。）

## 典型用法

**写法只有一种**（配对），**位置要求原文只给了一条**：

```cpp
ON_FIRST_INVOCATION_BEGIN();
    ...
    ...
ON_FIRST_INVOCATION_END();
```

（上面这段与「语法 / 参数」节里的 Example 1 是同一段原文；加了可选花括号的写法见 Example 2。）

| 场景 | 原文说的结果 |
|---|---|
| **多 site** | 块里的语句**并行作用于所有 active site**（第 ② 条），**只跑一次**（第 ③ 条） |
| **单 site** | `For single-site testing, this API is ignored.` —— **被忽略** |
| 块里放 `TEST()` / `LIMIT()` / `judgeAndLog_***` | **绝不许**（第 ⑤ 条） |
| 块里放 `FW_TASK` | 允许，**但必须用带 site 参数的那一对 `BEGIN_EXTENSION` / `END_EXTENSION` 包**（第 ④ 条） |

**原文没有 `## Procedure`，也没有 `## Before you begin`**；三个 Example 之外没有别的用法说明。
**所以「先做什么后做什么」本页给不了**——本页能给的只有上表那四条「条件 → 结果」。

**一条本页答不了的**：多 site 时**谁必须待在这个块里**。[[connect]] 那页记着它的出处文档写着
`For multi-site testing, the CONNECT API must be used in the first-invocation block except the "each site" loop block.`
——**那条要求不在本页的出处文档里**（本页这一篇一个字没提 `CONNECT()`），**本页只记「[[connect]] 那边这么写」这一层**。

## 和谁有关

- [[on-first-invocation-end]] — **配对的另一半，管块的结束**。两篇的 `sources:` 是**两篇不同的文档**（`…138` / `…139`），**本页不写那一篇的内容**，只按原文那句 `must be used as a pair` 链它。
- [[testmethod]] / [[mapping-testmethod]] — **本页 `stage: testmethod` 的理由**。[[mapping-testmethod]] 主表第 6 行「多 site 并行 setup 块」的 **L2 格就是本页与 [[on-first-invocation-end]]**，**L1 格与 L3 格是 `—`**（该页给了理由：这是纯 test method 侧的作用域块，固件层没有对应物）。
- [[for-each-site-begin]] / [[for-each-site-end]] — 原文 `## Related information` 把这两个块与本页并列。[[mapping-testmethod]] 第 7 行把「逐 site setup 块」写成**嵌套在上面那个块里**——**那是那一页的读法，本页的出处文档没有写嵌套关系**，本页不把它当原文。
- [[connect]] — **方向是单向的**：本页的出处文档**一个字没提 `CONNECT()`**；而 [[connect]] 那页记着它的出处文档要求 `CONNECT()` 必须写在 first-invocation 块里（多 site 时）。**本页没有独立读那一篇**（它不在本页 `sources:` 里）。
- [[flush]] — Example 3 的最后一行调的就是 `FLUSH()`。**这是本页出处文档与 [[flush]] 唯一一处接触**，原文对那一行没有任何解释。
- [[controlling-multiple-sites]] / [[level-spec]] / [[sequencer-status]] / [[dc-result-accessor]] — 这几页在 `extract/dangling.csv`（**2026-09-20 的读数**）里写着 `on-first-invocation-begin` 这个名字（该页记录本名字 **8 处引用**、跨 7 个 stage）。**本页没有读它们**——所以「它们各自在什么语境下提本页」本页一个字没有。（那张单每次重刷都会变，引它要标清是哪一刻。）
- **入边（`extract/edges.jsonl`，2026-09-17 的快照）**：链到本页出处文档 `…138` 的边 **112 条 / 75 篇**，**全部 `resolved`**（111 条 `inline` + 1 条 `toc`），**0 条落在代码跨度里**。最密的几篇：`02.07.04.01.117_HW_STATE`（5）、`02.07.10.02.01_SmartCalc__Thread_per_site__and__Common_thread`（4）、`02.07.13.05.01_Basic_rules_for_SmartRDI`（4）。**这 112 条边涉及的正文，本页一条没读**，只用了计数。
- **只写反引号、不写链接的名字**：`ON_LAST_INVOCATION_BEGIN` / `ON_LAST_INVOCATION_END`（`02.07.04.01.140` / `.141`）、`FOR_SEMI_PARALLEL_TEST_BEGIN` / `FOR_SEMI_PARALLEL_TEST_END`（`.73` / `.74`）、`Controlling Multiple Sites`（`02.07.03.13`）、`Site States and Test Method Programs`（`02.07.03.13.06`）、以及 Example 3 里那批调用（`Routing.pin`、`Analog.DGT`、`EXECUTE_TEST`、`TM::SINGLE`、`ARRAY_D`）——**原文里出现，但都不在 `extract/prose-allowlist.txt` 里**，按 §9.1 一律反引号。
  （`FLUSH` 在清单里，但清单里那一条是 [[flush]] 这个**对象页名**；Example 3 里那一行是 `FLUSH()` 的**调用**，本页按名字链 [[flush]]、不链那一行。）

## 版本

本文档**有** `## Functional changes` 段，**只有一条**：

- `Introduced before SmarTest 6.3.2`

**这一条是哨兵值，不是「6.3.2 的变更」**（`schema.md` §11.2②）：`Introduced before` 的意思是
「**在本文档集覆盖范围开始之前就已经有了**」——**照字面读会读成「6.3.2 新增了 ON_FIRST_INVOCATION_BEGIN」，那是错的。**
对照页：[[smartest-6.3.2]]（**版本页，不是本页建的**）。

**本篇没有任何别的版本条目**，所以本页正文里的东西**都没有版本归属**：

| 本页的内容 | 语料给的版本 |
|---|---|
| 那五条 `## Application note` | **未写** |
| 三个 Example（含「花括号可选」那条说明） | **未写** |
| 「单 site 时被忽略」 | **未写** |

**即：「多 site 这条限制是哪个版本加的」，语料未写。本页不推测。**

## 出处

- 定义文档（本页 `sources:` 唯一一篇，**整篇读过**）：
  `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.138_ON_FIRST_INVOCATION_BEGIN.md`
  （TDC `29526.htm`，4,491 字节 / 96 行）。
- **本篇没有重复投放**：全语料按 `source_topic` 查 `29526.htm`，**只有这一个文件**。
- **本页「语法 / 参数」节的来源就是这一篇自己**（节首没有「取自子主题」后缀），节里那 1,590 字符
  是原文的 `## Syntax` + 三个 `## Examples` + 段末那段说明。

### 本页读的图：**0 张，因为这一篇一张图都没有**

**实测该篇对 `raw/` 的图片引用 0 处**（`grep -c '!\['` 零命中）。
**这不是「图够不着」，是这一篇本来就不带图**——所以本页**没有任何来自图的结论**，
也没有任何一处需要标「④ 图证」。**本条与 [[on-first-invocation-end]] 那页一样**（那篇也是 0 张）。

### 本页与 [[on-first-invocation-end]] 那一篇的差别（**本页实测 diff 出来的，不是转述**）

两篇去掉标题与编号后**只差四处**：

1. **首句**（本页是 `declares the beginning of the block that enables you to execute setup and test for all sites in parallel`）；
2. **配对句里被链的是哪一个名字**；
3. **本页独有 `## Application note`（五条）**，END 那篇在同一个位置上只有一句指路（`see ON_FIRST_INVOCATION_BEGIN`）；
4. **语法块那一行**（`ON_FIRST_INVOCATION_BEGIN();` vs `ON_FIRST_INVOCATION_END();`）。

**其余部分两篇逐字相同**：三个 Examples、段末那段说明、头文件那一行、
`## Related information` 的九个名字、`## Functional changes` 那一条。
**这条 diff 是理解这两页的钥匙：BEGIN 那一篇是「有内容的」那一篇，END 那一篇只有指路。**

### 本页没做的

- **`## Related information` 列的九篇一篇没读**：`ON_FIRST_INVOCATION_END`（`.139`）、
  `ON_LAST_INVOCATION_BEGIN`（`.140`）、`ON_LAST_INVOCATION_END`（`.141`）、
  `FOR_EACH_SITE_BEGIN`（`.70`）、`FOR_EACH_SITE_END`（`.72`）、
  `FOR_SEMI_PARALLEL_TEST_BEGIN`（`.73`）、`FOR_SEMI_PARALLEL_TEST_END`（`.74`）、
  `Controlling Multiple Sites`（`02.07.03.13`）、`Site States and Test Method Programs`（`02.07.03.13.06`）
  ——**所以「这几个块之间怎么嵌套、能不能互相套」本页一个字没有**（原文也没写）。
- **`BEGIN_EXTENSION` / `END_EXTENSION` 自己那两篇没读**（它们也不在 `## Related information` 名单里）
  ——**所以第 ④ 条那个「带 site 参数与不带参数到底差在哪」本页答不了**，本页只有原文那一句 `should not`。
- **`TEST` / `LIMIT` / `TESTSET` 三篇没读**——所以「为什么在块里判定会把坏片判成好片」，
  **本页只有原文那一句警告，没有机制**。
- **Example 3 里那批 API 的参数含义本页一个字没有**：`Routing.pin` / `Analog.DGT` /
  `EXECUTE_TEST` / `ARRAY_D` / `TM::SINGLE` / `FLUSH()` 各自是什么，本页不知道。
- **没有实跑。** 没有写过 first-invocation 块、没有在多 site 机台上跑过、
  没有验证过「单 site 时被忽略」。**`verified: doc-only` 指的就是这件事。**
- **没有跑 `verify_stages.py`**（按开工简报的要求，避免与别的批次抢同一个报告文件）。
- **没有动 `wiki/index.md`**，也没有把本页挂进 [[testmethod]] 那页。

### ⚠️ 语料瑕疵（照实记，一处都没替它改）

**① 一处粘连：`branch.CAUTION`。** 原文 `## Application note` 的最后一条里，
`else branch.` 与 `CAUTION` 之间**没有空格、也没有换行**（原文这两个字本来是两段）：

> 「Do not make the first-invocation block conditional or make sure to put a dummy first-invocation block in the else branch.CAUTION The TEST() and LIMIT() statements as well as all of the "judgeAndLog_***" statements described in TESTSET must never be used inside a first-invocation block.」

**本页在第 ⑤ 条那一格里原样引了这一句**（引文不许替语料修字，§11.2）。
（同型毛病在 `connect` 那篇是 `state.Note`、在 `flush` 那篇是 `flush.You`——**三处不是同一个文件，是同一类**。）

**② 同一句里 `multisite` 与 `multi-site` 两种拼法并存。** 第 ① 条写 `multisite testing`，
第 ④ 条写 `for multi-site testing`——**同一篇文档、两种拼法**。本页两处都按原样引，**没有统一**。

**③ `judgeAndLog_***` 里的 `***` 是原文的通配写法，不是加粗标记。**
引文里原样保留，**本页没有把它改写成 `judgeAndLog_XXX` 或别的形式**。

**④ 本页这一篇没有编码坏字（§11.2① 那一族）**：用 `[一-鿿]` 实测零命中。
**也没有 §11.2⑤ 那个整词替换**（`DC/DC power units` 实测 0 命中）。
**这不是「没找到」，是查过、结果为零**——**这一点在本页比在别的页更要紧**，因为这是一页 API 页，
上面「语法 / 参数」节里的 `ON_FIRST_INVOCATION_BEGIN` / `ON_FIRST_INVOCATION_END` / `ARRAY_D` /
`EXECUTE_TEST` / `MapiUtil.h` 这类标识符**都是从正文逐字读到的**，
**没有一处是坏字或整词替换的产物**（§11.2⑤ 说那一族的铁证就是「标识符里出现 `/` 或空格」——本页没有）。

`verified: doc-only`
