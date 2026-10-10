---
type: object
title: Device directory structure
layer: file
stage: project
tags: [project, device, directory-structure, file-layout, subdirectory]
related: [device-technology-directory, new-device-wizard, project-explorer-view, test-program-explorer, setup-perspective, technology-file-for-a-device, tpt-generate-device-dir]
sources:
  - 01_Getting_started/01.07_Testing_a_Basic_Digital_Device/01.07.01.01.01_Device_directory_structure.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# Device directory structure

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

**没有加标记的语法段。** 定义文档里没有 `Syntax` / `Parameters` / `Example`
这类**段标记**，跟着 `Subtopics` 找一层也没有。
**所以本脚本一个字都不收录**——没有段标记时「哪一段是语法」是猜，而猜就是编（§4）。

<!-- 语法节 end -->

## 是什么

**device directory（device 工程目录）就是建一个 device 时生成的那个目录**——
本页讲的是**它下面有哪些子目录**。原文对这一层的说明只有一句：

> 「The device directory includes a number of subdirectories.」

**这一篇文档实际给的东西只有四样**：① 一条查看命令（`cd` + `ls -al`）；② 一份**例子的**目录清单；
③ 从 GUI 看它的两个视图；④ 两条版本记录。
**每个子目录「是干什么用的」，本文档一个字都没写**——本页也没有（见「和谁有关」与「出处」）。

### 怎么看它（原文只给了一条命令）

> 「Take a look at the generated device structure:」

> 「In a terminal window, change into the device project directory you just created (for example, my_74ACT299_tp) with the command cd and type the command ls -al.」

`my_74ACT299_tp` 是原文举的**例子名**，不是固定名字。

### 例子清单里的 29 个子目录

下面这些名字**取自**原文那份 `ls -al` 输出的最后一列——**这是转录，不是逐字引文**
（本页的逐字引文只有上面那两句）：

| | | |
|---|---|---|
| `.settings` | `analog_control` | `applicat` |
| `calibration` | `ch_attributes` | `configuration` |
| `data_set` | `di_report` | `error_map` |
| `format` | `levels` | `license` |
| `pin_attributes` | `profiles` | `report` |
| `routing` | `scan_res` | `shmoo` |
| `testflow` | `testfunc` | `testmethod` |
| `testprog` | `testtable` | `timing` |
| `timing_dgrm` | `vectors` | `wafertyp` |
| `waste` | `waveform` | |

同一份输出里还有**三个不是目录**的条目（另有 `ls -al` 固定带的 `.` 与 `..` 两行）：

| 条目 | 权限 | 大小 |
|---|---|---|
| `.project` | `-rw-r--r--` | 484 |
| `.technology` | `-rw-r--r--` | 213 |
| `lock_file` | `-rw-rw-rw-` | 42 |

**⚠️ 限定（文档事实）**：原文只说 `includes a number of subdirectories`，
**没说这 29 个是全部、也没说它们都必须存在**。这份清单是**某一次、某一台机器**上的样子——
例子里的日期就能看出来：除 `applicat`（`Nov  2  2010`）、`shmoo`（`May  3  2010`）、
`configuration` / `levels` / `testflow`（`Jul  5  2011`）、`timing`（`Jul  7  2011`）
和 `lock_file`（`Aug  1 13:18`）之外，**其余条目都是 `Apr 30  2010`**。

**（推断）这份例子大约抓在某年 8 月前后。** 依据：`lock_file` 的日期是 `Aug  1 13:18`，
**没有年份**，而 `ls -l` 对**半年内**改过的文件显示时刻、对更早的显示年份；
清单里最新的目录日期是 `Jul  7  2011`，所以抓取时间落在 **2011-08 到 2012-02** 之间。
**文档自己没写抓取时间**，这条是我按 `ls` 的显示规则推的。

**（推断）逐行的 `<user name>` / `<user group>` 是脱敏占位符。** 依据：`ls -al` 在这个位置
打印的是真实的用户名与组名，而原文**每一行**都是尖括号包着的通用词。
**原文如此，本页照抄，不替它填。**

