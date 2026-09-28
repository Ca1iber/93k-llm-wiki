# 93K 测试开发 Wiki — Index

<!-- index-token: cl100k_base=9060 o200k_base=7690 -->

> **这是入口。每次查询第一个读这份文件。**
> 硬约束：必须能塞进一个 context window（预算 < 25,000 token）。**2026-09-20 从 15,000 上调**，理由与代价见 `schema.md` §7；**触发线：22,000 或对象 300 页时回来重定**。
> **本页多大，看上面那行 `<!-- index-token -->`**——**那是本页自己声明的数**，
> 第十四类己 每次对账拿实测和它比（待办 ⑯，2026-09-18 做掉；量法见 `schema.md` §7）。
> 余量 = **25,000 − 那个数**。**⚠️ 这里刻意不写具体数字**：
> 写进来它就成了本页的一部分，改一次要再量一次，**量完又变**——自己喂自己，收敛不了。
> **数字只写在标记里，一处。**
> **量过的历史**（每次都是当时为准，**不是现值**）：11,529（空表）→ 12,415 → 12,862 →
> 13,261（2026-09-18 一天内五次），涨的全是**元信息**（七个 `<!-- index-count: … -->` 标记、
> 一次标题升格、几处说明），**不是新页**。**填约束/排错两节之前查过：拆分前提不成立**，
> 所以**没有**建 `index-constraints.md` / `index-errors.md`（§7：「别把『拆了更整齐』当成『拆』的理由」）。
> **改了本页任何内容之后跑一次 `python -X utf8 extract/check_index_budget.py --write`**——
> 不跑第十四类己 会红，**而那个红是对的**。
（脊椎 9 / 概念 33 / 约束 14 / 对象 289 / 排错 6 / 映射 9）。
**⚠️ 别把上面那个「212」和报告里那个「内容页」数混起来**：第八类的「内容页」= `wiki/` 下除 `log.md`
外的**全部** `.md`（含 143 个版本页与目录页），**是本索引的两倍多**。
同一个词两个意思——本索引说「逐页列出的五类」，报告说「链接检查的范围」。

---

## 阶段（脊椎，9）

<!-- index-count: 阶段 = 9 -->

按测试开发的实际顺序。**九页已建成**，每页固定十节，`verified: doc-only`。

- [[project]] — 建工程 / Device / 目录结构
- [[pin]] — Pin / Channel 配置
- [[level]] — Level 电平配置
- [[timing]] — Timing / Wavetable
- [[pattern]] — Pattern / Vector
- [[testmethod]] — Test Instance / Test Method
- [[testflow]] — Testflow 组装
- [[run]] — Run / Debug
- [[results]] — Results / 数据与判定

对账：`extract/stage-report.md`（**十四类**检验）。**全绿只证明格式齐、
引的文档与引的句子都真的存在、候选没漏、链接不悬空、命名统一、
脚本写的那一节和脚本的产出是同一个东西（**而且该有它那节的页面确实都有**）、
版本页的条目逐字回得到 raw、
**本页每一节列出的页和对应目录里的文件互相都对得上**、
**`extract/wiki-plan.csv` 里每一行的 `status` 和每一页都有登记行**、
**本页自己声明的 token 数和实测一致且没超预算**——不证明内容对。**
「文档事实 / 推断 / 建议」分得对不对、L1/L2/L3 归层对不对、边界守得对不对，
**机器判不了，必须人读**。

## 已知缺口（五条）

<!-- index-count: 已知缺口 = 5 -->

> **2026-09-20 第二次瘦身**：这一节的正文（2,292 token）**一字不删地搬进了 `log.md`**
> 的 `## [2026-09-20] 索引瘦身（第二次）`。**索引留「现在缺什么」，`log.md` 留「怎么走到今天」**（§7）。
> **下面是五条指针**——细节去 `log.md`。
> **这一节不是待办清单，是「已知的坑」**，踩之前先看一眼。

