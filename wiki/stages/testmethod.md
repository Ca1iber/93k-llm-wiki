---
type: stage
title: Test Method — 编写 C++ 测试方法（UTM）并编译出测试方法库
tags: [testmethod, utm, test-method-api, cpp, utm-library, multisite]
related: ["[[project]]", "[[pin]]", "[[level]]", "[[timing]]", "[[testflow]]", "[[run]]"]
sources:
  - 01_Getting_started/01.06_Test_methods/01.06.01_Test_Method_Introduction.md
  - 01_Getting_started/01.06_Test_methods/01.06.02.01_1._Create_a_Test_Method_Project.md
  - 01_Getting_started/01.06_Test_methods/01.06.02.02_2._Create_a_Test_Method_Class.md
  - 01_Getting_started/01.06_Test_methods/01.06.02.03_3._Add_the_source_code.md
  - 01_Getting_started/01.06_Test_methods/01.06.02.04_4._Build_the_project_to_get_the_universal_test_method_library.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.01_Introduction.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.02_Universal_Test_Method.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.02.02.01_How_to_create_a_universal_test_method_project.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.02.02.02_How_to_create_a_universal_test_method_class.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03_Test_Method_Programming_Essentials.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.02_DC_Test_Programming.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.10_Executing_Firmware_Commands.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.13_Controlling_Multiple_Sites.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.17_How_to_handle_the_API_fatal_errors.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04_API_Reference.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.70_FOR_EACH_SITE_BEGIN.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.88_GET_FUNCTIONAL_RESULT.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.97_GET_TEST_FOCUS.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.126_LIMIT.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.138_ON_FIRST_INVOCATION_BEGIN.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.231.01_SMC_ARM.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234_SPMU_TASK.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.241_TEST.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244_TESTSET.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.250_TMLimits.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.18_EVENT_VALUE_DOUBLE.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.05_Test_Method_Library.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.06_Test_method_snippets_provided_with_SmarTest.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.09_d2s-framework.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.10_SmartCalc_framework.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.11_Protocol_Aware_ATE.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.12_Offline_Result_Emulation.md
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13_SmartRDI.md
  - 02_System_reference/02.06_Command_Reference/02.06.09_AC_Testing_Commands.md
  - 02_System_reference/02.06_Command_Reference/02.06.10_DC_Measurement_Commands.md
  - 02_System_reference/02.06_Command_Reference/02.06.13_Commands_for_the_TMU_per_pin.md
  - 02_System_reference/02.06_Command_Reference/02.06.17_Commands_for_PRBS_per_pin_tests_and_loopback_tests.md
  - 02_System_reference/02.10_Data_Logging/02.10.01.08.01.01.03.01_Structure_of_a_TMLimits_CSV_file.md
created: 2026-09-17
updated: 2026-09-17
verified: doc-only
---

# Test Method（测试方法）

> 这一步把「要测什么、怎么判 pass/fail」写成一个 C++ 类，编译成 universal test method library（UTM 库）；库建好后 testflow 才有东西可调用。

## 目的

文档事实（`01.06.01`）：

- Test method 是用 test method API 创建的、标准或定制的 **C++ 测试程序**。
- Test method API 是对标准 C++ 语言的扩展，用于：从被测器件测量输出信号、取回测量数据、
  分析测量数据、把计算结果判为 pass/fail。
- Universal test method 是 **SmarTest 6.3 起**可用的编程风格与环境。它是一套标准 C++
  工程，**独立于任何 device project 与 Eclipse project**。

文档事实（`02.07.01`）：`02.07_Test_Method_Reference` 手册覆盖的题目依次是 ——
Universal Test Method（概念与创建/使用）、Test Method Programming Essentials、
API Reference、Test Method Library（预定义 DC/AC/PPTIA 库）、
SmarTest 自带 test method snippets、Concurrent test framework、d2s-framework、
SmartCalc framework。

文档事实（`02.07.03`）本阶段要完成的编程任务清单：
- **DC 测试**：设测量条件 → 执行测量 → （可选）取原始数据 → （可选）DSP 计算 → 与
  预定义 limit 比较并判 pass/fail。
- **AC 测试**：（可选）改 setup 数据 → 执行测量 → 取原始数据 → DSP 计算 →
  与 limit 比较并判 pass/fail。
- **流程控制**：控 sequencer / 监视状态、等待程序执行、访问 flag 和变量、设多 site 测试、
  实现 multi-port 测试、控制用户 GPIB 仪器（非系统用）、从 test method 执行 firmware 命令、
  处理 API fatal error。

**边界声明**：本页只讲 **test method 本身**（C++ 类 / UTM 库这一侧）。
testflow 里对一个 test method 的**调用**（test suite / test instance、limits 取值、
selector、flags）属于 `[[testflow]]` 阶段，本页不展开。

## 前置条件

文档事实（`02.07.02.02.01`，`Before you begin`）：

> Make sure you are using SmarTest 6.3 or later, and the **device primary setups are
> ready to use**.

文档事实（`02.07.02.02.02`，`Before you begin`）：

> Make sure you are using SmarTest 6.3 or later, and a **test method project has been
> created**.

合成两条前置：

1. **SmarTest 6.3 或更高版本** —— UTM 自 6.3 起才存在（`01.06.01` 与两处 `Before you begin` 三处互证）。
2. **device 的 primary setup 已就绪**（primary level / timing 等），出处 `02.07.02.02.01`。
   见 `[[project]]`、`[[level]]`、`[[timing]]`。
3. **test method project 已创建**（建 class 的前置）。见 `[[project]]`。
   同时需**先打开 C/C++ perspective**（`01.06.02.01`：Open Perspective 选 C/C++）。

补充说明（`01.06.01`）：UTM 工程**独立于 device project 与 Eclipse project**，
所以「device primary setup 就绪」不是编译层面的硬依赖，而是把 class 参数
（`SpecVariable` 等）接到真实 spec 上时才需要。

## 涉及对象

