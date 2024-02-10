#!/usr/bin/python3
"""This is the filestorage module that define FileStorage class"""

from json import dump
from json import load
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """serializes and deserializes instances

        Attr:
            __objects (dictionary): dictionary holding all instances
            __file_path (string): the path of the JSON file

        Methods:
            all(self)
            new(self, obj)
            save(self)
            reload(self)
    """
    __objects = {}
    __file_path = "file.json"

    def all(self):
        """returns the ___objects dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """appends obj to the __objects dict"""

        objKey = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[objKey] = obj

    def save(self):
        """serializes __objects to the JSON file"""

        serialized = {}

        for key, value in FileStorage.__objects.items():
            serialized[key] = value.to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as jsonF:
            dump(serialized, jsonF)

    def reload(self):
        """deserializes the JSON file"""
        all_classes = {'BaseModel': BaseModel,
                       'User': User,
                       'State': State,
                       'City': City,
                       'Amenity': Amenity,
                       'Place': Place,
                       'Review': Review}

        try:
            with open(FileStorage.__file_path, encoding="utf-8") as jsonStr:
                deserialized = load(jsonStr)
                for obj_val in deserialized.values():
                    class_name = obj_val["__class__"]
                    class_object = all_classes[class_name]
                    if class_object:
                        self.new(class_object(**obj_val))
        except FileNotFoundError:
            pass
