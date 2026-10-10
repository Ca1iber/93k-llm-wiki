#!/usr/bin/env python -X utf8
# -*- coding: utf-8 -*-
"""表格指针化 —— 把 md 里的表格换成指向上游 HTML 的指针。

用法：
    python -X utf8 extract/tabledel.py            # 空跑：只扫、只报数、只出清单
    python -X utf8 extract/tabledel.py --apply    # 真改

设计要点（见 extract/PLAN-表格指针化.md）：
  · **上游数表，不在 md 里找表**（md 侧压平的表没有任何标记）
  · **唯一命中**才动，分不清就整张不动
  · 指针文字全部是「固定措辞 + 上游照抄」，**没有一句是自撰的**
"""
import io, os, re, sys, json, hashlib, html, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TDC  = r"F:\master-dev\dorm-wsl-sytest\tdc-html"
HTM  = os.path.join(TDC, "raw")
MD   = os.path.join(TDC, "agent-markdown", "by-category")

MARK = "⚠️ 表格指针（非原文）"          # 幂等判据：已有指针的就跳过
MIN_TEXT = 3                             # 「空壳」阈值（人已确认）


# ---------------------------------------------------------------- 通用

def read(p, newline=''):
    return io.open(p, encoding='utf-8', errors='replace', newline=newline).read()


def norm(s):
    """比对用的归一化：小写、去标签、去 markdown 语法、**只留 ASCII 字母数字**。
    只留 ASCII 是为了对乱码免疫（`≤` 与 `鈮?` 都变成空）。"""
    s = re.sub(r'<[^>]+>', '', s)
    s = html.unescape(s)
    s = re.sub(r'!?\[([^\]]*)\]\(<[^>]*>\)', r'\1', s)   # md 链接/图片 → 链接文字
    s = s.replace('`', '').replace('\\|', '|').replace('|', ' ')
    return re.sub(r'[^0-9a-z]+', '', s.lower())


def sig(cells):
    """一张表的「内容签名」：去重后的格子文字集合。对合并格展开免疫。"""
    u = sorted({norm(c) for c in cells if norm(c)})
    return hashlib.sha1(('\x1f'.join(u)).encode('utf-8')).hexdigest()[:16]


# ---------------------------------------------------------------- 上游

def upstream_tables(h):
    """所有 <table>（含嵌套）→ [(tag, start, end)]"""
    out = []; i = 0
    while True:
        m = re.search(r'<table\b[^>]*>', h[i:])
        if not m: break
        st = i + m.start(); depth = 0; j = m.end() + i
        while j < len(h):
            nm = re.search(r'</?table\b', h[j:])
            if not nm: break
            j2 = j + nm.start()
            if h[j2:j2 + 7].lower() == '</table':
                if depth == 0: j = j2 + 8; break
                depth -= 1
            else: depth += 1
            j = j2 + 6
        out.append((m.group(0), st, j)); i = m.end() + i
    return out


def up_cells(seg):
    """一张表的格子文字（含所有嵌套格）"""
    return [html.unescape(re.sub(r'<[^>]+>', '', c))
            for c in re.findall(r'<t[dh]\b[^>]*>(.*?)</t[dh]>', seg, re.S)]


def up_dim(seg):
    rows = re.findall(r'<tr\b[^>]*>(.*?)</tr>', seg, re.S)
    ncol = len(re.findall(r'<col\b', seg))
    if not ncol:
        dims = [len(re.findall(r'<t[dh]\b', r)) for r in rows]
        ncol = max(dims) if dims else 0
    return len(rows), ncol


def first_row_text(seg, ncol):
    """上游第一行原文（供搜索）。多个格用 ' | ' 接。"""
    m = re.search(r'<tr\b[^>]*>(.*?)</tr>', seg, re.S)
    if not m: return ''
    cs = [re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', c))).strip()
          for c in re.findall(r'<t[dh]\b[^>]*>(.*?)</t[dh]>', m.group(1), re.S)]
    cs = [c for c in cs if c]
    if not cs: return ''
    out = ' | '.join(cs)
    return out[:160] + ('…' if len(out) > 160 else '')


