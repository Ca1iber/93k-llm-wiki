---
type: object
title: LEVEL_SPEC
layer: L2
stage: level
tags: [level-spec, level, l2, test-method-api, spec-set, spec-value, spec-variable, level-equation-set, primary-status, svlr, flush, restore]
related: [level, mapping-level, primary-status, spec-tool, spec-set, spec-value, spec-variable, svlr, timing-spec, level-file, level-equation-file, equation-based-level-setup, level-setup-tool, flush, spec-search, on-first-invocation-begin, for-each-site-begin]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.124_LEVEL_SPEC.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# LEVEL_SPEC

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,324 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.124_LEVEL_SPEC.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example 1: Changing the primary level specification

The level equation set 1 and spec set 2 are set as primary level specification.

```
LEVEL_SPEC spec1(1, 2);
Primary.level(spec1);
```

### Example 2: Changing a spec value in the primary spec set

The value of the spec v_low is changed to -2.1 V.

```
Primary.getLevelSpec().change("v_low", -2.1 V);
```

or

```
LEVEL_SPEC& ls_obj = Primary.getLevelSpec();
ls_obj.change("v_low", -2.1 V);
```

### Example 3: Changing a spec value in the primary spec set for a specific pin or all pins

For pin VCC the value of vdde is changed to 4.4 V:

```
Primary.getLevelSpec().change("vdde", 4.4, "VCC");
FLUSH(TM::APRM);
```

For all pins the value of vdde is changed to 4.5 V. This includes the VCC pin:

```
Primary.getLevelSpec().change("vdde", 4.5);
FLUSH(TM::APRM);
```

### Example 4: Changing a spec value and assigning a different value for each site

This example shows how you can change a spec value for the variable VCC. Different value is assigned for each site:

```
ON_FIRST_INVOCATION_BEGIN();

    LEVEL_SPEC newSpec(2,2); // Creating a LEVEL_SPEC object to change level set 2 and spec set 2

    FOR_EACH_SITE_BEGIN();

        newSpec.change("VCC", 0.1 * CURRENT_SITE_NUMBER() ); //Assigning new value to VCC

    FOR_EACH_SITE_END();

    FLUSH(); // Writing the changes to the tester

ON_FIRST_INVOCATION_END();
```

### Example 5: Querying a spec value in the primary spec set

The value of the spec v_low is returned:

```
double vLow = Primary.getLevelSpec().getSpecValue("v_low");
```

or (if you know the level equation set number and spec set number),

```
double vLow = LEVEL_SPEC(1, 2).getSpecValue("v_low");
```

<!-- 语法节 end -->

## 是什么

**`LEVEL_SPEC` 是 test method 里访问「一个 level equation set + 一个 spec set」内容的 L2 API。** 原文第一句：

> 「With this API, you can access the contents of an existing level equation and spec set.」

**「existing」是关键词**：它**不新建 equation set、也不新建 spec set**——**那两个是在 Level Setup Tool / equation based level setup 那边建好的**（见「和谁有关」）。

原文把能力列了六条（`The API offers the following functions:`，逐字如下）：

> 「- Retrieve the level equation set number」

> 「- Retrieve the level spec set number」

> 「- Retrieve the value of a spec」

> 「- Change the value of a spec」

> 「- Change the value of a spec for a specific pin」

> 「- Reset the values of specs」

**六个能力，五个成员函数**——原文 `## Member functions` 一节只有五个：

| 能力（原文那六条） | 成员函数 | 签名 |
|---|---|---|
| 取 equation set 号 | `getEquation()` | `INT getEquation();` |
| 取 spec set 号 | `getSpec()` | `INT getSpec();` |
| 取一个 spec 的值 | `getSpecValue()` | `DOUBLE getSpecValue(const STRING& spec);` |
| 改一个 spec 的值 | `change()`（第一个重载） | `void change(const STRING& spec, DOUBLE value);` |
| **改某个 pin 上的值** | **`change()`（第二个重载）** | `void change(const STRING& spec, DOUBLE value, const STRING& pin);` |
| 复位所有 spec | `restore()` | `void restore();` |

**「六对五」不是矛盾**：原文列的是**能力**，`change()` 的两个重载各占一条。

> **⚠️ 这五个成员函数与构造函数都不在「语法 / 参数」节里。** 脚本按**段标记**收，
> 而这一篇的段标记是 `## Examples`——**所以语法节收的是 Example 1–5，
> 构造函数与 `## Member functions` 那一节一个字都没进去**（§4：脚本负责抽取，不重写）。
> **本页在这里逐条写出它们**，逐字照原文。

