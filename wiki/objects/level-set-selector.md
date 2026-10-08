---
type: object
title: LevelSetSelector
layer: L2
stage: level
tags: [level, l2, test-method-api, offset-search, level-set, digital-offset-search, primary, equation-based-level]
related: [level, timing-set-selector, digital-offset-search-pins, level-spec, equation-based-level-setup, primary-status, mapping-level, smartest-7.2.1]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.123_LevelSetSelector.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# LevelSetSelector

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,703 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.123_LevelSetSelector.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

The available constructors are listed as follows:

- `LevelSetSelector()`;

This is the default constructor referring to the primary level set.

- `LevelSetSelector(const LevelSetSelector &`rhs`);`

Or,

`LevelSetSelector(const LevelSetSelector* `rhs`);`

These two constructors refer to an existing LevelSetSelector object.

- `LevelSetSelector(INT `levelSetId`);`

This constructor refers an existing level set, which can be a fixed level set or an equation based level set.

- LevelSetSelector(DIGITAL_OFFSET_SEARCH::PRM_ALL levelSet);

This constructor refers to either the primary level set or all fixed level sets.

Parameters
| Parameter | Description |
|---|---|
| rhs | An existing LevelSetSelector object |
| levelSetId | For a fixed level setup, it is the level set number.<br><br>For an equation based level setup, the level set ID is calculated as follows:<br><br>equset * 100000 + specset * 1000 + level_set_no |
| levelSet | DIGITAL_OFFSET_SEARCH::PRM or DIGITAL_OFFSET_SEARCH::ALL.<br><br>- DIGITAL_OFFSET_SEARCH::PRM: Refers to the primary level set, which is identical to the use of the default constructor.<br>- DIGITAL_OFFSET_SEARCH::ALL: Refer to all fixed level sets. |

Return value

There is no return value.

### Example

Upload the VIH offsets of all fixed level sets for the pin "pcie_rx1n".

```
STRING strpins("pcie_rx1n");
DIGITAL_OFFSET_SEARCH_TASK dos;
DIGITAL_OFFSET_SEARCH::LevelSetSelector dest(DIGITAL_OFFSET_SEARCH::ALL);

  dos.pin(strpins).resourceType(DIGITAL_OFFSET_SEARCH::VIH).searchType(DIGITAL_OFFSET_SEARCH::EYE)
     .start(15).numSteps(120).stepWidth(15).restoreFlag(DIGITAL_OFFSET_SEARCH::NO);
  dos.execute();

  dos.uploadResult(dest, DIGITAL_OFFSET_SEARCH::VIH);
```

<!-- 语法节 end -->

## 是什么

**`LevelSetSelector` 是一个「指哪儿」的对象——它指的是一个 level set，或者全部 fixed level set。**
本篇第一句就是它的全部定义：

> A class refers to a single level set or all fixed level sets, used by the DIGITAL_OFFSET_SEARCH_TASK and DIGITAL_OFFSET_SEARCH_PINS classes.

**它不是自己干活的类**：定义句的后半段说它是**被那两个名字的搜索类用的**，
而本篇**没有列任何成员函数**——整篇的语法面只有 **4 个构造函数**，
语法节末那一格写的是 `There is no return value.`。
所以它的身份是**一个「目的地」对象**：你把它造出来、交给搜索任务，
让搜索的结果落到它指的那些 level set 上（「典型用法」里例子的最后一行就是这个用法）。

头文件：`/opt/hp93000/soc/prod_com/include/MAPI/DigitalOffsetSearchTypes.h`。
（**本页读了 [[timing-set-selector]] 那一页**：它记的头文件是同一个
——`DigitalOffsetSearchTypes.h`。**它那一篇的 raw 本页没读**，
所以「两个类为什么共用一个头文件」本页没有依据。）

### 四种构造：三种指「一个」，一种指「一批」

| 构造函数（语法节逐字） | 指的是什么 | 语法节原文 |
|---|---|---|
| `LevelSetSelector()` | **primary level set** | `This is the default constructor referring to the primary level set.` |
| `LevelSetSelector(const LevelSetSelector& rhs)`<br>`LevelSetSelector(const LevelSetSelector* rhs)` | **一个已存在的 `LevelSetSelector` 对象**（引用 / 指针两种写法） | `These two constructors refer to an existing LevelSetSelector object.` |
| `LevelSetSelector(INT levelSetId)` | **一个已存在的 level set**——fixed 或 equation based 都行 | `This constructor refers an existing level set, which can be a fixed level set or an equation based level set.` |
| `LevelSetSelector(DIGITAL_OFFSET_SEARCH::PRM_ALL levelSet)` | **primary level set，或者全部 fixed level set** | `This constructor refers to either the primary level set or all fixed level sets.` |

