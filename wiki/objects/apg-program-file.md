---
type: object
title: APG program file
layer: file
stage: pattern
tags: [mtp, apg, mtl, file-format, program-code, pattern-compile]
related: [apg-pattern-file, device-access-file, device-architecture-file, maintenance-operations, pattern]
sources:
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03_APG_program_file.md
created: 2026-09-18
updated: 2026-09-20
verified: doc-only
---

# APG program file

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **2,540 字符逐字取自** `<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03_APG_program_file.md>` 及其子主题 `<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01_APG_program_file_syntax.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### APG program file syntax（整篇，取自子主题）

# APG program file syntax

#### Subtopics

- `Operators`（raw: `02.12.03.03.03.01.01_Operators.md`）
- `Loops`（raw: `02.12.03.03.03.01.02_Loops.md`）
- `Conditional execution`（raw: `02.12.03.03.03.01.03_Conditional_execution.md`）
- `Other control structures`（raw: `02.12.03.03.03.01.04_Other_control_structures.md`）
- `Variables`（raw: `02.12.03.03.03.01.05_Variables.md`）
- `Values`（raw: `02.12.03.03.03.01.06_Values.md`）
- `Subroutines`（raw: `02.12.03.03.03.01.07_Subroutines.md`）
- `Macros and functions in program files`（raw: `02.12.03.03.03.01.08_Macros_and_functions_in_program_files.md`）
- `Array in MTL`（raw: `02.12.03.03.03.01.09_Array_in_MTL.md`）

The syntax in the APG program file differs from that of the MTL configuration files. It is closely related to that of the C programming language.

## Syntax

The APG program file syntax supports a subset of the C syntax. All supported syntax elements are identical to the corresponding elements of C.

In particular, you can use in APG program files:

- All pre-processor statements (such as `#include`) supported by C
- The operators listed in `Operators`（raw: `02.12.03.03.03.01.01_Operators.md`）.
- `For` loops and if statements
- Subroutine definitions and calls
- Arrays
- `DC_EVENT() and DC_EVENT_RANGE()`（raw: `02.12.03.03.03.01.08_Macros_and_functions_in_program_files.md`）, predefined calls similar to subroutine calls
- Macros, function-like constructs that process data based on the current settings in the `APG pattern file`（raw: `02.12.03.03.02_APG_pattern_file.md`）

Some prominent elements of the C language that are not available:

- Data typing exclude the array data type
- Pointers and addresses
- Loops other than `for` loops
- Functions returning values

### Example

```
// solid.prog

#include "../../device_defs/access_defs/ddr3_operations.inc"
#include "../basic_access_sequences.inc"

main ()
{

// for debugging purposes un-comment the next 3 lines for a small core...
#define zStop 4
// #define yStop 64
// #define xstop 128

   for (bank=zStart; bank<zStop; bank+=1)
   {
      WriteBackground(bank,DW1,DW2,DW3,DW4,DW5,DW6,DW7,DW8);
      ReadBackground(bank,DW1,DW2,DW3,DW4,DW5,DW6,DW7,DW8);
   }

   for (bank=zStart; bank<zStop; bank+=1)
   {
      WriteBackground(bank,IDW1,IDW2,IDW3,IDW4,IDW5,IDW6,IDW7,IDW8);
      ReadBackground(bank,IDW1,IDW2,IDW3,IDW4,IDW5,IDW6,IDW7,IDW8);
   }

  pad(EndProgPad){}
}

//*************************************************/
//**** Subroutines ********************************/
//*************************************************/

EndProgPad()
{
  CLK(); CTRL(1,1); DES(); DBUS_IDLE();
}
```

<!-- 语法节 end -->

## 是什么

**APG program file 是「真正被编译成测试图形的那段代码」的载体。** 原文第一句：

> 「The APG program file contains the actual code from which the test pattern is compiled.
> It may also contain reusable maintenance operations.」

**扩展名 `.prog`**（`The program file has the .prog file name extension.`）。
**由 [[apg-pattern-file]] 用 `:apgProgram:` 关键字指过来**——
也就是说 **`.prog` 自己不知道别的文件在哪，路径是在 `.apg` 里写的**。

### 语言：C 的一个子集，**支持与不支持的都是闭合清单**

「语法 / 参数」节（**取自子主题 `02.12.03.03.03.01_APG_program_file_syntax.md`**）把边界划得很清：

