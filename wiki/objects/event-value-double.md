---
type: object
title: EVENT_VALUE_DOUBLE
layer: L2
stage: testmethod
tags: [testmethod, dc-events, event-value, value-source, level-equation, type-safety]
related: [event-waveform-vfim, event-waveform-vfvm]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.18_EVENT_VALUE_DOUBLE.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# EVENT_VALUE_DOUBLE

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **164 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.18_EVENT_VALUE_DOUBLE.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example

Define a fixed double value:

```
EVENT_VALUE_DOUBLE fixedValue(1.3);
```

Defines an equation variable reference:

```
EVENT_VALUE_DOUBLE eqnValue("LEV:frc1");
```

<!-- 语法节 end -->

## 是什么

**`EVENT_VALUE_DOUBLE` 是个「值来源」的封装，不是取值器。** 原文头两句把这件事说尽了：

> The EVENT_VALUE_DOUBLE helper class encapsulates the different handling of values, which may either be a fixed value, a spec, or an equation name. The class is not intended to retrieve the actual values from the equation system. It specifies the value source from where the final value will be retrieved at execution time.

**三种来源**：**固定值**、**spec**、**方程名**。**对象里存的只是「这个值从哪儿来」**——真正的取值发生在**执行时**，不在你造对象的时候。

头文件 `/opt/hp93000/soc/prod_com/include/MAPI/Events.h`。

### `LEV:` 前缀指的是「当前 level 方程集」

> All events support specs and equation variables defined in a level equation set. These variables can be addressed by the LEV: prefix (see example below), which refers to the current level equation set by the primaries.

**三个词本篇没有解释**：`spec`、`equation variable`、`primaries`。所以「`LEV:` 后面能写什么名字」「primaries 是哪个设置决定的」，**本页答不了**——本篇只写了这一句。

### 为什么有两个值类

> See also the second event value class EVENT_VALUE_INT. The separation into two value classes enforces type safety at compile time.

**这是原文自己给的理由**：拆成两个类，是为了**编译期**就把 int / double 用错的地方挡住。对照 `event-value-int`（那一篇本页也读了）：**它的重载只有 `INT` / `STRING` / `CHAR *`，没有 `FLOAT` / `DOUBLE`**——所以窄的那一侧不接收宽的。

### 三个成员函数：`isExpression()` / `getExpression()` / `getValue()`

| 成员函数 | 原文 |
|---|---|
| `bool isExpression() const;` | `This member function returns whether the object represents an expression (TRUE) or a fixed value (FALSE).` |
| `const STRING & getExpression() const;` | `This member function returns the expression. If the object represents a fixed value the expression string will be empty.` |
| `DOUBLE getValue() const;` | `This member function returns the value. If the object represents an expression, the returned value is 0. The expression is not resolved here!` |

**第三行是本页最要紧的一条**：**表达式对象的 `getValue()` 返回 0，而且原文用感叹号强调它不在这里解析**（`The expression is not resolved here!`）。也就是说——**别拿 `getValue()` 去读一个 `LEV:` 引用的实际电平值**，那是另一条路的事，本篇没说那条路是什么。

**默认构造是语料未写的一格**：签名清单里有 `EVENT_VALUE_DOUBLE();`，但参数说明只覆盖 `value` 与 `expression` 两类，**没有一句说默认构造出来的对象算固定值还是表达式**。

### 运算符

- **6 个赋值运算符**（`const EVENT_VALUE_DOUBLE &`、`INT`、`FLOAT`、`DOUBLE`、`const STRING &`、`const CHAR *`）：

> These assignment operators allow to change the objects value. Both, fixed values and expressions are supported.

- **2 个比较运算符**（`==` / `!=`）：

> These compare operators compare two objects for identity.

**⚠️ 原文用的是 `identity` 这个词，没有说是「值相等」。** 两个都装着固定值 `1.3` 的对象算不算 identity，**语料未写**——本页不替它解释。

### 参数语义

| 参数 | 原文 |
|---|---|
| `value` | `A fixed number the object will represent.` |
| `expression` | `The expression can be a spec or an equation variable.` |

