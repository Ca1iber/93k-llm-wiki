---
type: object
title: FOR_EACH_SITE_BEGIN
layer: L2
stage: testmethod
tags: [testmethod, test-method-api, mapi, multi-site, site-loop, loop-block, site-specific-setup, first-invocation-block]
related: [for-each-site-end, on-first-invocation-begin, on-first-invocation-end, controlling-multiple-sites, testmethod]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.70_FOR_EACH_SITE_BEGIN.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# FOR_EACH_SITE_BEGIN

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,751 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.70_FOR_EACH_SITE_BEGIN.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
FOR_EACH_SITE_BEGIN();
```

List of parameters

There are no parameters.

Return value

There is no return value.

### Example 1: Minimum code

The following example shows the minimum code for a "each site loop block". The ellipses ("...") are to be replaced with your code.

```
ON_FIRST_INVOCATION_BEGIN();
    ...
    ...
    FOR_EACH_SITE_BEGIN();
        ...
        ...
    FOR_EACH_SITE_END();
    ...
    ...
ON_FIRST_INVOCATION_END();
```

### Example 2: Optional curly brackets

The example utilizes optional pairs of curly brackets "{" and "}". These optional curly brackets are used for simplifying the correct indentation with assistance of the related Eclipse tool.

```
ON_FIRST_INVOCATION_BEGIN();
{
    ...
    ...
    FOR_EACH_SITE_BEGIN();
    {
        ...
        ...
    }
    FOR_EACH_SITE_END();
    ...
    ...
}
ON_FIRST_INVOCATION_END();
```

### Example 3

```
ON_FIRST_INVOCATION_BEGIN();
{
    //
    // Pre-measurement
    //
    PMU_IFVM pmuIfvm("Aout_trig");
    ...
    ...

    //
    // Serial execution for all Sites - BEGIN
    //
    FOR_EACH_SITE_BEGIN();
    {
        //
        // Get pre-measurement result for each site
        //
        DOUBLE V_off = pmuIfvm.getValue("Aout_trig");

        //
        // Set pre-measurement result for each site
        // as site-specific setup condition
        //
        DGT("Aout").vOffset(V_off);

        //Serial Execution for All Sites - END
    }
    FOR_EACH_SITE_END();

    //
    // Setup and test Execution on all active sites
    //
    EXECUTE_TEST(0.1 sec);
    ...
    ...
}
ON_FIRST_INVOCATION_END();
```

FOR_EACH_SITE_BEGIN() and FOR_EACH_SITE_END() declare the each site loop block in the first-invocation block. All APIs in each site loop block are executed serially for all sites when the program is run for the first tested site.

<!-- 语法节 end -->

## 是什么

**FOR_EACH_SITE_BEGIN 是 L2（test method API）里的一个「块开始」标记：没有参数、没有返回值，它做的事只有一件——把一段代码标成「逐 site 循环」。**
定义文档第一句（逐字）：

> This API declares the beginning of the block that allows you to execute setup sequentially for all sites before the parallel test.

**这一句里三个限定都是文档事实**：`sequentially`（串行）、`for all sites`（所有 site）、`before the parallel test`（在并行测试之前）。
**它不是「重复 N 遍同一件事」的循环**，是「**让 setup 对每个 site 各做一遍，然后才并行测**」。

**这个块的名字是原文自己起的**：

> - FOR_EACH_SITE_BEGIN and FOR_EACH_SITE_END must be used as a pair. The area enclosed by this pair is called "each site loop block".

注意原文用**双引号**把 `each site loop block` 括起来——**术语是它命名的**（本页沿用，不另起中文名）。
`must be used as a pair` 是硬约束：**本页只负责「开」，闭块在 for-each-site-end。**

**它为什么存在**（`## Application note`）：

> - The each site loop block enables site-specific setup (different setup conditions for each site) before parallel test execution.

**目的是「每个 site 一份不同的 setup 条件」**，不是把同一件事重复做 N 遍。

**定义位置**（原文）：

> This API is defined in the header file /opt/hp93000/soc/prod_com/include/MAPI/MapiUtil.h.

与 for-each-site-end 同一个头文件（`MAPI/` + `MapiUtil.h`）。

### 三条边界：用错了不一定有东西告诉你

这一页的语法是空的（`There are no parameters.` / `There is no return value.`，见上节），**所以真正要记的是边界**——

