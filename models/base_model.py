#!/usr/bin/python3
"""
This is the Base Model defines the BaseModel class
"""

from datetime import datetime
import models
from uuid import uuid4


class BaseModel:
    """this is the base class model

        Attr:
            id (uuid4): unique id for each instance
            created_at (datetime): timestamp for creation
            updated_at (datetime): timestamp for updation

        Methods:
            save(self)
            to_dict(self)
    """

    def __init__(self, *args, **kwargs):
        """ the class constructor
        """
        if kwargs:
            del kwargs["__class__"]
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime
                            (value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ returns the string representation of the instance
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ updates the public instance attribute updated_at
        """
        updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__
        """
        instance_dict = {}
        instance_dict["__class__"] = self.__class__.__name__

        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                instance_dict[key] = value.isoformat()
            else:
                instance_dict[key] = value

        return instance_dict
