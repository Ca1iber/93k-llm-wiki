---
type: object
title: TMLimits
layer: L2
stage: testmethod
tags: [tmlimits, limit, csv, test-number, testflow, smc, v93k-limits, limitinfo, test-method]
related: [limit, structure-of-a-tmlimits-csv-file, testflow, testflow-variable, testset, test-program-explorer, testmethod, bin]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.250_TMLimits.md
created: 2026-09-18
updated: 2026-09-20
verified: doc-only
---

# TMLimits

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **4,071 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.250_TMLimits.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example 1: Declare namespace

To use the TMLimits API, you need to declare the using of V93kLimits namespace in your test method:

```
using namespace V93kLimits;
```

### Example 2: Setting the test mode and performing a test

```
tmLimits.setTestMode("FT");
TestSet.TEST("pinName", "myTestName", tmLimits, 4);
```

### Example 3: Performing a test for testflow using multibin

Use

```
TestSet.cont(true).TEST("DC_Test", "myTestName", tmLimits, mLim1);
```

instead of

```
TestSet.cont(true).TEST("DC_Test", "myTestName", tmLimits.getLimitObj("myTestName"), mLim1);
```

### Example 4: Using the test table bins

Test table bins with TMLImits support different bins for one test suite.

Several tmLimits API calls remember the first failing bins, see Behavior example in `TESTSET().judgeAndLog_ParametricTest()`（raw: `02.07.04.01.244.10_TESTSET__.judgeAndLog_ParametricTest.md`）.

Requirements:

- Testflow: Multibin icon in the fail branch of test suite
- Test table: Bins of the corresponding limit keys are defined

```
TESTSET().cont(true).judgeAndLog_ParametricTest(pin, <testname>, , V93kLimits::tmLimits, <singlevalue>);
```

### Example 5: Accessing a value from LimitInfo

This code reads the limits from the test "myTestName" of the current test suite into a LimitInfo struct and retrieves the value for the units, storing it in a string variable.

```
using namespace V93kLimits;

string sTestsuiteName;
GET_TESTSUITE_NAME( sTestsuiteName );
string sTestName = "myTestName";

TMLimits::LimitInfo strLimitInfo;
strLimitInfo = tmLimits.getLimit( sTestsuiteName, sTestName );
string sTestTableTestModeUnit = strLimitInfo.Units;
```

### Example 6: Changing the values of a TMLimits object

```
LimitInfo& MyInfo = tmlimits.getLimit(testsuiteName, testname);
MyInfo.Lsl = 4;
```

This example creates a reference to a `LimitInfo object`（raw: `02.07.04.01.250_TMLimits.md#_110432__LimitInfo`） for the specified testsuite and test, and changes the `Lsl` value of the object to 4. Note that a reference is needed for this to work.

### Example 7: Using the lookup key to manually retrieve the limit with getLimitRef()

```
STRING_VECTOR string_vector_odd;
PPMU_MEASURE ppmu_measure_odd;
DOUBLE resultValue = 0.0;
//test setup and execution
....
//get the limit with the Limit key of ContactShort
tmLimits.setLookupKey("Limit key");
TMLimits::LimitInfo limitInfoContactShort = tmLimits.getLimitRef("ContactShort");
for (int i = 0; i < string_vector_odd.size(); i++)
{
    if (string_vector_odd[i] == "BBIOI_N_ch0")
    {
        //get the limit with the Limit key of ContactShort and with the pin of BBIOI_N_ch0
        tmLimits.setLookupKey("Limit key:Pins");
        TMLimits::LimitInfo limitInfoContactShortPin = tmLimits.getLimitRef("ContactShort:" + string_vector_odd[i]);
        resultValue=ppmu_measure_odd.getValue(string_vector_odd[i]);
        TestSet.cont(true).testnumber(limitInfoContactShortPin.TestNumber).judgeAndLog_ParametricTest(string_vector_odd[i],"Contact_Short",limitInfoContactShortPin.TEST_API_LIMIT, resultValue);
    }
    else
    {
        resultValue=ppmu_measure_odd.getValue(string_vector_odd[i]);
        TestSet.cont(true).testnumber(limitInfoContactShort.TestNumber).judgeAndLog_ParametricTest(string_vector_odd[i],"Contact_Short",limitInfoContactShort.TEST_API_LIMIT, resultValue);
    }
}
```

