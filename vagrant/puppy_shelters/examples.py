from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Shelter, Puppy
from random import randint
import datetime as dt
import random

engine = create_engine('sqlite:///puppyshelter.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

#1. Query all puppies and return the result in ascending alphabetical order
query = session.query(Puppy).order_by(Puppy.name)

#for q in query:
#    print q.name, q.dateOfBirth, q.gender, q.weight

#2. Query all the objects that are less than 6 months old organized by the youngest first
sixmonths = dt.date.today() - dt.timedelta(weeks = 26)

query = session.query(Puppy).filter(Puppy.dateOfBirth >= sixmonths).order_by(desc(Puppy.dateOfBirth))

for q in query:
    print q.name, q.dateOfBirth, q.gender, q.weight
