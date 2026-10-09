---
type: object
title: The device license file
layer: file
stage: project
tags: [device-license-file, licensing, per-device-licensing, project, model-file, dlf, file]
related: [model-file, global-section, testflow-analyzer-tool, technology-file-for-a-device, mapping-project, project, device-directory, error-flexlm-license-codes, spec-value, spec-variable]
sources:
  - 02_System_reference/02.04_Model_File_and_Licensing/02.04.05.06_The_device_license_file.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# The device license file

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,988 字符逐字取自** `<02_System_reference/02.04_Model_File_and_Licensing/02.04.05.06_The_device_license_file.md>` 及其子主题 `<02_System_reference/02.04_Model_File_and_Licensing/02.04.05.06.02_Device_license_file_syntax.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Device license file syntax（整篇，取自子主题）

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/114462.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：2 行 × 2 列。
# Device license file syntax

The syntax language of the device license file is identical to the syntax language of the model file. Parameters may vary, as the device license file must contain only license relevant entries. For details see `Model file syntax`（raw: `02.04.01.03_Model_file_sections.md`）.

Like the model file, the device license file is organized in several sections: GLOBAL, IOCHANNEL, BOARDCONF, and so on. In each of these sections you can define license relevant aspects. The GLOBAL section, for example, specifies what kind of system is used and what features are available system-wide.

CAUTION The device license file must contain only license relevant entries. All other entries belong in the model file. In the device license file they will cause a parser error. Each section that includes potential licenses requires a header, for example, GLOBAL or IOCHANNEL. Unrequired section headers must be removed.

## Additional entries for device specific licensing

In addition to the `Model file syntax`（raw: `02.04.01.03_Model_file_sections.md`）, the device license file allows additional entries for device specific licensing.

The following license relevant definitions are accepted in the GLOBAL section of the device license file:

 |

DSL

 |

Specifies Device Specific Licensing (DSL) and the device family tag.

DSL = DevFam_1

 |
 |

DSL_ALTERNATIVE

 |

Specifies an alternative device family tag.

DSL_ALTERNATIVE = DevFam_2

This tag is used when there are not enough licenses available to use the primary tag specified by the DSL line. Nevertheless, the pin configuration must be correctly signed for the primary tag, even if the alternative tag is used.

   | Note These parameters are only valid in the device license file, but not in the model file.

## Example

```
...
GLOBAL

    DSL = DevFam_1
    DSL_ALTERNATIVE = DevFam_2

...
```

<!-- 语法节 end -->

## 是什么

**`device license file` 是「每颗器件一份的 license 清单」**——它把「这颗器件真的需要哪些 license」
写下来，好只向 license server 要这些。原文第一句：

> 「The concept of licensing-per-device is based on a licensing file for each device, the device
> license file. This concept allows you to better utilize your licenses by requesting only those
> licenses from the license server that are really required for a device.」

**它解决的问题是「只买这颗器件真的要用的 license」**——原文那半句两头都在这个意思上：
`better utilize your licenses`（把已有的 license 用好）
与 `requesting only those licenses from the license server that are really required for a device`
（只向 license server 要这颗器件真正需要的）。

### 它是 model file 的补充，不是替代

> 「Licensing-per-device does not break the known model file concept and mechanisms. It is rather
> an add-on and enhancement of that concept. Therefore the device license file must contain only
> license relevant entries. To ensure compatibility the device license file uses the same syntax as
> the model file.」

**这一段给出三条硬事实**：

| # | 事实 | 原文 |
|---|---|---|
| 1 | 它**不**推翻 model file，是**加在它上面**的 | `does not break` 原来的那些概念与机制；`It is rather an add-on and enhancement of that concept` |
| 2 | 它**只能**含 license 相关的条目 | `must contain only license relevant entries` |
| 3 | 它的**语法与 model file 相同** | `uses the same syntax as the model file` |

**第 2 条的后果在「语法 / 参数」节里写着**（那一节是脚本从子主题逐字抽来的）：
非 license 相关的条目**放进 device license file 会引起 parser error**。
**即：写错位置不是「被忽略」，是报错**——这是本页最该先记的一条。

**离线在线都能用**，原文只有一句：

> 「Licensing-per-device works both offline and online.」

### 覆盖关系：device license file 赢了 model file

这一条最容易搞反，原文写得很直：

> 「The content of a device license file overrides all license specific entries in the model file.
> If for example, you specify a device license file without any licensing capabilities, the license
> definitions in the model file will simply be ignored.」

**两件事**：

- **device license file 里的内容覆盖（`overrides`）model file 里所有 license 相关条目**；
- **极端情形**：给一份**没有任何 licensing capability** 的 device license file，
  **model file 里的 license 定义就被完全忽略**——
  **所以「交一份什么 capability 都不写的」不等于「什么都没做」，
  它等于「把 model file 里那部分关掉」。**

**⚠️ 另有一条讲「空文件」的，只说了一半**：

> 「Note If a device license file (.license) exists, make sure it is not empty.」

**原文只说了「别让它空」，没有说「空了会怎样」**——**语料未写**。
（这一句在原文里是单独一段，位置在导语那几段之后、`## The structure` 之前。）

