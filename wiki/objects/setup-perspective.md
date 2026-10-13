---
type: object
title: Setup perspective
layer: gui
stage: project
tags: [gui, setup, perspective, work-center, eclipse, default-perspective, view-container]
related: [project, test-program-explorer, project-explorer-view, setup-management-tool]
sources:
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02_Setup_perspective.md
created: 2026-09-21
updated: 2026-09-21
verified: doc-only
---

> ⚠️ **本页若干处记的是 2026-10-10【之前】的语料形态。**
> 那一轮把语料里的表格一律换成了**指向上游 HTML 的指针**
> （见 `extract/PLAN-表格指针化.md`）。所以下文凡是说「表格被压平 / 被摊平 /
> 一格一行」的地方，指的是**更换之前**的样子 —— 现在语料里那个位置是**一句指针**，
> 真表仍在 `tdc-html/raw/` 的上游 HTML 里。**页码/引文都不受影响。**

# Setup perspective

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **5,256 字符逐字取自** `<01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02_Setup_perspective.md>` 及其子主题 `<01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02.03.01_Customized_hp83_import_for_encrypted_setup_files.md>`、`<01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02.04.05_Collision_handling.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Test Program Explorer › Protection for your setup files › Customized hp83 import for encrypted setup files）

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

### Example（取自子主题 Test Program Explorer › Setup Management Tool › Collision handling）

See the examples in each kind of setup master file collision handling.

<!-- 语法节 end -->

## 是什么

**Setup perspective 是 SmarTest 的默认透视图，也是第一次启动 SmarTest 时活动的那一个。**
原文两句话就是它的全部定义：

> 「The setup perspective is the default perspective, which is active when SmarTest is started for
> the first time. The setup perspective contains the views necessary to edit the SmarTest setup data.」

**三个要点，一个都不能漏**：

| 原文写的 | 意思 |
|---|---|
| `the default perspective` | **它是默认值**，不是「若干个可选项之一」 |
| `active when SmarTest is started for the first time` | **首次启动时它就在前台** |
| `contains the views necessary to edit the SmarTest setup data` | **它是一个「view 的容器」**，装的正好是编辑 setup 数据需要的那批 |

**所以本页的性质是「一个容器 + 一张清单」**：Setup perspective 自己**不讲任何机制**，
它只讲**里面装了哪九个 view、每个 view 干什么**。原文也**没有** `## Procedure` /
`## Before you begin` 之类的操作节（见「典型用法」）。

### 原文列的九个 view（9 个，本页数的）

| # | view | 原文给的职责 |
|---|---|---|
| 1 | **Test Program Explorer** | 层次化显示所有测试数据的逻辑结构；**「从这里启动所有编辑 device setup 数据的工具」** |
| 2 | **Project Explorer** | 树状显示 test method project 与 class；可从这里新建 |
| 3 | `Properties` | 显示当前高亮对象的属性——原文举的例是「test method project 的位置与修改日期」 |
| 4 | `Outline` | 显示编辑器里打开文件的大纲，**内容随当前编辑器而变** |
| 5 | `Help view` | 基于 TDC Viewer；上下文帮助按 `Shift+F1`；打开它在菜单上点 `Help > Help Content` |
| 6 | `Problems View` | 列表显示错误/警告**及它们的位置**；双击一条，光标跳到编辑器里那一行 |
| 7 | `Firmware view` | 在上面执行 firmware 命令 |
| 8 | `Console view` | 显示**与某个测试系统资源（test data component）相关**的错误 |
| 9 | `Error Log View` | 显示**来自测试系统与 Eclipse 插件的全部**错误 |

**第 8 与第 9 项的差别要看清楚**：`Console view` 是**按资源筛的**，
`Error Log View` 是**全量的**。原文对这两条的措辞只差这一点。

**表里第 3–9 项写的是反引号，而不是双方括号的 wikilink**：这七个名字不在
`extract/prose-allowlist.txt` 里，也就是**本 wiki 不打算给它们建页**——
链一个清单外的名字等于造一个永远悬空的死链（§9.1）。**只有前两项有页可链。**

