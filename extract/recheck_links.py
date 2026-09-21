#!/usr/bin/env python3
# recheck_links.py — 独立复算（检验计划第三类）
#
# 用真正的 markdown 解析器（markdown-it-py）走 token 流重抽全部链接，
# 与 extract.py 的手写正则 + 状态机结果做**双向差集**。
#
# 两套实现不共享任何代码：一套是 CommonMark 语法分析，一套是逐行正则 + 围栏状态机。
# 同时错的概率低，所以差异集是可信的信号。
#
#   A 有 B 无  → 大概率是正则误匹配（代码块里的伪链接、畸形括号）→ 人工确认
#   B 有 A 无  → 正则漏了 → 必须修 extract.py，不许放行
#
# 输入  docs 目录 + extract/edges.jsonl
# 输出  extract/link-diff.json

import json
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import unquote

from markdown_it import MarkdownIt

CORPUS = Path(r'F:\master-dev\dorm-wsl-sytest\tdc-html\agent-markdown\by-category')
OUTDIR = Path(r'F:\master-dev\understand-anything-wiki\extract')


def ast_md_links():
    """实现 B：markdown-it-py 走 token 流，取所有 href 以 .md 结尾的链接节点。

    解析器自己处理代码块、转义、嵌套括号——这些正是正则容易出错的地方。
    """
    md = MarkdownIt('commonmark')
    found = Counter()
    files = sorted(p for p in CORPUS.rglob('*.md') if p.is_file())
    for n, p in enumerate(files, 1):
        text = p.read_bytes().decode('utf-8', errors='replace')
        rel = p.relative_to(CORPUS).as_posix()
        for tok in md.parse(text):
            if tok.type != 'inline' or not tok.children:
                continue
            for ch in tok.children:
                if ch.type != 'link_open':
                    continue
                href = ch.attrGet('href') or ''
                if not href:
                    continue
                href = unquote(href)
                if href.split('#', 1)[0].lower().endswith('.md'):
                    found[(rel, href)] += 1
        if n % 2000 == 0:
            print(f'  AST ... {n}/{len(files)}')
    return found


def regex_links():
    """实现 A 的产出：直接读 extract.py 写的 edges.jsonl。

    顺带取回每条边的行号与 in_code_span——A−B 的归因要用（见 attribute_only_a）。
    同一 (from, to_raw) 出现多次时保留**任意一条**即可：A−B 是按 key 计数，
    归因要回答的是「B 漏掉的这些 key 处在什么块里」，取哪一次出现都指向同一个块。
    """
    found = Counter()
    meta = {}
    with open(OUTDIR / 'edges.jsonl', encoding='utf-8') as f:
        for line in f:
            e = json.loads(line)
            k = (e['from'], e['to_raw'])
            found[k] += 1
            meta[k] = {'line': e['line'], 'in_code_span': e['in_code_span']}
    return found, meta


def attribute_only_a(only_a, meta):
    """把 A−B 逐条钉到 markdown-it 自己认定的块类型上。

    为什么必须机器算：报告早先手写成「其余为 CommonMark 判为缩进代码块的行」，
    人工核对一看，6 条里有 1 条根本不是缩进代码块，是 `<script>` 起头的 HTML 块
    一路吞到文件末尾。**手写的归因会错，错的归因等于没归因。**

    返回 {'code_span': n, 'indented_code_block': n, 'html_block': n,
          'fence': n, 'unknown': n, 'unknown_detail': [...]}
    unknown 必须为 0；不为 0 就是有新的、没名字的差异类型，不许放行。
    """
    md = MarkdownIt('commonmark')
    need = {}
    for k in only_a:
        rel = k[0]
        if meta.get(k, {}).get('in_code_span'):
            continue
        need.setdefault(rel, None)

    blocks = {}
    for rel in need:
        text = CORPUS.joinpath(rel).read_bytes().decode('utf-8', errors='replace')
        blocks[rel] = sorted(
            (tk.map[0], tk.map[1], tk.type)
            for tk in md.parse(text)
            if tk.map and tk.type in ('html_block', 'code_block', 'fence')
        )

    KIND = {'code_block': 'indented_code_block'}
    out = Counter()
    detail = []
    for k, v in sorted(only_a.items()):
        m = meta.get(k, {})
        if m.get('in_code_span'):
            out['code_span'] += v
            continue
        if k not in meta:
            out['unknown'] += v
            detail.append({'doc': k[0], 'target': k[1], 'count': v,
                           'why': 'edges.jsonl 里找不到这条边'})
            continue
        ln = m['line']
        hit = [b for b in blocks.get(k[0], []) if b[0] < ln <= b[1]]
        if not hit:
            out['unknown'] += v
            detail.append({'doc': k[0], 'target': k[1], 'count': v, 'line': ln,
                           'why': '不在任何 html_block / code_block / fence 内'})
            continue
        out[KIND.get(hit[0][2], hit[0][2])] += v
        detail.append({'doc': k[0], 'target': k[1], 'count': v, 'line': ln,
                       'block': hit[0][2], 'span': [hit[0][0], hit[0][1]]})
    return out, detail


def main():
    if (sys.stdout.encoding or '').lower().replace('-', '') != 'utf8':
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')

    if not (OUTDIR / 'edges.jsonl').is_file():
        sys.exit('先跑 extract.py')

    a, meta = regex_links()
    print(f'A (正则)      {sum(a.values()):6d} 条')
    b = ast_md_links()
    print(f'B (markdown-it) {sum(b.values()):6d} 条')

    only_a = a - b
    only_b = b - a

    def sample(counter, n=40):
        return [{'doc': k[0], 'target': k[1], 'count': v}
                for k, v in list(counter.items())[:n]]

    attrib, attrib_detail = attribute_only_a(only_a, meta)
    print()
    print('A−B 归因：', dict(attrib))

    out = {
        'a_total': sum(a.values()),
        'b_total': sum(b.values()),
        'only_a_total': sum(only_a.values()),
        'only_b_total': sum(only_b.values()),
        'only_a_kinds': len(only_a),
        'only_b_kinds': len(only_b),
        'only_a_samples': sample(only_a),
        'only_b_samples': sample(only_b),
        'only_a_by_doc': Counter(k[0] for k in only_a).most_common(20),
        'only_b_by_doc': Counter(k[0] for k in only_b).most_common(20),
        'only_a_attribution': dict(attrib),
        'only_a_attribution_detail': attrib_detail,
    }
    with open(OUTDIR / 'link-diff.json', 'w', encoding='utf-8', newline='\n') as f:
        json.dump(out, f, ensure_ascii=False, indent=2, sort_keys=True)

    print()
    print(f'A 有 B 无（疑似正则误匹配）: {sum(only_a.values()):6d} 条 / {len(only_a)} 种')
    print(f'B 有 A 无（正则漏，必须修）: {sum(only_b.values()):6d} 条 / {len(only_b)} 种')
    print()
    if only_b:
        print('=== B 有 A 无 样例 ===')
        for k, v in list(only_b.items())[:20]:
            print(f'  x{v}  {k[0]}')
            print(f'        -> {k[1]}')
    if attrib.get('unknown'):
        print(f'\n❌ A−B 中有 {attrib["unknown"]} 条无法归因（不在代码段/缩进代码块/'
              f'HTML 块/围栏里）——这是新的差异类型，必须查明，不许放行。')
        for d in attrib_detail:
            if d.get('why'):
                print(f'   - {d["doc"]}:{d.get("line")} -> {d["target"]}  ({d["why"]})')
    print(f'\nDONE -> {OUTDIR / "link-diff.json"}')


if __name__ == '__main__':
    main()
