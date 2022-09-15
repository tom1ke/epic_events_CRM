from rest_framework.serializers import ModelSerializer

from .models import Event


class EventSerializer(ModelSerializer):
    
    class Meta:
        model = Event
        fields = [
            'client',
            'support_contact',
            'contract',
            'status',
            'attendees',
            'event_date',
            'notes',
            'date_created',
            'date_updated'
        ]