> 「The APG program file syntax supports a subset of the C syntax. All supported syntax elements are
> identical to the corresponding elements of C.」

**能用**（原文逐条列举）：

- All pre-processor statements (such as `#include`) supported by C
- The operators listed in `Operators`
- `For` loops and if statements
- Subroutine definitions and calls
- Arrays
- `DC_EVENT() and DC_EVENT_RANGE()`，predefined calls similar to subroutine calls
- Macros（`function-like constructs that process data based on the current settings in the APG pattern file`）

**不能用**（原文逐条列举）：

- Data typing exclude the array data type
- Pointers and addresses
- Loops other than `for` loops
- Functions returning values

> **这张「不能用」的清单比「能用」那张更有用**——**写 C 的习惯里，
> 除了 `for` 之外的循环、返回值、指针，全都不能用**。
> **原文说「不能用」的就这几样，别的没提**（即：没提 ≠ 保证能用）。

「语法 / 参数」节开头还有一句值得单记：

> 「The syntax in the APG program file **differs from** that of the MTL configuration files.
> It is **closely related to** that of the C programming language.」

**即：同一个 MTL 家族里，`.prog` 和 `.apg`/`.dvac` 那些不是一套语法。**
`.apg`/`.dvac` 用 `:keyword: { … }` 表格式语法，`.prog` 用 C 语法。

### 一条铁律：**必须有且只有一个 `main()`**

> 「The program file **must contain one** `main()` function and **can contain any number of
> subroutines that are called by name from** `main()`.」

**唯一的例外**就是下面这条 maintenance routine 规则——**例外原文自己标了 `Note Exception:`**。

### 例外：**只有维护例程、没有 `main()`** 的 `.prog`

这是本页最容易漏掉的一段。原文分两步说：

1. **常态**：维护例程（maintenance routine）就是普通子程序。
   > 「Maintenance routines are subroutines that are called for refresh maintenance operations.
   > They are defined in the APG program file like normal subroutines.
   > **Maintenance routines must not expect parameters to be passed to them.**」
2. **特例**：
   > 「If an APG program file contains just a maintenance routine (that is, **no `main()` function**),
   > this routine is compiled into a reusable maintenance routine.」

**判据是「文件里有没有 `main()`」，不是「这个子程序叫什么」**（推断——原文的判据写的就是
`contains just a maintenance routine (that is, no main() function)`，
**「只是」与「没有 main()」在原文里是同一件事的两种说法**）。

**反向也成立**：`Note Exception` 那句说
`If a program contains just a subfunction that is not passed any parameters, you can use it to
compile a reusable maintenance operation` ——**条件有两条：只有一个子函数、且它不接参数**。

### 示例里能读出的两件事

原文 `## Example` 是一段完整的 `solid.prog`。**本页不逐行讲**，只提两处：

- 它以 `#include` 起头（`"../../device_defs/access_defs/ddr3_operations.inc"`、
  `"../basic_access_sequences.inc"`）——**`#include` 的路径也是相对的**。
  **相对谁，本篇没写**（推断：`APG pattern file` 那篇说别的路径是
  `relative to the active directory`，但**本篇没说 `.prog` 里的 `#include` 是不是同一基准**）。
- 结尾的 `pad(EndProgPad){}` 调的是**文件末尾定义的子程序** `EndProgPad()`——
  **子程序可以定义在 `main()` 之后**（示例就是这么写的）。

### 那张文件依赖小图（**④ 图证，2026-09-20 补**）

本篇开头那张图是 `102176.png`（251×151，**alt 文字写 `.prog file highlighted`**）。
**图上没有图例**，raw 里也没有一句解释它，所以能读的只有两层：**框上的字**、
**哪个框跟哪个框连着**。**框里的字画在像素里，raw 里 grep 不到**——要核只能自己开
`F:\master-dev\dorm-wsl-sytest\tdc-html\raw\102176.png`。

- **9 个框摆成 3×3**，框里写的是文件扩展名：
  上排 `.tim` / `.dvar` / `.dac`，中排 `.wmap` / `.apg` / `.prog`，下排 `.pin` / `.pmap` / `.dcev`。
  **本图把 `.prog` 涂成橙色**（同一张图在那一族的 9 篇文档里各出现一次，每次换一个框高亮）。
- **`.prog` 那个框的边上数得出 5 处线头**（按像素逐边数的）：
  **上面 2 条**（都在最右列，也就是都通到 `.dac`）、
  **左面 2 条**（并排，通到 `.apg`）、**下面 1 条**（通到最右列的 `.dcev`）、**右面 0 条**。
