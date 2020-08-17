from sqlalchemy import create_engine,Column,Integer,String,DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
import pymysql
import sys
from datetime import datetime,date

DeclarativeBase = declarative_base()

class BasicItem(DeclarativeBase):
    __tablename__ = "dse"

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    brand=Column('brand',String(200), nullable=True)
    amount=Column('amount',Integer, nullable=True)
    status=Column('status',Integer,nullable=True)
    old=Column('old',String(10),nullable=True)
    current=Column('current',String(10),nullable=True)
    created_at =Column('created_at',DateTime,nullable=True)