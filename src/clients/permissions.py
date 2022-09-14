from rest_framework.permissions import BasePermission, SAFE_METHODS


class ClientAccessPermission(BasePermission):
    
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        
        if request.user.role == 2:
            return True
        
        if request.user.is_superuser:
            return True
    
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        
        if obj.sales_contact == request.user:
            return True
        
        if request.user.is_superuser:
            return True
