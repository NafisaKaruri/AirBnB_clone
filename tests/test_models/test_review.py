#!/usr/bin/python3
"""Test review model"""

from models.base_model import BaseModel
from models.review import Review
import unittest


class TestReview(unittest.TestCase):
    """Test the Review"""
    def setUp(self):
        """Instantiation"""
        self.r = Review()

    def tearDown(self):
        """Clear everything each test case"""
        pass

    def test_inheritance(self):
        """Test if Review is a subclass of BaseModel"""
        self.assertTrue(issubclass(Review, BaseModel))

    def test_isinstance(self):
        """Test if r is indeed an instance of Review"""
        self.assertEqual("<class 'models.review.Review'>", str(type(self.r)))

    def test_place_id(self):
        """Test if place_id is intialized with an empty string"""
        self.assertEqual(self.r.place_id, "")

    def test_user_id(self):
        """Test if user_id is intialized with an empty string"""
        self.assertEqual(self.r.user_id, "")

    def test_text(self):
        """Test if text is initialized with an empty string"""
        self.assertEqual(self.r.text, "")


if __name__ == "__main__":
    unittest.main()
