---
type: object
title: SpecVariable
layer: L2
stage: level
tags: [spec-variable, utm, parameter-type, unit, level, timing, testmethod, l2]
related: [spec-value, how-to-create-a-universal-test-method-class, mapping-testmethod, level-file, timing-file, spec-search, universal-test-method-library, spec-set, spec-tool, level-spec, timing-spec, svlr, pin-string, file-string, option-list, context-pins, smartest-6.5.0, level, timing, testmethod]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.02.13.04_SpecVariable.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# SpecVariable

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **2,014 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.02.13.04_SpecVariable.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example

The following example shows how to define a SpecVariable parameter and how to use it in the test method. Some functions used in the run() function are defined in the file SpecSearchUtil.hpp. This example is intercepted from SpecSearch test in the AC test method library.

```
//for testmethod framework interfaces
#include "testmethod.hpp"
//for testmethod API interfaces
#include "mapi.hpp"

#include "SpecSearchUtil.hpp"
class SpecSearch: public testmethod::TestMethod
{
protected:
  testmethod::SpecVariable spec;
  ...

protected:
  /**
   *Initialize the parameter interface to the testflow.
   *This method is called just once after a testsuite is created.
   */
  virtual void initialize()
  {
    addParameter("spec",
                 "SpecVariable",
                 &spec)
    .setComment("this parameter's format like:\n"
                "LEV.1.fooSpec[mV]\n"
                "type is LEV, equationSetId is 1\n"
                "name is fooSpec, unit is mV");
    ...
  }

  /**
   *This test is invoked per site.
   */
  virtual void run()
  {
    static SpecSearchUtil::SpecSearchUtilParam param;

    SpecSearchUtil::SpecSearchUtilResult result;

    /*----------------------------
     * 1. prepare for test
     *----------------------------
     */
    ON_FIRST_INVOCATION_BEGIN();
      /*process all parameters needed in test*/
      SpecSearchUtil::processParameters(spec.mName,
                                        spec.mType,
                                        setupPinlist,
                                        spec.mUnit,
                                        method,
                                        min,
                                        max,
                                        step,
                                        resolution,
                                        resultPinlist,
                                        param);
    ON_FIRST_INVOCATION_END();
    ...

    return ;
  }
};

REGISTER_TESTMETHOD("AcTest.SpecSearch", SpecSearch);
```

<!-- 语法节 end -->

## 是什么

**`SpecVariable` 是 UTM 的另一个参数类型：一个「指向 level / timing setup 文件里某个 spec 变量」的引用。**
原文第一句把范围、内容和格式一次说完：

> 「The parameter type SpecVariable is defined to represent the spec variables defined in the level
> and timing setup files in universal test method. It contains the information of spec type,
> equation set number, spec name and unit of the spec variable. Its value is in the format of
> "specType.equationSetNumber.specName[unit]".」

**和 [[spec-value]] 摆在一起，差别一句话**：`SpecValue` 的值就是**写下的那个字面量**；
`SpecVariable` 的值是一条**坐标**——它指到 setup 文件里的某个 spec 变量上去。
**两个类型都是「一个带单位的值」，只是值的来源不同。**

### 五个字段——**可以直接读，不走 getter**

原文列了五个字段（逐字）：

| 字段 | 原文说明 |
|---|---|
| `mFullName` | `The full name of the SpecVariable parameter.` |
| `mType` | `The type of the spec variable.` |
| `mEquationSetId` | `The equation set number the spec variable belongs to.` |
| `mName` | `The spec variable name.` |
| `mUnit` | `The unit of the spec variable.` |

> 「You can call the value of a field with th format "SpecVariable.field". For example the
> parameter name is spec, spec.mUnit calls the unit of the spec variable.」

**即 `spec.mUnit` 这种写法是原文给的用法**——字段是**公有成员**，不是 getter 函数。
（**`th` 应为 `the`，原文如此**，见「出处」⚠️①。）

### 值的格式：三段坐标 + 单位

原文给了两个逐字例子，各自带解释：

