---
type: object
title: ON_FIRST_INVOCATION_END
layer: L2
stage: testmethod
tags: [on-first-invocation-end, first-invocation-block, multisite, l2, test-method-api, scope-block, pair-with-begin]
related: [testmethod, mapping-testmethod, on-first-invocation-begin, for-each-site-begin, for-each-site-end, connect, flush, controlling-multiple-sites, level-spec, sequencer-status, smartest-6.3.2]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.139_ON_FIRST_INVOCATION_END.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# ON_FIRST_INVOCATION_END

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,588 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.139_ON_FIRST_INVOCATION_END.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
ON_FIRST_INVOCATION_END();
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

**`ON_FIRST_INVOCATION_END()` 是 first-invocation 块的结束标记。** 原文首句：

> 「This API declares the end of the first-invocation block that is started by ON_FIRST_INVOCATION_BEGIN.」

**它必须与 [[on-first-invocation-begin]] 成对**：

> 「ON_FIRST_INVOCATION_BEGIN and ON_FIRST_INVOCATION_END must be used as a pair. The area enclosed by this pair is called "first-invocation block".」

**这一篇的散文到此为止**——整篇只有「首句 + 配对句 + 一句指路」三句，第三句把块的全部细节推给了 BEGIN 那一篇：

> 「For details on the "first-invocation block" enclosed by ON_FIRST_INVOCATION_BEGIN and ON_FIRST_INVOCATION_END, see ON_FIRST_INVOCATION_BEGIN.」

**这就是本页最要紧的一条事实：END 侧没有自己的语义。** 「块里的语句什么时候跑、跑在哪些 site 上、不许放什么」**全在 [[on-first-invocation-begin]] 那边**，**本页不抄它**。

**没有参数、没有返回值**（上面「语法 / 参数」节里逐字写着 `There are no parameters.` 与 `There is no return value.`），定义位置原文写明：

> 「This API is defined in the header file /opt/hp93000/soc/prod_com/include/MAPI/MapiUtil.h.」

### 本页的出处文档里「有」、但不属于 END 的三件东西

**照实说清楚，免得读者把它们当成 END 的语义**：

| 原文里有的 | 它讲的是谁 |
|---|---|
| 段末那句 `ON_FIRST_INVOCATION_BEGIN and ON_FIRST_INVOCATION_END declare the first-invocation block. All APIs in this block are executed for all sites in parallel once only when the program is run for the first tested site. Hence, the analog modules on the all connected site, specified by the "Aout" pin, are enabled and then the measurements are done on all connected sites.` | **整个块**（两个名字都点了），**不是 END 独有的语义** |
| `## Examples` 里的三个例子 | **整个块**——每个例子都是从 `BEGIN` 写到 `END` |
| `## Related information` 里的九个名字 | **整块的相关文档**（两个 API 页里列的名单逐字相同） |

**这一段（含三个 Examples）与 [[on-first-invocation-begin]] 那一篇逐字相同**——两篇文档**共用同一个例子集**，所以「本页的例子」不是 END 自己的例子（**本页实测 diff 过，见「出处」**）。

**本页没有硬凑**：END 这一篇**没有 `## Application note` 段**，所以那五条「单 site 会被忽略 / 只跑一次 / 不许放 `TEST()`」的规则**本页一条都不写**——**它们不在本页的 `sources:` 里**。要那五条，看 [[on-first-invocation-begin]]。

## 典型用法

**只有一条**：把 `ON_FIRST_INVOCATION_END();` 写在块的结尾，与它前面的 `ON_FIRST_INVOCATION_BEGIN();` 配对。原文的措辞是 `must be used as a pair`（上引），**除了「成对」之外没有写任何位置要求**。

**一对可选的花括号**（Example 2 的说明；**这一段在本页的出处文档里就有，不是从 BEGIN 那页搬的**）：

> 「The example utilizes an optional pair of curly brackets "{" and "}". These optional curly brackets are used for simplifying the correct indentation with assistance of the related Eclipse tool.」

**那对花括号是可选的**，作用是配合 Eclipse 工具把缩进弄对——**不是语法必需**。

| 你想知道 | 本页能答吗 |
|---|---|
| 块里的语句什么时候跑、跑在哪些 site 上 | **答不了**——原文写的是 `see ON_FIRST_INVOCATION_BEGIN` |
| 单 site 时这个块会怎样 | **答不了**（同上） |
| 块里不许放什么 | **答不了**（同上） |
| 花括号要不要写 | **能答**：可写可不写（上面那句原文） |
| 能不能嵌套、能不能提前退出 | **答不了**——这一篇一个字没写 |

