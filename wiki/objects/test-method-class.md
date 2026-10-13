---
type: object
title: 2. Create a Test Method Class
layer: gui
stage: testmethod
tags: [testmethod, gui, wizard, test-method-class, utm, getting-started, parameters]
related: [how-to-create-a-universal-test-method-class, testmethod, pin-string, spec-variable]
sources:
  - 01_Getting_started/01.06_Test_methods/01.06.02.02_2._Create_a_Test_Method_Class.md
created: 2026-09-21
updated: 2026-09-21
verified: doc-only
---

> ⚠️ **本页若干处记的是 2026-10-10【之前】的语料形态。**
> 那一轮把语料里的表格一律换成了**指向上游 HTML 的指针**
> （见 `extract/PLAN-表格指针化.md`）。所以下文凡是说「表格被压平 / 被摊平 /
> 一格一行」的地方，指的是**更换之前**的样子 —— 现在语料里那个位置是**一句指针**，
> 真表仍在 `tdc-html/raw/` 的上游 HTML 里。**页码/引文都不受影响。**

# 2. Create a Test Method Class

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

**没有加标记的语法段。** 定义文档里没有 `Syntax` / `Parameters` / `Example`
这类**段标记**，跟着 `Subtopics` 找一层也没有。
**所以本脚本一个字都不收录**——没有段标记时「哪一段是语法」是猜，而猜就是编（§4）。

<!-- 语法节 end -->

## 是什么

**「Test Method Class」是 SmarTest GUI 里由向导产出的那一个类。**
本页讲的不是「怎么写这个类」，而是**在 GUI 里怎么把它生成出来、向导让你填什么**。

**它出现的位置很具体：**

> 「To create a new Test Method Class, right-click the project `Utmmethod` and select
> `New > Test Method Class` from the shortcut menu.」

**三件事一次说清**：入口是**项目右键菜单的 `New > Test Method Class`**；
它作用在**某个项目上**（这里点的是 `Utmmethod`）；
产出物是一个**类**，不是文件、不是 test suite。

### 向导只有两个输入：类名 + 参数

原文的 `## Procedure` 只有三步，**向导要你填的就这两样**：

| 步 | 在向导的哪个区域 | 填什么 |
|---|---|---|
| 1 | 右键菜单 | 选 `New > Test Method Class` |
| 2 | **`Class Name` 区域** | 类的名字（示例填的是 **`PspecSearch`**） |
| 3 | **`Parameters` 区域**，点 **`Add` 按钮** | **逐个加参数** |

> 「In the `Create a new Test Method class wizard`, type in the class name `PspecSearch`
> in the `Class Name` area.」

> 「Add the parameters listed in the table below to the class by clicking the `Add` button
> in the `Parameters` area.」

**注意向导的名字**：原文写的是 `Create a new Test Method class wizard`
（**`class` 是小写**，`Create` 是大写）——菜单项却写作 `Test Method Class`。
**同一件事在原文里就有两种大小写，本页照实记下、不替它统一。**

### 示例里加进去的八个参数（**逐字照抄原文那张表**）

这是本页唯一有内容的语料，也是**最容易漏掉的地方**——
**它不在本页「语法 / 参数」节里**（那一节的理由见下）：

| Parameter Type | Parameter Name |
|---|---|
| `PinString` | `sPinList` |
| `string` | `sResultPins` |
| `SpecVariable` | `sSpecVariableName` |
| `string` | `sSearchType` |
| `double` | `dxStart` |
| `double` | `dxStop` |
| `double` | `dxRes` |
| `double` | `dxStep` |

**这张表能读出三件事：**

1. **参数类型是语料里的一等公民**，不是随手写的类型名。
   `PinString` 和 `SpecVariable` **都是 SmarTest 自己的参数类型**——
   它们各有专页，**本页不解释它们是什么**（见「和谁有关」）。
