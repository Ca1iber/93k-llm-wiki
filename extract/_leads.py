"""一次性探针：把第七类「疑似自加结构」的**全部**命中打出来（报告只印前 5 条）。

用途：把筛查项的命中逐条回原文归类，判它是真缺陷还是滑窗接缝的误报。
**这是诊断脚本，不是检验的一部分**——它不改任何判据，只把已有的名单摊开。
原话是「用完即弃（不留：它一旦被当成检验，就又多一份要维护的规格）」。但
`baseline: git 接管` 那次**整体入库**把它一起收了进来（`wiki/log.md` 也引着它当那次诊断的凭据）。
**事实是它在库里，那就把话说对：留着，但它不是检验，别当规格维护。**

**上一版这个探针报 `units=2461 failing=2461`**：它没加载 `docs_by_rel_cache`
（那是 `main()` 里才填的），于是每一块都在空语料里查，**必然全灭**。
`cat7` 自己有一句 `assert len(wsfree) > 1_000_000` 挡住了这个坑，
我跳过 `cat7` 就等于跳过了那句断言。**这里把它原样补上。**
"""
import json
import re
import sys

sys.path.insert(0, r'F:\master-dev\understand-anything-wiki\extract')
import verify_stages as V

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

_docs = {d['rel']: d
         for l in (V.OUTDIR / 'docs.jsonl').open(encoding='utf-8')
         for d in [json.loads(l)]}
V.docs_by_rel_cache.extend(_docs)

normed = {}
for rel in V.docs_by_rel_cache:
    t = (V.CORPUS / rel).read_text(encoding='utf-8', errors='replace')
    if t.startswith('---'):
        i = t.find('\n---', 3)
        if i > 0:
            t = t[i + 4:]
    normed[rel] = V._norm(t)
blob = '\x00'.join(normed.values())
wsfree = re.sub(r'\s+', '', blob)
assert len(wsfree) > 1_000_000, f'语料没加载上（{len(wsfree)} 字符）'
print(f'语料：{len(normed)} 篇 / {len(wsfree)} 字符（去空白）')

for p in sorted(V.WIKI.rglob('*.md')):
    if V._skip_prose(p):
        continue
    s = str(p.relative_to(V.WIKI)).replace('\\', '/')
    _, body = V.parse_page(p)
    for b in V._extract_quotes(body):
        units = b['lines'] if (b['kind'] == 'fence' and b['lines']) \
            else V._windows(b['text'])
        for u in units:
            if V._hit(u, blob, wsfree) == 0 and (
                    u.startswith('- ') or ' - ' in u or '…' in u or '...' in u):
                print(f'\n[{s}]')
                print(f'  unit: {u}')
