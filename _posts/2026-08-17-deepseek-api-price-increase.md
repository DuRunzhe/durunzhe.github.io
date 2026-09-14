---
title: "主流大模型价格·能力·性价比横评（2026-08）：DeepSeek 涨价与 GLM-5.3-Flash 入局"
date: 2026-08-17
categories: ai
---

# 主流大模型价格、能力与性价比横评

> 📌 **版本 v2.2** · 初版 2026-08-17 · 更新 2026-08-27（新增 GLM-5.3-Flash 对比）· 更新 2026-09-09（Flash 系列降价，各表已按 9/10 新价同步）· 更新 2026-09-15（V4.1-Flash 换代发布 + 峰谷时段官方确认为工作日，见第十一章）

2026 年 8 月 13 日，DeepSeek 官宣 API 调价，8 月 17 日（北京时间零点）正式生效；9 月 10 日 Flash 系列又降价回撒。本文把历次价格版本、涨幅矩阵、同类型模型横评一次讲清，并勘误一篇流传甚广的公众号文章。

---

## 一、结论速览

1. **涨幅从 1.5 倍到 12 倍不等**，取决于「哪个模型、缓存命中还是未命中、高峰还是空闲」。
2. **涨得最狠的是「缓存命中」这一档**（Pro 涨 6 倍），过去近乎免费的那档成了最大涨幅来源，直接打击 Agent 类重缓存负载。
3. **涨得最少的是「缓存未命中」输入**（统一 1.5 倍），输出统一涨 2.25 倍。
4. **8/17 涨价后 DeepSeek 一度被反超，9/10 降价后部分夺回**——高峰时段 Flash 输出从 9 元降到 8 元，重新略低于 GPT-5.6 Luna（≈8.4 元）。
5. **8/26 智谱发布并开源 GLM-5.3-Flash（即匿名模型「牛来」Ox Alpha）**——输出约 3.5 元/百万 token（无峰谷），比 V4-Flash 空闲价（4 元）还低约 13%，官方称仅 DeepSeek 的 1/7（对应 V4-Pro 高峰价）；但「缓存命中」输入档 DeepSeek 仍更便宜。详见第十章。
6. **9/9 公告：9/10 12:00 起 Flash 系列降价**——命中 0.02 元（-60%）、未命中 1 元（-33%）、输出 4 元（-11%，均为空闲档）；除输出外回归涨价前价格，Pro 不变，各表已同步更新。
7. **9/10 同步换代：Flash 线升级为 V4.1-Flash**——全新架构最小尺寸模型，原生多模态视觉理解（Pro 反而不支持视觉）；Terminal-Bench 2.1 从 82.7 → 90.6 反超 V4-Pro，DeepSWE 74.2 超过 V4-Pro 与 GLM-5.3-Flash；模型名改为 `deepseek-flash`，旧名自动路由同价计费；V4-Pro 官宣 9/14 后继续服务。详见第十一章。

---

## 二、事件时间线

| 时间 | 动作 |
|---|---|
| 2026-04 | V4 预览版发布，推出 Pro / Flash 双线，限时 2.5 折 |
| 2026-05 | V4-Pro 限时折扣转永久价（输入 ¥3 / 输出 ¥6） |
| 2026-06 底 | 引入峰谷定价：北京时间 9:00–12:00、14:00–18:00 高峰翻倍 |
| 2026-07-31 | V4-Flash 正式版 API 公测，调用量起飞 |
| 2026-08-06 | 公告「整体上调，预计涨幅较大」 |
| 2026-08-13 | 官宣具体方案 + V4 Pro 正式版转正 |
| **2026-08-17** | **新价生效** |
| 2026-08-26 | 智谱发布 GLM-5.3-Flash，输出价低于 V4-Flash，输出地板价易主 |
| 2026-09-09 | 公告 Flash 系列降价（最高降幅 60%） |
| **2026-09-10** | **Flash 新价 12:00 生效 + V4.1-Flash 换代发布（模型名 `deepseek-flash`），V4-Pro 官宣保留** |

