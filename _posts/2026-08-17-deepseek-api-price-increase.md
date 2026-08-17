---
title: "DeepSeek API 涨价全解析：峰谷分时、涨幅矩阵与「60倍价差」的真相"
date: 2026-08-17
categories: ai
---

# DeepSeek API 涨价全解析

2026 年 8 月 13 日，DeepSeek 官宣 API 调价，8 月 17 日（北京时间零点）正式生效。这次不是一刀切翻倍，而是「峰谷分时 + 分档差异化」的组合拳。本文把新价、旧价、涨幅矩阵、同类型模型横评一次讲清，并勘误一篇流传甚广的公众号文章。

---

## 一、结论速览

1. **涨幅从 1.5 倍到 12 倍不等**，取决于「哪个模型、缓存命中还是未命中、高峰还是空闲」。
2. **涨得最狠的是「缓存命中」这一档**（Pro 涨 6 倍），过去近乎免费的那档成了最大涨幅来源，直接打击 Agent 类重缓存负载。
3. **涨得最少的是「缓存未命中」输入**（统一 1.5 倍），输出统一涨 2.25 倍。
4. **即便涨完，DeepSeek 仍是全球最便宜**——但在**高峰时段，Flash 档输出价已被 GPT-5.6 Luna 反超**，「便宜」只在空闲时段成立。

---

## 二、事件时间线

| 时间 | 动作 |
|---|---|
| 2026-04 | V4 预览版发布，推出 Pro / Flash 双线，限时 2.5 折 |
| 2026-05 | V4-Pro 限时折扣转永久价（输入 ¥3 / 输出 ¥6） |
| 2026-06 底 | 引入峰谷定价：工作日 9:00–12:00、14:00–18:00 高峰翻倍 |
| 2026-07-31 | V4-Flash 正式版 API 公测，调用量起飞 |
| 2026-08-06 | 公告「整体上调，预计涨幅较大」 |
| 2026-08-13 | 官宣具体方案 + V4 Pro 正式版转正 |
| **2026-08-17** | **新价生效** |

---

## 三、新价表（8/17 起，官方）

> 单位：元 / 百万 tokens。高峰时段 = 北京时间工作日 9:00–12:00、14:00–18:00，其余为空闲时段；空闲价 = 高峰价的 1/2。

| 模型 | 计费项 | 空闲时段 | 高峰时段 |
|---|---|---|---|
| V4-Flash | 输入（缓存命中） | 0.05 | 0.10 |
| V4-Flash | 输入（缓存未命中） | 1.5 | 3.0 |
| V4-Flash | 输出 | 4.5 | 9.0 |
| V4-Pro | 输入（缓存命中） | 0.15 | 0.30 |
| V4-Pro | 输入（缓存未命中） | 4.5 | 9.0 |
| V4-Pro | 输出 | 13.5 | 27.0 |

并发限制：Flash 2500 / Pro 500；上下文 1M、最大输出 384K 均未变。

---

## 四、涨幅矩阵：到底涨了多少？

「涨价前」指 8/16 之前实际执行的价（6 月底已引入高峰翻倍）。逐档对比：

| 模型 | 计费项 | 旧·空闲 | 旧·高峰 | 新·空闲 | 新·高峰 | 涨幅 |
|---|---|---|---|---|---|---|
| Flash | 缓存命中 | 0.02 | 0.04 | 0.05 | 0.10 | **2.5 倍** |
| Flash | 缓存未命中 | 1.0 | 2.0 | 1.5 | 3.0 | **1.5 倍** |
| Flash | 输出 | 2.0 | 4.0 | 4.5 | 9.0 | **2.25 倍** |
| Pro | 缓存命中 | 0.025 | 0.05 | 0.15 | 0.30 | **6 倍** |
| Pro | 缓存未命中 | 3.0 | 6.0 | 4.5 | 9.0 | **1.5 倍** |
| Pro | 输出 | 6.0 | 12.0 | 13.5 | 27.0 | **2.25 倍** |

### 关于「最高涨 12 倍」的真相

刷屏的「12 倍」特指 **V4-Pro 的「缓存命中」在高峰时段对比更早的平铺价**（4–6 月峰谷引入前）：0.30 ÷ 0.025 = 12 倍。

