from sqlalchemy import Column, Integer, String
from database import Base

"""SQL Alchemy is a python library used to interact with databases.
Acts as a bridge between python code and the database.

It is an ORM , without ORM you will have to manually write SQL queries"""

#The class is created bcs SQLAlchemy uses classes to represent database tables.
#A class is being used as a blueprint for a database table.
class url(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key = True, index=True)
    short_code = Column(String, unique=True, index = True)
    original_url = Column(String)