| 原文（逐字） | 意思 |
|---|---|
| This API is meaningful for multi-site testing. For single-site testing, this API is ignored. | **只在多 site 下有意义；单 site 下它被 ignored（忽略）** |
| All statements in the each site loop block are executed serially for all active sites when the program is run for the first tested site. | 块里的语句**在「第一个被测 site」那一次**执行，**串行**跑遍所有 active site |
| FOR_EACH_SITE_BEGIN and FOR_EACH_SITE_END must be used as a pair. | 少了 `FOR_EACH_SITE_END` 就没有闭合的块 |

**`ignored` 这一条要单独点出来，因为它是「错了不会响」的那一类：**

- 文档写的是「**被忽略**」，**但没说被忽略掉的是「这一次 API 调用」还是「整个 each site loop block」**。
  **语料未写**——本页不替它定。
- 本篇**没有** `## Errors` 段、**没有** `## Warnings` 段；`Return value` 一节只写 `There is no return value.`
  **所以没有任何返回值或错误码能让程序发现「用在了单 site 上」或「放错了位置」。**
  （**推断**，依据是上面这三条「本篇没有」——**不是**文档写了「不会有报错」，**是文档没写有**。）
- 同一句话在另一篇里**逐字相同**（`02.07.04.01.71` 的 `## Application note` 第二条）——
  说明「单 site 忽略」是这一族 API 的共同措辞，不是本页的孤例。

### 块放在哪：原文两处的覆盖面不一样

`## Application note` 把它写成**二选一**（下面两块在原文里前后相邻，**本页按原文的行边界断成两个引文块**，没有把它们并成一块，也没有加字）：

> The each site loop block must be placed

>   - in the first-invocation block declared by ON_FIRST_INVOCATION_BEGIN and ON_FIRST_INVOCATION_END or
>   - in the last-invocation block declared by ON_LAST_INVOCATION_BEGIN and ON_LAST_INVOCATION_END.

即：**放在 first-invocation 块里、或放在 last-invocation 块里，两处都行。**

**⚠️ 而 `## Examples` 之后那句只说了 first-invocation**（逐字）：

> FOR_EACH_SITE_BEGIN() and FOR_EACH_SITE_END() declare the each site loop block in the first-invocation block. All APIs in each site loop block are executed serially for all sites when the program is run for the first tested site.

**两处覆盖面不一样**（一处 first 或 last，一处只有 first）。
**本页两处都逐字引、都留着，不替语料统一、也不替它判定哪个为准**——见「出处」的 ⚠️。

### 一篇只有这五节

本篇的 `##` 级标题只有 `## Application note`、`## Syntax`、`## Examples`、`## Related information`、`## Functional changes`。
**没有 `## Errors`、没有 `## Warnings`、没有 `## Procedure`、没有 `## Before you begin`、也没有图**
（正文里 `../../../../raw/` 引用 **0 个**）。
**所以「是什么」只有上面这么多——是文档就这么多，不是本页漏了。**

## 典型用法

### 最小骨架（Example 1）

原文对示例一只有一句说明：

> The following example shows the minimum code for a "each site loop block". The ellipses ("...") are to be replaced with your code.

代码本体已由语法节逐字收录。**它的形状是固定的两层嵌套**：
`ON_FIRST_INVOCATION_BEGIN()` → `FOR_EACH_SITE_BEGIN()` → 你的逐 site 代码 → `FOR_EACH_SITE_END()` → `ON_FIRST_INVOCATION_END()`。
（**推断**：「必须嵌在 first-invocation 块里」这一层，依据是上面 `## Application note` 里 `must be placed` 那句的第一个选项。）

### 花括号是可选的

> The example utilizes optional pairs of curly brackets "{" and "}". These optional curly brackets are used for simplifying the correct indentation with assistance of the related Eclipse tool.

**花括号只为缩进方便（配合 Eclipse 工具），不是语法要求**——Example 1 就没写花括号。

### Example 3 的实际套路：先量、再逐 site 写回、最后才并行测

示例三是本篇唯一带业务内容的例子，三步（代码见语法节）：

