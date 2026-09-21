---
type: object
title: Error Map
layer: file
stage: results
tags: [error-map, failing-cycles, detailed-error-map, overview-error-map, result-analysis, test-processor, results]
related: [error-map-tool, timing-diagram-tool, analysis-views, raw-data-views, data-navigation-views, smartest-6.3.2, smartest-7.0.1]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.08.01_Error_Map.md
created: 2026-09-21
updated: 2026-09-21
verified: doc-only
---

# Error Map

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

**没有加标记的语法段。** 定义文档里没有 `Syntax` / `Parameters` / `Example`
这类**段标记**，跟着 `Subtopics` 找一层也没有。
**所以本脚本一个字都不收录**——没有段标记时「哪一段是语法」是猜，而猜就是编（§4）。

<!-- 语法节 end -->

## 是什么

**本篇正文只有 4 句话**（本页数过），**第一句就是定义句**，逐字：

> 「The error map is the basis for analyzing the test results. SmarTest uses the error map to
> record information about failing test cycles.」

**两句话各办一件事：**

| 原句（**逐字**） | 说的什么 |
|---|---|
| `The error map is the basis for analyzing the test results.` | **它是「分析测试结果」的基础**——**不是一种结果，是分析结果的底料** |
| `SmarTest uses the error map to record information about failing test cycles.` | **装的是 `information about failing test cycles`**——**记的粒度是「失败的测试周期」，不是「失败的测试项」** |

**第 2 句的主语是 `SmarTest`**——**是 SmarTest 用它来记，不是用户去写它。**
**所以本页这个东西是测试系统内部产出、被工具消费的一份数据**，不是一个用户要手工编辑的文件。

**本页 slug 是 `error-map`（这份数据），wiki 另有一页 [[error-map-tool]]（消费它的工具）**——
**两页不是同义词**；本篇这一句 `All result analysis tools (Error Map Tool, Timing Diagram etc.) use
the error map to generate different views to the results you obtain when performing tests.`
就是两者的关系（**工具用 map**）。

### 它有两种：detailed 与 overview

**原文逐字（本篇第 2 句）：**

> 「In fact, SmarTest provides two error maps, a detailed and an overview error map. The Detailed
> error map provides information on the cycle or even the edge level. The overview error map
> combines every 2000 or more cycles into one result depending on the number of cycles of the test
> setup.」

| 种类 | 原文（**逐字**） | 粒度 |
|---|---|---|
| `detailed` | `provides information on the cycle or even the edge level` | **cycle 级，甚至 edge 级** |
| `overview` | `combines every 2000 or more cycles into one result depending on the number of cycles of the test setup` | **每 2000（或更多）个 cycle 合成一个结果** |

**「2000」不是固定值。** 原文写的是 `every 2000 or more cycles`，
紧接着又写 `depending on the number of cycles of the test setup`——
**（推断）2000 是下限，具体多少个 cycle 合成一个结果由 test setup 的 cycle 数决定。**
**依据就是这一句里的 `or more` 与 `depending on` 两个词；
原文没有把这条关系写成一个公式，也没有给任何一张换算表。这是推断，不是文档事实。**

**⚠️ 有一处不对称要点出来：`detailed` 那一支有自己的文档，`overview` 那一支没有。**
本篇的 `#### Subtopics` 三条里只有 `Detailed error map`，**没有 `Overview error map`**
（见 `## 出处` ⑦）。**所以关于 overview 的全部信息，就只有上面这一句。**

### 它在哪：默认在 test processor 内部

**原文逐字（本篇第 3 句）：**

> 「Both of these error maps are located within the test processor. The detailed error map can also
> be located in the external RDRAM. But by default, the internal error map is used. For information
> on the configuration, see Result Mode.」

**这一句里三件事要分清楚：**

| # | 原文（**逐字**） | 含义 |
|---|---|---|
| 1 | `Both of these error maps are located within the test processor.` | **两种都在 test processor 里**（这是共同位置） |
| 2 | `The detailed error map can also be located in the external RDRAM.` | **只有 detailed 这一支「也能」放在外部 RDRAM** |
| 3 | `But by default, the internal error map is used.` | **默认用的是内部那一份** |

**「可以放在外部」与「默认放在内部」是两件事**——**第 2 条是能力，第 3 条是出厂状态。**

**第 2 条有两处原文没交代的：**

- **它只说 detailed「也能」放外部，没说 overview 能不能**——
  **（推断）言下之意是 overview 只能放内部**，**依据只是这一句只点了 detailed；
  原文没有一句排他性的话，所以这是推断。**
- **`external RDRAM` 是什么，原文没有解释**（本页只认得这四个字母是内存的一种，
  本篇没写它的展开，**本页不替它展开**）。

