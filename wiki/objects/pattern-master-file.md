---
type: object
title: The pattern master file
layer: file
stage: pattern
tags: [pattern, pattern-master-file, vector-setup-file, file-format, label, device-directory, test-program-explorer]
related: [pattern, vector-setup-file, device-directory, test-program-explorer, mapping-pattern, pattern-explorer, pattern-editor, apg-pattern-file, pin-mapping-file, project, smartest-6.3.2]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.05_The_pattern_master_file.md
created: 2026-09-20
updated: 2026-09-20
verified: doc-only
---

# The pattern master file

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,170 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.07.01.05_The_pattern_master_file.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

The syntax of the pattern master file is as follows:

hp93000,pattern_master_file,0.1

[path:

 [<relative_or_absolute_path_1 >]]

files:

 <file_name_1_1>

 <file_name_1_2>

 ...

 <file_name_1_m>

[[path:

 [<relative_or_absolute_path_2>]]

files:

 <file_name_2_1>

 <file_name_2_2>

 ...

 <file_name_2_n>

...]

The default for the path is the vectorssubdirectory of the current device. But if you specify a path, note that the reference directory for relative paths is the waste subdirectory of the device. Therefore, if your pattern files are in the subdirectory sample of the vectors directory, you must specify the relative path to this directory as ./vectors/sample.

You can add comments to a pattern master file after "-- " (2 times the minus sign followed by a space) at the beginning of a line.

### Example

Both the usage of relative paths and the insertion of comments are illustrated by the following example file:

```

hp93000,pattern_master_file,0.1

-- The following file must reside in <device>/vectors:
files:
   sample1.binl

-- The following path points to <device>/vectors/pmfl_test:
path: ../vectors/pmfl_test

files:
  sample2.binl.gz
  sample3.binl.gz
```

<!-- 语法节 end -->

## 是什么

**pattern master file 不是数据文件，是一张「清单」。** 它只装两样东西：**要用到的那些 pattern 文件的名字**，和**它们所在的目录路径**。向量数据本身在别处。

> 「Vector data can be organized in two ways. You can either keep all the labels (patterns) in one big vector setup file, or you can store every pattern in a separate file and specify the subset of them that you want to work with in a pattern master file. The pattern master file contains the names of the pattern files and also the directory path where they are located.」

**这一句同时钉了三件事：**

| # | 文档事实 | 为什么本页要用它 |
|---|---|---|
| 1 | 向量数据**只有两种**组织方式：一个大文件全装，或者**一个 pattern 一个文件 + 一张清单** | master file 是第二种方式的**入口** |
| 2 | 清单里装的是**文件名字 + 目录路径**，**不是向量数据** | 所以它小、可以手写 |
| 3 | 原文写的是 **`labels (patterns)`** —— **括号就是相等号** | 「label = pattern」在本篇里的出处（同阶段对照表 [[mapping-pattern]] 的「地基 ①」用的是另一篇 `02.08.04.16.04.01`） |

### 它和「一个大 vector setup file」的差别（原文只用四条说清）

| 比较项 | 一个大的 vector setup file | pattern master file |
|---|---|---|
| **能不能放在 device 目录之外** | **不能**——`must be located in the vectors subdirectory of your current device` | **能**——`You can store the patterns anywhere in your file system` |
| **加载什么** | 本篇未写 | **只加载你当前真正要用的那些 pattern** |
| **改完再存盘** | 本篇未写 | **保存 master file 时，只有被改过的 pattern 被存盘** |
| **下载时间** | 本篇未写 | **引用的 pattern 很多时可能相当长** |
| **谁创建** | 本篇未写 | **必须手工，或经 `ASCII interface`** |

**原文自己把这几条分成「优点」和「缺点」**：第 1 行是优点①（能放文件系统任何地方），第 2、3 行是优点②（省时间）的两条理由，第 4 行是**唯一一条缺点**，第 5 行（谁创建）**不在这个分类里**。逐字如下。

**优点的引导句是** `Using a pattern master file has two advantages:`。**第一条优点：**

> 「- You can store the patterns anywhere in your file system (whereas the big vector setup file must be located in the vectors subdirectory of your current device).」

**第二条优点（「省时间」）在原文里是父项 `- You save time because`，理由写在它下面两条子项里：**

> 「- you load only those patterns that you really need for your current purpose,」

> 「- when you have changed a pattern and then save the pattern master file, only the modified patterns are stored.」

**注意第 2 条子项隐含的一件事**：**「存 pattern」这个动作是由「保存 master file」触发的**——原文没有另一套「单独存某个 pattern」的说法。

**缺点一条，原文连对策一起给了：**