**两处措辞要分开读**：上面那条说的是 `without any licensing capabilities`（**没有 capability**），
这一条说的是 `not empty`（**文件为空**）——**原文没有把两者当成一回事，也没有说它们的关系**。
而语法节那条 CAUTION 又要求 `Unrequired section headers must be removed`
（不需要的 section header 必须删掉）——**三条合起来，「一份合法的、但什么都不写的 device license file
还剩多少内容」在语料里没有答案**（**这是本页的观察，不是文档结论**）。

### 结构：model file 的一个子集，作用上是它的扩展

> 「The structure of the device license file is a subset of the model file. The device license file
> does not replace the model file, but extends it. It lists those features that need to be
> licensed, like speed, memory, etc. Non-license relevant entries like test head, etc. belong into
> the model file.」

**`subset` 与 `extends` 两句要一起读**：**结构上**是子集（同样的 section 组织，条目更少），
**作用上**是扩展。**原文给了落点各一个例子**：

| 条目 | 归哪份文件 |
|---|---|
| `speed` / `memory` 这类**需要 license** 的 | device license file |
| `test head` 这类**与 license 无关**的 | model file |

**section 有哪几个、哪些必须删掉、以及 device license file 专有的两个参数**
（`GLOBAL` 段里的 `DSL` / `DSL_ALTERNATIVE`），**都在上面的「语法 / 参数」节里**
——**那一节整篇取自子主题**，本页不重复引（来源说明见「出处」）。

### 放在哪、叫什么名字

原文三条，**两个是要求、一个是建议**：

| | 原文 | 强度 |
|---|---|---|
| **目录** | `To use licensing-per-device, a directory named "license" must exist in your device-directory, and your device license files must reside in this sub-directory:` —— 落在 `<device-directory>/license` | **`must`** |
| **另一条路** | `Alternatively you can specify a device license file using the V93000_LICENSING environment variable.` | `Alternatively` |
| **扩展名** | `For the device license files in the license directory Advantest recommends to use the file name extension ".license". The file base name may reflect your different test scenarios, for example "finalTest.license", "waferSort.license", etc.` | **`recommends`** |

**「必须 / 建议」要分清**：目录是 `must exist`；环境变量是另一条路；
**只有扩展名那一句原文用了 `recommends`**——
**所以 `.license` 这个后缀不是硬要求，而 `finalTest.license` / `waferSort.license`
是原文给的「按测试场景起名」的例子。**

### 一份现成的样例文件

原文给了一个现成的样例：`/opt/hp93000/soc_<version>/pws/data/per-device-license.def`
（**那句原文里 `.def` 与 `documents` 之间少了一个空格**，见「出处」⚠️①），
它的作用是**既描述 device license file 的语法、也当样例用**。

**`<version>` 是原文的占位写法**，本页没有替它填任何具体版本号。

### 两条生成 / 取得的路