**第 3 条给了唯一的配置出口，逐字**：`For information on the configuration, see Result Mode.`
——**即「选内部还是外部」这件事的说明在 `Result Mode` 那一篇**（**本页没读**）。

### 谁消费它

**原文逐字（本篇第 4 句，也是正文最后一句）：**

> 「All result analysis tools (Error Map Tool, Timing Diagram etc.) use the error map to generate
> different views to the results you obtain when performing tests.」

**拆开看：**

| 原文片段 | 含义 |
|---|---|
| `All result analysis tools` | **所有**结果分析工具——**主语的量词是「全部」** |
| `(Error Map Tool, Timing Diagram etc.)` | **只举两个名字，末尾用 `etc.` 收**——**原文没有列全** |
| `use the error map to generate different views to the results` | **map 是输入，view 是输出** |
| `you obtain when performing tests` | **被看的对象是「跑测试时拿到的那些结果」** |

**所以本页这个对象在整条链上的位置是「中间物」**：
**测试执行产出它，结果分析工具读它、再长出各自的 view。**
**本页只有这一条链，任何一个 view 长什么样，本篇一个字都没有。**

### 本篇的结构

**本篇的顺序是：H1 → `#### Subtopics`（三条链接）→ 四句正文 → `## Functional changes`。**
**目录块在正文之前**，而**正文四句之间的分工很清楚**：
定义（第 1 句）→ 两种 map（第 2 句）→ 在哪（第 3 句）→ 谁用（第 4 句）。

**`#### Subtopics` 是 H4，直接挂在 H1 下面**——**H2 与 H3 在本篇里不存在**
（**与 [[edf]] 那页记的同一个形态；那一条本页引自 [[edf]] 页，不是本篇 raw。**）

## 典型用法

**本篇没有 `## Procedure`、没有 `## Before you begin`、没有一个代码块、没有一条命令、
没有一个配置项。** 正文四句全是陈述，**没有一句是「怎么做」。**

**本篇唯一能落成的用法是「去哪看」**（**三条子主题链接 + 正文里两个出口**，
共 5 条链接，**本页全部没有读过**）：

| 想了解 | 本篇给的出口（**逐字**） | 出口在哪 |
|---|---|---|
| detailed error map 里到底有什么 | `Detailed error map` | 子主题 `02.08.04.08.01.01`；**正文里也链了一次** |
| 怎么设采集方式 | `Setting the acquisition mode` | 子主题 `02.08.04.08.01.02`；**只在子主题列表里出现一次** |
| 怎么把 Timing Diagram 与 Error Map 工具对齐 | `Aligning Timing Diagram and Error Map tool` | 子主题 `02.08.04.08.01.03`；**同上** |
| **怎么配「内部 / 外部」** | `Result Mode` | `02.08.04.08.04.01_Result_Mode.md`——**本篇正文点名的唯一配置出口** |

**四格里没有一格讲 `overview` error map**——**本页对 overview 知道的，只有 `## 是什么`
里那一句。**（**原文在正文里链 `Detailed error map` 链了一次，
**子主题列表里完全没有 overview 的影子**，见 `## 出处` ⑦。）

**从原文能落成的判断只有一条**，**而且它是个提醒**：
**要看 edge 级的失败信息 → 只有 detailed 那一支有**
（原文逐字 `provides information on the cycle or even the edge level`）；
**要省地方 → overview 那一支会合并
（`combines every 2000 or more cycles into one result`）**。
**具体怎么选，本篇没有给判据——它把配置推给了 `Result Mode`。**

## 和谁有关

- [[error-map-tool]] — **消费本页这个对象的工具，也是两页关系的分界**。
  原文逐字：`All result analysis tools (Error Map Tool, Timing Diagram etc.) use the error map to
  generate different views to the results you obtain when performing tests.`
  **即：本页是「被用的那份数据」，那一页是「用它的那个工具」——不是同义词。**
  **本页只有这一句点名，那个工具自己怎么用、有哪些界面，本页一个字都没有
  （那一页本页没读）。**
- [[timing-diagram-tool]] — **（推断）原文那个 `Timing Diagram` 疑似就是它**。
  依据：原文在 `All result analysis tools` 的括号里并列了
  `Error Map Tool, Timing Diagram etc.`，而 wiki 有 [[timing-diagram-tool]] 一页；
  **原文写的是 `Timing Diagram`（两个词、无 `Tool`），与那页的页名不是一字不差，
  而本篇另一处又把两者合起来叫 `Aligning Timing Diagram and Error Map tool`**——
  **所以这两个名字怎么对上，本页没有依据断定。这是推断，不是文档事实。**
- [[analysis-views]] — **（推断）可能就是原文说的那些 `views`**。
  依据：原文说工具们 `use the error map to generate different views to the results`；
  **原文没有点 `analysis-views` 这个名字，那一页本页也没读**。
  **按语义相邻列出，不代表同物。**
