# -*- coding: utf-8 -*-
"""建页资料包 —— 把「建一个对象页所需的全部 raw 材料」打成一包。

**为什么要有这一步。**

`schema.md` §12 说「每次调用喂该簇的索引 + 相关原文摘录」，§4 说
「对象页的语法 / 参数表骨架由**脚本**从 raw 的 `## Syntax` / `## Parameters` 抽」。
两句话合起来的意思是：**建页时我不该去 9,398 篇里翻，也不该凭记忆默写参数表。**

这一个脚本把三样东西钉在一起：

1. **定义文档的全文**（`unowned.csv` 里的 `rel` 就是「定义它的那篇」）
2. **入边**（谁引用了它、引用的那句话是什么）—— 这是「和谁有关」一节的**唯一合法来源**。
   不是我想出来的关系，是语料里真的写了的关系，带原句可查。
3. **语法 / 参数段落的逐字抽取** —— §4 的分工。这一段进页面时**逐字照抄，不重写**；
   重写就会把「文档事实」降级成「我的转述」，而 §11 要求两者分得开。

**入边为什么要带语境句**：`hubs-dedup.csv` 只给一个数字（in_src=45）。
45 是个数，不是关系。要写「它和谁有关」，必须有**每一篇为什么提它**。
`edges.jsonl` 里每条边都存了 `context`（所在行）和 `line`，这就能回答「为什么」。

用：`python objpack.py <batch.txt>`，batch.txt 每行一个 rel（`#` 开头是注释）。
产出：`extract/pack/NN-<短名>.md`，一包一页。
"""
import csv
import json
import re
import sys
from pathlib import Path

BASE = Path(r'F:\master-dev\understand-anything-wiki')
OUT = BASE / 'extract'
CORPUS = Path(r'F:\master-dev\dorm-wsl-sytest\tdc-html\agent-markdown\by-category')

# 要逐字抽出来的段落名（小写比较）。**只认这些名字**——多认一个就可能把
# 散文当参数表抄进页面。少认一个的代价是那一节空着，看得见；多认的代价是错的。
SEC_HEADS = {
    'syntax', 'parameters', 'parameter', 'arguments', 'argument',
    'return value', 'return values', 'returns', 'example', 'examples',
    'usage', 'description',
}

# `## Example` 之外还有 `### Example 1: SmartRDI, pattern-based programming` 这种
# **带后缀的**例子标题。第一版只认整名相等，于是 `XPS256 programming - PMU operating mode`
# 只抽到了上面那段「Examples 导语」，**三个真正带代码的例子全丢了**——
# 而代码就是那一页的正文。
# 规则放宽到：**标题以 `example`/`examples` 开头**（后面可以跟序号或说明）。
# 不放宽到「标题里含 example」：那样 `Examples of what not to do` 之类也会进来。
SEC_EXAMPLE_PREFIX = re.compile(r'^examples?\b', re.I)

# 「去了图片就什么都不剩」的段。
#
# **这是修 H2/H3 那个 bug 时暴露出来的副作用。** 修完之后，
# `Data navigation views` 的子主题里那五个 `## Example` 全进来了——
# 打开一看，**每段只有一张截图**：
#
# ```
# ## Example
#  ![Data log summary view_Test Summary](<../../../../raw/136411.png>)
# ```
#
# 图片在 wiki 里**根本打不开**（相对路径指向 raw，`unlink()` 会把它改写成纯文本），
# 收进去等于给页面加五段 `!``…``（raw: …png）`。
#
# **判据是「文本量为零」**：把图片、链接、空白、纯标点都去掉后什么都不剩，就不收。
# 不是「整段是不是图片」——**带一句话说明的截图段要保留**（那句话是真内容）。
MD_IMG = re.compile(r'!\[[^\]]*\]\([^)]*\)')
MD_ANY_LINK = re.compile(r'\[[^\]]*\]\([^)]*\)')


def is_stub(body):
    """段正文去掉图片 / 链接 / 空白 / 标点后为空 → 没有文本量，不收。"""
    t = MD_ANY_LINK.sub('', MD_IMG.sub('', body))
    return not re.sub(r'[\s\W_]+', '', t)