> 「You can either develop your own device license files based on the provided example file or use
> the Testflow Analyzer Tool (TAT). The latter is recommended.」

**「自己照样例改」与「用 TAT 生成」两条路，原文推荐后者**——
TAT 是什么见 [[testflow-analyzer-tool]]（**本页没读它**）。

## 典型用法

**原文没有 `## Procedure`，也没有 `## Before you begin`**。
散在导语与 `## The structure` 两节里的动作，合起来是四步：

| # | 做什么 | 依据（原文） |
|---|---|---|
| 1 | **在 device 目录下建 `license` 子目录** | `a directory named "license" must exist in your device-directory` |
| 2 | **把 device license file 放进 `<device-directory>/license`**，扩展名建议 `.license` | `your device license files must reside in this sub-directory` + `Advantest recommends to use the file name extension ".license"` |
| 3 | **文件里只写 license 相关的条目**；section 头按需保留、不需要的删掉 | `must contain only license relevant entries` + 语法节那条 CAUTION |
| 4 | **有多份文件时指定用哪一份**；或者改走 `V93000_LICENSING` 环境变量 | `If you work with several device license files, you must specify the one to use.` / `Alternatively you can specify a device license file using the V93000_LICENSING environment variable.` |

**三条边界要说清**：

- **第 4 步的「怎么指定」本篇没写。** 原文只写
  `For details see Defining the device license file to be used.`
  ——**那篇本页没读**（原文给的是它自己的子主题）。
- **第 3 步的「哪些 section 必须留着」在语法节里（取自子主题），不在定义文档里**：
  定义文档只说「只能写 license 相关条目」，**具体到 section 名与「不需要的 header 必须删掉」
  这条 CAUTION，是子主题说的**。
- **文件从哪来**：照现成样例自己改，或者用 TAT 生成（`The latter is recommended.`）。

**顺序上的一个隐含前提（推断）**：`license` 子目录要在 device 目录里，
而 device 目录是建工程那一段的产物（见 [[device-directory]] / [[project]]）——
**所以这四步排在建 device 之后**。**依据只有 `in your device-directory` 这半句；
原文没有把这一步写成一个先后关系。**

## 和谁有关

- [[model-file]] — **本页的宿主概念，也是本页存在的理由**。
  三句关系都是原文说的：语法相同、结构是子集、内容覆盖；
  而 `test head` 这类非 license 条目**属于 model file**。
- [[global-section]] — **device license file 专有的两个参数写在 `GLOBAL` section 里**
  （`DSL` / `DSL_ALTERNATIVE`，见上面的语法节；那一节取自子主题）。
  **注意那里的措辞**：语法节末尾那条 `Note` 明写这两个参数
  `are only valid in the device license file, but not in the model file.`
  ——**即同一个 `GLOBAL` 段，两份文件允许的条目不同**。
  **[[global-section]] 那页讲的是 model file 里的 `GLOBAL`，本页没读它**。
- [[testflow-analyzer-tool]] — **原文推荐的生成方式**（`The latter is recommended.`）。
  按 [[mapping-project]] 主表那一行的说法，TAT 生成的是 `.licenses`，
  **「生成一份」与「指定用哪一份」是两件事**——**TAT 那篇本页没读**，
  这里只转述那张对照表的结论。
- [[technology-file-for-a-device]] — **另一条指定 device license file 的路**。
  [[mapping-project]] 主表「指定 device license file」那一行的**文件格**写的是
  `.technology` 的 `licensing_file`，**并链到本页**。
  **⚠️ 这个 `licensing_file` 参数本页的出处文档一个字没提**——
  两条路（`.technology` 里指定 与 `V93000_LICENSING` 环境变量）
  **在语料里没有一句把它们连起来的话**，所以这一条关系是从 [[mapping-project]] 那张表来的
  （**那篇 `.technology` 文档本页没读**，本页不替它说话）。
- [[mapping-project]] — **本页在建工程那张对照表上的位置**，见上一条；
  那一行还说明 **L1 格是 `n/a`**——即 **DSCP 没有对应参数**。
