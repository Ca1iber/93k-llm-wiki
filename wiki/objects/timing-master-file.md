---
type: object
title: Timing setup master file
layer: file
stage: timing
tags: [timing, master-file, timing-setup-file, split-and-assemble, setup-management]
related: [timing, timing-file, timing-equation-set, setup-management-tool, wavetable-file, level-master-file]
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.04.05_Timing_setup_master_file.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# Timing setup master file

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **633 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.04.05_Timing_setup_master_file.md>` 及其子主题 `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.04.05.01_Master_file_format_for_timing_setup.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> ⚠️ 定义文档自己**没有**完整语法段，带「取自子主题」后缀的段落是从子主题抄的——
> **来源写在段名里**，别把它当成定义文档自己写的。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Master file format for timing setup）

The following is an example of a timing master file:

```
hp93000,timing_master_file,0.1
# this is a comment
testerfile: demo.tim

EQNSET 1: files/part1.tim
EQNSET 2 [PIN_ALIAS_SET usb_set]: files/eqnset02.tim

WAVETABLE wtbl_1: files/part1.tim
WAVETABLE wtbl_2: files/wtbl_2.tim

MULTIPORT_SPEC "spec_1":files/part1.tim
MULTIPORT_SPEC "spec_2":files/spec_2.tim
DEFINES: files/defines.tim
```

In the assembled level setup file `demo.tim`, the alias set `usb_set` is used in the equation set 2. When `demo.tim` is splitted, the alias set `usb_set` is removed from the generated sub-file `eqnset02.tim` and package pin names are used.

<!-- 语法节 end -->

## 是什么

**master file 是「把一套 timing setup 拆成多个文件」时的那张索引。**
本文档**正文只有三句话**，而机制全在里面：

> 「The timing setup can be organized as one single file, or its individual parts, namely wavetables, equation sets, and multiport specifications, can be be stored in separate files. In the latter case the parts that belong together are connected by a master file which contains references to the respective files. This construction has the advantage that several users can work on the same timing setup in parallel.」

拆开来的三样是**原文点名的**：wavetables、equation sets、**multiport specifications**。
master file 里装的**不是数据，是指向各个子文件的引用**。
做这件事的理由原文也给了：**几个用户可以同时改同一套 timing setup**。

| 问题 | 本文档的答案 |
|---|---|
| 什么时候用 | **一套 setup 要几个人并行改**的时候 |
| 拆哪几样 | wavetables / equation sets / multiport specifications |
| master file 里装什么 | **指向子文件的引用**（不是数据本身） |
| 不拆行不行 | 行——原文第一句自己就给了 `organized as one single file` 这条退路 |

### 文件长什么样：正文没写，格式在子主题里

**本文档自己没有给格式。** 它只列了两个子主题：

- `Master file format for timing setup`
- `Editing the level and timing subfiles`

**格式正文在第一个子主题里**——本页「语法 / 参数」节已经把那一篇的 `## Example` **逐字**抄了进来
（节顶那行 `取自子主题` 就是这件事的声明）。**照那段例子可以读出四件事**：

| 从例子里看出来的 | 逐字 |
|---|---|
| 首行是文件标识 + 版本 | `hp93000,timing_master_file,0.1` |
| `#` 起头是注释 | `# this is a comment` |
| 有一条指向**装配后的完整文件**的引用 | `testerfile: demo.tim` |
| 三类部件各占若干行，形如引用 + 冒号 + 路径 | `EQNSET 1: files/part1.tim` |

**例子里三类部件都出现了**：`EQNSET`（两条）、`WAVETABLE`（两条）、`MULTIPORT_SPEC`（两条），
另有一条 `DEFINES: files/defines.tim`。**引用行可以带一个方括号里的附加说明**，
例子里的第二条 equation set 就是 `EQNSET 2 [PIN_ALIAS_SET usb_set]: files/eqnset02.tim`。

同节末尾那句讲的是**拆的时候 alias set 会怎样**（**这句来自子主题，不是本文档正文**）：

> 「In the assembled level setup file demo.tim, the alias set usb_set is used in the equation set 2. When demo.tim is splitted, the alias set usb_set is removed from the generated sub-file eqnset02.tim and package pin names are used.」

**即：装配态里用 alias set 写的那一层，拆完后落到子文件里会变成 package pin 名。**
（`demo.tim` 那句说的是 `level setup file`——**本页是 timing 页**，这处用词见「出处」⚠️ ②。）

## 典型用法

**本文档没有 `## Procedure` 段，也没有 `## Before you begin`，一句步骤都没有。**
它只有 `## Subtopics`（两篇）与 `## Related information`（两篇）。
所以这一节只能写「原文把这件事交给谁」：

- **要拆 / 要合，原文指向 [[setup-management-tool]]**（`## Related information` 的第一条就是它）。
- **要一份装配好的完整 setup 长什么样，原文指向 `Example of the equation based timing setup file`**
  （**未建**，本页没读）。
- **格式细节在子主题 `Master file format for timing setup` 里**——本页只有「语法 / 参数」节抄来的那段例子，
  **没有读那一篇**（见「出处」）。

**一句话**：**这份文档是目录页，不是说明书。**
「怎么拆、怎么合、拆完怎么验」这三问，本页的语料一问都没答。

