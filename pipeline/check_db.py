import sqlite3

conn = sqlite3.connect("store_intelligence.db")

cursor = conn.cursor()

cursor.execute("""
SELECT COUNT(*) FROM events;
""")

for row in cursor.fetchall():
    print(row)

conn.close()