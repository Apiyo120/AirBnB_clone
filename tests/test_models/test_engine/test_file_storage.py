#!/usr/bin/python3
"""Unittest module for the FileStorage class."""

import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import json
import os


class TestFileStorage(unittest.TestCase):
    """Test Cases for the FileStorage class."""

    def setUp(self):
        """Sets up test methods."""
        self.storage = FileStorage()

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()

    def resetStorage(self):
        """Resets the storage instances."""
        storage._FileStorage__objects = {}

    def test_file_path(self):
        """Test if __file_path exists."""
        self.assertTrue(hasattr(self.storage, "_FileStorage__file_path"))

    def test_objects(self):
        """Test if __objects exists."""
        self.assertTrue(hasattr(self.storage, "_FileStorage__objects"))

    def test_all(self):
        """Test the all() method."""
        obj_dict = self.storage.all()
        self.assertIsInstance(obj_dict, dict)
        self.assertIs(obj_dict, self.storage._FileStorage__objects)

    def test_new(self):
        """Test the new() method."""
        new_model = BaseModel()
        key = "{}.{}".format(type(new_model).__name__, new_model.id)
        self.assertNotIn(key, self.storage.all())
        self.storage.new(new_model)
        self.assertIn(key, self.storage.all())
        self.assertIs(self.storage.all()[key], new_model)

    def test_save_reload(self):
        """Test the save and reload methods."""
        new_model = BaseModel()
        key = "{}.{}".format(type(new_model).__name__, new_model.id)
        self.storage.new(new_model)
        self.storage.save()
        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path))
        with open(self.storage._FileStorage__file_path, "r") as f:
            saved_dict = json.load(f)
        self.assertIn(key, saved_dict)
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        self.assertIn(key, self.storage.all())


if __name__ == "__main__":
    unittest.main()
