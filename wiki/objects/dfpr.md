---
type: object
title: DFPR, DFPR? - (DeFine Pin Role)
layer: L1
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.64_DFPR__DFPR__-__DeFine_Pin_Role.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# DFPR, DFPR? - (DeFine Pin Role)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」节是脚本逐字抽的（§4），**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **2,359 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.64_DFPR__DFPR__-__DeFine_Pin_Role.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### DFPR

```
DFPR "alias_set_name","pin_alias", (package_pin_name)
```

### DFPR

```
DFPR?DEF|ALL, (alias_set_name::pin_alias|alias_set_name|@)
```

returns:

```
DFPR "alias_set_name", "pin_alias", (package_pin_name)
```

### Parameters

|

alias_set_name

 |

The alias set name.

If you assign a pair of pin alias and package pin name to a nonexistent alias set, an alias set is created named with this parameter.

In the query, you can define multiple alias sets or use the symbol @ to list all the defined pin alias sets.

 |
 |

pin_alias

 |

The pin alias.

 |
 |

package_pin_name

 |

The package pin name.

 |
 |

DEF|ALL

 |

If you select `ALL` in the query, for the pins without aliases, the package pin names are returned.

If `DEF` is chosen in the query, only the defined pin aliases are returned.

 |

### Examples

### Generic case

The pin configuration file includes three pins: `CP`, `S0`, and `S1`. There are two alias sets, `FUNC` and `TRANS.`

FUNC

 |

Alias

 |

Pin

 |
 |

CLK

 |

CP

 |

TRANS

 |

Alias

 |

Pin

 |
 |

Read

 |

S0

 |
 |

Write

 |

S1

 |

The following examples are the operations of these sets.

### Example 1

```
DFPR? DEF,(@)
```

returns

```
DFPR "FUNC","CLK",(CP)
DFPR "TRANS","Read",(S0)
DFPR "TRANS","Write",(S1)
```

This example returns the names of all defined alias sets together with their defined pin aliases. This query will not return the pins without aliases.

### Example 2

```
DFPR? ALL,(FUNC,TRANS)
```

returns

```
DFPR "FUNC","CLK",(CP)
DFPR "FUNC", "S0",(S0)
DFPR "FUNC", "S1",(S1)
DFPR "TRANS","CP",(CP)
DFPR "TRANS","Read",(S0)
DFPR "TRANS","Write",(S1)
```

This example returns the pin aliases for all pins in the alias sets `FUNC` and `TRANS`. For the pins without aliases, the package pin names are returned.

### Example 3

```
DFPR? DEF,(TRANS)
```

returns

```
DFPR "TRANS","Read",(S0)
DFPR "TRANS","Write",(S1)
```

This example returns the defined pin aliases in the alias set `TRANS`. This query will not return the pins without aliases.

### Example 4

```
DFPR? DEF,(FUNC::CLK)
```

returns

```
DFPR "FUNC","CLK",(CP)
```

This example returns the package pin name `CP` which is related to the pin alias `CLK` in the alias set `FUNC`.

### Example 5

```
DFPR "TRANS","CLK",(CP)
```

This example adds the package pin `CP` and its alias `CLK` to the alias set `TRANS`. Now the alias set `TRANS` is as the following.

 |

Alias

 |

Pin

 |
 |

Read

 |

S0

 |
 |

Write

 |

S1

 |
 |

CLK

 |

CP

 |

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.64_DFPR__DFPR__-__DeFine_Pin_Role.md>` 的 `## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if the package pin name has not been defined.

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
