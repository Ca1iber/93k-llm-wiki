# 93K 测试开发 Wiki — Index

<!-- index-token: cl100k_base=23216 o200k_base=20015 -->

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
（脊椎 9 / 概念 33 / 约束 14 / 对象 196 / 排错 6 / 映射 9）。
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

<!-- index-count: 对象 = 196 -->

**2026-09-21 第十批（50 对象 + 5 概念 = 55 页）——把第十四类甲报出来的漏列一次补齐：**

- [[alias-set-editor]] `gui/pin` — 编 pin alias set 的编辑器：两列是 **`Alias`（别名）→ `Pin`（封装针名）**，而 `Pin` 列的值**必须已在 `Pin Setting Editors` 里定义过**，这个编辑器不能凭空造针；
  查一个针的全部别名要点**行号**右键 → `Aliases per Pin`，`Search view` 里每行按 `<alias_set_name>::<alias_name>` 读
- [[assign-value-node]] `gui/testflow` — 在 testflow 的**某个点上把一个值赋给一个变量**的节点，而**本篇正文就只有这一句**；
  ⚠️ 六个问题（变量属于哪个域、值能是什么、一个节点赋几个、怎么加进去、会报什么错……）**语料一律未写**，唯一的界面线索是图名 `New Assign Value Node Wizard window`
- [[change-device-wizard]] `gui/project` — **activate 一颗 device**、并编辑它的 **technology data** 的向导，入口有两条：`93000 menu` 或 `Change Device button`；
  ⚠️ 与 HVM 的远程命令 `ChangeDevice` **词面相同、位置不同**，别合并；原文的子主题清单里三条都落在工艺数据一侧
- [[data-retrieval-library]] `L2/results` — 访问 `data log stream`（装的是**当前正在执行的那次生产测试**的全部事件）的 API，**免掉自己给 data log file 写 parser**；`Event Formatter` 建在它之上；
  ⚠️ 语法节的 example 里有多处 C 代码错误（`if(…);` 多一个分号、`=` 当 `==`、索引基数 0 与 1 并存），照抄会撞上
- [[dc-scale-limits-editor]] `gui/pin` — 给 **DC Scale 卡**配电压 / 电流**安全限值**的编辑器（超限触发 error message，且只对 DC Scale 卡生效），五格是 `Name` / `Max Volt[V]` / `Min Volt[V]` / `Max Source[A]` / `Min Source[A]`；
  ⚠️ 「该填多少」本页一个字没有（出口是 DC Scale Device Power Supplies 的规格），而正文最后一个列名与截图列头不是同一个词
- [[device-technology-directory]] `file/project` — `/opt/hp93000/soc/dev_tech` 下 `cmos` / `ecl` 两份**样板 device 目录**（34 行子目录表）：子目录里的文件装的是**固件命令**，给出新建 setup file 时用的**默认值**；
  ⚠️ `SmarTest 7.0.3` 删掉了 `bitmap` / `bitmap_conf` / `mem_llapg` / `scrambling` 四个目录——它们确实不在表里，而原文没说这张表是哪一版的表
- [[dfge]] `L1/pin` — 定义**表达式型 pin 组**（成员按 `+` 并 / `*` 交 / `-` 差 算出来，不是列名单）；`DFGE?` 只还你**组类型 + 表达式**，要看成员得换 `DFGP?`；
  ⚠️ 例子里出现了一个参数表没写的组类型 `X`（表里只允许 `I`/`O`/`IO`/`DC`，用别的还会报错），原文没有解释
- [[dfpt]] `L1/pin` — 定义 **port** 的固件命令：**重用已有的 port 名是「追加」不是覆盖**（`appended`），新旧两批 pin 并在一起，而本篇没有给任何「减」的手段；
  ⚠️ pin 侧通配是 `@`、port 侧是 `(@@)`（两种写法并存于同篇）；`port` 名上限 16 / 64 字符随 32 位 / 64 位 SmarTest 而变，而读者怎么判断自己是哪一种原文没说
- [[dtcp]] `L1/project` — `DSCP` 的补充命令，目前只支持 `testpoints` 与 `extended_dram_factor` 两个控制参数；
  ⚠️ 写下去的值先落在**已选（selected）**、要 `*RST` 才成为**生效（active）**，而 `DTCP?` 读的是 **selected**——**它不能用来确认激活是否成功**，本篇也没给读 active 值的办法
- [[dps-aux-task]] `L2/level` — 管 **DC Scale 卡**的 **surge tracker 与 TMU**（TMU 那一行原文写 `Currently not supported by any card`）；
  ⚠️ 构造函数那条 `Note` 禁止静态对象与成员变量，而版本段 `card added` 的 `PVI8`/`AVI64`/`FVI16` 三张卡不在正文的支持名单里
- [[edl-file]] `file/results` — **`EDL file` 与 `DataCollection file` 是同一件东西**，落在 session 的 `/var/opt/hp93000/soc/tmp` 下；
  ⚠️ **SmarTest 一关就被删**，不截断还会撑爆文件系统——变通办法（建硬链接）原文自己说 `not well known`
- [[error-map]] `file/results` — SmarTest 用来记 **failing test cycles** 的那份数据，分 **detailed**（cycle 甚至 edge 级）与 **overview**（每 2000 或更多 cycle 合成一个）两种；
  ⚠️ 版本段里挂着一条失效场景：用 **Pin Scale 9G** 的 pin 产生 / 比较 **prbs** 时 `the error map does not work`
- [[event-formatter]] `gui/results` — 给 **report window** 加菜单的报告工具，靠自带对话框分别管输出的 **format** 与 **scope**，用途写的是 `interactive debugging`；
  正文只有两段话，实操全在 **14 个**子主题里（本页一篇都没读）
