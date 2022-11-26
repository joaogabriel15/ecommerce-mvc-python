from sqlalchemy import Integer, String, BigInteger, Column, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
from . import State


class Country(Base):
    __tablename__ = "Country"
    

    id = Column(Integer, primary_key=True)
    description = Column(String(100))
    state = relationship("State", backref="Country")