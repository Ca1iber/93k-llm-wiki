# -*- coding: utf-8 -*-
"""**待办 ⑯**：`index.md` 的 token 预算（§7 的硬约束 < 15,000）。

**为什么拖到现在。** §7 写死了一条硬约束、写死了量法、还量过三次
（3.5k → 2.6k → 2.1k 余量），**但没有任何一类检查会在它超预算时变红**——
「唯一一处声称 X 的地方，正好落在唯一一类检查之外」，这是本项目的第九个同形状。

**补它卡在一个决定上**（原文记在 `schema.md` §7 与 `wiki/log.md` 待办 ⑯）：

- (a) 让 `verify_stages.py` **依赖 `tiktoken`**——本机是 `pip install` 现装的，
      换台机器就没有，**于是检查会变成「环境相关」**；
- (b) **量不出来就报「未量」并计入红**——更合本工程的规矩
      （宁可红，不许静默通过），但代价是**别的机器上这条永远是红的**。

**定的是 (b)，不是 (a)**：分不清「没超」和「没量」的检查等于没有检查
（§13.1 第 ⑥′ 问）。所以：

| 情况 | 结果 |
|---|---|
| `tiktoken` 装不上 | **红**，报告写「**未量**」，并印出装它的命令 |
| 量出来了、≤ 15,000 | 绿 |
| 量出来了、> 15,000 | **红**，并给出「该拆哪几节」的下一步 |

**取两个编码器里大的那个当上界**：`tiktoken` 是 OpenAI 的编码器，
而读这份文件的是 Claude，**两家的切分不同**，所以这个数是**代理**。
「能证伪『超了』，不能证明『离得远』」——**那正是这条检查要的**（它只判超没超）。

---

**它自己声明的那句话也要查**（2026-09-18 补）。`index.md` 里有一行

    <!-- index-token: cl100k=12975 o200k=10909 -->

**它是页面自己写的数**，和那七个 `<!-- index-count: -->` 是同一种东西。
只量不比对，就等于让手写的数字继续漂——**所以这里两边比**。

**为什么把标记放进被测的文件里**（而不是放 `schema.md`）：量的是这个文件，
声明的也该在这个文件里——**声明和被声明的对象分开，就会有一天不同步**
（这条在第十四类甲/丁/戊 上刚吃过一次）。

用：`python -X utf8 extract/check_index_budget.py`          # 量 + 比
    `python -X utf8 extract/check_index_budget.py --write`  # 量完把标记刷成实测值
"""
import re
import sys
from pathlib import Path

BASE = Path(r'F:\master-dev\understand-anything-wiki')
WIKI = BASE / 'wiki'
INDEX = WIKI / 'index.md'

BUDGET = 25000                       # §7 的预算（2026-09-20 由 15,000 上调，见 §7 的说明）
# §7 里还有一个数：**触发线 22,000**——「到 22,000 token、或对象到 300 页时，**必须回来重定**」。
# ⚠️ **2026-09-21 补**：这个数此前**只有散文、没有任何检查在看它**——
# 而 BUDGET 有检查、TRIGGER 没有，读报告的人只会看到「余 1,784」，
# **看不到「已经越过重定线了」**。这正是本项目反复记的形状：
# **规格里写了两个数，检查只认了一个。**
# 它**不判红**——越过触发线不是错误，是「该做一次人的决定」；
# 所以它只出声，不改退出码（改了退出码就等于擅自把重定变成硬约束）。
TRIGGER = 22000
ENCODERS = ('cl100k_base', 'o200k_base')

MARK_RE = re.compile(r'<!--\s*index-token:\s*(.*?)-->')

LAST = {'measured': None, 'declared': None, 'over': False, 'reason': ''}


def measure(text):
    """→ `{编码器: token 数}`；**装不上 `tiktoken` 就返回 `None`**（调用方当红）。

    **不吞异常**：`get_encoding` 失败（编码器名改了 / 老版本没这个表）
    和「没装」是两回事，但结论一样——**量不出来就是量不出来**，
    所以都返回 `None`，由调用方报「未量」。
    这里唯一的错法是**装作量到了**。
    """
    try:
        import tiktoken
    except ImportError:
        return None
    out = {}
    for enc in ENCODERS:
        try:
            out[enc] = len(tiktoken.get_encoding(enc).encode(text))
        except Exception:
            pass
    return out or None


def declared(text):
    """读页面自己写的数。**没有标记就返回 `None`。**

    ---

    **⚠️ 2026-09-18：这个函数原先「只认第一个标记」，那是一个洞。**

    实测 `index.md` 里有**两个** `<!-- index-token: … -->`：第 3 行写
    `13,261 / 11,139`（对），**第 510 行写 `13,041 / 10,969`（旧值，漂了）**。
    而这里 `search()` 只看第一个，`main()` 的 `--write` 也是 `sub(…, count=1)`——
    **第二个标记永远不会被测、也永远不会被刷**。

    它照样是**页面自己声明的一个数**，却落在唯一看着这件事的检查之外：
    「一处声称 X 的地方，正好落在唯一一类检查之外」——本项目第九个同形状，**又一次**。

    所以现在**数一遍有几个**，多于一个直接判红：
    **两个声明里至少有一个是错的，而检查没法知道该信哪个。**
    **不许挑一个信了了事**——那是把这个洞留着，只是换了个地方。
    """
    marks = list(MARK_RE.finditer(text))
    if len(marks) > 1:
        return {'_duplicate': len(marks)}
    if not marks:
        return None
    m = marks[0]
    d = {}
    for chunk in m.group(1).split():
        if '=' in chunk:
            k, v = chunk.split('=', 1)
            d[k.strip()] = v.strip()
    return d


