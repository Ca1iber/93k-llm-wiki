---
type: object
title: SHARED_CONTINUITY_TEST
layer: n/a
stage: pin
tags: [mtp, api, driver-sharing, continuity, short-circuit, shared-pins, non-shared-pins, cross-terminated-pins, testmethod, mtp-3.1.3, mtp-3.1.5]
related: [mtp-shared-test-commands, sharing-configuration-file, sharing-configuration, mtp-memory-test, pin, testmethod, pin-utility, mtp-maintenance-operations, mtp-3.1.3, mtp-3.1.5]
sources:
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.21_SHARED_CONTINUITY_TEST.md
created: 2026-09-24
updated: 2026-09-28
verified: doc-only
---

# SHARED_CONTINUITY_TEST

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **3,653 字符逐字取自** `<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.21_SHARED_CONTINUITY_TEST.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Examples

### Note

The following examples demonstrate how to use this API within a test method. If you want to see a complete test method code via SHARED_CONTNUITY_TEST, find it in /opt/93000mts/mts/solution_tools/common/sh_lib/DriverSharing.tar.gz.

### Example 1

Performing the continuity and short circuits test for the shared, and non-shared pins.

```
#include "solution_tools.h"
#include "testmethod.hpp"
#include "mapi.hpp"

class CSharedContinuity: public testmethod::TestMethod
{
protected:
  virtual void run()
  {
    ON_FIRST_INVOCATION_BEGIN();
    {
      // Always do initialization at the beginning of test
      mTest.init();

      // hand over the parameters to the test class
        mTest.pinNonShared("DQ_Bus,DQS_DiffBus,DM")
             .forceCurrentNonShared(100 uA)
             .pinCross("Clock_Bus")
             .forceCurrentCross(100 uA)
             .sharingConfigFile("default.cfg")
             .pinShared("Addr_Bus,Command_Bus")
             .forceVoltage(1.1)
             .terminationDPS("VTERM")
             .supplyDPS("VDD,VDDQ")
             .settlingTime(0)
             .output(MTP::OUTPUT_REPORT_UI);

      // execute the test
      mTest.execute();
    }
    ON_FIRST_INVOCATION_END();

    // set result
    mTest.judgeAndLog();

    // Print out in the UI Report Window.
    mTest.print();
  }

private:
  SHARED_CONTINUITY_TEST mTest;
};
```

### Example 2

Customizing the output.

```
#include "solution_tools.h"
#include "testmethod.hpp"
#include "mapi.hpp"

