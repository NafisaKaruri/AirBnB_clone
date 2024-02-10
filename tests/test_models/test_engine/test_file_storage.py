#!/usr/bin/python3
"""Test File Storage module"""

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import unittest


class TestFileStorage(unittest.TestCase):
    """Test the file storage class"""
    def setUp(self):
        """Instantiation"""
        self.fs = FileStorage()
        self.bm = BaseModel()

    def tearDown(self):
        """Clear everything each test case"""
        pass

    def test_isinstance(self):
        """Test if fs is a an instance of FileStorage"""
        self.assertEqual("<class 'models.engine.file_storage.FileStorage'>",
                         str(type(self.fs)))

    def test_file_path(self):
        """Tests if the file_path is indeed file.json"""
        self.assertEqual(self.fs._FileStorage__file_path, "file.json")

    def test_objectsType(self):
        """Tests if the __objects is a dictionary"""
        self.assertIsInstance(self.fs._FileStorage__objects, dict)

    def test_all(self):
        """Tests if the all method returns the __objects dictionary"""
        self.assertEqual(self.fs._FileStorage__objects, self.fs.all())

    def test_new(self):
        """Tests if the new method sets an obj in __objects"""
        self.fs.new(self.bm)
        key = self.bm.__class__.__name__ + "." + self.bm.id
        self.assertEqual(self.fs.all()[key], self.bm)


if __name__ == "__main__":
    unittest.main()
