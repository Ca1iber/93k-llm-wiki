---
type: object
title: tpt_generate_device_dir
layer: L3
stage: project
tags: [project, stpm, tpt, device-directory, command]
related: [stpm, stpm-control-file, tpt-import-from-device, device-directory, preprocessing-and-postprocessing-scripts]
sources:
  - 02_System_reference/02.09_Test_Program_Management/02.09.02.03.16_tpt_generate_device_dir.md
created: 2026-09-18
updated: 2026-09-20
verified: doc-only
---

# tpt_generate_device_dir

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,849 字符逐字取自** `<02_System_reference/02.09_Test_Program_Management/02.09.02.03.16_tpt_generate_device_dir.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
tpt_generate_device_dir(
tpt_dir = <tpt_directory>,
    device_dir = <directory>,
[device_name = <device_name>, ]
[pre_proc = <pre_proc>, ]
post_proc = <post_proc>]
)
```

### Parameters

The parameters in the order in which they are listed above:

| tpt_dir | <tpt_directory> (string) is the name and path of the directory containing the TPT files from which the device directory is to be generated.<br><br>The path can be either absolute or relative to the current working directory. |
|---|---|
| device_dir | <directory> (string) is the path, including the name, where the new device directory is created. The directory must either not exist yet (in which case STPM creates it) or it must be empty.<br><br>The path can be either absolute or relative to the current working directory. |
| device_name | <device_name> (string) is the name for the newly created device.<br><br>This parameter is optional. If it is omitted, "device" is used. |
| pre_proc | <pre_proc> is a script that is executed before this command.<br><br>The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.<br><br>This is an optional parameter. |
| post_proc | <post_proc> is a script that is executed after this command.<br><br>The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`）.<br><br>This is an optional parameter. |

### Example

This example creates a device directory for the device "my_device" from the TPT master file "my_tpt.tpt" (located in the current working directory). The device directory is located at the same level as the current working directory.

```
tpt_generate_device_dir(
    tpt_dir     = 'my_tpt/'
    device_dir  = '../my_device/'
    device_name = 'my_device',
    )
```

<!-- 语法节 end -->

## 是什么

**`tpt_generate_device_dir` 是 STPM 控制文件里的一条命令：从一份 test program template（TPT）长出一个新的 device directory。**

原文第一句把身份和用途一起给了：

> 「The tpt_generate_device_dir command for the SmarTest Program Manager (STPM) control file lets you create a new device directory from a test program template.」

**执行时 STPM 做两件事**——先建结构、再往里填：

> 「When executing the command, STPM creates the directory structure for the device and fills it with a testflow and related files, as specified in the template.」

**注意最后半句：填什么由 template 决定，不由本命令的参数决定。** 命令给的五个参数里，
**没有一个能决定「生成出来的设备里有哪些 testflow」**——那是 TPT 里写好的。

### 与 `tpt_import_from_device` 的交接：静态目录会被搬过来

原文第三条事实是这两条命令之间唯一的接口：

> 「If any static directories were imported with the copy_static_content parameter of the tpt_import_from_device command, tpt_generate_device_dir copies these directories into the newly generated device directory.」

**这句话把两页连成一条上下游链**：静态目录**「带不带、带哪些」是在 import 那一步用 `copy_static_content` 决定的**，
generate 这一步**只是把它们复制过去**，**自己没有开关**。

> **本页只能读到这里**：`copy_static_content` 怎么用、`static directory` 具体指什么，
> 都在 `tpt_import_from_device` 那篇里，**本页没读**。

### 五个参数，三个可选

| 参数 | 必填 | 值 | 原文给的约束 |
|---|---|---|---|
| `tpt_dir` | **必填** | `<tpt_directory>`（string） | **装 TPT 文件的那个目录**；路径**绝对或相对 cwd** 都行 |
| `device_dir` | **必填** | `<directory>`（string） | **新 device directory 的路径（含名字）**；**必须「还不存在」或「存在但为空」** |
| `device_name` | 可选 | `<device_name>`（string） | **省略时用 `"device"`** |
| `pre_proc` | 可选 | 一段脚本 | **在本命令之前**执行 |
| `post_proc` | 可选 | 一段脚本 | **在本命令之后**执行 |

**`device_dir` 那条约束是本页最该记住的一句**，原文写得很死：

> 「The directory must either not exist yet (in which case STPM creates it) or it must be empty.」

**「存在但非空」不在允许范围里。** 原文**只列出这两种可接受状态**，
**没有说给了非空目录会怎样**（报错？覆盖？原文未写）——**本页不替它补**。

### `pre_proc` / `post_proc` 的值**不在这篇里定义**

原文对这两个参数各只有一句，且都指向同一篇：

> 「`<pre_proc>` is a script that is executed before this command.」

> 「The syntax of the parameter value is described in Preprocessing and postprocessing scripts.」

（两句在原格里是**两段**，之间隔着换行；语料里那个换行现在写作 `<br>`。
**所以它们不是一段连续文字，必须分成两个引文块**——并成一个，
第七类会算「丢字符」。见 `schema.md` §11.1。）

（第二句里的文档名在原文里是一个**语料内部链接**，指向
raw: `02.09.02.03.03_Preprocessing_and_postprocessing_scripts.md`；
**本页把链接名摘出来放在引号外**，引号里保留逐字原文。）

**「是一段脚本」+「语法在别处」就是本篇关于它们的全部内容。**
**脚本是文件、是内联字符串、用什么语言，本页一个字都没有。**

## 典型用法

原文只有**一条** `### Example`，**代码逐字见上节的 `### Example` 块，本页不重复贴**。
它描述的三件事：