2. **命名前缀编码了类型**：`s` 打头的是 `string`（`sResultPins`、`sSearchType`），
   `dx` 打头的是 `double`（`dxStart` / `dxStop` / `dxRes` / `dxStep`）。
   —— **这是我从这 8 行里归纳的规律，不是原文写的规矩**（**推断**；
   依据是这 8 行里前缀与类型一一对应、没有反例，且原文没有任何一句提到命名约定）。
3. **这 8 个参数合起来是在描述一次「按变量搜索」**：一个 pin 列表、一组结果 pin、
   一个 spec 变量名、一个搜索类型，加一个四点的区间（起 / 止 / 分辨率 / 步长）。
   类的名字 `PspecSearch` 也指向这件事。

### 为什么本页「语法 / 参数」节是空的（**这不是缺陷，是脚本的规矩**）

本页上面那一节的开头是「没有加标记的语法段」。**但原文里确实有一张参数表**——
就是上面重现的那张。两件事不矛盾，脚本的理由写在骨架里：

**骨架那一节自己写着它的理由**：定义文档里没有 `Syntax` / `Parameters` / `Example`
这类「段标记」，**而没有段标记时「哪一段是语法」是猜，而猜就是编**（§4），
所以脚本**一个字都不收录**。

**代价要写明白：这张表的出处在本页正文（我转述的），不在那一节。**
读者若只想找参数表，**得看本页这一节，不能只看「语法 / 参数」那一节。**

### 向导之后：源码要自己加

原文 `## What to do next` 只有一句（原文里它是加粗的一句）：

> `Add the source code`

**即：向导产出的是「类 + 参数」这个壳，函数体不在向导里。**
至于源码怎么加、加进哪里，**本篇没写**（见「出处」）。

## 典型用法

**原文的 `## Procedure` 就是这三步**（**这是本篇唯一成步骤的内容**，照抄顺序）：

1. **右键项目 `Utmmethod` → `New > Test Method Class`。**
2. **在向导的 `Class Name` 区域填类名**（示例：`PspecSearch`）。
3. **在 `Parameters` 区域点 `Add`，把上表那 8 个参数逐个加进去。**

**然后照 `## What to do next` 去加源码**——**那一篇本篇没读，所以「加什么、加在哪」本页答不了**。

**从别的文档也推不出的两件事，先说在这里省得你找**：

- **向导里 `Add` 按钮点下去之后的对话框**长什么样、参数类型从哪个列表里选——
  **原文只写了「点 Add」，没写弹什么。本篇没有依据。**
- **`Utmmethod` 这个项目是教程自带的还是自己建的**——原文直接说「右键项目 Utmmethod」，
  **没交代它从哪来**。（**推断**：`Utmmethod` 是这篇 Getting started 教程用的示例工程名，
  依据是 `## Related information` 指向的那篇叫
  `How to create a universal test method class`，且本篇标题带序号 `2.`——
  它是教程里的一步，前面还有第 1 步。**但本篇没写第 1 步是什么。**）

## 和谁有关

- [[how-to-create-a-universal-test-method-class]] — **原文 `## Related information` 唯一列的一篇**，
  也是**本篇的前置**。**分工**：本页是「GUI 里用向导产出这个类」，
  那一篇是「怎么建」（`02.07.02.02.02`）——**两篇都讲建类，区别在这里**。
- [[testmethod]] — **stage 归属**。frontmatter 的 `stage: testmethod` 是**「最近的一段」**，
  不是「归属」——这个类建出来就是给 test method 那一段用的。
- [[pin-string]] — **示例里第一个参数的类型**（`PinString` / `sPinList`）。
  **本页只说「向导里能选它」，它自己是什么、怎么用，看它那一页。**
- [[spec-variable]] — **示例里第三个参数的类型**（`SpecVariable` / `sSpecVariableName`）。
  同上：**本页不解释它。**
- [[universal-test-method-library]] — **同一条链上的下一站**：
  本页产出的类属于 universal test method 这一族（`## Related information` 那篇的标题就是
  `How to create a universal test method class`），而**整族最终怎么变成产物**是那一页的事。
  **本页与它没有直接的文档级链接——这条关系是从「UTM」这个共同前缀读出来的（推断）。**
