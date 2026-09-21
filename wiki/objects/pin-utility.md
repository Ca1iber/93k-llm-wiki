---
type: object
title: PIN_UTILITY
layer: L2
stage: pin
tags: [testmethod, api, pin-utility, pin-list, pin-group, pin-name-expansion, string-vector, per-pin-result]
related: [pin, pin-group-editor, pin-configuration-tool, pin-string, test-method-class, testmethod, mapping-testmethod, dps-pins-editor, digital-pins-editor, utility-pins-editor, spmu-pin-task, spmu-pin-task-mode, flex-relay, ps1600, dc-scale-uhc4t-card, dc-scale-xps256-card, dps128-dps64-cards, on-first-invocation-begin, test, testset, tmlimits, universal-test-method-library, smartest-7.2.1]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.147_PIN_UTILITY.md
created: 2026-09-21
updated: 2026-09-21
verified: doc-only
---

# PIN_UTILITY

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **4,348 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.147_PIN_UTILITY.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example 1

```
STRING pinList  = "pin1,pin2,pin3";
STRING_VECTOR pinNameList;
pinNameList = PinUtility.getDigitalPinNamesFromPinList(pinList, TM::IO_PIN, TRUE,TRUE);
for (uint index = 0; index < pinNameList.size(); index++)
{
     cout << pinNameList [index] << endl;
      // pin1
      // pin2
      // pin3
}
```

### Example 2

```
STRING pinList1 = "pin1,pin2,pin3";
STRING pinList2 = "pin4,pin5,pin6";
STRING_VECTOR sum, sv1, sv2;
sv1 = PinUtility.getDigitalPinNamesFromPinList (pinList1, TM::IO_PIN, TRUE,TRUE);
sv2 = PinUtility.getDigitalPinNamesFromPinList (pinList2, TM::IO_PIN, TRUE,TRUE);
sum = sv1 + sv2;
sv1*=sv2;
```

### Example 3

The example shows how to use the getPinType parameter.

```
cout << "Pintype of dps1 is: \"" << PinUtility.getPinType("dps1") << "\"" << endl;
cout << "Pintype of dps2 is: \"" << PinUtility.getPinType("dps2") << "\"" << endl;
cout << "Pintype of pmu31 is: \"" << PinUtility.getPinType("pmu1") << "\"" << endl;
cout << "Pintype of pin1 is: \"" << PinUtility.getPinType("pin1") << "\"" << endl;
cout << "Pintype of hvpin1 is: \"" << PinUtility.getPinType("hvpin1") << "\"" << endl;
```

returns:

```
Pintype of dps1 is: "DCS-DPS128HC"
Pintype of dps2 is: "DCS-DPS128HV"
Pintype of pmu3 is: "DCS-VI32"
Pintype of pin1 is: "PS1600"
Pintype of hvpin1 is: "PS1600"
```

### Example 4

This is a complete example that shows how to use PIN_UTILITY together with getDigitalPinNamesFromPinList to extract single pin results. dForceLow, dForceHigh1 and dForceHigh2 are parameters defined in the test method.

```
/**********************************
 *This test is invoked per site.
 **********************************/
 virtual void run()
 {
 PPMU_SETTING setLeakLow , setLeakHigh ;
 PPMU_MEASURE measLeakHigh , measLeakLow ;
 PPMU_RELAY relClose , relOpen ;
 TASK_LIST tskLeak ;
 /*************************************************************
 * Execution Section:
 * This section will executed only once.
 * ***********************************************************/
 ON_FIRST_INVOCATION_BEGIN();
 setLeakLow.pin ( "leak_pins1,leak_pins2" ).vForce (dForceLow V )
 .iRange ( 100 uA).min( 1.2 uA ).max ( 20 uA ) ;
 // One PPMU_SETTING can hold different values for different pins.
 setLeakHigh.pin ( "leak_pins1" ).vForce (dForceHigh1 V ).iRange ( 100 uA).min( 1.2 uA ).max ( 20 uA ) ;
 setLeakHigh.pin ( "leak_pins2" ).vForce (dForceHigh2 V ).iRange ( 100 uA).min( 1.2 uA ).max ( 20 uA ) ;
 // value only test test OVAL is faster than PVAL
 measLeakHigh.pin ( "leak_pins1, leak_pins2" ).execMode( TM::OVAL );
 measLeakLow.pin ( "leak_pins1, leak_pins2" ).execMode( TM::OVAL );
 relClose.pin ( "leak_pins1, leak_pins2" ).status ( "PPMU_ON" );
 relClose.wait ( 1 ms );
 relOpen.pin ( "leak_pins1, leak_pins2" ).status ( "AC_ON" );
 //Multiple measurements and settings are combined into one measurement.
 //The results of all sites are cashed in the measrement objects.
 //There is not .setup() API needed because the values will NOT change during
 //the testprogram run.
 tskLeak.add(setLeakLow).add(relClose).add(measLeakLow)
 .add(setLeakHigh).add(measLeakHigh).add(relOpen);
 //Execute the Leakage Pattern and the taskList
 CONNECT();
 FUNCTIONAL_TEST();
 tskLeak.execute();
 ON_FIRST_INVOCATION_END();
 /*************************************************************
 * Result upload, calculation and datalog
 * This section will be executed for each site.
 * ***********************************************************/
 STRING_VECTOR pinNameList;
 int SizeOfNameList;
 //Get Results and Datalog from Group leak_pins1
 pinNameList = PinUtility.getDigitalPinNamesFromPinList("leak_pins1", TM::IO_PIN, TRUE,TRUE);
 SizeOfNameList = pinNameList.size();
 for (int index = 0; index < SizeOfNameList; index++)
 {
 TEST(pinNameList[index],"Leakage_Low" ,tmLimits, measLeakLow .getValue(pinNameList[index]), TRUE);
 TEST(pinNameList[index],"Leakage_High",tmLimits, measLeakHigh.getValue(pinNameList[index]), TRUE);
 }
 //Get Results and Datalog from Group leak_pins1
 pinNameList = PinUtility.getDigitalPinNamesFromPinList("leak_pins2", TM::IO_PIN, TRUE,TRUE);
 SizeOfNameList = pinNameList.size();
 for (int index = 0; index < SizeOfNameList; index++)
 {
 TEST(pinNameList[index],"Leakage_Low" ,tmLimits, measLeakLow .getValue(pinNameList[index]), TRUE);
 TEST(pinNameList[index],"Leakage_High",tmLimits, measLeakHigh.getValue(pinNameList[index]), TRUE);
 }
 return;
 }
```

