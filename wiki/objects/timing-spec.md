---
type: object
title: TIMING_SPEC
layer: L2
stage: timing
tags: [timing, test-method-api, timing-spec, spec-set, spec-value, spec-variable, primary-status, flush]
related: [timing, timing-specification, timing-equation-set, spec-set, spec-value, spec-variable, primary-status, level-spec, flush, svlr, spec-tool, timing-file, timing-set-selector, mapping-timing, smartest-6.3.2]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.249_TIMING_SPEC.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# TIMING_SPEC

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **2,410 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.249_TIMING_SPEC.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example 1: Change primary timing set

```
TIMING_SPEC spec1(1, 2);
Primary.timing(spec1);
Primary.timing(1);
```

spec1 is an object of the TIMING_SPEC class. The timing() member function of the PRIMARY_STATUS API sets timing equation set "1" and spec set "2" as the primary timing specification. The timing equation and spec set numbers must be specified using the corresponding object name spec1.

The second timing() member function defines the timing set "1" as the primary.

### Example 2: Change a primary timing spec value

```
TIMING_SPEC spec1(1, 2);
Primary.getTimingSpec().change("Tp", 10);
```

The change() member function changes the value of spec variable "Tp" to 10 nanoseconds. The Primary.getTimingSpec() statement returns the TIMING_SPEC API's class object, namely spec1, that defines the current primary timing specification.

```
TIMING_SPEC& ts_obj= Primary.getTimingSpec();
ts_obj.change("Tp", 10);
```

The change() member function changes the spec variable "Tp" to10 nanoseconds. By the ampersand (&) in the first statement, ts_obj is created as a reference to the class object returned by Primary.getTimingSpec() without copying the contents object.

```
TIMING_SPEC spec1(1, 2);
Primary.getTimingSpec().change("Tp", 10 ns);
```

In this example, with "ns" in the second parameter of the change() member function, the spec variable "Tp" is changed into 10-9 seconds. This is more convenient when you want your timing in nanoseconds be represented in seconds basis.

### Example 3: Retrieve a primary timing spec value

```
DOUBLE specValue = Primary.getTimingSpec().getSpecValue("Tp");
```

The getSpecValue() member function returns the value of the "Tp" spec variable in the currently defined primary specification. The Primary.getTimingSpec() statement returns the TIMING_SPEC API's class object that represents the spec set and equation set that are currently defined as the primary.

### Example 4: Retrieve a primary timing spec value for a multiport specification

```
DOUBLE specValue = Primary.timing(SPECIFICATION("spec")).getSpecification().getSpecValue("specValue@port");
```

The `getSpecValue()`（raw: `02.07.04.01.249_TIMING_SPEC.md#_29809__dle_getSpecValue`） member function returns a spec value for a single port of a multiport timing specification. The spec value and the port are defined by `"specValue@port"`. The multiport timing specification is selected by the `SPECIFICATION`（raw: `02.07.04.01.232_SPECIFICATION.md`） API.

### Example 5: Retrieve the timing equation set

```
INT tmg_eq;
    :
tmg_eq = Primary.getTimingSpec().getEquation();
```

The getEquation() member function returns the timing equation set number currently defined as the primary.

<!-- 语法节 end -->

## 是什么

**`TIMING_SPEC` 是一个 L2 的句柄，指向「某个 equation set 里的某个 spec set」的内容。**
原文第一句就是这件事：

> 「The TIMING_SPEC API accesses the data container holding the contents of an existing timing equation and spec set.」

**它不是「一份 timing 配置」，是「一套已经存在的 spec 值的操作柄」**——自己不带数据，只带两个编号
（equation set 号 + spec set 号）。它要解决的问题是：**测试方法跑到一半，想读/改当前主时序里某个 spec 变量的值。**

### 两个编号定位它，五个成员操作它

**下面这张表的签名不在本页的「语法 / 参数」节里**——raw 里它们挂在 `## Class definition` 与
`## Member functions` 下，不是 `## Syntax`（脚本的抽取口径如此，本页不改它，只在这里逐字引一次）：

```
TIMING_SPEC(INT eqnset, INT specset)
```

| 成员 | 签名（逐字） | 作用 |
|---|---|---|
| `getEquation()` | `INT getEquation()` | 返回 **equation set 号** |
| `getSpec()` | `INT getSpec()` | 返回 **spec set 号** |
| `getSpecValue()` | `DOUBLE getSpecValue(const STRING& spec)` | 返回**某个 spec 的值**；多 port 时参数写 `"spec@port"` |
| `change()` | `void change(const STRING& spec, DOUBLE value)` | **改某个 spec 的值** |
| `restore()` | `void restore()` | 把所有 spec **复位**到本 testsuite 的 test method 程序开始时的值 |

