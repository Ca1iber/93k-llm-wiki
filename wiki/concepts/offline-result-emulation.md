---
type: concept
title: Offline Result Emulation
layer: n/a
stage: run
tags: [offline-result-emulation, ore, emulation, offline-verification, regression-testing, pre-silicon, failure-injection, license-gated, smartest-7.1.3]
related: [run, results, testflow, test-method-class, universal-test-method-library, error-flexlm-license-codes, hardware-response-emulator, smartest-7.1.3]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.12_Offline_Result_Emulation.md
created: 2026-09-21
updated: 2026-09-21
verified: doc-only
---

# Offline Result Emulation

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **4,590 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.12_Offline_Result_Emulation.md>` 及其子主题 `<02_System_reference/02.07_Test_Method_Reference/02.07.12.04.01_OfflineResultEmulationConfig.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.12.05.01_Setup_file__mapping_to_SmarTest_concepts.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.12.06.01_Digital_offline_result_emulation.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.12.06.02_Parametric_offline_result_emulation.md>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.12.06.03_Offline_result_emulation_for_the_analog_API.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Configuration API for the offline result emulation › OfflineResultEmulationConfig）

```
OfflineResultEmulationConfig& oreConfig =
  OfflineResultEmulationConfig::instance();

oreConfig.load("ore/ore.xml");
oreConfig.enable();
oreConfig.disable();
oreConfig.unload();
```

### Example（取自子主题 Offline result emulation setup file › Setup file  mapping to SmarTest concepts）

Following is an example setup for digital failure injection data. It contains pattern elements.

```
<offlineResultEmulation>

  <pattern name="testPattern1">
      <site number="1">
        <pin name="Q0">
          <fail xmode_cycle="0"/>
          <fail xmode_cycle="1"/>
          <fail xmode_cycle="2"/>
        </pin>
      </site>
  </pattern>

```

```
  <pattern name="testPattern2">
    <site number="2">
      <pin name="Q0">
        <fail xmode_cycle="0"/>
        <fail xmode_cycle="1"/>
        <fail xmode_cycle="2"/>
        <fail xmode_cycle="4" to="7"/>
        <fail xmode_cycle="9"/>
      </pin>
    </site>
    <site number="1">
      <pin name="S0">
        <failAll/>
      </pin>
    </site>
  </pattern>

  <pattern name="testPatternX1">
    <site number="2">
      <pin name="S0">
        <failAll/>
      </pin>
    </site>
    <site number="1">
      <pin name="S0">
        <fail xmode_cycle="0"/>
      </pin>
    </site>
    <pin name="I/O1">
      <fail xmode_cycle="2" to="10"/>
    </pin>
  </pattern>

  <pattern name="testPattern3">
    <pin name="Q0">
      <fail xmode_vector="0" to="13"/>
      <fail xmode_vector="24"/>
    </pin>
    <pin name="S0">
      <fail xmode_vector="28"/>
      <fail xmode_vector="29"/>
      <fail xmode_vector="32"/>
      <fail xmode_vector="33"/>
      <fail xmode_vector="40"/>
      <fail xmode_vector="41"/>
      <fail xmode_vector="44"/>
      <fail xmode_vector="45"/>
    </pin>
    <pin name="I/O1">
      <fail xmode_cycle="105"/>
      <fail xmode_cycle="106"/>
      <fail xmode_cycle="116"/>
      <fail xmode_cycle="115"/>
      <fail xmode_cycle="114"/>
    </pin>
    <pin name="I/O2">
      <fail xmode_cycle="113"/>
      <fail xmode_cycle="100"/>
      <fail xmode_cycle="99"/>
    </pin>
  </pattern>

```

