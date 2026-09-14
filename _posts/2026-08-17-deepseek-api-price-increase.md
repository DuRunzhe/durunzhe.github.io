---
title: "主流大模型价格·能力·性价比横评（2026-08）：DeepSeek 涨价与 GLM-5.3-Flash 入局"
date: 2026-08-17
categories: ai
---

# 主流大模型价格、能力与性价比横评

## 版本与更新记录

> **v3.0** · 2026-09-15（结构重组：横评 → 价格史 → 购买 → 建议 → 选型 → 时间线）
> **v2.2** · 2026-09-15（V4.1-Flash 换代发布；峰谷时段确认工作日）
> **v2.1** · 2026-09-09（Flash 系列降价）· **v2.0** 2026-08-27（GLM-5.3-Flash 入局）· **初版** 2026-08-17

2026 年 8 月 13 日 DeepSeek 官宣 API 调价、8 月 17 日零点生效；9 月 10 日 Flash 线降价并换代为 V4.1-Flash。本文把历次价格版本、模型横评、购买入口、选型建议一次讲清。

---

## 一、同类型模型横评

> 单位：元 / 百万 tokens，美元按 ≈7 折算。DeepSeek 为「空闲 / 高峰」区间；**点击表头可切换该维度正序 / 反序**。

<table id="llm-price-table" style="width:100%;border-collapse:collapse;margin:14px 0;font-size:14px;line-height:1.6;">
<thead>
<tr style="background:#f5f5f5;">
<th data-sortable data-col="0" data-label="模型" style="padding:8px 10px;text-align:left;border:1px solid #e0e0e0;">模型</th>
<th style="padding:8px 10px;text-align:left;border:1px solid #e0e0e0;">厂商</th>
<th data-sortable data-col="2" data-label="输入（缓存命中）" style="padding:8px 10px;text-align:left;border:1px solid #e0e0e0;">输入<br><span style="font-weight:normal;color:#888;font-size:12px;">缓存命中</span></th>
<th data-sortable data-col="3" data-label="输入（缓存未命中）" style="padding:8px 10px;text-align:left;border:1px solid #e0e0e0;">输入<br><span style="font-weight:normal;color:#888;font-size:12px;">缓存未命中</span></th>
<th data-sortable data-col="4" data-label="输出" style="padding:8px 10px;text-align:left;border:1px solid #e0e0e0;">输出</th>
<th data-sortable data-col="5" data-label="上下文" style="padding:8px 10px;text-align:left;border:1px solid #e0e0e0;">上下文</th>
<th style="padding:8px 10px;text-align:left;border:1px solid #e0e0e0;">备注</th>
</tr>
</thead>
<tbody>
<tr>
<td style="padding:8px 10px;border:1px solid #e0e0e0;border-left:6px solid #9467bd;font-weight:bold;">GLM-5.3-Flash</td>
<td style="padding:8px 10px;border:1px solid #e0e0e0;">智谱</td>
<td data-v="0.21" style="padding:8px 10px;border:1px solid #e0e0e0;">0.21</td>
<td data-v="1.05" style="padding:8px 10px;border:1px solid #e0e0e0;">1.05</td>
<td data-v="3.5" style="padding:8px 10px;border:1px solid #e0e0e0;">3.5</td>
<td data-v="1000000" style="padding:8px 10px;border:1px solid #e0e0e0;">1M</td>
<td style="padding:8px 10px;border:1px solid #e0e0e0;">无峰谷；MIT 开源可自托管</td>
</tr>
<tr>
<td style="padding:8px 10px;border:1px solid #e0e0e0;border-left:6px solid #1f77b4;font-weight:bold;">DeepSeek V4.1-Flash</td>
<td style="padding:8px 10px;border:1px solid #e0e0e0;">DeepSeek</td>
<td data-v="0.02" style="padding:8px 10px;border:1px solid #e0e0e0;">0.02 / 0.04</td>
<td data-v="1.0" style="padding:8px 10px;border:1px solid #e0e0e0;">1.0 / 2.0</td>
<td data-v="4.0" style="padding:8px 10px;border:1px solid #e0e0e0;">4.0 / 8.0</td>
<td data-v="1000000" style="padding:8px 10px;border:1px solid #e0e0e0;">1M</td>
<td style="padding:8px 10px;border:1px solid #e0e0e0;">原生视觉；2500 并发；9/10 换代同价</td>
</tr>
<tr>
<td style="padding:8px 10px;border:1px solid #e0e0e0;border-left:6px solid #1f77b4;font-weight:bold;">DeepSeek V4-Pro</td>
<td style="padding:8px 10px;border:1px solid #e0e0e0;">DeepSeek</td>
<td data-v="0.15" style="padding:8px 10px;border:1px solid #e0e0e0;">0.15 / 0.30</td>
<td data-v="4.5" style="padding:8px 10px;border:1px solid #e0e0e0;">4.5 / 9.0</td>
<td data-v="13.5" style="padding:8px 10px;border:1px solid #e0e0e0;">13.5 / 27.0</td>
<td data-v="1000000" style="padding:8px 10px;border:1px solid #e0e0e0;">1M</td>
<td style="padding:8px 10px;border:1px solid #e0e0e0;">旗舰推理档；无视觉；500 并发</td>
</tr>
<tr>
<td style="padding:8px 10px;border:1px solid #e0e0e0;border-left:6px solid #2ca02c;font-weight:bold;">GPT-5.6 Luna</td>
<td style="padding:8px 10px;border:1px solid #e0e0e0;">OpenAI</td>
<td data-v="NaN" style="padding:8px 10px;border:1px solid #e0e0e0;">—</td>
<td data-v="1.4" style="padding:8px 10px;border:1px solid #e0e0e0;">≈1.4</td>
<td data-v="8.4" style="padding:8px 10px;border:1px solid #e0e0e0;">≈8.4</td>
<td data-v="0" style="padding:8px 10px;border:1px solid #e0e0e0;">—</td>
<td style="padding:8px 10px;border:1px solid #e0e0e0;">7 月底刚降 80%</td>
</tr>
<tr>
<td style="padding:8px 10px;border:1px solid #e0e0e0;border-left:6px solid #2ca02c;font-weight:bold;">GPT-5.6 Terra</td>
<td style="padding:8px 10px;border:1px solid #e0e0e0;">OpenAI</td>
<td data-v="NaN" style="padding:8px 10px;border:1px solid #e0e0e0;">—</td>
<td data-v="14" style="padding:8px 10px;border:1px solid #e0e0e0;">≈14</td>
<td data-v="84" style="padding:8px 10px;border:1px solid #e0e0e0;">≈84</td>
<td data-v="0" style="padding:8px 10px;border:1px solid #e0e0e0;">—</td>
<td style="padding:8px 10px;border:1px solid #e0e0e0;">旗舰档</td>
</tr>
<tr>
<td style="padding:8px 10px;border:1px solid #e0e0e0;border-left:6px solid #d62728;font-weight:bold;">Claude Sonnet 5</td>
<td style="padding:8px 10px;border:1px solid #e0e0e0;">Anthropic</td>
<td data-v="NaN" style="padding:8px 10px;border:1px solid #e0e0e0;">—</td>
<td data-v="14" style="padding:8px 10px;border:1px solid #e0e0e0;">≈14</td>
<td data-v="70" style="padding:8px 10px;border:1px solid #e0e0e0;">≈70</td>
<td data-v="0" style="padding:8px 10px;border:1px solid #e0e0e0;">—</td>
<td style="padding:8px 10px;border:1px solid #e0e0e0;">8/31 后涨到 ≈21 / 105</td>
</tr>
<tr>
<td style="padding:8px 10px;border:1px solid #e0e0e0;border-left:6px solid #d62728;font-weight:bold;">Claude Fable 5</td>
<td style="padding:8px 10px;border:1px solid #e0e0e0;">Anthropic</td>
<td data-v="NaN" style="padding:8px 10px;border:1px solid #e0e0e0;">—</td>
<td data-v="70" style="padding:8px 10px;border:1px solid #e0e0e0;">≈70</td>
<td data-v="350" style="padding:8px 10px;border:1px solid #e0e0e0;">≈350</td>
<td data-v="0" style="padding:8px 10px;border:1px solid #e0e0e0;">—</td>
<td style="padding:8px 10px;border:1px solid #e0e0e0;">顶级难题档</td>
</tr>
<tr>
<td style="padding:8px 10px;border:1px solid #e0e0e0;border-left:6px solid #ff7f0e;font-weight:bold;">Qwen3.8-Max</td>
<td style="padding:8px 10px;border:1px solid #e0e0e0;">阿里云</td>
<td data-v="NaN" style="padding:8px 10px;border:1px solid #e0e0e0;">—</td>
<td data-v="12" style="padding:8px 10px;border:1px solid #e0e0e0;">12</td>
<td data-v="36" style="padding:8px 10px;border:1px solid #e0e0e0;">36</td>
<td data-v="0" style="padding:8px 10px;border:1px solid #e0e0e0;">—</td>
<td style="padding:8px 10px;border:1px solid #e0e0e0;">国产旗舰长程档</td>
</tr>
</tbody>
</table>