构造函数的两个参数原文各一句：`eqnset` = `Equation set number`，`specset` = `Spec set number`。
头文件位置也是原文给的：

> 「This API is defined in the header file /opt/hp93000/soc/prod_com/include/MAPI/TimingSpec.h.」

### 它操作的是「primary」那一套

**这是最容易读漏的一层：`TIMING_SPEC` 的对象不等于「随便一套 spec 值」，它要接到「当前被定为 primary 的那一套」才起作用。**
原文把两条路都写了：

> 「To define a spec set of an equation set as the primary, execute the PRIMARY_STATUS API member function timing() for the corresponding TIMING_SPEC API's class object.」

> 「To change the definition of a spec value in the spec set that is currently defined as the primary, use the PRIMARY_STATUS API member function getTimingSpec() to return the corresponding TIMING_SPEC API's class object, and execute the TIMING_SPEC API change() member function for that returned class object.」

**一句话：`PRIMARY_STATUS` 是入口，`TIMING_SPEC` 是返回来的那个东西。**
（`PRIMARY_STATUS` 在语料里常写作 `Primary`——例子里就是 `Primary.timing(...)`、`Primary.getTimingSpec()`。）

### 改值什么时候真的生效 —— **不是立刻**

**API 只是改了内存里的值。**要它反映到硬件上，必须再执行下面这串 API 之一：

| 执行这个 | 说明 |
|---|---|
| `EXECUTE_TEST` / `START_TEST` / `DIGITAL_CAPTURE_TEST` / `NB_DIGITAL_CAPTURE_START` / `FUNCTIONAL_TEST` | 五条直接的 |
| `FLUSH` then `SPEC_SEARCH.execute()` member function) | 后半截是**另一个对象**的成员函数 |
| `FLUSH` then `SEQUENCER_STATUS.run()` member function) | 同上 |
| `FLUSH` then `PMU_IFVM.execute()` member function) | 同上 |
| `FLUSH` then `PMU_VFIM.execute()` member function) | 同上 |
| `FLUSH` then `TASK_LIST.execute()` member function) | 同上 |
| `FLUSH` then `DPS_VFIM.execute()` member function) | 同上 |

引导句逐字：

> 「The changes of the definitions specified by this API are actually reflected to the hardware when any of the following APIs is executed.」

**`FLUSH` 还有一个单独的作用——把改动反映到 MCD（界面侧）**：

> 「The changes of the definitions specified by this API can be also reflected to the MCD when the FLUSH API is executed. This is an option to reflect the changes on the user interface such as the Test Program Explorer and the Spec Tool.」

**所以「改了值」和「值生效了」是两件事，中间隔着一次 `FLUSH` 或一次测试执行。**
（上表七条以 `FLUSH then` 开头的原文，每条末尾都多一个 `)`——见「出处」的语料瑕疵⑤，本页照原样引。）

### 三条顺序规矩（**错了会静默丢数据**）

| 规矩 | 原文（逐字） | 不照做的后果 |
|---|---|---|
| **切 primary 之前先 `FLUSH`** | `If you need to reflect these changes (into the MCD), execute FLUSH(TM::APRM) once before specifying another primary spec set or primary equation set in the PRIMARY_STATUS API.` | 之前改的值**被丢掉、不执行** |
| **想在下个 testsuite 用回原值 → `restore()` + `FLUSH`** | `If you want to use the original spec values in the next testsuite, execute the restore() member function and FLUSH API in the test method program of the testsuite where you changed the spec values.` | 改动**会带进后面的 testsuite** |
| **要让界面显示「timing 已改」→ 先在 Spec Tool 里改一次值** | `if you need to reload the current timing setup file during debugging, first change a spec value in the Spec Tool window to cause the Test Program Explorer to indicate that the timing is changed.` | TPE **不显示** timing 已改，调试时重载 setup file 会踩坑 |

第一条的机理（**被丢掉的判据是「有没有 FLUSH 过」**）：

> 「the spec value changes specified in the TIMING_SPEC API's class objects are cleared if the FLUSH API has not been executed for them yet.」

第三条的机理（同一条 bullet 的前半）：

> 「The change() member function and FLUSH API change a spec value, but the Test Program Explorer does not indicate that the timing is changed.」