<!-- 语法节 end -->

## 是什么

**`PIN_UTILITY` 是 L2 的 test method API：把一串「针的名字」展开成「具体的针名清单」。**
原文第二段的定义逐字：

> 「The PIN_UTILITY API is used to expand pin names from a pin list, including the names of the
> pins in a pin group, and expands a STRING containing pin names that are separated by a comma,
> for example, "pin1, pin2, pin3,....".」

**展开的两个方向都在这一句里**：
**① 把（含 pin group 名的）pin list 摊平成具体 pin 名；② 认逗号分隔的那串写法**（`"pin1, pin2, pin3,...."`）。

### 为什么需要它（原文第一段，这是本页的「因为所以」）

原文开门一整段逐字：

> 「When creating a device test, all pins to be tested are defined using the Pin Configuration tool.
> Some of the pins in this pin list are often defined in pin groups. When a test is created using
> Test Methods, the test is specified for that pin list, and the measurement results are retrieved
> on a per-pin basis. The measurement results are associated with the pin names, so you must know
> the pin names of all the pins in the pin list, including the names of the pins in the pin groups,
> to retrieve the measurement results for all of the pins in the pin list.」

**这条链拆成四步：**

| # | 原文 | 事 |
|---|---|---|
| 1 | `all pins to be tested are defined using the Pin Configuration tool` | 针在 [[pin-configuration-tool]] 里定义 |
| 2 | `Some of the pins … are often defined in pin groups` | **pin list 里常常混着 pin group 名** |
| 3 | `the test is specified for that pin list, and the measurement results are retrieved on a per-pin basis` | **测试按 pin list 指定，取结果却按单针** |
| 4 | `The measurement results are associated with the pin names` | **结果挂在 pin 名上** |

**所以 `PIN_UTILITY` 存在的理由就是第 2 步与第 3 步之间的落差**：
**你手里是一串「名字」（其中可能有组名），要取结果时却必须一个针一个针地报名字。**
**它不是测量 API，是一个「名字的翻译层」。**

### 类怎么用：没有公开构造函数

原文 `## Class definition` 逐字：

> 「  Constructor This class has no public constructor.」

> 「To use the PIN_UTILITY API, you must always use the system-prepared class object PinUtility.
> You cannot create any object of this class.」

**即：`new` 不出来，只能用它已经准备好的那个对象 `PinUtility`**——
**四个例子里的写法都是 `PinUtility.getXxx(...)`**（**点号直接跟在类名上**）。

**头文件路径**（原文逐字）：

> 「This API is defined in the header file /opt/hp93000/soc/prod_com/include/MAPI/PinUtility.h.」

### 七个成员函数

原文 `Class definition` 一节有一份七项清单（**是同一文件内的锚点链接**），
`## Member functions` 一节逐个展开。**本页按那七项转述**（**原文的这些签名与参数表都没进
「语法 / 参数」节**，见 `## 出处`）：

