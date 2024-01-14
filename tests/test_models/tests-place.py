#!/usr/bin/python3
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    def setUp(self):
        self.place = Place()

    def test_id_is_string(self):
        self.assertIsInstance(self.place.id, str)

    def test_city_id_is_string(self):
        self.assertIsInstance(self.place.city_id, str)

    def test_user_id_is_string(self):
        self.assertIsInstance(self.place.user_id, str)

    def test_name_is_string(self):
        self.assertIsInstance(self.place.name, str)

    def test_description_is_string(self):
        self.assertIsInstance(self.place.description, str)

    def test_number_rooms_is_int(self):
        self.assertIsInstance(self.place.number_rooms, int)

    def test_number_bathrooms_is_int(self):
        self.assertIsInstance(self.place.number_bathrooms, int)

    def test_max_guest_is_int(self):
        self.assertIsInstance(self.place.max_guest, int)

    def test_price_by_night_is_int(self):
        self.assertIsInstance(self.place.price_by_night, int)

    def test_latitude_is_float(self):
        self.assertIsInstance(self.place.latitude, float)

    def test_longitude_is_float(self):
        self.assertIsInstance(self.place.longitude, float)

    def test_amenity_ids_is_list(self):
        self.assertIsInstance(self.place.amenity_ids, list)

    def test_amenity_ids_contains_strings(self):
        for amenity_id in self.place.amenity_ids:
            self.assertIsInstance(amenity_id, str)

    def test_id_is_unique(self):
        other_place = Place()
        self.assertNotEqual(self.place.id, other_place.id)


if __name__ == '__main__':
    unittest.main()