def load_docs():
    out = {}
    with (OUT / 'docs.jsonl').open(encoding='utf-8') as f:
        for ln in f:
            d = json.loads(ln)
            out[d['rel']] = d
    return out


def load_edges():
    """出边 / 入边两张表。**只收 `inline` 边。**

    第一版收了全部边，于是「Data navigation views」的入边报 **46 篇**，
    而 `hubs-dedup.csv` 报 **45**。差的 1 条是 `02_System_reference/index.md`
    的 `toc` 边（章节目录链接）。

    `hubs.csv` 的 `in_src` 从一开始就**只计 inline 边**（这话写在 `index.md` 里），
    所以资料包多算的那 1 条不是「语料事实」，是**我这张表的口径和排名表不一样**。
    页面上的入度只能有一个数，那就必须是排名表那个数——
    **同一个东西两个数，最后一定会有一个错的被写进页面。**
    """
    outb, inb, drop = {}, {}, 0
    with (OUT / 'edges.jsonl').open(encoding='utf-8') as f:
        for ln in f:
            e = json.loads(ln)
            if e['kind'] != 'inline':
                drop += 1
                continue
            outb.setdefault(e['from'], []).append(e)
            if e.get('resolved') and e.get('to'):
                inb.setdefault(e['to'], []).append(e)
    return outb, inb, drop


_SECTIONS_CACHE = None


def _sections_index():
    """`sections.jsonl` 一次读进内存，按 `doc` 建索引。

    **为什么要缓存（2026-09-20）**：`sections_of()` 原来是「每次调用重扫一遍整个文件」。
    单次调用无所谓，但 `error_block()` 每页调一次——170 页 × 23,315 行，
    **跑一次检查要两分钟以上**。缓存之后是毫秒级。
    """
    global _SECTIONS_CACHE
    if _SECTIONS_CACHE is None:
        idx = {}
        with (OUT / 'sections.jsonl').open(encoding='utf-8') as f:
            for ln in f:
                s = json.loads(ln)
                idx.setdefault(s.get('doc'), []).append(s)
        _SECTIONS_CACHE = idx
    return _SECTIONS_CACHE


def sections_of(rel):
    """从 sections.jsonl 取该篇的结构段落（Procedure / Dependency / Errors …）。"""
    return list(_sections_index().get(rel, ()))