## 和谁有关

- [[timing]] —— 本页 `stage: timing`。
- [[timing-file]] —— **不拆的时候**就是那一个文件。注意口径：原文只说 `one single file`，
  **`timing-file` 这个文件名本文档一次都没出现**；这一条是按职责排的（**推断**）。
- [[setup-management-tool]] —— **上游**：拆 / 合这个动作由它做，原文的 `## Related information` 直接指它。
- [[timing-equation-set]]、[[wavetable-file]] —— **下游的两个部件**：
  原文点名三类部件，其中 equation sets 与 wavetables 本 wiki 已有页（第三类 `multiport specifications` 未建）。
  **两页讲的是「这块内容什么格式」，本页讲的是「这块内容放在哪个文件里」**——
  是**同一套 setup 的两个维度**，不是同一个东西的两页。
- [[level-master-file]] —— **同类（推断）**：本页 Subtopics 的第二个子主题题面是
  `Editing the level and timing subfiles`，**同时提到 level**——
  这说明这套「拆成子文件 + 用 master file 串起来」的形式**level 与 timing 共用一个**。
  但**本文档正文里 `level` 一次都没出现**——通篇唯一的 `level` 就在那行子主题标题里
  （连子主题那句 `In the assembled level setup file demo.tim` 也不在本篇正文，
  它在 `Master file format for timing setup` 里）。
  **所以这条关系是（推断），而且本页没读 level 那一篇。**
- [[mapping-timing]] —— 那张对照表有一行「把一个 timing setup 拆成 / 合成多个文件」，
  三列（L1 / L2 / L3）全空，GUI 格指 [[setup-management-tool]]、文件格指本页。

## 版本

**本文档没有 `## Functional changes` 段。**（这是事实，不是缺陷——它是一张目录页，
正文本身只有三句话，`## Related information` 之后文件就结束了。）

**⚠️ 但「没有版本段」不等于「这件事没有版本事实」（2026-09-20 补，由 reviewer 查出）**：
本页「语法 / 参数」节里那段 Example **抄自子主题 `02.08.04.34.04.05.01`，而那一篇是有版本段的**，
两条还都正对着本页的内容：

- `SmarTest 6.5.2: Renamed macro variable AGILENT93000_MFH_PREFIX to VERIGY93000_MFH_PREFIX.`
- **`SmarTest 6.5.3: New keyword: PIN_ALIAS_SET.`**——**正对着本页引的那行例子**
  `EQNSET 2 [PIN_ALIAS_SET usb_set]: files/eqnset02.tim`。

**所以「`PIN_ALIAS_SET` 是 6.5.3 才有的关键字」是一条真实的版本事实**，
它不在本页的 `sources:` 里（**那一篇本页没读**）。**本页只是把它记在这里，不替它展开。**

## 出处

`sources:` 一篇，**整篇读完**：
`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.04.05_Timing_setup_master_file.md`
（TDC `91597.htm`，**全文 1,132 字节**，含 frontmatter 与两个子主题的链接行）。
**没有读 `sources` 之外的任何文档。**

**本页没做的：**

- **两个子主题都没读**：`02.08.04.34.04.05.01_Master_file_format_for_timing_setup`
  （**格式正文就在这一篇里**）与 `02.08.04.34.04.05.02_Editing_the_level_and_timing_subfiles`。
  **本页关于文件长相的全部内容，只来自「语法 / 参数」节里脚本逐字抄来的那段 `## Example`**
  ——**也就是说：本页没有一行是「我读了子主题」得来的**。
- **`## Related information` 的两篇没读**：`Setup Management Tool`（`01.01.07.02.02.04`）、
  `Example of the equation based timing setup file`。
- **一张图都没有。** 本文档对 `raw/` 下 `.png` 的引用是 **0 处**（逐处查过），
  所以**本页没有任何来自图的结论**——**不是图够不着，是这篇文档本来就没配图**（§11.4）。
- **没有实跑。** 没有拆过 / 合过任何 master file，没有开过 Setup Management Tool。
  `verified: doc-only` 指的就是这件事。
- **写这页时没有动 `wiki/index.md`、也没有把本页挂进 `wiki/stages/timing.md`**；**两者已由本批收尾统一挂入**（`index.md` 的对应条目、`stages/timing.md`）。（**2026-09-20 更正**：原文写「那是待办」——**收尾动作把它变成了假话**。）

**⚠️ 本页照实记下、一处都没替语料改的瑕疵：**

**① 正文有一处衍字：`can be be stored in separate files`**（`be` 重复）。本页引文里**照原样留着**。

**② 子主题那句里的 `splitted` 不是词**（应为 `split`），且同一句把 timing 的 master file 说成
`the assembled level setup file`。**两处都照原样引**，不替它改；
来源是子主题、不是本文档正文这件事，「语法 / 参数」节顶已经声明过，本页再说一次。

**③ `multiport specifications` 这个第三类部件，本 wiki 里没有页**，本页按原文用反引号写名字。

**④ 编码坏字：零处。** 实测这一篇的 CJK 字符数是 **0**（§11.2① 那一族在这篇里一处都没有）；
**`DC/DC power units` 那一族（§11.2⑤）也是 0 处**。

`verified: doc-only`
