#!/usr/bin/python3
"""Unittest module for the Review Class."""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for the Review class."""

    def setUp(self):
        """Set up a Review instance for testing."""
        self.review = Review()

    def test_attributes_existence(self):
        """Test if attributes exist in the Review instance."""
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertTrue(hasattr(self.review, 'text'))

    def test_attributes_defaults(self):
        """Test if attributes have default values in Review instance."""
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_attributes_assignment(self):
        """Test attribute assignment in the Review instance."""
        self.review.place_id = "place123"
        self.review.user_id = "user456"
        self.review.text = "This is a review."
        self.assertEqual(self.review.place_id, "place123")
        self.assertEqual(self.review.user_id, "user456")
        self.assertEqual(self.review.text, "This is a review.")

    def test_str_representation(self):
        """Test the string representation of the Review instance."""
        str_repr = str(self.review)
        expected_str = "[Review] ({}) {}".format(
            self.review.id, self.review.__dict__)
        self.assertEqual(str_repr, expected_str)


if __name__ == '__main__':
    unittest.main()
