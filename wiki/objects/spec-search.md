---
type: object
title: SPEC_SEARCH
layer: L2
stage: level
tags: [level, timing, spec-search, test-method-api, l2, primary-status, flush, limit, transition]
related: [level, timing, level-spec, timing-spec, primary-status, flush, limit, spec-tool, spec-value, spec-variable, mapping-level, mapping-timing, testflow-properties-view]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.233_SPEC_SEARCH.md
created: 2026-09-21
updated: 2026-09-21
verified: doc-only
---

> ⚠️ **本页若干处记的是 2026-10-10【之前】的语料形态。**
> 那一轮把语料里的表格一律换成了**指向上游 HTML 的指针**
> （见 `extract/PLAN-表格指针化.md`）。所以下文凡是说「表格被压平 / 被摊平 /
> 一格一行」的地方，指的是**更换之前**的样子 —— 现在语料里那个位置是**一句指针**，
> 真表仍在 `tdc-html/raw/` 的上游 HTML 里。**页码/引文都不受影响。**

# SPEC_SEARCH

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,352 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.233_SPEC_SEARCH.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

For creating a class object:

```
SPEC_SEARCH object("specName", specType);
```

For setting up a spec search test:

```
object.func1.func2 . . .funcN
```

For executing a spec search test:

```
object.execute();
```

For retrieving a result of the spec search test:

```
variable = object.getXXX();
```

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/29753.htm`
> 中**第 2 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 2 列。
> 首行（上游原文）：object | Class object name to be defined

### Example

```
SPEC_SEARCH search_1("freq",TM::TIM);
search_1.specPins("CPandMR").method(TM::Linear).
unit("Hz").start(50).stop(70).numberOfSteps(20).
resolution(0.01);

search_1.execute();
DOUBLE Pval, Fval;
switch(search_1.getResultSpec()){
case TM::TransitionPassFail :
case TM::TransitionFailPass :
Pval = search_1.getPassVal();
Fval = search_1.getFailVal();
break;
case TM::AllPass :
case TM::AllFail :
cout << "No transition found within the search interval" << endl;
break;
}
```

This example defines the "search_1" object and defines conditions of the spec search as shown below:

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/29753.htm`
> 中**第 14 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：7 行 × 2 列。
> 首行（上游原文）：Parameter | Value

Then executes a spec search test and checks the transition type. Then retrieves a pass/fail transition value or displays an error message.

<!-- 语法节 end -->

## 是什么

**`SPEC_SEARCH` 是一个 L2 API，它干两件事：执行一次 spec search 测试，并访问「存放这次测试条件的数据容器」。**
原文第一句就是这两件事，逐字：

> 「The SPEC_SEARCH API executes a spec search test, and accesses the data container holding the
> conditions of the spec search test.」

**它不是「读一个 spec 的值」，也不是「改一个 spec 的值」**——
**它是「把一个 spec 的值从 start 往 stop 挪，一路测，直到测出 pass/fail 跳变点」**。
原文对「什么时候停」只有一句：

> 「This API stops the spec search when pass/fail or fail/pass transition is found.」

**所以它的产物是「跳变发生的那两个值」（pass 值与 fail 值），不是「一个测量结果」。**
（**本页的读法（推断）**：依据是原文 `stops … when … transition is found` 这一句
＋ `getPassVal()` / `getFailVal()` 两个成员函数的说明——**两者合起来指向「找边界值」这个用途**。）

### 它搜的是哪一种 spec：**timing 或 level，两选一**

构造函数的两个参数原文各一句：`specName` = `Target spec name`，
`specType` = `Type of the target spec. The following specifiers can be set:`，两个取值是：

| 取值 | 原文 | 意思 |
|---|---|---|
| `TM::TIM` | `Timing spec` | 搜 **timing** spec |
| `TM::LEV` | `Level spec` | 搜 **level** spec |

**这一条解释了本页 `stage` 为什么是 `level`**：它**两边的 spec 都搜**，
而 `stage` 按 §6 填的是「最近的一段」——骨架给的是 `level`。
**本页的 raw 里 `TM::TIM` 与 `TM::LEV` 是并列的，没有偏向任何一边。**

### 它的完整外形：一个构造函数 + 十六个成员函数

**下面这一段是逐字引的，它不在本页的「语法 / 参数」节里**——
raw 里它们挂在 `## Class definition` 与 `## Member functions` 下（**脚本的抽取口径如此，本页不改它**）：

