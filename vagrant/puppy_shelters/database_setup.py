#Necesary modules
#Configuration modules
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative_base import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

#Create class for the corresponding tables to use
class Shelter(Base):
    __table_name__ = 'shelter'
    #
    name = Column(String(80), nullable = False)
    #
    address = Column(String(80), nullable = False)
    #
    city = Column(String(80), nullable = False)
    #
    state = Column(String(80))
    #


#Create engine for database contection
engine = create_engine('sqlite:///puppies.db')
#Add created class, as tables, to the database
Base.metadata.create_all(engine)