### Example 8: Using the lookup key to automatically retrieve the limit in judgeAndLog_ParametricTest()

```
tmLimits.setLookupKey("Test number");
// use the limit with the test number of 555:
TESTSET().testnumber(555).judgeAndLog_ParametricTest("io1","test12",tmLimits,-12);
tmLimits.setDefaultLookupKeys();
// use the limit with the Pins of "io1" and with the Test name of "test12"
TESTSET().judgeAndLog_ParametricTest("io1","test12",tmLimits,-12);
```

### Example 9: Limiting displayed warnings when loading a limits file.

This example shows all available parameter. However, it will suppress duplicate test numbers.

```
virtual void run()
{
    ON_FIRST_INVOCATION_BEGIN();

        tmLimits.setLookupKey("Test number:Limit_type");
        cout << "default usage" << endl;
        tmLimits.load();

        // use this to re-/set to default
        // tmLimits.load(TM::LIMIT_DEFAULT_WARNING);

        // use this to suppress duplicate key warnings
        // tmLimits.load(TM::LIMIT_NO_DUPLICATE_KEY_WARNING);

        // use this to suppress duplicate test number warnings
        tmLimits.load(TM::LIMIT_NO_DUPLICATE_TEST_WARNING);

        // use this to suppress all warnings
        // use this carefully!
        // tmLimits.load(TM::LIMIT_DEFAULT_WARNING);

    ON_FIRST_INVOCATION_END();

    return;
}
```

<!-- 语法节 end -->

## 是什么

**一句话：TMLimits 是一套 C++ API（命名空间 `V93kLimits`），让 testflow 从一张 CSV 表里取「限值」和「测试编号」。** 原文第一句：

> 「The TMLimits class lets you control limits and test numbering in your testflow with data from a CSV file.」

**限值和测试编号本来长在测试程序里，TMLimits 把它们挪到程序外面的一张表里。** 原文给了两个理由：

> 「You can easily switch between different testing modes or stages in the same testflow for different situations. For example, you can use a looser set of limits for wafer testing and a tighter one for quality control. These modes or stages are selected using the load() function.」

> 「The settings in the CSV file can be easily edited even without access to SmarTest, for example, using Open Office Calc or a standard text editor. This allows you to make adaptations on the fly.」

**两条理由合起来就是这个类的定位**：**一套 testflow + 多套限值，切换靠「测试模式（test mode / test stage）」**；**而且改限值不需要开 SmarTest**（原文举的编辑器是 Open Office Calc 或普通文本编辑器）。**这也是它唯一的卖点**——原文没有给任何别的用途。

### 没有构造函数，只有系统准备好的那一个对象

原文写得非常直：

> 「There is no constructor available for this class. You cannot create any object of this class:」

> 「To use the TMLimits class, you must always use the system-prepared class object tmLimits.」

**所以 `tmLimits` 这个对象名是固定的**，不是你 `new` 出来的变量名——**文档里所有例子都直接写 `tmLimits.xxx()`**。用之前还要声明命名空间（Example 1）：

```
using namespace V93kLimits;
```

**头文件路径原文照抄**：

> 「This API is defined in the header file /opt/hp93000/soc/prod_com/include/MAPI/TMLimits.h.」

**注意路径里还是 `hp93000`**（HP/Agilent 时代的目录名）。**原文照写，本页照抄，不解释。**

### 12 个成员函数

原文的成员函数清单有 12 条，其中 `getInstance()` 自己注明 `This function is used for internal purposes only.`。**取限值的三条路，签名逐字照抄**（这三段的签名**不在本页「语法 / 参数」节里**，见「出处」）：