如果拿「7 月已含峰谷的旧价」比，最高只有 6 倍。媒体报道混用了这两个口径，所以才有「涨 3 倍」和「涨 12 倍」两种说法——**都对，但对比基准不同**。

### 一个反直觉的规律

**你的缓存命中率越高，涨幅越大**。因为你原来主要吃便宜的缓存命中档：

- 命中率 40%（上下文多为新内容）：空闲时约涨 1.7 倍
- 命中率 90%（典型 Agent 循环）：空闲时约涨 2.1 倍

---

## 五、百万 token 等价换算

统一到「元 / 百万 tokens」，几个关键换算关系：

1. **缓存命中 vs 未命中**：命中价约是未命中的 1/30（旧价是 1/50）。缓存从「决定账单的主杠杆」降级为「几个杠杆之一」。
2. **输入 vs 输出**：输出价 = 未命中输入价的 3 倍（两模型一致）。
3. **高峰 vs 空闲**：全部固定 2 倍。
4. **Pro vs Flash**：Pro 全线是 Flash 的 3 倍。
5. **美元 ↔ 人民币**：DeepSeek 官方按约 **6.82 元/美元** 折算（如 $0.66 = 4.5 元、$3.96 = 27 元）。

**典型 Agent 负载实算（Flash 示例）**：输入 3 亿 token、缓存命中率 90%、输出 2000 万 token/月——旧价约 ¥10.6，新价全空闲约 ¥21.7（2 倍），全高峰约 ¥43.4（4 倍）。

---

## 六、同类型模型横评

> 元 / 百万 token，美元按 ≈7 折算。

| 模型 | 输入 | 输出 | 备注 |
|---|---|---|---|
| DeepSeek V4-Flash | 1.5 / 3.0 | 4.5 / 9.0 | 空闲 / 高峰 |
| DeepSeek V4-Pro | 4.5 / 9.0 | 13.5 / 27.0 | 空闲 / 高峰 |
| GPT-5.6 Luna（OpenAI） | ≈1.4 | ≈8.4 | 7 月底刚降 80% |
| GPT-5.6 Terra（OpenAI） | ≈14 | ≈84 | 旗舰档 |
| Claude Sonnet 5（Anthropic） | ≈14 | ≈70 | 8/31 后涨到 ≈21/105 |
| Claude Fable 5（Anthropic） | ≈70 | ≈350 | 顶级难题档 |
| Qwen3.8-Max（阿里） | 12 | 36 | 国产旗舰长程档 |

横向结论：

