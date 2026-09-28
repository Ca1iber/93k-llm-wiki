---
type: object
title: CCTchangeLevelSpec
layer: L2
stage: level
tags: [level, l2, test-method-api, spec, level-spec, cct, rename]
related: [level, level-spec, spec-value, spec-variable, cct-multiport-sequencer-synchronizer-api, mapping-level, smartest-7.2.0, smartest-7.2.1]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.14.02_CCTchangeLevelSpec.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# CCTchangeLevelSpec

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **288 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.14.02_CCTchangeLevelSpec.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
void CCTchangeLevelSpec(const string& old_spec, DOUBLE value);
```

Parameters
 |

Parameter

 |

Description

 |
 |

old_spec

 |

The name of the spec to change

 |
 |

value

 |

The value to use

 |

Return value

There is no return value.

### Example

```
CCTchangeLevelSpec("spec1", 1.2);
```

<!-- 语法节 end -->

## 是什么

**`CCTchangeLevelSpec` 是一条「按名字改一个 spec 的值」的函数。** 本篇第一句就是它的全部定义：

> Changes the value for the specified spec.

头文件：`/opt/hp93000/soc/testmethod/include/CCTestMethod.hpp`。

### 签名与参数

```
void CCTchangeLevelSpec(const string& old_spec, DOUBLE value);
```

| 项 | 原文 | 本页能说的 |
|---|---|---|
| **返回类型** | `void` | **没有返回值**——语法节末那一格：`There is no return value.` |
| **第 1 个参数** | `const string& old_spec`；说明是 `The name of the spec to change` | **参数名叫 `old_spec`，说明却只说「要改的那个 spec 的名字」**——**「old」是相对谁而言，本篇没说**（签名里没有对应的 `new_spec`）。 |
| **第 2 个参数** | `DOUBLE value`；说明是 `The value to use` | **类型大写 `DOUBLE`，而同一个签名里第 1 个参数写的是小写 `string`**——**一个签名里两种大小写风格**，原文如此，见「出处」⚠️①。 |
| **单位** | —— | **本篇没有写 `value` 的单位**，例子里的 `1.2` 是裸数。**语料未写。** |

### 本篇只有 60 行：一篇「一个函数一句话」的页

**它没有 `## Application` 段、没有 `## Procedure` 段、没有 `## Before you begin` 段、
没有 `## Important points` 段、没有一条 `Note` / `CAUTION`。**
全文的散文只有两句——第一句 `Changes the value for the specified spec.`，
第二句 `This function is defined in the header file /opt/hp93000/soc/testmethod/include/CCTestMethod.hpp.`，
其余都是语法块与两张参数格。

**所以下面这些一律是「语料未写」，本页不填（§11）：**

| 你可能会问 | 本篇的答复 |
|---|---|
| `spec` 是什么、在哪定义 | **语料未写** |
| `spec1` 这种名字从哪儿来 | **语料未写**（例子直接写了 `"spec1"`，没有说明它是在哪个文件、哪个 set 里定义的） |
| 改完之后要不要 FLUSH、改动落到哪一层 | **语料未写** |
| 改的是哪个 level set / 哪个 spec set 上的 spec | **语料未写**——**签名里根本没有 set 号** |
| 改一个不存在的 spec 会怎样 | **语料未写** |
| 它是 `CCTestMethod` 里的自由函数还是某个类的方法 | **语料未写**（本篇只说它定义在那个头文件里） |
| `CCT` 三个字母展开成什么 | **语料未写**（本篇没有出现 concurrent / multiport / CCT 之外的任何一个词） |

**本页只能保证签名、两个参数名、头文件路径、以及版本那两条**——其余一律回 raw 查。

## 典型用法

**本文档没有 `## Procedure`、没有 `## Before you begin`、没有 `## Important points`。**
`## Example` 段里只有一个代码块，一行：

```
CCTchangeLevelSpec("spec1", 1.2);
```

**能排出来的只有两步，两步都只有这一行的信息量：**

1. **知道要改的那个 spec 的名字**（例子里是 `"spec1"`）与**目标值**（例子里是 `1.2`）。
2. **调 `CCTchangeLevelSpec(名字, 值)`。**

