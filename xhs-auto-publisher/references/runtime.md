# Runtime Notes

## Expected Local Project

This skill assumes the real publisher project lives at:

- `/Users/chenhao/Desktop/code/xhs_ai_publisher`

If it moves, set:

- `XHS_PUBLISHER_REPO=/new/path/to/xhs_ai_publisher`

## Expected Python

Preferred Python for this machine:

- `/Users/chenhao/miniconda3/bin/python`

Reason:

- It already has `PyQt5`, `playwright`, and `fastapi` installed.
- The repo's `venv/bin/python` may be a broken symlink.

If another Python should be used, set:

- `XHS_PUBLISHER_PYTHON=/path/to/python`

## Service Behavior

The service entrypoint is:

- `src/web/app.py`

The scripts start it with:

- `PYTHONPATH=.`
- `XHS_WEB_DEBUG=0`
- `XHS_WEB_RELOAD=0`
- `XHS_WEB_EAGER_BROWSER=1`

## Useful Endpoints

- `/readyz`
- `/api/auth/status`
- `/api/status`
- `/api/publish`
- `/api/content/{content_id}`

## Preview Publish Semantics

`auto_publish=false` means:

- open Xiaohongshu creator flow
- upload image
- fill title and body
- stop before final submit

This is safe for demonstrations and smoke tests, but it is not a guaranteed platform draft save.