- [[file-string]] `L2/testmethod` — 值填**文件名**的 test method 参数类型（原文用的是复数 `file names`，能不能填多个语料未写）；
  ⚠️ 它是 **SmarTest 7.2.1** 才加的，而 `Before you begin` 只写 `SmarTest 6.3 or later`——**那句门槛管不住这个类型**
- [[flex-relay]] `L2/pin` — 装继电器设置的**数据容器**（数字 channel 与 utility line 驱动的用户继电器），`execute()` 时一次性下载、**不需要 `flush`**；
  ⚠️ `execute()` 是「全有或全无」——**一条错就一个设置都不下载**
- [[flsh]] `L1/run` — 让被缓冲在 **MCD** 里的四条 utility line 命令（`UPST` / `UPTI` / `UTST` / `UTTI`）生效的那条命令；
  ⚠️ 本篇**没有一句以 `FLSH` 为主语**的说明，而它会**强制关掉时钟**这件事写在 `FTCG` 那篇里
- [[fw-task]] `L2/testmethod` — 从 test method **直通固件层**的口子，三个重载分别对应「只下命令 / 读回字符串 / 读回二进制」；
  ⚠️ 命令串**哪怕只有一条也必须以 `\n` 或 `;` 结尾**，而 `answer` 超过 **1 MB** 不是截断、是 `a system error`
- [[hardware-response-emulator]] `gui/run` — 离线调 testflow / test suite 时，按准备好的内容把数据喂回 test method API 的后台工具，分 **Import** 与 **Store** 两个模式；
  ⚠️ 正文定义了两个模式却**没说 GUI 入口在哪**，「文件怎么准备」「哪些 API 支持」全在四个子主题里
- [[jsud]] `L1/timing` — 把已定义的 **jitter set** 删掉（`ALL` 全删），同族里唯一**没有查询形态**的那条命令；
  ⚠️ 删完之后会怎样、空集上 `ALL` 会不会报错都是**语料未写**，`## Application` 全文只有 `Jitter test.` 两个词
- [[jswf]] `L1/timing` — 按指定的 **clock resolution** 把 jitter 波形换算成 **offset sequence** 的查询命令，用户定义的波形不合规则时它会 `will correct the list`；
  ⚠️ `clock_resolution` **单位是 ps 不是 ns**（上游 `CLKR?` 返回的是 ns），而规则①按字面读**与两个例子都对不上**
- [[level-equation-file]] `file/level` — `USE_PROTOCOL` 语句，把已定义的 **protocol level segment**（device 的 protocol 目录里那个 `.prot_lev` XML）并进 equation system；
  ⚠️ 只能写在 `SPECS` / `EQUATIONS` 段、`SPECSET` 段**不支持**，而且原文说这句**必须手写**
- [[multiport-burst-editor]] `gui/pattern` — 管 **multiport burst** 与组成它的 **port burst** 的 pattern 工具，一个 Overview 页加若干 tab 页；
  ⚠️ **要看展开模式得先执行 testflow**，而**「怎么创建 / 编辑 burst」本篇一句都没有**（全在四篇子文档里）
- [[new-device-wizard]] `gui/project` — 建出一个 **device 目录**并在 **workspace** 里挂一条链接的向导，七条控件里夹着两条否定指令（`V3 delay adjust` 跳过、`Fast bidirectional capability` 不再支持）；
  ⚠️ 版本段那条 `Result Area Size` 在**正文里一次都没出现**，成对的两个向导版本记录并不对称
- [[option-list]] `L2/testmethod` — `OptionList` 是 test method 参数类型之一，而**原文对它的全部说明只有一句话**，取值形态含糊（多选还是单选）本页不替它定死；
  真正要紧的是把它与 `Options` **字段**分开——那个字段对所有类型都在，候选值之间用冒号 `:` 分隔。
- [[pattern-object]] `L2/pattern` — `PATTERN` 是「一个 subpattern 的元素容器」，**没有公有构造函数**，只能由 `PATTERN_CONTROLLER` 的 `label(...)` 取出来；
  `vecEvents()` 拿到的引用下一次 `vecEvents()` 或用 `label()` 改 pattern 就会**失效**，查不到 clamp 时出参是哨兵值 `999999` / `-999999`。
- [[pattern-tool]] `gui/pattern` — Pattern Tools 是 **Pattern Explorer / Pattern Editor / Multiport Burst Editor** 三个编辑器的合称，**只有 Explorer 能启动另两个、也只有它有删的权力**；
  两条硬限制：超过 **50 万条指令**的 pattern 在 Pattern Editor 打不开，**F330 scan pattern 三个 Eclipse 工具都不支持**。
- [[pin-configuration-master-file]] `file/pin` — 这份文件**自己不含任何 pin 定义**，只是一份「用哪几份 pin 配置文件、谁当 package、谁当 alias」的清单，由 `Setup Management Tool` 组装；
  组装前校验四条（site 数 / channel 归属 / context 不重名 / 方向相容），**任一条不过就中止并生成一条错误信息**。
- [[pin-string]] `L2/testmethod` — `PinString` 是参数类型，原文全部说明只有 `is used for pins, pin lists or pin groups` 一句；
  **取值形态、分隔符、写错会怎样、代码里怎么取一律语料未写**，而且它从 SmarTest 6.5.0 起才有——`Before you begin` 那句 6.3 门槛管不住这个类型。
- [[pin-utility]] `L2/pin` — `PIN_UTILITY` 不是测量 API，是把**含 pin group 名的 pin list 摊平成具体针名**的翻译层——取单针结果时要靠它；
  只能用它预置的对象 `PinUtility`（**无公有构造函数**），而且四个例子一律只给 4 个实参，签名却是 5 个参数。
