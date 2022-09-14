from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Event
from .serializers import EventSerializer
from .permissions import EventAccessPermission


class CreateEventMixin:
    
    def create(self, request, *args, **kwargs):
        event_data = request.data
        
        new_event = Event.objects.create(
            client_id = event_data['client'],
            attendees = event_data['attendees'],
            event_date = event_data['event_date'],
            notes = event_data['notes'],
            support_contact = self.request.user,
            status_id = 1
        )
        
        new_event.save()
        
        serializer = EventSerializer(new_event)
        
        return Response(serializer.data)


class AllEventsViewSet(CreateEventMixin, ModelViewSet):
    
    serializer_class = EventSerializer
    permission_classes = [EventAccessPermission]
    
    def get_queryset(self):
        return Event.objects.all()


class EventViewSet(CreateEventMixin, ModelViewSet):
    
    serializer_class = EventSerializer
    permission_classes = [EventAccessPermission]
    
    def get_queryset(self):
        return Event.objects.filter(client=self.kwargs['clients_pk'])
