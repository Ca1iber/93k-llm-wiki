# Purpose — 93K 测试开发 LLM Wiki

## 要解决的问题

让 agent 能**独立完成 Advantest V93000 / SmarTest 测试开发**，而不是只会查文档回答问题。

目标形态：agent 拿到一个器件，能自己走完

```
建工程 → Pin → Level → Timing → Pattern → Test Method → Testflow → 运行 → 结果
```

横跨三层接口：

| 层 | 内容 |
|---|---|
| **L1** | Firmware / setup command（配置文件里的命令） |
| **L2** | Test Method API（C++ 测试方法） |
| **L3** | 外部控制（SmartShell / Test suite control API / HVM） |

## 为什么不是 RAG

已经验证过：向量检索能找到"最相似的单篇文档"，但**组装不出跨文档的完整流程**。测试"如何完整创建一次测试开发流程"，返回的是 testflow 相关文档（相似度 0.54–0.59），而 Pin / Level / Timing / Pattern 完全不出现——因为**这批文档里根本不存在一篇"完整流程"的文档**。

流程是散的，需要被组织出来。这是 wiki 要干的事。

## 为什么不是"把 9,398 篇喂给模型改写"

试过（LLM-Wiki 0.6.11）。258 篇 raw 生成 1,059 页 wiki，约 4.1 页/篇。外推到 9,398 篇：

- 约 38,500 页 wiki
- 约 18,800 次 LLM 调用
- 成本约 ¥2,350，耗时一天以上

**根因是粒度，不是工具。** 逐篇 ingest 就是 O(N)。

**关键观察：语料本身很便宜。** 9,398 篇 / 26.8 MB / 约 670 万 token，通读一遍在任何模型上都是几十块钱以内的事。**贵的是"写"，不是"读"。** 所以正确做法是砍输出：脚本产出参考索引，LLM 只写概念与流程。

## 为什么 wiki 可行

**因为这批文档自己就带着一张关系网。**

- 75% 的文档（7,076 / 9,398）包含指向其他文档的链接
- 全库约 **50,073 条**交叉引用
- 每条链接都带语境句子，写明**为什么相关**

实例（`DFPN` 命令页）：

> "before you can use the DFPN command the sequencer state must be OFF (see the SQST command)"
> "Before cross-card ganging can be used, the connection must be enabled by DDIC"

这些就是**前置条件与依赖**——测试开发流程的骨架。它们早就写在文档里了，只是散在 9,398 个文件中，**没有任何索引能让 agent 找到**。

按被引用次数排名，核心骨架自动浮现：

```
119  PSFC   Parallel Setup FoCus
107  WSUS   Waveform Sets USed
 68  DSCP   Define System Control Parameter
 59  Pin configuration setup commands
 54  DFPN   DeFine Pin Name
 47  DFGP   DeFine GroUP
 46  Timing Setup Commands / SQPG SeQuencer ProGramming
```

**目录树不编码重要性，链接才编码**——`PSFC` 是全库第一枢纽，但埋在 `02.06.02.02.191`，从路径完全看不出来。

## 范围

**在范围内**

- 一个 LLM wiki：raw 层（已有）+ wiki 层（要建）+ schema 层（已定）
- 全栈知识覆盖：L1 + L2 + L3，九段流程

**当前不在范围内（后话）**

- MCP / 工具层（让 agent 真的发命令、改文件、调 API）
- 执行反馈闭环（跑完看结果、失败回查）

**wiki 只告诉 agent「该怎么做」。「做得到」是工具层的事，不要混为一谈。**

## 语料

- **来源**：SmarTest 7.10.3 TDC 文档
- **位置**：`F:\master-dev\dorm-wsl-sytest\tdc-html\agent-markdown\by-category`
- **规模**：9,398 篇 markdown / 26.8 MB / 平均 2,992 字节
- **结构**：4 个大类 → 18 个子类 → 约 110 个四级簇（层级编码在文件名前缀，不在目录里）

```
00_Overview                       2
01_Getting_started              256
02_System_reference           8,317   ← 88%
03_Use_cases_and_papers         574
99_Unlisted                     249
```

**铁律：raw 层不可变。** 缺什么错什么，都在 wiki 层标注，不许回头改证据。
