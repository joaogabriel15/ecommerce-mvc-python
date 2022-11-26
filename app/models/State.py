from sqlalchemy import Integer, ForeignKey, String, Column
from sqlalchemy.orm import  relationship
from .database import Base
from . import City, Country

class State(Base):
    __tablename__ = "State"
   

    id        = Column(Integer, primary_key=True)
    countryId    = Column(Integer, ForeignKey("Country.id"))
    description = Column(String(50))
    initials     = Column(String(2))

    city = relationship("City", backref="State")