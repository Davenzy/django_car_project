from rest_framework import permissions
    
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return bool(request.method in permissions.SAFE_METHODS and obj.owner_id.id == request.user and request.user.is_authenticated)