def verbatim_sections(text):
    """逐字抽 `## Syntax` / `## Parameters` 这类段落。

    手工逐行状态机，不引 yaml/markdown 库：`extract.py` 立的规矩是主链路零依赖。
    只在 **H2/H3** 上切；H4+ 归入当前段（文档里参数常在 H4）。

    **H2 段拥有它底下不命中的 H3 子段**（2026-09-18 修，见下）。

    ---

    **这个 bug 值得写下来，因为它是「检查比它自称的范围窄」的又一例，
    只是这次窄的是抽取器自己。**

    原实现遇到**命中的 H2**（`## Examples`）就开一个 buffer，**紧接着的 H3 立刻把
    `cur` 置空**——buffer 里只剩 H2 与第一个 H3 之间那几行导语（通常是空的，
    被末尾 `if b` 滤掉）。于是：

    ```
    ## Examples                     ← cur = 'Examples'，buf = []
    ### Executing an existing test suite   ← flush('Examples', '')，cur = None，**正文从这里全丢**
    ```

    实测（`gap_measure.py`，**老逻辑 vs 新逻辑逐篇做差**）：**256 篇 /
    新增 427,979 字符、减少 2,187 字符**。增量最大的单篇是
    `02.07.04.01.30_DEMODULATION.md`（**+21,337**）。
    减少的那 2,187 是 `is_stub` 挡掉的 **29 段「去了图片就什么都不剩」的段**
    （见下），**其余一篇都没写坏**。
    **没有一条检查发现过它**，因为「语法节非空」一直是绿的——
    对 `## Syntax` 直接带正文的文档，这条规则本来就够用。

    > **这个脚本的第一版量错了，也一并记着**：它数的是「命中 `SEC_HEADS` 的 H2
    > 底下所有 H3 子段」，**把本身就命中的 H3 也算进去了**——`### Example 1: …`
    > 这种老逻辑从来没漏过。于是报出 **517 篇 / 964,713 字符**，虚高了一倍多。
    > **「该收多少」是个会写错的定义；「两版跑一遍做差」不会。**

    **定性**：`SEC_HEADS` 里明明写着 `examples`，**抽取器声称收示例，却只收
    「H2 底下、第一个 H3 之前」那几行**。抽取范围比自称的窄，窄掉的那块没有灯。

    **修法**：H2 开的段继续拥有后面**不命中**的 H3——把那个 H3 标题行原样并进正文，
    读者仍看得见分段。H3 开的段**行为不变**（遇到下一个标题就结束），
    这条护栏保证已建页面的语法节不会因为本次改动而变形。
    """
    lines = text.splitlines()
    # 跳 frontmatter
    i = 0
    if lines and lines[0].strip() == '---':
        i = 1
        while i < len(lines) and lines[i].strip() != '---':
            i += 1
        i += 1
    cur, buf, out = None, [], []
    h2_owned = False        # 当前段是否由 H2 开（只有它拥有不命中的 H3 子段）
    for ln in lines[i:]:
        m = re.match(r'^(#{2,3})\s+(.+?)\s*$', ln)
        if m:
            lvl, name = len(m.group(1)), m.group(2).strip()
            hit = (name.lower() in SEC_HEADS or bool(SEC_EXAMPLE_PREFIX.match(name)))
            # H2 一律结束当前段；命中的标题一律结束当前段；
            # H3 开的段遇到任何标题都结束（**这条是行为护栏，不许改**）。
            if cur and (lvl == 2 or hit or not h2_owned):
                out.append((cur, '\n'.join(buf).strip()))
                cur, buf, h2_owned = None, [], False
            if hit:
                cur, buf, h2_owned = name, [], (lvl == 2)
            elif h2_owned:
                buf.append(ln)      # H3 标题行进正文，分段仍看得见
            continue
        if cur is not None:
            buf.append(ln)
    if cur:
        out.append((cur, '\n'.join(buf).strip()))
    # `is_stub` 挡掉「去了图片就什么都不剩」的段——**不静默**，
    # `gap_measure.py` 会数出来有多少段是这么被挡的。
    return [(n, b) for n, b in out if b and not is_stub(b)]


SUBTOPIC_HEAD = re.compile(r'^#{2,4}\s+subtopics\s*$', re.I)
MD_LINK = re.compile(r'\[([^\]]*)\]\(\s*<?([^)>\s]+)>?\s*\)')


def subtopic_rels(text, rel):
    """定义文档在 `Subtopics` 标题下声明的子主题，解析成语料内相对路径。

    **为什么需要它**：`Device architecture file` 的定义文档里**没有** `## Syntax` 段，
    语法在子主题 `Device architecture file syntax` 里（原文：*"The syntax for these
    settings is described in …"*）。只抽定义文档自己的段落，这一页的「语法 / 参数」
    就永远是空的——**而它是个文件格式页，没有语法等于没有正文。**

    **只取 `Subtopics` 标题紧跟着的那串列表项**，不是「这个标题到下一个标题之间」。
    第一版写的是后者，于是 `Device architecture file` 抽出 4 个子主题——
    因为这篇的 `#### Subtopics` 是个 **H4 标签**，而它后面的散文直接挂在 H1 下，
    中间**没有** `##` 标题，所以「到下一个标题为止」把**整段正文**都圈进来了，
    顺手把正文里提到的 `APG pattern file`、`Maintenance operations` 也算成了子主题。
    **那会让我从兄弟文档里抄语法。** 改成只认紧跟的列表项，这个口就堵死了。

    取多了的代价是张冠李戴（抄错参数表），取少了的代价是那一节空着（看得见）——
    **同 `SEC_HEADS` 的取舍：宁可空。**
    """
    lines = text.splitlines()
    start = None
    for i, ln in enumerate(lines):
        if SUBTOPIC_HEAD.match(ln):
            start = i + 1
            break
    if start is None:
        return []
    items = []
    for ln in lines[start:]:
        if not ln.strip():
            continue
        if re.match(r'^\s*[-*+]\s', ln):
            items.append(ln)
            continue
        break                      # 第一个非列表、非空行 —— 列表结束，后面是正文
    seg = '\n'.join(items)

    here = Path(rel).parent
    out = []
    for _t, p in MD_LINK.findall(seg):
        if p.startswith(('http:', 'https:', '#', 'mailto:')):
            continue
        cand = (here / p).as_posix()
        # `..` 归一并回到语料根；跨出语料的（`../../../../raw/102413.png`）自然落空
        parts = []
        for c in cand.split('/'):
            if c == '..':
                if parts:
                    parts.pop()
                else:
                    parts = None
                    break
            elif c not in ('', '.'):
                parts.append(c)
        if not parts:
            continue
        r = '/'.join(parts)
        if r.endswith('.md') and (CORPUS / r).is_file() and r != rel:
            out.append(r)
    return out


