---
type: object
title: LIMIT
layer: L2
stage: testmethod
tags: [testmethod, l2, api, limit, comparison-operator, data-logging, unit-scaling, pass-fail]
related: [test, testset, tmlimits, on-first-invocation-begin, for-each-site-begin, dc-test-programming, mapping-testmethod]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.126_LIMIT.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# LIMIT

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,028 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.126_LIMIT.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example 1

```
double low_limit, high_limit, thd_result;

TEST("Aout", "THD", LIMIT(TM::GT, low_limit, TM::LT, high_limit), thd_result);
```

The TEST() API judges the test result thd_result with the limit values specified by the LIMIT() API. Within the TEST() API notation, you can use the LIMIT() API to define the limit values for the judgment.

### Example 2

```
double thd_result;

TEST("Aout", "THD", TM::Pass, thd_result);
```

The TEST() API judges the test result thd_result and always returns a pass result because TM::Pass is described as the parameter.

### Example 3

```
double low_limit, high_limit, thd_result;
LIMIT lmt_obj;

lmt_obj.low(TM::GT, low_limit);
lmt_obj.high(TM::LT, high_limit);
lmt_obj.unit("dB");

TEST("Aout", "THD", lmt_obj, thd_result);
```

The LIMIT() API's class object lmt_obj is created. The member functions low() and high() of the LIMIT() API set the low and high limit values to that object. The member function unit() sets the unit of low_limit and high_limit to "dB". Then, TEST() API uses these limit values to judge the test.

<!-- 语法节 end -->

## 是什么

**LIMIT 是一个「限值容器」：它只装两样东西——上下限、以及两侧各自的比较算子。** 原文三句就把职责划完了：

> 「The LIMIT class accesses a data container holding the information on the lower limit, upper limit, and comparison operators.」

> 「The member functions of the LIMIT API manipulate the low or high limit value and comparison operators in the class object.」

> 「You can create a class object that represents the limit range by using the constructor function of this API.」

**它的唯一去处是当 [[test]] 的参数**：

> 「The LIMIT object can be used for judging the test result as pass or fail. That is to say, the object is used as a parameter of the TEST API for specifying the limit range.」

**和 [[test]] / [[get-functional-result]] 一样，它也有一个不许用的地方**：

> 「The LIMIT API cannot be used within a ON_FIRST_INVOCATION block, not even inside an FOR_EACH_SITE block.」

**定义在哪个头文件**：

> 「This API is defined in the header file /opt/hp93000/soc/prod_com/include/MAPI/Limit.h.」

### 两个构造函数：一个空的、一个装满的

| 构造函数 | 造出来的是什么 |
|---|---|
| `LIMIT()` | 「The default constructor LIMIT() creates an empty class object of the LIMIT API.」 |
| `LIMIT(TM::COMPARE opl, DOUBLE low, TM::COMPARE oph, DOUBLE high)` | 「This constructor creates the class object that contains the specified limit values and comparison operators.」 |

**空的怎么用**：先建空对象，再用 `low()` / `high()` 逐个填（见 Example 3）。
**装满的那个**：四个参数是「下限算子、下限值、上限算子、上限值」——**顺序就是签名里的顺序**（文档没有给这个构造函数的参数表，只把它甩给 `low()` / `high()` 的说明，原文：`For the parameter, see the description of member functions low() and high().`）。

### 比较算子 `TM::COMPARE`：五个，而且**两侧各只能用一半**

原文列全了五个（逐字）：

- `LT: Less than the limit value`
- `LE: Less than or equal to the limit value`
- `GT: Greater than the limit value`
- `GE: Greater than or equal to the limit value`
- `NA: No compare`

**但真能用的只有一部分**——这是这一页最容易用错的地方：

| 写在哪一侧 | 允许的算子（原文） | 不许用的 |
|---|---|---|
| `low()`（下限） | 「GT: Greater than the limit value,」「GE: Greater than or equal to the limit value), and」「NA: No compare.」 | **`LT` / `LE`** |
| `high()`（上限） | 「LT: Less than the limit value,」「LE: Less than or equal to the limit value, and」「NA: No compare.」 | **`GT` / `GE`** |
| `get()` 取出的 `opl` | 「The low limit comparison type. It can be TM::GT, TM::GE, or TM::NA.」 | — |
| `get()` 取出的 `oph` | 「The high limit comparison type. It can be TM::LT, TM::LE, or TM::NA.」 | — |