| 例子 | 原文的解释 |
|---|---|
| `"LEV.1.fooSpec[mV]"` | `means the spec variable is fooSpec in equation set 1 of level file, with the unit [mV].` |
| `"TIM.3.barSpec@port1[A]"` | `means the spec variable is barSpec in equation set 3 for port port1 of timing file, with unit [A].` |

**两个例子的解释里各自点名了文件**（`of level file` / `of timing file`），
所以「`LEV` 段指 level 文件、`TIM` 段指 timing 文件」**是文档事实**，不是本页推的。
（那两份文件的页见 [[level-file]] / [[timing-file]]。）

**⚠️ 格式串与 TIM 那个例子对不上**：原文给的格式是
`specType.equationSetNumber.specName[unit]`，**`@port` 这一段在格式串里没有**，
而 TIM 的例子带着 `@port1`，解释里也专门写了 `for port port1`。
**两处不能同时完整，本页并列，不替它补格式**（见「出处」⚠️③）。

**`specType` 的取值清单：语料未写。** 原文只出现过 `LEV` 与 `TIM` 两个前缀，
**没有给一张「specType 可以是哪些值」的表**——所以除这两个以外还有没有别的，本页没有依据。

### 三个成员函数（**这一节不在上面的「语法 / 参数」节里**）

**上面的「语法 / 参数」节只收了原文的 `## Example` 一节**（2,014 字符 = 那一份例子）。
**`## Member function` 那一节（572 字符）没有进去**——脚本按段标记收，
而这一篇的段标记是 `Example`（§4：脚本负责抽取，不重写）。
**所以下面这张表是本页从 raw 逐字抄的。**

| 成员函数 | 签名（raw 里每节开头的代码块） | 干什么（原文） |
|---|---|---|
| `parseFullName()` | `void parseFullName();` | `This function parses the input string to fill in the specific field of a SpecVariable parameter, including type, equation set number, spec name and unit.` |
| `Reset()` | `void Reset();` | `This function resets the value of a SpecVariable to empty.` |
| `operator =` | `SpecVariable& operator = (const SpecVariable& rhl)` | `This function sets the value for a SpecVariable parameter by copying from another SpecVariable parameter.` |

> 「There are three member functions defined for SpecVariable. These functions can be used in the
> test method to process and change the SpecVariable parameter.」

**两处要留意的**：

- **`parseFullName()` 填的是四个名字**（`type, equation set number, spec name and unit`），
  **而字段有五个**——`mFullName` 不在那串里，原文也没说它是不是就等于整个输入串
  （**推断**：从 `mFullName` 的定义 `The full name of the SpecVariable parameter.` 看，它应当就是
  那句 `"specType.equationSetNumber.specName[unit]"`；**原文没有这么说，本页不写成结论**）。
- **三个函数里没有一个是「取值」用的**——取字段就直接读成员（见上）。
  **原文用的词是 `process and change`，与 [[spec-value]] 那篇的 `get and set` 不同**
  （**推断**：这个差别反映的是两个类型职责不同，不是笔误；**原文没有对照说明**）。

## 典型用法

**原文没有 `## Procedure`，也没有 `## Before you begin`**——只有一节 `## Example`，导语是：

> 「The following example shows how to define a SpecVariable parameter and how to use it in the
> test method. Some functions used in the run() function are defined in the file SpecSearchUtil.hpp.
> This example is intercepted from SpecSearch test in the AC test method library.」

**「intercepted」这个词要说清**：这一段例子是从 `SpecSearch` 那个 test method 里**截出来的**，
所以下面第 4 步里有一半变量在屏幕上没有声明——**那是截取的结果，不是语料缺字。**

**从例子里能读出的顺序，四步**：

| # | 在哪 | 代码（逐字） |
|---|---|---|
| 1 | 文件头 | `#include "testmethod.hpp"` / `#include "mapi.hpp"` / `#include "SpecSearchUtil.hpp"` |
| 2 | 类定义里 | `testmethod::SpecVariable spec;` |
| 3 | `initialize()` 里 | `addParameter("spec", "SpecVariable", &spec).setComment("this parameter's format like:\n" "LEV.1.fooSpec[mV]\n" "type is LEV, equationSetId is 1\n" "name is fooSpec, unit is mV");` |
| 4 | `run()` 里 | `SpecSearchUtil::processParameters(spec.mName, spec.mType, setupPinlist, spec.mUnit, method, min, max, step, resolution, resultPinlist, param);` |

