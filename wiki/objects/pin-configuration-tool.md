---
type: object
title: Pin configuration tool
layer: gui
stage: pin
tags: [gui, pin, setup, pin-configuration, editor, pin-settings, context, utility-line, alias-set]
related: [pin, pin-configuration-file, pin-configuration-master-file, setup-management-tool, digital-pins-editor, dps-pins-editor, utility-pins-editor, utility-purpose-editor, pin-group-editor, port-editor, alias-set-editor, dc-scale-limits-editor, ground-sense-editor, protocol-editor, mapping-pin]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18_Pin_configuration_tool.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# Pin configuration tool

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **10,095 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18_Pin_configuration_tool.md>` 及其子主题 `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.02.07.01_Virtual_pins.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.02.08.03_Editing_an_expression-based_group.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01.01_Context_list.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01.02_Digital_Pins_editor.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01.03_DPS_Pins_editor.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.03_Port_Editor.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.13_Filter_line.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.14_Sorting_rows.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.04_Pin_configuration_file.md>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.05_Pin_configuration_master_file.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Examples（取自子主题 Using the Pin Configuration Tool › Working with pins › Virtual pins）

### Using virtual pins in test methods with judgeAndLog_ParametricTest.

The following example illustrates how virtual pins are used in a test method using judgeAndLog_ParametricTest().

`VP0001` and `VP2000` are virtual pins.

```
#include "testmethod.hpp"
#include "mapi.hpp"

/**
 * Test method class.
 *
 * For each testsuite using this test method, one object of this
 * class is created.
 */
class ExampleVirtualPinsParametricTest: public testmethod::TestMethod {

protected:

  /**
   *Initialize the parameter interface to the testflow.
   *This method is called just once after a testsuite is created.
   */
  virtual void initialize()
  {
  }

  /**
   * This method is invoked per site.
   */
  virtual void run()
  {
     string tSuiteName,ttestName;
     GET_TESTSUITE_NAME( tSuiteName );
     cout << "\n\n------------  TestVirtualPins.cpp (" << tSuiteName << ")  ---------\n\n";

     ARRAY_D values(2);
     LIMIT limits;

     /* Define example limits */
     limits.low(TM::GE,11); limits.high(TM::LE,22);

     /* Define example measurement values */
     values[0]=11;
     values[1]=22;

     /* Log results against the virtual pins VP0001 and VP2000 */
     TESTSET().judgeAndLog_ParametricTest("VP0001, VP2000", "VPIN_TEST1", limits, values);

     return;
  }

  /**
   *This function will be invoked once the specified parameter's value is changed.
   *@param parameterIdentifier
   */
  virtual void postParameterChange(const string& parameterIdentifier)
  {
    return;
  }

  /**
   *This function will be invoked once the Select Test Method Dialog is opened.
   */
  virtual const string getComment() const
  {
    string comment = " please add your comment for this method.";
    return comment;
  }
};
REGISTER_TESTMETHOD("ExampleVirtualPinsParametricTest", ExampleVirtualPinsParametricTest);

```

### Using virtual pins in test methods with judgeAndLog_ScanTest()

The following example illustrates how virtual pins are used in a test method using judgeAndLog_ScanTest().

`VP0001` and `VP2000` are virtual pins.

```
#include "testmethod.hpp"

//for test method API interfaces
#include "mapi.hpp"
using namespace std;

/**
 * Test method class.
 *
 * For each testsuite using this test method, one object of this
 * class is created.
 */
class TestVirtualPinsScan: public testmethod::TestMethod {

protected:
     int mSetToFail;
     string mAlarmMsg;
  /**
   *Initialize the parameter interface to the testflow.
   *This method is called just once after a testsuite is created.
   */
  virtual void initialize()
  {
    //Add your initialization code here
    //Note: Test Method API should not be used in this method!
  }

  /**
   *This test is invoked per site.
   */
  virtual void run()

  {
     SCAN_TEST_RESULT scanResult(TM::CYCLE_BASED_LOGGING);

     scanResult.totalFailures(4);
     scanResult.totalCyclesExecuted(64);

     /*
      * Virtual Pins, the setup provides VP0001..VP2000.
      * The first and last of 2000 Virtual Pins are also tested.
      */

     STRING_VECTOR pins = {"VP0001","VP2000"};
     ARRAY_CHAR expected(4);

     expected[0] = 'L';
     expected[1] = 'L';
     expected[2] = 'H';
     expected[3] = 'H';
     scanResult.pin(pins[0]).expectedData(expected);

     expected[0] = 'H';
     expected[1] = 'L';
     expected[2] = 'L';
     expected[3] = 'H';
     scanResult.pin(pins[1]).expectedData(expected);

     ARRAY_LL cycles(4);

     cycles[0] = 0;
     cycles[1] = 0;
     cycles[2] = 1;
     cycles[3] = 1;

     scanResult.pin(pins[0]).failingCycles(cycles); /* Exp: LLHH, Rcv: 0011 */
     scanResult.pin(pins[1]).failingCycles(cycles); /* Exp: HLLH, Rcv: 0011 */

     /**
      * Push failures to datalog, the virtual pin names should be logged
      * instead of "no_pin_name_given"
      */
     TESTSET().cont(true).judgeAndLog_ScanTest(scanResult);

     return;
  }

  /**
   *This function will be invoked once the specified parameter's value is changed.
   *@param parameterIdentifier
   */
  virtual void postParameterChange(const string& parameterIdentifier)
  {
    //Add your code
    //Note: Test Method API should not be used in this method!
    return;
  }

  /**
   *This function will be invoked once the Select Test Method Dialog is opened.
   */
  virtual const string getComment() const
  {
    string comment = " please add your comment for this method.";
    return comment;
  }
};
REGISTER_TESTMETHOD("TestVirtualPinsScan", TestVirtualPinsScan);

```

### Example（取自子主题 Using the Pin Configuration Tool › Working with pin groups › Editing an expression-based group）

A group contains all the input pins (all_in), without the pin I/O7. So the expression is all_in - I/O7.

After selecting I type, the steps for building such expression are:

- Click group all_in in the Available Group/Pin List and then click operator + Union. This results in the following group expression. !`Edit an Group Expression (1)`（raw: `../../../../agent-html/21668.png`）
- Click pin I/O7 in the Available Group/Pin List and then click operator - Difference. This results in the final group expression. !`Edit an Group Expression (2)`（raw: `../../../../agent-html/21669.png`）
- To evaluate the group expression, click Evaluate. The pins are printed to the Group Members area. !`Group Expression Result`（raw: `../../../../agent-html/21667.png`）

