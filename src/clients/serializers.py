from rest_framework.serializers import ModelSerializer

from .models import Client


class ClientSerializer(ModelSerializer):
    
    class Meta:
        model = Client
        fields = [
            'email',
            'first_name',
            'last_name',
            'sales_contact',
            'phone',
            'mobile',
            'company_name',
            'date_created',
            'date_updated'
        ]
