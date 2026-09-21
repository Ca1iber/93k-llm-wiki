---
type: object
title: EVENT_BASE
layer: L3
stage: testmethod
tags: [event, base-class, abstract, test-method-api, waveform-event, dc-event, xml, id]
related: [event-waveform-vfim, event-waveform-vfvm, event-formatter, dc-scale-xps256-card, dps128-dps64-cards, smartest-6.5.2]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.01_EVENT_BASE.md
created: 2026-09-18
updated: 2026-09-20
verified: doc-only
---

# EVENT_BASE

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

**没有加标记的语法段。** 定义文档里没有 `Syntax` / `Parameters` / `Example`
这类**段标记**，跟着 `Subtopics` 找一层也没有。
**所以本脚本一个字都不收录**——没有段标记时「哪一段是语法」是猜，而猜就是编（§4）。

<!-- 语法节 end -->

## 是什么

**`EVENT_BASE` 是所有具体 event 类型的**基类**。**

> 「The EVENT_BASE class is the base class for all other specific event types. It provides the
> interface for generic handling of all kinds of events, for example, downloading or binding to
> a test point in a pattern.」

**原文给了它两个用途**：

| 用途 | 原文 |
|---|---|
| **通用处理所有 event** | `provides the interface for generic handling of all kinds of events` |
| **两个例子** | **`downloading`**（下发）与 **`binding to a test point in a pattern`**（绑定到 pattern 里的一个 test point） |

> **「绑定到 pattern 里的一个 test point」是理解这个类族的钥匙**：
> **event 不是「一段代码」，是「pattern 上某个点的动作」**——
> **所以它需要一个标识（`id`）来指向那个点。**
> （这一句是本页依据原文两个例子作的**推断**，原文没有用「标识指向 pattern 上的点」这个说法。）

**定义在头文件** `/opt/hp93000/soc/prod_com/include/MAPI/Events.h`。

### 七种特化 event（原文列全了）

> 「The following event types are provided by specialized event classes：」

| # | 类型（原文） | 直译 |
|---|---|---|
| 1 | **Force Events** | 加电 / 强制类 |
| 2 | **Measurement Events** | 测量类 |
| 3 | **Combined Force & Measure Events** | 加电 + 测量合体类 |
| 4 | **Set Measurement Range Events** | 设测量量程类 |
| 5 | **Force Waveform Events** | 强制波形类 |
| 6 | **Measure Waveform Events** | 测波形类 |
| 7 | **Combined Force & Measure Waveform Events** | 强制 + 测波形合体类 |

**七种其实是「三组 × 两个维度」**（**推断**：把上面七条按前缀拆开看——
`Force` / `Measurement` / `Combined` 是一维，`（无波形）` / `Waveform` 是另一维，
`Set Measurement Range` 单独占一格；**原文没有这样归过类，这是本页的整理**）：

| | **不带波形** | **带波形** |
|---|---|---|
| **Force** | Force Events | Force Waveform Events |
| **Measure** | Measurement Events | Measure Waveform Events |
| **Force + Measure** | Combined Force & Measure Events | Combined Force & Measure Waveform Events |
| **（单列）** | **Set Measurement Range Events** | — |

**另有两条原文事实**：

> 「Specialized event classes are similarly displayed in the graphical user interface.」

**即：这七种特化类在 GUI 里也有对应的显示**——**GUI 侧的样子本文档没有展开**。

### 类的形状：一个**抽象**基类（**推断**）

原文 `## Class definition` 给的构造函数与成员函数（**逐字**）：

```
EVENT_BASE(const STRING & id);
EVENT_BASE(      INT      id);
```

```
void id(const STRING & id);
void id(      INT      id);
const STRING & getId() const;

bool operator == (const EVENT_BASE &) const;
bool operator != (const EVENT_BASE &) const;

virtual const STRING & getEventType() const = 0;
virtual bool hasXml() const = 0;
virtual void toXml(std::ostream& os) const = 0;
```