```
SPEC_SEARCH(const STRING& specName, TM::SPEC_TYPE specType);
```

```
SPEC_SEARCH& specPins(const STRING& pins);
SPEC_SEARCH& method(TM::SPEC_METHOD method);
SPEC_SEARCH& start(DOUBLE min);
SPEC_SEARCH& stop(DOUBLE max);
SPEC_SEARCH& stepWidth(DOUBLE step);
SPEC_SEARCH& numberOfSteps(INT step);
SPEC_SEARCH& resolution(DOUBLE resolution);
SPEC_SEARCH& resultPins(const STRING& r_pins);
SPEC_SEARCH& limits(STRING testname);
SPEC_SEARCH& limits(LIMIT limit);
SPEC_SEARCH& unit(const STRING& unit_v);
void execute();
TM::SPEC_RESULT getResultSpec();
DOUBLE getPassVal();
DOUBLE getFailVal();
```

**签名本身说明了两件事**：

1. **十一个成员返回 `SPEC_SEARCH&`**——**所以条件可以链式串起来写**
   （例子就是 `search_1.specPins("CPandMR").method(TM::Linear).unit("Hz").start(50).stop(70).numberOfSteps(20).resolution(0.01);`）。
   **`execute()` 与三个 `get*` 是仅有的四个不返回 `SPEC_SEARCH&` 的成员。**
2. **`limits()` 重载了两次**：一次收 `STRING testname`，一次收 `LIMIT limit`。

头文件位置也是原文给的：

> 「This API is defined in the header file /opt/hp93000/soc/prod_com/include/MAPI/SpecSearch.h.」

### 十一个设置型成员，逐个说清

**这张表是本节的主干**。引号内是原文，其余是本页的读法：

| 成员 | 原文要点（逐字引号内） | 本页的读法 |
|---|---|---|
| `specPins()` | `Specify a pin or a list of pins/pin groups.` + `The spec is shifted for these pins.` | **谁被挪**——被挪的是列出的这些 pin 上的 spec |
| `method()` | `specifies a search method`；枚举是 `enum SPEC_METHOD{Linear, Binary, LinBin};` | **怎么挪**（见下节三种方法） |
| `start()` | `defines a start values of the spec search`；**没给就取 spec window 里的 `"minimum"` 值** | 起点 |
| `stop()` | `defines a stop value of the spec search`；**没给就取 spec window 里的 `"maximum"` 值** | 终点 |
| `stepWidth()` | `defines the step width … in the unit specified with the corresponding spec.`；`optional if the mode is Binary` | 步长（**与 `numberOfSteps` 互相覆盖**，见下） |
| `numberOfSteps()` | `defines the number of steps`；`optional if the mode is Binary` | 步数（**同上**） |
| `resolution()` | `defines the smallest step size to be used in the binary search.`；**`required for all` 三种方法** | **唯一一个三种方法都必须给的** |
| `resultPins()` | `defines a name of a pin, pins or pin group that contribute to the pass/fail result`；**`optional and overrides the settings of the specPins member functions`** | **它覆盖 `specPins()`** |
| `limits()` | `sets the start and stop values using a test name or LIMIT API's class object`；**`optional and overrides the settings of the start and stop member functions`** | **它覆盖 `start()` / `stop()`** |
| `unit()` | `specifies the unit to be used for displaying results in data logging`；**`optional`** | **只影响数据日志里的显示**，不影响搜索 |
| `execute()` | `This member function executes a spec search test.` + `There are no parameters in this member function.` | 执行 |

**两处「互相覆盖」是这张表里最容易踩的**，原文各写了一句：

> `This value will be overridden when the numberOfSteps member function is used after this member function.`（`stepWidth()` 那一节）

> `This value will be overridden when the stepWidth member function is used after this member function.`（`numberOfSteps()` 那一节）

**两句合起来是一条顺序规则**：**后写的那个赢。**
**两条关于「可选」的说法要一起读**：`stepWidth` / `numberOfSteps` 都写 `This is optional if the mode is Binary.`
——**即：Binary 模式下这两个都可以不给**（**那 Linear / LinBin 下呢？本篇没有正面写**
——**这是本页读出来的空缺，本页不替它补**）。

### 三种搜索方法（`method()` 的唯一参数）

原文给的枚举与三个取值逐字：

