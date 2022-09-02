from rest_framework.serializers import ModelSerializer

from .models import Contract


class ContractSerializer(ModelSerializer):
    
    class Meta:
        model = Contract
        fields = [
            'client',
            'sales_contact',
            'status',
            'amount',
            'payment_due',
            'date_created',
            'date_updated'
        ]