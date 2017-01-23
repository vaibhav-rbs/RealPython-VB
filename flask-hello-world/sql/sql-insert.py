# Create a SQLite3 database and table

# import the sqlite3 library

import sqlite3

# import random library

from random import randint

# create a new database if the database does not already exist.

with sqlite3.connect('newnum.db') as connection:

     # get a cursor object used to execute SQL commands

     cursor = connection.cursor()

     # create a table
     cursor.execute("DROP TABLE if exists numbers")
     cursor.execute("CREATE TABLE numbers (num int)")

     for i in range(1,100):
         cursor.execute("INSERT INTO numbers VALUES (?)", (randint(0,100),))