| 取值 | 原文（逐字） |
|---|---|
| `TM::Linear` | `A linear search from the start value to the stop value, with a test interval of resolution.` |
| `TM::Binary` | `A binary search from start to stop. The minimum interval is set with the resolution.` |
| `TM::LinBin` | `A linear search from start to stop with an interval resolution, followed by a binary search between the last passed and first failed linear measured values, using the maximum resolution of the test system hardware.` |

**`LinBin` 是两者串起来**（先线性、再在「最后一个 pass」与「第一个 fail」之间二分），
**而且它的二分用的是「测试系统硬件的最大分辨率」**（`the maximum resolution of the test system hardware`）
——**这一句是三种方法里唯一提到硬件的**。

### 结果怎么取：一个判型 + 两个取值

**`getResultSpec()` 返回 `TM::SPEC_RESULT`，四个取值原文各一句**：

| 取值 | 原文 |
|---|---|
| `TransitionPassFail` | `A pass to fail transition is found.` |
| `TransitionFailPass` | `A fail to pass transition is found.` |
| `AllPass` | `All the functional tests are passed.` |
| `AllFail` | `All the functional tests are failed.` |

**两个取值成员的有效性规则必须成对读**（原文两句结构完全对称）：

| | pass→fail 跳变时 | fail→pass 跳变时 | 没有跳变时（AllPass / AllFail） |
|---|---|---|---|
| **`getPassVal()`** | **最大值**（`a maximum pass value`） | **最小值**（`a minimum pass value`） | **无效**（`does not return a valid value`） |
| **`getFailVal()`** | **最小值**（`a minimum fail value`） | **最大值**（`a maximum fail value`） | **无效**（`does not return a valid value`） |

**⚠️ 这两行的「最大 / 最小」是反着的，照抄时最容易抄错**：
**pass→fail 时 `getPassVal()` 给的是「最大的那个 pass 值」、`getFailVal()` 给的是「最小的那个 fail 值」；
fail→pass 时两个都换成另一头。** 原文用的就是 `maximum` / `minimum` 这两个词，**本页照原样转。**

**「没有跳变就无效」这件事原文写了两遍**（两个成员的说明里各一次，措辞一样），
**并且原文在 `getResultSpec()` 那一节给了用法建议**：
「From the returned specifier, you can determine which member function is applicable to
retrieve the transition value of the spec search test. See Example.」
——**先用 `getResultSpec()` 判型，再决定取哪个值**，例子就是照这个写的。

### 一条前置：**它自己会激活 primaries；用 `PRIMARY_STATUS` 改过的要先 `FLUSH`**

这是本页与别的页咬得最紧的一处，原文两句，第一句是**行为**、第二句是**前置**：

> 「Before the test, this API activates the digital primaries specified in the Testsuite dialog.
> To activate the digital primaries that are changed with the PRIMARY_STATUS API, put the FLUSH API
> prior to the SPEC_SEARCH API.」

| 事实 | 读法 |
|---|---|
| **它自己会激活 digital primaries** | **而且激活的是「Testsuite 对话框里指定的那些」**——**不是任意一套** |
| **但 `PRIMARY_STATUS` 改过的那一套，它激活不了** | **要在它前面放一次 `FLUSH`**（原文 `put the FLUSH API prior to the SPEC_SEARCH API`） |
| **为什么** | **本篇没有写理由**——只写了「要这么做」（**「FLUSH 把改动反映下去」这件事写在 [[flush]] 与 [[timing-spec]] 那一族里，本页没读**） |

**这条和 [[timing-spec]] 那一页的清单对得上**：那一页把「改值生效」的清单里
列了一条 `FLUSH then SPEC_SEARCH.execute() member function)`（**本页读过的 wiki 页**）。
**两边说的是同一件事：`SPEC_SEARCH` 想吃到 `PRIMARY_STATUS` 的改动，前面必须有 `FLUSH`。**

## 典型用法

### 例子逐行走一遍（**例子在「语法 / 参数」节里，本页不重复抄**）

| 行（逐字） | 它在干什么 |
|---|---|
| `SPEC_SEARCH search_1("freq",TM::TIM);` | **建对象**：目标 spec 名 `freq`，类型 **timing spec** |
| `.specPins("CPandMR")` | 被挪的 pin：`CPandMR` |
| `.method(TM::Linear)` | 用**线性**搜索 |
| `.unit("Hz")` | 结果在数据日志里的单位是 **Hz** |
| `.start(50).stop(70)` | 搜索区间 **50 Hz → 70 Hz** |
| `.numberOfSteps(20)` | **20 步** |
| `.resolution(0.01)` | 分辨率 **0.01** |
| `search_1.execute();` | **执行** |
| `switch(search_1.getResultSpec()){ … }` | **判型**：两种跳变 → 取 `getPassVal()` / `getFailVal()`；`AllPass`/`AllFail` → 打印 `No transition found within the search interval` |

