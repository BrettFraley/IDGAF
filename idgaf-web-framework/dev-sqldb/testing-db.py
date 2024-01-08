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

