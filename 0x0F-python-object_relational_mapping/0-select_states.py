#!/usr/bin/python3

import sys import argv
import MySQLdb
"""
script that lists all states from the
database hbtn_0e_0_usa

"""


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT id, name FROM "states" ORDER BY id")
    states = cur.fetchall()
    for state in states:
        print(state)
