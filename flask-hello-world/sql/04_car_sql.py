# Create a SQLite3 database and table

# import the sqlite3 library

import sqlite3

# create a new database if the database does not already exist.

with sqlite3.connect('cars.db') as connection:
    c = connection.cursor()
    c.execute("UPDATE inventory SET quantity = 16 WHERE model='Civic'")
    c.execute("UPDATE inventory SET quantity = 15 WHERE make='Toyota'")
