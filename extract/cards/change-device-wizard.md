# 取证卡：`change-device-wizard`

- **状态**：悬空 wikilink 目标（被引 5）
- **引用它的页**：`wiki/mappings/mapping-project.md`（3 处）、`wiki/stages/project.md`（2 处）
- **取证日**：2026-09-21

## raw

`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.03_Change_Device_wizard.md`

- 字节：**1314 B**（`len(path.read_bytes())`，含全 CRLF）
- 行数：**25**（`wc -l` 口径，未 +1）
- **in_src = 6**（口径：`extract/hubs-dedup.csv` 的 `in_src`，非 `hubs.csv`）
- topic = `111004`，单副本（同标题在 hubs-dedup 里只有 1 行）

## 是什么

SmarTest GUI 里的一个向导，用来**激活一个已有 device**并**编辑该 device 的 technology data**。

## 已有页

**无** object / concept / constraint 页认领。

- `wiki/mappings/mapping-project.md` 认领了（`mapping`，**不算**）
- `wiki/stages/project.md` 认领了（`stage`，**不算**）
- `wiki/objects/` 下**没有** `new-device-wizard.md` 也没有 `change-device-wizard.md`
  ——姊妹页 `[[new-device-wizard]]` 同样是悬空目标

## 建议

- **type = `object`**
- **layer = `gui`**
- **stage = `project`**

## 依据（逐字）

> With the Change Device wizard, you can activate a device and edit the technology data of the device.

> Introduced in SmarTest 6.5.2

## 风险

1. **⚠️ 同名异物——不许合并。** `wiki/mappings/mapping-project.md:339` 已经就这一点写过警告：
   HVM 远程控制命令 `ChangeDevice`（raw `02.09.01.10.03.02.02.12`，「sets the designated device for a SmarTest session」）
   与 GUI 的 Change Device wizard **词面相同、位置不同**（`02.09.01.10` vs `02.08.04.03`）。
   两边的出链**互不指向**。建页时**必须**把这条区别写进页面，否则读者会把两者当同一个。
2. **姊妹页缺位。** 本篇 `## Related information` 与 `#### Subtopics` 都指向 `New Device wizard`
   （`02.08.04.15`），该页在本 wiki 里**也没有**。只建 `change-device-wizard` 会让
   「建 device / 激活 device」这条链只补一半。
3. **不是命令参考篇。** 它在 `02.08_Setup_and_Result_Tools` 下，**不受 §12.1 约束**
   （§12.1 只挡 `02.06_Command_Reference` 的 975 篇）。所以「按需补建」在这里不适用，
   它是正当的 object 候选。
4. 出链只有 4 条子页 + 2 条 Related information，**没有**一条指向 HVM 那侧，**不能**据本篇推 HVM 行为。
