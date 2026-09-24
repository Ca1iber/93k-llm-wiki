---
type: object
title: VWFG? - (Verify WaveForms in Groups)
layer: L1
stage: timing
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.330_VWFG__-__Verify_WaveForms_in_Groups.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# VWFG? - (Verify WaveForms in Groups)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」节是脚本逐字抽的（§4），**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,794 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.330_VWFG__-__Verify_WaveForms_in_Groups.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

There are three different ways to call VWFG?:

```
VWFG? {waveform_set}, ["dev_cyc_name"], {(pinlist)}
VWFG? {specset_id},["dev_cyc_name"],{(pinlist)}
VWFG? {wavetable_name}, ["dev_cyc_name"], {(pinlist)}
```

All three forms return:

```
VWFG {status}
```

### Parameters

|

waveform_set

 |

Waveform Set Number. Enter PRM for the Primary Waveform Set, or an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）.

 |
 |

specset_id

 |

Derived as follows:

`100 * equation_set_no + specset_no`

 |
 |

wavetable_name

 |

The wavetable name. Enter a string of up to 40 alphanumeric characters (upper or lower case) enclosed in double quotes.

 |
 |

dev_cyc_name

 |

If you specify the name of a device cycle, only this device cycle will be checked. Enter ALL for all device cycle names in the device cycle table.

 |
 |

pinlist

 |

The name of the pin or pins whose definitions you want to check. This parameter can also include groups previously created by `DFGP, DFGP? - (DeFine GrouP)`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）. If more than one pin is to be included, the names must be separated with a comma. The symbol @ can be used to check all configured pins.

 |
 |

status

 |

The system returns:

0: The definitions are not the same.

1: The definitions are the same.

 |

### Example

```
> VWFG? "spec_search_wtb","SBC",(ser_in)
< VWFG 1
> VWFG? "spec_search_wtb",,(ser_in)
< VWFG 0
```

According to this example, the waveform and device cycle definition for device cycle SBC are the same for the pins in the group ser_in within the wavetable spec_search_wtb, but this does not hold for all device cycles that are defined for the pins of this group.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.330_VWFG__-__Verify_WaveForms_in_Groups.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

- waveform_set is greater than the range allowed by the `WSUS`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） command.
- specset_id is invalid because equation_set_no, specset_no or both are invalid.
- specset_id does not reference a defined wavetable.
- wavetable_name does not reference a defined wavetable.
- multi-port spec does not reference a defined wavetable.

<!-- 报错节 end -->

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