**原文自己还给了一张「这个例子定义了哪些条件」的对照表**（逐字转录要点）：
`Spec type` = `Timing spec (TM::TIM)`、`Target pin` = `CPandMR`、`Search method` = `Linear search (Linear)`、
`Search range` = `50 Hz to 70 Hz`、`Number of steps` = `20`、
`Resolution for the getPassVal or getFailVal member function` = `0.01`。

> **⚠️ 那张表的最后一行与成员函数的说明对不上**——见「出处」瑕疵②：
> 成员函数那一节说 `resolution` 是**搜索用的最小步长**（`required for all` 三种方法），
> 而例子这张表把它说成 **`Resolution for the getPassVal or getFailVal member function`**（取结果的精度）。
> **原文两处都在，本页并列摆着，不替它选一个。**

### 最短可用的一段（**照例子缩，非原文模板——所以本页不把它排成代码块**）

**本页不在这里贴一段「可照抄的代码」**：例子的完整形态在「语法 / 参数」节里，
**而任何缩写版都不是原文**——**排成代码块就会被当成逐字引文读**（§11.1）。
**所以这里只把形状说出来**：**建一个 `SPEC_SEARCH` 对象（传 spec 名与 `TM::TIM` / `TM::LEV`），
用链式写法依次挂上 `specPins(...)`、`method(...)`、`start(...)`、`stop(...)`、
`numberOfSteps(...)`（或 `stepWidth(...)`）、`resolution(...)`，然后 `execute()`**——
**最后按 `getResultSpec()` 的分支取 `getPassVal()` / `getFailVal()`。**
**要真用，回「语法 / 参数」节抄完整例子**（那里有 `unit("Hz")` 与那一整段 `switch` 结果处理）。

### 顺序（**本篇能确证的五步**）

1. **（如果用 `PRIMARY_STATUS` 改过 primary）先 `FLUSH`**——
   否则 `SPEC_SEARCH` 激活的不是你改的那一套（原文 `put the FLUSH API prior to the SPEC_SEARCH API`）。
2. **建对象**：`SPEC_SEARCH obj(specName, specType)`。
3. **链式设条件**：`specPins` / `method` / `start` / `stop` / 步长类 / `resolution` / `resultPins` / `limits` / `unit`。
   **`resolution` 必须是给的**（三种方法都要）。
   **步长类两个成员之间、`resultPins` 与 `specPins` 之间、`limits` 与 `start`/`stop` 之间，
   都是「后写的覆盖先写的」。**
4. **`execute()`**。
5. **先 `getResultSpec()` 判型，再按型取 `getPassVal()` / `getFailVal()`**——
   **`AllPass` / `AllFail` 时这两个值无效**，原文的例子在这种情况下只打印一句话。

### 三件本篇没写、用的人会问的

| 问题 | 本篇 |
|---|---|
| **「Testsuite 对话框里指定的 digital primaries」在哪设、设成什么** | **没写**（那是 GUI 侧的事，本页没读） |
| **搜索过程中「测」的是什么测试** | **没写**——原文只说 `All the functional tests are passed.` 里的 `functional tests`，**没说什么测试、多少次** |
| **三种方法各自耗时 / 适用场合** | **没写**（只有 `LinBin` 那一句提到它用硬件最大分辨率） |

## 和谁有关

