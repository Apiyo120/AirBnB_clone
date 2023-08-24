#!/usr/bin/python3
"""Unittest module for the State Class."""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for the State class."""

    def setUp(self):
        """Set up a State instance for testing."""
        self.state = State()

    def test_attributes_existence(self):
        """Test if attributes exist in the State instance."""
        self.assertTrue(hasattr(self.state, 'name'))

    def test_attributes_defaults(self):
        """Test if attributes have default values in the State instance."""
        self.assertEqual(self.state.name, "")


if __name__ == '__main__':
    unittest.main()
