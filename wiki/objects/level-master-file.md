---
type: object
title: Level setup master file
layer: file
stage: level
tags: [level, level-master-file, file-format, parallel-development, setup-management-tool, equation-set, testdata]
related: [level-file, level-equation-file, level-setup-tool, setup-management-tool, test-program-explorer, timing-master-file, device-directory, mapping-level]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.02.05_Level_setup_master_file.md
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02.04.04_Creating_a_level_master_file.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# Level setup master file

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **568 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.02.05_Level_setup_master_file.md>` 及其子主题 `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.02.05.01_Master_file_format_for_level_setup.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Master file format for level setup）

### Level master file

```
hp93000,level_master_file,0.1

# this is a comment
testerfile: demo.lev

EQNSET 1 [PIN_ALIAS_SET usb_set]: files/eqnset01.lev
EQNSET 2 : files/eqnset02.lev
EQNSET 3 : files/eqnset_34.lev
EQNSET 4 : files/eqnset_34.lev
TESTDATA : files/testdata.lev
DEFINES : files/defines.lev
GENERAL: GENERAL.lev
```

In the assembled level setup file `demo.lev`, the alias set `usb_set` is used in the equation set 1. When `demo.lev` is splitted, the alias set `usb_set` is removed from the generated sub-file `eqnset01.lev` and package pin names are used.

<!-- 语法节 end -->

## 是什么

**Level master file 不存电平值，它只存「指向」**——把一套 level setup 拆成多个文件之后，
用它把这几块串起来，并且**记着哪一号 equation set 在哪个文件里**。

定义文档 `02.08.04.14.02.05_Level_setup_master_file.md` 的正文就是这三句（本页逐句引，三句是连续的）：

> 「The level setup can be organized as one single file, or its individual level equation sets and testdata blocks (DFTD command) can be be stored in separate files.」

> 「In the latter case the parts that belong together are connected by a master file which contains references to the respective files.」

> 「This construction has the advantage that several users can work on the same level setup in parallel.」

**这三句里有三件事，要拆开说：**

1. **两种组织方式**：一个整体文件，或拆成「每个 equation set 一个文件 + testdata 块一个文件」。
2. **testdata 块在固件层是一条命令**：**`DFTD`**（原文自己点名，写在括号里）。
3. **拆的理由是并行开发**：`several users can work on the same level setup in parallel`
   ——这与 **[[setup-management-tool]]** 的定位是同一件事。
   （**推断**：两篇文档的 `## Related information` 都指向 Setup Management Tool，
   而那一页自己写的是「让多个用户在同一个 setup component 的不同部分并行工作、互不干扰」——
   **语料没有一句把 master file 与那个工具等同**，本页只并列，不合并。）

**⚠️ 第一句里的 `can be be stored` 是语料的原样**——`be` 重复了一次，
**本页照原样引，一处都没替它改**（§11.2）。

### 它的方向性：alias set 只活在「组装后」的那一份里

原文专门讲了 master file 里 `[PIN_ALIAS_SET usb_set]` 那个方括号的命运（两句连续）：

> 「In the assembled level setup file demo.lev, the alias set usb_set is used in the equation set 1.」

> 「When demo.lev is splitted, the alias set usb_set is removed from the generated sub-file eqnset01.lev and package pin names are used.」

**这句话定下了 master file 的方向性**：**pin alias set 只存在于组装后的整体文件里**；
**一旦拆开，子文件里没有 alias set，改用 package pin name**
（alias set 是什么见 [[level-setup-tool]] 与 [[equation-based-level-setup]]）。
**也就是说：并行改子文件的人拿到的不是别名，是包脚名。**

**⚠️ `splitted` 也是语料的原样**（标准写法是 `split`），照原样引。

### 文件里长什么样

**格式的完整例子在本页「语法 / 参数」节**（那是脚本逐字抽的，本页不重写）。这里只指出**怎么读它**：

