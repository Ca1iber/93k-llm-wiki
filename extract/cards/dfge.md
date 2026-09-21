# 取证卡：`dfge`

- **状态**：悬空 wikilink 目标（被引 5）
- **引用它的页**：`wiki/objects/dfgp.md`（3 处）、`wiki/mappings/mapping-pin.md`、
  `wiki/stages/pin.md`
- **取证日**：2026-09-21

## raw

`02_System_reference/02.06_Command_Reference/02.06.02.02.59_DFGE__DFGE__-__DeFine_Group_by_Expressions.md`

- 字节：**3787 B**
- 行数：**193**
- **in_src = 5**
- topic = `98544`，单副本

## 是什么

**`DFGE` / `DFGE?` 命令**——`DeFine Group by Expressions`：
用**表达式**定义一个 pin 组。表达式由 pin / pin group 名与集合运算符
`+`（并）、`*`（交）、`-`（差）构成，可用括号。
`DFGE?` 查询返回组的类型与表达式；固定型数字组则由 `DFGP?` 返回。

## 已有页

**无** object / concept / constraint 页认领。

- `wiki/stages/pin.md` 认领了（`stage`，**不算**）
- `wiki/objects/` 下有 `dfgp.md`（**不同命令**），**没有** `dfge.md`

## 建议

- **type = `object`**
- **layer = `L1`**（固件/命令层；`wiki/stages/pin.md:239` 已标 `[[dfge]]` `L1`）
- **stage = `pin`**

## 依据（逐字）

> The DFGE (DeFine Group Expressions) command defines an expression based group. Pin groups can be used as though they were individual pins. The DFGE? query returns the group type and group expression of the named group.

> returns the union of its arguments, that is, all pins that are contained in one of its arguments.

> An error is generated if: … The group definition is recursive. … The group expression is empty.

> Introduced before SmarTest 6.3.2

## 风险

1. **⚠️ §12.1：命令参考章单篇命令，有意不逐篇建页。**
   `02.06_Command_Reference` 那 975 篇的范围决定（2026-09-20 定）是**按需补建**。
   `dfge` 在 `02.06.02.02.59`，**正落在这条范围内**。
   若判断「不建」，则应把这 **5 处**引用改成不链（按 §9.1「清单外的名字不造悬空目标」）
   或在 [[pin]] 页的清单里保留为不链的正文名。
2. **不要据 `dfgp.md` 推 `DFGE` 的内容。**
   `wiki/objects/dfgp.md:159` 明写：

   > `[[dfge]]` — **另一条命令**（表达式型 pin 组）。**`DFGP` 自己的文档从头到尾没有提过 `DFGE`**（本页实测 0 命中）

   即：`DFGP` 那篇 raw **一个字都没提 `DFGE`**。若要为 `DFGE` 建页，
   内容**只能**来自 `02.06.02.02.59` 本篇，**不能**从 `dfgp` 页抄。
3. **两种组的关系在语料里是「并列」而非「互指」。**
   `DFGE?` 的返回值里**会**出现 `DFGP …`（固定组形态），
   这是**唯一**一处本篇提到 `DFGP` 的地方——是**查询返回格式**，
   不是「两者是同一件事」的证据。
4. 本篇 `## Errors` / `## Warnings` 很长（各 8 / 3 条），且包含**上限数字**
   （最多 2400 个组、全部组内 pin 总数上限 1843200）。这些是**可核验的硬数字**，
   建页时若引用必须逐字、不得改写。
5. 出链 `## Application` 只指向 `Configuration Setup Commands`（`02.06.03`），
   **没有**指向任何 GUI 页。`mapping-pin.md:50` 把 GUI 格填成 `[[pin-group-editor]]`
   是**那张表自己的对应声明**，不在本篇。