def _nice(rel):
    return re.sub(r'^\d+(\.\d+)*_', '', Path(rel).stem).replace('_', ' ')


# 声明的子主题树最多往下走几层。**不是随手定的数**：
# `test-suite-control-api` 的语法在第 **3** 层——根 → `…API reference` → `TestsuiteProxy`
# → `TestsuiteProxy.attachTestmethod()` 才有 `## Syntax`。只走一层时那一节是空的，
# 而这一章的全部实质就是那 48 篇成员函数的签名与参数。
# **走几层是语料自己说的**（`Subtopics` 列表），不是我猜的；这个上限只是防跑飞。
SUBTREE_MAX = 3


def _sub_parts(rel, depth, chain):
    """在**声明的** `Subtopics` 树里递归取 `SEC_HEADS` 段。

    返回 `[(段名, 正文, 来源 rel, 链)]`，`chain` 是从直接子主题到本节点的名字序列
    （用来在段名里写清「这段是从哪一篇、怎么找到的」）。

    **只在当前节点抽不到时才往下走。** 这是「先窄后宽」：抽得到就**不看孩子**，
    孩子的正文不会盖过父母。上一版只走一层，等于把「抽不到」当成了「没有」——
    **「我没找到」和「文档没有」是两件事**，九页返工就栽在这句话上。
    """
    body = (CORPUS / rel).read_text(encoding='utf-8', errors='replace')
    got = verbatim_sections(body)
    if got:
        return [(n, b, rel, chain) for n, b in got]
    if depth >= SUBTREE_MAX:
        return []
    out = []
    for sub in subtopic_rels(body, rel):
        out += _sub_parts(sub, depth + 1, chain + [_nice(sub)])
    return out


