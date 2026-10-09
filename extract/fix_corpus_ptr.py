#!/usr/bin/env python -X utf8
# -*- coding: utf-8 -*-
"""语料修复（第八批）：给**修不了的表格**插一句指向上游 HTML 的「指针」。

用法：`--limit N` 试点 / 无参空跑 / `--apply` / `--verify-only`

## 要干什么

前面几批把**能修的**表都修了。**剩下的修不了**（合并格 / 嵌套 / 与上游对不上 /
重复太多 / 有代码围栏）。这一批不再硬塞进 markdown，而是**在那张表的位置加一句注释**，
指向上游那张真表，让读者/agent 直接去读 HTML。

**不假装能表达，而是把「md 答不了 + 去哪儿查」写准。**
与「转录说明」是同一套规矩的两处应用（见 `schema.md` **§1.3**）。

## 覆盖范围与「锚」——★ 定位靠这个

| 类 | 锚 |
|---|---|
| ① 判据**认出来了**、只是有条规矩不让改 | 判据给的区域（**直接用**，不另抄判据） |
| ② 判据没认出来，但**格子内容在 md 里且全篇唯一** | 格子内容 |
| ③ 判据没认出来、格子太短或有歧义 | **表前那段散文**（上游 HTML 里每张表前面都有段文字，那段在 md 里也在） |
| ④ 文字确实找不到 | **不做**，单独列出来 |

★ **锚不是表格里的格子** —— 那才是「太短 / 有歧义」的原因；段落长而独特，好找。

## 位置与措辞

插在**压平块的上方**（读者该**先**看到「去这儿看」，不该先啃乱麻）。
措辞**固定**，含「第 N 个**有格子的** `<table>`」—— 不写这半句，读者数 `<table>`
会把 `<table id="vr">` 空壳也数进去，**差一位就全指错**。

## 产物

`extract/findings-corpus-ptr-evidence.md`、`extract/_assign_ptr.json`
"""
import hashlib
import html as _html
import json
import pathlib
import re
import sys

sys.path.insert(0, r'F:\master-dev\understand-anything-wiki\extract')
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import fix_corpus_tables as F
import fix_corpus_tables_merged as G
import fix_corpus_tables_v2 as V

WIKI, CORPUS, MD, RAW = F.WIKI, F.CORPUS, F.MD, F.RAW
# ★ 第八批（第一批指针）用的是 `…-corpus-ptr-evidence.md` / `_assign_ptr.json`。
#   这一批（第二批指针：补上"表前散文够不着"的那些）**另开两个文件** ——
#   否则空跑会把上一批 1,325 条的记录覆盖掉。**两批的记录都要留。**
EVID = WIKI / 'extract' / 'findings-corpus-ptr2-evidence.md'
ASSIGN = WIKI / 'extract' / '_assign_ptr2.json'

APPLY = '--apply' in sys.argv
LIMIT = int(sys.argv[sys.argv.index('--limit') + 1]) if '--limit' in sys.argv else None
TAG = re.compile(r'(?s)<[^>]+>')
ALPHA = re.compile(r'[^0-9A-Za-z]')


def pointer_text(topic, idx, R, C, rows, nl):
    """**固定措辞**的指针。只描述「markdown 表达不了 + 去哪儿查」，一个字不多说。

    ★ 两行之间用**文件自己的** `nl`（本仓 CRLF）—— 写死 `\\n` 会往 CRLF 文件里
    注入裸 LF。**这个坑在 `fix_corpus_tables_merged.py` 踩过一次，这次又踩了。**"""
    shape = []
    if any(c['colspan'] > 1 for r in rows for c in r):
        shape.append('colspan')
    if any(c['rowspan'] > 1 for r in rows for c in r):
        shape.append('rowspan')
    extra = ('，含 ' + ' 与 '.join(shape)) if shape else ''
    return (f'> ⚠️ 表格指针（非原文）：本表 markdown 表达不了。真表见 `tdc-html/raw/{topic}.htm`' + nl +
            f'> 中**第 {idx} 个有格子的 `<table>`**（跳过 `<table id="vr">` 空壳）：'
            f'{R} 行 × {C} 列{extra}。')