---

## 三、价格总览（官方，含全版本对照）

> 单位：元 / 百万 tokens。高峰时段 = 北京时间**周一至周五** 9:00–12:00、14:00–18:00（其余为空闲时段，**周末全天空闲价**）；空闲价 = 高峰价的 1/2。（官方价格页已明确标注「周一至周五」，此前「是否仅限工作日」的存疑正式解除。）

> ⏰ **计费时钟只有一个**：高峰/空闲按**北京时间**判定，全球所有调用方同一时刻看到的价格状态一致；你的**本地工作时间**落在哪个窗口，决定你实际付哪档价（见第八章时区换算）。

当前执行价（9/10 起；Flash 线已换代为 **V4.1-Flash**，价格不变，模型名 `deepseek-flash`）：

| 模型 | 计费项 | 空闲时段 | 高峰时段 |
|---|---|---|---|
| V4.1-Flash | 输入（缓存命中） | 0.02 | 0.04 |
| V4.1-Flash | 输入（缓存未命中） | 1.0 | 2.0 |
| V4.1-Flash | 输出 | 4.0 | 8.0 |
| V4-Pro | 输入（缓存命中） | 0.15 | 0.30 |
| V4-Pro | 输入（缓存未命中） | 4.5 | 9.0 |
| V4-Pro | 输出 | 13.5 | 27.0 |

并发限制：Flash 2500 / Pro 500；上下文 1M、最大输出 384K 均未变；V4.1-Flash 原生支持图像理解（Pro 不支持）。

### 全版本价格对照（按调价日期）

元 / 百万 token，格式：空闲 / 高峰（①期为无峰谷平价，单一值；— = 未开放）。

| 模型 | 计费项 | ① 5 月平价 | ② 6 月底–8/16 | ③ 8/17–9/9 | ④ 9/10 起 | 备注（④ vs ③；④ vs ①） |
|---|---|---|---|---|---|---|
| V4-Flash | 输入（缓存命中） | — | 0.02 / 0.04 | 0.05 / 0.10 | **0.02 / 0.04** | -60%；回归②原价 |
| V4-Flash | 输入（缓存未命中） | — | 1.0 / 2.0 | 1.5 / 3.0 | **1.0 / 2.0** | -33.3%；回归②原价 |
| V4-Flash | 输出 | — | 2.0 / 4.0 | 4.5 / 9.0 | **4.0 / 8.0** | -11.1%；仍为②的 2 倍 |
| V4-Flash | 月度成本（90% 命中负载*） | — | ≈7.5 | ≈14.9 | **≈11.5** | -22.8%；比② +53% |
| V4-Pro | 输入（缓存命中） | 0.025 | 0.025 / 0.05 | 0.15 / 0.30 | 0.15 / 0.30 | 未变；为①的 6 倍 |
| V4-Pro | 输入（缓存未命中） | 3.0 | 3.0 / 6.0 | 4.5 / 9.0 | 4.5 / 9.0 | 未变；为①的 1.5 倍 |
| V4-Pro | 输出 | 6.0 | 6.0 / 12.0 | 13.5 / 27.0 | 13.5 / 27.0 | 未变；为①的 2.25 倍 |
| V4-Pro | 月度成本（90% 命中负载*） | ≈21.7 | ≈42.7 | ≈44.6 | ≈44.6 | 未变；为①的约 2 倍 |

> *负载口径：输入 3000 万 token、缓存命中率 90%、输出 200 万 token/月，按各期空闲价计（① 为平价）。Flash ① 期（5 月）正式 API 尚未公测，故无该期价格。

**一眼看懂价格往返**：②引入峰谷（高峰翻倍）→ ③全面涨价（Flash 最高 2.5 倍、Pro 最高 6 倍）→ ④ Flash 把命中/未命中档完全退回②原价，只留输出档 2 倍涨幅，Pro 全程未动。**Flash 实质上从「全面涨价」回撤为「仅输出涨价」**。

