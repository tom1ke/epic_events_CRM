from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Contract
from .serializers import ContractSerializer
from .permissions import ContractAccessPermission


class CreateContractMixin:
    
    def create(self, request, *args, **kwargs):
        contract_data = request.data
        
        new_contract = Contract.objects.create(
            client_id = contract_data['client'],
            amount = contract_data['amount'],
            payment_due = contract_data['payment_due'],
            sales_contact = self.request.user
        )
        
        new_contract.save()
        
        serializer = ContractSerializer(new_contract)
        
        return Response(serializer.data)


class AllContractsViewSet(CreateContractMixin, ModelViewSet):
    
    serializer_class = ContractSerializer
    permission_classes = [ContractAccessPermission]
    
    def get_queryset(self):
        return Contract.objects.all()


class ContractViewSet(CreateContractMixin, ModelViewSet):
    
    serializer_class = ContractSerializer
    permission_classes = [ContractAccessPermission]
    
    def get_queryset(self):
        return Contract.objects.filter(client=self.kwargs['clients_pk'])
