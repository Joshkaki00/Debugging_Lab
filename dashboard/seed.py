"""Create dashboard.db and fill it with sample data.

Run with: python seed.py
"""

import random
from pathlib import Path

from db import Database

HERE = Path(__file__).parent
DB_PATH = HERE / "dashboard.db"

USERS = [
    # (id, name, number of projects)
    (1, "Ada", 4),
    (2, "Grace", 2500),
]


def seed(db, users=USERS, tasks_per_project=(0, 30), rng=None):
    rng = rng or random.Random(42)
    db.execute_script((HERE / "schema.sql").read_text())

    projects, tasks = [], []
    project_id = task_id = 0
    for user_id, user_name, project_count in users:
        db.conn.execute("INSERT INTO users (id, name) VALUES (?, ?)", (user_id, user_name))
        for n in range(1, project_count + 1):
            project_id += 1
            projects.append((project_id, user_id, f"{user_name}'s Project {n}"))
            for t in range(rng.randint(*tasks_per_project)):
                task_id += 1
                tasks.append((task_id, project_id, f"Task {t + 1}", int(rng.random() < 0.6)))

    db.conn.executemany("INSERT INTO projects (id, owner_id, name) VALUES (?, ?, ?)", projects)
    db.conn.executemany("INSERT INTO tasks (id, project_id, title, done) VALUES (?, ?, ?, ?)", tasks)
    db.conn.commit()
    return len(projects), len(tasks)


if __name__ == "__main__":
    db = Database(DB_PATH, network_delay=0)
    project_count, task_count = seed(db)
    print(f"Created {DB_PATH.name}: {len(USERS)} users, {project_count} projects, {task_count} tasks")
    for user_id, name, count in USERS:
        print(f"  user {user_id}: {name} ({count} projects)")
