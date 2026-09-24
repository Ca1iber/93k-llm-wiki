---
type: object
title: Match loops
layer: L1
stage: testmethod
tags: [testmethod, l1, match-loop, counted-match-loop, timed-match-loop, fast-sync, multi-site, error-map, sequencer, pattern]
related: [testmethod, error-map, sequencer, stme, sqst, ps5000, controlling-multiple-sites, alphabetical-list-of-flags, technology-file-for-a-device, smartest-6.3.2, smartest-7.4.0]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.08.04.03_Match_loops.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# Match loops

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **4,433 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.07.01.08.04.03_Match_loops.md>` 及其子主题 `<02_System_reference/02.06_Command_Reference/02.06.07.01.08.04.03.01_Counted_match_loops.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.01.08.04.03.02_Timed_match_loop.md>`、`<02_System_reference/02.06_Command_Reference/02.06.07.01.08.04.03.03.01_How_to_use_Fast_Sync.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Counted match loops）

The following is a simple example of a counted match loop:

```
SQPG 3,MACT,256,CONTINUE,,(@)
SQPG 4,GENV,5,,,(@)
SQPG 5,MRPT,5,,,(@)
```

Note that only the GENV or RPTV instruction is allowed immediately before the MACT instruction. CONTINUE, which is optional, tells SmarTest to continue the surrounding test even if the match loop failed.

### Example（取自子主题 Timed match loop）

The following listing illustrates a timed match loop:

```
SQPG 11,WTER,,,,(@)
SQPG 12,MBGN,,,,(@)
SQPG 13,GENV,2,,,(@)
SQPG 14,WTER,,,,(@)
SQPG 15,MJPE,,,,(@)
SQPG 16,MEND,,,,(@)
```

### Example 2: Define the max number of match ports on a test processor（取自子主题 Fast Sync › How to use Fast Sync）

```
class SetNife: public testmethod::TestMethod
{
public:
    Boolean firstRun;

protected:
    int mErrorProb;

    virtual void initialize()
    {
        addParameter("errorProb", "int", &mErrorProb, testmethod::TM_PARAMETER_INPUT)
                   .setDefault("0");

        firstRun = true;
    }

    virtual void run()
    {
        if (firstRun)
        {
            ON_FIRST_INVOCATION_BEGIN();

                DISCONNECT();

                if ( mErrorProb < 1 || mErrorProb > 8 )
                {
                    cout << "NIFE not set!!!" << endl;
                }
                else
                {
                    char buf[1000];

                    sprintf (buf, "SQST OFF\nNIFE %i\n", mErrorProb);

                    FW_TASK(buf);
                }

            ON_FIRST_INVOCATION_END();

            firstRun = false;
        }

        return;

    } // virtual void run()
...
...
};
REGISTER_TESTMETHOD(...);
```

### Example 3: Use the Fast Sync feature for blocking functional test（取自子主题 Fast Sync › How to use Fast Sync）

```
class BlockingFuncTest: public testmethod::TestMethod
{
protected:

    int mFast;

    virtual void initialize()
    {
        addParameter("fast", "int", &mFast, testmethod::TM_PARAMETER_INPUT)
                   .setDefault("1");
    }

    virtual void run()
    {
        static STRING tsName;
        static STRING lblName;

        ON_FIRST_INVOCATION_BEGIN();

            GET_TESTSUITE_NAME(tsName);

            lblName = Primary.getLabel();

            CONNECT();

            mFast?FW_TASK("STME FAST,\n"):FW_TASK("STME ON,\n");

            FUNCTIONAL_TEST();

            FW_TASK("STME OFF,\n");

        ON_FIRST_INVOCATION_END();

        Boolean res = GET_FUNCTIONAL_RESULT();

        TEST(tsName, lblName, res?TM::Pass:TM::Fail,true);

        return;

    } // virtual void run()
...
...
};
REGISTER_TESTMETHOD(...);
```

### Example 4: Use the Fast Sync feature for non-blocking functional test（取自子主题 Fast Sync › How to use Fast Sync）

```
class NonBlockingFuncTest: public testmethod::TestMethod
{
protected:

    int mFast;

    virtual void initialize()
    {
        addParameter("fast", "int", &mFast, testmethod::TM_PARAMETER_INPUT)
                   .setDefault("1");
    }

    virtual void run()
    {
        static STRING tsName;
        static STRING lblName;

        ON_FIRST_INVOCATION_BEGIN();

            GET_TESTSUITE_NAME(tsName);

            lblName = Primary.getLabel();

            CONNECT();

            mFast?FW_TASK("STME FAST,\n"):FW_TASK("STME ON,\n");

            START_TEST();

            WAIT_TEST_DONE(TM::WAIT_DIGITAL);

            FW_TASK("STME OFF,\n");

       ON_FIRST_INVOCATION_END();

       Boolean res = GET_FUNCTIONAL_RESULT();

       TEST(tsName, lblName, res?TM::Pass:TM::Fail,true);

        return;

    } // virtual void run()
...
...
};
REGISTER_TESTMETHOD(...);
```

