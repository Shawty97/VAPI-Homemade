#!/usr/bin/env python
import os

ESSENTIAL_FILES = [
    "app.py",
    "routers/health.py",
    "routers/websocket_router.py",
    "services/websocket_service.py",
    "services/audio_service.py",
    "services/llm_service.py",
    "services/ultra_low_latency_service.py",
    "services/webhook_service.py",
    ".env.example",
    "config/agent_personalities.yaml",
    "prompts/prompts.yaml",
    "requirements.txt",
    "docker-compose.yml",
    "Dockerfile",
    "scripts/build_production.ps1",
    "scripts/deploy.sh",
    "tests/test_api.py",
    "tests/test_voice.py",
    "tests/test_performance.py",
    "pytest.ini",
]

missing = [f for f in ESSENTIAL_FILES if not os.path.exists(f)]

if missing:
    print("Missing files:", ", ".join(missing))
    exit(1)
print("All essential files present")
