#!/usr/bin/env bash
set -euo pipefail

BASE_URL="${XHS_PUBLISHER_BASE_URL:-http://127.0.0.1:8000}"

echo "--- /api/auth/status ---"
curl -fsS "${BASE_URL}/api/auth/status"
echo

echo "--- /api/status ---"
curl -fsS "${BASE_URL}/api/status"
echo