### Example 5: Use the Fast Sync feature for Independent Sequencer Run on the Smart Scale cards（取自子主题 Fast Sync › How to use Fast Sync）

```
class IndependentSequencerRuns: public testmethod::TestMethod
{
protected:

    int mFast;

    virtual void initialize()
    {
            addParameter("fast", "int", &mFast, testmethod::TM_PARAMETER_INPUT)
                        .setDefault("1");
    }

    virtual void run()
    {
        static STRING tsName;
        static STRING lblName;

        ON_FIRST_INVOCATION_BEGIN();

            GET_TESTSUITE_NAME(tsName);

            lblName = Primary.getLabel();

            CONNECT();

            SEQUENCER_CONTEXT_ITEM s1("matchCt");
            SEQUENCER_CONTEXT_ITEM s2("otherCt");

            s1.setPorts("match");
            s2.setPorts("other");

            SEQUENCER_CONTEXT seqCon;

            seqCon.add(s1).add(s2).apply();

            mFast?FW_TASK("STME FAST,\n"):FW_TASK("STME ON,\n");

            START_TEST("matchCt");
            FUNCTIONAL_TEST("otherCt");
            WAIT_TEST_DONE(TM::WAIT_DIGITAL,"matchCt");

            FW_TASK("STME OFF,\n");

        ON_FIRST_INVOCATION_END();

        Boolean res = GET_FUNCTIONAL_RESULT("match");

        TEST(tsName, lblName, res?TM::Pass:TM::Fail,true);

        return;

    } // virtual void run()
...
...
};
REGISTER_TESTMETHOD(...);
```

<!-- 语法节 end -->

## 是什么

**match loop（匹配循环）是 sequencer 指令层的一层控制：把一段向量反复执行，
直到 DUT 的输出「匹配」上期望值为止。** 要解决的问题很具体——**没有复位 pin 的 DUT**：

> 「Match loops are used to put a DUT without a reset pin into a state required for some test. The general principle is to specify a sequence of vectors that are executed in a loop and, if repeated often enough, put the DUT successively into each of its possible states. After each repetition, it is checked if the desired state has been reached. If so, the loop is terminated. If not, it is repeated.」

**四步循环**：跑一段向量 → 检查状态 → 到了就停 → 没到就再来一遍。
**「successively into each of its possible states」是它的前提假设**——
重复得够多，DUT 就会把所有可能状态走一遍，其中一个是你要的。

### 为什么必须补 dummy vector（**这是机制的核心，也是最容易漏的一条**）

> 「A certain time is required for evaluating the compare result and to propagate it to the error flag that controls the repetition of the loop. To provide this time span, a number of dummy vectors without compare actions must be generated after the functional vectors before the end of the match loop.」

**即：比较结果要传回那个「控制是否再循环」的 error flag，是需要时间的。**
**这段时间用「不含比较动作的 dummy vector」填出来**——**不是可选的装饰，是机制要求。**
**两种风格（下面）在这件事上的做法不一样**，这正是它们的第一条差别。

### 那个 error flag 还兼一个别的用途

> 「Note This error flag is also used for conditional subroutine calls, see SVEC subroutines.」

（原文 `Note` 后**没有冒号**；`SVEC subroutines` 在 raw 里是一个链接，
指向 `02.06.07.01.08.05.02_SVEC_subroutines.md`，**本页没读**。）

### 两种风格：**旧的那一种只为兼容而存在**（本页最该记住的一句）

> 「SmarTest provides two styles of match loops. They differ in two respects, first in the way the dummy vectors are generated, and second in their termination mechanism. The older type is only supported for compatibility reasons. For new applications, you should use the new style Counted match loops.」

**两条差别**：① dummy vector 怎么产生；② 怎么终止。
**原文明确说新应用要用新的那一种**（`Counted match loops`），
**旧的那一种只为了兼容而保留**。
（推断）**两种风格就是 `Counted match loops`（新）与 `Timed match loop`（旧）**——
依据是原文只写了「两种风格」、把新的那种点名成 `Counted match loops`，
**以及本篇 `Subtopics` 底下正好挂着这两篇加一篇 `Fast Sync`**（见「出处」）。

### 两种终止机制：超时 与 超次数