```
LimitInfo& getLimit(const std::string& key);
LimitInfo& getLimit(const std::string& testSuiteName, const std::string & limitParamName);
LimitInfo& getLimit(const std::string& testSuiteName, const std::string & limitParamName, const std::string & pinName);
LimitInfo& getLimit(const std::string& testSuiteName, const std::string & limitParamName, const std::string & pinName, int testNumber);
```

```
const LimitInfo& getLimitRef(const string& key)
const LimitInfo& getLimitRef(const string& testsuite, const string& testname, const string& pin = "", int testnumber = -1, int sbin = -1)
```

```
LIMIT& getLimitObj(const string& LimitParamName)
LIMIT& getLimitObj(const string& LimitParamName, const string& PinName)
```

```
int load()
int load(const string& limitfile)
int load(const string& limitfile, const string& mode)
int load(TM::LIMIT_WARNING_LEVEL = TM::LIMIT_DEFAULT_WARNING)
```

**两条路返回的是 `LimitInfo`（结构），第三条返回的是 `LIMIT` 对象**——**`LIMIT` 和 `LimitInfo` 在原文里是两个不同的东西**，第三条路的 caveat 就出在这里（见下面 multibin）。其余 8 个签名也是逐字：

| 函数 | 签名（原文逐字） | 原文说它干什么 |
|---|---|---|
| `clear()` | `void clear()` | 「Clears all values from the limit table in the TMLimits object.」 |
| `getInstance()` | `static TMLimits& getInstance()` | 「This function is used for internal purposes only.」 |
| `setTestMode()` | `int setTestMode(const string& mode)` | 「Sets the test mode for the TMLimits object.」 |
| `getTestMode()` | `string getTestMode();` | 「This function returns the currently configured test mode.」 |
| `loadOnDemandAndReturnStatus()` | `bool loadOnDemandAndReturnStatus();` | 「returns whether a test table exists and can be loaded or is already loaded」 |
| `setLookupKey()` | `void setLookupKey(const std::string& lookupkey);` | 「Sets the key(s) to look up for a limit in the test table.」 |
| `setDefaultLookupKeys()` | `void setDefaultLookupKeys();` | 「Reset the lookup keys of the test table.」 |
| `getLookupKey()` | `const std::string& getLookupKey();` | 「Returns the current lookup key.」 |

**`loadOnDemandAndReturnStatus()` 的返回规则是原文唯一写全了的三分支**：

> 「- If a test table is already loaded in the test method or in the Test Program Explorer, true will be returned.」
> 「- If a test table exists and is used in the testflow but not loaded, the function will load the test table and return true.」
> 「- If no test table exists or a test table exists but not loaded and not used in the testflow, false will be returned.」

### `TMLimits::LimitInfo` 里装什么

原文：**「TMLimits::LimitInfo is a struct for limit data:」** 24 个字段。**分四组记**（括号里是原文的类型）：

- **身份**：`SuiteName` / `TestName` / `PinName`（`string`）、`TestNumber`（`int`）
- **限值本身**：`Lsl` / `Usl`（`double`，上下规格限）、`LslTyp`（「The type of lower limit: GT, GE, or NA」）、`UslTyp`（「The type of upper limit: LT, LE, or NA」）、`Units`（`string`）、`OffSet`（「A value that is added to the test results before they are compared to the limits」）
- **分选与判 PASS 区**：`PassRegion`（「The pass region, used for part average testing: L, I, H, or X」）、`BinhNum` / `BinhName`（硬件 bin）、`BinsNum` / `BinsNumString` / `BinsName`（软件 bin）、`Exec`（「Whether this test is to be executed (Y) or not (N)」）
- **接回 SmarTest 与自定义列**：`TestRmrks`、`TEST_API_LIMIT`（原文注 `[LIMIT]`：「The SmarTest object for this test」）、`ParamString`（`map <string, string>`）、`ParamDouble`（`map <string, double>`）——后两个原文说是「for accessing user-defined columns」

**这张表和 CSV 是一对一的关系**，原文只给了一句话：

> 「Most of the elements of LimitInfo correspond to columns in TMLimits CSV files.」

**注意「Most of」**——**原文没有说哪几个不对应**，本页也不猜。

### 测试模式：两条路，谁生效看「改动史」