**第 3 步值得单说**：那条 `.setComment` **把这个参数的格式与含义写进了注册语句本身**
（`this parameter's format like:`、`type is LEV, equationSetId is 1`、`name is fooSpec, unit is mV`）
——**即：这个参数是给人手填的字符串，所以在注册时把格式贴在参数上**。
**原文没有另起一句解释为什么这么做**（**推断**，依据就是那三行注释文字本身）。

**第 4 步值得单说**：`spec` 的**字段当实参**传出去（`spec.mName` / `spec.mType` / `spec.mUnit`），
**没有经过任何转换**——又一次印证「字段就是可读成员」。
**这一句包在 `ON_FIRST_INVOCATION_BEGIN()` / `ON_FIRST_INVOCATION_END()` 里**
（原文注释：`/*---------------------------- * 1. prepare for test *---------------------------- */`）。

**两条例子里看得出来、但原文没写的：**

- **例子从头到尾没有调 `parseFullName()`，也没有调 `Reset()`。** 字段是直接读的。
  **所以「什么时候才需要 `parseFullName()`」原文没有例子**——
  **（推断）**：既然 `addParameter` 注册的是一个字符串、而 `mName` / `mType` / `mUnit` 是分开的字段，
  中间那一步应当就是 `parseFullName()`；**依据只是字段名与函数名对得上，原文没有说这一步在哪。**
- **`SpecSearchUtil.hpp` 与 `processParameters()` 不是框架 API**：原文只说
  `Some functions used in the run() function are defined in the file SpecSearchUtil.hpp`
  ——**它们是那个 test method 自己带的工具文件**，不是 SmarTest 的接口。
  **`setupPinlist` / `method` / `min` / `max` / `step` / `resolution` / `resultPinlist` 七个实参
  在截出来的这段里没有声明**，本页不知道它们是什么。

**下一步**：原文 `## Related information` 只给了 `How to create a universal test method class` 一篇
（见「和谁有关」）；**本篇没有 `## What to do next` 段**。

## 和谁有关

- [[how-to-create-a-universal-test-method-class]] — **本页唯一的上游**。
  本篇 `## Related information` 只有它一条；那页把 `SpecVariable` 列进参数类型清单，
  并给了一句定义（`timing 或 level 文件里定义的 spec variable`）——**本页是那句话的专页**。
  那页的版本表还写着 `SmarTest 6.5.0: New parameter types: PinString, SpecVariable`
  ——**与本篇的 `## Functional changes` 对得上**（见「版本」）。
- [[spec-value]] — **同一批清单里的兄弟类型**。
  两个类型都表示「一个带单位的值」，**差别在值的来源**：
  本页指到 setup 文件里的变量上，`SpecValue` 是写下的字面量。
  **这一句的两半分别来自两篇的出处文档，本页没有把它们合并成一条文档事实。**
- [[level-file]] / [[timing-file]] — **本页的值指向的那两份文件**。
  原文两个例子的解释里明写 `equation set 1 of level file` 与 `equation set 3 for port port1 of timing file`。
  **但这两份文件长什么样、spec 变量在里面怎么声明，本页一个字没有**——那两篇本页都没读。
- [[spec-search]] — **本篇例子的来处**：原文写 `intercepted from SpecSearch test in the AC test method library`。
  **那篇文档本页没读**，所以只知道例子的出处是一个叫 `SpecSearch` 的 test method。
- [[universal-test-method-library]] — **`the AC test method library` 就是它的一支**（**推断**，
  依据是原文那半句 `in the AC test method library` 与那页讲的是同一批库文件；**原文没有写全称**）。
