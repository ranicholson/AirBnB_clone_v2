#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):

    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ """
        new = self.value(city_id="123")
        self.assertEqual(type(new.city_id), str)
        self.assertEqual(new.city_id, "123")

    def test_user_id(self):
        """ """
        new = self.value(user_id="321")
        self.assertEqual(type(new.user_id), str)
        self.assertEqual(new.user_id, "321")

    def test_name(self):
        """ """
        new = self.value(name="Aloha")
        self.assertEqual(type(new.name), str)
        self.assertEqual(new.name, "Aloha")

    def test_description(self):
        """ """
        new = self.value(description="Yeah it's nice")
        self.assertEqual(type(new.description), str)
        self.assertEqual(new.description, "Yeah it's nice")

    def test_number_rooms(self):
        """ """
        new = self.value(number_rooms=5)
        self.assertEqual(type(new.number_rooms), int)
        self.assertEqual(new.number_rooms, 5)

    def test_number_bathrooms(self):
        """ """
        new = self.value(number_bathrooms=2)
        self.assertEqual(type(new.number_bathrooms), int)
        self.assertEqual(new.number_bathrooms, 2)

    def test_max_guest(self):
        """ """
        new = self.value(max_guest=7)
        self.assertEqual(type(new.max_guest), int)
        self.assertEqual(new.max_guest, 7)

    def test_price_by_night(self):
        """ """
        new = self.value(price_by_night=50)
        self.assertEqual(type(new.price_by_night), int)
        self.assertEqual(new.price_by_night, 50)

    def test_latitude(self):
        """ """
        new = self.value(latitude=3.50)
        self.assertEqual(type(new.latitude), float)
        self.assertEqual(new.latitude, 3.50)

    def test_longitude(self):
        """ """
        new = self.value(longitude=4.50)
        self.assertEqual(type(new.longitude), float)
        self.assertEqual(new.longitude, 4.50)