### Example（取自子主题 Elements of the Pin Configuration Tool › Pin setting editors › Context list）

The figure below illustrates an invalid allocation of contexts which are mixed.

 !`Incorrect Allocation of Contexts - Invalid Setup`（raw: `../../../../agent-html/56188.png`）

The figure below shows a valid context configuration where the context you allocated to the pins has also been allocated to the corresponding timing, level and vector label.

 !`Correct Allocation of Contexts - Valid Setup`（raw: `../../../../agent-html/56189.png`）

### Examples（取自子主题 Elements of the Pin Configuration Tool › Pin setting editors › Digital Pins editor）

### DC Scale pin (PMU mode) setup

The following table shows an example configuration for DC Scale pins in PMU mode.

| Name | Type | Mode | HW | Connection Set | Comment | Tester Channel |
|---|---|---|---|---|---|---|
| Vdd_1 | dc | SIG | DCS-DPS128HC |  |  | 10104 |
| Vdd_2 | dc | SIG | DCS-DPS128HC |  |  | 10105-10106 |

### Utility DC pin setup

  !`Utility DC pin setup`（raw: `../../../../agent-html/355197.png`）

### Example（取自子主题 Elements of the Pin Configuration Tool › Pin setting editors › DPS Pins editor）

See `DC Scale pin (DPS mode) setup`（raw: `02.08.04.18.03.01.03.01_DC_Scale_pin__DPS_mode__setup.md`）

### Example（取自子主题 Elements of the Pin Configuration Tool › Port Editor）

The following picture shows a port Port_IO consisting of eight pins.

In the Available Pin List, the "鈭? character preceding with the pin name means that this pin has been added to Port_IO.

 !`Port Example`（raw: `../../../../agent-html/97848.png`）

### Example（取自子主题 Elements of the Pin Configuration Tool › Filter line）

When you type I/O in the filter line of the Pin Name column, all the pins whose names include I/O are shown.

 !`Filter Example`（raw: `../../../../agent-html/97823.png`）

### Example（取自子主题 Elements of the Pin Configuration Tool › Sorting rows）

The following examples sort the Pin Name column in ascending and descending order.

 !`Sort in Ascending Order`（raw: `../../../../agent-html/97825.png`）  !`Sort in descending order`（raw: `../../../../agent-html/97826.png`）

### Example（取自子主题 Pin configuration file）

- The figures below show the pin setting and the contents of the related pin configuration file. !`A mixed-signal pin configuration example - digital pins`（raw: `../../../../agent-html/21671.png`）   !`A mixed-signal pin configuration example - DPS pins`（raw: `../../../../agent-html/105641.png`）   !`A mixed-signal pin configuration example - analog pins`（raw: `../../../../agent-html/105640.png`）

```
hp93000,config,0.1
DFPN 10208,"108",(IAQ_D8)
DFPN 10207,"107",(IAQ_D7)
DFPN 10206,"106",(IAQ_D6)
DFPN 10205,"105",(IAQ_D5)
DFPN 10204,"104",(IAQ_D4)
DFPN 10203,"103",(IAQ_D3)
DFPN 10202,"102",(IAQ_D2)
DFPN 10201,"101",(IAQ_D1)
DFPN 10403,"",(WDA_TRIG)
DFPN 10401,"",(WDB_TRIG)
DFPS 11,POS,(VCC1)
DFPS 12,POS,(VEE)
DFPS 14,POS,(DRC_IN_TERM)
DFAN "MCB231,1,i","232",(input_a_1)
DFAN "MCB231,2,i","234",(input_a_2)
PSTE 1
CONF OFF,F160,(IAQ_D8,IAQ_D7,IAQ_D6,IAQ_D5,IAQ_D4,IAQ_D3,IAQ_D2,IAQ_D1,
    WDA_TRIG,WDB_TRIG)
RDIV 0,(IAQ_D8,IAQ_D7,IAQ_D6,IAQ_D5,IAQ_D4,IAQ_D3,IAQ_D2,IAQ_D1,
    WDA_TRIG,WDB_TRIG)
DDSL 0,(VCC1)
DDSL 0,(VEE)
DDSL 0,(DRC_IN_TERM)
PSLC 0.1,(VCC1,VEE,DRC_IN_TERM)
NOOP "6.1.0",,,
```

- The following lines shows a multi-port pin configuration file. The firmware command DFPT is used to define ports.

```
hp93000,config,0.1
DFPN 10102,"12",(CP_1)
DFPN 10302,"12",(CP_2)
...
DFPT (CP_1,DS7_1,DS0_1,I/O7_1,I/O6_1,I/O5_1,I/O4_1,I/O3_1,I/O2_1,
    I/O1_1,IO0_1,Q7_1,Q0_1,S1_1,S0_1,_MR_1), (port_1)
DFPT (CP_2,DS7_2,DS0_2,I/O7_2,I/O6_2,I/O5_2,I/O4_2,I/O3_2,I/O2_2,
    I/O1_2,I/O0_2,Q7_2,Q0_2,S1_2,S0_2,_MR_2), (port_2)
...
```

Note You can use a text editor instead of the Pin Configuration Tool to create or edit a pin configuration file in the form of a set of firmware commands.

### Examples（取自子主题 Pin configuration master file）

### package.cfg

The following example shows how the Setup Management Tool assembles three pin configuration files according to the master file.

The file `package.cfg` is the package file, and the other two files, `TRANSIO.cfg` and `USB.cfg,` are the alias files.

```
hp93000,config,0.1
DFPN 10201,"",(Data_in_2)
DFPN 10202,"",(Data_in_1)
DFPN 10212,"",(Data_in_5)
DFPN 10213,"",(Data_in_4)
DFPN 10214,"",(Data_in_3)
PSTE 1
CONF OFF,F160,(Data_in_2,Data_in_1,Data_in_5,Data_in_4,Data_in_3)
RDIV 0,(Data_in_2,Data_in_1,Data_in_5,Data_in_4,Data_in_3)
NOOP "6.5.2",,,
```

### transio_file.cfg

```
hp93000,config,0.1
DFPN 10202,"",(Data1)
DFPN 10201,"",(Data2)
PSTE 1
CONF IO,F160,(Data1,Data2)
RDIV 0,(Data1,Data2)
NOOP "6.5.2",,,
```

