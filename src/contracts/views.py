from http import client
from rest_framework.viewsets import ModelViewSet

from .models import Contract
from .serializers import ContractSerializer


class AllContractsViewSet(ModelViewSet):
    
    serializer_class = ContractSerializer
    
    def get_queryset(self):
        return Contract.objects.all()


class ContractViewSet(ModelViewSet):
    
    serializer_class = ContractSerializer
    
    def get_queryset(self):
        return Contract.objects.filter(client=self.kwargs['clients_pk'])
