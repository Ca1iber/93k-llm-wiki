#!/usr/bin/env python3
# extract.py — 从 TDC 语料抽结构数据，产出建 wiki 页的依据
#
# 零 LLM / 零网络 / 零第三方依赖（仅 stdlib）。
#
# 为什么不用并发：语料 26.8 MB，单线程正则解析秒级完成。并发是给网络 I/O 用的，
# 这里没有网络。而且顺序化是「幂等性」检验的前提——并发写入会让行序不可复现。
#
# 输入  F:\master-dev\dorm-wsl-sytest\tdc-html\agent-markdown\
#          by-category\        9,398 篇
#          catalog-markdown.csv  9,393 条（+1 行表头）
# 输出  F:\master-dev\understand-anything-wiki\extract\
#          docs.jsonl      每篇一行
#          edges.jsonl     每条交叉引用一行
#          hubs.csv        入度/出度排名（含「去重来源篇数」in_src——挑 object 页看它）
#          sections.jsonl  结构段落正文
#          failures.jsonl  解析失败 / 异常清单（第五类检验的数据源）

import csv
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import unquote

# ---------------------------------------------------------------- 配置

CORPUS = Path(r'F:\master-dev\dorm-wsl-sytest\tdc-html\agent-markdown\by-category')
CATALOG = CORPUS.parent / 'catalog-markdown.csv'
OUTDIR = Path(r'F:\master-dev\understand-anything-wiki\extract')

CONTEXT_MIN = 20        # 语境句子短于此长度则向上并入前行
CONTEXT_MERGE_MAX = 3   # 最多向上并入几行
CONTEXT_MAX = 300       # 语境句子长度上限
FIRST_PARA_MAX = 300    # 首段长度上限
SECTION_MAX = 6000      # 单个结构段落正文上限

# 结构段落 → 组别。组别直接对应 schema.md §2 的页面类型。
SECTION_GROUPS = {
    'constraint': {'Dependency', 'Dependencies', 'Predependencies', 'Postdependencies',
                   'Dependency and constraints', 'Dependency and Constraints',
                   'Before you begin', 'Prerequisites', 'Preconditions', 'Requirements'},
    'procedure':  {'Procedure', 'Procedures', 'About this task', 'What to do next'},
    'error':      {'Errors', 'Error', 'Warnings', 'Limits'},
    'version':    {'Functional changes'},
    'syntax':     {'Syntax', 'Parameters', 'Return value', 'Return Value',
                   'Prototype', 'Member functions', 'Class definition',
                   'Example', 'Examples'},
    'concept':    {'Mode of operation', 'Application'},
    'related':    {'Related information', 'Further information', 'More Info',
                   'Subtopics'},   # Subtopics 全库 1,693 处，**永远是 H4**，只认 H2 会整段丢
}
SECTION_H2 = {h: g for g, hs in SECTION_GROUPS.items() for h in hs}

