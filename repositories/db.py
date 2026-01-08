# repositories/db.py
from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Any

DB_PATH = Path("data") / "gymtracker_v2.db"


def get_conn() -> sqlite3.Connection:
    """
    Abre conexão com SQLite.
    row_factory = sqlite3.Row faz cada linha se comportar como dict (row["coluna"]).
    """
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def fetch_all(query: str, params: tuple[Any, ...] = ()) -> list[dict[str, Any]]:
    """
    Executa um SELECT e retorna lista de dicts (cada dict = uma linha).
    """
    with get_conn() as conn:
        cur = conn.execute(query, params)
        rows = cur.fetchall()
    return [dict(r) for r in rows]
