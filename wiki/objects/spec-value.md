---
type: object
title: SpecValue
layer: L2
stage: level
tags: [spec-value, utm, parameter-type, unit, level, testmethod, l2]
related: [spec-variable, how-to-create-a-universal-test-method-class, mapping-testmethod, level-spec, timing-spec, spec-set, spec-tool, svlr, pin-string, file-string, option-list, context-pins, universal-test-method-library, smartest-6.5.2, level, testmethod]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.02.13.03_SpecValue.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# SpecValue

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,233 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.02.13.03_SpecValue.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example

In the following example, `specVa1` is a parameter variable defined in the type SpecValue.

```
class TestSpecValue: public testmethod::TestMethod {
protected:
    testmethod::SpecValue specVa1;
  virtual void initialize()
  {

    addParameter("specVa1","SpecValue",&specVa1).setDefault("3800[mV]");
  }
  /**
   *This test is invoked per site.
   */
  virtual void run()
  {
   //specify a value and unit for specVa1
   specVa1.inputValueUnit("1500[mV]");
   //retrieves the value, unit, base unit and the unit options of specVa1
   double value = specVa1.getValue();
   STRING unit = specVa1.getUnit();
   STRING baseUnit=specVa1.getBaseUnit();
   const vector<string>* optionVec1 = specVa1.getUnitOptionVector();
   cout << "******The content of specVa1******"<<endl;
   cout << "value "  << value <<endl;
   cout <<"unit " <<unit <<endl;
   cout <<"base unit " <<baseUnit <<endl;
   for (size_t i=0;i<optionVec1->size();i++)
   {
      cout << "unit option " <<i <<":" << (*optionVec1)[i]<<endl;
   }
   //converts the value of specVa1 to the unit V.
   value = specVa1.getValueAsTargetUnit("V");
   cout <<"spec value with unit [V] " <<value <<endl;
   return;
 }
...
};
REGISTER_TESTMETHOD("TestSpecValue", TestSpecValue);
```

<!-- 语法节 end -->

## 是什么

**`SpecValue` 是 UTM（universal test method）的一个参数类型：一个「带单位的值」。** 原文第一句就是全部定义：

> 「The parameter type SpecValue is defined to represent a value with unit. Its value is in the
> format of "value[unit]".」

**两件事一次说完**：它**是参数类型**（在 test method 里声明、由 `addParameter` 注册的那一类东西），
不是命令、也不是文件；它的值**必须带单位**，写法固定为 `value[unit]`（例子里的 `3800[mV]` / `1500[mV]`）。

> 「There are several member functions defined for SpecValue. These member functions can be used
> in the test method to get and set the value and the unit of a SpecValue parameter.」

**即：这一族成员函数的用处，是从 test method 代码里取 / 设「值」和「单位」两样东西。**

### 十个成员函数（**这一节不在上面的「语法 / 参数」节里**）

**上面的「语法 / 参数」节只收了原文的 `## Example` 一节**（1,233 字符 = 那一份例子）。
**`## Member functions` 那一节（4,037 字符）一个字都没进去**——
脚本按段标记收，而这一篇的段标记是 `Example`，不是 `Member functions`（§4：脚本负责抽取，不重写）。
**所以下面这张表是本页从 raw 逐字抄的**，不是我从语法节复制的。

| 成员函数 | 签名（raw 里每节开头的代码块） | 干什么 |
|---|---|---|
| `getValue()` | `double getValue() const;` | 返回值 |
| `getUnit()` | `const std::string& getUnit() const;` | 返回 `unit` 那部分 |
| `getBaseUnit()` | `const std::string& getBaseUnit() const;` | 返回 base unit |
| `getUnitOptionVector()` | `const std::vector<std::string>* getUnitOptionVector() const;` | 返回指向 unit option vector 的**指针**；没指定 base unit 时返回 `0` |
| `setBaseUnit()` | `void setBaseUnit(const std::string& inputBase);` | 设 base unit；必要时更新 unit option list |
| `getValueAsTargetUnit()` | `double getValueAsTargetUnit(const std::string& targetUnit);` | 把值换算成指定单位 |
| `inputValueUnit()` | `bool inputValueUnit(const std::string& input);` | 改这个参数的值；格式不对返回 `false` |
| `parseValueUnit()` | `bool parseValueUnit(const std::string& input, std::string& valueStr, std::string& unit);` | 拆出 value 与 unit，分别存进两个出参 |
| `reset()` | `void reset();` | 所有成员变量复位 |
| `operator =` | `SpecValue& operator = (const SpecValue& rhl);` | 从另一个 SpecValue 拷贝 |

