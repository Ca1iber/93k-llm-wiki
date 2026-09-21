---
type: object
title: GET_FUNCTIONAL_RESULT()
layer: L2
stage: testmethod
tags: [testmethod, l2, api, functional-test, result, multiport, sequencer-context, fail-cycles, datalog]
related: [test, testset, primary-status, flush, prlt, dps-aux-pin-task, execution-context, on-first-invocation-begin, task-list, mapping-testmethod]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.88_GET_FUNCTIONAL_RESULT.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# GET_FUNCTIONAL_RESULT()

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **9,575 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.88_GET_FUNCTIONAL_RESULT.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

Note GET_FUNCTIONAL_RESULT() should reside outside the `ON_FIRST_INVOCATION block`（raw: `02.07.04.01.138_ON_FIRST_INVOCATION_BEGIN.md`）. Any action which restarts the sequencers will erase the functional results.

-

Functions returning Boolean:

```
Boolean GET_FUNCTIONAL_RESULT(void);
Boolean GET_FUNCTIONAL_RESULT(const STRING& pin);
Boolean GET_FUNCTIONAL_RESULT(const STRING& pin, const STRING& context);
Boolean GET_FUNCTIONAL_RESULT(const STRING& port, const STRING& labelName, TM::FUNCIONAL_RESULT_TYPE type);
```

 Note To retrieve the result of specified label and port, the `TM::FUNCIONAL_RESULT_TYPE`（raw: `02.07.04.01.88_GET_FUNCTIONAL_RESULT.md#_29400__div_FUNCIONAL_RESULT_TYPE`） type must be set to TM::FTST_BURST.
-

Functions returning the result as `FUNC_TEST_BURST_RESULT`（raw: `02.07.04.01.88_GET_FUNCTIONAL_RESULT.md#_29400__p_FUNC_TEST_BURST_RESULT`）:

```
void GET_FUNCTIONAL_RESULT(const STRING& port,
                           std::vector<FUNC_TEST_BURST_RESULT>& ret, bool bReadPinFailCycles = false);

void GET_FUNCTIONAL_RESULT(const STRING_VECTOR& portlist,
                           const STRING& sequencer_execution_context,
                           std::vector<FUNC_TEST_BURST_RESULT>& ret, bool bReadPinFailCycles = false);

void GET_FUNCTIONAL_RESULT(const STRING& port,
                           const STRING& sequencer_execution_context,
                           std::vector<FUNC_TEST_BURST_RESULT>& ret, bool bReadPinFailCycles = false);
```

This API is defined in the header file /opt/hp93000/soc/prod_com/include/MAPI/Execute.h.

  Parameters

 | Parameter  | Description |
 | pin

port

  | Defines the pin name of which the functional test result shall be retrieved.

For multiport testing, a port name can be specified instead of a single pin.

If this parameter is omitted (first syntax only), TRUE is returned only if all pins have passed, else FALSE is returned.

 |
 | portlist  | List of string elements defining ports and set up as `STRING_VECTOR`（raw: `02.07.04.02.15_STRING_VECTOR.md`）.

The portlist is to be used if the functional test results for more than one port shall be retrieved.

 |
 | context  | The `execution context`（raw: `../02.06_Command_Reference/02.06.07.01.08.05.03.02.03_Using_execution_contexts.md`） of the last executed test for that context. |
 | sequencer_execution_context  | The sequencer execution context, see `SEQUENCER_CONTEXT`（raw: `02.07.04.01.201_SEQUENCER_CONTEXT.md`） and `SEQUENCER_CONTEXT_ITEM`（raw: `02.07.04.01.202_SEQUENCER_CONTEXT_ITEM.md`）. |
 | labelName  | Specifies the label of which the functional test result will be retrieved. |
 | type  | The value type FUNCIONAL_RESULT_TYPE defines the type of the functional result.Currently the type can only be TM::FTST_BURST for retrieving the burst result of the multiport test.

```
namespace TM

    typedef enum
    {
        FTST_BURST

    }FUNCTIONAL_RESULT_TYPE;
```

 |
 | ret  | The result of type FUNC_TEST_BURST_RESULT containing the executed label, the start cycle, the pass/fail result and the optional fail cycles map of the execution.

ret is an already defined vector of type TM::FUNC_TEST_BURST_RESULT that is handled as reference.

TM::FUNC_TEST_BURST_RESULT is defined as follows:

