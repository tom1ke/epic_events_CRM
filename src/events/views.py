from rest_framework.viewsets import ModelViewSet

from .models import Event
from .serializers import EventSerializer
from .permissions import EventAccessPermission


class AllEventsViewSet(ModelViewSet):
    
    serializer_class = EventSerializer
    permission_classes = [EventAccessPermission]
    
    def get_queryset(self):
        return Event.objects.all()


class EventViewSet(ModelViewSet):
    
    serializer_class = EventSerializer
    permission_classes = [EventAccessPermission]
    
    def get_queryset(self):
        return Event.objects.filter(client=self.kwargs['clients_pk'])
