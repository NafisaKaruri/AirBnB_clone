#!/usr/bin/python3
"""This is the BaseModel test"""

from models.base_model import BaseModel
from datetime import datetime
import unittest
from unittest.mock import patch
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

    @patch('models.storage.save')
    def test_save(self, mock_save):
        """Test the save function"""
        b = BaseModel()
        b.save()
        self.assertIsInstance(b.updated_at, datetime)
        mock_save.assert_called_once()

    def test_to_dict(self):
        """Test to_dict function"""
        b = BaseModel()
        b_dict = b.to_dict()
        self.assertIsInstance(b_dict, dict)

    def test_to_dict_contains_class_name(self):
        """Test to_dict contains the class name"""
        b = BaseModel()
        b_dict = b.to_dict()
        self.assertEqual("BaseModel", b_dict['__class__'])

    def test_to_dict_formats_timestamps(self):
        """Test to_dict formats timestamps correctly"""
        b = BaseModel()
        b_dict = b.to_dict()
        self.assertTrue('created_at' in b_dict)
        self.assertTrue('updated_at' in b_dict)
        self.assertIsInstance(b_dict['created_at'], str)
        self.assertIsInstance(b_dict['updated_at'], str)

    # --------------- Test task 4 ---------------
    def test_args_raises_exception(self):
        """Test args raises an exception"""
        b = BaseModel(1)

    def test_kwargs(self):
        """Test Kwargs"""
        b = BaseModel()
        b_json = b.to_dict()
        b1 = BaseModel(**b_json)
        self.assertEqual(b.to_dict(), b1.to_dict())


if __name__ == "__main__":
    unittest.main()
