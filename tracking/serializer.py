# tracking/serializers.py
from rest_framework import serializers

from .models import TrackingNumber

class TrackingNumberSerializer(serializers.ModelSerializer):
    """
    Tracking number serializer
    """
    class Meta:
        """
        Class meta options
        """
        model = TrackingNumber
        fields = ['tracking_number', 'created_at', 'customer_id', 'customer_name', 'customer_slug', 
                  'origin_country_id', 'destination_country_id', 'weight']
