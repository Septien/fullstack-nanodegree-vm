import sys

from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

#Let SQLALchemy know that our classes  correspond to tables on our database
Base = declarative_base()

#Class for the restaurant table
class Restaurant(Base):
    #Let SQLAlchemy know which variable we'll be using to refer to our table
    __tablename__ = 'restaurant'
    #Name of the restaurant. Must contain a value
    name = Column(String(80), nullable = False)
    #Primary key
    id = Column(Integer, primary_key = True)

#Class for the menu_item table
class MenuItem(Base):
    __tablename__ = 'menu_item'
    #Name of the entry. Must contain a value
    name = Column(String(80), nullable = False)
    #Primary Key
    id = Column(Integer, primary_key = True)
    #Course
    course = Column(String(250))
    #
    description = Column(String(250))
    #
    price = Column(String(8))
    #Specify relationship amog tables
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    #
    restaurant = relationship(Restaurant)

#Goes at the end
#
engine = create_engine('sqlite:///restaurantmenu.db')

#Add the created classes as new tables in the database
Base.metadata.create_all(engine)
