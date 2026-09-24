---
type: object
title: SHARING_CONFIGURATION
layer: n/a
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25_SHARING_CONFIGURATION.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# SHARING_CONFIGURATION

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」节是脚本逐字抽的（§4），**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **4,120 字符逐字取自** `<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25_SHARING_CONFIGURATION.md>` 及其子主题 `<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.01_SHARING_CONFIGURATION.getInstance.md>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.02_SHARING_CONFIGURATION.hasLoaded.md>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.03_SHARING_CONFIGURATION.load.md>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.04_SHARING_CONFIGURATION.setRefPin.md>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.05_SHARING_CONFIGURATION.getModeContext.md>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.06_SHARING_CONFIGURATION.isFXDLIgnorePin.md>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.07_SHARING_CONFIGURATION.utilitySearchFirst.md>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.08_SHARING_CONFIGURATION.utilitySearchNext.md>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.09_SHARING_CONFIGURATION.utilityActionExecute.md>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.10_SHARING_CONFIGURATION.utilityGetApplicableSitesString.md>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.11_SHARING_CONFIGURATION.utilitySubstitutePins.md>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.12_SHARING_CONFIGURATION.domainsGetXSize.md>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.13_SHARING_CONFIGURATION.domainsGetYSize.md>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.14_SHARING_CONFIGURATION.domainsGetZSize.md>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.15_SHARING_CONFIGURATION.domainsGetApplicableSitesString.md>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.16_SHARING_CONFIGURATION.domainsGetSiteAtPos.md>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.17_SHARING_CONFIGURATION.getTerminatedPinList.md>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.18_SHARING_CONFIGURATION.getBufferPinMap.md>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.19_SHARING_CONFIGURATION.getDomain.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax（取自子主题 SHARING CONFIGURATION.getInstance）

```
static SHARING_CONFIGURATION & getInstance() [static]
```

### Example（取自子主题 SHARING CONFIGURATION.getInstance）

This code fragment demonstrates how to use getInstance() to create the SHARING_CONFIGURATION object for using other member functions.

```
//You must first use getInstance() to get the only one active object of the SHARING_CONFIGURATION class.
SHARING_CONFIGURATION &sharingConfig = SHARING_CONFIGURATION::getInstance();

//Load sharing configuration file "default.cfg".
sharingConfig.load("default.cfg");
```

### Syntax（取自子主题 SHARING CONFIGURATION.hasLoaded）

```
bool hasLoaded() const
```

### Syntax（取自子主题 SHARING CONFIGURATION.load）

```
void load(const string & config)
```

 |

Parameter

 |

Description

 |
 |

config

 |

The name of the sharing configuration file which you want to load.

The file must be located in the <device directory>/configuration/ directory.

 |

### Syntax（取自子主题 SHARING CONFIGURATION.setRefPin）

```
void setRefPin(const string & pinName)
```

 |

Parameter

 |

Description

 |
 |

pinName

 |

The name of a pin whose sharing configuration information you want to load.

 |

### Syntax（取自子主题 SHARING CONFIGURATION.getModeContext）

```
const string & getModeContext() const
```

### Syntax（取自子主题 SHARING CONFIGURATION.isFXDLIgnorePin）

```
bool isFXDLIgnorePin(const string & pinname) const
```

 |

Parameter

 |

Description

 |
 |

pinName

 |

The name of a pin for which you want to know whether it is ignored by the fixture delay settings.

 |

### Syntax（取自子主题 SHARING CONFIGURATION.utilitySearchFirst）

```
int utilitySearchFirst(const string & name) const
```

 |

Parameter

 |

Description

 |
 |

name

 |

The name of a utility control line which you want to find in the `utility control block`（raw: `02.12.02.05.06.07.07.02_Sharing_configuration_file.md`）.

 |

### Syntax（取自子主题 SHARING CONFIGURATION.utilitySearchNext）

```
int utilitySearchNext(const string & name) const
```

 |

Parameter

 |

Description

 |
 |

name

 |

The name of a utility control line which you want to search in the `utility control block`（raw: `02.12.02.05.06.07.07.02_Sharing_configuration_file.md`）.

 |

### Syntax（取自子主题 SHARING CONFIGURATION.utilityActionExecute）

```
int utilityActionExecute(int index) const
```

 |

Parameter

 |

Description

 |
 |

index

 |

The location of a utility control line within the utility_control block in the `Sharing configuration file`（raw: `02.12.02.05.06.07.07.02_Sharing_configuration_file.md`）.

0 represents the first line.

 |

### Syntax（取自子主题 SHARING CONFIGURATION.utilityGetApplicableSitesString）

```
string utilityGetApplicableSitesString(int index) const
```

 |

Parameter

 |

Description

 |
 |

index

 |

The location of a utility control line within the utility_control block in the `Sharing configuration file`（raw: `02.12.02.05.06.07.07.02_Sharing_configuration_file.md`）.

0 represents the first line.

 |

### Syntax（取自子主题 SHARING CONFIGURATION.utilitySubstitutePins）

```
void utilitySubstituePins(int index, const string & pinsFrom, string & pinsTo) const
```

 |

Parameter

 |

Description

 |
 |

index

 |

The location of a utility control line within the utility_control block in a `Sharing configuration file`（raw: `02.12.02.05.06.07.07.02_Sharing_configuration_file.md`）. In this line, pins' substitutions are defined.

0 represents the first line in the utility_control block.

 |
 |

pinsFrom

 |

The pin names which will be substituted with new names. Multiple names are separated with commas.

Both the pin names and the new names have already been defined in the utility control line

 |
 |

pinsTo

 |

This variable stores the returned new names which replace the pin names in pinsFrom.

The new names have already been defined in the utility control line.

 |

### Syntax（取自子主题 SHARING CONFIGURATION.domainsGetXSize）

```
int domainsGetXSize() const
```

### Syntax（取自子主题 SHARING CONFIGURATION.domainsGetYSize）

```
int domainsGetYSize() const
```

### Syntax（取自子主题 SHARING CONFIGURATION.domainsGetZSize）

```
int domainsGetZSize() const
```

### Syntax（取自子主题 SHARING CONFIGURATION.domainsGetApplicableSitesString）

```
string domainsGetApplicableSitesString(int x, int y) const
```

 |

Parameter

 |

Description

 |
 |

x

 |

The position in the X dimension, starts from 0.

 |
 |

y

 |

The position in the Y dimension, starts from 0.

 |

### Syntax（取自子主题 SHARING CONFIGURATION.domainsGetSiteAtPos）

```
int domainsGetSiteAtPos(int x, int y, int z) const
```

 |

Parameter

 |

Description

 |
 |

x

 |

The position in the X dimension, starts from 0.

 |
 |

y

 |

The position in the Y dimension, starts from 0.

 |
 |

y

 |

The position in the Z dimension, starts from 0.

 |

### Syntax（取自子主题 SHARING CONFIGURATION.getTerminatedPinList）

```
string getTerminatedPinList(const string & vterm) const
```

 |

Parameter

 |

Description

 |
 |

vterm

 |

The termination pin terminates the pins you want to retrieve.

 |

### Syntax（取自子主题 SHARING CONFIGURATION.getBufferPinMap）

```
const map<int, string> & getBufferPinMap() const
```

### Syntax（取自子主题 SHARING CONFIGURATION.getDomain）

```
vector <int> getDomain(int site) const
```

 |

Parameter

 |

Description

 |
 |

site

 |

The site number from which you want to get the domain.

 |

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