def has_nested(tag, seg):
    return bool(re.search(r'<table\b', seg[len(tag):]))


def enumerate_upstream():
    """→ {(topic, idx): {...}}，idx 只数内容表（有格子且 ≥3 字符）"""
    out = {}
    for fn in sorted(os.listdir(HTM)):
        if not fn.lower().endswith(('.htm', '.html')): continue
        h = read(os.path.join(HTM, fn))
        k = 0
        for tag, st, en in upstream_tables(h):
            seg = h[st:en]
            cs = up_cells(seg)
            if not cs or len(norm(''.join(cs))) < MIN_TEXT: continue      # 空壳
            R, C = up_dim(seg)
            out[(fn, k)] = dict(topic=fn, idx=k, tag=tag,
                                R=R, C=C, sig=sig(cs),
                                first=first_row_text(seg, C),
                                nested=has_nested(tag, seg))
            k += 1
    return out


# ---------------------------------------------------------------- md 侧

MD_ROW = re.compile(r'^\s*\|.*\|\s*$')
MD_SEP = re.compile(r'^\s*\|[\s:\-|]+\|\s*$')


def md_blocks(text):
    """md 里所有「表形态」的区域 → [(kind, start_line, end_line)]，行号闭开区间。
    kind: 'table' = 正常 markdown 表块；'flat' = 压平残片（行首 ' | '）。"""
    lines = text.split('\n'); out = []; i = 0
    while i < len(lines):
        if lines[i].startswith(' | '):                       # 压平残片
            j = i
            while j < len(lines) and (lines[j].startswith(' | ') or not lines[j].strip()):
                j += 1
            while j > i and not lines[j - 1].strip(): j -= 1   # 收尾去掉空行
            out.append(('flat', i, j)); i = j
        elif MD_ROW.match(lines[i]):                          # 正常表块
            j = i
            while j < len(lines) and MD_ROW.match(lines[j]): j += 1
            if any(MD_SEP.match(l) for l in lines[i:j]):
                out.append(('table', i, j))
            i = j
        else:
            i += 1
    return out


def block_cells(lines, kind, a, b):
    seg = '\n'.join(lines[a:b])
    if kind == 'flat':
        cells = []
        for l in lines[a:b]:
            if not l.strip(): continue
            cells += [c for c in l.strip().strip('|').split('|')]
    else:
        cells = []
        for l in lines[a:b]:
            if MD_SEP.match(l): continue
            cells += [c for c in l.strip().strip('|').split('|')]
    return [c.strip() for c in cells if c.strip()]


def build_md_index():
    """→ md_blocks_by_file: {md_path: [(kind,a,b,sig)]}"""
    idx = {}
    for dp, _, fns in os.walk(MD):
        for fn in fns:
            if not fn.endswith('.md'): continue
            p = os.path.join(dp, fn)
            text = read(p)
            lines = text.split('\n')
            bl = []
            for kind, a, b in md_blocks(text):
                cs = block_cells(lines, kind, a, b)
                if not cs: continue
                bl.append((kind, a, b, sig(cs), len(cs)))
            if bl: idx[p] = bl
    return idx


# ---------------------------------------------------------------- 扫覆盖

def topic_to_md():
    """md 文件 → source_topic（以及反查）"""
    f2t, t2f = {}, {}
    for dp, _, fns in os.walk(MD):
        for fn in fns:
            if not fn.endswith('.md'): continue
            p = os.path.join(dp, fn)
            m = re.search(r'source_topic:\s*"([^"]+)"', read(p))
            if m:
                f2t[p] = m.group(1); t2f.setdefault(m.group(1), []).append(p)
    return f2t, t2f


