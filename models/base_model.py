#!/usr/bin/python3
"""Base class"""
import uuid
from datetime import datetime
import models

class BaseModel:

    tform = "%Y-%m-%dT%H:%M:%S.%f"
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    self.__dict__[key] = datetime.strptime(value, self.tform)
                else:
                    self.__dict__[key] = value            
        else:
            models.storage.new(self)                    

    def __str__(self):
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        dictionary = self.__dict__
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