> 「Finally, there is a mechanism that terminates the loop if the desired state has not been reached after a certain time (timed match loop) or a certain number of repetitions (counted match loop). In this case, the whole test will fail by default (this can be changed for counted match loops).」

| 风格 | 谁来终止 | 到点了会怎样 |
|---|---|---|
| **timed match loop** | **一个时间**（`after a certain time`） | **整个测试失败**（默认） |
| **counted match loop** | **一个次数**（`a certain number of repetitions`） | **整个测试失败**——**但这一种可以改成继续**（`this can be changed for counted match loops`） |

**「默认失败、counted 可以改成继续」这一条是两种风格唯一一处行为差异**，
**它就是 counted 那一篇里 `CONTINUE` 选项的来处**（见下）。

### 匹配循环的结果**不进 error map**

> 「Note that the results of the match loop cycles are not recorded in the error map. They contribute to the general outcome of the test only insofar as the test will fail if no match can be established.」

**两层意思**：① **循环体内的周期结果不记进 error map**；
② 它对总结果**唯一的贡献**是「匹配不上就判失败」。→ [[error-map]]。

### 多站（multi-site）要特别小心

> 「Match loops require special care in a multi-site test. For details see Controlling the site match function.」

**原文只说了「要小心」，细节整句推给另一篇**（`Controlling the site match function`，
raw: `02.06.03.01.10.04`，**本页没读**）→ 见 [[controlling-multiple-sites]] 那一行说明。

### 三种风格的具体做法（三篇子主题里的内容）

> 下面三小节的依据是**本篇 `Subtopics` 挂的三篇**（`.01 Counted match loops`、`.02 Timed match loop`、
> `.03 Fast Sync` 及其 `.03.01 How to use Fast Sync`），**它们不在本页 frontmatter 的 `sources:` 里**。
> **每小节都写明句子出自哪一篇**；本页没有从这四篇之外引入任何内容。

#### Counted match loops（新的那一种）

**与 timed 的差别，原文列了两条**：

> 「Counted match loops differ from timed match loops in the following respects:」

- 「You can specify the maximum number of unsuccessful repetitions. If this number is exceeded, the match loop is terminated, and the surrounding test fails, unless you explicitly specify the test to continue.」
- 「For the evaluation of the error flag, you must specify the dummy vector(s) without compare actions explicitly:」

**第二条底下还有五个子项**（原文如此），里面三个数值得记：

- 「Minimum one dummy vector must be specified.」
- 「You do not have to adjust the number of dummy vectors to the exact time required for setting the error flag; the system repeats the specified dummy vector(s) as often as required.」
- 「The total number of executed dummy vectors for the required delay time is typically in the range from some hundred to more than 1000 vectors.」

**结构是「两个循环」**：`There are two loops, the main loop and the wait loop. The body of the main loop executes the compare vectors once, and then the wait loop.`

**指令序列**（原文）：

> 「A counted match loop is started with the MACT instruction. This instruction specifies the maximum number of unsuccessful repetitions for the main loop. The CONTINUE option specifies to carry on with the test even if all repetitions of the match loop failed. Then the compare vectors must be specified with a GENV or RPTV instruction (an exception is when using Nested match loops, in which case you may insert the MACT or MRPT instruction here). These must be followed by the MRPT instruction, which defines the number of dummy vectors to be repeated in the wait loop. You can specify more than one dummy vector if the total number of cycles within the match loop must be a multiple of a number greater than 1.」

**例（脚本已逐字收进本页「语法 / 参数」节）**：

```
SQPG 3,MACT,256,CONTINUE,,(@)
SQPG 4,GENV,5,,,(@)
SQPG 5,MRPT,5,,,(@)
```

原文对这三行的说明是：
`Note that only the GENV or RPTV instruction is allowed immediately before the MACT instruction. CONTINUE, which is optional, tells SmarTest to continue the surrounding test even if the match loop failed.`
（**那句 `immediately before the MACT instruction` 的措辞本页存疑**，见 `## 出处` ⚠️⑥。）

**两个查询**（原文点名，`02.06.02.02` 那一章的命令）：

- `CHFA?` ——「This query returns the result of the last match loop cycle for selected pins.」
- `MCNT?` ——「This query returns the number of match loop passes that were needed to satisfy the match condition.」

**两条硬约束，值得单列**：

