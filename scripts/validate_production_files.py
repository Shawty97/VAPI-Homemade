#!/usr/bin/env python3
"""Validate that only essential production files exist in repository.

Checks the presence of required files/directories defined by project rules.
"""
from __future__ import annotations
import sys
from pathlib import Path

ESSENTIAL_FILES = [
    "app.py",
    "routers",
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
    "test_api.py",
    "test_voice.py",
    "test_performance.py",
    "pytest.ini",
]


def main() -> int:
    missing = [f for f in ESSENTIAL_FILES if not Path(f).exists()]
    if missing:
        for f in missing:
            print(f"Missing: {f}")
        return 1
    print("All essential files are present.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