| # | 函数 | 一句话（原文） | 参数 |
|---|---|---|---|
| 1 | `expandDigitalPinNamesFromPinList()` | `converts the pin names of the specified pin type contained in the pin list into a string vector` | 3 个（见下）**——已弃用** |
| 2 | `getDigitalPinNamesFromPinList()` | 同上，**但要用的就是它**；**组里的针按字母序或组定义序排** | **5 个**（见下） |
| 3 | `getDpsPinNamesFromPinList()` | `converts the DPS pin names contained in the pin list into a string vector` | 2 个 |
| 4 | `getPinType()` | `queries the hardware capabilities behind a pin (MCB, MCE, PS400, PS1600)` | 1 个：`PinName` |
| 5 | `getSharedDigitalPins()` | `returns all digital pins which are shared in more than one site` | **无** |
| 6 | `getSharedDpsPins()` | `returns all dps pins which are shared in more than one site` | **无** |
| 7 | `createPinListFromPinNames()` | 反向：**把 pin 名的 vector 合成一条逗号分隔的 pin list 字符串** | 1 个：`pinName` |

**三条要先说清：**

- **① 第 1 个已弃用。** 原文逐字：
  > 「This member function is only supported for downward compatibility. For new applications,
  > getDigitalPinNamesFromPinList() should be used instead.」
  **所以新旧两条路都在，新的那条是 [[pin-utility]] 自己的第 2 个函数。**
- **② 七个函数里只有头两个 + 第 3 个是「展开」。** 第 4 个查硬件、第 5/6 个查共享、
  第 7 个是**反向合成**。**「展开」这个词只覆盖前三个。**
- **③ 七个都被原文说成返回 `std::vector`（`STRING_VECTOR`）**，原文反复用同一句：
  `Since this member function will return a std::vector, you can use all available methods
  provided in the Standard Template Library (STL) for std::vector, such as loop over all the
  elements or adding two separate lists.`
  （**这一句在第 1、2、3、5、6 个函数下都出现了一遍。**）
  **例外是第 4 个（`getPinType` 返回单个 `STRING`）与第 7 个（返回 `const STRING&`）。**

### `pinType`：五个值，可以用 `|` 组合

原文两份参数表对 `pinType` 写的是同一份取值清单：

| 值 | 原文 |
|---|---|
| `TM::I_PIN` | — |
| `TM::O_PIN` | — |
| `TM::IO_PIN` | — |
| `TM::DC_PIN` | — |
| `TM::ALL_DIGITAL` | — |

**组合写法**原文给了例子，**但两份表给的措辞不一样**：

| 在哪 | 原文逐字 |
|---|---|
| `expandDigitalPinNamesFromPinList()` 的表 | `` `TM::O_PIN|TM::DC_PIN` will return all output and dc pins. `` |
| `getDigitalPinNamesFromPinList()` 的表 | `TM::O_PIN|TM::DC_PIN will return all "o" and "dc" pins.` |

**同一件事写了两遍，一遍说 `output and dc pins`、一遍说 `"o" and "dc" pins`**
（**后一遍还给 `o` / `dc` 加了引号**）。**原文如此（见 `## 出处` ④）。**

### 两个 `throw` 开关：默认值不一样，而且**只有一份表写了默认值**

`getDigitalPinNamesFromPinList()` 的第 3、4 个参数是两个错误开关。
**原文只有这一个函数把它们写成「`TRUE` / `FALSE (default)`」两行**：

| 参数 | `TRUE` | `FALSE` |
|---|---|---|
| `throwErrorOnMissingPinNames` | `An error is thrown if any pin in the list is not defined.` | **`FALSE (default)`**：`Undefined pins are not transferred into the vector. No error is thrown.` |
| `throwErrorOnMismatchedPinTypes` | `An error is thrown if the pin list contains any pin that has not one of the types specified with pinType.` | **`FALSE (default)`**：`Only pins that have one of the requested types are transferred into the vector. No error is thrown.` |

**⚠️ 可对照的是弃用的那个 `expandDigitalPinNamesFromPinList()`**：
**它的同名开关（`ignoreMissingPins`）写的是 `TRUE = no error if the pin is not defined` /
`FALSE = error if pin is not defined`，而且没有标默认值。**
**所以新旧两个函数的同名开关，极性是相反的**：
**新函数里 `TRUE` = 抛错，旧函数里 `TRUE` = 不抛错（`ignore` 那个词就是这么来的）。**

### `sortOrder`：两个取值

原文逐字：

> 「It controls the order of the returned pins. It can be PIN_UTILITY::ALPHABETICAL for the
> alphabetical order or PIN_UTILITY::DEFINITION_ORDER for the group definition order.」

**两个取值：`PIN_UTILITY::ALPHABETICAL`（字母序）/ `PIN_UTILITY::DEFINITION_ORDER`（组定义序）。**
**正文另有一句补充**（在函数说明里，不在参数表里）：
`For pins defined in pin groups, the pins are listed in alphabetical order or pin group definition
order.` ——**即这个排序只对「来自 pin group 的针」有可分辨的效果。**