**一、L3 返工已完成**（九页 stage 曾有四页的 L3 断言是错的）。教训：**枚举式的定义漏一项，
会让一个对象没有槽位可放**。→ `schema.md` §2.1

**二、悬空 wikilink 是建页 backlog 的首选清单**：`extract/dangling.csv`（第八类产出）。
⚠️ **它和 `unowned.csv` 是两张不同的单**——前者说「流程页缺了它就断」，后者说「语料里常出现」。

**三、slug 归一已完成**（49 个目标曾被写成非 §5 拼法；`PATTERN` 撞过 stage 名）。
**指错比重复更坏：重复页看得见，指错看不见。** → `schema.md` §5

**四、26 个高入度对象不属于任何 stage —— 已清**。stage 之外照建 `object` 页，判据是**入度**。
⚠️ **工作单清空 ≠ 工作做完**：`in_src < 20` 的对象那张单**从头到尾没管过**。

**五、抽取器漏收过一大块示例代码**（256 篇 / 427,979 字符）——**这是最贵的一次，
而它绿了很久**：「语法节非空」这条规则对它本来就够用。

## 概念

<!-- index-count: 概念 = 33 -->

> **需要理解才能正确使用**的东西。判据：理解错了会导致配置写错（`schema.md` §2.3）。

**2026-09-21 第十批（5 页，与对象那 50 页同批）——全是概念页：**

- [[context-pins]] `L2/testmethod` — test method 参数类型之一（原文那张清单里 9 个名字的第 7 个），**原文对它的全部说明只有一句话**：用来定义 concurrent test framework 里的 `CCF_FocusedPins`；
  ⚠️ 名字里的 `Context` 指 **CTF 的语境**、不是「测试执行期的运行上下文」，且原文在 `CTF` 与 `CCF` 两个缩写之间来回用
- [[edf]] `file/results` — Event Data Logging Format 的章首页，**全篇正文只有 5 条子主题链接、0 句定义句**——「EDF 是什么」**语料未写**，本页只能当目录用；
  ⚠️ 文件名把标题里的 `(EDF)` 括号吃成了两个 `_`，按标题里那个 `(EDF)` 去搜文件会搜不到
- [[flag]] `n/a/testflow` — Testflow Tool 提供的**四类开关**（`Testflow flags` / `Testflow flags for data logging` / `Test suite flags` / `Site control flags`），用于调试与**控制测试的执行**；
  ⚠️ 定义句只说「四类、谁提供、干什么用」，**一个 flag 名都没列**，清单在 `alphabetical-list-of-flags`；优先级那条硬话（test suite 自己的 flag 盖过 test level 与 testflow flag）只在子主题示例里
- [[offline-result-emulation]] `n/a/run` — 在**首片器件到位之前**，让 testflow / test method / DSP routine 拿到**用户按 device specification 定义**的测试与测量结果，**不需要录好的数据**；
  ⚠️ 它有独立的 license 硬门：没有 `S&S_TOOLS_PACKAGE SW` 就 `disabled`
- [[waveform-set]] `n/a/timing` — **存在系统内存里的逻辑容器**（所以本页没有语法、没有文件格式、没有参数表）；装全体 pin 共用的 system clock period / default device cycle name，加**逐 pin** 的 device cycle 表、物理波形表与**一个或多个 timing set**；
  ⚠️ `timing set` 与它是 `forms a part of` 的**包含**关系、不是并列；本页 slug 也**不是** 02.06 那条 `JSWF` 抖动命令

**2026-09-20 第九批（6 页，与对象那 21 页同批）：**