```
  <pattern name="testPatternX8">
    <pin name="I/O2">
      <fail xmode_cycle="2" to="6"/>
      <fail xmode_cycle="9" to="13"/>
      <fail xmode_cycle="17" to="18"/>
      <fail xmode_cycle="22"/>
      <fail xmode_cycle="29" to="30"/>
      <fail xmode_cycle="25"/>
      <fail xmode_cycle="36" to="37"/>
      <fail xmode_cycle="42" to="43"/>
      <fail xmode_cycle="52" to="53"/>
      <fail xmode_cycle="58" to="59"/>
      <fail xmode_cycle="23" to="24"/>
      <fail xmode_cycle="39" to="40"/>
      <fail xmode_cycle="55" to="56"/>
      <fail xmode_cycle="71" to="72"/>
      <fail xmode_cycle="87" to="88"/>
      <fail xmode_cycle="103" to="104"/>
      <fail xmode_cycle="119" to="120"/>
      <fail xmode_cycle="135" to="136"/>
    </pin>
  </pattern>

</offlineResultEmulation>
```

### Example（取自子主题 Examples on how to use offline result emulation › Digital offline result emulation）

### XML setup file

```
<offlineResultEmulation>

   <pattern name="myPattern1">

```

```
     <pin name="Q1">
       <fail xmode_cycle="256771"/>
       <fail xmode_cycle="9"/>
     </pin>
     <pin name="S0">
       <failAll/>
     </pin>
   </pattern>

</offlineResultEmulation>
```

### Example（取自子主题 Examples on how to use offline result emulation › Parametric offline result emulation）

### XML setup file

```
<offlineResultEmulation>

   <measurementname="myMeasurement1">
     <testSuite name="myTestSuite1">
       <sitenumber="2">
         <pinname="Q2">
           <valueval="1.25"/>
         </pin>
       </site>
     </testSuite>
   </measurement>

   <measurementname="myMeasurement3">
     <pinname="Q4">
       <waveform>
         <value val="1.23"/>
         <value val="1.24"/>
         <value val="1.25"/>
       </waveform>
     </pin>
   </measurement>

   <measurementname="myMeasurement2">
     <pinname="Q3">
       <waveform file="/home/demo/matlab/tx106m1.txt"/>
     </pin>
   </measurement>

</offlineResultEmulation>
```

### Example（取自子主题 Examples on how to use offline result emulation › Offline result emulation for the analog API）

### Setup file

```
<offlineResultEmulation>

   <measurementname="TxDAC_106">
     <sitenumber="1">
       <pinname="TX0">
         <waveformid="1" file="/home/demo/MATLAB/tx106m1s1.txt"/>
         <waveform id="2" file="/home/demo/MATLAB/tx106m2s1.txt"/>
       </pin>
     </site>
     <sitenumber="2">
       <pinname="TX0">
         <waveform id="1" file="/home/demo/MATLAB/tx106m1s2.txt"/>
         <waveform id="2" file="/home/demo/MATLAB/tx106m2s2.txt"/>
       </pin>
     </site>
   </measurement>

</offlineResultEmulation>
```

Waveform files are ASCII files and may consist of just one value per line, but no header. For example:

```
0.9384127738399521
0.90442446110833
0.861447503687353
0.8120801816825381
0.7546371242146311
0.6935424298416738
0.6282343082705816
0.5615217109667776
[..]
```

or

```
208
199
188
177
163
150
135
122
106
[..]
```

<!-- 语法节 end -->

## 是什么

**ORE（Offline Result Emulation，离线结果仿真）是「**在真器件还不存在的时候，让测试程序照样拿到
测试/测量结果**」的一套机制**——**结果是用户自己按器件规格定义出来的，不是录下来回放的。**

**定义句，原文逐字**（这是本页最重的一句）：

> 「Offline result emulation (ORE) enables user defined test and measurements results for offline verification, debugging and regression testing of test flows, test methods, and DSP routines before the device is available, without needing recorded data.」

**一句拆成五格**：

| 格 | 原文 | 说的是什么 |
|---|---|---|
| **给什么** | `user defined test and measurements results` | **用户定义**的测试结果与测量结果 |
| **干什么用** | `for offline verification, debugging and regression testing` | 离线**验证** / **调试** / **回归测试** |
| **对哪些对象** | `of test flows, test methods, and DSP routines` | **testflow / test method / DSP routine** 三层 |
| **什么时候** | `before the device is available` | **首片器件到位之前** |
| **附加条件** | `without needing recorded data` | **不需要录好的数据** |

