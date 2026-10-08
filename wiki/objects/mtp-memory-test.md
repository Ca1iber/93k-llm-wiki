---
type: object
title: MTP_MEMORY_TEST
layer: L2
stage: pattern
tags: [mtp, memory-test-plus, mtp-memory-test, memory-test, bitmap, redundancy-analysis, fail-bit-count, multiport, hidden-upload]
related: [hidden-upload, smartcalc, smc-background-process-locks-config, error-map, pattern, mtp-maintenance-operations, mtp-shared-test-commands, mtpt]
sources:
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17_MTP_MEMORY_TEST.md
created: 2026-09-18
updated: 2026-09-20
verified: doc-only
---

# MTP_MEMORY_TEST

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **4,691 字符逐字取自** `<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17_MTP_MEMORY_TEST.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

There are two kinds of syntaxes:

- `MTP_MEMORY_TEST(void);`

This constructor creates an object for the MTP_ MEMORY_TEST() class.

- `MTP_MEMORY_TEST(const std::string& `resultArea`);`

This constructor is used when using the `Hidden upload`（raw: `../02.07_Test_Method_Reference/02.07.10.04.05_Hidden_upload.md`） algorithm in memory tests. Refer to Example 5 below or the example in `MTP_MEMORY_TEST.startTest()`（raw: `02.12.06.17.40_MTP_MEMORY_TEST.startTest.md`） for its usages.

Parameter
| Parameter | Description |
|---|---|
| resultArea | Name of a result area that you have previously defined.<br><br>This result area stores the error map of a functional test. |

### Example 1

Creating an MTP_MEMORY_TEST object:

```
MTP_MEMORY_TEST memoryTest;
```

### Example 2

Executing a simple bitmapping test method:

```
void MemoryTest::run()
{
  MTP_MEMORY_TEST memoryTest;

  memoryTest.enableAddressBasedResults(true).setImmediateBitmapToFile(true);

  // Execution is called only for first site
  ON_FIRST_INVOCATION_BEGIN();
  {
    CONNECT();
    memoryTest.execute();
  }
  ON_FIRST_INVOCATION_END();

  memoryTest.judgeAndLog();
}
```

### Example 3

Executing a simple bitmapping test method with fail bit count enabled:

```
void MemoryTest::run()
{
  MTP_MEMORY_TEST memoryTest;

  memoryTest.enableAddressBasedResults(true).setImmediateBitmapToFile(true);
  memoryTest.enableFailCount(true).
  memoryTest.setFBCLimit(MTP:DEVICE,100).setFBCLimit(MTP:PIN,10)
  .setFBCLimit(MTP:BANK,10);

  // Execution is called only for first site
  ON_FIRST_INVOCATION_BEGIN();
  {
    CONNECT();
    memoryTest.execute();
  }
  ON_FIRST_INVOCATION_END();

  memoryTest.judgeAndLog();
}
```

### Example 4

Executing an advanced bitmapping test method with retrieval of the failed addresses, logging, and query between pin index and pin name:

```
void MemoryTest::run()
{
  MTP_MEMORY_TEST memoryTest;

  memoryTest.enableAddressBasedResults(true);
  memoryTest.setMaxFailingAddressesToReconstructPerPin(1024);
  memoryTest.setFailAddressListOrdering(MTP:FAIL_CYCLE);

  // Execution is called only for first site
  ON_FIRST_INVOCATION_BEGIN();
  {
    CONNECT();
    memoryTest.execute();
  }
  ON_FIRST_INVOCATION_END();

  MTP_MEMORY_PATTERN& march6n = memoryTest.getMemroyPort("A").getMemoryPattern("march6n");
  ARRAY_ADDRESSES addressList;
  LONG nr_addresses;

  nr_addresses = march6n.getFailingAddressList("DQ_00",1024, addressList);

  // Loop over address list
  for(int i = 0 ; i  < nr_addresses ; i++)
  {
    MsgStream msg;
    msg << x =  << addressList[i].x << endl;
    msg << y =  << addressList[i].y << endl;
    msg << z =  << addressList[i].z << endl;
    // Print out address to report window
    cout << msg.c_str();
    // Store address in datalog
    PUT_DATALOG(msg.c_str());
  }

  // query dq index from pin name
  String pinName = "DQ_00";
  INT_VECTOR dqDC/DC power units = march6n. getDQDC/DC power unitsByPinName(pinName);
  INT_VECTOR::iterator pinIter;
  for (pinIter = dqDC/DC power units.begin(); pinIter != dqDC/DC power units.end(); ++pinIter) {
  msg << "DQ index for pin " << pinName << " : " << *pinIter <<  ";" << endl;
 }

  // query pin name from pin index
  int pinIdx = 0;
  STRING_VECTOR pinNameList = march6n.getPinNameListByDQIndex(pinIdx);
  if(!pinNameList.empty())
 {
   STRING_VECTOR::iterator pinNameIter;
   for (pinNameIter = pinNameList.begin(); pinNameIter != pinNameList.end(); ++pinNameIter) {
   msg << "Pin name for DQ index " << pinIdx << " : " << *pinNameIter << ";" << endl;
    }
 }

  //generate bitmap file.
  march6n.setBitMapFilePath("/data/bitmaps");
  march6n.addBitMapFileUserComments("Manual Bitmap");
  march6N.setBitMapFileName("march6N");
  march6n.generateBitmapFile();
}
```

### Example 5

Testing with hidden-upload algorithm

```
void SMCApiValidationTest::SMC_I_Mode()
{
  std::string resultArea;
  GET_TESTSUITE_NAME(resultArea);

  MTP_MEMORY_TEST memoryTest(resultArea);
  memoryTest.enableAddressBasedResults(true);
  memoryTest.setBitmapMode(MTP::BINARY_ENCODING);

  // Test Execution
  ON_FIRST_INVOCATION_BEGIN();
  {
    CONNECT();

    // define a new result area configuration set.
    RESULT_AREA_CONFIG_SET resConfSet(resultArea);
    // configure this result area for all pins.
    RESULT_AREA_CONFIG_PINS& resConfSetPins = resConfSet.pin("@");
    resConfSetPins.setErrorMapResultAreaSize(1024);

    memoryTest.execute();

    // Enable hidden calculation
    FOR_EACH_SITE_BEGIN()
        // kick off calculation thread
        SMC_ARM(memoryTest);
    FOR_EACH_SITE_END();
  }
  ON_FIRST_INVOCATION_END();
}

