from cgitb import lookup
from django.urls import path, include
from rest_framework_nested import routers

from .views import StatusViewSet


status = routers.SimpleRouter()
status.register(r'status', StatusViewSet, basename='status')


urlpatterns = [
    path(r'', include(status.urls))
]