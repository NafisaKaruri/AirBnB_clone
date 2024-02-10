#!/usr/bin/python3
"""This is the BaseModel test"""

from models.base_model import BaseModel
from datetime import datetime
import unittest
import uuid


class TestBaseModel(unittest.TestCase):
    """This class tests the base_model module"""
    def setUp(self):
        """Instantiation"""
        pass

    def tearDown(self):
        """Clear"""
        pass

    # --------------- Test task 3 ---------------
    def test_isinstance(self):
        """Tests is instance"""
        b = BaseModel()
        self.assertEqual("<class 'models.base_model.BaseModel'>", str(type(b)))

    def test_id(self):
        """Tests id"""
        b = BaseModel()
        self.assertIsInstance(b.id, str)

    def test_created_at(self):
        """Tests created_at"""
        b = BaseModel()
        self.assertEqual(datetime, type(b.created_at))

    def test_updated_at(self):
        """Tests updated_at"""
        b = BaseModel()
        self.assertEqual(datetime, type(b.updated_at))

    def test_str(self):
        """Tests the string presentation of the instance"""
        b = BaseModel()
        self.assertEqual(f"[BaseModel] ({b.id}) {b.__dict__}", str(b))

    def test_save(self):
        """Test the save function"""
        b = BaseModel()
        b.save()
        self.assertIsInstance(b.updated_at, datetime)

    def test_to_dict(self):
        """Test to_dict function"""
        b = BaseModel()
        b_dict = b.to_dict()
        self.assertIsInstance(b_dict, dict)

    # --------------- Test task 4 ---------------
    def test_args(self):
        """Test args"""
        b = BaseModel(1)

    def test_kwargs(self):
        """Test Kwargs"""
        b = BaseModel()
        b_json = b.to_dict()
        b1 = BaseModel(**b_json)
        self.assertEqual(b.to_dict(), b1.to_dict())


if __name__ == "__main__":
    unittest.main()
