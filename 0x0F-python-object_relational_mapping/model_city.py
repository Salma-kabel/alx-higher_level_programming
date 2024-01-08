#!/usr/bin/python3
"""
contains the class definition of a City
that inherits instance Base = declarative_base()
"""

"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base
"""
from lib2to3.pytree import Base
from sre_parse import State
from unicodedata import name
from sqlalchemy import Column, ForeignKey, Integer, String, null
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class City(Base):
    """inherits from base links to the MySQL table cities"""
    __tablename__ = "cities"
    id = Column(Integer, unique=True, nullable=False,primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, ForeignKey('states.id'))
