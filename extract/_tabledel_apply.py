# -*- coding: utf-8 -*-
"""① 批次驱动：每 100 张表一条 commit，记 base/head。"""
import io, os, sys, json, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tabledel as T

TDC = T.TDC
N = 100


def git(*a):
    return subprocess.run(['git'] + list(a), cwd=TDC, capture_output=True,
                          text=True, encoding='utf-8').stdout.strip()


def main():
    plan, exc = T.plan_l1()
    plan.sort(key=lambda x: x[0])
    print(f"① 计划 {len(plan)} 处，分 {(len(plan)+N-1)//N} 批")
    batches = []
    for start in range(0, len(plan), N):
        chunk = plan[start:start + N]
        base = git('rev-parse', 'HEAD')
        recs, n = T.apply_plan(chunk, dry=False)
        files = sorted({r['md'] for r in recs})
        subprocess.run(['git', 'add', '-A', 'agent-markdown'], cwd=TDC,
                       capture_output=True)
        msg = (f"表格指针化（已修表①）第 {start+1}-{start+n} 张："
               f"{len(files)} 篇，删表 {n} 张")
        subprocess.run(['git', 'commit', '-q', '-m', msg], cwd=TDC, capture_output=True)
        head = git('rev-parse', 'HEAD')
        batches.append(dict(batch=len(batches) + 1, lo=start + 1, hi=start + n,
                            base_commit=base, head_commit=head,
                            files=len(files), tables=n))
        print(f"  批 {len(batches):2}  {start+1:5}-{start+n:<5} {len(files):3} 篇  {head[:8]}")
    io.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '_assign_tabledel_l1.json'),
            'w', encoding='utf-8').write(json.dumps(batches, ensure_ascii=False, indent=1))
    print(f"\n完成 {sum(b['tables'] for b in batches)} 张，{len(batches)} 个 commit")


if __name__ == '__main__':
    main()
