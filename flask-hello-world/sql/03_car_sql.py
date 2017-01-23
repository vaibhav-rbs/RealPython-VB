# Create a SQLite3 database and table

# import the sqlite3 library

import sqlite3

# create a new database if the database does not already exist.

with sqlite3.connect('cars.db') as connection:
    c = connection.cursor()

    car_inventory_count = [
        ('Honda', 'Civic', 5),
        ('Honda', 'Accord', 3),
        ('Toyota', 'Camry', 2),
        ('Toyota', 'Corrola', 5),
        ('Kia', 'Sorrento', 1)
        ]



    c.executemany('INSERT INTO inventory VALUES (?,?,?)', car_inventory_count)
