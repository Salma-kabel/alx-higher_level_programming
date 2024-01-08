#!/usr/bin/python3
"""
lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa using mysqldb
"""

from sys import argv
import MySQLdb


def main():
    """
    connect to database
    """
    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states WHERE name LIKE "N%" ORDER BY id")
    states = = cur.fetchall()
    for state in states:
        print(state)


if __name__ == "__main__":
    main()