**三条纯虚函数（`= 0`）说明它是抽象基类**——**推断**：
原文没有用 `abstract` 这个词，**推断依据是那三个 `= 0` 与 `virtual`**——
**按 C++ 语义，带纯虚函数的类不能直接实例化**。
**但原文同时又给了一个带说明的构造函数**（见下），
**两件事并列摆着，原文没有解释怎么调和。本页照实并列，不替它调和。**

**成员函数按用途分四组**：

| 组 | 函数 | 说明 |
|---|---|---|
| **标识** | `id(...)` ×2（string / int）、`getId()` | **`id` 有 setter 与 getter 两个方向**；getter 返回 `const STRING &` |
| **比较** | `operator ==`、`operator !=` | 两个都接 `const EVENT_BASE &` |
| **类型名** | `virtual const STRING & getEventType() const = 0` | **纯虚——基类不给实现** |
| **XML** | `virtual bool hasXml() const = 0`、`virtual void toXml(std::ostream& os) const = 0` | **两个都纯虚**；`toXml` 往一个 `std::ostream` 里写 |

> **`id` 既能是 `STRING` 也能是 `INT`**——原文在构造函数的参数说明里写死了这句：
> 「`id` ｜ **Event identifier. It can be a string or an integer.**」
> **两套重载贯穿到底**：构造函数两个、`id()` 两个、而 `getId()` **只有一个**（返回 `const STRING &`）。
> **（即：`id` 可以用整数给，但读回来一定是字符串。这一步是原文的重载表能直接看出来的，不是推断。）**

### 构造函数在原文里**出现了两次**

原文有两个 `### Constructor` 标题、**代码块一字不差**，第一个后面直接是下一个标题，
第二个后面才有说明与参数表：

> 「This constructs an object of the EVENT_BASE class.」

| 参数 | 原文 |
|---|---|
| **`id`** | **`Event identifier. It can be a string or an integer.`** |

**这就是本页关于构造函数能拿到的全部信息**——**没有说 `id` 的取值范围、唯一性、冲突怎么办。**

### 这个类自己的 `Subtopics`（原文的导航，**四篇**）

原文开头用 `#### Subtopics` 列了四篇：

| 子话题（原文） | 讲什么（从标题看） |
|---|---|
| `Timing of DC events` | DC event 的时序 |
| `Timing of DC events - XPS256` | **按卡分：XPS256** |
| `Timing of DC events - DPS128 / DPS64` | **按卡分：DPS128 / DPS64** |
| `MSET timing of digital pins` | digital pin 的 `MSET` 时序 |

> **这四篇的存在说明「event 的时序」是按**卡**分的**——
> **同一个概念在 XPS256 上和 DPS128/DPS64 上各有说法**（**推断**，依据是后两个标题的形状）。
> **这四篇本页一篇都没读**（见「出处」）。

## 典型用法

**⚠️ 本文档**没有**给任何一个用法示例、过程或 `Before you begin`。**
原文全文只有：一段定义、一份七类清单、一个头文件路径、一份类定义（构造函数 + 成员函数）、
一次重复的构造函数小节、一条版本记录。**所以本页写不出「几步走」的流程——
下面四条都是把原文已有的事实摆成可用形状，不是原文给的步骤。**

**1. 想知道「某个 event 是什么类型」**：**调 `getEventType()`**——
它是纯虚，**实现由特化类给**（按上面七类）。
**返回值是 `const STRING &`，即类型名字符串。**

**2. 想把 event 序列化出去**：**先问 `hasXml()`，再调 `toXml(os)`**——
**两个都是纯虚**，**所以「有没有 XML」是运行期问的，不是编译期知道的**（**推断**：
依据是 `hasXml()` 返回 `bool` 且为虚函数）。

**3. 想比较两个 event**：**`==` / `!=`**，接的是 `const EVENT_BASE &`——
**即一个 `EVENT_BASE` 引用可以接任何特化类对象**（**推断**：这是基类引用的常规语义；
**原文只说这两个运算符存在**）。