### 值与单位

- **值必须在 spec set 的 min/max 之间**：

  > 「The value must be within the range between the minimum and maximum values specified in the spec set.」

- **默认单位是纳秒**：

  > 「In SmarTest, all timing values are in nanoseconds by default.」

- **第二参数可以带单位后缀**：Example 2 的第三种写法是 `Primary.getTimingSpec().change("Tp", 10 ns);`，
  原文的解释是「the spec variable "Tp" is changed into 10-9 seconds」——
  **即：带上 `ns` 就是「按秒为基准表示纳秒」**，原文说这样写更方便。

### 一条 CAUTION：**别把 API 和固件命令混用**

这是本页最重的一条，原文用 CAUTION 标出，**并且同时点名了 `LEVEL_SPEC`**：

> 「Never mix the LEVEL_SPEC or TIMING_SPEC API and firmware commands modifying values for other reasons than debugging purposes (see note below)! LEVEL_SPEC and TIMING_SPEC test method APIs cache values in order to enable the .restore() functionality. This caching is not available on the firmware level.」

**机理一句话：API 侧缓存了值，`restore()` 靠这份缓存；固件层没有这份缓存。**
所以从固件侧改值，API 的 `restore()` 就不再可靠。**唯一的例外是调试**（原文写了 `for debugging purposes`）。

**同一条 CAUTION 的后半是「改了不落盘」**：

> 「In both cases, changing spec values takes effect without changing the level or timing file! If you want to change spec values permanently you must do so in the corresponding setup file itself.」

**所以：走 API 改值 = 只影响这一次运行；要永久改，回 setup file 里改。**

**被允许的调试路径**原文也给了：

> 「For debug purpose only: If you want to change the spec value while the application model is running without having to abort the execution, you can pause the application model, change the spec value with the firmware command SVLR directly from hpt and then resume the running of the application model.」

——**注意这条路要求「pause → 改 → resume」，不是随便改。**

### 一条格式限制，和一处原文自己没对齐的地方

限制逐字：

> 「In this API, only one member function can be specified per statement.」

**但原文自己的 Example 2 写的是 `Primary.getTimingSpec().change("Tp", 10);`——一条语句里出现了两个成员函数名**
（`getTimingSpec()` 与 `change()`）。**本页把两处并列摆着，不判哪一处是笔误**（见「出处」瑕疵⑦）。

### 「只有这一种办法」——原文的原话，带 `Currently`

> 「Currently, you can change the primary timing specification or the value of a spec variable in the current specification only if you explicitly define an object of the TIMING_SPEC API class and then refer to this object」

它给的例子就是：

```
TIMING_SPEC spec1(1, 2);
Primary.timing(spec1);
```

**取对象有两条等价的路**（原文 Important points 里成对给出的）：

| 路 | 写法 | 原文 |
|---|---|---|
| 用 `getTimingSpec()` 取回 | `Primary.getTimingSpec().getSpecValue("T")` | `Primary.getTimingSpec() returns the object of the current primary specification` |
| 直接用对象名 | `spec1.getSpecValue("T")` | `if spec1 defines the current primary specification, specify as follows` |

原文把两条路的等价性也写明了：

> 「Both statements shown above produce the same result if spec1 defines the current primary timing specification.」

## 典型用法

### 五种用法，全在原文的 `## Examples` 里

| 你想干什么 | 写法（逐字） | 原文的说明 |
|---|---|---|
| **把某套 spec set 定成 primary** | `TIMING_SPEC spec1(1, 2);`<br>`Primary.timing(spec1);` | 设 equation set `1` + spec set `2` 为 primary；**号码必须通过 `spec1` 这个对象名传** |
| **只把某个 timing set 定成 primary** | `Primary.timing(1);` | `The second timing() member function defines the timing set "1" as the primary.` |
| **改 primary 里某个 spec 的值** | `Primary.getTimingSpec().change("Tp", 10);` | 把 `Tp` 改成 **10 纳秒** |
| **同上，但用引用避免拷贝** | `TIMING_SPEC& ts_obj= Primary.getTimingSpec();`<br>`ts_obj.change("Tp", 10);` | 原文：`ts_obj is created as a reference to the class object returned by Primary.getTimingSpec() without copying the contents object` |
| **带单位改值** | `Primary.getTimingSpec().change("Tp", 10 ns);` | 按秒为基准表示纳秒 |
| **读 primary 里某个 spec 的值** | `DOUBLE specValue = Primary.getTimingSpec().getSpecValue("Tp");` | 返回当前 primary 里 `Tp` 的值 |
| **读多 port 的一个 port 的值** | `DOUBLE specValue = Primary.timing(SPECIFICATION("spec")).getSpecification().getSpecValue("specValue@port");` | `"specValue@port"` 里 `@` 前是 spec 名、`@` 后是 port |
| **读当前 primary 的 equation set 号** | `INT tmg_eq;`<br>`    :`<br>`tmg_eq = Primary.getTimingSpec().getEquation();` | 返回 equation set 号 |

