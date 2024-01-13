import sqlite3

con = sqlite3.connect('massive.db')
cursor = con.cursor()

for i in range(10):
    table = f"CREATE TABLE user_{i}(id TEXT DEFAULT 'empty user {i}', name, testfile)"
    cursor.execute(table)
    con.commit()

# CREATE TABLE customers ( id INTEGER PRIMARY KEY, store_code TEXT DEFAULT "store1" NOT NULL, name TEXT )