void SMCApiValidationTest::SMC_backgroundProcessing(MTP_MEMORY_TEST memoryTest)
{
  // hidden calculation
  memoryTest.judgeAndLog();
  memoryTest.generateBitmapFile();
}
```

<!-- 语法节 end -->

## 是什么

**`MTP_MEMORY_TEST` 是 MTP 里那个「跑完内存测试之后，把结果做成按地址的结果、再做冗余分析」的类。**

> 「Generates address-based results and performs redundancy analysis after executing a memory test. Multiport is supported.」

**这一句给了三件事**：① 输出是 **address-based results**；② 它做 **redundancy analysis**；
③ **支持 multiport**。
**注意 `after executing a memory test`**——**它管的是「跑完之后」**（形状见下面「三步」那张表）。

**MTP 专属，而且只有一个头文件：**

> 「Note This API is available only for MTP. It is defined in the header file /opt/93000mts/mts/execution_engine/include/MtpMemoryTest.h.」

- **`available only for MTP`** 是硬门槛：**不是 MTP 的环境里根本没有这个类**（不是「不支持」，是没有）。
- 头文件在 `/opt/93000mts/mts/execution_engine/include/` 下
  ——**`mts` 装在 `/opt`，这正是 MTP（Memory Test Plus）自己的包**（**`mts` 这个缩写的展开是本页的推断，原文没说**）。
- **⚠️ 这一句的排版有瑕疵**：`Note` 后面直接接正文，**没有冒号、也没有 `that`**
  （**和 `[[pste]]` 那一页记过的 `Note Do not confuse …` 是同一类**，见 `## 出处` ⚠️①）。

### 两个构造函数（**第二个是 hidden upload 专用**）

`## 语法 / 参数` 里逐字有两条，**本页不重抄**。要点是**它们不是「新旧」，是两条路**：

| 写法 | 什么时候用 | 逐字 |
|---|---|---|
| `MTP_MEMORY_TEST(void);` | 默认构造（Example 1–4 都是这条） | —— |
| `MTP_MEMORY_TEST(const std::string& resultArea);` | **配 hidden upload 用** | 「This constructor is used when using the Hidden upload algorithm in memory tests.」 |

**第二个构造函数的参数是真有内容的一句**（参数表逐字）：

> 「Name of a result area that you have previously defined.

> This result area stores the error map of a functional test.」

**读法**：传进去的是**「你已经定义好的」result area 名**，**它拿来存 functional test 的 error map**。
**所以 hidden upload 那条路的形状是：你先建好 result area → 把名字交给构造函数 → 后台线程往里算**
（Example 5 逐字就是这么写的，见 `## 典型用法` 第 5 条）。

### 三步：配置 → `execute()` → `judgeAndLog()`

**这是本页最该记住的形状**——Example 2 / 3 / 4 三条例子的骨架**逐字相同**：