**这一段是整篇最绕的，也是用错一次就会跑错限值的地方。** 原文给了两条设置路径：testflow 变量 `TMLimit_TestMode`，或者成员函数 `setTestMode()` / `load(<limitfile>,<mode>)`。哪个生效：

> 「Which setting is actually valid (which can be checked with the getTestMode() member function) depends on the change history of both access methods.」

**变量这条路要同时满足两条才会生效**：

> 「Generally, the test mode of the testflow variable becomes valid if the following two conditions are both satisfied:」

> 「- One of the following member functions of TMLimits is called: getLimit(), getLimitRef(), getLimitObj() / load() (without parameters!).」
> 「- The current value of the variable is different from the value it had at the last call of one of these member functions or of setTestMode().」

**成员函数那条路的规则正好相反，简单得多**：

> 「In contrast, if the test mode is set with one of the member functions, the specified test mode becomes valid always and immediately, even if the value of the actual call equals that of the last call.」

**（推断）所以「用变量」比「用函数」脆**——依据上面两条的对比：函数是「写一次就生效」，变量是「值变了才算」，**而且变了之后还要有一次取限值的调用才会被看到**。**原文没有把这条写成警告，是本页从两条规则的差异里读出来的。**

**这个行为还跨多次 testflow 执行**，原文专门用一整段说：

> 「Note that this behavior holds across multiple test flow executions. If the variable is set and the testflow is executed for the first time, then its value will be the valid test mode until the first change of the test mode within the testflow. But if the testflow is executed repeatedly, the initial test mode of the later executions will depend on whether the initial value of the testflow variable is different from its value at the end of the previous execution. If it is, the value of the testflow variable will be the initial valid test mode of the actual execution. If it is not, the test mode that was valid at the end of the previous execution will be used as the first test mode of the actual execution.»

**换句话说：第二轮起的初始模式取决于「上一轮结束时是什么模式」**——**这是状态残留，不是每轮重新初始化。原文写得很清楚，但读起来要转三个弯。**

### 在 SMC 框架里用 TMLimits 的三条硬规矩

原文开头就点名了前提（`Four-step SmartCalc implementation`，**本页没读**），然后给三条：

> 「- The functions getLimit(), getLimitRef(), and getLimitObj() for retrieving data from the TMLimits table are threadsafe.」

**这一条解释了为什么 `getLimit()` 的内部对象是「每线程一个」**：原文说内部 `LimitInfo`（以及 `getLimitObj()` 的内部 `LIMIT`）「is available once per thread, meaning there is one object for the main thread of SmarTest and one more internal LIMIT object for each SMC background thread」，**且「Multiple calls of this function within one thread refer always to the same internal LimitInfo object」**——**所以取到之后必须马上用掉，或者自己拷一份**：

```
TMLimits::LimitInfo limitInfo_1 = tmLimits.getLimit("testSuite_1","test_1");
TMLimits::LimitInfo limitInfo_2 = tmLimits.getLimit("testSuite_1","test_2");
```

**第二条是顺序要求**，原文连例子一起给：

> 「- Ensure that the TMLimits table is loaded into the memory before calling SMC_ARM(), for example:」

```
tmLimits.load("tmuVerify_limits.csv");
SMC_ARM(XXX);
```

**第三条是 CAUTION，语气最重**：

> 「- Ensure that all required settings are done before an SMC background process is armed. CAUTION You must not change or reload a TMLimits table while an SMC background process is armed or running. Violating this rule may result in invalid data or the crash of the test method.」

## 典型用法

> **原文的 `## Examples` 九段已经逐字收在本页「语法 / 参数」节里**（4,071 字符）。
> **本节不重抄那九段代码，只写「什么条件下走哪一条」。**

**0. 先声明命名空间**（Example 1）：`using namespace V93kLimits;`——**原文说这是「To use the TMLimits API」的前提**。

**1. 决定表怎么进来。** `load()` 有三个入口，区别只在「文件名和模式从哪来」：

