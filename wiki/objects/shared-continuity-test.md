---
type: object
title: SHARED_CONTINUITY_TEST
layer: n/a
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.21_SHARED_CONTINUITY_TEST.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# SHARED_CONTINUITY_TEST

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」节是脚本逐字抽的（§4），**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **3,653 字符逐字取自** `<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.21_SHARED_CONTINUITY_TEST.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Examples

### Note

The following examples demonstrate how to use this API within a test method. If you want to see a complete test method code via SHARED_CONTNUITY_TEST, find it in /opt/93000mts/mts/solution_tools/common/sh_lib/DriverSharing.tar.gz.

### Example 1

Performing the continuity and short circuits test for the shared, and non-shared pins.

```
#include "solution_tools.h"
#include "testmethod.hpp"
#include "mapi.hpp"

class CSharedContinuity: public testmethod::TestMethod
{
protected:
  virtual void run()
  {
    ON_FIRST_INVOCATION_BEGIN();
    {
      // Always do initialization at the beginning of test
      mTest.init();

      // hand over the parameters to the test class
        mTest.pinNonShared("DQ_Bus,DQS_DiffBus,DM")
             .forceCurrentNonShared(100 uA)
             .pinCross("Clock_Bus")
             .forceCurrentCross(100 uA)
             .sharingConfigFile("default.cfg")
             .pinShared("Addr_Bus,Command_Bus")
             .forceVoltage(1.1)
             .terminationDPS("VTERM")
             .supplyDPS("VDD,VDDQ")
             .settlingTime(0)
             .output(MTP::OUTPUT_REPORT_UI);

      // execute the test
      mTest.execute();
    }
    ON_FIRST_INVOCATION_END();

    // set result
    mTest.judgeAndLog();

    // Print out in the UI Report Window.
    mTest.print();
  }

private:
  SHARED_CONTINUITY_TEST mTest;
};
```

### Example 2

Customizing the output.

```
#include "solution_tools.h"
#include "testmethod.hpp"
#include "mapi.hpp"

class CSharedContinuity: public testmethod::TestMethod
{
protected:
    virtual void run()
    {
      ON_FIRST_INVOCATION_BEGIN();
      {
        // Always do initialization at the beginning of test
        mTest.init();

        // hand over the parameters to the test class
        mTest.pinNonShared("DQ_Bus,DQS_DiffBus,DM")
             .forceCurrentNonShared(100 uA)
             .pinCross("Clock_Bus")
             .forceCurrentCross(100 uA)
             .sharingConfigFile("default.cfg")
             .pinShared("Addr_Bus,Command_Bus")
             .forceVoltage(1.1)
             .terminationDPS("VTERM")
             .supplyDPS("VDD,VDDQ")
             .settlingTime(0)
             .output(MTP::OUTPUT_REPORT_UI);

        // execute the test
        mTest.execute();
      }
      ON_FIRST_INVOCATION_END();

      // set result
      mTest.judgeAndLog();

      // Print out in the UI Report Window.
      STRING_VECTOR pinSharedNames =
        PinUtility.getDigitalPinNamesFromPinList("Addr_Bus,Command_Bus", TM::ALL_DIGITAL, TRUE);
      STRING_VECTOR pinNonSharedNames =
        PinUtility.getDigitalPinNamesFromPinList("DQ_Bus,DQS_DiffBus,DM", TM::ALL_DIGITAL, TRUE);
      STRING_VECTOR pinCrossNames =
        PinUtility.getDigitalPinNamesFromPinList("Clock_Bus", TM::ALL_DIGITAL, TRUE);

      cout << "Test result of site " << CURRENT_SITE_NUMBER() << ": " << mTest.getPassFail() << endl;

      for (STRING_VECTOR::const_iterator it = pinSharedNames.begin();
           it != pinSharedNames.end(); ++it)
      {
        cout << "PIN (" << *it << ")\t" << mTest.getPassFail(*it) << "\t" << mTest.getValue(*it) << endl;
      }

      for (STRING_VECTOR::const_iterator it = pinNonSharedNames.begin();
           it != pinNonSharedNames.end(); ++it)
      {
        cout << "PIN (" << *it << ")\t" << mTest.getPassFail(*it) << "\t" << mTest.getValue(*it) << endl;
      }

      for (STRING_VECTOR::const_iterator it = pinCrossNames.begin();
           it != pinCrossNames.end(); ++it)
      {
        cout << "PIN (" << *it << ")\t" << mTest.getPassFail(*it) << "\t" << mTest.getValue(*it) << endl;
      }
    }

private:
    SHARED_CONTINUITY_TEST mTest;
};
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