| 对象 | 层级 | 在本阶段干什么 |
|---|---|---|
| `[[test-method-project]]` | gui | C/C++ perspective 下 `New > Test Method Project` 建出的 C++ 工程，UTM 库的容器（`01.06.02.01`） |
| `[[test-method-class]]` | gui | `New > Test Method Class` 向导产出的类模板；决定类名、参数、limits（`01.06.02.02`、`02.07.02.02.02`） |
| `[[run]]`（`run()` 函数） | L2 代码 | 测试方法的执行体，测量+判定+记录都写在这里（`01.06.02.03`） |
| `[[initialize]]`（`initialize()` 函数） | L2 代码 | 初始化钩子；文档示例在此加 limit：`addLimit("limit");`（`01.06.02.03`） |
| `[[add-limit]]` | L2 | 在 `initialize()` 里给 test method class 注册 limit 名（`01.06.02.03`） |
| `[[on-first-invocation-begin]]` | L2 | 声明「首次调用块」开始——多 site 并行 setup/execution 的边界（`02.07.04.01.138`、`01.06.02.03`） |
| `[[on-first-invocation-end]]` | L2 | 结束上述块（`02.07.04.01.138`） |
| `[[for-each-site-begin]]` | L2 | 声明「逐 site 顺序 setup」块开始；**必须放在 first-invocation 或 last-invocation 块内部**（`02.07.04.01.70`） |
| `[[for-each-site-end]]` | L2 | 结束 each-site 循环块（`02.07.04.01.70`） |
| `[[connect]]` | L2 | 连接资源/给 DUT 上电；示例写法 `CONNECT(); // Connect, if tester is disconnected`（`01.06.02.03`、`02.07.03.02`） |
| `[[disconnect]]` | L2 | 断开；文档明确「continuity 测试前必须先执行 DISCONNECT 序列」（`02.07.03.02`） |
| `[[test]]` | L2 | 判定+写 datalog；**禁止在 first-invocation 块内使用**（`02.07.04.01.241`） |
| `[[testset]]` | L2 | 测试编号/命名容器 + `judgeAndLog_***` 系列，是 TEST 的推荐替代（`02.07.04.01.244`） |
| `[[limit]]` | L2 | 承载 low/high limit 与比较运算符的数据容器，作 `TEST()` 的 limit 参数（`02.07.04.01.126`） |
| `[[tmlimits]]` | L2 + file | 用外部 CSV 文件控 limits 与 test numbering（`02.07.04.01.250`） |
| `[[fw-task]]` / `[[begin-extension]]` / `[[end-extension]]` | L2（L1 通道） | 从 test method 里直接执行 firmware 命令（`02.07.03.10`） |
| `[[spec-value]]` | L2 参数类型 | 参数类型之一，格式 `"value[unit]"`（`02.07.02.02.02`） |
| `[[spec-variable]]` | L2 参数类型 | 引用 timing/level 文件里定义的 spec 变量（`02.07.02.02.02`） |
| `[[pin-string]]` | L2 参数类型 | 用于 pins / pin lists / pin groups（`02.07.02.02.02`） |
| `[[file-string]]` | L2 参数类型 | 把文件名作为参数值（SmarTest 7.2.1 起）（`02.07.02.02.02`） |
| `[[option-list]]` | L2 参数类型 | 可为参数输入多个候选选项（SmarTest 7.2.0 起）（`02.07.02.02.02`） |
| `[[context-pins]]` | L2 参数类型 | 用于 concurrent test framework 的 `CCF_FocusedPins` 参数（SmarTest 7.2.0 起）（`02.07.02.02.02`） |
| `[[universal-test-method-library]]` | file | 本阶段最终产物：编译出的 UTM 库（见「产物」） |
| SmarTest GUI（C/C++ perspective、Project Explorer、Console view、Properties view） | gui | 建工程/建类/编译/看错误/看参数一致性（`01.06.02.01`、`01.06.02.04`、`02.07.02.02.02`） |

## L1 — Firmware / Setup Command

L1 在本阶段**不是主体**：命令本体在 `02_System_reference/02.06_Command_Reference` 里，
test method 侧只提供**调用通道**。

### 调用通道（文档事实，`02.07.03.10`）

> You can execute firmware command to control your hardware directly by using the
> **FW_TASK, BEGIN_EXTENSION and END_EXTENSION** APIs.

- `FW_TASK` 执行一条 firmware 命令；若命令有回值，可接收其输出。
- `BEGIN_EXTENSION` / `END_EXTENSION` 声明一个「扩展块」，可在其中以 firmware 层级访问
  系统硬件或 MCD。

文档给出的最小示例（逐字，`02.07.03.10`）：

```cpp
STRING dfcm("DFCM 1,4000,50,-1.0,1.00,4000,5,NGNG,(CP)\n");
STRING ptstq("PTST? 1,NONE,CVAL\n");

BEGIN_EXTENSION();
  FW_TASK(dfcm);
  STRING answer;
  FW_TASK(ptstq, answer);
      :
      :
END_EXTENSION();
```

文档事实，扩展块的 setup 冲突规避（`02.07.03.10`）：
- 在 `BEGIN_EXTENSION` / `END_EXTENSION` 声明的扩展块期间，test method 的 **caching
  机制被临时关闭**，这是系统隐式做的。
- **进入扩展块前应先执行 `FLUSH` API**。`ANALOG`、`ANALOG_STATUS`、`PRIMARY_STATUS`、
  `ROUTING_STATUS` 等 test method API 的 setup 数据存在 caching 机制里，`FLUSH` 把它们
  下载到系统硬件或 MCD。

文档事实（`02.07.04.01.138`）：多 site 场景下，first-invocation 块内可用
`BEGIN_EXTENSION`（带 site 参数）+ `END_EXTENSION` 包住 `FW_TASK`；
**不应用不带参数的 `BEGIN_EXTENSION`**。

### 命令本体在哪（文档事实，章首页）

`02.07.03.10` 明确指向 `02.06_Command_Reference` 手册。按域分的入口章：

