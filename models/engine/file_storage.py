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
        n_dict = {obj: new_dict[obj].to_dic() for obj in new_dict.keys()}
        with open(self.__file_path, "w") as file:
            json.dump(n_dict, file)

    def reload(self):
        '''checks if file exists and loads back the inside
        '''
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                data = json.loads(file.read())
                for key, value in data.items():
                    name_c = key.split(".")
                    obj_id = eval(name_c)
                    obj = obj_id(**value)
                    self.__objects[key] = obj

        except FileNotFoundError:
            pass