### 一处最容易看漏的结构差异

原文这九项**不是同一等级的介绍**：

- **前两项**（Test Program Explorer / Project Explorer）各有一条独立的 `- [名字](链接)` 加独立段落说明。
- **从第 3 项 `Properties` 起，原文的排版散了**——逐字是这样写的：

  > `- [Properties](<…Testflow_Properties_view.md>)`
  > `- This view shows the properties of an object that you are highlighting.`

  **说明句自己带了一个 `- `**，成了和「Properties」**同级**的一条列表项。
- **`Outline` 与 `Help view` 连链接都没有**，说明各自变成一个独立段落；
  `Firmware view` / `Console view` / `Error Log View` 又变回带链接的列表项。

**这是语料排版的问题，不是内容的问题**——逐字证据见「出处」的 ⚠️ ②。

### 唯一一条与「默认状态」有关的变更

整个 `## Functional changes` 段里只有一条讲 view 的默认可见性：

> 「SmarTest 6.5.2: The Firmware view is visible by default」

**（推断）反过来说，6.5.2 之前 `Firmware view` 不是默认显示的**——
推断依据是「版本段把『默认可见』记成一条变更」，**原文只写了变更之后的那个状态，没有写变更之前是什么样**。

### 一张图，本页没看

原文带一张截图，alt 文本是 `V93000 Setup Perspective`（raw: `../../../../raw/91473.png`）。
**本页没看这张图**，所以「九个 view 在屏幕上各占哪一栏、怎么摆」**本页一个字都没有**。

## 典型用法

**这一篇没有操作节。** 原文没有 `## Procedure`、没有 `## Before you begin`、没有 `## Results`。
把三件常问的事对一下：

| 你想干的事 | 本篇给不给 |
|---|---|
| 「怎么切到 / 切出 Setup perspective」 | **不给。** 原文只说还有别的 perspective（`available perspectives`），细节推给了父篇 `Perspectives` |
| 「怎么把 view 加进来 / 挪位置 / 复位」 | **不给。** 推给了 `Working with a perspective` |
| 本篇唯一一条可以照做的操作 | **`Help view` 那两个动作**：按 `Shift+F1` 取上下文帮助；菜单 `Help > Help Content` 打开 TDC Viewer |

**原文推出去的两篇（`Perspectives`、`Working with a perspective`）本页都没读**，
所以上面两行「不给」是**事实**，不是省略（见「出处」）。

**一条使用上的判断**：**因为它是默认 perspective，所以「我在哪个 perspective 里」这件事
在刚启动时不需要想**——原文说 `active when SmarTest is started for the first time`。
**但本篇没有写「之后怎么回来」**，那在父篇里。

## 和谁有关

- [[project]] — **本页 `stage: project` 的理由**：原文说它装的是「编辑 SmarTest setup 数据」所需的那组 view。
- [[test-program-explorer]] — 本页列的**第一个** view；原文说**所有编辑 device setup 数据的工具都从它启动**，
  所以它是这一页通向 setup 编辑侧的入口。
- [[project-explorer-view]] — 本页列的**第二个** view；**本页只转述「它显示 test method project 与 class」**，
  它自己的工具栏、图标、右键菜单**在它自己那一页**。
- [[setup-management-tool]] — **这条关系是从本页「语法 / 参数」节看出来的**：
  那一节两个 Example 的来源是 `Test Program Explorer › Setup Management Tool › Collision handling`
  与 `Test Program Explorer › Protection for your setup files › Customized hp83 import for encrypted setup files`，
  **说明 Setup perspective 的子树里包含 [[setup-management-tool]]**。
  这也解释了**本页「语法 / 参数」节为什么会出现 hp83 加密导入与 collision handling 两段和 perspective 无关的代码**。
- **清单外、本页不链（用反引号写名字）**：`Properties`、`Outline`、`Help view`、
  `Problems View`、`Firmware view`、`Console view`、`Error Log View` ——
  这七个名字**不在 `prose-allowlist.txt` 里**。
