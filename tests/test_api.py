import unittest
from flask import Flask
from api.v1.app import app


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