1. **进 each site loop 之前**先做 pre-measurement：`PMU_IFVM pmuIfvm("Aout_trig");`
2. **进 each site loop**，逐 site 取结果、逐 site 写回 setup。原文在这一步开头写着
   > // Get pre-measurement result for each site

   紧接着的代码是 `DOUBLE V_off = pmuIfvm.getValue("Aout_trig");`；写回那一步的注释是（原文里**连着两行**）
   > // Set pre-measurement result for each site
   > // as site-specific setup condition

   对应的代码是 `DGT("Aout").vOffset(V_off);`
   （**注意**：`// Get` 开头那行与 `// Set` 开头那行在原文里**不是相邻两行**——
   中间还夹着 `//` 空注释行和 `DOUBLE V_off = pmuIfvm.getValue("Aout_trig");` 那一行。
   **本页因此拆成两个引文块，没有把它们拼成一块。**）
3. **出 each site loop 之后**才跑测试：`EXECUTE_TEST(0.1 sec);`，原文注释逐字：
   > // Setup and test Execution on all active sites

**这个顺序就是「site-specific setup before parallel test」的形状**（**推断**，依据是它自己的注释 `// Serial execution for all Sites - BEGIN` 与 `// Setup and test Execution on all active sites`，与首段那句「setup 按 site 串行、跑遍所有 site、在并行测试之前」对得上）。

**⚠️ `EXECUTE_TEST(0.1 sec)` 里的 `0.1 sec` 是什么语法，本篇没有解释**（**语料未写**）——
本页不替它解释，也不替它改写法。

### 该用 `FOR_EACH_SITE_BEGIN` 还是 `FOR_EACH_SITE_BEGIN_WITH_QUERY`

本篇两处（首段与 `## Application note`）指向同一个选择：

> If you want to sequentially setup and query, use FOR_EACH_SITE_BEGIN_WITH_QUERY.

> - To query setup and result information for the active sites, use FOR_EACH_SITE_BEGIN_WITH_QUERY.

**只在循环里写 setup → 用本页这个；还要在循环里查 setup / 结果 → 换 `FOR_EACH_SITE_BEGIN_WITH_QUERY`。**

后者的闭块用的是同一个 `FOR_EACH_SITE_END`，`02.07.04.01.71` 写得很清楚
（**该篇不在本页 `sources:` 里，理由见「出处」**）：

> It must be used together with FOR_EACH_SITE_END as a pair, called "each site with query loop block". The query focus will be reset by FOR_EACH_SITE_END().

**即：闭块的那一半不变，换的只是「开」这一半。**

## 和谁有关

下表每一行都标了**依据**——哪些是本篇明写的（文档事实），哪些是**按名字读出来的（推断）**。

| 目标 | 是什么关系 | 依据 | 写法 |
|---|---|---|---|
| `FOR_EACH_SITE_END` | **配对的那一半**：本篇开块，它闭块 | 本篇明写 `must be used as a pair` | [[for-each-site-end]] |
| `FOR_EACH_SITE_BEGIN_WITH_QUERY`（raw: `02.07.04.01.71`） | **同族的替代品**：要「setup + 查询」时换它，闭块仍是 `FOR_EACH_SITE_END` | 本篇两处明写要改用它；该篇读了全文 | 不在允许名单，写名字 |
| `ON_FIRST_INVOCATION_BEGIN` / `ON_FIRST_INVOCATION_END`（raw: `02.07.04.01.138` / `.139`） | **外层容器（首选）**：each site loop block `must be placed in` 它俩声明的 first-invocation 块 | 本篇明写 | [[on-first-invocation-begin]] / [[on-first-invocation-end]] |
| `ON_LAST_INVOCATION_BEGIN` / `ON_LAST_INVOCATION_END`（raw: `02.07.04.01.140` / `.141`） | **外层容器（备选）**：原文说也可以放在它们声明的 last-invocation 块里 | 本篇明写 | 不在允许名单 |
| `API Behavior on Multi-Site Testing`（raw: `02.07.03.13.07`） | **正文点名的去处**：讲「只对 setup-focus 状态 site 生效」与「总是对全部 site 生效」两类 API | 本篇 `## Application note` 里 `see` 指向它（**该篇没读**） | 不在允许名单 |
| `CURRENT_SITE_NUMBER()`（raw: `02.07.04.01.20`） | 同族取数 API | **只出现在 `## Related information` 里，本篇没给任何用法**；「取数」是**推断** | 不在允许名单 |
| `FOR_SEMI_PARALLEL_TEST_BEGIN` / `FOR_SEMI_PARALLEL_TEST_END`（raw: `02.07.04.01.73` / `.74`） | 另一对块标记 | 同上：只在 `## Related information` 里；「另一对块标记」是**推断** | 不在允许名单 |
| `Controlling Multiple Sites`（raw: `02.07.03.13`） | **上游总述**：多 site 那一章 | 只在 `## Related information` 里；关系是**推断** | [[controlling-multiple-sites]] |
| `Site States and Test Method Programs`（raw: `02.07.03.13.06`） | 上游：site 状态与 test method 程序的关系 | 只在 `## Related information` 里；关系是**推断** | 不在允许名单 |

