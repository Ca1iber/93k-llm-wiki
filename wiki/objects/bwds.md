---
type: object
title: BWDS, BWDS? - (Break Waveform Definition String)
layer: L1
stage: timing
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.14_BWDS__BWDS__-__Break_Waveform_Definition_String.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# BWDS, BWDS? - (Break Waveform Definition String)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」节是脚本逐字抽的（§4），**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **2,097 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.14_BWDS__BWDS__-__Break_Waveform_Definition_String.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### BWDS

```
BWDS {wvf_set}, [break_waveform_index], [mode], {definition_string}, {(pinlist)}
```

### BWDS?

```
BWDS? {wvf_set|"wavetable_name"|specset_id|"multi-port_spec"}, [break_waveform_index], [mode], {(pinlist)}
```

returns:

```
BWDS {wvf_set|"wavetable_name"|specset_id|"multi-port_spec"}, [break_waveform_index], [mode], {definition_string}, {(pinlist)}
```

Parameters
 |

wvf_set

 |

Waveform Set Number (range 1 to maximum). Enter ALL for all waveform sets. Enter PRM for the Primary waveform set. The maximum number is determined by the command `WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）.

 |
 |

wavetable_name

 |

The wavetable name. Enter a string of up to 40 alphanumeric characters (upper or lower case) enclosed in double quotes. wavetable_name can only be specified in the query.

 |
 |

specset_id

 |

Derived as follows:

100 * equation_set_no + specset_no

specset_id can only be specified in the query.

 |
 |

multi-port_spec

 |

To query a multi-port specification, enter the name of the specification.

 |
 |

break_waveform_index

 |

Enter DEF for the default break waveform or an integer in the range 0 to 3. This parameter is optional in release 2.0 and can only be used to select the default break waveform (DEF).

 |
 |

mode

 |

NOT USED.

 |
 |

definition_string

 |

The definition string consists of a sequence of items each of which associates a drive action with a drive edge.

Receive edge are always denoted by rn.

All edges which are not explicitly specified are set to N. In the query only those edges that are used are printed.

For details of the syntax see `WFDS, WFDS? - (WaveForm Definition String)`（raw: `02.06.02.02.335_WFDS__WFDS__-__WaveForm_Definition_String.md`）.

 |
 |

pinlist

 |

The name of the pin or pins for which break waveform definitions are to be made or read back. The symbol @ can be used to specify all configured input and IO pins. If more than one pin is to be included, the names must be separated with a comma.

 |

### Example

```
> BWDS? 1,,,(@)
< BWDS 1,,,"",(io)
< BWDS 1,,,"d1:F00 d5:F10",(clk)
```

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.14_BWDS__BWDS__-__Break_Waveform_Definition_String.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

- waveform_set is greater than the range allowed by the command `WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）.
- There is a mismatch between the edge actions and edge order in the specified waveform.
- A tri-state action is defined or implicitly required on edge 2 or 5 (only for P/C/Ce systems).

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
