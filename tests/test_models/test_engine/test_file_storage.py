#!/usr/bin/python3
"""Test File Storage module"""

import models
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

    def test_save(self):
        """Test if the save method serializes __objects to the json file"""
        models.storage.new(self.bm)
        models.storage.save()
        saved = ""
        with open("file.json", "r") as jsonf:
            saved = jsonf.read()
            self.assertIn(f"BaseModel.{self.bm.id}", saved)

    def test_reload(self):
        """Test if the reload method deserializes the json to __objects"""
        models.storage.new(self.bm)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn(f"BaseModel.{self.bm.id}", objs)


if __name__ == "__main__":
    unittest.main()
