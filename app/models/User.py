from sqlalchemy import Integer, String, BigInteger, Column,CHAR, Table
from sqlalchemy.orm import relationship
from .database import Base
from . import Andress

class User(Base):
    __tablename__ = "User"
    

    id = Column(BigInteger, primary_key=True)
    situation = Column(String(20))
    userType = Column(String(20))
    name = Column(String(100))
    gender = Column(CHAR(1))
    CPF = Column(Integer)
    telephone = Column(String(15))
    phone = Column(String(15))
    email = Column(String(100))
    password = Column(String(100))
    token = Column(String(100))

    andress = relationship("Andress", backref="User")
    