**`NA` 两侧都合法** = 「这一侧不比较」（单边限值就靠它）。
（`GE` 那一行原文多一个右括号，见「出处」①。本页正文按语义读，**引文里原样留着**。）

### 两个常量对象：不看测量值，直接给结论

> 「The following constant objects of the LIMIT() API can control the test result judgment in the TEST() API regardless of the actual measurement.」

| 常量对象 | 效果（原文） |
|---|---|
| `TM::Pass` | `Always pass` |
| `TM::Fail` | `Always fail` |

**它们也是 LIMIT 的对象**——所以能直接站在 [[test]] 的 `limit` 参数位置上（Example 2 就是这么用的）。

### 六个成员函数，分成「写」与「读」两拨

| 成员函数 | 干什么（原文） |
|---|---|
| `low(TM::COMPARE op, DOUBLE value)` | 「This member function sets the comparison operator and lower limit value of the class object.」 |
| `high(TM::COMPARE op, DOUBLE value)` | 「This member function sets the comparison operator and upper limit value of the class object.」 |
| `unit(const STRING& unit)` | 设单位（**只影响数据日志，见下**） |
| `get(TM::COMPARE &opl, double &low, TM::COMPARE &oph, double &high) const` | 「This member function retrieves the limit values and limit comparison types.」 |
| `getLow(double *) const` | 「This member function retrieves the low limit value and returns the comparison type.」 |
| `getHigh(double *) const` | 「This member function retrieves the high limit value and returns the comparison type.」 |

**读的一拨只有 `get()` 一次拿四个值**；`getLow()` / `getHigh()` **只拿一侧的值，算子靠返回值给**（两个都是 `TM::COMPARE` 返回值 + `double *` 出参）。

### `unit()`：唯一一个**不影响判定**的成员函数

> 「This member function sets the unit for the class object. The unit is used for data logging purposes and will not affect the Pass/Fail result of the test.」

**它只决定「数据日志里的数字按什么单位打印」。** 两种格式：

> 「The format of this parameter can be:」

- `"limit_unit"` —— 只有一个单位，日志里就按它打。
- `"lower_unit;lower_power;upper_unit;upper_power"` —— 用 10 的幂给两侧各配一个单位，**日志会按幂更小的那个统一缩放**。

> 「The unit with smaller value of power will be used in the data logging. The value should be specified like "mV;-3;uV;-6".」

**它会照抄，不校验**：

> 「SmarTest will not check whether the specified lower_unit/upper_unit matches with the lower_power/upper_power. It just copies the string specified for lower_unit or upper_unit as the unit to data log.」

**原文给了一张对照表**（下限 1、上限 5、实测 3）。**注意它不在本页 `## 语法 / 参数` 节里**——脚本这一篇只抽了三段 `### Example`（共 1,028 字符），**`unit()` 那一整节都没有进去**。**下面是本页按原文那张表逐格重排的**（数字与单位照抄原表）：

| 指定的 unit | 日志里打出来的 下限/上限/实测 | 单位 | 谁生效 |
|---|---|---|---|
| 不指定 | 1 / 5 / 3 | （空） | 原值不动 |
| `"V"` | 1 / 5 / 3 | `V` | 只换单位名，不缩放 |
| `"mV;-3;V;0"` | 1000 / 5000 / 3000 | `mV` | `-3` 比 `0` 小 → 取 mV 那一侧 |
| `"uV;-4;V;0"` | 10000 / 50000 / 30000 | `uV` | `-4` 比 `0` 小 → 取 uV 那一侧 |
| `"mV;-3;uV;-6"` | 1000000 / 5000000 / 3000000 | `uV` | `-6` 比 `-3` 小 → 取 uV 那一侧 |

**这张表最值钱的一格是最后一行**：`"mV;-3;uV;-6"` 的单位**不是** `mV`，是 `uV`——**规则是「幂小的那个赢」，不是「先写的那个赢」。**

## 典型用法

**文档没有 `## Procedure` 段**；三个 Example 就是三种用法，顺序是本页按「从简到繁」排的（**排序是本页做的（推断）**）。

**1. 内联构造，直接当第三个参数**（Example 1）——最省事的一档：

> 「The TEST() API judges the test result thd_result with the limit values specified by the LIMIT() API. Within the TEST() API notation, you can use the LIMIT() API to define the limit values for the judgment.」

