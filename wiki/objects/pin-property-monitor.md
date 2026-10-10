---
type: object
title: PinPropertyMonitor
layer: L2
stage: pin
tags: [testmethod, api, pin, tester-status, instrument-status, print, debug, pin-list, smartest-7.5.2, smartest-7.6.0]
related: [pin, testmethod, test-method-class, pin-utility, smartest-7.5.2, smartest-7.6.0]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.148_PinPropertyMonitor.md
created: 2026-09-24
updated: 2026-09-28
verified: doc-only
---

# PinPropertyMonitor

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **628 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.148_PinPropertyMonitor.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Parameters

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/346544.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
> 首行（上游原文）：Parameter | Description

### Example

```
ARRAY_I sites;
GET_ACTIVE_SITES(sites);
//string pinList = "SWITCH_R/4,SWITCH_R/2,SWITCH_R,SWITCH_2R";
pinList = "@";
PinPropertyMonitor ppm1(); //get tester status for all sites and pins
PinPropertyMonitor ppm1(sites, pinList); //get tester status for given sites and pins
PinPropertyMonitor ppm1(sites, pinList, "PPMU"); //filter by instrument "PPMU"
PinPropertyMonitor ppm1(sites, pinList, "PPMU", "slewI"); //filter by instrument "PPMU" and property "slewI"
```

<!-- 语法节 end -->

## 是什么

**PinPropertyMonitor 是「把 tester 当前的仪器设置读出来、打出来」的类。** 原文的定义句就是全部机制：

> 「The pin property monitor is a class which provides functions to read and print tester status
> (the current settings of all instruments) to system console or to text files.」

**两个动词、两个去处**：`read` + `print`；出到 **system console** 或 **text files**。
**它是只读的**——原文没有给任何 setter，**它不改任何设置**。

**头文件与包含方式**（原文紧接着的一段）：

> 「This API is defined in the header file `/opt/hp93000/soc/prod_com/include/MAPI/PinPropertyMonitor.h`.
> You do not need to manually include it in your test method because it is included in MAPI.」

两个要点：① 它在 **`soc/prod_com`** 那一支下——**MAPI 族**，不是 MTP 的 `solution_tools`；
② **不用手工 include**，MAPI 已经带了。

### 四个构造函数 = 四档过滤

原文 `### Constructor` 给了四个重载（上面「语法 / 参数」节逐字收了）。**参数越多，筛得越窄**：

| 构造 | 范围 |
|---|---|
| **`PinPropertyMonitor()`** | **全部 sites + 全部 pins** |
| **`(sites, pins)`** | 指定 sites + 指定 pins |
| **`(sites, pins, instruments)`** | 再按仪器过滤 |
| **`(sites, pins, instruments, property)`** | 再按属性过滤 |

**`instruments` 与 `property` 都是字符串，不是枚举。** `instruments` 的合法取值原文列了 **10 个**：

`RELAY` / `PE_Driver` / `PE_Receiver` / `PE_Termination` / `PPMU` / `DPS` / `RELS` /
`DPS128HC` / `CSAS` / `PSAS`

> **这 10 个名字原文只给了名字**（`Possible options are:`），**一个字的解释都没有**。
> 所以「`RELS` / `CSAS` / `PSAS` / `DPS128HC` 分别是什么」**语料未写**，
> **本页也没有读任何一张卡的页**——**别照名字猜**。

### `property` 这一档：文档里只出现过一个值

**本篇 `### Parameters` 表里只有 `Instruments` 一行**（见上面语法节）——
**第四个参数 `property` 根本没进那张表**，两个子主题里也没有它的参数说明。
唯一出现过的值是 Example 里的 **`"slewI"`**（配 `"PPMU"` 用）。

**所以「`property` 能填什么」本页答不了。** 能确定的只有一件事：
它是**一个字符串过滤条件**，和 `instruments` 一起把输出收窄到「某个仪器的某个属性」。

### 两个成员函数：一个进内存，一个进文件

本篇 `### Member functions` **只列了两个名字、没有一句说明**。说明在它们的子主题里：

| 成员函数 | 干什么 | 出到哪 |
|---|---|---|
| **`printStatus()`** | 把 tester 状态存进一个 string stream | **内存**（或直接到 console） |
| **`printStatus2File()`** | 把 tester 状态写进文本文件 | **磁盘**（`waste` 目录） |

**`printStatus()` 有两个重载**：

- `PinPropertyMonitor & printStatus();`
- `PinPropertyMonitor & printStatus(std::ostream& ss);` —— 存进你给的流，
  之后自己用 `ss.str()` 把文本取出来。

**`printStatus2File()` 一个签名、两个参数**：

