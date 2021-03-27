#!/usr/bin/python3
"""Storage engine for database
"""


import models
from models.base_model import BaseModel, Base
from models.city import City
from models.state import State
from models.amenities import Amenities
from models.user import User
from models.review import Review
from models.place import Place
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from os import getenv


classes = {
    "Amenity": Amenity,
    "City": City,
    "User": User,
    "State": State,
    "Place": Place,
    "Review": Review}


class DBStorage:

    """Database Storage
    """
    __engine = None
    __session = None

    def __init__(self):
        """Constructor for DB storage engine
        """
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                HBNB_MYSQL_USER,
                HBNB_MYSQL_PWD,
                HBNB_MYSQL_HOST,
                HBNB_MYSQL_DB))

        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Display all objects
        """
        all_dict = {}
        for items in classes:
            if cls is None:
                obj = self.__session.query(classes[items]).all()
                for v in obj:
                    k = v.__class__.__name__ + '.' + v.id
                    all_dict[k] = v
        return all_dict

    def new(self, obj):
        """add object to current database session
        """
        self.__session.add(obj)

    def save(self):
        """Commit changes
        """
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from database
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Magic
        """
        Base.metadata.create_all(engine)
        sm = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sm)
        self.__session = Session()