def scan():
    up = enumerate_upstream()
    print(f"上游内容表            : {len(up)}")
    mdidx = build_md_index()
    nblk = sum(len(v) for v in mdidx.values())
    print(f"md 侧表形态区域        : {nblk}  （分布在 {len(mdidx)} 篇）")

    # sig → [(md, kind, a, b)]
    bysig = collections.defaultdict(list)
    for p, bl in mdidx.items():
        for kind, a, b, sg, nc in bl:
            bysig[sg].append((p, kind, a, b))

    f2t, t2f = topic_to_md()
    located = []; exc = []
    for key, t in sorted(up.items()):
        mds = t2f.get(t['topic'], [])
        if not mds:
            exc.append((key, '无对应 md', t)); continue
        cands = []
        for p in mds:
            for (mp, kind, a, b) in bysig.get(t['sig'], []):
                if mp == p: cands.append((p, kind, a, b))
        if len(cands) == 1:
            located.append((key, t, cands[0]))
        elif not cands:
            exc.append((key, 'md 里找不到对应的表形态', t))
        else:
            exc.append((key, f'md 里命中 {len(cands)} 处（不唯一）', t))

    used = {(p, a, b) for _, _, (p, kind, a, b) in located}
    orphan = [(p, k, a, b) for p, bl in mdidx.items() for (k, a, b, sg, nc) in bl
              if (p, a, b) not in used]

    print()
    print(f"★ 已定位（唯一命中）   : {len(located)}")
    print(f"★ 例外                : {len(exc)}")
    c = collections.Counter(r for _, r, _ in exc)
    for r, n in c.most_common(): print(f"     {n:5}  {r}")
    print(f"★ md 侧多出来的区域    : {len(orphan)}   ← 反查不回去")
    co = collections.Counter(k for _, k, _, _ in orphan)
    print(f"     {dict(co)}")

    out = {'located': len(located), 'exception': len(exc), 'orphan': len(orphan)}
    with io.open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                              '_scan_summary.json'), 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    return located, exc, orphan


if __name__ == '__main__':
    if '--scan' in sys.argv or len(sys.argv) == 1:
        scan()


# ------------------------------------------------- L2：用上游格子文字框范围

def locate_by_cells(lines, cells):
    """拿上游格子的文字去 md 里框出这张表占的行区间。
    要求：特征格（归一化后 ≥4 字符）多数命中，且区间里确实有 ' | ' 行。"""
    nl = [norm(l) for l in lines]
    targets = [norm(c) for c in cells if len(norm(c)) >= 4]
    if len(targets) < 2: return None
    uniq = collections.Counter(targets)
    pos = []
    for t in uniq:
        hit = [i for i, l in enumerate(nl) if t and t in l]
        if len(hit) == 1: pos.append(hit[0])
    need = max(2, int(len(uniq) * 0.6))
    if len(pos) < need: return None
    a, b = min(pos), max(pos) + 1
    # 向上/向下吃掉相邻的 ' | ' 行与空行
    while a > 0 and (lines[a - 1].startswith(' | ') or not lines[a - 1].strip()): a -= 1
    while b < len(lines) and (lines[b].startswith(' | ') or not lines[b].strip()): b += 1
    seg = '\n'.join(lines[a:b])
    if ' | ' not in seg and not MD_ROW.match(lines[a]): return None
    # 复核：区间内应包含绝大多数特征格
    ns = norm(seg)
    if sum(1 for t in uniq if t in ns) < int(len(uniq) * 0.7): return None
    return a, b