| 调用 | 原文 | 模式取谁 |
|---|---|---|
| `load()` | 「If you call load() without any parameters, it uses the TMLimit_FileName testflow variable to determine the file to load and the current value of the TMLimit_TestMode variable for the desired mode.」 | `TMLimit_TestMode` 变量（**且受上面那两条条件限制**） |
| `load(<file>)` | 「it loads the specified file and uses the mode "Default". With the "Default" test mode, the first test mode occurring in the specified test table is selected.」 | 表里出现的第一个 mode |
| `load(<file>,<mode>)` | 「it loads the specified file and sets the specified mode.」 | 你给的那个 |

**文件放哪儿是硬约束，不看这张表就会找不到文件**：

> 「The specified name can include a path, which must be relative to the testtable/ directory within the current device directory. If just a file name is given, the file must be located in the testtable/ directory.」

**mode 是什么，原文的定义是开放的**：

> 「A TMLimits CSV file can contain multiple versions of any of the parameters (such as upper and lower test limits) except the key columns, with each version being assigned to a test mode. Test modes can also be specified for user-defined columns.」
> 「These modes, such as quality assurance, are user definable; a CSV file can include an unlimited number of modes.」

**2. 决定测试怎么拿到限值。** 两条路，原文都给了例子：

- **整表直接喂给测试函数（原文明说推荐）**：Example 3 的 `TestSet.cont(true).TEST("DC_Test", "myTestName", tmLimits, mLim1);`，原文说的替代对象是 `...tmLimits.getLimitObj("myTestName")...`。
- **自己先取一个限值对象**：`getLimit()` / `getLimitRef()` / `getLimitObj()`——**取到的东西是「每线程一份的内部对象」，不是拷贝**（见上）。

**`getLimitObj()` 配 multibin 是个陷阱，原文专门写了一段**：

> 「This function sets multibin to the values contained in the TMLimits object. If multibin is used in the testflow, do not use getLimitObj() to access the TMLimits object. Instead, use getLimit() or, if you use a judgeAndLog_xxx or TEST() function, use a variant that directly accesses TMLimits (instead of through a member function).」

**性能上，原文两次点名 `getLimitRef()`**：

> 「Note For performance reasons, we recommend that you use getLimitRef(), described below, instead of this function unless you want to modify the test limits it returns.」

> 「This function is significantly faster than getLimit() and should be preferred. If you do not need to modify the LimitInfo object, use this function for maximum performance.」

**代价是它返回 `const`，改不了**——**要改就得自己拷一份，而原文说拷这一下就「needs about the same amount of test time as getLimit()」**，等于把性能优势还回去了。**这是本页看到的最实用的一条取舍。**

**3. 决定怎么定位到「哪一行的限值」——lookup key。** Example 7（手动）和 Example 8（自动）演示了同一件事的两面：

> 「To retrieve the limits with getLimitRef(), you can specify any combinations of columns in the test table as the lookup key.」

> 「To directly use the tmLimits as an input parameter of TESTSET().judgeAndLog_ParametricTest(), only the combinations of Suite name, Test name, Pins or Test number can be used as the lookup key.」

**默认的 lookup key 是四选一**，原文列的是：

> 「- Suite name, Test name, Pins」「- Suite name, Test name」「- Limit key, Pins」「- Limit key」

**4. 找不到限值会直接报错，不是静默跳过**：

> 「If there is a Pins column in the limits but no test matches pin, the execution will lead to an error:」
> 「Error: no limit found for testsuite=..., testname=..., pin=..., testnumber=...」

**pin 的匹配规则原文写了两条**：匹配上就返回（**「This includes tests where the Pins column contains a pin group that includes pin.」**——**pin group 也算**），以及**「If no Pins column exists, pin is ignored.」**

**5. 加载时压掉警告。** Example 9 给的是 `load(TM::LIMIT_NO_DUPLICATE_TEST_WARNING)` 这一类；可选的四种原文列在参数节：`LIMIT_DEFAULT_WARNING`（默认，全部输出）、`LIMIT_NO_DUPLICATE_KEY_WARNING`、`LIMIT_NO_DUPLICATE_TEST_WARNING`、`LIMIT_NO_WARNING`。**注意 `LIMIT_NO_WARNING` 那条原文自己带了警告**：

