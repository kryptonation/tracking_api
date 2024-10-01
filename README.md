
# Scalable Tracking Number Generator API

This project implements a scalable tracking number generator API using Django Rest Framework (DRF). It supports generating unique tracking numbers for parcels and is designed to handle high concurrency.

## Features
- Generates unique tracking numbers.
- Supports query parameters for origin, destination, weight, and customer details.
- Designed to handle concurrent requests efficiently.
- Scalable for horizontal scaling.
- Includes test cases for various edge cases.

## Requirements
- Python 3.x
- Django 4.x
- Django Rest Framework
- PostgreSQL
- Gunicorn (for deployment)

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-repository/tracking-api.git
cd tracking-api
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Setup Database
Configure PostgreSQL in `settings.py` using environment variables:
```python
import os
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(default=os.getenv('DATABASE_URL'))
}
```

### 4. Run Migrations
```bash
python manage.py migrate
```

### 5. Start the Development Server
```bash
python manage.py runserver
```

### 6. Run Test Cases
```bash
python manage.py test
```

## API Endpoints

### Generate Tracking Number
- **Endpoint**: `/api/next-tracking-number`
- **Method**: `GET`
- **Query Parameters**:
    - `origin_country_id` (string): ISO 3166-1 alpha-2 country code of the origin country (e.g., "US").
    - `destination_country_id` (string): ISO 3166-1 alpha-2 country code of the destination country (e.g., "CA").
    - `weight` (float): Weight of the parcel in kilograms (up to 3 decimal places).
    - `created_at` (string): RFC 3339 formatted timestamp (e.g., "2024-09-30T19:29:32+08:00").
    - `customer_id` (UUID): Customer's unique identifier (e.g., "de619854-b59b-425e-9db4-943979e1bd49").
    - `customer_name` (string): Name of the customer (e.g., "RedBox Logistics").
    - `customer_slug` (string): Slugified name of the customer (e.g., "redbox-logistics").

- **Response**:
```json
{
    "tracking_number": "ABC123456789",
    "created_at": "2024-09-30T19:29:32+08:00"
}
```

## Deployment

### 1. Install Gunicorn
```bash
pip install gunicorn
```

### 2. Create a `Procfile`
Create a `Procfile` in the root of your project with the following content:
```
web: gunicorn tracking_api.wsgi --log-file -
```

### 3. Deploy on Render
- Push your code to GitHub/GitLab.
- Create a new web service on [Render](https://render.com/).
- Set up the build and start commands.
- Run migrations using the shell:
```bash
python manage.py migrate
```

## Testing
This project includes a test suite that covers edge cases such as missing parameters, invalid weights, and timestamp formats.

### Example Tests
```python
# tracking/tests.py
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

class TrackingNumberAPITest(TestCase):
    def setUp(self):
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
        response = self.client.get(reverse('next-tracking-number'), self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('tracking_number' in response.data)
    
    def test_missing_parameters(self):
        invalid_payload = self.valid_payload.copy()
        del invalid_payload['origin_country_id']
        response = self.client.get(reverse('next-tracking-number'), invalid_payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], "All parameters are required")
    
    def test_invalid_weight(self):
        invalid_payload = self.valid_payload.copy()
        invalid_payload['weight'] = 'invalid_weight'
        response = self.client.get(reverse('next-tracking-number'), invalid_payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
```

### Author
- Your Name
- Your Email
- GitHub Profile
