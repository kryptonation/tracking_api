# tracking/utils.py
import random
import string
from .models import TrackingNumber

def generate_unique_tracking_number():
    """
    Function to generate a unique tracking number
    """
    while True:
        tracking_number = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
        if not TrackingNumber.objects.filter(tracking_number=tracking_number).exists():
            return tracking_number