**原文那句概括（`get and set the value and the unit`）盖不住后两个**：`reset()` 是复位、
`operator =` 是复制，**它们不「取 / 设值」**——**（推断）**，依据就是上面这张表里的职责。
原文说 `several member functions`，没有给数目。

### 单位是一套「base unit + option vector + 当前单位」的三层模型

原文：

> 「Base unit is one of the units of a category and is used to represents specific unit category.
> For example, voltage units includes "nV", "uV", "mV", "V". Any one of them could be the base
> unit for voltage.」

**三个东西要分开**：

| 名字 | 是什么 | 谁动它 |
|---|---|---|
| **base unit** | 类别里的**任意一个**单位；选它 = 声明「这个参数属于哪个类别」 | `setBaseUnit()` |
| **unit option vector** | 该类别下的**全部**单位 | 由 base unit 决定，`setBaseUnit()` 会更新 |
| **当前单位** | 值实际用的那一个 | `inputValueUnit()`；由 `getUnit()` 读出。**`setDefault()` 也会带上它——这一条是（推断）**，见「典型用法」 |

> 「This function returns a pointer to unit option vector if a base unit is specified.
> Otherwise, 0 is returned. The unit vector contains all units of this category indicated by the
> base unit. For example, the unit option vector for voltage includes "nV", "uV", "mV", "V".」

**预定义的五类**（原文是一张清单，照抄）：

| 类别 | 单位 |
|---|---|
| Voltages | V, mV, uV, nV |
| Current | A, mA, uA, nA |
| Time | s, ms, us, ns, ps, fs |
| Frequency | THz, GHz, MHz, kHz, Hz |
| Bit width | UI |

**清单之外也能当 base unit**：

> 「If the input base unit is not in the predefined categories, it will be accepted as a new unit
> category with this input unit only. For example, mySpecValueVar.setBaseUnit("specalUnit"); is
> valid.」

**即：写一个清单外的单位，就自成一个「只有这一个单位」的新类别**（`option vector` 只有一项）。

**`setBaseUnit` 的入参不要带方括号**：

> 「The base unit to set. "[]" is not needed for this base unit input.」

### 两种「改单位」的语义完全不同

**`setBaseUnit("")` 不是「不改」，是清空**：

> 「If the specified base unit is empty, the current unit will be cleaned and no unit is available
> for the SpecValue parameter.」

**而 `inputValueUnit()` 遇到对不上的单位，是静默沿用旧单位。** 原文给了四个条件分支，
这是本页最该表格化的一处：

| `inputValueUnit(input)` 的形态 | 结果（原文） |
|---|---|
| 不是 `value[unit]` 格式 | **返回 `false`，什么都不改**（`false will be returned with no change happening`） |
| `unit` 在当前 base unit 的类别里 | **值和单位都生效**（`both "value" and "unit" will be set to effective`） |
| `unit` **不在**当前 base unit 的类别里 | **沿用上一个单位**（`the previous unit will be used`） |
| 只给纯数值（`pure value input`） | **沿用上一个单位**（`the previous unit will be used`） |

**第二、三行合起来是本页最值钱的一条**：给错单位**不报错、不返回 `false`**，
只是「拿旧单位去套这个数」——**所以 `inputValueUnit()` 的 `true` 返回值不保证单位是你写的那个。**

### 取值侧的四条边界

| 情形 | 结果（原文） |
|---|---|
| 值只有数值、没带单位（`getUnit()`） | 返回**上一个值的单位**（`the unit of the previous value will be returned`） |
| 参数刚初始化（`getUnit()`） | 当前单位 **= 指定的 base unit**（`the current unit is the same as the specified base unit`） |
| 没有 base unit（`getValueAsTargetUnit()`） | **返回当前值，不换算**（`If no base unit exists, it returns the current value.`） |
| 目标单位不在 unit option list 里（`getValueAsTargetUnit()`） | **抛 `std::runtime_error`**（`a std::runtime_error will be issued`） |

