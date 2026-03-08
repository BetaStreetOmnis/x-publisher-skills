# x-publisher-skills

一个面向 Codex / CLI Agent 的开源技能仓库，聚焦“内容发布自动化”相关场景。

[🇨🇳 简体中文](./README.md) | [🇺🇸 English](./readme_en.md)

## 项目简介

`x-publisher-skills` 用来沉淀可复用的发布类技能（skills），让不同 Agent 可以直接复用现有项目、运行时环境和发布流程，而不是每次都从零实现一遍登录、服务启动、接口检查和浏览器自动化。

当前仓库优先收录两类能力：

- 已有本地发布系统的技能化封装
- 面向内容平台的预览发布、登录检查与受控发布流程

## 已收录技能

### `xhs-auto-publisher`

将本地 `xhs_ai_publisher` 项目作为小红书 / Rednote 自动发布后端来使用。

能力包括：

- 启动或复用本地 Web 发布服务
- 检查小红书登录状态
- 运行“只预览、不最终发布”的自动填写流程
- 在明确要求时执行受控正式发布
- 复用本地持久化 Chrome 登录态与运行数据

技能目录：

- `xhs-auto-publisher/`

## 仓库结构

```text
x-publisher-skills/
├── README.md
├── readme_en.md
└── xhs-auto-publisher/
    ├── SKILL.md
    ├── agents/openai.yaml
    ├── references/
    └── scripts/
```

## 使用方式

### 1. 浏览技能说明

先阅读对应技能目录下的：

- `SKILL.md`

### 2. 按需执行脚本

例如 `xhs-auto-publisher` 提供了：

- `scripts/start_service.sh`
- `scripts/check_auth.sh`
- `scripts/preview_publish.py`

### 3. 接入你的技能目录

你可以将整个技能目录复制或软链接到自己的 Codex skills 目录中使用。

## 适用说明

- 本仓库中的部分技能会依赖本地已有项目路径
- 部分脚本会依赖本机 Python、浏览器 profile、数据目录等运行环境
- 如果换机器使用，请优先阅读技能内的 `references/` 文档并调整路径配置

## 目标

这个仓库的目标不是做“通用 SDK”，而是沉淀一组真正能在实际发布工作流里复用的 Agent 技能资产。

后续会继续加入更多和发布、登录态复用、预览发布、平台自动化相关的技能。
