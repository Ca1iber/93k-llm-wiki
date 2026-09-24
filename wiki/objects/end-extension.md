---
type: object
title: END_EXTENSION
layer: L2
stage: testmethod
tags: [testmethod, l2, test-method-api, extension-block, fw-task, firmware-command, pair, site-focus, pointer-page]
related: [testmethod, begin-extension, fw-task, flush, on-first-invocation-begin, mapping-testmethod, command-reference, smartest-6.3.2]
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.59_END_EXTENSION.md
created: 2026-09-24
updated: 2026-09-24
verified: doc-only
---

# END_EXTENSION

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **158 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.59_END_EXTENSION.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
void END_EXTENSION();
```

List of parameters

There are no parameters.

### Example

See the Examples section of `BEGIN_EXTENSION`（raw: `02.07.04.01.10_BEGIN_EXTENSION.md`）.

<!-- 语法节 end -->

## 是什么

**`END_EXTENSION` 是「扩展块」的闭括号。** 它那一篇的第一句就把自己和 `BEGIN_EXTENSION` 绑在一起：

> This API declares the end of the extension block that is started by BEGIN_EXTENSION. This API is used together with BEGIN_EXTENSION as a pair to declare the extension block.

**本篇是一篇「指路页」**——原文第二句就把细节全部推走了：

> For details on the extension block enclosed by BEGIN_EXTENSION and END_EXTENSION, see BEGIN_EXTENSION.

**所以本页不讲机制**：扩展块怎么用、里面能放什么、进块前要做什么，
**全在 `BEGIN_EXTENSION` 那一篇里**（本页读了它那一篇，见 [[begin-extension]]）。
**本页只讲「这个 API 自己有什么」和「哪些话在哪一篇」。**

### 这个 API 自己只有三件事

| 项 | 原文（「语法 / 参数」节里逐字） | 读法 |
|---|---|---|
| **签名** | `void END_EXTENSION();` | **只有一个形态，没有重载** |
| **参数** | `There are no parameters.` | **没有参数**（原文这一节的标题是 `List of parameters`，下面直接跟这一句） |
| **头文件** | `This API is defined in the header file /opt/hp93000/soc/prod_com/include/MAPI/Extension.h.` | **与 `BEGIN_EXTENSION` 同一个头文件**——两篇 raw 写的是同一个绝对路径 |

### 两个 API 的行为，分别写在哪一篇（**这是本页最有用的一张表**）

| 行为 | 写在哪一篇 | 本页（`END_EXTENSION`）里有没有 |
|---|---|---|
| 「扩展块」的定义 + 必须成对 | **两篇都有** | ✓（就是上面第一句引文） |
| 块里能放什么（`FW_TASK` / 自己写的函数 / **不许放别的 test method API**） | `BEGIN_EXTENSION` | ✗ |
| 进块前先执行 `FLUSH`、块内 caching 被临时关掉 | `BEGIN_EXTENSION` | ✗ |
| `sites` 参数怎么给（`STRING` / `ARRAY_I` 两种写法） | `BEGIN_EXTENSION` | ✗ |
| **出块时 setup focus sites 会还原** | **`BEGIN_EXTENSION`**（**讲的是本页这个 API 的行为，却不在本页这一篇里**） | ✗ |
| 嵌套不正确 → nest 信息在 test suite 结束时被初始化 + report window 出现 warning | `BEGIN_EXTENSION` | ✗ |
| Example | **`BEGIN_EXTENSION`**（本篇 `## Example` 整段只有一句指路） | ✗ |

**关于倒数第三行**：那句在 `BEGIN_EXTENSION` 那一篇里逐字是

> END_EXTENSION just after BEGIN_EXTENSION reverts the setup focus sites to the same settings as before entering the extension block.

**——它描述的是 `END_EXTENSION` 一进一出造成的效果，却写在本页之外那一篇里。**
**本页照实引它、并写明它出自 [[begin-extension]]**；**本页不据此把它算成「本页的文档事实」**
（本页 `sources:` 里只有 `02.07.04.01.59` 那一篇，那一篇一个字都没提这个行为）。

**一句话总结本页的边界**：**`END_EXTENSION` 自己那一篇能提供的，
就是上面三行（签名 / 无参数 / 头文件）+ 两句指路 + 一条版本行。**
**这不是本页偷懒，是本篇本来就短**——按 §11 与 §2.2，**本页不替它补机制，
也不把 [[begin-extension]] 的内容搬过来重讲。**