def collect_syntax(rel):
    """抽语法 / 参数段；**定义文档没有时跟 `Subtopics`（可递归）**。

    返回 `(parts, srcs)`：`parts` 是 `[(段名, 逐字正文)]`，`srcs` 是每段各自的来源 rel。

    **为什么每段都要记来源**：`Sharing configuration file` 的语法在**自己**文档里，
    `Device architecture file` 的语法在**子主题**里。两者抄进页面后长得一模一样，
    **不写明来源就分不出来**——而「这段是从哪篇抄的」正是 §11 要的那条线。

    子主题分两种，处理方式不同：

    - **`*_file_syntax` 子主题 → 整篇照收**。理由：这类文档**通篇就是关键字表**
      （实测 `Device architecture file syntax` 共 961 行，L132–L950 全是
      `Keywords and parameters` / `Bit inversion keywords` / … 的表，
      只有末尾 5 行是 `Related information` + `Functional changes`）。
      用 `SEC_HEADS` 那套按标题抽只会抓到**第一张表**（`## Keywords and parameters`），
      后面十几张全丢——**而它们才是参数表的主体**。所以这里整篇收，只砍尾部元信息。
    - **其他子主题 → 仍按 `SEC_HEADS` 抽**，抽不到就算了。

    **整篇收不违反 §3「不抄原文」**：§3 禁的是把**产品文档**搬进 wiki，
    §4 授权的正是「语法 / 参数表由脚本从 raw 抽」。一篇 `_file_syntax` 就是一张参数表。
    """
    body = (CORPUS / rel).read_text(encoding='utf-8', errors='replace')
    subs = subtopic_rels(body, rel)

    # ① `_file_syntax` 子主题**无条件收整篇**。
    #    「无条件」是被数据逼出来的：`Device architecture file` 自己有一个 `## Example`，
    #    第一版写成「自己有段落就不看子主题」，于是它的参数表**永远进不了页面**——
    #    而那一整篇 961 行就是参数表。**「有段落」不等于「有参数表」**，
    #    判据得是「有没有 `_file_syntax` 子主题」。
    parts, srcs = [], []
    for sub in subs:
        if Path(sub).stem.endswith('_file_syntax'):
            sbody = (CORPUS / sub).read_text(encoding='utf-8', errors='replace')
            parts.append((f'{_nice(sub)}（整篇，取自子主题）', strip_tail(sbody)))
            srcs.append(sub)

    own = verbatim_sections(body)
    # ② 自己和 `_file_syntax` 子主题都没有 → 再放宽一层，看其他子主题的 `SEC_HEADS` 段。
    #    顺序不能反：先窄后宽，宽的那层只在窄的全落空时才走。
    if not own and not parts:
        for sub in subs:
            for n, b, src, chain in _sub_parts(sub, 1, [_nice(sub)]):
                # 段名里写全「怎么找到的」。**一层时不写链**——那样和上一版的段名
                # 逐字相同，已建页面的语法节就不会因为这次改动而变（回归护栏）。
                via = ' › '.join(chain) if len(chain) > 1 else chain[0]
                parts.append((f'{n}（取自子主题 {via}）', b))
                srcs.append(src)
    # ③ 还是空 → 最后一层：正文里的管道表格。**只在前面全落空时才走**，
    #    否则会把任意一张散文表格塞进「语法 / 参数」节。
    if not own and not parts:
        for k, t in enumerate(table_runs(body), 1):
            parts.append((f'Tables（脚本逐字抽取，第 {k} 张）', t))
            srcs.append(rel)

    # ③ 参数表在前、自己的 `Example` 在后：页面读起来是「先查表、再看例」。
    parts += [(n, b) for n, b in own]
    srcs += [rel] * len(own)
    assert len(parts) == len(srcs), '语法段与来源数对不上'
    return parts, srcs


TAIL_HEADS = ('related information', 'functional changes', 'subtopics')


def strip_tail(text):
    """砍掉 `Related information` / `Functional changes` / `Subtopics` 及其后的一切。

    这三段不是语法，是元信息；`Functional changes` 另有 `sections.jsonl` 收着。
    **砍在第一个命中的 H2 上**，不是砍最后一个——命名重复时先出现的先砍，宁少不多。
    """
    lines = text.splitlines()
    i = 0
    if lines and lines[0].strip() == '---':
        i = 1
        while i < len(lines) and lines[i].strip() != '---':
            i += 1
        i += 1
    for j in range(i, len(lines)):
        m = re.match(r'^##\s+(.+?)\s*$', lines[j])
        if m and m.group(1).strip().lower() in TAIL_HEADS:
            return '\n'.join(lines[i:j]).strip()
    return '\n'.join(lines[i:]).strip()


TABLE_ROW = re.compile(r'^\s*\|.*\|\s*$')
TABLE_MIN = 3


def table_runs(text):
    """逐字抽**连续 ≥3 行的管道表格**。

    **为什么要这一层**：`Pogo pad and via design` 通篇没有 `## Syntax` 标题，
    但它的正文里有一张 10 行的设计参数表（L30–L39：信号 pogo via 钻孔尺寸 / 最小 via 长度 /
    相邻接地 via 数 / via 间距 / …）。**那张表就是这一页的「参数」。**
    脚本抽不出来的话，只能我照抄——**那就是 §4 明令不许的手抄参数表。**

    规则窄到不能再窄：**只看连续的 `| … |` 行，少于 3 行不算**。
    这样散文里偶发的一两个竖线不会触发；真表格跑不掉。

    **已知它会漏**：这张表的第一行（`Minimum pad size`）在语料里是坏的——
    HTML 转 markdown 时被拆成了 `| Minimum pad size: |` + 空行 + 建议散文 + 空行 + `|`，
    **不构成连续行**，所以脚本抓不到它，只有下面 10 行被抓到。
    这个缺口**不修**：修它要猜那段散文属于哪一行，**猜就是编**。缺口写在页面上。
    """
    runs, cur = [], []
    for ln in text.splitlines():
        if TABLE_ROW.match(ln):
            cur.append(ln.rstrip())
        else:
            if len(cur) >= TABLE_MIN:
                runs.append('\n'.join(cur))
            cur = []
    if len(cur) >= TABLE_MIN:
        runs.append('\n'.join(cur))
    return runs