- **重建测试结果要求 8 的倍数**：「If a pattern contains more than one match loop, a full reconstruction of the test results is only possible if the number of cycles created by the loops is always a multiple of 8. This is required for the cycles generated within the match loop body as well as for the cycles generated with MRPT. For MRPT this can be ensured by specifying 8 vectors for this instruction.」
- **Pin Scale 5000 上另有四条**（原文：`For the Pin Scale 5000 card, the pattern containing the match loop must meet the following criteria:`）：
  「The start position of the match loop must be a multiple of 8 cycles.」/
  「The number of cycles within the match loop must be a multiple of 8.」/
  「There must not be any instructions to generate break cycles within the match loop.」/
  「There must not be a conditional branch instruction within the match loop.」
  违反时的绕法原文也给了：把 `.technology file` 里的
  `check_exa_scale_seq_restrictions` 设成 `off`——「However, the result for each cycle after the match loop may not be acquired correctly.」

#### Timed match loop（旧的那一种）

> 「The WTER (WaiT on ERror) and MBGN (Match BeGiN) instructions start a match loop. Vectors are executed in a continuous loop, until the DUT outputs match the expected data. The WTER, MJPE (Match JumP on Error) and MEND (Match END) instructions complete the match loop.」

**起停各三条指令，名字里带缩写展开**：`WTER` = WaiT on ERror、`MBGN` = Match BeGiN、
`MJPE` = Match JumP on Error、`MEND` = Match END。

**dummy vector 是自动生成的**（这是它和 counted 的第一条差别）：

> 「The break vectors are generated automatically. Note that the error map does not record data during a match loop. If your DUT outputs do not match the required condition, you can break the sequence by using the BRK parameter of the SQST command, see SQST, SQST? - (SeQuencer STate). In this case, the last loop in your sequence is recorded on the error map.」

**超时行为（本篇唯一给了数的地方）**：

> 「If a match is not found within 900 seconds (default value), a SmarTest Work Center is called and the sequencer enters the break state. You can set the SmarTest Work Center period yourself using the SQTO (SeQuencer TimeOut) command. Note that in a multi-site setting, SmarTest cannot determine on which site the SmarTest Work Center occurred. It will declare all sites as failed.」

**三个要点**：默认 **900 秒**；**multi-site 下无法判断发生在哪个 site，会把所有 site 判失败**；
超时时间可以用 `SQTO` 命令改（`SQTO` 在 raw 里**没有链接**）。

#### Fast Sync（7.4.0 起）

> 「Serial interfaces on many DUTs require non-deterministic handling. Normally they consist of a small number of pins (1, 2 or 4). Fast Sync enables the local synchronization of the test processor (TP). It enables up to 8 sync ports reacting independently on non-deterministic DUT responses per test processor.」

- **支持范围**：`The feature is supported for all Smart Scale cards.`
- **它省掉的是什么**：「Each test processor supports from 1 to 8 local synchronization, which can be applied in parallel on all the test processors. Therefore, for Match loops and conditional jumps, it eliminates the overhead caused by site scaling synchronization.」
- **拓扑前提**（原文是 `Note`）：`For pins of a DUT belonging to a match loop, they need to be located on the same test processor. For best throughput, try to minimize the number of independent match loops on a test processor.`
  —— **同一条前提在 `How to use Fast Sync` 的 `Before you begin` 里也写了一遍**，
  **但那里把 `match` 写成了 `mach`**（见 `## 出处` ⚠️③）。
- **规模**：`Instead of 255 sites only, Fast Sync enables non-deterministic device handling for massive multisites (1024 sites).`

## 典型用法

**先说范围**：**本页的 `sources`（父篇）没有 `## Procedure`，也没有 `## Before you begin`。**
`Before you begin` 与 `Procedure` **只出现在子主题 `How to use Fast Sync` 里**，
所以下面第 3 点那套步骤**只适用于 Fast Sync**，不是 match loop 的通用流程。

**1. counted match loop：三条 `SQPG` 一个循环**

顺序是**固定的三件**（原文：`A counted match loop is started with the MACT instruction`）：

| 步 | 指令 | 给什么 | 原文要点 |
|---|---|---|---|
| 1 | `MACT` | **最大失败重复次数** | 「specifies the maximum number of unsuccessful repetitions for the main loop」；可选加 `CONTINUE` = 失败也继续跑外层测试 |
| 2 | `GENV` 或 `RPTV` | **比较向量** | **只有这两个能紧接在 `MACT` 之后**（`Nested match loops` 是原文给的例外） |
| 3 | `MRPT` | **wait loop 里重复的 dummy vector 数** | **至少 1 个**；要凑 8 的倍数时可以给多个 |

**语法节里的例子就是**：`MACT,256,CONTINUE` → `GENV,5` → `MRPT,5`。

**2. timed match loop：四条指令夹住循环体**

语法节里的例子是 `WTER` → `MBGN` → `GENV` → `WTER` → `MJPE` → `MEND`，
**dummy vector 不用自己给**（原文：`The break vectors are generated automatically.`）。

