---
title: "一种将浏览器操作 CLI 化的 Skill 设计模式"
date: 2026-05-23
categories: AI Skill 设计
---

# 一种将浏览器操作CLI化的SKILL

设计哲学：用文件系统替代状态机,**把浏览器的状态和操作抽象为文件系统和 CLI 命令的一种 Skill 设计模式**。



**将任意网站的浏览器操作抽象为三个 CLI 命令**的 Skill。

核心抽象：三个动词

```
$ websim auth-probe   →  "我还能用吗？"
$ websim discover     →  "这个网站怎么交互？"
$ websim request      →  "帮我做这件事。"
```

传统浏览器自动化里，登录态是一个隐式的、易丢失的状态——关掉浏览器就没了。

Web-Simulator 把状态**物化为文件**：

```
# 登录一次，生成文件
~/.web-simulator/.session/sites/bigmodel.cn/default/
├── cookies.json    # "这是我的身份"
└── meta.json       # "这是关于身份的说明"

# 之后所有命令自动读取这些文件
# 用户不需要关心 "怎么带着 cookie"——CLI 替你管了
```

这和 Git 的 .git/ 目录、Docker 的 docker volume 是一样的思想——**把易失的状态固化为可复用的文件，然后用 CLI 操作这些文件。**

工作流演进的三个台阶:

```
台阶 1: 点来点去
  ┌─────────────┐
  │ 打开浏览器    │  ← 人在操作，不可复现
  │ 登录、导航、点击 │
  └─────────────┘

台阶 2: 浏览器脚本化 (Playwright)
  ┌─────────────┐
  │ page.click() │  ← 程序操作，可复现
  │ page.fill()  │     但依赖 DOM，一改就崩
  └─────────────┘

台阶 3: CLI 化 (web-simulator 定位)
  ┌─────────────┐
  │ websim check │  ← 命令操作，不依赖 DOM
  │ websim buy   │     登录态透明、API 优先、可调度
  └─────────────┘
```



关键设计原则



1. **按域名隔离** — 每个网站的登录态完全独立
2. **env 分层** — 同域名的不同环境（测试/线上）用 --env 区分
3. **API 优先** — 能走 HTTP 的不上浏览器，fallback-policy 只在 API 失败时启用
4. **Chrome 隔离** — CDP 必须用 ~/.web-simulator/.chrome-profiles/ 下的独立 profile，绝不碰用户日常浏览器
5. **非侵入** — 不做 pkill Chrome 等进程级清理，不影响用户正在使用的 Chrome
6. **兜底留白** — fallback-policy.js 的 FALLBACKS 注册表是空的，留给各站点按需注册

三层架构：

```
┌────────────────────────────────────────────────┐
│              SKILL.md（声明层）                  │
│  触发条件 · 输入规范 · 安全红线 · Gotchas         │
├────────────────────────────────────────────────┤
│        scripts/websim_router.js（路由层）        │
│  统一入口 → 分发到具体脚本 → 失败回退到浏览器      │
├──────────┬──────────┬──────────┬───────────────┤
│  auth    │ discover │ request  │  lib/（基础设施）│
│ _probe   │ _flow    │ _api     │                │
│ .js      │ .js      │ .js      │                │
└──────────┴──────────┴──────────┴───────────────┘
```

基础设施（lib/）:

```
| 模块                 | 职责         | 关键能力                                   |
| ------------------ | ---------- | -------------------------------------- |
| constants.js       | 全局常量       | AUTH_STATES、DATA_ROOT、站点配置             |
| session-store.js   | 会话存储       | 按 <domain>/<env> 读写 cookies.json       |
| api-session.js     | API 会话     | 加载/验证/刷新登录态，自动 CDP 恢复                  |
| cdp-session.js     | CDP 连接     | 启动隔离 Chrome、连接调试端口、导航/读 cookie         |
| web-api.js         | HTTP 客户端   | 带 cookie/auth 的 GET/POST，支持 auth-probe |
| wrapper-store.js   | Wrapper 存储 | 按 workflow 管理 api-discovery.json 等     |
| args.js            | 参数解析       | --base-url / --auth-probe / --env 等    |
| fallback-policy.js | 降级策略       | API 失败 → 浏览器兜底（当前注册表为空）                |
```

session生命周期：

```
                 ┌──────────┐
                 │  加载存储  │
                 │  cookies  │
                 └────┬─────┘
                      ▼
              ┌───────────────┐
              │  auth-probe    │ ← 调 /api/me 验证
              │  返回状态       │
              └───┬───┬───┬───┘
                  │   │   │
         authenticated expired sso_required
                  │   │   │
                  ▼   ▼   ▼
              直接用  CDP刷新  启动Chrome
                      │      手动登录
                      ▼       │
                  保存cookies ─┘
```

