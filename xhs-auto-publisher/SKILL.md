---
name: xhs-auto-publisher
description: Operate the local xhs_ai_publisher project to start the Web publishing service, verify Xiaohongshu login state, and run preview or controlled publish flows with the existing persistent Chrome profile under ~/.xhs_system. Use when Codex or Lobster needs to reuse the installed local publisher instead of reimplementing browser login or posting logic, especially for starting the service, checking auth, preview-filling a note without final submit, or running a real publish from the local project.
---

# Xhs Auto Publisher

## Overview

Use this skill to drive the existing local `xhs_ai_publisher` project as an automation backend for Xiaohongshu publishing.

Prefer the bundled scripts in `scripts/` over ad-hoc shell commands. They already know the default repo path, service port, login-status endpoints, and preview-publish behavior.

## Default Runtime

- Default repo path: `/Users/chenhao/Desktop/code/xhs_ai_publisher`
- Default Python: `/Users/chenhao/miniconda3/bin/python`
- Default service URL: `http://127.0.0.1:8000`
- Default persistent profile: `~/.xhs_system/chrome_user_data`
- Override repo path with `XHS_PUBLISHER_REPO`
- Override Python with `XHS_PUBLISHER_PYTHON`
- Override service URL with `XHS_PUBLISHER_BASE_URL`

## Core Workflow

1. Start or reuse the Web service with `scripts/start_service.sh`.
2. Verify login state with `scripts/check_auth.sh`.
3. Run one of the publishing flows:
   - Preview only: `scripts/preview_publish.py --title ... --content ... --image ...`
   - Real publish: `scripts/preview_publish.py --title ... --content ... --image ... --auto-publish`
4. Read the printed `content_id` and final content status.

## Important Behavior

- `--auto-publish` omitted means preview mode only.
- Preview mode fills the Xiaohongshu publish page and stops before the final submit.
- Preview mode marks the local content record as `draft`, but this does **not** guarantee the note was saved into Xiaohongshu's platform draft box.
- If the user specifically wants a Xiaohongshu platform draft, leave the page open and let the user click “保存草稿” manually if the button is present.
- If `/api/auth/status` reports `logged_in=false`, do not force a publish. Let the user log in first with the local app/browser flow.

## Scripts

### `scripts/start_service.sh`

Start the local Web service on port `8000` and wait until `/readyz` is healthy. Reuse an existing listener when already running.

### `scripts/check_auth.sh`

Fetch `/api/auth/status` and `/api/status`, then print both raw JSON payloads. Use this before any publish attempt.

### `scripts/preview_publish.py`

Send content to `/api/publish` and poll `/api/content/{id}` until it lands in `draft`, `published`, or `failed`.

Common examples:

```bash
scripts/preview_publish.py \
  --title "测试预览：请勿正式发布" \
  --content "这是一条自动化预览测试内容。" \
  --image "/Users/chenhao/Desktop/code/xhs_ai_publisher/images/ui.png"
```

```bash
scripts/preview_publish.py \
  --title "正式发布测试" \
  --content "这是一条正式发布测试内容。" \
  --image "/Users/chenhao/Desktop/code/xhs_ai_publisher/images/ui.png" \
  --auto-publish
```

## References

- Read `references/runtime.md` when the repo path, Python path, or runtime behavior differs from the defaults.
