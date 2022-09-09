from rest_framework.permissions import BasePermission, SAFE_METHODS


class ContractAccessPermission(BasePermission):
    message = 'You are not assigned to this contract'
    
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        return True if request.method in SAFE_METHODS else obj.sales_contact == request.user