# ------------------------------------------------------------------ 锚 ③：表前那段散文

class TP3(F.TableParser):
    """在 `F.TableParser` 上记下每个 `<table>` 的**源码行范围**（起、止）。

    用途有二：① 取「表前那段散文」；② **把落在别的表里的文字剔掉** ——
    否则「表前散文」会取到**上一张表的格子文字**，指针就插到上一张表身上了。"""

    def __init__(self):
        super().__init__()
        self.span = []
        self._open = []

    def handle_starttag(self, tag, attrs):
        if tag == 'table':
            self._open.append(self.getpos()[0])
            self.span.append([self.getpos()[0], None])
        super().handle_starttag(tag, attrs)

    def handle_endtag(self, tag):
        if tag == 'table' and self._open:
            ln = self.getpos()[0]
            for s in reversed(self.span):
                if s[1] is None:
                    s[1] = ln
                    break
            self._open.pop()
        super().handle_endtag(tag)


_CACHE = {}


def table_spans(topic):
    """该 htm 里每个 `<table>` 的行范围 —— **只保留「有格子的」**，与 `F.upstream_tables` 同序。"""
    if topic in _CACHE:
        return _CACHE[topic]
    h = RAW / (topic + '.htm')
    if not h.exists():
        _CACHE[topic] = None
        return None
    raw = h.read_bytes().decode('utf-8', 'replace')
    tp = TP3()
    try:
        tp.feed(raw)
    except Exception:
        _CACHE[topic] = None
        return None
    spans, k = [], 0
    for t in tp.tables:
        if not t['rows'] or all(not r for r in t['rows']):
            continue
        s = tp.span[k] if k < len(tp.span) else [1, 1]
        spans.append((s[0], s[1] if s[1] else s[0]))
        k += 1
    _CACHE[topic] = (spans, raw.split('\n'))
    return _CACHE[topic]


def pre_table_paras(topic, idx, want=3):
    """上游第 idx 个表**之前**最近的几段可见文字（由近到远），**剔掉落在别的表里的**。"""
    got = table_spans(topic)
    if not got:
        return []
    spans, lines = got
    if idx > len(spans):
        return []
    start = spans[idx - 1][0]
    # 把「别的表的行范围」挖掉，剩下的才算表外的散文
    inside = set()
    for a, b in spans:
        if a < start:
            inside.update(range(a, min(b, start) + 1))
    txt_lines = [lines[i - 1] for i in range(1, start) if i not in inside]
    joined = '\n'.join(txt_lines)
    joined = re.sub(r'(?i)</(p|li|h[1-6]|div|figcaption)>', '\n', joined)
    txt = _html.unescape(TAG.sub(' ', joined))
    paras = [re.sub(r'\s+', ' ', p).strip() for p in txt.split('\n')]
    paras = [p for p in paras if len(p) >= 12]
    return paras[-want:][::-1]


# ------------------------------------------------------------------ 定位

def post_table_paras(topic, idx, want=3):
    """上游第 idx 个表**之后**最近的几段可见文字（由近到远），**剔掉落在别的表里的**。

    用在「表前面没有可用散文」的场合 —— 那时只能从**表的后面**认它。
    插法也不同：认出来的是表**后面**那行，指针就插在它**上方**（即压平块的下方）。"""
    got = table_spans(topic)
    if not got:
        return []
    spans, lines = got
    if idx > len(spans):
        return []
    end = spans[idx - 1][1]
    inside = set()
    for a, b in spans:
        if a > end:
            inside.update(range(max(a, end), min(b, end + 400) + 1))
    txt_lines = [lines[i - 1] for i in range(end + 1, min(len(lines), end + 400) + 1)
                 if i not in inside]
    joined = '\n'.join(txt_lines)
    joined = re.sub(r'(?i)</(p|li|h[1-6]|div|figcaption)>', '\n', joined)
    txt = _html.unescape(TAG.sub(' ', joined))
    paras = [re.sub(r'\s+', ' ', p).strip() for p in txt.split('\n')]
    paras = [p for p in paras if len(p) >= 12]
    return paras[:want]


