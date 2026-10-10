---
type: object
title: PQFC, PQFC? - (Parallel Query FoCus)
layer: L1
stage: pin
tags: [pqfc, firmware-command, query-focus, site-focus, multi-site, pin-configuration, l1-command]
related: [psfc, pste, pals, site-control-window, site-focus-required-before-command, controlling-multiple-sites, mapping-pin, pals-before-other-setup]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.03.02.19_PQFC__PQFC__-__Parallel_Query_FoCus.md
created: 2026-09-21
updated: 2026-09-21
verified: doc-only
---

# PQFC, PQFC? - (Parallel Query FoCus)

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **348 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.03.02.19_PQFC__PQFC__-__Parallel_Query_FoCus.md>`。**不是转述。**
> §4 说语法/参数表由脚本抽、不许 LLM 重写；§3 说「不抄原文」指的是
> **别把整篇文档搬进 wiki**，不是「参数表也要改写一遍」——
> 改写参数表就是把文档事实降级成我的转述（§11）。
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### PQFC

```
PQFC {site}
```

### PQFC?

```
PQFC?
```

### Parameters

> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/98688_2.htm`
> 中**第 1 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：1 行 × 2 列。
> 首行（上游原文）：site | The site parameter is single integer representing the number of the site that has or shall have the query focus.

### Example

```
PQFC 2
```

This example sets the query focus to site 2.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.03.02.19_PQFC__PQFC__-__Parallel_Query_FoCus.md>` 的 `## Warnings`、`## Errors` 段。
> **不是转述**（§4：脚本能产出的不许调 LLM）。**本页没有增删一个字**；
> 段内的语料内部相对链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Warnings

PQFC returns a warning if the specified site is not available. In such cases the query focus is not changed.

### Errors

An error is generated if not all pins at the site have had their channels assigned by the PALS command. \

<!-- 报错节 end -->

## 是什么

**`PQFC` 设的是「查询焦点」——同一时刻只有一个 site 在焦点里，`PQFC` 决定是哪个。**
原文第一句把它的作用域钉死了：

> 「The PQFC command defines which site has the query focus. This site is the only site
> for which setup data can be retrieved or results displayed. The PQFC? query returns
> the site which currently has the query focus.」

`retrieved or results displayed` 这一半是全部范围：焦点 site 是**唯一**能取 setup 数据、
能显示结果的 site。`PQFC` 写、`PQFC?` 读。

### 焦点有两条，`PQFC` 只管其中一条

`PQFC` 管**查询焦点**（取回来的数据属于哪个 site），
[[psfc]] 管 **setup 焦点**（后续命令改的是哪些 site 的配置）。**两者是成对的、方向不同。**

> **这一组对照是本页据 [[psfc]] 那一页说的。本篇 raw 只写 `query focus`——
> 全篇没有 `setup focus`、没有 `PSFC`、也没有 [[psfc]] 的链接。**

### 上电后焦点不一定是 site 1

> 「After loading the pin configuration the query focus is set to the first available site.
> This might not be site 1. The available sites are represented by a "1" in the reply
> to PSTE? STR.」

**原文在这里自己划了重点（`This might not be site 1`）**——
「site 1 拿着焦点」是个**不能假设**的前提。要知道现在是哪个 site，只有两条路：
`PQFC?`，或者读 [[pste]] 的答复（**原文说可用 site 在里面是 `1`；
但 `STR` 没展开，答复格式也没给**）。

### `CAUTION`：这一条建议改用 `tpi`

> 「CAUTION This command implements the tpi interface for multisite testing.
> Use the tpi call instead of this firmware command.」

**这是一条「别用固件命令、改走 `tpi` 调用」的原厂建议**，位置在正文第一段之后。
**`tpi` 全篇只出现在这一句里，没有定义、没有例子、也没有链接。**

## 典型用法

**① 设焦点：`PQFC {site}`。** 唯一参数 `site` 是一个整数
（原文：`single integer representing the number of the site that has or shall have the query focus`）。
语法节给的例子是 `PQFC 2`，说明「把查询焦点设到 site 2」。

**② 查焦点：`PQFC?`**，无参数，返回当前拿着焦点的 site。

**③ 什么时候必须设：** 这件事的作用面由 [[site-focus-required-before-command]] 那条约束定义——
有一批固件命令**只作用于当前焦点里的 site，用之前必须先设焦点**。
**那一页把 `PQFC` 归在「Query site focus」一侧。**
（**这一句引自该约束页；本篇 raw 里没有那张清单表。**）

**④ 多 site 取结果只能逐个来。** 因为 `the only site`——
一次只有一处焦点，「把所有 site 的结果拿全」在用法上是一轮一轮切过去，
不是一条命令给全。（**「必须轮流」这个结论是
[[site-focus-required-before-command]] 页展开的，本篇只写到「唯一」这一层。**）

**⑤ 设置失败时焦点不动。** 见下方 `Warnings`：**指定的 site 不可用 → 返回 warning，
且焦点保持不变**。**失败不会把系统留在「焦点未知」的状态。**