### 对象的两种建法

**第一种：自己建对象，指定 equation set 与 spec set。**

```
LEVEL_SPEC obj(eqnset, specset);
obj.memberFunction();
```

> 「First you define a LEVEL_SPEC object for the specified equation set and spec set. Then you can work with the object using the member functions of LEVEL_SPEC.」

**一条硬规矩**：

> 「Only one member function can be specified in per statement.」

（**`in per statement` 原文如此**——见「出处」⚠️②。**本页照原样引。**）

**第二种：挂在 primary 上，省掉 set 号。**

```
Primary.getLevelSpec().func();
```

> 「With this syntax, you work with the current primary level spec.」

`getLevelSpec()` 是 **[[primary-status]]** 的成员函数（原文点名并要求参见那篇）；
`func()` 是本页五个成员函数之一。**[[primary-status]] 本页没读**——
**`getLevelSpec()` 自己的签名、`Primary.level(...)` 的行为，本页一个字没有。**

### 三条 `Note` / `CAUTION`，是这一页的边界

**① 不要混：C++ API 与固件命令改同一个值，只许调试时这么干。**

> 「CAUTION Never mix the LEVEL_SPEC or TIMING_SPEC API and firmware commands modifying values for other reasons than debugging purposes (see note below)!」

> 「LEVEL_SPEC and TIMING_SPEC test method APIs cache values in order to enable the .restore() functionality. This caching is not available on the firmware level.」

> 「In both cases, changing spec values takes effect without changing the level or timing file! If you want to change spec values permanently you must do so in the corresponding setup file itself.」

**这一段把三件事同时说清了：**

| 问题 | 答案 |
|---|---|
| `restore()` 为什么救得回来 | **API 在 C++ 侧缓存了原值**（`cache values in order to enable the .restore() functionality`） |
| 为什么固件命令改过的值救不回来 | **那份缓存固件层没有**（`This caching is not available on the firmware level`） |
| 改这个值会不会动到 level / timing 文件 | **不会**（`without changing the level or timing file!`）；**要永久改，得改对应的 setup 文件本身** |

**② 调试时可以停了 application model，从 `hpt` 敲固件命令 `SVLR`，再继续。**

> 「Note For debug purpose only: If you want to change the spec value while the application model is running without having to abort the execution, you can pause the application model, change the spec value with the firmware command SVLR directly from hpt and then resume the running of the application model.」

**这一句就是本页与 [[svlr]] 的关系**：同一件事（改 spec 值）的两条路——
**一条在 C++ 里（本页），一条在 `hpt` 里（`SVLR`）**，而且**原文把固件那条标成 debug 专用**。

**③ 给某个 pin 改的值，只活一个 flush 周期。**

> 「Note The value for the specified pin is only stored for one flush cycle. You cannot retrieve the pin specific values using getSpecValue(spec).」

| 问题 | 答案 |
|---|---|
| 给一个 pin 单独改的值能留多久 | **一个 flush 周期** |
| 能不能用 `getSpecValue(spec)` 读回来 | **不能**（`You cannot retrieve the pin specific values using getSpecValue(spec).`） |

**注意第二条的射程**：`getSpecValue()` **只取不到 per-pin 的那一份**，不是「读不了值」。

### `restore()` 复位的基准点

> 「This member function resets the values of all specs to the ones that were in effect when the test method program in the current test suite is started.」

**基准点是「本 test suite 的 test method 程序开始时」**——
**不是「上一次 change 之前」，也不是「下载的时候」。**

## 典型用法

原文给了五个 Example，**一个 Example 一个动作**（逐字见「语法 / 参数」节）：

| Example | 干什么 | 关键那一行 |
|---|---|---|
| 1 | 把某一组 equation set / spec set 设成 primary | `LEVEL_SPEC spec1(1, 2);` + `Primary.level(spec1);` |
| 2 | 改 primary spec set 里的一个值 | `Primary.getLevelSpec().change("v_low", -2.1 V);` |
| 3 | 改**某个 pin**（或**所有 pin**）上的值 | `Primary.getLevelSpec().change("vdde", 4.4, "VCC");` + `FLUSH(TM::APRM);` |
| 4 | **每个 site 一个值** | `ON_FIRST_INVOCATION_BEGIN();` … `FOR_EACH_SITE_BEGIN();` … `newSpec.change("VCC", 0.1 * CURRENT_SITE_NUMBER() );` … `FLUSH();` |
| 5 | 查一个 spec 的值 | `double vLow = Primary.getLevelSpec().getSpecValue("v_low");` |