> 「A possible disadvantage of using a pattern master file is that the download time for the vectors can be rather long if the number of patterns referenced in the master file is very large. In this case you can convert the vector setup into a big vector file by loading it and then saving it under another name in the Test Program Explorer.」

### 创建方式与位置（本任务要回 raw 核的那一句）

> 「The pattern master file must be created manually (or with the ASCII interface). The file itself must be located in the vectorssubdirectory of the current device.」

**这句钉死两件事：**

| 要核的说法 | 核的结果 |
|---|---|
| **必须手工或用 `ASCII interface` 创建** | **核得实**。而且**本篇没有任何一句提到用 GUI wizard 建它**（全文没有 `wizard` 这个词） |
| **必须位于 `<device>/vectors`** | **核得实**（同句第二个分句；Example 第一条注也写 `<device>/vectors`） |
| **后缀是 `.pmfl`** | ⚠️ **本篇核不实**。**全文没有 `.pmfl` 这个串**——唯一出现 `pmfl` 的地方是 Example 里的一个**目录名** `pmfl_test`（`path: ../vectors/pmfl_test`）。**目录名不是后缀**，本页据此不写 `.pmfl` |

**「后缀是 `.pmfl`」那句话的出处不在本页的 `sources` 里**——它是 `wiki/stages/pattern.md` 第 150 行的写法。**本页没有读到支持它的原文，所以按 §11「文档没写就写语料未写」处理：本页不写后缀。**（这**不等于**说 `.pmfl` 是错的——**只是本篇给不出依据**。见「出处」第 5 条。）

### 文件长什么样

结构**逐字**见上面「语法 / 参数」节（脚本抽的 `## Syntax` 与 `## Example` 两段）。把那段归纳成四类行：

| 行的种类 | 写法（逐字以语法节为准） | 它在文件里干什么 |
|---|---|---|
| **头行** | `hp93000,pattern_master_file,0.1` | **原文把它放在最前，但没有解释它**——`hp93000` / `pattern_master_file` / `0.1` 三个字段各是什么，**本篇一个字没写** |
| **路径行** | `path:` + 一个相对或绝对路径 | 给**它下面那批 `files:`** 定目录 |
| **文件行** | `files:` 后跟**一行一个文件名** | 要用的 pattern 文件 |
| **注释行** | 行首 `-- `（**两个减号 + 一个空格**） | 注释。原文给了确切写法，见下 |

**注释那一句逐字是：**

> 「You can add comments to a pattern master file after "-- " (2 times the minus sign followed by a space) at the beginning of a line.」

**语法节里那些方括号（单层的一对与双层的一对）原文没有给图例。**（推断）**它们是「可选」与「可重复」**——推断依据是 Example：**Example 的第一组只有 `files:`、没有 `path:`**，第二组才是 `path:` + `files:`；而语法节里 `path:` 外面正套着一层 `[ ]`。**本篇没有一句解释这套括号，所以这是推断，不是文档事实。**

### 路径怎么解析（本篇唯一一处自己说不通的地方）

原文这一段的逐字：

> 「The default for the path is the vectorssubdirectory of the current device. But if you specify a path, note that the reference directory for relative paths is the waste subdirectory of the device. Therefore, if your pattern files are in the subdirectory sample of the vectors directory, you must specify the relative path to this directory as ./vectors/sample.」

**照字面读，这篇文档自己给出了两个互斥的「相对路径基准」：**

| 出处 | 它要求的基准 | 为什么这么读 |
|---|---|---|
| 上面那句的 `Therefore` 子句 | **`<device>`** | 「`<device>/vectors/sample` 要写成 `./vectors/sample`」**只有在基准是 `<device>` 时才成立** |
| Example 的第一条注（`-- The following path points to <device>/vectors/pmfl_test:` 配 `path: ../vectors/pmfl_test`） | **`<device>/vectors`** | **只有基准是 `<device>/vectors` 时，`..` 才正好回到 `<device>`**，拼出来才是 `<device>/vectors/pmfl_test` |

**两句在同一篇里、挨得很近，而且没有版本差别可用来解释**——这点和 [[mapping-pattern]] ③ 记的那条同类冲突不同：那一条**能**用 `Functional changes` 的版本线解开，这一条**不能**。**本页不替它选一个。**

**又：`the waste subdirectory of the device` 里的 `waste`，本篇只出现这一次，前后没有一句解释它**——它是不是 device 下面的某个子目录、是不是别处打错的词，**本篇给不出判据**，照录（见「出处」的 ⚠️ ②）。