**最小可用的一段**（改 primary 里一个 spec 值，原文的 Example 2 原样）：

```
TIMING_SPEC spec1(1, 2);
Primary.getTimingSpec().change("Tp", 10);
```

### 顺序（**这是本页最容易做错的一步**）

**API 调用本身不产生后果，后果在「谁接着执行」上。**照下面这个顺序写：

1. **（要改 primary 的话）先确认上一轮的改动已经 `FLUSH` 过**——
   不 `FLUSH` 就切 primary，**改过的值会被丢掉**。
2. **调 API 改值**（`change()` / `restore()`）。
3. **让它生效**：执行上表那串 API 之一（最常用的是 `FLUSH`，或直接跑 `FUNCTIONAL_TEST` 这类测试）。
4. **想在下一个 testsuite 用回原值**：在本 testsuite 里补一次 `restore()` **再** `FLUSH`。
5. **（调试时）要重载 setup file**：先在 Spec Tool 里手工改一次值，让 TPE 显示 timing 已改，
   否则重载会出意外（原文只说「TPE 不显示已改」，具体后果语料未写）。

### 两个前提

- **必须先显式定义 `TIMING_SPEC` 对象**（原文 `## Important points` 第一条，带 `Currently`）——
  不能只写一句 `Primary.getTimingSpec().change(...)` 就指望它能改 primary 本身。
- **一句一个成员函数**（原文 `In this API, only one member function can be specified per statement.`）。

### 原文那条 `FLUSH` 顺序的反例

原文用一个「错在哪」的例子把第 1 步讲清楚了——**`FLUSH` 在切 spec set 之后才执行，所以前面两次 `change()` 白做**：

```
TIMING_SPEC spec1(1, 2);
TIMING_SPEC spec2(1, 3);
Primary.timing(spec1);
FUNCTIONAL_TEST();
TEST(TM::CONTINNUE);
Primary.getSpecification().change("T", 10);
Primary.getSpecification().change("T2", 20);
Primary.timing(spec2);
FLUSH;
```

原文的判词逐字：`In the following example, FLUSH is not executed before the change to the spec set "3" is specified. Therefore, the changes specified for "T" and "T2" are ignored (not executed).`

> **照这段抄的时候注意两件事**：① 这里用的取对象方法是 `Primary.getSpecification()`，
> **不是别的段落里的 `Primary.getTimingSpec()`**——原文没说这两个是不是同一个（见「出处」瑕疵⑦）；
> ② `TEST(TM::CONTINNUE);` 里的 `CONTINNUE` **原文就是三个 N**（见「出处」瑕疵②）。**照原样，别改。**

## 和谁有关

**每条都写清是什么关系**。凡是「本页没读那篇」的，都标出来——**那是本页的取材边界，不是关系不存在**。

