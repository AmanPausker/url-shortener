
from sqlalchemy import create_engine
#Create engine is used to create the connection layer b/w python and the database

from sqlalchemy.orm import sessionmaker, declarative_base
#This defines WHICH database SQLAlchemy should connect to.
#
# SQLite connection format:
#
# sqlite:///./urls.db
DATABASE_URL = "sqlite:///./urls.db"
# Sessions are extremely important in SQLAlchemy.
#
# A Session represents:
# "a temporary conversation with the database"
#
# You use sessions to:
# - add data
# - query data
# - update data
# - delete data
# - commit transactions
#
# Example:
# db.add(...)
# db.commit()
# db.query(...)
#
# declarative_base() creates a special base class
# used for defining ORM models.
#
# Every SQLAlchemy model class will inherit from this Base.
#
# Example:
# class URL(Base):
#
# This allows SQLAlchemy to:
# - track models
# - generate tables
# - map Python objects to database rows

engine = create_engine(
    DATABASE_URL, 
    connect_args = {"check_same_thread":False}
)

SessionLocal = sessionmaker(
    autocommit = False,
    autoflush = False,
    bind = engine
)
Base = declarative_base()