BULLET = re.compile(r'^\s*[-*]\s+(.+?)\s*$')
LINKTXT = re.compile(r'^\[([^\]]*)\]\(\s*<?[^)>\s]+>?\s*\)$')
# 参数名的形状：全小写、下划线分隔、长度够。`vout_rise_settling_t_ms_c2c` / `ilimit_sink`。
IDENT = re.compile(r'^[a-z][a-z0-9_]{2,60}$')
IDENT_MIN = 3          # 少于 3 条不算清单
IDENT_RATIO = 0.8      # ≥80% 的条目得是裸标识符，才认作参数清单


def ident_lists(text):
    """找**未加标记的参数清单**：一串 ≥3 条、其中 ≥80% 是裸标识符的列表项。

    **只报告，不收录**——这是这个函数存在的全部意义。

    为什么需要它：`XPS256 programming - DPS operating mode` 全篇没有 `## Syntax`，
    而**它整页的实质就是一张参数清单**（`ilimit_sink` / `vout_fall_t_ms_per_volt_c2c` /
    `open_loop_protection` …，挂在「Level setup overview」下面）。
    抽取器前三层全落空，于是页面上写着「**无**，定义文档里没有语法段」——
    **那句话会把读者引到错的方向**：他会以为这张卡没什么可配的。

    但**不能因此去收录它**：哪些段是「语法」、哪些段只是散文里提了一串名字，
    在没有段标记的情况下**是猜**，而猜就是编（§4）。
    所以这里给出的是**指路**：哪一段、多少条、前几个叫什么——**回 raw 看原样**。

    返回 `[(上文最近的标题行, 条数, [前 3 个例子])]`，按出现顺序。
    """
    out, cur, head = [], [], ''
    lines = text.splitlines()
    for i, ln in enumerate(lines):
        m = BULLET.match(ln)
        if m:
            item = m.group(1)
            lm = LINKTXT.match(item)
            if lm:                      # 列表项是链接时，看**链接文本**是不是标识符
                item = lm.group(1)
            cur.append((item.strip(), i))
            continue
        # 列表断了：结算
        if cur:
            got = _ident_run(cur, lines, head)
            if got:
                out.append(got)
            cur = []
        # 记最近的「标题或冒号结尾的行」当上下文——用来告诉读者**这一段在哪**
        s = ln.strip()
        if s.startswith('#') or s.endswith(':'):
            head = s.lstrip('# ').strip()
    if cur:
        got = _ident_run(cur, lines, head)
        if got:
            out.append(got)
    return out


def _ident_run(cur, lines, head):
    if len(cur) < IDENT_MIN:
        return None
    names = [x[0] for x in cur]
    n_ident = sum(1 for n in names if IDENT.match(n))
    if n_ident < len(names) * IDENT_RATIO:
        return None
    return (head, len(names), names[:3])


def slugify(rel):
    """给包文件起名用，**不是** wiki 的 slug（wiki 的 slug 是 §5 那套，人工定）。"""
    s = Path(rel).stem
    s = re.sub(r'^\d+(\.\d+)*_', '', s)
    s = re.sub(r'[^0-9A-Za-z]+', '-', s).strip('-').lower()
    return s[:48]


