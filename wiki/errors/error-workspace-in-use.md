---
type: error
title: 启动 SmarTest 报 workspace 被占用 / NFS 文件锁不可用
tags: [error, startup, workspace, nfs, file-lock]
related: [[project]]
sources:
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.04.02_Warnings_and_error_messages_when_starting_SmarTest.md
created: 2026-09-18
updated: 2026-09-18
verified: doc-only
---

# 启动 SmarTest 报 workspace 被占用 / NFS 文件锁不可用

## 症状

**在 SmarTest 启动阶段报出来**（不是跑测试的时候）。文档给了两条：

> Workspace in use, choose a different one.

> java.io.IOException: No locks available

**两条的处置是同一套**，所以本页放在一页里——
**它们不是同一句话的两种写法**（一个是「别人占着」，一个是「文件锁根本用不了」），
但**解决办法重合**（见下）。

## 触发条件

**共同的根因是「这个 workspace 上的文件锁拿不到」**，两种情形：

- **别的进程／别人正在用同一个 workspace。**
- **workspace 放在 NFS 挂载的 home 目录上，而那台 NFS 不允许文件锁。**
  第二种和「谁在用」无关——**没人用也照样报**，这是它和第一种的分别。

> 说明：「共同根因」这一句是**本页的归纳**，不是文档明写的。
> 依据是**两条给的第一条建议是同一句**（原文里那句话出现了两次，见「出处」的说明）。

## 怎么办

**两条建议，原文各一行（照抄，含列表符 `- `）：**

> - Check if another user is working in the specified workspace.

> - Check with your system administrator that on NFS mounted home directories file locks are allowed. If file locks are not allowed, create your workspace under /var/....

**第二条里那句是要点**：**在 NFS 上文件锁被禁掉时，把 workspace 建到 `/var/...` 下面。**
`/var` 是本地盘，绕开了 NFS——**这是文档给的绕过办法，不是权宜之计。**

## 同一篇里还有一个「启动时的 Warning」（不是错误）

**启动阶段不只有错误，还有一条要你补引用工程的提示**：

> On start up SmarTest checks all references, including the device and referenced test methods and asks you for any referenced project that is not yet imported.

**处置是一步动作**：

> - To import referenced projects, click Import missing projects into workspace to import projects:

**这条为什么值得单独写出来**：它是**警告不是错误**，但**不处理就没法往下做**——
「引用的工程还没导进来」时，后面任何依赖那个工程的东西都会出问题。
**看到它不要当噪声略过。**

> ⚠️ 原文这两处各跟着一张截图（`![Warning window](<…>)` / `![Import projects into workspace](<…>)`），
> **本页转述了截图旁边的文字，没有转述图**——图里是什么，本页说了不算。

## 文档没写清的地方

1. **`Workspace in use` 时怎么确认「是谁在用」，文档没写。** 只让你去 "Check"。
   进程名、锁文件位置、查看命令——**本次未找到**。
2. **`/var/...` 的 `...` 是什么，文档没写全。** 原文就是三个点。
   **本页不猜具体路径**——按字面，它指的是「`/var` 下面某个本地可写位置」。
3. **两个报错和两条建议的**逐条**对应关系，文档的单据被摊平了，读不准。**
   原文是一张 `Error` / `Solution` 两列表，**`sections.jsonl` 抽出来的是一串单元格**，
   单元格边界在抽取时就丢了（同一个毛病在 `DDIC` 那篇的参数表上也出现过，
   见 [[cross-card-ganging-requires-ddic]] 里那段「不能当文档矛盾用」）。
   **能确证的**：两条建议里的第二条在原文里**出现两次**（两张行的 Solution 格都是它），
   所以它**对两个报错都适用**——这一点是数出来的，不是读出来的。
4. **版本**：这一篇的 `## Functional changes` 写的是
   `- Introduced before SmarTest 6.3.2`——**哨兵值，不是版本事实**（§11.2 ②）。
   本页不据此写版本。

## 出处

| 说法 | raw |
|---|---|
| 启动时检查引用、补导工程的 Warning | `01.01.04.02_Warnings_and_error_messages_when_starting_SmarTest.md` |
| `Workspace in use, choose a different one.` | 同上 |
| `java.io.IOException: No locks available` | 同上 |
| NFS 文件锁那两句（**原文出现两次**） | 同上 |
| 「另一条建议」的原文：`- Check if another user is working in the specified workspace.` | 同上（**只出现一次**） |

同一篇 raw 还挂了两个相关页：
`01.01.04_SmarTest_workspaces.md`（workspace 是什么）与
`01.01.04.01_SmarTest_Work_Center.md`（本页所在章）。**两篇都没有 wiki 页**，
所以本页写成文件名、不写 wikilink（§9.1）。

文档事实，`verified: doc-only`。

## 相关

- [[project]]——「引用的工程没导进来」那个 Warning 牵涉的对象；
  `project` 是**九页脊椎里的一页**（stage 页），能点动。
- `workspace`（工作区）——**这一页不存在，所以不写它的 wikilink**（§9.1）：
  `workspace` 既不在 `extract/dangling.csv`，也不在 `extract/unowned.csv`。
  讲 workspace 的原文是 `01.01.04_SmarTest_workspaces.md`（路径见上表）。
