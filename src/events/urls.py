from cgitb import lookup
from django.urls import path, include
from rest_framework_nested import routers

from .views import EventViewSet
from contracts.urls import contracts, client_contracts, user_client_contracts


events = routers.SimpleRouter()
events.register(r'events', EventViewSet, basename='events')

contract_events = routers.NestedSimpleRouter(contracts, r'contracts', lookup='contracts')
contract_events.register(r'events', EventViewSet, basename='contract_events')

client_contract_events = routers.NestedSimpleRouter(client_contracts, r'contracts', lookup='contracts')
client_contract_events.register(r'events', EventViewSet, basename='client_contract_events')

user_client_contract_events = routers.NestedSimpleRouter(user_client_contracts, r'contracts', lookup='contracts')
user_client_contract_events.register(r'events', EventViewSet, basename='user_client_contract_events')


urlpatterns = [
    path(r'', include(events.urls)),
    path(r'', include(contract_events.urls)),
    path(r'', include(client_contract_events.urls)),
    path(r'', include(user_client_contract_events.urls)),
]