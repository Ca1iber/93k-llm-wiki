---
type: object
title: EVENT_VALUE_INT
layer: L2
stage: testmethod
tags: [testmethod, l2, api, events, level-equation, type-safety, spec, expression]
related: [event-base, vec-events, level, level-spec, level-equation-file, equation-based-level-setup, spec-variable, spec-value, primary-status, mapping-testmethod]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.19_EVENT_VALUE_INT.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# EVENT_VALUE_INT

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **157 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.19_EVENT_VALUE_INT.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example

Defines a fixed double value:

```
EVENT_VALUE_INT fixedValue(1);
```

Defines an equation variable reference:

```
EVENT_VALUE_INT eqnValue("LEV:frc1");
```

<!-- 语法节 end -->

## 是什么

**`EVENT_VALUE_INT` 是一个「值的来源」的包装类——它装的不是值，是「这个值到时候从哪儿来」。** 这是这一页最要紧的一句，原文把它写成两句话：

> 「The EVENT_VALUE_INT helper class encapsulates the different handling of values, which may either be a fixed value, a spec, or an equation name.」

> 「The class is not intended to retrieve the actual values from the equation system. It specifies the value source from where the final value will be retrieved at execution time.」

**所以它的三个成员函数都不去解方程**——`getValue()` 在表达式上返回的是 `0`（见下）。**它的用途是在编译期把一个设定项写成「固定值 / 表达式」二选一，真正的取值推迟到执行时。**

**表达式那一侧的取值来自 level 方程组，前缀是 `LEV:`**：

> 「All events support specs and equation variables defined in a level equation set. These variables can be addressed by the LEV: prefix (see example below), which refers to the current level equation set by the primaries.」

**定义在哪个头文件**：

> 「This API is defined in the header file /opt/hp93000/soc/prod_com/include/MAPI/Events.h.」

### 为什么要分成 INT / DOUBLE 两个类

> 「See also the second value class EVENT_VALUE_DOUBLE. The separation into two value classes enforces type safety at compile time.」

**即：`INT` 与 `DOUBLE` 分成两个类，是为了让类型错误在编译期就报出来**——**这是文档给的唯一理由**（`在编译期` 这几个字就是原文 `at compile time`）。

### 四个构造函数、三个成员函数、六个运算符

| 类别 | 成员（**raw 的 `## Class definition` 里逐字列出；本页 `## 语法 / 参数` 节只收了 `### Example` 那一段，不含这些**） |
|---|---|
| **构造函数** | `EVENT_VALUE_INT(const INT value)` / `(const STRING & expression)` / `(const CHAR * expression)` / `EVENT_VALUE_INT()` |
| **成员函数** | `bool isExpression() const` / `const STRING & getExpression() const` / `INT getValue() const` |
| **运算符** | 赋值四种（拷贝、`INT`、`STRING`、`CHAR *`）；比较两种（`==`、`!=`） |

**构造函数的两个参数**（原文参数表）：

> 「A fixed number the object will represent.」

> 「The expression can be a spec or an equation variable.」

**运算符那一栏有两组，读法不一样**：

- **四个赋值运算符**（`=` 接 `EVENT_VALUE_INT` / `INT` / `STRING` / `CHAR *`）——**说明这个对象建好之后还能整个换掉来源**（固定值可以改成表达式，反之亦然）。**原文没有给赋值后再 `isExpression()` 的例子**，这是本页从运算符表读出来的**（推断）**。
- **两个比较运算符只有 `==` 与 `!=`**——**运算符表里没有任何大小比较**（`<` / `>` / `<=` / `>=` 一个都没有）。**为什么只判等、不判大小，文档没写（语料未写）**；**本页不替它猜**。

**它是「helper class」**——原文用的就是这个词（`The EVENT_VALUE_INT helper class ...`），**而这一族真正的执行体是事件（event），不是它**：它只在事件的设置/读值接口上当参数类型出现（见「和谁有关」）。

### 三个成员函数：一个问「是哪一路」，两个各取一路

| 成员函数 | 语义（原文） | 另一半的表现 |
|---|---|---|
| `isExpression()` | 「This member function returns whether the object represents an expression (TRUE) or a fixed value (FALSE).」 | — |
| `getExpression()` | 「This member function returns the expression.」 | **「If the object represents a fixed value the expression string will be empty.」** |
| `getValue()` | 「This member function returns the value.」 | **「If the object represents an expression, the returned value is 0. The expression is not resolved here!」** |