> 「Use this with caution, because no warnings will be displayed at all.」

**6. 在 SMC 里用，顺序不能错**：先把表 `load()` 进内存，再 `SMC_ARM()`；**armed 或 running 期间不许换表、不许重载**（CAUTION 原文见上）。

## 和谁有关

- [[structure-of-a-tmlimits-csv-file]] — **表的结构页**。原文两处把 `LimitInfo` 的字段指回 CSV 的列：
  「Most of the elements of LimitInfo correspond to columns in TMLimits CSV files.」
  **两页是「谁读」↔「读的东西长什么样」**
- [[limit]] — **`getLimitObj()` 返回的那个 `LIMIT` 对象的页面**。原文的 `TEST_API_LIMIT` 字段类型也是 `[LIMIT]`
- [[testflow-variable]] — **`TMLimit_FileName` 和 `TMLimit_TestMode` 两个变量的宿主**。
  **这两个变量名是 `load()` 无参版本的全部输入**，**但它们「在哪声明、怎么写」本页没有**（原文没写）
- [[testflow]] / [[test-suite]] — 本页 `stage: testmethod` 上游的两个阶段页；
  原文的「test number」「test suite name」都是 testflow 语境里的词
- [[testset]] — **`TESTSET().judgeAndLog_ParametricTest()` 是直接吃 `tmLimits` 的那一族函数**；
  **原文说 lookup key 的限制正是为这条用法设的**
- [[test-program-explorer]] — **表的来源之一**：`loadOnDemandAndReturnStatus()` 的三分支里两次点名它；
  原文还说表格式是「files written by saving the test table from the test program explorer」
- [[device-directory]] — **`testtable/` 是「相对当前 device directory」的**，文件找不到时先查这里
- [[bin]] — `LimitInfo` 里的 `BinhNum` / `BinsNum` 一族，和 Example 4 的 test table bins
- [[testmethod]] — **调用方**：所有例子都写在 test method 的 `run()` 里（Example 9 明写 `virtual void run()`）
- [[smc-background-process-locks-config]] — **SMC 背景进程那一段的邻居话题**（**本页没读那篇，不主张具体关系**）
- `TEST()` / `TESTSET()` / `TESTSET().judgeAndLog_ParametricTest()` / `SMC_ARM()` / `LIMIT` / `Four-step SmartCalc implementation` / `Test Number Generator and TMLimits` / `Saving test numbers as TMLimits CSV files` — **原文里的链接目标**，**除 [[limit]] 外本页都没读**（raw: `02.07.04.01.241_TEST.md`、`02.07.04.01.244_TESTSET.md`、`02.07.04.01.244.10_TESTSET__.judgeAndLog_ParametricTest.md`、`02.07.04.01.231.01_SMC_ARM.md`、`02.07.04.01.126_LIMIT.md`、`02.07.10.04.03_Four-step_SmartCalc_implementation.md`、`02.10.01.08.01_Test_Number_Generator_and_TMLimits.md`、`02.10.01.08.01.01.03_Saving_test_numbers_as_TMLimits_CSV_files.md`）

## 版本

原文有 `## Functional changes` 段，**12 条，全部照抄**：

- **Introduced in SmarTest 6.5.0**
- SmarTest 6.5.1: dump() function removed
- SmarTest 6.5.1: load() can now be called without parameters
- SmarTest 6.5.1: New function setTestMode()
- SmarTest 6.5.3: New function getTestMode()
- SmarTest 7.1.4: New function getLimitRef()
- SmarTest 7.1.4: New function setLookupKey()
- SmarTest 7.1.4: New function setDefaultLookupKeys()
- SmarTest 7.1.4: New function getLookupKey()
- SmarTest 7.1.4: New member function loadOnDemandAndReturnStatus()
- SmarTest 7.2.0: The sbin and testnumber parameters are evaluated
- SmarTest 7.3.4: New parameters for the load member function: LIMIT_WARNING_LEVEL

**三条值得单独说**：

