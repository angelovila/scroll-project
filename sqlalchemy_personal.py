
#configuration
import datetime  # this is for dateadded column on Items class
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, DateTime, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Cases(Base):
    __tablename__ = 'cases'

    id = Column(Integer, primary_key=True)
    pdf = Column(String(250), nullable=False)
    prosecutor_defendant = Column(String(300))
    gr_number = Column(String(300))
    date = Column(String(50)) #figure out date format


class Items(Base):  #class
    __tablename__ = 'items'  #table

    id = Column(Integer, primary_key=True)  #mapper
    name = Column(String(250), nullable=False)
    description = Column(String(300), nullable=True)
    categoryID = Column(Integer, ForeignKey('categories.id'))
    dateadded = Column(DateTime, default = datetime.datetime.utcnow)
    user_id = Column(Integer, ForeignKey('users.id'))
    image = Column(String(250))
    users = relationship(Users)





#configuration
engine = create_engine('sqlite:///cases.db')


Base.metadata.create_all(engine)