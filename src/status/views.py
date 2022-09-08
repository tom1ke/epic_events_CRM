from rest_framework.viewsets import ModelViewSet

from .models import Status
from .serializers import StatusSerializer


class StatusViewSet(ModelViewSet):
    
    serializer_class = StatusSerializer
    
    def get_queryset(self):
        return Status.objects.all()