**（建议）实践上只能自己定死一件事**：**写 `path:` 之前先决定按哪个基准算，然后把意图写成行上面的注释**——**Example 自己就是这么做的**（两组上面各有一条 `--` 注释）。**这是本页的建议，不是文档要求。**

### 别把这一篇的两个对象混起来

**这篇 raw 同时喂两页**（[[vector-setup-file]] 的 `sources:` 里也有同一篇），所以下面这几块**属于对面那一页**：

| 原文里的句子 | 它其实在讲什么 |
|---|---|
| `one big vector setup file`、`whereas the big vector setup file must be located in the vectors subdirectory of your current device` | **vector setup file 的位置约束**——不是 master file 的（master file 的约束是另外一句，见上） |
| `In this case you can convert the vector setup into a big vector file by loading it and then saving it under another name in the Test Program Explorer.` | **vector setup file 的转换动作**——但它是**从 master file 的缺点引出来的**，所以它是 master file 的补救手段 |
| Example 里的 `sample1.binl` / `sample2.binl.gz` / `sample3.binl.gz` | **被清单引用的 pattern 文件**（属于 vector setup 那一侧）。**本篇没有一句说 `.binl` 是 vector setup file 的后缀**——它只说这些是 **pattern 文件的名字** |

**本篇一个字都没讲 vector setup file 自己的格式**（头行、字段、怎么建）。**那一份格式不在本页，本页也不写它**——`02.06.07.01.05` 里能被判给 vector setup file 的只有上面表里那三块，**一句格式说明都没有**；`vector-setup-file` 那个对象的格式说明在 [[vector-setup-file]] 那一页，不在本页。

## 典型用法

**本文档没有 `## Procedure` 段，也没有 `## Before you begin` 段**——**所以本篇不提供步骤**。下面每一条都能在原文里找到落点，落点写在每条后面。

**1. 先决定要不要用它**（条件 → 结论，全部出自原文）：

| 你的情况 | 结论 |
|---|---|
| pattern 要放在 `<device>/vectors` **以外** | **必须**用 master file（一个大 vector setup file 做不到这件事） |
| 只想加载当前用得上的那几个 pattern | 用 master file（这是原文列的第 2 条优点） |
| pattern 数量**很大**、又在用 master file | **下载时间可能相当长**——这是原文点名的**唯一缺点** |
| 上一行那种情况，而你更在意下载时间 | **原文给的对策**：把它 load 进来，再在 `Test Program Explorer` 里**另存一个名字**，转成一个大的 vector 文件 |

**2. 建它：手工，或经 `ASCII interface`。** **本篇里没有第三种创建方式**（GUI 侧的说法见「和谁有关」）。

**3. 放它：`<device>/vectors`。** Example 的第一条注就是这句话的示范：`-- The following file must reside in <device>/vectors:`。

**4. 写它：照四类行写**（见「是什么」那张表），注释用行首 `-- `。**Example 逐组读**：

| Example 里的组 | 原文给它的注 | 这一组说明了什么 |
|---|---|---|
| `files:` + `sample1.binl` | `-- The following file must reside in <device>/vectors:` | **不写 `path:` 就是走默认目录**（推断：原文说 `The default for the path is the vectorssubdirectory of the current device`，而这一组没写 `path:`） |
| `path: ../vectors/pmfl_test` + `files:` + `sample2.binl.gz` / `sample3.binl.gz` | `-- The following path points to <device>/vectors/pmfl_test:` | **写了 `path:` 就换目录**，而且**同一份清单可以分好几组**（语法节里双层方括号那一层就是重复的意思，推断见上） |

**Example 存在的理由原文写明了**：`Both the usage of relative paths and the insertion of comments are illustrated by the following example file:`——**它是一份「相对路径 + 注释」的双料示范**。

**5. 改完 pattern 之后：保存 master file。** 原文说这一步**只会把被改过的 pattern 存盘**。**「保存」这个动作在 GUI 里做还是在命令里做，本篇未写。**

**6. 下载太慢时：转成一个大的 vector 文件。** **顺序是 load 在前、另存在后**（原文：`by loading it and then saving it under another name`），场所是 `Test Program Explorer`。

**7. 本页给不了你的**：**没有一条命令**（本篇 0 条固件命令、0 个 API）、**没有步骤顺序**、**没有 GUI 位置**、**没有任何示例之外的文件**。本页只有**这份清单文件的格式、它存在的原因、和它自己的两处说不通**。

## 和谁有关

