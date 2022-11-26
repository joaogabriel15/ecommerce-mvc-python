from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
from . import Andress, State


class City(Base):
    __tablename__ = "City"
   

    id = Column(Integer,primary_key=True)
    stateId = Column(Integer, ForeignKey("State.id"))
    description = Column(String(100))


    andress = relationship("Andress", backref="City" )