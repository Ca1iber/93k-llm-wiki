---
type: object
title: WFDS, WFDS? - (WaveForm Definition String)
layer: L1
stage: timing
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.335_WFDS__WFDS__-__WaveForm_Definition_String.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# WFDS, WFDS? - (WaveForm Definition String)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」节是脚本逐字抽的（§4），**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **5,887 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.335_WFDS__WFDS__-__WaveForm_Definition_String.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### WFDS

```
WFDS {wvf_set}, {wfIndex}, [mode], {definition_string}, {(pinlist)}
WFDS {specset_id|"multiport_spec"}, {wfIndex}, [mode], {definition_string}, {(pinlist)}, ALLOW_EQ
```

### WFDS?

```
WFDS? {wvf_set|"wavetable"|specset_id|"multiport_spec"}, {wfIndex}, [mode], {(pinlist)}
```

returns:

```
WFDS {wvf_set|"wavetable"|specset_id|"multiport_spec"}, {wfIndex}, [mode], {definition_string}, {(pinlist)}
```

### Parameters

|

wvf_set

 |

Waveform set number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）. For the query you can also enter ALL for all waveform sets. Enter PRM to select the primary waveform set.

 |
 |

wavetable_name

 |

The wavetable name. Enter a string of up to 40 alphanumeric characters (upper or lower case) enclosed by double quotes.

 |
 |

specset_id

 |

Derived as follows:

`100 * equation_set_no + specset_no`

 |
 |

multiport_spec

 |

To query a multiport specification, enter the name of the specification.

 |
 |

wfIndex

 |

Waveform index. Enter an integer between 0 and 255. The index references a waveform in a device cycle. For the query you can also enter ALL for all waveform DC/DC power units. The waveform index is also used by the `WAVE, WAVE? - (WAVEform)`（raw: `02.06.02.02.333_WAVE__WAVE__-__WAVEform.md`） command.

Note that the index must be specified decimally here, whereas in the wavetable, it is coded hexadecimally.

 |
 |

mode

 |

Not used.

 |
 |

definition_string

 |

Edge action definition string which consists of drive actions for the drive/ bidirectional edges only. On Pin Scale systems, there is only one drive edge type, which is denoted by di (1 鈮? i 鈮?8).

With these edges you can associate the following actions:

- N: No action
- F0N: Drive 0, no tri-state action
- F1N: Drive 1, no tri-state action
- FN0: No drive action, tri-state off
- FNZ: No drive action, tri-state on
- F00: Drive 0, tri-state off
- F0Z: Drive 0, tri-state on
- F10: Drive 1, tri-state off
- F1Z: Drive 1, tri-state on
- D1N: Drive parameter 1 (DD1), no tri-state action
- D1N: Drive parameter 2 (DD2), no tri-state action
- C1N: Drive complement of parameter 1 (DD1), no tri-state action
- C2N: Drive complement of parameter 2 (DD2), no tri-state action
- DN1: No drive action, tri-state parameter 1 (DD1)
- DN2: No drive action, tri-state parameter 2 (DD2)
- D11: Drive parameter 1 (DD1), tri-state parameter 1 (DD1)
- C11: Drive complement of parameter 1 (DD1), tri-state parameter 1 (DD1)
- D22: Drive parameter 2 (DD2), tri-state parameter 2 (DD2)
- C22: Drive complement of parameter 2 (DD2), tri-state parameter 2 (DD2)

All edges which are not explicitly set are set to N. In the query only those edges that are used are printed.

The following table shows which data-dependent drive actions use the driver formatter, which use the tri-state formatter, and which use both. You have to consider this when assigning parameters to the `WAVE`（raw: `02.06.02.02.333_WAVE__WAVE__-__WAVEform.md`） command. See also `Specifying the actions`（raw: `02.06.06.01.03.01.01_Specifying_the_actions.md`）.

 |
 |

 |

Data-dependent Drive Action

 |

Driver

 |

Tri-state

 |
 |

D1N, D2N, C1N, C2N

 |

yes

 |

no

 |
 |

DN1, DN2

 |

no

 |

yes

 |
 |

D11, C11, D22, C22

 |

yes

 |

yes

 |
 |

 |

On Smart Scale systems, there are two types of drive edges, denoted by fi and si (1 鈮?i 鈮?8). For both of them, only the action codes 0, 1, and N are admitted. But the Smart Scale systems also support the old di syntax. For more information see `Defining waveforms for Smart Scale pins`（raw: `02.06.06.01.03.02_Defining_waveform_shapes_for_Smart_Scale_pins.md`）.

 |
 |

 |

On the expected data side the actions you can define are:

- N: No action
- E0: Edge compare to 0
- E1: Edge compare to 1
- EI: Edge compare to intermediate
- EX: Edge compare to mask
- EU: Edge compare to unstable
- C: Capture digital data (selective digital capture)
- D: Do not capture digital data (selective digital capture)

Note that waveforms that are to be used for selective digital capture must contain exactly one compare action.

- W0: Window open with compare to 0
- W1: Window open with compare to 1
- WI: Window open with compare to intermediate
- WX: Window open with compare to mask
- WU: Window open with compare to unstable
- WC: Window close
- EE1: Edge compare to parameter 1 (ED1)
- EE2: Edge compare to parameter 1 (ED2)
- WE1: Window open with compare to parameter 1 (ED1)
- WE2: Window open with compare to parameter 1 (ED2)
 |
 |

pinlist

 |

The name of the pin or pins for which the waveform is to be defined or read back. This parameter can also include groups previously created by `DFGP, DFGP? - (DeFine GrouP)`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）. The @ symbol can be used to specify all configured pins. If more than one pin is to be included, the names must be separated with a comma.

 |
 |

ALLOW_EQ

 |

This extra parameter allows you to define or change logical waveforms for an equation based timing. Note that only the runtime settings are affected; the definitions in the wavetable are not changed.

Note also the following:

- Every runtime change will affect all specifications that use the respective wavetable.
- Since the new or changed waveform must be evaluated and downloaded for every specification that uses the respective wavetable, the change tends to be rather slow.
- The runtime definitions are not checked for consistency. It is up to the user to ensure this.
 |

### Example

```
> WFDS 1,0,,"e1:F00 e2:D1N e3:F00",(io)
> WFDS 1,1,,"r4:EE1",(io)
> WFDS 1,0,,"d1:F00 d2:F10 d3:F10 d4:F00 d5:F10 d6:F00 d7:F10 d8:F00",(clk)

> WFDS? 1,ALL,,(@)
< WFDS 1,0,,"d1:F00 d2:D1N d3:F00",(io)
< WFDS 1,1,,"r4:EE1",(io)
< WFDS 1,0,,"d1:F00 d2:F10 d3:F10 d4:F00 d5:F10 d6:F00 d7:F10 d8:F00",(clk)
```

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.335_WFDS__WFDS__-__WaveForm_Definition_String.md>` 的 `## Errors`、`## Warnings` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

- wvf_set is greater than the range allowed by the WSUS command, or < 1
- The waveform index is outside the range of 0 - 256 (Pin Scale systems)
- There is a mismatch between the edge actions and edge order in the specified waveform
- You specify a drive action for an output pin
- You specify a receive action for an input pin
- There is a mismatch in edge direction between the waveform you have defined and existing waveforms
- There is a missing window close action between two window open actions
- There is a missing window open action between two window close actions

### Warnings

A warning is generated if edge delays are auto-corrected to fit in with the programmed waveform. The timing sets belonging to the affected waveform set are modified as necessary

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