### usb_file.cfg

```
hp93000,config,0.1
DFPN 10214,"",(Data3)
DFPN 10213,"",(Data4)
DFPN 10212,"",(Data5)
PSTE 1
CONF IO,F160,(Data3,Data4,Data5)
RDIV 0,(Data3,Data4,Data5)
NOOP "6.5.2",,,
```

The pin configuration master file is the following:

```
hp93000,config_master_file,0.1
testerfile:demo.cfg

Package:package.cfg

TRANSIO:transio_file.cfg
USB:usb_file.cfg
```

The pin configuration file assembled from the above files looks like this:

```
hp93000,config,0.1
DFPN 10201,"",(Data_in_2)
DFPN 10202,"",(Data_in_1)
DFPN 10212,"",(Data_in_5)
DFPN 10213,"",(Data_in_4)
DFPN 10214,"",(Data_in_3)
DFPR "TRANSIO","Data2",(Data_in_2)
DFPR "TRANSIO","Data1",(Data_in_1)
DFPR "USB","Data5",(Data_in_5)
DFPR "USB","Data4",(Data_in_4)
DFPR "USB","Data3",(Data_in_3)
PSTE 1
CONF OFF,F160,(Data_in_2,Data_in_1,Data_in_5,Data_in_4,Data_in_3)
RDIV 0,(Data_in_2,Data_in_1,Data_in_5,Data_in_4,Data_in_3)
NOOP "6.5.2",,,
```

<!-- 语法节 end -->

## 是什么

**Pin Configuration tool 不是一个窗口，是 SmarTest setup 里编辑 pin 配置文件的那一组编辑器。**
它的定义文档只有两句正文，第二句就是它的全部职责：

> 「With the Pin Configuration tool you edit the pin configuration file.」

**「编辑那个文件」就是它的身份。** 由此得出本页反复要用的一条结论：
**它的产物只有一个——[[pin-configuration-file]]**，落在 `<device_dir>/configuration`。

**而它是整个 setup 的第一道门**（原文两句连读）：

> 「The pin configuration file is the first setup file that must be completed before you can test a new device.」

> 「If the pin configuration details have not been entered, the software will not let you enter details about the DUT in any other setup window.」

**这两句是「pin 配置是全流程前置条件」这条约束的直接出处**——
原文说的是**软件层面不让你往下走**，不是「建议先做」。

### 它是一棵树 + 一组编辑器，不是单个窗口

> 「The Pin Configuration tool contains a hierarchical view in the Test Program Explorer and setup editors.」

所以「打开这个工具」= **打开 setup perspective，然后在 Test Program Explorer 里双击一个 setup component**：

> 「Make sure that the setup perspective is opened.」

> 「in the Test Program Explorer view, double-click the setup component.」

组 / port / alias set 要先展开、且必须已存在：

> 「click the triangle to expand all the items.」

> 「double-click the group, port or alias set to open the setup editor.」

> 「create a new group, port or alias set.」

> 「double-click the newly created group, port or alias set in the Test Program Explorer view.」

### 它的编辑器清单（`02.08.04.18.03` 的表格，逐条）

| 编辑器 | 职责（原文 `Function` 列，逐字） |
|---|---|
| `Pin Settings` | `Define the pin.` |
| `Groups` | `Define the pin group.` |
| `Ports` | `Define the port.` |
| `Alias Sets` | `Define the pin alias sets.` |
| `DC Scale Extensions` | `Request licenses for extended features of DC Scale cards.` |
| `DC Scale Limits` | `Define voltage and current limits for DC Scale cards.` |
| `DC Scale Regulation` | `Select regulation settings for DC Scale cards.` |
| `DC Scale Safety` | `Select global safety parameters for voltage drop levels.` |
| `Ground sense editor` | `Select sites for ground sense pins.` |
| `Protocol Assignments` | `Assign protocols and pin roles to ports and resource pins.` |

`Pin Settings` 本身再分五种（`02.08.04.18.03.01`）：

> 「There are the following types of pin setting editors:」

- **Digital Pins editor** / **DPS Pins editor** / **Utility Pins editor** / **Utility Purpose Editor** / **Virtual Pins editor**

> 「The pin information is entered in the pin configuration area of the corresponding Pin setting editor. The digital pins editor also contains the context information.」

> 「For multi-site testing, the tester channels for all the sites are displayed in the pin setting editors.」

### ⚠️ 一处名字对不上，照实记

`02.08.04.18.02.01`（Opening the setup editor）说双击可以打开的是这四个：

> 「- the Pin Setting Editor」

> 「- the Core Allocation Editor」

> 「- the DPS Channel Mode Editor」

> 「- the Utility Purpose Editor」

而 `02.08.04.18.03`（Elements）给的清单是上面那张表里的十个编辑器。
**`Core Allocation Editor` 与 `DPS Channel Mode Editor` 两个名字在整个 9,398 篇 raw 里
各只出现 1 次——就是这一篇**（查过，`grep -lF` 数过篇数）。**它们没有自己的文档页。**
**本页照实记，不替语料调和、也不判哪个是旧名。**

### 三个 `Pin Settings` 编辑器：各自管哪一种 pin

**这是本页最实用的一张表。** 三个编辑器**不是三个工具**，
而是**同一棵树 `Pin Settings` 下的三种 pin**；它们**共用同一个产物**（pin 配置文件），
**列名与列的语义按 pin 的种类不同**。

| | [[digital-pins-editor]] | [[dps-pins-editor]] | [[utility-pins-editor]] |
|---|---|---|---|
| 管什么 pin | `Digital pins and DC Scale pins in PMU operating mode` | DPS 模式的 DC Scale pin | utility pogo pin（给 utility line 起符号名） |
| 表格列（**原文表格的顺序**） | `Name` / `No` / `Type` / `Mode` / `Scaling` / `HW` / `Connection Set` / `Comment` / `Tester Channel` | `Name` / `Pol` / `C[uF]` / `HW` / `Comment` / `Tester Channel` | `Name` / `Mode` / `t[ms]` / `Comment` / `Tester Channel` |
| 关键取值 | `Type`：`off` / `i` / `o` / `io` / `dc`；`Mode`：`std` / `fast` / `SIG` / `CMON` | `Pol`：`POS` | `Mode`：`w` / `r` / `rw`，外加 4 个 shutdown 关键词 |
| 只有这一格才有的东西 | **Context 列表**（右上 `CONTEXT` 下拉） | 负载电容 `C[uF]` | utility line 的等待时间 `t[ms]` |
| 引入版本 | SmarTest 6.5.0 | SmarTest 6.5.0 | SmarTest 6.5.0 |