| 那一行的形状 | 它是什么 |
|---|---|
| `hp93000,level_master_file,0.1` | 文件头：**格式名 + 版本号**（`level_master_file` 就是它的格式名） |
| `# this is a comment` | 注释 |
| `testerfile: demo.lev` | **组装后的那个整体 level setup 文件**（本页两篇 sources 里的「例子里叫 `demo.lev`、流程里叫 `levels`」指的就是这一格） |
| `EQNSET <n> [PIN_ALIAS_SET <set>]: <file>` | **每个 equation set 一行**；方括号里可以点名一个 pin alias set，不点名时冒号前留空 |
| `EQNSET 3` 与 `EQNSET 4` 指向同一个 `eqnset_34.lev` | **两个 equation set 可以共用同一个文件** |
| `TESTDATA : <file>` | testdata 块——对应上面那句里的 **`DFTD`** |
| `DEFINES : <file>` | defines 块 |
| `GENERAL: GENERAL.lev` | general 块 |

**`EQNSET <n> [PIN_ALIAS_SET <set>]: <file>` 这一格还有一个别处用得上的意义**：
同阶段的 [[mapping-level]] 把「选「equation set + spec set + level set」三个坐标」那一行的
**文件格**填成了**本页的 `EQNSET <n>: <file>` 条目**。**本页与它一致**（那一行本页也复述不出更多，
它的 L2 / L3 格是别的篇的事）。

**一处本页答不了的**：`GENERAL` 这条**本页的两篇 sources 里没有一句解释它**。
`mapping-level` 把「在 testflow 里切 set 时的先后顺序」落在它上面（`GENERAL.lev`），
**但那句依据在 `02.08.04.14.04.11.01`，本页没读**——所以本页只记「格式例子里有这一条」。

### ④ 图证：创建流程里那两张对话框

**这是本页 `sources:` 里唯一的两张图**（定义文档 `02.08.04.14.02.05` 自己 0 张图；
带图的是 `01.01.07.02.02.04.04_Creating_a_level_master_file.md`）。**两张本页都开了**：

| 图 | 对话框标题栏 | 图上逐字可见的东西 |
|---|---|---|
| `141712.png` | **`Select file to load`** | 左栏 `Places` 四项：`jspreux` / `Desktop` / `File System` / `jm_delme`；**路径面包屑 `jspreux > devices > mfh_74ACT299 > levels`**；`Name` 列里一行 `levels`（`Modified` 列写着 `Today`）；按钮 `Add` / `Remove`（都是灰的）；右下 `All Files` 下拉框；`OK` / `Cancel` |
| `141713.png` | **`Enter or select NEW file name`** | `Name:` 输入框里是 **`levels.mfh`**；`Save in folder:` 是 **`levels`**；`Browse for other folders`；`OK` / `Cancel` |

**图解决掉的两件事**：

1. **「加载 level setup 文件」与「Save As 成 `.mfh`」这两步各弹哪个窗口、长什么样。**
   正文只有两句祈使句（`Load the level setup file` / `Save the level setup file as file.mfh`），
   **窗口的标题、字段名、按钮名正文一个字没有**——图给了。
2. **device 目录长什么样。** 面包屑 `jspreux > devices > mfh_74ACT299 > levels` 把
   「device 目录 → `levels` 子目录」这条路径画出来了，**这正是流程第 3 步
   「Navigate to the **levels** subdirectory of your device directory」那句话的落点**（→ [[device-directory]]）。

**哪些字在 raw 里 grep 不到（§11.4 ④ 档的判据）**：

| 图上读到的串 | 9,398 篇 raw md 里的命中篇数 |
|---|---|
| **`Select file to load`** | **0** |
| **`mfh_74ACT299`** | **0** |
| **`jspreux`** | **0** |
| **`jm_delme`** | **0** |
| `Enter or select NEW file name` | 2（**但不在本页 `sources:` 里**） |
| `levels.mfh` | 1 |
| `Save Level setup`（`141713.png` 的 alt） | 2 |

**严格够「grep 不到」这条判据的是前四行。** **要核只能自己再开那两张图。**
——**这四串是示例里的名字**（一个示例 device 名 + 两个 `Places` 条目 + 一个对话框标题），
**不承载规格**，所以**本页不据此改动任何一句**；其中**唯一有意义的是 `Select file to load`**：
它说明第 1 步那个对话框是**通用文件选择框**，不是 level 专用框。

**图答不了的**：`.mfh` 的格式规范（图只给了文件名）、`## Procedure` 第 3 步生成的那五个文件
分别长什么样、`changelog.txt` 里冲突记成什么格式——**都没有**。

## 典型用法

### 创建流程（`01.01.07.02.02.04.04` 的 `## Procedure`，四步）