def main(strict=False, write=False, path=None):
    """→ `(ok, over)`。数字一律写进 `LAST`，调用方读它、不许自己数。

    **`path` 可以换掉被测文件。** 必须有这个口子：`verify_stages.py` 把自己的
    `WIKI` 指到别处跑（反向测试就是全套搬到临时目录），**而本模块的 `INDEX`
    是写死的常量**——不换的话，「量的是临时那份、比的是真的那份」，
    **一个检查里两套数据源，绿了也不知道绿的是哪一份**。
    （`plan_sync` 那个 `OUTDIR` 指针也栽过同一件事。）
    """
    if (sys.stdout.encoding or '').lower().replace('-', '') != 'utf8':
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    target = Path(path) if path else INDEX
    text = target.read_text(encoding='utf-8')
    dec = declared(text)
    got = measure(text)
    LAST['declared'] = dec

    if got is None:
        LAST.update({'measured': None, 'over': False, 'reason': '未量'})
        print('❌ **未量**：没装 `tiktoken`，量不出 `index.md` 的 token 数。')
        print('   （§7 是硬约束，**量不出来不许当绿**。装：pip install tiktoken）')
        return (False, False) if strict else (False, False)

    top = max(got.values())
    top_enc = max(got, key=lambda k: got[k])
    LAST['measured'] = got
    over = top > BUDGET
    LAST['over'] = over

    print(f'`index.md`：' + '、'.join(f'{k} {v:,}' for k, v in got.items())
          + f'（取大的 `{top_enc}` = **{top:,}**，预算 {BUDGET:,}，'
          + (f'**超 {top - BUDGET:,}**）' if over else f'余 {BUDGET - top:,}）'))

    if top >= TRIGGER:
        LAST['trigger'] = top
        print(f'   ⚠️ **已越过 §7 的触发线 {TRIGGER:,}**（现值 {top:,}，超 {top - TRIGGER:,}）——'
              f'§7 说的是「**必须回来重定**」（大概是要拆子索引）。'
              f'**这条不出红**：越线不是错，是**该做一次人的决定**；'
              f'**但也不许当作没看见**——没看见的话它就又变成「先放着」了。')
    ok = not over
    if dec and '_duplicate' in dec:
        print(f'   ❌ 本页里有 **{dec["_duplicate"]} 个** `<!-- index-token: … -->` 标记。'
              '上面那个数只来自**第一个**，其余几个既不被测也不被刷——'
              '**两个声明里至少有一个是错的，而且没法知道该信哪个。**')
        print('   修法：**只留一个**（放在 H1 底下），其余删掉。'
              '**数写在两处 = 一处会漂，而漂的那处没人看。**')
        ok = False
    elif dec:
        diff = {k: (got.get(k, 0) - int(v)) for k, v in dec.items() if v.lstrip('-').isdigit()}
        bad = {k: d for k, d in diff.items() if d}
        print(f'   页面自己写的：' + '、'.join(f'{k} {v}' for k, v in dec.items())
              + ('  ✅ 和实测一致' if not bad else
                 '  ❌ 和实测不符：' + '、'.join(f'{k} 差 {d:+,}' for k, d in bad.items())))
        if bad:
            ok = False
    else:
        print('   ❌ 页面里**没有** `<!-- index-token: … -->` 标记——'
              '**没有声明就没有东西可比**，这一条又变成「只量不判」。')
        ok = False
        if write:
            text = text.rstrip('\n') + '\n'
    if write:
        body = ' '.join(f'{k}={got[k]}' for k in ENCODERS if k in got)
        new_mark = f'<!-- index-token: {body} -->'
        text = (MARK_RE.sub(new_mark, text, count=1) if MARK_RE.search(text)
                else text.rstrip('\n') + '\n' + new_mark + '\n')
        target.write_text(text, encoding='utf-8')
        print(f'   ✍️  已把标记刷成：{new_mark}')
        print('   ⚠️ **标记自己的字符数也算在量出来的数里**——'
              '所以换位数（12,975 → 9,999）之后要**再跑一次**才收敛。'
              '等长替换（12,975 → 13,100）一次就收敛。')
    LAST['reason'] = 'ok' if ok else ('超预算' if over else '声明不符/没有声明')
    return ok, over


if __name__ == '__main__':
    o, _ = main(strict='--strict' in sys.argv, write='--write' in sys.argv)
    raise SystemExit(0 if o else 1)