# 正则
RE_H = re.compile(r'^(#{1,6})\s+(.+?)\s*$')
RE_FENCE = re.compile(r'^\s*(`{3,}|~{3,})')
# 锚文本允许**一层嵌套方括号**。语料里真实存在这种写法：
#   [Voltage filter[Hz]](<...>)          [TMU_RESULTS.[ ]](<...>)
#   [SWNG, SWNG? - (SWiNG [mV] ...)](<...>)
# 用 [^\]]* 会把它们整条漏掉——`[Hz]](` 有两个连续右括号，正则回溯不过去。
# 这个 bug 是第三类「独立复算」用 markdown-it 抓出来的（B−A = 20 条）。
RE_ANGLE = re.compile(r'\[((?:[^\[\]]|\[[^\[\]]*\])*)\]\(\s*<([^>]+)>\s*\)')
RE_PLAIN = re.compile(r'\[((?:[^\[\]]|\[[^\[\]]*\])*)\]\(\s*([^)<>\s]+\.md)\s*\)')
RE_LIST = re.compile(r'^\s*(?:[-*+]|\d+[.)])\s+')
# 强调符**只在词边界上才是强调**。行内下划线不是强调——
# `../01_Getting_started/01.01_SmarTest_Work_Center/...` 里的 `_` 是路径的一部分。
# 早先用 `[*_`]+` 全局剥离，把 URL 改成了 `../01Gettingstarted/...`，
# 语境是**证据**，把证据改坏比留着标记更糟。第四类抽样核对抓到了这一条。
#
# 已知残留：`02.*` 这类通配写法里的 `*` 仍会被当作强调符剥掉。
# 全库无此写法，故不为此加复杂度。
RE_EMPH = re.compile(r'`+|(?<!\w)\*+|\*+(?!\w)|(?<!\w)_{1,3}|_{1,3}(?!\w)')
# 链接目标 `](<...>)` 是**机器用的路径**，不是给人读的散文，强调剥离必须绕开它。
# `02.06.02.02.281_TSTL__TSTL__-__TeST_Label.md` 里的 `__-__` 恰好满足
# 「下划线紧邻非词字符」，会被上面的式子剥成 `-`，把路径改坏。
# 两种语法都要护：语料主语法 `](<path>)`，和 5 个 index.md 用的 `](path.md)`。
# 只护前者会漏掉 981 条——`1._Create_a_Test_Method_Project.md` 被剥成
# `1.Create_a_Test_Method_Project.md`。
RE_TARGET_PROTECT = re.compile(r'\]\(\s*(?:<[^>]*>|[^)<>\s]+\.md)\s*\)')


def strip_emph(s):
    """剥强调符，但**链接目标原样保留**。"""
    out, last = [], 0
    for m in RE_TARGET_PROTECT.finditer(s):
        out.append(RE_EMPH.sub('', s[last:m.start()]))
        out.append(m.group(0))
        last = m.end()
    out.append(RE_EMPH.sub('', s[last:]))
    return ''.join(out)
RE_FM_KV = re.compile(r'^([A-Za-z_][A-Za-z0-9_]*)\s*:\s*(.*?)\s*$')
RE_SCHEME = re.compile(r'^[A-Za-z][A-Za-z0-9+.\-]*://')

# 非 .md 的已知资源扩展名。**不静默丢弃**——每类都计数并进报告。
ASSET_EXT = {
    '.png', '.jpg', '.jpeg', '.gif', '.svg', '.bmp', '.ico', '.tif', '.tiff',
    '.pdf', '.zip', '.gz', '.tar', '.7z',
    '.htm', '.html', '.xml', '.json', '.csv', '.txt', '.log',
    '.xls', '.xlsx', '.doc', '.docx', '.ppt', '.pptx',
    '.exe', '.dll', '.lib', '.js', '.css',
    '.wav', '.mp3', '.mp4', '.avi', '.mov',
    '.stil', '.wgl', '.evcd', '.vcd', '.stdf', '.atdf',
}

# 只有 target_kind == 'doc' 的链接才是真正的文档交叉引用，才进 edges.jsonl。
# 图片、页内锚点、外部 URL 全部计数但不建边——它们不是「为什么相关」的证据。


def code_span_spans(ln):
    """返回该行内联代码跨度（`...`）覆盖的 [start, end) 区间。

    正文里存在 `` `[gio_open()](<...>)` `` 这种写法——作者用反引号把链接**引用**起来，
    渲染后它不是链接。正则看不出来，markdown-it 看得出来。这是第三类检验抓到的第二类差异。

    这里只做标记，不丢弃：边仍然入 edges.jsonl，打上 in_code_span 供下游过滤。
    """
    spans, i, n = [], 0, len(ln)
    while i < n:
        if ln[i] != '`':
            i += 1
            continue
        j = i
        while j < n and ln[j] == '`':
            j += 1
        ticks = j - i
        k = j
        closed = False
        while k < n:
            if ln[k] == '`':
                m = k
                while m < n and ln[m] == '`':
                    m += 1
                if m - k == ticks:
                    spans.append((i, m))
                    i = m
                    closed = True
                    break
                k = m
            else:
                k += 1
        if not closed:
            i = j
    return spans


