#!/usr/bin/python3
"""
Script that lists all states from the
database hbtn_0e_0_usa
"""

from sys import argv
import MySQLdb


def main():
    db = MySQLdb.connect(host="localhost",
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY id")
    states = cur.fetchall()
    for state in states:
        print(state)


if __name__ == "__main__":
    main()
