---
type: object
title: TimingSetSelector
layer: L2
stage: timing
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.02.17_TimingSetSelector.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# TimingSetSelector

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」节是脚本逐字抽的（§4），**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **2,562 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.02.17_TimingSetSelector.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

The default constructor `TimingSetSelector()` is equal to `TimingSetSelector(DIGITAL_OFFSET_SEARCH::PRM, DIGITAL_OFFSET_SEARCH::PRM). R` efers to the primary timing set.

The available constructors are:

```
TimingSetSelector();
TimingSetSelector (const TimingSetSelector& rhs);
TimingSetSelector (const TimingSetSelector* rhs);
TimingSetSelector (const STRING& multiportspec, INT timingset);
TimingSetSelector (INT waveformORspecId, INT timingset);
TimingSetSelector (DIGITAL_OFFSET_SEARCH::PRM_ALL waveformOrSpec,
                   INT timingset);
TimingSetSelector (const STRING& multiportspec,
                   DIGITAL_OFFSET_SEARCH::PRM_ALL timingset);
TimingSetSelector (INT waveformOrSpecId,
                   DIGITAL_OFFSET_SEARCH::PRM_ALL timingset);
TimingSetSelector (DIGITAL_OFFSET_SEARCH::PRM_ALL waveformOrSpec,
                   DIGITAL_OFFSET_SEARCH::PRM_ALL timingset);
TimingSetSelector(const TimingSetSelector & rhs, INT timingSet);
TimingSetSelector(const STRING& waveformOrSpec, const STRING& timingSet);
TimingSetSelector(const STRING& timingSelector);
```

Parameters
 |

Parameter

 |

Description

 |
 |

rhs

 |

The name of an existing TimingSetSelector object.

 |
 |

multiportspec

 |

The name of a multi-port specification, in a multi-port setup.

 |
 |

waveformORspecId (INT)

 |

In fixed timing setup, it is the waveform set number.

In equation based timing setup, it is a timing specification ID calculated as follows:

`100*equation_set_no + specset_no`

 |
 |

waveformOrSpec (`DIGITAL_OFFSET_SEARCH::PRM_ALL`)

 |

It can be:

- DIGITAL_OFFSET_SEARCH::PRM: Selects the primary specification
- DIGITAL_OFFSET_SEARCH::ALL: Selects all waveform sets in the fixed timing set.

Note that this option is only supported for waveform sets, not for specification ID's.

 |
 |

timingset

(`INT`)

 |

The timing set number to select.

 |
 |

timingset

(`DIGITAL_OFFSET_SEARCH::PRM_ALL`)

 |

It can be:

- DIGITAL_OFFSET_SEARCH::PRM: Selects the current primary timing set.
- DIGITAL_OFFSET_SEARCH::ALL: Selects all timing sets in a timing set group.
 |

Return value

There is no return value.

### Example

```
DIGITAL_OFFSET_SEARCH_TASK dos;
STRING strpins1("pcie_tx1n");
DIGITAL_OFFSET_SEARCH::TimingSetSelector dest("multi_port", DIGITAL_OFFSET_SEARCH::ALL);

  dos.pin(strpins1).resourceType(DIGITAL_OFFSET_SEARCH::RECEIVE).searchType(DIGITAL_OFFSET_SEARCH::EYE)
     .start(15).numSteps(120).stepWidth(15)
     .restoreFlag(DIGITAL_OFFSET_SEARCH::NO);
  dos.execute();
  dos.uploadResult(dest, DIGITAL_OFFSET_SEARCH::ALL_EDGES);
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