### `getPinType()`：查的是「针背后那块硬件」

原文逐字：

> 「This member function queries the hardware capabilities behind a pin (MCB, MCE, PS400, PS1600).
> For analog setups, you can query the pin type and set filters or frequencies according to the
> capabilities of the hardware.」

**括注里是四个硬件名：`MCB` / `MCE` / `PS400` / `PS1600`。**
⚠️ **而 Example 3 的返回里出现的是另一批名字**（`DCS-DPS128HC` / `DCS-DPS128HV` /
`DCS-VI32` / `PS1600`）——**只有 `PS1600` 一个两边都有**（见 `## 出处` ⑤）。

### `STRING_VECTOR` 的四种运算（原文 `## Important points`）

原文逐字给出四条，**这是「展开之后能干什么」的那一半**：

| 运算 | 原文 | 结果 |
|---|---|---|
| `+` | `returns a STRING_VECTOR object that contains all the elements of the two argument vectors without duplicates` | **并集（去重）** |
| `-` | `returns a STRING_VECTOR object that contains all the elements that occur in the first argument vector, but not in the second` | **差集（在第一个里、不在第二个里）** |
| `*` | `returns a STRING_VECTOR object that contains all the elements that occur in both argument vectors` | **交集** |
| `+=` `-=` `*=` | `If you use the extended operators +=, -=, or *=, the result will be stored in the first argument vector.` | **结果存回第一个** |

**外加一条 const 的告诫**，逐字：

> 「When using the normal operators, which return the const type, you can continue to operate on
> the result as a normal const variable but not modify them. If you need to perform other changes,
> you can store the result into your own variable (or instance) first.」

### 四个例子在原文里的位置

原文 `## Examples` 一节有四个 `### Example N`，**四个都在本页的「语法 / 参数」节里逐字**：

| # | 例子 | 用到的函数 |
|---|---|---|
| 1 | 展开 `"pin1,pin2,pin3"` 并逐个打印 | `getDigitalPinNamesFromPinList` |
| 2 | 两条列表各展开一次，然后做 `+` 与 `*=` | `getDigitalPinNamesFromPinList` |
| 3 | 五个针各查一次类型并打印 | `getPinType` |
| 4 | **完整的泄漏测试**：setting / measure / relay / task list，然后在 per-site 段用展开取单针结果 | `getDigitalPinNamesFromPinList` |

**⚠️ 七个函数里，例子只用了两个**（`getDigitalPinNamesFromPinList` 与 `getPinType`）——
`getDpsPinNamesFromPinList` / `getSharedDigitalPins` / `getSharedDpsPins` /
`createPinListFromPinNames` **在多例里一次都没出现**（见 `## 出处` ⑥）。

## 典型用法

**原文没有 `## Procedure` / `## Before you begin` / `## What to do next` 段**，
**用法完全靠 `## Examples` 那四段代码**。**本页按那四段代码落成动作**：

**① 单次展开（Example 1）**

1. 准备一条逗号分隔的 pin list：`STRING pinList = "pin1,pin2,pin3";`
2. 声明一个 `STRING_VECTOR` 接返回。
3. `pinNameList = PinUtility.getDigitalPinNamesFromPinList(pinList, TM::IO_PIN, TRUE,TRUE);`
4. 用 `size()` + `[]` 遍历（**原文的注释把预期输出写在循环里**：
   `// pin1` / `// pin2` / `// pin3`）。

**② 两条列表做集合运算（Example 2）**

- 两次展开拿到 `sv1` / `sv2`，然后 `sum = sv1 + sv2;`（**并集**）与 `sv1 *= sv2;`（**交集**，
  结果存回 `sv1`）。**注意 `Example 2` 里 `sum` 只被赋值、没有被打印**。

**③ 查硬件类型（Example 3）**

- `PinUtility.getPinType("dps1")` 这样逐针查，**返回值直接当 `STRING` 打印**。
  **原文的 `## Member functions` 里对 `getPinType` 的那一句是
  `See also Example 3 below.`**

**④ 完整用法：按 pin group 取单针结果（Example 4，本页最有用的一段）**

| 阶段 | 原文代码在做什么 |
|---|---|
| **执行段（`ON_FIRST_INVOCATION_BEGIN()` 到 `ON_FIRST_INVOCATION_END()`，只跑一次）** | 建 `PPMU_SETTING` / `PPMU_MEASURE` / `PPMU_RELAY`，**每个对象的 `.pin(...)` 里填的都是 pin list 或 pin group 名**（`"leak_pins1,leak_pins2"` / `"leak_pins1"`），然后挂进 `TASK_LIST`，`CONNECT()` → `FUNCTIONAL_TEST()` → `tskLeak.execute()` |
| **结果段（每个 site 跑一遍）** | **`pinNameList = PinUtility.getDigitalPinNamesFromPinList("leak_pins1", TM::IO_PIN, TRUE,TRUE);`** 把**组名**摊成针名，再 `for` 一圈用 `pinNameList[index]` 去 `measLeakLow.getValue(...)` 取那一针的值，并 `TEST(...)` 上报 |

