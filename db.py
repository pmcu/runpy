import sqlite3

conn = sqlite3.connect("testdb.db")

cur = cur conn.cursor()
cur.execute('''
CREATE TABLE IF NOT EXIST people
(first_name TEXT, last_name Text)''')
conn.commit()
cur.close()
conn.close()
