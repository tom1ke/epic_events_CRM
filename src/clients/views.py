from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Client
from .serializers import ClientSerializer
from .permissions import ClientAccessPermission


class ClientViewSet(ModelViewSet):
    
    serializer_class = ClientSerializer
    permission_classes = [ClientAccessPermission]
    
    def get_queryset(self):
        return Client.objects.all()
    
    def create(self, request, *args, **kwargs):
        client_data = request.data
        
        new_client = Client.objects.create(
            email = client_data['email'],
            first_name = client_data['first_name'],
            last_name = client_data['last_name'],
            phone = client_data['phone'],
            mobile = client_data['mobile'],
            company_name = client_data['company_name'],
            sales_contact = self.request.user
        )
            
        
        new_client.save()
        
        serializer = ClientSerializer(new_client)
        
        return Response(serializer.data)