**这三行合起来是一条陷阱说明**：**两条路各自有一个「空值」**——固定值对象的 `getExpression()` 返回空串，表达式对象的 `getValue()` 返回 `0`。**所以「取到 0 / 取到空串」不等于「值就是 0 / 表达式是空的」**，要先用 `isExpression()` 分流。**那三个字是原文自带的感叹号：`The expression is not resolved here!`**

## 典型用法

**文档没有 `## Procedure` / `## Usage` 段**，只有一个 `## Example`（两行代码）。用法就这两种：

**1. 要固定值**：

> 「Defines a fixed double value:」

对应代码是 `EVENT_VALUE_INT fixedValue(1);`（**注意说明文字说 `double`，而类是 INT——见「出处」③**）。

**2. 要引用 level 方程组里的变量**：

> 「Defines an equation variable reference:」

对应代码是 `EVENT_VALUE_INT eqnValue("LEV:frc1");`——**`LEV:` 前缀指的就是上面那句里的 current level equation set**。

**读完值之前先分流（推断）**：按三个成员函数的语义，**取值的顺序应当是 `isExpression()` → 是表达式就 `getExpression()`、不是就 `getValue()`**。**原文没有给这样的例子**（Example 只有构造两行，一次都没有调这三个成员函数），**所以这一步是本页按成员函数的语义排的（推断），不是文档里抄来的流程。**

**它在这一族里的位置**：这个类**不自己出现在测试代码的执行段**，而是**被事件对象的设置/读值方法当参数类型用**——见「和谁有关」里那 46 条入边。

## 和谁有关

**入边 46 条 / 35 篇（含 1 条 `index.md` 的 toc），出边 2 条 / 1 个目标**——取自 `extract/edges.jsonl`（`resolved=true`；**链接证，不是本页 sources 的正文**）。

- `EVENT_VALUE_DOUBLE`（**清单外**）——**唯一的出边目标（2 条），也是入边里最密的一个（同一族里它被链 91 次）**。本页 source 里那句 `See also the second value class EVENT_VALUE_DOUBLE.` 就是这条边的出处；raw 路径：`02.07.04.01.63.18_EVENT_VALUE_DOUBLE.md`。**「两个类怎么选」本页没有答案**（**那一篇本页没读**）。
- [[event-base]] — **同一族的基类**：族索引 `02.07.04.01.63_EVENT_...__DC_events_API_reference.md` 一把链出四个名字（`EVENT_BASE`、`EVENT_VALUE_DOUBLE`、`EVENT_VALUE_INT`、`VEC_EVENTS`）——**本页与 [[event-base]] 是并列关系，不是继承关系**（**继承关系那一句在 EVENT_BASE 那篇里，本页没读**）。
- [[vec-events]]— 同一条族索引链里的第四个名字。
- **本页入边的绝对主力是那一族的 `averages` / `getAverages` 成员页**（`02.07.04.01.63.*`，例子：`EVENT_CFIM.getAverages.md`、`EVENT_CFIM.averages.md`、`EVENT_WAVEFORM_VCVM.getAverages.md` 等，**全部清单外**）——**说明这个类最常出现在「平均值的设定或读取」这条路径上**（**这一条只有链接证的份量；本页没有读那一族任何一篇**）。
- [[level]] / [[level-spec]] / [[level-equation-file]]/ [[equation-based-level-setup]] — **`LEV:` 前缀指过去的那套东西**：`level equation set`、`spec`、`equation variable` 三个词在本页 source 里都有，**解释都在那些页里**（**本页一篇都没读**）。
- [[spec-variable]] / [[spec-value]] — **参数表里那个 `spec`**：原文说表达式「可以是 spec 或 equation variable」，**而 spec 是什么本页不知道**（**那两页没读**）。
- [[primary-status]] — **`the primaries` 这个词**：原文说 `LEV:` 指「当前由 primaries 设定的 level equation set」，**而 `primaries` 在本页 source 里没有再解释**；与它同名的那一页是 L2 的 `PRIMARY` 族——**这条关联只凭名字，是本页的推断（推断），不是文档说的。**
- [[mapping-testmethod]] — 本阶段的跨层对照表：**它没有把本页排进任何一行**（本页是事件侧的取值包装，不在 GUI↔L2↔L1 的那条主链上）。
- **本页之外**：这一族同前缀的对象页在本 wiki 里目前只有 `event-base` 与 `event-value-double` 两页（其余同名页清单里没有），**所以上面那一大票 `02.07.04.01.63.*` 的名字本页一律用反引号写**。

## 版本

`## Functional changes` 段**一条**（逐字）：

- `Introduced in SmarTest 6.5.2`