def scan2():
    up = enumerate_upstream()
    f2t, t2f = topic_to_md()
    lines_cache = {}
    def L(p):
        if p not in lines_cache: lines_cache[p] = read(p).replace('\r\n', '\n').split('\n')
        return lines_cache[p]

    l1 = 0; l2 = 0; exc = []
    for key, t in sorted(up.items()):
        mds = t2f.get(t['topic'], [])
        if not mds:
            exc.append((key, '无对应 md', t)); continue
        # L1：正常 markdown 表块，按内容签名唯一命中
        hit = None
        for p in mds:
            bl = [b for b in md_blocks('\n'.join(L(p))) if b[0] == 'table']
            cand = [b for b in bl if sig(block_cells(L(p), 'table', b[1], b[2])) == t['sig']]
            if len(cand) == 1: hit = (p, cand[0][1], cand[0][2]); break
        if hit:
            l1 += 1; t['how'] = ('L1', hit); continue
        # L2：用格子文字框
        got = None
        for p in mds:
            r = locate_by_cells(L(p), up_cells_of(t))
            if r: got = (p, r[0], r[1]); break
        if got:
            l2 += 1; t['how'] = ('L2', got); continue
        exc.append((key, 'L1/L2 都没定位到', t))

    print(f"上游内容表          : {len(up)}")
    print(f"  L1 正常表块命中    : {l1}")
    print(f"  L2 格子文字框到    : {l2}")
    print(f"  ★ 仍定位不到        : {len(exc)}")
    c = collections.Counter(r for _, r, _ in exc)
    for r, n in c.most_common(): print(f"       {n:5}  {r}")
    return up, exc


_CELLS_CACHE = {}
def up_cells_of(t):
    k = (t['topic'], t['idx'])
    if k not in _CELLS_CACHE:
        h = read(os.path.join(HTM, t['topic']))
        n = 0
        for tag, st, en in upstream_tables(h):
            seg = h[st:en]; cs = up_cells(seg)
            if not cs or len(norm(''.join(cs))) < MIN_TEXT: continue
            if n == t['idx']:
                _CELLS_CACHE[k] = cs; break
            n += 1
    return _CELLS_CACHE.get(k, [])


# ------------------------------------------------- L3：用已有的指针文字定位

def load_ledger():
    led = {}
    for name in ['_assign_tables.json','_assign_tables_merged.json','_assign_tables_v2.json',
                 '_assign_ptr.json','_assign_ptr2.json']:
        d = json.load(io.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), name),
                              encoding='utf-8'))
        items = d if isinstance(d, list) else d.get('items', d)
        for e in items:
            t = e['topic']
            if not t.endswith(('.htm', '.html')): t += '.htm'
            led[(t, int(e['tbl']))] = e
    return led


def locate_by_pointer(text, entry):
    """已有指针的：用【整段】指针文字定位，不能用第一行 ——
    同一文件里所有指针的第一行完全相同（只有『第 N 个』那句不同）。
    实测：只用第一行会把 9 张表全指到同一行。"""
    ptr = entry.get('new', '')
    if not ptr or MARK not in ptr: return None
    tn = text.replace('\r\n', '\n')
    # 先试整段（去掉首尾空白、按行 strip 后拼接，抗缩进差异）
    key = '\n'.join(l.strip() for l in ptr.replace('\r\n', '\n').strip().split('\n') if l.strip())
    lines = tn.split('\n')
    keylines = key.split('\n')
    for i in range(len(lines) - len(keylines) + 1):
        if all(lines[i + k].strip() == keylines[k] for k in range(len(keylines))):
            return i
    return None