**三条最要紧的细节：**

**① `dc` 这个 `Type` 底下压着两种完全不同的东西**（Digital Pins editor 逐字）：

> 「- A DC Scale pin in PMU operating mode or」

> 「- a utility DC pin」

**② PMU 模式的 DC Scale pin 有硬取值**（同篇 `## DC Scale pin (PMU mode) setup`）：

> 「For a DC Scale pin in PMU operating mode, the parameter must be dc.」

> 「For a DC Scale pin in PMU operating mode, it must be SIG.」

**③ utility line 的 `Mode` 不只是读写方向，还能让 utility line 当安全线 / 全局关断线**（Utility Pins editor 逐字）：

> 「- triggerIfHigh: Safety line」

> 「- triggerIfLow: Safety line」

> 「- triggerSiteIfHigh: Global shutdown line」

> 「- triggerSiteIfLow: Global shutdown line」

### Context：pin 配置与 timing / level / vector 的挂钩

**Context 列表是 Digital Pins editor 的一部分**（`02.08.04.18.03.01.01` 逐字）：

> 「The Context list is part of the Digital Pins editor.」

> 「The context is just an arbitrary name (except the name "DEFAULT", when being selected, the pins will automatically be defined as standard pins and allocated the mode "std") which identifies a particular pin configuration.」

> 「The maximum number of contexts you can define is 10.」

> 「For a valid setup, the level, timing and vector data for a particular test suite have to belong to the same context.」

**最后一句是一条真约束**（§2.4 的 **D3 一致匹配**）：同一个 context 名必须**在四处都写成一样**。
原文列了这四处：

> 「- Level equation sets」

> 「- Timing equation sets」

> 「- Wavetables」

> 「- Vector labels (via the wavetable definition)」

**本页只写「这条规矩存在」，不写它的取证**——那属于 `constraint` 类页面的活。

### 它和文件的关系：`corresponding exactly to`

`02.08.04.18.04` 明说文件里是一组固件命令，而且与界面上的参数**逐条对应**：

> 「The file contains a set of firmware commands corresponding exactly to the parameters specified within the Pin Configuration tool.」

**⚠️ 但这个工具不是唯一的路**（同一篇的 Note，逐字）：

> 「Note You can use a text editor instead of the Pin Configuration Tool to create or edit a pin configuration file in the form of a set of firmware commands.」

### 拆分：master file 与 Setup Management Tool

> 「A pin configuration can be organized as one single file, or different parts of the pin configuration can be stored in separate files. In the latter case, the respective pin configuration files can be merged through a master file which contains references to the individual files.」

> 「Splitting the pin configuration into multiple individual files allows multiple users to work on the configuration in parallel.」

细则（四条校验规则、`.cfg` 的格式）见 [[pin-configuration-master-file]]，本页不展开。
**本页只说清一件事：拆文件这件事发生在「工具之外」**——
组装它的是 [[setup-management-tool]]，不是这个工具。

### Port 不是 pin group 的别名，但行为上是

`02.08.04.18.03.03`（Port Editor）给了三条规则，逐字：

> 「- A port must not have the same name as a pin or pin group.」

> 「- Port definitions correspond to fixed group definitions. Expression-based port definitions are not supported.」

> 「- Ports are automatically pin groups. That is, ports in a setup can be used as an ordinary pin group. For example:」

**第三条是关系的实质**：port **可以直接当普通 pin group 用**，
所以它既能进 level setup 的 pin group 列表，也能进「表达式型 pin group」的定义里——
**这一条把 [[port-editor]] 与 [[pin-group-editor]] 连起来了**。

## 典型用法

**先交代一件事**：原文的 `## Subtopics`（`02.08.04.18.02_Using_the_Pin_Configuration_Tool.md`）
声明了 **11 条子过程**——`Opening the setup editor`、
`Importing the pin configuration from a CSV file`、`Exporting the pin configuration to a CSV file`、
`Discarding the changes in the pin configuration tool`、`Applying pin configuration data`、
`Saving a modified pin configuration`、`Working with pins`、`Working with pin groups`、
`Working with ports`、`Working with utility purposes`、
`Setting DC Scale voltage and current limits`。

**本页只读了其中第一条。** 所以下面给得出的只有这一条路，其余的写「本页没读」，不猜。

### 打开一个 setup 编辑器（原文 `## Procedures` / `## Results`）

1. **确认 setup perspective 已打开**（`## Before you begin` 逐字：
   `Make sure that the setup perspective is opened.`）。
2. **在 Test Program Explorer 里双击 setup component** → 编辑器打开
   （`The editor is opened.`）。
3. 若目标是**组 / port / alias set 且已定义过**：先点三角展开全部条目，
   再双击目标。
4. 若目标**还没定义过**：先**新建**组 / port / alias set，再双击它。

### 一条顺序上的硬前提（不是流程，是门槛）

| 条件 | 结果（原文逐字） |
|---|---|
| pin 配置文件还没填完 | `the software will not let you enter details about the DUT in any other setup window.` |
| 填完了 | 才能往下做 Level / Timing / Pattern 等别的 setup |

**这条是 pin 在整个流程里位置的唯一书面依据**，也是 `stage: pin` 排在 `project` 之后的理由。

### 一条不开 GUI 也能干的路

用**文本编辑器**直接写固件命令来建 / 改 pin 配置文件（依据就是上面那句 Note）。
**代价与边界**：那条 Note 只说「可以」，**没说能写哪些命令、哪些字段在文本里写不了**——
**语料未写**，本页不补。
命令各自的语法、参数、报错见 [[mapping-pin]] 与各命令页，**本页一条都没有**。

### 多 site 怎么显示

> 「For multi-site testing, the tester channels for all the sites are displayed in the pin setting editors.」

**具体长什么样图里有**（见「出处」的 ④ 图证档）：
`Tester Channel` 一列**按 site 拆成 `Site 1` / `Site 2` 子列**，同一根针不同 site 可以不同；
Utility Pins editor 上是 `Site 1` 到 `Site 4` 四列。

### 11 条子过程本页给不出的东西

