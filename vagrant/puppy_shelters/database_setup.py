#Necesary modules
#Configuration modules
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Float
from sqlalchemy.ext.declarative_base import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

#Create class for the corresponding tables to use
class Shelter(Base):
    __tablename__ = 'shelter'
    #
    name = Column(String(80), nullable = False)
    #
    address = Column(String(250))
    #
    city = Column(String(80))
    #
    state = Column(String(20))
    #
    zipCode = Column(String(10))
    #
    website = Column(String)
    #
    id = Column(Integer, primary_key = True)

class Puppy(Base):
    __tablename__ = 'ppuppy'
    #
    name = Column(String(40), nullable = False)
    #
    birth_date = Columnt(Date)
    #
    gender = Column(String(6), nullable = False)
    #
    weight = Column(Float)
    #
    shelt_id = Column(Integer, ForeignKey('shelter.id'))
    #
    shelter = relationship(Shelter)

#Create engine for database contection
engine = create_engine('sqlite:///puppies.db')
#Add created class, as tables, to the database
Base.metadata.create_all(engine)