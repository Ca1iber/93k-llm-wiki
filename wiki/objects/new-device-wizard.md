---
type: object
title: New Device wizard
layer: gui
stage: project
tags: [gui, project, wizard, device, device-directory, technology, vector-memory, workspace]
related: [change-device-wizard, device-directory, technology-file-for-a-device, device-technology-directory, workspace, project]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.15_New_Device_wizard.md
created: 2026-09-21
updated: 2026-09-21
verified: doc-only
---

# New Device wizard

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **315 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.15_New_Device_wizard.md>` 及其子主题 `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.15.04_Default_levels_file_for_a_device.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Default levels file for a device）

### .default_levels file

All resources except vol_diff and voh_diff are set to customized default values.

```
vil         =  2250mV
vih         =  2500mV

vihh        =  7.0V

vol         =  2250mV
voh         =  2500mV

vt          =  2500mV
vcom        =  2500mV

rec_swing   =  0.800V
rec_offset  =  0.500V
```

<!-- 语法节 end -->

## 是什么

**New Device wizard 干两件事，原文一句话说完**：

> 「With the New Device wizard, you can create a new device directory and create a link to your workspace.」

**两件事要拆开读**：① **在磁盘上建出一个 device 目录**；② **在你的 workspace 里建一条指向它的链接**。
**「建目录」和「挂进工作区」是两步，不是一个动作**——这一点是后面
`Change to new device after creation` 那个勾选项存在的前提。

### 这一篇的形状：一串「控件说明」

**原文没有分页、没有编号、没有「第几步」**，就是**一串平铺的 `- ` 条目**，
一条讲一个控件或一个选项。**本页按「控件 → 要做什么」把它整理成表**——
**顺序照原文，没有重排**：

| # | 控件 / 选项 | 原文说的 |
|---|---|---|
| 1 | **`Change to new device after creation`** | 勾上 → **建完就把这颗新 device activate 掉**（`if you want this new device to be activated after creation`） |
| 2 | **`Device Path`** 文本框 | **同时指定新 device 的路径和名字**（`the path and the name`） |
| 3 | **`Device technology`** 列表 | 选**器件的半导体工艺**；**`Default is cmos`** |
| 4 | **`V3 delay adjust`** | **跳过它**（`Skip the V3 delay adjust option.`）——**`It is supported only by the HSM3600 card.`** |
| 5 | **`Fast bidirectional capability`** | **不再支持**（`is no longer supported`） |
| 6 | **`Preinitialize vector memory to value`** + 初始化值 | **把向量存储器重新初始化成指定值**；**支持范围 `0 to 255`** |
| 7 | **`Expand the extra options`** | **展开后可以改某些系统参数的最大值**——`These values determine the amount of memory reserved for the respective data structures`；**并且可以选 `RFI to RFE compatibility mode`**（当 RFI 板被限制到 RFE 卡时） |

**第 4、5 两条是「什么不要动」**——一篇讲「怎么建 device」的文档里夹了两条否定指令，
**它们的位置在第 3 与第 6 条之间，不会出现在任何「必填项」清单里。**

**第 7 条是本页唯一一处「改了会影响内存占用」的地方**：
`These values determine the amount of memory reserved for the respective data structures`。
**原文只说了「这些值决定保留多少内存」，没有说要怎么定**。

### 图：只有一张，而且是「展开之后」的形态

原文带一张截图，alt 文本是 **`Expand the extra options`**（raw: `../../../../raw/354785.png`）。
**注意它的 alt 说的是第 7 条那个动作**——所以**这张图拍的是「展开额外选项之后」的样子**，
不是向导打开时的默认样子。**本页没看这张图**，所以控件长什么样、按什么顺序排，本页不知道。

### 它和 Change Device wizard 是一对

原文的 `Related information` 里**第二条就是它**：

> `[Change Device wizard](<02.08.04.03_Change_Device_wizard.md>)`