| 步 | 调用 | 放在哪 |
|---|---|---|
| ① **配置** | `enableAddressBasedResults(...)` / `setImmediateBitmapToFile(...)` / `setFBCLimit(...)` … | **`ON_FIRST_INVOCATION_BEGIN()` 之前** |
| ② **执行** | `memoryTest.execute();` | `ON_FIRST_INVOCATION_BEGIN()` / `ON_FIRST_INVOCATION_END()` **之间**，**且前面有 `CONNECT();`** |
| ③ **判定与落盘** | `memoryTest.judgeAndLog();` | `ON_FIRST_INVOCATION_END()` **之后** |

**②③ 的分界线是三条例子一致给的**（Example 2、3 逐字相同；Example 4 在 ③ 之后接着取 failed addresses）。
**三条例子里都有同一句注释、且都在同一个位置**（`ON_FIRST_INVOCATION_BEGIN()` 上面那一行）：

> `// Execution is called only for first site`

**这句话的意思本篇没有展开**——**它说的是「这段只在第一个 site 上跑」还是「这条注释只是解释 `ON_FIRST_INVOCATION`」，
原文没有说**（§10：本页不替它选一个）。

**`ON_FIRST_INVOCATION_BEGIN()` / `CONNECT()` 都不是 MTP 的东西**（它们是 test method 的标准宏），
**本篇直接用了、一个字都没解释**。

### 那 41 个成员函数：本篇只给名字，一个都不解释

`#### Subtopics` 一节列了 **41 个**成员函数（`addAddressFilter()` … `waitTestDone()`），
**每一个都有自己的子主题**——**但本篇正文只解释了 0 个**，
**只有 5 个 Example 顺带用到了其中一部分**。
**⚠️ 这 41 篇子主题本页一篇都没读**（见 `## 出处`）——**这是本页最大的缺口。**

**本篇没有给分组。下表的分组是本页照函数名的字面做的**（**是读法，不是文档事实**），
**目的是让读者知道这 41 个名字落在哪几件事上**：

| 组（本页按名字归的） | 个数 | 成员 |
|---|---|---|
| **`setRA*`——冗余分析的整套配置** | **10** | `setRAAlgorithm`、`setRABeginAction`、`setRAConfigFile`、`setRACounting`、`setRAEnablingMode`、`setRAEndAction`、`setRAExecutionName`、`setRAGenerateOverlaidBfd`、`setRAResourceFaulty`、`setRAUseCountingResults` |
| **fail bit count / fail address** | **7** | `enableFailBitCount`、`setFBCLimit`、`setFailAddressListOrdering`、`setFailListStyle`、`setMaxFailingAddressesToLogPerPin`、`setMaxFailingAddressesToReconstructPerPin`、`setNumberOfFailCyclesToAcquirePerPin` |
| **bitmap 文件** | **6** | `addBitMapFileUserComments`、`generateBitmapFile`、`setBitMapFileName`、`setBitMapFilePath`、`setBitmapMode`、`setImmediateBitmapToFile` |
| **执行与生命周期** | **7** | `execute`、`judgeAndLog`、`print`、`isRepairable`、`startTest`、`waitTestDone`、`addAddressFilter` |
| **取东西（`get*`）** | **4** | `getMemoryPatternNamesList`、`getMemoryPort`、`getMemoryPortNamesList`、`getPassFailResult` |
| **结果的范围与开关** | **4** | `enableAddressBasedResults`、`setMultiPatternResultMode`、`setOptions`、`setResultPins` |
| **捕获窗口** | **3** | `restrictToChannelCaptureMemorySize`、`setStartCaptureCycle`、`setStopCaptureCycle` |
| 合计 | **41** | —— |

**这张表里能读出两件有用的事**（**都是本页的推断，标明**）：

- **「冗余分析」不是一条命令，是十个 `setRA*`**——**说明 redundancy analysis 在 MTP 里是一套要配的东西**
  （`setRAConfigFile` 要看配置文件、`setRABeginAction` / `setRAEndAction` 是首尾动作、
  `setRAResourceFaulty` 是资源标记…… **这些名字本身就能读出一层意思，但**本篇一个字都没解释它们）。
- **`startTest()` 与 `waitTestDone()` 是一对，`execute()` 是另一条**——
  **推断**：`execute()` 是阻塞的一条龙，`startTest()` / `waitTestDone()` 是把它拆成「起」和「等」。
  **依据**：`## Syntax` 里那句「Refer to Example 5 below or the example in `MTP_MEMORY_TEST.startTest()`
  for its usages.」——**hidden upload 那条路要的正是「不阻塞」的起法**。
  **但 `startTest()` 那一篇本页没读，所以这只是推断。**

## 典型用法

**⚠️ 先说明成色**：本篇**没有 `## Procedure`、没有 `## Before you begin`**，
正文只有 一句话简介 ＋ `## Syntax` ＋ `## Examples`（5 个）＋ `## Related information` ＋ `## Functional changes`。
**五条例子的代码逐字就在本页 `## 语法 / 参数` 里**（脚本收的，**本页不重抄**）——
**下面写的是「这五条例子各是什么形状、抄的时候要注意什么」。**