- [[raw-data-views]] / [[data-navigation-views]] — **（推断）同上，都是「view」那一侧的名字**。
  **依据只是页名里有 `views`，原文一个都没提**；
  **本页没有依据判断它们与 `error map` 是上下游还是无关。**
- [[smartest-6.3.2]] / [[smartest-7.0.1]] — **版本页**。本页 `## 版本` 两条各落一个：
  `Introduced before SmarTest 6.3.2` 落前者，`SmarTest 7.0.1: …` 落后者。
- `Result Mode`（**未建、不在 allowlist，故用反引号**）— **原文指定的唯一配置出口**：
  `For information on the configuration, see Result Mode.`
  **本页没读**——**所以「内部 / 外部怎么选、在哪配」本页一个字都没有。**
- `Detailed error map`（**未建、不在 allowlist**）— **子主题第 1 条，也是正文里唯一被
  正文再链一次的子主题**。**本页没读**，**所以 detailed 那一支的内容本页没有。**
- `Setting the acquisition mode` / `Aligning Timing Diagram and Error Map tool`
  （**两个，均未建、均不在 allowlist**）— **子主题第 2、3 条**，
  **都只在子主题列表里出现一次，正文一个字没提。本页都没读。**
- `test processor`（**未建**）— **两种 error map 的默认所在**
  （`Both of these error maps are located within the test processor.`）。
  **原文没有解释 test processor 是什么。**
- `external RDRAM`（**未建**）— **detailed error map 的备选位置**
  （`The detailed error map can also be located in the external RDRAM.`）。
  **原文没有解释 RDRAM 是什么，也没有说它多大、放在哪块板上。**
- `Pin Scale 9G` / `prbs`（**两个，均未建**）— **版本段第二条里那两种东西**。
  **本篇没有介绍 `Pin Scale 9G` 是什么卡，也没有展开 `prbs` 这四个字母。**
  **本页不替它展开。**

## 版本

**本文档有 `## Functional changes` 段，两条**，逐字：

- **Introduced before SmarTest 6.3.2**
- **SmarTest 7.0.1: For the test where the Pin Scale 9G pins are used to generate a prbs or compare the DUT data with a prbs, the error map does not work.**

**第一条是 §11.2 ② 那个哨兵。** `Introduced before SmarTest 6.3.2` 的意思是
**「早于语料覆盖范围」**，**不是「6.3.2 新增」**——
**所以 error map 本身成立于哪个版本，这份语料里没有。**

**⚠️ 第二条不是一条「变更」，是一条「已知失效场景」。**
它记的不是「7.0.1 加了什么 / 去了什么」，而是
**「某种测试下 error map 根本不工作」**：主语是 `the error map`，
谓语是 `does not work`。**原文把它挂在 `## Functional changes` 之下、并冠以版本号
`SmarTest 7.0.1:`。**

**这一条有两种读法，原文都排除不了，本页并列不判：**

| 读法 | 说的是 |
|---|---|
| (a) **7.0.1 引入的缺陷** | 版本号前缀表示「从这一版起如此」 |
| (b) **缺陷更早，7.0.1 才写进文档** | 版本号前缀只表示「这一版时记下了这件事」 |

**原文既没说它是「introduced」、也没说它是「known issue」，只有一个版本号加一个冒号。**

**（推断）触发条件是两种测试，`or` 连接**——
逐字 `the test where the Pin Scale 9G pins are used to generate a prbs or compare the DUT data
with a prbs`——**即「用 Pin Scale 9G 的 pin 产生 prbs」或「拿 DUT 数据与 prbs 比较」；
依据就是那个 `or`，但原文把它写成 `the test where … or …`**，
**（推断）这是「一类测试」而不是「两件独立的事」。这是推断，不是文档事实。**

**7.0.1 之后修没修，本篇没有依据**——**版本段只有这两条，之后再没有条目。**

**与 wiki 目标版本（SmarTest 7.10.3）的关系**：
**本篇最后一条是 7.0.1，7.0.1 到 7.10.3 之间 error map 有没有变、上面那条失效还在不在，
本篇给不出任何依据。**

详见 [[smartest-6.3.2]] / [[smartest-7.0.1]]。

## 出处

`sources:` 一篇：
`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.08.01_Error_Map.md`

**本页没做的：**

- **本篇正文只有 4 句话、1,557 个字符**（本页数过），
  **所以本页的「是什么」一节把这 4 句拆开逐句交代，而不是概括**——
  **凡本页没写的（具体格式、字段、容量、每 cycle 记多少位），本篇都没有。**
- **三条子主题一条都没读**（`Detailed error map` / `Setting the acquisition mode` /
  `Aligning Timing Diagram and Error Map tool`）——
  **这是本页最大的空缺：detailed 那一支的实际内容全部在子主题里，本页只有
  「它到 cycle / edge 级」这一句。**
