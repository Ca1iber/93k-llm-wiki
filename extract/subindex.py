# -*- coding: utf-8 -*-
"""§7 的子索引登记表 —— **`wiki/<类型>/index-<类型>.md` 不是「那个类型的一页」**。

## 为什么要单独一个模块

`verify_stages.py`（第十四类）与 `check_syntax_fresh.py`（第十二类）**都要读它**：

- 第十四类甲/乙/丙：算「这个类型有几页」时**要把子索引扣掉**；
- 第十二类：子索引不是 `objscaffold.py` 出的骨架，**不该要求它有 `<!-- 语法节 begin -->`**。

而 `check_syntax_fresh` 是**被 `verify_stages` import 的**（`import check_syntax_fresh as csf`）——
让它反过来 import `verify_stages` 就成环。**登记表只能有一份，两处各写一份必然漂。**

## 为什么不用「文件名以 `index-` 开头」这个模式

`verify_stages.py` 里 `IDX_PAGES` 那段已经写过这条理由，这里再写一遍，因为
**这个模块的存在就是为了让那句理由能落地**：

> 按名字模式豁免，就等于让「新加一个子索引」**自动获得豁免**——
> 那正是 §13 记过的那类洞（改个文件名就改变检查范围，本身就是缺陷）。

所以这里是**具名的**：新增一个子索引，必须**同时**在 `STEMS` 里加名、
并在 `verify_stages.IDX_PAGES` 里写清「谁生成它 / 哪条检查接替」——
**接不上就红着**，防的是静默生长。

`verify_stages.py` 里有一条断言盯着两边一致（`STEMS` ↔ `IDX_PAGES` 的 stem），
所以不会出现「一个登记了、另一个没登记」。
"""

# rel（相对 `wiki/`）→ stem。**两个脚本都从这里取。**
SUBINDEX = {
    'versions/index-versions.md': 'index-versions',
    'objects/index-objects.md': 'index-objects',
}

STEMS = frozenset(SUBINDEX.values())
