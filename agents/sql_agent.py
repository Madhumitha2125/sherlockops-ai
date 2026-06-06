import sqlite3
import pandas as pd

DB_PATH = "data/sherlock.db"


def run_sql_query(query):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(query)
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description] if cursor.description else []

    conn.close()

    return {
        "columns": columns,
        "rows": rows
    }


def get_transaction_failures():
    query = """
    SELECT date, failed_transactions, total_transactions
    FROM transactions
    ORDER BY date DESC
    LIMIT 7;
    """
    return run_sql_query(query)