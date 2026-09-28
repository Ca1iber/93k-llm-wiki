---
type: object
title: playPattern()
layer: L2
stage: pattern
tags: [pattern, play-pattern, l2, test-method-api, multiport, cct, synchronization]
related: [cct-multiport-sequencer-synchronizer-api, multiport-burst-editor, pattern, primary-status, test-method-class, test-suite, port-editor, testmethod]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.149_playPattern.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# playPattern()

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **523 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.149_playPattern.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
void playPattern(const STRING& _burstName);
```

### Example

```
CCTMultiportSync     Sync;
...
GET_TESTSUITE_NAME(tsName);
Sync.registerCCTestMethod(tsName, this);
...
PatternPort::getInstance().setPort(Port);
PatternPort::getInstance().setWaitTemplatePatternName(WaitTemplate);
Sync.registerSyncPort(PatternPort::getInstance());

Sync.start();

if(CCTgetDevelopMode()!=0)
{
        PatternPort::getInstance().playPattern(FlatPatt);
}
Sync.sync();
Sync.flush();
Primary.label(Sync.getMultiPortBurstName());
Sync.dumpMPBGraph();

```

<!-- 语法节 end -->

## 是什么

**`playPattern()` 是 CCT Multiport Sync（多端口同步）那一族里的一个成员 API：
它把一个 `PatternPort` 的 label 嵌进输入的 burst pattern label 里。** 原文全文只有两句：

> 「This API is used to embed PatternPort Label to this input burst pattern label.」

> 「This function is defined in the header file
> /opt/hp93000/soc/testmethod/include/CCTMultiportSync.hpp.」

**第一句是它的职能，第二句是它的位置**——而**第二句里有个值得注意的落差**：
**函数声明在 `CCTMultiportSync.hpp` 里，调用却写在 `PatternPort` 的实例上**
（示例逐字：`PatternPort::getInstance().playPattern(FlatPatt);`）。
**本篇没有解释这两者是什么关系**（**语料未写**）。
按 [[cct-multiport-sequencer-synchronizer-api]] 那份「族」名单，
`PatternPort& getInstance()` 与 `playPattern()` 是**两条并列的成员页**，
**所以「它属于 PatternPort 还是 CCTMultiportSync」这一点，语料只能从签名表读，本篇读不出来。**

### 签名：一个参数，**没有参数释义**

```
void playPattern(const STRING& _burstName);
```

| 项 | 值 |
|---|---|
| 返回 | `void`——**没有返回值，也没有状态可查** |
| 形参 | `const STRING& _burstName`，一个 |
| **参数释义** | **本篇没有 `Parameters` 段，一个字都没有。** **`_burstName` 到底指什么、格式如何，语料未写**（见「出处」） |

**唯一的线索是示例里的实参**：本页示例传的是 `FlatPatt`（一个变量），
而**另一篇**（`.02`，见「出处」）里传的是字符串字面量
`PatternPort::getInstance().playPattern("ADC_Control");`——**两种形态都出现过**。
**（推断）`_burstName` 是一个 flat pattern / flat label 的名字**：
依据是**两篇的例子都拿它跟 flat pattern 绑在一起**（本页变量名 `FlatPatt`、
`.02` 那次实参是端口名 `"ADC_Control"`），**但两篇都没有一句参数说明。**

### 示例里的位置：**它只在一个 `if` 里被调用**

本例的完整代码在「语法 / 参数」节（脚本逐字抽的），**这里是逐句读法**：

| 行（逐字） | 它在这一串里干什么 |
|---|---|
| `CCTMultiportSync     Sync;` | 建一个同步器对象 |
| `...` | **原文自带的省略号**（省略的是别处的准备代码） |
| `GET_TESTSUITE_NAME(tsName);` | 取当前 test suite 名 |
| `Sync.registerCCTestMethod(tsName, this);` | **把当前 test method 注册给同步器**（`this` 就是调用者） |
| `PatternPort::getInstance().setPort(Port);` | 给 `PatternPort` 设端口 |
| `PatternPort::getInstance().setWaitTemplatePatternName(WaitTemplate);` | 设 **wait template pattern 名** |
| `Sync.registerSyncPort(PatternPort::getInstance());` | **把这个端口注册进同步器**（同步只对已注册端口做） |
| `Sync.start();` | 起同步段 |
| `if(CCTgetDevelopMode()!=0)` | **只在「非生产模式」时才进这一支**（见下） |
| `PatternPort::getInstance().playPattern(FlatPatt);` | **本页的主角**：把 `FlatPatt` 这个 label 播进这个端口 |
| `Sync.sync();` / `Sync.flush();` | 结束同步段 |
| `Primary.label(Sync.getMultiPortBurstName());` | **把同步器拼出来的 multiport burst 名设成 sequencer 的 start label** |
| `Sync.dumpMPBGraph();` | 把组装结果画出来 |

**那个 `if` 不是随手写的，它对应一条文档规则**——来自**另一篇**
（`.01`，见「出处」）的 `## Development Mode` 一节，逐字：