def scan3():
    up = enumerate_upstream()
    led = load_ledger()
    f2t, t2f = topic_to_md()
    LC = {}
    def L(p):
        if p not in LC: LC[p] = read(p).replace('\r\n', '\n').split('\n')
        return LC[p]

    stat = collections.Counter(); exc = []
    for key, t in sorted(up.items()):
        mds = t2f.get(t['topic'], [])
        if not mds:
            stat['无对应 md'] += 1; exc.append((key, '无对应 md', t)); continue
        # L3 优先：台账里有指针的，先用指针文字定位
        e = led.get((t['topic'], t['idx']))
        if e and e.get('new', '').find(MARK) >= 0:
            for p in mds:
                ln = locate_by_pointer(read(p), e)
                if ln is not None:
                    r = locate_by_cells(L(p), up_cells_of(t))
                    if r: stat['L3 指针+格子框'] += 1
                    else:  stat['L3 只找到指针'] += 1
                    t['how'] = ('L3', (p, ln, r)); break
            else:
                stat['L3 指针文字不在 md 里'] += 1; exc.append((key, '指针文字不在 md 里', t))
            continue
        # L1
        hit = None
        for p in mds:
            for kind, a, b in md_blocks('\n'.join(L(p))):
                if kind != 'table': continue
                if sig(block_cells(L(p), 'table', a, b)) == t['sig']: hit = (p, a, b); break
            if hit: break
        if hit: stat['L1 正常表块'] += 1; t['how'] = ('L1', hit); continue
        # L2
        got = None
        for p in mds:
            r = locate_by_cells(L(p), up_cells_of(t))
            if r: got = (p, r[0], r[1]); break
        if got: stat['L2 格子框'] += 1; t['how'] = ('L2', got); continue
        stat['★ 都没定位到'] += 1; exc.append((key, '都没定位到', t))

    print(f"上游内容表 {len(up)}")
    for k, v in stat.most_common(): print(f"  {k:22} {v}")
    return up, exc


# --------------------------------------- 已知指针位置时，框出压平区的范围

def flat_region(lines, ln, cells):
    """从指针那行往后，吃掉：空行 / ' | ' 行 / 内容能在上游格子里找到的段落。
    返回 (起, 止) 行号；判据是「这段文字属于这张表」。"""
    cn = {norm(c) for c in cells if len(norm(c)) >= 4}
    # 先跳过指针块本身（连续的 '>' 行）
    j = ln
    while j < len(lines) and (lines[j].startswith('>') or not lines[j].strip()): j += 1
    a = j
    while j < len(lines):
        l = lines[j]
        if not l.strip() or l.startswith(' | '): j += 1; continue
        if l.startswith('>') or l.startswith('#'): break
        k = j
        while k < len(lines) and lines[k].strip() and not lines[k].startswith('>') \
              and not lines[k].startswith('#'): k += 1
        para = norm('\n'.join(lines[j:k]))
        if len(para) >= 4 and any(para in c or (len(c) >= 8 and c in para) for c in cn):
            j = k; continue
        break
    while j > a and not lines[j - 1].strip(): j -= 1
    return (a, j) if j > a else None


def scan4():
    up = enumerate_upstream()
    led = load_ledger()
    f2t, t2f = topic_to_md()
    LC = {}
    def L(p):
        if p not in LC: LC[p] = read(p).replace('\r\n', '\n').split('\n')
        return LC[p]

    stat = collections.Counter(); exc = []; plan = []
    for key, t in sorted(up.items()):
        mds = t2f.get(t['topic'], [])
        if not mds:
            stat['无对应 md'] += 1; exc.append((key, t, '无对应 md')); continue
        e = led.get((t['topic'], t['idx']))
        cells = up_cells_of(t)
        # L3：已有指针
        if e and MARK in e.get('new', ''):
            done = False
            for p in mds:
                ln = locate_by_pointer(read(p), e)
                if ln is None: continue
                r = flat_region(L(p), ln, cells)
                if r: plan.append((key, t, p, r, 'L3', ln)); stat['L3 指针+框出'] += 1
                else: plan.append((key, t, p, (ln, ln + 1), 'L3-窄', ln)); stat['L3 只有指针行'] += 1
                done = True; break
            if not done: stat['★ 指针文字不在 md'] += 1; exc.append((key, t, '指针不在 md'))
            continue
        # L1
        hit = None
        for p in mds:
            for kind, a, b in md_blocks('\n'.join(L(p))):
                if kind == 'table' and sig(block_cells(L(p), 'table', a, b)) == t['sig']:
                    hit = (p, a, b); break
            if hit: break
        if hit: plan.append((key, t, hit[0], (hit[1], hit[2]), 'L1', None)); stat['L1'] += 1; continue
        # L2
        got = None
        for p in mds:
            r = locate_by_cells(L(p), cells)
            if r: got = (p, r[0], r[1]); break
        if got: plan.append((key, t, got[0], (got[1], got[2]), 'L2', None)); stat['L2'] += 1; continue
        stat['★ 定位不到'] += 1; exc.append((key, t, '定位不到'))

    print(f"上游内容表 {len(up)}")
    for k, v in stat.most_common(): print(f"  {k:20} {v}")
    print(f"\n可改 {len(plan)}  /  例外 {len(exc)}")
    return up, plan, exc