**1. 最小可用形状（Example 2）**：

```text
① 配置（block 外）  memoryTest.enableAddressBasedResults(true).setImmediateBitmapToFile(true);
② 执行（block 内）  ON_FIRST_INVOCATION_BEGIN(); { CONNECT(); memoryTest.execute(); } ON_FIRST_INVOCATION_END();
③ 判定（block 外）  memoryTest.judgeAndLog();
```

**这一条能直接抄**——**Example 2 是本篇五条例子里唯一一条本页没有发现问题的**（见 `## 出处` ⚠️）。

**2. 要 fail bit count，就加 `enableFailCount` ＋ 三级 `setFBCLimit`（Example 3）**：
三级分别是 **`DEVICE` / `PIN` / `BANK`**，**三个 × 一个上限**。
——**⚠️ 但 Example 3 的代码有两处瑕疵，照抄会踩**（行尾断链的点号、`MTP:DEVICE` 单冒号），
**见 `## 出处` ⚠️④**。**照抄前必须先按那一节改。**

**3. 要 failed addresses 那条路（Example 4），本篇给的顺序是「先设上限、再取、再遍历」：**

| 步 | 调用（逐字） | 本页能读出的 |
|---|---|---|
| 设上限 | `setMaxFailingAddressesToReconstructPerPin(1024);` | **和下面取的时候那个 `1024` 是同一个数**——**推断：两边要对上**（**原文没有明说这两个 1024 必须一致**） |
| 设排序 | `setFailAddressListOrdering(MTP:FAIL_CYCLE);` | **⚠️ 单冒号**，同一篇 Example 5 写的是 `MTP::BINARY_ENCODING`（双冒号） |
| 取 | `nr_addresses = march6n.getFailingAddressList("DQ_00",1024, addressList);` | **返回条数**，地址进 `ARRAY_ADDRESSES addressList` |
| 遍历 | `addressList[i].x` / `.y` / `.z` | **地址是三元组**（x/y/z），**本篇就这一处露出这个结构** |
| 出口 | `cout << msg.c_str();` 与 `PUT_DATALOG(msg.c_str());` | **一条去 report window、一条去 datalog** |
| 落盘 | `march6n.generateBitmapFile();` | **和 Example 2/3 的 `judgeAndLog()` 是两种不同的落盘** |

> **这一条路有一个版本坑，抄之前一定要看**：Example 4 用来拿 `march6n` 的那次调用是
> `.getMemroyPort("A").getMemoryPattern("march6n")`，
> **而 `getMemoryPattern()` 正是 `## Functional changes` 说 `MTP 3.2.1` 删掉的两个函数之一**
> ——**详见 `## 出处` ⚠️⑥**。**本页不替它调和，但会明确告你：照 Example 4 原样抄有版本风险。**

**4. 还有两个「查」的接口（Example 4 末段）**：**DQ index 与 pin name 可以互查**
（`…ByPinName(pinName)` 取 index；`getPinNameListByDQIndex(pinIdx)` 取名字）。
**⚠️ 这两个函数名在本篇里是坏的**（`DC/DC power units` 那一段），**见 `## 出处` ⚠️⑤。**

**5. hidden upload 那条路（Example 5）——形状和上面 1 完全不同：**

| 步 | 做法 | 依据 |
|---|---|---|
| ① 拿 suite 名当 result area 名 | `std::string resultArea;` ＋ `GET_TESTSUITE_NAME(resultArea);` | Example 5 前两行 |
| ② **用第二个构造函数** | `MTP_MEMORY_TEST memoryTest(resultArea);` | 与 `## Syntax` 那条对得上 |
| ③ 建 result area 并给足容量 | `RESULT_AREA_CONFIG_SET resConfSet(resultArea);` → `resConfSet.pin("@")` → `setErrorMapResultAreaSize(1024);` | **`pin("@")` 里那个 `@` ——推断是「所有 pin」；本篇没有解释它** |
| ④ 起后台线程 | `SMC_ARM(memoryTest);`（在 `FOR_EACH_SITE_BEGIN()` 里） | **注释逐字是 `// kick off calculation thread`** |
| ⑤ 把 ③ 步挪进后台 | `SMC_backgroundProcessing(MTP_MEMORY_TEST memoryTest)` 里做 `judgeAndLog();` ＋ `generateBitmapFile();` | **注释逐字是 `// hidden calculation`** |

**这一条路的关键差别**：**Example 2–4 里 `judgeAndLog()` 是紧接着 `execute()` 在同一个函数里调的；
Example 5 把它搬到了另一个函数里**——**这就是 hidden upload 省下来的时间**。