- [[dut-interface-layout]] `n/a/project` — DUT 接口版图；**给画板人的**
- [[utility-lines]] `n/a/pin` — utility line 总入口
- [[setting-up-dc-scale-pins-with-smartrdi]] `n/a/testmethod` — 用 SmartRDI 设 DC Scale pin
- [[smartrdi-tmu-test-setup]] `n/a/testmethod` — SmartRDI 的 TMU 测试设置
- [[test-number-generator-and-tmlimits]] `n/a/results` — 测试编号与 TMLimits
- [[setting-up-a-shmoo-test-with-the-shmoo-tool]] `n/a/results` — 怎么设一次 shmoo 测试

- [[pogo-pad-and-via-design]] `n/a/pin` — DUT board 上 pogo 焊盘/过孔的尺寸规则；**画板子的人用的**，不是测试工程师
  （唯一被推断的一处：「utility/DPS 焊盘要更大是因为要过电流」，原文只说「要更大」）
- [[pogo-block-compatibility]] `n/a/pin` — pogo block 的**兼容性**：SD/HD/VHD 三种 block 的针数与网格差
  （**同系列三页之一**，与上一条、下一条同属 `02.03.07.07`）
- [[inter-layer-via-design]] `n/a/pin` — 板子内部换层的 via 怎么做；**全 wiki 最短的定义文档**（922 字节）
  原文档只给八个变量名、不给数值，所以这页的用法是「去哪里拿数值」
- [[dut-board-grounding]] `n/a/pin` — **接地这件事本身**：对 DUT board 设计者「地」指什么、
  混合信号接地与今天 SOC 接地的分野、**几组互相冲突的设计目标**、设计要过的四个量
- [[logical-boards]] `n/a/pin` — 逻辑板概念；**页里记了一处原文自相矛盾，没有替它裁决**
- [[sequencer-controlled-utility-lines]] `n/a/pattern` — utility line 的**动态访问**：
  由 pattern sequencer 控制，**能与 pattern 同步**；**走内部数据通路还是串行接口取决于机台代次**
  （与对象页 [[utility-line-assignments]] 同族）
- [[gpib-lan-communication-conventions]] `L3/project` — GPIB/LAN 通信约定：**11 个记号**；
  **SRQ 那几条只在 GPIB 下成立**，`+`(1-n) 与 `*`(0-n) 是两个不同的量词
- [[hv-protection]] `n/a/pin` — **高压保护**：什么时候**必须**给 DUT board 加保护电路
  （合规范围表）、保护电路怎么构成、**它带来的代价**（`The 24 V current consumption…about
  4.5 mA…about 30 mA…75 %`、`< 1 nA` / `0.3 ns` 的实测影响）；
  ⚠️ **两篇原文对根因条数说法不一**（主文档 `two`、AVI64 文档 `three`），**页里未裁决**

**2026-09-18 第四批（14 页，照 `dangling.csv` + `in_src ≥ 20` 两批并起来建的）：**

- [[command-reference]] `n/a/project` — `02.06` 整章：**L1 固件命令字典**（**975 篇**）的入口与读法（*2026-09-20 更正：原写 367，实际 975*）
- [[controlling-multiple-sites]] `n/a/run` — **多 site 怎么控制**：焦点、并行、site 间差异
- [[dc-test-programming]] `n/a/testmethod` — DC 测试编程：**这一类测试怎么组织**（不是某一条命令）
- [[direct-probe-stiffener]] `n/a/project` — Direct-Probe stiffener：直针探测时的加强板
- [[dut-board-design-reference]] `n/a/project` — DUT 板设计参考的**总入口**；**语料里被引 95 篇，全库并列第一**
- [[edf-data-organization]] `n/a/results` — EDF 数据**怎么组织**；**语料里被引 78 篇**
- [[edf-data-types]] `n/a/results` — EDF 的**数据类型**；**语料里被引 72 篇**
- [[equation-based-level-setup]] `n/a/level` — **用方程而不是常数**描述 level 条件
- [[ganging]] `n/a/pin` — ganging：**多张卡并联驱动同一个 DUT pin**；跨卡 ganging 要先 `DDIC`（见 [[cross-card-ganging-requires-ddic]]）
- [[how-to-create-a-universal-test-method-class]] `n/a/testmethod` — 怎么写一个**通用**测试方法类
- [[layout-information-dut-board]] `n/a/project` — DUT 板的**版图信息**（尺寸、孔位这类要交给画板人的东西）
- [[setting-chart-display-options]] `n/a/results` — **图怎么画**（坐标轴、刻度这类显示选项）
- [[smartrdi-vector-and-protocol-programming]] `n/a/testmethod` — SmartRDI 下的**向量与协议编程模型**
- [[timing-setup-commands]] `n/a/timing` — `02.06.06` 整章：timing 类 L1 命令成组出现，讲清分组关系

