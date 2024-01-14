#!/usr/bin/python3
"""
Initialisation of class
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.place import Place


class FileStorage:
    """ The file storage (Serialisation and deserialisation)"""

    def __init__(self):
        self.__file_path = 'file.json'
        self.__objects = {}

    def all(self):
        """ Returns the __objects attribute """

        return self.__objects

    def new(self, obj):
        """  Adds a new object to the __objects attribute"""

        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """ Serializes all objects in the __objects
        attribute to a JSON file """

        with open(self.__file_path, 'w') as f:
            to_save = {k: v.to_dict() for k, v in self.__objects.items()}
            f.write(json.dumps(to_save))

    def reload(self):
        """ Deserializes all objects from the JSON
        file to the __objects attribute """

        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as file:
                objs = json.loads(file.read())
                if not len(objs):
                    return
                a = objs.items()
                {k: self.new(eval(v['__class__'])(**v)) for k, v in a}
        except FileNotFoundError:
            pass