**⑥ 只有一条出错条件**：**该 site 上还有 pin 没由 [[pals]] 分配通道**。
即 **`PQFC` 依赖 pin 配置已经做完**——`PALS` 没跑完，连设焦点都不成。

## 和谁有关

- [[psfc]]（**已建**）— **另一条焦点**：setup 焦点。**本页只主张「有这一对」**；
  **那一页的参数、`ALL`、`MCDIgnore` 等本页一个字不写，也没有打开它核对。**
- [[pste]]（**已建**）— **原文点名的可用 site 判据**：`PSTE?` 答复里的 `1`。
  **`STR` 指什么、答复长什么样，本篇没说**；那页本页没读。
- [[pals]]（**已建**）— **`Errors` 里唯一的点名**：pin 通道必须先经 `PALS` 分配。
- [[pals-before-other-setup]]（**已建**）— **同一条依赖的另一侧记法**。
  **那一页收了哪些命令，本页没读，不据它说任何话。**
- [[site-control-window]]（**已建**）— **原文 `## Application` 的全文就是它**（`Site Control window.`）。
  那一页称 `PQFC` 是它的 L1 侧——**那句话出自那一页，不是本篇。**
- [[site-focus-required-before-command]]（**已建**）— **覆盖本命令的那条总约束**。
- [[controlling-multiple-sites]] / [[mapping-pin]] — **同一件事在 L2 / 映射层的记法**。
  **两页本页都没读。**
- `tpi` / `Site Control window`（**GUI 窗口名**）— **原文里的名字**。
  `tpi` 不在 allowlist，用反引号；**它在语料里指什么，本页不知道。**

## 版本

**`## Functional changes` 只有一条：`Introduced before SmarTest 6.3.2`。**

**它没有给出精确的引入版本，也没有任何改动、废弃或重命名条目。**
`Introduced before X` 这个写法本身说明这一条只是「不晚于 X」，不是「在 X 引入」。

## 出处

本页只读了 `sources:` 里那一篇
（`02.06.03.02.19_PQFC__PQFC__-__Parallel_Query_FoCus.md`）。
**本篇在命令参考里属于很短的一类**：`## Application`、`## Warnings`、`## Errors`
三节各只有一句话，`## Functional changes` 只有一行。
`## 是什么` 与 `## 典型用法` 的顺序基本沿用它自己的小节顺序。

**本页没有做的事：**

① 没有回 `02.06.01.05_Site_dependent_firmware_commands.md`（那份「哪些命令吃焦点」的清单表）
去看 `PQFC` 是否列在表里；
② 没有读 [[psfc]]、[[pste]]、[[pals]]、[[psas]]、[[site-control-window]]、
[[site-focus-required-before-command]]、[[controlling-multiple-sites]]、[[mapping-pin]] 中任何一页的 raw；
③ 没有读 `tpi` 的任何文档；
④ 没有验证 `CAUTION` 所说的 `tpi` 接口在 SmarTest 7.10.3 里是否真的可用、是否真的等价；
⑤ 没有找到 `site` 的合法取值范围（见下 ⚠️ ⑨）。

**引用规模**：`extract/hubs-dedup.csv` 记本篇被 **11 篇**文档引用（`in_src=11`）。
（`extract/hubs.csv` 对同一条 rel 给的是另一个数；**§11.5 规定这个数字取 dedup 那一份。**）

### ⚠️ 语料瑕疵（逐字，本页不代改）

> ① **`## Parameters` 的表没有表头、也没有列分隔。** raw 第 28–36 行里
> **每个 `|` 单独占一行**，`site` 与说明文字散在中间行——**整张表是散架的**。
> ② **`## Application` 全文是 `Site Control window. \`**——
> **一个名词短语加一个行尾反斜杠，没有动词。**
> ③ **`## Errors` 也以 ` \` 收尾**（`…assigned by the PALS command. \`）。**反斜杠是原文里的。**
> ④ **`CAUTION` 后面直接接句子**，没有冒号、没有换行分隔：`CAUTION This command implements…`。
> ⑤ **`The site parameter is single integer`** ——**缺冠词 `a`**。
> ⑥ **`tpi` 只在那一句 `CAUTION` 里出现，无定义、无例子、无链接**——
> **而它正是这条 `CAUTION` 让读者转去用的东西。**
> ⑦ **`STR` 同样没有展开**：`the reply to PSTE? STR` 里的 `STR` 全篇无解释。
> ⑧ **本篇没有 `## Related information` 一节**——命令之间的关系全靠正文里那几处相对链接。
> ⑨ **没有给 `site` 的合法范围**：没写下界、没写是否自 1 起算、
> **也没写越界时走 `Warnings` 还是 `Errors`**（这两节各只覆盖一种情形）。
> ⑩ **`## PQFC` 与 `## PQFC?` 是两个并列的二级标题**，本篇**没有 `## Syntax` 段**——
> 脚本抽的语法节因此按这两个标题取材。
> ⑪ **`## Example` 排在 `## Errors` 之后**，与多数命令页把例子放在语法附近的排法不同。