| 项 | 例子里给的值 | 原文的话 |
|---|---|---|
| 设备名 | `my_device` | `creates a device directory for the device "my_device"` |
| 来源 | `my_tpt.tpt` | `from the TPT master file "my_tpt.tpt" (located in the current working directory)` |
| 落点 | `../my_device/` | `The device directory is located at the same level as the current working directory.` |

**按原文能确定的顺序：**

1. **让 `tpt_dir` 指的那个目录里有 TPT 文件。** 原文**没说 TPT 从哪来**；
   本篇只在静态目录那条里提到 `tpt_import_from_device` 的产物，**没说 TPT 只能这么来**。
2. **给 `device_dir` 挑一个还不存在、或者空的路径。** **这一步会决定命令成不成**——
   见上面的两种可接受状态。
3. **决定 `device_name`**（不填就是 `"device"`）。
4. **需要前后处理时再给 `pre_proc` / `post_proc`**（语法在别处，见上）。

**什么时候用它**：把一份模板变成一个新设备的工程骨架。**它是「新建设备」这条链上的一步**，
不参与测试执行——这也是本页 `stage: project` 的理由。

**本页没有的部分**：原文**没有 `## Procedure`、没有 `## Before you begin`、没有 `## What to do next`**，
所以**没有一条「先做 A 再做 B」是原文教的**——上面四步是从参数约束反推出来的，**（推断）**，
依据就是 `device_dir` 的那句 `must either not exist yet … or it must be empty`。

## 和谁有关

- [[stpm]]（**已建**）— 本命令**属于它**；原文称本命令是「for the SmarTest Program Manager (STPM) control file」的
- [[stpm-control-file]]（**已建**）— 命令**写在它里面**；**本页没读它**，
  所以**命令在控制文件里的书写位置、同一份文件里还有哪些命令**，本页全无
- [[tpt-import-from-device ]] — **上游**。它用 `copy_static_content` 把静态目录带进 TPT，
  **本命令再把它们复制进新 device directory**——**这是原文写明的唯一一处两命令交接**
- [[device-directory ]] — **产物**。本命令生成的就是它；**它长什么样、里面除 testflow 还有什么，本篇未写**
- [[preprocessing-and-postprocessing-scripts ]] — `pre_proc` / `post_proc` 的**语法在那儿**；
  **原文把这两个参数的说明整个外包给了它**，**本页没读**
- [[device-technology-directory ]] — **仅凭命名与阶段相邻**：
  同以 device 为单位的目录对象；**本篇原文没提它**，这一条不是文档事实

## 版本

原文**有** `## Functional changes` 段，六条：