> 「Sets the develop mode of the MultiportSync instance. It skips burst in Production Mode for
> Throughput. The available mode are:」

> 「0 = OFF」

> 「1 = Learning (if setup exists, then use it. Otherwise create it)」

> 「2 = Development (if setup exists, delete it and re-generate it」

**三档里只有 `0` 是「关」**——所以 `CCTgetDevelopMode()!=0` 恰好是
**「不在生产模式（OFF）时才播」**（**推断**：依据是那条 `It skips burst in Production Mode for
Throughput.` 与三个取值的字面；**本页 raw 一个字没讲 develop mode**）。
**这条规则的用意是省时间：生产模式下跳过 burst 生成。**

### 它在整条链上的位置

**它不是「跑 pattern」，是「把一段 single-port pattern 挂到 multiport burst 上去」**，
而且是**在同步段内、由同步器接管的那种挂法**。依据是本篇示例的次序
（`Sync.start()` → `playPattern()` → `Sync.sync()`）**与另一篇对同一个 API 的归类**
（`.01` 的标题级目录把它列在 `## Playing a flat pattern` 之下，见「出处」）。
**「跑起来之后会怎样、label 之间怎么对齐」在本页 raw 里一个字没有**——
那属于 [[cct-multiport-sequencer-synchronizer-api]] 那一页讲的同步机制。

## 典型用法

**本篇没有 `## Procedure`、没有 `## Before you begin`、没有编号步骤**——
它整篇是「两句散文 + 一个签名 + 一段示例 + 一条相关链接 + 一行版本」。
**所以下面的顺序是本页从两篇 raw 的示例里拼出来的，不是原文写的步骤**（依据逐条注明）。

**1. 调用顺序（本篇示例 + `.02` 的同类示例，两处次序一致）**：

| # | 做什么 | 逐字依据 | 出处 |
|---|---|---|---|
| 1 | 建同步器 | `CCTMultiportSync     Sync;` | 本页示例 |
| 2 | （把 test method 注册进去） | `Sync.registerCCTestMethod(tsName, this);` | 本页示例 |
| 3 | 给端口设端口名 / wait template | `PatternPort::getInstance().setPort(Port);` / `setWaitTemplatePatternName(WaitTemplate);` | 本页示例 |
| 4 | **注册这个端口** | `Sync.registerSyncPort(PatternPort::getInstance());` | 本页示例 |
| 5 | 开同步段 | `Sync.start();` | 本页示例 |
| 6 | **`playPattern(<burst pattern 名>)`** | `PatternPort::getInstance().playPattern(FlatPatt);` | 本页示例 |
| 7 | 收同步段 | `Sync.sync();` / `Sync.flush();` | 本页示例 |
| 8 | 把 burst 名交给 sequencer 当 start label | `Primary.label(Sync.getMultiPortBurstName());` | 本页示例 |

> **第 6 步的位置是这条 API 最实用的信息**：它在 `start()` 之后、`sync()` 之前——
> **也就是「这一段归同步器管」的区间内。**
> **`.02` 里那段同名示例少了三处**：第 2 步（`registerCCTestMethod`）、
> 示例末尾的 `Primary.label(...)` 与 `dumpMPBGraph()`、以及那个 `if` 外包装；
> **`start` → `playPattern` → `sync` → `flush` 这四行两处逐字相同**，
> **`.02` 那边没有多出来的行**（**读到的另一篇**，见「出处」）。

**2. 前置条件（三条硬约束，来自另一篇 `.09` 的 `Prerequisites` 段）**：

> 「Before you can use the CCT Multi-port Sequencer Synchronizer API, make sure that the following
> conditions are met:」

- `Digital pattern must be multi-port based` → [[pattern]]
- `Timing set must be multi-port based` → [[timing]]
- `Must be used in Concurrent Test Framework environment`

**这三条属于整个 API 集，不只是本函数**；**`playPattern()` 自己有没有额外的前置条件，
本篇没有写。**

**3. 什么时候用它**：

| 你的情形 | 用不用它 |
|---|---|
| **要把一段 single-port flat pattern 塞进 multiport burst 的某个端口** | **用它**（原文 `embed PatternPort Label to this input burst pattern label`） |
| **已经有了 flat pattern、只想让它在生产模式跑** | **不用**——示例里那一支被 `if(CCTgetDevelopMode()!=0)` 挡着，**生产模式下跳过 burst 生成** |
| **要同步的是 PA transaction / DC 测试 / digital capture** | **不是这个函数**：那些走 `RegisterControlPort` 那一族 / `DCDynamicPort` / `DigitalCapturePort`（**读到的另一篇**；本页不展开，见 [[cct-multiport-sequencer-synchronizer-api]]） |

**4. 限制（三条，属整个 API 集，来自 `.09` 的 `Limitations` 段）**：

- `Ports containing CTIM/CLEV in the digital pattern are not supported.`
- `D2S is not supported`
- `BADC is not supported`

**5. 出错怎么办**：**本篇没有 `## Errors` 段，也没有 `## Warnings` 段**
（骨架里因此没有「报错条件」节，不是漏写）；
**`playPattern()` 自己失败时是什么表现，语料未写**（见「出处」）。

## 和谁有关

- [[cct-multiport-sequencer-synchronizer-api]] — **父页（上游）**。本篇 `## Related information`
  只有这一条链接；而**那一页的「族」名单里确实列着 `playPattern()`**
  （**本页读到的 wiki 页**——那一页自己写明：这份名单「来源是链接结构，不是任何一句原文」）。
  **整个 API 集的前置条件、限制、同步机制都在那一页，本页不重复。**
- [[pattern]] — **`stage: pattern` 的阶段页**。它的 L2 表里有一行逐字写着
  `[[play-pattern]]（L2，02.07.04.01.149）— 播放 pattern，多端口用 PatternPort / CCTMultiportSync 同步。`
  （**本页读到的 wiki 页**，不是本篇 raw）。
- [[multiport-burst-editor]] — **GUI 侧的对物（同类）**：那里是人在界面上编 multiport burst /
  port burst，本页是代码里往 burst 上挂 label。**本页 raw 没有提它**，
  「对物」的依据是两边讲的都是 multiport burst（**本页的观察**）。
- [[primary-status]] — **示例最后一步的下游**：`Primary.label(Sync.getMultiPortBurstName());`
  把 burst 名设成 sequencer 的 start label，**这一步才让 pattern 有了执行入口**。
- [[test-method-class]] — **调用者是谁（上游）**：示例里 `Sync.registerCCTestMethod(tsName, this);`
  把 `this`（当前 test method）注册进去，**所以这个 API 是从 test method 里调的**。
- [[testmethod]] — **`layer: L2` 的归属侧**。**这是本页从 frontmatter 读出来的结构**
  （`layer: L2` + `stage: pattern` + 调用方是 test method），**不是本篇的一句话**；
  本篇只提供了那句 `Sync.registerCCTestMethod(tsName, this);`。
- [[test-suite]] — **`GET_TESTSUITE_NAME(tsName)` 取的就是它**；
  另一篇还提到 CCT group 下**每个 test suite 各有自己的 multiport burst**、
  并发执行时可以跨 test suite 拼（**读到的另一篇**，本页不展开）。
- [[port-editor]] — **端口那一侧的 GUI**（`setPort()` 设的端口从哪来）。**本页 raw 没提它**，
  这一条是并列关系，不是文档事实。
- [[smartest-7.3.2]] — **引入版本**（见「版本」）。
- `PatternPort` / `CCTMultiportSync` / `DCDynamicPort` / `DigitalCapturePort`（**均未建**）—
  **同一族的类**。**`PatternPort` 尤其要留意**：本页的函数声明在 `CCTMultiportSync.hpp` 里，
  **却在 `PatternPort` 上调用**——**这个落差本篇没有解释**（见「是什么」）。

## 版本

**本文档有 `## Functional changes` 段，段里只有一条**：

- `Introduced in SmarTest 7.3.2`

**这一条不是 §11.2 ② 那个哨兵值**——它写的是 `Introduced in`（没有 `before`），
**是一个真版本号**：**`playPattern()` 在 SmarTest 7.3.2 引入**，本 wiki 面向 7.10.3，所以在。

**它和父页对得上**：[[cct-multiport-sequencer-synchronizer-api]] 的版本段也是
`Introduced in SmarTest 7.3.2`，**读到的另一篇**（`.01`）的版本段同样是这一条。
**三处一致**——**所以「这一族是 7.3.2 一次性进来的」这个读法有三份依据**
（**推断**：三处都只写了同一个版本号，**没有一处写「本函数比 API 集晚」或「早」**）。

**版本段里没有的东西**（照实记，不替它补）：**没有第二条**。
所以「`PatternPort` 这个类是哪一版加的」「示例里的 `setWaitTemplatePatternName` 是哪一版加的」
**在本篇里查不到**。

## 出处

`sources:` 一篇：

- `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.149_playPattern.md`
  （frontmatter 的 `source_topic` 是 `148423.htm`；**1,228 字节 / 49 行，整篇读完**——
  字节按 `st_size`、行数按 `wc -l`，§11.5 口径）
- 本页的「语法 / 参数」节是脚本从这一篇抽的（**本页一个字没动**）。
- **本篇没有 `## Errors` / `## Warnings` 段**，所以本页没有「报错条件」节——不是漏写。
- **上游 `.htm` 核过**：`raw/148423.htm`（**2,499 字节**；`<img` **0 次**）。
  **核的是示例里的两个 `...`**：那一行在 `.htm` 里就是 `...`（原文自带的省略号），
  **不是压缩或抽取加的**——所以本页引它时不构成 §11.1 的「自加省略号」。

### ⚠️ 本页动了 PROSE-SPEC 的「例外」并在此声明（这是本节最要紧的一段）

**`sources:` 那一篇是一个 49 行的壳**：正文只有两句散文 + 一个签名 + 一段示例 +
一条相关链接 + 一行版本，**机制整段推给了 `## Related information` 指的
`CCT Multiport Sequencer Synchronizer API`**。
按 PROSE-SPEC 的例外条款（`sources:` 那篇若是**纯索引**、或**只有几十行的壳**，
可以读那些子主题，**但必须在 `## 出处` 里逐条声明**），
**本页读了下面三篇**——**三次取材的用途与边界，逐条列出**：

| 读了哪一篇 | 路径 | 字节 / 行数 | 为什么读 | 读了哪部分 |
|---|---|---|---|---|
| **CCT API 集索引** | `03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.05.09_CCT_Multiport_Sequencer_Synchronizer_API.md` | **5,717 / 102** | **本篇 `Related information` 指的就是它**；前置条件、限制、同步机制只在它里面 | **整篇读完** |
| **它的子主题（用法）** | `03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.05.09.01_Using_the_CCT_Multi-Port_Sequencer_Synchronizer_API.md` | **8,698 / 158** | 索引的 `#### Subtopics` 第一条；**`## Development Mode` 与 `## Playing a flat pattern` 两节解释示例里那个 `if`** | **整篇读完** |
| **它的子主题（API 清单）** | `03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.05.09.02_CCT_multi-port_user_interface_APIs.md` | **11,714 / 346** | 索引的 `#### Subtopics` 第二条；**里面有 `playPattern` 的另外两处调用**（含一处字符串字面量实参） | **⚠️ 只读了两个片段：第 1–60 行与第 180–319 行**；**第 61–179 行与第 320–346 行没读** |

**三条边界，写清楚**：

1. **上面凡是出自这三篇的话，本页都标了「读到的另一篇」。**
   它们**不是**本页 `sources:` 的内容，**本页不为它们的完整性背书**。
2. **`.02` 本页没有整篇读完**（见上表最后一行）——
   **所以「`PatternPort` 到底是什么、`setWaitTemplatePatternName` 的语义、
   `Sync.start()` 到 `Sync.flush()` 之间到底发生什么」本页一个字没有**，
   **别看本页读了三篇就以为那一族读全了。**
3. **本页的 figure 证据只有一张**：`.09` 里的
   `raw/148151.png`（**6,060 字节**）——**图证**：四列端口
   （`JTAG_Port` / `Trigger_Port` / `DC_Port` / `Digital_Capture_Port`）的时间线，
   蓝色块是各自的活动（`Send device set up sequence using JTAG interface` /
   `Trigger 1st RF waveform` / `Measure Current` / `Digital Capture`，
   另外几格是 `Wait`），**右侧有两个 `sync` 标记**（两个同步点）。
   **它是 `.09` 的图，不是本篇的图**；**图里的字搜不到**（§11.4），
   **而且它没有版本标注**——**所以本页没有用它下任何关于版本的结论。**
   `.01` 里另有四张图（`148163.png` / `148164.png` / `148174.png` / `148383.png`），
   **本页没看**。

**本页没做的**：

- **`PatternPort` 那一篇没读**（本页只在 `[[cct-multiport-sequencer-synchronizer-api]]`
  的族名单里见过这个名字）。**所以上面那个「声明在 `CCTMultiportSync.hpp`、调用在
  `PatternPort` 上」的落差，本页只指出它，不解释它。**
- **`registerCCTestMethod` / `registerSyncPort` / `getMultiPortBurstName` / `dumpMPBGraph` /
  `setWaitTemplatePatternName` 各自的成员页一篇没读**——
  **示例里每一步的语义，本页只有「这一行大概在做什么」这一级**（依据是方法名的字面），
  **不是文档事实。**
- **同族的 `DCDynamicPort` / `DigitalCapturePort` / `RegisterControlPort` 一侧没读。**
- **`CCTgetDevelopMode()` 自己那一篇没读**（`.01` 的 `## Development Mode` 是二手）。
- **没在任何 93K 机台上调过 `playPattern()`**（`verified: doc-only`）。
  **所以「传一个不存在的 burst 名会怎样」「生产模式下跳过它会不会报错」本页答不了。**

> ⚠️ **语料瑕疵（三处在本篇，三处在读到的另一篇），逐条照实记、一处都没替它改**：
> **① 本篇只有两句话，参数一个字没有。** 一个 `const STRING& _burstName` 形参
> **没有任何参数释义**——**这是本篇最大的空白**（不是缺陷记录，是取材事实）。
> **② 本篇的 `## Related information` 只有一条**（`CCT Multiport Sequencer Synchronizer API`），
> **所以「本函数还能跟谁一起用」本篇没有说**——上面「和谁有关」里凡是超出这一条的，
> 本页都标了依据来源。
> **③ 坏字：本篇 0 个。** 按 §11.2 ① 的判据（英文文档里出现任何汉字都是坏字）逐字查过，
> **本篇一个汉字都没有**——**但这是「本页读到的」，不是「本篇没有」**（§13.1：没找到 ≠ 没有）。
> **④ `.09` 里有一处坏字**：逐字为 `- Insert sequencer鈥慶ontrolled DC tests into the pattern`，
> **`鈥慶` 是 `‑c` 的乱码形态**（对照表 `extract/encoding-map.csv` 第 6 行：`鈥慶` = `‑c`），
> **所以原文此处应为 *sequencer-controlled***。**本页照原样引，旁边注正字。**
> 同篇还有一处 `the length or execution time of each port鈥檚 labels is recorded`——
> **`鈥檚` = `'s`**（对照表第 20 行），即 *port's*。
> **⑤ `.01` 里有两处**：`where n 鈮?1 (default 1)`（出现两次）——
> **`鈮` 按对照表第 123 行只能报「原字符落在 U+2240–U+227F 之间」（第三字节已丢，反解不了）**，
> **上下文是「大于等于」，但本页不给它定字**（§11.2 ①：这一类不许当映射用）；
> 以及 `## Development Mode` 最后一条逐字是
> `2 = Development (if setup exists, delete it and re-generate it`
> ——**少一个右括号**，本页照原样引（见「是什么」）。
> **⑥ 读到的另一篇里还有一批代码级毛病，本页没有引用它们，所以不逐条展开**；
> 其中与本页示例**直接相关**的一处要记：`.01` 与 `.02` 里的同名代码段
> `Lshift::getINstance(tsName).write(0x18, 0x22);` **把 `getInstance` 写成了 `getINstance`**
> （**同一段里 `getInstance` 与 `getINstance` 混用**）——
> **本页的示例里没有这一行**（本篇 raw 里没有 `Lshift`），
> **记在这里是因为拿本页去搜那一族的人会撞上它。**
> **这一族的编码损坏与代码毛病，[[cct-multiport-sequencer-synchronizer-api]] 那一页已先记过两处。**

`verified: doc-only`
