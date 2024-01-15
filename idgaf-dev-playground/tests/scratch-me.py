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
    rows = cursor.execute(f"SELECT * FROM {table}")
    print(rows)

con.close()

import sqlite3

con = sqlite3.connect('massive.db')
cursor = con.cursor()

for i in range(10):
    table = f"CREATE TABLE user_{i}(id INTEGER PRIMARY KEY, name, testfile)"
    cursor.execute(table)
    con.commit()

# CREATE TABLE customers ( id INTEGER PRIMARY KEY, store_code TEXT DEFAULT "store1" NOT NULL, name TEXT )

import sqlite3

con = sqlite3.connect('tests.db')
cursor = con.cursor()
cursor.execute("CREATE TABLE tests(testname, testfile)")
con.commit()

res = cursor.execute("SELECT testname FROM sqlite_master")
res.fetchone()

cursor.execute("""
    INSERT INTO tests VALUES
        (Test Name Test),
        (Test Name Location)
""")

con.commit()

res = cursor.execute("SELECT testname, testfile FROM tests")
data = res.fetchall()
print(data)