---

## 四、「涨了 12 倍」还是「涨了 3 倍」？（口径勘误）

各档涨幅已在上表②→③列（Flash 最高 2.5 倍、Pro 最高 6 倍）。刷屏的「12 倍」特指 **V4-Pro「缓存命中」高峰时段对比更早的平铺价**（4–6 月峰谷引入前）：0.30 ÷ 0.025 = 12 倍；若拿「7 月已含峰谷的旧价」比，最高只有 6 倍。媒体报道混用了两个基准——**都对，但口径不同**。

### 一个反直觉的规律

**你的缓存命中率越高，涨幅越大**。因为你原来主要吃便宜的缓存命中档：

- 命中率 40%（上下文多为新内容）：空闲时约涨 1.7 倍
- 命中率 90%（典型 Agent 循环）：空闲时约涨 2.1 倍

---

## 五、百万 token 等价换算

统一到「元 / 百万 tokens」，几个关键换算关系：

1. **缓存命中 vs 未命中**：命中价是未命中的 1/50（9/10 起回到涨价前的比例；8/17–9/9 曾是 1/30）。
2. **输入 vs 输出**：Pro 输出价 = 未命中输入价的 3 倍；Flash 8/17–9/9 期间同为 3 倍，9/10 降后拉大为 4 倍。
3. **高峰 vs 空闲**：全部固定 2 倍。
4. **Pro vs Flash**：8/17 起官方定价梯度为 3 倍；9/10 Flash 降价后拉大到 3.4（输出）～ 7.5 倍（命中档）。
5. **美元 ↔ 人民币**：DeepSeek 官方按约 **6.82 元/美元** 折算（如 $0.66 = 4.5 元、$3.96 = 27 元）。

---

## 六、同类型模型横评

> 元 / 百万 token，美元按 ≈7 折算。

| 模型 | 输入 | 输出 | 备注 |
|---|---|---|---|
| DeepSeek V4.1-Flash | 1.0 / 2.0 | 4.0 / 8.0 | 空闲 / 高峰；9/10 降价+换代后 |
| DeepSeek V4-Pro | 4.5 / 9.0 | 13.5 / 27.0 | 空闲 / 高峰 |
| GLM-5.3-Flash（智谱） | ≈1.05 | ≈3.5 | 8/26 发布即开源，无峰谷 |
| GPT-5.6 Luna（OpenAI） | ≈1.4 | ≈8.4 | 7 月底刚降 80% |
| GPT-5.6 Terra（OpenAI） | ≈14 | ≈84 | 旗舰档 |
| Claude Sonnet 5（Anthropic） | ≈14 | ≈70 | 8/31 后涨到 ≈21/105 |
| Claude Fable 5（Anthropic） | ≈70 | ≈350 | 顶级难题档 |
| Qwen3.8-Max（阿里） | 12 | 36 | 国产旗舰长程档 |

横向结论：

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

> 📌 **怎么读这张图**：横轴是模型，纵轴是元/百万 tokens（对数刻度，每格差 10 倍）。每个模型左侧浅色条=输入（缓存未命中），右侧深色条=输出；DeepSeek 的条是「空闲~高峰」区间（淡色到深色），紫色条 GLM-5.3-Flash 为单一定价。一眼可见：**GLM-5.3-Flash 与 DeepSeek 两条柱在最底部，Claude Fable 5 在最顶部（差约 100 倍）**。

- **空闲时段**：GLM-5.3-Flash 输出 3.5 元（无峰谷）仍比 V4-Flash 空闲 4 元低约 13%，保持输出地板价；DeepSeek Flash 则比 Qwen3.8-Max（36 元）便宜 9 倍、比 GPT-5.6 Terra（84 元）便宜 21 倍。
- **高峰时段**：V4-Flash 输出降为 8 元，**重新略低于 GPT-5.6 Luna（≈8.4 元）**（9/10 前 9 元曾被反超）；与 GLM-5.3-Flash（3.5 元）仍差 2.3 倍；Pro 输出 27 元与 Qwen3.8-Max（36 元）差距缩到 1.3 倍。
- **第三方托管**（OpenRouter 上的 DeepInfra 等）：Flash 档第三方普遍更便宜（输入 $0.08~0.14 vs 官方高峰 $0.44），Pro 档官方空闲价仍无人能敌。

