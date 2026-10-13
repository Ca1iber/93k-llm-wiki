# -*- coding: utf-8 -*-
"""补回被 `?` 吃掉的空格：上游 `™ connecting` 里，`™` 的第三字节和后面的空格
被一起吃掉（`A2 20` 凑不成合法 GBK 对），换回 `™` 后空格没了。
判据：`™` 紧夹在两个字母数字之间 → 补一个空格。（只做 `™`，它后面在原文档里总跟着空格。）"""
import io, os, re, sys, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tabledel as T

n = 0; files = 0
for dp, _, fns in os.walk(T.MD):
    for fn in fns:
        if not fn.endswith('.md'): continue
        p = os.path.join(dp, fn)
        s = T.read(p)
        if '™' not in s: continue
        out = re.sub(r'(?<=[0-9A-Za-z])™(?=[0-9A-Za-z])', '™ ', s)
        if out != s:
            n += len(re.findall(r'(?<=[0-9A-Za-z])™(?=[0-9A-Za-z])', s))
            files += 1
            io.open(p, 'w', encoding='utf-8', newline='').write(out)
print(f'补空格 {n} 处 / {files} 篇')
if n:
    subprocess.run(['git', 'add', '-A', 'agent-markdown'], cwd=T.TDC, capture_output=True)
    subprocess.run(['git', 'commit', '-q', '-m', f'补回被吃掉的空格：™ 前后紧邻字母数字处补一个，{n} 处'],
                   cwd=T.TDC, capture_output=True)
    print(subprocess.run(['git', 'log', '--oneline', '-1'], cwd=T.TDC, capture_output=True,
                         text=True, encoding='utf-8').stdout.strip())