<script>
(function () {
  var table = document.getElementById('llm-price-table');
  if (!table || !table.tHead) return;
  var ths = table.querySelectorAll('th[data-sortable]');
  Array.prototype.forEach.call(ths, function (th) {
    th.style.cursor = 'pointer';
    th.title = '点击切换正序 / 反序';
    th.addEventListener('click', function () {
      var tbody = table.tBodies[0];
      var rows = Array.prototype.slice.call(tbody.rows);
      var col = parseInt(th.getAttribute('data-col'), 10);
      var dir = th.getAttribute('data-dir') === 'asc' ? 'desc' : 'asc';
      Array.prototype.forEach.call(ths, function (o) {
        if (o !== th) {
          o.removeAttribute('data-dir');
          o.innerHTML = o.getAttribute('data-label');
        }
      });
      th.setAttribute('data-dir', dir);
      rows.sort(function (a, b) {
        var av = parseFloat(a.cells[col].getAttribute('data-v'));
        var bv = parseFloat(b.cells[col].getAttribute('data-v'));
        if (isNaN(av)) av = Infinity;
        if (isNaN(bv)) bv = Infinity;
        if (col === 0) {
          av = a.cells[0].textContent.trim();
          bv = b.cells[0].textContent.trim();
          return dir === 'asc' ? av.localeCompare(bv, 'zh') : bv.localeCompare(av, 'zh');
        }
        return dir === 'asc' ? av - bv : bv - av;
      });
      rows.forEach(function (r) { tbody.appendChild(r); });
      th.innerHTML = th.getAttribute('data-label') + (dir === 'asc' ? ' ▲' : ' ▼');
    });
  });
})();
</script>

