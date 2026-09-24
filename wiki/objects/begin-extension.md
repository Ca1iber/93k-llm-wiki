---
type: object
title: BEGIN_EXTENSION
layer: L2
stage: testmethod
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.10_BEGIN_EXTENSION.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# BEGIN_EXTENSION

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」节是脚本逐字抽的（§4），**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,273 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.10_BEGIN_EXTENSION.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
void BEGIN_EXTENSION();
void BEGIN_EXTENSION(STRING& sites);
void BEGIN_EXTENSION(ARRAY_I& sites);
```

Parameter
 |

I/O

 |

Parameter

 |

Description / Range

 |
 |

I

 |

sites

 |

This parameter sets the setup focus sites for the statements in the extension block.

To make the extension block effective for sites 1 to 3 in four sites,

STRING: "1110".

ARRAY_I: sites[0]=1, sites[1]=2, and sites[2]=3.

 |

### Example 1: BEGIN_EXTENSION and END_EXTENSION declare the extension block

```
STRING dfcm("DFCM 1,4000,50,-1.00,1.00,4000,5,I,0,PPNP,(CP)\n");
STRING ptstq("PTST? 1,NONE,NONE,PVAL\n");

BEGIN_EXTENSION();

    FW_TASK(dfcm);

    STRING answer;

    FW_TASK(ptstq, answer);
    ...
    ...

END_EXTENSION();
```

### Example 2: Extension block for all enabled sites

```
STRING enabled_sites;

GET_ENABLED_SITES(enabled_sites);

BEGIN_EXTENSION(enabled_sites);

    //
    // Your FW_TASK code
    //
    ...
    ...

END_EXTENSION();
```

The GET_ENABLED_SITES API retrieves the information of the current enabled sites and stores it to the variable enabled_sites. BEGIN_EXTENSION and END_EXTENSION declare the extension block for multi-site testing. In this example, the extension block is effective for the current enabled sites. BEGIN_EXTENSION sets the current enabled sites to the setup focus sites. Therefore, the statements will be performed for the current enabled sites only.

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