| 子过程 | 本页有吗 |
|---|---|
| `Opening the setup editor` | **有**（上面那四步） |
| `Applying pin configuration data` / `Saving a modified pin configuration` / `Discarding the changes in the pin configuration tool` | **没有**。所以「改完怎么生效、改错了怎么撤」本页一个字没有 |
| `Importing the pin configuration from a CSV file` / `Exporting the pin configuration to a CSV file` | **没有**。CSV 的列、格式、往返保真度本页都没依据 |
| `Working with pins` / `pin groups` / `ports` / `utility purposes` | **没有**。本页只有「这些编辑器各有哪几列」（见「是什么」的表），没有「怎么建一个」 |
| `Setting DC Scale voltage and current limits` | **没有**。限值那件事本页只知道有个 [[dc-scale-limits-editor]] |

## 和谁有关

| 页 | 关系是什么 |
|---|---|
| [[pin-configuration-file]] | **产物**（唯一产物）。落在 `<device_dir>/configuration`，内容是固件命令 |
| [[pin-configuration-master-file]] | **拆文件时的总表**；把多个 `.cfg` 合成一份，由 [[setup-management-tool]] 执行组装 |
| [[setup-management-tool]] | **下游的执行者**：它读 master file 去合并，并做四条校验 |
| [[digital-pins-editor]] | **本工具 `Pin Settings` 下的一个编辑器**：数字 pin + PMU 模式 DC Scale pin + **Context 列表** |
| [[dps-pins-editor]] | 同上：DPS 模式的 DC Scale pin（`Pol` / `C[uF]`） |
| [[utility-pins-editor]] | 同上：utility pogo pin（`Mode` 的读写方向与 4 个 shutdown 关键词） |
| [[utility-purpose-editor]] | 同工具的编辑器：一组 utility line + 标准状态（原文 `Select sites for ground sense pins.` 之外的 `Utility purpose` 一族） |
| [[pin-group-editor]] / [[port-editor]] / [[alias-set-editor]] | 同工具的另外三个编辑器（`Groups` / `Ports` / `Alias Sets`）。**[[port-editor]] 与 [[pin-group-editor]] 的关系在「是什么」里明写了** |
| [[dc-scale-limits-editor]] | DC Scale 卡的电压 / 电流**限值**（同工具的 `DC Scale Limits`） |
| [[ground-sense-editor]] / [[protocol-editor]] | 同工具的 `Ground sense editor` 与 `Protocol Assignments` |
| [[pin]] | 本页 `stage: pin` 的理由。**这是「最近的一段」，不是归属**（§6） |
| [[mapping-pin]] | 同一段的三层对照（GUI ↔ 文件 ↔ L1）。**本页不重复它的表**；本页补的是它没有的「工具内部结构」 |
| `Virtual Pins editor` | 第五种 pin setting editor。**不在允许名单，写名字** |
| `Core Allocation Editor` / `DPS Channel Mode Editor` | **见「是什么」里那条对不上**。**不在允许名单，写名字** |

## 版本

**定义文档 `02.08.04.18_Pin_configuration_tool.md` 自己没有 `## Functional changes` 段。**
它全部正文是一句 `This section introduces the usage of the Pin configuration tool.`
加五条 `Subtopics`。**这是事实，不是缺陷。**
版本条目全在它声明的子主题里，逐篇转录（**出处写在每行**）：

| 哪一篇 | 条目（逐字） |
|---|---|
| `02.08.04.18.01` Introduction | `Introduced before SmarTest 6.3.2` |
| `02.08.04.18.02` Using | `Introduced before SmarTest 6.3.2` |
| `02.08.04.18.02.01` Opening the setup editor | `Introduced before SmarTest 6.3.2` |
| `02.08.04.18.03` Elements | `SmarTest 6.5.2: The Alias Sets editor is added.` / `SmarTest 7.1.0: Added Protocol Assignments.` / `SmarTest 7.1.3: Move utility purpose editor to Pin Settings.` / `SmarTest 7.2.1: DC Scale Limits added.` / `SmarTest 7.4.0: DC Scale Extensions added.` / `SmarTest 7.10.1: DC Scale Regulation and DC Scale Safety added.` / `SmarTest 7.10.3: Ground sense added` |
| `02.08.04.18.03.01` Pin setting editors | `SmarTest 6.5.0: Added digital pins editor, analog pins editor, DPS pins editor, and utility pins editor.` / `SmarTest 6.5.0: The site text box removed. For multi-site testing, the tester channels for all the sites are displayed in the pin setting editors.` / `SmarTest 7.1.3: Move utility purpose editor to Pin Settings.` / `SmarTest 7.3.1: New "Connection Set" column in the Digital Pins editor.` / `SmarTest 7.10.2: New "Scaling..." column in the Digital Pins editor.` |
| `02.08.04.18.04` Pin configuration file | `Introduced before SmarTest 6.3.2` |
| `02.08.04.18.05` Pin configuration master file | `Introduced in SmarTest 6.5.2` |
| `02.08.04.18.03.01.01` Context list | `Introduced before SmarTest 6.3.2` / `SmarTest 6.5.0: The Context list is only located in the Digital Pins editor.` |
| `02.08.04.18.03.01.02` Digital Pins editor | `Introduced in SmarTest 6.5.0` / `7.1.3: Changed the parameter Instrument to HW.` / `7.1.3: Removed the parameter Ser.R[ohm].` / `7.1.3: Added the HV mode option.` / `7.2.0: Modified pin name length.` / `7.3.1: New parameter "Connection Set".` / `7.3.1: DC Scale PVI8 card added.` / `7.4.0: DC Scale AVI64 card added.` / `7.5.0: DC Scale FVI16 card added.` / `7.10.0: PVI8 not supported, HV mode option not supported` / `7.10.1: DC Scale XPS256 card added.` / `7.10.2: XPS256 current monitor: New option "CMON" for "Mode" column and new "Scaling" column.` |
| `02.08.04.18.03.01.03` DPS Pins editor | `Introduced in SmarTest 6.5.0` / `7.1.3: Changed the parameter Polarity to Pol.` / `7.1.3: Changed the parameter Load Capacitor [uF]/V-Ramp [us] to C[uF].` / `7.1.3: Changed the parameter Instrument to HW.` / `7.3.1: DC Scale PVI8 card added.` / `7.3.2: DC Scale UHC4T card added.` / `7.4.0: DC Scale AVI64 card added.` / `7.5.0: DC Scale FVI16 card added.` / `7.10.1: DC Scale XPS256 card added.` |
| `02.08.04.18.03.01.04` Utility Pins editor | `Introduced in SmarTest 6.5.0` / `7.1.3: Changed the parameter "Operation Mode" to "Mode".` / `7.1.3: Changed the parameter "Delay [ms]" to "t[ms]".` / `7.10.1: Three-digit utility pogo block designator on V93000 EXA Scale systems.` / `7.10.2: New keywords for the Mode parameter to configure shutdown of XPS256 pins using utility lines.` |
| `02.08.04.18.03.03` Port Editor | `Introduced before SmarTest 6.3.2` |

