from rest_framework.permissions import BasePermission, SAFE_METHODS


class UserAccessPermission(BasePermission):
    
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        return True if request.method in SAFE_METHODS else request.user.is_superuser
