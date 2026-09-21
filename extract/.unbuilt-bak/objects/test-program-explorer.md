---
type: object
title: Test Program Explorer
layer: gui
stage: project
tags: [gui, setup, work-center, explorer, setup-perspective, load-save]
related: [setup-perspective, setup-management-tool, pin-configuration-tool, pattern-tool, pattern-explorer, project-explorer-view, shmoo-tool, integrated-result-tool]
sources:
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02_Test_Program_Explorer.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# Test Program Explorer

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **5,825 字符逐字取自** `<01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02_Test_Program_Explorer.md>` 及其子主题 `<01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02.01.08.02_When_merging_levels.md>`、`<01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02.03.01_Customized_hp83_import_for_encrypted_setup_files.md>`、`<01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02.04.05_Collision_handling.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example 1（取自子主题 Working with Test Program Explorer › Appending a file to a loaded file  Merge › When merging levels）

Levels loaded before merging: SET 1,SET 2

Levels in the file that will be merged: SET 1

Merging the file results in:

Levels loaded: SET 1, SET 2

where SET 1 is the set of the merged file (the previous SET 1 got replaced), and SET 2 is unchanged.

### Example 2（取自子主题 Working with Test Program Explorer › Appending a file to a loaded file  Merge › When merging levels）

Levels loaded before merging: SET 1, SET 2

Levels in the file that will be merged: SET 1, SET2, SET3

Merging the file results in:

Levels loaded: SET 1, SET 2, SET 3

where SET 1 and SET 2 are the sets of the merged file (the previous SET 1 and SET 2 were replaced), and SET 3 is the appended SET 3 of the merged file.

### Example（取自子主题 Protection for your setup files › Customized hp83 import for encrypted setup files）

The following code example, which assumes that the encryption pass word is "VERIGY93K", shows a possible implementation:

```
/*
 *-- system includes ------------------------------------------------------
 */
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
/*
 *-- module include -------------------------------------------------------
 */
#include "tpi_c.h"
#include "ci_types.h"
#include "libcicpi.h"
/*
 *-- defines -------------------------------------------------------------
 */
#define SA_PROCESS_INFO "/opt/hp93000/soc/pws/bin/saprocessinfo -sep ' '"
/*
 *-- globals variables ----------------------------------------------------
 */
/*
 *-- functions ------------------------------------------------------------
 */
