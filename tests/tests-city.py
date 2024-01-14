#!/usr/bin/python3
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    def setUp(self):
        self.city = City()

    def test_id_is_string(self):
        self.assertIsInstance(self.city.id, str)

    def test_state_id_is_string(self):
        self.assertIsInstance(self.city.state_id, str)

    def test_name_is_string(self):
        self.assertIsInstance(self.city.name, str)

    def test_id_is_unique(self):
        other_city = City()
        self.assertNotEqual(self.city.id, other_city.id)


if __name__ == '__main__':
    unittest.main()
