# -*- coding: utf-8 -*-
"""② 批次驱动：每 100 个区域一条 commit，记 base/head。"""
import io, os, sys, json, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tabledel as T

TDC = T.TDC
N = 100


def git(*a):
    return subprocess.run(['git'] + list(a), cwd=TDC, capture_output=True,
                          text=True, encoding='utf-8').stdout.strip()


def main():
    plans = T.plan_l2_v3()
    plans.sort(key=lambda x: x[0])
    # 把 plans 摊平成「一个区域一条」，再按 N 分批
    flat = [(p, nl, a, b, blk) for p, nl, items in plans for (a, b, blk) in items]
    print(f"② 计划 {len(flat)} 个区域 / {len(plans)} 篇，分 {(len(flat)+N-1)//N} 批")
    batches = []
    for start in range(0, len(flat), N):
        chunk = flat[start:start + N]
        base = git('rev-parse', 'HEAD')
        byfile = {}
        for p, nl, a, b, blk in chunk: byfile.setdefault(p, (nl, []))[1].append((a, b, blk))
        nreg = 0
        for p, (nl, items) in byfile.items():
            lines, _ = T.split_lines(T.read(p))
            for a, b, blk in sorted(items, key=lambda x: -x[0]): lines[a:b] = blk
            io.open(p, 'w', encoding='utf-8', newline='').write(nl.join(lines))
            nreg += len(items)
        subprocess.run(['git', 'add', '-A', 'agent-markdown'], cwd=TDC, capture_output=True)
        msg = f"表格指针化（压平区②）第 {start+1}-{start+nreg} 个区域：{len(byfile)} 篇"
        subprocess.run(['git', 'commit', '-q', '-m', msg], cwd=TDC, capture_output=True)
        head = git('rev-parse', 'HEAD')
        batches.append(dict(batch=len(batches)+1, lo=start+1, hi=start+nreg,
                            base_commit=base, head_commit=head,
                            files=len(byfile), regions=nreg))
        print(f"  批 {len(batches):2}  {start+1:5}-{start+nreg:<5} {len(byfile):3} 篇  {head[:8]}")
    io.open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         '_assign_tabledel_l2.json'), 'w', encoding='utf-8'
            ).write(json.dumps(batches, ensure_ascii=False, indent=1))
    print(f"\n完成 {sum(b['regions'] for b in batches)} 个区域，{len(batches)} 个 commit")


if __name__ == '__main__':
    main()
