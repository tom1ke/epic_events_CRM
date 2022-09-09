from rest_framework.viewsets import ModelViewSet

from .models import Client
from .serializers import ClientSerializer
from .permissions import ClientAccessPermission


class ClientViewSet(ModelViewSet):
    
    serializer_class = ClientSerializer
    permission_classes = [ClientAccessPermission]
    
    def get_queryset(self):
        return Client.objects.all()
    