**原文没有 `## Procedure`，也没有 `## Before you begin`。**

## 和谁有关

- [[on-first-invocation-begin]] — **配对另一半，也是本页的语义所在**（原文那句 `see ON_FIRST_INVOCATION_BEGIN`）。**两篇是两篇不同的文档**（`…138` / `…139`），**本页不搬它那五条 `## Application note`**。
- [[testmethod]] / [[mapping-testmethod]] — **本页 `stage: testmethod` 的理由**。[[mapping-testmethod]] 主表第 6 行「多 site 并行 setup 块」的 **L2 格是本页与 [[on-first-invocation-begin]]**，**L1 / L3 两格是 `—`**（该页的理由：纯 test method 侧的作用域块，固件层没有对应物）。
- [[for-each-site-begin]] / [[for-each-site-end]] — 原文 `## Related information` 里与本页并列的两个作用域块。**原文没有写它们与本页是什么关系**（只是并列）。
- [[connect]] / [[controlling-multiple-sites]] / [[level-spec]] / [[sequencer-status]] — 这几页在 `extract/dangling.csv`（**2026-09-20 的读数**）里写着 `on-first-invocation-end` 这个名字（该页记录本名字 **7 处引用**，比 [[on-first-invocation-begin]] 少一处——**少的那一处是 [[dc-result-accessor]]**）。**本页没有读它们。**
- **入边（`extract/edges.jsonl`，2026-09-17 的快照）**：链到本页出处文档 `…139` 的边 **53 条 / 39 篇**（**全部 `resolved`**；52 条 `inline` + 1 条 `toc`；**0 条落在代码跨度里**）。
  **对照 [[on-first-invocation-begin]] 的 112 条 / 75 篇——BEGIN 被链的次数是本页的两倍多。**
  **两个名字在同一批文档里不对称，这是本页给的一个数**；**为什么不对称，语料没有一句话说，本页不解释。**
- [[flush]] — Example 3 的最后一行调的就是 `FLUSH()`（那一行在上面「语法 / 参数」节里）。**这是本页出处文档与 [[flush]] 唯一一处接触**，原文对那一行没有任何解释。
- **只写反引号、不写链接的名字**：`ON_LAST_INVOCATION_BEGIN` / `ON_LAST_INVOCATION_END`（`02.07.04.01.140` / `.141`）、`FOR_SEMI_PARALLEL_TEST_BEGIN` / `FOR_SEMI_PARALLEL_TEST_END`（`.73` / `.74`）、`Controlling Multiple Sites`（`02.07.03.13`）、`Site States and Test Method Programs`（`02.07.03.13.06`）、以及 Example 3 里那批调用（`Routing.pin`、`Analog.DGT`、`EXECUTE_TEST`、`TM::SINGLE`、`ARRAY_D`）——**都不在 `extract/prose-allowlist.txt` 里**，按 §9.1 一律反引号。

## 版本

本文档**有** `## Functional changes` 段，**只有一条**：

- `Introduced before SmarTest 6.3.2`

**这一条是哨兵值，不是「6.3.2 的变更」**（`schema.md` §11.2②）：`Introduced before` 的意思是
「**在本文档集覆盖范围开始之前就已经有了**」——**照字面读会读成「6.3.2 新增了 ON_FIRST_INVOCATION_END」，那是错的。**
对照页：[[smartest-6.3.2]]（**版本页，不是本页建的**）。

**本页这一条与 [[on-first-invocation-begin]] 那篇的那一条逐字相同**——**两篇文档的版本段是同一个模板行**。
**两篇都没有第二条**，所以「END 是什么时候引入的、那三个 Example 是哪个版本的」**语料未写，本页不推测**。

## 出处

- 定义文档（本页 `sources:` 唯一一篇，**整篇读过**）：
  `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.139_ON_FIRST_INVOCATION_END.md`
  （TDC `29532.htm`，3,233 字节 / 90 行）。
- **本篇没有重复投放**：全语料按 `source_topic` 查 `29532.htm`，**只有这一个文件**。
- **本页「语法 / 参数」节的来源就是这一篇自己**，节里那 1,588 字符是原文的 `## Syntax` + 三个 `## Examples` + 段末那段说明。
- **本页比 [[on-first-invocation-begin]] 那页短，是原文如此、不是本页漏了**：这一篇**没有 `## Application note` 段**，正文只有三句散文（首句 / 配对句 / 指路句）。