**四条读法（都是把原文两处并起来得的）：**

- **改完要 `FLUSH`。** Example 3 两段都以 `FLUSH(TM::APRM);` 结尾，Example 4 的 `FLUSH();`
  后面还带一句注释 `// Writing the changes to the tester`。
  **为什么必须 FLUSH、FLUSH 到不到硬件——本页答不了**：
  [[flush]] 那页写的是「`LEVEL_SPEC` 的改动**只到固件层、不到硬件**」，
  **那一条不是本页的出处文档说的**（见「出处」）。
- **改一个 pin 和改所有 pin 是同一个函数的重载。** Example 3 给了两段：带 `"VCC"` 的一段落在一个 pin 上，
  不带 pin 的那段是 `4.5`，「**including the VCC pin**」——**即不带 pin 就是全体（含刚才单独改过的那个）。**
- **Example 2 的第二种写法把结果绑成了一个引用**（`LEVEL_SPEC& ls_obj = Primary.getLevelSpec();`），
  **而 Example 5 的第二种写法直接构造临时对象**（`LEVEL_SPEC(1, 2).getSpecValue("v_low")`）。
  **两种写法并存，本页并列，不判哪种是规范写法。**（**推断**：只能说明 `getLevelSpec()` 返回的东西可绑引用。
  ——**它的返回类型本页没读到**，因为 [[primary-status]] 那篇本页没读。）
- **Example 4 的三个作用域块**：`ON_FIRST_INVOCATION_BEGIN/END`（[[on-first-invocation-begin]] /
  [[on-first-invocation-end]]，**均未建**）套着 `FOR_EACH_SITE_BEGIN/END`
  （[[for-each-site-begin]] / [[for-each-site-end]]，**均未建**），
  里面用 `CURRENT_SITE_NUMBER()` 算值。**那三个块本页一个都没读**，
  **所以「它们各自什么语义、能不能不嵌套」本页答不了。**

**本篇没有 `## Procedure`，也没有 `## Before you begin`**——**原文只有 `## Usage of the API`、
`## Member functions`、`## Examples` 三节加一组 Related information。**

**⚠️ `-2.1 V` 不是合法 C++**（数值后面跟一个单位），**原文 Example 2 的两段都这么写**——
**本页照原样引，一处没替它改**（见「出处」⚠️③）。

## 和谁有关

- [[level]] / [[mapping-level]] — **本页 `stage: level` 的理由**。[[mapping-level]] 主表第 124 行「运行时改 spec 值并重算」把这一件事分到五格：**GUI = [[spec-tool]] 的 Download（`File > Download`）；文件 = [[level-file]] 的 `SPECS` / `SPECSET` 块；L1 = [[svlr]]；L2 = 本页与 `Primary.getLevelSpec()`；L3 = `?`**——**本页与 [[svlr]] 在同一行里分列 L2 / L1 两格**。
- [[primary-status]] — **本页的另一半**：`Primary.getLevelSpec()` 与 Example 1 的 `Primary.level(spec1)` 都出自它。原文 `Related information` 第一条就是它。**那页本页没读**（wiki 里已有页），**所以上面那两条的签名本页一个字没有。**
- [[timing-spec ]] — **同一套 API 的 timing 侧**：原文的 CAUTION 把两者并列（`the LEVEL_SPEC or TIMING_SPEC API`），`Related information` 也点了它。**它的成员函数、签名本页一个字没有**；**「本页与它是同一套设计」是本页的（推断）**，依据只有那句并列。
- [[svlr]] — **改同一个东西的固件命令**，被原文写在「debug 专用」的 `Note` 里（见上）。**别把它和 [[spec-set]] / [[spec-tool]] 混**：本页与 [[svlr]] 是**改值**的两条路，那两个是**容器与工具**。
- [[spec-tool]] — **GUI 侧改 spec 值的入口**（[[mapping-level]] 那一行的 GUI 格）。**本页没读它**，所以**「GUI 上怎么改、改完要不要 Download」本页答不了**。
- [[spec-set]] / [[spec-value]] / [[spec-variable]]（**后两个未建**）— **本页操作的是「spec set 里的一个 spec 值」**：[[spec-set]] 是那个容器的页，[[spec-value]] / [[spec-variable]] 是 **UTM 参数类型**那一侧（[[mapping-testmethod]] 主表把它挂在建 test method 类那一行的 L2 格）。**三层东西，本页只占「L2 改值」这一格**（**推断**，依据是各自页名与两张对照表的行位）。
- [[level-file]] / [[level-equation-file]]（**后者未建**）— **值存在哪**：[[mapping-level]] 把 spec 值放在 [[level-file]] 的 `SPECS` / `SPECSET` 块里；原文则明说改值**不动 level 文件**（`changing spec values takes effect without changing the level or timing file!`）。**两页本页都没读。**
- [[equation-based-level-setup]] / [[level-setup-tool]] — **equation set 与 spec set 是在那两处建起来的**；本页只访问 `an existing level equation and spec set`。**两页本页都没读。**
- [[flush]] — Example 3 与 4 里的 `FLUSH`；**改动到不到硬件由它决定**。**那页本页没读**，「只到固件层」那句是从它转述的。
- [[spec-search ]] — [[mapping-level]] 给它单独一行（Spec Tool 里做 search 测量），**与本页不是同一件事**；**本页不把它算成 spec 改值。**
- **只写反引号、不写链接的名字**：`CURRENT_SITE_NUMBER()`、`Primary.getLevelSpec()`、`Primary.level(...)`、`FLUSH(TM::APRM)`、`SPECS` / `SPECSET`、`hpt`——**它们都不在 `extract/prose-allowlist.txt` 里**，按 §9.1 一律反引号。（`FLUSH` 有页，但这一篇里写的是带参数的调用，**故与 [[flush]] 分开写**。）