**最后一行是全篇唯一一处提到报错的地方。** 把它和上面那张表并排看，会发现**同一件「单位对不上」的事，
两个函数行为相反**：`inputValueUnit()` 静默沿用旧单位，`getValueAsTargetUnit()` 直接抛异常。
**原文没有解释这个不对称，本页照实并列。**

### `reset()` 复位成什么

> 「This function resets all member variable to default. This means the base unit and the current
> unit are set to empty, the value is set to zero and the pointer of unit option vector is set to
> zero.」

**四样东西各自复位**：base unit 空、当前单位空、值 `0`、option vector 指针 `0`。
**注意 base unit 也被清掉**——而 base unit 一空，`getUnitOptionVector()` 就返回 `0`（见上表）。

## 典型用法

**原文没有 `## Procedure`，也没有 `## Before you begin`**——只有一节 `## Example`，
导语是 `In the following example, specVa1 is a parameter variable defined in the type SpecValue.`
**从那一份例子里能读出的顺序，只有四步**：

| # | 在哪 | 代码（逐字） | 原文的解说 |
|---|---|---|---|
| 1 | 类定义里 | `testmethod::SpecValue specVa1;` | —（那一行没有单独解说） |
| 2 | `initialize()` 里 | `addParameter("specVa1","SpecValue",&specVa1).setDefault("3800[mV]");` | 原文对 `initialize()` 的注释：`This method is called just once after a testsuite is created.` |
| 3 | `run()` 里 | `specVa1.inputValueUnit("1500[mV]");` | 原文行末注释：`//specify a value and unit for specVa1` |
| 4 | `run()` 里 | `getValue()` / `getUnit()` / `getBaseUnit()` / `getUnitOptionVector()` 四个连续取，再 `getValueAsTargetUnit("V")` 换算 | 注释分别是 `//retrieves the value, unit, base unit and the unit options of specVa1`、`//converts the value of specVa1 to the unit V.` |

原文对 `run()` 的注释是 `This test is invoked per site.`

**两条例子里看得出来、但原文没写的：**

- **例子从头到尾没有调 `setBaseUnit()`**，而第 4 步照样取到了 `getBaseUnit()` 与
  `getUnitOptionVector()`——**说明 base unit 是第 2 步的 `setDefault("3800[mV]")` 带进来的**
  （**推断**，依据是例子里唯一设置值的动作只有 `setDefault` 与 `inputValueUnit`；
  **原文没有一句说 `setDefault` 会设 base unit**）。
- **例子对 `getUnitOptionVector()` 的返回值直接解引用**（`optionVec1->size()`、`(*optionVec1)[i]`），
  **没有判空**——而原文明说没有 base unit 时它返回 `0`。**照例子抄会漏掉判空。**

**下一步**：原文 `## Related information` 只给了 `How to create a universal test method class` 一篇
（见「和谁有关」）；**本篇没有 `## What to do next` 段**。

## 和谁有关

- [[how-to-create-a-universal-test-method-class]] — **本页唯一的上游**。
  本篇 `## Related information` 只有它一条；那页把 `SpecValue` 列进参数类型清单，
  并给了一句定义（格式是 `"value[unit]"`）——**本页是那句话的专页**。
- [[mapping-testmethod]] — **本页在建 test method 那条链上的位置**。
  那张对照表「建 test method 类：模板 / 类名 / 参数」一行的 **L2 格**把
  [[pin-string]] / [[spec-variable]] / 本页 / [[file-string]] / [[option-list]] / [[context-pins]]
  并排放在一起——**即：它们是同一批「参数类型」，不是动作**。
- [[spec-variable]] — **同一批清单里的兄弟类型**。两者都表示「一个带单位的值」，
  但**取值来源不同**：`SpecValue` 的值就是写下的字面量，
  `SpecVariable` 指的是 level / timing setup 文件里定义的一个 spec 变量。
  **注意：这一句依据的是 [[spec-variable]] 那一篇，不是本页的出处文档**——
  **本篇一个字没提 level / timing 文件**，所以「本页用于哪一侧」在语料里没有依据。
