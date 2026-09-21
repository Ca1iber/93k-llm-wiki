---
type: object
title: DFPT, DFPT? - (DeFine PorT)
layer: L1
stage: pin
tags: [dfpt, firmware-command, port, port-definition, pin-configuration, pinlist, l1-command]
related: [dfgp, dfge, pin, mapping-pin, pin-configuration-file, port-editor, conf, dfpn, dfps, udgp]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.66_DFPT__DFPT__-__DeFine_PorT.md
created: 2026-09-21
updated: 2026-09-21
verified: doc-only
---

# DFPT, DFPT? - (DeFine PorT)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **761 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.66_DFPT__DFPT__-__DeFine_PorT.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Parameters

|

pinlist

 |

Pin name or names. If more than one pin is required, the names must be separated with a comma. The @ character can be used to refer to all configured pins. The pin list can contain digital or DC Scale pins, or a combination of both.

 |
 |

port

 |

The name of the port to which the pins are associated. The maximum number of characters is 16 for 32-bit SmarTest and 64 for 64-bit SmarTest.

 |
 |

portlist

 |

List of ports for which the associated pins are to be displayed. Specify `(@@)` to retrieve the definitions of all ports.

 |

### Example

```
DFPT? (port_1, port_2)
```

returns:

```
DFPT (CP_1,DS7_1,DS0_1,I/O7_1,...,I/O0_1,Q7_1,
Q0_1,S1_1,S0_1,_MR_1),(port_1)
DFPT (CP_2,DS7_2,DS0_2,I/O7_2,...,I/O0_2,Q7_2,
Q0_2,S1_2,S0_2,_MR_2),(port_2)
```

<!-- 语法节 end -->

## 是什么

**`DFPT` 定义 port。** 原文两句：

> 「The DFPT (DeFine PorT) command defines a port. Reusing a port name causes the pins in the
> new port definition to be appended to the pins in the original definition.」
>
> 「The DFPT? query is used to check a single or all port definitions.」

**第二句是这个命令最容易踩的地方**：**重用一个已存在的 port 名，不是覆盖，是追加**——
新旧两批 pin 会并在一起。**本篇没有给任何「把 pin 从 port 里拿掉」的手段**（见 `## 典型用法` ⑤）。

**原文没有定义「port 是什么」**——只说它有一批关联的 pin、有一个名字。
**port 与 pin 组（`DFGP` / `DFGE`）的区别，本篇一个字都没有。**

## 典型用法

**① 定义：`DFPT {(pinlist)}, {(port)}`；查询：`DFPT? {(portlist)}`。**
**两个实参都带圆括号**，与 `DFGE` 的写法（表达式带引号、组名带括号）不同。

**② `pinlist` 的三种写法**（原文逐句）：

> 「Pin name or names. If more than one pin is required, the names must be separated with a comma.
> The @ character can be used to refer to all configured pins.
> The pin list can contain digital or DC Scale pins, or a combination of both.」

**`@` = 所有已配置的 pin**；**同一份 pinlist 里可以混 digital 与 DC Scale。**

**③ 两个通配符长得不一样，别混**：

| 你要 | 写 | 原文 |
|---|---|---|
| pin 的全部 | `@` | `The @ character can be used to refer to all configured pins.` |
| port 的全部 | `(@@)` | `Specify (@@) to retrieve the definitions of all ports.` |

**pin 侧是一个 `@`、port 侧是两个 `@@` 且要带括号**——原文没有把这两条并排解释。

**④ `port` 名有长度上限，而且和 SmarTest 是 32 位还是 64 位有关**（原文逐字）：

> 「The maximum number of characters is 16 for 32-bit SmarTest and 64 for 64-bit SmarTest.」

**原文没有说读者怎么判断自己装的是哪一种。**

**⑤ 重名 = 追加，所以同一个 port 会被越加越大。**
原文用 `appended` 这个词，**没有给「减」的对应说法，也没有给上限**。
（**「没有减的办法」是本页的观察，不是原文写的**——
`DFGE` 的表达式有 `-` 运算符，`DFPT` 的语法里**没有任何运算符**，这是本页据语法行的判断。）

**⑥ 原文的例子**——一次查两个 port：

```
DFPT? (port_1, port_2)
```

返回（原文逐字）：

```
DFPT (CP_1,DS7_1,DS0_1,I/O7_1,...,I/O0_1,Q7_1,
Q0_1,S1_1,S0_1,_MR_1),(port_1)
DFPT (CP_2,DS7_2,DS0_2,I/O7_2,...,I/O0_2,Q7_2,
Q0_2,S1_2,S0_2,_MR_2),(port_2)
```

**注意返回里那个 `...`**——见 ⚠️ ④。

## 和谁有关

### 同族的三个「定义型」命令，「重名」的命运各不相同

| 命令 | 定义什么 | 重名时 |
|---|---|---|
| `DFPT`（本页） | port | **追加**（`appended`）——**本篇 raw 明写** |
| [[dfgp]] | 固定 pin 组（列名单） | **本页没读那篇 raw，不写** |
| [[dfge]] | 表达式型 pin 组（给规则） | **覆盖**（`the old definition will be overwritten`），且只是警告 |

> **`DFGE` 那一格的依据**：写本页的同一批次里也在写 [[dfge]]，
> **手上是 `DFGE` 那篇 raw**（不是转引 wiki 页）。
> **`DFGP` 那一格是空的，因为那篇本页没读。**

