#!/usr/bin/python3
"""Unittest module for the BaseModel Class."""

from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
import json
import os
import re
import time
import unittest
import uuid


class TestBaseModel(unittest.TestCase):

    """Test Cases for the BaseModel class."""

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resets the storage instances."""
        storage._FileStorage__objects = {}

    def test_save(self):
        """Tests the save method."""
        self.model.save()
        key = "{}.{}".format(type(self.model).__name__, self.model.id)
        self.assertIn(key, storage.all())
        self.assertIn(self.model, storage.all().values())

    def test_to_dict(self):
        """Tests the to_dict method."""
        self.assertEqual(type(self.model.to_dict()), dict)
        self.assertTrue("to_dict" in dir(self.model))
        self.assertTrue('__class__' in self.model.to_dict())
        self.assertEqual(self.model.to_dict()['__class__'], 'BaseModel')
        self.assertTrue('id' in self.model.to_dict())
        self.assertTrue('created_at' in self.model.to_dict())
        self.assertTrue('updated_at' in self.model.to_dict())
        self.assertEqual(type(self.model.to_dict()['created_at']), str)
        self.assertEqual(type(self.model.to_dict()['updated_at']), str)

    def test_id_type(self):
        """Tests the type of the id attribute."""
        self.assertEqual(type(self.model.id), str)

    def test_created_at_type(self):
        """Tests the type of the created_at attribute."""
        self.assertEqual(type(self.model.created_at), datetime)

    def test_updated_at_type(self):
        """Tests the type of the updated_at attribute."""
        self.assertEqual(type(self.model.updated_at), datetime)

    def test_str_representation(self):
        """Tests the __str__ representation of BaseModel."""
        expected = "[{}] ({}) {}".format(
                type(self.model).__name__, self.model.id, self.model.__dict__)
        self.assertEqual(expected, str(self.model))


if __name__ == "__main__":
    unittest.main()
