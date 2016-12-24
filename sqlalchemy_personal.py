
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
    party1 = Column(String(300))
    party2 = Column(String(300))
    gr_number = Column(Integer)
    date_day = Column(Integer)
    date_month = Column(Integer)
    date_year = Column(Integer)



#configuration
engine = create_engine('sqlite:///cases.db')


Base.metadata.create_all(engine)