# ------------------------------ 修订：先找第一个 ' | ' 行（或往后扫），再框范围

def flat_region2(lines, ln, cells, kind=''):
    cn = {norm(c) for c in cells if len(norm(c)) >= 4}
    back = ('表后' in kind) or ('插在块下方' in kind)

    def eat(start, step):
        """从 start 出发，沿 step 方向吃：空行 / ' | ' 行 / 命中上游格子的段落"""
        j = start; got = 0
        while 0 <= j < len(lines):
            l = lines[j]
            if not l.strip():
                j += step; continue
            if l.startswith(' | '):
                j += step; got += 1; continue
            if l.startswith('>') or l.startswith('#'): break
            k = j
            while 0 <= k < len(lines) and lines[k].strip() and not lines[k].startswith('>') \
                  and not lines[k].startswith('#'):
                k += step
            lo, hi = (k + 1, j + 1) if step < 0 else (j, k)
            para = norm('\n'.join(lines[lo:hi]))
            if len(para) >= 4 and any(para in c or (len(c) >= 8 and c in para) for c in cn):
                j = k + step; got += 1; continue
            break
        return j, got

    # 指针块之后（或之前）的第一个 ' | ' 行
    start = None
    rng = range(ln, min(len(lines), ln + 40)) if not back else range(ln, max(-1, ln - 40), -1)
    cnt = 0
    for j in rng:
        if lines[j].startswith(' | '): start = j; break
        cnt += 1
        if cnt > 40: break
    if start is None: return None
    step = -1 if back else 1
    j, got = eat(start, step)
    if got < 2: return None
    a, b = (min(start, j + 1), max(start, j + 1))
    if step < 0: a, b = min(j, start + 1), max(j, start + 1)
    while a > 0 and not lines[a - 1].strip(): a -= 1
    while b < len(lines) and not lines[b].strip(): b += 1
    return a, b


# ------------------------------ 结构法：把 ' | ' 行按间隔聚成「压平区」

def flat_clusters(lines, gap=10):
    """' | ' 行之间间隔 ≤ gap 的算同一区；区间内夹的段落一并纳入。
    返回 [(起, 止)]（止为开区间）。"""
    pos = [i for i, l in enumerate(lines) if l.startswith(' | ') or l.rstrip() == ' |']
    if not pos: return []
    groups = []; cur = [pos[0]]
    for p in pos[1:]:
        if p - cur[-1] <= gap: cur.append(p)
        else: groups.append(cur); cur = [p]
    groups.append(cur)
    out = []
    for g in groups:
        a, b = g[0], g[-1] + 1
        # 收尾：把紧跟的空行也算进去；遇到标题就停
        while b < len(lines) and (not lines[b].strip() or lines[b].startswith(' | ')):
            b += 1
        out.append((a, b))
    return out


def scan5():
    up = enumerate_upstream()
    f2t, t2f = topic_to_md()
    # 只处理「md 侧有压平区」的文件
    files = set()
    for key, t in up.items():
        for p in t2f.get(t['topic'], []): files.add(p)
    print(f"相关 md 文件 {len(files)}")
    nclu = 0; nline = 0
    for p in files:
        L = read(p).replace('\r\n', '\n').split('\n')
        for a, b in flat_clusters(L):
            nclu += 1; nline += b - a
    print(f"结构法聚出的压平区 : {nclu} 个，共 {nline} 行")
    return files


