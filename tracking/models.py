# tracking/models.py
import uuid

from django.db import models

class TrackingNumber(models.Model):
    """
    Tracking number model
    """
    tracking_number = models.CharField(max_length=16, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    customer_id = models.UUIDField(default=uuid.uuid4, editable=False)
    customer_name = models.CharField(max_length=255)
    customer_slug = models.SlugField()
    origin_country_id = models.CharField(max_length=2)
    destination_country_id = models.CharField(max_length=2)
    weight = models.DecimalField(max_digits=6, decimal_places=3)
