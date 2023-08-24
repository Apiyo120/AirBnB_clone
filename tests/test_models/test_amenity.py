#!/usr/bin/python3
"""Unittest module for the Amenity Class."""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class."""

    def setUp(self):
        """Set up an Amenity instance for testing."""
        self.amenity = Amenity()

    def test_attributes_existence(self):
        """Test if attributes exist in the Amenity instance."""
        self.assertTrue(hasattr(self.amenity, 'name'))

    def test_attributes_defaults(self):
        """Test if attributes have default values in the Amenity instance."""
        self.assertEqual(self.amenity.name, "")


if __name__ == '__main__':
    unittest.main()
