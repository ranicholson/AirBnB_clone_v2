#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship



class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="delete", backref="state")

    if models.hbnb_storage != "db":
        @property
        def cities(self):
            """File storage getter"""
            citylist=[]
            for obj in models.hbnb_storage.all():
                if obj.state_id == self.id:
                    citylist += obj
            print(citylist)