# ---------------------------------------------------------------- 生成指针

LINK_RE = re.compile(r'(!?)\[([^\]]*)\]\(<([^>]+)>\)')


def table_links(lines, a, b):
    """表内的链接（**不含图片**）。§七①：删表会砍边，必须原样搬到指针块里。
    它们是原文（链接文字 + 目标都是 md 里现成的），不违反 §1.3。"""
    out, seen = [], set()
    for m in LINK_RE.finditer('\n'.join(lines[a:b])):
        if m.group(1) == '!': continue                     # 图片不算
        txt, url = m.group(2).strip(), m.group(3)
        if not txt or (txt, url) in seen: continue
        seen.add((txt, url)); out.append(f'[{txt}](<{url}>)')
    return out


def pointer_block(t, links=None, rel_raw="tdc-html/raw"):
    """§三 定稿的指针块：固定措辞 + 上游照抄，无一句自撰。"""
    L = [f"> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。"
         f"真表见 `{rel_raw}/{t['topic']}`",
         f"> 中**第 {t['idx']+1} 个有格子的 `<table>`**（跳过 `<table id=\"vr\">` 空壳）："
         f"{t['R']} 行 × {t['C']} 列" + ("，含嵌套表。" if t.get('nested') else "。")]
    if t.get('first'):
        L.append(f"> 首行（上游原文）：{t['first']}")
    if links:
        N = 20
        s = ' · '.join(links[:N])
        L.append(f"> 表内引用（{len(links)} 条，供检索）：{s}"
                 + ("…" if len(links) > N else ""))
    return '\n'.join(L)


def cells_of_region(lines, a, b):
    """一个区域里所有像“格子内容”的文字（供与上游格子比对）"""
    cs = []
    for l in lines[a:b]:
        if l.lstrip().startswith('|'):
            cs += [c for c in l.strip().strip('|').split('|')]
        elif l.strip():
            cs.append(l)
    return [c for c in (x.strip() for x in cs) if c]


def run(dry=True):
    up = enumerate_upstream()
    f2t, t2f = topic_to_md()
    bytopic = collections.defaultdict(list)
    for key, t in up.items(): bytopic[t['topic']].append(t)

    regions_total = 0; replaced = 0; tabs_used = set()
    files_touched = 0; exc = []
    for p, topic in sorted(f2t.items()):
        tabs = bytopic.get(topic, [])
        if not tabs: continue
        lines = read(p).replace('\r\n', '\n').split('\n')
        regs = [(a, b, 'block') for kind, a, b in md_blocks('\n'.join(lines)) if kind == 'table']
        regs += [(a, b, 'flat') for a, b in flat_clusters(lines)]
        regs.sort()
        if not regs: continue
        regions_total += len(regs); files_touched += 1
        for a, b, rkind in regs:
            rc = {norm(c) for c in cells_of_region(lines, a, b)}
            rc = {c for c in rc if len(c) >= 4}
            if not rc: continue
            hit = []
            for t in tabs:
                tc = {norm(c) for c in up_cells_of(t)}
                tc = {c for c in tc if len(c) >= 4}
                if not tc: continue
                if len(tc & rc) >= max(1, int(len(tc) * 0.6)): hit.append(t)
            if not hit:
                exc.append((p, a, b, '区域对不上任何上游表')); continue
            replaced += 1
            for t in hit: tabs_used.add((t['topic'], t['idx']))
    print(f"相关文件        : {files_touched}")
    print(f"md 侧区域       : {regions_total}")
    print(f"  匹配上并替换  : {replaced}")
    print(f"  匹配不上      : {len(exc)}")
    print(f"上游表被覆盖    : {len(tabs_used)} / {len(up)}")
    miss = [k for k in up if k not in tabs_used]
    print(f"★ 上游表没被覆盖 : {len(miss)}")
    c = collections.Counter(t['topic'].rsplit('.', 1)[-1] for k, t in up.items() if k in set(miss))
    print(f"    按后缀 {dict(c)}")
    return up, tabs_used, exc


