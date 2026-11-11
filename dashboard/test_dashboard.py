from pathlib import Path
from types import SimpleNamespace

import pytest

from dashboard import dashboard
from db import Database


@pytest.fixture
def db():
    """A small in-memory database with hand-picked data."""
    database = Database(":memory:", network_delay=0)
    database.execute_script((Path(__file__).parent / "schema.sql").read_text())
    database.execute_script(
        """
        INSERT INTO users (id, name) VALUES (1, 'Ada'), (2, 'Grace');

        INSERT INTO projects (id, owner_id, name) VALUES
          (1, 1, 'Website redesign'),
          (2, 1, 'Empty project'),
          (3, 1, 'Finished project'),
          (4, 2, 'Someone else''s project');

        INSERT INTO tasks (project_id, title, done) VALUES
          (1, 'Pick fonts', 0),
          (1, 'Draft homepage', 0),
          (1, 'Buy domain', 1),
          (3, 'Ship it', 1),
          (4, 'Not Ada''s task', 0);
        """
    )
    return database


def test_counts_open_tasks_per_project(db):
    rows = dashboard(db, SimpleNamespace(id=1))
    assert {"project": "Website redesign", "open_tasks": 2} in rows


def test_includes_projects_with_no_tasks(db):
    rows = dashboard(db, SimpleNamespace(id=1))
    assert {"project": "Empty project", "open_tasks": 0} in rows


def test_includes_projects_where_every_task_is_done(db):
    rows = dashboard(db, SimpleNamespace(id=1))
    assert {"project": "Finished project", "open_tasks": 0} in rows


def test_only_shows_the_users_own_projects(db):
    rows = dashboard(db, SimpleNamespace(id=1))
    assert len(rows) == 3
    assert all(row["project"] != "Someone else's project" for row in rows)
