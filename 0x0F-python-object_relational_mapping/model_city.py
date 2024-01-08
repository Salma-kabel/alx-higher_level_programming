#!/usr/bin/python3
"""
contains the class definition of a City
that inherits instance Base = declarative_base()
"""


from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """inherits from base links to the MySQL table cities"""
    __tablename__ = "cities"
    id = Column(Integer, unique=True, nullable=False,primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, ForeignKey('states.id'))
