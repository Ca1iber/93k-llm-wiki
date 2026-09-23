#!/usr/bin/env python -X utf8
# -*- coding: utf-8 -*-
"""
A 类修复的**下游**：把 wiki 页**散文**里被拍平的数字改回 `^` 写法。

为什么必须改：wiki 页是**引用** raw 的。raw 改了而 wiki 不改，
第七类检查（wiki 引文与语料逐字相同）会反过来判 wiki 失败——
**wiki 就变成在错引自己的 raw 层。**

## 只管散文。**脚本写的那两节一个字都不许碰。**

页面里有 **两节是脚本写的**（§4：脚本能产出的不许 LLM 改）：

| 节 | 边界标记 | 谁生成 |
|---|---|---|
| `## 语法 / 参数` | `<!-- 语法节 begin -->` … `<!-- 语法节 end -->` | `objscaffold.syntax_block()` |
| `## 报错条件` | `<!-- 报错节 begin -->` … `<!-- 报错节 end -->` | `objscaffold.error_block()` |

**改它们有两个后果，那天都真的发生了：**

1. **改了会白改。** `MARK_BEGIN` 那行自己就写着「**手改会在下次
   `--refresh-syntax` 时消失**」——**工具早警告过，我没读到。**
2. **改了会改错。** 这一节的内容按各篇原始文档分别抽取；**同一句雷同的话
   在 8 篇文档里出现时，对证判据分不出 wiki 里那句是从哪一篇来的**，
   于是把「上游 HTML 本来就写着 `248`」的那两处也一并"修"了。
   → **对证判据的盲区**：它能证明「这句话在语料**某处**长这样」，
   **不能证明「这句话是从哪一篇来的」**。
   **这一次是第十二类（页面 ↔ 脚本逐字节）抓出来的，不是本脚本自己。**

正解：**别碰它，让脚本重刷** ——
`python objscaffold.py --refresh-syntax <slug>...`，脚本会按修好的 raw 重新生成。

## 判据（只有一条，不靠关键词猜语境）

把候选处的粘连数字改写成 `2^N`，**去修好的语料里搜**：
搜得到（且匹配段必须**包含这个指数**）→ 真损坏；搜不到 → 无关数字（`MCB231`、`RS-232`、`Specification 102`）。

> **教训一**：先前用「幂语境关键词」（`range of` / `between 0 and` …）当过滤，
> 漏掉了 `range 0 to`、`between 1 and`、`range for` 这些同义说法——**真数 91，只改到 49**。
> **过滤式判据会把「我没想到的写法」判成没问题。** 只有回到证据才能兜住。
>
> **教训二**：兜住了「漏」，却出了「错」——见上面那两节。
> **判据不自证**：它对散文成立，对脚本那一节不成立。**范围要和判据一起写死。**

## 搜索范围（**两侧都要写死，不然判据会自己变宽或变窄**）

**一、语料侧**：只搜**那 60 篇有过损坏的文件**（约 460 KB），不搜全库 26 MB——
wiki 里出现损坏拷贝，来源只可能是这 60 篇。快 80 倍，判据一样硬。

**二、wiki 侧**：只扫**页面**（`wiki/` 下那 7 个目录），
**不扫 `wiki/index.md`（目录）与 `wiki/log.md`（改动记录）**。

- **`wiki/log.md` 里有意引着「改前」的形态当证据**（`0 to248 - 1`、`231 - 1`…）。
  **扫它 = 有机会把记录改成假的**——那是 A 类修复唯一的账，比页面上的数字重要得多。
- `wiki/index.md` 列的是页名与链接，不是散文。

> **这一条是被一次「计数对不上」逼出来的。** 2026-09-23 往 log 里追加了一段文字之后，
> 「跳过候选」从 7662 变成 7664。查下去：`log.md` 里有 `语法节 begin` ×6、**`end` ×0**，
> 而 `owned_spans()` 找不到 `end` 时**保守地一路划到文件尾**——
> 于是 `log.md` **整篇**都被当成「脚本管的范围」跳过了。
>
> **也就是说：此前 `log.md` 没被误改，靠的是这个兜底碰巧盖住了它，不是判据在管它。**
> **靠碰巧保护住的东西不算保护**——兜底是给页面写的，`log.md` 只是搭了个便车。
>
> **排除是具名且可证伪的**：脚本先断言 `wiki/` 根下**只有**这两个非页面文件。
> **多出第三个就直接报错**——宁可停下问一句，也不许它悄悄落在扫描范围之外
> （「范围比自称的窄」这个毛病，本项目已经犯过很多次）。

用法：
    python -X utf8 fix_wiki_superscript.py            # 空跑
    python -X utf8 fix_wiki_superscript.py --apply    # 真改

依据：schema.md §1.2。上游清单：extract/_assign.json。
"""
import json, re, sys, pathlib, collections