<div style="margin:16px auto;">
<svg viewBox="0 0 800 438" xmlns="http://www.w3.org/2000/svg" role="img" style="width:100%;height:auto;max-width:760px;font-family:-apple-system,Segoe UI,Microsoft YaHei,sans-serif;">
<text x="160" y="20" font-size="15" font-weight="bold" fill="#222">元 / 百万 tokens（对数刻度）</text>
<line x1="160.0" y1="38" x2="160.0" y2="412" stroke="#ddd" stroke-width="1"/>
<text x="160.0" y="34" font-size="9" fill="#999" text-anchor="middle">0.5</text>
<line x1="216.5" y1="38" x2="216.5" y2="412" stroke="#ddd" stroke-width="1"/>
<text x="216.5" y="34" font-size="9" fill="#999" text-anchor="middle">1</text>
<line x1="306.2" y1="38" x2="306.2" y2="412" stroke="#ddd" stroke-width="1"/>
<text x="306.2" y="34" font-size="9" fill="#999" text-anchor="middle">3</text>
<line x1="404.4" y1="38" x2="404.4" y2="412" stroke="#ddd" stroke-width="1"/>
<text x="404.4" y="34" font-size="9" fill="#999" text-anchor="middle">10</text>
<line x1="494.0" y1="38" x2="494.0" y2="412" stroke="#ddd" stroke-width="1"/>
<text x="494.0" y="34" font-size="9" fill="#999" text-anchor="middle">30</text>
<line x1="592.2" y1="38" x2="592.2" y2="412" stroke="#ddd" stroke-width="1"/>
<text x="592.2" y="34" font-size="9" fill="#999" text-anchor="middle">100</text>
<line x1="681.8" y1="38" x2="681.8" y2="412" stroke="#ddd" stroke-width="1"/>
<text x="681.8" y="34" font-size="9" fill="#999" text-anchor="middle">300</text>
<line x1="780.0" y1="38" x2="780.0" y2="412" stroke="#ddd" stroke-width="1"/>
<text x="780.0" y="34" font-size="9" fill="#999" text-anchor="middle">1000</text>
<text x="142" y="66" font-size="12.5" fill="#333" text-anchor="end" font-weight="bold">DeepSeek V4 Flash</text>
<rect x="160.0" y="48" width="235.8" height="14" fill="#1f77b4" rx="2" opacity="0.9"/>
<rect x="160.0" y="48" width="179.2" height="14" fill="#1f77b4" rx="2" opacity="0.45"/>
<text x="401.8" y="59" font-size="10.5" fill="#333">4.5~9</text>
<text x="160.0" y="41" font-size="8.5" fill="#999">输出</text>
<rect x="160.0" y="68" width="146.2" height="10" fill="#1f77b4" rx="2" opacity="0.35"/>
<text x="312.2" y="76" font-size="9.5" fill="#666">1.5~3</text>
<text x="160.0" y="62" font-size="8.5" fill="#aaa">输入(未命中)</text>
<text x="142" y="118" font-size="12.5" fill="#333" text-anchor="end" font-weight="bold">DeepSeek V4 Pro</text>
<rect x="160.0" y="100" width="325.4" height="14" fill="#1f77b4" rx="2" opacity="0.9"/>
<rect x="160.0" y="100" width="268.8" height="14" fill="#1f77b4" rx="2" opacity="0.45"/>
<text x="491.4" y="111" font-size="10.5" fill="#333">13.5~27</text>
<text x="160.0" y="93" font-size="8.5" fill="#999">输出</text>
<rect x="160.0" y="120" width="235.8" height="10" fill="#1f77b4" rx="2" opacity="0.35"/>
<text x="401.8" y="128" font-size="9.5" fill="#666">4.5~9</text>
<text x="160.0" y="114" font-size="8.5" fill="#aaa">输入(未命中)</text>
<text x="142" y="170" font-size="12.5" fill="#333" text-anchor="end" font-weight="bold">GPT-5.6 Luna</text>
<rect x="160.0" y="152" width="230.1" height="14" fill="#2ca02c" rx="2" opacity="0.9"/>
<text x="396.1" y="163" font-size="10.5" fill="#333">8.4</text>
<text x="160.0" y="145" font-size="8.5" fill="#999">输出</text>
<rect x="160.0" y="172" width="84.0" height="10" fill="#2ca02c" rx="2" opacity="0.35"/>
<text x="250.0" y="180" font-size="9.5" fill="#666">1.4</text>
<text x="160.0" y="166" font-size="8.5" fill="#aaa">输入(未命中)</text>
<text x="142" y="222" font-size="12.5" fill="#333" text-anchor="end" font-weight="bold">Qwen3.8 Max</text>
<rect x="160.0" y="204" width="348.8" height="14" fill="#ff7f0e" rx="2" opacity="0.9"/>
<text x="514.8" y="215" font-size="10.5" fill="#333">36</text>
<text x="160.0" y="197" font-size="8.5" fill="#999">输出</text>
<rect x="160.0" y="224" width="259.2" height="10" fill="#ff7f0e" rx="2" opacity="0.35"/>
<text x="425.2" y="232" font-size="9.5" fill="#666">12</text>
<text x="160.0" y="218" font-size="8.5" fill="#aaa">输入(未命中)</text>
<text x="142" y="274" font-size="12.5" fill="#333" text-anchor="end" font-weight="bold">Claude Sonnet 5</text>
<rect x="160.0" y="256" width="403.1" height="14" fill="#d62728" rx="2" opacity="0.9"/>
<text x="569.1" y="267" font-size="10.5" fill="#333">70</text>
<text x="160.0" y="249" font-size="8.5" fill="#999">输出</text>
<rect x="160.0" y="276" width="271.8" height="10" fill="#d62728" rx="2" opacity="0.35"/>
<text x="437.8" y="284" font-size="9.5" fill="#666">14</text>
<text x="160.0" y="270" font-size="8.5" fill="#aaa">输入(未命中)</text>
<text x="142" y="326" font-size="12.5" fill="#333" text-anchor="end" font-weight="bold">GPT-5.6 Terra</text>
<rect x="160.0" y="308" width="418.0" height="14" fill="#2ca02c" rx="2" opacity="0.9"/>
<text x="584.0" y="319" font-size="10.5" fill="#333">84</text>
<text x="160.0" y="301" font-size="8.5" fill="#999">输出</text>
<rect x="160.0" y="328" width="271.8" height="10" fill="#2ca02c" rx="2" opacity="0.35"/>
<text x="437.8" y="336" font-size="9.5" fill="#666">14</text>
<text x="160.0" y="322" font-size="8.5" fill="#aaa">输入(未命中)</text>
<text x="142" y="378" font-size="12.5" fill="#333" text-anchor="end" font-weight="bold">Claude Fable 5</text>
<rect x="160.0" y="360" width="534.4" height="14" fill="#d62728" rx="2" opacity="0.9"/>
<text x="700.4" y="371" font-size="10.5" fill="#333">350</text>
<text x="160.0" y="353" font-size="8.5" fill="#999">输出</text>
<rect x="160.0" y="380" width="403.1" height="10" fill="#d62728" rx="2" opacity="0.35"/>
<text x="569.1" y="388" font-size="9.5" fill="#666">70</text>
<text x="160.0" y="374" font-size="8.5" fill="#aaa">输入(未命中)</text>
<rect x="160.0" y="411" width="14" height="8" fill="#1f77b4" rx="1" opacity="0.9"/>
<text x="178.0" y="418" font-size="9.5" fill="#555">输出价（深色条=空闲，浅色叠层=高峰）</text>
<rect x="350.0" y="411" width="14" height="8" fill="#1f77b4" rx="1" opacity="0.35"/>
<text x="368.0" y="418" font-size="9.5" fill="#555">输入价（缓存未命中）</text>
</svg>
</div>

