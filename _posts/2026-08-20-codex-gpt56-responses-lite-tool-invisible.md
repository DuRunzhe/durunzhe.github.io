---
title: "Codex CLI + GPT-5.6 工具全部「消失」：Responses Lite 私有格式与第三方网关的兼容性坑"
date: 2026-08-20
categories: [ai, tooling]
tags: [Codex, GPT-5.6, Responses Lite, 第三方网关, 排障]
---

# Codex CLI + GPT-5.6 工具全部「消失」

> 环境：codex-cli 0.147.0 · macOS · 自定义中转（`wire_api = "responses"`）· 模型 `gpt-5.6-sol / terra / luna`
> 状态：已定位根因并修复

## 一、问题现象

用 Codex CLI 搭配 **GPT-5.6 系列模型**时，会话拿不到任何可执行工具。典型表现：

- 问它 git 状态，它回复：**「当前会话未提供终端执行工具，无法直接读取 Git 状态。请在仓库根目录执行 `git status --short --branch`…」**，让你手动执行。
- 英文侧原话：*"I can't run `ls` because no shell execution tool is available in this session."*（见 [openai/codex#31894](https://github.com/openai/codex/issues/31894)）
- 不只是 shell：文件读写、自定义 MCP 工具也可能全部不可见。

**关键判据**：同一仓库、同样提示词，换成 `gpt-5.5` 就能正常调用工具——说明不是仓库或用户操作的问题，而是 **GPT-5.6 + 特定后端（第三方中转站）的组合触发**。

## 二、影响版本

| 维度 | 说明 |
|---|---|
| 引入时间 | GPT-5.6 模型进入 codex 内置模型目录（约 2026-07，v0.144/v0.145 时代），5.6 系列条目在二进制内置目录中默认 `use_responses_lite: true` |
| 官方确认报错版本 | `codex-cli 0.144.0`（#31894 报告者环境） |
| 复现范围 | 0.144.5、0.145.0-alpha.18（#33679）、0.146、0.147.0 均受影响 |
| 触发条件 | ① 模型为 gpt-5.6 系列；② 后端不是 OpenAI 原生服务，而是第三方中转/网关（Azure、CPA、sub2api 等） |
| 里程碑 | v0.145.0（2026-07-21）内置模型全面迁移到 GPT-5.6 Terra/Luna，多智能体 V2 转正，受影响面扩大 |

`use_responses_lite` 开关逻辑由提交 [e0096db（PR #26487）](https://github.com/openai/codex/commit/e0096db6dc8a2f89394986123802a676a1be20c5) 加入。

## 三、对应 Issue

| Issue | 内容 | 状态 |
|---|---|---|
| [#31894](https://github.com/openai/codex/issues/31894) | **核心问题**：`codex exec` + `gpt-5.6-sol` 时 `additional_tools` 里的工具声明未被后端提升为可调用工具，模型报「没有 shell 工具」 | 打开中；无维护者回复、无 assignee |
| [#31870](https://github.com/openai/codex/issues/31870) / [#31875](https://github.com/openai/codex/issues/31875) / [#31882](https://github.com/openai/codex/issues/31882) | Azure AI Foundry 三连败：拒绝 Lite 内部头（400）、`collaboration` 命名空间被保留、`additional_tools` 被静默丢弃 | 打开中 |
| [#33679](https://github.com/openai/codex/issues/33679) | 5.6 Sol 开启 Responses Lite 后自定义 MCP 工具被隐藏；`use_responses_lite: false` 即恢复 | 打开中 |
| [#34487](https://github.com/openai/codex/issues/34487) | Desktop 端 `model_catalog_json` 已加载但选择器不显示自定义模型（衍生缺陷） | 打开中 |
| [#35932](https://github.com/openai/codex/issues/35932) | 自定义 provider 下子代理收不到 `spawn_agent` 任务（`TASK_PAYLOAD_MISSING`） | 打开中 |
| [#36382](https://github.com/openai/codex/issues/36382) | DeepSeek 官方配置下工具静默不可用（同族问题） | 打开中 |
| 相关 #30861 / #31475 | 工具调用发出后直接崩溃（与「工具不可见」相反的另一类故障） | — |
| 相邻已修复 | `execexec` 命名空间碰撞（`namespace == name` 查找失败）、工具 schema 双写（保留 `additional_tools` 的同时写回顶层 `tools`） | 已修复（只覆盖 OpenAI 原生路径） |

## 四、官方声明

**OpenAI 官方目前没有针对「第三方中转站 + GPT-5.6 工具不可用」给出正式声明或完整修复。** 可查证事实：

- [#31894](https://github.com/openai/codex/issues/31894) 处于无人维护、无官方回复状态，仅报告者本人提交候选补丁（工具 schema 同时保留在 `additional_tools` 与顶层 `tools`，并补回归测试）。
- 相邻问题部分修复已合入，但只覆盖 OpenAI 原生路径，**没有解决第三方网关不认 `additional_tools` 的根本问题**。
- 结论：**官方层面当前无可用修复**，「禁用 Responses Lite」是社区验证过的稳定绕行方案（参考 [Responses Lite 机制分析](https://codex.danielvaughan.com/2026/07/26/codex-cli-responses-lite-wire-format-gpt56-tool-visibility-azure-provider-compatibility/)）。

## 五、根因机制

1. **模型目录硬编码**：GPT-5.6 条目在 codex 内置目录 `models.json` 里标记 `"use_responses_lite": true`。
2. **请求形状改变**（Responses Lite 私有格式）：
   - 顶层 `tools` 设为 `null`（标准位置没有工具 schema）；
   - 工具 schema 塞进 `input[0]` 的 `additional_tools` item（`role: "developer"`）；
   - 带内部头 `X-OpenAI-Internal-Codex-Responses-Lite` 通知后端按此解析；
   - 多智能体 V2 工具（`spawn_agent` 等）走 `collaboration` 命名空间，自 v0.144.4 起默认加密。
3. **第三方网关不兼容**：丢弃 `additional_tools`、不提升嵌套工具声明、或拒绝内部头（Azure 返回 400）。
4. **结果**：模型拿到零个可调用工具——没有 shell、没有文件系统、没有 MCP，只能回复「当前会话未提供终端执行工具」。

一句话：**Responses Lite 是面向 OpenAI 自家后端做的私有传输优化，却被默认对所有人开启，第三方网关无法解析，工具因此集体丢失。**

## 六、修复方式（按可靠性排序）

1. **禁用 Responses Lite（推荐）**：复制内置模型目录 → 把 5.6 三个模型的 `use_responses_lite` 改为 `false` → `config.toml` 增加 `model_catalog_json` 指向自定义目录 → 重启 codex。
2. **升级/更换中转站**：让网关兼容 GPT-5.6 新请求形状与 `/alpha/search` 端点（CPA/sub2api 类升级后即修复）。
3. **换模型**：用 `gpt-5.4` 或网关可正确处理、非 Lite 的模型。
4. **换官方路径**：直接用 OpenAI 原生 API / ChatGPT 登录，绕开中转。
5. **降级 codex**（如 0.143.0），临时手段，会丢新功能。
6. **等官方修复**：关注 [#31894](https://github.com/openai/codex/issues/31894) 更新。

## 七、实操步骤（方案一）

```bash
# 1. 生成内置模型目录（含 use_responses_lite 标记）
codex debug models --bundled > ~/.codex/models_cache.json

# 2. 复制到自己的目录（注意：models_cache.json 会被 codex 覆盖，务必另存）
mkdir -p ~/.codex/model-catalogs
cp ~/.codex/models_cache.json ~/.codex/model-catalogs/models-no-lite.json

# 3. 编辑 models-no-lite.json：把 gpt-5.6-sol / terra / luna 三个模型的
#    use_responses_lite 改为 false（复制完整条目再改，保留 base_instructions 等必填字段）
```

`config.toml` 增加一行（**必须绝对路径，不能用 `~`**）：

```toml
model_catalog_json = "/Users/<yourname>/.codex/model-catalogs/models-no-lite.json"
```

验证：

```bash
codex debug models   # 确认三个 5.6 模型均为 use_responses_lite = False
```

**端到端验证**：修复后 codex 已能正常调用 `exec` shell 工具——让模型执行 `git status --short --branch`，它成功运行并正确报告了结果，说明第三方网关对标准 Responses 工具调用（顶层 `tools`）正常工作，修复生效。

## 八、注意事项 / 排障提示

- `model_catalog_json` **必须用绝对路径**，写 `~` 会报 `No such file or directory (os error 2)`。
- 改目录时**复制完整条目再改**（保留 `base_instructions`、`supports_reasoning_summaries`、`visibility` 等必填字段），不要手写精简 JSON。
- `codex debug models --bundled` 或 `~/.codex/models_cache.json` 会被 codex 覆盖，务必另存到自己的目录。
- 若重启后仍有问题，优先检查中转站对标准 Responses 工具调用（顶层 `tools`）的支持情况。