def classify_target(raw):
    """链接目标分类：doc / asset / anchor / external / noext。"""
    if raw.startswith('#') or raw.startswith('//'):
        return 'anchor' if raw.startswith('#') else 'external'
    if RE_SCHEME.match(raw):
        return 'external'
    path_part = raw.split('#', 1)[0]
    if not path_part:
        return 'anchor'
    ext = Path(path_part).suffix.lower()
    if ext == '.md':
        return 'doc'
    if ext in ASSET_EXT:
        return 'asset'
    return 'noext' if not ext else 'other'


# ---------------------------------------------------------------- 工具

def walk(root):
    """递归收 *.md，排序返回。

    排序不是可选项——rglob 的顺序取决于文件系统，不排序则两次运行输出不同，
    第六类幂等性检验必然失败。
    """
    return sorted(p for p in root.rglob('*.md') if p.is_file())


def read_text(path):
    """读文件。编码异常不静默吞掉，降级读取并把事实返回给调用方。

    全库是 CRLF。归一化成 LF，否则 \r 会渗进段落正文和语境句子。
    注意：约 11% 的文件带 GBK 误码乱码（`碌`=µ、`鈮`=≥ 等），那是**转换阶段就损坏了**，
    以合法 UTF-8 形式存在，这里解得出来也修不了——属于语料缺陷，记进 wiki，不在这里动。
    """
    raw = path.read_bytes()
    try:
        text = raw.decode('utf-8')
        err = None
    except UnicodeDecodeError as e:
        text = raw.decode('utf-8', errors='replace')
        err = f'utf-8 解码失败: {e}'
    return text.replace('\r\n', '\n').replace('\r', '\n'), err


def clean_context(lines, i):
    """从第 i 行抽语境句子。

    规则写死在计划里，不许临场发挥，因为第四类抽样核对的就是它：
      1. 取链接所在那一行
      2. 剥掉行首列表符与 markdown 强调符
      3. 若结果 < CONTEXT_MIN 字符，向上并入前一行（最多 CONTEXT_MERGE_MAX 行）
      4. 截断到 CONTEXT_MAX
    """
    cur = RE_LIST.sub('', lines[i]).strip()
    j = i
    while len(strip_emph(cur)) < CONTEXT_MIN and j > 0 and (i - j) < CONTEXT_MERGE_MAX:
        j -= 1
        prev = RE_LIST.sub('', lines[j]).strip()
        if prev:
            cur = prev + ' ' + cur
    cur = strip_emph(cur)
    return re.sub(r'\s+', ' ', cur).strip()[:CONTEXT_MAX]


def parse_frontmatter(lines):
    """返回 (frontmatter dict | None, 失败行, 正文起始行号)。"""
    if not lines or lines[0].strip() != '---':
        return None, [], 0
    end = None
    for i in range(1, min(len(lines), 200)):
        if lines[i].strip() == '---':
            end = i
            break
    if end is None:
        return None, ['<frontmatter 起始 --- 未闭合>'], 0

    fm, fails = {}, []
    for raw in lines[1:end]:
        s = raw.strip()
        if not s or s.startswith('#'):
            continue
        m = RE_FM_KV.match(s)
        if not m:
            fails.append(raw)
            continue
        k, v = m.group(1), m.group(2)
        if len(v) >= 2 and v[0] == v[-1] and v[0] in '"\'':
            v = v[1:-1]
        fm[k] = v
    return fm, fails, end + 1


# ---------------------------------------------------------------- 单篇解析

