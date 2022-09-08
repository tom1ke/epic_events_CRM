from django.urls import path, include
from rest_framework_nested import routers

from .views import ContractViewSet, AllContractsViewSet
from clients.urls import clients

all_contracts = routers.SimpleRouter()
all_contracts.register(r'contracts', AllContractsViewSet, basename='all-contracts')

client_contracts = routers.NestedSimpleRouter(clients, r'clients', lookup='clients')
client_contracts.register(r'contracts', ContractViewSet, basename='client-contracts')


urlpatterns = [
    path(r'', include(all_contracts.urls)),
    path(r'', include(client_contracts.urls)),
]