class CSharedContinuity: public testmethod::TestMethod
{
protected:
    virtual void run()
    {
      ON_FIRST_INVOCATION_BEGIN();
      {
        // Always do initialization at the beginning of test
        mTest.init();

        // hand over the parameters to the test class
        mTest.pinNonShared("DQ_Bus,DQS_DiffBus,DM")
             .forceCurrentNonShared(100 uA)
             .pinCross("Clock_Bus")
             .forceCurrentCross(100 uA)
             .sharingConfigFile("default.cfg")
             .pinShared("Addr_Bus,Command_Bus")
             .forceVoltage(1.1)
             .terminationDPS("VTERM")
             .supplyDPS("VDD,VDDQ")
             .settlingTime(0)
             .output(MTP::OUTPUT_REPORT_UI);

        // execute the test
        mTest.execute();
      }
      ON_FIRST_INVOCATION_END();

      // set result
      mTest.judgeAndLog();

      // Print out in the UI Report Window.
      STRING_VECTOR pinSharedNames =
        PinUtility.getDigitalPinNamesFromPinList("Addr_Bus,Command_Bus", TM::ALL_DIGITAL, TRUE);
      STRING_VECTOR pinNonSharedNames =
        PinUtility.getDigitalPinNamesFromPinList("DQ_Bus,DQS_DiffBus,DM", TM::ALL_DIGITAL, TRUE);
      STRING_VECTOR pinCrossNames =
        PinUtility.getDigitalPinNamesFromPinList("Clock_Bus", TM::ALL_DIGITAL, TRUE);

      cout << "Test result of site " << CURRENT_SITE_NUMBER() << ": " << mTest.getPassFail() << endl;

      for (STRING_VECTOR::const_iterator it = pinSharedNames.begin();
           it != pinSharedNames.end(); ++it)
      {
        cout << "PIN (" << *it << ")\t" << mTest.getPassFail(*it) << "\t" << mTest.getValue(*it) << endl;
      }

      for (STRING_VECTOR::const_iterator it = pinNonSharedNames.begin();
           it != pinNonSharedNames.end(); ++it)
      {
        cout << "PIN (" << *it << ")\t" << mTest.getPassFail(*it) << "\t" << mTest.getValue(*it) << endl;
      }

      for (STRING_VECTOR::const_iterator it = pinCrossNames.begin();
           it != pinCrossNames.end(); ++it)
      {
        cout << "PIN (" << *it << ")\t" << mTest.getPassFail(*it) << "\t" << mTest.getValue(*it) << endl;
      }
    }

private:
    SHARED_CONTINUITY_TEST mTest;
};
```

<!-- 语法节 end -->

## 是什么

**`SHARED_CONTINUITY_TEST` 是 MTP 给「有 driver sharing 的 DUT」做连通性与短路测试的 C++ 类 API。**
原文的定义句把范围一句话说完了：

> 「The SHARED_CONTINUITY_TEST class provides an API for checking the continuity and finding the
> short circuits for the DUTs with driver sharing. **It tests shared, non-shared, and
> cross-terminated pins in a single pass.**」

**最后半句是它存在的理由**：三类针——**shared / non-shared / cross-terminated**——
**一次 pass 全测完**，不用分三次跑。

### 三类针，三种加力方式，三条 limit

| 针的类别 | setup 链上成对出现的两个调用 | 必须加的那条 limit（字面字符串） |
|---|---|---|
| **shared pins** | **`pinShared(pinlist)` + `forceVoltage(v)`** | `"Shared Voltage(mv)"` |
| **non-shared pins** | **`pinNonShared(pinlist)` + `forceCurrentNonShared(current)`** | `"Non-Shared Voltage(mv)"` |
| **cross-terminated pins** | **`pinCross(pinlist)` + `forceCurrentCross(current)`** | `"Cross-Terminated Voltage(mv)"` |

**配对方式值得记一笔**：**shared 那一类加电压（`forceVoltage`），另外两类加电流**
（`forceCurrentNonShared` / `forceCurrentCross`）。**三条 limit 的说明句结构完全相同**，
都是 `Defines the minimum and maximum pass voltages (mv) for the` 后面接自己的那一类针名
（`shared pins.` / `non-shared pins.` / `cross-terminated pins.`）——
**也就是说三类最后都是按电压判的**，non-shared / cross 那两类虽然加的是电流，
判的仍是电压。

> ⚠️ **三条 limit 名里写的都是小写 `mv`**，不是 `mV`。**这是要照着敲的字面量，别自己改成 `mV`。**
> 原文如此，本页照抄（[[mtp-shared-test-commands]] 已记过同一件事）。

### 用它的两个硬前提

原文把「自建 test method 时你该做什么」写成两条（`When you use this API to create your own custom test method, you should:`）：

1. **按测试针加上面那三条 limit**——加法与取值落在
   `How to create a universal test method class`（**本页没读**）。
2. **把 driver sharing API 的库和头文件 include 进来**——
   `Include the driver sharing API library and header file to complete a test method code.`
   细节在 `Setting up for using driver sharing APIs`（**本页没读**）。

**外加一条可用性边界**，原文用 `Note` 单独框出来：

> 「**The SHARED_CONTINUITY_TEST API is available only for MTP.**」

**所以它不是通用 93K API。** 头文件路径也印证这一点：

> 「This API is defined in the header file
> `/opt/93000mts/mts/solution_tools/common/include/SHARED_CONTINUITY_TEST.h`.」

**在 `solution_tools` 下**——和 [[pin-property-monitor]] 那种 `soc/prod_com` 的 MAPI 族**不是一支**。

### 同一个测试，MTP 给了三种做法（本页是 ②）

原文自己写了一个三选一（`There are two other methods to check the shared continuity:`）：

| | 做法 | 原文说的适用场合 |
|---|---|---|
| **①** | **`SharedContinuity` test method**（MTP 自带） | `Use it when you Do not have special requirements such as a customized testing algorithm or a special output format.` 原文还加一句 **`It is the easiest way to develop a test.`** |
| **②** | **`SHARED_CONTINUITY_TEST`**（**本页**） | **自建 test method、要定制算法或输出格式时** |
| **③** | **`MTP_CONTINUITY_TASK`** API | `Use it when you want to test the pins (either shared, non-shared or cross-terminated pins) with different test conditions in one test method.` |

**②和③的差别原文没有在本篇展开**，它只留了一句话：

> 「More differences between the SharedContinuity test method, SHARED_CONTINUITY_TEST, and
> MTP_CONTINUITY_TASK are described in MTP_CONTINUITY_TASK.」

**那一篇本页没读**，所以「什么时候该用 ②、什么时候该用 ③」**本页答不了**。
**注意原文 ① 那条里的 `Do` 是大写**——原文如此，本页照抄。

### 类定义：17 个成员函数，分四组

原文 `## Class definition` 的分组（**上面「语法 / 参数」节只收了 `## Examples`，没收这一段**，
所以这张表是本节补的）：

