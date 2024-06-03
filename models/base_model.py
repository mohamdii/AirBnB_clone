#!/usr/bin/python3
"""Base class"""
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()


    def __str__(self):
        return "[{}] ({}) {}".format(
            self.__class__.__name__, 
            self.id, BaseModel.__dict__)


    def save(self):
        self.updated_at = datetime.today()


    def to_dict(self):
        dictionary = self.__dict__
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
