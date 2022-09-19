import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO visits (ip_address) VALUES (?)", ("79.88.106.115",))

connection.commit()
connection.close()