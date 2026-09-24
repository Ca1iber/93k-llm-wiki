---
type: object
title: Match loops
layer: L1
stage: testmethod
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.08.04.03_Match_loops.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# Match loops

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」节是脚本逐字抽的（§4），**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

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

（待补）

## 典型用法

（待补）

## 和谁有关

（待补）

## 版本

（待补）

## 出处

（待补）
