#!/usr/bin/python3
"""Test place module"""

from models.base_model import BaseModel
from models.place import Place
import unittest


class TestPlace(unittest.TestCase):
    """Test the Place"""
    def setUp(self):
        """Instantiation"""
        self.p = Place()

    def tearDown(self):
        """Clear everything each test case"""
        pass

    def test_inheritance(self):
        """Test if Place is a subclass of BaseModel"""
        self.assertTrue(issubclass(Place, BaseModel))

    def test_isinstance(self):
        """Test if p instance is indeed an instance of Place"""
        self.assertEqual("<class 'models.place.Place'>", str(type(self.p)))

    def test_city_id(self):
        """Test if city_id is intialize with an empty string"""
        self.assertEqual(self.p.city_id, "")

    def test_user_id(self):
        """Test if user_id is intialize with an empty string"""
        self.assertEqual(self.p.user_id, "")

    def test_name(self):
        """Test if name is intialize with an empty string"""
        self.assertEqual(self.p.name, "")

    def test_description(self):
        """Test if description is intialize with an empty string"""
        self.assertEqual(self.p.description, "")

    def test_number_roomsType(self):
        """Tests if the number of rooms is an int"""
        self.assertIsInstance(self.p.number_rooms, int)

    def test_number_roomsVal(self):
        """Test if number_rooms is intialize with a value 0"""
        self.assertEqual(self.p.number_rooms, 0)

    def test_number_bathroomsType(self):
        """Tests if the number_bathrooms is an int"""
        self.assertIsInstance(self.p.number_bathrooms, int)

    def test_number_bathroomsVal(self):
        """Test if number_bathrooms is intialize with a value 0"""
        self.assertEqual(self.p.number_bathrooms, 0)

    def test_max_guestType(self):
        """Tests if max_guest is an integer"""
        self.assertIsInstance(self.p.max_guest, int)

    def test_max_guestVal(self):
        """Test if max_guest is initalized with a value of 0"""
        self.assertEqual(self.p.max_guest, 0)

    def test_price_by_nightType(self):
        """Tests if price_by_night is an int"""
        self.assertIsInstance(self.p.price_by_night, int)

    def test_price_by_nightVal(self):
        """Test if price_by_night is initialized with a value of 0"""
        self.assertEqual(self.p.price_by_night, 0)

    def test_latitudeType(self):
        """Test if latitude is of type float"""
        self.assertIsInstance(self.p.latitude, float)

    def test_latitudeVal(self):
        """Test if latitude is initialized to a value of 0.0"""
        self.assertEqual(self.p.latitude, 0.0)
    
    def test_longitudeType(self):
        """Test if longitude is of type float"""
        self.assertIsInstance(self.p.longitude, float)

    def test_longitudeVal(self):
        """Test if longitude is initialized with a value of 0.0"""
        self.assertEqual(self.p.longitude, 0.0)

    def test_amenity_id(self):
        """Test if amenity_id is an empty list"""
        self.assertEqual(self.p.amenity_ids, [])


if __name__ == "__main__":
    unittest.main()
