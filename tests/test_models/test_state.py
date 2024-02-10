#!/usr/bin/python3
"""Test user module"""

from models.base_model import BaseModel
from models.state import State
import unittest


class TestState(unittest.TestCase):
    """Test the User"""
    def setUp(self):
        """Instantiation"""
        self.s = State()

    def tearDown(self):
        """Clear everything each test case"""
        pass

    def test_inheritance(self):
        """Test if State is a subclass of BaseModel"""
        self.assertTrue(issubclass(State, BaseModel))

    def test_isinstance(self):
        """Test if s is an instance of State"""
        self.assertEqual("<class 'models.state.State'>", str(type(self.s)))

    def test_name(self):
        """Test if name is intialized with an empty string"""
        self.assertEqual(self.s.name, "")

        
if __name__ == "__main__":
    unittest.main()