**先看前提**。`## About this task` 交代了做法：**用一个已经存在的 level setup 建 master file**，
那个参考文件叫 `levels`，里面有**两个 equation set**（`Equation set 1` / `Equation set 2`）。

`## Before you begin` 只有一句：

> 「Ensure that you have a device in place, load the pin configuration and the level setup file.」

**即 `level` 这一段的前置在这里被点名了：device 就位 + 加载 pin configuration + 加载 level setup 文件**
（→ [[pin-configuration-file]]）。

| # | 做什么 | 原文要点 |
|---|---|---|
| 1 | 从 Test Program Explorer 加载 level setup 文件 | 「If not already loaded, Load the level setup file from the Test Program Explorer as shown below.」（图 `141712.png`） |
| 2 | **Save As 成 `.mfh`** | 「Save the level setup file as file.mfh i.e levels.mfh as illustrated below.」（图 `141713.png`） |
| 3 | **到 device 目录的 `levels` 子目录，确认文件生成** | 「Navigate to the levels subdirectory of your device directory and verify that the following files are created.」 |
| 4 | `## What to do next` | 「Load the level master file levels.mfh or continue to create further setup files.」 |

**第 3 步要确认的五个文件（原文逐条列了说明）**：

| 文件 | 原文的说明（照原样引） |
|---|---|
| `changelog.txt` | 「contains information about conflicts that come up during the assembling of complex setups.」 |
| `eqnset_01.lev` | 「regular SmarTest level file containing only equation set 1.」 |
| `eqnset_02.lev` | 「regular SmarTest level file containing only equation set 2.」 |
| `levels` | 「regular SmarTest level file containing the complete level setup.」 |
| `levels.mfh` | 「level master file.」 |

**三件值得留意的事**：

- **`levels` 这个文件没有扩展名**——原文写的就是 `levels`。**它与 `levels.mfh` 是两个文件**
  （`141712.png` 的 `Name` 列里那个 `levels` 就是它）。
- **这两个子文件原文叫「regular SmarTest level file」**，**没有**用 [[level-equation-file]]
  这个名字。**本页不替语料改名**——那个名字是不是指这两个文件，本页没有依据可判。
- **`changelog.txt` 的存在说明「组装复杂 setup 时会出冲突」**——**它是什么冲突、怎么处置，
  原文没说**（`Editing the level and timing subfiles` 那篇可能讲，**本页没读**）。

### 一条省事的替代路径

> 「You can use the same creation procedure to create a master file for timing or for level setup.」

**即 timing 的 master file 用同一套步骤**（→ [[timing-master-file]]）。
**但本页只读了 level 那一侧的实例**，timing 侧的文件名、目录、生成物本页没有。

### 做完之后

`## Results` 的原话是：

> 「As a result, you have created a levels master file levels.mfh that references the eqnset_01.lev and eqnset_02.lev. See also Using the Setup Management Tool from the Test Program Explorer.」

并指向 `01.01.07.02.02.04.02_Using_the_Setup_Management_Tool_from_the_Test_Program_Explorer.md`
——**那篇本页没读**，所以「**怎么用它来做并行开发**」本页没有：
本页只知道**它存在、它是这个流程的下一步**（→ [[setup-management-tool]]）。

## 和谁有关

每条都说清**是什么关系**：

- [[setup-management-tool]] —— **同一目的的配套工具**。本页的原文说拆文件的理由是
  「多个用户可以在同一套 level setup 上并行工作」；那个工具管的是「多人改同一份 setup
  而不互相干扰」。**两篇文档的 `## Related information` 都指向它**，这是最硬的一条关系。
- [[level-file]] —— **它的下游（被指向的那一份）**。master file 的 `testerfile` 那一行
  指的就是组装后的整体 level setup 文件。
- [[level-equation-file]] —— **拆出来的子文件**（`eqnset_01.lev` 这种）。
  **本页的 sources 没有用这个名字**，只说它们是「regular SmarTest level file」——
  **两者的关系本页没判**。
- [[level-setup-tool]] —— **上游工具**。master file 是那个工具编出来的东西被拆开后的索引；
  `EQNSET` / `PIN_ALIAS_SET` 这两个关键字都出自那一侧的语法。
- [[test-program-explorer]] —— **创建流程的场所**：加载 level setup 文件、
  Save As 成 `.mfh`、第 4 步再加载 `levels.mfh`，**都在那儿**。
