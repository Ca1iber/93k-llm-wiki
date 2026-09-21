# -*- coding: utf-8 -*-
"""重建 `wiki/index.md` 的两节 + 把「已知缺口」的账本搬进 `log.md`。

**为什么要脚本、不手改。** 这次要往索引里加 **71 行**、同时**搬走 5,664 token**
的账本。手改 71 行的 `[[ ]]` 集合，第十四类甲（索引每节列出的页 ↔ 目录里的文件
互为子集）会逐条对——少一个链接、多一个反引号，它就红。
`[[ ]]` 的集合是**机械事实**，所以由脚本落盘；**每行后面那句钩子是人的判断**，
写在本文件顶部的表里。

---

## 一、为什么非搬不可（不是「拆了更整齐」）

§7 的硬约束是 `index.md < 15,000 token`，`check_index_budget.py` 看着它。
实测 2026-09-18：全页 13,261，而 **`## 已知缺口（五条）` 一节独占 5,664 token（43%）**。

加 71 行（约 +2,500）会到 **~15,760，超预算**。§7 说超了按类型拆子索引——
**但先看那 43% 是什么**：它不是页目录，是**「数字怎么动的」的流水账**
（243→258→254→252→262→256 的逐次对账、每次消掉几个新造几个）。
`log.md` 里已经写着「**这一段留着，因为『数字怎么动的』比数字本身有用**」——
那正是它该在的地方。**索引是每次查询第一个读的文件，它每一行都要挣得自己的位置。**

所以这一步是**搬家**，不是删：
- 「**现在缺什么**」（五条）留在索引里，**短**。
- 「**这个数是怎么走到今天的**」进 `log.md`，**一字不删**。

> ⚠️ **不是「超预算就拆子索引」**：真正该拆的判据是「**这一节不是页目录**」。
> 上面那 43% 满足；`## 对象` 那 2,121 满足不了（它就是页目录）。
> **别把「拆了更整齐」当成「拆」的理由**（§7），也**别把「先拆了再说」当解法**。

## 二、另外修掉一个洞

`index.md` 里有 **两个** `<!-- index-token: … -->`（第 3 行 13,261 对、
**第 510 行 13,041 是旧的**）。`check_index_budget` 原先只认第一个，
`--write` 也只刷第一个——**第二个既不被测也不被刷，永远漂着**。
已改成「多于一个标记直接判红」，本脚本负责把多的那个删掉。

用：`python -X utf8 extract/index_rebuild.py`          # 只看要写什么
    `python -X utf8 extract/index_rebuild.py --write`  # 真写
"""
import csv
import re
import sys
from pathlib import Path

BASE = Path(r'F:\master-dev\understand-anything-wiki')
WIKI = BASE / 'wiki'
INDEX = WIKI / 'index.md'
LOG = WIKI / 'log.md'
PLAN = BASE / 'extract' / 'wiki-plan.csv'

