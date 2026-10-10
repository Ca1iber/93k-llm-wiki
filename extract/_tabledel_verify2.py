# -*- coding: utf-8 -*-
"""§六③：把这一批【真写进去】的指针逐条回核上游。"""
import io, os, re, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tabledel as T

txt = io.open(r'C:\Users\Administrator\AppData\Local\Temp\ptrs.txt' if os.path.exists(r'C:\Users\Administrator\AppData\Local\Temp\ptrs.txt') else '/tmp/ptrs.txt',
              encoding='utf-8', errors='replace').read().split('\n')
# 每两条一组：文件 + 第N张/R×C
rows = []
cur = None
for l in txt:
    if '表格指针' in l:
        m = re.search(r'raw/([^`]+)`', l); cur = m.group(1) if m else None
    elif cur and '个有格子的' in l:
        m = re.search(r'第 (\d+) 个.*?：(\d+) 行 × (\d+) 列', l)
        if m: rows.append((cur, int(m.group(1)), int(m.group(2)), int(m.group(3))))
        cur = None
print(f"这一批写进去的指针断言: {len(rows)} 条")
up = T.enumerate_upstream()
ok = bad = 0; ex = []
for topic, n, R, C in rows:
    t = up.get((topic, n - 1))
    if t and t['R'] == R and t['C'] == C: ok += 1
    else:
        bad += 1
        if len(ex) < 8:
            ex.append((topic, n, R, C, (t['R'], t['C']) if t else '上游没这张'))
print(f"  ★ 与上游一致 : {ok}")
print(f"  ★ 与上游不符 : {bad}")
for e in ex: print("    ", e)