- [[device-directory]] —— **产物落点**：生成的五个文件都在 device 目录的 `levels` 子目录里
  （`141712.png` 的面包屑画的就是这条路径）。
- [[pin-configuration-file]] —— **前置**：`## Before you begin` 要求先加载 pin configuration。
- [[timing-master-file]] —— **同类（同一套流程的另一个实例）**。原文一句
  「the same creation procedure to create a master file for timing or for level setup」把它们钉在一起。
- [[testflow]] / [[sldo]] / [[fw-task]] —— **下游用法（本页无依据）**。
  `mapping-level` 把「在 testflow 里切 set 时的先后顺序」落在本页的 `GENERAL` 条目上，
  并把 L1 格填 [[sldo]]、L2 格填 [[fw-task]]——**那三格的依据在 `02.08.04.14.04.11.01`，
  本页没读**。本页只知道格式例子里有 `GENERAL: GENERAL.lev` 这一条。
- [[mapping-level]] —— **同阶段的对照表页**。本页与它一致（`EQNSET <n>: <file>` 是它那一行的
  文件格）；**没有冲突**。
- [[level]] —— 本页 `stage: level` 的理由：它是 level 阶段的一种产物文件。
- **定义文档自己声明的两个子主题**（`Master file format for level setup`，
  raw: `02.08.04.14.02.05.01_Master_file_format_for_level_setup.md`；`Editing the level and timing subfiles`，
  raw: `02.08.04.14.02.05.02_Editing_the_level_and_timing_subfiles.md`）—— **本页都没读**。
  它们是 master file 的格式规范与「怎么编辑子文件」，
  §9.1 第 4 条说这类子主题算「会存在的页」；但它们不在 `extract/prose-allowlist.txt` 里，
  **故按规矩用反引号 + raw 路径，不写双方括号**。

## 版本

**本页的两篇 sources 各有一条 `## Functional changes`，而且它们说的不是同一件事**：

- 定义文档 `02.08.04.14.02.05_Level_setup_master_file.md`：**`Introduced before SmarTest 6.3.2`**
- 创建流程文档 `01.01.07.02.02.04.04_Creating_a_level_master_file.md`：
  **`SmarTest 7.2.1: Added level master file creation procedure.`**

**⚠️ 第一条是 §11.2 ② 说的「哨兵值」，不是「6.3.2 新增了 master file」**——
它的意思是**在本文档集覆盖范围开始之前就已经有了**（见 [[smartest-6.3.2]]）。

**两条合起来能读出什么（推断，本页显式标）**：**master file 这个格式早于 6.3.2 就存在；
而「用 Save As 把它生成出来」这套创建流程是 SmarTest 7.2.1 才加进文档的**（→ [[smartest-7.2.1]]）。
**这个「格式早、流程晚」的读法是推断**——两条记录一条讲格式可用性、一条讲流程的新增，
**语料没有一句把它们连起来**，所以**本页并列两条，不合成一句**。

## 出处

`sources:` 两篇：

- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.02.05_Level_setup_master_file.md`
  （TDC `91598.htm`，**1,051 字节 / 22 行**）—— 定义文档。它的正文只有：`## Subtopics` 两项、
  上面引的那一段（三句）、`## Related information` 一项、`## Functional changes` 一条。
- `01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02.04.04_Creating_a_level_master_file.md`
  （TDC `141711.htm`，**2,090 字节 / 45 行**）—— 创建流程。`## About this task` / `## Before you begin` /
  `## Procedure` / `## Results` / `## What to do next` / `## Related information` / `## Functional changes`。

**本页「语法 / 参数」节那 568 字符不是来自定义文档自己**——段名里写着来源是子主题
`02.08.04.14.02.05.01_Master_file_format_for_level_setup.md`。

**本页没做的**：

- **定义文档声明的两个子主题一篇都没读**：`Master file format for level setup`（`02.08.04.14.02.05.01`）、
  `Editing the level and timing subfiles`（`02.08.04.14.02.05.02`）。
  **所以本页没有格式规范**——哪些条目必填、哪些条目可省、`GENERAL` / `DEFINES` 各装什么、
  注释与大小写规则，**本页一个字都没有**，本页只有「怎么读语法节那个例子」。
- **没有读任何命令文档**：`DFTD`、`EQSP`、`EQFS` 只作为**定义文档原文里的串**出现，
  **它们的参数、语法、返回值本页没有**。
