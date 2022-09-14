from rest_framework.permissions import BasePermission, SAFE_METHODS


class ClientAccessPermission(BasePermission):
    
    def has_permission(self, request, view):
        return True if request.method in SAFE_METHODS else request.user.role == 2
    
    def has_object_permission(self, request, view, obj):
        return True if request.method in SAFE_METHODS else obj.sales_contact == request.user
