---
type: object
title: TESTSET().testname()
layer: L2
stage: results
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244.23_TESTSET__.testname.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# TESTSET().testname()

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」节是脚本逐字抽的（§4），**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,289 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244.23_TESTSET__.testname.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
TESTSET & testname(const STRING &name);
TESTSET & testname(const STRING &name, const bool forceSTDFTestName);
```

 |

Parameter

 |

Description

 |
 |

name

 |

The test name that is stored in the EDL as a `TestNameAttribute`（raw: `../02.10_Data_Logging/02.10.01.06.05.61_TestNameAttrType.md`） for a test result. Used when one of the `TEST`（raw: `02.07.04.01.241_TEST.md`） methods is subsequently called.

Test names can contain any printable ASCII characters, that is, characters with codes from 32 to 126. This includes the space, digits, lowercase letters, uppercase letters, and these punctuation characters: !"#$%&'()*+,-./:;<=>@?[\]^_`{|}~ There is no fixed maximum length for the names in SmarTest. However, STDF limits test names to 255 characters, so test names should not be longer if STDF data logging is intended.

 |
 |

forceSTDFTestName

 |

If this parameter is true, the data formatter writes the name value name directly into the TEST_NAM field of the `TSR record`（raw: `../02.10_Data_Logging/02.10.03.05.26_Test_Synopsis_Record__TSR.md`）.

If the parameter is false, the data formatter calculates the content of the TEST_NAM field from the test suite name, test name, and pin name.

This parameter is optional. The default is false.

 |

### Example

```
TESTSET().testname("Sample_test");
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
