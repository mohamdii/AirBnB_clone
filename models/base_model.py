#!/usr/bin/python3
"""
uuid module is to make unique ids
date time n.module.
"""
import uuid
from datetime import datetime
from models.engine.file_storage import FileStorage
f = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """the base class
    """

    def __init__(self, *args, **kwargs):
        """*args, **kwargs"""

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, f)
                setattr(self, key, value)
        else:
            FileStorage.new(self)
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """returns message"""

        prt2 = "({}) {}".format(self.id, self.__dict__)
        return "[{}] ".format(self.__class__.__name__) + prt2

    def save(self):
        """save module
        """

        self.updated_at = datetime.now()
        FileStorage.save()

    def to_dict(self):
        """to dict module"""

        dic = self.__dict__.copy()
        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()
        return dic
