#!/usr/bin/env python3
import argparse
import json
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path


def http_json(url: str, payload=None, timeout: int = 20):
    headers = {"Content-Type": "application/json"}
    data = None if payload is None else json.dumps(payload, ensure_ascii=False).encode("utf-8")
    request = urllib.request.Request(url, data=data, headers=headers)
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser(description="Run Xiaohongshu preview or controlled publish through the local service.")
    parser.add_argument("--title", required=True)
    parser.add_argument("--content", required=True)
    parser.add_argument("--image", action="append", dest="images", required=True)
    parser.add_argument("--auto-publish", action="store_true")
    parser.add_argument("--base-url", default="http://127.0.0.1:8000")
    parser.add_argument("--poll-seconds", type=float, default=2.0)
    parser.add_argument("--timeout-seconds", type=int, default=180)
    args = parser.parse_args()

    image_paths = [str(Path(path).expanduser().resolve()) for path in args.images]
    missing = [path for path in image_paths if not Path(path).exists()]
    if missing:
        print(json.dumps({"error": "missing_images", "paths": missing}, ensure_ascii=False), file=sys.stderr)
        return 2

    payload = {
        "title": args.title,
        "content": args.content,
        "image_files": image_paths,
        "auto_publish": bool(args.auto_publish),
    }

    try:
        publish_response = http_json(f"{args.base_url}/api/publish", payload=payload, timeout=30)
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        print(json.dumps({"error": "publish_http_error", "status": exc.code, "body": body}, ensure_ascii=False), file=sys.stderr)
        return 3
    except Exception as exc:
        print(json.dumps({"error": "publish_request_failed", "detail": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 4

    print(json.dumps({"publish_response": publish_response}, ensure_ascii=False))
    content_id = str(publish_response.get("content_id") or "").strip()
    if not content_id:
        print(json.dumps({"error": "missing_content_id"}, ensure_ascii=False), file=sys.stderr)
        return 5

    deadline = time.time() + max(5, int(args.timeout_seconds))
    while time.time() < deadline:
        time.sleep(max(0.2, float(args.poll_seconds)))
        try:
            content_response = http_json(f"{args.base_url}/api/content/{content_id}", timeout=15)
        except Exception as exc:
            print(json.dumps({"warning": "poll_failed", "detail": str(exc)}, ensure_ascii=False), file=sys.stderr)
            continue

        content = content_response.get("data") or {}
        status = str(content.get("status") or "")
        print(json.dumps({"content_id": content_id, "status": status, "error_message": content.get("error_message")}, ensure_ascii=False))
        if status in {"draft", "published", "failed"}:
            print(json.dumps({"final": content}, ensure_ascii=False))
            return 0 if status != "failed" else 6

    print(json.dumps({"error": "timeout", "content_id": content_id}, ensure_ascii=False), file=sys.stderr)
    return 7


if __name__ == "__main__":
    raise SystemExit(main())
