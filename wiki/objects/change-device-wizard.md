---
type: object
title: Change Device wizard
layer: gui
stage: project
tags: [gui, project, wizard, device, activate-device, technology, change-device]
related: [new-device-wizard, device-directory, technology-file-for-a-device, project]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.03_Change_Device_wizard.md
created: 2026-09-21
updated: 2026-09-21
verified: doc-only
---

# Change Device wizard

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **315 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.03_Change_Device_wizard.md>` 及其子主题 `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.03.04_Default_levels_file_for_a_device.md>`。**不是转述。**
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

**这篇定义文档只有两句话。** 一句说它干什么，一句说它从哪开。**没有第三句。**

> 「With the Change Device wizard, you can activate a device and edit the technology data of the device.」
>
> 「This wizard can be opened from 93000 menu or by clicking the Change Device button.」

**它干两件事，两个动作的性质不同**：

| 动作 | 原文用词 | 说明 |
|---|---|---|
| **activate 一颗 device** | `activate a device` | **切到哪一颗**——这是「当前在做的那颗 device」这件事本身 |
| **编辑它的 technology data** | `edit the technology data of the device` | **改数据**——改的是**被 activate 的那一颗**的工艺数据 |

**注意第二件事的宾语**：`the technology data of **the device**`——
**「那颗 device」的 technology data**。**原文用的是定冠词 `the`**，
（推断）指的就是前半句刚 activate 的那一颗；**原文没有把这条依赖写成规则**。
**也就是说：本篇没有一句话写「必须先 activate 才能编辑」，那一步是语序推出来的。**

### 两个入口，一个是菜单、一个是按钮

> 「This wizard can be opened from 93000 menu or by clicking the Change Device button.」

| 入口 | 原文写的 |
|---|---|
| `93000 menu` | **菜单**——原文写的是 `from 93000 menu`（**没有定冠词 `the`**，逐字如此，见「出处」⚠️ ①） |
| **`Change Device button`** | **按钮**——原文在 `Related information` 里**专门给了它一篇**（`Changing the device with the Change Device button`） |

**「按钮 ≠ 向导」这件事值得单独说一句**：
**`Change Device button` 是一个按钮，本页讲的是它点开之后的那个向导**——
**两者不是同一个对象**。原文把「用按钮换 device」的细节放在**另一篇**里，
**本页没读那一篇**，所以「点一下那个按钮会发生什么」本页答不出来。

> **⚠️ 与同名的 HVM 远程命令 `ChangeDevice` 不是一回事。**
> 本 wiki 里另有一个**词面相同、位置不同**的东西：HVM 的远程命令 `ChangeDevice`
> （`02.09.01.10.03.02.02.12`）。**本页没有把它合并进来，也没有读它**——
> 批次注意事项明确要求不要合并（词面同、位置不同）。**看到 `ChangeDevice` 先分清是在哪一层。**

### 它的子主题说明了它的范围

原文的 `#### Subtopics` 列了四个（**本页都没读**）：

| # | 子主题 | 属于「activate」还是「edit technology data」 |
|---|---|---|
| 1 | `Changing the device with the Change Device button` | activate 侧 |
| 2 | `Editing technology data` | edit 侧 |
| 3 | `Technology file for a device` | edit 侧 |
| 4 | `Default levels file for a device` | edit 侧 |

**四分之三在讲 technology data**——**所以这个向导的主体其实是「改工艺数据」，
「activate」只是它的入口动作**（推断，依据是子主题的分布）。

## 典型用法

**原文没有 `## Procedure`、没有 `## Before you begin`、没有 `## Results`。**
**两句话之外一个字都没有**——所以「怎么操作这个向导」在本篇里**不存在**。

| 你想知道 | 本篇给不给 |
|---|---|
| 怎么打开它 | **给**：`93000 menu` 或 `Change Device button`（两条路，都没给步骤） |
| 打开后先做什么 | **不给** |
| activate 一颗 device 需要什么前提 | **不给**（那一篇是子主题 `Changing the device with the Change Device button`） |
| 怎么编 technology data | **不给**（子主题 `Editing technology data`） |
| 怎么切回原来那颗 / 切错了怎么办 | **不给** |

**唯一的实用判断（推断）**：**这个向导是「换 device」和「改工艺数据」两件事共用的入口**——
推断依据同上，是子主题里三篇讲 technology data。**原文没有这么写。**

**下面这条不是使用建议，是一个核对提示**：**动手前先确认你点的是
`Change Device button` 还是那个 HVM 的 `ChangeDevice` 命令**——
**两者词面几乎一样，而本页只讲前者**（见上）。

## 和谁有关

