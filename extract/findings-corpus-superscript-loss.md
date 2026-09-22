# 语料损坏：**151 处**上标在 HTML→markdown 转换时被拍平，全变成错误的数

发现时间：2026-09-22
发现方式：**人先发现的**（`2^48` → `248`），然后脚本精确对账 HTML 与 markdown 把范围查全。
归属：**(c) 语料本身如此 → 记录**。**但 2026-09-22 起，这一类被单独立为「A 类」，可以改**
（见 `schema.md` §1.2）——**本文只记录，尚未改。**

---

## 一、逐字证据

`EMAP`（`02.06.02.02.103`，源 HTML `98590.htm`）：

```
HTML      : The range for this parameter is 0 to2<sup>48</sup> - 1.
markdown  : The range for this parameter is 0 to248 - 1.
```

`GETV`（`02.06.02.02.135`）：

```
HTML      : ... must be in the range 0 to 2147483648 (2<sup>31</sup>).
markdown  : ... must be in the range 0 to 2147483648 (231).
```

> ⚠️ **两个缺陷叠在一起，别记成一件。**
> HTML 源里**本来就是 `0 to2`，没有空格**——`to248` 里丢的那个空格**不是转换丢的**。
> 转换只干了第二件事：把 `<sup>48</sup>` 拍平成 `48`。

## 二、精确范围（脚本对账，不是抽样）

对 `tdc-html/raw/` 全部 9,351 个 htm/html 与 9,393 篇 markdown 逐篇对照：

| 项 | 数 |
|---|---|
| HTML 里 `<sup>` 总数 | **1,720**（376 个文件） |
| 其中「**内容纯数字 + 前面紧贴数字**」 | **151 处**（**60 个文件**） |
| 这 151 处**被拍平成粘连字面量**的 | **151 / 151 = 100%** |
| 受影响 markdown 文档 | **60 篇** |
| 找不到对应 markdown 的 | **0**（映射完整） |

**指数取值——全是 2 的幂和 10 的幂：**

```
2^48  ×70    2^31  ×18    2^21  ×14    2^32   ×7    2^12  ×7
2^7   ×5     2^24  ×4     2^18  ×4     2^5    ×4    2^3   ×3
2^16  ×3     2^2   ×2     2^19  ×2     2^15   ×1    2^23  ×1    2^28  ×1
10^18 ×2     10^7  ×1     10^9  ×1     10^2   ×1
```

**偏偏是这两种**——文档讲「范围 / 上限」用的就是它们。
**`2^48` = 281,474,976,710,656，拍平后写成 `248`。丢一个上标，从 2.8×10¹⁴ 变成 248。**

## 三、为什么十五类检查一条都看不见它

**因为语料就是基准。** 所有检查做的是「wiki ↔ 语料」比对。
**语料自己错了，一个忠实的 wiki 页在每一类检查下都是绿的。**

- 第六类查 frontmatter 字段**在不在** → 与数字无关
- 第七类查 wiki 引文与语料**逐字相同** → **语料错，页也跟着错，于是「相同」，判过**
- 第十四类查 `index.md` 的自我声明 → 无关

> **这是「检查比它自称的范围窄」的第 N 次，但形状是新的：**
> 前几次是**检查的范围**没盖住，这一次是**基准本身**有问题——
> **再宽的检查也抓不到，因为尺子本身是弯的。**

## 四、渗进了 wiki：29 条短语 / 4 页

| 页 | 命中短语数 |
|---|---|
| `wiki/concepts/command-reference.md` | **23** |
| `wiki/objects/vector-setup-file.md` | **2** |
| `wiki/concepts/timing-setup-commands.md` | **2** |
| `wiki/objects/timing-setup-tool.md` | **2** |

**`vector-setup-file.md` 那两条最要命**（讲 PRBS 最大值）：

```
PRBS is set to its maximum value 231 - 1          ← 该是 2^31 - 1
which is also set to its maximum value 212 - 1    ← 该是 2^12 - 1
```

`command-reference.md` 里 23 条，形态如：

```
The start cycle is in the range 0 to 248 when the sequencer runs...
The range of the value must be between 0 and 248 - 1
...must be in the range 0 to 2147483648 (231).
Signifies error counter overflow. The hardware error counter has a range of 231.
```

## 五、`<sub>` 的对照——**为什么不构成同类问题**

| 标签 | 总数 | 拍平后果 |
|---|---|---|
| `<sup>` | 1,699 | **换了个数**（`2^48`→`248`）——**真错** |
| `<sub>` | 1,031 | `V_GS`→`VGS`——**这正是它平时的写法**，不算错 |

