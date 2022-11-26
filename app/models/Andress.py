from sqlalchemy import Integer, String, BigInteger, Column, ForeignKey
from .database import Base
from . import City, User


class Andress(Base):
    __tablename__ = "Andress"
   

    id = Column(BigInteger, primary_key=True)
    cityId = Column(Integer, ForeignKey("City.id"))
    street=Column(String(100))
    number=Column(Integer)
    userId=Column(BigInteger, ForeignKey('User.id'))
    complement=Column(String(100))
    reference=Column(String(100))
    district=Column(String(100))
    CEP=Column(String(25))
    