| 和谁 | 什么关系 | 依据 |
|---|---|---|
| [[flush]] | **前置（必须先执行）**。要用 `PRIMARY_STATUS` 改过的那套 primaries，**必须在 `SPEC_SEARCH` 之前放一次 `FLUSH`** | 本篇第一段（**文档事实**）；**`FLUSH` 自己的 raw 本页没读** |
| [[primary-status]] | **上游（改动来源）**。原文那句说的就是「被 `PRIMARY_STATUS` API 改过的 digital primaries」 | 本篇第一段（**文档事实**）；**那篇 raw 本页没读** |
| [[timing-spec]] | **同类对照 / 交叉印证**。`specType` 取 `TM::TIM` 时搜的是 timing spec；而那一页的「改值生效」清单里**列了 `FLUSH then SPEC_SEARCH.execute()`** ——**与本篇那句 `put the FLUSH API prior to …` 是同一件事** | [[timing-spec]]（**本页读过的 wiki 页**）；本篇 `TM::TIM`（**文档事实**） |
| [[level-spec]] | **另一半（level 侧）**。`specType` 取 `TM::LEV` 时搜的是 level spec；那一页**已经把关系划清**：它写着 [[mapping-level]] 给本页「单独一行（Spec Tool 里做 search 测量）」，**并明写「与本页不是同一件事」「本页不把它算成 spec 改值」** | [[level-spec]] 的 `## 和谁有关`（**本页读过的 wiki 页**）；本篇 `TM::LEV`（**文档事实**） |
| [[limit]] | **`limits()` 的第二种形态**：`limits(LIMIT limit)` 收的是 `Class object name of the LIMIT API.` | 本篇 `limits()` 一节（**文档事实**）；**`LIMIT` 那一篇本页没读** |
| [[spec-value]] / [[spec-variable]] | **它挪动的那个量**。原文用的是 `The spec is shifted for these pins.`——**本篇没有出现 `spec value` 这个说法**，所以这一行是**本页的读法（推断）**，依据是「shift 一个 spec」＋ `getPassVal()` / `getFailVal()` 取的是数值 | 本篇 `specPins()` 一节（**文档事实：`The spec is shifted`**） |
| [[spec-tool]] | **GUI 侧的同族入口**。[[level-spec]] 那页说 [[mapping-level]] 给本页标注的位置是「Spec Tool 里做 search 测量」 | [[level-spec]]（**本页读过的 wiki 页**）——**本页没读 `spec-tool` 那一篇** |
| [[mapping-level]] / [[mapping-timing]] | **两张跨层对照表**。前者给本页留了一行（据 [[level-spec]]），后者是 timing 侧的对照表。**两页本页都没读** | 本页没读（**取材边界**） |
| `Properties view`（**未建**） | `limits(STRING testname)` 那句写的是 `Test name that can be referred from the Properties view.`——**「哪个 Properties view」本篇没写**。**本页不替它链任何 view 页** | 本篇 `limits()` 一节（**文档事实：只有这句描述**） |
| [[level]] / [[timing]] | **两个 stage 页**。本页 `stage: level` 是骨架给的（§6：「最近的一段」不是「归属」）——**而本篇 raw 里 `TM::TIM` 与 `TM::LEV` 并列**，所以这个值不能读成「它只属于 level」 | frontmatter 约定 + 本篇 `specType` 取值（**文档事实**） |

> **一条来自别人页面的记载，本页照实转述**：[[level-spec]] 的 `## 和谁有关` 里，
> 本页被写着「[[spec-search]]（未建）」——**那是一句话里的时间戳**：
> 那一页写的时候本页还没有页，**现在本页存在（骨架已建，正文就是本页）**。
> **本页不改那一页**（§9.1 与「不要动别人的页」），只在这里记一笔。

## 版本

**本文档没有 `## Functional changes` 段。**

这是**查过的事实，不是漏读**：本篇的 `##` 级标题只有四个——
`## Class definition`、`## Constructor`、`## Member functions`、`## Example`
（实测把全部 `#` 开头的行列出来核对过）。**`Functional changes` 这个串在本篇里出现 0 次。**

**所以**：`SPEC_SEARCH` 是哪个版本引入的、`LinBin` 是不是后加的、`TM::LEV` 一开始就支持吗——
**在本篇里一个字都查不到**。（本页**不替它编一个版本号**。）

## 出处

`sources:` **一篇**：

- `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.233_SPEC_SEARCH.md`
  （frontmatter 的 `source_topic` 是 `29753.htm`，**11,281 字节 / 547 行，整篇读完**——
  按 §11.5 口径：字节是 `st_size`，行数是 `wc -l`）
- **重复投放检查做过**（§10 第 0 步）：全语料里 `source_topic: "29753...` **只有这一份**，
  **没有第二投放**。
- 本页的「语法 / 参数」节是脚本从这一篇抽的（**本页一个字没动**）。
  **它抽到的是两段**：`### Syntax`（四种用法的骨架）与 `### Example`（那一段完整例子）。
  **十六个成员函数的签名不在语法节里**——raw 里它们挂在 `## Class definition` 与 `## Member functions` 下
  （**脚本按段标记抽，所以不进去**）。**本页在正文里逐字引了一次，语法节一个字没动。**

