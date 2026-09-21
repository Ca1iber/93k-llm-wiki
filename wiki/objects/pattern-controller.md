---
type: object
title: PATTERN_CONTROLLER
layer: L2
stage: pattern
tags: [pattern, l2, test-method-api, subpattern, dc-test, ppmu, badc, dc-scale, pattern-controller]
related: [pattern, pattern-object, mapping-pattern, dc-result-accessor, flex-relay, dc-test-programming, testmethod, pin, testflow, smartest-6.3.2]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.142_PATTERN_CONTROLLER.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# PATTERN_CONTROLLER

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **2,521 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.142_PATTERN_CONTROLLER.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

The general format for setting up a DC subpattern is

```
obj.label().add(dc_task_1).add(dc_task_2)...add(dc_task_n);
```

The general format for downloading or executing a DC subpattern, or retrieving test results, is

```
obj.func();
```

The parameters have the following meaning:

 | obj  | Object of the PATTERN_CONTROLLER class |
 | func()  | Member function of the PATTERN_CONTROLLER class |
 | add()  | Member function of the PATTERN class |

### Examples

### PPMU IVFM test

In this example, a PPMU IVFM test on the pin `S0` and a PPMU VFIM test on the pin `S1` are performed from the pattern. The subroutine label `DC_Sub_Q0` is used for the execution of DC test.

```
PPMU_SETTING        setting, precharge;
PPMU_RELAY          relay_on, relay_off;
PPMU_MEASURE        meas1;
PPMU_CLAMP          clamp_on, clamp_off;
PATTERN_CONTROLLER  controller;

ON_FIRST_INVOCATION_BEGIN();

    //
    // Setups for PPMU
    //
    setting.pin("S0").iRange(1 mA).min(0 V).max(4.3 V).iForce(10 uA);
    setting.pin("S1").iRange(10 mA).min(-10 uA).max(30 uA).vForce(3.3 V);

    precharge.pin("S0").iRange(20 mA).min(0 mA).max(30 mA) .vForce(2.8 V);

    //
    // Relay setups
    //
    relay_on.pin("S0,S1").status("PPMU_ON");
    relay_on.wait(1.3 ms);
    relay_off.pin("S0,S1").status("AC_ON");

    //
    // Measurement setups
    //
    meas1.pin("S0,S1").execMode(TM::PVAL);

    //
    // Hardware specific programming to avoid hot switching
    // on the Current Force setup
    //
    if(GET_TESTER_CLASS()==TM::PINSCALE)
    {
        clamp_on.pin("S0").status("CLAMP_ON").low(2.6 V).high(2.9 V);
        clamp_off.pin("S1").status("CLAMP_OFF");
    }

    //
    // Set up the controller
    //
    if(GET_TESTER_CLASS()==TM::PINSCALE)
        controller.label("DC_Sub_Q0","Q0_Port").add(setting).add(clamp_on)
              .add(relay_on).add(clamp_off).add(meas1).add(relay_off);
    else
        controller.label("DC_Sub_Q0","Q0_Port").add(precharge)
              .add(relay_on).add(setting).add(meas1).add(relay_off);

    controller.execMode("PPF").execute();

ON_FIRST_INVOCATION_END();

//
// Result upload and datalog
//
TEST("S0", "DC_TEST", controller.getPassFail("S0")?TM::Pass:TM::Fail,TRUE);
TEST("S1", "DC_TEST", controller.getPassFail("S1")?TM::Pass:TM::Fail,TRUE);
```

### PS1600 DC measurement examples

For DC value measurement examples using the PS1600 pin PMU (PPMU) and board ADC (BADC) see `PS1600 DC value measurements`（raw: `../02.05_Test_Head_Cards/02.05.04.01.03.04_PS1600_DC_value_measurements.md`）.

<!-- 语法节 end -->

## 是什么

**PATTERN_CONTROLLER 是「在 pattern 里跑 DC 测试」的那条 L2 通道。** 它把测试方法里用
`PPMU_...` / `BADC_...` 那一族 API 定义好的测量集**下载成一段 DC 子程序（DC subpattern）**，
再把它执行掉。

