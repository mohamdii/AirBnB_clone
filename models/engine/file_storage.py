#!/usr/bin/python3
import json
from models.base_model import BaseModel


class FileStorage:
    """storing data to json"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return all"""

        return self.__objects

    def new(self, obj):
        """create new obj"""

        self.__objects[self.__class__.name + "." + obj.id] = obj

    def save(self):
        '''
            saves into file
        '''
        new_dict = self.__objects
        n_dict = {obj: new_dict[obj].to_dict() for obj in new_dict.keys()}
        with open(self.__file_path, mode="w") as file:
            json.dump(n_dict, file)

    def reload(self):
        '''checks if file exists and loads back the inside
        '''
        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as file:
                data = json.loads(file)
                for key, value in data.items():
                    obj_key = key.split(".")[1]
                    object = BaseModel(**value)
                    self.__objects[key] = obj

        except FileNotFoundError:
            pass
