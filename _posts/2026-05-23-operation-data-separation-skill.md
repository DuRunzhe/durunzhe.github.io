---
title: "操作与数据分离的 Skill 设计模式"
date: 2026-05-23
categories: AI Skill 设计
---

# 操作与数据分离的SKILL

## 方案

将skill设计为流程、脚本+运行时数据两部分，运行时数据存储到用户目录下`.SKILL名称`，运行时数据里面可以存放用户敏感数据、临时数据、非通用的特定环境、特定机器的数据。

## 目的

将具体的、不通用的数据部分和通用的、普适的操作流程、脚本进行解耦，方便skill维护和分发

## 案例

Web-simulator:一个浏览器模拟技能，实现通过API优先的方式模拟浏览器操作。大致流程是先通过CDP启动调试模式的Chrome浏览器，拿到登录凭证，加上一套登录状态检测、维护、更新方案，探测操作所用的API封装为脚本，同时每个网站的数据被存储到运行时数据目录中.

数据目录：

```
~/.web-simulator/                ← DATA_ROOT（可覆盖）
│
├── .session/sites/<domain>/<env>/
│   ├── cookies.json             ← 浏览器 cookie
│   └── meta.json                ← 元信息
│
├── .wrapper/sites/<domain>/<env>/<workflow>/
│   ├── api-discovery.json       ← API 发现结果
│   ├── <workflow>.wrapper.js    ← 可复用脚本
│   └── README.md                ← 文档
│
├── .chrome-profiles/<domain>/<env>/
│   └── ...                      ← 隔离 Chrome 配置
│
└── reports/                     ← 发现报告
```

