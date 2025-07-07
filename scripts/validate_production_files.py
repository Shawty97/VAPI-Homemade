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
    "services/sip_service.py",
    "services/webhook_service.py",
    "services/security.py",
    "services/pipeline_service.py",
    "routers/call_router.py",
    "routers/pipeline_router.py",
    "routers/webhook_router.py",
    "routers/rtc_router.py",
    ".env.example",
    "config/agent_personalities.yaml",
    "prompts/prompts.yaml",
    "requirements.txt",
    "docker-compose.yml",
    "Dockerfile",
    "scripts/build_production.ps1",
    "scripts/deploy.sh",
    "scripts/task_master.py",
    "tests/test_api.py",
    "tests/test_pipeline_api.py",
    "tests/test_task_master.py",
    "tests/test_webhook.py",
    "tests/test_rtc.py",
    "tests/test_voice.py",
    "tests/test_performance.py",
    "pytest.ini",
]

missing = [f for f in ESSENTIAL_FILES if not os.path.exists(f)]

if missing:
    print("Missing files:", ", ".join(missing))
    exit(1)
print("All essential files present")
