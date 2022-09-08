from cgitb import lookup
from django.urls import path, include
from rest_framework_nested import routers

from .views import StatusViewSet
from contracts.urls import all_contracts, client_contracts
from events.urls import all_events, client_events


all_contracts_status = routers.NestedSimpleRouter(all_contracts, r'contracts', lookup='contracts')
all_contracts_status.register(r'status', StatusViewSet, basename='all-contracts-status')

client_contracts_status = routers.NestedSimpleRouter(client_contracts, r'contracts', lookup='contracts')
client_contracts_status.register(r'status', StatusViewSet, basename='client-contracts-status')

all_events_status = routers.NestedSimpleRouter(all_events, r'events', lookup='events')
all_events_status.register(r'status', StatusViewSet, basename='all-events-status')

client_events_status = routers.NestedSimpleRouter(client_events, r'events', lookup='events')
client_events_status.register(r'status', StatusViewSet, basename='client-events-status')


urlpatterns = [
    path(r'', include(all_contracts_status.urls)),
    path(r'', include(client_contracts_status.urls)),
    path(r'', include(all_events_status.urls)),
    path(r'', include(client_events_status.urls)),
]