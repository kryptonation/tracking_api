# tracking/tests.py
from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework import status

from django.urls import reverse
from .models import TrackingNumber

class TrackingNumberAPITest(TestCase):
    """
    Test tracking number API
    """
    def setUp(self):
        """
        Initialize the test case
        """
        self.client = APIClient()
        self.valid_payload = {
            'origin_country_id': 'US',
            'destination_country_id': 'CA',
            'weight': '1.234',
            'created_at': '2024-09-30T19:29:32+08:00',
            'customer_id': 'de619854-b59b-425e-9db4-943979e1bd49',
            'customer_name': 'RedBox Logistics',
            'customer_slug': 'redbox-logistics'
        }

    def test_create_tracking_number(self):
        """
        Test creating a new tracking number
        """
        response = self.client.get(reverse('next-tracking-number'), self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('tracking_number' in response.data)
    
    def test_missing_parameters(self):
        """
        Test missing parameters
        """
        invalid_payload = self.valid_payload.copy()
        del invalid_payload['origin_country_id']
        response = self.client.get(reverse('next-tracking-number'), invalid_payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], "All parameters are required")
    
    def test_invalid_weight(self):
        """
        Test invalid weight
        """
        invalid_payload = self.valid_payload.copy()
        invalid_payload['weight'] = 'invalid_weight'
        response = self.client.get(reverse('next-tracking-number'), invalid_payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