- [[port-editor]] `gui/pin` — Port Editor 是「给一个 port 挑成员」的两栏搬移式编辑器，而**三条 port 定义规则**才是要紧的——不许与 pin / pin group 重名、**不支持表达式型定义**、port **自动就是 pin group**；
  原文那句里的记号是一个坏字（`鈭?`），图上显示成勾选字形，图上四个按钮与 `Type` 列原文一个字没写。
- [[pqfc]] `L1/pin` — `PQFC` 设的是**查询焦点**，被设中的 site 是**唯一**能取 setup 数据、显示结果的 site，而**上电后焦点不一定是 site 1**；
  原文自带一条 `CAUTION` 建议改用 `tpi`，且唯一的出错条件是**该 site 还有 pin 没经 `PALS` 分配通道**。
- [[project-explorer-view]] `gui/project` — Setup perspective 里的这个 view 既是 device 的导入/激活入口，又能编译 test method 共享库；
  要留意**同一节里前两句讲 device、紧跟的六条清单讲 test method 代码**，原文没有过渡句，而工具栏三个图标的 alt 文本还写着改名前的 `Navigator view`。
- [[run-dialog]] `gui/run` — 跑 testflow 的唯一配置面板（`Run > Run configurations`），三种模式**右栏控件不是同一组**，且**要看结果必须先把 `debug_mode` 设成 `off` 以外的值**；
  最要紧的差别是 `ABORT TESTFLOW` **不停循环**而 `ABORT` / `RESET` 停，`Break` 按钮也中止不了循环。
- [[setup-perspective]] `gui/project` — SmarTest 的**默认 perspective**，首次启动时活动的就是它，它自身不讲机制、只装了九个 view；
  ⚠️ 本页「语法 / 参数」节那两段代码（hp83 加密导入、collision handling）**不是本篇的内容**，是脚本顺子主题抄进来的。
- [[smartcalc]] `L2/testmethod` — SmartCalc（SMC）把耗时计算与数据上传**藏进后台线程**来压测试时间，调用形状是三段：`SMC_` 包装的执行 → `FOR_EACH_SITE` 里 `SMC_ARM` → `ON_FIRST_INVOCATION_END()` 之后 `SMC_SYNCHRONIZE()`；
  与 `smartcalc-framework` 的分界是「怎么调」对「为什么」（两页的「语法 / 参数」节逐字相同）。
- [[software-bin-summary-tab]] `gui/results` — data store 里所有 **software bin** 的合并汇总，表最上面一行（`cyan` 底）其实是**过滤器**，点列标题三下是升序 → 降序 → 取消排序；
  两个坑：`Site` / `Site%` 两列**由 hardware bin summary 有没有按 site 分组决定**，而 `Save and Clear` **存完就把流清掉**，原文没给「只存不清」。
- [[spec-search]] `L2/level` — `SPEC_SEARCH` 不是读或改一个 spec 值，而是**把 spec 从 start 挪到 stop、测到 pass/fail 跳变点为止**，`TM::TIM` 与 `TM::LEV` 两选一；
  用法陷阱：`resolution` **三种搜索方法都必须给**，`stepWidth` 与 `numberOfSteps` **后写的覆盖先写的**，用 `PRIMARY_STATUS` 改过 primaries 时要先 `FLUSH`。
- [[sprm]] `L1/level` — 选「这一轮用哪几组 primary set」，**只登记、不激活**（激活是 `aprm`）；
  ⚠️ 原文一条 `Note`：**报错也照样把传进去的值存下**，而例子里回的 `101003` 与 `dps_set_id` 公式末尾那个 `+ 1` 对不上
- [[spst]] `L1/level` — specset 的**状态位**查询；语义是反的：**位被清零才执行检查、被置位就跳过检查**；
  ⚠️ 全篇只有 `SPST?`（读），**怎么把某个位置起来原文没给**，位表里还整个缺了位 11
- [[stdf]] `file/results` — 怎么让 STDF 自动生成：改 `global.conf` 的 `formatter.stdf.generateStdf=true`，**必须重启 SmarTest 才生效**；
  ⚠️ 版本段写的是 `SmarTest 7.4.5: Removed stdf_generation flag`，**与正文那个键名对不上**，而这篇不讲 STDF 格式本身
- [[test-method-class]] `gui/testmethod` — GUI 向导产出这个类，**只填类名 + 参数两项**，示例 `PspecSearch` 加了 **8 个参数**（`PinString` / `SpecVariable` 等）；
  函数体不在向导里（`## What to do next` 只有一句 `Add the source code`），而那张参数表**不在本页的「语法 / 参数」节里**
- [[testflow-master-file]] `file/testflow` — testflow 拆成多文件后把它们拉回一起的那份**索引**，存在理由就是多人并行；
  **单个 test suite 或 bin 不能单独成文件**，所以顶层对象必须是 group，第二行 `testerfile:` 必须存在
- [[testflow-variable]] `file/testflow` — `flowvars.csv`（由 `generate_template` 生成）：把各 STP 的变量与 flag 映射到 MTP，系统 flag **无论设没设都永远在表里**；
  **`Value` 列的空格子必须填满，否则 STPM 建 MTP 时报错**——而一行 CSV 长什么样（表头、分隔符）原文一行示例都没有
- [[timing-specification]] `file/timing` — equation based timing 的**产物**：wavetable（波形）+ equation set（周期与边沿延迟）合成，还含 spec set 与检查项；
  落盘在 `<device_folder>/timing`、**文件名任意**，而**要下载给固件（`EQFS` / `EQSP`）就必须按 timing setup file 的写法写**