**要中途打断它**：用 `SQST` 的 `BRK` 参数——**原文说这样「序列里最后一个循环会被记进 error map」**
（`In this case, the last loop in your sequence is recorded on the error map.`），
**这是 error map 里唯一能看到匹配循环痕迹的情形**。

**3. Fast Sync 的步骤（十条，原文 `## Procedure` 逐条）**

`## Before you begin` 两条前提：
`Make sure you are using SmarTest 7.4.0 or later versions.`
与 `Make sure the device pins, which belong to a mach loop, are located on the same test processor. For best throughput, minimize the number of independent match loops on a test processor.`

| 步 | 原文 |
|---|---|
| 1 | 「According to the steps described in `Multiport operation`, define a port or ports for the Fast Sync pins and ports for other pins.」 |
| 2 | 「Define levels as usual.」 |
| 3 | 「Set up the a `multiport timing`.」（**原文这里有 `the a` 这个重复词**，见 `## 出处` ⚠️⑤） |
| 4 | 「Create a `multiport timing specification`.」 |
| 5 | 「Define a clock group for the fast sync port as shown in `Example 1: Multiport timing`.」 |
| 6 | 「Refer to `Creating a multiport burst` to set up the pattern.」 |
| 7 | 「In the Flow Data Editor, on the Flags tab, set the `site_match_mode` testflow flag to off.」 |
| 8 | 「On the Test Suites tab, choose each test suite, and in the opened Properties view, under the Site Control section, set the `Site Match` flag to OFF.」 |
| 9 | 「Define the max number of match ports on a test processor using the commands `SQST, SQST? - (SeQuencer STate)` and `NIFE, NIFE? - (Number of Independent Fast Error)` in `disconnected` mode. For a test method example, refer to `Example 2: Define the max number of match ports on a test processor` below.」 |
| 10 | 「In the test method, use the `STME FAST` firmware command to enable the Fast Sync feature.」 |

（**上表 10 行**——原文 `## Procedure` 的项目符号数就是 10 个，
**本页按原始行数逐条列出，没有合并也没有删**。）

`## Results` 只有一句：`The overhead for site scaling synchronization is significantly reduced.`

**例子**：`Example 1` 是一张图（**本页没看**）；`Example 2` 到 `Example 5` 是四段 testmethod 的 C++ 代码，
**脚本已经逐字收进本页「语法 / 参数」节**。四段各自回答一个场景：

| 例子 | 场景（原文标题） |
|---|---|
| `Example 2` | `Define the max number of match ports on a test processor`——用 `SQST OFF` + `NIFE %i` 两条 firmware 命令设上限 |
| `Example 3` | `Use the Fast Sync feature for blocking functional test`——`FUNCTIONAL_TEST()` 阻塞式 |
| `Example 4` | `Use the Fast Sync feature for non-blocking functional test`——`START_TEST()` + `WAIT_TEST_DONE(TM::WAIT_DIGITAL)` |
| `Example 5` | `Use the Fast Sync feature for Independent Sequencer Run on the Smart Scale cards`——`SEQUENCER_CONTEXT` 起两路独立 sequencer |

**四段共用的骨架**：`ON_FIRST_INVOCATION_BEGIN()` 里先 `CONNECT()`，
再按 `mFast` 选 `FW_TASK("STME FAST,\n")` 或 `FW_TASK("STME ON,\n")`，
跑完 `FW_TASK("STME OFF,\n")`，最后取 `GET_FUNCTIONAL_RESULT()` 的结果、调 `TEST` 判 pass/fail。

**4. 顺序上的三条硬约束（跨风格，都是文档事实）**

- **`MACT` 之前只许 `GENV` 或 `RPTV`**（counted）。
- **`MACT` / `MRPT` / `GENV` / `RPTV` 这些指令属于 `SQPG` 编程**——
  语法节里每个例子都用 `SQPG` 开头的那种行来写（`SQPG 3,MACT,256,CONTINUE,,(@)` 这种形状）。
  **`SQPG` 那一篇本页没读**（见 `## 出处`）。
- **多站下会有一堆额外前提**（同 test processor、8 的倍数、不能有 break/条件分支），
  **动手前照上面那两张表逐条核**。

## 和谁有关

