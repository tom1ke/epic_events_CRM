from rest_framework.permissions import BasePermission, SAFE_METHODS


class EventAccessPermission(BasePermission):
    message = 'You are not assigned to this event'
    
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        return True if request.method in SAFE_METHODS else obj.support_contact == request.user