**这就是 `PIN_UTILITY` 的用法要点**：
**设置 / 测量那一侧可以直接写组名**（`setLeakLow.pin("leak_pins1,leak_pins2")`），
**而取结果那一侧要把组名摊成针名**——
**这正是原文第一段那条「链」在代码里的样子。**

**从原文能落成的动作：**

| 要做的 | 依据 |
|---|---|
| 展开一条（含组名的）pin list | `getDigitalPinNamesFromPinList(pinList, pinType, TRUE, TRUE, sortOrder)` |
| 只在某个类型里展开 | 第 2 个参数给 `TM::I_PIN` / `O_PIN` / `IO_PIN` / `DC_PIN` / `ALL_DIGITAL`，**可以用 `\|` 组合** |
| 让未定义的针直接抛错 | `throwErrorOnMissingPinNames` 给 `TRUE` |
| 让类型不匹配直接抛错 | `throwErrorOnMismatchedPinTypes` 给 `TRUE` |
| 控制组内针的排法 | 第 5 个参数给 `PIN_UTILITY::ALPHABETICAL` 或 `PIN_UTILITY::DEFINITION_ORDER` |
| 只取 DPS 针 | `getDpsPinNamesFromPinList(dpsPinList, throwErrorOnMissingPinNames)` |
| 查针背后是什么硬件 | `getPinType(pinName)` |
| 查跨 site 共享的针 | `getSharedDigitalPins()` / `getSharedDpsPins()` |
| 把针名向量合回一条字符串 | `createPinListFromPinNames(pinNameVector)` |
| 两条清单求并 / 差 / 交 | `+` / `-` / `*`；**要存回左边就用 `+=` / `-=` / `*=`** |

**⚠️ 一处要留意的写法差别**：**四个例子里调用 `getDigitalPinNamesFromPinList` 一律只给 4 个实参**
（`pinList, TM::IO_PIN, TRUE,TRUE`），**而原文的签名是 5 个参数**
（第 5 个是 `sortOrder`）。**原文没有说第 5 个有默认值**（见 `## 出处` ③）。

## 和谁有关

- [[pin]] — **本 API 展开出来的就是它**。原文第一段说结果 `are associated with the pin names`，
  而展开的目的就是拿到 `the pin names of all the pins in the pin list`。
  **pin 是什么、怎么定义，在那页；本页只有「名字怎么摊平」这一件事。**
- [[pin-configuration-tool]] — **上游，而且是原文第一句就点名的**：
  `all pins to be tested are defined using the Pin Configuration tool.`
  **本页的输入（pin list 与 pin group 名）都是在那里定义的**，本页没有那边的任何事实。
- [[pin-group-editor]] — **`pin group` 名从哪来**。原文说展开要
  `including the names of the pins in a pin group`——**本页只讲「组名会被摊开」，
  组怎么建、组里有什么规矩在那页。**
- [[pin-string]] — **（推断）名字近，但本页没有依据说它们是一回事。**
  [[pin-string]] 是 test method 参数的**类型**（原文那句是
  `PinString is used for pins, pin lists or pin groups.`）；
  **本页是把 pin list 摊成针名的 API**。
  **两者看着像同一件事的两侧（一个是「参数值」，一个是「展开它」），
  但那是本页的推断，依据只是两篇各自的定义句；本篇 raw 里 `PinString` 出现 0 次，
  本页也没有读 [[pin-string]]。**
- [[test-method-class]] / [[testmethod]] — **本页的宿主**：
  API 只能在 test method 的 `run()` 里用（**四个例子都是裸语句，Example 4 是
  `virtual void run()`**）。**frontmatter 的 `stage: pin` 是「最近的一段」，
  `layer: L2` 指的是它属于 Test Method API 这一层。**
- [[on-first-invocation-begin]] — **Example 4 里那个「只跑一次」的边界**：
  展开取结果那一段在 `ON_FIRST_INVOCATION_END()` **之后**，**即每 site 跑一遍**。
  **本页只有这一个用法事实，那两个标记本身在那页。**
- [[tmlimits]] / [[test]] / [[testset]] — **Example 4 里展开之后拿去干什么**：
  `TEST(pinNameList[index],"Leakage_Low",tmLimits, measLeakLow.getValue(...), TRUE)`。
  **`tmLimits` 与 `TEST` 的规矩在那几页，本页没有。**
- [[spmu-pin-task]] / [[spmu-pin-task-mode]] / [[flex-relay]] / [[dps-pins-editor]] —
  **（推断）同族的 pin 侧 L2 对象**，**依据只是它们同在 `02.07.04` 那一支、
  且都围绕「给一批针做同一件事」**。**本篇 raw 里这四个名字一个都没有**，
  **本页没有读那几页，所以这是推断，不是原文明写的。**
