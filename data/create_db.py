import sqlite3

conn = sqlite3.connect("sherlock.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE transactions (
    id INTEGER PRIMARY KEY,
    date TEXT,
    failed_transactions INTEGER,
    total_transactions INTEGER
)
""")

cursor.executemany("""
INSERT INTO transactions (date, failed_transactions, total_transactions)
VALUES (?, ?, ?)
""", [
    ("2026-01-01", 50, 1000),
    ("2026-01-02", 120, 1100),
    ("2026-01-03", 300, 1200),
    ("2026-01-04", 450, 1300),
    ("2026-01-05", 900, 1500)
])

conn.commit()
conn.close()

print("Database created!")