**本页能确定的只有这一条链接**：原文把 [[change-device-wizard]] 当作「相关」列了出来。
**「它干什么」不在本页 source 里**，见 [[change-device-wizard]]。
**两个字面事实放在这里**：① 本页自己用的是 **`create`（建新的）**，
而 `activated` 这个词在本页只出现在**第 1 条那个勾选项**里（`Change to new device after creation`
——**勾上就是把新建的这颗 activate 掉**）；② **两个向导的子主题清单里有三条标题完全相同**
（见「和谁有关」）。

## 典型用法

**原文没有 `## Procedure` / `## Before you begin` / `## Results`。**
能照做的只有上面那张表——**它是控件清单，不是步骤清单**。

### 照原文能拼出的顺序

**原文没有给顺序**，下面这一串是**按表的排列推的**（推断，依据是字段的依赖关系：
`Device Path` 必须先有，`Change to new device after creation` 是事后动作）：

1. **填 `Device Path`**（路径 + 名字）→ 决定了目录建在哪、叫什么。
2. **选 `Device technology`**（默认 `cmos`）。
3. **要不要 `Preinitialize vector memory to value`**：要就把值和 `0–255` 之间的初始化值填上。
4. **要不要展开 `extra options`** 改内存保留量 / 选 `RFI to RFE compatibility mode`。
5. **`V3 delay adjust` 跳过**（除非你是 HSM3600 卡——原文说那个选项只它支持）。
6. **`Fast bidirectional capability` 不用找**，原文说不再支持。
7. **要不要 `Change to new device after creation`**：勾上则建完直接切过去。

**原文一条操作都没写「点哪个按钮结束」**——所以**向导怎么提交、有没有 `Finish`，本页不知道**。

### 两条容易踩的

- **`Device Path` 一个框同时管路径和名字**（`the path and the name`）。
  **原文没有说路径和名字是怎么拼的**（哪一段是目录、哪一段是 device 名），
  本页不猜。
- **`Preinitialize vector memory` 的范围是 `0 to 255`**，原文给了括号里的 `supported range`；
  **这是本篇唯一一个带数值范围的字段**。

## 和谁有关

- [[change-device-wizard]] — **成对的那一个**：**原文在 `Related information` 里直接链它**，
  这是本篇唯一的依据。**它做什么，见它自己那一页**；本页不代它说。
  **一个字面事实**：两个向导的四个子主题里有**三条标题完全相同**
  （`Editing technology data`、`Technology file for a device`、`Default levels file for a device`）
  ——**这也是两页「语法 / 参数」节都抄到同一段 `.default_levels` 示例的原因**。
- [[device-directory]] — **本页建出来的东西就是它**（`create a new device directory`）。
  目录里有哪些子目录、放什么，**在本页只有名字，内容在 [[device-directory]] 那一页**。
- [[workspace]] — 原文说第二个动作是 `create a link to your workspace`；
  **workspace 本身是什么、链接长什么样，本篇没讲**。
- [[technology-file-for-a-device]] — **本篇的子主题之一就叫 `Technology file for a device`**
  （`02.08.04.15.03_Technology_file_for_a_device.md`）。
  第 3 条那个 `Device technology` 列表选出来的工艺**往哪里落**，
  **本页只说「选半导体工艺」，没说是写进 technology file**（推断：两者相关，
  但**原文没有把这两件事连起来**，本页不替它连）。
- [[device-technology-directory]] — 名字与第 3 条的 `Device technology` 很近，
  **但本篇一个字没提它**；**两者是不是一回事，本页不下结论**。
- **清单外、本页不链（用反引号写名字）**：`Creating a new device`、
  `Editing technology data`、`Default levels file for a device`（都是本篇的子主题）、
  `HSM3600`、`RFI`、`RFE`、`row_init_vectors_with_value`
  —— **这些名字都不在 `prose-allowlist.txt` 里**。
- **一条关于「入口」的话，本页只说原文说的那部份**：原文 `Related information` 第一条是
  `Creating a new device`（`01.01.10.03.01_Creating_a_new_device.md`），
  **它说明另有一条「建 device」的路径存在**；**那条路径和本向导是什么关系，原文没说**，
  本页也没读那一篇。

