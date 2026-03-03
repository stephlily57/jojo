
import sqlite3
from pathlib import Path
from time import time

DB_DIR = Path("data")
DB_DIR.mkdir(exist_ok=True)

DB_PATH = DB_DIR / "history.db"

def _init():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(
        """CREATE TABLE IF NOT EXISTS history (
            ts REAL,
            source TEXT,
            payload TEXT
        )"""
    )
    conn.commit()
    conn.close()

_init()

def append_event(source: str, payload: str):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO history VALUES (?, ?, ?)", (time(), source, payload))
    conn.commit()
    conn.close()