def line_of_unique(md_lines, nm_lines, needle):
    """`needle`（已归一）在 md 里唯一命中时，返回那个行号；否则 None。"""
    hits = [i for i, x in enumerate(nm_lines) if needle and needle in x]
    return hits[0] if len(hits) == 1 else None


def line_of_prose(nm_lines, prose):
    """拿「表前那段散文」去反查 md 的行号：先找**结尾对得上**的，再找**包含**它的。

    尾部长度依次试 60 / 40 / 25 —— 散文被转换改过时，短的更容易命中。"""
    if not prose:
        return None
    flat = F._flatten(prose)
    for L in (60, 40, 25, 15):
        tail = flat[-L:]
        if len(tail) < 12:
            continue
        hits = [i for i, x in enumerate(nm_lines) if x.endswith(tail)]
        if len(hits) == 1:
            return hits[0]
        hits = [i for i, x in enumerate(nm_lines) if tail in x]
        if len(hits) == 1:
            return hits[0]
    head = flat[:60]                      # 尾部对不上时，拿**开头**再试一次
    if len(head) >= 20:
        hits = [i for i, x in enumerate(nm_lines) if x.startswith(head)]
        if len(hits) == 1:
            return hits[0]
    return None


def main():
    if '--verify-only' in sys.argv:
        return verify_only()

    fixed = set()
    # ★ 必须含**自己的**清单 `_assign_ptr.json` —— 漏了它，重跑会把已经插过指针的表再插一遍。
    for f in ('_assign_tables.json', '_assign_tables_merged.json', '_assign_tables_v2.json',
              '_assign_ptr.json'):
        fp = WIKI / 'extract' / f
        if fp.exists():
            for x in json.loads(fp.read_text(encoding='utf-8')):
                fixed.add((x['md'], x['tbl']))

    stat, accepted = {}, []

    def bump(k, n=1):
        stat[k] = stat.get(k, 0) + n

    docs = []
    for p in sorted(MD.rglob('*.md')):
        text = p.read_bytes().decode('utf-8', 'replace')
        allt, bol, eol, outside = V.md_tokens_v2(text)
        if outside:
            continue
        docs.append((p, text, allt, bol, eol))
    print(f'候选文档：{len(docs):,} 篇')
    if LIMIT:
        docs = docs[:LIMIT]

    for p, text, allt, bol, eol in docs:
        nl = '\r\n' if '\r\n' in text else '\n'
        rel = p.relative_to(MD).as_posix()
        m = F.SOURCE_TOPIC.search(text)
        if not m:
            continue
        topic = m.group(1).replace('.htm', '')
        ups, why = F.upstream_tables(topic)
        if not ups:
            continue
        # ★ 「这张表已经有指针了没」**直接从语料里认**，不看清单 ——
        #   清单在空跑时就会被重写，拿它当"已做"会把空跑的产物当成既成事实。
        #   ★ 必须**在同一块指针内部**配对：`真表见 …` 之后**换行**、紧跟一行以 `> ` 开头、
        #   含「第 N 个」。原来用 `[\s\S]{0,120}?` 太松 —— 一篇里有多个指针时会张冠李戴
        #   （读到 A 的「真表见」配上了 B 的「第 N 个」），凭空多认出一批"已挂过"。
        already = {(t, int(n)) for t, n in re.findall(
            r'真表见 `tdc-html/raw/([^`]+?)\.htm`\r?\n> [^\n]*?第 (\d+) 个有格子的', text)}
        md_lines = text.split(nl)
        nm_lines = [F.norm_md(l) for l in md_lines]
        for ui, u in enumerate(ups):
            if (rel, ui) in fixed:
                continue
            # ★ 不再跳过「列数不齐」—— 那条是**修表**的规矩（形状不齐就拼不出来），
            #   对**挂路牌**没道理：路牌只需要知道表在哪，不需要形状对。
            if (topic, ui + 1) in already:
                continue                      # 语料里已经有它的指针了
            rows, R, C = u['rows'], len(u['rows']), len(u['rows'][0])
            blocked = []
            try:
                if u['skip'] == '合并格':
                    cands, reason = G.match_merged(text, allt, bol, eol, rows, blocked=blocked)
                else:
                    cands, reason = F.match_table(text, allt, bol, eol, rows, R, C, blocked=blocked)
            except Exception:
                bump('判据异常')
                continue
            blocked_hit = cands is blocked      # 判据在挡下时**把 blocked 当候选返回**
            if cands and not blocked_hit:
                # 正常路径下拿到候选：要么真能修（不该出现），要么「同表多处命中」
                keep, spans = [], []
                for c in sorted(cands, key=lambda c: -(c[1] - c[0])):
                    if any(not (c[1] <= s or c[0] >= e) for s, e in spans):
                        continue
                    spans.append((c[0], c[1]))
                    keep.append(c)
                if len(keep) == 1:
                    bump('★还能修但没修（不该出现）')
                    continue
                a = text.rfind('\n', 0, keep[0][0]) + 1
                anchor = len(text[:a].split(nl)) - 1
                kind = f'① 同表多处命中（{len(keep)} 处）'
            else:
                anchor = None
                kind = None
            if blocked_hit:                    # ① 判据认出来了，被规则挡下
                a = text.rfind('\n', 0, blocked[0][0]) + 1
                anchor = len(text[:a].split(nl)) - 1
                kind = f'① 规则挡下（{reason}）'
            if anchor is None:
                # 位置**只由「表前那段散文」定** —— 只有它能给压平块定界。
                # （格子的文字给不出位置：压平块内部和块外面长得一模一样）
                for prose in pre_table_paras(topic, ui + 1):
                    ln = line_of_prose(nm_lines, prose)
                    if ln is not None:
                        anchor, kind = ln, '③ 表前散文（精确）'
                        break
            if anchor is None:
                # 「表前散文」够不着时，从**表的后面**认它 —— 认出来的是表后那行，
                # 指针就插在它**上方**（= 压平块的下方）。标签里标明，与"上方"区分。
                for prose in post_table_paras(topic, ui + 1):
                    ln = line_of_prose(nm_lines, prose)
                    if ln is not None and ln >= 1:
                        anchor, kind = ln - 1, '③b 表后散文（插在块下方）'
                        break
            if anchor is None:
                # 「表的第一行」当锚：第一行**就是块的顶**，找到它就知道块从哪开始。
                #   （比用"最长那一格"强 —— 那个可能落在块中间。）
                first = ALPHA.sub('', ''.join(F.norm_up(''.join(c['txt'])) for c in rows[0]))
                if len(first) >= 15:
                    k = line_of_unique(md_lines, nm_lines, first)
                    if k is not None:
                        anchor, kind = k, '⑤ 表的第一行'
            if anchor is None:
                # 退路：用格子文字找到"它在这一带"，再退回**本节小标题**（粗，但不会插错位置）
                cells = [F.norm_up(''.join(c['txt'])) for r in rows for c in r]
                long = max(cells, key=len) if cells else ''
                k = line_of_unique(md_lines, nm_lines, long) if len(long) >= 40 else None
                if k is not None:
                    for i in range(k, -1, -1):
                        if re.match(r'^#{1,6} ', md_lines[i]):
                            anchor, kind = i, '④ 本节标题（粗定位）'
                            break
            if anchor is None:
                bump('⑤ 定不了位（单列）')
                continue
            ptr = pointer_text(topic, ui + 1, R, C, rows, nl)
            a = sum(len(l) + len(nl) for l in md_lines[:anchor + 1])
            # 前面留一个空行（否则紧贴标题/段落，某些渲染器会把它并进上一段）
            accepted.append(dict(path=p, topic=topic, tbl=ui, R=R, C=C, kind=kind,
                                 table=nl + ptr, orig=text[a:a], a=a, e=a, tail=nl))
            bump(kind)

    n = len(accepted)
    print(f'\n✅ 可插指针 **{n:,} 处**，涉及 **{len({x["path"] for x in accepted}):,} 篇**')
    for k, v in sorted(stat.items(), key=lambda kv: -kv[1]):
        print(f'   {k:<28} {v:,}')

    if LIMIT:
        print('\n[试点 --limit] 不写产物。')
        for x in accepted[:5]:
            print('=' * 74)
            print(f"{x['path'].relative_to(MD).as_posix()}  ← raw/{x['topic']}.htm 表#{x['tbl']}"
                  f"   {x['kind']}")
            i = x['a']
            print('  插在这个位置之前：')
            print('    ' + repr(x['path'].read_bytes().decode('utf-8', 'replace')[i - 90:i][-90:]))
            print('  指针：')
            print('    ' + x['table'].replace('\r\n', '\n    '))
        return

    if not F.guard(EVID, n, '证据表') or not F.guard(ASSIGN, n, '清单'):
        print('   （什么都没写，语料也没动。）')
        sys.exit(2)

    esc = lambda s: s.replace('\\', '\\\\').replace('|', '\\|').replace('\r\n', '⏎')
    with EVID.open('w', encoding='utf-8', newline='\n') as fh:
        fh.write('# 语料「指针」证据表 —— 给修不了的表格插 HTML 指针（第八批）\n\n')
        fh.write(f'写于 2026-10-09。共 **{n:,}** 处 / **{len({x["path"] for x in accepted}):,}** 篇。\n\n')
        fh.write('修不了的表不再硬塞进 markdown，改在**那张表的位置**加一句指向上游 HTML 的注释。\n'
                 '**原压平文本一个字不删**，指针只是加一句。与「转录说明」是同一套规矩（§1.3）。\n\n')
        fh.write('| # | markdown | 上游 | 表 | 锚 | 指针 |\n|---|---|---|---|---|---|\n')
        for i, x in enumerate(accepted, 1):
            fh.write(f"| {i} | `{x['path'].relative_to(MD).as_posix()}` | `{x['topic']}.htm` | "
                     f"#{x['tbl']} | {x['kind']} | `{esc(x['table'])}` |\n")
    print(f'\n证据表 → {EVID}')

    _m = [dict(md=x['path'].relative_to(MD).as_posix(), topic=x['topic'], tbl=x['tbl'],
               R=x['R'], C=x['C'], kind=x['kind'], a=x['a'],
               sha1_orig=hashlib.sha1(x['orig'].encode('utf-8')).hexdigest(),
               orig=x['orig'], new=x['table']) for x in accepted]
    ASSIGN.write_text(json.dumps(_m, ensure_ascii=False, indent=0), encoding='utf-8')
    print(f'机器可读清单 → {ASSIGN}（{len(_m):,} 条）')

    if not APPLY:
        print('\n[空跑] 没有改任何文件。加 --apply 才真改。')
        return

    per = {}
    for x in accepted:
        per.setdefault(x['path'], []).append(x)
    changed = 0
    for p, recs in sorted(per.items(), key=lambda kv: str(kv[0])):
        t = p.read_bytes().decode('utf-8', 'replace')
        crlf = t.count('\n') == t.count('\r\n')
        for x in sorted(recs, key=lambda r: -r['a']):
            t = t[:x['a']] + x['table'] + x['tail'] + t[x['e']:]
            changed += 1
        if crlf:
            assert t.count('\n') == t.count('\r\n'), f'{p.name}: 混入了裸 LF'
        p.write_bytes(t.encode('utf-8'))

    bad = F._replay_verify(per)
    if bad:
        print(f'\n⛔ 重放验证失败 {len(bad)} 篇，前 5：')
        for rel, why in bad[:5]:
            print(f'   {rel}: {why}')
        sys.exit(3)
    print(f"\n[已插] {changed:,} 处，涉及 {len(per):,} 篇（逐字节重放通过）")


def verify_only():
    _m = json.loads(ASSIGN.read_text(encoding='utf-8'))
    per = {}
    for x in _m:
        per.setdefault(MD / x['md'], []).append(
            dict(a=x['a'], e=x['e'], orig=x['orig'], table=x['new'], tail=x['tail']))
    print(f'清单 {len(_m):,} 条 / {len(per):,} 篇；对 `git show HEAD:` 逐字节重放…')
    bad = F._replay_verify(per)
    print(('✅ 重放一致：%d/%d 篇' % (len(per), len(per))) if not bad else f'⛔ 失败 {len(bad)} 篇')
    if bad:
        sys.exit(3)


if __name__ == '__main__':
    main()