### 横向结论

**价格梯队（按输出价从低到高）：**

| 排名 | 模型 | 输出价（元/百万） | 相对 V4.1-Flash 空闲价 |
|---|---|---|---|
| 1 | GLM-5.3-Flash | ≈3.5 | 低约 13% |
| 2 | DeepSeek V4.1-Flash | 4.0 / 8.0 | 基准 |
| 3 | GPT-5.6 Luna | ≈8.4 | 高约 2.1 倍 |
| 4 | DeepSeek V4-Pro | 13.5 / 27.0 | 高 3.4~6.8 倍 |
| 5 | Qwen3.8-Max | 36 | 高 9 倍 |
| 6 | Claude Sonnet 5 | ≈70（将涨至 105） | 高 17.5 倍 |
| 7 | GPT-5.6 Terra | ≈84 | 高 21 倍 |
| 8 | Claude Fable 5 | ≈350 | 高 87.5 倍 |

**输入梯队（按缓存未命中价从低到高）：**

| 排名 | 模型 | 输入价（元/百万） |
|---|---|---|
| 1 | DeepSeek V4.1-Flash | 1.0 / 2.0 |
| 2 | GLM-5.3-Flash | ≈1.05 |
| 3 | GPT-5.6 Luna | ≈1.4 |
| 4 | DeepSeek V4-Pro | 4.5 / 9.0 |
| 5 | Qwen3.8-Max | 12 |
| 6 | Claude Sonnet 5 / GPT-5.6 Terra | ≈14 |
| 7 | Claude Fable 5 | ≈70 |

**缓存命中输入梯队（DeepSeek 的绝对优势区）：**

| 排名 | 模型 | 命中价（元/百万） | 命中 / 未命中比 |
|---|---|---|---|
| 1 | DeepSeek V4.1-Flash | 0.02 / 0.04 | 1 / 50 |
| 2 | DeepSeek V4-Pro | 0.15 / 0.30 | 1 / 30 |
| 3 | GLM-5.3-Flash | ≈0.21 | 1 / 5 |

**能力梯队（官方/第三方口径，仅列有据可查项）：**

| 模型 | 关键能力指标 | 口径 |
|---|---|---|
| DeepSeek V4.1-Flash | Terminal-Bench 2.1 **90.6** / DeepSWE 74.2 / GPQA Diamond 90.9 | DeepSeek 官方 9/10 |
| DeepSeek V4-Pro | Terminal-Bench 2.1 87.9 / DeepSWE 62.7 / HLE 42.7（带工具 60.0） | DeepSeek 官方 8/13 |
| GLM-5.3-Flash | AA 综合智能 57 / DeepSWE v1.1 63.4 / AutomationBench 48.8 | 智谱官方 + Artificial Analysis |
| Claude Opus 4.8 | AA 综合智能 ≈57（与 GLM-5.3-Flash 同分水平） | Artificial Analysis |
| Claude Fable 5 | 顶级难题档（V4-Pro 报道口径 ≈97%） | 媒体报道 |