```
typedef struct
{
    STRING labelname;
    int id;
    int startCyc;
    int numberOfCycles;
    bool result;
    std::map<std::string, int> failCyclesMap;
    int isFailCyclesValid;

} FUNC_TEST_BURST_RESULT;
```

 | Return value  | Description |
 | labelname  | The name of the executed label. |
 | id  | Index of the label within the burst. id is set to 0 for the first label. |
 | startCyc  | The start cycle of the label within the burst. |
 | numberOfCycles  | The number of cycles of the label. |
 | result |

Returns a TRUE or FALSE.

If multiple pins or a port has been passed all containing pins must pass to return a TRUE. If any of the pins fail a FALSE is returned.

 |
 | failCyclesMap  | A map containing the name of failing pins as string and the number of fail cycles as int.

The map is filled only if parameter `bReadPinFailCycles`（raw: `02.07.04.01.88_GET_FUNCTIONAL_RESULT.md#_29400__r_bReadPinFailCycles`） has been set to TRUE.

 |
 | isFailCyclesValid |

The parameter shows the state of filling the failCyclesMap:

-

-1: The pin fail cycles were not read. The function was called with parameter bReadPinFailCycles set to FALSE.

-

0: The pin fail cycles were read but are not valid (`ERCC?`（raw: `../02.06_Command_Reference/02.06.02.02.110_ERCC__-__ERror_in_Cycle_range_Count.md`） valid_code flag was OVFL or LESS).

1: The pin fail cycles were read successfully.

   | |
 | bReadPinFailCycles  | The optional parameter initiates filling the failCyclesMap of parameter `ret`（raw: `02.07.04.01.88_GET_FUNCTIONAL_RESULT.md#_29400__r_ret`） if set to TRUE.The default value is FALSE.Note Use this parameter with caution. Filling the fail cycles map with data that must be read from the hardware may significantly increase the test time.  |   Return value There are two types of functions for this API:

- Boolean

The pass/fail result is returned as Boolean:

  - TRUE if the selected pin or all pins of the selected ports have passed the functional test or
  - FALSE if any of the selected pins or any pin of the selected ports has failed the functional test.

- void

These functions have no return value. The requested data is returned by a parameter of type FUNC_TEST_BURST_RESULT that is to be defined in the calling function and transferred as reference. For more information refer to parameter `ret`（raw: `02.07.04.01.88_GET_FUNCTIONAL_RESULT.md#_29400__r_ret`） and `Example 3`（raw: `02.07.04.01.88_GET_FUNCTIONAL_RESULT.md#_29400__Example_3`）.

### Example 1

In the following example the result of PIN1 will be retrieved and stored in the result variable after executing `FUNCTIONAL_TEST()`（raw: `02.07.04.01.75_FUNCTIONAL_TEST.md`）.

```
ON_FIRST_INVOCATION_BEGIN();

    FUNCTIONAL_TEST();

ON_FIRST_INVOCATION_END();

Boolean result = GET_FUNCTIONAL_RESULT("PIN1");
```

### Example 2

This example retrieves the result of all pins involved in that PPMU measurement.

```
TASK_LIST Ppmu_task;

//
// Add the measurement settings to Ppmu_task;
//

ON_FIRST_INVOCATION_BEGIN();

    Ppmu_task.execute();

ON_FIRST_INVOCATION_END();

Boolean result = GET_FUNCTIONAL_RESULT();
```

### Example 3

The following example returns the result of all executed patterns.

```
std::vector<FUNC_TEST_BURST_RESULT> mpResult;

ON_FIRST_INVOCATION_BEGIN();

    FW_TASK("DCRM OVEM,LMAP,,(@@)");

    FUNCTIONAL_TEST();

    FW_TASK("DCRM OVEM,FCM,,(@@)");

ON_FIRST_INVOCATION_END();

GET_FUNCTIONAL_RESULT("dig12_dc1Port", mpResult);

for ( uint i = 0; i < mpResult.size(); i++ )
{
    FUNC_TEST_BURST_RESULT funcTestRes = mpResult[i];

    cout << "Result for label " << funcTestRes.labelname << ": "
         << (funcTestRes.result==true ? "true" : "false" ) << endl;
}
```

### Example 4

The following example illustrates how to retrieve a functional result of a test executed using `GET_FUNCTIONAL_RESULT()`（raw: `02.07.04.01.88_GET_FUNCTIONAL_RESULT.md`） on a special sequencer context.