# ── 71 行：`slug: 钩子`。**钩子是人写的**，一句，讲清「它是什么 / 为什么值得一页」。
#    能引「谁在等它」就引——那正是这批页建出来的理由（§9.1）。
OBJ_HOOK = {
    # ── L1 固件命令：11 条，全部是别的页伸手要的悬空目标 ──
    'ctxt': '`CTXT`（ConTeXT）：定义 mode context；**level / timing 两条「mode context 必须一致」'
            '的约束都要它**',
    'dfpn': '`DFPN`（DeFine Pin Name）：给 pin 起名；**pin 页与三条约束页共同的前置命令**',
    'sqst': '`SQST`（SeQuencer STate）：读/设 sequencer 状态；level 与 pin 的约束页都要它',
    'pals': '`PALS`（Pin ALlocation for multiple Sites）：多 site 的 pin 分配；'
            '**必须在任何其他 setup 命令之前**',
    'psfc': '`PSFC`（Parallel Setup FoCus）：并行 setup 的焦点；**执行前必须先设站点焦点**',
    'conf': '`CONF`（CONFiguration）：pin configuration；`PALS` 必须先于它',
    'dscp': '`DSCP`（Define System Control Parameter）：系统控制参数',
    'jscf': '`JSCF`（Jitter Set ConFiguration）：配置 jitter 集；**必须先定义再引用**',
    'jsdf': '`JSDF`（Jitter Set DeFinition）：定义 jitter 集；与 `JSCF`/`JSPR` 同族',
    'jspr': '`JSPR`（Jitter Set PRimary set）：指定主 jitter 集',
    'pste': '`PSTE`（Parallel SiTe Enable）：启用并行 site',
    'sequencer': '定序程序本身：`SQST` 读的是它的状态，pattern 与 pin 的约束都围着它',
    # ── L3 测试方法 API ──
    'primary-status': '`PRIMARY_STATUS`：primary 侧的测量入口，level / timing / pattern 三段共用',
    'sequencer-status': '`SEQUENCER_STATUS`：从测试方法侧读 sequencer 状态',
    'tmlimits': '`TMLimits`：测试方法侧写 limits 的接口；results 与 testmethod 两段都要它',
    'alphabetical-list-of-flags': '结果旗标一览；**语料里被引 62 篇**，是 flag 类问题的入口',
    'dc-result-accessor': '`DC_RESULT_ACCESSOR`：DC 测量结果的取数接口',
    'dps-power-flags-get-functions': '`DPS` 电源旗标的 `get...()` 一族函数',
    'spmu-pin-task-mode': '`SPMU_PIN_TASK.mode()`：SPMU 的 pin 工作模式',
    'smartcalc-framework': 'SmartCalc 框架：**用公式而不是常数描述测试条件**',
    'smartrdi': 'SmartRDI：**DC Scale 类卡件的编程接口**；'
                '「怎么用」（TMU 测试、DC Scale pin 设置）并在本页',
    'event-base': '`EVENT_BASE`：**所有 `EVENT_*` 测试方法的基类**，讲清它才讲得清那一族',
    'event-waveform-vfim': '`EVENT_WAVEFORM_VFIM`：同一时刻产生波形并测量；'
                           '**与 [[event-waveform-vfvm]] 是两个类**（`.63.38` / `.63.39`）',
    # ── gui ──
    'report-window': '报错窗口；**两页排错页的入口**，但排错页讲的是「看到什么报错」，'
                     '本页讲窗口本身',
    'timing-diagram-tool': 'Timing Diagram Tool：**pattern / results / run / timing 四段共用**；'
                           '「怎么用」并在本页',
    'error-map-tool': 'Error Map Tool：把失败的 bit 映射回物理位置',
    'shmoo-tool': 'Shmoo Tool：**怎么设一个 shmoo 测试**并在本页；'
                  '生成侧在这里，画图侧在 [[analysis-views]]',
    'setup-management-tool': 'Setup Management Tool：工程内 setup 的管理',
    'integrated-result-tool': 'Integrated Result Tool：**所有分析视图跑在它里面**',
    'digital-pins-editor': 'Digital Pins editor：**图形界面上配 pin**，与 L1 命令是两条路',
    'stpm': 'SmarTest Program Manager：程序管理工具',
    'protocol-editor': 'Protocol editor：编辑协议（时序与电平的协议化描述）',
    'test-summary-tab': 'Test summary tab：**十一种分析视图都在这里选**（`Bin wafer map` 除外）',
    'raw-data-views': 'Raw data views：未经汇总的原始结果',
    # ── file ──
    'model-file': '**model file**：机台硬件配置的根文件；**启动读不到就起不来**（见排错两页）',
    'testflow-file': 'testflow 文件：测流的存储形态',
    'stpm-control-file': 'STPM control file：程序管理器的控制文件',
    'technology-file-for-a-device': 'Technology file：**器件的工艺角信息**；'
                                    '原候选 `technology-file` 是同一对象的另一种叫法，已并入本页',
    'global-section': 'model file 里的 `GLOBAL` 段',
    'data-logging-profiles': 'Data Logging Profiles：**记什么、记多细**由它定',
    'structure-of-a-tmlimits-csv-file': 'Test number 与 limits 的 CSV 表结构；'
                                        '生成侧（Test Number Generator）并在本页',
    'special-test-suites': 'Special test suites：testflow 里的特殊测试组',
    'rdi-configure-file': '`RDI_Configure` 文件：SmartRDI 的配置文件',
    'device-access-file': 'MTL 的 Device access file：**怎么访问器件**',
    'pin-mapping-file': 'MTL 的 Pin mapping file：**测试 pin ↔ 器件 pin 的映射**',
    'apg-pattern-file': 'APG pattern file：**算法图形发生器的图形描述**',
    'apg-program-file': 'APG program file：APG 的程序（图形之外的循环与控制）',
    # ── L2 / 卡件 / 板级 ──
    'spec-set': 'Spec sets：**成组地切换 spec 值**（多 site / 多条件）',
    'execution-context': 'execution context：**不能随用随起名字**，必须先在固件级定义',
    'tpt-generate-device-dir': '`tpt_generate_device_dir`：生成器件目录',
    'dpspins-resources': '`DPSPINS` 的 resource 关键字：电压斜坡等参数的写法',
    'mtp-memory-test': '`MTP_MEMORY_TEST`：存储器件测试',
    'dc-scale-xps256-card': 'DC Scale XPS256 卡：**语料里被引 95 篇，全库并列第一**',
    'dc-scale-uhc4t-card': 'DC Scale UHC4T 卡；**DUT 板侧那一章**'
                           '（`02.03.08.01.06`，原候选 `dc-scale-uhc4-uhc4t-card`）已并入本页',
    'utility-card': 'Utility Card：**给 DUT 供非测试用电**的那张卡',
    'utility-power-supplies': 'Utility power supplies：外部 utility 电源',
    'utility-pogo-block-utility-card-v93000-exa-scale-systems':
        'Utility Card 的 pogo block（V93000 EXA Scale 系统）',
}