**⚠️ 上表里所有 `Introduced before SmarTest 6.3.2` 都是哨兵值，不是「6.3.2 新增」**（§11.2 ②）。
它的意思是「**在本文档集覆盖范围开始之前就已经有了**」。
**只有 `Introduced in SmarTest X.Y.Z` 那种写法才是「那一版新加的」**——
上表里 `02.08.04.18.05` 的 `Introduced in SmarTest 6.5.2` 就属于后者。

**两条值得单独拎出来：**

- **`SmarTest 7.10.3: Ground sense added`** —— 本 wiki 面向 **7.10.3**，
  这条是**当前版本最新的一条**，也说明 [[ground-sense-editor]] 是这一版才有的。
- **`SmarTest 6.5.0: Added digital pins editor, analog pins editor, DPS pins editor, and utility pins editor.`**
  —— 这里点了一个「**analog pins editor**」，而**当前 `Pin setting editors` 那篇列的五个编辑器里没有它**
  （只有 Digital / DPS / Utility / Utility Purpose / Virtual）。
  `02.08.04.18.04` 的示例图里**还留着一个 `Analog Pins` 页签**（见「出处」的图证）。
  **语料自相矛盾，本页照记，不替它调和、也不替它判「是删了还是漏了」。**

## 出处

**读了什么，要说清，因为这一页的 `sources:` 只有一篇，而那一篇只是个目录**：

- **`sources:` 里那一篇 `02.08.04.18_Pin_configuration_tool.md`（`source_topic` `17541.htm`）整篇读完**——
  但它**几乎没有正文**：全篇 **16 行**（`wc -l`，`st_size` 754 字节），剥掉 frontmatter 后 **12 行**，
  **其中只有 1 行是散文**（`This section introduces the usage of the Pin configuration tool.`），
  其余是一个 `#` 标题、一个 `#### Subtopics` 和**五条 `Subtopics`**。它是一张目录，不是一个文档。
  （⚠️ 2026-09-20 更正：本页原写「**正文只有 2 行**」——**「正文」是哪个口径没写，而 2 对不上任何一个**
  （全篇 16 / 剥 frontmatter 后 12 / 散文 1）。**数本身不是错，是量它的那把尺没写出来**，见 `schema.md` §11.5。）
- **所以本页正文的事实来自它自己声明的 `Subtopics`**
  （§9.1 允许链的第 4 类目标：「定义文档自己声明的 `Subtopics`」）。
  **这些路径不在 `sources:` 那一行里，本页明说这件事。**
  **整篇读完的 12 篇**：`02.08.04.18.01`（Introduction）、`02.08.04.18.02`（Using）、
  `02.08.04.18.02.01`（Opening the setup editor）、`02.08.04.18.03`（Elements）、
  `02.08.04.18.03.01`（Pin setting editors）、`02.08.04.18.03.01.01`（Context list）、
  `02.08.04.18.03.01.02`（Digital Pins editor）、`02.08.04.18.03.01.03`（DPS Pins editor）、
  `02.08.04.18.03.01.04`（Utility Pins editor）、`02.08.04.18.03.03`（Port Editor）、
  `02.08.04.18.04`（Pin configuration file）、`02.08.04.18.05`（Pin configuration master file）。
  **引文只来自这 12 篇。**

**本页没做的**：

- **`## Subtopics` 里那 11 条子过程一条没读**（见「典型用法」的表）。所以
  **「填完怎么存、怎么应用、怎么撤、CSV 长什么样」本页一个字没有。**
- **另外 9 个编辑器一篇没读**：`Pin group editor` / `Alias Set Editor` /
  `DC Scale Extensions editor` / `DC Scale Limits editor` / `DC Scale Regulation editor` /
  `DC Scale Safety editor` / `Ground sense editor` / `Protocol assignments` /
  `Utility Purpose Editor` / `Virtual Pins editor`，以及 `Apply button` / `State indicator` /
  `Filter line` / `Sorting rows` 四个小元素。
  **上表里它们的「职责」一行，是 Elements 那篇表格里的 `Function` 列逐字**，
  **不是从它们自己的文档里读的**——这一点必须说清。
- **命令侧一篇没读。** `DFPN` / `DFPT` / `DFPS` / `DFAN` / `CONF` / `RDIV` / `DDSL` / `PSLC` / `PSTE`
  **本页只见到它们出现在 `02.08.04.18.04` 与 `02.08.04.18.05` 的示例代码块里**；
  每条命令的参数、语法、报错**本页一个字没有**。它们的三层对照见 [[mapping-pin]]。
- **一条 L2 API 都没读**（`SetUtilityLines` / `GetUtilityLines` / `SMC_TEST()` /
  `judgeAndLog_*` 等只在 Utility Pins editor 的正文里被提到名字）。
- **没有实跑。** 没在机台上开过这个工具、没生成过 pin 配置文件。`verified: doc-only`。

### ④ 图证：读了 10 张，逐张如下

（§11.4 / §2.5：**④ = 图证**，**从 raw 自带的图里读出来的**。
**它的强度比「语料明说」「文档间链接」都硬**——图是文档自带的，不是我的推断；
**但它不可检索**：拿图里的字去 9,398 篇 raw 里 grep 是 **0 命中**的，要核只能自己再开那张图。
**下面每一张我都写了它解决什么、以及它答不了什么。**）

