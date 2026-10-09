#!/usr/bin/env python -X utf8
# -*- coding: utf-8 -*-
"""语料修复：**表格被压平**（HTML `<table>` → markdown 时行列结构被拍平）。

用法：
    python -X utf8 extract/fix_corpus_tables.py                # 空跑：只报数、只出证据表
    python -X utf8 extract/fix_corpus_tables.py --limit 15     # 只跑前 15 篇（试点）
    python -X utf8 extract/fix_corpus_tables.py --apply        # 真改

## 病

上游 HTML 里是真表格（`<table><tr><th>/<td>`）。转成 markdown 时**行列结构被拍平**：
每格文字各占一行，格与格之间夹「只有竖线的行」，行与行之间是**两条**。
**内容一个字没丢，丢的是「谁挨着谁」**——宽表里哪个默认值属于哪个参数就再也读不出来了。

## 判据（**这不是「编一张表」，是「解析 + 逐格验」**）

压平后的形状是**规则的**，所以能解析回来。关键洞察：**压平文本其实是一张 markdown 表，
它的每个 `|` 分隔符被格内的块级换行冲散了。** 一张 R 行 C 列的表，` |` token 恰好
**R×(C+1) 个**（每行 C 个格子两侧共 C+1 条竖线）。于是：

1. 从上游 `.htm` 抽出所有 `<table>`，解析成网格（`<tr>`→行，`<th>/<td>`→格）
2. 在 md 里取**连续 R×(C+1) 个 ` |` token**（首 token 必须在行首、末 token 在行尾），
   按「C 格一组、组间一个空档」切回 R×C 网格
3. **逐格核对**：解析回来的网格**必须和上游网格一格不差**（行数、列数、每格文字）
4. **对不上就整张不动**——宁可少修，不修错

**第 3 条是整件事的安全阀。没有它，就是在编一张表，而编表比压平更坏。**

## 只改下游

`tdc-html/raw/*.htm` **一个字节不动**：它既是 A 类的唯一对证上游，也是「重放」的退路
（`git show HEAD:` 永远再生得出「修复前」）。理由见 `schema.md` §1.2。

## 不认领的邻族缺陷（**刻意放过，见 §1.2「A 类授权只覆盖被批准的那几处」**）

- **上标被拍平**（`2<sup>48</sup>` → `2^48`）：第一批已改。比对时 `^` 两边都剥掉，
  于是「已改的 `2^48`」与「没改的脚注标记 `1)`」都认。
- **坏字**（`鈥?` / `鈮?` / `…nbsp;`）：坏字那几批的账，本修复器不碰，
  但**不因此否决表格结构**——这类文档会在判据上「网格不等」而被弃，会计数报出来。

## 边界规则

| 情况 | 处置 |
|---|---|
| 上游有 colspan / rowspan | **整张跳过**（markdown 表格表达不了合并格） |
| 上游某行列数与其它行不齐 | **整张跳过** |
| 格内含多段 / 换行 | 段间 `<br><br>`、段内 `<br>`（本工程表格单元格的既有写法） |
| 格内含 `|` | 转义成 `\\|` |
| 格内有代码围栏 ``` | **整张跳过**并计数 |
| md 含行首竖线行（另一来源的表格） | **整篇跳过**（那是 Doxygen 一类的另一种产物） |
| 表外的图被粘在末竖线之后 | 仅当**后面再无任何 token** 时接受，并断开成独立段落 |

## 产物三件套（全部入库）

- `extract/findings-corpus-tables-evidence.md` —— 逐处对照的证据表
- `extract/_assign_tables.json` —— 机器可读清单（含 orig / new，**供重放**）
- 本脚本

## 换行规矩（本工程踩过两次的坑）

一律 `read_bytes().decode('utf-8','replace')` / `write_bytes(...)`。
**Windows 上 `read_text()` 会把 CRLF 悄悄转成 LF、`write_text()` 会把 LF 加成 CRLF。**
改完必须验 `git diff --numstat` 的**新增行数 == 删除行数**。
"""
import collections
import html as _html
import hashlib
import json
import pathlib
import re
import sys
from html.parser import HTMLParser

WIKI = pathlib.Path(r'F:\master-dev\understand-anything-wiki')
CORPUS = pathlib.Path(r'F:\master-dev\dorm-wsl-sytest\tdc-html')
MD = CORPUS / 'agent-markdown' / 'by-category'
RAW = CORPUS / 'raw'
EVID = WIKI / 'extract' / 'findings-corpus-tables-evidence.md'
ASSIGN = WIKI / 'extract' / '_assign_tables.json'