## 版本

本文档**有** `## Functional changes` 段，两条：

- `Introduced before SmarTest 6.3.2`
- `SmarTest 7.1.1: Change function for a specific pin / pin list added`

**第一条是哨兵值，不是「6.3.2 的变更」**（`schema.md` §11.2②）：`Introduced before` 的意思是「**在本文档集覆盖范围开始之前就已经有了**」——**照字面读会生成一条「6.3.2 新增了 LEVEL_SPEC」，那是错的。**

**第二条正对「语法 / 参数」节里的第二个重载**：

| 版本 | 原文条目 | 落在本页哪一处 |
|---|---|---|
| **7.1.1** | `Change function for a specific pin / pin list added` | **`void change(const STRING& spec, DOUBLE value, const STRING& pin);` 这个三参数重载是 7.1.1 才有的**——**7.1.1 之前 `change()` 只能改全体** |
| 7.1.1 | 同上 | **也正好对上那条 `Note The value for the specified pin is only stored for one flush cycle.`**——**per-pin 的改动与那个寿命限制是同一版进来的**（**推断**，依据是两处说的都是「给单个 pin 改值」这一件事） |

**同批条目也收在 `wiki/versions/` 的 [[smartest-7.1.1]] 页里**——**那页不是本页建的**，这里只指路。

## 出处

- 定义文档（本页 `sources:` 唯一一篇，**整篇读过**）：
  `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.124_LEVEL_SPEC.md`
  （TDC `29495.htm`，6,625 字节 / 197 行）。
- **本页「语法 / 参数」节的来源就是这一篇自己**（节首没有「取自子主题」后缀），
  节里只有 `## Parameters` 的参数表与五个 `### Example`（外加各例的导语，**围栏块 8 个**）——
  **构造函数、`## Member functions`、三条 `Note` / `CAUTION` 都不在里面**
  （脚本按段标记收，本篇的段标记是 `## Examples`），**本页在正文里逐条补写了它们**。
  （**2026-09-20 更正**：原写「那 1,324 字符只是 Example 1–5 那五个代码块」——
  字符数与块数都不对，实测 **2,055 字符 / 8 个围栏块**；由 reviewer 查出。）

### 本页读的图：**0 张，因为这一篇一张图都没有**

**实测该篇对 `raw/` 的图片引用 0 处**（`grep -o 'raw/[0-9]*\.\(png\|jpg\)'` 零命中）。
**这不是「图够不着」，是这一篇本来就不带图**——所以本页**没有任何来自图的结论**，
也没有任何一处需要标「④ 图证」。

**另有一件要分清的事**：[[mapping-level]] 读过 3 张图（那是它 `sources:` 里
`02.08.04.14*` / `02.08.04.30*` 那批文档的图），**那 3 张图不属本页的 `sources:`，本页一张没开**。
它自己的结论是「三张图没有填掉任何一个 `?`，也没有把任何一格（推断）升成文档事实」——
**本页引它这一句，没有自己去开图。**

### 本页没做的

- **`Related information` 三篇只算指了路，一篇没读**：`PRIMARY_STATUS - (Primary)`（`02.07.04.01.167`，
  wiki 里已有页）、`Changing spec value in primary level spec set`（`02.07.03.03.02.02`，**用例页**）、
  `TIMING_SPEC`（`02.07.04.01.249`）。**所以 `Primary.getLevelSpec()` / `Primary.level(...)` 的签名本页一个字没有。**
