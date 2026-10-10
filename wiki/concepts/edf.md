---
type: concept
title: Event Data Logging Format (EDF)
layer: file
stage: results
tags: [edf, event-data-logging, data-logging, logging-format, results-file, subtopic-index]
related: [edf-data-organization, edf-data-types, event-formatter, stdf, edl-file, data-retrieval-library, timestamp-attr-type, data-logging-profiles]
sources:
  - 02_System_reference/02.10_Data_Logging/02.10.01.06_Event_Data_Logging_Format__EDF.md
created: 2026-09-21
updated: 2026-09-21
verified: doc-only
---

# Event Data Logging Format (EDF)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **249 字符逐字取自** `<02_System_reference/02.10_Data_Logging/02.10.01.06_Event_Data_Logging_Format__EDF.md>` 及其子主题 `<02_System_reference/02.10_Data_Logging/02.10.01.06.05.54_TestConditionAttrType.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax（取自子主题 Attribute types › TestConditionAttrType）

!`TestConditionAttrType structure`（raw: `../../../../raw/127716.png`）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/127714.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：6 行 × 4 列。
> 首行（上游原文）：Field name | Data type | Description | Comments

<!-- 语法节 end -->

## 是什么

**本篇不是一篇说明文，是一条「子主题清单」。**
`## 语法 / 参数` 节以外的全部正文只有 7 行（更准确地说：全文 14 行，frontmatter 占 5 行，
正文 9 行里还有 2 行空行）——**一行 H1、一行 H4、五条子主题链接，此外一句陈述句都没有。**

**所以「EDF 是什么」这句定义，本页写不出来——语料未写。**
本页能做的是：把本篇**有**的东西（标题、五个子主题名、编号、链接写法）逐字摆清楚，
并把它**没**说的东西（定义、用途、谁写谁读、什么时候生成）也摆清楚。

**`EDF` 三个字母展开成 `Event Data Logging Format`，这串字只出现在标题里**——
H1 是 `# Event Data Logging Format (EDF)`，frontmatter 的 `title` 是
`"Event Data Logging Format (EDF)"`。**正文里一次都没有展开过这个缩略语。**
**标题里的展开是「全称」，不是「定义」**——它没说 EDF 是什么、装什么、给谁看。
**本页不拿它当定义句，也不替它补一句。**

### 全篇正文，逐字

本篇正文的全部内容就是下面这些（除标题外，逐字，含列表符）：

> `- [EDF data organization](<02.10.01.06.01_EDF_data_organization.md>)`
> `- [EDF data types](<02.10.01.06.02_EDF_data_types.md>)`
> `- [Event types](<02.10.01.06.03_Event_types.md>)`
> `- [Creating your own custom events with the DCL library](<02.10.01.06.04_Creating_your_own_custom_events_with_the_DCL_library.md>)`
> `- [Attribute types](<02.10.01.06.05_Attribute_types.md>)`

**标题两行也是逐字**：`# Event Data Logging Format (EDF)` 与 `#### Subtopics`。

### 五个子主题，逐字

| # | 子主题名（**逐字**） | 链到的文件（**逐字**） | 本 wiki 有没有页 |
|---|---|---|---|
| 1 | `EDF data organization` | `02.10.01.06.01_EDF_data_organization.md` | 有：[[edf-data-organization]] |
| 2 | `EDF data types` | `02.10.01.06.02_EDF_data_types.md` | 有：[[edf-data-types]] |
| 3 | `Event types` | `02.10.01.06.03_Event_types.md` | **无** |
| 4 | `Creating your own custom events with the DCL library` | `02.10.01.06.04_Creating_your_own_custom_events_with_the_DCL_library.md` | **无** |
| 5 | `Attribute types` | `02.10.01.06.05_Attribute_types.md` | **无** |

**这五行是本篇唯一承载信息的五句话**，**它们都是名词短语，不是句子**——
**把链接一去掉，本篇就没有任何可读内容了。**

**（推断）这五条就是 EDF 这一节的覆盖面**——数据怎么组织、有哪几种数据类型、
有哪几种事件、怎么自己造事件、属性（attribute）有哪几种。
**依据只是这五个名字本身；原文没有一句话说「EDF 包含以下五部分」或类似的话。
这是推断，不是文档事实。**

### 编号里藏着的一层结构（推断）

**（推断）这五条是本篇的直接子项，而第 5 条 `Attribute types` 自己还有子项。**

- **依据一**：五条的编号是 `02.10.01.06.01` … `02.10.01.06.05`，
  **正好接在本篇编号 `02.10.01.06` 后面多一位**——按这套编号法，多一位就是低一层。
