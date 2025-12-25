import sqlite3

# connect to database
conn = sqlite3.connect("brain_game.db")
cursor = conn.cursor()

# print all
cursor.execute("SELECT * FROM scores")
rows = cursor.fetchall()

print("--- Player Data ---")
for row in rows:
    print(row)

conn.close()