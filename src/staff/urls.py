from django.urls import path, include
from rest_framework_nested import routers

from .views import UserViewSet


staff = routers.SimpleRouter()
staff.register(r'staff', UserViewSet, basename='staff')


urlpatterns = [
    path(r'', include(staff.urls))
]