### 这 9 条链接的排版：语料没给空格

`## Related information` 那一节的 9 条链接**一个空格都没有**，全部挤在一行。
原文是这样接的——**下面是完整子串，没有省略**：

`](<02.07.04.01.72_FOR_EACH_SITE_END.md>)[FOR_EACH_SITE_BEGIN_WITH_QUERY]`

**`]` 和 `[` 之间没有空格**，本页照记、没替它加。

### 三对块标记之间怎么互相嵌套，语料只写了一半

本篇出现了三族块标记：`FOR_EACH_SITE_*`（本篇与 for-each-site-end）、
`ON_FIRST_INVOCATION_*` / `ON_LAST_INVOCATION_*`（[[on-first-invocation-begin]] / [[on-first-invocation-end]]）、
以及只在 `## Related information` 里露脸的 `FOR_SEMI_PARALLEL_TEST_*`。

- **明写的只有一层**：`FOR_EACH_SITE_*` 的块要放在 `ON_FIRST_INVOCATION_*`（或 `ON_LAST_INVOCATION_*`）声明的块里——见上面那句 `must be placed`。
- **其余语料未写**：`FOR_SEMI_PARALLEL_TEST_*` 与它们是什么关系、两个 each site loop block 能不能并列或嵌套、
  `ON_FIRST_INVOCATION_*` 里除了 each site loop block 还能放什么——**本篇一句都没有**。
  **本页不猜，也不替它排。**

### 另有一页把本篇当依据

[[execution-context-requires-firmware-definition]] 那页的 `sources:` 列了 **8 篇**，
本篇是其中之一，在那页的对照表里标注的用途是「**成对句**」——
也就是说，**本篇 `must be used as a pair` 这句在别处被当成一条约束的依据**。
（依据：读了那页的 frontmatter 与那张对照表；**那页的正文结论本页不复述**。）

### `layer: L2` / `stage: testmethod` 的含义

§6 说 `stage` 填的是「**读者该去哪一段里找它的用法**」，**不是归属**。
本页是测试方法（L2）里怎么写的问题，所以最近的一段是 [[testmethod]]。

## 版本

本篇 `## Functional changes` 段**只有一条**：

> - Introduced before SmarTest 6.3.2

**这一条是哨兵值，不是「6.3.2 新增了它」**（§11.2 ②）：
`before` 的意思是「**在本文档集覆盖范围开始之前就已经有了**」。
**照字面读会生成一条「6.3.2 新增」的假信息，而且格式齐整。**

**注意它和 `Introduced in SmarTest X.Y.Z` 是两种写法**：后者才是「那一版新加的」。本篇这条是前者。

**因此本页不链 `smartest-6.3.2`**——链过去等于承认「它是 6.3.2 引进的」，而这条记录说的恰好相反。

另：`## Functional changes` 是**本篇最后一个 `##` 段**，段后**没有脚注块**（全文到这一行就结束，共 129 行）——
**§11.2 ③ 那条「版本段吞掉脚注」在本篇没有发生。**

## 出处