<div style="margin:16px auto;">
<svg viewBox="0 0 800 490" xmlns="http://www.w3.org/2000/svg" role="img" style="width:100%;height:auto;max-width:760px;font-family:-apple-system,Segoe UI,Microsoft YaHei,sans-serif;">
<text x="160" y="20" font-size="15" font-weight="bold" fill="#222">元 / 百万 tokens（对数刻度）</text>
<line x1="160.0" y1="38" x2="160.0" y2="460" stroke="#ddd" stroke-width="1"/>
<text x="160.0" y="34" font-size="9" fill="#999" text-anchor="middle">0.5</text>
<line x1="216.5" y1="38" x2="216.5" y2="460" stroke="#ddd" stroke-width="1"/>
<text x="216.5" y="34" font-size="9" fill="#999" text-anchor="middle">1</text>
<line x1="306.2" y1="38" x2="306.2" y2="460" stroke="#ddd" stroke-width="1"/>
<text x="306.2" y="34" font-size="9" fill="#999" text-anchor="middle">3</text>
<line x1="404.4" y1="38" x2="404.4" y2="460" stroke="#ddd" stroke-width="1"/>
<text x="404.4" y="34" font-size="9" fill="#999" text-anchor="middle">10</text>
<line x1="494.0" y1="38" x2="494.0" y2="460" stroke="#ddd" stroke-width="1"/>
<text x="494.0" y="34" font-size="9" fill="#999" text-anchor="middle">30</text>
<line x1="592.2" y1="38" x2="592.2" y2="460" stroke="#ddd" stroke-width="1"/>
<text x="592.2" y="34" font-size="9" fill="#999" text-anchor="middle">100</text>
<line x1="681.8" y1="38" x2="681.8" y2="460" stroke="#ddd" stroke-width="1"/>
<text x="681.8" y="34" font-size="9" fill="#999" text-anchor="middle">300</text>
<line x1="780.0" y1="38" x2="780.0" y2="460" stroke="#ddd" stroke-width="1"/>
<text x="780.0" y="34" font-size="9" fill="#999" text-anchor="middle">1000</text>
<text x="142" y="66" font-size="12.5" fill="#333" text-anchor="end" font-weight="bold">GLM-5.3 Flash</text>
<rect x="160.0" y="48" width="158.7" height="14" fill="#9467bd" rx="2" opacity="0.9"/>
<text x="324.7" y="59" font-size="10.5" fill="#333">3.5</text>
<text x="160.0" y="41" font-size="8.5" fill="#999">输出</text>
<rect x="160.0" y="68" width="60.5" height="10" fill="#9467bd" rx="2" opacity="0.35"/>
<text x="226.5" y="76" font-size="9.5" fill="#666">1.05</text>
<text x="160.0" y="62" font-size="8.5" fill="#aaa">输入(未命中)</text>
<text x="142" y="118" font-size="12.5" fill="#333" text-anchor="end" font-weight="bold">DeepSeek V4 Flash</text>
<rect x="160.0" y="100" width="226.5" height="14" fill="#1f77b4" rx="2" opacity="0.9"/>
<rect x="160.0" y="100" width="169.5" height="14" fill="#1f77b4" rx="2" opacity="0.45"/>
<text x="392.0" y="111" font-size="10.5" fill="#333">4~8</text>
<text x="160.0" y="93" font-size="8.5" fill="#999">输出</text>
<rect x="160.0" y="120" width="113.0" height="10" fill="#1f77b4" rx="2" opacity="0.35"/>
<text x="279.0" y="128" font-size="9.5" fill="#666">1~2</text>
<text x="160.0" y="114" font-size="8.5" fill="#aaa">输入(未命中)</text>
<text x="142" y="170" font-size="12.5" fill="#333" text-anchor="end" font-weight="bold">DeepSeek V4 Pro</text>
<rect x="160.0" y="152" width="325.4" height="14" fill="#1f77b4" rx="2" opacity="0.9"/>
<rect x="160.0" y="152" width="268.8" height="14" fill="#1f77b4" rx="2" opacity="0.45"/>
<text x="491.4" y="163" font-size="10.5" fill="#333">13.5~27</text>
<text x="160.0" y="145" font-size="8.5" fill="#999">输出</text>
<rect x="160.0" y="172" width="235.8" height="10" fill="#1f77b4" rx="2" opacity="0.35"/>
<text x="401.8" y="180" font-size="9.5" fill="#666">4.5~9</text>
<text x="160.0" y="166" font-size="8.5" fill="#aaa">输入(未命中)</text>
<text x="142" y="222" font-size="12.5" fill="#333" text-anchor="end" font-weight="bold">GPT-5.6 Luna</text>
<rect x="160.0" y="204" width="230.1" height="14" fill="#2ca02c" rx="2" opacity="0.9"/>
<text x="396.1" y="215" font-size="10.5" fill="#333">8.4</text>
<text x="160.0" y="197" font-size="8.5" fill="#999">输出</text>
<rect x="160.0" y="224" width="84.0" height="10" fill="#2ca02c" rx="2" opacity="0.35"/>
<text x="250.0" y="232" font-size="9.5" fill="#666">1.4</text>
<text x="160.0" y="218" font-size="8.5" fill="#aaa">输入(未命中)</text>
<text x="142" y="274" font-size="12.5" fill="#333" text-anchor="end" font-weight="bold">Qwen3.8 Max</text>
<rect x="160.0" y="256" width="348.8" height="14" fill="#ff7f0e" rx="2" opacity="0.9"/>
<text x="514.8" y="267" font-size="10.5" fill="#333">36</text>
<text x="160.0" y="249" font-size="8.5" fill="#999">输出</text>
<rect x="160.0" y="276" width="259.2" height="10" fill="#ff7f0e" rx="2" opacity="0.35"/>
<text x="425.2" y="284" font-size="9.5" fill="#666">12</text>
<text x="160.0" y="270" font-size="8.5" fill="#aaa">输入(未命中)</text>
<text x="142" y="326" font-size="12.5" fill="#333" text-anchor="end" font-weight="bold">Claude Sonnet 5</text>
<rect x="160.0" y="308" width="403.1" height="14" fill="#d62728" rx="2" opacity="0.9"/>
<text x="569.1" y="319" font-size="10.5" fill="#333">70</text>
<text x="160.0" y="301" font-size="8.5" fill="#999">输出</text>
<rect x="160.0" y="328" width="271.8" height="10" fill="#d62728" rx="2" opacity="0.35"/>
<text x="437.8" y="336" font-size="9.5" fill="#666">14</text>
<text x="160.0" y="322" font-size="8.5" fill="#aaa">输入(未命中)</text>
<text x="142" y="378" font-size="12.5" fill="#333" text-anchor="end" font-weight="bold">GPT-5.6 Terra</text>
<rect x="160.0" y="360" width="418.0" height="14" fill="#2ca02c" rx="2" opacity="0.9"/>
<text x="584.0" y="371" font-size="10.5" fill="#333">84</text>
<text x="160.0" y="353" font-size="8.5" fill="#999">输出</text>
<rect x="160.0" y="380" width="271.8" height="10" fill="#2ca02c" rx="2" opacity="0.35"/>
<text x="437.8" y="388" font-size="9.5" fill="#666">14</text>
<text x="160.0" y="374" font-size="8.5" fill="#aaa">输入(未命中)</text>
<text x="142" y="430" font-size="12.5" fill="#333" text-anchor="end" font-weight="bold">Claude Fable 5</text>
<rect x="160.0" y="412" width="534.4" height="14" fill="#d62728" rx="2" opacity="0.9"/>
<text x="700.4" y="423" font-size="10.5" fill="#333">350</text>
<text x="160.0" y="405" font-size="8.5" fill="#999">输出</text>
<rect x="160.0" y="432" width="403.1" height="10" fill="#d62728" rx="2" opacity="0.35"/>
<text x="569.1" y="440" font-size="9.5" fill="#666">70</text>
<text x="160.0" y="426" font-size="8.5" fill="#aaa">输入(未命中)</text>
<rect x="160.0" y="463" width="14" height="8" fill="#1f77b4" rx="1" opacity="0.9"/>
<text x="178.0" y="470" font-size="9.5" fill="#555">输出价（深色条=空闲，浅色叠层=高峰）</text>
<rect x="350.0" y="463" width="14" height="8" fill="#1f77b4" rx="1" opacity="0.35"/>
<text x="368.0" y="470" font-size="9.5" fill="#555">输入价（缓存未命中）</text>
<rect x="540.0" y="463" width="14" height="8" fill="#9467bd" rx="1" opacity="0.9"/>
<text x="558.0" y="470" font-size="9.5" fill="#555">GLM-5.3 Flash（无峰谷）</text>
</svg>
</div>