def parse_doc(path, corpus_root, is_catalogued):
    """一篇 → dict + 边列表 + 段落列表 + 失败列表。"""
    rel = path.relative_to(corpus_root).as_posix()
    text, decode_err = read_text(path)
    lines = text.split('\n')
    is_index = path.name == 'index.md'

    fm, fm_fails, body_start = parse_frontmatter(lines)

    headings = []
    title = None
    edges = []
    sections = []
    failures = []
    link_kinds = Counter()
    angle_hits = plain_hits = 0
    code_blocks = 0
    first_para = None

    in_fence = False
    fence_char = None
    cur_h2 = cur_group = cur_line = None
    cur_level = 99
    cur_body = []

    def close_section():
        # 只收 SECTION_H2 里列出的段落。收全库每一个标题会把 sections.jsonl
        # 灌进几千条与建页无关的噪声（实测多出 6,527 条 group=None）。
        # 幂等：没有打开中的段落时是空操作。
        nonlocal cur_body, cur_h2, cur_group, cur_level
        if cur_h2 is not None and cur_group is not None:
            body = '\n'.join(cur_body).strip()
            if body:
                sections.append({
                    'doc': rel, 'h2': cur_h2, 'group': cur_group,
                    'level': cur_level,
                    'line': cur_line, 'chars': len(body),
                    'truncated': len(body) > SECTION_MAX,
                    'body': body[:SECTION_MAX],
                })
        cur_h2 = cur_group = None
        cur_level = 99
        cur_body = []

    if decode_err:
        failures.append({'doc': rel, 'kind': 'decode_error', 'detail': decode_err})
    if fm is None:
        failures.append({'doc': rel, 'kind': 'no_frontmatter',
                         'detail': '文件首行不是 ---'})
    if not is_catalogued:
        failures.append({'doc': rel, 'kind': 'not_in_catalog', 'detail': ''})
    for bad in fm_fails:
        failures.append({'doc': rel, 'kind': 'fm_parse_failure', 'detail': bad})

    for i in range(body_start, len(lines)):
        ln = lines[i]

        # --- 围栏必须挡在标题和链接之前：代码块里的 # 和 [x](y.md) 是最大的假阳性来源
        mf = RE_FENCE.match(ln)
        if in_fence:
            if mf and mf.group(1)[0] == fence_char:
                in_fence = False
            if cur_h2 is not None:
                cur_body.append(ln)
            continue
        if mf:
            in_fence = True
            fence_char = mf.group(1)[0]
            code_blocks += 1
            if cur_h2 is not None:
                cur_body.append(ln)
            continue

        # --- 标题
        mh = RE_H.match(ln)
        if mh:
            level = len(mh.group(1))
            htext = mh.group(2)
            headings.append({'level': level, 'text': htext, 'line': i + 1})
            if level == 1 and title is None:
                title = htext
            # 段落按**层级**关闭，不按固定 H2：H3 及以上属于当前段落，同级或更高级才关闭。
            if cur_h2 is not None and level <= cur_level:
                close_section()
            if htext in SECTION_H2:
                close_section()   # 若仍开着（被更低级别标题嵌套），先收尾
                cur_h2 = htext
                cur_group = SECTION_H2[htext]
                cur_level = level
                cur_line = i + 1
            elif cur_h2 is not None:
                # 段落**内**的子标题要留在正文里。原先一律不入正文，后果是
                # `## Procedures` 下 `### Creating a new workspace` /
                # `### Opening an existing workspace` / `### Switching to another workspace`
                # 三段的**标题全丢**，正文糊成一段分不清哪句属于哪步——
                # 而这三行标题正是这三段唯一的语义标签。第四类附的段落正文回验
                # （穷举 23,315 条，840 条对不上）抓到的就是这一条。
                cur_body.append(ln)
            # 其余标题行不进正文段，但**不能就此 continue**——标题里可能嵌链接。
            # 实测 5 例，例如 `# class [FPGA](<../.../FPGA.md>) All Members`。
        else:
            if cur_h2 is not None:
                cur_body.append(ln)
            if first_para is None and ln.strip() and not ln.strip().startswith(('|', '>', '    ')):
                first_para = ln.strip()[:FIRST_PARA_MAX]

        # --- 链接：先 ANGLE，再 PLAIN，按 span 去重。
        #     只把 .md 目标当交叉引用；其余按类型计数（见 classify_target）。
        cs = code_span_spans(ln)

        def in_code_span(m):
            return any(m.start() >= s and m.end() <= e for s, e in cs)

        angle_spans = []
        for m in RE_ANGLE.finditer(ln):
            angle_spans.append((m.start(), m.end()))
            angle_hits += 1
            raw = m.group(2)
            tk = classify_target(raw)
            link_kinds[tk] += 1
            if tk == 'doc':
                edges.append((m.group(1), raw, i + 1, in_code_span(m)))
        for m in RE_PLAIN.finditer(ln):
            if any(m.start() >= s and m.end() <= e for s, e in angle_spans):
                continue
            plain_hits += 1
            raw = m.group(2)
            tk = classify_target(raw)
            link_kinds[tk] += 1
            if tk == 'doc':
                edges.append((m.group(1), raw, i + 1, in_code_span(m)))

    close_section()
    if in_fence:
        failures.append({'doc': rel, 'kind': 'unclosed_fence',
                         'detail': f'第 {len(lines)} 行仍未闭合'})
    if not headings:
        failures.append({'doc': rel, 'kind': 'no_headings', 'detail': ''})
    elif title is None:
        failures.append({'doc': rel, 'kind': 'no_h1', 'detail': ''})

    # --- 解析边的目标路径
    edge_rows = []
    for link_text, raw_to, line_no, in_cs in edges:
        # 剥掉 #锚点再解析。语料里存在 `foo.md#_107991__task_bar` 这种写法，
        # 不剥就会把真链接误判成悬空。
        path_part, _, anchor = raw_to.partition('#')
        target = None
        for cand in (path_part, unquote(path_part)):
            try:
                t = (path.parent / cand).resolve()
            except (OSError, ValueError):
                continue
            if t.is_file():
                target = t
                break
        resolved = target is not None
        try:
            to_rel = target.relative_to(corpus_root.resolve()).as_posix() if resolved else None
        except ValueError:
            to_rel, resolved = None, False

        if not resolved:
            failures.append({'doc': rel, 'kind': 'dangling_link',
                             'detail': f'line {line_no}: {raw_to}'})

        edge_rows.append({
            'from': rel,
            'to': to_rel,
            'to_raw': raw_to,
            'anchor': anchor or None,
            'resolved': resolved,
            'kind': 'toc' if is_index else 'inline',
            'in_code_span': in_cs,
            'line': line_no,
            'link_text': link_text,
            'context': clean_context(lines, line_no - 1),
        })

    doc = {
        'rel': rel,
        # 原始文件大小（CRLF 未归一化）。用 stat 而不是 len(text)，否则和 `find -printf %s` 对不上。
        'bytes': path.stat().st_size,
        'chars': len(text),
        'is_index': is_index,
        'in_catalog': is_catalogued,
        'frontmatter': fm,
        'title': title,
        'headings': headings,
        'heading_count': len(headings),
        'first_para': first_para,
        'code_blocks': code_blocks,
        'out_degree': len(edge_rows),
        'edge_angle': angle_hits,
        'edge_plain': plain_hits,
        'link_kinds': dict(link_kinds),
        'struct_sections': sorted({s['h2'] for s in sections}),
        'struct_groups': sorted({s['group'] for s in sections if s['group']}),
    }
    return doc, edge_rows, sections, failures