**注意它写的是 `Introduced in`，不是 `Introduced before`**——**这是一个真的引入版本，不是哨兵值**（对照：本篇所属的那一族里 `Introduced before SmarTest 6.3.2` 那种写法才是哨兵，见 `wiki/schema.md` §11.2②）。**所以：`EVENT_VALUE_INT` 在 SmarTest 6.5.2 之前的版本上不存在。**

## 出处

`sources:` 一篇，**整篇读完**（126 行 / 2,895 字节，**本页五个对象页里最短的一篇**）：

- `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.19_EVENT_VALUE_INT.md`
  （TDC topic `116912.htm`，头文件 `MAPI/Events.h`）

**本页怎么读的这一篇**：`## Class definition`（构造函数 / 成员函数目录 / 运算符）、`## Member functions`（三个成员函数全文）、`## Example`（两行）、`## Related information`（1 个目标）、`## Functional changes`（1 条）**全部读过**；引文没有一句来自本页 sources 之外。

**本页没做的**：

- **没有读 `EVENT_VALUE_DOUBLE` / `EVENT_BASE`**——**「为什么有时该用 INT、有时该用 DOUBLE」本页不能答**（source 只说了「分开是为了编译期类型安全」这一句理由）。
- **没有读那一族任何一篇事件页**（`EVENT_CFIM` / `EVENT_CFVM` / `EVENT_WAVEFORM_*` 等）：**「`getAverages()` 收到这个对象之后怎么用」本页一个字都没有**——那 46 条入边只说明「它们链过来了」。
- **没有读 [[level]] / [[level-spec]] / [[spec-variable]] / [[spec-value]] / [[equation-based-level-setup]] 任何一篇**：**`LEV:` 前缀到底是哪一套方程、`spec` 与 `equation variable` 有什么区别，本页都答不了**——本页只有 source 里那一句定义。
- **没有开过图**：**这一篇的 raw（md 与上游 `raw/116912.htm`）里一张图都没有**——实测 `<img>` 0 个、`.png` 引用 0 个，**所以本页没有任何图证可写**。**不是「图够不着」**（`wiki/schema.md` §11.4 已更正那条错说法），**是这一篇里没有图**。
- **没有实跑**：**没有在真实机台上验证过「表达式对象的 `getValue()` 真的返回 0」**、也没有写过一次 `LEV:` 引用。`verified: doc-only` 指的就是这件事。
- **没有动 `wiki/index.md`**，也没有把本页挂进 `wiki/stages/testmethod.md`。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：

> ① **`### Constructor` 出现了两次**：一次在 `## Class definition` 底下（第 18 行）、一次在运算符之后（第 48 行），**两次的代码块一模一样**（四个构造函数）。**第二次那个小节自己带着完整正文**（`This constructs an object of the EVENT_VALUE_INT class.` + 参数表），**所以它不是空壳重复，是整节重复**。**本页 `## 语法 / 参数` 节只收 `### Example` 那一段，这个重复没有进本页**——本页在这里照实记下。

> ② **小节标题拼错**：`### getExpresssion()`——**比函数名 `getExpression()` 多一个 `s`**（**紧接着的代码块里写的是正确的 `const STRING & getExpression() const;`**，**同一行标题与代码块自相矛盾**）。**本页原样引，不改标题。**

> ③ **Example 的说明文字写错类型**：`Defines a fixed double value:`——**而这个类是 `EVENT_VALUE_INT`、下一行的代码是 `EVENT_VALUE_INT fixedValue(1);`**。**`double` 是从 DOUBLE 那一篇抄过来的说法**（**本页照原样引；本页的读法：这只是说明文的笔误，`fixedValue(1)` 给的是整数 1**——**语料没有解释，这是本页的推断**）。

> ④ **同一个概念两种标题写法**：`## Class definition` 底下的小节叫 `### Member Functions`（大写 `F`），而正文那一节的段标题是 `## Member functions`（小写 `f`）——**同一篇里两种写法并存**。

> ⑤ **构造函数的参数表在 raw 里是被压平的**（`Parameter | Parameter | Description` 那一串单行成列）——**这个形状在本页 `## 语法 / 参数` 节里看不到**（脚本这一篇只收了 `### Example` 那一段），**本页正文是按语义把它读成一张参数表的**（那是本页的读法）。**这是语料的形状，不是脚本切错**（§4）。

**本页三类话的边界**（§11 的三分）：`文档事实` = 所有 `> 「…」` 引文，以及标了「原文」的说法；`推断` = 正文里每一处标了（推断）的句子（含「先 `isExpression()` 再分流」「赋值运算符说明来源可以整体换掉」「③ 那条是从 DOUBLE 抄过来的笔误」三处，**除这些以外本页没有别的主张**）；`建议` = **本页一句都没有**。

`verified: doc-only`
