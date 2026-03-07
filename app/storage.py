import sqlite3
from pathlib import Path

DB_PATH = Path("data/prescripts.db")

def init_db():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS prescripts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL,
            mode TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            status TEXT DEFAULT 'new'
        )
    """)
    conn.commit()
    conn.close()

def save_prescript(content: str, mode: str):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO prescripts (content, mode) VALUES (?, ?)",
        (content, mode)
    )
    conn.commit()
    conn.close()

def get_recent_prescripts(limit: int = 10) -> list[str]:
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        """
        SELECT content FROM prescripts
        WHERE content != '静候下一则指令'
        ORDER BY id DESC LIMIT ?
        """,
        (limit,)
    )
    rows = cur.fetchall()
    conn.close()
    return [row[0] for row in rows][::-1]