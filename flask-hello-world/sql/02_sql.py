# Create a SQLite3 database and table

# import the sqlite3 library

import sqlite3

# create a new database if the database does not already exist.

conn = sqlite3.connect('new.db')

# get a cursor object used to execute SQL commands

cursor = conn.cursor()


# create a table

cursor.execute("""INSERT INTO population VALUES 
       ('New York City', 'NY', 84000000)
""")

cursor.execute("""INSERT INTO population VALUES 
       ('San Francisco', 'CA', 800000)
""")

# commit the changes.
conn.commit()

conn.close()