> 📌 **怎么读这张图**：横轴是模型，纵轴是元/百万 tokens（对数刻度，每格差 10 倍）。每个模型左侧浅色条=输入（缓存未命中），右侧深色条=输出；DeepSeek 的条是「空闲~高峰」区间，紫色条 GLM-5.3-Flash 为单一定价。一眼可见：**GLM-5.3-Flash 与 DeepSeek 两条柱在最底部，Claude Fable 5 在最顶部（差约 100 倍）**。

**横向三点**：

1. **输出侧**：GLM-5.3-Flash（3.5 元）仍是输出地板价；DeepSeek V4.1-Flash 空闲（4 元）紧随其后，高峰（8 元）仍略低于 GPT-5.6 Luna（≈8.4 元）。
2. **输入侧（重缓存负载）**：DeepSeek 断层领先——命中价 0.02 元，只有 GLM（0.21 元）的 1/10，是 Agent 多轮/工具循环的最优解。
3. **第三方托管**（OpenRouter 上的 DeepInfra 等）：Flash 档第三方普遍更便宜（输入 $0.08~0.14 vs 官方高峰 $0.44），Pro 档官方空闲价仍无人能敌。

---

## 二、全版本价格对照（分模型 · 按时间线追加）

> 单位：元 / 百万 tokens，格式「空闲 / 高峰」（① 期无峰谷，为单一价；— = 未开放）。④ 期为 2026-09-10 起的现价。

### DeepSeek V4.1-Flash（原 V4-Flash 线，9/10 换代同价）

**模型特色：** 全新模型结构系列中的最小尺寸；**原生多模态视觉理解**（Pro 不支持）；1M 上下文 / 384K 最大输出 / 2500 并发；官方基准 Terminal-Bench 2.1 **90.6**、DeepSWE **74.2**、GPQA Diamond 90.9——同价位 Agent / 终端能力最强档。模型名建议用 `deepseek-flash`。

| 计费项 | ① 5 月平价 | ② 6 月底–8/16 | ③ 8/17–9/9 | ④ 9/10 起 | ④ vs ③ |
|---|---|---|---|---|---|
| 输入（缓存命中） | — | 0.02 / 0.04 | 0.05 / 0.10 | **0.02 / 0.04** | -60% |
| 输入（缓存未命中） | — | 1.0 / 2.0 | 1.5 / 3.0 | **1.0 / 2.0** | -33.3% |
| 输出 | — | 2.0 / 4.0 | 4.5 / 9.0 | **4.0 / 8.0** | -11.1% |
| 月度成本（90% 命中负载*） | — | ≈7.5 | ≈14.9 | **≈11.5** | -22.8% |

