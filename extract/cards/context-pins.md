# 取证卡：`context-pins`

- **状态**：悬空 wikilink 目标（被引 5）
- **引用它的页**：`wiki/concepts/how-to-create-a-universal-test-method-class.md`、
  `wiki/mappings/mapping-testmethod.md`、`wiki/objects/spec-value.md`、
  `wiki/objects/spec-variable.md`、`wiki/stages/testmethod.md`（各 1 处）
- **取证日**：2026-09-21

## raw

**定义它的那篇**：`02_System_reference/02.07_Test_Method_Reference/02.07.02.02.02_How_to_create_a_universal_test_method_class.md`

- 字节：**7317 B**
- 行数：**94**
- **in_src = 23**
- 单副本

**同名的 API 篇（不是定义篇，见「风险」）**：

| raw | 字节 | 行 | in_src |
|---|---|---|---|
| `02.07.04.01.14.08_CCTgetContextPins.md` | 833 B | 36 | **2** |
| `02.07.04.01.14.32_CCTsetContextPins.md` | 865 B | 52 | **2** |

## 是什么

test method 的**参数类型 `ContextPins`**（SmarTest 7.2.0 起），
用来定义 concurrent test framework 里的 `CCF_FocusedPins` 参数。
它是「参数类型清单」里的一个**类型**，不是动作、不是命令。

## 已有页

**无** object / concept / constraint 页认领。

- `wiki/concepts/how-to-create-a-universal-test-method-class.md` 认领的是 `02.07.02.02.02`
  这篇 how-to 本身，**不是** `context-pins` 这个类型。
- 同一批五个类型里，**只有 `spec-value`、`spec-variable` 建了页**；
  `file-string`、`option-list`、`context-pins` **三个都悬空**。

## 建议

- **type = `concept`**
- **layer = `L2`**（test method 参数类型属 L2 API 层）
- **stage = `testmethod`**

## 依据（逐字）

> ContextPins is used to define the parameter [CCF_FocusedPins](...) in the concurrent test framework.

> SmarTest 7.2.0: New parameter types: ContextPins, OptionList

> The type can be int, double, string, PinString, SpecVariable, SpecValue, ContextPins, OptionList or FileString.

## 风险

1. **⚠️ 命令参考章单篇命令——§12.1 有意不逐篇建页。**
   `CCTgetContextPins`（in_src=2）与 `CCTsetContextPins`（in_src=2）都在
   `02.06_Command_Reference` 下。按 §12.1 的范围决定，**它们不建对象页**。
   所以 `[[context-pins]]` **不应该**指到那两篇上去。
   定义在本篇 how-to（`02.07.02.02.02`，in_src=23），**这才是该认领的 raw**。
2. **命名易混——不要与 `[[execution-context]]` 互链。**
   `wiki/objects/execution-context.md` 已存在，讲的是 mode / execution context
   （`CTXT`、`Mode contexts`、sequencer 的同步/独立上下文那一族）。
   `ContextPins` 是 test method 的**参数类型**，**两者不是一回事**，
   仅词面都含 "context"。建页时**不要**把两者接起来。
3. **第三方相关篇**：`02.07.08.04_Test_method_parameters.md`（in_src=6）讲的是
   `CCF_FocusedPins` **参数本身**（值可以是 pin 名 / pin group 名 / port 名 / DPS pin 名），
   与本篇的**参数类型 `ContextPins`** 是两个层次。引用时要分清。
4. 「五个类型」这条清单只出现在本篇 + `wiki/mappings/mapping-testmethod.md` 的表里。
   若只建 `context-pins` 而 `file-string` / `option-list` 继续悬空，
   那五个并列的链接会**三缺二**，读者看到的仍是一张破表。
