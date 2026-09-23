"""
database.py

Responsibility: everything to do with the SQLite database.

This file knows how to:
- connect to the SQLite database file
- create the "posts" table from sql/schema.sql
- save processed data into it
- run a query against it and return the result as a DataFrame

Keeping this logic in one place means the rest of the project
(pipeline.py, analytics.py) never has to write raw sqlite3 connection
code themselves.
"""

import sqlite3
import pandas as pd
from src import config

def get_connection():
    "This opens and returns a connection to the SQLite database file."
    config.DATABASE_DIR.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(config.DATABASE_PATH)
    return connection

def create_table(connection):
    """This creates the posts table using the schema defined in sql/schema.sql."""
    with open(config.SCHEM_SQL_PATH, "r") as schema_file:
        schema_sql = schema_file.read()
    connection.executescript(schema_sql)
    connection.commit()

def save_to_database(data):
        """
    Saves the processed DataFrame into the SQLite "posts" table.

    The table's existing rows are cleared first (DELETE, not DROP), so the
    table keeps using the schema and PRIMARY KEY defined in sql/schema.sql
    instead of pandas guessing a schema on its own. This also means the
    pipeline can be run again and again without creating duplicate rows.
    """

    data = data.copy()

    # SQLite doesn't have a native datetime type, so Timestamp is stored as a plain ISO-format text string
    data["Timestamp"] = data["Timestamp"].astype(str)

    # Booleans are stored as 0/1, which is how SQLite represents them.
    data["Has_Media"] = data["Has_Media"].astype(int)
    data["Is_Verified"] = data["Is_Verified"].astype(int)

    connection = get_connection()
    create_table(connection)
    connection.execute("DELETE FROM posts")
    connection.commit()

    data.to_sql("posts", connection, if_exists="append", index=False)

    row_count = connection.execute("SELECT COUNT(*) FROM posts").fecthone()[0]
    print(f"Saved {row_count} rows to the 'posts' in {config.DATABASE_PATH}")

    connection.close()

def run_query(query):
        """Runs a SQL query against the database and returns the result as a DataFrame."""
        connection = get_connection()
        result = pd.read_sql_query(query, connection)
        connection.close()
        return result

if __name__ == "__main__":
    print(run_query("SELECT(*) AS total_rows FROM posts"))