# Create a SQLite3 database and table

# import the sqlite3 library

import sqlite3

# create a new database if the database does not already exist.

with sqlite3.connect('new.db') as connection:
    c = connection.cursor()

cities = [
    ('Boston', 'MA', 600000),
    ('Chicago', 'IL', 600000),
    ('Houston', 'TX', 600000),
    ('Phoenix', 'AZ', 600000)
]


# create a table

cursor.execute('INSERT INTO population VALUES (?,?,?)', cities)

# commit the changes.
conn.commit()

conn.close()
