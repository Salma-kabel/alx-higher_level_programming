#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
"""

from sys import argv
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("""SELECT cities.name, states.name FROM cities
                JOIN states ON cities.state_id = states.id
                ORDER BY cities.id""")
    states = cur.fetchall()
    for i, state in enumerate(states, start=0):
        if state[1] == argv[4]:
            if i != 0:
                print(", ", end="")
            print(state[0], end="")
    print("")
