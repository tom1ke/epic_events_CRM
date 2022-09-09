from rest_framework.viewsets import ModelViewSet

from .models import Status
from .serializers import StatusSerializer
from .permissions import StatusAccessPermission


class StatusViewSet(ModelViewSet):
    
    serializer_class = StatusSerializer
    permission_classes = [StatusAccessPermission]
    
    def get_queryset(self):
        return Status.objects.all()