1. **`Introduced in SmarTest 6.5.0` 是真的版本号，不是哨兵值。** 它写的是 `in`，不是
   `Introduced before SmarTest 6.3.2` 那种「本文档集覆盖之前就有」的说法（schema §11.2 ②）。
   **所以「TMLimits 从 6.5.0 起可用」是可以照字面用的。**
2. **6.5.1 删掉了一个函数 `dump()`。** 原文的成员函数清单里没有它，**九个例子里也没有它**——
   **也就是说：语料里只有「它没了」这一句，从来没有过「它是什么」。**
3. **7.1.4 一口气加了 5 个函数**（`getLimitRef()` / `setLookupKey()` / `setDefaultLookupKeys()` /
   `getLookupKey()` / `loadOnDemandAndReturnStatus()`）——**本页正文里「lookup key」那一整块用法、
   以及「性能上优先用 `getLimitRef()`」这条建议，全部是 7.1.4 之后才存在的。**
   **7.1.4 之前的程序里这两样都没有。**

**7.1.4 → 7.3.4 之间文档还有一次行为变更**（7.2.0 `sbin` / `testnumber` 参数才开始被求值）——
**照字面读：7.2.0 之前这两个参数写在调用里也不起作用。**

## 出处

`sources:` 一篇：

`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.250_TMLimits.md`
（TDC `110432.htm`，共 631 行）

**本页没做的**：

- **只读了这一篇。** 本页正文里每一个事实都出自这 632 行。
- **原文里 8 个链接目标全部没读**：`TESTSET()` / `TEST()` /
  `TESTSET().judgeAndLog_ParametricTest()` / `SMC_ARM()` / `LIMIT` /
  `Four-step SmartCalc implementation` / `Test Number Generator and TMLimits` /
  `Saving test numbers as TMLimits CSV files`。
  **所以「怎么用 `judgeAndLog_ParametricTest()` 把 `tmLimits` 传进去才算对」
  本页只有原文那一句 lookup key 的限制，没有函数那一侧的说明。**
- **`Structure of a TMLimits CSV file` 那篇没读**——**本页知道「字段大多对应列」，
  但列名怎么写、一行长什么样、`testtable/` 目录下还有哪些文件，本页一概没有。**
- **`TMLimit_FileName` / `TMLimit_TestMode` 两个 testflow 变量的声明方式没读**
  （原文没写，指向 `testflow variable` 的话题）。
- **没有实测**：本页没有写过一行 `V93kLimits` 代码，没有打开过任何 CSV，
  没有在机台上跑过 `load()` / `SMC_ARM()` 的顺序。
  **「设错测试模式会跑错限值」这句话的后果，本页是照规则推的，不是验的。**
- **原文没有一张图**，本页没有任何来自图的结论。
- **「语法 / 参数」节里是九段例子，不是签名表。** 脚本这一节抽到的是原文的 `## Examples`
  （4,071 字符）。**12 个成员函数的签名和 `LimitInfo` 字段表在原文里都没有段标记，
  脚本一个字都没收**——**所以本页在「是什么」里照抄了签名并逐字引了字段说明，
  否则这个页面会没有任何 API 形状。这是文档事实的搬运，不是我的转述（§11）。**