| 组 | 成员函数 |
|---|---|
| **构造函数** | `SHARED_CONTINUITY_TEST ()` |
| **Initial**（1 个） | `init()` |
| **Setup**（11 个，**全部返回类引用**） | `sharingConfigFile(filename)` / `pinShared(pinlist)` / `forceVoltage(voltage)` / `pinNonShared(pinlist)` / `forceCurrentNonShared(current)` / `pinCross(pinlist)` / `forceCurrentCross(current)` / `terminationDPS(dps)` / `supplyDPS(dps)` / `settlingTime(time)` / `output(MTP::OUTPUT_TYPE)` |
| **Execute**（1 个，`void`） | `execute()` |
| **Result**（5 个重载 / 4 个函数） | `judgeAndLog()` / `print (const ostream &out=std::cout) const` / `getPassFail()` / `getPassFail(pin)` / `getValue(pin)` |

**Setup 那 11 个全部返回 `SHARED_CONTINUITY_TEST &`，就是为了一路 `.` 挂下去**；
`execute()` 返回 `void`，所以链到它为止。

**17 这个数**＝ 1（init）+ 11（setup）+ 1（execute）+ 4（result 那四个函数，`getPassFail` 算两个重载）
＝ **17 个成员函数**，也正是本篇 `#### Subtopics` 列出的条数。[[mtp-shared-test-commands]] 也记的是 17。

### ⚠️ setup 链的**例子顺序**和**清单顺序**不一样

同一篇文档里出现了两种顺序，**并列如下，本页不判哪个对**：

| | 顺序 |
|---|---|
| **`Setup functions:` 那一组** | `sharingConfigFile` → `pinShared` → `forceVoltage` → `pinNonShared` → `forceCurrentNonShared` → `pinCross` → `forceCurrentCross` → `terminationDPS` → `supplyDPS` → `settlingTime` → `output` |
| **Example 1 的调用链** | `pinNonShared` → `forceCurrentNonShared` → `pinCross` → `forceCurrentCross` → `sharingConfigFile` → `pinShared` → `forceVoltage` → `terminationDPS` → `supplyDPS` → `settlingTime` → `output` |

**差别在「配好三类针」和「配 sharing config」谁先**（清单是 config 先、例子里是三类针先），
**其余 7 个的先后完全一致**。

> **原文一个字都没说顺序有要求。** 那 11 个都返回类引用、是给链式调用设计的，
> **（推断）**顺序应当无关——**但依据只是「两个顺序都出现在同一篇里、且原文没给约束」，
> 本页没有正面依据，用时按原文例子写最稳。**

### 结果侧：四个口，两个在类外

- **`judgeAndLog()`** —— 原文注释 `// set result`（判 + 记）。
- **`print()`** —— 原文注释 `// Print out in the UI Report Window.`。
- **`getPassFail()` / `getPassFail(pin)`** —— 整体判 / 按针判。
- **`getValue(pin)`** —— 按针取值。