| 页 | 是什么关系 | 依据 |
|---|---|---|
| [[testmethod]] | **本页 `stage: testmethod` 的理由**（frontmatter）；**Fast Sync 那四段例子全是 `testmethod::TestMethod` 派生类** | frontmatter + 语法节里 `Example 2`–`Example 5` |
| [[error-map]] | **匹配循环的周期结果不进它**；唯一例外是用 `SQST` 的 `BRK` 打断时 | 父篇正文 + `Timed match loop` |
| [[sequencer]] | **上位概念**：`MACT` / `MRPT` / `GENV` / `RPTV` / `WTER` / `MBGN` / `MJPE` / `MEND` 都是 sequencer 指令 | 父篇与两篇子主题用例 |
| [[stme]] | **开关 Fast Sync 的命令**：`STME FAST`（子主题点名） | `How to use Fast Sync` 的 `## Procedure` 与四段例子 |
| [[sqst]] | **两个用处**：① `SQST` 的 `BRK` 参数打断 timed 循环；② 用 `SQST OFF` + `NIFE` 设每 TP 的最大匹配端口数 | `Timed match loop` + `How to use Fast Sync` |
| [[ps5000]] | **卡片限制的载体**：Pin Scale 5000 上那四条 pattern 约束 | `Counted match loops` |
| [[technology-file-for-a-device]] | **绕开条件的开关**：`check_exa_scale_seq_restrictions` 设成 `off` | `Counted match loops` |
| [[alphabetical-list-of-flags]] | **两个要关掉的 flag**：`site_match_mode` 与 `Site Match` | `How to use Fast Sync` 的 `## Procedure` 第 7、8 步 |
| [[controlling-multiple-sites]] | **多站注意事项的去处**：父篇把 `Controlling the site match function` 整句推给那一篇——（推断）**本 wiki 这一页与那篇同名，但本页没有去核它们是不是同一篇** | 父篇正文；`Controlling the site match function`（raw: `02.06.03.01.10.04`）**未读** |
| [[smartest-6.3.2]] | **版本页**：四篇里的哨兵值都落在它身上 | 四篇的 `## Functional changes` |
| [[smartest-7.4.0]] | **版本页**：Fast Sync 与 `CONTINUE` 两条变更落在它身上 | 父篇与三篇子主题的 `## Functional changes` |
| [[connect]] / [[disconnect]] / [[fw-task]] / [[get-functional-result]] / [[on-first-invocation-begin]] / [[on-first-invocation-end]] / [[test]] | **Fast Sync 四段例子里调用的 API**——**本页只从例子里看到名字，没有它们各自的说明** | 语法节里 `Example 2`–`Example 5` |
| `SQPG, SQPG? - (SeQuencer ProGramming)`（raw: `02.06.02.02.237`） | **所有例子的书写形式**；**未读** | 四篇的例子里都是 `SQPG` 行 |
| `CHFA?` / `MCNT?` / `EPRC?` / `SQTO` / `NIFE` / `MACT` / `MRPT` / `GENV` / `RPTV` / `WTER` / `MBGN` / `MJPE` / `MEND` / `BRK`（**均未建，不链**） | 这些名字在四篇里出现，**但大半没有链接、也没有各自的说明** | 父篇与三篇子主题 |
| `SVEC subroutines`（raw: `02.06.07.01.08.05.02`） | **error flag 的另一个用途**；**未读** | 父篇那句 `Note` |
| `Nested match loops`（raw: `03.02.05.02.07`） | **`MACT` 之前那条限制的唯一例外**；**未读** | `Counted match loops` |
| `SmartLoop` / `Multiport operation` / `multiport timing` / `Creating a multiport burst` / `Sequencing groups and pattern structure`（**均未读、不链**） | Fast Sync 步骤与多端口限制的去处 | `How to use Fast Sync` 与 `Counted match loops` |
| `Counted match loops` / `Timed match loop` / `Fast Sync` / `How to use Fast Sync`（`02.06.07.01.08.04.03.01` / `.02` / `.03` / `.03.01`） | **本页的三个子主题**（父篇 `Subtopics` 挂的三篇 + 其中一篇的子主题）。**本页没给它们单独建页**；它们的语法已被脚本收进本页「语法 / 参数」节 | 父篇 `Subtopics` 与语法节的段名后缀 |

**本页没有引用 `edges.jsonl` 的入边/出边数字**（没读边数据，故不报条数）。

## 版本

**本页读了四篇文档，四篇都有自己的 `## Functional changes` 段，逐条转录如下。**

**父篇（`Match loops`）两条**：

- `Introduced before SmarTest 6.3.2`
- `SmarTest 7.4.0: New feature Fast Sync.`

**子主题 `Counted match loops` 两条**：

- `Introduced before SmarTest 6.3.2`
- `SmarTest 7.1.4: Option for MACT instruction: CONTINUE`

**子主题 `Timed match loop` 一条**：

- `Introduced before SmarTest 6.3.2`

**子主题 `Fast Sync` 一条 / `How to use Fast Sync` 一条**（两篇写的是同一句）：

- `Introduced in SmarTest 7.4.0`

**读法四条：**