int securityChecks()
{
    FILE *fd;
    char command[1024+1];
    char output[1024+1];

    fprintf(stderr, "\n\n");
    /**************************************************/
    /**          Are we online or offline?           **/
    /**************************************************/
    INT32 mode;
    GetOnlineMode(&mode);
    fprintf(stderr, "Online?\t\t\t%ld\t(0 = offline, 1 = online)\n", mode);
    /**************************************************/
    /**          Which user mode?                    **/
    /**************************************************/
    long usermode;
    GetUserMode(&usermode);
    fprintf(stderr, "Usermode?\t\t%ld\t(Protected mode has value 5)\n", usermode);
    if(5 != usermode) {
      return -1;
    }

    /**************************************************/
    /**          Who has called us?                  **/
    /**************************************************/
    fprintf(stderr, "The pid of our parent is %d\n", getppid());
    /**************************************************/
    /**Is our caller registered with the SmarTest SW?**/
    /**************************************************/
    sprintf(command,"%s| grep SA_PRC_TF | awk {'print $3'}", SA_PROCESS_INFO);
    fd=popen(command, "r");
    int registered_pid;

    fgets(output, 1024, fd);
    sscanf(output,"%d", &registered_pid);

    fprintf(stderr, "Pid registered for TF: %d\n", registered_pid);
    fclose(fd);

    if(registered_pid != getppid()) {
      return -1;
    }
    /**************************************************/
    /**        md5sum of our parent                  **/
    /**************************************************/
    sprintf(command, "md5sum /proc/%d/exe", getppid());
    fd=popen(command, "r");
    char temp[1024+1];
    fgets(output, 1024, fd);
    char md5sum[32+1];
    sscanf(output, "%s %s", md5sum, temp);
    fprintf(stderr, "md5sum of parent:\t%s\n", md5sum);
    fclose(fd);

    /**************************************************/
    /**            location of our parent            **/
    /**************************************************/
    sprintf(command, "/proc/%d/exe", getppid());
    int length=readlink(command, output, 1024);
    output[length]=0;
    fprintf(stderr, "loc of parent:\t\t%s\n", output);

    /**************************************************/
    /**   working directory of our parent            **/
    /**************************************************/
    sprintf(command, "/proc/%d/cwd", getppid());
    length=readlink(command, output, 1024);
    output[length]=0;
    fprintf(stderr, "cwd of parent:\t\t%s\n", output);
    /**************************************************/
    /**   root directory of our parent            **/
    /**************************************************/
    sprintf(command, "/proc/%d//", getppid());
    length=readlink(command, output, 1024);
    output[length]=0;
    fprintf(stderr, "root of parent:\t\t%s\n", output);
    return 0;
}
void decrypt(int argc, char* argv[])
{
  if(-1 == securityChecks()) {
    return;
  }
  char command[1024+1];
  if(0 == strcmp(argv[2], "config")) {
    fprintf(stderr, "Loading pins...\n");
    sprintf(command, "echo %s | ccrypt -c -k - %s", "VERIGY93K", argv[1]);
    system(command);
  }
  else if(0 == strcmp(argv[2], "level")) {
    fprintf(stderr, "Loading levels...\n");
    sprintf(command, "echo %s | ccrypt -c -k - %s", "VERIGY93K", argv[1]);
    system(command);
  }
  else if(0 == strcmp(argv[2], "timing")) {
    fprintf(stderr, "Loading timing...\n");
    sprintf(command, "echo %s | ccrypt -c -k - %s", "VERIGY93K", argv[1]);
    system(command);
  }
}
void plain(int argc, char* argv[])
{
  char command[1024+1];
  if(strstr(argv[1], ".gz")) {
    sprintf(command, "gunzip -c %s", argv[1]);
  }
  else if(strstr(argv[1], ".Z")) {
    sprintf(command, "uncompress -c %s", argv[1]);
  }
  else {
    sprintf(command, "cat %s", argv[1]);
  }
  system(command);
}
int main(int argc, char* argv[])
{
    HpInit();
    if(argc == 5) {
      if(0 == strcmp(argv[2], "config")) {
    decrypt(argc, argv);
      }
      else if(0 == strcmp(argv[2], "level")) {
    decrypt(argc, argv);
      }
      else if(0 == strcmp(argv[2], "timing")) {
    decrypt(argc, argv);
      }
      else {
    plain(argc, argv);
      }
    }
    exit(CI_CALL_PASS);                /* program completed without error */
    HpTerm();
}
```

### Example（取自子主题 Setup Management Tool › Collision handling）

See the examples in each kind of setup master file collision handling.

<!-- 语法节 end -->

## 是什么

> **一句话**：**Test Program Explorer 是 setup 数据的那棵树，也是打开所有 setup 工具的那个入口。**

它是 `Setup perspective` 的一部分，而**载入 setup 数据这件事就走它这道门**。
「它现在是什么状态」全写在树上——**一个组件显示成什么样子，就说明它加载了没有、改过没有、属于不属于当前 device。**

原文第一句把「在哪」和「是什么」一起说了：

> The Test Program Explorer is included in the Setup perspective and provides a hierarchical view of the test setup data.

它是树，**同时也是启动器**——树上的节点背后是各个 device setup 工具：

> From here, you call up all the device setup tools like the Pin Configuration Tool, the Pattern Tool etc.

### 关键机制：它是 setup 数据「从磁盘进测试系统」的那道门

这是本页最该记住的一句机制话，原文只写了这一句：

> When you load the setup data using the Test Program Explorer, the data will be loaded from the file system of the system controller to the test system.

**方向要记牢：来源是「系统控制器的文件系统」，去处是「测试系统」。**（文档事实）
**怎么载、能载哪几类、能不能只载一半——原文没写（语料未写）。**

### 树上每个节点显示成什么，是三种状态在说话

**这是本页最实用的一张表。** 同一个节点，显示成什么样子，意思完全不同：

| 树上看到 | 意思 | 原文（逐字） |
|---|---|---|
| **显示文件名**，而不是组件名（原文举的例是 `<Levels...>`） | **那个数据文件已加载** | `If a file name is displayed instead of the component (for example, <Levels...>), the related data file is loaded.` |
| 文件名旁有 **`*`** | **数据被改过、还没保存** | `If the symbol * is displayed besides the file name, the data was changed and not yet saved.` |
| 文件名旁有 **`[external]`** | 加载的这个组件**不属于当前 active device** | `If the text [external] is displayed besides the file name, a component is loaded that does not belong to the active device.` |

原文还给了一个配对例子——**同一张图里一个加载了、一个没加载**：

> In the figure above for example the vector file is loaded (file name vectors_func_first) and the pin attributes file is not loaded.

**⚠️ 第一行那个「例」本页读不通**（见下）：括号里的 `<Levels...>` 被放在「显示的是文件名」那一侧，**可它看着像组件名的占位写法**（(推断)：原文别处把 `Pin Configuration` 这类叫 setup component，依据是 `Double-click any setup component to open the relating setup tool.` 那句）。**两种读法都通，原文没说清，本页不判、也不替它改。**

**另外这三个记号怎么消除，原文只写了一个**：`*` 靠**保存**消（见下「工具栏」），`[external]` 和「加载了没有」**原文没有说该怎么办**（语料未写）。

### 双击 = 打开对应的 setup 工具

> Double-click any setup component to open the relating setup tool.

> An example: When you double-click the Pin Configuration, then the Pin Configuration Tool is opened.

**这是原文给出的唯一一个交互**（(推断)：依据是全文只有这一处讲「怎么从树进到工具」）。**右键菜单、拖拽、搜索框之类本页语料未写。**

### 这棵树里也挂结果文件

> The Test Program Explorer also displays some result files like shmoo data.

**(推断) 这棵树同时挂 setup 与 result 两类东西**——依据是这一句，加上 `## Functional changes` 里 7.0.3 那条 `Bitmap result data is no longer displayed in the Test Program Explorer.`：**「结果数据」这一类曾经更多，7.0.3 把 bitmap 那一部分摘掉了**，剩下 shmoo 这类还在。**具体哪几类结果文件会显示，语料未写。**