- 父篇 `Perspectives`（`01.01.07`）、`Working with a perspective`（`01.01.07.01`）、
  `V93000 Tool Bar`（`01.01.10`）—— **本页都没读**。
- **原文没有列出「还有哪些 perspective」**，所以**其他 perspective 页与本页的关系，本页不能下结论**；
  能确认的只有一句：**Setup perspective 是默认的那一个**。

## 版本

原文 `## Functional changes` 段两条：

| 条目 | 读法 |
|---|---|
| `Introduced before SmarTest 6.3.2` | **哨兵值，不是「6.3.2 的变更」**——它的意思是「**在本文档集覆盖范围开始之前就已经有了**」（§11.2 ②）。**照字面读会生成一条「6.3.2 新增了 Setup perspective」的假信息，而且格式齐整。** |
| `SmarTest 6.5.2: The Firmware view is visible by default` | **本篇唯一一条真正的功能变更** |

## 出处

`sources:` 一篇：
`01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02_Setup_perspective.md`（TDC `91689.htm`）

**本页没做的**：

- **父篇 `01.01.07_Perspectives` 没读**——批次注意事项明令不许把它的内容吸进来。
  所以「perspective 是什么、怎么打开 / 保存 / 复位、一共有哪几个」**本页一个字都没有**。
- **九个 view 各自的专页一篇没读**：`01.01.07.02.02_Test_Program_Explorer`、
  `01.01.08.02_Project_Explorer_view`、`01.01.08.09_Problems_View`、`01.01.08.08_Firmware_view`、
  `01.01.08.05.01_Console_view__System_console`、`01.01.08.07_Error_Log_View`、
  `Testflow_Properties_view`、`Pattern editor properties view`。
  **本页对每个 view 只有原文那一句话**——它们各自长什么样、能做什么，本页没有。
- **子主题 `01.01.07.02.01_Device_Technology_Defaults` 没读**，
  所以 `Device Technology Defaults` 是什么、它下面有什么，本页没有。
- **`Related information` 的两篇没读**：`Working with a perspective`、`V93000 Tool Bar`。
- **图 `raw/91473.png`（`V93000 Setup Perspective`）没看**——
  **本页没有任何来自图的结论**，九个 view 的实际布局不知道。
- **本页没在真机上看过这个 perspective**（`verified: doc-only`）。
  原文里九个 view 有没有装、装在哪一栏，都是文档事实，不是本机事实。

> ⚠️ **本篇的三处语料瑕疵，本页照实记下、一处都没替它改**：
>
> ① **`Error Log View` 那一条里 `displays` 重复、`form` 应为 `from`**（逐字引）：
> `This view displays displays all errors coming form the test system and from Eclipse plug-ins.`
>
> ② **列表被压平**：`Properties` 的说明句自带 `- `，成了与「Properties」**同级**的列表项——
> 逐字是 `- This view shows the properties of an object that you are highlighting.`；
> 而 `Outline` 与 `Help view` 这两项**连链接都没有**（同批的另外七项都是 `[名字](链接)` 的形状）。
>
> ③ **`## Related information` 里两个链接中间没有任何分隔符**（逐字引）：
> `[Working with a perspective](<01.01.07.01_Working_with_a_perspective.md>)[V93000 Tool Bar](<01.01.10_V93000_Tool_Bar.md>)`

**另记一条口径，不是语料的错、但读这一页必须知道**：
本页「语法 / 参数」节的两段 Example **不是本篇 source 的内容**——
它们逐字来自 `01.01.07.02.02.03.01_Customized_hp83_import_for_encrypted_setup_files.md`
与 `01.01.07.02.02.04.05_Collision_handling.md`，即 **Test Program Explorer 子树下面更深的地方**
（**这两篇本页也没读**）。脚本顺着 `Subtopics` 往下走时把它们抄了进来。
**所以别把「Setup perspective」这一页读成「Setup perspective 与 hp83 加密导入有关」。**

`verified: doc-only`
