from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Event
from .serializers import EventSerializer
from .permissions import EventAccessPermission


class EventViewSet(ModelViewSet):
    
    serializer_class = EventSerializer
    permission_classes = [EventAccessPermission]
    
    def create(self, request, *args, **kwargs):
        event_data = request.data
        
        new_event = Event.objects.create(
            client_id = event_data['client'],
            contract_id = event_data['contract'],
            attendees = event_data['attendees'],
            event_date = event_data['event_date'],
            notes = event_data['notes'],
            support_contact = self.request.user,
            status_id = 1
        )
        
        new_event.save()
        
        serializer = EventSerializer(new_event)
        
        return Response(serializer.data)
    
    def get_queryset(self):
        if 'staff_pk' in self.kwargs:
            return Event.objects.filter(support_contact=self.kwargs['staff_pk'])
        
        if 'contracts_pk' in self.kwargs:
            return Event.objects.filter(contract=self.kwargs['contracts_pk'])
        
        else:
            return Event.objects.all()
