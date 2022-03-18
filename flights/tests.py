from http import client
import unittest

from django.test import TestCase, Client

from flights.models import Planet

class PlanetListViewTest(TestCase):
    def setUp(self):
        client = Client()

        Planet.objects.create(
            id   = 1,
            name = "지구",
            code = "ERH"
        )

        Planet.objects.create(
            id   = 2,
            name = "달",
            code = "MON"
        )

        Planet.objects.create(
            id   = 3,
            name = "수성",
            code = "MCR"
        )
        
    def test_success_view_get_planet_list(self):
        client = Client()
        response = client.get('/flights/planet')

        self.assertEqual(response.json(),{
            "planet_list": [
                {
                    "planet_id" : 1,
                    "planet_name" : "지구",
                    "planet_code" : "ERH"
                }, 
                {
                    "planet_id": 2,
                    "planet_name": "달",
                    "planet_code": "MON"
                },
                {
                    "planet_id": 3,
                    "planet_name": "수성",
                    "planet_code": "MCR"
                }
            ]
        })