- [[tpt-import-from-device]] `L3/project` — STPM 控制文件里的一条命令：从现成 device directory 生成 test program template（**与 `tpt-generate-device-dir` 反向**）；
  **`tpt_dir` 非空就必须 `allow_overwrite = 1`**，`copy_static_content` 只收 device 目录**顶层**的名字，列到那六个标准目录会告警且不拷内容
- [[universal-test-method-library]] `file/testmethod` — **章首页**：UTM 库从零建的四步（工程 → 类 → testflow → 调试）+ 两条前置（SmarTest 6.3 以上、device primary setups 可用）；
  ⚠️ 四步的内容全在下钻篇里，**「产物叫什么、落在哪个目录」本篇一个字没有**（`lib*.so` / `Debug/` 在本篇均 0 命中）
- [[uptd]] `L1/level` — 问「硬件里的数据与当前 device 文件还对得上吗」，**27 个 `status` 选项**各盯一类数据，power-on 或 `*RST` / `dscp` 会把所有 flag 归 0；
  四个 Command Set（`DFRM` / `PRBH` / `PRCS` / `USRP`）的 flag 语义**与其余 23 格相反**——盯的是进程有没有在跑
- [[utility-line-view]] `gui/run` — Hardware Perspective 里查 / 设 utility line 读写的视图，**范围是 all utility lines（含没在 pin configuration 里定义的那些）**；
  表头显示 channel 号 `[01–32]` 且**从右往左**，line 自己的编号则差 1（`[00–31]`）
- [[utility-purpose-editor]] `gui/pin` — 给一个 utility purpose **挑 utility line**：名字 ≤16 个字母数字字符，`Settling Time` 多 site 时**所有 site 必须同值**；
  ⚠️ 图证与正文打架：图上 `16501` 那一行四个 site 的值是 `0/1/0/1`，而正文写 `you must set the same value for all sites`
- [[wavetable]] `n/a/timing` — **定义页**：一张 wavetable = 一个或多个 `PINS` 小节，每节 = 一串 pin + 纯波形（`must be specified`）；
  ⚠️ 它的语法是一张**铁路图**而不是文字，图上五个记号里**正文只解释了 `pin_list` 一个**，其余四个只存在于图里

**2026-09-20 第九批（21 对象 + 6 概念 = 27 页）。⚠️ 这一批是「工作单判据修好之后」冒出来的真欠账**
（判据从「被 stage 页提到」改成「**有页**」，见 `log.md`）——**它们全是 §12 判据（入度 ≥20）下该有页的**：

- [[testset]] `L2/testmethod` — testmethod 的主类（入度 70）
- [[event-value-double]] / [[event-value-int]] `L2/testmethod` — 事件值类型（67 / 34）
- [[spmu-pin-task]] / [[spmu-task]] / [[dps-task]] `L2/testmethod` — DPS/SPMU 编程的任务句柄（54/36/35）
- [[get-functional-result]] `L2/testmethod` — 取功能测试结果（38）
- [[test]] `L2/testmethod` — `TEST` 那个类（slug 短，别当泛泛而谈）
- [[limit]] / [[task-list]] `L2/testmethod` — limit 与任务清单（各 30）
- [[pattern-controller]] `L2/pattern` — subpattern 元素的容器（30）
- [[smc-test]] / [[smc-synchronize]] `L2/testmethod` — SmartCalc 家族（27 / 24）
- [[digital-offset-search-pins]] `L2/pattern` — 数字 offset 搜索 pin（26）
- [[digital-capture-test]] `L2/testmethod` — 数字捕获测试（20）
- [[for-each-site-begin]] `L2/testmethod` — 「每个 site」块的**开始**标记（**建页前**在
  `dangling.csv` 里**被引 18 处**——**这个数会随建页消失**，§9.1）；
  与 `for-each-site-end` **必须成对**，围出的区域叫 each site loop block
- [[for-each-site-end]] `L2/testmethod` — 「每个 site」块的**结束**标记（21）；
  ⚠️ **循环体语义与示例全被原文推给了 `FOR_EACH_SITE_BEGIN`，本页单读不完整**
- [[stpm-merge-rules-file]] `file/project` — STPM 合并规则文件（33）
- [[pin-configuration-tool]] `gui/pin` — Pin 配置工具族的总入口（27）；
  ⚠️ **它的 10 张图分两代**，旧三张是 7.1.3 之前的界面
- [[signal-analyzer]] `gui/results` — Signal Analyzer（24）
- [[dfgp]] `L1/pin` — `DeFine GrouP`：定义**固定** pin 组（23）；表达式型是 `dfge`，另一条
- [[psas]] `L1/results` — `PSAS?` 电源累积状态（**只有查询形态**）（21）
- [[dut-interface-layout]] `n/a/project` — DUT 接口版图（51）；
  ⚠️ **备用号 265–272 与 DPS 1–8 的配对不能顺推**（原文脚注自己点破了）
- [[utility-lines]] `n/a/pin` — utility line 总入口（38）
- [[setting-up-dc-scale-pins-with-smartrdi]] `n/a/testmethod` — 用 SmartRDI 设 DC Scale pin（22）；
  **首次 code-based 测量必须与首次 `iForce()`/`vForce()` 分成两条命令行**
- [[smartrdi-tmu-test-setup]] `n/a/testmethod` — SmartRDI 的 TMU 测试设置（21）；
  **`execute()` 只是「开始」，测量落在块内下一个 event**
- [[test-number-generator-and-tmlimits]] `n/a/results` — 测试编号与 TMLimits（23）
- [[setting-up-a-shmoo-test-with-the-shmoo-tool]] `n/a/results` — 怎么设一次 shmoo 测试（27）

**2026-09-20 第八批（12 页，`dangling.csv` 被引 ≥7 那一档的余下部分）：**

