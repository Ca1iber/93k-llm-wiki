# 第七类放过去的一处真缺陷 —— **两道闸，各漏一点**

发现时间：2026-09-24（补页第二批）
发现方式：写页的 agent 在**别的页面**上撞见它，报给了主会话。

## 现象

`wiki/objects/hardware-bin-summary-tab.md` 里有一段自称逐字的引文：

```
**原文逐字（`## Table` 一节末段）：**

> 「…This is indicated by a triangle. Clicking again sorts the table by the
> column in descending order, which is indicated by an upside-down triangle. Clicking again unsorts
> the table. …」
```

而 raw 那一段逐字是（**中间夹着两张行内插图**）：

```
…This is indicated by a triangle ![Data log summary view_Ascending triangle](<../../../../raw/136425.png>). Clicking again sorts the table by the column in descending order, which is indicated by an upside-down triangle ![Data log summary view_Descending triangle](<../../../../raw/136426.png>). Clicking again unsorts the table. …
```

**页面丢了两处 `![…](<…>)` 标记，还把 `triangle ` 改成了 `triangle.`。**
**第七类当时报的是「✅ 对不上的 1 处，其中页面自称「逐字」的 0 处」，放行。**

## 两道闸各漏一点，合起来就放行了

| 闸 | 该拦的理由 | 为什么没拦住 |
|---|---|---|
| **覆盖率闸**（`cov >= 0.8`） | 引文对不上 3 个窗、覆盖率 80% | **正好卡在阈值上**——`>=` 是闭区间，80% 算过 |
| **「自称逐字」识别** | 页面写的是 `**原文逐字（…）：**` | **它认不出这个写法**，于是「自称逐字」计 0，**不按硬标准判** |

两道闸**单看都合理**：留一点余量给排版差异；只对明确自称逐字的严判。
**合起来的效果是**：一段 20% 错的引文、配上一个它认不出的自称写法，**全绿通过**。

> 这正是本项目反复记的那个形状——**「检查比它自称的范围窄」**。
> 但这一次的形态新一点：**不是一条判据窄，是两条判据的余量叠在一起**。
> 每条单看都在自己的余量内，**叠加之后余量的乘积就是漏洞**。

## 处置

- **那一处已修**：按 §11.1「截取只许在引文块的头尾，块内部必须连续；真要跳就断开成两个引文块」
  断成**三块**，两块图用散文夹在中间写明（`…136425.png` / `…136426.png`，并注明本页没看）。
  修完第七类报 **对不上的 0 处**（原来是 1 处 / 覆盖率 80%）。
- **两道闸本身一个字没改** —— 改判据要另议，且这一处的教训是「余量会叠加」，
  不是「阈值该调成 0.9」。**先把这处记下来。**

## 复算

```bash
cd F:\master-dev\understand-anything-wiki
python -X utf8 extract/verify_stages.py | grep -A 2 'hardware-bin-summary-tab.md'
```
修前该页报「对不上的 1 处」；修后「对不上的 0 处」。

---

## 第二个洞（2026-09-24 补）：**含中文的引文块，第七类一个都不看**

发现方式：写 `vpin` 页的 agent **自查时抓到一处真错**，而它**不在第七类的报告里**——
追下去发现：那个 `>` 块里夹了中文，而第七类的判据**只收不含 CJK 的块**（§13.1 第八次记的）。
错的是：把 `An error occurs if:` 与下面那条带 `- ` 列表符的行**合成了一句引文**，
**丢了列表符**（§11.1「丢了字符就算错」）。

### 有多大

```bash
cd F:\master-dev\understand-anything-wiki
python -X utf8 - <<'PY'
import pathlib, re
CJK = re.compile(r'[\u4e00-\u9fff]')
tot = skip = 0
for p in pathlib.Path('wiki').rglob('*.md'):
    if p.name in ('index.md', 'log.md') or p.name.startswith('index-'):
        continue
    t = p.read_text(encoding='utf-8')
    for blk in re.findall(r'(?:^>.*\n?)+', t, re.M):
        tot += 1
        if CJK.search(blk):
            skip += 1
print(tot, skip, f'{skip/tot:.1%}')
PY
```

实测 **5,129 个 `>` 引文块，其中 1,418 个（27.6%）含中文、一律不被检查。**

### 为什么这个洞比上一个严重

上一个（80% 覆盖率）影响的是**边界情形**；这一个影响的是**四分之一以上的引文**，
而且**这工程的页面本来就是中文写的**——引文常常写成
「> 原文写着 `An error occurs if:` —— 然后……」这种中英混排。
**混排越自然，越不在检查范围内。**

与 §13.1 第八次同源（那次是「只收不含 CJK 的块」被当成一条小限制记下来的），
**但那次没人量过它盖掉了多少**。量了才知道是 27.6%。

### 处置

**判据一个字没改。** 改它要想清楚：CJK 块里哪部分是引文、哪部分是作者的话，
**机器分不出来**（这正是当初把它排除的理由）。要收，得先有一个**标记引文边界**的写法
（例如规定引文必须独立成块、作者的话不许与引文同段）。
**在那之前，这 1,418 块只有靠写页的人自查。**
