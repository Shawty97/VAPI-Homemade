import argparse
import json
import os
import re
from typing import List, Dict

TASK_FILE = os.getenv("TASK_FILE", "tasks.json")


def load_tasks() -> List[Dict[str, str]]:
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_tasks(tasks: List[Dict[str, str]]) -> None:
    with open(TASK_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)


def initialize_project(args: argparse.Namespace) -> None:
    if os.path.exists(TASK_FILE):
        print("Task file already exists")
    else:
        save_tasks([])
        print("Project initialized")


def parse_prd(args: argparse.Namespace) -> None:
    tasks = load_tasks()
    last_id = max([t.get("id", 0) for t in tasks], default=0)
    with open(args.prd, "r", encoding="utf-8") as f:
        lines = f.readlines()
    added = 0
    for line in lines:
        match = re.match(r"\s*[-*]\s+(.*)", line)
        if match:
            last_id += 1
            tasks.append({"id": last_id, "desc": match.group(1).strip(), "status": "pending"})
            added += 1
            if added >= args.limit:
                break
    save_tasks(tasks)
    print(f"Added {added} tasks")


def next_task(args: argparse.Namespace) -> None:
    tasks = load_tasks()
    for task in tasks:
        if task.get("status") == "pending":
            print(f"[{task['id']}] {task['desc']}")
            return
    print("No pending tasks")


def list_tasks(args: argparse.Namespace) -> None:
    tasks = load_tasks()
    for task in tasks:
        if args.status and task.get("status") != args.status:
            continue
        print(f"[{task['id']}] {task['status']} - {task['desc']}")


def update_task(args: argparse.Namespace) -> None:
    tasks = load_tasks()
    for task in tasks:
        if task.get("id") == args.id:
            task["status"] = args.status
            break
    save_tasks(tasks)
    print("Task updated")


def main() -> None:
    parser = argparse.ArgumentParser(description="Taskmaster CLI")
    sub = parser.add_subparsers(dest="cmd")

    init_p = sub.add_parser("initialize-project")
    init_p.set_defaults(func=initialize_project)

    parse_p = sub.add_parser("parse-prd")
    parse_p.add_argument("prd", help="PRD markdown file")
    parse_p.add_argument("--limit", type=int, default=10, help="Max tasks to parse")
    parse_p.set_defaults(func=parse_prd)

    next_p = sub.add_parser("next-task")
    next_p.set_defaults(func=next_task)

    list_p = sub.add_parser("list")
    list_p.add_argument("--status", help="Filter by status")
    list_p.set_defaults(func=list_tasks)

    upd_p = sub.add_parser("update-task")
    upd_p.add_argument("id", type=int)
    upd_p.add_argument("--status", default="done")
    upd_p.set_defaults(func=update_task)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