- [[new-device-wizard]] — **成对的那一个，也是本篇 `Related information` 的第三条**。
  **一个字面事实**：两个向导的四个子主题里有**三条标题完全相同**
  （`Editing technology data`、`Technology file for a device`、`Default levels file for a device`）
  ——**这就是两页「语法 / 参数」节抄到同一段 `.default_levels` 示例的原因**。
  **「谁建、谁切」这个分工，本页只写本篇这一半：本篇是 `activate` + `edit`。**
- [[device-directory]] — **activate 的宾语是一颗 device**，而 device 落在 device 目录里；
  **目录结构本身本篇没讲**，在 [[device-directory]] 那一页。
- [[technology-file-for-a-device]] — **本篇的子主题之一就叫 `Technology file for a device`**。
  **但本篇正文一个字没提 technology file**：正文只写 `edit the technology data`，
  **没有说这些数据存在 technology file 里**（推断：两者相关；**原文没有把这条连起来**）。
- [[project]] — 本页 `stage: project` 的理由：它管的是「当前用哪一颗 device」这个工程状态。
- **清单外、本页不链（用反引号写名字）**：`Change Device button`、
  `Changing the device with the Change Device button`、`Editing technology data`、
  `Technology file for a device`、`Default levels file for a device`、`93000 menu`
  —— **这些名字都不在 `prose-allowlist.txt` 里**。

## 版本

原文 `## Functional changes` 段**只有一条**：

| 条目 | 读法 |
|---|---|
| `Introduced in SmarTest 6.5.2` | **真变更，不是哨兵值**——措辞是 **`in`** 而不是 `before`（§11.2 ② 的哨兵值是 `Introduced before SmarTest 6.3.2`）。**所以它确实是 6.5.2 引入的。** |

**和 [[new-device-wizard]] 对一下**：**两者引入版本同为 `SmarTest 6.5.2`**，
**但那一页还多一条 `SmarTest 7.2.2: New parameter: Result Area Size`**，
**本页 7.2.2 一条都没有**——**成对的两个向导，版本记录并不对称。**

## 出处

`sources:` 一篇：
`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.03_Change_Device_wizard.md`（TDC `111004.htm`）
—— **这是一篇极短的文档**：两句话 + 四个子主题 + 三条 `Related information` + 一条版本记录。
**本页没有从别处补任何一句**，所以本页也短；**这不是省略，是 source 就这么大。**

**本页没做的**：

- **四个子主题一篇没读**：`02.08.04.03.01_Changing_the_device_with_the_Change_Device_button`、
  `02.08.04.03.02_Editing_technology_data`、`02.08.04.03.03_Technology_file_for_a_device`、
  `02.08.04.03.04_Default_levels_file_for_a_device`。
  **所以上面那四行「给不给」的表里，「不给」是事实，不是本页偷懒。**
- **`Related information` 的三篇没读**：
  `01.01.10.03.02_Changing_the_device_with_the_Change_Device_button`、
  `01.01.10.03.03_Editing_technology_data`、`02.08.04.15_New_Device_wizard`
  （**最后一篇是 [[new-device-wizard]] 的 source，属于另一页**）。
- **HVM 远程命令 `ChangeDevice`（`02.09.01.10.03.02.02.12`）没读，也没有合并**——
  这是**一批要遵守的边界**，不是一个省略：**词面相同、位置不同，合并会把两层的语义搅在一起。**
- **一张图都没看**——本篇**也没有图**。
- **`Change Device button` 长什么样、在哪个工具栏，本页不知道**（那一篇没读）。
- **本页没在真机上用过这个向导**（`verified: doc-only`）。

> ⚠️ **本篇的两处语料瑕疵，本页照实记下、一处都没替它改**：
>
> ① **缺定冠词**：`This wizard can be opened from 93000 menu or by clicking the Change Device button.`
> —— **`from 93000 menu` 里少一个 `the`**（同批文档里同类句子写的是 `in the SmarTest Work Center`）。
> **本页引这一句时原样保留了 `from 93000 menu`。**
>
> ② **同一篇文档在两个路径下各有一份，标题完全一样。** 逐字对照：
> `#### Subtopics` 里写的是
> `- [Changing the device with the Change Device button](<02.08.04.03.01_Changing_the_device_with_the_Change_Device_button.md>)`、
> `- [Editing technology data](<02.08.04.03.02_Editing_technology_data.md>)`；
> 而 `## Related information` 里写的是
> `[Changing the device with the Change Device button](<../../01_Getting_started/01.01_SmarTest_Work_Center/01.01.10.03.02_Changing_the_device_with_the_Change_Device_button.md>)`、
> `[Editing technology data](<../../01_Getting_started/01.01_SmarTest_Work_Center/01.01.10.03.03_Editing_technology_data.md>)`。
> **标题相同、路径不同（`02.08.04.03.xx` vs `01.01.10.03.xx`），原文没有说明这两份的关系。**
> **本页不判它们是不是同一份内容的两处副本**——那要读过才说得准，**本页两处都没读。**

`verified: doc-only`
