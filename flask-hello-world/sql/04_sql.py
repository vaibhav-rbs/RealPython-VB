# Create a SQLite3 database and table

# import the sqlite3 library

import sqlite3
import csv

# create a new database if the database does not already exist.

employees =  csv.reader(open("employees.csv", "rU"))

with sqlite3.connect('new.db') as connection:
    c = connection.cursor()


    # create a table

    c.execute('CREATE TABLE employees (firstname TEXT, lastname TEXT)')

    c.executemany("INSERT INTO employees(firstname, lastname) values (?,?)", employees)

    # commit the changes.