| 和谁 | 什么关系 | 依据 |
|---|---|---|
| [[primary-status]] | **宿主 / 前置**。`TIMING_SPEC` 的对象通常从它的 `getTimingSpec()` 取回；要把它指的那套设成 primary，用它的 `timing()` 成员函数 | 本页正文三条引文（**文档事实**） |
| [[level-spec]] | **同类对照（level 侧的对应物）**。原文那条 CAUTION **一句话同时点名两个 API**，并说两者共用同一套缓存机制 | 本页正文 CAUTION 引文（**文档事实**） |
| [[flush]] | **下游触发**。改值要它才生效（反映到硬件/MCD）；切 primary 前也必须先执行它 | 本页正文两张表（**文档事实**） |
| [[svlr]] | **替代路径，只许调试用**。固件命令，能在 application model 跑着的时候改 spec 值（pause → 改 → resume） | 本页正文 Note 引文（**文档事实**） |
| [[spec-tool]] | **GUI 侧的改值入口**，也是原文那条「让 TPE 显示 timing 已改」规矩里点名的工具 | 本页正文引文（**文档事实**） |
| [[spec-search]] | 原文「改值生效」清单里 `FLUSH then SPEC_SEARCH.execute()` 那一项 | 本页正文清单（**文档事实**） |
| [[timing-specification]] / [[timing-equation-set]] / [[spec-set]] | **它指的东西**。它访问的容器就是「equation set 里的 spec set」；这三个名字说的是容器的三个层次 | 原文第一句 + 构造函数参数（**文档事实**） |
| [[timing-file]] / [[timing-master-file]] | **落盘的那一侧**。「改值不落盘」这条把两者划开：要永久改，得改 setup file | 本页正文 CAUTION 引文（**文档事实**） |
| [[spec-value]] / [[spec-variable]] | **它读写的量**。`getSpecValue()` / `change()` 对的就是它们 | 原文成员函数说明（**文档事实**） |
| [[timing-set-selector]] | **同 stage 的另一个 L2 入口**（那页未建）。本页只从 `PRIMARY_STATUS` 的 `timing()` 里见到「timing set 号」这一层，**`TimingSetSelector` 本篇没读** | 本篇没读那篇（**取材边界**） |
| [[aprm]] | **L1 侧的同类动作**（激活 primary sets）——原文那条顺序规矩里写的 `FLUSH(TM::APRM)` 正好点到了 `APRM` 的编号 | 本页正文引文（**文档事实**） |
| [[mapping-timing]] | **对照表页**（已建）。本页在那个主表里占两格：L2 列的 `TIMING_SPEC(eqnset, specset)`（绑 specification 那一行）与 `change()` / `restore()` / `getSpecValue()`（赋 spec 值那一行）；它的 ⑧ 还并列了本页「纳秒」与其他两篇的单位说法 | 那页的表与 ⑧（**本页读过的 wiki 页**） |
| [[timing]] | **stage 页**。本页 `stage: timing` 填的是「**最近的一段**」不是「归属」——`TIMING_SPEC` 本身是 test method 里的 API，只是它动的东西是 timing 数据（§6） | frontmatter 约定 |
| [[tpi-program-routines]] | **L3 侧的同类入口**（`DataManager` 的 `dm_timing`）。**本页没读那 31 篇**，只从 [[mapping-timing]] 的记载知道它存在 | 本页没读（**取材边界**） |

**一条反例，必须显式记一笔**：`Primary.getSpecification()` 与 `Primary.getTimingSpec()` **在同一篇里并用**
（前者出现在 `## Important points` 的顺序规矩例子里，后者出现在 Example 2/3/5 与 `## Important points` 的另一处）。
**原文没说这两个取对象方法的区别**——本页**不把它们当成同一个**，也不当成矛盾。

## 版本

本文档**有** `## Functional changes` 段，段里**只有一条**：

- **Introduced before SmarTest 6.3.2** → [[smartest-6.3.2]]

> **这一条是 §11.2 ② 说的哨兵值，不是「6.3.2 新增了这个 API」。**
> 措辞是 `before`（不是 `in`），意思是「**在本套文档覆盖范围开始之前就已经有了**」。
> **所以本页不能推断 `TIMING_SPEC` 是 6.3.2 引入的**——只能说：**7.10.3 上有，且它比 6.3.2 更老。**

**版本段里没有的东西**（照实记，不替它补）：**没有一条 `SmarTest X.Y.Z:` 形式的变更记录**。
所以「`change()` 的 `10 ns` 写法、`restore()`、多 port 的 `"spec@port"` 分别是哪个版本进来的」
**在本篇里查不到**——要查得去 [[smartest-6.3.2]] 之后的各版本页，或去别的文档。

## 出处

`sources:` **一篇**：

- `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.249_TIMING_SPEC.md`
  （TDC `29809.htm`，12,565 字节 / 251 行，**整篇读完**）
- 本页的「语法 / 参数」节是脚本从这一篇的 `## Examples` 段逐字抽的（**本页一个字没动**）。
  本页**没有核实**它抽全了没有——**但从内容看，这一篇的 `## Class definition` 与
  `## Member functions` 两段（构造签名 + 五个成员签名）不在那个节里**（raw 里它们不叫 `## Syntax`），
  所以本页在正文里逐字引了一次。

**本页没做的**：

- **`Related information` 指的六篇一篇没读**：`Timing Specifications - Reference`、
  `Timing Specifications - Example`、`Timing Spec Vars and Level Spec Vars`、`Timing spec set`、
  `LEVEL_SPEC`（前四篇在 `02.08_Setup_and_Result_Tools`，第五篇在 `02.07.04.01.124`）。
  **所以「spec set 怎么编辑、`LEVEL_SPEC` 那边长什么样」本页一个字没有。**
