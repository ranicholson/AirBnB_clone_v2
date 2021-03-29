#!/usr/bin/python3
""" City Module for HBNB project """

import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from os import getenv


class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    name = Column(String(128), primary_key=True, nullable=False)
    