- `02.06.09_AC_Testing_Commands` → `Concepts of AC test functions`、
  `List of AC test function commands`（如 `CYRM`、`DPSR`、`DRLS?`、`EDDC?`、`EDSP`、
  `ESGB`、`EXSR`、`FTSM`）
- `02.06.10_DC_Measurement_Commands` → `Concepts of DC measurement`、
  `List of DC measurement commands`（如 `CSAS?`、`CTXT`、`DDIC`、`DFCT`、`DPSE`、
  `GNOS?`、`MEAS`、`MSET`）
- `02.06.13_Commands_for_the_TMU_per_pin` → TMU per pin 测量**周期信号的脉宽、周期长度、
  上升/下降时间**等
- `02.06.17_Commands_for_PRBS_per_pin_tests_and_loopback_tests` → PRBS / loopback /
  基于 pattern 的 SmartLoop 测试

**归属判定**：这四章是**命令参考**（L1 层），不是 test method API 参考；它们只在被
`FW_TASK` 调用时才与本阶段发生关系。本页不展开各命令语法，命令细节归各自的
`[[命令对象页]]`。

## L2 — Test Method API

### 类模板与参数

文档事实（`02.07.02.02.02`）：`New > Test Method Class` 向导里 `Templates` 可选三种：

- **Normal test method class** — 普通 test method
- **Concurrent test method class** — 基于 CTF 的 test method
- **Customized shmoo test method class** — 定制 shmoo test method（SmarTest 7.2.0 起）

文档明确建议：**不要把 normal test method 和 concurrent test method 放进同一个工程**
（"To easily manage the test methods, it is not recommended to put normal test methods
and concurrent test methods in one project."）。

文档事实，类名约束：
- 类名**必须以大写字母开头**，否则向导报错。
- **避免在不同 UTM 工程里用同一个类名**；若必须同名，把源文件放进工程子目录以区分相对路径。

文档事实，参数类型全集（`02.07.02.02.02`）：
`int`、`double`、`string`、`PinString`、`SpecVariable`、`SpecValue`、`ContextPins`、
`OptionList`、`FileString`。

版本沿革（`02.07.02.02.02` `Functional changes`）：
- SmarTest 6.5.0：新增 `PinString`、`SpecVariable`
- SmarTest 6.5.2：新增 `SpecValue`；新增 Build Test Method 提醒对话框
- SmarTest 7.1.3：向导支持选择 test method class 模板
- SmarTest 7.2.0：新增 `Customized shmoo test method class` 模板；新增 `ContextPins`、`OptionList`
- SmarTest 7.2.1：新增 `FileString`

文档事实，参数属性（`Add a new parameter` 窗口）：
`Identifier`（testflow editor 里显示的参数名）、`Type`、`Variable`（`run()` 里用的变量名，
自动为 `m` + 参数名，可改）、`Default`（可选）、`Options`（可选，候选值以**冒号 `:`** 分隔）、
`Comment`（可选）。**支持参数层级**：用 `.` 建层级，例如 `x.start` / `x.stop` / `x.step` / `x.scale`。

文档事实，输出参数与 limits：
- 输出参数从 `result0` / `result1` / `result2` / `result3` 中选。
- Limits 区**只能指定 limit 名字**；limit 的**值**在 tabular testflow editor 或
  Properties View 里设置/修改。详见 `[[testflow]]`。
- 参数增删可以直接改 test method 源文件。

### 一个完整的 run() 示例

文档事实（`01.06.02.03`，AC 搜索测试 `PspecSearch`）：

`initialize()` 里：
```cpp
addLimit("limit");
```

`run()` 里：
```cpp
// Declare V93000 variables
SEARCH_FUNC_TASK tSearch;
CONNECT();  // Connect, if tester is disconnected

ON_FIRST_INVOCATION_BEGIN();
   // Define measurement sequence and execute test
   tSearch.pin(mSPinList).spec(mSSpecVariableName.mName,mSSpecVariableName.mType).method(mSSearchType).start(mDxStart)
          .stop(mDxStop).stepWidth(mDxStep).resolution(mDxRes).resultPins(mSResultPins);

   // Execute measurement
   tSearch.execute();
ON_FIRST_INVOCATION_END();

//judge and log the test results
if (tSearch.getPassFail() == TRUE)
{
   // Check for valid measurement results & datalog
   TEST(mSPinList,"limit",tSearch.getPassValue(mSPinList));
}
```

注意示例里 `mSPinList` 等 `m` 前缀变量，正对应向导自动生成的 `Variable` 命名
（`m` + 参数名）——两篇文档互相印证。同时注意结构：
**测量在 first-invocation 块内、判定与记录在块外**，这正是本页要讲清的生命周期骨架。

### ON_FIRST_INVOCATION_BEGIN ↔ TESTSET：本阶段的生命周期骨架

这是全库**第二热**的 L2 对象（`in_src=74`），它的约束条件决定了整个 test method 的写法。

文档事实（`02.07.04.01.138`）：

- `ON_FIRST_INVOCATION_BEGIN` 与 `ON_FIRST_INVOCATION_END` **必须成对使用**，
  中间区域称为 **"first-invocation block"**。
- **多 site 才有意义；单 site 下该 API 被忽略。**
- 块内可写 Setup 与 Execute API，使它们对**所有 active site 并行**执行。
  也可写其它函数，但这些函数要么只对**当前被测 site**工作（例如 Result API），
  要么与 site 无关（例如 Computation API）。
- 块内**所有语句只在程序为第一个被测 site 运行时执行一次**。
- **禁止把 first-invocation 块写成条件式的**；若写了 if，必须在 else 分支放一个
  dummy first-invocation 块。
- 头文件：`/opt/hp93000/soc/prod_com/include/MAPI/MapiUtil.h`。无参数、无返回值。

**最关键的禁令（文档事实，`02.07.04.01.138` CAUTION 逐字）**：

