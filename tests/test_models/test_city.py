#!/usr/bin/python3
"""Unittest module for the City Class."""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for the City class."""

    def setUp(self):
        """Set up a City instance for testing."""
        self.city = City()

    def test_attributes_existence(self):
        """Test if attributes exist in the City instance."""
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertTrue(hasattr(self.city, 'name'))

    def test_attributes_defaults(self):
        """Test if attributes have default values in the City instance."""
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    if __name__ == '__main__':
        unittest.main()