### 厂商官网 / API 购买地址

| 厂商 | 模型 | 官网 / 购买地址 |
|---|---|---|
| DeepSeek | V4-Flash / V4-Pro | [platform.deepseek.com](https://platform.deepseek.com)（API 平台） |
| OpenAI | GPT-5.6 Luna / Terra | [platform.openai.com](https://platform.openai.com)（API 平台） |
| Anthropic | Claude Sonnet 5 / Fable 5 / Opus 4.8 | [console.anthropic.com](https://console.anthropic.com)（Console） |
| 阿里云 | Qwen3.8-Max | [bailian.console.aliyun.com](https://bailian.console.aliyun.com)（百炼） |
| 智谱 | GLM-5.3-Flash / GLM-5.3 | [open.bigmodel.cn](https://open.bigmodel.cn)（开放平台） · 国际站 [z.ai](https://z.ai) |

---

## 七、「60 倍价差」的真相（公众号文章勘误）

8 月 12 日 V4 Pro 转正当晚，多篇文章称「性能差 Claude Fable 5 仅 2.8%，价格差 60 倍」。这个「60 倍」是按**涨价前的 6 元输出价**对比 Claude Fable 5 约 360 元输出得出的。

但 8/17 新价生效后，V4 Pro 输出价变为 13.5（空闲）/ 27（高峰）元。重算：

- **空闲时段**：13.5 vs 360 → 约 **27 倍**
- **高峰时段**：27 vs 360 → 约 **13 倍**

「性能对标」的结论（2.8% 差距、DeepSWE 12.8→62.7、Agent 能力跃升）依然有效；但「60 倍价差」和「6 元输出价」8/17 起已作废，做成本决策时务必用最新价表重算。

---

## 八、落地建议

1. **错峰跑批**：非实时任务挪到 18:00 后，直接省一半（最无脑的省钱法）。
2. **保缓存命中率**：固定 System Prompt / 工具定义放上下文最前，命中率拉高可抵消大部分涨幅。
3. **高频档降级到 Flash**：Pro 是 Flash 的 3.4～7.5 倍，常规调用可路由到 Flash。
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
<td style="padding:8px 12px;border:1px solid #e0e0e0;"><b>V4 Flash 空闲时段</b></td>
<td style="padding:8px 12px;border:1px solid #e0e0e0;">≈4 元/百万输出（9/10 起）</td>
<td style="padding:8px 12px;border:1px solid #e0e0e0;">谷价=峰价一半，非实时任务错峰立省 50%</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #e0e0e0;border-left:6px solid #4fa3d1;font-weight:bold;">高频实时对话<br><span style="font-weight:normal;color:#888;font-size:12px;">客服、聊天机器人</span></td>
<td style="padding:8px 12px;border:1px solid #e0e0e0;"><b>V4 Flash</b></td>
<td style="padding:8px 12px;border:1px solid #e0e0e0;">8 元/百万输出（峰）</td>
<td style="padding:8px 12px;border:1px solid #e0e0e0;">2500 并发，千 token 输出≈0.008 元</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #e0e0e0;border-left:6px solid #66b3ff;font-weight:bold;">Agent 多轮任务<br><span style="font-weight:normal;color:#888;font-size:12px;">编码助手、工具调用</span></td>
<td style="padding:8px 12px;border:1px solid #e0e0e0;"><b>V4 Flash + 高缓存命中</b></td>
<td style="padding:8px 12px;border:1px solid #e0e0e0;">命中输入仅 0.02 元（9/10 起）</td>
<td style="padding:8px 12px;border:1px solid #e0e0e0;">固定前缀→命中率 60%+，输入几乎免费</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #e0e0e0;border-left:6px solid #9467bd;font-weight:bold;">高性价比 Agent / 批量<br><span style="font-weight:normal;color:#888;font-size:12px;">8/26 新增选项</span></td>
<td style="padding:8px 12px;border:1px solid #e0e0e0;"><b>GLM-5.3-Flash（智谱）</b></td>
<td style="padding:8px 12px;border:1px solid #e0e0e0;">≈3.5 元/百万输出</td>
<td style="padding:8px 12px;border:1px solid #e0e0e0;">输出比 V4-Flash 空闲价（4 元）低约 13%，开源 MIT 可自托管；缓存命中输入不如 DeepSeek 划算</td>
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
3. **能不 Pro 就不 Pro**——Pro 是 Flash 的 3.4～7.5 倍，日常任务 Flash 够用
4. **贵模型只干贵活**——把旗舰模型留给真正需要能力天花板的场景

---

## 十、新变量：GLM-5.3-Flash 入场（8/26）

> 8 月 26 日智谱发布 GLM-5.3-Flash 后追加；各表价格已同步按 9/10 新价更新。

### 「牛来」掉马：Ox Alpha = GLM-5.3-Flash

8 月 26 日，智谱正式发布并开源 GLM-5.3-Flash。官方确认，此前突然出现在 OpenCode 和 OpenRouter、被全网猜测的神秘匿名模型 Ox Alpha（网友称「牛来」），其实就是 GLM-5.3-Flash 的匿名预览版。匿名测试期间它很快成为当周最受欢迎的模型之一——**且所有真实用户流量全部跑在国产 AI 芯片上**。

### 价格：输出档全面低于 DeepSeek（含逐档对照）

GLM-5.3-Flash 标准 API 定价（美元/百万 token，人民币按 ≈7 折算，无峰谷、单一价）：

| 计费项 | 美元 | 人民币≈ |
|---|---|---|
| 输入（缓存未命中） | 0.15 | ≈1.05 |
| 输出 | 0.50 | ≈3.5 |
| 输入（缓存命中） | 0.03 | ≈0.21 |

官方定位：正常价仅 GLM-5.3 的 1/10，限时折扣更低到 1/20；约 Claude Opus 4.8 的 1/40、DeepSeek 的 1/7。

**与 DeepSeek 逐档对照**（元/百万 token；DeepSeek 为 空闲/高峰）：

| 计费项 | GLM-5.3-Flash | V4.1-Flash | V4-Pro |
|---|---|---|---|
| 输入（缓存命中） | 0.21 | 0.02 / 0.04 | 0.15 / 0.30 |
| 输入（缓存未命中） | 1.05 | 1.0 / 2.0 | 4.5 / 9.0 |
| 输出 | 3.5 | 4.0 / 8.0 | 13.5 / 27.0 |

（DeepSeek Flash 一列为 9/10 降价后新价，现由 V4.1-Flash 同价接替；8/17–9/9 旧价为 0.05/0.10、1.5/3.0、4.5/9.0）

三点结论：

1. **输出价全面更低**：GLM 3.5 元 < V4-Flash 空闲 4 元（低约 13%）< V4-Flash 高峰 8.0 元（低 56%）< V4-Pro 高峰 27 元（低 87%）。「DeepSeek 是输出地板价」的位置在 8/26–9/9 期间易主，9/10 降价后差距明显收窄但仍未夺回。
2. **缓存命中档 DeepSeek 反而更便宜**：0.02~0.30 元 vs GLM 0.21 元（9/10 起 Flash 命中价 0.02 元，只有 GLM 的 1/10）。DeepSeek 命中/未命中价差回到 50 倍，GLM 只有 5 倍——对重缓存 Agent 负载（多轮对话、工具循环），**DeepSeek 仍是输入成本之王**；GLM 的便宜主要落在输出侧。
3. **官方「1/7」的口径**：约对应 V4-Pro 高峰输出价（27 ÷ 3.5 ≈ 7.7）；若拿 V4-Flash 空闲输出比，实际只有 1/1.3。做成本对比时先确认基准，别被单一倍数带偏。

### 能力：57 分进入第一梯队（含对比）

Artificial Analysis 综合智能指数 57 分，与 Claude Opus 4.8 处于同一分数水平；AA 测试中每任务折扣成本仅约 $0.045（≈0.3 元）。

| 指标 | GLM-5.3-Flash | 对比对象 |
|---|---|---|
| AA 综合智能指数 | 57 | ≈ Claude Opus 4.8（同水平） |
| DeepSWE v1.1 | 63.4（GLM-5.2 为 46.2） | DeepSeek V4 Pro 报道口径 62.7，同水平* |
| AutomationBench | 48.8（GLM-5.2 为 26.2） | — |
| Z.ai Code Bench（最高推理） | 29.0 | Claude Opus 4.8 = 29.5 |

> *DeepSWE 两项数据来源版本/口径不同（V4 Pro 为媒体报道的 DeepSWE 得分，GLM 为智谱公布的 v1.1），不宜直接断言谁强，仅作量级参考。**可以确定的是**：达到这一档 Agent 编码能力，GLM 的 API 输出价只有 DeepSeek 的几分之一。另注意 Z.ai Code Bench 是智谱自家 benchmark，29.0 vs 29.5 要留一点余地看。

### 为什么便宜：320B 只激活 18B + 混合注意力

- **参数**：320B 总参数、每次只激活 18B（GLM-4.5 为 355B/32B），层数 92 → 45。模型变「轻」，能力反而超过 GLM-5.2，编程和 Agent 能力逼近 Claude Opus 4.8。
- **架构**：首次采用稀疏注意力 + 线性注意力混合架构——长上下文不再全量昂贵计算，相比 GLM-5.3，Attention 计算量降至约 1/3，KV Cache 占用降约 4.4 倍。
- **定性**：不是 GLM-5.3 的「青春版」，而是重新设计的效率架构——**旗舰的能力，Flash 的成本**。

### 原生多模态 + 100 万上下文

GLM-5 系列第一个原生多模态模型：预训练阶段就融合文本/图片等多模态数据（预训练数据 30T Token），支持最高 100 万 Token 上下文。Agent 可以直接看网页、理解界面并点击操作，也能根据视觉反馈检查自己刚生成的内容再修改——定位不仅是 Coding，而是「看得见、点得动、做得完」的 Agent 底座。

### 全部跑在国产芯片上（容易被忽略的细节）

Ox Alpha 匿名测试期间，所有真实用户流量由国产 AI 芯片承载：基于 SGLang 的推理系统（编码/预填充/解码分阶段优化），运行在数万张国产加速卡上，实现约 3 倍端到端服务性能提升。模型 + 芯片 + 推理框架 + 大规模真实流量，国产组合完成了一次实战验证。

### 发布即开源

与 GLM-5.3 发布时还要等两周才开放权重不同，GLM-5.3-Flash 直接开放权重：Hugging Face 已上线（huggingface.co/zai-org/GLM-5.3-Flash），MIT License，本地部署支持 SGLang、vLLM、TokenSpeed。

### 对 DeepSeek 定价的影响（个人判断，9/9 已部分应验）

- DeepSeek 8/17 刚涨完价，8/26 GLM 就以更低的输出价入场，且开源、可自托管——「涨价护城河」被削了一刀。
- **预判应验**：8/27 本文曾判断「若 GLM 低价策略持续，DeepSeek 的峰谷涨价逻辑可能反过来被压出『Flash 特惠档』」——9/9 DeepSeek 即公告 Flash 全线降价，除输出外基本回归涨价前水平。
- 短期：DeepSeek 的缓存命中档（0.02 元）+ 2500 并发，重缓存负载仍是输入侧最优；输出侧 GLM-5.3-Flash 仍略便宜且可自托管。
- 中长期：价格战进入「同样一块钱能买到多少智能」的阶段，Flash 档已回到「以量取胜」的低价路线，Pro 档是否跟进是下一个观察点。

---

## 十一、DeepSeek 换代反击：V4.1-Flash（9/10）

> 9/15 追加：降价只是 9/10 的一半动作，另一半是 Flash 线换代。

### 换了什么：全新架构 + 原生多模态

- **V4.1-Flash 是全新模型结构系列中的最小尺寸模型**，官方称设计初衷为「能力上限更高、推理速度更快、吞吐更大、可扩展到更大参数模型」——同架构更大模型可期。
- **原生多模态视觉理解**：8/21 的实验模型 V4-Flash-Vision-Exp（多模态 Agent 能力接近 Opus-4.8）即其前身，已随 V4.1-Flash 上线而下线。图像理解能力反超 Pro（Pro 不支持视觉）。
- **价格与 9/10 降价后的 Flash 完全一致**，本文所有 Flash 价格表直接适用；上下文 1M / 输出 384K / 并发 2500 均不变。

### 模型名变更（API 迁移注意）

| 模型名 | 说明 |
|---|---|
| `deepseek-flash` | **推荐**，指向 V4.1-Flash |
| `deepseek-v4-flash` / `deepseek-v4-flash-vision-exp` | 旧名已下线，暂时自动路由到 V4.1-Flash，按 Flash 价计费 |

### 能力：Agent/终端基准明显抬升（官方口径）

| 基准 | V4.1-Flash | 上代 V4-Flash 正式版 | V4-Pro 正式版 |
|---|---|---|---|
| Terminal-Bench 2.1 | **90.6** | 82.7 | 87.9（被反超） |
| DeepSWE | **74.2** | 54.4 | 62.7 |
| NL2Repo | 65.4 | 54.2 | 61.5 |
| Automation-Bench | 54.8 | 25.1 | 31.8 |
| Agents' Last Exam | 31.8 | 25.2 | 25.7 |
| GPQA Diamond | 90.9 | — | — |
| HLE（带工具） | 63.9 | — | — |
| Codeforces Rating | 3471 | — | — |

> 同价位 Agent 能力整体上一档：DeepSWE 74.2 反超 V4-Pro（62.7）与 GLM-5.3-Flash（63.4，智谱口径 v1.1）；Terminal-Bench 2.1 90.6 也超过 V4-Pro 的 87.9——**Flash 档买到 Pro 档的 Agent/终端能力**，加上原生视觉，「同价更智能」直接回应 GLM 的低价攻势。

### V4 Pro 保留 + 峰谷时段勘误

- **V4 Pro 继续服务**：官方原计划 9/14 后调整 V4 Pro 服务，9/10 更新为「应广大用户需求，9/14 之后继续提供 API 调用服务，计费方式保持不变」。
- **峰谷为工作日制**：官方价格页已明确高峰时段为**周一至周五**——第八章时区表按工作日理解即可，**周末跑批全天空闲价**，错峰空间比原文判断的更大。

---

## 数据来源

- DeepSeek 官方定价页（api-docs.deepseek.com/quick_start/pricing）与官方更新日志（api-docs.deepseek.com/zh-cn/updates，含 9/10 V4.1-Flash 发布公告）及 9/9 开放平台调价公告（界面新闻/澎湃/新浪报道）
- 新浪财经、Reuters、Pandaily 报道
- ofox.io、aireiter.com 逐档价格核对
- 智谱官方发布（z.ai/blog/glm-5.3-flash，8/26）
- Hugging Face：huggingface.co/zai-org/GLM-5.3-Flash（MIT License）
- Artificial Analysis 综合智能指数
- 微信公众号文章《GLM-5.3 Flash 来了！比 DeepSeek 更强、更便宜》（8/27 阅读，含官方口径与 benchmark 数据）