CON_HOOK = {
    'dut-board-design-reference': 'DUT 板设计参考的**总入口**；**语料里被引 95 篇，全库并列第一**',
    'layout-information-dut-board': 'DUT 板的**版图信息**（尺寸、孔位这类要交给画板人的东西）',
    'direct-probe-stiffener': 'Direct-Probe stiffener：直针探测时的加强板',
    'ganging': 'ganging：**多张卡并联驱动同一个 DUT pin**；'
               '跨卡 ganging 要先 `DDIC`（见 [[cross-card-ganging-requires-ddic]]）',
    'edf-data-organization': 'EDF 数据**怎么组织**；**语料里被引 78 篇**',
    'edf-data-types': 'EDF 的**数据类型**；**语料里被引 72 篇**',
    'equation-based-level-setup': '**用方程而不是常数**描述 level 条件',
    'smartrdi-vector-and-protocol-programming': 'SmartRDI 下的**向量与协议编程模型**',
    'dc-test-programming': 'DC 测试编程：**这一类测试怎么组织**（不是某一条命令）',
    'controlling-multiple-sites': '**多 site 怎么控制**：焦点、并行、site 间差异',
    'how-to-create-a-universal-test-method-class': '怎么写一个**通用**测试方法类',
    'setting-chart-display-options': '**图怎么画**（坐标轴、刻度这类显示选项）',
    'command-reference': '`02.06` 整章：**L1 固件命令字典**（367 篇）的入口与读法',
    'timing-setup-commands': '`02.06.06` 整章：timing 类 L1 命令成组出现，讲清分组关系',
}


