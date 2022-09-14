from rest_framework.permissions import BasePermission, SAFE_METHODS


class EventAccessPermission(BasePermission):
    
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        
        if request.user.role == 2:
            return True
        
        if request.method != 'POST' and request.user.role == 3:
            return True
        
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        
        if obj.support_contact == request.user:
            return True
        
        if obj.client.sales_contact == request.user:
            return True
