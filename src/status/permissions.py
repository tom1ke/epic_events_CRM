from rest_framework.permissions import BasePermission


class StatusAccessPermission(BasePermission):
    message = 'You are not allowed to perform this action'
    
    def has_permission(self, request, view):
        return request.user.is_superuser