> ⚠️ **本篇的语料瑕疵，照实记，一处都没替它改**：
>
> ① **`confirm` / `conform` 混用**：
> `The file must confirm to the TMLimits data format, such as files written by saving the test table from the test program explorer.`
> ——**应为 `conform`。本页照抄，不替它改。**
> ② **`will not been found`（应为 `will not be found`），同一句在一篇里出现两次**：
> `Otherwise the test defined by limitParamName will not been found in the limit table.`
> ——一次在 `getLimitObj()` 的参数节，一次在紧随其后的正文里。**逐字相同，两处都错。**
> ③ **`in the type of string`**（`BinsNumString` 那格）：
> `The software bin number for failed tests in the type of string.`
> ——**常见写法是 `as a string`。本页照抄，不判对错。**
> ④ **成员函数清单里 `setDefaultLookupKeys` 唯独没有 `()`**：
> 上一条是 `setLookupKey()`、下一条是 `getLookupKey()`，**夹在中间的它写作 `setDefaultLookupKeys`。**
> **正文和 `## Functional changes` 里它都带 `()`，只有清单这一处不带。**
> ⑤ **两处空的项目符号**：`getLimit()` 和 `getLimitRef()` 的参数说明里各有一处，
> 形态是「一个 `-` 后面什么都没有」——
> `- If a test matching pin (and the other provided parameters) is found, the corresponding limits are returned. This includes tests where the Pins column contains a pin group that includes pin.`
> `-`
> **这一处看起来是原文 HTML 里一个空 `<li>` 落成的。本页不补内容。**
> ⑥ **Example 9 的最后一条注释和代码对不上，而且和上一段自相矛盾**：
> 上面写 `// use this to re-/set to default` 后面跟 `// tmLimits.load(TM::LIMIT_DEFAULT_WARNING);`，
> 下面写 `// use this to suppress all warnings` `// use this carefully!` **后面跟的却还是**
> `// tmLimits.load(TM::LIMIT_DEFAULT_WARNING);`。
> ——**按参数节的说明，「压掉所有警告」对应的是 `LIMIT_NO_WARNING`，而 `LIMIT_NO_WARNING`
> 在九个例子里一次都没出现过。同一个调用，两种相反的注释。照实记，不替它改。**
> ⑦ **Example 6 里类对象写成小写**：
> `LimitInfo& MyInfo = tmlimits.getLimit(testsuiteName, testname);`
> ——**`tmlimits`，而原文别处一律是 `tmLimits`（大写 L）。**
> ⑧ **`load()` 的四个重载里有两个能零参数调用**：
> `int load()` 与 `int load(TM::LIMIT_WARNING_LEVEL = TM::LIMIT_DEFAULT_WARNING)`
> ——**后者带默认参数。原文说「There are three ways to specify the desired file」，
> 但列了四条签名，也没说 `load()` 会解析到哪一条。**
> **（推断）这是文档没说清，不是编译不过**——依据只有原文这两行本身，**本页没有验证过。**
> ⑨ **`This example shows all available parameter.`**（Example 9 的引子）
> ——**应为 `parameters`。**
> ⑩ **格式：小标题被压成带前导空格的行**，例如 `  Constructor`、`  Member functions`、
> ` TMLimits::LimitInfo`、`  clear()`、`  load()`、` setLookupKey()`。
> **原文的层级在转 markdown 时丢了**，于是 `clear()` 这种函数名和 `Member functions` 这种节名
> 长得一样。**同一处还有个后果**：参数表把「Return value」的说明吞进了单元格，例如
> `| testsuite  | The name of the test suite that contains the described test.  |   Return value A reference to an internal ...`。
> **本页照实引，不重排。**
> ⑪ **同一张 `LimitInfo` 表里类型大小写不一致**：`Lsl` / `Usl` 是 `double`，
> 而 `OffSet` 是 `DOUBLE`；字段名 `OffSet` 的驼峰也和 `Lsl` / `Usl` 不同风格。
> **照实记，不替它统一。**
> ⑫ **硬件 bin 的字段名是 `BinhNum` / `BinhName`**（说明写的是 `The hardware bin number for failed tests`），
> 软件 bin 是 `BinsNum` / `BinsName`。**`Binh` 是不是 `BinH` 的笔误，原文没有第二处可对照，
> 本页不判。**
> ⑬ **同一篇里 testset 有两种写法**：Example 2 / 3 / 6 用 `TestSet.cont(true).TEST(...)`，
> Example 4 / 7 / 8 用 `TESTSET().judgeAndLog_ParametricTest(...)`。
> **两种都照抄，本页不判哪个是规范写法。**
> ⑭ **Example 7 在循环里反复调 `setLookupKey()`**（先 `"Limit key"`，循环内改成 `"Limit key:Pins"`），
> **而 lookup key 是全表级的设置，`if` 分支改过之后不会再改回来。**
> **本页只记这个结构，不判它对错**——原文没有解释这个例子为什么要这样写。

`verified: doc-only`