def main():
    if (sys.stdout.encoding or '').lower().replace('-', '') != 'utf8':
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    write = '--write' in sys.argv
    t = INDEX.read_text(encoding='utf-8')

    # ---- 甲 · 把「已知缺口」整节搬到 log.md ----
    i = t.index('## 已知缺口')
    j = t.index('## 概念')
    gap_old = t[i:j].rstrip() + '\n'
    n_gap_lines = gap_old.count('\n')
    print(f'「已知缺口」原节：{n_gap_lines} 行 / {len(gap_old):,} 字符 → 搬进 log.md')

    new_gap = """## 已知缺口（五条）

<!-- index-count: 已知缺口 = 5 -->

> **⚠️ 2026-09-18：这一节从 468 行缩到本节。** 它原先 5,664 token = **全页的 43%**，
> 而 `index.md` 是**每次查询第一个读的文件**（§7 硬约束 < 15,000 token）。
> 缩掉的**不是内容，是位置**：那 468 行讲的是「**数字怎么走到今天的**」
> （243→258→254→252→262→256 的逐次对账、每次消掉几个新造几个、哪一批有功劳哪一批没有），
> **一字不删地搬进了 `log.md` 的 `## [2026-09-18] index.md 瘦身` 一节**。
> **索引留「现在缺什么」，`log.md` 留「怎么走到今天」。**
> 这不是「拆了更整齐」——是那 43% 本来就不是页目录（§7）。

**一、L3 返工已完成。** 九页 stage 原有七页的 L3 只写「文档未覆盖」，其中**四页的断言本身是错的**
（例：level 页写「Test suite control API 不提供任何 level 值接口」，而
`TestsuiteProxy.setEquationBasedLevel()` 就是）。错因是建页简报里「L3 很薄」被照办。
**九页已按 §2.1 返工**为「横切入口 + 本阶段专属族」，并在页内留下改判记录。
连带查出 `schema.md` §3 把 L3 枚举成 67 篇而**漏了 TPI 的 31 篇**，已改 98 篇——
漏一项的后果不是少一个数，是 [[tpi-program-routines]] **没有槽位可放**，
被降级成「`L3`（推断，存疑）」。**枚举式的定义，漏一项就会造成这种降级。**

**二、悬空 wikilink 是建页 backlog 的首选清单。** 它们**不是页面错误**，
是**已经建成的页伸手去要、但还没建的页**。当前清单与逐目标账见 `extract/dangling.csv`
（第八类产出；报告里印**口径指纹** `sha256[:12]`，口径变了就是变了，不和上一版混着比）。
**判据**：第八类只扫**内容页**（`stages/` `objects/` `concepts/` + 本页），
`log.md` 是记录、要能引用坏拼法，不在范围内。

> **这张单和 `unowned.csv` 是两张不同的工作单，交集很小。**
> `dangling.csv` 说「**流程页缺了它就断**」（按被引处数）；
> `unowned.csv` 说「**语料里常出现**」（按 `in_src ≥ 20`）。
> 实测过一次：**建 16 页只让第八类消掉 1 个**——那 16 页是照入度建的，
> 绝大多数**根本没人链接过**。**想让第八类降，得照 `dangling.csv` 建。**
> 上一批 71 页（2026-09-18）就是照 `dangling.csv` 前段 + `in_src ≥ 20` 两批并起来建的。

**三、slug 归一已完成（第九类 ✅）。** 共 **49 个**目标曾被写成非 §5 拼法
（`Integrated_Result_Tool` / `TMLimits` / `EDF` / `ON_FIRST_INVOCATION_BEGIN` / `SpecValue`…），
不归一就会按不同 slug 建出重复页。**其中一个撞了 stage 名**：`PATTERN`（L2 类）
机械转出 `pattern`，而那是脊椎第七段——已加限定词为 [[pattern-object]]，
规矩写进 `schema.md` §5。**指错比重复更坏：重复页看得见，指错看不见。**

**四、26 个高入度对象不属于任何 stage —— ✅ 已清（2026-09-18）。**
工作单 `extract/unowned.csv`（`python unowned.py` 生成，**断言自己的数与
`stage-report.md` 第六类相等，不等就退出**——清单和报告永远是同一个数）。
第六类的 ❌ **从 26 → 0**。
**2026-09-18 定：stage 之外照建 `object` 页**（§12），判据是**入度**，
不是「属不属于某段流程」——stage 是**流程脊椎**，硬塞会把脊椎撑歪。

> ⚠️ **工作单清空 ≠ 工作做完。** `unowned.csv` 只收 `in_src >= 20` 的候选；
> **反向也不成立**：第六类转 ✅ 只证明「每个高入度候选都有归宿」，**不证明「那页写得对」**。
> 而 `in_src < 20` 的对象**这张单从头到尾没管过**——那是另一个尺度的欠账。
> **入度是判据之一，不是唯一判据**（反例已有两个：[[pogo-block-compatibility]]、
> [[inter-layer-via-design]]，都是照定义文档自己的 `Subtopics` 建的）。

**五、抽取器漏收过一大块示例代码（2026-09-18 查出并修）。**
`## Examples` / `## Syntax` 底下的 `### 子段`**被整段丢掉**——状态机遇到 H2 开段、
紧接着的 H3 立刻把它关掉。**实测 256 篇 / 新增 427,979 字符**的示例代码从未进过任何页面。
**没有一条检查发现过它**，因为「语法节非空」一直是绿的：对 `## Syntax` 直接带正文的文档，
这条规则本来就够用。**这是「检查比它自称的范围窄」的第四次，也是最贵的一次——
前三次窄的是检查，这一次窄的是产出。**

连带三件事：①`is_stub` 挡掉 29 段「去了图片就什么都不剩」的段；
②两个页面的语法节原写着「无」——那是**从抽取器的盲区推出来的，不是文档事实**，
已改成脚本管辖并收到内容，页里写明了这次更正；
③`refresh()` 的边界判据换过三次，现在靠页面里的 `<!-- 语法节 begin/end -->` 标记
+ **没有标记就拒绝执行的互锁**。**教训**：脚本对「页面长什么样」的假设，
写成判据就会变成删数据的刀。

**新增第十二/十三类检查**：脚本写的那一节和脚本**现在**的产出是否逐字一致
（`check_syntax_fresh.py`）；版本页声称的「条目原样转录」是否成立
（`check_version_fresh.py`，**条目逐条回 raw 找完全子串，不经过抽取器**）。
**两处此前都是空的**——脚本换了页面没跟上、或者条目被手改过，**没有灯会亮**。

> **第十四类补了三条**：`wiki-plan.csv` 的 `status` 与文件在不在对不上（丁）、
> 页面在目录里而表里没登记行（戊）、**本页自己声明的 token 数和实测一致且没超预算**（己）。
> 第九类补了两条：**文件名本身**合不合 §5、以及**不许两个文件共用一个 stem**。

---

"""
    t = t[:i] + new_gap + t[j:]

    # ---- 乙 · 删掉多出来的那个 index-token 标记 ----
    marks = list(re.finditer(r'<!--\s*index-token:.*?-->', t))
    print(f'index-token 标记：{len(marks)} 个')
    if len(marks) > 1:
        for m in marks[1:]:
            line = t[:m.start()].count('\n') + 1
            print(f'   删掉第 {line} 行那个：{m.group(0)}')
            t = t[:m.start()].rstrip() + '\n' + t[m.end():].lstrip('\n')
            t = re.sub(r'\n{3,}', '\n\n', t)

    # ---- 丙 · 把 71 页登记进两节 ----
    plan = {r['slug']: r for r in csv.DictReader(
        PLAN.open(encoding='utf-8')) if r['slug'] and not r['slug'].startswith('#')}

    def add(section_head, next_head, hook, kind, dirname):
        nonlocal t
        i = t.index(section_head)
        j = t.index(next_head, i)
        block = t[i:j]
        files = sorted(p.stem for p in (WIKI / dirname).glob('*.md'))
        have = set(re.findall(r'\[\[([^\]]+)\]\]', block))
        new = [s for s in files if s not in have]
        # **只给「新登记的」要求钩子**：已经在索引里的那批，它们的描述写在
        # 前面几个批次的段落里，不在本文件的表里——要求它们也有钩子，
        # 等于逼我把已有描述抄第二遍（两处描述 = 一处会漂）。
        miss = [s for s in new if s not in hook]
        if miss:
            raise SystemExit(f'❌ {dirname} 里有页没写钩子，**不许静默漏掉**：{miss}')
        for s in hook:
            if s not in files:
                raise SystemExit(f'❌ 钩子表里的 `{s}` 在 {dirname}/ 里没有对应页')
        if not new:
            print(f'   {section_head}：无需登记')
            return
        # 计数标记也要跟着改
        m = re.search(r'<!--\s*index-count:\s*%s\s*=\s*(\d+)\s*-->' % kind, block)
        if not m:
            raise SystemExit(f'❌ {section_head} 里没有 `index-count: {kind}` 标记')
        block = block[:m.start()] + f'<!-- index-count: {kind} = {len(files)} -->' \
            + block[m.end():]
        lines = ['']
        lines.append(f'**2026-09-18 第四批（{len(new)} 页，照 `dangling.csv` + `in_src ≥ 20` 两批并起来建的）：**')
        lines.append('')
        for s in new:
            r = plan.get(s, {})
            lines.append(f'- [[{s}]] `{r.get("layer","?")}/{r.get("stage","?")}` — {hook[s]}')
        lines.append('')
        k = block.index('\n---\n', len(section_head))
        # **末尾必须 `+ t[j:]`。** 第一版写成 `t[:i] + block[:k] + lines + block[k:]`——
        # 而 `block` 只到 `j` 为止，于是**这一节之后的整份文件被静默丢掉**
        # （`## 对象` 及以后全没）。实测：这么切完 `'## 对象' in t` 变成 False。
        # **切片的下标写错不会报错，只会少东西**——所以下面那句断言不是装饰。
        t = t[:i] + block[:k] + '\n'.join(lines) + block[k:] + t[j:]
        if '## 对象' not in t or '## 排错' not in t:
            raise SystemExit('❌ 拼接把后面的小节弄丢了——切片写错了，停下')
        print(f'   {section_head}：登记 {len(new)} 页，计数标记改成 {len(files)}')

    add('## 概念', '## 约束', CON_HOOK, '概念', 'concepts')
    add('## 对象', '## 排错', OBJ_HOOK, '对象', 'objects')

    # ---- 丁 · 头部那句「（脊椎 9 / 概念 8 / …）」跟着改 ----
    t = re.sub(r'（脊椎 9 / 概念 8 / 约束 14 / 对象 22 / 排错 6；映射还没有页）',
               '（脊椎 9 / 概念 {c} / 约束 14 / 对象 {o} / 排错 6；映射还没有页）'
               .format(c=len(list((WIKI/'concepts').glob('*.md'))),
                       o=len(list((WIKI/'objects').glob('*.md')))), t)

    if not write:
        print('\n（只看，没写。加 --write 才写。）')
        return

    import snapshot
    box = snapshot.save(quiet=True)
    INDEX.write_text(t, encoding='utf-8')
    # 搬走的那一节进 log.md
    with LOG.open('a', encoding='utf-8') as f:
        f.write('\n---\n\n## [2026-09-18] index.md 瘦身：把「数字怎么动的」搬到这里\n\n'
                '**来源**：`wiki/index.md` 的 `## 已知缺口（五条）` 一节，'
                f'原文 {n_gap_lines} 行 / {len(gap_old):,} 字符 / **5,664 token = 全页 43%**。\n\n'
                '**为什么搬**：§7 硬约束 `< 15,000 token`，而这一批要往索引加 71 行。\n'
                '搬的是**位置不是内容**——索引留「现在缺什么」，这里留「怎么走到今天的」。\n'
                '**下面一字未删、未改**（只把标题从 `##` 降一级，因为进了 log.md）。\n\n'
                + gap_old.replace('\n## ', '\n### ') + '\n')
    print(f'\n✅ index.md 已重写（{len(t):,} 字符）；账本已追加到 log.md')
    print(f'   ↳ 改前快照 `{box}`')
    print('   下一步：python -X utf8 extract/check_index_budget.py --write')


if __name__ == '__main__':
    main()