### 工具栏：四个图标

原文只有一句引入语，后面跟一张**两列（图标 / 功能）的表**：

> The toolbar of the Test Program Explorer View contains the following icons:

按 raw 里的**相邻顺序**读（**那张表在 raw 里已经被拆散，配对只能按相邻读**，见「出处」②）：

| 图标（原文的 alt 文本） | 功能（逐字） |
|---|---|
| `Test program explorer view - collapse button` | `Collapses all test setup components.` |
| `Test program explorer view - save button` | `Only save the test setup components which are the modified and not yet saved, or save all the loaded test setup components.` |
| `Test program explorer view - expand button` | `Expands all test setup components.` |
| `Navigator view - menu button` | `Provides menu items for expanding and collapsing all test setup components.` |

两条要点：

- **save 图标的行为是「两选一」，而且可以配**：原文把两种行为写在**同一句**里——`Only save the test setup components which are the modified and not yet saved, or save all the loaded test setup components.`；原文另有一句 `You can set the behavior of this icon in Test Program Explorer preference page.`（那篇本页没读）。(推断) 也就是说**「点一下存什么」不是固定的**，取决于那个 preference——依据就是这句话本身。
- **收 / 放整棵树有两条路**：两个专用图标（collapse / expand），**外加**第 4 个图标的菜单项（`Provides menu items for expanding and collapsing all test setup components.`）。

### 这棵树的层级长什么样：**语料未写**

树有几层、按什么分组、每组底下挂什么——**原文一句没写**。
原文只**举了四个名字**：`Levels...`、`Pin Configuration`、`vector file`、`pin attributes file`。
**没有分类清单，也没有组件表。** 所以「这棵树的全貌」本页给不出——**要全貌得看那五张图，本页一张没看**（见「出处」）。

## 典型用法

**先把一句话说清：原文没有 `## Procedure`，也没有 `## Before you begin`。**
所以下面这条顺序是**本页按原文散句编排的（推断）**，序号即原文出现的先后，**不是原文给的流程**。

1. **在 `Setup perspective` 里找到它**——它是那个 perspective 的一部分（原文第一句）。
2. **载入 setup 数据**——**这一步就是这道门的作用**：数据从系统控制器的文件系统进到测试系统。
3. **看树上的三个记号**（`*` / `[external]` / 显示的是文件名还是组件名）判断当前状态——见「是什么」里那张表。
4. **双击一个组件** → 打开对应的 setup 工具（原文的例子：双击 `Pin Configuration`，打开 Pin Configuration Tool）。
5. **改完要保存**：点 save 图标；**存什么（只存脏的还是全存）在 `Test Program Explorer preference page` 里设**（那篇本页没读）。(推断) **存之前那个 `*` 不会消失**——依据是 `*` 的定义就是 `changed and not yet saved`。
6. **收 / 放整棵树**：collapse / expand 两个图标，或第 4 个图标里的菜单项。
7. **要看结果文件**（如 shmoo data）也从这棵树进。