**2. 要「无条件 pass」时，直接把常量对象放进去**（Example 2）：

> 「The TEST() API judges the test result thd_result and always returns a pass result because TM::Pass is described as the parameter.」

**3. 先建对象、再逐项设置、再传进去**（Example 3）——**要单位、或者要复用同一个限制对象时走这条**：

> 「The LIMIT() API's class object lmt_obj is created. The member functions low() and high() of the LIMIT() API set the low and high limit values to that object. The member function unit() sets the unit of low_limit and high_limit to "dB". Then, TEST() API uses these limit values to judge the test.」

**三种用法的分工记法**：**判据只有 `low()` / `high()` 里的「值 + 算子」**；**`unit()` 在判据之外**（只改日志）；**`TM::Pass` / `TM::Fail` 让判据整个失效**。

**单边限值怎么写（推断）**：**把不要的那一侧写成 `NA`**——依据是上面算子表里 `NA` 两侧都登记为合法值、含义是 `No compare`。**原文没有给单边限值的例子**，这一条是**本页的读法**，不是文档事实。

## 和谁有关

**入边 70 条 / 32 篇（含 1 条 `index.md` 的 toc，以及 8 条本页自己的锚点链接），出边 11 条 / 4 个目标**——取自 `extract/edges.jsonl`（`resolved=true`；**链接证，不是本页 sources 的正文**）。

- [[test]] — **唯一的使用者**：`limit` 参数位上放的就是 LIMIT 对象；两篇**互为出边**（本页链 `TEST` 1 条，TEST 那篇链本页 3 条）。**测试侧那三处 `LIMIT` 的用法，本页的 Example 1/2/3 与它一一对得上。**
- [[tmlimits]] — **隔壁那一族**：TMLimits 那篇链到本页 **4 条**（入边里排第三密），**但本页的 source 里一个字都没有它**——两个族的取舍（什么时候用 LIMIT、什么时候用 TMLimits）**语料未写**。
- [[testset]] — **继任族的用法**：`TESTSET__.judgeAndLog_ParametricTest` 链到本页 2 条（入边），**而本页的 source 里没有 TESTSET 这个名字**——**这条关系只有链接证（第二档）**。
- [[on-first-invocation-begin]] / [[for-each-site-begin ]] — **禁用区**：LIMIT 不许出现在这两个块里（本页 `## Class definition` 前那句 note）。
- `GET_LIMIT_OBJECT`（**清单外**）— **反方向的入口**：那一篇链到本页 **2 条**，说明**除了自己 new 一个 LIMIT，还能从别处取一个现成的限制对象**；**那一篇本页没读**，所以怎么取、从哪取，**这一页一个字都没有**。
- **入边最密的三处**：`02.07.04.01.231.45_SMC_TEST.md`（**6 条**）、`Hidden_data_logging`（`02.07.10.04.09` 与性能手册下 `03.01.05.05` 那篇同名文档各 5 条）、`02.07.04.01.160.01_PPMU_PIN_SETTING.md`（3 条）——**都在讲「限值怎么进判定/日志」的别的路径**，本页没有读它们。
- **那一族 DC event 的 `.limits` 成员页（`02.07.04.01.63.*`，清单外）一共 8 篇各链本页 2 条**——**说明「限值」这个对象在事件 API 里也到处都是**（见 [[event-value-int]] 那一族同一个前缀）。
- [[dc-test-programming]] / [[mapping-testmethod]] — 本 wiki 里把本页与判定/日志放在一起的两页：前者是 DC 测试的编程侧，后者那张跨层对照表的「limit 的**值**」那一行 L2 格写的就是本页。
- **GUI 侧：本页的 source 里一个界面名字都没有。** 限值在 GUI 上长什么样、`testname` 怎么对上那张表——**语料未写**；**本页没有去别的文档里找**（本页只写 `sources` 那一篇里有的东西）。

## 版本

**本文档没有 `## Functional changes` 段**（也没有 `## Related information` 段）——**这是这一篇的事实，不是本页的缺口**。所以：

- **LIMIT 是哪个版本引入的、`unit()` 的两种格式是不是一起加的、`get()` / `getLow()` / `getHigh()` 里哪几个是后加的——本页一个字都答不了**，**语料未写**。
- 要查这类问题，只能回到版本页按 `LIMIT` 关键字翻（如 `wiki/versions/smartest-*.md`），**本页没有做这件事**。