def main():
    if (sys.stdout.encoding or '').lower().replace('-', '') != 'utf8':
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    if len(sys.argv) < 2:
        raise SystemExit('用：python objpack.py <batch.txt>')

    rels = [l.strip() for l in (OUT / sys.argv[1]).read_text(encoding='utf-8').splitlines()
            if l.strip() and not l.startswith('#')]
    docs, (outb, inb, drop) = load_docs(), load_edges()
    packdir = OUT / 'pack'
    packdir.mkdir(exist_ok=True)
    print(f'（edges.jsonl 里 {drop} 条非 inline 边未计入——toc 目录边，'
          f'口径同 hubs-dedup.csv）')

    for n, rel in enumerate(rels, 1):
        d = docs.get(rel)
        if not d:
            print(f'❌ 不在 docs.jsonl：{rel}')
            continue
        body = (CORPUS / rel).read_text(encoding='utf-8', errors='replace')

        w = [f'# 建页资料包 {n:02d} — {rel}', '']
        w += ['## 0. 元信息', '',
              f"- 标题（frontmatter）：{(d['frontmatter'] or {}).get('title')}",
              f"- H1：{d['title']}",
              f"- 字节：{d['bytes']}；出度：{d['out_degree']}；入边：{len(inb.get(rel, []))}",
              f"- frontmatter：`{json.dumps(d['frontmatter'] or {}, ensure_ascii=False)}`",
              f"- 标题结构：{' / '.join(h['text'] for h in d['headings'][:40])}", '']

        w += ['## 1. 定义文档全文（raw，禁止修改）', '', '```markdown', body.rstrip(), '```', '']

        v, vsrc = collect_syntax(rel)
        subs = sorted(set(s for s in vsrc if s != rel))
        w += ['## 2. 语法 / 参数段落（脚本逐字抽取，§4 —— 进页面时照抄，不重写）', '']
        if subs:
            w += [f'> ⚠️ 定义文档自己**没有** `Syntax`/`Parameters` 段，'
                  f'以下取自**子主题**：{", ".join(f"`{s}`" for s in subs)}。', '']
        if v:
            for name, b in v:
                w += [f'### 〔{name}〕', '', '```text', b, '```', '']
        else:
            w += ['*（这篇没有 `Syntax`/`Parameters` 这类段落，子主题里也没有——'
                  '那就没有语法可抄，页面不许自己编一个）*', '']

        # 入边：按来源篇聚，一篇一条，带原句。
        # **同一篇引它多次只算一条**——不然「和谁有关」会被「同一篇里反复提」灌水，
        # 正是 index.md 里 `WSUS` 那个坑。
        grp = {}
        for e in inb.get(rel, []):
            grp.setdefault(e['from'], []).append(e)
        w += [f'## 3. 入边 {len(grp)} 篇（谁引它、引它的原句 —— 「和谁有关」的唯一来源）', '']
        if not grp:
            w += ['*（无入边。**那它为什么在候选表里？** 先查清楚再建页。）*', '']
        for f, es in sorted(grp.items(), key=lambda kv: -len(kv[1])):
            fd = docs.get(f, {})
            t = (fd.get('frontmatter') or {}).get('title') or fd.get('title') or Path(f).stem
            w += [f'### ← {t}', f'`{f}`（引 {len(es)} 次）', '']
            for e in es[:4]:
                w += [f"- L{e['line']}：{e['context'].strip()[:300]}"]
            w += ['']

        od = {}
        for e in outb.get(rel, []):
            if e.get('resolved') and e.get('to'):
                od.setdefault(e['to'], e['link_text'])
        w += [f'## 4. 出边 {len(od)} 个（它引谁）', '']
        for t, txt in sorted(od.items()):
            td = docs.get(t, {})
            tt = (td.get('frontmatter') or {}).get('title') or td.get('title') or Path(t).stem
            w += [f'- [[{txt}]] → `{t}`（{tt}）']
        w += ['']

        s = sections_of(rel)
        if s:
            w += ['## 5. 结构段落（Procedure / Dependency / Errors …）', '']
            for x in s:
                t = f"{x.get('group') or ''} {x.get('h2') or ''}".strip() or '（无标题）'
                w += [f'### 〔{t}〕（L{x.get("line")}，{x.get("chars")} 字符'
                      f'{"，已截断" if x.get("truncated") else ""}）', '',
                      (x.get('body') or '')[:2000], '']

        p = packdir / f'{n:02d}-{slugify(rel)}.md'
        p.write_text('\n'.join(w), encoding='utf-8')
        print(f'✅ {p.name}  ({len(inb.get(rel, []))} 入边 / {len(outb.get(rel, []))} 出边)')


if __name__ == '__main__':
    main()