- [[vector-setup-file]] — **关系：两种组织方式里的另一支（清单 ↔ 载体），而且两页共用这一篇 raw**。那一页的 `sources:` 里也有 `02.06.07.01.05`，并且**本篇的 `## Syntax` 与 `## Example` 两段被脚本抽进了它的语法节**（在那页里带 `（取自子主题 The pattern master file）` 的标注）。**所以两页语法节内容重复是脚本行为，不是内容写混了**；界线见「是什么」最后一小节。
- [[device-directory]] — **关系：位置约束的宿主**。master file 必须落在 `<device>/vectors`，Example 里 `<device>/vectors` 出现两次。
- [[test-program-explorer]] — **关系：下游的补救手段**。**本篇唯一指名的工具**就是它（原文写 `Test Program Explorer`）：下载太慢时在那里 load + 另存，把 vector setup 转成一个大 vector 文件。
- [[pattern]] — **关系：同阶段的脊椎页（`stage: pattern`）**。本篇是这个阶段的**产物清单文件**；本篇第一句的 `labels (patterns)` 也是「label = pattern」的一条出处。
- [[mapping-pattern]] — **关系：同阶段对照表；它和本页在「谁创建 master file」上记载不同**。[[mapping-pattern]] ③ 记的是 GUI 侧那一篇（`02.08.04.16.01.15.01`）说 master file 由 `New Pattern Setup wizard` 创建，**而本篇说必须手工或经 `ASCII interface`**；对照表已按版本解释这条冲突（wizard 是 SmarTest 7.1.3 才加的，本篇那句的落款是 `Introduced before SmarTest 6.3.2`）。**那篇 raw 本页没读**，本页只把两边并列，不替语料选一个。
- [[pattern-explorer]] — **关系：GUI 侧的入口，但本篇一个字没提它**。本篇全文没有 `Pattern Explorer` / `pmfl setup` 这类词；GUI 侧的操作（建立 master file、以及「GUI 操作会把路径与文件名补进 master file」）记在 [[mapping-pattern]] 的正文里，**那几篇 raw 本页没读**。
- [[project]] — **关系：上游阶段**。`<device>/vectors` 先存在，本页讲的这个文件才有地方放。**这一条转自 `wiki/stages/pattern.md` 的「前置条件」第 5 条，本篇没有独立证据。**
- **同 `layer: file` + `stage: pattern` 的邻页**（[[apg-pattern-file]]、[[pin-mapping-file]]、[[device-access-file]]、[[device-architecture-file]]、[[apg-program-file]]）—— **本篇 raw 一个字没提这几页里的任何一个**。（推断：它们同族，依据只是同层同阶段；**本页不主张任何具体关系**。）
- **入边 4 条**（取自 `extract/edges.jsonl`：`inline` 3 条 + `toc` 1 条；**出边 0 条**）：`02_System_reference/02.06_Command_Reference/02.06.07.01_Concepts_of_vector_setup.md`（[[vector-setup-file]] 的定义篇，链接文本就是 `The pattern master file`）、`02_System_reference/02.06_Command_Reference/02.06.07.01.03.01_From_global_to_port_specific_vector_areas__Migration_and_compatibility.md`（讲的是 master file 的下载时间可能更长）、`01_Getting_started/01.03_Using_SmarTest/01.03.04_Working_with_testflows_efficiently.md`（把 master file 放在「在 Setups 页 load 专用 setup 并 initialize (parse)」这一步里）、`02_System_reference/index.md`（目录页）。**这四篇本页一篇都没读**，只读了边里的链接文本和半句上下文，**所以本节不引它们的原句**。
- **只能写反引号、不能写成链接的名字**：`label`（无页）、`ASCII interface`（无页）、`hp93000`（文件头行原文）。

## 版本

原文有 `## Functional changes` 段，**只有一条**：

- **Introduced before SmarTest 6.3.2**

> 这一条是哨兵值，不是「6.3.2 新增的」。它写的是 `before`——意思是「在本文档集覆盖范围开始之前就已经有了」（schema §11.2 ②）。**照字面读会凭空造出一条「SmarTest 6.3.2 新增了 pattern master file」的假信息，而且格式齐整。**

**原文没有第二条变更记录**——**所以「这份清单文件的格式在 6.3.2 之后改过没有」，本页没有依据。**

**（推断）头行里的 `0.1` 是这份文件格式自己的版本号，不是 SmarTest 版本。** 推断依据：它和 `hp93000`、`pattern_master_file` 同在一行（`hp93000,pattern_master_file,0.1`），而本篇 `## Functional changes` 用的是 SmarTest 版本号——**两套号出现在两个地方，原文没有一处把它们连起来**，所以这是推断。

**另记一条**：[[mapping-pattern]] ③ 把「谁创建 master file」的冲突按版本解释（GUI 侧那个 wizard 是 SmarTest 7.1.3 才加的）。**那是对照表的结论**；本篇在这里只提供它引用的那句话，以及本篇自己的落款 `Introduced before SmarTest 6.3.2`。