> **⚠️ 本页对这一条的保留**：Example 5 的 `SMC_backgroundProcessing` **是按值收对象的**
> （`MTP_MEMORY_TEST memoryTest`，不是引用），**而对象里存着一个 result area 名**。
> **本篇没有说 `MTP_MEMORY_TEST` 能不能拷贝**——
> **这是本页注意到的一个点，不是语料说的**（**没有编译过，`verified: doc-only`**）。
> **另外：这个构造函数的引入版本比其他都新，见 `## 版本`。**

**6. 本页答不上来的（**语料未写 / 本页未读**）：**
- **41 个成员函数的参数、取值、返回值**——**全在没读的子主题里**。
- **`MTP::DEVICE` / `MTP::PIN` / `MTP::BANK` 各该给什么数** —— 本篇只给了 Example 3 的 `100` / `10` / `10`，
  **没有说这三个数是什么意思**。
- **`@` 是什么意思**、`setErrorMapResultAreaSize(1024)` 里的 1024 和 Example 4 的 1024 有没有关系。
- **`isRepairable()` / `print()` / `setOptions()` / `setResultPins()` 各自怎么用**——本篇一个都没提。

## 和谁有关

### 本篇亲自点名的（**文档事实**）

| 本篇写的 | 链 | 依据（本篇） |
|---|---|---|
| `Hidden upload` | [[hidden-upload]] | `## Syntax` 里那句 `This constructor is used when using the Hidden upload algorithm in memory tests.` ＋ 那一处的相对链接 |
| `error map` | [[error-map]] | 参数表：`This result area stores the error map of a functional test.` |
| `SMC_ARM(...)` / `SMC_backgroundProcessing(...)` | [[smartcalc]]、[[smc-background-process-locks-config]] | **Example 5 的代码里**（`SMC_ARM(memoryTest);` 与 `SMC_backgroundProcessing(MTP_MEMORY_TEST memoryTest)`）。**⚠️ 本篇没有出现 `SmartCalc` 这个词组**——**只出现了 `SMC_` 前缀的函数名**，**所以「这就是 SmartCalc」是本页按前缀做的推断** |
| 名字里带 `pattern` 的一串 | [[pattern]]（**本页的 `stage`**） | `getMemoryPattern("march6n")`、`getMemoryPatternNamesList()`、`MTP_MEMORY_PATTERN` ——**本页的 `stage: pattern` 靠的就是这一串**（**这是本页的读法，见 `## 出处` 的「待复核」**） |
| `MTP_MEMORY_PATTERN` | **反引号 ＋ raw 路径** `02.12.06.15_MTP_MEMORY_PATTERN.md` | `## Related information`（**它不在 allowlist 里，故不链**） |
| `MTP_MEMORY_PORT` | **反引号 ＋ raw 路径** `02.12.06.16_MTP_MEMORY_PORT.md` | 同上（**也不在 allowlist 里**） |
| `RESULT_AREA_CONFIG_SET`、`RESULT_AREA_CONFIG_PINS`、`GET_TESTSUITE_NAME`、`ON_FIRST_INVOCATION_BEGIN`、`CONNECT`、`PUT_DATALOG`、`MsgStream` | **反引号** | Example 2 / 4 / 5 的代码 |

### 「相关」里最实的一条：`MTP_MEMORY_PORT` 是**子类**

`## Related information` 只给了两个名字，**但版本段把其中一个的关系说清楚了**：

> 「Two similar functions are provided with MTP_MEMORY_PORT, which is a new sub-class for MTP_MEMORY_TEST to support multiport.」

**所以本篇第 52 行的 `Multiport is supported` 和 `MTP_MEMORY_PORT` 这个子类是同一件事的两面**：
**multiport 是 3.2.1 靠新增一个子类做到的**，而 `getMemoryPattern()` 那一对被从 `MTP_MEMORY_TEST` 挪了过去。

**⚠️ 而这中间的层级关系本篇没有讲清楚**：`getMemoryPort()` 明明是 `MTP_MEMORY_TEST` 的成员
（子主题清单里有 `MTP_MEMORY_TEST.getMemoryPort()`），
Example 4 也确实是 `memoryTest.getMemroyPort("A").getMemoryPattern("march6n")` 这样一路走下去的
——**但「哪些函数留在了 `MTP_MEMORY_TEST`、哪些挪进了 `MTP_MEMORY_PORT`」本篇没有一张名单**（**本页不替它补**）。

### 本篇点名、但没有页、故用反引号的

- `MTP_MEMORY_PATTERN` / `MTP_MEMORY_PORT`（raw 路径见上表）——**本页没读这两篇**
  （**`## Related information` 里那两条链接之间连分隔符都没有，见 `## 出处` ⚠️⑦**）。