- [[spec-set]] / [[spec-tool]] / [[level-spec]] / [[svlr]] — **同一族「spec」名字，但都不是本页**：
  那几个讲的是 level 侧 spec 变量 / spec set 的容器、GUI 与改值接口。
  **本页的出处文档没有链到它们中的任何一个**，所以这里的「同族」是
  **按名字与 [[mapping-level]] / [[mapping-testmethod]] 的行位**说的（**推断**），不是文档事实。
- [[universal-test-method-library]] — **这类参数真正被用起来的地方**：UTM 库里的 test method
  就是拿这些参数类型当输入参数（**依据是 [[how-to-create-a-universal-test-method-class]]，不是本篇**）。
- [[smartest-6.5.2]] — **版本落点**，见「版本」。
- `addParameter`（**未建**；raw: `02.07.04.01.03_addParameter.md`）— 第 2 步注册参数用的那个 API；
  **那篇本页没读**，`.setDefault` 那一环的签名与返回值本页没有。

## 版本

本文档**有** `## Functional changes` 段，**只有一条**：

- **`Introduced in SmarTest 6.5.2`**

> **这一条不是 §11.2② 的哨兵值。** 哨兵值写的是 `Introduced **before** SmarTest 6.3.2`
> （意思是「**在本语料覆盖范围开始之前就已经有了**」）；本篇写的是 `Introduced in 6.5.2`
> ——**是一个真版本号**。**两句话只差一个词，读法完全相反，这一处最容易误判。**

**旁证（wiki 内部，不在本页 `sources:` 里）**：[[smartest-6.5.2]] 的条目里有一条就是本篇的出处文档
（`02.07.02.13.03_SpecValue.md`，条目文字与上面那条一致）——**那页不是本页建的，这里只指路。**
同一页里另有一批条目说 UTM 库里的 test method（`Continuity` / `GeneralPMU` / `Leakage` / `HighZ` 等）
**在 6.5.2 把参数类型改成了 `SpecValue`**——
**那批文档本页一篇没读，只在这里指路**（它们属于 [[universal-test-method-library]] 那一侧的证据）。

**原文没有给这两个版本号以外的任何变更记录**——所以
「6.5.2 之后这十个成员函数的语义改过没有」本页没有依据。

## 出处

`sources:` 一篇：`02_System_reference/02.07_Test_Method_Reference/02.07.02.13.03_SpecValue.md`
（TDC `115043.htm`，6,769 字节 / 257 行）——**整篇读完**。

**「语法 / 参数」节只收了原文的 `## Example` 一节**（1,233 字符）。
**`## Member functions`（4,037 字符）整节在用上表中由本页逐条写出**——
**所以上面那张签名表不在脚本辖区里，不是「改语法节」。**

**本页没做的**：

- **只读了这一篇的正文。** 正文里每一个文档事实都出自这 257 行。
- **一处例外，要明确交代**：为做 §10 的**第 0 步（先查是不是同一篇被投放了两次）**，
  本页比对过版本页条目里出现的另一条路径
  `02_System_reference/02.07_Test_Method_Reference/02.07.04.02.14_SpecValue.md`
  ——**只比对了字节数、首 5 行 frontmatter 与「去掉 frontmatter 后的正文 diff」，没有读它的正文当依据。**
  结果：两份**正文逐字节相同**，只有 frontmatter 的 `source_topic`（`115043.htm` / `115043_2.htm`）
  与 `source_html` 不同，**§10 的判据（去掉 `_2` 后缀后相同）成立**。
- **`## Member functions` 各节末尾的 `Parameter` 小表没有逐格转写。**
  原文在 `setBaseUnit` / `getValueAsTargetUnit` / `inputValueUnit` / `parseValueUnit` / `operator =`
  五节下面各挂了一张小表；**本页只写了其中两处**（`setBaseUnit` 的 `inputBase` 那格、
  `parseValueUnit` 的三个 I/O 行），**其余几格的说明文字本页没有搬**。
- **`## Related information` 那一篇没读**：`How to create a universal test method class`
  （wiki 里已有页，见 [[how-to-create-a-universal-test-method-class]]）。
  **所以「向导里怎么把这个类型加进参数表」本页没有。**
- **`addParameter` 那篇没读**，例子里那条链式调用（`addParameter` 之后接 `.setDefault`）
  **本页只照例子抄了一行，没有回原文核它的签名。**
- **没读任何一篇 UTM 库的 test method 文档**——**「哪些测试用了 `SpecValue`」本页只有版本页的指路，
  没有一手依据。**