# ================================================================ ① 正常表块

def split_lines(text):
    """→ (lines, nl)。带保护：不处理混用换行的文件。"""
    if re.search(r'\r(?!\n)', text): return None, None
    nl = '\r\n' if '\r\n' in text else '\n'
    return text.replace('\r\n', '\n').split('\n'), nl


ANNO_KW = ('转录说明', '表格指针')       # 旧批次留下的批注


def _is_anno(l):
    return l.lstrip().startswith('>') and any(k in l for k in ANNO_KW)


def extend_region(lines, a, b):
    """把紧贴在表块前后的旧批注块（转录说明 / 旧表格指针）一并纳入删除范围。
    表被拿掉之后，那些批注指的就是一张不存在的表 —— 会变成孤儿。"""
    hi = b
    while True:
        j = hi
        while j < len(lines) and not lines[j].strip(): j += 1
        if j < len(lines) and _is_anno(lines[j]):
            while j < len(lines) and lines[j].lstrip().startswith('>'): j += 1
            hi = j; continue
        break
    lo = a
    while True:
        j = lo - 1
        while j >= 0 and not lines[j].strip(): j -= 1
        if j >= 0 and _is_anno(lines[j]):
            while j >= 0 and lines[j].lstrip().startswith('>'): j -= 1
            lo = j + 1; continue
        break
    return lo, hi


def plan_l1():
    """正常 markdown 表块 → 指针。只做【内容签名唯一命中】的。"""
    up = enumerate_upstream()
    f2t, t2f = topic_to_md()
    bytopic = collections.defaultdict(list)
    for k, t in up.items(): bytopic[t['topic']].append(t)

    plan = []; exc = []
    for p, topic in sorted(f2t.items()):
        tabs = bytopic.get(topic, [])
        if not tabs: continue
        text = read(p)
        lines, nl = split_lines(text)
        if lines is None:
            exc.append((p, '文件换行混用')); continue
        sigs = {t['sig']: t for t in tabs}
        for kind, a, b in md_blocks('\n'.join(lines)):
            if kind != 'table': continue
            sg = sig(block_cells(lines, 'table', a, b))
            t = sigs.get(sg)
            if t is None:
                exc.append((p, f'第 {a+1} 行的表块对不上上游')); continue
            a2, b2 = extend_region(lines, a, b)      # 顺手吃掉旧批注
            lk = table_links(lines, a, b)            # §七①：表内引用要保住
            plan.append((p, a2, b2, t, nl, lk))
    return plan, exc


def apply_plan(plan, dry=True, batch=None, log=None, assign_path=None):
    """→ (改了哪些文件, 记录)。batch=(起,止) 只做这一段（每 100 张一次）。"""
    from collections import defaultdict
    if batch: plan = plan[batch[0]:batch[1]]
    byfile = defaultdict(list)
    for p, a, b, t, nl, lk in plan: byfile[p].append((a, b, t, nl, lk))
    recs = []; n = 0
    for p, items in sorted(byfile.items()):
        text = read(p)
        lines, nl = split_lines(text)
        before = list(lines)
        for a, b, t, _, lk in sorted(items, key=lambda x: -x[0]):   # 从后往前替换
            lines[a:b] = pointer_block(t, lk).split('\n')
        new = nl.join(lines)
        recs.append(dict(md=os.path.relpath(p, MD).replace(os.sep, '/'),
                         topic=t['topic'], tbl=t['idx'], R=t['R'], C=t['C'],
                         sha1_before=hashlib.sha1(text.encode('utf-8')).hexdigest(),
                         n=len(items)))
        n += len(items)
        if not dry: io.open(p, 'w', encoding='utf-8', newline='').write(new)
    return recs, n
