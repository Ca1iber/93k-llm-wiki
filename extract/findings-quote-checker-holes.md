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
