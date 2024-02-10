#!/usr/bin/python3
"""Test amenity"""

from models.amenity import Amenity
from models.base_model import BaseModel
import unittest


class TestAmenity(unittest.TestCase):
    """Test the Amenity class"""
    def setUp(self):
        """Instantiation"""
        pass

    def tearDown(self):
        """Clear everything each test case"""
        pass

    def test_inheritance(self):
        """Test Amenity is a subclass of BaseModel"""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_isinstance(self):
        """Test if instance is indeed an instance of Amenity"""
        a = Amenity()
        self.assertEqual("<class 'models.amenity.Amenity'>", str(type(a)))

    def test_name_instance(self):
        """Test if name is intialize with an empty string"""
        a = Amenity()
        self.assertEqual(a.name, "")


if __name__ == "__main__":
    unittest.main()