- [[disconnect]] `L2/testmethod` — 断开；**与 [[connect]] 共用同一篇文档**（那篇两个都讲）
- [[spec-value]] `L2/level` — UTM 的 spec 值；**`inputValueUnit()` 单位对不上时静默沿用上一个**，
  而同族的 `getValueAsTargetUnit()` **抛异常**——同一件事两个函数行为相反
- [[spec-variable]] `L2/level` — spec 变量的坐标式名字（`"LEV.1.fooSpec[mV]"`）；五个字段是**公有成员、不走 getter**
- [[timing-spec]] `L2/timing` — `TIMING_SPEC(eqnset, specset)`：改 / 读 timing spec 值
- [[wavetable-file]] `file/timing` — 存 wavetable 的那份文件
- [[dfps]] `L1/pin` — 把 DPS channel / DC Scale（DPS 模式）绑到器件 pin 并给极性；⚠️ **两份投放**
- [[on-first-invocation-begin]] / [[on-first-invocation-end]] `L2/testmethod` — 一对作用域：
  声明「**只在第一次调用时执行**」的范围起止
- [[testflow-properties-view]] `gui/testflow` — 显示并改 testflow 属性
- [[aprm]] `L1/level` — 把 primary set **真正激活**；⚠️ **四个投放**（三份正文逐字节相同）
- [[device-license-file]] `file/project` — **它会覆盖 model file 的 license 条目**：
  交一份什么都不写的，**等于把 model file 那部分关掉**，不是「什么都没做」
- [[eqfs]] `L1/timing` — 把 equation set / spec set **LOAD** 进固件（别与 [[eqsp]] 混，那是另一条）
- [[eqsp]] `L1/timing` — 同族的**另一条**：`EQFS` 走**文件**、`EQSP` 走**规格**（`spec_type` 取 `LEV`/`TIM`）

**2026-09-20 第七批（12 页，`dangling.csv` 被引 8–11 那一档）。⚠️ 这一批的钩子句取自
**stage 表格里已经写好的描述**，不是「本页最值钱的一条」——**因为写它们的 agent 在自查前断线，
没留下回报，我没有独立读过每一页**（另有 3 个 reviewer 在复核，见 `log.md`）：**

- [[bin]] `n/a/testflow` — 分选落点；`stop bin` / `otherwise bin` / `float bin` 等
- [[connect]] `L2/testmethod` — 连接资源 / 给 DUT 上电；与 `disconnect` 是一对
- [[timing-setup-tool]] `gui/timing` — timing 阶段主工具：编 wavetable 与 equation set
- [[dps-pins-editor]] `gui/pin` — DPS pin 表格（`Name`/`Pol`/`C[uF]`…）；
  ⚠️ **它那页查出一件事：`mapping-pin` 用的旧截图上列名是 7.1.3 之前的旧名**
- [[flow-data-editor]] `gui/testflow` — 表格视图，八个页签（Test Suite…）
- [[level-spec]] `L2/level` — `LEVEL_SPEC(eqnset, specset)`：改 / 读 level spec 值
- [[svlr]] `L1/level` — **运行时**改 spec 变量值并重算（`SVLR` / `SVLR?`）
- [[test-suites-page]] `gui/testflow` — `Result > Pass/Fail` 单元格着色那一页
- [[testflow-analyzer-tool]] `L3/project` — 统计 device 实际用掉的 set 数，用来优化 `.technology`。
  ⚠️ **文档第一句 `TAT is a command line tool.`——所以它是 L3，不是 gui**（2026-09-20 更正，见 `log.md`）
- [[timing-equation-set]] `file/timing` — 存 edge position / period 的那份文件
- [[timing-master-file]] `file/timing` — 一个 device 的 timing 总入口
- [[utility-pins-editor]] `gui/pin` — utility pin 的名字、方向、settling time、channel

**2026-09-20 第六批（11 页，`dangling.csv` 头 19 个的后 11 个——**这批把最密的死链清了**）：**

- [[spec-tool]] `gui/level` — spec 变量有 **scope** 语义（`local` 该 port 一份 / `global` 几个 port 共用）；
  shmoo 里要按 **`SVLR` 的写法 `<spec_variable>@<port_name>`** 做局部改写
- [[level-setup-tool]] `gui/level` — **`MODECONTEXT "<名字>"` 是文件里绑 context 的关键字**——
  **语法节整个没给，是图挖出来的**（④ 图证）
- [[level-master-file]] `file/level` — **pin alias set 只活在「组装后」的整体文件里**；
  一旦拆开，子文件里的 alias set 被移除、改用 **package pin name**
- [[testflow-tool]] `gui/testflow` — 硬件响应文件那个四段式键的字段名是
  `Testsuite; MAPI; call#; site#`（**图证**，正文只说了「四段是什么」）
- [[flow-sequence-editor]] `gui/testflow` — **Palette 的 15 项**（`Select`/`Run Test`/`Good Bin`/`If/Then`…）**只在图里**
- [[test-suite]] `n/a/testflow` — 四类各一句话的**分诊台**；**7.6.1 新增那类的属性名只在图里**
- [[ci-cpi]] `L3/testflow` — **15 个签名**（Production 10 + User 5）；
  ⚠️ **site 编号两套约定同页并存**（一段从 1 数、一段从 0 数再打印 `site+1`）
- [[pattern-editor]] `gui/pattern` — **expanded 只认「当前 primary pattern」**；
  `SC`/`DVC`/`PW` 三个格式码的展开只有图上齐
- [[timing-file]] `file/timing` — specset ID = `(equation_set_nr × 100) + specification_set_nr`；
  ⚠️ **同一篇 TDC 文档投了三次**（`10597` / `_2` / `_3`）
