import sqlite3
import pandas as pd
from src.config import DATABASE_PATH, SCHEMA_PATH

def init_db():
    conn = sqlite3.connect(DATABASE_PATH)
    if SCHEMA_PATH.exists():
        with open(SCHEMA_PATH, "r") as f:
            conn.executescript(f.read())
    conn.close()

def save_to_db(df: pd.DataFrame, table_name: str = "posts"):
    init_db()
    conn = sqlite3.connect(DATABASE_PATH)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()