---

## 约束

<!-- index-count: 约束 = 14 -->

> 前置条件、依赖、顺序要求。全栈自动化成败的关键。
> 命名 `<主体>-requires-<前置>`；**同一个谓语不一定是同一条规矩**——四形态判据（顺序前置 /
> 状态前提 / 一致匹配 / 位置归属）见 `schema.md` §2.4。**14 页全部是 `L1`，各带一个 stage。**

- [[pals-before-other-setup]] `L1/pin` — `PALS` **必须在任何其他 setup 命令之前**，包括 `CONF`
- [[pin-config-requires-sequencer-off]] `L1/pin` — 改 pin configuration 前 sequencer 必须 **OFF**；
  **整个命令族共有**（`DFPN`/`UDEF`/`CONF`/`PALS` 各写过一遍，措辞不同）
- [[pin-config-locked-during-test]] `L1/pin` — **测试运行中固件不接受任何配置改动**
  （两篇不同文档各写一遍，`source_topic` 不同，**不是重复投放**）
- [[synchronized-pins-require-same-test-processor]] `L1/pin` — 同步或环回的一组 pin
  必须分在**同一个测试处理器**上；**三篇合成一条**（7+2+1=10 处引用）
- [[cross-card-ganging-requires-ddic]] `L1/pin` — 跨卡 ganging 前必须先用 `DDIC`
  **把 DUT 板上那条连接使能**（不是软件里列在一起就算）
- [[constraint-level-mode-context-match]] `L1/level` — level setup 的 mode context
  必须与 pin configuration 一致；**level / timing / pattern 三处必须相同**
- [[constraint-timing-mode-context-match]] `L1/timing` — 一个 primary timing setup 指向的
  equation set 与 base wavetable 必须属**同一个 mode context**
- [[execution-context-requires-firmware-definition]] `L1/pattern` — `exec_context`
  **不能随用随起名字**，必须先在**固件级**定义过
- [[label-edit-requires-tstl-selection]] `L1/pattern` — 改 label 里的向量/指令前
  必须先用 `TSTL` 把它**选为编辑态**
- [[referenced-set-requires-prior-definition]] `L1/pattern` — 集合类对象（spec value /
  search / jitter / transition test set）**必须先定义再引用，定义过的不能再定义**
- [[rdi-call-requires-begin-end-block]] `L1/testmethod` — `RDI_*` 调用必须在
  `RDI_BEGIN()`/`RDI_END()` 块内，且**块内参数必须一致**（两条形状不同，页里分开写）
- [[testname-requires-matching-limits]] `L1/testmethod` — 参数例程自定的 `testName`
  必须在 test suite 里有**同名 limits**
- [[site-focus-required-before-command]] `L1/run` — 只用「当前焦点 site」的那批命令，
  执行前**必须先设站点焦点**
- [[smc-background-process-locks-config]] `L1/run` — SMC 后台进程跑起来后，
  它读的三样不许再动：**test method class 成员变量 / TMLimits 表 / Mode context**

---

## 映射

<!-- index-count: 映射 = 9 -->

