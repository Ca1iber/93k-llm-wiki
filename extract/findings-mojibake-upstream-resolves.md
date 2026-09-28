# `鈥` / `鈼` / `鈩` 那族坏字：**上游有正字，所以是可修的**

发现时间：2026-09-24（补页第三批）
发现方式：写 `wfds` 页的 agent 核上游 `.htm`，发现语料里的 `鈮?` 在上游是干净的 `≤`。

## 工程原来的结论（§11.2 ①）**要被推翻**

原来记的是：

> `鈥?`：三字节字符**第三字节被 `?` 替掉**的一族，**不唯一**，落在 `U+2100–U+213F`；
> **（推断）**语境看是 `™`，按 §11.2 **不许当映射用**。

而且**记成了不可修的语料损坏**（当时的口径：2,889 处 / 531 篇）。
理由听起来是硬的：**第三字节没了，所以定不出是哪个字**。

## 那句话少说了一个前提：**上游还在**

`tdc-html/raw/<source_topic>.htm` 是转换的**输入**。若它没坏，**正字就在里面**——
不需要猜、不需要映射表、不需要「唯一性」。这正是 §1.2 对 A 类的定义：
**「上游明写着原意，转换时被毁」**。

## 实测（全库，2026-09-24）

判据：语料一侧用 `[鈥鈼鈩].` 扫；再按 frontmatter 的 `source_topic` 取上游 `.htm`，
**看那一篇的 `.htm` 里还有没有坏字**。

| | |
|---|---|
| 坏字处数 | **3,220** |
| 涉及篇数 | **605** |
| **上游 `.htm` 干净**（正字取得到） | **602 篇（99.5%）** |
| 上游 `.htm` 也坏 | **0 篇** |
| `.htm` 不在 | 3 篇 |

**没有一篇是「上游也坏」的。** 三篇 `.htm` 不在的：`Hardware_view` / `Utility_Line_view` /
`Profiling_of_DC_Scale_cards_with_Hardware_view` 的投放件。

## 已知的一个限制（别把它说满）

上面那个判据是**按篇**的（这一篇的 `.htm` 里有没有坏字），**不是按处**的。
「这一篇的 `.htm` 干净」**不等于**「这一篇里每一处坏字都能在上游一一对上」——
要按处对上，得先有一份**能把 md 里的那一处映射回 `.htm` 里那一段**的判据，
而那正是 `findings` 里另一个待办（`\\.Note ` 那 336 处也卡在同一件事上：
**218/336 定位失败**）。

**所以本文给的是「这条路存在、而且大概率通」，不是「3,220 处逐处已对上」。**

## 处置

**一个字没动。** §1.2 的流程是**先摆证据 → 经人批准 → 改 → 记 log → 重跑 extract**。
这份文件是第一步。要不要做、先在哪一层做（md 还是 raw）、`≤` 这类符号要不要
连**上游自己的 HTML 实体**一起抄，都要人定。

## 复算

```bash
cd F:\master-dev\understand-anything-wiki
python -X utf8 - <<'PY'
import pathlib, re
C = pathlib.Path(r'F:\master-dev\dorm-wsl-sytest\tdc-html\agent-markdown\by-category')
R = pathlib.Path(r'F:\master-dev\dorm-wsl-sytest\tdc-html\raw')
bad = re.compile(r'鈥.|鈼.|鈩.')
clean = dirty = nohtm = 0
for p in C.rglob('*.md'):
    t = p.read_text(encoding='utf-8', errors='replace')
    if not bad.search(t):
        continue
    m = re.search(r'^source_topic:\s*["\']?([^"\'\s]+)', t, re.M)
    h = R / f"{m.group(1).replace('.htm','')}.htm" if m else None
    if not h or not h.exists():
        nohtm += 1
    elif bad.search(h.read_text(encoding='utf-8', errors='replace')):
        dirty += 1
    else:
        clean += 1
print(f'上游干净 {clean} / 上游也坏 {dirty} / htm 不在 {nohtm}')
PY
```