> The PATTERN_CONTROLLER API serves to execute DC Scale DC and PPMU BADC tests from within a pattern (for conceptual information see Executing PPMU tests from a pattern).

**它解决的是「数字测试与 DC 测试在同一段 pattern 里交替」这件事**：

> It can be used to execute DC tests in parallel with digital test for different ports, and also to alternate (switch between) digital and DC tests in one pattern run, without the need to stop and start the sequencer before the DC test.

**最后半句是全部价值所在**：跑 DC 测试**不必先停定序器再起定序器**。

文档自己把它拆成三件事（原文的三条 bullet）：

> - Downloads measurement sets defined with the PPMU_... and BADC_... APIs
> - Inserts instructions (which will execute these sets) into a predefined subpattern
> - Executes the current primary sets

**三件事对应成员函数**：`label()` 开门（拿到子程序对象）→ `setup()` 下载并插 `MEAS` 指令 →
`execute()` 执行 → `getPassFail()` 取结果；`execMode()` 决定判定粒度（见下）。
头文件是 `/opt/hp93000/soc/prod_com/include/MAPI/PatternController.h`。

### 它操作的是 `PATTERN` 对象——**那个 `PATTERN` 不是 stage 页 `[[pattern]]`**

> The PATTERN_CONTROLLER API calls objects of the PATTERN class. This is a subsidiary data container that holds the measurement data for individual subpatterns.

**这一句里的 `PATTERN` 是类名**（`02.07.04.01.142.01`，本页的子主题），
**不是 pattern 那一段流程**。§5 为这件事专门定过一条：L2 的 `PATTERN` 类 → `[[pattern-object]]`，
与 stage 页 `[[pattern]]` 区分；**那条规矩是「`PATTERN` 撞 stage 名」撞出来的**
（「指错比重复更坏：重复页看得见，指错看不见」，`schema.md` §5）。
**本页照这条写：对象侧一律走 `[[pattern-object]]`，流程侧才走 `[[pattern]]`。**

**「容器」这个词在这里是字面意思**：`.add()` 收进去的那些测量对象**被链进一个子程序**，
而链接用的**是运行期动态生成的内部 ID**：

> For PPMU BADC tests with digital cards the subpattern must be empty, as the PATTERN_CONTROLLER will dynamically link the measurements defined with test method APIs into the empty subpattern in the order they are added to the PATTERN_CONTROLLER. This link uses internal IDs. Once the measurements are linked into the subpattern, it cannot be stored permanently, as these IDs are dynamically created depending on single test suite execution and complete test flow execution.

**两个后果**：① 数字卡上的 PPMU BADC 测试**必须用空子程序**（不是「建议」，是硬条件）；
② **加进去的顺序就是语义**——示例里两种机台类别的 `.add()` 次序不同，见「典型用法」。

### 一组只在这一页有的数：BADC / PPMU 测量的耗时

> twait = (25 渭s + N * 4 渭s)

> 25 渭s is a one-time overhead

> After the measurement is performed, SmarTest needs an additional time (typical) of 20 渭s * N, where N is the number of samples, to fetch the results. For this additional duration of time, the BADC cannot be used to perform a new measurement.

> In additional, an extra wait time of, at least, 60 渭s must be added for the first BADC measurement after switching the measurement mode on one channel for EXA Scale digital cards or Smart Scale digital cards in Exa Scale compatibility mode.

**`渭` 是语料的坏字，应为 `µ`**（本篇 4 处，见「出处」）。**引文里照原样留着**（§11.2）。
把这三句连起来读，得到的是**排测试顺序时要留的余量**：N 个采样点要 `25 + 4N` 微秒，
取结果又要 `20N` 微秒，而**这 `20N` 微秒里 BADC 不能再起一次测量**。

### 五条「Important points」——**这一页真正要读的一段**

原文这一节的标题就是 `## Important points`，五条**全是「条件 → 结论」**，没有一句背景铺陈：

