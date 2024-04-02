from REST_Framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True 
        
        return bool(request.user and request.user.is_staff)
    
class IsOwnerOrRealOnly(permissions.BasePermission):
    def has_object_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        rerurn object.user == request.user