- **`Introduced before SmarTest 6.3.2` 是哨兵值**（§11.2 ②）：
  意思是「**在本文档集覆盖范围开始之前就已经有了**」，
  **不是「6.3.2 新增了 match loop / counted match loop / timed match loop」**。
  四篇里有三篇写它。照字面读会生成三条假信息，而格式齐整。
- **Fast Sync 那两篇写的是 `Introduced in`（不是 `before`）**——
  **那才是真正的「7.4.0 新增」**。两条与父篇的
  `SmarTest 7.4.0: New feature Fast Sync.` **对得上**。
- **`CONTINUE` 这个选项是 7.1.4 加的**，不是 counted match loop 一开始就有的。
- **本 wiki 面向 7.10.3**，在 `6.3.2` / `7.1.4` / `7.4.0` 三个门槛之后，
  **所以这几样在这一版上都有**——（推断）**依据是版本号大小，不是机台核对**。

版本页：[[smartest-6.3.2]]、[[smartest-7.1.4]]、[[smartest-7.4.0]]。

## 出处

**本页的 `sources:` 只有一篇**：
`02_System_reference/02.06_Command_Reference/02.06.07.01.08.04.03_Match_loops.md`
（TDC `10563.htm`；**2,579 字节 / 35 行**，全文 CRLF，末行带换行。**整篇读完。**）

**另外四篇也读了，它们不在 `sources:` 里**——**这一点必须写明，否则读者不知道本页正文里
那三小节的依据从哪来**：它们是父篇自己 `Subtopics` 一节挂的子主题，
而**骨架的「语法 / 参数」节已经把它们引进来当语法来源**（段名里带「取自子主题（篇名）」那样的后缀）。
本页正文里**每一小节都标了出自哪一篇**，没有第五篇：

| 文件 | TDC | 字节 / 行 | 非 ASCII |
|---|---|---|---|
| `02.06.07.01.08.04.03.01_Counted_match_loops.md` | `96935.htm` | 6,040 / 71 | **3 处**（见 ⚠️②） |
| `02.06.07.01.08.04.03.02_Timed_match_loop.md` | `10568.htm` | 1,649 / 33 | 0 |
| `02.06.07.01.08.04.03.03_Fast_Sync.md` | `150814.htm` | 1,921 / 32 | 0 |
| `02.06.07.01.08.04.03.03.01_How_to_use_Fast_Sync.md` | `150838.htm` | 7,778 / 260 | 0 |

（**行数口径是 `wc -l`（= `splitlines()`），不加 1**，见 §11.5。）

**本页没做的**：

- **父篇 `## Related information` 那三条链接指的就是上面那三篇子主题**（本页读了）。
  **但子主题自己再往下挂的那一篇没读**：`Counted match loops` 的 `#### Subtopics` 底下是
  `Adjusting the junctions between match loop and surrounding label`
  （raw: `02.06.07.01.08.04.03.01.01`）——
  **所以「匹配循环与它外面那个 label 的衔接怎么调」本页一个字都没有。**
  （`Fast Sync` 底下那一篇 `How to use Fast Sync` 读了，见上表。）
- **图两张一张没看**：`Counted match loops` 的 `10564.png`（**main loop + wait loop 的结构图**）
  与 `Timed match loop` 的 `10567.png`（**break vector 插在哪里的图**），
  `Fast Sync` 的 `150828.png`、`How to use Fast Sync` 的 `348946.png` 同样没看。
  **所以「两个循环在时序上怎么排」「break vector 插在哪个位置」「Fast Sync 的结构图长什么样」
  本页一个字都写不出来**——**这与「图够不着」不是一回事**：图在
  `tdc-html/raw/` 下，**本页没有去开**（§11.4）。
- **父篇没有 `## Procedure` / `## Before you begin` / `## Example` / `## Parameters` 段**，
  所以「match loop 的通用操作流程」**本篇根本没有**；
  「典型用法」那一节是本页按三篇子主题拼的，**每一块都标了出处**。
- **四篇里没有一篇给完整的 `SQPG` 语法**：所有例子都是 `SQPG` 开头的那种行，
  **`SQPG` 自己的参数含义（`CONTINUE` 之外那些、`GENV` 的 `5` 是什么意思）本页答不了**。
- **没有实跑。** 没有在任何机台上建过 counted / timed 匹配循环，也没有开过 Fast Sync。
  `verified: doc-only` 指的就是这件事。
- **没有用 `edges.jsonl`**，故不报入边/出边条数。

