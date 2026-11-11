"""Small database helper used by the dashboard.

In production the app talks to a database server over the network. Locally we
use SQLite (a database stored in a single file), and add a short delay to each
query so local timing behaves like production.
"""

import sqlite3
import time
from types import SimpleNamespace

# Round-trip time to the production database server, in seconds.
NETWORK_DELAY = 0.005


def _row_to_object(cursor, row):
    columns = [description[0] for description in cursor.description]
    return SimpleNamespace(**dict(zip(columns, row)))


class Database:
    def __init__(self, path, network_delay=NETWORK_DELAY):
        self.conn = sqlite3.connect(path)
        self.conn.row_factory = _row_to_object
        self.network_delay = network_delay
        self.query_count = 0

    def query(self, sql, *params):
        """Run a SQL query and return a list of rows.

        Each row's columns are attributes, so you can write row.name.
        Use ? placeholders for values: db.query("... WHERE id = ?", 42)
        """
        self.query_count += 1
        time.sleep(self.network_delay)
        return self.conn.execute(sql, params).fetchall()

    def execute_script(self, sql):
        self.conn.executescript(sql)
        self.conn.commit()