**几点照实说明：**

- **例子里没有一个 set 号、没有一个 pin 名**——**所以「它改的是哪一组 spec」在例子里是隐式的**。
  （**本页的（推断）**：从签名只有两个参数看，它改的只能是**当前生效的那一组**——
  `old_spec` 是一个**名字**而不是「set 号 + 名字」；依据仅此，
  **本篇没有一句话支持这个推断**。）
- **例子没有 `#include`、没有函数上下文**——**它是在哪个入口里被调（`initialize()` 之类），
  本篇一个字都没写**（**语料未写**）。
- **没有说改完要不要 FLUSH、要不要 restore**——**语料未写**。
  （对照 [[level-spec]]：那一页那一族才写了 `FLUSH` 与 `restore()`——
  **本页读了那一页，没读它那一篇的 raw**；**两条路是不是同一件事，本页没有依据**。）

## 和谁有关

- [[level]] — **stage 页，也是本页 `stage: level` 的理由**。本函数改的是 level spec 的值；
  **「Level 这一段整体怎么走」在那一页，本页不写流程**（§2.2）。
  （**本页读了 [[level]] 那一页**：它把本页记成
  「`CCTchangeLevelSpec(spec, value)`，`CCTestMethod.hpp`，7.2.0 引入」——
  **那一句里的三个事实都与本篇一致**。那一页的 `sources` 里**没有本页这一篇**。
  **它引的别篇 raw 本页一篇都没读。**）
- [[level-spec]] — **另一条「在 test method 里改 level spec 值」的路**。
  [[level-spec]] 讲的是 `LEVEL_SPEC(eqnset, specset)` 那个类。**本篇一个字都没提它**，
  所以**两者是同一件事的两条路、还是两个不同场景，本页没有依据**；
  **按页名与「改 level spec 值」这一件事并列，不代表同物。**
  两个签名上看得见的一处差别是：**[[level-spec]] 的入口带 `eqnset` 与 `specset` 两个 set 号，
  本函数的签名里一个 set 号都没有**——**这一步是（推断）**。
  （**[[level-spec]] 那一页本页读了；它那一篇的 raw 本页没读。**）
- [[spec-value]] / [[spec-variable]] — **`spec` 这个词在本 wiki 里的另外两页**：
  它们是 **UTM 参数类型**（一个值 + 单位 / 一条指向某个 spec 变量的引用）。
  **本篇没有出现它们任何一个名字**，**三页的关系本页没有依据**；
  这里只按名字并列，**防止下一个读者拿它们来「补」本页**。
- [[cct-multiport-sequencer-synchronizer-api]] — **同一个 `CCT` 前缀的另一页**。
  本函数定义在 `CCTestMethod.hpp` 里，而那一页讲的是一整套
   **CCT Multi-port Sequencer Synchronizer API**。
  **本篇没有一句说明两者同族**（**本条是（推断）**，依据只有 `CCT` 这个前缀与
  `CCTestMethod.hpp` 这个路径；**本页读了那一页，没读它那一篇的 raw**）。
  **不据此声称同族，也不据此声称同一次调用里要一起用。**
- [[mapping-level]] — **跨层对照表**。另：**本页在 [[level]] 那一页的 L2 表里占一格**
  （**本页读了 [[level]] 那一页**）。**[[mapping-level]] 那页本身本页没读。**
- [[smartest-7.2.0]] / [[smartest-7.2.1]] — **版本页**：本篇 `## Functional changes` 两条的落点。
- **本篇没有点名任何别的 API、任何固件命令、任何 GUI 工具、任何文件。**
  全文只有两句话、一个签名、一个例子——**所以本页 `related` 里没有一条是文档点名的**
  （版本那两条除外，它们来自 `## Functional changes`）。

## 版本

本文档有 `## Functional changes` 段，**两条**：

- **Introduced in SmarTest 7.2.0**
- **SmarTest 7.2.1: Rename the API from CCT_changeLevelSpec to CCTchangeLevelSpec.**