`sources:` **一篇**：
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.70_FOR_EACH_SITE_BEGIN.md`
（TDC `29344.htm`，4,682 字节，129 行）。**整篇读完。**

**这两个数怎么量的**（§11.5 口径）：字节 = 文件实际大小 `len(path.read_bytes())`；
行数 = `wc -l`。本语料全是 CRLF（本篇 129 行 = 129 个 `\r\n`），
**用 `len(read_text())` 量会少掉「行数」个字节**（4,682 − 129 = 4,553）——**那不是本篇的大小**。

**另外两篇读了全文，但没有写进 `sources:`**：

- `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.71_FOR_EACH_SITE_BEGIN_WITH_QUERY.md`
  （TDC `116559.htm`，4,113 字节，121 行）。**整篇读完。**
- `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.72_FOR_EACH_SITE_END.md`
  （TDC `29350.htm`，1,661 字节，40 行）。**整篇读完。**

**为什么不放进 `sources:`**：本 wiki 的 `sources:` 意思是「**本页讲的就是这一篇**」。
`71` 与 `72` 各自是**另一个对象**（各该有自己的页），把它们挂到本页的 `sources:` 上，
等于替它们声明「已经有页了」——那正好是 §13.1「第七次」记的那个病。
**它们给本页提供的事实，正文里逐条注明了来源。**
（这两篇是本页的两侧：`72` 是配对的那一半，`71` 是同族的第三条命令。）

**本页没做的**：

- **`## Related information` 那 9 个目标里，7 个一篇没读**：
  `CURRENT_SITE_NUMBER()`、`ON_FIRST_INVOCATION_BEGIN`、`ON_FIRST_INVOCATION_END`、
  `FOR_SEMI_PARALLEL_TEST_BEGIN`、`FOR_SEMI_PARALLEL_TEST_END`、`Controlling Multiple Sites`、
  `Site States and Test Method Programs`。
  （另两个 `FOR_EACH_SITE_END` = `72`、`FOR_EACH_SITE_BEGIN_WITH_QUERY` = `71`，已读全文。）
  **所以「和谁有关」表里标了「推断」的那几行，关系是按名字读出来的**，
  不是从那几篇自己的文档里读的。
- **`API Behavior on Multi-Site Testing`（`02.07.03.13.07`）没读**——本篇正文点名要去的正是这一篇。
  **「哪类 API 只对 setup-focus 状态 site 生效、哪类总是对全部 site 生效」这个答案，本页给不了。**
- **`71` 只用了两句**（闭块仍是 `FOR_EACH_SITE_END`、query focus 会被 `FOR_EACH_SITE_END()` 复位），
  它的 `## Application note`、三个示例的细节**本页没有展开**——那是它自己那一页的事。
- **图：本篇 0 张**（正文里 `../../../../raw/` 引用 **0 个**）。**所以本页没有任何来自图的结论。**
  这是「**本页没用图**」，不是「图够不着」（§11.4）。
- **没有实跑**：没在机台上写过 `FOR_EACH_SITE_BEGIN()`，单 site / 多 site 都没跑过。
  `verified: doc-only` 指的就是这件事。

**⚠️ 语料瑕疵，照实记**：

- **坏字（§11.2 ①，判据 `[一-鿿]`）：本篇 0 处**——全文非 ASCII 字符 **0 个**。查过，不是没看。
- **整词替换（§11.2 ⑤，`DC/DC power units`）：0 命中。** 本篇没有这两族毛病。
- **`## Related information` 那 9 条链接之间一个空格都没有**（与本 wiki 已记的 `for-each-site-end` 那处同形），
  完整子串见「和谁有关」那一节，**本页照记、没替它加空格**。
- **同一篇里「块放在哪」的覆盖面不一致**（本页独有，正文见「是什么」）：
  `## Application note` 那处是**二选一**——
  > - in the last-invocation block declared by ON_LAST_INVOCATION_BEGIN and ON_LAST_INVOCATION_END.

  而 `## Examples` 之后那处**只提 first-invocation**——
  > declare the each site loop block in the first-invocation block.

  **两处都逐字引在此，没有统一、没有替语料选一个。** 哪个为准，**语料未写**。
- **示例代码里的注释排版不一致**：Example 3 里注释大多以 `// ` 起头，
  但有一行是 `//Serial Execution for All Sites - END`（`//` 后没有空格）。**照抄，没替它加空格。**
- **`71` 篇里有一处多余的反引号**：`It must be used together with FOR_EACH_SITE_END`` as a pair`
  （链接后面跟着**两个**反引号）。本页引那句时按 §11.1 的规范化去掉了反引号——
  **记在这里，免得读者以为原文没这处。**
- **两篇的示例节标题不一样**：本篇是 `## Examples`（复数），`02.07.04.01.72` 是 `## Example`（单数）。
  **同一套文档两种写法，照记。**

`verified: doc-only`
