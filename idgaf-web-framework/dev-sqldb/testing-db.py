import sqlite3

con = sqlite3.connect('tests.db')
cursor = con.cursor()
cursor.execute("CREATE TABLE tests(testname, testfile)")
con.commit()

res = cursor.execute("SELECT testname FROM sqlite_master")
res.fetchone()

cur.execute("""
    INSERT INTO tests VALUES
        (Test Name Test),
        (Test Name Location)
""")

con.commit()

res = curspr.execute("SELECT testname, testfile FROM tests")
data = res.fetchall()
print(data)


"""
data = [
    ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
    ("Monty Python's The Meaning of Life", 1983, 7.5),
    ("Monty Python's Life of Brian", 1979, 8.0),
]
cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
con.commit()  # Remember to commit the transaction after executing INSERT.

"""