**最后一格是本页的分水岭。** `without needing recorded data` ——
**它和「录一遍真器件的输出、再回放」是两条路**：ORE **不要求你先有数据**，
**它把「结果」这一侧变成你自己按规格写出来的一份定义。**
（**语料里没有把这两条路并列比较过**，这句是本页从这半句话读出来的。
**（推断）的依据只有 `without needing recorded data` 这半句本身**。）

### 你定义的是「故障」，不是「数值」

原文第二段（逐字），说的是这套东西**怎么用起来**：

> 「On the basis of the device specification you define different kinds of failures that your test programs shall detect. With ORE you can start evaluating the test programs before the first device is available and complement the pre-silicon evaluation of the production process.」

**两句、两件事**：

| 句 | 原文 | 要点 |
|---|---|---|
| 1 | `On the basis of the device specification you define different kinds of failures that your test programs shall detect.` | **依据是 device specification**；**你定义的是「故障种类」，而测试程序的任务是「把它们检出来」** |
| 2 | `With ORE you can start evaluating the test programs before the first device is available and complement the pre-silicon evaluation of the production process.` | **两个收益**：首片之前就开始评估测试程序；**补充**（`complement`）pre-silicon 评估 |

**注意第 2 句用的是 `complement`（补充），不是 `replace`（取代）**——
**ORE 的定位是 pre-silicon 评估的补充，原文没有说它可以替代流片前的任何环节。**

**「你定义故障、程序负责检出」这层关系解释了 ORE 的用法形态**：
**失败是注入进去的（injected），判定是测试程序自己做的**——
**所以 ORE 同时也在考「你的测试程序检不检得出来」，不只是「给你一组假数据」。**
（**这句是上一格那半句的直接后果，本页标为推断**：原文只写了
`you define different kinds of failures that your test programs shall detect`，
**没有一个字讲「注入」这个词**。语法节里的元素名 `<fail …/>` / `<failAll/>` 与
`digital failure injection data` 那句，也与这一读法一致——**但那是语法节里的子主题内容，
不在本篇正文**。）

### 许可：这一条是硬门

原文 `## License overview` 一节，两句（**逐字**）：

> 「Offline result emulation (ORE) is available with the S&S_TOOLS_PACKAGE SW license. If this license is not available ORE is disabled.」

| 条件 | 结果（**原文**） |
|---|---|
| 有 `S&S_TOOLS_PACKAGE SW` license | `ORE is available` |
| 没有这个 license | `ORE is disabled` |

**两件事要紧**：

1. **它有独立的 license 门**，而且**不是「报错」而是「被禁用」**（`disabled`）——
   **原文没有写「禁用」在界面上/命令上是什么表现。**
2. **原文紧接着把「哪些产品有哪种 license」推给另一篇**（逐字）：
   `For an overview of all licensed V93000 products by Product ID, as they are referenced on the Entitlement Certificates, see Licensed V93000 products.`
   ——**`Licensed V93000 products` 那一篇本页没读**（连 raw 路径一起写在这里：
   `02_System_reference/02.04_Model_File_and_Licensing/02.04.02.01_V93000_License_Master_Look-up_Table.md`）。

### 本篇是「章首」，它自己不长——它的内容在六个子主题里

原文在正文之前先给了 `#### Subtopics` 清单，**六条**（**逐字**）：

- `Pre-silicon and emulation workflow`（`02.07.12.01_…`）
- `Concept of offline result emulation`（`02.07.12.02_…`）
- `Test program requirements for offline result emulation`（`02.07.12.03_…`）
- `Configuration API for the offline result emulation`（`02.07.12.04_…`）
- `Offline result emulation setup file`（`02.07.12.05_…`）
- `Examples on how to use offline result emulation`（`02.07.12.06_…`）

**这六条合起来才是 ORE 的全貌**，而**本篇（章首）只给了定义、定位和 license 三样**。
**（推断）这六条的顺序本身是有意义的**：从工作流 → 概念 → 测试程序要求 → 配置 API →
setup 文件 → 例子，**是一条「先搞清概念、再备好程序、最后才是配置与语法」的阅读路线**；
**依据只是这份清单的排列顺序与各条标题的字面意思——原文没有一句话说这是顺序要求。**

