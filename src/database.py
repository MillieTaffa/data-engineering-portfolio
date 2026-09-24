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
    with open(config.SCHEMA_SQL_PATH, "r") as schema_file:
        schema_sql = schema_file.read()
    connection.executescript(schema_sql)
    connection.commit()

def save_to_database(data):
    """
    Saves the processed DataFrame into the SQLite "posts" table.
    """
    data = data.copy()
    data["Timestamp"] = data["Timestamp"].astype(str)
    data["Has_Media"] = data["Has_Media"].astype(int)
    data["Is_Verified"] = data["Is_Verified"].astype(int)

    with get_connection() as connection:
        create_table(connection)
        connection.execute("DELETE FROM posts")
        data.to_sql("posts", connection, if_exists="append", index=False)
        row_count = connection.execute(
            "SELECT COUNT(*) FROM posts"
        ).fetchone()[0]

    print(f"Saved {row_count} rows to 'posts' in {config.DATABASE_PATH}")


def run_query(query):
    """Runs a SQL query against the database and returns a DataFrame."""
    with get_connection() as connection:
        return pd.read_sql_query(query, connection)

if __name__ == "__main__":
    print(run_query("SELECT COUNT(*) AS total_rows FROM posts"))
