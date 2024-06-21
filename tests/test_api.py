import unittest
from flask import Flask
from api.v1.app import app
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class StatusEndpointTestCase(unittest.TestCase):
    """Test case for the /status route."""

    @classmethod
    def setUpClass(cls):
        """Set up the Flask test client."""
        app.testing = True
        cls.client = app.test_client()

    def test_status_endpoint(self):
        """Test the /status endpoint."""
        response = self.client.get('/api/v1/status')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'status': 'OK'})

    def test_stats_endpoint_(self):
        """Test the /stats endpoint."""
        response = self.client.get('/api/v1/stats')
        amenities = storage.count(Amenity)
        cities = storage.count(City)
        places = storage.count(Place)
        reviews = storage.count(Review)
        states = storage.count(State)
        users = storage.count(User)
        stats = {
            "amenities": amenities,
            "cities": cities,
            "places": places,
            "reviews": reviews,
            "states": states,
            "users": users
        }
        self.assertDictEqual(response.json, stats)