```
STRING sContext = "global";

ON_FIRST_INVOCATION_BEGIN();

    SEQUENCER_CONTEXT_ITEM context1(sContext);

    context1.setPorts("port1");

    SEQUENCER_CONTEXT context;

    context.add(context1).apply();

    CONNECT();

    FW_TASK("DCRM OVEM,LMAP,,(@@)");

    START_TEST(sContext);

    int a, b;

    WAIT_TEST_DONE(36000, &a, &b ,sContext);

    FW_TASK("DCRM OVEM,FCM,,(@@)");

ON_FIRST_INVOCATION_END();

std::vector<FUNC_TEST_BURST_RESULT> result;

GET_FUNCTIONAL_RESULT("port1", sContext, result);

cout << endl << "*** Current Site number: " << CURRENT_SITE_NUMBER() << " ***" << endl;

for ( uint i = 0; i < result.size(); i++ )
{
    FUNC_TEST_BURST_RESULT funcTestRes = result[i];

    cout << "Result for label " << funcTestRes.labelname << ": "
         << (funcTestRes.result==true ? "TRUE" : "FALSE" ) << endl;

    cout << "startCycle: " << funcTestRes.startCyc << endl << "numberOfCycles: "
         << funcTestRes.numberOfCycles << endl << "----------------------------------------------------" << endl;
}

DISCONNECT();
```

### Example 5: Reading the number of fail cycles per pin

The following example shows how to read the number of fail cycles per pin. Note Use parameter bReadPinFailCycles with caution. Filling the fail cycles map with data that must be read from the hardware may significantly increase the test time.

```
ON_FIRST_INVOCATION_BEGIN();
{
    ...
    ...

    FW_TASK("DCRM OVEM,LMAP,,(@@)");

    FUNCTIONAL_TEST();
}
ON_FIRST_INVOCATION_END();

vector<FUNC_TEST_BURST_RESULT> mpResult;

GET_FUNCTIONAL_RESULT("Port_1", mpResult, true);

for (uint labelIndex = 0; labelIndex < mpResult.size(); labelIndex++)
{
    FUNC_TEST_BURST_RESULT funcTestRes = mpResult[labelIndex];

    cout << "Label " << funcTestRes.labelname << endl;
    cout << endl;
    cout << "\tResult:\t\t\t"        << (funcTestRes.result==true ? "true" : "false" ) << endl;
    cout << "\tisValidFailCycles:\t" << funcTestRes.isFailCyclesValid << endl;
    cout << endl;
    cout << "\tfailCyclesMap:" << endl;
    cout << endl;

    map<string, int>::iterator iterator;

    for (iterator = funcTestRes.failCyclesMap.begin(); iterator != funcTestRes.failCyclesMap.end(); ++iterator)
    {
        cout << "\t\tFail cycles for pin " << iterator->first << " : " << iterator->second << endl;
    }

    cout << endl;
}
```

The code above results in the following output if failing pins have been found:

```
Label ...

    Result:            false
    isValidFailCycles: 1

    failCyclesMap:

        Fail cycles for pin ... : ...
        Fail cycles for pin ... : ...
        ...
```

<!-- 语法节 end -->

## 是什么

**`GET_FUNCTIONAL_RESULT()` 是 L2 的「读上一次测量结果」API。** 它自己第一段就把「上一次」的外延说清了（逐字）：

> 「Returns the pass/fail result of the last measurement. The measurement can be either a functional test, PPMU, SPMU or DPS measurement. The function can as well return the pass/fail result of the last functional test executed in a multiport burst pattern or return the pass/fail result for a specific pin and a specific execution context.」

**三件事藏在第一段里**：① 它读的不只是功能测试，**PPMU / SPMU / DPS 测量的结果也能读**；② **multiport burst** 模式下的功能测试结果它也能给；③ 结果可以**按 pin 要、也可以按 execution context 要**。

**定义在哪个头文件**：

> 「This API is defined in the header file /opt/hp93000/soc/prod_com/include/MAPI/Execute.h.」

### 一族两形态：返回 `Boolean` 的 4 个重载，和往 `vector` 里写的 3 个重载