### 从 GUI 看同一份结构（原文只点了两个视图）

> 「From the SmarTest Setup Perspective observe the content of the structure in the Project Explorer view and in the Test Program Explorer view:」

这句下面原文挂了一张**两列的表**，两列各一张截图（`Project Explorer view` 与 `Test Program Explorer view`）。
**两张图本页都没看**，所以**本页没有任何来自图的结论**——那两个视图长什么样、树有几层、
device 目录在树里怎么显示，**本页都不知道，只知道名字**。
那张表的 markdown 已经转坏了（管道符单独成行），**照实记在「出处」**。

## 典型用法

**原文只给了两条路。整篇没有 `## Procedure`、也没有 `## Before you begin`**
（二级节只有 `## Related information` 与 `## Functional changes` 两个）：

| 想干什么 | 原文给的步骤 |
|---|---|
| **看目录清单**（在文件系统里） | 终端里 `cd` 进刚建好的 device 工程目录（例子：`my_74ACT299_tp`）→ 敲 `ls -al` |
| **看结构**（在 GUI 里） | 进 **SmarTest Setup Perspective** → 看 `Project Explorer view` 与 `Test Program Explorer view` |

**没有第三步。** 原文既没说该拿这份清单做什么，也没说目录缺了/多了会怎样。

**一个前提（推断）**：两条路都假设 **device 已经建好了**——命令那句写的是
`the device project directory you just created`，视图那句也要求人已经在 Setup Perspective 里。
**「怎么建一个 device」不在这篇文档里**（它只出现在 `## Related information` 的第一个链接）。

## 和谁有关

### A. 本页 raw 的 `## Related information` 给了 5 条

四条有链接、一条只有文字。四条链接的目标路径**我核对过，在语料里都存在**（含
`01.02_SmarTest_workstation_administration` 的小写目录名）：

| 链接文本 | raw 里的目标 | wiki 里有没有对应的页 |
|---|---|---|
| `Creating a new device` | `../01.01_SmarTest_Work_Center/01.01.10.03.01_Creating_a_new_device.md` | **没有同名页**；wiki 里「建 device 的 GUI 入口」叫 `[[new-device-wizard]]`（**未建**）——**只是名字不同，本页不判两者是否同一篇** |
| `Device Technology Directory` | `../01.01_SmarTest_Work_Center/01.01.07.02.01.01_Device_Technology_Directory.md` | `[[device-technology-directory]]`（**未建**） |
| `SmarTest directory structure` | `01.07.01.01.02_SmarTest_directory_structure.md` | **没有**。它是本页 raw 的**同目录兄弟**（同一篇的第 2 篇） |
| `SmarTest Software Base Directory` | `../01.02_SmarTest_workstation_administration/01.02.02.02.01_SmarTest_Software_Base_Directory.md` | **没有** |
| `SmarTest temporary directory` | **原文没有给链接** | — |

**这五篇一篇都没读**（见「出处」）。所以**device 目录与兄弟目录（SmarTest 目录、软件 base 目录、
technology 模板目录、临时目录）的异同，本页一个字都没有。**

> 顺带记一个**事实**（不改、也不判）：本页 raw 的**同目录**下另有一篇
> `01.07.01.01_Creating_a_new_device.md`（同一篇走查的第 2 篇），
> **而 `## Related information` 里的 `Creating a new device` 指的是 `01.01_SmarTest_Work_Center/`
> 下的那篇，不是同目录这篇。** 两篇是什么关系，**本页没读、不判。**

### B. 正文点到的两个视图

- `Project Explorer view` → `[[project-explorer-view]]`（**未建**）——本页 raw 的正文点名了它。
- `Test Program Explorer view` → `[[test-program-explorer]]`（**已建**，`gui/project`）——
  **raw 写的是 `view`，页名没有 `view`**。
- `SmarTest Setup Perspective` → `[[setup-perspective]]`（**未建**）——原文那句就是从这个
  perspective 说起。**这一步的对应是 wiki 的判断，不是本页 raw 写的**：`wiki/stages/project.md`
  把 `[[setup-perspective]]` 记成默认 perspective（两个 view 都含在里面）。