| 情形 | 文档给的结论 | 原文关键句（逐字） |
|---|---|---|
| 用子程序跑 DC 测试 | **不能**用 `PPMU_MEASURE` 取结果，它的 `execMode()` **被忽略**；**只有** `getPassFail()` / `GET_FUNCTIONAL_RESULT` 两条路；**测得的数值拿不到** | `Therefore, you cannot retrieve the measured values of the test.` |
| test suite 触发子程序、而 PPMU DC set 已用尽 | **抛错**；**不走**标准 DC 测试的 fall-back 机制 | `It does not employ the fall-back mechanism that is used for standard DC tests in this situation` |
| 想在循环里跑「参数随循环变」的子程序 | **必须**用 `setup()`；`MEAS` 一旦插入，子程序**不可再改** | `the sequencer subpattern into which the PATTERN_CONTROLLER API writes the MEAS instructions cannot be modified with this API after insertion of the MEAS instructions` |
| 主 pattern 在调用之后还有向量 | **Timing Diagram 表现不出来**——它只显示测量期生成的少量 break vector | `the temporal relations of these vectors to those of the digital ports will not be represented correctly by the Timing Diagram` |
| 想要每 pin 的细节结果 | 拿不到；BADC 的 pin 结果要走 [[dc-result-accessor]]；`execMode()` 对 `BADC_MEASURE` **被忽略** | `Global pass/fail results can be retrieved, but detail results per pin are not available.` |

**第一行那条最容易被踩**：写这套代码的人看到 `meas1.pin("S0,S1").execMode(TM::PVAL)`
（示例第 206 行）会以为结果在 `PPMU_MEASURE` 里——**不在**。

### 五个成员函数：各自只讲一件事

| 成员函数 | 一句话 | 关键约束 |
|---|---|---|
| `label(subpattern_name, port)` | 返回持有该 label 的 DC 任务的 `[[pattern-object]]` | 后面**只能接着**调 `PATTERN` 的成员函数；子程序**必须已存在**；`port` 默认 `@` |
| `execMode(mode)` | 决定执行模式 | **决定权在它**，不在 `PPMU_MEASURE` |
| `setup()` | 下载测量集 + 往子程序插 `MEAS` 指令 | **一个 testflow 执行期内只写一次** |
| `execute()` | 执行当前 primary set | 子程序还空时**它自己先调 `setup()`** |
| `getPassFail(...)` | 全局或按 pinlist 取 PASS/FAIL | 带 pinlist 时**全 pass 才算 PASS** |

**`label()` 的那条顺序约束是硬的**：

> A call of this function must be followed by calls of member functions of the PATTERN class. You cannot call another member function of the PATTERN_CONTROLLER class after calling label().

**`execMode()` 的那条是「谁说话算数」**：

> It is the execMode() function of the PATTERN_CONTROLLER API that determines the execution mode. The execution mode of the PPMU_MEASURE API is ignored. But it must be specified nonetheless, since otherwise no measurement would be performed.

**最后半句是个陷阱**：`PPMU_MEASURE` 的 `execMode()` **被忽略、但必须写**——不写就**不做测量**。

**`setup()` 的「只写一次」是性能设计，代价是参数不能随循环变**：

> For performance reasons, the instructions are written into the subpattern only once within one testflow execution; that is, the API will not modify them later on.

> if the same subpattern is used by more than one class object of the PATTERN_CONTROLLER API within one testflow, or if the testflow is executed in a loop, setup() expects that the same measurement sets can be used for the subpattern every time. If this is not the case (because the measurement parameters depend on variables so that they change from one loop repetition to the next, or because they are different for two class objects), it will issue an error message.

**`setup()` 另有一个用法**：它可以在**同一个类对象内**临时改掉上一次的参数定义——
文档把它指给「参数含变量」的那一类测量（`Managing DC Tests with Variable Parameters`，**那篇本页没读**）。

## 典型用法

**总形状**（文档的 `## Syntax` 给的两行，脚本已逐字抄在上面）：先
`obj.label(...).add(a).add(b)...add(n);` 串一条链，再 `obj.func();` 调一个成员函数。

**完整流程（照本篇唯一的例子 `PPMU IVFM test` 走）**：

1. **声明对象**——四个 PPMU 对象（`PPMU_SETTING` / `PPMU_RELAY` / `PPMU_MEASURE` / `PPMU_CLAMP`）
   各声明若干个，加一个 `PATTERN_CONTROLLER controller;`。
