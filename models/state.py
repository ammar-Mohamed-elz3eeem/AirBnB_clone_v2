#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import String, Integer, Column
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="save-update, merge, delete")
    else:
        name = ""

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """ getter for cities using state.id """
            filtered_cities = []
            all_cities = models.storage.all('City')
            for val in all_cities.values():
                if val.state_id == self.id:
                    filtered_cities.append(val)
            return filtered_cities
