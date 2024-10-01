# tracking/views.py
from django.utils.dateparse import parse_datetime

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import TrackingNumber
from .serializers import TrackingNumberSerializer
from .utils import generate_unique_tracking_number


class NextTrackingNumberView(APIView):
    """
    Next tracking number view
    """
    def get(self, request):
        """
        Get method to generate the next tracking number
        """
        origin_country_id = request.query_params.get('origin_country_id')
        destination_country_id = request.query_params.get('destination_country_id')
        weight = request.query_params.get('weight')
        created_at = request.query_params.get('created_at')
        customer_id = request.query_params.get('customer_id')
        customer_name = request.query_params.get('customer_name')
        customer_slug = request.query_params.get('customer_slug')

        # Validate all required parameters
        if not all([origin_country_id, destination_country_id, weight, created_at, customer_id, customer_name, customer_slug]):
            return Response({"error": "All parameters are required"}, status=status.HTTP_400_BAD_REQUEST)

        # Parse weight and timestamp
        try:
            weight = float(weight)
            created_at = parse_datetime(created_at)
        except ValueError:
            return Response({"error": "Invalid weight or timestamp format"}, status=status.HTTP_400_BAD_REQUEST)

        # Generate the tracking number
        tracking_number = generate_unique_tracking_number()

        # Create a new tracking number object
        tracking_obj = TrackingNumber.objects.create(
            tracking_number=tracking_number,
            origin_country_id=origin_country_id,
            destination_country_id=destination_country_id,
            weight=weight,
            created_at=created_at,
            customer_id=customer_id,
            customer_name=customer_name,
            customer_slug=customer_slug
        )

        serializer = TrackingNumberSerializer(tracking_obj)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