**两个要注意的地方**：

- **这些函数写在 `ON_FIRST_INVOCATION_END()` 之外**（例子里 setup + `execute()`
  包在 `ON_FIRST_INVOCATION_BEGIN()` / `END()` 里，取结果在块外）——
  **即每个 site 都取一遍**。
- **`print` 的签名写的是 `const ostream &out=std::cout`**——形参是 `const ostream`。
  **（这条原文如此，是上游的写法，见 `## 出处`）**「往一个 const 流里写」在 C++ 里说不通，
  **原文没解释，本页也不替它改**。

## 典型用法

**1. 调用的形状是四段：`init()` → 链式 setup → `execute()` → 取结果。**

- **`init()` 必须第一个调**——原文例子的注释：`// Always do initialization at the beginning of test`。
- 原文对这段写法还加了一句说明：`// hand over the parameters to the test class`，
  **也就是「参数在链上交给测试对象」**。
- **`execute()` 之后才轮到 `judgeAndLog()` / `print()`**。

**2. 用之前先做两件事**（本篇 `When you use this API to create your own custom test method, you should:`
那两条，见上面「是什么」）：**加三条 limit** + **include driver sharing 的库与头文件**。

**3. 三类针的配法**（照 Example 1 的形态）：
`pinNonShared("DQ_Bus,DQS_DiffBus,DM")` 配 `forceCurrentNonShared(100 uA)`；
`pinCross("Clock_Bus")` 配 `forceCurrentCross(100 uA)`；
`pinShared("Addr_Bus,Command_Bus")` 配 `forceVoltage(1.1)`。
**pin list 是逗号分隔的字符串**，不是数组。

**4. 要定制输出**：原文 Example 2 给的就是这个。它的做法是
**用 [[pin-utility]] 把三类 pin list 摊成针名**
（`PinUtility.getDigitalPinNamesFromPinList(pinlist, TM::ALL_DIGITAL, TRUE)`），
**再逐针调 `mTest.getPassFail(*it)` 与 `mTest.getValue(*it)`**，
自己 `cout` 成想要的格式——**这就是 ② 存在的意义（① 的格式是固定的）**。

**5. 完整的 test method 代码从哪来**：原文 `### Note` 给了一个压缩包路径
`/opt/93000mts/mts/solution_tools/common/sh_lib/DriverSharing.tar.gz`
（**只是一个路径，包不在语料里**）。

**6. `sharingConfigFile()` 传什么**：例子里是 `"default.cfg"`——
**一个相对文件名**。它该放在哪，**本篇没写**；
[[sharing-configuration-file]] 那一页记着「多处引用文档把路径写成 `<device directory>/configuration/`」
——**那条依据在那一页，不在本页；本页不重复那边的规矩。**

## 和谁有关

- [[mtp-shared-test-commands]] — **本页的上位页**：它把 `SHARING_CONFIGURATION` /
  `SHARED_CONTINUITY_TEST` / `SHARED_LEAKAGE_PARALLEL_TEST` 三个放在一起讲三选一，
  而 **`02.12.06.21_SHARED_CONTINUITY_TEST.md` 正是它 `sources:` 里的三篇之一**。
  **两页必须口径一致**；本页是这一个类的专页，挖得更深（类定义、两种顺序、结果侧）。
- [[shared-leakage-parallel-test]] — **平行兄弟**：漏电侧的同一个形状（一次 pass 三类针）。
  本篇 `Related information` **没有列它**（它在另一篇里），
  所以「同族」这条来自 [[mtp-shared-test-commands]] 的三篇并置，**不是本篇的一句话**。
- [[sharing-configuration-file]] — **上游输入**：`sharingConfigFile(filename)` 传的就是这个文件。
  那一页里已经写了它和 `terminationDPS()` / `supplyDPS()` 的关系。
- [[sharing-configuration]] — 同族：读同一个文件的另一个类（**只读数据、不测东西**）。
- [[pin-utility]] — **Example 2 直接用它的成员**：
  `PinUtility.getDigitalPinNamesFromPinList(pinlist, TM::ALL_DIGITAL, TRUE)`
  把三类 pin list 摊成针名，再喂给 `getPassFail` / `getValue`。