## 典型用法

**本文档没有 `## Procedure` 段、没有 `## Before you begin` 段、没有 `## Important points` 段，
`## Example` 段也没有代码**——整段只有一句：

> See the Examples section of BEGIN_EXTENSION.

**所以「怎么用」本篇给的答案就是「去 `BEGIN_EXTENSION` 那一篇的 Examples 看」。**
（那两个 Example 已经在 [[begin-extension]] 的「语法 / 参数」节里逐字，本页不重抄。）

**能确定的两条（都出自本页自己的 raw）：**

| 要知道的 | 答案 | 依据 |
|---|---|---|
| 它长什么样 | `void END_EXTENSION();` | `## Syntax` |
| 要传参数吗 | 不用，`There are no parameters.` | `## Syntax` 下面那句 |
| 和谁一起用 | `BEGIN_EXTENSION`，**成对**（`used together with BEGIN_EXTENSION as a pair`） | 首段 |
| 里面写什么 | **本篇没说**——去看 [[begin-extension]] | `## Example` 那句指路 |

**写法上的顺序（本页能说的）**：**先 `BEGIN_EXTENSION` 开块，块里写语句，最后 `END_EXTENSION` 收尾。**
「块里能写什么、开块前要做什么」不在本篇，**在 [[begin-extension]]**。

## 和谁有关

- [[begin-extension]] — **配对的前半，也是本页唯一的实质关系。** 本页 raw 里
  `## Related information` 与 `## Example` 两节**指的都是它**，连定义句也是
  （`the extension block that is started by BEGIN_EXTENSION`）。
  **两篇的 raw 不同**（`02.07.04.01.59` vs `02.07.04.01.10`），**本页读了那一篇**：它的 119 行里有机制、
  参数说明与两个 Example，**本页一行都不重抄**。
- [[fw-task]] — 本页 `## Related information` 的第二个名字（`BEGIN_EXTENSION` 那一篇的第三个）。
  **本页的 raw 对 `FW_TASK` 只有这一处提及**——所以「它和本页这个 API 怎么配合」
  **本页一个字都没有**；那一层在 [[fw-task]] 与 [[begin-extension]] 两页里。
  （本页没读 `FW_TASK` 那一篇的 raw。）
- [[testmethod]] — **stage 页，也是本页 `stage: testmethod` 的理由。** 它那一页把
  本页与 [[begin-extension]]、[[fw-task]] 并列在「L2（L1 通道）」那一格，
  注意是**三个名字并列**：**那一页没有单独讲 `END_EXTENSION`**。
- [[on-first-invocation-begin]] — **多 site 场景里用到这一对的地方**：那一页记着它那一篇要求
  `FW_TASK` 裹在**带 site 参数**的 `BEGIN_EXTENSION` / `END_EXTENSION` 里。
  **那条要求不在本篇的 raw 里**（本篇全文没有出现 `ON_FIRST_INVOCATION` 这个词）。**本页只登记它来自哪。**
- [[flush]] / [[command-reference]] — **本篇一个字都没提它们**。
  与它们有关的一切（进块前先 `FLUSH`、固件命令本体在 `02.06`）**都在 [[begin-extension]] 那一页**，
  本页不为它们做任何断言。
- [[mapping-testmethod]] — **跨层对照表**：它把本页填在「在 test method 里执行固件命令」那一行的
  L2 格，与 [[fw-task]]、[[begin-extension]] 并列。
- **本页 raw 的 `## Related information` 只有两个名字**（`BEGIN_EXTENSION` 与 `FW_TASK`），
  **两个都已列在上面**——所以**没有别的文档点名本页**这一层，本页不缺东西可写。
- [[smartest-6.3.2]] — **版本页**：本篇 `## Functional changes` 那一条的落点（是哨兵，见「版本」）。

## 版本

本文档有 `## Functional changes` 段，**只有一条**：

- `Introduced before SmarTest 6.3.2`

**这是 §11.2 ② 那个哨兵值，不是「6.3.2 引入了它」**：措辞是 `before` 不是 `in`，
意思是「**在本文档集覆盖范围开始之前就已经有了**」。所以：