- [[flush]] `L2/run` — **FLUSH 推两段、目的地不同**：`ROUTING_STATUS` 到硬件，
  而 `PRIMARY_STATUS`/`TIMING_SPEC`/`LEVEL_SPEC`/`SPECIFICATION` **只到 MCD**（`does not reflect them to the hardware`）
- [[site-control-window]] `gui/run` — **`focus` 会自动切、也能手设**（图证）；**并行组数 = `Cycle ÷ Size`**（推断）

**2026-09-20 第五批（8 页，照 `dangling.csv` 最前面那几个建的——**这些是「脊椎已经伸手要」的**）：**

- [[pin-configuration-file]] `file/pin` — Pin Configuration 工具写出的那份；**被引 26 次，全库第一**
- [[level-file]] `file/level` — level 主产物；**两条互斥路线（equation based / fixed）在目录上成对**
- [[test-program-explorer]] `gui/project` — 工程树；**树上三种状态（文件名/`*`/`[external]`）是读它的钥匙**
- [[pattern-explorer]] `gui/pattern` — 浏览/编辑 pattern 与 burst；**`*.pmfl` 是一道功能门槛**
- [[vector-setup-file]] `file/pattern` — 装 label 与向量数据；**大文件 or 一 pattern 一文件，二选一**
- [[pattern-master-file]] `file/pattern` — 列 pattern 及其路径；**必须手工写、必须在 `<device>/vectors`**
- [[device-directory]] `file/project` — device 目录结构；**那份 29 个目录的清单只是「某一次的」**
- [[flags-page]] `gui/run` — Flags tab；**语料里唯一实质来源是它自带的那张图**

- [[sharing-configuration-file]] `file/pin` — load board 的分流结构定义；`<device>/configuration/` 下**必须有**
- [[device-architecture-file]] `file/pattern` — MTL 器件架构文件；语法在**子主题**里（页面已标明来源）
- [[data-navigation-views]] `gui/results` — 结果浏览界面
- [[xps256-pmu-operating-mode]] `L2/level` — XPS256 PMU 的四种工作模式 + 三种编程风格
  （**SmarTest 7.10.1 引入**，是 wiki 里唯一一篇「最近才有」的页）
- [[cct-multiport-sequencer-synchronizer-api]] `L2/pattern` — CCT 多端口定序同步 API
- [[xps256-programming-dps-operating-mode]] `L2/level` — XPS256 DPS 的编程接口；
  **必须用方程**才能用到全部功能（原文硬要求），八个 Hardware view 按钮
- [[xps256-status-flags]] `L2/level` — XPS256 的状态/保护标志：三类标志、每标志四个字段、
  **testflow 与 hardware view 两套不同的 reconnect 步骤**（本 wiki 最长的对象页）
- [[tpi-program-routines]] `L3/run` — Test Program Interface：**10 组 29 个 C 函数**（`tpi_c.h`）
  + `DataManager` 的 `dm_*` 结构化数据通道；**被 12 页引，是悬空清单第一名**
- [[test-suite-control-api]] `L3/run` — Test suite control API：`TestsuiteProxy` **33 个成员**
  + **14 个会话级函数**，**在 testflow 工具之外**控制 test suite（**被 8 页引**）

**2026-09-18 第二批（**本表逐条列出 12 页**）：**

> ⚠️ **这个标题原写「13 页」，与它自己列的 12 条对不上。已改。**
> **批次标题的数字不是总数**——`log.md` 里的「第二批」是另一套分组（那一批记的是 4 页）。
> **凡是「这一节有几页」的问题，一律以本节末那个核实过的数为准，不以批次标题为准。**

- [[tp360]] `gui/project` — Test Program 360 桌面工具：**怎么打开**（两个环境变量、两条路）
  + App Center 上的两个坑；**`H1` 用工具名不用文档名**，理由写在页里
- [[analysis-views]] `gui/results` — 结果侧 12 个分析视图，**按「要先选中什么」归类**；
  页里两处「最容易读错」是重点
- [[dps128-dps64-cards]] `n/a/level` — DC Scale DPS128/DPS64 卡：**一个对象 5 篇定义文档合成一页**
  （`rel` 列写成 `A;B;C;D;E` 的第一例，`sources:` 因此能认领多篇）
- [[utility-line-assignments]] `n/a/pin` — utility line 与 **utility pogo block**：
  **16 线块 / 32 线块、DUT 接口总线上限 64/128/256**，以及内部与外部 utility 电源各走哪个针
- [[dps-aux-pin-task]] `L2/level` — `DPS_AUX_PIN_TASK`：**`DPS_AUX_TASK` 的从属数据容器**，
  **不能用 `new` 造**，只能经 `DPS_AUX_TASK.pin()` 拿；七个成员函数
- [[event-waveform-vfvm]] `L2/testmethod` — `EVENT_WAVEFORM_VFVM`：同一时刻产生波形并测量
  （**页里记了原文 `#### Subtopics` 19 条里有一条挂着别的类**）
- [[hidden-upload]] `L2/testmethod` — 把包上传**藏在下一个测试的 sequencer 执行后面**
- [[mtpt]] `file/project` — MTPT（STPM MCM mapping tables）：**14 张 CSV 表怎么分组、哪两张不许改**
- [[preprocessing-and-postprocessing-scripts]] `file/project` — `pre_proc` / `post_proc`：
  **`&xxx` 在执行时被改写成 `--xxx`**，26 个系统参数
- [[mtp-shared-test-commands]] `L2/testmethod` — Driver sharing 支撑 API（`SHARING_CONFIGURATION` 一族）
- [[mtp-maintenance-operations]] `n/a/pattern` — 存储器件刷新：周期 / 类型 / 可打断位置 / 排期方式
- [[timestamp-attr-type]] `file/results` — EDF 里的时间戳属性类型；**全 wiki 最短的对象页之一**