| 形态 | 语法 | 拿到什么 |
|---|---|---|
| **Boolean** | `GET_FUNCTIONAL_RESULT(void)` / `(const STRING& pin)` / `(const STRING& pin, const STRING& context)` / `(const STRING& port, const STRING& labelName, TM::FUNCIONAL_RESULT_TYPE type)` | **一个 pass/fail** |
| **void** | `(const STRING& port, std::vector<FUNC_TEST_BURST_RESULT>& ret, bool bReadPinFailCycles = false)` / 同上带 `STRING_VECTOR& portlist` / 同上带 `const STRING& sequencer_execution_context` | **每个 label 一条 `FUNC_TEST_BURST_RESULT`，写进调用方自己定义的 vector** |

**无参那个重载的语义是「全 pass 才 TRUE」**：

> 「If this parameter is omitted (first syntax only), TRUE is returned only if all pins have passed, else FALSE is returned.」

**void 那一族的语义**：

> 「These functions have no return value. The requested data is returned by a parameter of type FUNC_TEST_BURST_RESULT that is to be defined in the calling function and transferred as reference.」

**多 pin 归并规则**（Boolean 形态）：

> 「If multiple pins or a port has been passed all containing pins must pass to return a TRUE. If any of the pins fail a FALSE is returned.」

### `FUNC_TEST_BURST_RESULT` 的七个字段（逐字见上面 `语法 / 参数` 节的 struct）

| 字段 | 含义（原文） |
|---|---|
| `labelname` | 「The name of the executed label.」 |
| `id` | 「Index of the label within the burst. id is set to 0 for the first label.」 |
| `startCyc` | 「The start cycle of the label within the burst.」 |
| `numberOfCycles` | 「The number of cycles of the label.」 |
| `result` | pass/fail（见上面那条多 pin 归并规则） |
| `failCyclesMap` | 「A map containing the name of failing pins as string and the number of fail cycles as int.」 |
| `isFailCyclesValid` | 下面这条三态 |

**`isFailCyclesValid` 是「这张 map 可不可信」的三态开关**（逐字）：

> 「-1: The pin fail cycles were not read. The function was called with parameter bReadPinFailCycles set to FALSE.」

> 「0: The pin fail cycles were read but are not valid (ERCC? valid_code flag was OVFL or LESS).」

> 「1: The pin fail cycles were read successfully.」

**读 fail cycle 要显式开口，而且有代价**：

> 「The map is filled only if parameter bReadPinFailCycles has been set to TRUE.」

> 「Note Use this parameter with caution. Filling the fail cycles map with data that must be read from the hardware may significantly increase the test time.」

### 三条会让结果作废的规则（这一页最该背的部分）

**① 打开这个开关的动作本身不算作废，但别的命令会**：

> 「Pass/fail results that are retrieved by command PRLT are invalidated by commands CSAS and PSAS.」

> 「We recommend therefore using the command PRLT directly after the related functional test and before command CSAS or PSAS are performed.」

**② 同一条规则也管 API，不是只管命令**：

> 「This behavior applies not only to the commands but also to the related APIs: Function GET_FUNCTIONAL_RESULT() must be performed before any of the DPS_AUX_PIN_TASK.check...() functions is called or the results of GET_FUNCTIONAL_RESULT() are invalid.」

（那句里的 `check...()` 是**原文自己的省略写法**，指的是 `DPS_AUX_PIN_TASK.check` 开头的**一族**函数——本页没有把它展开，因为原文没展开。）

**③ 改了 sequencer context 就读不到，要先恢复**：

> 「Changing the SEQUENCER_CONTEXT will invalidate the results that are read by API GET_FUNCTIONAL_RESULT().」

> 「The original sequencer start label must be restored by API Primary.label() followed by a FLUSH() before the results are read by GET_FUNCTIONAL_RESULT().」

**④ 必须待在 first-invocation 块外**：

> 「GET_FUNCTIONAL_RESULT() should reside outside the ON_FIRST_INVOCATION block. Any action which restarts the sequencers will erase the functional results.」

**这四条合起来的读法**：**功能测试结果是一份「会被抹掉」的状态**，不是可以随时回来取的容器；**凡是重启 sequencer 或改写 context 的动作，都在抹它。**

### multiport 的那条专用语法要配对的枚举

> 「To retrieve the result of specified label and port, the TM::FUNCIONAL_RESULT_TYPE type must be set to TM::FTST_BURST.」

