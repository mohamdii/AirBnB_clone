#!/usr/bin/python3


class FileStorage:
    """storing data to json"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return all"""

        return self.__objects

    def new(self, obj):
        """create new obj"""

        self.__obj