**2026-09-18 第三批（1 页）：**

- [[pogocabling-section]] `file/pin` — model file 里的 `POGOCABLING` 段：
  **pogo 块密度 / 卡型 / 编号怎么写**，写完对不上就**启动即退出**；
  **一个路径下有五段**，`## 语法 / 参数` 由脚本管辖（5,426 字符，含摊平的卡笼表）；
  ⚠️ **`SmarTest 7.10.0` 起不支持 Single density 卡等一批卡型**——本 wiki 面向 7.10.3，**这条要看**

**本节的两个数不必手写**（脊椎 9 页在外）。**建页理由有四种，不是一种**：

> ⚠️ **2026-09-20 删掉了一处历史数**：这里原写「对象 **98** 页 + 概念 **22** 页（上一节）= **120** 页」——
> 那是**某一批建完时**的数，后面的批次一建就过期了（现值见本节开头的 `<!-- index-count -->` 标记）。
> **它就是下面那句话说的那种东西**：能自动查的数就别手写。
> （同时修了一处同形状的：第十四类丙 登记的正则写「（**下一节**）」，而原文是「（**上一节**）」——
> **一个字的差，那条声明就一直匹配不上、一直印「这句没找到」**。同 §13.1 第十六次。）

> **这个数不必手写**：**本节列出的 `[[ ]]` 与目录里的文件互为子集，这一条由第十四类甲自动查**，
> 不靠人想起来（此前「每次 ingest 后更新」这条规则**没有任何检查看着**，
> 于是两页建好了却没人填进目录，三个数同时少 1：[[pogocabling-section]]、[[hv-protection]]）。
> **当时的 79/22 是 2026-09-18 的读数；2026-09-20 已到 143/28。**
> **本批 71 页是脚本登记进去的**（`extract/index_rebuild.py`）：
> `[[ ]]` 的集合是**机械事实**、由脚本落盘；每行后面那句钩子是人的判断、写在脚本顶部的表里。

1. **有 stage 归属 + 入度高** —— xps256 三页、device-architecture-file 等
2. **定义文档自己声明的 `Subtopics`** —— [[pogo-block-compatibility]]、[[inter-layer-via-design]]
   （入边各 1 条，**按入度根本轮不到它们**）
3. **wiki 内部引用** —— [[tpi-program-routines]]、[[test-suite-control-api]]
   （语料内指向根文档的行内边只有 1 条，而 wiki 里被引 12 / 8 处）
   **这一种是「脊椎已经伸手要它」，不是任何语料内指标。**
4. **入度（第六类工作单）** —— 其余多数的出处是 `extract/unowned.csv`
   （`in_src >= 20` 且不属于任何 stage）。**这一种现在清空了。**
5. **悬空链接（第八类工作单）** —— **2026-09-18 第四批 71 页的主判据**：
   已经建成的页**伸手去要**、但还不存在的页（`extract/dangling.csv`）。
   **这一种与前四种都不一样**：它不是「语料里常出现」，是「**流程页缺了它就断**」。
   71 页 = `dangling.csv` 前段 ∪ `in_src ≥ 20` 的散文对象，**两者交集为 0**。

> **别把第 3 种和第 4 种混起来**：`dangling.csv`（谁链了它）和 `unowned.csv`（语料里多常出现）
> **是两张不同的工作单**，交集很小——**建 16 页只让第八类消掉 1 个**，就是证据（见上面缺口二）。

**2026-09-18 第四批（57 页，照 `dangling.csv` + `in_src ≥ 20` 两批并起来建的）：**

- [[alphabetical-list-of-flags]] `L3/testmethod` — 结果旗标一览；**语料里被引 62 篇**，是 flag 类问题的入口
- [[apg-pattern-file]] `file/pattern` — APG pattern file：**算法图形发生器的图形描述**
- [[apg-program-file]] `file/pattern` — APG program file：APG 的程序（图形之外的循环与控制）
- [[conf]] `L1/project` — `CONF`（CONFiguration）：pin configuration；`PALS` 必须先于它
- [[ctxt]] `L1/level` — `CTXT`（ConTeXT）：定义 mode context；**level / timing 两条「mode context 必须一致」的约束都要它**
- [[data-logging-profiles]] `file/results` — Data Logging Profiles：**记什么、记多细**由它定
- [[dc-result-accessor]] `L3/testmethod` — `DC_RESULT_ACCESSOR`：DC 测量结果的取数接口
- [[dc-scale-uhc4t-card]] `n/a/pin` — DC Scale UHC4T 卡；**DUT 板侧那一章**（`02.03.08.01.06`，原候选 `dc-scale-uhc4-uhc4t-card`）已并入本页
- [[dc-scale-xps256-card]] `n/a/pin` — DC Scale XPS256 卡：**语料里被引 95 篇，全库并列第一**
- [[device-access-file]] `file/pattern` — MTL 的 Device access file：**怎么访问器件**
- [[dfpn]] `L1/pin` — `DFPN`（DeFine Pin Name）：给 pin 起名；**pin 页与三条约束页共同的前置命令**
- [[digital-pins-editor]] `gui/pin` — Digital Pins editor：**图形界面上配 pin**，与 L1 命令是两条路
- [[pin-group-editor]] `gui/pin` — Pin group editor（**建页前**被引 12 处，同上）：分 **Fixed groups** 与
  **Expression-based groups** 两类，`DFGP` / `DFGE` 是它们在 L1 那一侧的对应命令
