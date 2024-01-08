import sqlite3

con = sqlite3.connect('massive.db')
cursor = con.cursor()

tablesQuery = "SELECT name FROM sqlite_schema WHERE type='table'"
results = cursor.execute(tablesQuery)
tableNames = []

for row in results:
    tableNames.append(row[0])


for table in tableNames:
    insert = f"INSERT INTO {table} VALUES(id='user_{table}', name='empty user', testfile='empty test file')"
    query = cursor.execute(insert)
    con.commit()


for table in tableNames:
    rows = curser.execute(f"SELECT * FROM {table}")
    print(rows)

con.close()

