#!/usr/bin/python3
"""
    This is the filestorage model
"""

from json import dump
from json import load
from models.base_model import BaseModel

class FileStorage:
    """serializes and deserializes instances
        
        Attr:
            __objects (dictionary): dictionary holding all instances
            __fpath (string): the path of the JSON file

        Methods:
            all(self)
            new(self, obj)
            save(self)
            reload(self)
    """
    __objects = {}
    __fpath = "file.json"
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
        
        with open(FileStorage.__fpath, "w", encoding="utf-8") as jsonF:
            dump(serialized, jsonF)

    def reload(self):
       """deserializes the JSON file"""
       allClasses = {'BaseModel': BaseModel}

       try:
           with open(FileStorage.__fpath, encoding="utf-8") as jsonStr:
               deserialized = load(jsonStr)
               for objVal in deserialized.values():
                   className = objVal["__class__"]
                   classObject = allClasses[className]
                   self.new(classObject(**objVal))
       except FileNotFoundError:
           pass