### C. wiki 内部给的关系（**这几条的出处是别的 wiki 页，不是本页 raw**，逐条标了）

- `[[tpt-generate-device-dir]]`（已建）—— **生成**本页描述的那个目录。
  依据：该页自己写着 `[[device-directory]]（未建）— 产物。本命令生成的就是它`。**上游。**
- `[[technology-file-for-a-device]]`（已建）—— **`.technology` 是 device 目录的成员**
  （本页例子清单里就有它）。依据：该页写着 `.technology` 住在 device 目录里。
  **同类（同目录成员）。**
- `[[device-technology-directory]]`（未建）—— **建 device 时用它初始化 device 目录里的子目录结构**。
  依据：`wiki/stages/project.md`。**上游（模板）。** 它同时是本页 raw 的一条 Related information。
- `[[new-device-wizard]]`（未建）—— **建出这个目录的 GUI 入口**。依据：`wiki/stages/project.md`。**上游。**

### D. 入边：本页现在是 9 篇页面的出边目标

`grep` 到 **11 处 `[[device-directory]]`**，落在 **9 篇**里：
`data-logging-profiles`、`pin-configuration-file`、`stpm`、`stpm-control-file`、
`technology-file-for-a-device`、`tmlimits`、`tpt-generate-device-dir`、
`stages/project.md`（2 处）、`mappings/mapping-project.md`（2 处）。

**这 9 篇本页一篇都没读**——所以它们各自说 device 目录什么，**本页不知道，也不往本页搬**。
（有两条从链接旁边的原话就能看出关系：`tmlimits` 说 `testtable/` 是相对**当前** device directory 的；
`data-logging-profiles` 说 `profiles/` 挂在 device 目录下面。**这两句是它们写的，不是本页 raw 写的。**）

## 版本

原文 `## Functional changes` 段两条，逐字：

> 「- Introduced before SmarTest 6.3.2」

> 「- SmarTest 7.2.2: The testtable subdirectory is created in the device directory when creating a new device.」

**第一条是哨兵值，不是「6.3.2 的变更」**（本 wiki 的规矩，见 `wiki/schema.md` §11.2②）：
`Introduced before …` 的意思是「**在本文档集覆盖范围开始之前就已经有了**」。
**照字面读会得到一条假信息**——「SmarTest 6.3.2 新增了 device directory」，
而且格式齐整、看上去很可信。**所以本页不这么写。**
（对照：`[[smartest-6.3.2]]` 页上并**没有**「新增 device directory」这样一条。）

**第二条是真正的功能变更**：**`[[smartest-7.2.2]]` 起，新建设备时会在 device 目录里建
`testtable` 子目录**。也就是说这条讲的是 **`testtable` 这个子目录何时开始自动出现**，
不是目录结构整体何时引入。

例子清单里**已经有 `testtable`**（日期 `Apr 30  2010`）——但**那份清单是哪一版 SmarTest 建的，
文档没写**，所以**本页不拿它去对这条版本记录**。

## 出处

`sources:` 一篇：
`01_Getting_started/01.07_Testing_a_Basic_Digital_Device/01.07.01.01.01_Device_directory_structure.md`
（TDC `130830.htm`，**3,894 字节 / 74 行**）。

### 「语法 / 参数」节是空的——**空 ≠ 没有内容**

这篇文档里**根本没有 `Syntax` / `Parameters` / `Example` 这类段标记**：
整篇只有三个标题——`# Device directory structure`、`## Related information`、`## Functional changes`。
没有段标记，脚本就一个字都不收，**这是脚本的正确行为，不是这页缺东西**（§4）。

**但它并不是没东西可抄。** 本页真正的「参数」就是**那份 29 个目录名的清单**——
它躺在文档正文那段**没有标题的** `ls -al` 输出里。**没有标题时「哪一段是语法」是猜，
而猜就是编**，所以脚本拒绝收它。那份清单由我抄进「是什么」一节，
**并且明说了那是转录、不是逐字引文**。

### 本页没做的

