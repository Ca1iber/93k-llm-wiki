# 待处置：6 页的 `title` 和 H1 填成了**源文档的标题**，于是撞在一起

发现时间：2026-09-21
发现方式：**本来在查另一件事**——怀疑「同一对象被建成了两页」。
查完发现那个怀疑是错的，**但顺手查出了这个**。

---

## 一、先记下**不成立**的那个怀疑（免得以后有人再查一遍）

`objects/smartcalc.md` 与 `objects/smartcalc-framework.md`：
同一篇源文档、同样的「语法 / 参数」节（逐字相同）、同样是 `type: object`、同样是 `layer: L2`。
看起来像重复建页。

**不是。** `wiki-plan.csv` 的 `note` 列写着：

> `smartcalc` … **分界已定：本页讲「怎么调」（API 侧），`smartcalc-framework` 讲「为什么、是什么」**

而且**「一篇文档喂多个 slug」在计划里是常态**：`wiki-plan.csv` 267 行里有 **15 组**，
绝大多数是**不同类型的页**（约束 + 对象、映射 + 对象、阶段 + 约束），
每页在 `note` 列里都写明了各讲什么。

**结论：这是设计，不是 bug。没有重复页。**

---

## 二、真问题：`title` / H1 填的是源文档的标题

既然「一篇文档喂多页」是常态，那就该**每页各有各的标题**——
上面那 15 组里 **13 组确实各不同**（`level`「Level — 电平配置」/ `timing`「Timing / Wavetable — 波形与时序设置」/ `device-directory`「Device directory structure」…），
说明**规矩本来就是「各页各标题」**。

**但有 2 组全同：**

| 源文档 | 页 | `title` 与 H1 |
|---|---|---|
| `02.07.02.02.02_How_to_create_a_universal_test_method_class` | `concepts/how-to-create-a-universal-test-method-class` | How to create a universal test method class ✅ **这页是对的** |
| 同上 | `objects/pin-string` | How to create a universal test method class ❌ |
| 同上 | `concepts/context-pins` | How to create a universal test method class ❌ |
| 同上 | `objects/file-string` | How to create a universal test method class ❌ |
| 同上 | `objects/option-list` | How to create a universal test method class ❌ |
| `02.07.10_SmartCalc_framework` | `objects/smartcalc-framework` | SmartCalc framework ⚠️ |
| 同上 | `objects/smartcalc` | SmartCalc framework ⚠️ |

**卷入 7 页；其中 6 页的标题是错的**（那 5 页组的「正主」那页标题本来就是对的）。

**正文是好的。** 抽 `objects/file-string.md` 核过：`## 是什么` 通篇在讲 FileString
（「**FileString 是 test method 参数的一种类型**」），**只有 `title:` 字段和顶上的 H1 串了**。
`smartcalc` 那两页也一样——两页正文各讲各的（一页「怎么调」、一页「为什么/是什么」），
**只有标题没区分**。

**影响**：标题是读者看到的第一行，也是 `index.md` 之外唯一的「这东西叫什么」。
**5 页共用一个标题之后，从标题看不出哪页是哪页**——上面那 4 页对象页，
从「How to create a universal test method class」这个标题，读者猜不到里面讲的是 PinString。

**为什么会这样（推断，未证实）**：这几页是**从同一篇文档的同一批子主题**生成的，
生成时把**源文档的标题**当成了页面标题，没有换成每页各自的主题。
`wiki-plan.csv` 的 `note` 列里**每页的主题都写清楚了**，说明计划那一侧是分得开的，
**是页面这一侧没跟上**。

---

## 三、为什么十五类全绿也看不见它

- **第六类**只查 `title` **在不在**（`need = ['type','title','tags',…]` 那张必需字段表），
  **不查它对不对**。「是个非空字符串」就过。
- **第十一类**查的是**「层」**的跨页一致性（同一对象在两页里被标成不同层），
  **不碰标题**。
- **第十四类**管 `index.md` 的自我声明，不管 412 个页面的 `title` 字段。

**又是一次「检查比它自称的范围窄」**——第六类的名字叫「格式齐」，
它确实只保证**齐**，不保证**对**。而「齐」和「对」之间差着这 6 页。

> 这一条的特别之处：**它不是「判据查错方向」，是「判据只查有没有、不查是什么」。**
> 前几次记的都是范围问题（漏了哪些页 / 哪些块），这一次漏的是**同一个字段的另一半属性**。

---

## 四、复核办法

```bash
cd F:\master-dev\understand-anything-wiki\wiki
python -X utf8 - <<'PY'
import re, pathlib, collections
by_t = collections.defaultdict(list)
for p in pathlib.Path('.').rglob('*.md'):
    t = p.read_text(encoding='utf-8')
    if not t.startswith('---\n'): continue
    fm = t[4:].split('\n---\n', 1)[0]
    ti = (re.search(r'^title:\s*(.*)$', fm, re.M) or [None, ''])[1].strip()
    if ti: by_t[ti].append(p.as_posix())
for ti, ps in sorted(by_t.items()):
    if len(ps) > 1:
        print(f'「{ti}」')
        for p in ps: print('   ', p)
PY
```

预期输出：**2 组**（5 页 + 2 页）。若多于 2 组，说明又长出了新的。

## 五、处置 —— **未处置**

**要改的是 6 页**（`how-to-create-a-universal-test-method-class` 那页不动）。
每页要动**两处**：frontmatter 的 `title:` 和正文顶上的 `# `（H1）——**两处同错，要一起改**。

正确的标题**抄 `wiki-plan.csv` 的 `note` 列**，那一列本来就是给这个用的：

| 页 | 现标题（错） | 该改成（据 plan 的 note） |
|---|---|---|
| `objects/pin-string` | How to create a universal test method class | test method 参数类型 PinString |
| `concepts/context-pins` | 同上 | test method 参数类型 ContextPins |
| `objects/file-string` | 同上 | test method 参数类型 FileString |
| `objects/option-list` | 同上 | test method 参数类型 OptionList |
| `objects/smartcalc-framework` | SmartCalc framework | （讲「为什么 / 是什么」那侧，措辞待定） |
| `objects/smartcalc` | SmartCalc framework | （讲「怎么调」那侧，措辞待定） |

**`smartcalc` 那两页的措辞没现成的**——`note` 里写的是「怎么调」/「为什么、是什么」，
是**分界说明**不是**标题**。这两页的标题要**人写**，不能从 `note` 直接抄。

**⚠️ 改标题算不算动散文？** 不算——`title` 是 §6 的字段，
`extract/PROSE-SPEC.md` 第 2 条明说写散文的 agent **不许动** `type`/`title`/`layer`/`stage`/`sources`/`created`/`verified`。
所以这 6 页只能由**主会话**改，不能派 agent 改。

## 六、与另一件事的关系

[[findings-stage-object-coverage]]：同一轮查出来的另一笔账（70 个对象页没被阶段页点名）。
**两笔都不影响用，都是「少了一层索引」，不是「内容错」。**
