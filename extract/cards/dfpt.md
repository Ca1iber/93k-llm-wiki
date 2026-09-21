# 取证卡：`dfpt`

- **状态**：悬空 wikilink 目标（被引 5）
- **引用它的页**：`wiki/objects/dfgp.md`（2 处）、`wiki/mappings/mapping-pin.md`、
  `wiki/stages/pin.md`、`wiki/objects/pin-configuration-file.md`
- **取证日**：2026-09-21

## raw

`02_System_reference/02.06_Command_Reference/02.06.02.02.66_DFPT__DFPT__-__DeFine_PorT.md`

- 字节：**1622 B**
- 行数：**81**
- **in_src = 5**
- topic = `98552`，单副本

## 是什么

**`DFPT` / `DFPT?` 命令**——`DeFine PorT`：**定义一个 port**（一组可独立跑不同 timing / 独立 sequencer 程序的 pin）。
**复用同一个 port 名会把新 pin 追加到原定义上**（不是覆盖）。
`DFPT?` 用来查单个或全部 port 定义。

## 已有页

**无** object / concept / constraint 页认领。

- `wiki/stages/pin.md` 认领了（`stage`，**不算**）
- `wiki/objects/pin-configuration-file.md` **正文里链了** `[[dfpt]]`（`sources:` 里**没有**认领它）
- `wiki/objects/` 下没有 `dfpt.md`

## 建议

- **type = `object`**
- **layer = `L1`**（`wiki/stages/pin.md:248` 已标 `[[dfpt]]` `L1`）
- **stage = `pin`**

## 依据（逐字）

> The DFPT (DeFine PorT) command defines a port. Reusing a port name causes the pins in the new port definition to be appended to the pins in the original definition.

> The DFPT? query is used to check a single or all port definitions.

> The name of the port to which the pins are associated. The maximum number of characters is 16 for 32-bit SmarTest and 64 for 64-bit SmarTest.

> Introduced before SmarTest 6.3.2

## 风险

1. **⚠️ §12.1：命令参考章单篇命令，有意不逐篇建页。**
   与 `dfge` 同理，`02.06.02.02.66` 落在 `02.06_Command_Reference` 范围内。
   **但注意**：`wiki/objects/pin-configuration-file.md:203` 已经写下既有决定：

   > `[[dfpn]]` / `[[dfps]]` / `[[dfpt]]` / `[[dfpr]]` / `[[pste]]` / `[[conf]]` — **例子里逐行出现的命令**（**`DFPS` / `DFPT` / `DFPR` 未建，但它们在 allowlist 里，所以照链**）

   即：**这三个 slug 被列在 allowlist 里、被有意允许悬空链**。
   这与 §12.1 的「不逐篇建」**并存**，本卡只陈述这条既存事实，**不代替决定**。
   若最终决定建页，应同步更新那一句「未建」的措辞。
2. **⚠️ raw 自身的拼写不一致——引用时要留意。**
   门面标题是 `DFPT, DFPT? - (DeFine PorT)`，但正文里的小标题写成了：

   > ## DFTP

   （`DFTP` ≠ `DFPT`，是 raw 里的笔误。）
   逐字引用该行时必须**保留原样并加注**，否则会被 `check_*` 类脚本判为改写。
3. **`port` 是什么，本篇给的定义很薄。**
   本篇只说了「定义一个 port」与「可复用/追加」，
   **`wiki/stages/pin.md:248`** 那句「一组可独立跑不同 timing / 独立 sequencer 程序的 pin」
   **不在本篇 raw 里**（那是 spine 页的归纳）。建页时不得把那句当本篇依据。
4. 与 `dfge` 一样，本篇 `## Application` 只指向 `Configuration Setup Commands`（`02.06.03`），
   **没有** GUI 出链。`mapping-pin.md:51` 的 GUI 格 `[[port-editor]]` 是那张表的声明。
5. `[[dfgp]]` **不是** `[[dfpt]]` 的上位概念——两者是并列的命令。
   `wiki/objects/dfgp.md:194` 把这层关系写得很清楚（`CONF` / `DFPT` / `UDGP` 同族并列）。
