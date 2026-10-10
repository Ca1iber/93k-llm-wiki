# -*- coding: utf-8 -*-
"""§六 自查：③ 指针内容回核 —— 指针里写的「第 N 张、R 行 × C 列」对不对。"""
import os, re, sys, random, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tabledel as T

PTR = re.compile(r'第 (\d+) 个有格子的 `<table>`.*?：(\d+) 行 × (\d+) 列', re.S)

def main():
    up = T.enumerate_upstream()
    # topic → md
    t2f = collections.defaultdict(list)
    for dp, _, fns in os.walk(T.MD):
        for fn in fns:
            if not fn.endswith('.md'): continue
            p = os.path.join(dp, fn)
            m = re.search(r'source_topic:\s*"([^"]+)"', T.read(p))
            if m: t2f[m.group(1)].append(p)

    random.seed(7)
    keys = random.sample(sorted(up), min(400, len(up)))
    checked = ok = bad = 0; ex = []
    for topic, idx in keys:
        p = (t2f.get(topic) or [None])[0]
        if not p: continue
        s = T.read(p)
        # 本篇里所有指针断言
        ms = list(PTR.finditer(s))
        if not ms: continue
        checked += 1
        got = {(int(m.group(1)), int(m.group(2)), int(m.group(3))) for m in ms}
        want = {(t['idx'] + 1, t['R'], t['C']) for k, t in up.items() if k[0] == topic}
        if (idx + 1, up[(topic, idx)]['R'], up[(topic, idx)]['C']) in got: ok += 1
        else:
            bad += 1
            if len(ex) < 6:
                ex.append((os.path.basename(p)[:44], up[(topic, idx)]['idx'] + 1,
                           up[(topic, idx)]['R'], up[(topic, idx)]['C']))
    print(f"抽 {checked} 篇含指针的文件：本篇指针与本篇上游表能对上的 {ok}，对不上的 {bad}")
    for a, b, c, d in ex:
        print(f"   {a}  上游第 {b} 张 ({c}×{d}) 在本篇指针里找不到")

if __name__ == '__main__':
    main()