- **两张图一张没看**：`raw/91705.png`（`Project Explorer view`）、`raw/123063.png`（`Test Program Explorer view`）。
  **本页没有任何来自图的结论**——那两个视图长什么样、树有几层、device 目录在树里的哪一层，
  **本页都不知道，只知道名字**。
- **`## Related information` 指向的 4 篇一篇都没读**：
  `01.01.10.03.01_Creating_a_new_device.md`、`01.01.07.02.01.01_Device_Technology_Directory.md`、
  `01.07.01.01.02_SmarTest_directory_structure.md`、`01.02.02.02.01_SmarTest_Software_Base_Directory.md`，
  也没有去找第 5 条 `SmarTest temporary directory` 到底指哪一篇。
  **所以「device 目录的结构」和「SmarTest 自己的目录结构」是什么关系，本页一个字都没有。**
- **那 29 个子目录各自是干什么的，本页一个字都没写**——**不是我省略了，是这篇文档没写**。
  「和谁有关」C 节里那几条「某某住在 device 目录下」的边，**出处是别的 wiki 页，不是本页 raw**。
- **引用了本页的 9 篇 wiki 页一篇都没读**（清单见「和谁有关」D 节）。
- **没在任何真实机器上跑过 `cd` / `ls -al`**，也没在任何 SmarTest 上打开过那两个视图。
  所有关于例子的判断都只在纸上。**`verified: doc-only`。**

### ⚠️ 语料瑕疵（照实记，一处都没替它改）

**① 本篇一个坏字都没有。** `file` 报它是 `ASCII text, with CRLF line terminators`——**纯 ASCII**。
对照全语料 **11.2% 的篇数含坏字**（`wiki/schema.md` §11.2①），**这一篇是干净的那一类**。
所以本页没有 `碌`/`渭`/`卤`/`鈥慴` 之类的字要记。

**② `## Related information` 那 5 条被压成了一行，第 5 条连链接都没有。**
那一行 **448 字符**，**5 条之间没有任何分隔符、没有列表符、没有换行**。
按 §11.1② 剥掉链接标记后，逐字是这样（**连在一起就是原文的样子**）：

> 「Creating a new deviceDevice Technology DirectorySmarTest directory structureSmarTest Software Base DirectorySmarTest temporary directory」

而且**前 4 条有链接目标、第 5 条 `SmarTest temporary directory` 只有文字、没有链接**。
**原文如此**，本页不替它补分隔符、也不替第 5 条补链接。

**③ 那句视图的说明下面，表格被转坏了。** 管道符单独成行（` |`），
两列的表头（`Project Explorer view` / `Test Program Explorer view`）和两个截图被分在两处，
**按 markdown 根本渲染不出表**。**原文如此**，本页照记。

**④ `ls -al` 那份输出里混着两个空行**，位置固定：`scan_res` 与 `shmoo` 之间一个、
`shmoo` 与 `testflow` 之间一个。**真实的 `ls -al` 输出不会凭空多出空行**，
所以这是转写时进来的（`shmoo` 也正好是清单里唯一一个 `May` 日期的条目）。**原文如此**，本页照记。

**⑤ （推断）`.` 那一行的链接数对不上清单。** `.` 行写的是 `drwxr-xr-x 29`，
而清单里**数得出 29 个子目录**（含 `.settings`）；按 Unix 的目录链接数约定
（`.` 的链接数 = 子目录数 + 2），这里**应该是 31**。旁证：紧随其后的 `..` 行写 `4`，
正好是「2 个子目录 + 2」。**两种读法本页都留着**：可能是这份清单**被裁过或手工编过**，
也可能是**所在文件系统没有精确维护这个计数**。**本页不判。**
—— 但这足以说明一件事：**那 29 个名字是例子，不是规范清单**（原文自己也没说它完整）。

> 另记一条（**属于 wiki 仓库、不属于语料**）：`wiki/objects/tpt-generate-device-dir.md`
> 里写的是 `[[device-directory]]（未建）`，而本页现在已经建了——**那句话是它写的时候的状态**。
> **本页没有改它**（改别人的页要单独做）。

`verified: doc-only`