2. **配好每个对象**（`.pin()/.iRange()/.min()/.max()/.iForce()` / `.vForce()` 之类）——
   **这一步与 PATTERN_CONTROLLER 无关**，它是那一族 API 自己的语法。
3. **`controller.label("DC_Sub_Q0","Q0_Port")`**——`DC_Sub_Q0` 是**已经存在的子程序名**，
   `Q0_Port` 是它所属的端口。
4. **`.add(...)` 按执行次序串**——**这一步是本页的关键**：同一个例子给了**两条不同次序**，
   按 `GET_TESTER_CLASS()==TM::PINSCALE` 二选一。PINSCALE 那条插了 clamp 两个对象
   （避开 current force 上的热切换），非 PINSCALE 那条改用 `precharge`。
5. **`controller.execMode("PPF").execute();`**——先定粒度再执行；这里用的是字符串写法 `"PPF"`。
6. **`TEST("S0", "DC_TEST", controller.getPassFail("S0")?TM::Pass:TM::Fail, TRUE);`**——
   **每 pin 的结果只能这样取**，`getPassFail(pinlist)` 的返回值接给 `TEST`。

**几条顺序/前提**：

- **进来的地方**：例子把整条链放在 `ON_FIRST_INVOCATION_BEGIN()` / `ON_FIRST_INVOCATION_END()`
  之间（见 `[[on-first-invocation-begin]]` / `[[on-first-invocation-end]]`）——
  **写一次、不要每 site 重做**。
- **要循环跑、参数还随循环变** → **必须显式调 `setup()`**，否则报错（见上）。
- **想拿每 pin 的 BADC 数值** → 不在本 API，走 [[dc-result-accessor]]。
- **PS1600 的 PPMU / BADC 例子不在本篇**：文档在 `### PS1600 DC measurement examples`
  里把读者推给了 `PS1600 DC value measurements`（raw: `../02.05_Test_Head_Cards/02.05.04.01.03.04_PS1600_DC_value_measurements.md`，**本页没读**）。

## 和谁有关

**同一个对象家族的两半（本页最容易指错的一处）**：

- `[[pattern-object]]`（**未建**）— `PATTERN` 类本身：**装 DC 任务的容器**，由本页的
  `label()` 返回。**本页只讲控制器这一侧**；`add()` 收哪些对象、`PATTERN` 自己还有哪些成员函数，
  **在那一页**（本页没读，见「出处」）。
- [[pattern]]（stage 页）— **流程侧**：label / pattern 怎么定义、`SQLB` / `SQPG` 怎么用。
  本页与它的关系是**「用别人定义好的子程序」**：文档要求 `the subpattern must already exist`
  （**那一句是这句关系的依据**），**本页不定义 label**。**注意别把 `PATTERN` 这个名字指到这页**。

**被本页的结论直接推出的两页**：

- [[dc-result-accessor]] — 文档点名：BADC 的 pin 结果**必须**用它上传（`must be uploaded using the DC_RESULT_ACCESSOR API`）。
- [[dc-test-programming]]（**未读**）— 本页 `.add()` 收的那几个对象（`PPMU_SETTING` 一族）属于
  DC 测试编程那一族；**那页讲什么本页没有依据，只按对象族指路**。

**同类/相邻（本页的 `## Related information` 一行里列出的）**：`SPMU_TASK`、`FLEX_RELAY`
（→ [[flex-relay]]）、`PS1600 DC value measurements`、`BADC_PIN_MEASURE` / `BADC_PIN_SETTING` /
`BADC_SETTING` / `BADC_MEASURE`——**这些名字里只有 `FLEX_RELAY` 在
`extract/prose-allowlist.txt` 里**，其余一律反引号。
**注意 `SPMU_TASK` 不是 [[spmu-pin-task-mode]]**：后者是「SPMU 的 pin 工作模式」，
**本页没有依据说两者是同一个东西**。

**对账时发现的一件事**：[[mapping-pattern]] 的主表 **17 行里没有 PATTERN_CONTROLLER 这一行**，
它的 `related:` 也没有本页。**「从 pattern 里跑 DC 测试」这个目的，那张三层对照表没有覆盖**
——这是那张表的一个缺口，不是本页的缺口。