- 另外三个参数类型 `string` / `double` —— **是 C++ 内建类型，不建页、也不链**。

> **本页的 `related` 都是从原文里读出来的**：`## Related information` 一条、
> 参数表的类型列四条（含两个内建类型）。
> **本页没有查 `edges.jsonl`** —— 这篇是 Getting started 教程的一步，
> **它的入边/出边本页一条都没核。**

## 版本

原文 `## Functional changes` 只有一条，而且**是哨兵值**：

- **`Introduced before SmarTest 6.3.2`**

⚠️ **这一条不许读成「6.3.2 新增了这个向导」。** 按 §11.2 ②：
**`Introduced before SmarTest 6.3.2` 是语料的一个哨兵写法**，
意思是「在本文档集覆盖范围开始之前就已经有了」——
它**不指任何一个具体版本**，只是「很早就有」。

**所以本页能说的只有一句：这个向导在 SmarTest 6.3.2 之前就已经存在。**
**它具体从哪一版起有，本篇答不了**（原文也没写）。

## 出处

`sources:` 一篇：
`01_Getting_started/01.06_Test_methods/01.06.02.02_2._Create_a_Test_Method_Class.md`

**本页没做的**：

- **`## What to do next` 指的 `Add the source code` 那一篇没读**——
  **所以「向导之后源码怎么写、加在哪」本页一个字都没有。**
  本页只写到这里为止：**向导产出的是壳，不是实现。**
- **`## Related information` 那一篇没读**——`How to create a universal test method class`
  （`02.07.02.02.02`）。**所以「建一个 universal test method class 的完整做法」本页没有**，
  本页只有「本篇这一篇教程里那三步」。
- **教程的第 1 步和第 3 步没读**：本篇标题带序号 `2.`，**说明它前面和后面还有步**，
  而**本篇没有说明那些步是什么**。
- **三个参数类型没有专页材料**：`PinString` 与 `SpecVariable` 的专页 **本页没读**
  （它们不在本篇 `sources:` 里），`string` / `double` 是 C++ 内建类型、**本篇也没有任何一句解释**。
  **所以本页只列了类型名，没有解释它们的取值与约束。**
- **一张图没看**——**本篇 raw 里本来就没有图**（整篇 107 行，无 `![` 引用）。
- **`## Syntax` / `## Parameters` / `## Example` 段本篇没有**——
  **这就是本页「语法 / 参数」节为空的原因**（上面「为什么本页「语法 / 参数」节是空的」已写）。

> ⚠️ **本篇的语料瑕疵，照实记录，一处都没替它改**：
> ① **那张参数表在 HTML 转 markdown 时被压平了**：raw 里**每一个单元格单独占一行、
>    行与行之间还夹着空行**，表头两格是**空的**。原文（raw 第 14–94 行）长这样：
>    ```
>     |
>
>     Parameter Type
>
>     |
>
>     Parameter Name
>
>     |
>    ```
>    然后才是 `PinString` / `sPinList` 这样一格一行地排下去。
>    **本页上表是按「两列一行」重排的**——**重排是为了能读，不是语料原样**；
>    **逐字的那份在 raw 第 14–94 行。**
> ② **大小写不统一**：向导名 `Create a new Test Method class wizard` 里是小写 `class`，
>    而菜单项与本节标题写的是 `Test Method Class`，大写 `Class`
>    （**同一件事两种写法，原文如此**）。
> ③ **标题里的序号是内容的一部分**：本篇标题是 `2. Create a Test Method Class`，
>    **那个 `2.` 是语料的原样**（它是教程的步号），本页 frontmatter 的 `title` 也照抄了它。
> ④ **`## What to do next` 那一节只有一句、没有链接**：
>    写的是一句加粗的 `Add the source code`，**没有指向任何文档**——
>    所以本页连「去哪篇读」都答不了（见上）。

`verified: doc-only`
