#Necesary modules
#Configuration modules
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative_base import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

#Create engine for database contection
engine = create_engine('sqlite:///puppies.db')
#Add created class, as tables, to the database
Base.metadata.create_all(engine)