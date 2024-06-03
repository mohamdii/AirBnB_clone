#!/usr/bin/python3
"""Base class"""
import uuid
import datetime


class BaseModel:
    def __init__(self):
        self.id = uuid.uuid4()
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()


    def __str__(self):
        return "[{}] ({}) {}".format(
            self.__class__.__name__, 
            self.id, BaseModel.__dict__)
        
    def save(self):
        self.updated_at = datetime.datetime.now()
        
    def to_dict(self):
        dictionary = self.__dict__
        dictionary['__class__'] = self.__class__.__name__
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        return dictionary

if __name__ == '__main__':
    a = BaseModel()
    print(a.updated_at, a.id)
    print(a.to_dict())
    print(a)
    """print(str(a))"""