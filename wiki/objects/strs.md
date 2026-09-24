---
type: object
title: STRS? - (Spec TRansition Search)
layer: L1
stage: timing
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.251_STRS__-__Spec_TRansition_Search.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# STRS? - (Spec TRansition Search)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」节是脚本逐字抽的（§4），**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **4,714 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.251_STRS__-__Spec_TRansition_Search.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
STRS? ["exec_context",] [start], [stop], {mode}, [(pinlist)], {spec_type}, {"spec_name[@port[@UNCHANGED]]"}, [stepwidth], {resolution}
```

returns:

```
STRS {res_spec}, [pass_meas_value], [fail_meas_value], [(pinlist)]
```

### Parameters

|

exec_context

 |

An execution context. For more information on execution contexts see `Using execution contexts`（raw: `02.06.07.01.08.05.03.02.03_Using_execution_contexts.md`） .

 |
 |

start

 |

Double float with up to 5 digits after the decimal point defining the value of spec_name at the start of the search. The maximum valid range is -21474.83648 to +21474.83647, though this may be limited by the maximum and minimum values defined with the spec. If the parameter is omitted, the minimum value as defined in the spec set will be used.

The start value can be greater than the stop value. In this case the search will be in the negative direction.

 |
 |

stop

 |

Double float with up to 5 digits after the decimal point defining the value of spec_name where you want the search to end. The maximum valid range is -21474.83648 to +21474.83647, though this may be limited by the maximum and minimum values defined with the spec. If the parameter is omitted, the maximum value as defined in the spec set will be used.

The stop value can be smaller than the start value. In this case the search will be in the negative direction.

 |
 |

mode

 |

Search mode. Use:

L to specify a linear search,

LB to specify linear/binary search,

B to specify a binary search.

 |
 |

pinlist

 |

The name of the pin or pins for which the value of the spec variable is to be modified. This parameter may also include groups previously created by the `DFGP`（raw: `02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.md`） command. If more than one pin is to be included, the names must be separated with a comma.

The @ character indicates all pins. This is the default.

 |
 |

spec_type

 |

Which specification type to use. Use :

LEV to specify levels, or

TIM to specify timing.

 |
 |

spec_name

 |

A string of up to 64 alphanumeric characters (upper or lower case) enclosed in double quotes.

If you use the option @port`[`@UNCHANGED`]`, (see the port parameter), you must include this extension in the double quotes, too.

 |
 |

port

 |

In a multi-port setup, you can add a port name to the spec variable. This will have the effect that the value of the variable will be modified only for pins belonging to this port. This holds even if the variable has global scope for this port in the timing specification.

If you specify the spec variable without a port in a multi-port setup, its value will only be modified for a pin whose port has the spec variable set to global scope.

For more information on the scope of a variable see `Global and local scope of base variables`（raw: `02.06.06.01.05.03.01_Global_and_local_scope_of_base_variables.md`）.

Note that if a port that is specified with the name of the variable it is this port on which the value of the variable will be modified. The setup pins have no influence on this.

On a Pin Scale system, the specification of a port will have an additional effect:

If spec_name is used in the definition of the port period, this port will be temporarily used as the primary port. For more information see `Modifying the period for a search or shmoo in a multi-port setup`（raw: `02.06.09.01.01.01_Modifying_the_period_for_a_search_or_shmoo_in_a_multi-port_setup__Pin_Sc.md`）.

This switch can be suppressed by adding @UNCHANGED to the port name.

 |
 |

stepwidth

 |

The search step width in the unit specified with the corresponding spec. This is optional if mode is B.

 |
 |

resolution

 |

The smallest step size to be used in the search. Especially useful in a binary search of a range of floating point numbers, where the number of values between start and stop is infinite. The unit must be the same as defined with the spec.

 |
 |

res_spec

 |

LT (less than)

LE (less than or equal to)

EQ (equal to)

GE (greater than or equal to)

GT (greater than).

 |
 |

pass_meas_value

 |

A double float defining the passed measured value, with up to 5 digits after the decimal point. Valid range is -21474.83648 to +21474.83647.

This parameter contains the last (in a PASS/FAIL transition) or the first (in a FAIL/PASS transition) value where the test passed.

 |
 |

fail_meas_value

 |

A double float defining the failed measured value, with up to 5 digits after the decimal point. Valid range is -21474.83648 to +21474.83647.

This parameter contains the first (in a PASS/FAIL transition) or the last (in a FAIL/PASS transition) value where the test failed.

 |

### Example

```
STRS? 0.5,2.0,LB,,LEV,"aclk_vo_swing",0.1,0.1
```

returns

```
STRS GE,2,,
```

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.251_STRS__-__Spec_TRansition_Search.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if the primary sets used are not equation-based.

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
