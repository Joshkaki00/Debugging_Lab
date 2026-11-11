"""Project dashboard: one row per project with its number of open tasks.

Run with: python dashboard.py <user_id>
"""

import sys
import time
from pathlib import Path

from db import Database

DB_PATH = Path(__file__).parent / "dashboard.db"


def dashboard(db, user):
    projects = db.query("SELECT * FROM projects WHERE owner_id = ?", user.id)
    result = []
    for p in projects:
        tasks = db.query("SELECT * FROM tasks WHERE project_id = ?", p.id)
        result.append({"project": p.name, "open_tasks": len([t for t in tasks if not t.done])})
    return result


def main():
    if not DB_PATH.exists():
        sys.exit("dashboard.db not found. Run `python seed.py` first.")
    if len(sys.argv) != 2:
        sys.exit("Usage: python dashboard.py <user_id>")

    db = Database(DB_PATH)
    users = db.query("SELECT * FROM users WHERE id = ?", int(sys.argv[1]))
    if not users:
        sys.exit(f"No user with id {sys.argv[1]}")
    user = users[0]

    print(f"Loading dashboard for {user.name}...")
    start = time.perf_counter()
    rows = dashboard(db, user)
    elapsed = time.perf_counter() - start

    for row in rows[:5]:
        print(f"  {row['project']:<30} {row['open_tasks']:>3} open tasks")
    if len(rows) > 5:
        print(f"  ... and {len(rows) - 5} more projects")
    print(f"Loaded {len(rows)} projects in {elapsed:.2f} seconds")


if __name__ == "__main__":
    main()