- **Introduced in SmarTest 7.0.4**
- **SmarTest 7.2.1**：`Swapped the order of the device_dir and device_name parameters.`
- **SmarTest 7.2.1**：`Changed the default of the device_name parameter.`
- **SmarTest 7.2.1**：`Replaced the tpt_path parameter with tpt_dir.`
- **SmarTest 7.2.1**：`Renamed command to tpt_generate_device_dir.`
- **SmarTest 7.2.2**：`Added the pre_proc and post_proc parameters.`

**这一节比看上去重**：**SmarTest 7.2.1 一个版本里动了四处**——
**参数顺序**、**参数默认值**、**参数改名**（`tpt_path` → `tpt_dir`）、**命令自己改名**。
**四条挤在同一个版本号上，说明这个命令在 7.2.1 被整体重做过一遍。**

**三条需要点出来的边界：**

| 版本记录说的话 | **它没说的事** |
|---|---|
| `Renamed command to tpt_generate_device_dir.` | **旧名是什么——原文没写** |
| `Changed the default of the device_name parameter.` | **旧默认值是什么——原文没写**（现默认是 `"device"`） |
| `Replaced the tpt_path parameter with tpt_dir.` | **`tpt_path` 在新版本里是否还被接受——原文没写** |

**`tpt_path` 这个名字在整篇里只出现这一次**（就在版本记录里）——
**正文的 Syntax / Parameters 已经全部是 `tpt_dir`**，所以照旧文档写脚本的人会在这一条上撞到。

## 出处

`sources:` 一篇：
`02_System_reference/02.09_Test_Program_Management/02.09.02.03.16_tpt_generate_device_dir.md`

**本页没做的**：

- **`tpt_import_from_device` 那篇没读。** `copy_static_content` 参数**怎么用、能带进什么、静态目录指什么**，
  本页一个字没有——**本页只有「它带的目录会被复制过来」这一句原文**。
- **`STPM control file` 那篇没读。** 命令在控制文件里的**书写位置、调用上下文、同文件还有哪些命令**，本页全无。
- **`Preprocessing and postprocessing scripts` 那篇没读。** `pre_proc` / `post_proc`
  **的值怎么写、是不是文件路径、支持什么语言**，本页没有。
- **源文档里没有图**（那一篇正文里没有任何插图，也**没有 `Subtopics`** 那一层要查）。
  **所以本页没有任何来自图的结论。**
- **没有实跑。** `Example` 那一段只有一条例子，**本页没有扩充它、也没有在任何环境上执行过**——
  `verified: doc-only` 指的就是这件事。
- **`device_dir` 给非空目录会怎样，原文没写，本页也没查。**

> ⚠️ **本篇的语料瑕疵四处，本页照实记下、一处都没替它改**（语法节是逐字取的，**这些形态在页面上原样可见**）：
>
> ① **语法块的末行多一个 `]`**：
> `post_proc = <post_proc>]`
> ——**`[` 与 `]` 在块里不成对**（前面三个可选参数各自成对）。
> **同一处还自相矛盾**：参数说明里 `post_proc` 明写 `This is an optional parameter.`，
> **而语法块里它没有被 `[ ]` 括起来**。
>
> ② **语法块的行缩进不一致**：`tpt_dir` 那行**顶格**，其后各行**缩进四格**。原文如此。
>
> ③ **Example 里的 `tpt_dir` 少了逗号**：`tpt_dir     = 'my_tpt/'` 后面没有逗号，
> 而同一块里 `device_dir` / `device_name` 都有。
>
> ④ **Example 的说明与它自己的参数值对不上**。说明写的是从一个 **master file** 取：
> `from the TPT master file "my_tpt.tpt" (located in the current working directory)`
> 而例子给的是 `tpt_dir = 'my_tpt/'`，**`tpt_dir` 的定义却是「装 TPT 文件的目录」**：
> `<tpt_directory> (string) is the name and path of the directory containing the TPT files from which the device directory is to be generated.`
> **一个是「cwd 下的 `my_tpt.tpt` 文件」，一个是「cwd 下的 `my_tpt/` 子目录」——两处指的不是同一个位置。**
> **原文没有解释这个差异，本页不判谁对。**
>
> 另：**参数表在原文里是「表格被拍平成一格一行」的形态**（分隔符 ` |` 自己占一行），
> 语法节按原文抄，**本页没有替它重排**。

`verified: doc-only`
