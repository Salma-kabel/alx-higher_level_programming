"""
script that lists all states from the
database hbtn_0e_0_usa

"""

#!/usr/bin/python3

from sys import argv
import MySQLdb


if __name__ == "__main__":
    """connect to data base"""

    db = MySQLdb.connect(host="localhost",
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT id, name FROM "states" ORDER BY id")
    states = cur.fetchall()
    for state in states:
        print(state)
