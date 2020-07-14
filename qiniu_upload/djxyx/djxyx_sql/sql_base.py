import sqlite3
import os
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

sqlite_db = "sqlite:///%s" % os.path.join(os.path.dirname(__file__), 'test.db')
engine = sqlalchemy.create_engine(sqlite_db)
Session = sessionmaker(bind=engine)
session = Session()


def create_tables():
    Base.metadata.create_all(engine, checkfirst=True)