| 图 | 出处篇 | 读到了什么 | 解决了什么 |
|---|---|---|---|
| `355141.png` | `02.08.04.18.03.01.02` | Digital Pins 页签。列头逐字 `Name` / `No` / `Type` / `Mode` / `Scaling[V/A]` / `HW` / `Connection Set` / `Comment` / `Tester Channel`；`Tester Channel` 下分 `Site 1` / `Site 2`；右上 `CONTEXT:` 下拉，值 `DEFAULT`；行如 `CP` / `12` / `i` / `std` / `PS1600` / `10509` / `10609` | 把**当前版本**的列名钉到字面；`Tester Channel` 按 site 拆列也钉到字面 |
| `354609.png` | `02.08.04.18.03.01.03` | DPS Pins 页签。列头 `Name` / `Pol` / `C[uF]` / `HW` / `Comment` / `Tester Channel`（`Site 1` / `Site 2`）；行 `PWR POS 1.0 DCS-DPS128HC 22510 22511`、`VCC 1 POS 2.3 DCS-DPS128HC 22504 22502`、`VCC 2 POS 2.3 DCS-DPS128HC 22501 22505` | 同上；并且**证明 7.1.3 那三条改名已经落到界面上** |
| `354720.png` | `02.08.04.18.03.01.04` | Utility Pins 页签。列头 `Name` / `Mode` / `t[ms]` / `Comment` / `Tester Channel`（`Site 1` 到 `Site 4` 四列）；行含 `SAFETY LINE  triggerIfHigh`、`GLOBAL SHUTDOWN  triggerSiteIfHigh` | `Mode` 那 4 个 shutdown 关键词**真的在界面上**；被复用的行底色变黄 |
| `355197.png` | `02.08.04.18.03.01.02` | Digital Pins 页签的一个局部。一行逐字是 `DMM 1` / `1` / `dc` / `std` /（`Scaling` 一格是灰的）/ `DMM` /（中间两列被裁掉）/ `UTIDC165` | **Utility DC pin 的 `Mode` 填 `std`**——**正文没写这件事** |
| `56188.png` | `02.08.04.18.03.01.01` | Testsuite Dialog（`Testsuite Dialog` 窗口，`Primaries` / `Flags` / `Site Control` 三个页签）。三条标注逐字 `timing context (Defined in timing equation set)` / `level context (Defined in level equation set)` / `vector label context (Defined in wavetable)`；`Context` 行的值 `differential/DEFAULT/differential`；`Testsuite name` 是 `FD_X4LH` | 把「混用的 context 长什么样」画出来了，**并且暴露了 context 的三段写法与顺序** |
| `56189.png` | 同上 | `Common context of all setup data` 标注；三个文件窗口，路径逐字 `/var/opt/hp93000/soc/tmp/93k.T7RX0b/edit_timEqn`、`edit_timWvt`、`edit_lvlEqn`，每个窗口里各有 `MODECONTEXT "differential"`；`Context` 行值 `differential` | 有效 setup = **四处同名**；而且**这三处的落点文件是哪个**图里写着 |
| `97848.png` | `02.08.04.18.03.03` | `Port_IO` 窗口。左表 `Available Pin List`（列 `Pin Name` / `Type`），右表 `Port Members`（同两列）；四个按钮 `Add >` / `Add All >>` / `< Remove` / `<< Remove All`；已加入的行前有一个**勾选标记** | **Port 编辑器的操作面**（原文只有一句话 + 一个坏字，见下） |
| `21671.png` | `02.08.04.18.04` | Digital Pins 页签。列头逐字 **`Name` / `NO` / `Type` / `Mode` / `Ser.R[Ohm]` / `Instrument` / `Comment` / `Tester Channel`（`Site1`）**；行 `IAQ_D8 108 off std 0.0 PS3600 10208` 起共 10 行 | **这是一张 7.1.3 之前的旧界面截图**（见下） |
| `105641.png` | 同上 | DPS Pins 页签。列头逐字 **`Name` / `Polarity` / `Load Capacitor [uF]/V-Ramp [us]` / `Instrument` / `Comment` / `Tester Channel`（`Site1`）**；行 `VCC1 POS 0.1 MSDPS DPS11`、`VEE POS 0.1 MSDPS DPS12`、`DRC_IN_TERM POS 0.1 MSDPS DPS14` | 同上 |
| `105640.png` | 同上 | **`Analog Pins`** 页签。列头 `Name` / `NO` / `Type` / `Instrument` / `Comment` / `Tester Channel`（`Site1` 下再分 `Pogo` / `Pad`）；行 `input_a_1 232 i MCB 23116 S2`、`input_a_2 234 i MCB 23114 S2` | 同上；**并且 `Analog Pins` 这个页签在当前编辑器清单里找不到** |

**⚠️ 这一页最要紧的一条图证结论：后三张是旧界面，前四张是新界面。**

这**不是矛盾**——它们是两批不同年代的截图，**而图没有版本标注**（这正是 §11.4 说的图证最容易过期的地方）。
**判据是文本**，就在同一族的 `## Functional changes` 里：

- `02.08.04.18.03.01.02`：`SmarTest 7.1.3: Changed the parameter Instrument to HW.` /
  `SmarTest 7.1.3: Removed the parameter Ser.R[ohm].`
- `02.08.04.18.03.01.03`：`SmarTest 7.1.3: Changed the parameter Polarity to Pol.` /
  `SmarTest 7.1.3: Changed the parameter Load Capacitor [uF]/V-Ramp [us] to C[uF].` /
  `SmarTest 7.1.3: Changed the parameter Instrument to HW.`

对照表如下（**本页正文里的列名一律用「当前该读成」那一列**；
旧名只在下面出现）：

| 旧图上的字 | 当前该读成 | 依据 |
|---|---|---|
| `Instrument` | **`HW`** | 两篇的 `7.1.3` 改名条目 |
| `Polarity` | **`Pol`** | DPS Pins editor `7.1.3` |
| `Load Capacitor [uF]/V-Ramp [us]` | **`C[uF]`** | DPS Pins editor `7.1.3` |
| `Ser.R[Ohm]` | **这一列已经没有了** | Digital Pins editor `SmarTest 7.1.3: Removed the parameter Ser.R[ohm].` |
| `NO` | **`No`** | 新图 `355141.png` 上是 `No` |
| `Site1` | **`Site 1`** | 新图 `354609.png` / `354720.png` 上是 `Site 1` |

**⚠️ 一处必须说清的判据强度**：**旧图上那些列名不是「错的」**——
它们是**旧版本的正确写法**。**本页把它们列出来，是因为不列会让人把旧名当现名**，
这正是本工程在 pin 这一族刚踩过的坑（见 [[mapping-pin]]）。

**图证答得了、文本答不了的（这两条标 ④）**：