# ---------------------------------------------------------------- 主流程

def main():
    # Windows 控制台默认 GBK，中文输出会花屏
    if (sys.stdout.encoding or '').lower().replace('-', '') != 'utf8':
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')

    if not CORPUS.is_dir():
        sys.exit(f'语料目录不存在: {CORPUS}')
    OUTDIR.mkdir(parents=True, exist_ok=True)

    catalogued = set()
    if CATALOG.is_file():
        with open(CATALOG, encoding='utf-8-sig', newline='') as f:
            for row in csv.DictReader(f):
                p = (row.get('MarkdownPath') or '').strip()
                if p:
                    # catalog 里写的是 `by-category/00_Overview/...`，
                    # 而 rel 是相对 by-category 的 `00_Overview/...`。不剥前缀会全表失配。
                    catalogued.add(p.removeprefix('by-category/'))
    print(f'catalog: {len(catalogued)} 条')

    files = walk(CORPUS)
    print(f'扫描到 {len(files)} 篇 markdown')

    docs, all_edges, all_sections, all_failures = [], [], [], []
    for n, p in enumerate(files, 1):
        rel = p.relative_to(CORPUS).as_posix()
        d, e, s, f = parse_doc(p, CORPUS, rel in catalogued)
        docs.append(d)
        all_edges.extend(e)
        all_sections.extend(s)
        all_failures.extend(f)
        if n % 1000 == 0:
            print(f'  ... {n}/{len(files)}')

    # 入度：分「全部链接」与「仅正文链接」两套
    #
    # 另算第三套：**有多少篇不同的文档引用了它**（`src_inline`）。
    # 这不是前两套的变体，是另一个量纲，而且挑 object 页只能用这一套：
    # 出现次数会被「同一篇里反复提到」灌水——实测 `Error_handling` 163 次只来自 9 篇，
    # `DPSPINS_resources` 286 次来自 54 篇；而 `PSFC` 130 次来自 115 篇。
    # 按次数排的前 20 与按来源篇数排的前 20 **一篇都不重合**。
    # 「这个对象在语料里有多通用」问的是后者。
    in_all, in_inline = Counter(), Counter()
    src_inline = defaultdict(set)
    for e in all_edges:
        if e['resolved']:
            in_all[e['to']] += 1
            if e['kind'] == 'inline':
                in_inline[e['to']] += 1
                src_inline[e['to']].add(e['from'])

    def dump_jsonl(name, rows):
        with open(OUTDIR / name, 'w', encoding='utf-8', newline='\n') as f:
            for r in rows:
                f.write(json.dumps(r, ensure_ascii=False, sort_keys=True) + '\n')

    dump_jsonl('docs.jsonl', docs)
    dump_jsonl('edges.jsonl', all_edges)
    dump_jsonl('sections.jsonl', all_sections)
    dump_jsonl('failures.jsonl', all_failures)

    # 排序按 `in_src`（去重来源篇数）——这是「通用度」，也是挑 object 页的口径。
    # 并列时依次看 `in_inline`、`rel`，保证全序 → 第六类幂等性的前提。
    with open(OUTDIR / 'hubs.csv', 'w', encoding='utf-8', newline='\n') as f:
        f.write('path,in_all,in_inline,in_src,out,is_index\n')
        for d in sorted(docs, key=lambda x: (-len(src_inline[x['rel']]),
                                             -in_inline[x['rel']], x['rel'])):
            f.write(f"{d['rel']},{in_all[d['rel']]},{in_inline[d['rel']]},"
                    f"{len(src_inline[d['rel']])},"
                    f"{d['out_degree']},{int(d['is_index'])}\n")

    n_res = sum(1 for e in all_edges if e['resolved'])
    kinds = Counter()
    for d in docs:
        kinds.update(d['link_kinds'])
    print()
    print(f'docs.jsonl      {len(docs)} 行')
    print(f'edges.jsonl     {len(all_edges)} 行  (解析成功 {n_res} / 悬空 {len(all_edges)-n_res})')
    print(f'sections.jsonl  {len(all_sections)} 行')
    print(f'failures.jsonl  {len(all_failures)} 行')
    print(f'hubs.csv        {len(docs)} 行')
    print()
    print(f'全部链接 {sum(kinds.values())} 条，按目标类型:')
    for k, v in kinds.most_common():
        print(f'  {v:6d}  {k}')
    print()
    print('失败类型分布:')
    for k, v in Counter(x['kind'] for x in all_failures).most_common():
        print(f'  {v:6d}  {k}')
    print()
    print('段落组别分布:')
    for k, v in Counter(s['group'] for s in all_sections).most_common():
        print(f'  {v:6d}  {k}')
    print()
    print('入度前 15（按**出现次数**，仅正文链接）:')
    for r, c in in_inline.most_common(15):
        print(f'  {c:4d} 次 / {len(src_inline[r]):3d} 篇  {r}')
    print()
    print('入度前 15（按**去重来源篇数**，仅正文链接）:')
    for r, s in sorted(src_inline.items(), key=lambda kv: (-len(kv[1]), kv[0]))[:15]:
        print(f'  {len(s):4d} 篇 / {in_inline[r]:3d} 次  {r}')
    print(f'\nDONE -> {OUTDIR}')


if __name__ == '__main__':
    main()
