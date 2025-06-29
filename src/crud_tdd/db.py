
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "crud_tdd.db"
SCHEMA_PATH = Path(__file__).parent / "schema.sql"

def init_db():
    if DB_PATH.exists():
        DB_PATH.unlink()
    conn = sqlite3.connect(DB_PATH)
    with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()