APPLY = '--apply' in sys.argv
LIMIT = int(sys.argv[sys.argv.index('--limit') + 1]) if '--limit' in sys.argv else None

SOURCE_TOPIC = re.compile(r'^source_topic:\s*["\']?([^"\'\s]+)', re.M)
LONE = re.compile(r'^\s*\|\s*$')
# 分隔符 token：竖线，前面是一个空格，后面是空白或行尾
TOKEN = re.compile(r'(?<= )\|(?=[ \t\r\n]|$)')
# md 侧排版语法（**只剥排版，不剥语义**）
MD_IMG = re.compile(r'!\[((?:[^\[\]]|\[[^\[\]]*\])*)\]\([^)]*\)')
MD_LINK = re.compile(r'\[((?:[^\[\]]|\[[^\[\]]*\])*)\]\([^)]*\)')
MD_ESC = re.compile(r'\\([\\`*_{}\[\]()#+\-.!|<>~])')
MD_ITEM = re.compile(r'(?m)^[ \t]*(?:[-*+]|\d+[.)])[ \t]+')
MD_ITEM_ALONE = re.compile(r'(?m)^[ \t]*[-*+][ \t]*$')
MIN_CONTENT = 4        # 格子净内容下限：低于此的表近乎无信息（两格全空的 1×2 会到处撞上）
BLOCK_END = {'p', 'div', 'figure', 'figcaption', 'li', 'tr', 'td', 'th', 'table',
             'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'dt', 'dd', 'section', 'blockquote'}


def guard(path, n, what):
    """互锁：本次结果为 0 条而目标已有内容时 → 拒绝写（防「空表覆盖好清单」）。"""
    if n or not path.exists() or path.stat().st_size == 0:
        return True
    print(f'\n⛔ 拦截：本次{what}为 0 条，而 {path.name} 已有 '
          f'{path.stat().st_size:,} 字节——**拒绝用空结果覆盖**。')
    return False


# --------------------------------------------------------------------------- 上游

class TableParser(HTMLParser):
    """收集所有 `<table>`，每格记 colspan/rowspan 与文字片段（图片折成 alt）。"""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.tables = []
        self._st = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'table':
            self._st.append({'rows': [], 'row': None, 'cell': None})
            return
        if not self._st:
            return
        t = self._st[-1]
        if tag == 'tr':
            t['row'] = []
        elif tag in ('td', 'th'):
            if t['row'] is None:
                t['row'] = []
            t['cell'] = {'txt': [], 'colspan': int(a.get('colspan') or 1),
                         'rowspan': int(a.get('rowspan') or 1)}
        elif tag == 'img' and t['cell'] is not None:
            t['cell']['txt'].append('\x00' + (a.get('alt') or '') + '\x00')
        elif tag == 'br' and t['cell'] is not None:
            t['cell']['txt'].append('\n')
        elif tag == 'sup' and t['cell'] is not None:
            # 与「上标被拍平」那一批的改法对齐；^ 在比对时两边都会剥掉
            t['cell']['txt'].append('^')

    def handle_endtag(self, tag):
        if not self._st:
            return
        t = self._st[-1]
        if tag == 'table':
            self._st.pop()
            self.tables.append(t)
        elif tag == 'tr':
            if t['row'] is not None:
                t['rows'].append(t['row'])
            t['row'] = None
        elif tag in ('td', 'th'):
            if t['cell'] is not None and t['row'] is not None:
                t['row'].append(t['cell'])
            t['cell'] = None
        elif tag in BLOCK_END and t['cell'] is not None:
            t['cell']['txt'].append('\n')       # 发换行，让上游也有「行首」可言

    def handle_data(self, d):
        if self._st and self._st[-1]['cell'] is not None:
            self._st[-1]['cell']['txt'].append(d)


def upstream_tables(topic):
    """返回 (tables, 原因)。tables 为 None 表示上游 htm 不在。"""
    h = RAW / (topic + '.htm')
    if not h.exists():
        return None, '上游 htm 不在'
    tp = TableParser()
    try:
        tp.feed(h.read_bytes().decode('utf-8', 'replace'))
    except Exception as e:                       # 兜住不静默
        return [], f'htm 解析异常:{type(e).__name__}'
    out = []
    for t in tp.tables:
        rows = t['rows']
        if not rows or all(not r for r in rows):
            continue                             # <table id="vr"> 空壳
        if any(c['colspan'] > 1 or c['rowspan'] > 1 for r in rows for c in r):
            out.append({'rows': rows, 'skip': '合并格'})
            continue
        w = {len(r) for r in rows}
        if len(w) != 1 or 0 in w:
            out.append({'rows': rows, 'skip': '列数不齐'})
            continue
        out.append({'rows': rows, 'skip': None})
    return out, None


# ------------------------------------------------------------------------ 规范化

def _flatten(s):
    """两边共用的收尾：删「只有列表标记的行」→ 剥行首列表标记 → 剥 `^` → 抹掉空白。"""
    s = MD_ITEM_ALONE.sub('', s)
    s = MD_ITEM.sub('', s)
    s = s.replace('^', '')
    return re.sub(r'\s+', '', s)


def norm_up(s):
    """上游格子：图片已折成 alt，块级标签已发换行。"""
    return _flatten(_html.unescape(s.replace('\x00', '')))


def norm_md(s):
    """md 格子：剥掉 markdown 的**排版**语法，只留可见文字。"""
    s = MD_IMG.sub(r'\1', s)
    s = MD_LINK.sub(r'\1', s)
    s = s.replace('`', '')
    s = MD_ESC.sub(r'\1', s)
    return _flatten(_html.unescape(s))


# ------------------------------------------------------------------------- md 侧

def md_tokens(text):
    """返回 (全部 token 位置, 行首 token 下标, 行尾 token 下标集合, 是否含行首竖线行)。"""
    for line in text.splitlines(keepends=True):
        if line.startswith('|'):
            return None, None, None, True
    allt = [m.start() for m in TOKEN.finditer(text)]
    bol_idx, eol_idx = [], set()
    for i, p in enumerate(allt):
        bol = text.rfind('\n', 0, p) + 1
        if text[bol:p].strip() == '':
            bol_idx.append(i)
        e = p + 1
        nl = text.find('\n', e)
        if nl == -1:
            nl = len(text)
        if text[e:nl].strip() == '':
            eol_idx.add(i)
    return allt, bol_idx, eol_idx, False


def _has_paragraph_break(gap):
    """间隔里有没有**空行**（两层换行）。空行=段落边界；只有一层换行=同一张表内部。"""
    return re.search(r'\n[ \t]*\n', gap) is not None


def parse_region(text, allt, eol_idx, i, P):
    """取 P 个连续 token 切回 chunks。返回 (chunks, start, end) 或 None。

    ★ 四条「有界」判据。压平表**内部**相邻 token 只隔一层换行，**表与表/段落之间**
    隔一个空行。所以区域若与**前一个/后一个 token** 只隔一层换行（或没有间隔），
    说明它是**某张更大表的中段**，不是一张完整的表 —— 拿它去替换会把大表打碎。

    实测教训：`02.03.06.02.02.04_E8023PD_...md` 那张大 pogo pin 分配表，
    内部的 ` |   | |` 行边界被一张「1×2 两格全空」的上游表撞上，
    替换进去就会把大表拦腰截断。"""
    if i + P > len(allt) or (i + P - 1) not in eol_idx:
        return None
    start, end = allt[i], allt[i + P - 1] + 1
    bol = text.rfind('\n', 0, start) + 1
    if text[bol:start].strip():                    # 首 token 之前的行内前缀必须是空白
        return None
    if i > 0:                                      # ① 前方有界
        gap = text[allt[i - 1] + 1:start]
        if gap.strip() == '' and not _has_paragraph_break(gap):
            return None
    e = end
    while e < len(text) and text[e] in ' \t':
        e += 1
    if e < len(text) and text[e] not in '\r\n' and i + P != len(allt):
        # 末 token 之后还粘着内容：只有「后面再无 token」（表外的图粘上来了）才接受
        return None
    if i + P < len(allt):                          # ② 后方有界
        gap = text[end:allt[i + P]]
        if gap.strip() == '' and not _has_paragraph_break(gap):
            return None
    toks = allt[i:i + P]
    chunks = [text[start if k == 0 else toks[k - 1] + 1: toks[k]] for k in range(P)]
    chunks.append(text[end:e])
    return chunks, start, e


def cells_of(chunks, R, C):
    """按「C 格一组、组间一个空档」切。返回 (cells, ok)。"""
    cells, idx = [], 1
    for ri in range(R):
        for _ in range(C):
            cells.append(chunks[idx])
            idx += 1
        if ri < R - 1:
            if chunks[idx].strip():
                return None, False
            idx += 1
    return cells, True


# --------------------------------------------------------------------------- 排版

def clean_cell(chunk):
    """把 md 里的一格文字排成单元格里的单行：段间 <br><br>、段内 <br>；转义 |。"""
    s = chunk.replace('\r\n', '\n').strip()
    if not s:
        return ''
    paras, cur = [], []
    for line in s.split('\n'):
        if line.strip() == '':
            if cur:
                paras.append(cur)
                cur = []
        else:
            cur.append(line.strip())
    if cur:
        paras.append(cur)
    body = '<br><br>'.join('<br>'.join(x) for x in paras)
    body = re.sub(r'[ \t]{2,}', ' ', body)
    body = re.sub(r'(?<!\\)\|', r'\\|', body)     # 格内竖线转义
    return body


def match_table(text, allt, bol_idx, eol_idx, rows, R, C, blocked=None):
    """在一篇 md 里找**这张**上游表的压平区域。

    返回 (候选列表, 跳过原因或 None)。候选是 (start, end, cells, flat_up)。
    「整张不动」的两种情形（围栏 / 内容近于空）**一发现就作废全部候选**。

    ★ `blocked` 传一个 list 时，被规则挡下的那次**也把区域交出来**
    （`fix_corpus_ptr.py` 要靠它知道该把指针插在哪）—— **判据只有这一份，别另抄。**"""
    P = R * (C + 1)
    flat_up = [norm_up(''.join(c['txt'])) for r in rows for c in r]
    cands, fitted = [], False
    for i in bol_idx:
        r = parse_region(text, allt, eol_idx, i, P)
        if not r:
            continue
        chunks, start, end = r
        if chunks[0].strip() or chunks[-1].strip():
            continue
        cells, ok = cells_of(chunks, R, C)
        if not ok:
            continue
        fitted = True                       # 窗口放得下（只是格可能对不上）
        if [norm_md(c) for c in cells] != flat_up:
            continue
        if any('```' in c for c in cells):  # 围栏会撑破表格 → 整张不动
            if blocked is not None:
                blocked.append((start, end, cells, flat_up))
                return blocked, '格内有代码围栏'
            return [], '格内有代码围栏'
        if sum(len(norm_md(c)) for c in cells) < MIN_CONTENT:
            if blocked is not None:
                blocked.append((start, end, cells, flat_up))
                return blocked, '内容近于空（判据太弱）'
            return [], '内容近于空（判据太弱）'
        cands.append((start, end, cells, flat_up))
    if cands:
        return cands, None
    return [], ('网格不等' if fitted else '窗口放不下')


def render_table(cells, R, C, nl):
    out = []
    for ri in range(R):
        row = cells[ri * C:(ri + 1) * C]
        out.append('| ' + ' | '.join(row) + ' |')
        if ri == 0:
            out.append('|' + '---|' * C)          # 本工程既有的表头分隔风格
    return nl.join(out)


def _show_pilot(accepted, MD):
    """试点：把「原 md 片段 → 新表」逐处打出来，供人工对着上游看。"""
    for x in accepted:
        print('=' * 78)
        print(f"{x['path'].relative_to(MD).as_posix()}   ← 上游 {x['topic']}.htm 表 #{x['tbl']}"
              f"   {x['R']}×{x['C']}")
        print('--- 原 md 片段 ---')
        print('  ' + repr(x['orig'][:300]))
        print('--- 新表 ---')
        for line in x['table'].split('\r\n'):
            print('  ' + line[:150])


def _replay_verify(per):
    """★ `schema.md` §1.2 指定的**真正判据**：从 git 基线**逐字节重放**。

    拿 `git show HEAD:<path>`（改动前的语料）当基线，按清单里的偏移逐处替换，
    结果必须与工作区**一字不差**。这比 `git diff --numstat` 对称强：
    本族修复**必然**让行数大幅减少（每格一行 → 每行一格），
    「新增==删除」那条验法在这里不适用（§1.2 第 4 条：判据随对象变，计数不再是判据）。

    注意：**必须在提交本次改动之前跑**，否则 HEAD 已经是改后的了。
    注意：**本仓 `core.autocrlf=true`** —— git 存 LF、工作区是 CRLF。
    `git show` 出来的是 LF，清单里的偏移是**工作区字节偏移**，所以必须先对齐换行，
    否则「逐字节」永远对不上（第一次跑就是 100% 误报）。"""
    import subprocess
    bad = []
    for p, recs in per.items():
        rel = p.relative_to(CORPUS).as_posix()
        r = subprocess.run(['git', '-C', str(CORPUS), 'show', f'HEAD:{rel}'],
                           capture_output=True)
        if r.returncode != 0:
            bad.append((rel, 'git show 取不到基线'))
            continue
        base = r.stdout.decode('utf-8', 'replace')
        cur = p.read_bytes().decode('utf-8', 'replace')
        if '\r\n' in cur and '\r\n' not in base:      # ★ autocrlf：基线补回 CR
            base = base.replace('\n', '\r\n')
        elif '\r\n' not in cur and '\r\n' in base:
            base = base.replace('\r\n', '\n')
        for x in sorted(recs, key=lambda y: -y['a']):
            if base[x['a']:x['e']] != x['orig']:
                bad.append((rel, f"基线偏移 {x['a']} 处与 orig 不符（基线已变？）"))
                break
            base = base[:x['a']] + x['table'] + x['tail'] + base[x['e']:]
        else:
            if base != cur:
                bad.append((rel, '重放结果与工作区不一致'))
    return bad


def verify_only():
    """只跑「逐字节重放」验证（对着当前工作区与 git 基线 + 现有清单）。
    用于：apply 之后单独复核，或改完验证器后重新复核。"""
    if (sys.stdout.encoding or '').lower().replace('-', '') != 'utf8':
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    _m = json.loads(ASSIGN.read_text(encoding='utf-8'))
    per = {}
    for x in _m:
        key = CORPUS / 'agent-markdown' / 'by-category' / x['md']
        per.setdefault(key, []).append(
            dict(a=x['a'], e=x['e'], orig=x['orig'], table=x['new'], tail=x.get('tail', '')))
    print(f'清单 {len(_m):,} 条，涉及 {len(per):,} 篇；对 `git show HEAD:` 逐字节重放…')
    bad = _replay_verify(per)
    if bad:
        print(f'⛔ 失败 {len(bad)} 篇，前 10：')
        for rel, why in bad[:10]:
            print(f'   {rel}: {why}')
        sys.exit(3)
    print(f'✅ 重放一致：{len(per):,}/{len(per):,} 篇，逐字节相同。')


# --------------------------------------------------------------------------- 主流程

def main():
    if '--verify-only' in sys.argv:
        return verify_only()
    if (sys.stdout.encoding or '').lower().replace('-', '') != 'utf8':
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')

    docs = []
    for p in sorted(MD.rglob('*.md')):
        t = p.read_bytes().decode('utf-8', 'replace')
        if sum(1 for l in t.splitlines() if LONE.fullmatch(l)) >= 2:
            docs.append(p)
    print(f'候选文档（孤立竖线 ≥2 行）：{len(docs):,} 篇')
    if LIMIT:
        docs = docs[:LIMIT]
        print(f'--limit {LIMIT} → 只跑前 {len(docs)} 篇')

    stat, tbl_stat = {}, {}
    accepted = []

    def bump(d, k, n=1):
        d[k] = d.get(k, 0) + n

    for p in docs:
        text = p.read_bytes().decode('utf-8', 'replace')
        nl = '\r\n' if '\r\n' in text else '\n'
        allt, bol_idx, eol_idx, col0 = md_tokens(text)
        if col0:
            bump(stat, '含行首竖线（另一来源的表格）')
            continue
        m = SOURCE_TOPIC.search(text)
        if not m:
            bump(stat, '无 source_topic')
            continue
        topic = m.group(1).replace('.htm', '')
        ups, why = upstream_tables(topic)
        if ups is None:
            bump(stat, why)
            continue
        for u in ups:
            if u['skip']:
                bump(tbl_stat, '上游:' + u['skip'])
        good = [u for u in ups if not u['skip']]
        if not good:
            bump(stat, '上游无可用表')
            continue

        by_tbl = {}
        for ui, u in enumerate(ups):
            if u['skip']:
                continue
            mine, reason = match_table(text, allt, bol_idx, eol_idx,
                                       u['rows'], len(u['rows']), len(u['rows'][0]))
            by_tbl[ui] = mine
            if reason:
                bump(tbl_stat, reason)

        # ① **一张上游表在文档里只许对上「一处」**：对上 ≥2 处互不重叠的，
        #    分不清是「重复投放该都改」还是「撞上了」——按「宁可少修，不修错」
        #    **整张不动**（也避免只改一半）。
        picked = []
        for ui, lst in sorted(by_tbl.items()):
            R, C = len(ups[ui]['rows']), len(ups[ui]['rows'][0])
            lst = sorted(lst, key=lambda c: -(c[1] - c[0]))     # 长的优先
            keep, spans = [], []
            for c in lst:
                if any(not (c[1] <= s or c[0] >= e) for s, e in spans):
                    continue                                # 窗口重叠 → 同一个区域
                spans.append((c[0], c[1]))
                keep.append((ui, R, C) + c)
            if len(keep) == 1:
                picked.append(keep[0])
            elif keep:
                bump(tbl_stat, '同表多处命中（分不清 → 整张不动）')
        if not picked:
            bump(stat, '无表对上')
            continue
        # ② 跨表抢同一段（两张上游表内容相同时会撞）：长的优先，弃后者。
        picked.sort(key=lambda c: -(c[4] - c[3]))
        chosen, spans = [], []
        for c in picked:
            if any(not (c[4] <= s or c[3] >= e) for s, e in spans):
                bump(tbl_stat, '同一段被两个上游表抢（弃一）')
                continue
            spans.append((c[3], c[4]))
            chosen.append(c)
        chosen.sort(key=lambda c: c[3])
        bump(stat, '全部表对上' if len(chosen) == len(good) else '仅部分表对上')

        for ui, R, C, start, end, cells, flat_up in chosen:
            a = text.rfind('\n', 0, start) + 1
            body = [clean_cell(c) for c in cells]
            tbl = render_table(body, R, C, nl)
            # ★ 自校验：**把生成的新表再解析一遍**，必须还能还原出上游网格。
            #   这一道抓「转义 / <br> / 列数编排」写错，是独立于上面那次核对的重验。
            #   （`<br>` 还原成换行再规范化——否则行首的 `- ` 不再在行首，剥不掉）
            back = [norm_md(re.sub(r'<br>(?:<br>)*', '\n', x)) for x in body]
            assert back == flat_up, f'{p.name}: 新表回解不回上游网格'
            assert len(tbl.split(nl)) == R + 1, f'{p.name}: 新表行数不对'
            e = end
            while e < len(text) and text[e] in ' \t':
                e += 1
            tail = nl if (e < len(text) and text[e] not in '\r\n') else ''
            accepted.append(dict(path=p, topic=topic, tbl=ui, R=R, C=C, cells=cells,
                                 table=tbl, orig=text[a:e], a=a, e=e, tail=tail))

    # ---------------------------------------------------------------- 报告
    n_tbl = len(accepted)
    n_doc = len({x['path'] for x in accepted})
    print(f'\n✅ 可修表 **{n_tbl:,} 张**，涉及 **{n_doc:,} 篇**')
    print('\n跳过（按类，**不许静默跳过**）：')
    for k, v in sorted(stat.items(), key=lambda kv: -kv[1]):
        print(f'   {k:<28} {v:,} 篇')
    print('上游表侧：')
    for k, v in sorted(tbl_stat.items(), key=lambda kv: -kv[1]):
        print(f'   {k:<28} {v:,} 张')

    if LIMIT:
        # 试点：**不写产物**。否则 15 篇的结果会盖掉全量清单——那正是 guard() 要防的事。
        print('\n[试点 --limit] 不写证据表 / 清单。')
        _show_pilot(accepted, MD)
        return

    if not guard(EVID, n_tbl, '证据表') or not guard(ASSIGN, n_tbl, '清单'):
        print('   （什么都没写，语料也没动。）')
        sys.exit(2)

    # ---------------------------------------------------------------- 产物
    esc = lambda x: x.replace('\\', '\\\\').replace('|', '\\|').replace('\r\n', '⏎')
    with EVID.open('w', encoding='utf-8', newline='\n') as fh:
        fh.write('# 语料表格修复证据表 —— 「表格被压平」\n\n')
        fh.write(f'写于 2026-10-08。共 **{n_tbl:,}** 张表 / **{n_doc:,}** 篇。\n\n')
        fh.write('**每张表都逐格核对过**：按「R×(C+1) 个 ` |` token」切回网格后，'
                 '每一格的文字必须与上游 `.htm` 的对应格一致（空格/换行/列表标记/'
                 '反引号/链接图片标记等**排版差异**已规范化；上标标记 `^` 两边都剥，'
                 '因为那是另一批的账）。**不一致的表一律不改。**\n\n')
        fh.write('**只改 `agent-markdown/`，上游 `raw/*.htm` 一个字节不动。**\n\n')
        fh.write('两处**注明的**改动，都是 markdown 语法逼出来的，不是改内容：\n\n')
        fh.write('1. **第一行一律成为表头**（跟着一行 `|---|---|`）。'
                 'GFM 的表格必须有表头分隔行，上游第一行是 `<td>` 的那些也躲不过。'
                 '**格子内容一字未动**。\n')
        fh.write('2. **格内的换行改写成 `<br>` / `<br><br>`**（段内 / 段间）。'
                 'markdown 单元格里放不下真换行。`<br>` 也是本工程表格单元格的既有写法'
                 '（见 `schema.md` 的约束表）。**文字一字未增未删。**\n\n')
        fh.write('`原 md 片段` 里 `⏎` 代表换行；`新表` 里 `⏎` 同样是换行。\n\n')
        fh.write('| # | markdown | 上游 | 表 | 尺寸 | 原 md 片段（截 150 字符） | 新表 |\n')
        fh.write('|---|---|---|---|---|---|---|\n')
        for n, x in enumerate(accepted, 1):
            rel = x['path'].relative_to(MD).as_posix()
            o = esc(x['orig'][:150]) + ('…' if len(x['orig']) > 150 else '')
            fh.write(f"| {n} | `{rel}` | `{x['topic']}.htm` | #{x['tbl']} | "
                     f"{x['R']}×{x['C']} | `{o}` | `{esc(x['table'])}` |\n")
    print(f'\n证据表 → {EVID}')

    # ★ 清单**整份重写**，不做并集：并集会把上一次运行的陈旧条目留下来。
    #  「空表盖好表」由 guard() 拦，不靠并集。
    # `a` / `e` 是**基线文件里的字节偏移**（重放要用它精确定位，不能只靠 orig 文本——
    # 实测有 426 处区域原文在文件里出现不止一次，靠文本替换会改错地方）。
    _m = [dict(md=x['path'].relative_to(MD).as_posix(), topic=x['topic'], tbl=x['tbl'],
               R=x['R'], C=x['C'], a=x['a'], e=x['e'],
               sha1_orig=hashlib.sha1(x['orig'].encode('utf-8')).hexdigest(),
               orig=x['orig'], new=x['table']) for x in accepted]
    ASSIGN.write_text(json.dumps(_m, ensure_ascii=False, indent=0), encoding='utf-8')
    print(f'机器可读清单 → {ASSIGN}（{len(_m):,} 条，本次全量重写）')

    if not APPLY:
        print('\n[空跑] 没有改任何文件。加 --apply 才真改。')
        return

    per = {}
    for x in accepted:
        per.setdefault(x['path'], []).append(x)
    changed = 0
    for p, recs in sorted(per.items(), key=lambda kv: str(kv[0])):
        t = p.read_bytes().decode('utf-8', 'replace')   # ★ 不用 read_text
        crlf_only_before = t.count('\n') == t.count('\r\n')
        for x in sorted(recs, key=lambda r: -r['a']):
            assert t[x['a']:x['e']] == x['orig'], f"{p.name}: 区域与预期不符"
            t = t[:x['a']] + x['table'] + x['tail'] + t[x['e']:]
            changed += 1
        if crlf_only_before:
            # ★ 换行不许被动过：本来全 CRLF，改完还得全 CRLF
            assert t.count('\n') == t.count('\r\n'), f'{p.name}: 混入了裸 LF'
        p.write_bytes(t.encode('utf-8'))                # ★ 不用 write_text

    bad = _replay_verify(per)
    if bad:
        print(f"\n⛔ 重放验证失败 {len(bad)} 篇，前 5：")
        for rel, why in bad[:5]:
            print(f'   {rel}: {why}')
        sys.exit(3)
    print(f"\n[已改] {changed:,} 张表，涉及 {len(per):,} 篇"
          f"（逐字节重放验证通过：{len(per):,}/{len(per):,} 篇）")


if __name__ == '__main__':
    main()
