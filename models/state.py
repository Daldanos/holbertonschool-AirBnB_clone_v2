#!/usr/bin/python3
""" State Module for HBNB project """
from base_model import BaseModel, Base
from city import City
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete-orphan")

    @property
    def cities(self):
        from models import storage
        cities2 = models.storage.all(City)
        r = []
        for c in cities2:
            if c.state_id == self.id:
                r.append(c)
        return r