- `PinPropertyMonitor & printStatus2File(const string& targetName, openmode openMode=NEW);`
- **`targetName`**：`A string given by user based on which the output files are named.`
- **文件落在哪**：`Printed files are saved in the waste folder under your project root.`
  —— **是项目根底下的 `waste` 目录，不是项目根**。清目录时别把它当用户文件。
- **`openMode` 三个取值**，差别全在「同名文件已经存在时怎么办」：

| `openMode` | 行为 |
|---|---|
| **`NEW`**（默认） | **保留**已有文件，更新后的状态存成**新文件**（例如 `a` → `a_1`） |
| **`OUT`** | **覆盖**已有文件 |
| **`APP`** | 保留已有内容，把更新后的状态**追加**到文件末尾 |

**调用时带类名限定**：子主题的 Example 写的是 `PinPropertyMonitor::NEW` / `::OUT` / `::APP`。

## 典型用法

**用法只有两步：构造（选过滤档）→ 调一个成员函数。**

**1. 原文 Example 的四行**（上面语法节逐字收了）**就是四档过滤的演示**——
四行只差参数个数，每行末尾的注释自己写着那一档筛什么：

| 行 | 注释（原文） |
|---|---|
| `PinPropertyMonitor ppm1();` | `get tester status for all sites and pins` |
| `PinPropertyMonitor ppm1(sites, pinList);` | `get tester status for given sites and pins` |
| `PinPropertyMonitor ppm1(sites, pinList, "PPMU");` | `filter by instrument "PPMU"` |
| `PinPropertyMonitor ppm1(sites, pinList, "PPMU", "slewI");` | `filter by instrument "PPMU" and property "slewI"` |

> ⚠️ **这四行照抄会编不过**（两处，都是上游的错，见 `## 出处`）：
> ① **`ppm1` 被声明了四次**——同一个作用域里不能重名；
> ② **`pinList = "@";` 之前没有声明 `pinList`**（上一行那个 `pinList` 声明整行是注释）。
> **要照着写，请按上面四个构造函数签名写，不要照这四行抄。**

**2. `"@"` 是什么**：原文在那四行之前，先给了一行**被注释掉的真 pin list**
（`//string pinList = "SWITCH_R/4,SWITCH_R/2,SWITCH_R,SWITCH_2R";`），
紧接着才是 `pinList = "@";`，而第一档的注释说它是 `for all sites and pins`。
**（推断）**：`"@"` 是「全部 pin」的通配写法——**依据只是这两行的并置，原文没有明说。**

**3. 落盘的最小用法**（来自 `printStatus2File()` 子主题的 Example，本页改写成一句）：
先 `GET_ACTIVE_SITES(sites)` 拿 sites，再 `PinPropertyMonitor ppm1(sites, "@")`，
然后对同一个对象连调三次 `printStatus2File`，`openMode` 分别传
`PinPropertyMonitor::NEW` / `::OUT` / `::APP`——**一次看全三种落盘行为**。

**4. 什么时候用它**：**它是调试/诊断用的**——读的是 `the current settings of all instruments`，
也就是**当前态的快照**，不是测量结果。
`stages/pin.md` 把它记成「**打印 pin 属性状态，偏调试**」，是同一件事。

**5. 怎么接进一个完整的自定义 test method**：原文 `## Related information` **只指了一篇**
（`Printing tester status from test method`），**那篇本页没读**，所以**这一问本页没有答案**。

## 和谁有关

- [[pin]] — **本页 `stage: pin` 的依据**。`stages/pin.md` 已把本页收在 L2 的 pin 侧 API 表里，
  原话是「**打印 pin 属性状态，偏调试**」。
- [[testmethod]] — **宿主**：本页是 **Test Method API**（`layer: L2`），只能在 test method 里用。
- [[test-method-class]] — 宿主的具体形态。**（推断）**：本篇连一个完整的类外壳都没给
  （Example 是四行裸语句），说「它得放在 test method class 里」是按 [[testmethod]] 这一层说的。
- [[pin-utility]] — **（推断）同族邻居，但本页没有依据说它们互相调用**。
  依据只有两条：**同一支**（都在 `02.07.04.01`，本页 `.148`、它 `.147`）；
  上游 `.htm` 的 `<meta name="keywords" content="PIN_UTILITY">` 里写着 **`PIN_UTILITY`**。
  **本篇 raw 里 `PinUtility` 出现 0 次**——**这是位置证据，不是文档事实。**
- [[smartest-7.5.2]] / [[smartest-7.6.0]] — **版本页**：本页 `## 版本` 的两条就落在这两页上。
- `Printing tester status from test method`（**未建**）— 原文 `## Related information` **只列了它**；
  **本页没读**，所以「怎么接进完整的 test method」本页没有。
