import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("""SELECT inventory.model, inventory.make, inventory.quantity, orders.order_date FROM inventory, orders WHERE orders.make=inventory.make and orders.model=inventory.model""")

    rows = c.fetchall()


for r in rows:
    print ("MAKE: {}".format(r[0]))
    print ("MODEL: {}".format(r[1]))
    print ("ORDER: DATE {}".format(r[3]))