- [[mapping-testmethod]] — **本页在建 test method 那条链上的位置**。
  那张对照表「建 test method 类：模板 / 类名 / 参数」一行的 **L2 格**把
  [[pin-string]] / 本页 / [[spec-value]] / [[file-string]] / [[option-list]] / [[context-pins]]
  并排放在一起——**即：它们是同一批「参数类型」，不是动作**。
- [[spec-set]] / [[spec-tool]] / [[level-spec]] / [[timing-spec]] / [[svlr]] — **同一族「spec」名字，但都不是本页**：
  那几个讲的是 level / timing 侧 spec 变量与 spec set 的容器、GUI 与改值接口。
  **本页的出处文档没有链到它们中的任何一个**，所以这里的「同族」是
  **按名字与 [[mapping-level]] / [[mapping-testmethod]] 的行位**说的（**推断**），不是文档事实。
- [[smartest-6.5.0]] — **版本落点**，见「版本」。
- `addParameter` / `setComment`（**均未建**；raw: `02.07.04.01.03_addParameter.md`）—
  第 3 步注册参数的那两个调用；**那篇本页没读**，签名与返回值本页没有。

## 版本

本文档**有** `## Functional changes` 段，**只有一条**：

- **`Introduced in SmarTest 6.5.0`**

> **这一条不是 §11.2② 的哨兵值。** 哨兵值写的是 `Introduced **before** SmarTest 6.3.2`
> （意思是「**在本语料覆盖范围开始之前就已经有了**」）；本篇写的是 `Introduced in 6.5.0`
> ——**是一个真版本号**。**两句话只差一个词，读法完全相反，这一处最容易误判。**

**旁证（wiki 内部，不在本页 `sources:` 里）**：[[smartest-6.5.0]] 的条目里有一条就是本篇的出处文档
（条目文字与上面那条一致）——**那页不是本页建的，这里只指路。**
同一页另有一条 `addParameter` 的条目写着 `SmarTest 6.5.0: Supports new parameter types:
SpecVariable, PinString`——**即：6.5.0 同时给了类型和注册它的入口**。
**那篇文档本页没读，这一句只在这里指路，不进本页正文当结论。**

**原文没有给 6.5.0 以外的任何变更记录**——所以
「`parseFullName()` / `Reset()` 的语义改过没有」本页没有依据。

## 出处

`sources:` 一篇：`02_System_reference/02.07_Test_Method_Reference/02.07.02.13.04_SpecVariable.md`
（TDC `115042.htm`，4,550 字节 / 145 行）——**整篇读完**。

**「语法 / 参数」节只收了原文的 `## Example` 一节**（2,014 字符）。
**`## Member function`（572 字符）整节在上表中由本页逐条写出**——
**所以上面那张签名表不在脚本辖区里，不是「改语法节」。**

**本页没做的**：

- **只读了这一篇的正文。** 正文里每一个文档事实都出自这 145 行。
- **一处例外，要明确交代**：为做 §10 的**第 0 步（先查是不是同一篇被投放了两次）**，
  本页比对过版本页条目里出现的另一条路径
  `02_System_reference/02.07_Test_Method_Reference/02.07.04.02.13_SpecVariable.md`
  ——**只比对了字节数、首 5 行 frontmatter 与「去掉 frontmatter 后的正文 diff」，没有读它的正文当依据。**
  结果：两份**正文逐字节相同**，只有 frontmatter 的 `source_topic`（`115042.htm` / `115042_2.htm`）
  与 `source_html` 不同，**§10 的判据（去掉 `_2` 后缀后相同）成立**。
  **⚠️ 这在本页的 `sources:` 里没有体现**——frontmatter 只列了一条路径，
  所以「本页引的是哪一份」这件事**在页面上看不出来**（见下 ⚠️④）。
- **`## Member function` 三个函数各自的 `Parameter` 小表没有转写**：
  `operator =` 那一节下面挂的那张（只有 `rhl` 一格）**本页把它的说明并进了上面那张表**，
  其余没有更多内容。
- **`## Related information` 那一篇没读**：`How to create a universal test method class`
  （wiki 里已有页，见 [[how-to-create-a-universal-test-method-class]]）。
  **所以「向导里怎么把这个类型加进参数表」本页没有。**
