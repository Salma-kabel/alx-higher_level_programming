#!/usr/bin/python3
"""
creates the State “California” with the City
“San Francisco” from the database hbtn_0e_100_usa
"""


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session1 = sessionmaker(bind=engine)
    session = session1()

    session.add(State(name='California', cities=[City(name='San Francisco')]))
    session.commit()
    session.close()