**三种常见组合：**

- **setup 与结果在同一棵树里看**——原文：`The Test Program Explorer also displays some result files like shmoo data.`
- **换 device / 换项目时先找 `[external]`**：(推断) 这个记号是「这个组件不属于当前 active device」的提醒，**别的 device 的 setup 被一起载进来时它会亮**——依据是那句的定义；**原文没有说看到它该怎么办**。
- **拿不准加载了没有 → 看显示的是文件名还是组件名**（原文那条 `instead of the component`）。

## 和谁有关

**每条都标了是什么关系**：

- [[setup-perspective]]（**未建**）— **容器 / 前置**：原文第一句说 Explorer 是**它的**一部分
- [[setup-management-tool]] — **子主题**：原文 `## Subtopics` 的第四条（那篇文档本页没读，页已建）
- `Working with Test Program Explorer` / `Customizable Scripts` / `Protection for your setup files`（**均未建**）— 另外三个子主题。**其中两篇的示例被脚本抄进了本页的「语法 / 参数」节**（段名里的「取自子主题」就是它们）
  - raw: `01.01.07.02.02.01_Working_with_Test_Program_Explorer.md`
  - raw: `01.01.07.02.02.02_Customizable_Scripts.md`
  - raw: `01.01.07.02.02.03_Protection_for_your_setup_files.md`
- [[pin-configuration-tool]] / [[pattern-tool]]（**均未建**）— **下游工具**：原文举的两个「从这里调起的 device setup 工具」
- `Test Program Explorer preference page`（**未建**）— **配置处**：save 图标的行为在这儿设（raw: `01.01.14.25_Test_Program_Explorer_preference_page.md`）
- [[project-explorer-view]] / [[pattern-explorer]]（前者**未建**）— **同类（推断）**：本页语料**没有提到它们**，只按「Explorer = 一棵树」这个命名同族列在这里
- [[shmoo-tool]] / [[integrated-result-tool]] — **结果侧（推断）**：原文只说这棵树 `also displays some result files like shmoo data`；**shmoo 结果本身在哪个工具里看，本页语料没写**
- [[vector-setup-file]]（**推断，依据很薄**）— 原文那句 `the vector file is loaded (file name vectors_func_first)` 里的 `vector file` 名字对得上；**原文没说它是不是这个对象**
- [[smartest-6.5.4]] / [[smartest-7.0.3]] / [[smartest-7.1.0]] / [[smartest-6.3.2]] — **时间轴上的邻居**：本页「版本」那几条各自的归宿

## 版本

原文**有** `## Functional changes` 段，共 5 条，**逐字如下**（原文是列表项）：

- **哨兵值**：`Introduced before SmarTest 6.3.2`
- **SmarTest 6.5.4**：`Channel attributes added to Device Information.`
- **SmarTest 7.0.3**：`Test control removed from Test Program Explorer.`
- **SmarTest 7.0.3**：`Bitmap result data is no longer displayed in the Test Program Explorer.`
- **SmarTest 7.1.0**：`Protocols and Protocol Assignments added.`

**第一条不是「6.3.2 新增」，是哨兵值。** 措辞是 `before`——意思是**在本文档集覆盖范围开始之前就已经有了**（§11.2 ②）。
**照字面读会生成一条「6.3.2 新增了 Test Program Explorer」的假信息，而且格式齐整。** 本页不这么读。这条的归宿见 [[smartest-6.3.2]]。

**另外两点：**

- **7.0.3 有两条，两条都是「拿走」**（`Test control removed from Test Program Explorer.`、`Bitmap result data is no longer displayed in the Test Program Explorer.`）——**这个视图在 7.0.3 变窄了**（文档事实，原文如此）。**「为什么拿走」原文没说。** (推断) `Test control` 大概是树上的测试控制入口，但**原文只有一个词，本页不展开**。
- **7.1.0 新增的 `Protocols` 与 `Protocol Assignments` 是什么，本页语料没写**——原文只给了这两个名字。

## 出处

`sources:` 一篇：
`01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02_Test_Program_Explorer.md`

**本页没做的**：

