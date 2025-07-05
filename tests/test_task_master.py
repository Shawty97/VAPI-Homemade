import os
import subprocess
import json

TASK_FILE_ENV = {"TASK_FILE": "tasks_test.json"}


def cleanup() -> None:
    if os.path.exists("tasks_test.json"):
        os.remove("tasks_test.json")


def test_task_master_parse_next(tmp_path) -> None:
    env = os.environ.copy()
    env.update(TASK_FILE_ENV)
    cleanup()
    subprocess.run(["python", "scripts/task_master.py", "initialize-project"], check=True, env=env)
    subprocess.run(["python", "scripts/task_master.py", "parse-prd", "VAPI_HOMEMADE_PRD.md", "--limit", "1"], check=True, env=env)
    out = subprocess.check_output(["python", "scripts/task_master.py", "next-task"], env=env)
    assert b"[1]" in out
    cleanup()
