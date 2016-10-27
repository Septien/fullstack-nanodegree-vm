import sys

from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

#Let SQLALchemy know that our classes  correspond to tables on our database
Base = declarative_base()


#Goes at the end
#
engine = create_engine('sqlite:///restaurantmenu.db')

#Add the created classes as new tables in the database
Base.metadata.create_all(engine)