## 典型用法

**两种造法**（上面「语法 / 参数」节的两个 Example 就是这两句）：

| 想要什么 | 怎么写 | 事后怎么认 |
|---|---|---|
| **固定值** | `EVENT_VALUE_DOUBLE fixedValue(1.3);` | `isExpression()` 返回 FALSE，`getExpression()` 是空串 |
| **方程引用** | `EVENT_VALUE_DOUBLE eqnValue("LEV:frc1");` | `isExpression()` 返回 TRUE，`getExpression()` 是 `"LEV:frc1"` |

**用法上的四条**：

1. **要传值的地方直接传**——它是个 helper class，本来就是给别的 API 当参数用的（谁用它见下一节）。
2. **改值用 `operator =`**：6 个重载覆盖了 `EVENT_VALUE_DOUBLE` / `INT` / `FLOAT` / `DOUBLE` / `STRING` / `CHAR *`，**固定值和表达式都能换**。
3. **想读回「你当初写了什么表达式」→ `getExpression()`**；想读回固定值 → `getValue()`。
4. **不要用 `getValue()` 去求 `LEV:` 的值**——表达式对象上它固定返回 0，而且原文明确说「这里不解析」。

**本页答不了的一步**：**怎么把表达式解析成实际值**。原文只说「at execution time 去取」，**没有给那一步的 API**；本页 sources 之外的东西不写。

## 和谁有关

**入边 90 条 / 67 篇**（`edges.jsonl`，`inline` 口径；**自指 0 条**）。**几乎全部来自同一族**：`02.07.04.01.63.*`（DC events API reference）里那些**接受它当参数的成员函数页**。按函数名分组：

| 链到本页的成员函数（入边来源） | 链到 `event-value-int` 的成员函数 |
|---|---|
| `limitLow()` / `limitHigh()` / `getLimitLow()` / `getLimitHigh()` | `averages()` / `getAverages()` |
| `cForce()` / `getCForce()` | |
| `vClampLow()` / `vClampHigh()` / `getVClampLow()` / `getVClampHigh()` | |
| `iClampLow()` / `iClampHigh()` | |
| `setFilterValue()` / `getFilterValue()` | |
| `iRange()` / `getIRange()` | |

**（推断）这个分工是「设量值用 DOUBLE、设次数用 INT」**——依据**只是那些成员函数的名字**（`limit` / `force` / `clamp` / `range` 是量值，`averages` 是平均次数）。**本页没有读那些成员函数的正文**，所以这只是一条按名字排的读数，不是文档说的。

**边数据里还有整篇的事件页链到本页**：`EVENT_CF`、`EVENT_CFIM`、`EVENT_CFVM`、`EVENT_FDM`、`EVENT_FILTER`、`EVENT_IC*`、`EVENT_IM`、`EVENT_RANGE_*`、`EVENT_RDM`、`EVENT_VC*`、`EVENT_VF*`、`EVENT_VM` 等（**一篇没读**）。

- `event-value-int` — **兄弟页**。原文那句 `See also the second event value class EVENT_VALUE_INT.` 就是它。**⚠️ 这个名字不在 `extract/prose-allowlist.txt` 里，所以本页只能写反引号 + 路径，不给链接**（同 `mapping-testmethod` 记 `mapping-pin` 那处的处理）。
- [[event-waveform-vfim]] / [[event-waveform-vfvm]] — 同族里**已经建了页**的两篇：`EVENT_WAVEFORM_VFIM` 与 `EVENT_WAVEFORM_VFVM` 那两篇在 `edges.jsonl` 里链到本页（**本页没有读它们**，关系只有「它们认为读者该来看本页」这一条证据）。
- `EVENT_BASE` — **本页没读，也不能判断它和本页是什么关系**。名字像不代表有继承关系：本页是「值的来源」，不是事件本身。
- **上游是谁用它、下游它喂给谁**：本页 sources 里**没有**一张「谁接收它」的清单——**上面那张函数名表是从 `edges.jsonl` 数出来的，不是文档列的**。

## 版本

原文 `## Functional changes` 只有一条：