## 出处

`sources:` 一篇：`02_System_reference/02.06_Command_Reference/02.06.07.01.05_The_pattern_master_file.md`（**2,837 字节 / 84 行**，TDC 源 `58905.htm`）。**整篇读完了**——`## Syntax` / `## Example` / `## Functional changes` 三段，加上三段之外的散文全部。

**本页没做的**：

1. **只读了这一篇。** `sources` 之外的 raw 一篇没读——包括 [[vector-setup-file]] 的定义篇 `02.06.07.01_Concepts_of_vector_setup`、GUI 侧建 master file 的 `02.08.04.16.01.15.01_Creating_a_pattern_master_file`、维护它的 `02.08.04.16.01.15_Working_with_pattern_master_files`、以及那批向量设置命令（`SQLB` / `SQLA` / `SQPG` 等）。**所以「怎么用命令操作 master file」本页一个字都没有。**
2. **链源那三篇没读**（入边里的 `01.03.04`、`02.06.07.01.03.01`、`02.06.07.01_Concepts_of_vector_setup`）。**「和谁有关」里讲到入边的那一条，全部只来自 `extract/edges.jsonl` 的链接文本与半句上下文**，不是读原篇得来的。
3. **没有看图——而且本篇一张图都没有**（raw 全文不含 `![`）。**所以本页没有任何来自图的结论**。这一点和 [[mapping-pattern]] ⑬ 说的那批 GUI 页**相反**：那一批是「有图没看」，这一篇是「本来就没图」。
4. **没有实跑。** 没有生成过 master file，没有在 `Test Program Explorer` 里做过 load + 另存，**也没有验证过 `path:` 的相对基准到底是哪一个**——**这正是本页唯一一处不能自解的疑点**（见「是什么」）。`verified: doc-only` 指的就是这件事。
5. **没有动别的页。** 没有改 `wiki/index.md`；没有改 `wiki/stages/pattern.md`——**那一页第 150 行写本篇后缀是 `.pmfl`，本页核不实**，但改页不在本任务范围内，所以只把不一致记在这里、**那页一个字没动**。
6. **「语法 / 参数」节不是空的。** 脚本抽到了本篇的 `## Syntax` 与 `## Example` 两段（节头写着 1,170 字符）——**所以本页不需要解释「空语法节」那件事**（对照 [[analysis-views]]，那一页才是空的那种）。

> ⚠️ **本篇的语料瑕疵，照实记，一处都没替它改**：
>
> ① **同一篇里 `vectorssubdirectory` 的拼法不一致**：**无空格**的写法出现两次——`The file itself must be located in the vectorssubdirectory of the current device.` 与 `The default for the path is the vectorssubdirectory of the current device.`；**有空格**的写法出现一次——`whereas the big vector setup file must be located in the vectors subdirectory of your current device`。**两个写法都在同一篇里，本页照录。**（[[mapping-pattern]] ⑤ 也记了这一条。）
>
> ② **`the waste subdirectory of the device` 里的 `waste`**：**本篇只出现这一次，前后没有一句解释它**。**照录，不猜它是哪个词的错**——本篇没有给判据（这一点与 ③ 有关联：如果知道 `waste` 指哪个目录，③ 的基准问题就能定一半）。
>
> ③ **路径基准自相矛盾**（照字面读）：`Therefore, if your pattern files are in the subdirectory sample of the vectors directory, you must specify the relative path to this directory as ./vectors/sample.` 要求基准是 `<device>`；而 Example 的注 `-- The following path points to <device>/vectors/pmfl_test:` 配 `path: ../vectors/pmfl_test` 要求基准是 `<device>/vectors`。**两句互斥**，而且**不像 [[mapping-pattern]] ③ 那条能用 `Functional changes` 的版本线解开**——这两句紧邻、没有版本差别。**本页并列两处，不替它选。**
>
> ④ **语法节里 `<relative_or_absolute_path_1 >` 的尖括号内多一个空格**（对照第二组写的是 `<relative_or_absolute_path_2>`，**没有**那个空格）。**照录**；这一处在「语法 / 参数」节里，本页一个字没动。
>
> ⑤ **本篇没有坏字。** 全文 **0 个 CJK 字符、0 个非 ASCII 字符**（`python -X utf8` 数过）。**所以本页引文里不会出现 `碌` / `渭` / `鈥慴` 那一族坏字——不是本页清过，是这一篇本来就没有**（对照 schema §11.2 ①：全语料 11.2% 的篇含坏字，**本篇不在那一批里**）。

`verified: doc-only`