**⚠️ 这六条本页一条都没读**（见 `## 出处`）——**所以本页只能给「ORE 是什么、为什么用、
什么条件下能用」，给不出「怎么配、写在哪、字段叫什么」**。
**后一半在语法节里能看见一部分**（脚本从其中几个子主题逐字抽的，**来源写在段名里**），
**但语法节不是本页写的**（§4：语法/参数表由脚本抽）。

### 语法节里看得见的三件事（**只描述，不解释**）

语法节是脚本抽的，**它的段名自己交代了出处**，从段名能看出 ORE 有三个面：

| 面 | 语法节里的段名（**逐字**） | 它给的是 |
|---|---|---|
| **配置 API** | `Example（取自子主题 Configuration API for the offline result emulation › OfflineResultEmulationConfig）` | `OfflineResultEmulationConfig::instance()` / `.load("ore/ore.xml")` / `.enable()` / `.disable()` / `.unload()` |
| **setup 文件** | `Example（取自子主题 Offline result emulation setup file › Setup file  mapping to SmarTest concepts）` | `<offlineResultEmulation>` 下的 `<pattern>` / `<site>` / `<pin>` / `<fail …>` / `<failAll/>` |
| **三类例子** | `… › Digital offline result emulation` / `… › Parametric offline result emulation` / `… › Offline result emulation for the analog API` | 三份 XML：数字失败、测量值、波形文件 |

**从这三行能定的两件事**（**依据是语法节里可见的文字，不是本页的推断**）：

1. **ORE 的入口是一个进程内的单例配置对象**：`OfflineResultEmulationConfig::instance()`
   ——**`instance()` 说明它是单例**（这是 C++ 名字的字面读法）。
2. **它的配置来自一个 XML 文件**：`.load("ore/ore.xml")`——**例子里的路径是 `ore/ore.xml`**，
   **而 `enable()` / `disable()` / `unload()` 是三个动作**（**这三个动作各自的后果，
   语法节里没有说明，本页也不替它编**）。

## 典型用法

**本篇（章首）没有 `## Procedure`、没有 `## Before you begin`、没有 `## Example`**——
**它只有 `#### Subtopics`、两段正文、`## License overview` 和 `## Functional changes`。**
**所以「怎么用」在本页只能给到下面这个粒度**；**再往下的步骤在六个子主题里，本页没读。**

**按原文能落成的动作**（每一条的依据都是逐字的，**顺序是本页按清单排列还原的，不是原文写的**）：

| # | 动作 | 依据（**原文**） |
|---|---|---|
| 0 | **先确认有 `S&S_TOOLS_PACKAGE SW` license** | `If this license is not available ORE is disabled.` |
| 1 | **准备好 device specification** | `On the basis of the device specification you define different kinds of failures …` |
| 2 | **定义「测试程序应当检出的那些故障」** | 同上半句 |
| 3 | **用它来评估测试程序**——在首片器件到位之前 | `you can start evaluating the test programs before the first device is available` |
| 4 | **拿它做离线验证 / 调试 / 回归测试** | 定义句：`for offline verification, debugging and regression testing` |
| 5 | **用它补充 pre-silicon 评估** | `complement the pre-silicon evaluation of the production process` |

**关于「配置 API」这一步，语法节里有现成的五行**（**逐字，本页照抄语法节**）：

```
OfflineResultEmulationConfig& oreConfig =
  OfflineResultEmulationConfig::instance();

oreConfig.load("ore/ore.xml");
oreConfig.enable();
oreConfig.disable();
oreConfig.unload();
```

**⚠️ 这五行旁边的段名写的是 `Example`，而它没有任何说明文字**——
**五个调用哪个先哪个后、`load` 之后要不要 `enable`、重复 `load` 会怎样，语法节里一个字都没有，
本篇正文也没有。本页不替它排顺序。**

**关于 XML 那一侧**：语法节里给了四份 setup 文件示例
（一份按 SmarTest 概念映射的、一份数字的、一份参数的、一份模拟 API 的），
**本页只指路，不复述字段**——**字段级的说明在本页没读的 `Offline result emulation setup file` 子主题里。**