- **`addParameter` / `setComment` 那篇没读**，例子里那条链式调用
  **本页只照例子抄了一行，没有回原文核它的签名。**
- **`SpecSearch` 那篇没读**——**例子是「intercepted」的，本页不知道它前后还有什么。**
- **`level file` / `timing file` 那两篇都没读**——
  **所以 spec 变量在文件里怎么声明、`equationSetNumber` 怎么编、`@port` 那一段的完整含义，
  本页一个字没有。**
- **图：0 张，因为这一篇一张图都没有。** 实测该篇对 `raw/` 的图片引用 **0 处**
  （`grep -o 'raw/[0-9]*\.\(png\|jpg\)'` 零命中），**上游 `raw/115042.htm`（6,689 字节）里也没有一个 `<img>`**
  ——**这不是「图够不着」，是这一篇本来就不带图**。
  所以本页**没有任何来自图的结论**，也没有一处需要标「④ 图证」。
- **没有实跑**：没有声明过 `SpecVariable` 参数、没有在机台上填过一次 `"LEV.1.fooSpec[mV]"`
  这样的串、没有验过填错的串会怎样。
  **`verified: doc-only` 指的就是这件事。**
- **没有跑 `verify_stages.py`**（按本批分工，避免抢同一个报告文件）。
- **没有动 `wiki/index.md`**，也没有把本页挂进 [[level]] / [[timing]] / [[testmethod]] 三页。

> ⚠️ **本篇的语料瑕疵，照实记、一处都没替它改**：
>
> ① **`th` 应为 `the`**：
>    `You can call the value of a field with th format "SpecVariable.field".`
>    ——**本页正文引这一句时原样写 `th`，没有改成 `the`。**
>
> ② **`operator =` 的签名少了结尾分号**，**而 [[spec-value]] 那一篇的同名函数是有的**：
>    本篇是 `SpecVariable& operator = (const SpecVariable& rhl)`，
>    兄弟篇是 `SpecValue& operator = (const SpecValue& rhl);`。
>    **同一批两篇文档，同一处不一致**——本页照原样引，不补分号。
>    **同族还有第二处不一致**：本篇的复位函数叫 **`Reset()`（大写 R）**，
>    兄弟篇叫 **`reset()`（小写）**；**本篇的节标题是 `## Member function`（单数），
>    兄弟篇是 `## Member functions`（复数）**。**两篇都没有版本记录说明谁改的，本页并列，不判。**
>
> ③ **格式串与 TIM 那个例子对不上**：格式串写的是 `specType.equationSetNumber.specName[unit]`，
>    **没有 `@port` 这一段**；而例子是 `"TIM.3.barSpec@port1[A]"`，
>    解释里还专门写了 `for port port1`。
>    **即：`@port` 是格式的一部分，却没有出现在格式串里。** 本页并列出两处，不替它补格式。
>
> ④ **同一篇文档在语料里有两个投放，本页 frontmatter 只列了一个。**
>    两条路径是 `02.07.02.13.04_SpecVariable.md`（本篇，`source_topic` = `115042.htm`）与
>    `02.07.04.02.13_SpecVariable.md`（`source_topic` = `115042_2.htm`），
>    **去掉 `_2` 后缀后相同**，正文逐字节相同（比对方法见「本页没做的」第二条）。
>    **按 §10，这是「同一篇页被投放了两次」，不是两篇文档**——
>    **引用本页时不要把它们当成两条独立来源**（[[smartest-6.5.0]] 页里它们仍各占一条，
>    因为那一页是按路径收录的）。
>
> ⑤ **字段五个、`parseFullName()` 的说明只点了四个**：
>    字段表列了 `mFullName` / `mType` / `mEquationSetId` / `mName` / `mUnit` 五个，
>    而 `parseFullName()` 写的是 `including type, equation set number, spec name and unit`——
>    **`mFullName` 不在那串里**。**「填完整个串是否等于填了 `mFullName`」原文没说，本页不判。**

`verified: doc-only`