**而这个枚举目前只有一个取值**——见上面参数表 `type` 那格：`Currently the type can only be TM::FTST_BURST for retrieving the burst result of the multiport test.`（**「目前只有一种」是文档事实**，不是本页的推断。）

## 典型用法

**文档没有 `## Procedure` 段**；五个 Example 覆盖了五种用法，本页把它们按「你手上有什么」排成五条（**排序是本页做的（推断）**，例子本身都是逐字引的）。

**1. 跑完功能测试就读单个 pin 的结果**（Example 1）——**测试在块里、读结果在块外**，这是全篇最要紧的形状：

> 「In the following example the result of PIN1 will be retrieved and stored in the result variable after executing FUNCTIONAL_TEST().」

**2. 读一次 PPMU 测量里所有 pin 的结果**（Example 2）——测量由 [[task-list]] 的 `execute()` 触发，读结果用**无参**重载：

> 「This example retrieves the result of all pins involved in that PPMU measurement.」

**3. 读 multiport burst 里每个 label 的结果**（Example 3）——用 `port` + `vector` 那个重载，然后逐条遍历：

> 「The following example returns the result of all executed patterns.」

**4. 读「特定 sequencer context 下」的结果**（Example 4）——**这一条把前面③那条规则补全了**：例子里先建 `SEQUENCER_CONTEXT_ITEM context1(sContext)`、`context1.setPorts("port1")`，再用 `SEQUENCER_CONTEXT context; context.add(context1).apply();` 应用，然后才 `START_TEST(sContext)` / `WAIT_TEST_DONE(36000, &a, &b ,sContext)`，最后 `GET_FUNCTIONAL_RESULT("port1", sContext, result);`：

> 「The following example illustrates how to retrieve a functional result of a test executed using GET_FUNCTIONAL_RESULT() on a special sequencer context.」

**5. 读每个 pin 的 fail cycle 数**（Example 5）——**唯一一个要用 `bReadPinFailCycles = true` 的例子**：

> 「The following example shows how to read the number of fail cycles per pin.」

输出的形状原文也给了（`Result:` / `isValidFailCycles:` / `failCyclesMap:` 三行，`isValidFailCycles: 1` 表示读成功了）：

> 「The code above results in the following output if failing pins have been found:」

**顺序约束速查**（四条规则的落点，全部来自上面「是什么」里那几段）：

| 你想读的 | 必须满足 | 谁会让它作废 |
|---|---|---|
| 功能测试结果 | 调用点在 `ON_FIRST_INVOCATION_BEGIN/END` **块外** | 任何重启 sequencer 的动作 |
| 经固件命令读的结果 | `PRLT` 紧跟在功能测试之后 | `CSAS` / `PSAS` |
| 经 API 读的结果 | 在 `DPS_AUX_PIN_TASK.check...()` 一族**之前** | 那些 `check...()` 调用 |
| 指定 context 的结果 | 先 `Primary.label()` + `FLUSH()` 把原始 start label 恢复 | 改 `SEQUENCER_CONTEXT` |

**常见的组合**：**`ON_FIRST_INVOCATION` 块里做测量（`FUNCTIONAL_TEST()` / `PPMU_task.execute()` / `START_TEST`+`WAIT_TEST_DONE`），块外一行 `GET_FUNCTIONAL_RESULT` 取值**——五个例子里有四个是这个形状。

## 和谁有关

**入边 55 条 / 44 篇（含 1 条 `index.md` 的 toc），出边 32 条 / 21 个目标**——取自 `extract/edges.jsonl`（`resolved=true`；**这是链接证，不是本页 sources 的正文**）。