- **依据二**：本页 `## 语法 / 参数` 节自己的来源标注写着
  `<02_System_reference/02.10_Data_Logging/02.10.01.06.05.54_TestConditionAttrType.md>`
  ——**编号是 `.06.05.54`，比第 5 条 `.06.05` 又多一位**。
- **所以 `.06.05.54` 挂在 `Attribute types` 底下。**

**要注意的是：本篇正文没有链到 `.06.05.54`，只链到 `.06.05`。**
**本页的语法节是从那个更深一层的子主题抽的，而本篇正文提都没提它**——
**这是一处以「页面的语法节来源」和「本篇正文的链接」不一致的地方，本页照实并列。**

### `## 语法 / 参数` 节里有什么（以及它为什么不是本页的定义）

本页语法节**不是本篇抽的**，节首那行 ⚠️ 已经写明：
来源是**子主题** `<…06.05.54_TestConditionAttrType.md>`，**不是定义文档自己写的**。

节里只有一张表和一个图引用：

| 节里的内容 | 逐字 | 是什么 |
|---|---|---|
| 图引用 | `!TestConditionAttrType structure`（raw: `../../../../raw/127716.png`） | **一张结构图，本页没打开** |
| 表头 | `Field name` / `Data type` / `Description` / `Comments` | 四列 |
| 字段 1 | `length` / `int` / `Attribute length` | 备注列逐字 `These fields form the attribute header.`——**注意 `fields` 是复数，说明这句管的不止这一行；表格压平之后看不出它跨几行** |
| 字段 2 | `type` / `short` / `Attribute type` | **备注列是空的** |
| 字段 3 | `conditionCount` / `unsigned short` / `Number of conditions (pairs of a Key string and a Value string).` | 说明后面成对出现 |
| 字段 4 | `Key` / `string` / `Name of the condition` | 成对的前一半 |
| 字段 5 | `Value` / `string` / `Value of the condition` | 成对的后一半 |

**注意它描述的是 `TestConditionAttrType` 一个结构，不是一个格式（format）的全貌**——
**「EDF 的语法」这句，本篇和这个子主题都没有给。**
**本页不拿这张表去反推 EDF 的定义**（§11：不许把别处文档的内容写进本页正文；
何况这一节的来源子主题本页根本没读，见 `## 出处`）。

### 本篇「没有」的清单（这些是事实，不是缺陷）

| 本篇有没有 | |
|---|---|
| `## Functional changes` | **没有** |
| `## Errors` / `## Warnings` | **没有** |
| `## Procedure` / `## Before you begin` | **没有** |
| 代码块 | **0 个** |
| 图片（正文） | **0 张**（语法节那张图来自子主题） |
| 链接 | **5 条，全部指向子主题**（没有一条指向别处、没有外链） |
| 定义句 | **0 句** |

## 典型用法

**本篇没有 `## Procedure`、没有 `## Before you begin`、没有一句可执行的话、没有一个代码块。**
**所以「EDF 怎么用」本页给不出来——语料未写。**
**本篇唯一能落成的用法是导航**：想知道什么，去哪个子主题。
（**子主题的实际内容本页一条都没有**，见下表和 `## 出处`。）

| 想了解 | 本篇给的出口（**逐字**） | 出口那边 |
|---|---|---|
| EDF 的数据怎么组织 | `EDF data organization` | 子主题 `.06.01`；wiki 页 [[edf-data-organization]]（**本页没读**） |
| 有哪几种数据类型 | `EDF data types` | 子主题 `.06.02`；wiki 页 [[edf-data-types]]（**本页没读**） |
| 有哪几种事件 | `Event types` | 子主题 `.06.03`；**wiki 无页、本页没读** |
| 怎么自己造事件 | `Creating your own custom events with the DCL library` | 子主题 `.06.04`；**wiki 无页、本页没读** |
| 属性有哪几种、长什么样 | `Attribute types` | 子主题 `.06.05`；**wiki 无页、本页没读**；本页语法节那张表抽自它下面的 `.06.05.54` |

**这张表只能当目录用，不能当依据用**——
**表里五条的实际内容，本页和本篇都没有。**
**尤其：五个出口说的全是「EDF 里有什么」，没有一个出口说「EDF 用来干什么」。**

**一处要提醒的**：`EDF` 这个缩略语在本篇的**子主题名里也只出现两次**
（`EDF data organization`、`EDF data types`），**后三条子主题名改用 `Event` / `Attribute`**
——**同一张清单里，前两条用缩略语、后三条不用，本篇没有解释为什么**（见 `## 出处` ②）。