- **`SVLR` 那篇没读**——本页只知道原文那句「debug 时可以敲 `SVLR`」，
  **固件那一侧的参数、查询形式、`PRM` / `ALL` 怎么用，本页一个字没有**（**那一侧在 [[svlr]]**）。
- **`FLUSH` 那篇没读**——Example 3 / 4 里为什么必须 `FLUSH`，本页是从 [[flush]] 转述的，
  **不是本页的出处**。
- **头文件 `/opt/hp93000/soc/prod_com/include/MAPI/LevelSpec.h` 没法核对**（它不是语料里的文件）——
  **本页只有原文给的那五个成员函数与一个构造函数**，**没有更多**。
- **`## Member functions` 那五节各自的 `Parameter` 小表本页只抄了签名**——
  `value` 那一格原文写着 `The value must be within the range that is specified in the spec set.`，
  **「超范围会怎样」原文没写**（**语料未写**）。
- **没有实跑。** 没有写过调 `LEVEL_SPEC` 的 test method、没有在机台上改过任何一个 spec 值、
  没有验证过 per-pin 的改动是不是真的只活一个 flush 周期。**`verified: doc-only` 指的就是这件事。**
- **没有跑 `verify_stages.py`**（按开工简报的要求，避免与别的批次抢同一个报告文件）。
- **没有动 `wiki/index.md`**，也没有把本页挂进 [[level]] 那页。

### ⚠️ 语料瑕疵（照实记，一处都没替它改）

**① 本篇与 [[svlr]] 那篇的同一段有一处空白不同：本篇是 `itself. Note`，那篇是 `itself.Note`。**
正文那一大段 CAUTION 与紧跟着的 `Note` 在**本篇** raw 里是分开的：

> 「If you want to change spec values permanently you must do so in the corresponding setup file itself. Note」

**`itself.` 与 `Note` 之间有空格。**（**缺那个空格的是 [[svlr]] 那篇的出处文档**——
见 [[svlr]] 的「出处」⚠️③。两篇是同源文本，**两篇那段 CAUTION 的文字只有这一处不同**
（另有一处不同是 raw 链接的相对路径，属目录深度，不算文字）；
`SVLR` 那一份里 `Note` 直接粘在 `itself.` 后面。**本页照本篇 raw 引，那个空格没有丢。**）

**② 一处语法不通：`in per statement`。**

> 「Only one member function can be specified in per statement.」

**`in per statement` 读不通**（该是 `per statement` 或 `in one statement`）。
**本页正文引了这一句，没有替它改。**

**③ 两处 `-2.1 V` 不是合法 C++。** Example 2 的两段写法里，值都写成 `-2.1 V`：

> 「Primary.getLevelSpec().change("v_low", -2.1 V);」

**数值后面直接跟一个单位 `V`**，这在 C++ 里不成立。**原文两处都这么写**，
**本页照原样引，一处没替它改**——**也没有在正文里把它「修」成 `-2.1`。**

**④ Example 5 的第二种写法与 `## Usage of the API` 的两步写法不一致。**
`## Usage of the API` 说的是「先定义对象、再用成员函数」，
而 Example 5 的第二段直接写 `double vLow = LEVEL_SPEC(1, 2).getSpecValue("v_low");`
（**构造一个临时对象**）。
**两种写法并存，本页在「典型用法」里并列，没有替语料选一个。**

**⑤ 构造函数的参数表被下一节的小标题吃掉了一格。** raw 里那张表最后一行是

```
 | specset  | Spec set number.  |   Member functions
```

**`Member functions` 这个节标题粘在表格的最后一个单元格里**——
**所以那张表在 md 里读不出「表在哪结束」**。本页在正文里把 `eqnset` / `specset` 两格单独写出，
**没有把那三个词当成一格。**

**⑥ 本页这一篇没有编码坏字（§11.2① 那一族）**：用 `[一-鿿]` 实测零命中；
**也没有 §11.2⑤ 那个整词替换**（`DC/DC power units` 实测 0 命中）。
**这不是「没找到」，是查过、结果为零。**
**本页正文里出现的 C++ 标识符**（`LEVEL_SPEC` / `getEquation` / `getSpec` / `getSpecValue` /
`change` / `restore` / `Primary.getLevelSpec` / `FLUSH` / `TM::APRM`）**全部来自这一篇的正文，
没有一处是从图里抄的**——§11.2⑤ 提醒的那类「坏标识符」在本篇不存在。

`verified: doc-only`
