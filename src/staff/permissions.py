from rest_framework.permissions import BasePermission, SAFE_METHODS


class UserAccessPermission(BasePermission):
    
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        if request.user.is_superuser:
            return True
    
    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser