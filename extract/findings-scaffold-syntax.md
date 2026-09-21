# 待处置：`objscaffold.py` 的语法节漏掉「语法行」本身

发现时间：2026-09-21
发现方式：写 `wiki/objects/dtcp.md` 时，发现该页「语法 / 参数」节里**没有语法行**，
顺着查下去发现不是孤例。

## 现象

有些命令页的「语法 / 参数」节**只有 `### Parameters`（以及 `### Example(s)`），
完全没有那条 `CMD {参数}` 语法定义行**。

已核实的例子（都逐条回 raw 对过）：

| 页 | raw 里的语法行 | 语法节里有没有 |
|---|---|---|
| `dtcp` | `DTCP {"key"}, {"value"}` / `DTCP? {"key"}` | **没有** |
| `pste` | `PSTE {sites}` / `PSTE {sites\|"site_string"}` | **没有**（该页第 131 行那个是**写页人自己补的表格**，不是脚本抽的） |
| `pqfc` | `PQFC {site}` / `PQFC?` | **没有** |

## 原因

`extract/objscaffold.py` **只认 `Syntax` / `Parameters` / `Example` 三个段名**
（其注释第 6 行、第 190 行写明了这个设计）。

而语料里有一批命令页**不写 `## Syntax`**，而是把语法直接放在
**以命令名命名的二级标题**底下，例如：

```
## DTCP
```
DTCP {"key"}, {"value"}
```
## DTCP?
```

于是脚本认出同篇的 `## Parameters`、`## Examples`，**却认不出语法那一节**，
语法节就成了「有参数表、没有语法」的样子。

## 影响面

用「语法节区间里找不到 raw 那行语法」扫过全部 229 个带语法节的页，
命中 **22 页**（只查了每页第一条 source，因此是**下界**）：
`conf` `ctxt` `dfge` `dfgp` `dfpn` `dfps` `dfpt` `dscp` `dtcp` `eqsp` `jscf`
`jsdf` `jspr` `pals` `pqfc` `psfc` `pste` `sprm` `sqst` `svlr` `timing-equation-set` `uptd`。

**其中相当一部分是已经建好、且已经过 `check_syntax_fresh.py` 的页**
（`pste` / `psfc` / `dfgp` / `dscp` / `uptd` / `sprm` …）。
`check_syntax_fresh.py` **查不出这一类**——它比对的是「页面里的块 == 脚本会生成的块」，
而脚本生成的就是这个漏了语法行的版本，所以它一路报「过期 0」。

## 归类

按本工程的对账规矩，这是 **(a) 脚本 bug**——不是语料如此，也不是基线工具不精确。

## 建议的修法（未执行，等定夺）

1. `objscaffold.py` 的段名表里**增加一条**：二级标题等于本篇命令名
   （或「命令名 + `?`」）时，也当语法段处理；
2. 跑 `objscaffold.py --refresh-syntax`；
3. 重跑 `check_syntax_fresh.py`，并抽查上面那 22 页的语法节。

## 为什么没有当场就改

`--refresh-syntax` 会**一次性重写 229 页的语法节**。
此刻正有一批写页工作在落盘（本次运行中 55 页里已完成 51 页），
**这时候动全库的脚本生成块，会让「页里的块和脚本输出对不上」这个状态
出现在几十页上，且分不清是谁造成的**。
所以先落成这一份记录，把原因、影响面、修法都钉死，由主会话（或人）决定何时执行。
