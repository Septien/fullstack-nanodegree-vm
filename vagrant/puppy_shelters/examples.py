from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Shelter, Puppy
from random import randint
import datetime
import random

engine = create_engine('sqlite:///puppyshelter.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

#1. Query all puppies and return the result in ascending alphabetical order
query = session.query(Puppy).order_by(Puppy.name)

for q in query:
    print q.name, q.dateOfBirth, q.gender, q.weight
