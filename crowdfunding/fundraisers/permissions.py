from rest_framework import permissions 
from rest_framework.exceptions import NotAuthenticated, PermissionDenied

class IsOwnerOrReadOnly(permissions.BasePermission):
    message = 'You need to be owner of this fundraiser in order to perform this action.'
    def has_object_permission(self,request,view,obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
    
class IsSupporterOrReadOnly(permissions.BasePermission):
    message = 'You need to be supporter of this pledge in order to perform this action.'
    def has_object_permission(self,request,view,obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.supporter == request.user
    
class CustomIsAuthenticatedOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    def has_permission(self, request, view):
        # Allow safe methods (GET, HEAD, OPTIONS) for everyone
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # If user is not authenticated, raise custom error
        if not request.user or not request.user.is_authenticated:
            raise NotAuthenticated(detail="You must be logged in to create a pledge or fundraiser.")
        
        return True