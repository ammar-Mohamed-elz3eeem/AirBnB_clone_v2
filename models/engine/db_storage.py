#!/usr/bin/python3
"""
This module will be for defining new storage system
for database management
"""


from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.user import User
from models.amenity import Amenity

classes = {
    "Amenity": Amenity,
    "User": User,
    "City": City,
    "State": State,
    "Place": Place,
    "Review": Review
}


class DBStorage():
    """
    DBStorage Class:
        This class will be responsible for creating new storage
        for database and will work as database management storage
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        - control what database to connect to
        - control type of enivornment for the database
        """
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}:3306/{}"
                                      .format(
                                          getenv("HBNB_MYSQL_USER"),
                                          getenv("HBNB_MYSQL_PWD"),
                                          getenv("HBNB_MYSQL_HOST"),
                                          getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """ query all objects found in database """
        new_dict = {}
        if cls is not None:
            objs = self.__session().query(eval(cls)).all()
            for obj in objs:
                new_dict[obj.__class__.__name__ + "." + obj.id] = obj
        else:
            for classname in classes:
                if cls is None or cls is classes[classname] \
                           or cls is classname:
                    objs = self.__session.query(classname).all()
                    for obj in objs:
                        new_dict[obj.__class__.__name__ + "." + obj.id] = obj
        return new_dict

    def new(self, obj):
        """ adds obj to database session """
        self.__session.add(obj)

    def save(self):
        """ commits session changes to db """
        self.__session.commit()

    def delete(self, obj):
        """ delete obj from database if it is not none """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ implement a method to make session and connect database """
        Base.metadata.create_all(bind=self.__engine)
        session_fact = sessionmaker(expire_on_commit=False, bind=self.__engine)
        Session = scoped_session(session_fact)
        self.__session = Session

    def close(self):
        """this function will handle closing db session"""
        self.__session.remove()