- [[project]] — **本页 `stage: project` 的理由**：device license file 是 device 目录里的一份文件，
  属于建工程那一段的产物。
- [[error-flexlm-license-codes]] — **licensing 出问题时的排错页**（一个负数码 + 一句英文）。
  **原文没有链到它**，这里的关系是**按主题**说的（**推断**），不是文档事实。
- `License evaluation`（**未建**；raw: `02.04.05.06.01_License_evaluation.md`）—
  定义文档 `#### Subtopics` 的第一条。**本页没读。**
- `Device license file syntax`（**未建**；raw: `02.04.05.06.02_Device_license_file_syntax.md`）—
  `Subtopics` 的第二条，**也是本页「语法 / 参数」节的整篇来源**。**本页没有打开它**（见「出处」）。
- `Defining the device license file to be used`（**未建**；raw: `02.04.05.06.03_Defining_the_device_license_file_to_be_used.md`）—
  「多份文件时怎么指定」，原文把它推给这一篇。**本页没读。**
- `The licensing environment variable`（**未建**；raw: `02.04.05.06.04_The_licensing_environment_variable.md`）—
  原文点名的 `V93000_LICENSING` 的专页。**本页没读**，所以只知其名。
- `Licensed V93000 products`（**未建**；raw: `02.04.02.01_V93000_License_Master_Look-up_Table.md`）—
  原文点名的「哪些 V93000 特性与产品要 license」清单页。**本页没读。**

## 版本

本文档**有** `## Functional changes` 段，**只有一条**：

- **`Introduced before SmarTest 6.3.2`**

> **这一条是 §11.2② 的哨兵值，不是「6.3.2 新增了 device license file」。**
> 它写的是 `before`——意思是「**在本文档集覆盖范围开始之前就已经有了**」。
> **照字面读会凭空造出一条「SmarTest 6.3.2 新增了 licensing-per-device」的假信息，
> 而且格式齐整。**
> **对照着看**：同批的 [[spec-value]] / [[spec-variable]] 两篇写的是 `Introduced in`
> 加一个真版本号——**那才是真版本号**。**同一个句式只差一个词（`in` / `before`），读法完全相反。**

**原文没有给任何后续变更条目**——所以「section 清单、`DSL` 的语义、
扩展名建议在 6.3.2 之后改过没有」本页没有依据。

## 出处

`sources:` 一篇：
`02_System_reference/02.04_Model_File_and_Licensing/02.04.05.06_The_device_license_file.md`
（TDC `85159.htm`，3,812 字节 / 53 行）——**整篇读完**。

**⚠️ 「语法 / 参数」节的来源不是这篇。** 那一节的节首自己写着
`及其子主题 <02_System_reference/02.04_Model_File_and_Licensing/02.04.05.06.02_Device_license_file_syntax.md>`，
**整节 1,863 字符逐字取自那个子主题**。**那个子主题不在本页 `sources:` 里，本页没有打开它**——
本页对它的了解，**只限于「它被脚本逐字抄进了上面那一节」这一件事**。
所以 `GLOBAL` / `IOCHANNEL` / `BOARDCONF` 那几个 section 名、`DSL` / `DSL_ALTERNATIVE` 两个参数、
以及那条 `parser error` 的 CAUTION，**本页只在转录它的那一节里见过，没有回原文核过上下文**。
**定义文档自己没有 `## Syntax` 段**（它的实质内容只有导语与 `## The structure`、TAT 两节），
**这是「语法在子主题里」这件事的由来**——不是本页的缺陷，是语料的结构如此。

**按 §10 第 0 步查过「是不是同一篇被投放了两次」：这一篇只有一个投放。**
按 `source_topic` = `85159.htm` 与标题 `The device license file` 在 9,398 篇 raw md 里各扫一遍，
**都只命中本页出处这一条路径**——所以本页的 `sources:` 列一条就是全部，
**不存在「同一篇数了两遍」的问题**（对照 [[aprm]] 那一页：同一篇有四个投放）。
**这是正面的查证结果，不是「没查」。**

**本页没做的**：

