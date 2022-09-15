from django.urls import path, include
from rest_framework_nested import routers

from .views import ClientViewSet
from staff.urls import staff

clients = routers.SimpleRouter()
clients.register(r'clients', ClientViewSet, basename='clients')

user_clients = routers.NestedSimpleRouter(staff, r'staff', lookup='staff')
user_clients.register(r'clients', ClientViewSet, basename='user_clients')


urlpatterns = [
    path(r'', include(clients.urls)),
    path(r'', include(user_clients.urls))
]
