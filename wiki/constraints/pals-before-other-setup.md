---
type: constraint
title: PALS 必须在任何其他 setup 命令之前
layer: L1
stage: pin
tags: [constraint, pin-configuration, multi-site]
related: [[pin]], [[pals]], [[dfpn]], [[conf]], [[pste]], [[pin-config-requires-sequencer-off]]
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.173_PALS__PALS__-__Pin_ALlocation_for_multiple_Sites.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# PALS 必须在任何其他 setup 命令之前

## 约束是什么

**`PALS` 必须在任何其他 setup 命令之前使用，包括 `CONF`。** 文档原句：

> Note that PALS must be used before any other setup command (including CONF).

## 在什么条件下成立

- **只对多 site 配置有意义。** `PALS` 的职责是给 **site 1 以外**的 site 分配通道；
  site 1 的通道由 `DFPN` 定义：

  > Channels for site 1 are defined with DFPN.

- **`site` 参数的取值有下界**（同篇）：

  > The integer must be greater than 1

## 违反了会怎样

> **⚠️ 文档没写「顺序错了会怎样」。** 原句是 "must be used before"，
> **没给报错形态，也没说后果**。本页不猜。

`PALS` 自己有一张 Errors 列表（同篇），**那四条与顺序无关**，是参数与状态检查：

> - The specified channel number is not valid;
> - The specified channel is not installed;
> - The specified pin name is already used as a group name;
> - The sequencer is in RUN or BREAK mode.

（**原文是列表，本页照抄列表**；引文里的 `- ` 与分号都是原文的一部分，§11.1。）

## 工程上应该把多 site 配置放在哪里

> **⚠️ 下面这段是推断，不是文档事实。** 推断链写在下面，**证据只有两条**：

1. **文档事实**：site 1 的 channel 由 `DFPN` 定（"Channels for site 1 are defined with DFPN."）。
2. **文档事实**：`PALS` 必须在**其他任何 setup 命令之前**。

**推断**：两条合起来，多 site 配置应当放在**整个配置的最前面**——
在 site 1 的 `DFPN` 之后、`CONF` 之前。**理由**：`PALS` 的「之前」如果包括 `DFPN`，
它就没有 site 1 可依附（site 1 是 "which always exists"，但它的通道名还没定）；
而 `PALS` 又必须在 `CONF` 之前。**两条约束只有这一个交点。**

**这个推论本次未在 raw 里找到直接确认**，所以它是**推断**、`verified: doc-only`。
**上机验证的办法**：把 `PALS` 放在 `CONF` 之后跑一次，看是否报错——
**报错就证伪了「之前」的宽松读法，不报错也不等于两种顺序等价**（文档可能只是没检查）。

## 出处

| raw | 里面的原句 |
|---|---|
| `02.06.02.02.173_PALS__PALS__-__Pin_ALlocation_for_multiple_Sites.md` | Note that PALS must be used before any other setup command (including CONF). |
| 同上 | Channels for site 1 are defined with DFPN. |
| 同上 | The integer must be greater than 1 |

**三句都在同一篇里**（`02.06.02.02.173`）。`DFPN` 自己那篇
（`02.06.02.02.63`）**通篇没提 site 1**——所以它不是本页的 `sources:`，
本页链 `DFPN` 是因为要跳过去看那条命令，**不是因为它是证据**。

## 相关约束

- [[pin-config-requires-sequencer-off]]——`PALS` 也在那条锁的管辖内。
- [[pste]]——定 site 数量，与 `PALS` 同属多 site 流程。
