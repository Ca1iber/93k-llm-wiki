#!/usr/bin/env python3
# show.py — 按分类号打印语料原文（只读，给建页时核对用）
#
# 用法  python show.py 02.06.05 01.07.01          # 精确匹配分类号
#       python show.py --head 02.06.05             # 只打前 800 字符
#       python show.py --grep 定义                  # 按标题关键词找
#
# 存在的理由：建页时**不许凭印象写**，每句话都要能回到原文。
# 这个脚本让「回原文」是一行命令，而不是一次搜索。

import re
import sys
from pathlib import Path

CORPUS = Path(r'F:\master-dev\dorm-wsl-sytest\tdc-html\agent-markdown\by-category')
INDEX = Path(r'F:\master-dev\understand-anything-wiki\extract\docs.jsonl')
RE_STEM = re.compile(r'(\d+(?:\.\d+)*)_(.*)')


def body(rel, limit=None):
    txt = (CORPUS / rel).read_text(encoding='utf-8')
    if txt.startswith('---'):
        i = txt.find('\n---', 3)
        if i > 0:
            txt = txt[i + 4:]
    txt = txt.strip()
    return txt[:limit] if limit else txt


def main():
    if (sys.stdout.encoding or '').lower().replace('-', '') != 'utf8':
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')

    args = sys.argv[1:]
    limit = None
    if args and args[0] == '--head':
        limit = 800
        args = args[1:]
    grep = None
    if args and args[0] == '--grep':
        grep = args[1]
        args = args[2:]

    import json
    rows = [json.loads(l) for l in INDEX.open(encoding='utf-8')]

    if grep:
        for d in rows:
            stem = d['rel'].split('/')[-1][:-3]
            m = RE_STEM.match(stem)
            hay = (d.get('title') or '') + ' ' + stem
            if grep.lower() in hay.lower():
                print(f'{m.group(1) if m else "?":14s} {d["rel"]}')
        return

    want = set(args)
    hit = 0
    for d in rows:
        stem = d['rel'].split('/')[-1][:-3]
        m = RE_STEM.match(stem)
        if not m or m.group(1) not in want:
            continue
        hit += 1
        print('=' * 74)
        print(f'#### {d["rel"]}   [{d["bytes"]}B]')
        print(body(d['rel'], limit))
        print()
    if not hit:
        sys.exit(f'没找到：{sorted(want)}')


if __name__ == '__main__':
    main()
