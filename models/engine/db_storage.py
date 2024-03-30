#!/usr/bin/python3
"""This module defines a class to manage databases for hbnb clone"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os


class DBStorage:
    """This class manages storage of hbnb models in database"""
    __engine = None
    __session = None

    def __init__(self):
        from models.base_model import Base
        user = os.getenv("HBNB_MYSQL_USER")
        password = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        database = os.getenv("HBNB_MYSQL_DB")

        DBStorage.__engine = create_engine(f"mysql+mysqldb://{user}:{password}@{host}:3306/{database}", pool_pre_ping=True)

        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(DBStorage.__engine)


    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        
        lst = DBStorage.__session.query(cls).all()
        r = {}
        for obj in lst:
            r[obj.__class__.__name__ + "." + obj.id] = obj
        return r


    def new(self, obj):
        """Adds new object to database"""
        DBStorage.__session.add(obj)
        

    def save(self):
        """Saves storage dictionary to file"""
        DBStorage.__session.commit()

    def reload(self):
        """Reload database"""
        from models.base_model import Base
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        Base.metadata.create_all(DBStorage.__engine)
        session_class = sessionmaker(bind=DBStorage.__engine, expire_on_commit=False)
        DBStorage.__session = scoped_session(session_class)
    
    def delete(self, obj=None):
        """ Deletes object from database"""
        if obj:
            DBStorage.__session.delete(obj)

