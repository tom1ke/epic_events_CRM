from rest_framework.permissions import BasePermission, SAFE_METHODS


class UserAccessPermission(BasePermission):
    
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        if request.user.role == 1:
            return True
