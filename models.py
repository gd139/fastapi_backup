from cgitb import text
from contextlib import nullcontext
from datetime import date, datetime
import email
from enum import unique
from msilib.schema import Class
from sqlite3 import Timestamp, connect
import string
from xml.dom.minidom import Text
from numpy import delete, integer
from pydantic import PostgresDsn
#from .database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Boolean, Column, Integer, String, column,ForeignKey
from sqlalchemy.sql.expression import Null,text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from database import Base
import time


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String,nullable=False)
    published = Column(Boolean, server_default="TRUE",nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default = text('now()'))
    owner_id = Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),nullable=False)
    owner = relationship("User")
 

class User(Base):
    __tablename__ = "users"

    email= Column(String,nullable=False,unique=True)
    password= Column(String,nullable=False)
    id = Column(Integer, primary_key=True, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default = text('now()'))

class Vote(Base):
    __tablename__ = "votes"

    post_id=Column(Integer,ForeignKey("posts.id",ondelete="CASCADE"),primary_key=True)
    user_id=Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),primary_key=True)
  