> GUI 操作 ↔ 文件 ↔ L1 命令 ↔ L2 API ↔ L3 接口 的三层对照。
> **九个阶段各一页。** 每页的证据**分四档**写死：**① 语料明说对应** / **② 文档之间有链接** /
> **③ 只有单侧** / **④ 图证**（从 raw 的图里读出来的，**不可检索**——要核只能自己开那张图）；
> 填名字 = 有证据，`?` = 语料没写（**不猜**），`—` = 这一层不存在这个对应物。
> ⚠️ **用 `edges.jsonl` 当证据前必须先剔「跨章重复投放」**——见 `log.md` 2026-09-20 那条。
> ⚠️ **④ 图证还要核版本**：图没有版本标注，**列名/按钮名/字段名**这类命名性的东西，
> 要先查那篇的 `## Functional changes` 有没有更晚的改名（`log.md` 有实例）。

**地基最硬的三页**（语料自己声明了对应关系）：

- [[mapping-project]] `n/a/project` — `.technology` 参数表**逐行**给出「Change Device wizard 字段 ↔
  DSCP 参数」，**比 pin 那页更硬**（那边只声明整链对应）。30 行 / 150 格，52 个 `—`。
  另：`extended_dram_factor` 与 `testpoints` **不走 DSCP 走 DTCP**，所以「L1 列 = DSCP 列」不成立
- [[mapping-pin]] `n/a/pin` — **语料自己给了地基**：pin 配置文件「contains a set of firmware commands
  `corresponding exactly to` the parameters specified within the Pin Configuration tool」。
  **L3 整列是 `—`**（定义动作外部进程插不进来），**L2 只有四行有值**——
  **这个分布本身就是一条信息**
- [[mapping-timing]] `n/a/timing` — **五个列都有实料**，`—` 的分布本身有结构。
  timing setup file **本身就是一份命令脚本**；L2/L3 在这段是「**选择与引用**」不是「定义」

**另有两条结构性发现**：

- [[mapping-level]] `n/a/level` — **level 有两条互斥路线**，而这决定 L1 列怎么读：
  equation based 时 level 是 **`EQSP` 的一个字符串参数**；fixed 时**要用固件命令逐 set 写常量**。
  **所以 L1 填具体命令的行只在 fixed 路线成立**——这是语料自己写的，也是本页最值钱的一格
- [[mapping-pattern]] `n/a/pattern` — **桥是从 L1 那头搭过来的**（命令/API→GUI 63 条，GUI→命令 30 条），
  与 pin/timing 相反。GUI 写 `LOOP`/`RETURN`，`SQPG` 写 `LBGN`/`RSUB`——**名字不同、没编对应物**

**其余四页**（证据较碎，页里都直说了薄在哪）：

- [[mapping-testmethod]] `n/a/testmethod` — **首次把 `01.06` 那四步 GUI 走查与 `02.07` 的 L2 条目对上**
  （主链是语料自己搭的）。**L3 那三格是（推断）**：`02.09.01.14` 全族 92 条出链**一条都没离开 `02.09`**
- [[mapping-testflow]] `n/a/testflow` — 语料明写 flag 的「**两个名字**」（GUI 名 ↔ 文件关键字）
  且 `on`/`off` 在文件与 API 里都是 `1`/`0`。**L1 列基本是空的**，唯一「语料明说」的是 `SVLR`
- [[mapping-run]] `n/a/run` — 价值在**两条完整链条**：起测链
  （`testflow-tool`→`testflow-file`→`SQST RUN`→`START_TEST()`）与 flag 链。
  **本页没有 pin 那种总纲句**，L3 整列 15 格里 10 格是 `?`
- [[mapping-results]] `n/a/results` — **`—` 一格都没用上**：五层在 results 段都真存在。
  采样那件事**有两条不同层的路**（固定走 GUI flag + L3 CPI，自适应走 L2 profile API）

---

## 对象

<!-- index-count: 对象 = 289 -->

