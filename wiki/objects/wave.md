---
type: object
title: WAVE, WAVE? - (WAVEform)
layer: L1
stage: timing
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.333_WAVE__WAVE__-__WAVEform.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# WAVE, WAVE? - (WAVEform)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」节是脚本逐字抽的（§4），**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **4,675 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.333_WAVE__WAVE__-__WAVEform.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### WAVE

```
WAVE {wvf_set}, {wfIndex}, [DD1], [DD2], [ED1], [ED2], {pwfIndex}, {(pinlist)}
WAVE {specset_id|"multiport_spec"}, {wfIndex}, [DD1], [DD2], [ED1], [ED2], {pwfIndex}, {(pinlist)}, ALLOW_EQ
```

### WAVE?

```
WAVE? {wvf_set|"wavetable_name"|specset_id|"multi-port_spec"}, {(pinlist)}
```

returns:

```
WAVE {wvf_set|"wavetable_name"|specset_id|"multi-port_spec"}, {wfIndex}, [DD1], [DD2], [ED1], [ED2], {pwfIndex}, {(pinlist)}
```

### Parameters

|

wvf_set

 |

Waveforms set number. Enter an integer in the range 1 to the maximum number of allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`）. For the query command you can also enter ALL for all waveform sets.

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

The wavetable name. Enter a string of up to 40 alphanumeric characters (upper or lower case) enclosed by double quotes.

 |
 |

multiport_spec

 |

To change or query a multiport specification, enter the name of the specification.

 |
 |

wfIndex

 |

Logical waveform index. This index identifies the logical waveform for which a physical waveform is to be created. The values specified for the DD1, DD2, ED1, and ED2 parameters must be in accordance with the format of this logical waveform.

 |
 |

DD1 and DD2

 |

First and second drive data parameter. These are optional parameters and contain values for both drive data and tri-state. The values you can define are:

 |
 |

F0N

 |

drive 0

 |
 |

F1N

 |

drive 1

 |
 |

FN0

 |

tri-state off

 |
 |

FNZ

 |

tri-state on

 |
 |

F00

 |

drive 0, tri-state off

 |
 |

F0Z

 |

drive 0, tri-state on

 |
 |

F10

 |

drive 1, tri-state off

 |
 |

F1Z

 |

drive 1, tri-state on

 |
 |

ED1 and ED2

 |

First and second receive data parameter. These are optional parameters. The values you can define are:

 |
 |

F0

 |

compare to 0

 |
 |

F1

 |

compare to 1

 |
 |

FI

 |

compare to intermediate

 |
 |

FX

 |

compare to mask

 |
 |

FU

 |

compare to unstable

 |
 |

C

 |

capture digital data

 |
 |

D

 |

do not capture digital data

 |
 |

The values C and D are used for selective digital capture. The following rules apply to these values:

- A waveform that is used for selective digital capture cannot contain more than one compare action. Therefore, if you specify C or D for one of ED1 or ED2, you cannot specify a value for the other Expected Data parameter.
- If you issue more than one instance of the WAVE command for the same logical waveform, the values you specify for the same Expected Data parameter in these different WAVE instances must be homogeneous; that is, either all or none of them must be C or D. You cannot, for instance, set ED1 to C in one of these WAVE instances, and set it to F1 in another.
 |
 |

pwfIndex

 |

Physical waveform index. Enter an integer between 0 and 31 (0 and 255 on the Pin Scale Digital systems) for each physical waveform . The index is stored in the vector area and references the physical waveform in the physical waveform table.

 |
 |

pinlist

 |

The name of the pin or pins for which physical waveform states are to be defined or read back. This parameter can also include groups previously created by `DFGP, DFGP? - (DeFine GrouP)`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`）. The symbol @ can be used to specify all configured pins. If more than one pin is to be included, the names must be separated by commas.

 |
 |

ALLOW_EQ

 |

This extra parameter allows you to define physical waveforms for an equation based timing. Note that only the runtime settings are affected; the definitions in the wavetable are not changed.

Note also the following:

- Every runtime change will affect all specifications that use the respective wavetable.
- Since the new waveform must be evaluated and downloaded for every specification that uses the respective wavetable, the change tends to be rather slow.
- The runtime definitions are not checked for consistency. It is up to the user to ensure this.
 |

### Example

```
> WFDS 1,2,,"d1:D11 d3:0 d4:C11",(pin1,pin2,pin3,pin4)
> WAVE 1,2,F00,,,,4,(pin1,pin2,pin3,pin4)
> WAVE 1,2,F10,,,,5,(pin1,pin2,pin3,pin4)
```

This example first defines a logical waveform with the index 2 for waveform set 1. The waveform uses the data parameter D11, the fixed action 0, and the complement C11 of D11. Then two physical waveforms are defined for logical waveform 2, which are referenced by the physical waveform DC/DC power units 4 and 5. Waveform 4 drives to 0 at edge d1, to 0 at d3, and to 1 at d4. Waveform 5 drives to 1 at edge d1, to 0 at d3, and to 0 at d4.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.333_WAVE__WAVE__-__WAVEform.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

- wvf_set is greater than the range allowed by the `WSUS`（raw: `02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.md`） command.
- The logical waveform index is outside the range of 0-31 (for P/C/Ce systems) or 0-255 (Pin Scale systems).
- The physical waveform index is outside the range of 0-31 (0-255 on the Pin Scale Digital Cards).
- You try to define a physical waveform for which no logical waveform exists. Define the waveform first with (`WFDS, WFDS? - (WaveForm Definition String)`（raw: `02.06.02.02.335_WFDS__WFDS__-__WaveForm_Definition_String.md`）.
- There is a mismatch of action between the data parameter in the `WFDF`（raw: `02.06.02.02.334_WFDF__WFDF__-__WaveForm_DeFinition.md`） or `WFDS`（raw: `02.06.02.02.335_WFDS__WFDS__-__WaveForm_Definition_String.md`） definition and the corresponding fixed action as specified by WAVE.
- You try to redefine a physical waveform for a waveform. Delete the waveform and any associated physical waveforms first with `WFUD - (WaveForm UnDefine)`（raw: `02.06.02.02.338_WFUD_-__WaveForm_UnDefine.md`）.
- specset_id is invalid because equation_set_no, specset_no, or both are invalid.
- specset_id does not reference a defined wavetable.
- wavetable_name does not reference a defined wavetable.

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