- **本页答不出「哪一版才有 `END_EXTENSION`」。**
- **和 [[begin-extension]] 是同一条**——两篇的 `## Functional changes` 都是这一行，
  **所以两个 API 在版本记录上是同步的**（**「同一行」是文档事实，「同时引入」是（推断）**，
  依据只是两篇写了同一个版本号与同一个措辞）。
- 版本页 [[smartest-6.3.2]] 对这个哨兵的处理是**单列一节讲那 2,677 条的做法、不逐条铺开**；
  本页这一条**不在它正文列出的 33 条里**。

## 出处

`sources:` 一篇：
`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.59_END_EXTENSION.md`
（TDC `29303.htm`，35 行 / 941 字节）。**整篇读完——它全文就是本页上面引的那几句。**

**本页没做的：**

- **`BEGIN_EXTENSION` 的 raw 读了**（`02.07.04.01.10`，119 行），因为本篇两处都指着它
  （`## Example` 与 `## Related information`），**不读它就只剩一页空壳**。
  **代价要说清**：本页「是什么」里那张「写在哪一篇」的表，**是两篇对比的产物**，
  其中「本页有没有」那几格是**我逐项核出来的**，不是原文的表格。
- **`FW_TASK`（`02.07.04.01.77`）没读**——本页 raw 的 `## Related information` 点了它，
  **但只点了名字**。所以「`END_EXTENSION` 与 `FW_TASK` 之间有什么接口上的要求」本页没有。
- **`02.07.03.10_Executing_Firmware_Commands.md` 没读**（[[testmethod]] stage 页引的是它）。
- **一张图都没看——因为这一篇里没有图。** 实测全文 **0 处** `.png` / `.jpg` / `raw/`。
  **所以本页没有任何来自图的结论。**
- **没有实跑。** 没在任何机台上开过一段扩展块，也没有验证过「`END_EXTENSION` 之后 site focus
  真的还原了」这件事。`verified: doc-only` 指的就是这件事。
- **本文档没有 `## Procedure` / `## Before you begin` / `## Important points` 段，
  `## Example` 段也没有代码。** 所以上面「典型用法」只有一张四行的表，
  **那不是本页偷工，是本篇的全部**。

> ⚠️ **本篇的语料瑕疵，本页照实记下、一处都没替它改**：
> ① **`## Related information` 那一行里两个链接之间没有任何分隔符**，在 raw 里是连着的一串：
> `[BEGIN_EXTENSION](<02.07.04.01.10_BEGIN_EXTENSION.md>)[FW_TASK](<02.07.04.01.77_FW_TASK.md>)`
> ——**一个空格都没有**。（同一形态在别的篇里也有，[[fw-task]] 那一页的 ⚠️⑦ 记过同一件事。）
> ② **`## Syntax` 节里参数那一行的标题是 `List of parameters`**（另起一行、独立成段），
> 下面跟一句 `There are no parameters.`——**而 `BEGIN_EXTENSION` 那一篇同一位置是一张
> 摊平的参数表**。**两篇形态不同，各自照录**；本页不据此说哪一篇的写法是"对的写法"。
> ③ **`## Example` 段里没有例子。** 整段只有一句 `See the Examples section of BEGIN_EXTENSION.`——
> **一个代码块都没有**。语法节里那个 `### Example` 标题下面就是这句话，
> **不是脚本抽漏了，是原文如此**（同一形态在 [[add-limit]] 那一篇里也有，见那一页的 ⚠️①）。
> ④ **`END_EXTENSION` 的效果之一（site focus 还原）写在本页之外那一篇里**——
> **这不是本篇的错字，是「一个 API 的行为写在另一个 API 的名下」**：
> 出处在 [[begin-extension]] 那一篇（那句以 `END_EXTENSION just after BEGIN_EXTENSION` 开头）。
> **两页都把它记下来了**，免得下一份材料只读一篇就以为「`END_EXTENSION` 什么也不做」。
> ⑤ **本篇没有坏字，也没有省略号。**（实测：非 ASCII 字符 0 处，U+2026 与三个 ASCII 点的那种写法各 0 处。）
> **但这是「本页量过的」**，判据是本篇这一个文件；§11.2 ① 那族在别的篇里大量存在。

`verified: doc-only`——**本页没有在任何真实机台上开过一段扩展块**
（§11：文档里有 ≠ 这台机器上能用；尤其「出块后 site focus 是否真还原」这一条，
**它连本篇的 raw 都不在，是 [[begin-extension]] 那一篇的话**，动手前先照实机核对）。