> 📌 **怎么读这张图**：横轴是模型，纵轴是元/百万 tokens（对数刻度，每格差 10 倍）。每个模型左侧浅色条=输入（缓存未命中），右侧深色条=输出；DeepSeek 的条是「空闲~高峰」区间（淡色到深色）。一眼可见：**DeepSeek 两条柱在最底部，Claude Fable 5 在最顶部（差约 40~70 倍）**。

- **空闲时段**：DeepSeek 仍是绝对地板价。Flash 输出 4.5 元，比 Qwen3.8-Max（36 元）便宜 8 倍、比 GPT-5.6 Terra（84 元）便宜 18 倍。
- **高峰时段**：Flash 输出 9 元 **已被 GPT-5.6 Luna（≈8.4 元）反超**；Pro 输出 27 元与 Qwen3.8-Max（36 元）差距缩到 1.3 倍。
- **第三方托管**（OpenRouter 上的 DeepInfra 等）：Flash 档第三方普遍更便宜（输入 $0.08~0.14 vs 官方高峰 $0.44），Pro 档官方空闲价仍无人能敌。

---

## 七、「60 倍价差」的真相（公众号文章勘误）

8 月 12 日 V4 Pro 转正当晚，多篇文章称「性能差 Claude Fable 5 仅 2.8%，价格差 60 倍」。这个「60 倍」是按**涨价前的 6 元输出价**对比 Claude Fable 5 约 360 元输出得出的。

但新价 8 月 17 日已经生效，V4 Pro 输出价变成 13.5（空闲）/ 27（高峰）元。重算：

- **空闲时段**：13.5 vs 360 → 约 **27 倍**
- **高峰时段**：27 vs 360 → 约 **13 倍**

「性能对标」的结论（2.8% 差距、DeepSWE 12.8→62.7、Agent 能力跃升）依然有效；但「60 倍价差」和「6 元输出价」**今天起已经作废**，做成本决策时务必用新价表重算。

---

## 八、落地建议

1. **错峰跑批**：非实时任务挪到 18:00 后，直接省一半（最无脑的省钱法）。
2. **保缓存命中率**：固定 System Prompt / 工具定义放上下文最前，命中率拉高可抵消大部分涨幅。
3. **高频档降级到 Flash**：Pro 是 Flash 的 3 倍，常规调用可路由到 Flash。
4. **美区团队占时区便宜，欧区上午撞高峰**：美国（东西岸）整个工作时段都落在空闲区，完全避开高峰价；欧洲团队上午正好是高峰时段（柏林/巴黎 9:00–12:00、伦敦 9:00–11:00），批量任务应挪到下午或晚上跑。

