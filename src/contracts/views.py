from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Contract
from .serializers import ContractSerializer
from .permissions import ContractAccessPermission


class ContractViewSet(ModelViewSet):
    
    serializer_class = ContractSerializer
    permission_classes = [ContractAccessPermission]
    
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
    
    def get_queryset(self):        
        if 'staff_pk' in self.kwargs:
            return Contract.objects.filter(sales_contact=self.kwargs['staff_pk'])
        
        if 'clients_pk' in self.kwargs:
            return Contract.objects.filter(client=self.kwargs['clients_pk'])
        
        else:
            return Contract.objects.all()