- **`PRIMARY_STATUS` 那一篇没读。** 本页知道 `timing()` / `getTimingSpec()` 存在、
  知道它们返回什么，**但那一篇自己的参数、重载、其他成员，本页不知道**。
- **`FLUSH` / `SVLR` / `SPEC_SEARCH` / `SEQUENCER_STATUS` / `PMU_IFVM` / `PMU_VFIM` /
  `TASK_LIST` / `DPS_VFIM` / `SPECIFICATION` 九条被点名的对象，一篇都没读正文**——
  本页只从本篇的清单里知道**它们的名字**与「执行了它，改动才会生效」这一件事。
- **`02.07.03.03.02.01_Changing_spec_value_in_primary_timing_spec_set` 没读**——
  它是 [[mapping-timing]] 拿来当 L2 侧材料的篇目之一（**那页读了，本页没读**）。
- **四张图都没有**（**这是事实，不是「够不着」**）：本篇对 `raw/` 的引用 **0 处**——
  实测 `.png` / `.jpg` / `.gif` / `!\[` / `<img` / `raw/` 六种写法在本篇里**全部 0 命中**。
  **所以本页没有任何来自图的结论。**
- **没有实跑。** 没在机台上改过任何 spec 值、没调过 `FLUSH`、没有验证过「不 FLUSH 就切 primary 会丢值」。
  `verified: doc-only` 指的就是这件事。

**⚠️ 本篇的六处语料瑕疵，本页照实记下、一处都没替它改**（①③④ 本页回上游 `.htm` 核过）：

> ① **`Note` 与 `CAUTION` 两个块被压成一行、中间没有分隔**：
> `are in nanoseconds by default.CAUTION Never mix the LEVEL_SPEC or TIMING_SPEC` 这两句被粘在了一起
> （原文此处是 `by default.` 紧接 `CAUTION Never mix`）。
> **上游 `29809.htm` 里是两段**（`</div><div class="caution">`）——**所以这是 HTML→md 压平造成的**。
> **本页在正文里引这两句时，各自只引到自己的句尾**，没有把 `default.CAUTION` 这个粘连体抄进引文。

> ② **`TEST(TM::CONTINNUE);` —— `CONTINNUE` 是三个 N。**
> **上游 `.htm` 里也是 `CONTINNUE`**（实测：`29809.htm` 里 `CONTINNUE` 1 次、`CONTINUE` **0 次**）
> ——**属 §11.2 ⑥ 那族（上游就坏的，救不回来）**，不是转换坏的。
> **本页照原样留在代码块里**，一个字没改（真去敲这段代码时要注意）。

> ③ **`to10 nanoseconds`（`to` 与 `10` 之间缺空格）**——Example 2 第二段的正文。
> **上游 `.htm` 里也是 `to10`**（实测 1 次）→ 同属 §11.2 ⑥。

> ④ **`10-9 seconds` 里的上标丢了**。上游 `.htm` 写的是 `10<sup>-9</sup> seconds`
> ——**是 HTML→md 把上标压成了普通字符 `-9`**。
> **本页在正文里照原样引**（所以那句话读起来像「10 减 9 秒」，实际是 10⁻⁹ 秒）。

> ⑤ **「改值生效」清单里那七条以 `FLUSH then` 开头的条目，每条末尾都多一个 `)`**：
> `FLUSH then SPEC_SEARCH.execute() member function)`——**左括号没有对应的右括号**。
> **原文如此，本页照原样引**（上面那张表就是逐字抄的）。

> ⑥ **`Example 5` 的代码块里有一行只有四个空格加一个冒号**（`    :`）——
> 是原文的续行标记，**本页照原样抄进了代码块**。

> ⑦ **`Primary.getSpecification()` 与 `Primary.getTimingSpec()` 在同一篇里并用**，
> **原文没说这两个取对象方法的区别**。**本页把两处并列摆着，不判哪个是笔误、也不把它们合并**。

**另有一条不属于「瑕疵」但值得记的**：本页的**「语法 / 参数」节里没有任何 C++ 签名**——
那一节整篇是 `## Examples` 的五个例子。**这不是本节缺内容，是 raw 的组织方式**
（签名在 `## Class definition` / `## Member functions` 下）。**本页在正文里补引了一次，语法节一个字没动。**

`verified: doc-only`
