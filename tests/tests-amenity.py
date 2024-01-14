#!/usr/bin/python3
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def setUp(self):
        self.amenity = Amenity()

    def test_id_is_string(self):
        self.assertIsInstance(self.amenity.id, str)

    def test_name_is_string(self):
        self.assertIsInstance(self.amenity.name, str)

    def test_id_is_unique(self):
        other_amenity = Amenity()
        self.assertNotEqual(self.amenity.id, other_amenity.id)


if __name__ == '__main__':
    unittest.main()
