#!/usr/bin/env bash
set -euo pipefail

BASE_URL="${XHS_PUBLISHER_BASE_URL:-http://127.0.0.1:8000}"
REPO_DIR="${XHS_PUBLISHER_REPO:-/Users/chenhao/Desktop/code/xhs_ai_publisher}"
PYTHON_CMD="${XHS_PUBLISHER_PYTHON:-/Users/chenhao/miniconda3/bin/python}"
LOG_DIR="${HOME}/.xhs_system/logs"
LOG_FILE="${LOG_DIR}/xhs_web_skill.log"

mkdir -p "$LOG_DIR"

if curl -fsS --max-time 3 "${BASE_URL}/readyz" >/dev/null 2>&1; then
  echo "[OK] Service already ready at ${BASE_URL}"
  exit 0
fi

cd "$REPO_DIR"
nohup bash -lc "cd '$REPO_DIR' && export PYTHONPATH=. XHS_WEB_DEBUG=0 XHS_WEB_RELOAD=0 XHS_WEB_EAGER_BROWSER=1; '$PYTHON_CMD' src/web/app.py" >"$LOG_FILE" 2>&1 &

for _ in $(seq 1 45); do
  if curl -fsS --max-time 3 "${BASE_URL}/readyz" >/dev/null 2>&1; then
    echo "[OK] Service ready at ${BASE_URL}"
    echo "[INFO] Log: ${LOG_FILE}"
    exit 0
  fi
  sleep 1
done

echo "[ERROR] Service did not become ready"
echo "[INFO] Check log: ${LOG_FILE}"
exit 1