### DeepSeek V4-Pro（旗舰推理档）

**模型特色：** 深度推理与 Agent 旗舰；HLE 42.7（带工具 60.0）、Terminal-Bench 2.1 87.9、DeepSWE 62.7；**不支持图像理解**；并发 500。9/10 官方宣布 9/14 后继续提供服务、计费不变。

| 计费项 | ① 5 月平价 | ② 6 月底–8/16 | ③ 8/17–9/9 | ④ 9/10 起 | ④ vs ① |
|---|---|---|---|---|---|
| 输入（缓存命中） | 0.025 | 0.025 / 0.05 | 0.15 / 0.30 | 0.15 / 0.30 | 6 倍 |
| 输入（缓存未命中） | 3.0 | 3.0 / 6.0 | 4.5 / 9.0 | 4.5 / 9.0 | 1.5 倍 |
| 输出 | 6.0 | 6.0 / 12.0 | 13.5 / 27.0 | 13.5 / 27.0 | 2.25 倍 |
| 月度成本（90% 命中负载*） | ≈21.7 | ≈42.7 | ≈44.6 | ≈44.6 | ≈2 倍 |

### GLM-5.3-Flash（智谱 · 对比参照）

**模型特色：** 320B 总参数、每次仅激活 18B；首次采用稀疏注意力 + 线性注意力混合架构（相比 GLM-5.3，注意力计算量降至约 1/3、KV Cache 占用降约 4.4 倍）；原生多模态、1M 上下文；**MIT 开源可自托管**（SGLang / vLLM / TokenSpeed）；匿名测试期（Ox Alpha「牛来」）全部真实流量跑在国产 AI 芯片上。

| 计费项 | 价格（无峰谷） | 美元原价 |
|---|---|---|
| 输入（缓存命中） | ≈0.21 | 0.03 |
| 输入（缓存未命中） | ≈1.05 | 0.15 |
| 输出 | ≈3.5 | 0.50 |

> *月度成本口径：输入 3000 万 token、缓存命中率 90%、输出 200 万 token/月，按各期空闲价计（① 期为平价）。Flash ① 期（5 月）正式 API 尚未公测，故无该期价格。

### 口径与换算备忘

**峰谷规则**：高峰 = 北京时间**周一至周五** 9:00–12:00、14:00–18:00；其余时段（含**周末全天**）为空闲价，空闲价 = 高峰价的一半。计费时钟只有一个，全球调用方同一时刻价格状态一致。

**涨幅口径**：刷屏的「涨 12 倍」特指 V4-Pro 缓存命中档 **高峰价 ÷ 5 月平铺价**（0.30 ÷ 0.025）；若以 7 月已含峰谷的旧价计算，最高 6 倍——两个口径都对，媒体混用了基准。反直觉规律：**缓存命中率越高，涨幅越大**（命中率 40% 约涨 1.7 倍，90% 约涨 2.1 倍）。

**「60 倍价差」重算**：原按 V4-Pro 旧输出价 6 元对 Claude Fable 5 的约 360 元算得；8/17 新价后重算为**空闲约 27 倍、高峰约 13 倍**。性能对标的结论（≈97%、DeepSWE 跃升）仍有效，但价格倍数须用最新价表重算。

**关键换算**：命中价 = 未命中价的 1/50（9/10 起恢复，8/17–9/9 曾为 1/30）；输出 = 未命中输入的 3 倍（Flash 9/10 起为 4 倍）；高峰 = 空闲 × 2；Pro 是 Flash 的 3.4（输出）～7.5 倍（命中档）；美元按官方约 **6.82 元/美元** 折算（粗算按 ≈7 元）。

---

## 三、厂商官网 / API 购买地址

