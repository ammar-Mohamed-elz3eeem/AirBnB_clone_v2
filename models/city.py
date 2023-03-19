#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from os import getenv


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        __tablename__ = "cities"
        name = Column(String(128), nullable=False)
        state_id = Column(Integer(), ForeignKey("states.id"), nullable=False)
    else:
        name = ""
        state_id = ""
