import sqlite3

print("Creating DB")
conn = sqlite3.connect("fb.db")
print("DB created")

conn.execute(
    "CREATE TABLE IF NOT EXISTS facebook ( id INTEGER PRIMARY KEY AUTOINCREMENT, username char(100) NOT NULL UNIQUE, email char(100) NOT NULL UNIQUE, password char(100) NOT NULL, cookie char(128) UNIQUE)"
)
conn.execute(
    "INSERT INTO facebook (username, email, password) VALUES ('Charles', 'charlescedelle@orange.fr', 'test')"
)
conn.commit()
print("Table create")