### 本页读的图：**0 张，因为这一篇一张图都没有**

**实测该篇对 `raw/` 的图片引用 0 处**（`grep -c '!\['` 零命中）。
**这不是「图够不着」，是这一篇本来就不带图**——所以本页**没有任何来自图的结论**，也没有一处需要标「④ 图证」。

### 本页与 [[on-first-invocation-begin]] 那一篇的差别（**本页实测 diff 出来的，不是转述**）

两篇去掉标题与编号后**只差四处**：① 首句；② 配对句里被链的是哪一个名字；
③ **BEGIN 那篇独有 `## Application note`（五条）**，本页在同一个位置上只有那句指路；
④ 语法块那一行。**其余两篇逐字相同**（三个 Examples、段末说明、头文件那一行、
`## Related information` 名单、`## Functional changes`）。
**所以「这两页看着像同一篇」不是本页抄的，是语料本来就那样**——**两篇的 Example 集是共用的**。

### 本页没做的

- **[[on-first-invocation-begin]] 那一篇的 `## Application note` 与首句，本页一律不写**——
  那是**那一篇的内容**，不在本页的 `sources:` 里。**这是本页「薄」的原因；本页没有为了把两页对齐而搬它。**
- **`## Related information` 列的九篇一篇没读**：`ON_FIRST_INVOCATION_BEGIN`（`.138`）、
  `ON_LAST_INVOCATION_BEGIN`（`.140`）、`ON_LAST_INVOCATION_END`（`.141`）、
  `FOR_EACH_SITE_BEGIN`（`.70`）、`FOR_EACH_SITE_END`（`.72`）、
  `FOR_SEMI_PARALLEL_TEST_BEGIN`（`.73`）、`FOR_SEMI_PARALLEL_TEST_END`（`.74`）、
  `Controlling Multiple Sites`（`02.07.03.13`）、`Site States and Test Method Programs`（`02.07.03.13.06`）
  ——**所以「这几个块之间怎么嵌套」本页一个字没有。**
- **`TEST` / `LIMIT` / `TESTSET` 没读。** 注意：**这三个名字本页的出处文档根本没有点名**
  （它们只出现在 BEGIN 那一篇的 `CAUTION` 里）——**所以本页连那条警告都写不了。**
- **Example 3 里那批 API 的参数含义本页一个字没有**（`Routing.pin` / `Analog.DGT` /
  `EXECUTE_TEST` / `ARRAY_D` / `TM::SINGLE` / `FLUSH()`）。
- **没有实跑。** 没有写过 first-invocation 块、没有在多 site 机台上跑过。
  **`verified: doc-only` 指的就是这件事。**
- **没有跑 `verify_stages.py`**（按开工简报的要求，避免与别的批次抢同一个报告文件）。
- **没有动 `wiki/index.md`**，也没有把本页挂进 [[testmethod]] 那页。

### ⚠️ 语料瑕疵（照实记，一处都没替它改）

**① 段末那句话里单复数不一致：`the all connected site` 与 `on all connected sites` 并存。**

> 「Hence, the analog modules on the all connected site, specified by the "Aout" pin, are enabled and then the measurements are done on all connected sites.」

**前半句是 `the all connected site`（单数 `site`，`all` 的位置也怪），后半句是 `all connected sites`（复数）。**
**本页不替它选一个数、也不改语序**——引文里原样保留（§11.2）。
**这段在 [[on-first-invocation-begin]] 那一篇里逐字相同**（两篇共用这一段），**所以那页有同一处**。

**② 本页这一篇没有编码坏字（§11.2① 那一族）。** 用 `[一-鿿]` 实测**零命中**；
**也没有 §11.2⑤ 那个整词替换**（`DC/DC power units` 实测 0 命中）。
**这不是「没找到」，是查过、结果为零**——**这一点在这一页要紧**：上面「语法 / 参数」节里的
`ON_FIRST_INVOCATION_BEGIN` / `ON_FIRST_INVOCATION_END` / `ARRAY_D` / `EXECUTE_TEST` / `MapiUtil.h`
**都是从正文逐字读到的**，没有一处是坏字或整词替换的产物。

**③ 本页这一篇里没有 `Note` / `CAUTION` 与上文的粘连**（实测这一类零命中）——
**BEGIN 那一篇有**（`branch.CAUTION`）。**本页照实说本页没有，不把那一处记到本页头上。**

`verified: doc-only`