**4. 想给 event 一个标识**：**构造时传 `id`，或事后用 `id(...)` 改**——
**string 与 int 两种都给。**
**但原文没说「标识重复了会怎样」「标识和 pattern 里的 test point 怎么对应」——
语料未写。**

**5. 要查时序**：**照卡去查上面四篇 Subtopics 之一**（**本页没有时序内容**）。

## 和谁有关

**子类 / 特化（同一件事的具体形态）**：

- [[event-waveform-vfim]] / [[event-waveform-vfvm]] — **两者都在 allowlist 里、都已建页**，
  名字里的 `VFIM` / `VFVM` 与原文七类里的 **Force Waveform Events** / **Measure Waveform Events**
  对得上（**推断**：**本页没有读那两篇，所以「它们是本类的哪个子类」这句话是本页从名字形状推的**，
  **不是那两篇说的**）。
  **本页是基类，它们是把纯虚函数实现的那些类。**
- [[event-formatter]]（**在 allowlist 里**）— 本页的 `hasXml()` / `toXml(std::ostream&)` 说明
  **event 可以被序列化成 XML**；**而「格式化 / 输出成什么形状」属于另一侧。**
  **该页本页没读，本页只作指向，不断言它的内容。**（**推断链接**：
  本页连它的依据是「XML 输出」这件事，不是原文点了它的名。）

**按卡分的四篇子话题（本页一篇没读，只作指向）**：

- `Timing of DC events`（**未建**）— 通用那份时序
- `Timing of DC events - XPS256`（**未建**）— 与 [[xps256-status-flags]] / [[dc-scale-xps256-card]]
  同一张卡的那一条线；**本页只提供「该去那儿查时序」这一步**
- `Timing of DC events - DPS128 / DPS64`（**未建**）— 与 [[dps128-dps64-cards]] 同一条线
- `MSET timing of digital pins`（**未建**）— digital pin 那一侧；
  **与本页关系只有「MSET 也是一种 event 时序」这一层**（**推断**：原文把它列在 Subtopics 里，
  **没有说它是本类的一个子类**）

**同层 / 同阶段**：

- [[smartcalc-framework]] / [[tmlimits]] / [[dc-result-accessor]] 等
  **同为 `layer: L3` / `stage: testmethod` 的 test method API 页**——
  **本页与它们只在「同属这一层」上相关，本页没读它们中的任何一篇，不作内容上的断言。**

**被本页点名的（均未建，不链）**：

- **七种特化 event 类的**自己的页**——`Force Events` / `Measurement Events` /
  `Combined Force & Measure Events` / `Set Measurement Range Events` / `Force Waveform Events` /
  `Measure Waveform Events` / `Combined Force & Measure Waveform Events`：
  **这七个名字**一个都不在 allowlist 里**，所以本页只用反引号，没有链。**
  **它们是本页真正的「下游」——本类只给接口，实现全在它们身上。**

## 版本

本文档有 `## Functional changes` 段，**全部内容一条**：

- **`Introduced in SmarTest 6.5.2`**

> **这一条用的措辞是 `Introduced in`，不是 `Introduced before`**——
> 按 §11.2 ②，`Introduced before …` 是哨兵值（意思是「本文档集覆盖之前就有了」），
> **而 `in` 是**真版本记录**。**
> **所以 `EVENT_BASE` 是 SmarTest 6.5.2 引入的，这条可以当真。**
>
> **对照页**：[[smartest-6.5.2]]（**未建**）——该版覆盖范围本页没读。
> **本页不列出 6.5.2 还改了什么**（§3：不镜像目录树）。

## 出处