- [[digital-pins-editor]] / [[utility-pins-editor]] — **（推断）pin 名字的来源那一侧**。
  **同样是按 stage/名字相邻列出的，本页没有依据。**
- [[ps1600]] — **两处硬件名清单里唯一同时出现的那一个**
  （`getPinType` 的括注里有 `PS1600`，Example 3 的返回里也有 `PS1600`）。
  **本页只有这个字符串，那张卡本身在那页。**
- [[dc-scale-uhc4t-card]] / [[dc-scale-xps256-card]] / [[dps128-dps64-cards]] —
  **（推断）Example 3 返回串里那三个 `DCS-…` 名字的可能所指**
  （`DCS-DPS128HC` / `DCS-DPS128HV` / `DCS-VI32`）。
  **依据只是名字里的 `DPS128` / `VI32` 与那几页的页名对得上；
  原文没有把这些名字链到任何地方，本页也没有读那几页——所以这是推断。**
- [[universal-test-method-library]] — **（推断）宿主工程**：本页的函数是 UTM 的 API。
  **依据只是本篇 `02.07.02.02.02` 那一支的姊妹篇讲的是「怎么建 UTM 类」这件事；
  本篇 raw 里 `universal` 0 次，所以这是推断。**
- `MCB` / `MCE` / `PS400`（**均未建、均不在 allowlist，故用反引号**）——
  `getPinType` 括注里那四个硬件名里的前三个。
- `TM::PIN_TYPE` / `TM::I_PIN` / `TM::O_PIN` / `TM::IO_PIN` / `TM::DC_PIN` /
  `TM::ALL_DIGITAL` / `PIN_UTILITY::ALPHABETICAL` / `PIN_UTILITY::DEFINITION_ORDER` /
  `PPMU_SETTING` / `PPMU_MEASURE` / `PPMU_RELAY` / `TASK_LIST` / `CONNECT` /
  `FUNCTIONAL_TEST`（**均未建**）— **本篇出现、wiki 里没有页的名字。**

## 版本

原文 `## Functional changes` **只有一条**，逐字：

- `SmarTest 7.2.1: New parameter: getPinType (supported with 7.2.1.1 and higher)`

**这一条不是 §11.2 ② 那个哨兵值**（不是 `Introduced before SmarTest 6.3.2`）——
**它讲的是 7.2.1 加的那个参数（`getPinType`），是一条真版本事实。**

**三条读法：**

1. **`getPinType` 从 7.2.1 起才有**，而且**括注把门槛又推细了一格**：
   `(supported with 7.2.1.1 and higher)`——**即 7.2.1 里还要 `.1` 之后的**。
   **本 wiki 面向 SmarTest 7.10.3，远在门槛之上。**
2. **`PIN_UTILITY` 这个 API 本身什么时候有的，本篇没说**——
   **这一篇的 `Functional changes` 里没有第一条「API 引入」那样的条目，
   也没有哨兵值**（**对照 [[pin-string]] 那篇：它的第一条就是哨兵值**）。
   **所以「本 API 成立于哪个版本」这份语料里没有依据**（见 `## 出处` ②）。
3. **七个函数里只有 `getPinType` 有版本条目。** 另外六个（含两个展开的主力）
   **在本篇的版本段里一个字都没有**——**所以它们早于 7.2.1，还是 7.2.1 里新加的，
   本篇没有说。**

详见 [[smartest-7.2.1]]。

## 出处

`sources:` 一篇：
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.147_PIN_UTILITY.md`
（`70858.htm`，483 行）——**整篇读完**。

**本页做了什么**：

- **整篇读完**（这是本批最长的一篇 raw）。
- **没有读任何别的文档**——本页的事实全部来自这一篇。
- **没有看任何图**（**没有图可看**：本篇 raw 里图片引用 0 处，
  `## Examples` 四段全是代码块）。

**本页没做的**：

- **七个成员函数的签名与参数表都没有进「语法 / 参数」节。** 脚本抽到的段只有四个
  `### Example N`（4,348 字符），**`## Class definition`、`## Member functions`、
  `## Important points`、`## Examples` 的散文一句都没进**。
  **所以本页正文里那七行函数表、两份 `pinType` 取值表、两个 `throw` 开关表、
  `STRING_VECTOR` 那四条运算，全都是本页从原文转述的，不是逐字**；
  **凡加 `>` 的地方才是逐字原文。** 要精确到签名与括号，得回原文。
- **`PinUtility.h` 头文件没读**（它不在语料里，是一个系统路径）——
  **所以七个函数的完整签名（含默认值）、`TM::PIN_TYPE` 与
  `PIN_UTILITY::SORT_ORDER` 的枚举定义，本页只有原文写出来的那部分。**