- **`Result Mode` 没读** —— **而它是原文指定的唯一配置出口**
  （`For information on the configuration, see Result Mode.`），
  **所以「内部还是外部怎么选、在哪改」本页给不出来。**
- **`overview` error map 在语料里找不到对应的文档页**
  （子主题列表里没有它，见下 ⚠️ ⑦）——**本页对它的全部认识就是正文那一句。**
- **`test processor` 与 `external RDRAM` 都没读、原文也没解释** ——
  **所以「内部 / 外部」在物理上指什么、差别多大，本页一个字都没有。**
- **`Pin Scale 9G` 与 `prbs` 都没读、原文也没展开** ——
  **所以版本段那条失效的触发条件，本页只能照抄原句。**
- **一张图都没有。** 原文没有图片（本页查过：0 处图片语法）。
- **没有交叉验证任何别处的文档**（§11：本页只写这一篇里有的）。
  **尤其：[[error-map-tool]] / [[timing-diagram-tool]] 都没读**——
  **本页与它们的关系全部取自本篇这一篇的正文，没有从对面回校过。**
- **`layer: file` / `stage: results` 不是本篇写的**——
  **本篇没有 `## Application` 这类自我定位段**，这个归属是本 wiki 的既有划分。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> **① 正文只有 4 句，且四句的分工整齐到像提纲。** 逐字（正文全部非空行）：
> `The error map is the basis for analyzing the test results. SmarTest uses the error map to record information about failing test cycles.` /
> `In fact, SmarTest provides two error maps, a detailed and an overview error map. …` /
> `Both of these error maps are located within the test processor. …` /
> `All result analysis tools (Error Map Tool, Timing Diagram etc.) use the error map to generate different views to the results you obtain when performing tests.`
> ——**四句话把「是什么 / 有几种 / 在哪 / 谁用」各占一句，
> 没有一句过渡、没有一个小节标题。本页照实说，不替它扩写。**
>
> **② `#### Subtopics` 是 H4，直接挂在 H1 下面。** 本篇的非 H1 标题只有这一个，
> 层级是 H4——**H2 与 H3 在本篇里不存在**。
> （**与 [[edf]] 那页记的同一个形态；那一条本页引自 [[edf]] 页，不是本篇 raw。**）
>
> **③ 子主题目录块排在正文之前，而 `## Functional changes` 排在正文之后。**
> 本篇的顺序是：H1 → `#### Subtopics`（三条）→ 四句正文 → `## Functional changes`。
> **目录与正文之间没有标题分隔**，三条 bullet 结束后直接接段落。
>
> **④ 五个链接全部是 `[文本](<文件名.md>)` 的写法**——**文件名外面套尖括号、
> 且不带任何目录前缀**（只靠同级目录相对定位）。逐字例：
> `- [Setting the acquisition mode](<02.08.04.08.01.02_Setting_the_acquisition_mode.md>)`。
>
> **⑤ `Detailed error map` 在**同一篇**里被链了两次，另两条子主题一次都没被正文提到。**
> 子主题列表逐字：
> `- [Detailed error map](<02.08.04.08.01.01_Detailed_error_map.md>)`；
> 正文第 2 句逐字：
> `The [Detailed error map](<02.08.04.08.01.01_Detailed_error_map.md>) provides information on the
> cycle or even the edge level.`
> ——**同一个文件、同一个相对路径，链两次**；
> **而 `Setting the acquisition mode` 与 `Aligning Timing Diagram and Error Map tool` 两条
> 只在子主题列表里出现，正文一个字都没提。** **本页照实说，不替它加。**
>
> **⑥ `etc.` 收尾，工具清单没有列全。** 逐字：
> `All result analysis tools (Error Map Tool, Timing Diagram etc.) use the error map …`
> ——**括号里只给了两个名字，用 `etc.` 收口；
> 主语却是 `All`。本页照实说：本页只知道这两个名字。**
>
> **⑦ `overview error map` 没有对应的子主题。** 正文第 2 句说
> `SmarTest provides two error maps, a detailed and an overview error map`，
> **而 `#### Subtopics` 三条里只有 `Detailed error map`，
> 没有 `Overview error map`**。
> ——**两种 map 里有一种没有自己的文档出口。本页照实并列，不替它补一条。**
>
> **⑧ 版本段第二条读起来是「已知失效」而不是「变更」。** 逐字见 `## 版本`。
> ——**原文把它放在 `## Functional changes` 下，措辞却是 `the error map does not work`；
> 是缺陷引入还是补记，原文没有交代。本页并列两种读法，不判哪个。**
>
> **⑨ 本篇没有 §11.2 ① 那种编码损坏**（本页查过：汉字 0 个、`鈥` 0 处）。
> **本篇 1,557 个字符，是本批 7 页里第二短的一篇。**

`verified: doc-only`