> ⚠️ **语料瑕疵，逐条照实记下、一处都没替它改**：
>
> ① **父篇 `## Related information` 的三条链接是粘在一起的，中间没有任何分隔符**：
> `[Counted match loops](<02.06.07.01.08.04.03.01_Counted_match_loops.md>)[Timed match loop](<02.06.07.01.08.04.03.02_Timed_match_loop.md>)[Fast Sync](<02.06.07.01.08.04.03.03_Fast_Sync.md>)`
> ——三条之间**没有空格、没有换行、没有逗号**。
> （同一篇的 `Subtopics` 一节用的是**带 `- ` 的列表**，两处写法不一致。）
> **本页照原样引，没替它加分隔符。**
> ② **`Counted match loops` 里的坏字（§11.2 ①）**，`SmartLoop` 那一条逐字是：
> `SmartLoop鈩?setup: See [Executing a pattern鈥慴ased SmartLoop test](<02.06.17.04_Executing_a_pattern__ased_SmartLoop_test.md>).`
> ——两处坏字：**`鈩?`**（三字节字符的第三字节被 `?` 替掉的一族，**不唯一**，
> 落在 `U+2100–U+213F` 区间；**（推断）语境看是 `™`**，
> 因为 `SmartLoop™` 是商标写法，**但按 §11.2 ① 不许当映射用**）、
> **`鈥慴ased`**（= `‑based`，**紧跟的 ASCII 字母 `b` 被一起吃掉**，所以拿 `based` 去搜搜不到）。
> **注意连文件名都带着这个伤**：链接目标是
> `02.06.17.04_Executing_a_pattern__ased_SmartLoop_test.md`（**`pattern` 后面是两个下划线**）。
> **本页照原样转录，没修字、也没改路径。**
> ③ **`How to use Fast Sync` 的 `Before you begin` 里有一个错别字**：
> `Make sure the device pins, which belong to a mach loop, are located on the same test processor.`
> ——**`mach loop` 应为 `match loop`**（同一个意思在 `Fast Sync` 那一篇里写对了：
> `For pins of a DUT belonging to a match loop, they need to be located on the same test processor.`）。
> **本页照原样引，没替它改。**
> ④ **`Fast Sync` 那一篇里 `local synchronization` 用了单数形式**：
> `Each test processor supports from 1 to 8 local synchronization`
> ——同篇前面写的是 `up to 8 sync ports`。**两个说法指同一件事，本页并列，不替它统一。**
> ⑤ **`How to use Fast Sync` 的 `## Procedure` 第 3 步有一个重复词**：
> `Set up the a `multiport timing`.`
> ——**`the a`**。**照原样引。**
> ⑥ **`Counted match loops` 的例子说明里那句限制，本页存疑**：
> `Note that only the GENV or RPTV instruction is allowed immediately before the MACT instruction.`
> ——`MACT` 是**起**这个循环的指令（同篇正文：`A counted match loop is started with the MACT instruction.`），
> **「紧接在 `MACT` 之前」在循环内部是讲不通的**。
> 同篇正文另有一句例外（`an exception is when using Nested match loops`）。
> **本页把三句话并列，不替它裁定标的是「之前」还是「之后」。**
> ⑦ **`Timed match loop` 里两个名字被点名却都没有链接**：
> `SQTO (SeQuencer TimeOut) command` 与 `BRK parameter of the SQST command`
> 里的 `SQTO`；而同一句里 `SQST, SQST? - (SeQuencer STate)` 是带链接的。
> **另外 `a SmarTest Work Center is called` 这句缺一个名词**（像是指某个对话框/提示），
> **本篇没说被「叫出来」的是什么。本页照实记，不补词。**
> ⑧ **`Counted match loops` 与 `Timed match loop` 的 `#### Subtopics` 用的是四级标题**，
> 而各自正文里再也没有别的标题——**父篇也一样**（父篇唯一的标题是 `## Related information`
> 与 `## Functional changes`，子主题列表挂在四级标题下）。**这是语料的结构，不是本页改的。**
> ⑨ **`Fast Sync` 那一篇有一个残句**：
> `Instead of 255 sites only, Fast Sync enables non-deterministic device handling for massive multisites (1024 sites).`
> ——**以 `Instead of` 开头，缺主句**。**照原样引。**
> ⑩ **父篇与 `Timed match loop` 两篇本身没有坏字**（0 处非 ASCII），
> **坏字只在 `Counted match loops` 那一篇里（3 处）**——即上面 ② 那两个形态。
> **「本页量过的」判据只是这四篇**；§11.2 ① 那族在别的篇里大量存在。

`verified: doc-only`——**本页没有在任何真实机台上跑过匹配循环，也没开过 Fast Sync**
（§11：文档里有 ≠ 这台机器上能用；尤其 `MACT` 那条「只许 `GENV`/`RPTV` 紧接」、
8 的倍数要求、以及 Pin Scale 5000 那四条 pattern 约束，**动手前先照实机核对**）。
