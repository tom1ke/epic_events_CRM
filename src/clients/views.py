from rest_framework.viewsets import ModelViewSet

from .models import Client
from .serializers import ClientSerializer


class ClientViewSet(ModelViewSet):
    
    serializer_class = ClientSerializer
    
    def get_queryset(self):
        return Client.objects.all()
    