- [[pin-configuration-file]]（**已建**）— **`DFPT` 的落点**。
  那一页把 `DFPT` 列在例子里逐行出现的命令之中，**并注明「它自己的参数定义在本篇，不在那篇」**。
  （**这一句引自那一页；本页没有打开它核对**。）
- [[port-editor]]（**已建**）— **（推断）GUI 侧**，依据只是名字相近。
  **本篇没有提任何 GUI、没有提任何工具窗口**；**那一页本页没读。**
- [[pin]] / [[mapping-pin]]（**已建**）— 本阶段的脊椎页与映射表。
  **两页都把 `DFPT` 与 `DFGP` / `DFGE` / `UDGP` 并列**（**这一条引自 [[dfgp]] 页的转述，本页没读那两页**）。
- [[conf]] / [[dfpn]] / [[dfps]] / [[udgp]] — **同族命令**（设 pin 类型与工作模式 / 定义 pin 名 /
  定义 DPS pin / 撤销组）。**四个名字本篇一个都没出现**，这里只标同族位置。
- `Configuration Setup Commands`（**未建**）— **原文 `## Application` 的点名对象**。
  **它是章节名，不在 allowlist，用反引号。**
- `@` / `(@@)` — 原文的两种通配写法，**不是页名**。

## 版本

**一条：`Introduced before SmarTest 6.3.2`。**

**没有精确引入版本，也没有任何改动、废弃或重命名条目。**
**注意 `port` 名长度上限那条（16 / 64）没有版本标注**——
所以「64 位放宽到 64 字符」是从哪一版开始的，本篇没说。

## 出处

本页只读了 `sources:` 那一篇（`02.06.02.02.66`）。
**另外读了 `DFGE` 那篇 raw**（写 [[dfge]] 时同一个会话读的），
用于上面那张「重名命运」对照表的第二行——**页内已单独标注哪一格来自哪一篇。**

**本篇没有 `## Errors`，也没有 `## Warnings`。**

**本页没有做的事：**

① 没有读 [[dfgp]] 的 raw——所以那张对照表的 `DFGP` 那一格是空的；
② 没有读 [[pin]] / [[mapping-pin]] / [[pin-configuration-file]] / [[port-editor]] 中任何一页；
③ 没有读 `Configuration Setup Commands` 那一章——**`DFPT` 在 pin 配置流程里的位置、以及它和 `CONF` 的先后关系，本页没有**；
④ 没有验证「port 与 pin 组有什么区别」（**本篇根本没写，不是本页没找**）；
⑤ **没有找到「从 port 里移除一个 pin」的办法**——本篇没有给，但**本页无法断言语料别处也没有**。

**引用规模**：`extract/hubs-dedup.csv` 记本篇被 **5 篇**文档引用（`in_src=5`）。

### ⚠️ 语料瑕疵（逐字，本页不代改）

> ① **小标题拼错：`## DFTP`。** 定义那一节的标题把 `DFPT` 写成了 `DFTP`——
> **而它里面的代码块拼的是对的**（`DFPT {(pinlist)}, {(port)}`），
> **紧跟在它后面的另一个小标题 `## DFPT?` 也是对的。**
> **所以同一页上，错的那个标题夹在两个正确拼写之间。** 本页逐字保留 `DFTP`，不代改。
> ② **`## Parameters` 整张表散架**：**没有表头行**，`|` 各自单独占一行，
> 三格（`pinlist` / `port` / `portlist`）靠连续空行分隔，**`portlist` 那一格的行结构还与前两格不同**
> （前两格有收尾的 `|`，它没有）。
> ③ **没有 `## Syntax` 段**：语法放在 `## DFTP`（拼错的那个）与 `## DFPT?` 底下。
> **脚本的段名表只认 `Syntax` / `Parameters` / `Example`**，
> 所以本页「语法 / 参数」节里**只有参数表、没有那两行语法**
> （见 `extract/findings-scaffold-syntax.md`）。
> **§4 规定该节不许手改，故本页把语法写在上面 `## 典型用法` ① 里。**
> ④ **例子的返回里含省略号 `...`**：`DFPT (CP_1,DS7_1,DS0_1,I/O7_1,...,I/O0_1,Q7_1,`——
> **这个 `...` 是原文里的**，**而原文没有说固件答复里真的会打印省略号、
> 还是文档自己把长名单截短了。**
> ⑤ **`## Application` 与 [[dfge]] 那篇逐字相同**（`Pin Configuration, see Configuration Setup Commands.`）——
> **同族命令的落点句是同一句复制过来的**，没有各自说明自己落在流程的哪一步。
> ⑥ **没有 `## Errors` / `## Warnings`**：未知 port 名、非法 pin 名、
> **以及最要紧的「port 名超过 16/64 字符会怎样」——全部未写**。
> **上限在 `Parameters` 里给了，后果一个字没有。**
> ⑦ **16 / 64 这个上限挂在「32 位 / 64 位 SmarTest」上**，
> **原文没有说读者怎么知道自己属于哪一种。**
> ⑧ **追加语义没有配任何上限或撤销手段**：可以反复对同一个 port 名追加，
> **本篇没有给「减」，也没有给「最多多少」**。
> ⑨ **两个通配符（pin 的 `@`、port 的 `(@@)`）形式不同，原文没有并排解释**，
> 只在 `Parameters` 表的两格说明里各出现一次。
> ⑩ **没有 `## Related information` 一节**：与同族命令的关系全靠正文里那几处链接承载。
> ⑪ **例子只有 `DFPT?`（读），没有一条 `DFPT`（写）的完整例子**——
> **所以「追加」这个行为在原文档里没有任何演示。**
