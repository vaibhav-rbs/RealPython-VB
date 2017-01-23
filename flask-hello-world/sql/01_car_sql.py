# Create a SQLite3 database and table

# import the sqlite3 library

import sqlite3

# create a new database if the database does not already exist.

conn = sqlite3.connect('cars.db')

# get a cursor object used to execute SQL commands

cursor = conn.cursor()


# create a table

cursor.execute("""CREATE TABLE inventory 
       (Make TEXT, Model TEXT, Quantity INT)
""")

conn.close()