- `Hidden upload`（raw: `../02.07_Test_Method_Reference/02.07.10.04.05_Hidden_upload.md`）——**本页没读**。

### 本页没链的（**因为本篇一个字都没提**）

- [[mtp-maintenance-operations]]、[[mtp-shared-test-commands]]、[[mtpt]]——**这三个都在 allowlist 里、
  在 wiki 里也都有页**（**名字是从 allowlist 得知的**），**但本篇一个字都没提它们**，
  **所以本页不写它们和 `MTP_MEMORY_TEST` 的关系**（同属 MTP 这一族是**本页看名单看出来的，不是文档事实**）。
- [[smartrdi]]——**本篇没有点名 SmartRDI**。
  **两页各自都出现 `SMC_` 前缀**（本页 Example 5 用 `SMC_ARM`），
  **但「这是同一套后台机制」本页没有依据下结论**（**smartrdi 那一页的 `SMC_` 用法出自它自己那些**没读的子主题），
  **故不写成关系。**
- [[mtp-3.1.3]] / [[mtp-3.1.6]] / [[mtp-3.2.1]] / [[mtp-3.3.2]]——**它们是版本页，链在 `## 版本` 里**，
  **本页没读它们的内容**（只确认了它们在 allowlist 里、在 `wiki/versions/` 里存在）。

## 版本

**本文档有 `## Functional changes` 段，七条（逐字）：**

- `Introduced in MTP 3.1.3`
- `MTP 3.1.6: (MTP on SOC 103.3.0) New member functions addAddressFilter() and getMemoryPatternNamesList() are added.`
- `MTP 3.1.6: (MTP on SOC 103.3.0) New member function setMultiPatternResultMode() is added.`
- `MTP 3.2.1: Supports multiport and redundancy analysis.`
- `MTP 3.2.1: Removes the member functions: getMemoryPatternNamesList() and getMemoryPattern(). Two similar functions are provided with MTP_MEMORY_PORT, which is a new sub-class for MTP_MEMORY_TEST to support multiport.`
- `MTP 3.3.2: Pre-setups for using the MTP_MEMORY_TEST API have been automatically done by the system.`
- `MTP 3.3.2: Adds a new constructor syntax, MTP_MEMORY_TEST(const std::string& resultArea)`

**对应到 wiki 的版本页**（**本页没读它们，只按号对上**）：
[[mtp-3.1.3]] / [[mtp-3.1.6]] / [[mtp-3.2.1]] / [[mtp-3.3.2]]。

**读法（这一节有四件事要记住）：**

| 要点 | 说明 |
|---|---|
| **不是 §11.2 ② 那个哨兵** | 第一条是 `Introduced in MTP 3.1.3`——**带了产品名和号**，**不是 `Introduced before SmarTest 6.3.2` 那种「覆盖之前就有」的哨兵**。**所以这七条可以直读。** |
| **号有两层** | **`MTP 3.1.6` 后面还套了一个 `(MTP on SOC 103.3.0)`**——**原文没有说这两套号是什么关系**（§11.2 ④）。**看到 `103.3.0` 别把它读成 MTP 的第三个版本号。** |
| **API 是「先长后缩」的** | **3.1.6 加了三个函数**（`addAddressFilter`、`getMemoryPatternNamesList`、`setMultiPatternResultMode`）；**3.2.1 又把其中两个删了**（`getMemoryPatternNamesList`、`getMemoryPattern`）。**所以「名字出现过」不等于「这个版本里还在」**——**本页 ⚠️⑥ 那个 Example 4 的坑就是这么来的。** |
| **`resultArea` 这个构造函数很新** | **它是 3.3.2 才加的**（最后一条），**而 hidden upload 那条路（Example 5）依赖它**——**照 Example 5 抄，版本下限是 3.3.2。** |
| **3.3.2 还有一条「你什么都不用做了」** | `Pre-setups for using the MTP_MEMORY_TEST API have been automatically done by the system.` ——**⚠️ 原文没有说那些 pre-setups 是什么、3.3.2 之前要做什么**（**语料未写**）。**这一条和 Example 2–4 里那些 `enableAddressBasedResults(...)` 是不是同一批事，本页不知道。** |

> **MTP 其实还有另一条号线**：本 wiki 的 `wiki/versions/` 里有 `mtp-7.5.0` / `mtp-7.5.2` / `mtp-7.6.0`
> 这些版本页，**而本篇这一段一个 7.x 都没用**（**这是本页对 allowlist 与目录的观察，不是本篇的话**）。
> **两条号怎么并存，本篇没写、本页也不推断。**

## 出处

