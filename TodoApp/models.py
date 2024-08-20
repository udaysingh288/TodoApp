from database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True,autoincrement=True,index=True)
    email = Column(String(50), nullable=False,unique=True)
    username = Column(String(50),nullable=False,unique=True)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    hashed_password = Column(String(50),nullable=False)
    is_active = Column(Boolean,default=True)
    role=Column(String(50),nullable=False)



class Todos(Base):
    __tablename__='todos'
    id = Column(Integer,primary_key=True,index=True)
    title=Column(String)
    description=Column(String)
    priority=Column(Integer)
    complete=Column(Boolean,default=False)
    owner_id=Column(Integer,ForeignKey('users.id'))