**上游/下游**：上游是测试方法里那一族测量对象的配置（[[testmethod]] 段）；
下游是 `TEST()` 落结果（[[results]] 段）。本页**只占中间那一段**。

## 版本

**本文档有 `## Functional changes` 段，只有一条**：

- **Introduced before SmarTest 6.3.2**

**这是 §11.2 ② 那个哨兵值，不是「6.3.2 新增了 PATTERN_CONTROLLER」。**
`before` 的意思是「**在本文档集覆盖范围开始之前就已经有了**」——
**照字面读会读出一条格式齐整的假信息**。**本页照原样记，不加解释性日期。**
除这一条之外，本篇没有别的版本条目。

## 出处

`sources:` 一篇：
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.142_PATTERN_CONTROLLER.md`
（TDC `71357.htm`，249 行 / 13,417 字节）。**整篇读完**。

**本页没做的**：

- **子主题 `02.07.04.01.142.01_PATTERN.md` 没读。** 所以：`PATTERN` 类**自己**有哪些成员函数、
  `add()` 收的参数类型、`PATTERN` 的构造与生命期——**本页一个字都没有**。
  本页只在「`label()` 返回它」这个粒度上说它。
- **概念篇 `02.07.03.02.07_Executing_PPMU_tests_from_a_pattern.md` 没读**
  （正文第一句就把它指为「概念信息在这里」）。
- **`02.07.03.02.06.03_Managing_DC_Tests_with_Variable_Parameters.md` 没读**，
  所以「变量参数怎么配合 `setup()`」的细节本页没有。
- **`02.07.03.02.06.01_DC_set_management.md` 没读**，所以那句
  `the fall-back mechanism that is used for standard DC tests` **具体是什么机制，本页答不了**。
- **`DC_RESULT_ACCESSOR`（`02.07.04.01.28`）的原文没读**，只读了本篇点名它的那一句。
- **BADC 一族（`.08` / `.08.01` / `.09` / `.09.01`）、`SPMU_TASK`（`.234`）、
  `FLEX_RELAY`（`.68`）、PS1600 那篇**——一篇没读，全部只在本篇的链接里出现过。
- **`Per pin on pass` / `Per pin on fail` 两个 flag 的原文没读**
  （本篇链到 `02.08.04.32.01.02.07.01_Alphabetical_list_of_flags.md`）。
- **一张图都没看——因为这一篇里没有图。** 实测：本篇全文 **0 处** `raw/`、
  **0 处** `.png` / `.jpg`。**所以本页没有任何来自图的结论**；**这不是「图够不着」，
  是这一篇里根本没有图**（§11.4：没看图就写「本页没用图」——那才是真的；理由不许编）。
- **没有实跑。** 没有在任何机台上跑过本 API、没有建过子程序、没有验过那条耗时公式。
  `verified: doc-only` 指的就是这件事。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
> **① 编码坏字 `渭` = `µ`，4 处**（第 30 / 31 / 34 / 36 行），全部落在微秒数上：
> `twait = (25 渭s + N * 4 渭s)`、`25 渭s is a one-time overhead`、`20 渭s * N`、`60 渭s`。
> **处置照 §11.2 ①：页面原样转录**——**拿 `µs` 去 raw 里搜是搜不到的，要搜坏掉的 `渭`**。
> **② 两处语法失手，都在参数表里**：`the DC test will executes in the same way as the mode TM::PPF`
> 与 `the DC test will executes in the same way as the mode TM::GPF`——**`will executes` 重复了助动词**。
> **③ `In additional, an extra wait time of, at least, 60 渭s must be added`**——
> 照字面读不通（`In additional` 不成立），本页**只引不改**。
> **④ `The subpattern for which the DC task are to be specified.`**——`task` 与 `are` 数不一致
> （同句后一半 `Note that the subpattern must already exist.` 是对的）。
> **⑤ 本页未发现 `DC/DC power units`（§11.2 ⑤ 那族整词替换）。** 实测本篇 0 命中。
> **但这是「本页读到的」，不是「本篇干净」**（§13.1 第 ⑥′）。

`verified: doc-only`
