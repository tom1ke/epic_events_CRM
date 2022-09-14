from rest_framework.viewsets import ModelViewSet

from .models import User
from .serializers import UserSerializer
from .permissions import UserAccessPermission


class UserViewSet(ModelViewSet):
    
    serializer_class = UserSerializer
    permission_classes = [UserAccessPermission]
    
    def get_queryset(self):
        return User.objects.all()
