#!/usr/bin/python3
"""Test cite module"""

from models.base_model import BaseModel
from models.city import City
import unittest


class TestCity(unittest.TestCase):
    """Test the City"""
    def setUp(self):
        """Instantiation"""
        self.c = City()

    def tearDown(self):
        """Clear everything each test case"""
        pass

    def test_inheritance(self):
        """Test if City is a subclass of BaseModel"""
        self.assertTrue(issubclass(City, BaseModel))

    def test_isinstance(self):
        """Test if c is indeed an instance of City"""
        self.assertEqual("<class 'models.city.City'>", str(type(self.c)))

    def test_state_id(self):
        """Test if state_id is intialize with an empty string"""
        self.assertEqual(self.c.state_id, "")

    def test_name(self):
        """Test if name is intialized with an empty string"""
        self.assertEqual(self.c.name, "")


if __name__ == "__main__":
    unittest.main()