**参数表一共三行**（`rhs` / `levelSetId` / `levelSet`）：

| 参数 | 原文说明 | 本页要补一句的 |
|---|---|---|
| `rhs` | `An existing LevelSetSelector object` | **签名取的是引用或指针，参数表却说「一个已存在的对象」**——两者不是同一种说法。原文如此，见「出处」⚠️②。 |
| `levelSetId` | fixed 时是 level set 号；equation based 时按公式算（见下） | —— |
| `levelSet` | `DIGITAL_OFFSET_SEARCH::PRM or DIGITAL_OFFSET_SEARCH::ALL.` | 见下 |

### level set ID 是三个字段拼出来的

`INT levelSetId` 那一格对 equation based 那一侧给了公式（逐字）：

> equset * 100000 + specset * 1000 + level_set_no

**这是一个「按位拼号」的写法**：三个字段各占一段十进制位——
`equset` 落在十万位以上、`specset` 乘 1000 落在千位、`level_set_no` 在末三位。
（**这一步是本页的（推断）**，依据只是 `100000` / `1000` 这两个系数；
**原文没有写任何一个字段的取值范围**。）

**本 wiki 的 [[level]] 页把同一公式记成 `100000 * equation_set_no + 1000 * specset_no + level_set_no`**
（**本页读了那一页**）——**两处数值相同、乘数顺序与变量名不同**
（`equset` / `specset` 对上 `equation_set_no` / `specset_no`）。
**本页只并列，不判哪一种是规范写法**（§10）。

### `levelSet` 那格：`PRM` 与 `ALL` 各指什么

两个取值，原文逐字：

> - DIGITAL_OFFSET_SEARCH::PRM: Refers to the primary level set, which is identical to the use of the default constructor.

> - DIGITAL_OFFSET_SEARCH::ALL: Refer to all fixed level sets.

**注意第二条的谓语是 `Refer` 而不是 `Refers`**——原文如此，见「出处」⚠️③。

**本篇只有这一处 `PRM` / `ALL`**：`PRM` 指 primary level set、`ALL` 指全部 fixed level set，
**没有第二个参数位、没有第二套意思**。
（对照 [[timing-set-selector]] 那一页：它记着 timing 侧同一个 `PRM` / `ALL`
**在两个参数位上意思不同**——**本页读了那一页，没读它那一篇的 raw**。）

### 类型名 `PRM_ALL` 与取值名 `PRM` / `ALL` 不是一回事

第 4 个构造函数的参数类型写的是 **`DIGITAL_OFFSET_SEARCH::PRM_ALL`**，
而参数表里它的说明写的是 **`DIGITAL_OFFSET_SEARCH::PRM or DIGITAL_OFFSET_SEARCH::ALL`**。
**即：`PRM_ALL` 是那个枚举类型的名字，`PRM` / `ALL` 是它的两个取值。**
**同族还有哪些取值、定义在哪，本篇一个字都没写——语料未写。**

## 典型用法

**本文档没有 `## Procedure` 段，也没有 `## Before you begin` 段。**
能当用法读的只有 `## Example` 段那一块代码（逐字见「语法 / 参数」节），
它的题目已经把用途说完了：

> Upload the VIH offsets of all fixed level sets for the pin "pcie_rx1n".

把那段代码排成步骤：

| # | 做什么 | 代码（`## Example` 逐字） |
|---|---|---|
| 1 | 指定要搜的那个 pin | `STRING strpins("pcie_rx1n");` |
| 2 | 造一个搜索任务 | `DIGITAL_OFFSET_SEARCH_TASK dos;` |
| 3 | **造 selector，指明目的地** | `DIGITAL_OFFSET_SEARCH::LevelSetSelector dest(DIGITAL_OFFSET_SEARCH::ALL);` |
| 4 | 配搜索条件 | `dos.pin(strpins).resourceType(DIGITAL_OFFSET_SEARCH::VIH).searchType(DIGITAL_OFFSET_SEARCH::EYE).start(15).numSteps(120).stepWidth(15).restoreFlag(DIGITAL_OFFSET_SEARCH::NO);` |
| 5 | 执行搜索 | `dos.execute();` |
| 6 | **把结果上传到 selector 指的地方** | `dos.uploadResult(dest, DIGITAL_OFFSET_SEARCH::VIH);` |

**第 6 步是本类在例子里的落点，也是本页唯一能确证的用法**：
**selector 是 `uploadResult()` 的第一个实参，也就是「结果往哪儿放」。**

**几点照实说明：**

