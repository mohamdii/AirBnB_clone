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

        self.__objects[obj.__class__.name + "." + str(obj)] = obj

    def save(self):
        '''
            saves into file
        '''
        new_dict = self.__objects
        n_dict = {obj: new_dict[obj].to_dict() for obj in new_dict.keys()}
        with open(self.__file_path, mode="w+") as file:
            json.dump(n_dict, file)

    def reload(self):
        '''checks if file exists and loads back the inside
        '''
        data = {}
        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as file:
                data = json.loads(file.read())
        except FileNotFoundError:
            pass