| 厂商 | 模型 | 输出价（元/百万，空闲档） | 官网 / 购买地址 |
|---|---|---|---|
| DeepSeek | V4.1-Flash / V4-Pro | 4.0 / 13.5 | [platform.deepseek.com](https://platform.deepseek.com)（API 平台） |
| 智谱 | GLM-5.3-Flash / GLM-5.3 | ≈3.5 | [open.bigmodel.cn](https://open.bigmodel.cn)（开放平台）· 国际站 [z.ai](https://z.ai) |
| OpenAI | GPT-5.6 Luna / Terra | ≈8.4 / ≈84 | [platform.openai.com](https://platform.openai.com)（API 平台） |
| Anthropic | Claude Sonnet 5 / Opus 4.8 / Fable 5 | ≈70 / — / ≈350 | [console.anthropic.com](https://console.anthropic.com)（Console） |
| 阿里云 | Qwen3.8-Max | 36 | [bailian.console.aliyun.com](https://bailian.console.aliyun.com)（百炼） |

> 开源自托管入口：GLM-5.3-Flash 权重发布于 [huggingface.co/zai-org/GLM-5.3-Flash](https://huggingface.co/zai-org/GLM-5.3-Flash)（MIT License）。

---

## 四、落地建议（按最新事实）

1. **错峰跑批**：非实时任务挪到 18:00 后；**周末全天都是空闲价**（峰窗仅工作日 7 小时），周末跑批最划算。
2. **保缓存命中率**：固定 System Prompt / 工具定义放上下文最前，命中价 0.02 元几乎免费，是抵消涨价的最有效手段。
3. **能用 Flash 就不用 Pro**：Pro 是 Flash 的 3.4～7.5 倍；且 Flash 已**原生支持视觉**、Agent/终端基准反超 Pro，默认档位放 Flash。
4. **多模态任务**：走 V4.1-Flash（官方 API，`deepseek-flash`）或 GLM-5.3-Flash（可自托管、开源）。
5. **迁移提示**：旧模型名 `deepseek-v4-flash` / `deepseek-v4-flash-vision-exp` 已下线但自动路由到 V4.1-Flash，建议尽快改为 `deepseek-flash`。
6. **美区团队占时区便宜，欧区上午撞高峰**：美国（东西岸）整个工作时段都落在空闲区；欧洲团队上午正好是高峰，批量任务应挪到下午或晚上。

**海外团队高峰时段速查（2026 年夏令时）：**

| 团队所在地 | 时区 | 本地高峰时段 | 9-18 工作时段撞峰 |
|---|---|---|---|
| 北京 | UTC+8 | 9:00–12:00、14:00–18:00（工作日） | 7 小时 |
| 东京/首尔 | UTC+9 | 10:00–13:00、15:00–19:00 | 6 小时 |
| 印度 | UTC+5:30 | 6:30–9:30、11:30–15:30 | 4.5 小时 |
| 柏林/巴黎 | UTC+2 (CEST) | 3:00–6:00、8:00–12:00 | 3 小时（上午） |
| 伦敦 | UTC+1 (BST) | 2:00–5:00、7:00–11:00 | 2 小时（上午） |
| 纽约 | UTC-4 (EDT) | 前日 21:00–0:00、2:00–6:00 | 0 小时 ✅ |
| 旧金山 | UTC-7 (PDT) | 前日 18:00–21:00、23:00–3:00 | 0 小时 ✅ |

> ⚠️ 冬令时注意：北半球 10 月底后欧洲/美国进入冬令时，各时区换算相差 1 小时，峰窗整体错位；上表仅适用于 2026 年夏令时。

---

## 五、按任务选模型：性价比决策图

> 不同任务对延迟、质量、成本的要求不同，**没有「最好的模型」，只有「最合适的选择」**。按 2026-09-10 价格：

<table style="width:100%;border-collapse:collapse;margin:14px 0;font-size:14px;line-height:1.6;">
<thead>
<tr style="background:#f5f5f5;">
<th style="padding:8px 12px;text-align:left;border:1px solid #e0e0e0;">任务类型</th>
<th style="padding:8px 12px;text-align:left;border:1px solid #e0e0e0;">推荐模型</th>
<th style="padding:8px 12px;text-align:left;border:1px solid #e0e0e0;">价格参考</th>
<th style="padding:8px 12px;text-align:left;border:1px solid #e0e0e0;">理由</th>
</tr>
</thead>
<tbody>
<tr>
<td style="padding:8px 12px;border:1px solid #e0e0e0;border-left:6px solid #1f77b4;font-weight:bold;">批量/离线任务<br><span style="font-weight:normal;color:#888;font-size:12px;">夜间跑批、数据清洗</span></td>
<td style="padding:8px 12px;border:1px solid #e0e0e0;"><b>V4.1-Flash 空闲时段</b></td>
<td style="padding:8px 12px;border:1px solid #e0e0e0;">≈4 元/百万输出</td>
<td style="padding:8px 12px;border:1px solid #e0e0e0;">谷价=峰价一半，夜间+周末跑批立省 50%</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #e0e0e0;border-left:6px solid #4fa3d1;font-weight:bold;">高频实时对话<br><span style="font-weight:normal;color:#888;font-size:12px;">客服、聊天机器人</span></td>
<td style="padding:8px 12px;border:1px solid #e0e0e0;"><b>V4.1-Flash</b></td>
<td style="padding:8px 12px;border:1px solid #e0e0e0;">8 元/百万输出（峰）</td>
<td style="padding:8px 12px;border:1px solid #e0e0e0;">2500 并发，千 token 输出≈0.008 元</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #e0e0e0;border-left:6px solid #66b3ff;font-weight:bold;">Agent 多轮任务<br><span style="font-weight:normal;color:#888;font-size:12px;">编码助手、工具调用</span></td>
<td style="padding:8px 12px;border:1px solid #e0e0e0;"><b>V4.1-Flash + 高缓存命中</b></td>
<td style="padding:8px 12px;border:1px solid #e0e0e0;">命中输入仅 0.02 元</td>
<td style="padding:8px 12px;border:1px solid #e0e0e0;">固定前缀→命中率 60%+，输入几乎免费；Agent 基准同价位第一</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #e0e0e0;border-left:6px solid #9467bd;font-weight:bold;">视觉/多模态<br><span style="font-weight:normal;color:#888;font-size:12px;">看图、界面操作</span></td>
<td style="padding:8px 12px;border:1px solid #e0e0e0;"><b>V4.1-Flash（官方）/ GLM-5.3-Flash（自托管）</b></td>
<td style="padding:8px 12px;border:1px solid #e0e0e0;">4 元 / ≈3.5 元</td>
<td style="padding:8px 12px;border:1px solid #e0e0e0;">两者均原生多模态；GLM 支持 MIT 开源自部署</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #e0e0e0;border-left:6px solid #ff9f43;font-weight:bold;">复杂推理/长文档<br><span style="font-weight:normal;color:#888;font-size:12px;">分析、总结、结构化</span></td>
<td style="padding:8px 12px;border:1px solid #e0e0e0;"><b>V4-Pro 空闲时段</b></td>
<td style="padding:8px 12px;border:1px solid #e0e0e0;">13.5 元/百万输出</td>
<td style="padding:8px 12px;border:1px solid #e0e0e0;">HLE 42.7（带工具 60.0），性能≈Claude Fable 5 的 97%，价格仅 1/26</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #e0e0e0;border-left:6px solid #d62728;font-weight:bold;">高质量编码/深度研究<br><span style="font-weight:normal;color:#888;font-size:12px;">关键场景不差钱</span></td>
<td style="padding:8px 12px;border:1px solid #e0e0e0;"><b>GPT-5.6 Terra / Claude Fable 5</b></td>
<td style="padding:8px 12px;border:1px solid #e0e0e0;">84~350 元</td>
<td style="padding:8px 12px;border:1px solid #e0e0e0;">能力天花板，稳定性与生态更成熟</td>
</tr>
</tbody>
</table>

**核心原则：**

1. **能错峰就错峰**——非实时任务挪到 18:00 后或周末，成本直接减半。
2. **能缓存就缓存**——固定 System Prompt / 工具定义，命中率决定 Agent 成本。
3. **能不 Pro 就不 Pro**——Pro 是 Flash 的 3.4～7.5 倍，日常任务 Flash 够用（且支持视觉）。
4. **贵模型只干贵活**——把旗舰模型留给真正需要能力天花板的场景。

---

## 六、事件时间线（按日期）

| 日期 | 事件 |
|---|---|
| 2026-04 | DeepSeek V4 预览版发布：Pro / Flash 双线，限时 2.5 折 |
| 2026-05 | V4-Pro 限时折扣转为永久价（输入 ¥3 / 输出 ¥6） |
| 2026-06 底 | 引入峰谷定价：北京时间 9:00–12:00、14:00–18:00 高峰翻倍 |
| 2026-07-31 | V4-Flash 正式版 API 公测（Agent 能力大幅增强，适配 Codex） |
| 2026-08-06 | 公告「整体上调，预计涨幅较大」 |
| 2026-08-13 | 官宣调价方案 + V4-Pro 正式版转正（思考强度 low/high/max、原生 Responses API） |
| **2026-08-17** | **新价生效**：Pro 命中档最高 6 倍、Flash 最高 2.5 倍 |
| 2026-08-21 | V4-Flash-Vision-Exp 多模态实验模型上线（多模态 Agent 接近 Opus-4.8） |
| 2026-08-26 | 智谱发布并开源 GLM-5.3-Flash（匿名模型 Ox Alpha「牛来」掉马）；输出价 3.5 元，**输出地板价易主** |
| 2026-09-09 | DeepSeek 公告 Flash 系列降价（最高降幅 60%） |
| **2026-09-10** | **Flash 新价 12:00 生效 + V4.1-Flash 换代发布**（模型名 `deepseek-flash`、原生多模态）；V4-Pro 官宣 9/14 后继续服务 |
| 2026-09-15 | 本文 v3.0 结构重组（横评排序、价格史分模型、时间线按日期） |

---

## 数据来源

- DeepSeek 官方定价页（[api-docs.deepseek.com/quick_start/pricing](https://api-docs.deepseek.com/zh-cn/quick_start/pricing)）与官方更新日志（[api-docs.deepseek.com/zh-cn/updates](https://api-docs.deepseek.com/zh-cn/updates)，含 9/10 V4.1-Flash 发布公告）
- DeepSeek 9/9 开放平台调价公告（界面新闻 / 澎湃 / 新浪报道）
- 新浪财经、Reuters、Pandaily 报道
- ofox.io、aireiter.com 逐档价格核对
- 智谱官方发布（[z.ai/blog/glm-5.3-flash](https://z.ai/blog/glm-5.3-flash)，8/26）
- Hugging Face：huggingface.co/zai-org/GLM-5.3-Flash（MIT License）
- Artificial Analysis 综合智能指数
- 微信公众号文章《GLM-5.3 Flash 来了！比 DeepSeek 更强、更便宜》（8/27 阅读，含官方口径与 benchmark 数据）
