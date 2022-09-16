from cgitb import lookup
from django.urls import path, include
from rest_framework_nested import routers

from .views import ContractViewSet
from clients.urls import clients, user_clients
from staff.urls import staff

contracts = routers.SimpleRouter()
contracts.register(r'contracts', ContractViewSet, basename='contracts')

user_contracts = routers.NestedSimpleRouter(staff, r'staff', lookup='staff')
user_contracts.register(r'contracts', ContractViewSet, basename='user_contracts')

client_contracts = routers.NestedSimpleRouter(clients, r'clients', lookup='clients')
client_contracts.register(r'contracts', ContractViewSet, basename='client_contracts')

user_client_contracts = routers.NestedSimpleRouter(user_clients, r'clients', lookup='clients')
user_client_contracts.register(r'contracts', ContractViewSet, basename='user_client_contracts')


routers.NestedMixin
urlpatterns = [
    path(r'', include(contracts.urls)),
    path(r'', include(user_contracts.urls)),
    path(r'', include(client_contracts.urls)),
    path(r'', include(user_client_contracts.urls)),
]