**289 页，单独一份：→ [[index-objects]]** (`wiki/objects/index-objects.md`)

> **为什么搬走**：这一节 196 行时已占根索引 26,096 字符；2026-09-28 又建了 93 页，
> 根索引只剩 1,784 token 余量，**再放 93 行必超 §7 的 25,000 预算**。
> §7 对这一刻的规定就是拆子索引，**子索引跟着类型目录走**。
> 页数与清单仍由第十四类甲核对（它已按 `IDX_SUBINDEX` 认这份子索引）。


## 排错

<!-- index-count: 排错 = 6 -->

> **每页从症状写起**（「看到这个报错」），`schema.md` §2.6。**6 页，全部 `verified: doc-only`。**
> ⚠️ **一类容易读错的地方：报错串和"哪一类错误"不是一回事。** 下面第一条就明说
> **没有可搜的报错串**——入口是 report window，不是搜索框。

- [[error-model-file-rejected-at-startup]] — 启动报 model file 错误，**四种类型**，
  症状是**软件起不来**；第四类（license number）例外，可能**降级启动**而不是不启动
- [[error-workspace-in-use]] — 启动阶段报 **workspace 被占用 / NFS 文件锁不可用**
- [[error-flexlm-license-codes]] — **一个负数码 + 一句英文**（−1…−26），
  **同码同义**；⚠️ `−21` 列在这张「错误」表里但**不是错误**；
  ⚠️ **完整码表不在语料里**（指向 FlexNet Licensing End User Guide 的 Appendix E）
- [[error-result-server-transmission-timeout]] — report window 报
  `error occurs during data transmission with Result Server`
- [[error-data-queue-empty]] — `Data Queue Empty`，**execution error**（执行期，不是编译期）
- [[error-utility-power-supply-not-enabled]] — **不是报错文本，是一种现象**：
  外部 utility 电源的输出使不了能

---

## 版本

**目录页：[[index-versions]]**（142 个版本页，5 条产品线、10,393 条，**零 LLM**）。
回答「这个功能哪一版才有 / 哪一版变了」：条目**原样转录**自语料的
`## Functional changes` 段，由 `extract/versions.py` 机械分组（§4 铁律）。
文件一律带产品前缀（`smartest-7.10.3.md`）——**不加前缀会撞名**，版本号跨产品重复（§11.2 ④）。

> ⚠️ **`smartest-6.3.2` 那一页不是「6.3.2 改了什么」。** 语料有 2,677 条写的是
> `Introduced before SmarTest 6.3.2`——**是 `before`**，意思是「本文档集覆盖之前就有了」。
> 照字面读会得出「6.3.2 新增了 2,677 个功能」（§11.2 ②）。

**要看某个对象自己从哪版开始**，优先看**它那页的 `## 版本` 段**（人读原文写的），
版本页是机械摊开——两者用途不同。

---

## 语料与元信息

- raw 层：`F:\master-dev\dorm-wsl-sytest\tdc-html\agent-markdown\by-category`
  （**9,398 篇物理文档 = 8,786 个唯一 TDC 页**；504 页被重复投放在多章下，冗余 607 篇。
  判据见 `schema.md` §10「重复投放」——**这个数影响一切计数**）
- schema：[schema.md](../schema.md)
- purpose：[purpose.md](../purpose.md)
- 操作日志：[log.md](log.md)

### 建页单位：簇（**101 个**）

`ingest` 的单位不是文档，是簇。规则：**前缀树上的体量封顶割**——整棵子树装得下
100k token 就整块拿走，装不下才按下一段分类号分叉，分完把同父下相邻的簇合并回去。

- 清单：`extract/clusters.jsonl`（101 簇 / 9,393 篇，中位 81k token，无超预算）
- 规则：`extract/clusters.py` 文件头
- 对账：`extract/cluster-report.md`（七类检验）