`sources:` 一篇：
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17_MTP_MEMORY_TEST.md`
（TDC `128974.htm`，**255 行**）

**本页没做的（按缺口大小排）：**

- **41 个子主题，一篇都没读。** 本篇的 `#### Subtopics`（第 10–50 行）逐条列了
  `02.12.06.17.01` … `02.12.06.17.41`——**这 41 个成员函数的参数、取值、返回值全在里面**。
  **这是本页最大的缺口**：**本页 `## 是什么` 那张分组表是按函数名归的，不是读出来的。**
- **`MTP_MEMORY_PATTERN`（`02.12.06.15`）与 `MTP_MEMORY_PORT`（`02.12.06.16`）没读**
  ——它们是 `## Related information` 的全部内容，
  **而 `MTP_MEMORY_PORT` 还是 3.2.1 为 multiport 新增的子类**。
- **`Hidden upload`（`../02.07_Test_Method_Reference/02.07.10.04.05`）没读**
  ——第二个构造函数的用法在那篇。
- **`MTP_MEMORY_TEST.startTest()`（`02.12.06.17.40`）没读**
  ——`## Syntax` 自己说 hidden upload 的用法可以看它的例子。
- **零张图。** 本篇没有图片引用。
- **没有 `## Procedure` / `## Before you begin`**——正文只有
  一句话简介 / `## Syntax` / `## Examples` / `## Related information` / `## Functional changes`。
  **所以 `## 典型用法` 是照五条例子的形状写的，不是照原文步骤抄的。**
- **加粗声明**：**本页正文没有手抄的语法块**——本篇的 `## Syntax` 与全部 5 个 Example
  **都被脚本收进了本页 `## 语法 / 参数`**（4,689 字符），**本页只在需要指出问题时才引用个别行**。