- **四个子主题文档一篇没读**：`01.01.07.02.02.01_Working_with_Test_Program_Explorer.md`、`01.01.07.02.02.02_Customizable_Scripts.md`、`01.01.07.02.02.03_Protection_for_your_setup_files.md`、`01.01.07.02.02.04_Setup_Management_Tool.md`。所以**「怎么在这棵树里干活」的细节（文件合并、加密导入、碰撞处置）本页一个字都没有**——底下「语法 / 参数」节里确实有它们的三段示例，**但那是脚本抄的，不是本页读的**。
- **`Setup perspective` 那篇没读**（raw: `01.01.07.02_Setup_perspective.md`）——**Explorer 在那个 perspective 里的位置、旁边还有哪些视图，本页没有。**
- **`Test Program Explorer preference page` 那篇没读**（raw: `01.01.14.25_Test_Program_Explorer_preference_page.md`）——**save 图标的行为到底是哪几种、默认哪一种，本页不知道**，只知道「可以在那儿设」。
- **五张图一张没看**（`123063.png` 主视图、`91718.png` collapse、`101679.png` save、`91717.png` expand、`91711.png` menu）。**本页没有任何来自图的结论**——**连四个图标长什么样都不知道，只有 alt 文本。**
- **没有实跑**：没在任何 SmarTest 上打开过这棵树。`verified: doc-only`。「文档里有」≠「这台机器上能用」（§11）。
- **树的全貌没有**：层级、分组、组件清单本页都给不出，原因同上（原文没写 + 图没看）。

**关于「语法 / 参数」节：本节非空，但「定义文档自己的语法段」是空的。**

- 本节四段**全部带「取自子主题」后缀**：`Working with Test Program Explorer › Appending a file to a loaded file  Merge › When merging levels`（2 段）、`Protection for your setup files › Customized hp83 import for encrypted setup files`（1 段）、`Setup Management Tool › Collision handling`（1 段）。**定义文档自己一段都没有。**
- 抽取实测（本页作者跑的，只读不写）：定义文档的 `verbatim_sections()` 返回**空**，`collect_syntax()` 于是走「其他子主题的段」那一层、取回 4 段；定义文档的 `table_runs()` 也返回**空**。
- **⚠️ 这就是「空 ≠ 没有参数」在本页的具体形态**：**定义文档里真有一张参数样子的表——工具栏四个图标 + 各自的功能**（raw 第 33–65 行）——**它没有进这一节**，因为它在 raw 里已经被 HTML→md 转换拆散，**没有连续 ≥3 行的管道行**（脚本只收连续 ≥3 行）。**要看那张表，回 raw 第 33 行起**；「是什么」里那张表是**按 raw 的相邻行手工转的，不是脚本抽的**。
- **(推断)** 本节四段讲的**都不是 Explorer 本身**：一眼能看出的依据是段名里的子主题路径——**Levels 合并**、**hp83 加密导入**、**setup master file 碰撞**，分别属于另外三个对象。**「这四段为什么会出现在这一页」是脚本的落空回退，不是原文说 Explorer 有这些示例。**

> ⚠️ **本篇的语料毛病，本页照实记下、一处都没替它改**：

**① `## Functional changes` 的第一条是哨兵值**，**不是「6.3.2 新增」**：

> Introduced before SmarTest 6.3.2

措辞是 `before`（§11.2 ② 的同一件事）。本页「版本」一节按哨兵读。

**② 工具栏那张两列表，在 raw 里是散的。** 表头只剩四行**孤立**的管道行（` |`、`Icon`、` |`、`Function`），**每个图标行与它下面的功能说明之间都夹着空行**——整张表从头到尾**没有连续 ≥3 行的管道行**（实测 `table_runs()` 返回空）。**「图标 ↔ 功能」的配对只能按相邻读**；本页「是什么」里就是这么排的，**没有替它补表、也没有把两格合成一行。**

**③ `besides` 用了两次**，按上下文应为 `beside`：

> If the symbol * is displayed besides the file name, the data was changed and not yet saved.

> If the text [external] is displayed besides the file name, a component is loaded that does not belong to the active device.

**原文如此，本页照抄。**

**④ 第四个图标的 alt 文本跟另外三个不是一族**：三个都以 `Test program explorer view - ` 开头（注意 `program` 是小写），第四个叫 `Navigator view - menu button`——**同一张表里两种命名。**

**⑤ `(for example, <Levels...>)` 一处有两个毛病。** 一是**角括号没有转义**——(推断) 多数渲染器会把它当成 HTML 标签吃掉，依据是 raw 里它就是裸的 `<Levels...>`；二是**那个 `...` 是原文自带的省略写法**，本页照抄，**没有换成 `…`**。**另外**（见「是什么」）：这个例子被放在「显示的是文件名」那一侧，**而 `Levels...` 看着像组件名的占位写法**——**两种读法都通，原文没说清，本页不判。**

`verified: doc-only`