## 版本

原文 `## Functional changes` 段两条：

| 条目 | 读法 |
|---|---|
| `Introduced in SmarTest 6.5.2` | **这是真变更，不是哨兵值。** 措辞是 **`in`** 而不是 `before`—— §11.2 ② 里那个哨兵值是 `Introduced before SmarTest 6.3.2`。**所以 New Device wizard 确实是 6.5.2 引入的。** |
| `SmarTest 7.2.2: New parameter: Result Area Size` | **7.2.2 加了一个参数 `Result Area Size`。** ⚠️ **但 `Result Area Size` 这个词在本篇正文里一次都没出现**（本页逐字核过）。**（推断）它多半属于正文第 7 条 `Expand the extra options … edit the maximum values for certain system parameters` 那一组**，推断依据是「正文只有那一处在讲『系统参数的最大值』」；**原文没有把版本条目和正文哪一条对上**，所以这只是推断 |

**和 [[change-device-wizard]] 对一下**：**两者的引入版本同为 `SmarTest 6.5.2`**，
**但本页多一条 7.2.2 的 `Result Area Size`**——**成对的两个向导，版本记录并不对称**。

## 出处

`sources:` 一篇：
`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.15_New_Device_wizard.md`（TDC `111005.htm`）
—— 这是一篇**很短的文档**：一句定义 + 七条控件说明 + 版本段，**没有操作节**。

**本页没做的**：

- **四个子主题一篇没读**：`02.08.04.15.01_Creating_a_new_device`、
  `02.08.04.15.02_Editing_technology_data`、`02.08.04.15.03_Technology_file_for_a_device`、
  `02.08.04.15.04_Default_levels_file_for_a_device`。
  **所以「建 device 的完整步骤」「technology data 怎么编」「technology file 与
  default levels file 长什么样」本页一个字都没有。**
- **`Related information` 的两篇没读**：
  `01.01.10.03.01_Creating_a_new_device`、`02.08.04.03_Change_Device_wizard`。
  **注意后一篇是另一页 [[change-device-wizard]] 的 source**——
  本页 source 只有一句「New Device wizard 能 create 一个 device 目录并挂到 workspace」，
  **`activate` 那半句（Change Device wizard 干什么）不在本页 source 里**。
  本页对「两者是一对」的判断，**依据只是本页 `Related information` 的这一条链接**
  加上一个字面事实：**两个向导的子主题清单里有三条标题完全相同**
  （`Editing technology data`、`Technology file for a device`、`Default levels file for a device`）。
  **`activate` 那一侧的细节见 [[change-device-wizard]]。**
- **图 `raw/354785.png` 没看**（alt 是 `Expand the extra options`）——
  **本页没有任何来自图的结论**；向导的页数、控件排布、默认值控件长什么样，都不知道。
- **`row_init_vectors_with_value` 指向的那一节没读**——
  所以「向量存储器初始化成某个值」到底做什么，本页只有原文那一句。
- **本页 `## 语法 / 参数` 节的 Example 不是本篇 source 的内容**：
  它逐字来自子主题 `02.08.04.15.04_Default_levels_file_for_a_device.md`（**本页没读**），
  内容是 `.default_levels` 文件的一个片段。**别把这一页读成「New Device wizard 会写
  `.default_levels`」**——原文没有把那件事和向导连起来。
- **本页没在真机上走过这个向导**（`verified: doc-only`）。

> ⚠️ **语料瑕疵：本篇一处都没发现。**
> 本页按 §11.2 的判据（`[一-鿿]`）逐行扫过 source，**没有坏字、没有发现自相矛盾**。
> 这里写「没有发现」，不是「保证没有」——**本页只扫了这一篇**。
>
> **只记一条不算瑕疵、但读的时候要知道的措辞**：第 7 条那句是
> `These values determine the amount of memory reserved for the respective data structures`，
> **`respective` 指的是哪些数据结构，原文没有列**。

`verified: doc-only`