WIKI = pathlib.Path(r'F:\master-dev\understand-anything-wiki')
APPLY = '--apply' in sys.argv

# 脚本写的两节——**只认标记，不认别的**（同 objscaffold 的道理：边界由写它的人留记号）
OWNED = [
    ('<!-- 语法节 begin', '<!-- 语法节 end -->',              '语法节'),
    ('<!-- 报错节 begin', '<!-- 报错节 end -->',              '报错节'),
]


def owned_spans(txt):
    """返回页面里**脚本管**的字符区间列表。找不到 end 时保守取到文件末——
    **宁可不改，不可改错**。"""
    out = []
    for b, e, _ in OWNED:
        for m in re.finditer(re.escape(b), txt):
            i = m.start()
            j = txt.find(e, i)
            out.append((i, len(txt) if j < 0 else j + len(e)))
    return out


def in_owned(spans, pos):
    return any(a <= pos < b for a, b in spans)


# ── 有意引用的「改前」形态——**不是待修项** ──────────────────────────────
#
# 标注里引旧值当证据（「修前的 markdown 写的是 `… 231 - 1`」），**引文本身必须保持原样**，
# 否则那段记录就假了。判据分不出「引用」和「断言」——这是它的第三处盲区。
#
# **例外具名、可证伪**：这一串必须还在页里。**不在了就说明标注被删或被改，
# 例外立刻失效并报错**——不是「我知道它没问题」，是「每次运行都验一遍」。
QUOTED_OLD = [
    ('wiki/objects/vector-setup-file.md',
     '`the first parameter of PRBS is set to its maximum value 231 - 1`',
     '标注 ④ 有意引的「修前」形态'),
    ('wiki/objects/vector-setup-file.md',
     '`the second parameter, which is also set to its maximum value 212 - 1`',
     '标注 ④ 有意引的「修前」形态'),
]


def check_quoted_old():
    """每次运行都验那两串还在。**失效要响。**"""
    for rel, s, why in QUOTED_OLD:
        p = WIKI / rel
        if s not in p.read_bytes().decode('utf-8', 'replace'):
            raise SystemExit(f'❌ 例外失效：{rel} 里已找不到 {s!r}（{why}）——'
                             f'标注被删或被改了，请人工看一眼再跑')


A = json.loads((WIKI / 'extract' / '_assign.json').read_text(encoding='utf-8'))
tok2 = {}
for a in A:
    tok2.setdefault(a['lit'], (a['base'], a['exp']))

fixed = ' '.join(re.sub(r'\s+', ' ', p.read_bytes().decode('utf-8', 'replace'))
                 for p in sorted({pathlib.Path(a['md']) for a in A}))
print(f'语料比对串：{len({a["md"] for a in A})} 篇 / {len(fixed):,} 字符')

check_quoted_old()

# ── wiki 侧的范围：**只扫页面** ─────────────────────────────────────
#
# 不扫 `wiki/index.md`（目录）与 `wiki/log.md`（改动记录）。
# **`log.md` 里有意引着「改前」的形态当证据**——扫它就可能把记录改成假的。
#
# 这个排除**具名且可证伪**：先断言根下**只有**这两个非页面文件。
# 多出第三个就报错——**宁可停下问一句，也不许它悄悄落在范围之外。**
PAGE_DIRS = ('concepts', 'constraints', 'errors', 'mappings', 'objects', 'stages', 'versions')
NOT_PAGE = {'index.md': '目录：列的是页名与链接，不是散文',
            'log.md': '改动记录：**里面有意引着「改前」的形态当证据，扫它会把记录改成假的**'}

