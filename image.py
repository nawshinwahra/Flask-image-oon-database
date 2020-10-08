import sqlite3
conn = sqlite3.connect('image.db')
cursor = conn.cursor()

command = """CREATE TABLE new_employee ( id INTEGER PRIMARY KEY, name TEXT NOT NULL, photo BLOB NOT NULL);"""


cursor.execute(command)
conn.commit()
cursor.close()
conn.close()