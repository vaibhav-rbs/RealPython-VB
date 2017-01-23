import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("""SELECT COUNT(orders.model) FROM  orders where make = 'Honda'""")

    rows = c.fetchall()


for r in rows:
    print ("MAKE: {}".format(r[0]))