- **一个函数都没有实跑、没有编译过。** `verified: doc-only` 指的就是这件事。
- **`Pin Configuration tool` / `pin group` / `pin` 三篇都没读** ——
  所以 `pin list` 在配置侧到底是什么形态、组名怎么拼，本页没有。
- **Example 4 里那些 PPMU 对象没读** —— `PPMU_SETTING` / `PPMU_MEASURE` /
  `PPMU_RELAY` / `TASK_LIST` 的 API 本页一个字没有（**它们只是被引用来展示用法的**）。
- **`getPinType` 返回的那几个硬件名（`MCB` / `MCE` / `PS400` / `PS1600` /
  `DCS-DPS128HC` / …）本页没有去任何地方核**——**它们是字符串，不是本页的结论。**
- **没有动 `wiki/index.md`**，也没有把本页挂进 `wiki/stages/pin.md`。

> ⚠️ **本篇的语料瑕疵与对不上的地方，照实记、一处都没替它改**：
>
> **① Example 3 的「打印标签」与「返回串」对不上，而且代码里那一行自己就自相矛盾。**
> 逐字三处：
> ```
> cout << "Pintype of pmu31 is: \"" << PinUtility.getPinType("pmu1") << "\"" << endl;
> ```
> ```
> Pintype of pmu3 is: "DCS-VI32"
> ```
> ——**代码那行的标签写 `pmu31`、传进去的针名是 `pmu1`；而返回串里的标签是 `pmu3`。**
> **同一个针在同一个例子里有三个名字**（`pmu31` / `pmu1` / `pmu3`）。
> **原文没有解释，本页照抄，不替它统一。**
> （**这一处在「语法 / 参数」节里也是这个样子**——那一节逐字抽的就是这些例子。）
>
> **② 版本段没有「这个 API 是哪一版引入的」这一条。** 只有一个 `SmarTest 7.2.1` 条目，
> **讲的是 `getPinType` 这个参数**。**也没有哨兵值。**
> **所以本页不能在「版本」节写「`PIN_UTILITY` 成立于 X 版」**——**语料未写。**
>
> **③ 四个例子里调用 `getDigitalPinNamesFromPinList` 一律只给 4 个实参，
> 而签名是 5 个参数。** 逐字（签名）：
> ```
> const STRING_VECTOR getDigitalPinNamesFromPinList(const STRING& pinList,
>             const TM::PIN_TYPE expectedPinTypes,
>             const BOOLEAN throwErrorOnMissingPinNames,
>             const BOOLEAN throwErrorOnMismatchedPinTypes,
>             const SORT_ORDER sortOrder);
> ```
> ——**签名里 5 个都没有默认值**，而例子里写的是
> `PinUtility.getDigitalPinNamesFromPinList(pinList, TM::IO_PIN, TRUE,TRUE);`
> （**4 个，且第 4 个后面没有第 5 个**）。**两种可能，原文都没排除**：
> **(a) `sortOrder` 在头文件里有默认值**（**头文件不在语料里，本页核不到**）；
> **(b) 例子是旧签名的残留**。**本页两种并列，不判哪个对，也不替例子补第 5 个实参。**
>
> **④ 同一份 `pinType` 例子写了两遍，措辞不一样。** 逐字：
> `` `TM::O_PIN|TM::DC_PIN` will return all output and dc pins. ``（**带反引号，`output and dc`**）
> 与 `TM::O_PIN|TM::DC_PIN will return all "o" and "dc" pins.`（**无反引号，`"o" and "dc"`**）。
> **两处说的是同一件事。本页并列，不替它统一。**
>
> **⑤ `getPinType` 的括注里那四个硬件名，与 Example 3 的返回不是同一批。**
> 正文括注逐字：`(MCB, MCE, PS400, PS1600)`；
> Example 3 返回逐字：`"DCS-DPS128HC"` / `"DCS-DPS128HV"` / `"DCS-VI32"` / `"PS1600"`。
> ——**只有 `PS1600` 一个两边都有**；
> **`MCB` / `MCE` / `PS400` 在返回里一个都没有，`DCS-…` 那三个在括注里一个都没有。**
> **原文没说这两批是什么关系（是同一套名字的新旧两代？还是两个不同的东西？）。**
> **本页并列，不替它判定。**
>
> **⑥ 七个成员函数里，例子只用了两个。**
> `getDpsPinNamesFromPinList` / `getSharedDigitalPins` / `getSharedDpsPins` /
> `createPinListFromPinNames` **在这四段例子（以及全文的其它地方）里一次都没有出现**
> （本页逐字查过：`createPinListFromPinNames` 全文只出现 **3** 次，
> **都是它的标题、清单项与签名那一行**）。**所以那四个函数怎么用，本篇没有例子。**
>
> **⑦ `createPinListFromPinNames` 的参数表指向的是错的例子。** 逐字：
> `See Example 1, below.` ——**而 Example 1 里调的是
> `getDigitalPinNamesFromPinList`，`createPinListFromPinNames` 一次都没出现。**
> **两者的说明文字确实对得上**（`createPinListFromPinNames` 的说明里举的
> `pin1, pin2, and pin3 → "pin1,pin2,pin3"`，正是 Example 1 打印出来的内容），
> **但那一段代码里没有这个函数。本页照实指出，不替它改指针。**
> （**对照 `getPinType` 的 `See also Example 3 below.` 是对的**——Example 3 确实用了它。）
>
> **⑧ 参数名在签名与参数表之间不一致。** 逐字：
> 签名是 `const BOOLEAN ignoreMissingPinNames)`，
> **而参数表那一行的小标题是 `ignoreMissingPins`**（**少了 `Names`**）。
> **同一份文档里两种写法。本页在正文里两个都写出来，不替它统一。**
> **同类还有一处**：`getDigitalPinNamesFromPinList` 签名里的参数叫 `expectedPinTypes`，
> **而参数表那一行的小标题是 `pinType`**（**与弃用那个函数的参数名相同**）。
>
> **⑨ `## Class definition` 一节的结构是残的。** 逐字：
> ```
>   Constructor This class has no public constructor.
>
> To use the PIN_UTILITY API, you must always use the system-prepared class object PinUtility. You cannot create any object of this class.
>
>  Member functions
>
> - [expandDigitalPinNamesFromPinList()](<…>)
> ```
> ——**`Constructor` 是裸词开头、后面直接跟句子**（没有冒号、没有列表符），
> **`Member functions` 那一行行首多一个空格、也不是标题**（在 markdown 里会被当成段落续行）。
> **而后面的 `## Member functions`（带 `##`、同样两个词）才是真标题。**
> **所以同一份文档里 `Member functions` 出现两次、一次是裸行、一次是标题。**
> **本页照实说，不替它补 `##`。**
>
> **⑩ `## Member functions` 里每个函数的「小标题」是坏掉的表格残留。** 逐字（例）：
> ```
>    |  getDigitalPinNamesFromPinList()
> ```
> ——**行首三个空格 + 一个裸 `|` + 两个空格，然后才是函数名**（**不是 `###` 标题**）。
> **本页数过：七个函数条目里只有三个（`getDigitalPinNamesFromPinList` / `getDpsPinNamesFromPinList` /
> `getPinType`）带这个 `   |  ` 前缀；另外四个不带**——
> 其中 `expandDigitalPinNamesFromPinList()` 是**行首两个空格**
> （`  expandDigitalPinNamesFromPinList()`），
> 而 `getSharedDigitalPins()` / `getSharedDpsPins()` / `createPinListFromPinNames()`
> 是**行首一个空格**（` getSharedDigitalPins()`）。
> **所以同一节里有三种行首形态。本页照实说，不替它删竖线、不替它补标题、也不替它统一缩进。**
> （**参数表本身也是同一族毛病**：一格一行、被空行与裸 `|` 隔开——
> 与 [[dscp]] / [[uptd]] / [[dc-scale-limits-editor]] 几篇的表格残破同形。）
>
> **⑪ Example 4 的注释里有四处笔误，逐字记下、一处都没改：**
> - `*This section will executed only once.` —— **`will` 后面少一个 `be`。**
> - `The results of all sites are cashed in the measrement objects.`
>   —— **`cashed` 应为 `cached`、`measrement` 应为 `measurement`**（**同一句里两个错**）。
> - `There is not .setup() API needed because the values will NOT change during`
>   —— **`not` 应为 `no`。**
> - **同一个注释用了两次，第二次还指的是另一段代码**：两处都是
>   `//Get Results and Datalog from Group leak_pins1`，
>   **而第二处底下那段代码调的是 `PinUtility.getDigitalPinNamesFromPinList("leak_pins2", …)`**
>   ——**注释写 `leak_pins1`、代码用 `leak_pins2`**（**典型的复制粘贴残留**）。
> **本页照抄，不替它改。**
>
> **⑫ 例子里打印的标签用 `Pintype`（小写 `t`），而函数名是 `getPinType`（大写 `T`）。**
> 逐字：`cout << "Pintype of dps1 is: \"…` ——**同一个词在一行里两种大小写。**
> **本页照抄。**
>
> **⑬ §11.2 ① 那种编码损坏本篇没有。** 本页查过：**本篇只有 ASCII**——
> CJK 字符 0 个、U+00A0 0 个、`鈥` 0 个、`鈭` 0 个。
> **§11.2 ⑤ 那个整词替换（`DC/DC power units`）本篇 0 命中。**
> （**注意本篇里有 `DCS-VI32` 这种正常名字，与 `DC/DC` 那一族无关——本页没有误判。**）

`verified: doc-only`