## 和谁有关

- [[edf-data-organization]] — **本篇正文第 1 条子主题**（逐字 `EDF data organization`），
  链到 `02.10.01.06.01_EDF_data_organization.md`。
  **本篇只有这一行链接，那个子主题讲什么、本页没读那一页，所以本页给不出它的内容。**
- [[edf-data-types]] — **第 2 条**（逐字 `EDF data types`），链到 `…06.02`。
  **同上：本篇只有这一行链接，本页没读那一页。**
- [[event-formatter]] — **（推断）上下游，但依据很弱**。
  **依据只有两条**：① 两页的 frontmatter 同组（`layer: file`、`stage: results`）；
  ② 名字上一个像「事件的格式」、一个像「事件的格式化器」。
  **本篇一个字都没提 Event Formatter，那一页本页也没读。**
  **这是推断，不是文档事实——本页不据它写任何机制。**
- [[stdf]] / [[edl-file]] — **（推断）同类，都是 results 侧的「文件 / 格式」页**。
  **依据只是 frontmatter 的分组**（同样是 `layer: file`、`stage: results`）；
  **本篇没有提过这两个名字，两页本页也都没读。**
- [[timestamp-attr-type]] — **（推断）同族的另一个 `…AttrType`**。
  依据：本页 `## 语法 / 参数` 节里的结构叫 `TestConditionAttrType`，
  而 allowlist 里另有一个 `timestamp-attr-type`（`TimestampAttrType`）——
  **两者名字同构**。**但本页没读那一页、也没读 `TestConditionAttrType` 所在的子主题，
  所以它们是不是同一套机制、有没有共同父类，本页没有依据判断。**
- [[data-logging-profiles]] / [[data-retrieval-library]] — **（推断）同章**。
  依据：本篇 `sources:` 路径的前两级是 `02_System_reference/02.10_Data_Logging/`，
  **从路径看它们落在 Data Logging 这一章里**；
  **本篇正文没有提到它们，两页本页也都没读。**
- `Event types` / `Creating your own custom events with the DCL library` / `Attribute types`
  （**三个，均未建、均不在 allowlist，故用反引号**）——
  **本篇正文第 3 / 4 / 5 条子主题**，也是本篇正文仅有的五个出口里的三个。
- `TestConditionAttrType`（**未建、不在 allowlist**）— **本页语法节那张表的结构名**，
  来自子主题 `.06.05.54`，**这一篇**没有链到它（见 `## 是什么` 里「编号里藏着的一层结构」）。
- `DCL library`（**未建、不在 allowlist**）— **第 4 条子主题名里点名的库**
  （逐字 `the DCL library`）。**本篇没有解释 DCL 是什么，也没有链它。**
  **本页只知道「造自定义事件要用它」这个从名字里读出的方向——这是从名字读的，不是原文说的。**
- `EDF data organization` / `EDF data types`（**两个名字本身不在 allowlist**）—
  **对应 wiki 页 [[edf-data-organization]] / [[edf-data-types]]，见上。**

## 版本

**本文档没有 `## Functional changes` 段。**
**本篇也没有任何别处提到版本**——正文 0 句，只有标题与五条子主题链接。

**所以 EDF 是哪个版本引入的、7.x 之间改过什么，本篇未写**——
**本页不做推断，因为本篇连一个可以推的锚点都没有**
（没有版本号、没有 `Introduced before…`、没有新旧命令对照）。

**这与本 wiki 面向的真机版本（SmarTest 7.10.3）是什么关系，本篇一个字都没有。**

## 出处

`sources:` 一篇：
`02_System_reference/02.10_Data_Logging/02.10.01.06_Event_Data_Logging_Format__EDF.md`

**本页没做的：**

- **五个子主题一篇都没读。** **这是本页最大的空缺**：本篇正文的**全部内容**就是指向它们
  的五条链接，**而它们各自讲什么，本页一页都没有**——
  **所以「EDF 是什么」本页只能写「语料未写」，不能靠这五个标题去填空。**
- **语法节的来源子主题 `.06.05.54_TestConditionAttrType.md` 没读。**
  语法节里那张 `TestConditionAttrType` 表、以及那几个字段的语义，
  **本页只按语法节里逐字摆出来的内容转述，没有回那一篇核过**。
