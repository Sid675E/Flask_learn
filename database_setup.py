import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
##### Use in configuration and class code ######
from sqlalchemy.orm import relationship
##### For creating foriegn key relationship #####
from sqlalchemy import create_engine

Base = declarative_base()
#####Instance of the declarative_base Class imported above #####
####### insert at end of the file ######

class Restaurant(Base):
    __tablename__ = 'restaurant'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class MenuItem(Base):
    __tablename__ = 'menu_item'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    price = Column(String(8))
    course = Column(String(250))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)


engine = create_engine('postgresql+psycopg2://postgres:XxxAahSn@2*5@localhost/restr')


Base.metadata.create_all(engine)