**本页没做的**：

- **没有 `## Related information` 段可读**——本篇**没有这一节**（实测 `Related information` 出现 0 次）。
  **所以没有一个「官方指定该看哪几篇」的清单**；本页的「和谁有关」全部是从正文里点到的名字
  （`PRIMARY_STATUS` / `FLUSH` / `Testsuite dialog` / `LIMIT` / `Properties view`）**加本页读过的 wiki 页**拼出来的。
- **本篇没有 `#### Subtopics`**（实测出现 0 次）——**所以它没有下钻层可读。**
- **`PRIMARY_STATUS` / `FLUSH` / `LIMIT` 三篇的 raw 一篇没读**——
  本页只在**本篇**里见过它们的名字与那一两句话。
- **`Test suite` 对话框、`Properties view`、`spec tool`、`spec window` 这些 GUI 侧的东西一样没读**——
  **所以「`start` / `stop` 不写时取的那个 `"minimum"` / `"maximum"` 在哪设」本页答不了**
  （原文只说 `defined in the spec window of the timing or level spec`）。
- **`TIMING_SPEC` / `LEVEL_SPEC` 两篇没读**——本页只在 [[timing-spec]] 与 [[level-spec]]
  （**两页 wiki，已读**）里知道它们的存在与那一条「FLUSH then」的清单。
- **图**：**本篇对 `raw/` 的引用 0 处**——实测 `.png` / `.jpg` / `.gif` / `!\[` / `<img` / `raw/`
  六种写法在本篇里**全部 0 命中**。**所以本页没有任何来自图的结论，这张「没有图」是查过的事实，
  不是「够不着」。**
- **没有实跑。** 没在机台上跑过 spec search、没验过 `Linear` / `Binary` / `LinBin` 的差别、
  没验过 `AllPass` 时 `getPassVal()` 到底返回什么。
  `verified: doc-only` 指的就是这件事。

**⚠️ 本篇的语料瑕疵，本页照实记下、一处都没替它改**：

> ① **`stepWidth()` 与 `numberOfSteps()` 两个签名的参数名，两处不一样。**
> `## Class definition` 里逐字是：
>
> `SPEC_SEARCH& stepWidth(DOUBLE step);`
>
> `SPEC_SEARCH& numberOfSteps(INT step);`
>
> 而 `## Member functions` 里那两节的签名逐字是：
>
> `SPEC_SEARCH& stepWidth(DOUBLE width);`
>
> `SPEC_SEARCH& numberOfSteps(INT num);`
>
> **同一个函数、同一篇文档、两处参数名不同（`step` vs `width` / `step` vs `num`）。**
> **本页两处都照原样引，没有替它统一。**

> ② **例子的结果表把 `resolution` 说成「取结果的精度」。** 逐字：
>
> `Resolution for the getPassVal or getFailVal member function`
>
> 而 `resolution()` 那一节写的是 `defines the smallest step size to be used in the binary search.`
> 与 `This parameter is required for all the spec search method, Linear, Binary and LinBin.`
> **「搜索用的最小步长」与「取 pass/fail 值的精度」不是同一个意思**——
> **两处都在本篇里，本页并列摆着，不替它判哪个是笔误。**

> ③ **参数表被压平后「取值 + 说明」粘成一段**：`method()` 那一节的参数格里逐字是
> `TM::Linear A linear search from the start value to the stop value` 之类——
> **三个取值连着各自的说明挤在同一格里**（和同批其它篇一个形状）。
> **本页在正文里把三个取值拆成三行**（那是**本页的排版**，
> **引文块里照原样保留不拆**——见正文那张表的引号内文字）。

> ④ **`start()` 一节里 `defines a start values of the spec search`——`a` 与复数 `values` 不搭**
> （`stop()` 那节写的是 `defines a stop value`，单数）。
> **原文如此，本页照原样引，没有替它改。**

> ⑤ **`resolution()` 那一节里，圆整规则举的例子是 `start` 被圆整**：
> `if resolution is set to 0.01 and start value is set to 1.555, start value will be rounded off
> and assumed to be 1.56.`——**但它同一段还说会圆整 `stepWidth` 与 `numberOfSteps`**，
> **那两个举不出来例子**（原文只举了 `start` 一个）。**这不是错，是原文的举证范围，记一笔。**

`verified: doc-only`
