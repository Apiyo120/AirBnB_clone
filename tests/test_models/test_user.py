#!/usr/bin/python3
"""Unittest module for the User Class."""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for the User class."""

    def setUp(self):
        """Set up a User instance for testing."""
        self.user = User()

    def tearDown(self):
        """Tear down test methods."""
        del self.user

    def test_attributes_existence(self):
        """Test if attributes exist in the User instance."""
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))

    def test_attributes_defaults(self):
        """Test if attributes have default values in the User instance."""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")


if __name__ == '__main__':
    unittest.main()