- **图：0 张，因为这一篇一张图都没有。** 实测该篇对 `raw/` 的图片引用 **0 处**
  （`grep -o 'raw/[0-9]*\.\(png\|jpg\)'` 零命中），**上游 `raw/115043.htm`（11,263 字节）里也没有一个 `<img>`**
  ——**这不是「图够不着」，是这一篇本来就不带图**。
  所以本页**没有任何来自图的结论**，也没有一处需要标「④ 图证」。
- **代码里的 C++ 一律照抄，没有编译核对**：例子里 `STRING unit` 与
  `const vector<string>* optionVec1` 这两处的类型写法能不能编过，**本页没有验**（见下 ⚠️⑤）。
- **没有实跑**：没有编译过任何调 `SpecValue` 的 test method，
  没有在机台上确认过 `inputValueUnit()` 遇到类别外单位时是不是真的静默沿用旧单位。
  **`verified: doc-only` 指的就是这件事。**
- **没有跑 `verify_stages.py`**（按本批分工，避免抢同一个报告文件）。
- **没有动 `wiki/index.md`**，也没有把本页挂进 [[level]] / [[testmethod]] 两页。

> ⚠️ **本篇的语料瑕疵，照实记、一处都没替它改**：
>
> ① **`to represents` 与 `units includes` 两处主谓/不定式不合**，原文如此，本页照原样引：
>    `Base unit is one of the units of a category and is used to represents specific unit category.`
>    `For example, voltage units includes "nV", "uV", "mV", "V".`
>    ——**同一篇稍后那句 `the unit option vector for voltage includes` 是对的**，
>    **一篇里两种数并存，本页并列，不替它统一。**
>
> ② **`based` 应为 `base`**：
>    `This function sets the base unit and updates the unit option list if the specified based unit
>    is not in the current unit list.`
>
> ③ **例子里的新单位名 `specalUnit` 应为 `specialUnit`**：
>    `For example, mySpecValueVar.setBaseUnit("specalUnit"); is valid.`
>    ——**本页正文引这一句时原样写 `specalUnit`，没有改成正确拼法。**
>
> ④ **同一批单位，同一篇里两种排列方向**：预定义清单写 `Voltages: V, mV, uV, nV`（从大到小），
>    而 `getBaseUnit()` 与 `getUnitOptionVector()` 两处写 `"nV", "uV", "mV", "V"`（从小到大）。
>    **五个单位、两种顺序，原文没说哪种是规范，本页并列。**
>
> ⑤ **例子用 `STRING` 与 `vector<string>`，签名用 `std::string` 与 `std::vector<std::string>`**：
>    例子是 `STRING unit = specVa1.getUnit();` 与 `const vector<string>* optionVec1 = specVa1.getUnitOptionVector();`，
>    而成员函数节的签名是 `const std::string& getUnit() const;` 与
>    `const std::vector<std::string>* getUnitOptionVector() const;`。
>    **原文没有说 `STRING` 是不是 `std::string` 的别名**，本页不替它们合并。
>
> ⑥ **`parseValueUnit()` 的参数表里 `valueStr` 那格多了一组反引号**——原文逐字：
>
> ```
> The "`value`"`` part of the input.
> ```
>
> **「双引号 value 双引号」后面紧跟着两个反引号**；而同一张表里 `unit` 那格是干净的
> `The "[unit]" part of the input.`。**这是 md 转换留下的记号**，
> 本页只在这一条里照原样记它，正文没有复现那两个多出来的反引号。
>
> ⑦ **同一篇文档在语料里有两个投放，本页 frontmatter 只列了一个。**
>    两条路径是 `02.07.02.13.03_SpecValue.md`（本篇，`source_topic` = `115043.htm`）与
>    `02.07.04.02.14_SpecValue.md`（`source_topic` = `115043_2.htm`），
>    **去掉 `_2` 后缀后相同**，正文逐字节相同（比对方法见「本页没做的」第二条）。
>    **按 §10，这是「同一篇页被投放了两次」，不是两篇文档**——
>    **引用本页时不要把它们当成两条独立来源**（[[smartest-6.5.2]] 页里它们仍各占一条，
>    因为那一页是按路径收录的）。

`verified: doc-only`