- **第 4、5、6 步里每一个方法都属于 `DIGITAL_OFFSET_SEARCH_TASK`**
  （`pin()` / `resourceType()` / `searchType()` / `start()` / `numSteps()` / `stepWidth()` /
  `restoreFlag()` / `execute()` / `uploadResult()`），**本篇没有它们的定义**；
  那一篇 raw 本页没读（raw 路径见「和谁有关」）。
- **`start(15)` / `numSteps(120)` / `stepWidth(15)` 三个数是什么单位、什么含义**——**语料未写**。
- **第二个实参 `DIGITAL_OFFSET_SEARCH::VIH` 与 `resourceType()` 那个同名**，
  **说明「搜什么资源」与「上传什么资源」在这个例子里是同一个值**；
  **还能取哪些值、要不相同时怎么写——本篇未写。**
  （对照：[[timing-set-selector]] 那一页的例子里 `uploadResult()` 的第二个实参写的是
  `ALL_EDGES`——**本页读了那一页，没读它那一篇的 raw**。）
- **例子把本类写成带命名空间的 `DIGITAL_OFFSET_SEARCH::LevelSetSelector`**，
  而「语法 / 参数」节的构造函数清单写的是不带命名空间的 `LevelSetSelector`。
  **两处写法不同，原文如此。**
- **`restoreFlag(DIGITAL_OFFSET_SEARCH::NO)` 的语义**——**本篇一个字都没写**。

## 和谁有关

- [[level]] — **stage 页，也是本页 `stage: level` 的理由**。本类选的是 level set；
  **「Level 这一段整体怎么走」在那一页，本页不写流程**（§2.2）。
- [[timing-set-selector]] — **本篇 `## Related information` 一节唯一的一条**
  （逐字：`TimingSetSelector`，raw：`02.07.04.02.17_TimingSetSelector.md`）。
  **两个类是「同一个形状的另一半」**：它指的是 timing set，本类指的是 level set
  （**这一步是（推断）**，依据两条：① 两个类名同形，都以 `SetSelector` 结尾；
  ② 本页语法节里第 4 个构造函数的参数类型与参数表里都是
  `DIGITAL_OFFSET_SEARCH::PRM_ALL`——**同一个命名空间**）。
  **本页读了 [[timing-set-selector]] 那一页，没读它那一篇的 raw**——
  所以它有哪些构造函数、timing spec ID 怎么算，**本页一个字都没有**。
- [[digital-offset-search-pins]] — **文档点名的使用者之一**
  （`used by the DIGITAL_OFFSET_SEARCH_TASK and DIGITAL_OFFSET_SEARCH_PINS classes.`）。
  那一页讲的是**一批 pin 上的偏移搜索条件容器**，**本页讲的是结果落到哪**。
  **两页的 raw 互不相同，本页没读它**——所以那条「被它用」的话本页只能照抄。
- `DIGITAL_OFFSET_SEARCH_TASK`（**不在 allowlist，故不链**）— **本类的宿主，也是唯一入口**。
  例子里每一个动作都是它的方法。raw：`02.07.04.01.36_DIGITAL_OFFSET_SEARCH_TASK.md`。
  **本页没读**——所以 `uploadResult()` 的完整签名、`pin()` 怎么给、
  搜索步长 / 步数的单位，本页都没有。
- [[level-spec]] / [[equation-based-level-setup]] — **「equation based level set」那一侧的落点**：
  本页构造函数的说明里出现了这个词组
  （`which can be a fixed level set or an equation based level set`），
  而**「equation based level set 是什么、怎么建、ID 怎么编」不在本篇**。
  **两页本页都没读**；这里只按词组与页名指路。
- [[primary-status]] — **`PRM` 那三个字母的语义落点**。本类的默认构造与
  `DIGITAL_OFFSET_SEARCH::PRM` 读的都是「primary level set」，
  而**「当前 primary 是哪个」这件事不在本篇**。
  **本篇没点名那一页**（**本条是（推断）**，依据只是 `primary` 这个词）；**那一页本页没读**。
- [[mapping-level]] — **跨层对照表**。另：**本页在 [[level]] 那一页的 L2 表里占一格**
  （那张表把它记成「`DIGITAL_OFFSET_SEARCH_TASK` / `DIGITAL_OFFSET_SEARCH_PINS` 里选 level set
  （7.2.1 引入）」，**本页读了 [[level]] 那一页**）。
  **[[mapping-level]] 那页本身本页没读。**
- [[smartest-7.2.1]] — **版本页**：本篇 `## Functional changes` 唯一的落点。
- **本篇没有点名任何 GUI 工具、也没有点名任何固件命令**（全文没有出现工具名或命令名）——
  **所以本类与 GUI 侧、与 L1 命令的关系，本篇没有依据。**

## 版本

本文档有 `## Functional changes` 段，**只有一条**：