`sources:` 一篇：
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.01_EVENT_BASE.md`
（raw 的 `source_topic: "116893.htm"`）。

**本页没做的**：

- **四篇 Subtopics 一篇都没读**：`Timing of DC events`、
  `Timing of DC events - XPS256`、`Timing of DC events - DPS128 / DPS64`、
  `MSET timing of digital pins`。
  **所以：DC event 的时序是什么、三张卡上差在哪里、`MSET` 是什么——本页一个字都没有。
  本页只有它们四个的标题。**
- **七种特化 event 类一篇都没读**（原文只列了名字，**没给任何链接**）。
  **所以七种各自怎么用、`getEventType()` 各返回什么字符串、`toXml()` 写出什么，
  本页全都没有。** 本文档连它们的类名都没给。
- **`Subtopics` 那四篇之外，本文档没有 `Related information`、没有 `Before you begin`、
  没有 `What to do next`。** 本页没有漏读任何「原文指向的其它文档」——
  **本文档只有那四个外链。**
- **本文档没有任何示例、任何过程、任何参数表（`id` 那一行除外）。**
  所以「典型用法」一节里的五条**都是本页从类定义里读出来的形状，不是原文给的步骤**——
  本页在那一节开头已经写明这一点。
- **没有任何图。** 本篇没有图片引用。
  （原文提到 `Specialized event classes are similarly displayed in the graphical user interface`，
  **但没给图**，**所以 GUI 里长什么样本页不知道。**）
- **`Subtopics` 之外，`02.07.04.01.63.0x` 这一族还有没有别的页，本页不知道**——
  **本页只读了这一篇。**

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
>
> **① `### Constructor` 这一节在原文里出现了两次，代码块一字不差。**
> 第一次（`## Class definition` 下第一个小节）**代码块后面直接就是 `### Member functions`**，
> 没有一行说明；第二次出现在成员函数之后，**才有
> `This constructs an object of the EVENT_BASE class.` 与 `id` 的参数表。**
> **同一件事两节，一节有正文一节没正文。** 本页把两处的内容合起来写了，
> **但在「是什么」里明说了它出现了两次。**
>
> **② `#### Subtopics` 的标题层级比它下面的正文还深，而且出现在**任何** `##` 之前。**
> 逐字：文件第一个标题行就是 `#### Subtopics`（**H4**），
> 而后的 `## Class definition` 是 **H2**、`### Constructor` 是 **H3**。
> **即：文档从一个 H4 开始，层级是倒的。**
>
> **③ 两处代码块的排版不齐**（不是本页改的）。逐字：
> `EVENT_BASE(      INT      id);`、`void id(      INT      id);`——
> **`INT` 两侧塞了大量空格**，显然是对齐 `const STRING &` 用的，但 `STRING` 那行本身是
> `EVENT_BASE(const STRING & id);`，**两行并没有真对齐**。
>
> **④ 一处 `operator` 写法带空格。** 逐字：
> `bool operator == (const EVENT_BASE &) const;`——**`operator ==` 与参数表之间各带空格**，
> `!=` 那条同样是 `bool operator != (const EVENT_BASE &) const;`。**本页照引。**
>
> **⑤ 构造函数参数表是被拆行的单行表。** 逐字：
> ` | id  | Event identifier. It can be a string or an integer. |`
> ——**一行两格，前后各一个前导空格**；这是这份语料里「单行表」的正常形态
> （和 [[xps256-status-flags]] 那种被拆成 18 段的多行表不同）。
>
> **⑥ 语法节那句「跟着 `Subtopics` 找一层也没有」在本篇是**事实**，不是通用措辞。**
> 本篇 raw 里**确实有**一个 `#### Subtopics` 段（四篇外链），
> **脚本跟进去找过，那四篇的段标记不在本节收录范围，所以本节为空。**
> **空的原因不是「没有段标记」，而是「有段标记但不在被抽的那几篇里」——
> 这一点脚本的说明文字没有区分，本页在此讲清。**
> **本页正文里关于「没有任何语法示例」的判断，依据是**本篇 raw 的正文**，
> 不是这个空节。**

`verified: doc-only`