- **`.prog` 与 `.dvar` 之间没有直接连线**——`.dvar` 在中间那一列，
  而 `.prog` 上面那两条线都在最右列。

**这一条对本页的一处推断有用**：原文说 `.prog` `can also contain device parameters from the
Device architecture file`，而本页推断「这个引用应该在 `.apg` 里声明，但本篇没写」——
**图上 `.prog` 与 `.dvar` 之间确实没有直接连线**。
**但这只能算「不矛盾」，不算证据**：图里没有一处文字说明那些线是什么意思，
**「没有直接连线」等不等于「引用不在 `.prog` 里声明」，图答不了**（推断）。

**图没答掉的**：`#include` 的相对基准（图里没有 `.inc` 这类框）；
**线型（实线 / 点线）与箭头方向的含义**——图里没有图例，那几篇文档里 grep
`dotted line` / `solid line` 也是 0 命中，**本页不猜**；
**`main()` 与维护例程编译出来的东西落在哪儿**（图里也没有 maintenance 类的框）。

## 典型用法

**原文没有 `## Procedure` / `## Before you begin` 段**，它是一篇格式说明。
从原文能读出来的顺序只有这一条链：

1. **写 `.prog`**：C 子集语法，**一个 `main()`**（或只放一个维护例程，见上）。
2. **写 `.apg`**，用 `:apgProgram:` 指向它（**`.prog` 自己不被直接编译**）。
3. **编译**——**怎么编译本篇一个字没写**，`apgc` 命令那篇本页没读。

**两种用法，选哪种看你要什么**：

| 你要什么 | `.prog` 里放什么 | 结果 |
|---|---|---|
| **一个测试图形** | `main()` + 任意多个子程序 | 编译成测试图形 |
| **一个可复用的维护例程** | **只有那个子程序，没有 `main()`**，且**它不接参数** | 编译成 reusable maintenance routine |

**写维护例程的两条硬约束**（原文都写了）：

- **不能期待参数传进来**（`must not expect parameters to be passed to them`）。
- 它服务的对象是 **refresh maintenance operations**——即编译好的例程**再被 `.apg` 的
  `:maintenanceOperation:` 按名引用**（这条连接关系在 [[apg-pattern-file]] 那一侧）。

## 和谁有关

- [[apg-pattern-file]] — **上游**。`:apgProgram:` 从那里指过来；
  **`.prog` 的路径、以及它用到的 device parameters 的来源，都在 `.apg` 里交代**
- [[device-architecture-file]] — **参数来源**。原文：
  `It can also contain device parameters from the Device architecture file.`
  **注意是「参数」，不是路径**——**`.prog` 里能直接用设备参数，但原文没说这个引用在哪声明**
  （推断：应该是在 `.apg` 里，但**本篇没写**）
- [[device-access-file]] — **被调用方**。原文在那一篇里说
  `The device access defined in the device access file are called from the APG program file.`
  ——**`.prog` 里那些 `WriteBackground(...)` / `ReadBackground(...)` 就是 device access 调用**（推断，
  依据是示例里这些名字和 `.dvac` 示例里的 `:name: write_access` / `read_access` 同一族）
- [[maintenance-operations]] — **产物去向**。只有维护例程的 `.prog` 编译成
  reusable maintenance routine，**服务的正是这一类操作**
- `MTL Configuration Files`（**未建**）— 原文 `## Related information` 只指向这一篇；
  **本页没读它**
- **九篇语法子主题一篇都没读**：`Operators` / `Loops` / `Conditional execution` /
  `Other control structures` / `Variables` / `Values` / `Subroutines` /
  `Macros and functions in program files` / `Array in MTL`——
  **它们列在「语法 / 参数」节最上面那个 `#### Subtopics` 里**，
  **本页对它们只有标题**，**一条语法规则都没有**
- [[pattern]] — ★ **概念上的上游**：`.prog` 编译出来的东西就是 93K 的 pattern；
  **但原文没有把这两者连起来说**，**本条是关系提示，不是文档事实**（推断）

## 版本

原文 `## Functional changes` 只有一条：

- **`Introduced before SmarTest 6.3.2`**

**就这一条，没有别的。**

