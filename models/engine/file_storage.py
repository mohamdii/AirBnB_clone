#!/usr/bin/python3
"""Storage Class"""
import json

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects['{}.{}'.format(self.__class__.__name__, obj.id)] = obj

    def save(self):
        filename = self.__file_path
        obj = self.__objects
        objdict = {item: obj[item].to_dict() for item in obj.keys()}
        with open(filename, mode='w', encoding='utf-8') as file:
            json.dump(objdict, file)
            
    def reload(self):
        try:
            with open(self.__file_path) as file:
                objdict = json.load(file)
                for o in objdict.items():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