> The `TEST()` and `LIMIT()` statements as well as all of the "judgeAndLog_***" statements
> described in `TESTSET` **must never be used inside a first-invocation block**. Using any
> of these statements carries a high risk of defective devices being declared OK by the test.

同一条禁令在三篇文档里互相印证：
- `02.07.04.01.241_TEST`：`The TEST API cannot be used within a first-invocation block,
  not even inside an "each site" loop block.`
- `02.07.04.01.126_LIMIT`：`The LIMIT API cannot be used within a ON_FIRST_INVOCATION
  block, not even inside a FOR_EACH_SITE block.`

**推断（三层关系）**：把上述三条合起来看 —— `ON_FIRST_INVOCATION_BEGIN` 划出的是
**并行测量区**，`LIMIT` 与 `TEST` / `TESTSET().judgeAndLog_***` 划出的是
**串行判定与记录区**；二者必须物理分离。原因是并行区里所有 site 的语句只跑一次，
在那里做判定只会得到「一个 site 的结果」却写进所有 site 的 datalog —— 所以文档才说
「有把坏片判成 OK 的高风险」。这就是为什么 `01.06.02.03` 的示例把 `TEST(...)` 写在
`ON_FIRST_INVOCATION_END()` **之后**。

文档事实（`02.07.04.01.138` 示例 3，逐字节选）：

```cpp
ON_FIRST_INVOCATION_BEGIN();

    //
    // Setup and Test Execution
    //
    Routing.pin("Aout").connect(TM::SINGLE);
    Analog.DGT("Aout").enable();
    EXECUTE_TEST(0.1 sec);

    //
    // Retrieve measured analog waveform
    //
    ARRAY_D AnaWave = Analog.DGT("Aout").getWaveform();
    Routing.pin("Aout").disconnect();
    Analog.DGT("Aout").disable();

    FLUSH();

ON_FIRST_INVOCATION_END();
```

文档对它的解释：块内所有 API 只在程序为第一个被测 site 运行时对**所有 site 并行**
执行一次；因此所有已连接 site 上 `Aout` 引脚的模拟模块被启用，然后对所有已连接 site
做测量。

### FOR_EACH_SITE_BEGIN：并行区里的串行 setup

文档事实（`02.07.04.01.70`）：

- `FOR_EACH_SITE_BEGIN` 与 `FOR_EACH_SITE_END` **必须成对**，中间区域叫
  **"each site loop block"**。
- **多 site 才有意义；单 site 下被忽略。**
- 它给「并行测试执行之前」提供**逐 site 不同的 setup 条件**（site-specific setup）。
- **位置约束（关键）**：each site loop block **必须放在**
  - first-invocation 块（`ON_FIRST_INVOCATION_BEGIN` / `END`）**内部**，或
  - last-invocation 块（`ON_LAST_INVOCATION_BEGIN` / `END`）**内部**。
- 块内所有语句，在程序为第一个被测 site 运行时，对**所有 active site 顺序执行**。
- 若要顺序执行 setup **和 query**，用 `FOR_EACH_SITE_BEGIN_WITH_QUERY`。
- 头文件同 `MapiUtil.h`；无参数、无返回值。

文档给出的嵌套最小骨架（`02.07.04.01.70` 示例 1，逐字）：