- [[pin]] / [[testmethod]] — **对象与宿主**：测的是针；宿主是 test method
  （`init()` / `execute()` / 结果那一套都在 `run()` 里）。
- [[mtp-memory-test]] — **MTP 章根**；本页是它下面 `02.12.06` 那一支的 API 页。
- [[mtp-maintenance-operations]] — 同批建的 MTP 页（不同支：那份讲 pattern 侧的刷新）。
- [[mtp-3.1.3]] / [[mtp-3.1.5]] — **版本页**：本页 `## 版本` 的两条分别落在它们上。
- `SharedContinuity test method` / `SharedContinuity syntax`（**均未建**）— 上面三选一里的 **①**，
  **本页没读**，所以「① 的参数怎么填」本页没有。
- `MTP_CONTINUITY_TASK`（**未建**）— 三选一里的 **③**；**②③ 的具体差别就在那一篇里，本页没读**。
- `Setting up for using driver sharing APIs` / `How to create a universal test method class`（**均未建**）—
  上面那两条前提的落点；**本页都没读**。
- **17 篇成员函数子主题一篇都没读**（`init()` / `sharingConfigFile()` / `pinShared()` / `forceVoltage()` /
  `pinNonShared()` / `forceCurrentNonShared()` / `pinCross()` / `forceCurrentCross()` /
  `terminationDPS()` / `supplyDPS()` / `settlingTime()` / `output()` / `execute()` /
  `judgeAndLog()` / `print()` / `getPassFail()` / `getValue()`）——
  **本页对它们只有签名和分组**，**每个参数的取值范围、默认值、限制一条都没有**。

## 版本

**⚠️ 这一节的版本号是 MTP 版本号，不是 SmarTest 版本号**（和 [[mtp-shared-test-commands]] 同一个坑）。
本 wiki 别处写的多是 `SmarTest 7.2.0` 这种，**这里写的是 `MTP 3.1.x`，两套编号不可比。**

原文 `## Functional changes` 两条：

- **`Introduced in MTP 3.1.3`**
- **`MTP 3.1.5: Added new API: MTP_CONTINUITY_TASK.`**

> **第二条记的是「另一个 API」的新增，却挂在本篇底下。**
> `MTP_CONTINUITY_TASK` 是三选一里的 ③，**不是本页这个类的成员**。
> **本页照实转述，没有把它挪走**——原文就是写在这儿的。
> **[[mtp-shared-test-commands]] 已经记过同一现象，两页口径一致。**
>
> 另外：**本页的 `Introduced in` 不是哨兵值**（不是 §11.2② 那种 `before SmarTest 6.3.2`），
> 它给的是确切版本 `MTP 3.1.3`。
>
> **本篇没有给出 ② 相对 3.1.3 之后的任何变更**——所以「这个类此后没改过」这种话
> **不能从本篇推出来**，只能说明本文档没记。

## 出处

`sources:` 一篇：
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.21_SHARED_CONTINUITY_TEST.md`
（`129122.htm`，**10,535 字节，230 行**）——**整篇读完**。

**本页没做的**：

- **17 篇成员函数子主题一篇都没读**（清单见「和谁有关」最后一条）。
  **所以每个 setup 函数的参数范围、默认值、`MTP::OUTPUT_TYPE` 有哪些取值、
  `settlingTime` 的单位、`terminationDPS` / `supplyDPS` 传什么——本页全都没有。**
- **`MTP_CONTINUITY_TASK` 没读**（三选一里的 ③）——**②③ 的差别本页答不了**。
- **`SharedContinuity` test method 及其 syntax 没读**（①）。
- **`Setting up for using driver sharing APIs` / `How to create a universal test method class` 没读**——
  上面那两条前提**只有名字，没有步骤**。
- **`DriverSharing.tar.gz` 那个包不在语料里**（原文只给了路径字符串）。
- **本文档没有 `## Procedure`、没有 `## Before you begin`**，所以「典型用法」那一节
  是从 `When you use this API to create your own custom test method, you should:` 和两个 Example 里拼出来的。

