from rest_framework import permissions 

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
    message = "You must be logged in to create a pledge."