> ⚠️ **§11.2② 说过：这是哨兵值，不是「6.3.2 新增」。**
> 它的意思是「在本文档集覆盖范围开始之前就已经有了」。
> **照字面读会得到一条「6.3.2 引入了 APG program file」的假信息，而且格式齐整。**
>
> **顺带一个对照**（**来自我读的另一篇，不是本篇的结论**）：
> 同一批的 [[apg-pattern-file]] 有三条 `Functional changes`（其中两条是 MTP 2.6.6 / 3.0.3），
> **而本篇只有哨兵值那一条**——**所以「`.prog` 的格式此后没变过」这种话不能从本篇推出来**，
> 只能说明本文档没记。（推断）

## 出处

`sources:` 一篇：
`02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03_APG_program_file.md`
（`67572.htm`，2,971 字节，77 行）——**整篇读完**。

**本页做了什么、没做什么**：

- **「语法 / 参数」节不是 `sources:` 那篇抽的。** 那篇自己**没有完整语法段**，
  脚本改从子主题 `02.12.03.03.03.01_APG_program_file_syntax.md` 抄了 **2,540 字符**（骨架段名里写明了）。
  **那一篇本页没有读原文**——本节凡引语法节内容，依据是**页内那段逐字拷贝**。
- **九篇语法子主题一篇都没读**（`Operators` / `Loops` / `Conditional execution` /
  `Other control structures` / `Variables` / `Values` / `Subroutines` /
  `Macros and functions in program files` / `Array in MTL`）。
  **所以「怎么写一个 `for` 循环」「变量怎么声明」「数组怎么用」本页一个字都没有。**
- **`DC_EVENT()` / `DC_EVENT_RANGE()` 那篇没读**——那两个宏**本页只有名字**。
- **那张图看了（2026-09-20 补）**——**上一版这里写的是「一张图都没看」，
  并由此写下「本页没有任何来自图的结论」；那句话现在是错的，按实际改动如下**：
  `102176.png`（`.prog` 高亮的文件依赖小图）——**9 个框、`.prog` 边上有 5 处线头、
  与 `.dvar` 之间无直接连线**，见上文「那张文件依赖小图（④ 图证）」。
  **图上那些字在 raw 里 grep 不到**，要核只能自己开
  `F:\master-dev\dorm-wsl-sytest\tdc-html\raw\102176.png`。
- **图没答掉的**：`#include` 的相对基准、**线型与箭头的含义**、
  维护例程编译后落在哪儿（三条都在上文「④ 图证」最后一节里）。
- **`## Example` 那段 `solid.prog` 没有逐行讲解**，也**没有运行过**——
  `WriteBackground` / `ReadBackground` / `CLK()` / `CTRL(1,1)` / `DES()` / `DBUS_IDLE()`
  **这些名字是什么意思，本页一个都不知道**。
- **`MTL Configuration Files`（`## Related information` 唯一指向）没读。**
- **`Device architecture file` 没读**——所以「设备参数在 `.prog` 里怎么引用」本页只有原文那一句。
- **`Maintenance operations` / `Reusable maintenance operations` 两篇没读**——
  **reusable maintenance routine 长什么样、怎么被别的程序用，本页没有。**

> ⚠️ **本篇的语料瑕疵，照实记、一处没替它改**：
> ① **「不能用」清单里 `exclude` 应为 `except`**。原文逐字：
>    `Some prominent elements of the C language that are not available:`
>    `- Data typing exclude the array data type`
>    —— **`Data typing exclude` 读不通**（`data typing` 是单数，动词却用了原形 `exclude`），
>    **而且这一条要表达的是「除了数组之外没有数据类型」，用词应是 `except`**。
>    照字面读会读成「数据类型把数组类型排除掉了」，**意思正好反**。
> ② **示例代码里同一个变量三种大小写**：`#define zStop 4` / `// #define yStop 64` /
>    `// #define xstop 128` —— **`xstop` 的 `s` 是小写**，前两个是 `zStop` / `yStop`。
>    这三行是示例代码（**raw 不改**），**但它是本篇示例唯一的「改小核」开关**，
>    照抄时容易抄出一致性问题。
> ③ **`Note Exception:` 是两段标记连排**（`Note` + `Exception:`），
>    不是本节独有的问题——同一批文档里 `Note` 常这样跟别的词连排。
> ④ **示例代码里同一个概念两种写法**：`main ()` **函数名和括号之间有一个空格**，
>    而同一个文件结尾的 `EndProgPad()` **没有空格**。原文逐字如此，**本页照抄不改**。

`verified: doc-only`
