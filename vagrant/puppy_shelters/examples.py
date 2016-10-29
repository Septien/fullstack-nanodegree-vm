from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Shelter, Puppy
from random import randint
import datetime
import random

engine = create_engine('sqlite:///puppyshelter.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
sessino = DBSession()