## 和谁有关

- [[run]] — **最近的一段（`stage: run`）**。ORE 的用途是「在器件到位前把测试程序跑起来评估」，
  **这是 run 段的事**；**注意 §6：`stage` 填的是「读者该去哪一段找它的用法」，不是「归属」**，
  **本页不写流程叙述，流程在 [[run]] 那一页。**
- [[results]] — **ORE 造的就是 result**。定义句说的是
  `user defined test and measurements results`；
  **结果本身怎么组织、怎么读，在 [[results]] 那一页，本页只有「它是被定义出来的」这一句。**
- [[testflow]] — **ORE 服务的三个对象之一**。定义句逐字列出
  `test flows, test methods, and DSP routines`——**testflow 是第一个**。
  **本页没有 testflow 的任何事实**（它长什么样、怎么建，都不在本页）。
- [[test-method-class]] / [[universal-test-method-library]] — **同样是那三个对象里的
  `test methods`**；**（推断）「test method 的基类 / 库」与定义句里的 `test methods` 是同一族东西**，
  **依据只是名字**——**原文没有点任何一页、也没有给类名。
  **本页没有那两页的任何事实。**
- [[error-flexlm-license-codes]] — **（推断）license 那一侧的排错入口**。
  本篇明写 `If this license is not available ORE is disabled.`，
  **而那一页是 FlexLM license 报错码的页面**；
  **依据只有「都是 license」——本篇没有写「ORE 缺 license 会报哪条错」，
  所以这只是一条**可能**相关的入口，不是本篇给的因果链。本页没读那页。**
- [[hardware-response-emulator]] — **同形陷阱，本页把它标出来**：
  名字里都有 `emulat…`，**但本篇正文**（含 `Subtopics` 清单、license 节）
  **一个字都没提它**——**所以本页不能声称两者有关系**。
  **列在这里是为了防下一个 agent 拿它来「补」本页**（§2.1 那类同形陷阱的处置）。
  **本页没有那页的任何事实。**
- [[smartest-7.1.3]] — **版本页，本页 `## 版本` 唯一的落点**。
- 六个子主题（**均未建**，本页一条都没读）：`Pre-silicon and emulation workflow` /
  `Concept of offline result emulation` / `Test program requirements for offline result emulation` /
  `Configuration API for the offline result emulation` / `Offline result emulation setup file` /
  `Examples on how to use offline result emulation`。
  **这六条是原文自己声明的 `Subtopics`（§9.1 第 4 类：定义文档自己声明的子主题）**，
  **它们迟早要建页，所以这里照原文名字列出**——
  **但本页对它们的内容一无所知，一条都没读。**
- `Licensed V93000 products`（**未建**）— 原文把它指定为「哪些产品带哪种 license」的出处。
  **本页没读它，所以 `S&S_TOOLS_PACKAGE SW` 具体覆盖哪些产品，本页不知道。**

## 版本

本文档**有** `## Functional changes` 段，**只有一条**（逐字）：

- **Introduced in SmarTest 7.1.3**

**这不是 §11.2 ② 那个哨兵**（哨兵写的是 `Introduced before SmarTest 6.3.2`）——
**`Introduced in SmarTest 7.1.3` 是常规的引入条目：ORE 在 SmarTest 7.1.3 引入。**
**版本页见 [[smartest-7.1.3]]。**

**与 wiki 面向版本的关系**：本 wiki 面向 **SmarTest 7.10.3**，
**7.1.3 早于 7.10.3**，所以按文档的说法**这个功能在目标版本里已经在**。
**注意 §11**：这只说明**文档这么写**，不说明某台机台上装了、也不说明那台机台有对应的 license
（**而 license 这一条本篇明写了是道硬门**）。本页 `verified: doc-only`。

**版本段里没有别的条目**——**`OfflineResultEmulationConfig` 这个类名、
XML setup 文件的格式、那六个子主题各自的内容，分别是哪个版本进来的，语料里没有。**

## 出处

`sources:` 一篇：
`02_System_reference/02.07_Test_Method_Reference/02.07.12_Offline_Result_Emulation.md`

**本页没做的：**