- [[test]] — **分工（本页的读法，不是哪一篇给的总纲）**：TEST 判并记、本 API 按 pin / port 取结果。**边表里两篇之间只有单向的 2 条边**（`02.07.04.01.241_TEST.md` → 本页）；**本页 32 条出边的 21 个目标里没有 `TEST`，本页 `## Related information` 那 8 个目标里也没有 `TEST`**（两处都回 raw 与 `extract/edges.jsonl` 数过）。**TEST 那篇本页没读。**
- [[primary-status]] — **恢复手段**：`Primary.label()` 是「把原始 start label 弄回来」的那一步，后面必须再跟一次 [[flush]]。
- [[flush]] — 同上，`FLUSH()` 是那条恢复链的第二半。
- [[prlt]]（**未建**）/ `CSAS` / `PSAS` — **作废链**：本页 `## Syntax` 前面那段 note 的两个主角（`CSAS` 与 `PSAS` 在 raw 里是 L1 命令页的链接，**本页没读它们**）。
- [[dps-aux-pin-task]] — **顺序上的对手**：本页的结果必须在 `DPS_AUX_PIN_TASK.check...()` 一族之前取；**出边里那 4 条 `DPS_AUX_PIN_TASK.check*Error` / `checkPowerFlags` / `checkSurgeTracker` 都链回本页**，可见这条先后关系是双向被提到的。
- [[execution-context]] / `SEQUENCER_CONTEXT` / `SEQUENCER_CONTEXT_ITEM`（后两个**清单外**，见下面「出处」）——**context 三件套**：`context` 参数、`sequencer_execution_context` 参数、以及被改动作废结果的那个对象。
- [[testset]] — **继任族**：`TESTSET__.judgeAndLog_FunctionalTest` 也链到本页（入边 1 条）。
- [[task-list]] — **上游**：Example 2 的测量就是用 `PPMU_task.execute()` 触发的（本页 raw 的 Example 2 里逐字有这一行）。**但 `02.07.04.01.240_TASK_LIST.md` 的 13 条出边里没有一条指向本页**（实测 `extract/edges.jsonl`）——**所以这条关系只有本页一侧的证据；TASK_LIST 那篇本页没读。**
- [[on-first-invocation-begin]] — **共存规则**：块里做测量、块外读结果。
- `STRING_VECTOR`（**清单外**）— `portlist` 参数的类型。
- `SMC_FUNCTIONAL_TEST()` / `SMC_EXECUTE_TEST()` / `SMC_DIGITAL_CAPTURE_TEST()` / `SMC_EXECUTE_TMU_TEST()`（**均清单外**）— 本页出边指向的**后台线程（SMC）版本**，见 [[smartcalc-framework]]。
- [[mapping-testmethod]] — 那张跨层对照表里，「判定并写 datalog」那一行的 L2 格写的是 [[test]] / [[testset]] / [[limit]]，**本页不在那一格里**——本页管的是「**取结果**」，不是「判并记」。

**入边最密的一族是 `02.07.04.01.63.*` 与 `02.07.04.01.227.*`**（DC event 与 SHMOO_RESULT 那两族，各 4~5 条），**说明「读上一次结果」这个动作在事件与 shmoo 的 API 里也常被提到**；**最密的一篇是 `02.07.04.01.201_SEQUENCER_CONTEXT.md`（3 条）**——正是上面③那条规则的对手篇。

## 版本

`## Functional changes` 段六条（逐字）：

- `Introduced before SmarTest 6.3.2`
- `SmarTest 7.2.1: Returns result of functional test executed in a multiport burst pattern.`
- `SmarTest 7.2.1: New return value startCyc`
- `SmarTest 7.3.1: New return value numOfCyc`
- `SmarTest 7.4.2: New syntax using parameter portlist`
- `SmarTest 7.5.1: New optional parameter initiates reading of the pin fail cycles`

**第一条是哨兵值，不是「6.3.2 新增」**（`wiki/schema.md` §11.2②：全语料 2,677 条可用性行都写同一个版本号、措辞都是 `before`，意思是「本套文档集覆盖范围开始之前就有了」）。

**能落地的三条**：**7.2.1 才有了 multiport burst 的读法**（**所以 7.2.1 之前没有 `type` 那条专用语法**）；**7.4.2 才加了 `portlist` 重载**；**7.5.1 才加了 fail cycle 的读取**（**即 `bReadPinFailCycles` 与 `failCyclesMap` 是 7.5.1 起才有的**）。

## 出处

`sources:` 一篇，**整篇读完**（343 行 / 12,601 字节）：

- `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.88_GET_FUNCTIONAL_RESULT.md`
  （TDC topic `29400.htm`，头文件 `MAPI/Execute.h`）

**本页怎么读的这一篇**：开头三段 note（PRLT/CSAS/PSAS、SEQUENCER_CONTEXT、first-invocation）、`## Syntax`（两族语法 + 参数表 + struct）、`## Examples`（5 个）、`## Related information`（8 个目标）、`## Functional changes`（6 条）**全部读过**；引文没有一句来自本页 sources 之外。

**本页没做的**：