**上下标的后果不对称。** 下标拍平基本无害（全库 1,031 处只丢 1 处，且是 `f<sub>MAXφ</sub>` 这种希腊字母角标），
**上标拍平只要内容是数字就致命**。**这也解释了为什么这一类错能潜伏这么久**——
抽查时看到 `<sub>` 没事，很容易顺推 `<sup>` 也没事。

## 六、另有两个游离的 `<sup>` / `<sub>` 丢内容（非数字类）

同一轮扫描顺带查出，**内容整个没进 markdown**（不是拍平，是消失）：

| HTML | 内容 | 文件 |
|---|---|---|
| `<sup>` | `½` | `120836.htm` |
| `<sup>` | `-jωa`、`-jωδ` | `123520.htm` |
| `<sup>` | `●` | `138223.htm` |
| `<sub>` | `MAXφ` | `126977.htm` |

**都是公式和角标，量少（个位数），但对公式类文档是损坏。** 一并列此备查。

## 七、复核办法

```bash
cd F:\master-dev\dorm-wsl-sytest\tdc-html
python -X utf8 - <<'PY'
import re, pathlib, html
MD=pathlib.Path('agent-markdown/by-category'); HT=pathlib.Path('raw')
stem2md={}
for p in MD.rglob('*.md'):
    m=re.search(r'^source_topic:\s*["\']?([^"\'\s]+)', p.read_bytes().decode('utf-8','replace'), re.M)
    if m: stem2md.setdefault(m.group(1).replace('.htm','').replace('.html',''),[]).append(p)
body=re.compile(r'<body\b[^>]*>(.*)</body\s*>',re.I|re.S); plain=re.compile(r'<[^>]+>')
sup=re.compile(r'<sup\b[^>]*>(\d{1,3})</sup\s*>',re.I|re.S)
tot=bad=0
for f in sorted(HT.glob('*.htm'))+sorted(HT.glob('*.html')):
    raw=f.read_bytes()
    try: t=raw.decode('utf-8')
    except: t=raw.decode('cp1252','replace')
    m=body.search(t); seg=m.group(1) if m else t
    for mm in sup.finditer(seg):
        before=html.unescape(plain.sub('',seg[max(0,mm.start()-6):mm.start()])).rstrip()
        if not before or not before[-1].isdigit(): continue
        tot+=1
        lit=f'{before[-1]}{mm.group(1)}'
        for md in stem2md.get(f.stem,[]):
            if lit in md.read_bytes().decode('utf-8','replace'): bad+=1; break
print(f'数字上标贴数字: {tot} 处；被拍平: {bad} 处')
PY
```

**预期输出：`数字上标贴数字: 151 处；被拍平: 151 处`。若两个数不等或总数变了，说明语料被换过。**

## 八、处置 —— **未处置**（规矩已备好，等一次批准）

2026-09-22 人批准新增 `schema.md` **§1.2**：**A 类转换损坏经批准可以改，只改 `agent-markdown/`。**
所以这 151 处**现在可改，但本文没改**——**按 §1.2 第 1 步，要先把 HTML 与 markdown 并排列出来征意见。**

**改的时候要注意的三件事：**

- **改哪一层**：只改 `agent-markdown/`。**`tdc-html/raw/` 的 HTML 一个字不许动**——
  它是 A 类唯一的对证上游，改掉就再也证不了任何一处。
- **改完要跟着做的**：`wiki/` 那 4 页一起改；`extract/*.jsonl` 重跑。
- **已知代价**：本机**没有那个 HTML→markdown 转换器**，
  所以改动**不在转换链里**——日后若重新转换，这 151 处**会被覆盖**。
  **清单必须留**（本文就是那份清单），就是为了那一天能重放。

## 九、这件事真正的教训

**它推翻了一句此前一直被默认的话。**

此前所有 findings 记的都是「**检查比它自称的范围窄**」——
那是「尺子不够长」。**这一条是「尺子本身是弯的」：**

> **wiki 与语料比对通过，只证明「wiki 忠实于语料」，
> 不证明「语料是对的」。而在此之前，项目里没有任何一条检查、
> 任何一句规矩，把这两件事分开说过。**

`purpose.md` 说「wiki 的天花板 = 语料的天花板」——**这句话一直是对的，
只是此前没人量过天花板有多低。现在有数了：光上标这一项，就 151 处。**