- **没有在任何真实 MTP 上跑过这个类**（`verified: doc-only`）。
  **Example 2–5 能不能编译、`SMC_ARM` 能不能接一个对象、`isRepairable()` 到底可用不可用，
  本页只能保证「文档这么写」（§11）。**

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> **① 第 54 行的 `Note` 排版**：逐字是 ` Note This API is available only for MTP.`
> ——**`Note` 后面直接接正文，没有冒号、也没有 `that`**。
> **同一现象在 `[[pste]]` 那一页记过**（`Note Do not confuse …`）——**这一族文档的 `Note` 有两种排版。**
>
> **② 第 62 行多了一个空格**：逐字是
> `This constructor creates an object for the MTP_ MEMORY_TEST() class.`
> ——**`MTP_` 后面那个空格是多的**，**应为 `MTP_MEMORY_TEST()`**（标题、正文别处、子主题清单都是连着的）。
> **这个空格让这一段的函数名没法被当成标识符搜到。**
>
> **③ 第 64 行的构造函数签名里参数名被反引号包着**：逐字是
> ``- `MTP_MEMORY_TEST(const std::string& `resultArea`);` ``
> ——**而第 60 行那条构造函数不带任何标记**。**同一个 `## Syntax` 段里两种风格。**
> **（这一条本页只记「不一致」，不判断哪个是原意。**）
>
> **④ Example 3（第 133–135 行）有两处代码问题**：
> - **行尾一个孤零零的点号，链在这里断了**：`  memoryTest.enableFailCount(true).`
>   ——**下一行 `  memoryTest.setFBCLimit(MTP:DEVICE,100).setFBCLimit(MTP:PIN,10)` 是新语句**，
>   **所以 `enableFailCount(true)` 后面那个 `.` 接不上任何东西。**
> - **`MTP:DEVICE` / `MTP:PIN` / `MTP:BANK` 是单冒号**，
>   **而同一篇 Example 5 第 228 行写的是 `MTP::BINARY_ENCODING`（双冒号）**
>   ——**同一个枚举命名空间在同一篇文档里两种写法。**
>
> **⑤ Example 4（第 170–212 行）有五处代码问题，其中一处是函数名拼错**：
> - **`memoryTest.getMemroyPort("A")`（第 170 行）——`Memroy` 应为 `Memory`。**
>   依据：**本篇子主题清单第 17 行逐字是 `MTP_MEMORY_TEST.getMemoryPort()`**。
> - **`msg << x =  << addressList[i].x << endl;`（第 180 行）——`x = ` 少了引号**，
>   **应为 `"x = "`**；y、z 两行（第 181–182 行）同样。
> - **`String pinName = "DQ_00";`（第 190 行）——`String` 不是本篇别处用的类型**
>   （**同段用 `STRING_VECTOR`，Example 5 用 `std::string`**）。
> - **`INT_VECTOR dqDC/DC power units = march6n. getDQDC/DC power unitsByPinName(pinName);`（第 191 行）**
>   ——**变量名和函数名里各有一处 `DC/DC power units`**，
>   **含空格与斜杠，不是 C++ 标识符能有的形状。**
>   **推断（标明是推断）：原文应是 `getDQIndexByPinName`**——
>   依据是**同一段的注释逐字写着 `// query dq index from pin name`**，
>   且**同段的姊妹函数 `getPinNameListByDQIndex(pinIdx)`（第 199 行）是完好的**。
>   **本页不据此声明「文档就是这么定义的」**——**能确定的是：这串字不能编译。**
> - **`march6N.setBitMapFileName("march6N");`（第 211 行）——对象名从 `march6n` 变成了 `march6N`**（大写 N），
>   **而同一段其它三行（第 209、210、212 行）都是 `march6n`**。
>
> **⑥ Example 4 用了一个 `## Functional changes` 说「已经删掉」的函数。**
> Example 4 第 170 行调用 `getMemoryPattern("march6n")`，
> 而版本段逐字说 `MTP 3.2.1: Removes the member functions: getMemoryPatternNamesList() and getMemoryPattern().`
> ——**同一个 `getMemoryPattern()`：版本段说 3.2.1 删了，例子里还在调。**
> **原文没有说这个例子是哪一版的**（§10：本页不替它调和）。
> **两种解释都说得通**：
> - **① 这个例子是 3.2.1 之前写的、没有被更新**；
> - **② 「删掉」指的是从 `MTP_MEMORY_TEST` 挪到 `MTP_MEMORY_PORT` 下**——
>   **后半句有依据**：同一条版本自己接着说
>   `Two similar functions are provided with MTP_MEMORY_PORT, which is a new sub-class for MTP_MEMORY_TEST to support multiport.`
>
> **本页不选一种当答案**——**但无论哪一种，照 Example 4 原样抄都有踩版本坑的风险**，
> **所以本页在 `## 典型用法` 第 3 条里明确标了出来。**
>
> **⑦ 第 262 行 `## Related information` 的两个链接之间零分隔。** 逐字是
> `[MTP_MEMORY_PATTERN](<02.12.06.15_MTP_MEMORY_PATTERN.md>)[MTP_MEMORY_PORT](<02.12.06.16_MTP_MEMORY_PORT.md>)`
> ——**没有换行、没有空格、没有列表标记、没有标点**。
> **同一现象在 `[[smartcalc-framework]]` 那一页也记过**（那边是四个链接连在一起）。
> **后果：这一节在渲染后是两个黏在一起的名字，人眼容易漏掉第二个。**
>
> **⑧ 版本段的号有两层，原文没有给对应关系**：`MTP 3.1.6` 后面套 `(MTP on SOC 103.3.0)`
> ——**这是 `## 版本` 那一节的主体，此处只做索引**（§11.2 ④：同一产品线的号还会跨版本并存）。
>
> **⑨ 版本段最后一条既没有句号、签名里的 `;` 也掉了**：逐字是
> `- MTP 3.3.2: Adds a new constructor syntax, MTP_MEMORY_TEST(const std::string& resultArea)`
> ——**前面六条都有句号**（第 266–271 行），**只有第 272 行没有**。
>
> **⑩ 本页在本篇里没有发现 `渭` / `碌` / `掳` / `鈥` 那一类坏字。**
> **但这是「本页读到的」，不是「本篇干净」**（§13.1 第 ⑥′：
> **一条检查绿，可能是因为它根本没查到东西**）。
> **⚠️ 但本篇不是没问题的**：上面 ①–⑨ 里有 **9 处**瑕疵，
> **其中 ④⑤ 是「照抄就会编译不过」，⑥ 是「照抄就会撞版本」**——
> **「没发现坏字」和「这篇干净」是两件完全不同的事。**

> **待复核（这不是语料瑕疵，是本页对骨架字段的核对，本页没有改任何字段）**：
> **`layer: L2` 本页核过，是对的**——依据：本篇逐字说这个类
> `is defined in the header file /opt/93000mts/mts/execution_engine/include/MtpMemoryTest.h`，
> 且五条例子的宿主函数都是 `void MemoryTest::run()` / `void SMCApiValidationTest::SMC_I_Mode()`，
> **是 C++ 测试方法里的 API**（`schema.md` 第 84 行的 `L2 — Test Method API`）。
> **`stage: pattern` 本页认为两边都说得通，故列出来留给维护者**：
> - **支持 `pattern`**：名字里带 `pattern` 的一串（`getMemoryPattern`、`getMemoryPatternNamesList`、
>   `MTP_MEMORY_PATTERN`）、`setFailAddressListOrdering(MTP::FAIL_CYCLE)`、bitmap——
>   **这些都是 pattern 域的坐标**；
> - **支持 `results`**：本篇的动词大多落在产出上——`Generates address-based results`、
>   `judgeAndLog()`、`getPassFailResult()`、`generateBitmapFile()`、`PUT_DATALOG()`。
>
> **本页不替它改，也不选一个当答案**——**记在这里供维护者复核。**

`verified: doc-only`
