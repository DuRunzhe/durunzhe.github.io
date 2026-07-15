# 孤儿图归档 - 2026-07-15

清理 moto-comparison.html 中未被引用的 5 张孤儿图备份。

## 删除原因

GitHub Pages 部署后扫描发现以下 5 张图在 HTML 里**无任何引用**（孤儿图），
为保持图库整洁、避免 Jekyll 在 _site/ 复制无用文件，全部删除。

## 5 张孤儿图

| 文件名 | 大小 | 来源 commit | 替代方案 |
|---|---|---|---|
| `dinkg150.jpg` | 160KB | 26109b1 (2026-06-17) | 图库无替代，速览表无该车型列 |
| `kpv150.jpg` | 349KB | f736c62 (2026-06-17) | 被 `nk150.jpg` 替代（豪爵 NK150 林道版）|
| `srgt200.jpg` | 270KB | f736c62 (2026-06-17) | 图库无替代，速览表无该车型列 |
| `trk552x25.jpg` | 125KB | a27b345 (2026-07-15) | 被 `trk552x26.jpg` 替代（TRK 552X 2026 探险版）|
| `zontes150x.jpg` | 20KB | e8ebbb5 (2026-07-15) | 图库无替代，速览表无该车型列 |

## 删除操作

1. cp 到本目录（备份）✅
2. 从 `img/motos/` 删除（git rm）✅
3. commit `chore(moto): 清理 5 张孤儿图` ✅

## 恢复方法

如需将某张图恢复回图库：
```bash
cp drafts/orphans/moto-2026-07-15/xxx.jpg img/motos/
git add img/motos/xxx.jpg
git commit -m "feat(moto): 恢复孤儿图 xxx.jpg"
```

删除 commit: 将在本批次 commit 中包含
