#!/bin/bash
# Quick verification script

echo "=== Environment Check ==="
echo "CODESPACE_NAME: ${CODESPACE_NAME}"
echo ""

echo "=== Django Configuration ==="
cd /workspaces/flai-workshop-github-copilot-800/octofit-tracker/backend
source venv/bin/activate
python3 << EOF
import os
os.environ.setdefault('CODESPACE_NAME', os.getenv('CODESPACE_NAME', 'not-set'))
from octofit_tracker import settings
print(f"ALLOWED_HOSTS: {settings.ALLOWED_HOSTS}")
print(f"DEBUG: {settings.DEBUG}")
if hasattr(settings, 'USE_X_FORWARDED_HOST'):
    print(f"USE_X_FORWARDED_HOST: {settings.USE_X_FORWARDED_HOST}")
if hasattr(settings, 'SECURE_PROXY_SSL_HEADER'):
    print(f"SECURE_PROXY_SSL_HEADER: {settings.SECURE_PROXY_SSL_HEADER}")
EOF

echo ""
echo "=== MongoDB Status ==="
ps aux | grep mongod | grep -v grep || echo "MongoDB not running"

echo ""
echo "=== Port Status ==="
echo "Port 8000: $(lsof -i :8000 >/dev/null 2>&1 && echo 'In use' || echo 'Available')"
echo "Port 27017: $(lsof -i :27017 >/dev/null 2>&1 && echo 'In use (MongoDB)' || echo 'Available')"