- **`Scaling[V/A]` 这个列头**：原文表格里的列名只有 `Scaling`
  （`This column applies to the CMON option of the Mode column.`，单位 `V/A` 写在句子里）。
  **`Scaling[V/A]` 这个带方括号的写法在 9,398 篇 raw 里 grep 是 0 命中**——**只在图上**。
  同理，**`Ser.R[Ohm]`（大写 `O`）也是 0 命中**，而文本里写的是 `Ser.R[ohm]`（4 篇命中）。
- **Utility DC pin 的 `Mode` 是 `std`**（图 `355197.png`）：原文给了 `Type` = `dc` 的**两种**含义
  （PMU 模式的 DC Scale pin / utility DC pin），**但只规定了前者的 `Mode` 必须是 `SIG`**；
  **utility DC pin 的 `Mode` 该填什么，正文一个字没写**。图上那一行是 `dc` + `std`。
- **context 的三段写法与顺序**（图 `56188.png`）：值是 `differential/DEFAULT/differential`，
  三条标注从左到右是 timing / level / vector label——**所以顺序是 `timing/level/vector-label`**。
  正文只说「混用的就是这样」，**没说这个字段是三段、也没说段序**。
  （**这是结构性结论**（谁连谁、有几段），**不属于会被版本改名影响的那一类**，§11.4。）

**图证答不了的（照实说）**：

- **「哪些列必填、哪些组合非法」，图答不了**——图是「某一次具体配置」的截图，不是格式规范。
  那是文本的事，**而文本在这一点上也没写全**（上述 `355197.png` 那条就是例子）。
- **图里没有一个固件命令名。** 所以「**GUI 的哪一列对应文件里的哪一条命令**」——
  **这十张图一张都没答**。这一格是 [[mapping-pin]] 的活（它用 `02.08.04.18.04` 那三张图
  得出了 `DFPN` / `DFPS` / `DFAN` 的参数顺序），**本页不做**。
- **旧图上的两个值在当前文档里找不到对应，本页照记、不判它是什么**：
  - `MSDPS`（旧 DPS 图的 `Instrument` 列）。DPS Pins editor 的 `HW` 列**当前清单**逐字是
    `DCS-DPS128HC, DCS-UHC4T, DCS-XPS256`，**没有 `MSDPS`**；
    而 `MSDPS` 在整个 raw 里**只有 1 篇命中，且不在 pin 这一族里**。
  - `DPS11`（同图 `Tester Channel` 列）。它在新图 `354609.png` 上是**五位数字**（`22510`）。
    `DPS11` 在整个 raw 里**只有 1 篇命中，也不在 pin 这一族里**。
  **本页不判这是「已废弃命名」还是「另一套命名」——语料未写。**

**⚠️ 语料瑕疵，本页照实记，一处都没替它改（§11.2）。**

**① 坏字（§11.2 ①，UTF-8 被按 GBK 读）**：本页读的 12 篇里共 **8 处**，逐字如下。

- `02.08.04.18.03.01.02`（2 处）：

  `The CONTEXT drop鈥慸own list at the top right`

  `a five鈥慸igit channel鈥慖D`

  `鈥慸` 是 `‑d`（三字节的第三个字节被吃掉、ASCII `d` 并进了坏字），**原字是 `drop-down`**；
  `鈥慖` 同理是 `‑I`，**原字是 `channel-ID`**。
- `02.08.04.18.03.01.04`（5 处）：

  `# ; (鈥? ) ? @ ,`（禁字符列表那一条）

  `01 鈥?nbsp;32`（**出现 2 次**）、`(00 鈥?nbsp;31)`、`hardware鈥慶ontrolled shutdown`

  `鈥慶` 是 `‑c`，**原字是 `hardware-controlled`**。
- `02.08.04.18.03.03`（1 处）：

  `In the Available Pin List, the "鈭? character preceding with the pin name means that this pin has been added to Port_IO.`

  **这一个坏字与上面那几个不同族**：它是 `鈭`（**U+922D**）。`extract/encoding-map.csv` 第 128 行
  只把它记成「原字符在 **U+2200–U+223F** 之间，第三字节已丢，**反解不了**」——
  **所以本页只报区间，不猜它是哪个字。** 上面 `鈥` 那一族（U+9225）是可反解的
  （`鈥慸`=`‑d`、`鈥慶`=`‑c` 这一类**能反解**），**两族必须分开说，不能并成一类**。
  同一个 `鈭?` 在 `02.08.04.18.03.01.05`（`the "鈭? symbol preceding with the utility line`）
  与 `02.08.04.18.02.08.03`（`indicated with "鈭?.`）里也各出现一次——**本页这两篇没读**，
  是从同一支的邻居篇里看到的，**没有计入上面那 8 处**。

**处置照 §11.2：页面照原样转录，不替它改。**
**代价要写清：拿修好的字（`drop-down`、`channel-ID`、`hardware-controlled`）去 raw 里搜是搜不到的**，
要搜坏掉的那个形态。

**一处是图能帮上文本的**：`02.08.04.18.03.03` 那个 `鈭?`，
**图 `97848.png` 上那个位置是一个勾选标记**（已加入 `Port_IO` 的每一行前面）。
**但本页不据此改引文**——上面那串里原样留着 `鈭?`。
（**这是唯一一处「图能替文本补一个语义」的地方**：正文只说 `the "鈭? character`，
**没说那个字符长什么样**；图上是一个勾选标记。**但那个标记到底是 `✓` 还是 `√` 还是别的字形，
本页没有把它读成确定的字符**——所以这里只说「勾选标记」。）

**② 整词替换（§11.2 ⑤）**：本页读的 12 篇里查过 `DC/DC power units`，**0 命中**。
**这一族的损坏不在这几篇上。**

**③ 名字对不上的两处**（不是坏字，是**语料自己不一致**）：
`Core Allocation Editor` / `DPS Channel Mode Editor`（见「是什么」），
以及 `analog pins editor` 一说（见「版本」与图 `105640.png`）。**两处都照记，都没替它调和。**

**④ 图里的字一律不进 `>` 引文块**（§11.4）：`Scaling[V/A]` / `Ser.R[Ohm]` /
`differential/DEFAULT/differential` / `UTIDC165` 这一类串，
**本页全部写在表格与反引号里，没有一处放进引文块**。
（**本页没有 `Magnitude [dB]` 这种东西**——那个串属于 [[signal-analyzer]] 那一族，
本页的图里一张都没有。）

`verified: doc-only`