- [[dps-power-flags-get-functions]] `L3/run` — `DPS` 电源旗标的 `get...()` 一族函数
- [[dpspins-resources]] `L2/pin` — `DPSPINS` 的 resource 关键字：电压斜坡等参数的写法
- [[dscp]] `L1/project` — `DSCP`（Define System Control Parameter）：系统控制参数
- [[error-map-tool]] `gui/results` — Error Map Tool：把失败的 bit 映射回物理位置
- [[event-base]] `L3/testmethod` — `EVENT_BASE`：**所有 `EVENT_*` 测试方法的基类**，讲清它才讲得清那一族
- [[event-waveform-vfim]] `L3/testmethod` — `EVENT_WAVEFORM_VFIM`：同一时刻产生波形并测量；**与 [[event-waveform-vfvm]] 是两个类**（`.63.38` / `.63.39`）
- [[execution-context]] `L2/run` — execution context：**不能随用随起名字**，必须先在固件级定义
- [[global-section]] `file/project` — model file 里的 `GLOBAL` 段
- [[integrated-result-tool]] `gui/results` — Integrated Result Tool：**所有分析视图跑在它里面**
- [[jscf]] `L1/timing` — `JSCF`（Jitter Set ConFiguration）：配置 jitter 集；**必须先定义再引用**
- [[jsdf]] `L1/timing` — `JSDF`（Jitter Set DeFinition）：定义 jitter 集；与 `JSCF`/`JSPR` 同族
- [[jspr]] `L1/timing` — `JSPR`（Jitter Set PRimary set）：指定主 jitter 集
- [[model-file]] `file/project` — **model file**：机台硬件配置的根文件；**启动读不到就起不来**（见排错两页）
- [[mtp-memory-test]] `L2/pattern` — `MTP_MEMORY_TEST`：存储器件测试
- [[pals]] `L1/pin` — `PALS`（Pin ALlocation for multiple Sites）：多 site 的 pin 分配；**必须在任何其他 setup 命令之前**
- [[pin-mapping-file]] `file/pattern` — MTL 的 Pin mapping file：**测试 pin ↔ 器件 pin 的映射**
- [[primary-status]] `L3/level` — `PRIMARY_STATUS`：primary 侧的测量入口，level / timing / pattern 三段共用
- [[protocol-editor]] `gui/pattern` — Protocol editor：编辑协议（时序与电平的协议化描述）
- [[psfc]] `L1/pin` — `PSFC`（Parallel Setup FoCus）：并行 setup 的焦点；**执行前必须先设站点焦点**
- [[pste]] `L1/run` — `PSTE`（Parallel SiTe Enable）：启用并行 site
- [[raw-data-views]] `gui/results` — Raw data views：未经汇总的原始结果
- [[rdi-configure-file]] `file/testmethod` — `RDI_Configure` 文件：SmartRDI 的配置文件
- [[report-window]] `gui/results` — 报错窗口；**两页排错页的入口**，但排错页讲的是「看到什么报错」，本页讲窗口本身
- [[sequencer]] `L1/pattern` — 定序程序本身：`SQST` 读的是它的状态，pattern 与 pin 的约束都围着它
- [[sequencer-status]] `L3/pattern` — `SEQUENCER_STATUS`：从测试方法侧读 sequencer 状态
- [[setup-management-tool]] `gui/project` — Setup Management Tool：工程内 setup 的管理
- [[shmoo-tool]] `gui/results` — Shmoo Tool：**怎么设一个 shmoo 测试**并在本页；生成侧在这里，画图侧在 [[analysis-views]]
- [[smartcalc-framework]] `L3/testmethod` — SmartCalc 框架：**用公式而不是常数描述测试条件**
- [[smartrdi]] `L3/testmethod` — SmartRDI：**DC Scale 类卡件的编程接口**；「怎么用」（TMU 测试、DC Scale pin 设置）并在本页
- [[spec-set]] `L2/level` — Spec sets：**成组地切换 spec 值**（多 site / 多条件）
- [[special-test-suites]] `file/testflow` — Special test suites：testflow 里的特殊测试组
- [[spmu-pin-task-mode]] `L3/level` — `SPMU_PIN_TASK.mode()`：SPMU 的 pin 工作模式
- [[sqst]] `L1/pattern` — `SQST`（SeQuencer STate）：读/设 sequencer 状态；level 与 pin 的约束页都要它
- [[stpm]] `gui/project` — SmarTest Program Manager：程序管理工具
- [[stpm-control-file]] `file/project` — STPM control file：程序管理器的控制文件
- [[structure-of-a-tmlimits-csv-file]] `file/testmethod` — Test number 与 limits 的 CSV 表结构；生成侧（Test Number Generator）并在本页
- [[technology-file-for-a-device]] `file/project` — Technology file：**器件的工艺角信息**；原候选 `technology-file` 是同一对象的另一种叫法，已并入本页
- [[test-summary-tab]] `gui/results` — Test summary tab：**十一种分析视图都在这里选**（`Bin wafer map` 除外）
- [[testflow-file]] `file/testflow` — testflow 文件：测流的存储形态
- [[timing-diagram-tool]] `gui/pattern` — Timing Diagram Tool：**pattern / results / run / timing 四段共用**；「怎么用」并在本页
- [[tmlimits]] `L3/testmethod` — `TMLimits`：测试方法侧写 limits 的接口；results 与 testmethod 两段都要它
- [[tpt-generate-device-dir]] `L2/project` — `tpt_generate_device_dir`：生成器件目录
- [[utility-card]] `n/a/pin` — Utility Card：**给 DUT 供非测试用电**的那张卡
- [[utility-pogo-block-utility-card-v93000-exa-scale-systems]] `n/a/project` — Utility Card 的 pogo block（V93000 EXA Scale 系统）
- [[utility-power-supplies]] `n/a/project` — Utility power supplies：外部 utility 电源

---

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
