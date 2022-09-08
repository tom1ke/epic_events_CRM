from django.urls import path, include
from rest_framework_nested import routers

from .views import EventViewSet, AllEventsViewSet
from clients.urls import clients


all_events = routers.SimpleRouter()
all_events.register(r'events', AllEventsViewSet, basename='all-events')

client_events = routers.NestedSimpleRouter(clients, r'clients', lookup='clients')
client_events.register(r'events', EventViewSet, basename='client-events')


urlpatterns = [
    path(r'', include(all_events.urls)),
    path(r'', include(client_events.urls)),
]