| 版本 | 条目（逐字） | 意味着什么 |
|---|---|---|
| **7.2.0** | `Introduced in SmarTest 7.2.0` | **7.2.0 之前没有这条 API**。这是一条正常的 `Introduced in`，**不是 §11.2 ② 那个 `Introduced before` 哨兵**。 |
| **7.2.1** | `SmarTest 7.2.1: Rename the API from CCT_changeLevelSpec to CCTchangeLevelSpec.` | **7.2.0 上的名字是 `CCT_changeLevelSpec`（中间有下划线）**，7.2.1 改成现在这个名字。**本页的页名与函数名都是改后那一个。** |

**这条改名有一个实际后果**（**本页的（推断）**，依据只是「改名」这件事本身）：
**照 7.2.0 写的代码在源码里写的是旧名字 `CCT_changeLevelSpec`**——
在别人的老工程里搜旧名字，能找出这一族的调用点。
**本篇没有写旧名字在 7.2.1 上还能不能编**（**语料未写**）。

**7.2.1 之后有没有再改过、有没有被废弃——本篇一个字都没有。**
**「没记录」不等于「没改过」**（§13.1 第 ⑥′）。

## 出处

`sources:` 一篇：
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.14.02_CCTchangeLevelSpec.md`
（TDC `136736.htm`，60 行 / 841 字节）。**整篇读完**——**这页之所以短，是因为它本来就短**。

**本页没做的：**

- **第二个例子一个都没有。** 本篇 `## Example` 只有那一行
  （`CCTchangeLevelSpec("spec1", 1.2);`），**所以「真工程里怎么用」本页答不出来**。
- **`CCTestMethod.hpp` 那一族的其余 API 一篇没读**——本页只有这一篇。
  **所以「CCT 这一族里还有哪些函数、它们怎么配合」本页一个字都没有。**
- **[[level-spec]] 那一篇的 raw 没读**（`02.07.04.01.124_LEVEL_SPEC`）——
  本页只读了它的 wiki 页，**所以两条路的关系本页只能标（推断）**。
- **一张图都没看——因为这一篇里没有图。** 实测全文 **0 处** `.png` / `.jpg` / `raw/`。
  **所以本页没有任何来自图的结论**（§11.4：没看图就写「本页没用图」，理由不编）。
- **没有实跑。** 没有在任何机台上写过一行调 `CCTchangeLevelSpec` 的 test method，
  也没有验证过「改一个不存在的 spec 名」会怎样。`verified: doc-only` 指的就是这件事。
- **头文件 `/opt/hp93000/soc/testmethod/include/CCTestMethod.hpp` 没法核对**
  （它不是语料里的文件）——**本页只有原文给的那一条签名**。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改。**
> **①② 回上游 `tdc-html/raw/136736.htm`（2,716 字节 / 32 行）核过，结论写在后面。**
> ① **同一个签名里两种类型名风格**：
>   `void CCTchangeLevelSpec(const string& old_spec, DOUBLE value);`
>   ——**第 1 个参数用小写 `string`、第 2 个用大写 `DOUBLE`。**
>   **上游核过**：`136736.htm` 的 `<pre class="prettyprint copyable singleline">` 里逐字就是
>   `void CCTchangeLevelSpec(const string&amp; old_spec, DOUBLE value);`——
>   **上游如此，不是转换改的。**
> ② **参数名叫 `old_spec`，说明却是 `The name of the spec to change`**——
>   **「old」两个字在说明里没有对应物**（本篇没有 `new_spec`）。
>   **上游核过**：`136736.htm` 那两格逐字如此。
> ③ **本篇没有坏字。** 用 `[一-鿿]` 实测全文 **0 处非 ASCII 字符**
>   （没有 `鈥` / `渭` / `碌` 那一族）。**这是「本页量过的」，判据是本篇这一个文件**；
>   §11.2 ① 那族在别的篇里大量存在。

`verified: doc-only`——**本页没有在任何真实机台上调用过 `CCTchangeLevelSpec`**
（§11：文档里有 ≠ 这台机器上能用；尤其「它改的是哪一组 spec、
改动要不要 FLUSH 才落下去」，**文档没写清，动手前先照实机核对**）。