- **没有读那个 struct 以外的任何定义文档**：`SEQUENCER_CONTEXT`、`SEQUENCER_CONTEXT_ITEM`、`STRING_VECTOR`、`Primary.label()`（[[primary-status]]）、[[flush]]、`PRLT` / `CSAS` / `PSAS`、[[dps-aux-pin-task]]、`FUNCTIONAL_TEST()`、`START_TEST()`、`EXECUTE_TEST`、`DIGITAL_CAPTURE_TEST`、四个 `SMC_*` **一篇都没读**。**所以「怎么改 context」「`FLUSH()` 具体做什么」这类问题，本页一个字都没有。**
- **没有读 [[test]] 里指向本页的那两处细节之外的任何东西**——**TEST 与 GFR 的分工是本页从两篇各自的正文里并列出来的，不是哪一篇给的总纲。**
- **没有开过图**：**这一篇的 raw（md 与上游 `raw/29400.htm`）里一张图都没有**——实测 `<img>` 0 个、`.png` 引用 0 个，**所以本页没有任何图证可写**。**不是「图够不着」**（`wiki/schema.md` §11.4 已更正那条错说法），**是这一篇里没有图**。
- **没有实跑**：没跑过 multiport / 多 context 的测试，**没在第一台机子上验证过「改 context 之后结果真的读不出来」**。`verified: doc-only` 指的就是这件事。
- **没有动 `wiki/index.md`**，也没有把本页挂进 `wiki/stages/testmethod.md`。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：

> ① **同一个类型名两种拼法**：散文里写 `FUNCIONAL_RESULT_TYPE`（少一个 `T`），而代码块里写的是 `}FUNCTIONAL_RESULT_TYPE;`——**同一篇文档里 `FUNCIONAL` 与 `FUNCTIONAL` 并存**。**引文与 `语法 / 参数` 节里本页一律照原样留**（`语法 / 参数` 节里那几处 `FUNCIONAL` 都是脚本逐字抽出来的，本页一个都没改；**raw 里 `FUNCIONAL` 一共出现 4 次、`FUNCTIONAL_RESULT_TYPE` 出现 1 次**——**实测数过**）。**哪个是正式拼法，语料没说。**

> ② **版本记录里的名字与 struct 字段名不一致**：`## Functional changes` 写 `SmarTest 7.3.1: New return value numOfCyc`，**而 struct 里的字段叫 `numberOfCycles`、返回值表的行头也是 `numberOfCycles`**。**两处并列，本页不判哪个改名过、也不替它们统一。**

> ③ **缺空格的紧贴**（三处，本页原样引，**一处都没有用省略号接过去**）：`The optional parameter initiates filling the failCyclesMap of parameter ret if set to TRUE.` 后面紧跟 `The default value is FALSE.`、再接 `Note Use this parameter with caution.`——**`TRUE.` 与 `The`、`FALSE.` 与 `Note` 之间都没有空格**；另一处是 `The value type FUNCIONAL_RESULT_TYPE defines the type of the functional result.Currently the type can only be TM::FTST_BURST`（`.Currently` 同样紧贴）。

> ④ **参数表里 `pin` 与 `port` 被并进同一格**：raw 的形状是 `pin` 换行 `port` 换行 `  | Defines the pin name of which the functional test result shall be retrieved.`——**两个参数名挤在一个单元格里**，本页 `语法 / 参数` 节保留这个形状（§4：脚本抽的不许改），**本页正文按语义当成两个参数读**（那是本页的读法，**推断**）。

> ⑤ **`namespace` 那一段代码块是残缺的**：raw 是 `namespace TM` 换行 `    typedef enum` 换行 `    {` 换行 `        FTST_BURST` 换行 空行 `    }FUNCTIONAL_RESULT_TYPE;`——**`namespace` 后面没有花括号**（本页 `语法 / 参数` 节里逐字保留了它）。**语料如此，本页不补。**

> ⑥ **`## Syntax` 里有多处只有一个 `-` 的裸行**（分段符），本页 `语法 / 参数` 节照原样留着——**那不是本页的列表符，是语料的形状。**

**本页三类话的边界**（§11 的三分）：`文档事实` = 所有 `> 「…」` 引文，以及表里标了「原文」的格；`推断` = 正文里每一处标了（推断）的句子（**除这些以外本页没有别的主张**）；`建议` = **本页一句都没有**。

`verified: doc-only`
