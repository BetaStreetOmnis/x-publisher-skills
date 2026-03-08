# x-publisher-skills

An open-source skill repository for Codex / CLI agents, focused on publishing automation workflows.

[🇨🇳 简体中文](./README.md) | [🇺🇸 English](./readme_en.md)

## Overview

`x-publisher-skills` collects reusable publishing-oriented skills so different agents can reuse existing local projects, runtime environments, and posting workflows instead of reimplementing login, service startup, endpoint checks, and browser automation from scratch.

This repository currently focuses on two kinds of assets:

- skill wrappers around existing local publisher projects
- preview-publish, auth-check, and controlled publish flows for content platforms

## Included Skills

### `xhs-auto-publisher`

Use the local `xhs_ai_publisher` project as an automation backend for Xiaohongshu / Rednote publishing.

Capabilities:

- start or reuse the local Web publishing service
- verify Xiaohongshu login status
- run a preview-only publish flow without final submission
- run a controlled real publish when explicitly requested
- reuse the local persistent Chrome login state and runtime data

Skill location:

- `xhs-auto-publisher/`

## Repository Structure

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

## How to Use

### 1. Read the skill guide

Start with the skill's:

- `SKILL.md`

### 2. Run the bundled scripts when needed

For example, `xhs-auto-publisher` includes:

- `scripts/start_service.sh`
- `scripts/check_auth.sh`
- `scripts/preview_publish.py`

### 3. Add the skill to your own skills directory

You can copy or symlink the skill folder into your own Codex skills directory.

## Notes

- Some skills in this repository depend on local project paths
- Some scripts depend on machine-specific Python setups, browser profiles, and runtime data directories
- When using these skills on another machine, read the `references/` docs first and adjust the paths as needed

## Goal

This repository is not meant to be a generic SDK. It is meant to accumulate skill assets that are genuinely reusable in real publishing workflows.

More skills related to publishing, login-state reuse, preview publishing, and platform automation can be added over time.
