#!/usr/bin/python3
"""Test user module"""

from models.base_model import BaseModel
from models.user import User
import unittest


class TestUser(unittest.TestCase):
    """Test the User"""
    def setUp(self):
        """Instantiation"""
        pass

    def tearDown(self):
        """Clear everything each test case"""
        pass

    def test_inheritance(self):
        """Test User is a subclass of BaseModel"""
        self.assertTrue(issubclass(User, BaseModel))

    def test_isinstance(self):
        """Test if instance is indeed an instance of User"""
        a = User()
        self.assertEqual("<class 'models.user.User'>", str(type(a)))

    def test_email(self):
        """Test if email is intialize with an empty string"""
        a = User()
        self.assertEqual(a.email, "")

    def test_password(self):
        """Test if password is intialize with an empty string"""
        a = User()
        self.assertEqual(a.password, "")

    def test_first_name(self):
        """Test if first_name is intialize with an empty string"""
        a = User()
        self.assertEqual(a.first_name, "")

    def test_first_name(self):
        """Test if last_name is intialize with an empty string"""
        a = User()
        self.assertEqual(a.last_name, "")


if __name__ == "__main__":
    unittest.main()