## 出处

`sources:` 一篇，**整篇读完**（191 行 / 6,857 字节，**本页五个对象页里最短的一篇**）：

- `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.126_LIMIT.md`
  （TDC topic `29504.htm`，头文件 `MAPI/Limit.h`）

**本页怎么读的这一篇**：`## Class definition`（构造函数 / 算子 / 常量对象 / 成员函数目录）、`## Member functions`（6 个成员函数全文）、`## Examples`（3 个）**——这一篇只有这三节**，本页全部读过；引文没有一句来自本页 sources 之外。

**本页没做的**：

- **没有读 [[test]] 那篇的正文细节**（只在「和谁有关」里用了它的链接）：**「TEST 拿到这个对象之后具体怎么比」本页不写**——那是 [[test]] 的活。
- **没有读 [[tmlimits]]、`GET_LIMIT_OBJECT`、`SMC_TEST`、`Hidden_data_logging`、`PPMU_PIN_SETTING` 那几篇**（入边里最密的几处）。**所以「LIMIT 与 TMLimits 什么时候用哪个」本页没有任何依据**。
- **没有读 GUI 侧任何一篇**（`Tests` 页 / Properties view 之类）：**本页 source 里连一个界面名字都没有**，本页也没有去别处补。
- **没有开过图**：**这一篇的 raw（md 与上游 `raw/29504.htm`）里一张图都没有**——实测 `<img>` 0 个、`.png` 引用 0 个，**所以本页没有任何图证可写**。**不是「图够不着」**（`wiki/schema.md` §11.4 已更正那条错说法），**是这一篇里没有图**。
- **没有实跑**：没写过一行 `LIMIT` 判断，**没有在真实机台上验证过「`unit()` 不改判定」这句话**。`verified: doc-only` 指的就是这件事（§11：文档里有 ≠ 你这台会这样）。
- **没有动 `wiki/index.md`**，也没有把本页挂进 `wiki/stages/testmethod.md`。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：

> ① **冠词用错两处**：`Note The LIMIT API cannot be used within a ON_FIRST_INVOCATION block, not even inside an FOR_EACH_SITE block.`——`a ON_FIRST_INVOCATION` 应为 `an`、`an FOR_EACH_SITE` 应为 `a`（**两个都反了**）。**本页原样引**。

> ② **`GE` 那一行多一个右括号**：`- GE: Greater than or equal to the limit value), and`（`value` 后面那个 `)` 是多余的）。**本页原样引**。

> ③ **成员函数那一段的表被压平，`getHigh()` 的 `Parameter` 表头没了**，而 `getLow()` 那一行的尾部粘着下一个函数名——raw 逐字是 `` | low  | The low limit value.  |  getHigh()``（**`low()` / `unit()` / `get()` / `getLow()` 四处都有 `Parameter`/`Parameters` 表头，只有 `getHigh()` 那一处没有**）。**本页 `语法 / 参数` 节里看不到这个形状**（脚本只抽了三段 `### Example`，成员函数那一整节没有进去），**所以本页正文是按语义把 `getHigh()` 读成一个独立成员函数的（推断）**——**判据是上面引的那一段 raw 原行。**

> ④ **构造函数那一段没有参数表**：`LIMIT(TM::COMPARE opl, DOUBLE low, TM::COMPARE oph, DOUBLE high);` 的四个参数**原文只写了「看 low() 和 high() 的说明」**，**没有自己的参数表**——**所以「四个参数的顺序」本页是照签名读的（推断），不是文档明说的。**

> ⑤ **`TM::Pass` / `TM::Fail` 的取值在代码里怎么用，原文只给了 Example 2 一处**（`TEST("Aout", "THD", TM::Pass, thd_result);`）；**`Always pass` / `Always fail` 是常量对象表里的原文释义**（原表那两格就是这四个词，没有句子）。**本页照实并列，不替它编句子。**

**本页三类话的边界**（§11 的三分）：`文档事实` = 所有 `> 「…」` 引文，以及表里标了「原文」的格；`推断` = 正文里每一处标了（推断）的句子（含「单边限值写 `NA`」「四个参数的顺序」「按语义把 `getHigh()` 读成独立成员函数」三处，**除这些以外本页没有别的主张**）；`建议` = **本页一句都没有**。

`verified: doc-only`