**图**：**本篇没有图**——`raw/129122.htm` 里 `src=` 只有 `tdc.js`，md 里 `.png` / `.jpg` 引用数为 0。
**所以本页没有图证，也没有「图够不着」这类话。**

**核了上游 `.htm`：`raw/129122.htm`（19,333 字节）。结论按「转换坏的 / 上游就坏的」分开：**

**① 上游就坏的（救不回来）：**

- **`Shared Voltage(mv)` 用小写 `mv`**：上游出现 **2 次**，`mV` 出现 **0 次**。
- **`SHARED_CONTNUITY_TEST`（少了 `I`）**：上游出现 **1 次**，就在 `### Note` 那句里。
  **它落在本页「语法 / 参数」节里（脚本逐字抽的那段），所以那一节里也有它——
  那一节不许改，本页只能在这里记一笔。**
- **`print` 的形参写成 `const ostream`**：上游那个链接的锚文本就是
  `void print (const ostream &amp;out=std::cout) const`，逐字如此。
- **子主题清单里写的是 `SHARED_CONTINUITY_TEST().print()`**（类名后面跟一对圆括号），
  而同一篇的类定义里写的是 `void print (const ostream &out=std::cout) const`。**两种写法并存，上游如此。**
- **`## Examples` 的 `### Note` 里那行路径**：上游把它包在
  `<span class="filepath">` 里，**换行位置与 md 不同**（md 里那句是一整行）。
- **`MTP 3.1.5: Added new API: MTP_CONTINUITY_TASK.` 挂在本文档底下**：上游 `<div class="changes">` 里就是这样。

**② 转换坏的（可救）：**

- ⚠️ **`Note` 那一块的边界丢了**。上游是独立的一块
  `<div class="note"><span class="title">Note</span> The SHARED_CONTINUITY_TEST API is available only for MTP.</div>`，
  **在 md 里被粘进了上一条列表项的尾巴**：上一条列表项以
  `Setting_up_for_using_driver_sharing_APIs.md>)` 结尾，**后面直接就是 `.Note The SHARED_CONTINUITY_TEST API is available only for MTP.`**
  —— `Note` 与它前面那句的句号之间**连一个换行都没有**。
  **本页正文引用那句话时只引后半句（连续的、合法的截取）。**
- ⚠️ **`## Related information` 四条链接被挤成了一行**，中间**一个分隔符都没有**：
  那一行依次是 `[SharedContinuity test method]`、`[SharedContinuity syntax]`、
  `[MTP_CONTINUITY_TASK]`、`[Setting up for using driver sharing APIs]` 四个 Markdown 链接，
  **首尾直接相接**（第一条的 `>` 后面紧跟第二条的 `[`）。
  上游是**四个独立的 `<div>`**。**本页没有引用这一行**（照那样的串引用会连「没有分隔符」一起引进引文）。
- ⚠️ **`<a>` 的 `title` 属性全被丢了**。上游每个成员函数链接都带一句说明，例如
  `<a href="129176.htm" title="The getPassFail() member function of SHARED_CONTINUITY_TEST retrieves pass/fail results for all pins, or a specified pin in a shared continuity test.">bool getPassFail (void) const</a>`，
  以及 `print` 那条的 `title="The print() member function of SHARED_CONTINUITY_TEST prints the test results of a shared continuity test to a standard output (It is the UI report window in SmarTest), or others."`。
  **md 里只剩签名，一句说明都没有。**
  **所以「本篇成员函数没有说明」不是原文没有，是转换丢的。**
  **本页正文没有把这些 `title` 当依据用**——只在这里记明它们存在。
- ⚠️ **`02.12.06.21.15_SHARED_CONTINUITY_TEST__.print.md` 这个文件名里是两个下划线**——
  上游的链接文字是 `SHARED_CONTINUITY_TEST().print()`，
  转换时把 `()` 压成了 `_`，于是 `_().` 变成 `__`。
  **（这一条 [[mtp-shared-test-commands]] 已经记过，两页一致。）**

`verified: doc-only`