_root_md = sorted(p.name for p in (WIKI / 'wiki').glob('*.md'))
if _root_md != sorted(NOT_PAGE):
    raise SystemExit(f'❌ wiki/ 根下的 md 变了：{_root_md}（清单里是 {sorted(NOT_PAGE)}）。\n'
                     f'   范围是靠这份清单写死的——**多出来的那个算不算页面？先看它，再改清单。**')
pages = sorted(p for d in PAGE_DIRS for p in (WIKI / 'wiki' / d).rglob('*.md'))
print(f'扫描范围：{len(pages)} 个页面（{" ".join(PAGE_DIRS)}）；'
      f'跳过非页面 {sorted(NOT_PAGE)}')

hits, skipped, quoted = [], 0, 0
for pg in pages:
    txt = pg.read_bytes().decode('utf-8', 'replace')
    spans = owned_spans(txt)
    rel = pg.relative_to(WIKI).as_posix()
    # 例外按**出现区间**算，不按「附近」算——两串挨得近时，±N 的窗会漏掉后一串。
    old_spans = [(m.start(), m.end()) for r, s, _ in QUOTED_OLD if r == rel
                 for m in re.finditer(re.escape(s), txt)]
    for tok, (base, exp) in tok2.items():
        for m in re.finditer(r'(?<![\d.])' + re.escape(tok) + r'(?!\d)', txt):
            i = m.start()
            if in_owned(spans, i):
                skipped += 1
                continue                      # ★ 脚本写的那一节：不碰
            lo, hi = max(0, i - 90), i + len(tok) + 70
            win = txt[lo:hi]
            if any(a <= i < b for a, b in old_spans):
                quoted += 1
                continue                      # ★ 有意引的「改前」形态：不碰
            if '.md' in win or '](<' in win or 'http' in win:
                continue                      # 路径 / 链接里的数字
            corr = re.sub(r'\s+', ' ', win[:i - lo] + base + '^' + exp + win[i - lo + len(tok):]).strip()
            key = base + '^' + exp
            pos = corr.find(key)
            if pos < 0:
                continue
            for L in (80, 70, 60, 50, 40, 34, 28, 24):
                found = False
                for st in range(max(0, pos - L + 8), pos + 1):
                    s = corr[st:st + L]
                    if len(s) >= 24 and key in s and s in fixed:   # ★ 匹配段必须含该指数
                        found = True
                        break
                if found:
                    hits.append((pg, i, tok, L))
                    break

by = collections.defaultdict(list)
for pg, i, tok, L in hits:
    by[pg].append((i, tok, L))
print(f'\n散文里对证成立 {len(hits)} 处 / {len(by)} 页'
      f'   （脚本写的那两节跳过 {skipped} 处候选、有意引的「改前」形态跳过 {quoted} 处）')
for pg, hs in sorted(by.items(), key=lambda kv: str(kv[0])):
    print(f'  {pg.relative_to(WIKI).as_posix():<48} {len(hs)} 处')

if not APPLY:
    print('\n[空跑] 未改任何文件。')
    sys.exit(0)

for pg, hs in sorted(by.items(), key=lambda kv: str(kv[0])):
    raw = pg.read_bytes()
    txt = raw.decode('utf-8', 'replace')
    if txt.encode('utf-8') != raw:
        print(f'  !! 跳过（utf-8 往返不安全）：{pg.name}')
        continue
    spans = owned_spans(txt)
    for i, tok, L in sorted(hs, key=lambda x: -x[0]):
        assert not in_owned(spans, i), f'{pg.name}@{i} 落在脚本管的节里——判据有变，停'
        base, exp = tok2[tok]
        assert txt[i:i + len(tok)] == tok, f'{pg.name}@{i} 期望 {tok!r}'
        txt = txt[:i] + base + '^' + exp + txt[i + len(tok):]
    pg.write_bytes(txt.encode('utf-8'))
print(f'\n[已改] {len(hits)} 处 / {len(by)} 页')