- **Introduced in SmarTest 7.2.1**

**这是一条正常的 `Introduced in`，不是 §11.2 ② 那个 `Introduced before` 哨兵**——
所以它**可以照字面读**：**7.2.1 之前没有这个类**。

**两条边界：**

- **它之后有没有被改过、有没有被废弃——本篇一个字都没有。**
  **「没记录」不等于「没改过」**（§13.1 第 ⑥′）。
- **与它同批引入的是 [[digital-offset-search-pins]]**：那一页的 `## Functional changes`
  也只有 `Introduced in SmarTest 7.2.1` 一句（**本页读了那一页**；**它那一篇的 raw 本页没读**）。

## 出处

`sources:` 一篇：
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.123_LevelSetSelector.md`
（TDC `141182.htm`，69 行 / 2,505 字节）。**整篇读完。**

**本页没做的：**

- **`DIGITAL_OFFSET_SEARCH_TASK`（`02.07.04.01.36`）没读**——**这是本页最大的缺口**。
  本类是**被它用的**：例子里每一个动作都是它的方法。所以
  **`uploadResult()` 的签名、第二个实参除了例子里的 `VIH` 还能取什么、
  `pin()` 的 pin 列表怎么给、搜索步长 / 步数的单位**——**本页一个字都没有。**
- **`DIGITAL_OFFSET_SEARCH_PINS`（`02.07.04.01.36.01`）没读**
  （wiki 上的 [[digital-offset-search-pins]] 页**其 raw 本页也没读**）。
- **`TimingSetSelector`（`02.07.04.02.17`）那一篇 raw 没读**——
  它虽然是**本篇 `## Related information` 整节唯一的一条**，
  本页只读了它的 wiki 页，**它那一篇的 raw 一个字没有**。
- **一张图都没看——因为这一篇里没有图。** 实测全文 **0 处** `.png` / `.jpg` / `raw/`。
  **所以本页没有任何来自图的结论**（§11.4：没看图就写「本页没用图」，理由不编）。
- **没有实跑。** 没有在任何机台上做过一次 offset search，
  也没有验证过 `PRM` / `ALL` 两个取值的实际效果。`verified: doc-only` 指的就是这件事。
- **本文档没有 `## Procedure` / `## Before you begin` / `## Important points` 段**——
  上面「典型用法」那六步是**本页按 `## Example` 那一块代码排出来的**，
  **不是文档给的编号流程**；例子里的代码本身是原文逐字。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改。**
> **①②③ 回上游 `tdc-html/raw/141182.htm`（5,553 字节 / 68 行）核过，结论写在每条后面。**
> ① **四个构造函数在代码跨度上不一致**：第 1 个把 `;` 留在代码跨度之外；
>   第 2、3 个把参数名套进**嵌套的反引号**里；**第 4 个完全没有反引号**。原文逐字四种形态都不同。
>   **上游核过：这是上游自己的标记，不是转换坏的。** `141182.htm` 里逐字是
>   `<code>LevelSetSelector(const LevelSetSelector &amp;</code><span class="keyword">rhs</span><code>);</code>`
>   ——**上游就是把 `<code>` 拆成两段、中间插了一个 `keyword` 元素**，
>   markdown 的反引号忠实地照着 `<code>` 的边界断开；
>   而第 4 个 `<li>` 上游本来就**没有 `<code>`**（只有 `<span class="keyword">levelSet</span>`），
>   所以转换后也没有反引号。**结论：这一处是「上游如此」，不是 A 类转换损坏。**
> ② **参数表 `rhs` 那格与签名不符**：表里写 `An existing LevelSetSelector object`，
>   而签名取的是 `const LevelSetSelector&` / `const LevelSetSelector*`——**取的是引用或指针，不是「对象」**。
>   **上游核过：`141182.htm` 那个 `<td>` 里逐字就是这个句子**，不是转换改写。
> ③ **两处谓语有毛病**：`This constructor refers an existing level set`（`refers` 后缺 `to`），
>   以及 `DIGITAL_OFFSET_SEARCH::ALL: Refer to all fixed level sets.`（`Refer` 应为 `Refers`）。
>   **上游核过：`141182.htm` 逐字如此。**
> ④ **本篇没有坏字。** 用 `[一-鿿]` 实测全文 **0 处非 ASCII 字符**
>   （没有 `鈥` / `渭` / `碌` 那一族）。**这是「本页量过的」，判据是本篇这一个文件**；
>   §11.2 ① 那族在别的篇里大量存在。

`verified: doc-only`——**本页没有在任何真实机台上做过一次 offset search**
（§11：文档里有 ≠ 这台机器上能用；尤其 `PRM` / `ALL` 那两格的语义，**动手前先照实机核对**）。