**海外团队高峰时段速查（2026 年夏令时）：**

| 团队所在地 | 时区 | 本地高峰时段 | 9-18 工作时段撞峰 |
|---|---|---|---|
| 北京 | UTC+8 | 9:00–12:00、14:00–18:00 | 7 小时 |
| 东京/首尔 | UTC+9 | 10:00–13:00、15:00–19:00 | 6 小时 |
| 印度 | UTC+5:30 | 6:30–9:30、11:30–15:30 | 4.5 小时 |
| 柏林/巴黎 | UTC+2 (CEST) | 3:00–6:00、8:00–12:00 | 3 小时（上午） |
| 伦敦 | UTC+1 (BST) | 2:00–5:00、7:00–11:00 | 2 小时（上午） |
| 纽约 | UTC-4 (EDT) | 前日 21:00–0:00、2:00–6:00 | 0 小时 ✅ |
| 旧金山 | UTC-7 (PDT) | 前日 18:00–21:00、23:00–3:00 | 0 小时 ✅ |

> ⚠️ 冬令时注意：北半球 10 月底后欧洲/美国进入冬令时，各时区换算相差 1 小时，峰窗整体错位；上表仅适用于 2026 年 8 月（夏令时）。

---

## 九、按任务选模型：性价比决策图

> 不同任务对延迟、质量、成本的要求不同，**没有「最好的模型」，只有「最合适的选择」**。下面按任务类型给出推荐（2026-08-17 涨价后）：

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
<td style="padding:8px 12px;border:1px solid #e0e0e0;"><b>V4 Flash 空闲时段</b></td>
<td style="padding:8px 12px;border:1px solid #e0e0e0;">≈4.5 元/百万输出</td>
<td style="padding:8px 12px;border:1px solid #e0e0e0;">谷价=峰价一半，非实时任务错峰立省 50%</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #e0e0e0;border-left:6px solid #4fa3d1;font-weight:bold;">高频实时对话<br><span style="font-weight:normal;color:#888;font-size:12px;">客服、聊天机器人</span></td>
<td style="padding:8px 12px;border:1px solid #e0e0e0;"><b>V4 Flash</b></td>
<td style="padding:8px 12px;border:1px solid #e0e0e0;">9 元/百万输出（峰）</td>
<td style="padding:8px 12px;border:1px solid #e0e0e0;">2500 并发，千 token 输出≈0.009 元</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #e0e0e0;border-left:6px solid #66b3ff;font-weight:bold;">Agent 多轮任务<br><span style="font-weight:normal;color:#888;font-size:12px;">编码助手、工具调用</span></td>
<td style="padding:8px 12px;border:1px solid #e0e0e0;"><b>V4 Flash + 高缓存命中</b></td>
<td style="padding:8px 12px;border:1px solid #e0e0e0;">命中输入仅 0.05 元</td>
<td style="padding:8px 12px;border:1px solid #e0e0e0;">固定前缀→命中率 60%+，输入几乎免费</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #e0e0e0;border-left:6px solid #ff9f43;font-weight:bold;">复杂推理/长文档<br><span style="font-weight:normal;color:#888;font-size:12px;">分析、总结、结构化</span></td>
<td style="padding:8px 12px;border:1px solid #e0e0e0;"><b>V4 Pro 空闲时段</b></td>
<td style="padding:8px 12px;border:1px solid #e0e0e0;">13.5 元/百万输出</td>
<td style="padding:8px 12px;border:1px solid #e0e0e0;">性能≈Claude Fable 5 的 97%，价格仅 1/26</td>
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
1. **能错峰就错峰**——非实时任务全部挪到 18:00 后跑，成本直接减半
2. **能缓存就缓存**——固定 System Prompt/工具定义，命中率决定 Agent 成本
3. **能不 Pro 就不 Pro**——Pro 是 Flash 的 3 倍，日常任务 Flash 够用
4. **贵模型只干贵活**——把旗舰模型留给真正需要能力天花板的场景

---

## 数据来源

- DeepSeek 官方定价页（api-docs.deepseek.com，8/17 已更新）
- 新浪财经、Reuters、Pandaily 报道
- ofox.io、aireiter.com 逐档价格核对