**「有没有该在一起的被切散」是机器穷举判的，不需要人看**：切分规则的逆否命题
——「体量 ≤ 预算的前缀节点必须完整落在一个簇里」——在全库 **9,394 个前缀节点**
上逐个验过，**9,353 个读得下的一个都没被拆**；余下 41 个超预算的**必须**拆
（`02.07.04.01` 是预算的 11 倍，不拆塞不进任何一次调用）。

**簇是打包单位，不是主题单位**——合并按体量装箱，必然跨子主题（101 簇里 12 个跨章）。
判据不是「同簇文档是否同一主题」，而是：**一个对象页由「定义它的那篇文档」所在的簇
拥有**。切分是划分，所以属主唯一，跨章不会让两个簇写同一页。

> 9 个 `stage` 是**跨前缀**的簇，单独算——一个 stage 的资料散在多个前缀下。

### 全库枢纽排名（**按被多少篇不同的文档引用**）

依据 `extract/hubs-dedup.csv`（`extract/hubs_dedup.py` 生成），是**建页优先级的依据**。
**不是 `hubs.csv`** —— 那份有三个数错数的地方，见下。

**两处要扣的水分**（判据：frontmatter 的 `source_topic`，去掉 `_2` `_3` 这类后缀）：

| 水分 | 量 | 不扣会怎样 |
|---|---|---|
| **被引方重复投放** | 504 页 / 冗余 607 篇 | 同一对象 5 个副本路径，入度散在 5 条路径上 |
| **引用方重复投放** | 同上 | 同一篇页 5 份，各记一次引用 |

**两端都要归一**——第一版只归一了引用方，看到 `WSUS` 121→62 就以为完事了，
其实 62 还只是**其中一份副本**的入度。两端都归一后 `WSUS` 直接掉出前 20。

> **目录边（9,393 条）不用在这里扣**：`hubs.csv` 的 `in_src` 本来就只计 `inline` 边，
> `toc` 边（5 个章节目录页 `index.md` 的目录链接）从未计入。
> `hubs_dedup.py` 会先算未去重入度与 `hubs.csv` **逐行比对（9,398 行，0 处不符）**，
> 对不上就直接退出——两套独立实现一致，去重层才可信。

**为什么不用「被引用次数」**：次数会被「同一篇里反复提到」灌水。实测 `Error_handling`
被引 163 次，只来自 9 篇；`DPSPINS_resources` 被引 286 次，只来自 54 篇。
两个指标按次数排的前 20 与按来源篇数排的前 20 **一篇都不重合**。

```
in_src  对象
  95    DUT board design reference（文件）
  95    DC Scale XPS256 card（Head Card）
  78    EDF data organization（数据格式）
  72    EDF data types（数据格式）
  70    TESTSET（Test Method）
  67    EVENT_VALUE_DOUBLE（Test Method）
  65    ON_FIRST_INVOCATION_BEGIN（Test Method）
  63    PSFC, PSFC?（命令）
  62    Alphabetical list of flags（命令索引）
  56    SmartRDI
  55    RDI_Configure file（文件）
  54    SPMU_PIN_TASK
  51    DUT interface layout（文件）
  49    APG pattern file（文件）
  46    Structure of a TMLimits CSV file
  45    Data navigation views / Utility Card
  43    CCT Multiport Sequencer Synchronizer API
```

**`WSUS` 掉出了前 20**（原先排第 4，93）——它是被灌水最狠的一个。

分布：`in_src ≥ 20` 有 **125** 个，`≥ 10` 有 536 个，`≥ 5` 有 1,722 个。
**这 125 个就是 `object` 页的候选面**（`schema.md` §12：「只为高入度对象建页」）。

> 但**建页 backlog 的首选不是这份表，是 `extract/stage-report.md` 第八类**——
> 那 **256** 个悬空 wikilink 是**九页脊椎已经伸手去要的页**。
> 这份表只说「语料里常出现」，第八类说「流程页缺了它就断」。
