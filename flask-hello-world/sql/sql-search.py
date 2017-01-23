#!/usr/local/bin/python3

import argparse
parser = argparse.ArgumentParser()
import sqlite3

parser.add_argument("operation", type=str,
                    help="""Select the operation that you want to perform: AVG, MAX, MIN, SUM, EXIT """)
args = parser.parse_args()

with sqlite3.connect('newnum.db') as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT {}(num) from numbers".format(args.operation))
    get = cursor.fetchone()

print (get[0])