- **Introduced in SmarTest 6.5.2**

**没有哨兵值那一族**（本文档没有 `Introduced before …` 这种写法）。**本 wiki 面向 7.10.3**，而这张表停在 `6.5.2`——**7.10.3 上有没有加过别的重载，本篇没有记**。

## 出处

`sources:` 一篇：`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.18_EVENT_VALUE_DOUBLE.md`（TDC `116913.htm`，4,083 字节，140 行）。**整篇读完。**

**本页做了什么**

把这篇 4 KB 的短文档里**能用的那几件事**讲清了：值来源 vs 值的区别、`LEV:` 前缀、两个值类分开的理由、三个成员函数各自返回什么（尤其 `getValue()` 对表达式返回 0 这一条）、六加二共八个运算符、「谁在用本页」是从 `edges.jsonl` 数出来的分组表。

**本页没做的**

- **`## Related information` 指的 `EVENT_VALUE_INT` 那篇**——本页为它**另建了一页**（`wiki/objects/event-value-int.md`，同一批），两页都读了各自的 sources。**但「两个值类怎么配合」这件事两篇都没写**，所以两页都没有编。
- **事件族一篇没读**：`EVENT_CF`、`EVENT_CFIM`、`EVENT_CFVM`、`EVENT_FDM`、`EVENT_FILTER`、`EVENT_IC*`、`EVENT_IM`、`EVENT_RANGE_*`、`EVENT_RDM`、`EVENT_VC*`、`EVENT_VF*`、`EVENT_VM`、`EVENT_WAVEFORM_*`（**90 条入边就是从它们来的**）。所以**「到底哪个 API 收 `EVENT_VALUE_DOUBLE`、传进去之后它怎么被用」本页只有名字级的证据**。
- **`spec` / `equation variable` / `primaries` 三个词的定义本页没有**——它们不在这篇里，本页没去别处找。
- **没有实跑。** 没有编译过、没有在任何 93K 环境上跑过。`verified: doc-only`。
- **没有动 `wiki/index.md`**，也没有动别的页。

**图（§11.4）**

**本页 sources 那一篇里没有图。** 判据（可核）：转出来的 `.md` 里 `png` / `jpg` / 图片标记命中 **0**；**上游 `tdc-html/raw/116913.htm` 里 `<img` 命中 0**。所以本页**没有任何 ④ 图证——不是「图够不着」，是这篇文档本来就不带图。**

**编码与整词替换（照实记，一处都没替它改）**

- **汉字坏字 0 处**（`[一-鿿]` 命中 0）。
- **`DC/DC power units`（`Index` 被整词替换那一族）命中 0 处**——本页的标识符可以照抄。

**⚠️ 语料瑕疵（照实记，一处都没替它改）**

- **① `### Constructor` 出现了两次**：一次在 `## Class definition` 底下（只有签名），一次在 `## Member functions` 之前（带说明）。**同名小节重复**，脚本小节和正文都能看到这两处。
- **② 参数表的表头写坏了**：原文是 ` | Parameter  | Description |`，**首尾各多一个管道符**，转成 markdown 后这一行只剩两条空边框（表格因此在「语法 / 参数」节里被拆成两段）。
- **③ 参数表的两格是跨行的**：`value` 与 `expression` 的说明各被拆到单独的行上，中间夹着孤立的 ` |`。
- **④ 例句用了 `Define`**（`Define a fixed double value:`）；**兄弟篇 `event-value-int` 的同一句写 `Defines`**——同一族两种动词形式（那一处记在它的页上）。
- **⑤ 少一个撇号**：`These assignment operators allow to change the objects value.`——**`objects` 应为 `object's`**。本页正文照原样引了。
- **⑥ 两篇结构不对称**：本页有独立的 `## Operators` 一节，`event-value-int` 那篇的运算符只作为 `### Operators` 挂在 `## Class definition` 下。
- **⑦ 默认构造没有说明**：签名清单里有 `EVENT_VALUE_DOUBLE();`，参数表里却没有它——**这是语料缺的一格**，本页在正文里标了「语料未写」。

`verified: doc-only`
