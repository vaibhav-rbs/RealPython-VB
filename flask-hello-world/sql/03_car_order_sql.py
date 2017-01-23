import sqlite3

with sqlite3.connect('cars.db') as connection:
    c = connection.cursor()

    car_order_date = [
        ('Honda', 'Civic', 2017-01-01),
        ('Honda', 'Accord', 2017-01-02),
        ('Toyota', 'Camry', 2017-01-03),
        ('Toyota', 'Corrola', 2017-01-04),
        ('Kia', 'Sorrento', 2017-01-05),
        ('Honda', 'Civic', 2017-01-06),
        ('Honda', 'Civic', 2017-01-07),
        ('Honda', 'Civic', 2017-01-01),
        ('Honda', 'Civic', 2017-01-01),
        ('Honda', 'Civic', 2017-01-01),
        ('Honda', 'Accord', 2017-01-02),
        ('Toyota', 'Camry', 2017-01-03),
        ('Toyota', 'Corrola', 2017-01-04),
        ('Kia', 'Sorrento', 2017-01-05),
        ('Honda', 'Civic', 2017-01-06),
        ('Honda', 'Civic', 2017-01-07),
        ('Honda', 'Accord', 2017-01-02),
        ('Toyota', 'Camry', 2017-01-03),
        ('Toyota', 'Corrola', 2017-01-04),
        ('Kia', 'Sorrento', 2017-01-05),
        ('Honda', 'Civic', 2017-01-06),
        ('Honda', 'Civic', 2017-01-07),
        ('Honda', 'Accord', 2017-01-02),
        ('Toyota', 'Camry', 2017-01-03),
        ('Toyota', 'Corrola', 2017-01-04),
        ('Kia', 'Sorrento', 2017-01-05),
        ('Honda', 'Civic', 2017-01-06),
        ('Honda', 'Civic', 2017-01-07),
        ]

    c.executemany('INSERT INTO orders VALUES (?,?,?)', car_order_date)