- `PinPropertyMonitor.printStatus()` / `PinPropertyMonitor.printStatus2File()`（**均未建**）—
  两个成员函数的专页；**本页读了这两篇**（理由、字节与行数见 `## 出处`）。
- `MAPI`（**未建**）— 头文件由它带入；**它里面还有什么，本页不知道**。

## 版本

原文 `## Functional changes` 两条：

- **`Introduced in SmarTest 7.5.2`**
- **`SmarTest 7.6.0: PMUX status and utility line are supported.`**

**两条都是 SmarTest 版本号**（不是 MTP），所以这里没有
[[mtp-shared-test-commands]] 那种「两套版本号不可比」的坑。

> 第二条要读准主语：**新增的不是 `PMUX` / `utility line` 这两个东西本身，
> 而是「它们的 status 能被读到了」**（`are supported` 说的是这两种 status 进了 monitor 的视野）。
> **「utility line 是什么」本页一个字都没有。**（这一句是本页的读法，**推断**）

**两个子主题各自也写着 `Introduced in SmarTest 7.5.2`**，与本篇一致——
**三个版本号对得上，没有冲突。**

## 出处

`sources:` 一篇：
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.148_PinPropertyMonitor.md`
（`346544.htm`，**2,645 字节，61 行**）——**整篇读完**。

**⚠️ 例外声明：本页另外读了两篇子主题。** 清单如下（读它们是为了补本篇完全没写的机制）：

| 读了哪篇 | 字节 / 行数 | 为什么读 |
|---|---|---|
| `02.07.04.01.148.01_PinPropertyMonitor.printStatus.md` | **1,245 字节 / 55 行** | 本篇 `### Member functions` **只有名字、没有说明**；`printStatus()` 的两个重载与去处只在这篇 |
| `02.07.04.01.148.02_PinPropertyMonitor.printStatus2File.md` | **1,497 字节 / 50 行** | 同上；`openMode` 三值的语义与 `waste` 目录只在这篇 |

**用例外条款的判据**：`sources:` 那篇是 **61 行的壳**（构造函数 + 一张单行参数表 +
两个成员函数名 + 一段 Example），**机制全推给这两篇子主题**；
骨架的语法节只收了本篇的 `Parameters` 表与 `Example`——节首写的是
「625 字符逐字取自 `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.148_PinPropertyMonitor.md>`」，
**没有「及其子主题」后缀**。
**本页「是什么」里凡涉及两个成员函数签名、`openMode`、`waste` 目录的内容，依据是这两篇子主题，不是 `sources:` 那篇。**

**本页没做的**：

- **`## Related information` 只列的那一篇 `Printing tester status from test method` 没读。**
- **`MAPI` 没读**（它是个头文件路径，不在语料里）。
- **`Instruments` 那 10 个取值分别是什么，本页一个字都没有**——
  原文只说 `Possible options are:`，**没给一个字的解释**；本页也没读任何一张卡的页。
- **`property` 的合法取值没找到**：本篇 `## Parameters` 表里没有它，两篇子主题里也没有，
  **全文只出现过 Example 里的 `"slewI"` 一个值**。
- **`"@"` = 全部 pin 是本页的推断**，原文没写。

**图**：**本篇与两篇子主题都没有图**——`raw/346544.htm` 里 `src=` 只有 `tdc.js`，
三篇 md 里 `.png` / `.jpg` 引用数为 0。**所以本页没有图证，也没有「图够不着」这类话。**

**核了上游 `.htm`：`raw/346544.htm`（5,256 字节）。两条结论：**

- ✅ **Example 里 `ppm1` 声明四次、`pinList` 未声明——上游就是这样**。
  上面那段四行在上游 `.htm` 里逐字相同，**不是转换坏的，也救不回来**（§11.2 ⑥ 那一族）。
- ⚠️ **转换确实丢了东西**：上游两个成员函数链接**各自带一个 `title` 属性**——
  `<a href="346545.htm" title="Saves tester status to a string stream for later output.">` 与
  `<a href="346546.htm" title="Prints tester status to text files that are named as user specified.">`。
  **这两个 `title` 就是两个成员函数的说明**，而 md 里只剩两个空链接项，
  **`title` 全丢**，链接文字也从 `PinPropertyMonitor.printStatus()` 缩成了 `printStatus()`。
  **所以「md 里成员函数没有说明」不是原文没有，是转换丢的（可救）。**
  **本页正文里那两句说明，依据是两篇子主题各自的第一句**（与这两个 `title` 逐字相同），**不是这个 `title` 属性本身。**

`verified: doc-only`
