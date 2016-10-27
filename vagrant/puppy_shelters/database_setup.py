#Necesary modules
#Configuration modules
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

#Let SQLALchemy know that our classes  correspond to tables on our database
Base = declarative_base()

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
    __tablename__ = 'puppy'
    #
    id = Column(Integer, primary_key = True)
    #
    name = Column(String(40), nullable = False)
    #
    dateOfBirth = Column(Date)
    #
    picture = Column(String)
    #
    gender = Column(String(6), nullable = False)
    #
    weight = Column(Numeric(10))
    #
    shelt_id = Column(Integer, ForeignKey('shelter.id'))
    #
    shelter = relationship(Shelter)

#Create engine for database contection
engine = create_engine('sqlite:///puppyshelter.db')
#Add created class, as tables, to the database
Base.metadata.create_all(engine)