- **语法节里引的那张图 `../../../../raw/127716.png` 没打开。**
  §11.4 说 raw 里的图可读且该读；**这张图挂在语法节里、出自子主题，本页没有看它**，
  所以图上画的结构关系**本页一个字都没有**。
- **没有去别处找 EDF 的定义**（§11：本页只写 `sources:` 那几篇里有的）。
  **所以本页说的「语料未写」，准确范围是「本页 `sources:` 这一篇未写」**——
  **本页没有扫过全语料去确认别处有没有定义句，本页也没有那个依据。**
- **本篇正文一张图都没有**（唯一的图引用在语法节里、来自子主题，见上）。
- **没有交叉验证任何别处的文档**（§11）。尤其：**[[edf-data-organization]] /
  [[edf-data-types]] 两页虽然已存在，本页没有读它们**——
  **本页与它们的关系只有本篇正文那一行链接，没有内容上的互校。**
- **frontmatter 的 `layer: file` / `stage: results` 不是本篇写的**——
  **本篇原文一个字的自我定位都没有**（`## Application` 这类段不存在），
  **这个归属是本 wiki 的既有划分，不是文档事实。**

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> **① 正文 0 句：全篇的信息量只有「标题 + 五条链接」。** 逐字（正文全部非空行）：
> `# Event Data Logging Format (EDF)` / `#### Subtopics` /
> `- [EDF data organization](<02.10.01.06.01_EDF_data_organization.md>)` ×5 条。
> ——**一篇占着 `02.10.01.06` 这个「EDF 总入口」编号的文档，
> 自己一句话都没有。** 本页照实说，**不替它写一句定义**。
>
> **② 五条子主题名的构词不一致。** 前两条带 `EDF` 前缀（`EDF data organization` /
> `EDF data types`），后三条不带（`Event types` / `Attribute types`，
> 以及动词短语式的 `Creating your own custom events with the DCL library`）。
> **同一张清单里两种构词法，原文没有解释。**
>
> **③ `#### Subtopics` 是 H4，直接挂在 H1 下面。** 本篇的非 H1 标题只有这一个，
> 层级是 H4——**H2 与 H3 在本篇里不存在**。
> （**这是本篇自身的结构事实；别的文档怎么写，本页没读，不做比较。**）
>
> **④ 文件名把标题里的括号吃掉了。** frontmatter 与 H1 都写
> `Event Data Logging Format (EDF)`，**而语料文件名是
> `02.10.01.06_Event_Data_Logging_Format__EDF.md`**——
> **`(` 与 `)` 各变成了一个 `_`，括号中间那个空格也并了进去（`Format__EDF`）。**
> **这是语料的命名约定（括号进不了文件名），不是错字，
> 但会让按标题里的 `(EDF)` 去找文件的人搜不到。**
>
> **⑤ 五条链接一律写成 `[文本](<文件名.md>)` 的形式。** 逐字：
> `[EDF data organization](<02.10.01.06.01_EDF_data_organization.md>)`
> ——**文件名外面套了尖括号，且不带任何目录前缀**（只靠同级目录相对定位）。
> **本篇五条链接全是这一个写法，无一例外。**
>
> **⑥ frontmatter 用两种命名指向同一篇上游。**
> `source_topic: "34647.htm"`（**纯编号式**）与
> `source_html: "02_System_reference/02.10_Data_Logging/02.10.01.06_Event_Data_Logging_Format__EDF.htm"`
> （**目录路径式**），**同一个上游文件的两套写法**。
> **本页只核到 `tdc-html/raw/34647.htm` 这一个文件存在；另一种写法的文件本页没有去找。**
>
> **⑦ 本篇没有 §11.2 ① 那种编码损坏**（本页查过：`鈥` 0 处、汉字 0 个）。
> **本篇只有 588 个字符，是语料里最短的那一档。**
>
> **⑧ 语法节那张表被压平成「一格一行」，而且行间空 ` | ` 的条数不固定。**
> **这一条不在本篇正文里，在语法节所引的子主题里**（来源见节首 ⚠️），
> **本页照实记，因为它是本页实际承载的内容**：
> 表头四格之间各夹**一条** ` |`；而数据行之间夹的条数**依次是 2 / 2 / 3 / 3 / 2**
> （`These fields form the attribute header.` 之后 2 条、`Attribute type` 之后 2 条、
> `Number of conditions …` 之后 **3** 条、`Name of the condition` 之后 **3** 条、
> `Value of the condition` 之后 2 条）。**同一张表，同一个分隔符，条数不一致。**
> **本页不替它统一，也不据此推断原表有几行合并单元格。**

`verified: doc-only`