- **只读了定义文档这一篇，而且整篇读完。** 正文里每一个文档事实都出自这 53 行
  （**唯一例外是上面标了 `（推断）` 与标了来源是 [[mapping-project]] 的那几条**）。
- **四个 `Subtopics` 一篇没读**（`License evaluation` / `Device license file syntax` /
  `Defining the device license file to be used` / `The licensing environment variable`）。
  **所以：怎么指定用哪一份、环境变量怎么设、license 怎么被评估，本页一个字没有。**
- **`Device license file syntax` 那篇没读**——**见上，本页对它的了解只是「它被脚本抄过」。**
- **`.technology` 那篇没读**——`licensing_file` 这个参数本页只有 [[mapping-project]] 的转述。
- **TAT 那篇没读**——`它生成的是 .licenses` 这句是从 [[mapping-project]] 转述的。
- **`model file` 那篇没读**——「model file 里 license 相关条目长什么样」本页没有；
  本页只用了 [[model-file]] 的页名与 [[mapping-project]] 的行位。
- **图：0 张，因为这一篇一张图都没有。** 实测该篇对 `raw/` 的图片引用 **0 处**
  （`grep -o 'raw/[0-9]*\.\(png\|jpg\)'` 零命中），
  **上游 `raw/85159.htm`（7,558 字节）里也没有一个 `<img>`**
  ——**这不是「图够不着」，是这一篇本来就不带图**。
  所以本页**没有任何来自图的结论**，也没有一处需要标「④ 图证」。
- **语料瑕疵查过、结果为零**：本篇用 `[一-鿿]` 实测 **0 命中**（不是 §11.2① 那一族坏字），
  `DC/DC power units`（§11.2⑤ 那个整词替换）实测 **0 命中**。**这不是「没找」，是查过。**
- **没有实跑**：没有建过 `license` 子目录、没有写过 device license file、
  没有跑过 TAT、没有设过 `V93000_LICENSING`。
  **`verified: doc-only` 指的就是这件事。**
- **没有跑 `verify_stages.py`**（按本批分工，避免抢同一个报告文件）。
- **没有动 `wiki/index.md`**，也没有把本页挂进 [[project]] 那页。

> ⚠️ **本篇的语料瑕疵，照实记、一处都没替它改**：
>
> ① **`.def` 与 `documents` 之间少一个空格。** 原文那一句里的路径与动词是连写的：
>
> ```
> per-device-license.defdocuments
> ```
>
> **本页没有替它补空格**；正文里提到这个文件时，写的是完整路径
> `/opt/hp93000/soc_<version>/pws/data/per-device-license.def`（**这里是我按上下文断开的，
> 原文是连写的**），并把「少一个空格」记在这一条里。
>
> ② **`## Related information` 一节里四条链接首尾相接，中间没有任何分隔。**
>    原文这一节就是**一行**，逐字如下：
>
> ```
> [Defining the device license file to be used](<02.04.05.06.03_Defining_the_device_license_file_to_be_used.md>)[Model file sections](<02.04.01.03_Model_file_sections.md>)[Device license file syntax](<02.04.05.06.02_Device_license_file_syntax.md>)[The Testflow Analyzer Tool (TAT)](<02.04.05.07_The_Testflow_Analyzer_Tool__TAT.md>)
> ```
>
>    四条链接的方括号之间**一个空格都没有**，所以渲染出来是一串连写的名字。
>    **这是「md 里该有分隔的地方没有」这一类，与 [[how-to-create-a-universal-test-method-class]]
>    记的 `Comment` 与 `Note` 粘在一起是同一种现象。**
>
> ③ **那一句 `Note` 的行首多一个空格**：
>    ` Note If a device license file (.license) exists, make sure it is not empty.`
>    而且**它只说了「别让它空」，没说空了会怎样**（见上「语料未写」）。
>    **本页并列记下，不替它补后果。**
>
> ④ **`soc_<version>` 里的 `<version>` 是原文的占位写法**，**本页没有替它填任何具体版本号**，
>    也没有拿别的文档里的版本号去补它。

`verified: doc-only`
