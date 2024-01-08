#!/usr/bin/python3
"""
prints all City objects from the database hbtn_0e_14_usa
"""


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City



if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    session1 = sessionmaker(bind=engine)
    session = session1()
    for state, city in session.query(State, City).filter(
            State.id == City.state_id).order_by(City.id):
                print("{}: ({}) {}".format(state.name, city.id, city.name))
