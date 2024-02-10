#!/usr/bin/python3
"""This is the amenity module that defines amenity class"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """This Class defines the Amenity attributes
    Args:
        name (str): the Amenity name"""

    name = ""
