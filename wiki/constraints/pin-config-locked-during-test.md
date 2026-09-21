---
type: constraint
title: 测试运行中固件不接受任何配置改动
layer: L1
stage: pin
tags: [constraint, pin-configuration, firmware]
related: [[pin]], [[level]], [[timing]], [[pin-config-requires-sequencer-off]]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.03_Pin_configuration_setup_commands.md
  - 02_System_reference/02.06_Command_Reference/02.06.03.01.01_Introduction.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# 测试运行中固件不接受任何配置改动

## 约束是什么

**测试运行期间，firmware 不接受任何配置改动。** 文档原句（在**两篇不同文档**里各写了一遍，
`source_topic` 分别是 `10649.htm` 和 `10650.htm`，**不是重复投放**，见 §10 的判据）：

> The firmware does not accept any configuration changes while a test is running.

## 在什么条件下成立

文档**没有把「配置」限定成 pin configuration**——原句说的是
"any configuration changes"（**任何**配置改动），而这句话出现在
**Pin configuration setup commands 这一章**里。

- **文档事实**：不接受的改动范围写作 "any"。
- **⚠️ 范围是本页的推断，标出来**：这句话**能确证的下界**是 pin configuration
  （发表位置就在该章）；**它是否也覆盖 level / timing / pattern 的改动，本次未找到明说**。
  §2.1 的铁律：**「我没找到」和「文档没有」是两件事，页面只许写前者。**
  所以本页写「文档未把范围限定在 pin configuration」，**不写「覆盖全部 setup」**。

## 违反了会怎样

> **⚠️ 本次未找到任何描述报错形态的原文。**

两篇文档都只说了 "does not accept"，**没有一句写「会报什么错」**。
本页**不猜**（§11：不臆造）。工程上的可能形态有几种（命令被忽略 / 返回错误 / 返回旧值），
**但那都是推断，不写进本页的文档事实栏**。

**怎么回避这个问题**：别在测试运行中改配置——需要改就先把测试停下来。

## 与 [[pin-config-requires-sequencer-off]] 的关系

这两条**不是同一条**，别合并：

| | sequencer 状态约束 | 运行中锁定 |
|---|---|---|
| 说的是 | 改配置**要求** sequencer 是 OFF | 测试**运行中**不接受改动 |
| 判据 | `SQST` 的状态 | 测试是否在跑 |
| 违反的后果 | 文档明写报错（逐命令） | **文档未写** |

**两条一起才构成完整的前置条件**：OFF 是「可以改配置的窗口」，
但**窗口开着也不等于此刻能改**——OFF 之后、测试还没跑起来，才是能改的窗口。

## 出处

| raw | 里面的原句 |
|---|---|
| `02.06.03_Pin_configuration_setup_commands.md` | The firmware does not accept any configuration changes while a test is running. |
| `02.06.03.01.01_Introduction.md` | 同上（逐字相同） |

文档事实，`verified: doc-only`。

## 这条约束怎么被发现的

**不是靠 `Dependency` / `Before you begin` 这类显式标注段**——
它写在**章首的 Note 里**，而 `sections.jsonl` 的结构段抽取**不覆盖 Note**。
发现途径是写 [[pin]] 时逐句读了 `02.06.03` 这一章。

> 这件事本身值得记一笔：`extract/constraints.py` 按「同一句规矩在多少篇文档里复现」捞候选，
> 而**这条只出现在 2 篇文档里、且分散在章首 Note**，按那个判据它排不进候选头部。
> **机械判据抓得到的是「广而重复」的约束，抓不到「窄而致命」的约束**——
> 本页是后者的实例，靠的是人读。（§4：脚本产出机械索引，不替代人读。）