```cpp
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

**推断**：`ON_FIRST_INVOCATION_BEGIN` 是**外层**、`FOR_EACH_SITE_BEGIN` 是**内层**，
嵌套方向是单向的（each-site 必须在 first-invocation 里面，不能反过来）。所以
「first-invocation = 并行一次；each-site = 在内层按 site 逐个 setup」这个结构，
和 `02.07.03.13` 说的「setup 并行 + 测后处理串行」是同一种划分的两种写法。

### 多 site 编程总览

文档事实（`02.07.03.13`）：

要在多 site 下跑 test suite，需设置 testflow flag：**Parallel Mode Enable** 与
**Allow Parallel**。**但**——即使不优化，test method 程序仍会**对所有 site 顺序执行**，
和 user procedure 一样，因此**达不到最大性能**。

要达到最大性能，必须在 test method 程序里加 API 做优化，实现 setup 与 test 的并行执行；
而**测后处理（取结果、计算、判定等）仍是逐 site 串行**。

文档事实，核心机制：

- 多 site 测试里可定义一个并行执行块，称为 **`first-invocation` block**。该块在
  **程序为第一个被测 site 运行时，对所有 site 执行一次**。
- **Result API 永远只对「当前被测的单个 site」工作**（query focus）：程序为第一个被测
  site 运行时，它们把所有 site 的测量数据**暂存到 cache**；之后每次执行时从 cache 里
  返回当前 site 的数据。

文档事实，控制 setup focus / query focus 的 API 清单：

作用域块类：
- `ON_FIRST_INVOCATION_BEGIN` / `ON_FIRST_INVOCATION_END` —— 并行块
- `FOR_EACH_SITE_BEGIN` / `FOR_EACH_SITE_BEGIN_WITH_QUERY` / `FOR_EACH_SITE_END` —— each-site 循环块
- `FOR_SEMI_PARALLEL_TEST_BEGIN` / `FOR_SEMI_PARALLEL_TEST_END` —— 半并行测试块
  （半并行组由 `SEMI_PARALLEL_CONFIG()` 定义）

setup focus 类：
- `SET_TEST_FOCUS` — 把指定 site 置为 setup-focus 态；也可同时把除某个 site 外的所有
  enabled site 置为非 setup-focus；返回 site 的原状态
- `UNSET_TEST_FOCUS` — 把指定 site 从 setup-focus 态移除，返回原状态

信息获取类：
- `GET_TEST_FOCUS` — 返回 setup-focused 的 site 数与 site 号
- `GET_CONFIGURED_SITES` — 返回 pin configuration 里配置的 site 数与 site 号
- `GET_ENABLED_SITES()` — 当前 enabled sites，面向多 site 测试
- `GET_ACTIVE_SITES()` — 当前 active sites，即当前要执行 test method 程序的 site
- `CURRENT_SITE_NUMBER()` — 当前被测 site 的 site 号

文档事实，兼容性要点：

> The APIs listed above **except for** GET_TEST_FOCUS, GET_CONFIGURED_SITES,
> GET_ENABLE_SITES, GET_ACTIVE_SITES, and CURRENT_SITE_NUMBER **are ignored in
> single-site testing**.

因此可以写单 site / 多 site 都兼容的 test method 程序，将来再从单 site 升级到多 site。

文档事实，`GET_TEST_FOCUS` 的一个坑（`02.07.04.01.97`）：
> The size of the array is set to **1** if the API is executed **outside of the
> ON_FIRST_INVOCATION block or inside of a FOR_EACH_SITE loop block**.

即 `sites` 数组的尺寸会随调用位置变化 —— 在 those 位置下只有一个元素。

文档事实，TIA 特例（`02.07.03.13`）：GP-TIA/HP-TIA 里若两个 TIA core 接在同一
front-end module 且分给两个 site 做多 site，需在 `ANALOG().TIA()`、`Analog.TIA()`、
`Routing.pin().connect()` 这三个 API 里选特殊 core 标识符 **default core**
（即分配给各 site 的 TIA，在 pin configuration 里定义）。

### 判定与记录：TEST → TESTSET / judgeAndLog

文档事实（`02.07.04.01.241_TEST`）：

- `TEST` 判定测试数据 pass/fail 并记录。
- 文档明确：**推荐改用 `judgeAndLog` 系列 API**；`TEST` 系列**保留是为了向后兼容，
  将来版本可能被移除**。
- `TEST` 支持的功能测试 / AC / DC / flexible DC / DC dynamic / spec search / ppTIA /
  multiport 各有一套重载。头文件
  `/opt/hp93000/soc/prod_com/include/MAPI/TestControl.h`。
- 参数 `continue`：默认 FALSE（FAIL 就终止测试）；TRUE 或 `TM::CONTINUE` 则继续。
  **多 site 下第一个 site 行为不同**：即使 `continue=FALSE` 且返回 FAIL，第一个 site
  也总是继续；后续 site 才会终止。
- 参数 `reliability`：`TM::RELIABLE` / `TM::UNRELIABLE`，省略等于 `TM::RELIABLE`。
- 参数 `port`：**仅 multiport**；`TEST` 里**不能指定 pin group**。
- `pin`：单个 pin 名。`testname`：可被 Properties view 引用，可关联 Tests 页的 limits。

文档事实（`02.07.04.01.244_TESTSET`）：

- `TESTSET` 类访问的容器定义**某个 test suite 里结果的编号流程**（test numbering）。
  `testname()` / `testnumber()` 用于给具体测试指定用户自定义的名字与编号。
- 系统预置对象名 **`TestSet`**；头文件
  `/opt/hp93000/soc/prod_com/include/MAPI/TestSet_r.h`。
- **`judgeAndLog_***` 系列**（文档推荐的替代）：
  `judgeAndLog_FunctionalTest()`、`judgeAndLog_ParametricTest()`、`judgeAndLog_PmuIfvm()`、
  `judgeAndLog_PmuVfim()`、`judgeAndLog_Dps()`、`judgeAndLog_DpsVfim()`、
  `judgeAndLog_Spmu()`、`judgeAndLog_PpmuMeasure()`、`judgeAndLog_SpecSearch()`、
  `judgeAndLog_PptiaTask()`、`judgeAndLog_DcResultAccessor()`、`judgeAndLog_ScanTest()`，
  外加 `doLog_ShmooTest()`。
- 命名约定：前半 `judgeAndLog` 表示「按该测试结果判**整个 test suite** 的 P/F 并记录结果」；
  后半表示该 API 适用的测试类型。
- **线程约束（关键）**：`TESTSET` 类对象**不得跨多个线程共享**；在 SMC 后台处理里用时，
  只能在 `SMC_backgroundProcessing()` 方法内创建和使用。
- 测试编号要在 Testflow Editor 里启用 **`test_number_enable`** flag 才生效。
- 与 SMC 混用时：若在 SMC framework 内用 `TESTSET` 而非 `SMC_TEST`，binning 发生在
  `SMC_SYNCHRONIZE` 里，规则同 `SMC_TEST`。

文档事实（`02.07.04.01.88_GET_FUNCTIONAL_RESULT`）：返回**最近一次测量**的 pass/fail
结果 —— 该测量可以是 functional test、PPMU、SPMU 或 DPS 测量；也可返回 multiport
burst pattern 里最近一次 functional test 的结果，或指定 pin + 指定 execution context 的结果。

### limits：LIMIT 对象与 TMLimits CSV

文档事实（`02.07.04.01.126_LIMIT`）：
- `LIMIT` 类访问一个数据容器，内含 **lower limit、upper limit 和比较运算符**。
- 成员函数改这些值与运算符；用构造函数建出代表 limit 范围的对象。
- 该对象用作 `TEST` API 的参数来指定 limit 范围。
- **不得用于 `ON_FIRST_INVOCATION` 块内，`FOR_EACH_SITE` 块内也不行**（见上文禁令）。

文档事实（`02.07.04.01.250_TMLimits`）：`TMLimits` 类让你**用 CSV 文件里的数据**控制
testflow 的 limits 与 test numbering。文档给的收益：
- 可在同一 testflow 里**切换不同测试模式/阶段**（例如 wafer 测试用松 limit、
  QC 用紧 limit），通过 `load()` 函数选择。
- CSV 可**脱离 SmarTest 编辑**（Open Office Calc 或普通文本编辑器），便于现场改动。

文档事实（`02.10.01.08.01.01.03.01`，数据文件格式）：
TMLimits CSV 是标准 CSV，逗号分隔字段、换行分隔记录；**含两行表头 + 每个 test 一行**。
- 第一行表头是**列名**（列可自选，但必须有合适的 key 列）。
- 第二行是**每列所属的 test mode**。某列若没指定 test mode，则该列的值**适用于所有
  test mode**；指定了就只在选定该 mode 时生效。

### 各测试域的编程入口

文档事实（`02.07.03.02`，DC）：

**Pin PMU 路线**：`PPMU_SETTING` / `PPMU_PIN_SETTING`、`PPMU_RELAY` / `PPMU_PIN_RELAY`、
`PPMU_MEASURE` / `PPMU_PIN_MEASURE`、`TASK_LIST` —— 可逐 pin 设定 force 电压或电流、
施加到引脚、执行测量。

**DPS 路线**：`DPS_TASK` / `DPS_PIN_TASK`。

文档事实的重要 Note（`02.07.03.02`）：
- 优先用 **FlexDC API** 做 DC 测试编程，以节省测试时间。
- `DPS_TASK` 强制施加 primary DPS set 或 primary level spec/equation sets 里定义的电压
  并做电流测量。要改 force 电压值，就改 level 相关 primary，用 `PRIMARY_STATUS` API
  或用 `LEVEL_SPEC` API 改 level spec 值。
- 需要用 **DPS 电流测量的 auto-ranging**，或需要抑制 DPS 测量里 Testsuite 对话框指定的
  level/timing 相关 primary 激活时，**必须用 `DPS_VFIM`**；其他情况建议用
  `DPS_TASK` / `DPS_PIN_TASK`。（`DPS_TASK` 不支持 auto-ranging 和 preAction "NPRM"。）
- 测量结束后 pin PMU / DPS **保持连接并继续输出**；要停止输出就执行 DISCONNECT 序列。

文档事实，CONNECT/DISCONNECT 时机（`02.07.03.02`）：
> You need to execute the CONNECT sequence before the test, to apply the power to DUT
> and connect the target pins to tester resources.
> 用 continuity 测试配合 DC API 时，**必须先执行 DISCONNECT 序列**。

文档事实（`02.07.04.01.234_SPMU_TASK`）：`SPMU_TASK` 用 DC Scale 卡的 PMU 模式或数字卡
的 BADC **定义并执行并行 DC 测量**，需配合 `TASK_LIST` 使用；`SPMU_PIN_TASK` 是其
pin 级子对象（`SPMU_PIN_TASK.clamp/compare/connect/connectState/...` 等成员函数）。

文档事实（`02.07.04.01.63.18_EVENT_VALUE_DOUBLE`）：`EVENT_VALUE_DOUBLE` 是 helper 类，
封装「值可能是固定值、spec、或 equation 名」这三种情况的差异。**它不从 equation 系统
取实际值**，只指定**执行时**从哪里取值。所有 event 都支持 level equation set 里定义的
spec 与 equation 变量，用 **`LEV:` 前缀**引用（指向 primaries 设定的当前 level equation set）。
另有姊妹类 `EVENT_VALUE_INT` —— 拆成两个值类是为了**编译期类型安全**。

### SMC / 并发 / 协议 / 离线：本章的其它框架

文档事实（章首页归属判定）：

- `02.07.05_Test_Method_Library` — SmarTest **自带**的 test method 集合（非用户编写）。
  含 `ac_tml`、`dc_tml`、`multi_group_dc_tml`、`miscellaneous_tml`、`scan_tml`、
  `smartCalc`、`tmu_tml`。文档称其中 test method「throughput 尽可能优化且代码易读」。
  **归属：本阶段的下游** —— 用户可选择直接用预定义库而不自己写（`01.06.01` 的
  「predefined universal Test Method Libraries」）。
- `02.07.06_Test_method_snippets_provided_with_SmarTest` — SmarTest 自带的 test method
  **片段/模板**，按 DC / ADC / DAC / CODEC / baseband→RF / RF→baseband / RF→RF /
  miscellaneous 分类。**归属：本阶段**（写代码时可抄的素材）。
- `02.07.09_d2s-framework` — **dynamic-to-static**，自动生成静态、高效测试时间的
  vector label，同时保留开发期动态改动能力。`Introduced in SmarTest 6.5.4`。
  **归属：本阶段的框架扩展**（与 pattern/vector 侧交叉，见 `[[pattern]]`）。
- `02.07.10_SmartCalc_framework` — SmartCalc (SMC) 框架，把耗时的计算与数据上传
  移到**后台线程**以缩短测试时间。**归属：本阶段的框架扩展**；`SMC_ARM`（`in_src=47`）
  是它的入口 API。
- `02.07.11_Protocol_Aware_ATE` — 协议感知测试（JTAG / MDIO / I2C 等标准主机接口的
  事务级协议测试）。**归属：本阶段的框架扩展**（偏 use case）。
- `02.07.12_Offline_Result_Emulation` — 离线结果仿真（ORE），让用户自定义测试与测量
  结果，用于**离线验证**。**归属：本阶段相关，但属于验证手段** —— 见「验证」小节。
- `02.07.13_SmartRDI` — SmartRDI，含 `RDI`、`RDI_Configure` 文件、`Code structure with
  SmartRDI`、`RDI_INFO_LEVEL`、按字母序的函数表、DCVI alarm handling、
  d2s-like protocol test setup 等。**归属：本阶段的框架扩展**。

文档事实（`02.07.04.01.231.01_SMC_ARM`）：`SMC_ARM()` 的作用是**武装
`SMC_backgroundProcessing()` 方法并把指定数据传给它**。数据传递三种方式：
- 作为 test method 类的**成员变量**（文档推荐的传法）
- 最多 8 个**按值**可选参数
- 最多 8 个**按引用**可选参数

**重要约束**：后台进程运行期间，**用于后台进程的类成员变量不得被修改**。
这条限制同样适用于「在 test method class 的 `initialize()` 里定义的 test method 参数，
并已赋值给类成员变量」的情况。

### API 参考的规模与边界

文档事实（`02.07.04`）：`02.07.04_API_Reference` 下列：
APIs in alphabetical order、Test method specific data types and variables、
Encoding/Decoding Table for A-Law/μ-Law、Code Format Tables、Window functions。

**术语定义（文档事实，`02.07.04`，这是读这一章的总钥匙）**：

- **API** = SmarTest MAPI 提供的、**无需实例化**即可使用的函数。
- 标题级命名约定：API 写成 `ApiName()`，例如 `SMC_DISABLE()`。
- **Class** = UTM 提供的类，通常**必须实例化**出对象才能用。标题级写成 `ClassName`，
  例如 `SPMU_TASK`。
- **Member function** = 类成员，只能在对象上下文里用。标题级写成
  `ClassName.CMemberFunction()`，例如 `SPMU_TASK.execMode()`。

`02.07.04` 还规定：所有 UTM 参考条目的结构统一为 —— 描述 → `Syntax`（列出该 API/
成员函数的所有接口，含类构造函数；一个 interface 对应一种调用方式）→ 参数表（每个参数
可带 options 列表）→ 返回值 → 示例。

**归属提示**：`02.07.04` 及其下 1,314 篇条目是本阶段**对象页的语料来源**，不是流程；
本页只作层级归属，不复述单条 API 语法。

文档事实（`02.07.01`）：**不属于 test method 编程**的 API（HVM API、BLC API、
HVM session info API、digital calibration API、test suite control API）在
`02.09_Test_Program_Management` 里 —— 这一条对 L3 小节很重要。

## L3 — 外部控制

**L3 入口是横切的，能力面按阶段分族。** 文档事实：`TestsuiteProxy`
（`02.09.01.14.02.01`）的 33 个编号成员里，session / execute / `isPass` / `isExecuted` /
name / siteMatch 那几个是**横切面**，其余**天然按阶段分组**——这不是巧合，是文档自己的组织方式。
横切入口见 [[test-suite-control-api]]；产物文件接口见 [[tpi-program-routines]]（**同层、同样由外部客户端进程调用**，见该页「出处」）。

**本页是九页里 L3 专属面最厚的一页。** 文档事实（`02.09.01.14.02.01`）：test method 一族
有九个成员，占 `TestsuiteProxy` 编号成员的近三分之一——

| 分类号 | 成员 | 作用 |
|---|---|---|
| `.01` | `attachTestmethod()` | 把 test method 挂到 test suite |
| `.13` | `getTestmethodName()` | 取 test method 名 |
| `.14` | `getTestmethodParameterNames()` | 取参数名 |
| `.15` | `getTestmethodParameterValue()` | 读参数值 |
| `.32` | `setTestmethodParameterValues()` | 写参数值 |
| `.11` | `getTestmethodDefaultLimitNames()` | 取 default limits 名 |
| `.16` | `getTestmethodUserDefinedLimitNames()` | 取 user-defined limits 名 |
| `.12` | `getTestmethodLimitValue()` | 读 limit 值 |
| `.31` | `setTestmethodLimits()` | 写 limit 值 |

`attachTestmethod` 的签名与用例（`02.09.01.14.02.01.01`、`02.09.01.14.01`）：

```
bool attachTestmethod(const std::string& name);
```

```
ts.attachTestmethod("ac_tml.AC_TEST.FunctionalTest");
```

即 **test instance 的指定可以不点 GUI，由外部程序完成**；参数与 limit 也可外部读写。
调用方式见 `02.09.01.14.01`：外部 C++ 客户端，链接 `-ltestsuitecontrol_api`，
经 `run -x` 启动；该族 `Introduced in SmarTest 6.5.2`，7.10.3 可用。

同层的产物文件接口（[[tpi-program-routines]]）：`DataManager`（`02.09.01.09.02`）的
`dm_testprog` / `dm_testflow` / `dm_testtable`，配 `dm_copy_in` 等操作；`GetEQVariableValue`
（`.10`）读 equation 变量。

> **改判记录。** 本页上一版 L3 写：「除此之外，本阶段语料中没有其它外部控制接口（无 HVM
> 实际用法、无远程/脚本化接口文档）」，然后落到「文档未覆盖」。**那一句是错的**——
> Test suite control API 里 test method 是最完整的一族。已删。
>
> 上一版唯一找对的是 `02.07.01` 那句「这些 API 不在 test method 编程里用」——**它说的是
> 「不在 test method **内部**编程时调用」，不是「与 test method 无关」**。前者是调用位置，
> 后者是主题；上一版把这两个读混了。这族接口的对象**正是** test method。

## 产物

文档事实（`02.07.02.02.02`，`Results` 段，逐字）：

> You will find the test method library in the **Debug sub-directory** of the test method
> project directory. The test method library is located in the directory
> **`/home/demo/devices/act299_tml/Debug/`**.

即：
- 产物 = **universal test method library**（test method 库）。
- 位置 = **test method 工程目录下的 `Debug/` 子目录**。
- 文档给出的具体样例路径 = `/home/demo/devices/act299_tml/Debug/`。

文档事实，工程名与目录名（`02.07.02.02.01`）：
> The default project name is **device name plus "_tml"**.

这解释了 `act299_tml` 与 `01.06.02.01` 里「默认工程名是 `act299_tml`」的关系 ——
device 名 `act299` + `_tml`。两篇文档互相印证。

推断：`Debug/` 是 Eclipse CDT 的默认构建配置目录名，所以「库在 Debug 子目录」与
「工程在 `/home/demo/devices/` 下」两句话合起来，推出的库路径通式是
`<device目录>/<device名>_tml/Debug/`。文档只给了这一个具体样例，未给其它平台/配置下的路径。

文档事实（`01.06.02.04`）：库由 **Build Project** 产生 —— 在 Project Explorer 里右键
工程选 `Build Project`。

文档事实（`02.07.02.02.02`）：也可以**通过构建引用了该 test method 工程的 device
project 来间接构建它**（见 `02.07.02.02.03_How_to_create_and_execute_a_universal-test-method-based_testflow`）。

**三层对照表见 [[mapping-testmethod]]** —— GUI 操作 ↔ 文件 ↔ L1 命令 ↔ L2 API ↔ L3 接口 的按目的对照
（`wiki/mappings/mapping-testmethod.md`；证据分三档写明，**`?` 与 `—` 不同义**：前者是「本页没找到证据」，
后者是「这一层不存在这个对应物」）。

## 验证

文档事实（`01.06.02.04`）：Build Project 之后 ——

> Check the **Console view** to see whether there is any error occurred.

文档事实（`02.07.02.02.02`）：
- 若构建出错，改源文件后**重新构建**工程。
- 构建信息在 **Console view 的 C-Build console** 里看。若构建了多个工程，在
  Project Explorer 里高亮某个工程即可看该工程的构建信息。
- **重要提醒对话框**（SmarTest 6.5.2 起）：构建/清理工程时会弹框提醒
  **「building or cleaning the project does not make its library effective for the
  current device」** —— 即**建库 ≠ 对当前 device 生效**。

文档事实，参数一致性检查（`02.07.02.02.02`，这是最可操作的验证信号）：
> After you add or remove the parameters and **rebuild** the test method project, open the
> Properties view for the test suite using this test method, you will see that this view is
> **grayed** because the parameters displayed in this view are not consistent with those in
> the test method code. To activate the Properties view, click the **Inconsistency Check**
> button on the top right to update the parameter settings in the view according to the
> test method code.

即「改动参数 → 重新构建 → Properties view 变灰 → 点 Inconsistency Check 恢复」是一条
文档给出的验证/修复回路，也是判断「库与 testflow 侧是否同步」的可见信号。

文档事实（`02.07.13` 章首页）：`02.07.12_Offline_Result_Emulation` 让用户**自定义测试与
测量结果用于离线验证**，含 `Pre-silicon and emulation workflow`、`Test program
requirements for offline result emulation`、`Configuration API`、`Offline result
emulation setup file`、`Examples`。**这是文档里明确给出的、在无真实器件时验证 test
program（含 test method）的手段。** 其配置 API 与 setup 文件细节本阶段未读。

`What to do next`（`02.07.02.02.02`）：`Create a testflow.`

## 常见错误

文档事实（`02.07.02.02.02`）：
1. **类名不以大写字母开头** → 向导弹出错误信息。
2. **不同 UTM 工程用同一个类名** → 文档要求避免；若必须，把源文件放进工程子目录区分相对路径。
3. **加了/删了参数后 Properties view 变灰** → 这是预期行为，点 **Inconsistency Check** 按钮恢复。
   根因：view 里的参数与 test method 代码里的不一致。
4. **构建报错** → 改源文件后重新构建；在 C-Build console 看构建信息。
5. **改完工程但 device 侧没生效** → 弹框明说 building/cleaning 不会让库对当前 device 生效。

文档事实（`02.07.04.01.138`、`02.07.04.01.241`、`02.07.04.01.126`，最严重的一类）：
6. **在 first-invocation 块里使用 `TEST()` / `LIMIT()` / `judgeAndLog_***`**
   → 文档 CAUTION 措辞：**「有把坏器件判为 OK 的高风险」**。
   包括「在 each-site 循环块内」这种情况也一样禁止。

文档事实（`02.07.04.01.138`）：
7. **把 first-invocation 块写成条件式的** → 禁止；若一定有 if，必须在 else 分支放一个
   dummy first-invocation 块。

文档事实（`02.07.04.01.70`）：
8. **把 each-site 循环块放在 first-invocation / last-invocation 块之外** → 违反文档规定的位置约束。

文档事实（`02.07.04.01.244`）：
9. **跨线程共享 `TESTSET` 类对象** → 文档明确禁止。

文档事实（`02.07.03.10`）：
10. **进入 extension block 前没执行 `FLUSH`** → 可能与扩展块内的 firmware 命令发生
    setup 数据冲突。文档给的规避法：先 `FLUSH` 把 caching 里的 setup 数据下载到硬件/MCD。

文档事实（`02.07.03.13`）：
11. **只设了 testflow 的 Parallel Mode Enable / Allow Parallel flag 就以为拿到了并行性能**
    → 不够；不优化 test method 程序的话，程序仍对所有 site 顺序执行。

文档事实（`02.07.03.17`，API fatal error 专章）：
文档的前提是「Test Method API 被设计成运行时**不会**发生内部错误」，但仍可能因
未预见问题而出错；即使精心设计开发，运行时仍可能遇到 warning 或 error。
**两个错误级别**：

| 级别 | 程序执行行为 | Report window |
|---|---|---|
| Warning | 继续执行下一条语句（Go to next statement） | Warning Message |
| Error | **立即中止当前 test method 程序执行** | Error Message |

该章给出两种处理方式：`SET_EXCEPTION_HANDLER`（自定义异常处理器）与
「on demand」方式（各有一篇子文档）。本页未下钻其语法。

文档事实，构建期错误（`02.07.02.02.02`）：构建信息在 Console view 的 C-Build console；
若构建多个工程，在 Project Explorer 里高亮工程以分辨。

文档事实（`02.07.04.01.250_TMLimits`）相关的排错入口：
TMLimits 的 test mode 由 `load()` 切换；若 limits 表现与预期不符，先查
**CSV 第二行表头（test mode 行）** —— 某列没写 test mode 时该列对所有 mode 生效，
这会造成「改了 mode 但值没变」的观感（`02.10.01.08.01.01.03.01`）。

## 下一步

`[[testflow]]` —— 建库只是把「怎么测、怎么判」这件事封装好；文档在 `Results` 之后直接写
`What to do next: Create a testflow.`（`02.07.02.02.02`）。只有 testflow 里把该 test method
实例化成 test suite、绑上 spec / limits / pins 并插入流程，库才真正被执行。
相关操作见 `02.07.02.02.03_How_to_create_and_execute_a_universal-test-method-based_testflow`。
另外 `02.07.02.10_Editing_test_method_from_a_testflow` 说明库建好后仍可从 testflow 侧
反向编辑 test method。