- **`## Results` 指的那一篇没读**：`01.01.07.02.02.04.02_Using_the_Setup_Management_Tool_from_the_Test_Program_Explorer`。
- **`mapping-level` 放在本页 `GENERAL` 条目上那句依据（`02.08.04.14.04.11.01`）没读**——
  所以「`GENERAL` 是不是切 set 顺序的落点」，**本页只转述对照表页的填法，不声称是文档事实**。
- **看完了本页 sources 的全部两张图**：`141712.png`、`141713.png`
  （逐字内容与 grep 结果见「④ 图证」那一节）。
  **定义文档 `02.08.04.14.02.05_Level_setup_master_file.md` 自己 0 张图**
  （实测 0 处 `raw/` 引用），**所以本页 sources 里的图总共就这两张，本页全看了**。
- **没有实跑**：没有建过 `.mfh`、没有在 device 目录里看过那五个生成物。
  `verified: doc-only` 指的就是这件事。
- **没有动 `wiki/index.md`**，也没有把本页挂进 `wiki/stages/level.md`。

**⚠️ 本页读到的语料瑕疵，照原样记下、一处都没替它改（§11.2）**：

- **`can be be stored`**（定义文档第一句）——**`be` 重复**。本页照原样引了，见「是什么」。
  全库 grep：含 `be be stored` 的 raw md **3 篇**。
- **`When demo.lev is splitted`**（定义文档）——**`splitted` 不是标准过去分词**（应为 `split`）。
  本页照原样引了，见「是什么」。
- **同一个东西在同一篇里有两种文件名写法**：格式例子用**无下划线**的 `eqnset01.lev` / `eqnset02.lev`，
  同一例子里又用**有下划线**的 `eqnset_34.lev`；而创建流程那篇用的是**有下划线**的
  `eqnset_01.lev` / `eqnset_02.lev`。全库 grep：`eqnset01.lev` **2 篇**、`eqnset_01.lev` **3 篇**。
  **本页不替它统一，照原样并列。**
- **格式例子里冒号前的空格不一致**：`EQNSET 2 : files/eqnset02.lev` 冒号前有空格，
  而 `GENERAL: GENERAL.lev` 冒号前没有——**同一份例子里两种写法**。
- **`Save the level setup file as file.mfh i.e levels.mfh as illustrated below.`**——
  **`i.e` 后面缺逗号**；而且 **`file.mfh` 明显是占位符，原文没有把它标出来**
  （读起来像两个不同的文件名）。
- **`## Results` 那句把类型名与文件名挤在一起**（原句逐字引如下）——**照实记，不改**：

> 「As a result, you have created a levels master file levels.mfh that references the eqnset_01.lev and eqnset_02.lev.」

- **一句话中间的 `Load` 用了大写**：`If not already loaded, Load the level setup file from the Test Program Explorer as shown below.`——**与同一篇 `## Before you begin` 里的 `load the pin configuration` 小写不一致**（原文如此）。本页在「典型用法」表里照原样引了。
- **`## Functional changes` 里 `## Results` / `## What to do next` 与 `## Related information`
  都链到同一个 `Setup Management Tool`**——**一篇里指了同一个目标三次**。
  本页照实记，**不判它错**（那是语料的导航习惯）。

**本页检查过、但本页没遇到的瑕疵**：**本页两篇 sources 里一个汉字坏字都没有**
（实测 `[一-鿿]` 各 0 处，故 §11.2 ① 的 `碌` / `渭` / `卤` / `鈥` 一族在本页不存在）；
**§11.2 ⑤ 的整词替换本页两篇实测 0 处**（那一族的坏串形如 `DC/DC power units`——
**它是被替换坏的 `Index`，不是一个可用的名字，不许抄进任何代码**），
故**本页没有任何坏标识符可记**。

**引文规范化的说明**：本页引用块里的英文，**除 §11.1 允许的六条**（折叠空白、剥 markdown 链接标记、
去 `**` 与反引号、去中日韩引号、统一破折号、统一弯引号）**之外，一个字符都没动**；
`## Results` 那句里的语料内部链接（原文是 `See also [链接文字](<目标路径>)` 的形式）
**按第 ② 条剥成了纯文本**（`链接文字` 照原样保留），本页**没有改写它的任何一个词**。

`verified: doc-only`