- **只读了这一篇（章首）。六个子主题一条都没读**——
  `Pre-silicon and emulation workflow` / `Concept of offline result emulation` /
  `Test program requirements for offline result emulation` /
  `Configuration API for the offline result emulation` /
  `Offline result emulation setup file` / `Examples on how to use offline result emulation`。
  **这是本页最大的空缺**：**「测试程序要满足什么要求」「setup 文件的字段」「例子的完整形态」
  全在那六篇里，本页给不出。**
- **「怎么用」只到「按原文能落成的动作」这张表的粒度**——
  **本篇没有 `## Procedure` / `## Before you begin`，本页没有别的地方可补**
  （§2.2：object/concept 页不写流程，流程在 stage 页）。
- **`Licensed V93000 products` 没读**（raw 路径见 `## 是什么` 那一节）——
  **所以 `S&S_TOOLS_PACKAGE SW` 覆盖哪些产品、Entitlement Certificate 上怎么认，本页不知道。**
- **「其它测试程序都跑不起来」这类前提没查**：本篇**没有写 ORE 的运行前置**
  （要什么 run mode、能不能在真实机台上开），**本页不替它补。**
- **一张图都没看。** 本篇**没有图片引用**（`![` 0 处，本页核过）。
- **没有交叉验证任何别处的文档**（§11：本页只写这一篇里有的）。
  **尤其：`hardware-response-emulator` / `hardware-response-file` 与 ORE 是否有关系，
  本页没有去查——本篇里找不到依据，所以本页不声称。**

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> **① `#### Subtopics` 的标题层级与同一篇里其它标题不一致。** 逐字：这篇的四个标题是
> `# Offline Result Emulation` / `#### Subtopics` / `## License overview` / `## Functional changes`
> ——**`Subtopics` 用了四级（`####`）**，而它前后的标题是 `#` 与 `##`。
> **同一篇里层级跳了两级。本页照实记，不替它改。**
>
> **② 语法节里的 setup 例子被拆成多个代码块，`</offlineResultEmulation>` 只在最后一块闭合。**
> 语法节里可见：`<offlineResultEmulation>` 开在一个块里，`</offlineResultEmulation>` 闭在
> **第四个**块里，中间几块（`<pattern name="testPattern2">` …、
> `<pattern name="testPatternX1">` …、`<pattern name="testPatternX8">` …）**都是没有根元素的片段**；
> 数字例子那一份同样（第一块停在 `<pattern name="myPattern1">`，下一块才续上 `</pattern>`）。
> **本页没有读它的来源子主题，所以分不清「是语料里就分段写的」还是「抽取时按空行切开的」——
> 两种可能并列，本页不下结论、也不替它合并。**
>
> **③ 参数例子里的元素名与属性之间没有空格，而模拟例子里的同样的东西是正常的。**
> 逐字（语法节里可见）：
> `<measurementname="myMeasurement1">`、`<sitenumber="2">`、`<pinname="Q2">`、
> `<valueval="1.25"/>`、`<measurementname="myMeasurement3">`
> ——**`measurement` 与 `name`、`site` 与 `number`、`pin` 与 `name`、`value` 与 `val`
> 之间都没有空格，粘成了一个词**；
> **而同一节里模拟 API 那一份写的是 `<measurement name="TxDAC_106">`、`<site number="1">`、
> `<pin name="TX0">`** ——**空格是在的**。
> **两处并存于同一页。** 本页照原样列出，**不替它补空格**；
> **也没读来源子主题，所以不判这是转换丢字还是原文如此。**
>
> **④ `[..]` 是原例子里自己写的截断标记，不是本页加的省略号。**
> 语法节波形文件例子里逐字有 `[..]`（单独一行）。
> **按 §11.1，引文里的省略号只在「原文自己就写着它」时合法**——
> **这一处属于那种，照抄时不要把它当语法。**
>
> **⑤ 连字符与空格差一处的写法：`Setup file  mapping to SmarTest concepts`。**
> 语法节那个段名逐字有**两个空格**（`file` 与 `mapping` 之间）。
> **那是子主题的标题，本页照原样引，不替它并成一个空格。**

`verified: doc-only`
